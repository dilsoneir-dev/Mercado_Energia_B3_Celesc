"""Organiza os dados brutos do projeto para versionamento no GitHub.

Estrutura adotada (por fonte):
    data/CELESC/celesc_consumo_uc_1994_2026.csv.gz
    data/ANEEL/tarifas-homologadas-distribuidoras-energia-eletrica.csv.gz
    data/CCEE/pld_media_semanal_*.csv            (pequenos, ficam como estão)

O que o script faz:
  1. Localiza cada bruto original (.csv) e gera a versão comprimida (.csv.gz)
     na pasta da fonte. O .csv original NÃO é apagado nem movido; ele continua
     no disco e é ignorado pelo .gitignore.
  2. Confere a integridade: descompacta o .gz e compara o SHA-256 com o do
     original. Também avisa se algum .gz passar do limite do GitHub.
  3. Grava data/SHA256SUMS.txt com o hash do conteúdo original de cada bruto.
  4. Cria results/plots/ (usada pelos notebooks 02-04 para salvar figuras).

Uso (na raiz do repositório, pasta GitHub):
    python scripts/organizar_dados.py
"""

import gzip
import hashlib
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # pasta GitHub
DATA = RAIZ / "data"
LIMITE_GITHUB_MB = 100
AVISO_GITHUB_MB = 50

# (pasta de destino, nome do arquivo, locais onde o original pode estar)
BRUTOS = [
    (DATA / "CELESC", "celesc_consumo_uc_1994_2026.csv", [
        DATA / "CELESC",
        RAIZ.parent / "Apoio" / "Dados CELESC",
    ]),
    (DATA / "ANEEL", "tarifas-homologadas-distribuidoras-energia-eletrica.csv", [
        DATA / "ANEEL",
    ]),
]


def sha256_stream(f, bloco=8 * 1024 * 1024):
    h = hashlib.sha256()
    for parte in iter(lambda: f.read(bloco), b""):
        h.update(parte)
    return h.hexdigest()


def sha256_arquivo(caminho):
    with open(caminho, "rb") as f:
        return sha256_stream(f)


def sha256_gz(caminho):
    with gzip.open(caminho, "rb") as f:
        return sha256_stream(f)


def comprimir(origem, destino):
    # mtime=0 e sem nome no cabeçalho: o mesmo CSV gera sempre o mesmo .gz,
    # evitando commits "fantasmas" quando o script é rodado de novo.
    tmp = destino.with_suffix(destino.suffix + ".tmp")
    with open(origem, "rb") as f_in, open(tmp, "wb") as f_raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=f_raw, compresslevel=9, mtime=0) as f_out:
            shutil.copyfileobj(f_in, f_out, length=8 * 1024 * 1024)
    tmp.replace(destino)


def mb(caminho):
    return caminho.stat().st_size / 1e6


def main():
    if not (RAIZ / ".git").exists():
        sys.exit(f"ERRO: {RAIZ} não parece ser a raiz do repositório (sem .git).")

    hashes = {}
    problemas = []

    for pasta, nome, locais in BRUTOS:
        pasta.mkdir(parents=True, exist_ok=True)
        destino = pasta / f"{nome}.gz"
        origem = next((l / nome for l in locais if (l / nome).exists()), None)
        rel = destino.relative_to(RAIZ).as_posix()

        if origem is None:
            if destino.exists():
                print(f"[ok]   {rel} já existe (original .csv não encontrado; mantido como está)")
                hashes[rel] = sha256_gz(destino)
            else:
                problemas.append(f"{nome}: original não encontrado em {[str(l) for l in locais]}")
            continue

        print(f"[...]  {nome}: {mb(origem):.0f} MB em {origem.parent}")
        h_original = sha256_arquivo(origem)

        if destino.exists() and sha256_gz(destino) == h_original:
            print(f"[ok]   {rel} já está atualizado")
        else:
            print(f"       comprimindo (pode levar 1-3 min)...")
            comprimir(origem, destino)
            if sha256_gz(destino) != h_original:
                destino.unlink()
                problemas.append(f"{nome}: falha na verificação do .gz (arquivo removido)")
                continue
            print(f"[ok]   {rel}: {mb(origem):.0f} MB -> {mb(destino):.1f} MB (integridade conferida)")

        tamanho = mb(destino)
        if tamanho >= LIMITE_GITHUB_MB:
            problemas.append(f"{rel} tem {tamanho:.0f} MB: acima do limite do GitHub ({LIMITE_GITHUB_MB} MB)")
        elif tamanho >= AVISO_GITHUB_MB:
            print(f"[aviso] {rel} tem {tamanho:.0f} MB: o GitHub aceita, mas exibe aviso acima de {AVISO_GITHUB_MB} MB")
        hashes[rel] = h_original

    for pld in sorted((DATA / "CCEE").glob("pld_media_semanal_*.csv")):
        hashes[pld.relative_to(RAIZ).as_posix()] = sha256_arquivo(pld)

    linhas = ["# SHA-256 do CONTEÚDO ORIGINAL (descomprimido) de cada bruto.",
              "# Gerado por scripts/organizar_dados.py; permite verificar se a base mudou."]
    linhas += [f"{h}  {caminho}" for caminho, h in sorted(hashes.items())]
    (DATA / "SHA256SUMS.txt").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"[ok]   data/SHA256SUMS.txt ({len(hashes)} arquivos)")

    plots = RAIZ / "results" / "plots"
    plots.mkdir(parents=True, exist_ok=True)
    (plots / ".gitkeep").touch()
    print("[ok]   results/plots/ pronta")

    if problemas:
        print("\nPROBLEMAS:")
        for p in problemas:
            print("  -", p)
        sys.exit(1)

    print("\nConcluído. Próximo passo: rodar o notebook 00 e depois revisar o commit no VSCode.")


if __name__ == "__main__":
    main()
