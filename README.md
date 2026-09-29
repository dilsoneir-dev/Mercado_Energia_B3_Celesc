# Mercado_Energia_B3_Celesc

**Análise de Dados com Uso de Inteligência Artificial como Ferramenta de Apoio à Migração de Consumidores do Subgrupo B3 para o Mercado Livre de Energia**

Mestrado Profissional em Sistemas de Energia Elétrica (MPSEE) — IFSC, Câmpus Florianópolis
Disciplina: IAA68303 — Técnicas de Inteligência Artificial Aplicadas a Sistemas de Energia (2026.3 — T01)
Professor: Sérgio Luciano Ávila
Aluno: Dilsonei José Rigotti

---

## Objetivo Principal

Trazer um problema ligado a sistemas de energia com dados públicos disponíveis, efetuar a manipulação desses dados utilizando como suporte ferramentas de Inteligência Artificial (IA), realizar análises, buscar resultados e fazer projeções. Antes de ser uma busca original e complexa por resultados, o foco do trabalho é o de estabelecer um entendimento sobre o esforço necessário para se trabalhar com dados, efetuar simulações, comparar indicadores e propor cenários, considerando o uso de arquiteturas de redes neurais (como o LSTM) em bibliotecas existentes (caso do TensorFlow), desenvolvidas para criar, treinar e implantar modelos de Aprendizado de Máquina (Machine Learning) e Redes Neurais Profundas (Deep Learning).

## Objetivo Secundário

Projetar o consumo de energia elétrica do Subgrupo B3 Comercial (mercado cativo) da CELESC até 2030 e avaliar a vantajosidade financeira da migração desses consumidores para o Ambiente de Contratação Livre (ACL), cuja abertura para a baixa tensão está prevista pela Lei nº 15.269/2025 a partir de novembro de 2027.

## Estrutura do repositório

```
Mercado_Energia_B3_Celesc/
├── notebooks/
│   ├── 00_tratamento_dados_brutos.ipynb        # Ingestão e saneamento (CELESC, ANEEL, CCEE); trilhas B3_Cativo e Comercial_Livre_ACL
│   ├── 01_exploratorio_grupo_b_stl.ipynb       # Análise exploratória do Grupo B e decomposição STL
│   ├── 02_comparacao_modelos_b3.ipynb          # Holt-Winters, LSTM e Gradient Boosting (janela única + walk-forward)
│   ├── 03_projecao_consumo_b3_2030.ipynb       # STL e projeção de consumo até 2030
│   └── 04_analise_economica_migracao_acl.ipynb # Simulação Cativo x Livre, encargos do mercado livre e riscos
├── data/
│   ├── CELESC/  ANEEL/  CCEE/                  # Dados brutos originais (maiores em .csv.gz)
│   ├── SHA256SUMS.txt                          # "Impressão digital" de cada bruto: congela a versão dos dados
│   └── processed/                              # Séries tratadas, métricas, previsões e simulações
├── results/
│   └── plots/                                  # Figuras do relatório
├── report/
│   ├── Relatorio_TecnicasIA_Dilsonei.docx      # Relatório final (formato IEEE)
│   └── Apresentação_TecnicasIA_Dilsonei.pptx   # Apresentação do trabalho
├── scripts/
│   └── organizar_dados.py                      # Prepara os brutos (compressão .gz + SHA256SUMS.txt); fora dos notebooks
├── requirements.txt
├── .gitignore
└── README.md
```

## Fontes de dados

Os dados brutos estão versionados no próprio repositório e também podem ser obtidos nos portais públicos:

| Fonte | Conteúdo | Link |
|---|---|---|
| CELESC | Consumo mensal por município, classe e tipo de contratação (jan/1994–mar/2026) | https://www.celesc.com.br/home/mercado-de-energia/dados-de-consumo |
| ANEEL | Tarifas homologadas das distribuidoras (TUSD e TE), ago/2010–ago/2027 | https://dadosabertos.aneel.gov.br/dataset/tarifas-distribuidoras-energia-eletrica |
| CCEE | PLD médio semanal (2001–2026), filtrado no submercado Sul | https://dadosabertos.ccee.org.br/dataset/pld_media_semanal |

**Arquivos brutos não versionados.** Para manter o repositório leve, as versões descomprimidas dos brutos e as planilhas originais baixadas dos portais não são versionadas (ver `.gitignore`). Os notebooks leem apenas os arquivos `.csv.gz` versionados, cuja integridade pode ser conferida pelos hashes em `data/SHA256SUMS.txt`:

- `data/ANEEL/tarifas-homologadas-distribuidoras-energia-eletrica.csv` (~89 MB): versão descomprimida do `.csv.gz` versionado.
- `data/CELESC/Municipio_Mensal_1T_2026.xlsx` (~36 MB): planilha de consumo mensal por município baixada do portal de Dados de Consumo da CELESC (link acima), com data de arquivo de 02/08/2026. Não é lida pelos notebooks; é mantida apenas localmente como registro da fonte original.

**Congelamento dos dados (`data/SHA256SUMS.txt`).** Os portais da CELESC, da ANEEL e da CCEE são atualizados continuamente, então baixar os dados novamente não garante obter os mesmos arquivos usados neste trabalho. O `SHA256SUMS.txt` registra o hash SHA-256 (uma "impressão digital" do conteúdo) de cada arquivo bruto: ele congela a versão dos dados que gerou os resultados e permite detectar qualquer alteração posterior. Se um arquivo for substituído por uma versão nova baixada do portal, o hash deixa de coincidir.

**Preparação dos dados brutos (`scripts/organizar_dados.py`).** Script executado **fora dos notebooks**, antes do notebook 00, e necessário apenas quando os dados brutos são atualizados. Ele comprime os brutos grandes (CELESC e ANEEL) em `.csv.gz` para caberem no limite do GitHub (100 MB), confere a integridade da compressão comparando os hashes e gera o `data/SHA256SUMS.txt`. Não faz parte da análise: o tratamento, a modelagem e as simulações, que estão todos nos notebooks.

```bash
python scripts/organizar_dados.py
```

## Como executar

Ambiente de referência: **Python 3.11**, com as versões fixadas no `requirements.txt` (incluindo TensorFlow 2.21):

```bash
pip install -r requirements.txt
```

Execute os notebooks na ordem **00 → 02 → 03 → 04**. O notebook 01 é exploratório e independente: lê o arquivo versionado `data/processed/sc_grupo_b_mensal.csv`, cujo código de geração a partir da base bruta não faz parte do repositório. Como os dados brutos estão versionados e o LSTM roda em modo determinístico, a execução no ambiente do `requirements.txt` reproduz exatamente os números do relatório.

## Metodologia (resumo)

**Tratamento dos dados:** filtragem da classe Comercial e do tipo Cativo (representativos do Subgrupo B3); agregação de duplicatas; expurgo de registros com UC ≤ 0 e consumo < 0; filtro IQR (100–3.000 kWh/UC/mês). A série final tem 376 dos 387 meses (jan–nov/1994 ausentes na fonte).

**Modelos:**
- **LSTM** (TensorFlow/Keras) — 1 camada LSTM (32 unidades) + densa (16, ReLU) + saída linear; janela de 12 meses; z-score ajustado só no treino; Adam (lr = 0,005); early stopping; previsão recursiva.
- **Gradient Boosting** (HistGradientBoostingRegressor) — previsão recursiva com defasagens da série.
- **Holt-Winters** (statsmodels) — tendência e sazonalidade aditivas, 12 períodos (referência estatística).
- **STL** — FT = 0,956; FS = 0,667 para o B3 Comercial.

**Validação walk-forward** (21 janelas de 12 meses, 2005–2025, retreino a cada janela):

| Modelo | MAPE médio | Wilcoxon vs. HW |
|---|---|---|
| Holt-Winters | 9,01% | — |
| Gradient Boosting | 10,19% | p = 0,137 |
| LSTM | 12,84% | p = 0,002 |

**Simulação financeira (abr/2026–dez/2030):** Cativo = consumo × (TUSD + TE); Livre = consumo × (TUSD + PLD Sul + encargos). Sem encargos, a economia média projetada do Livre é de **24,8%** — um limite otimista.

**Encargos do mercado livre (notebook 04, Seção 6.1).** Ao migrar, o consumidor deixa de pagar a TE, mas passa a pagar diretamente componentes que no cativo estão embutidos nela. CDE, PROINFA, TFSEE, P&D/EE e ONS fazem parte da TUSD e são pagos igualmente nos dois ambientes, por isso não entram como custo adicional. Premissas de referência (R$/MWh, 2026):

| Componente | Otimista | Base | Pessimista |
|---|---|---|---|
| Perdas na rede básica (sobre o preço da energia) | 1,5% | 2,0% | 3,0% |
| ESS + EER + ERCAP | 10 | 20 | 40 |
| Angra 1 e 2 (Lei 15.235/2025, desde 2026) | 3 | 5 | 8 |
| Comercializador varejista + contribuição CCEE | 10 | 20 | 40 |
| Prêmio de risco do contrato sobre o PLD | 15 | 30 | 60 |
| Novos encargos da Lei 15.269/2025 (sobrecontratação, SUI), a partir de nov/2027 | 0 | 0 | 15 |
| **Economia média do Livre** | **19,7%** | **15,0%** | **4,6%** |
| Meses em que o Livre é mais barato | 57 de 57 | 55 de 57 | 42 de 57 |

**Validação histórica 2011–2025 (Seção 6.2):** um consumidor B3 exposto ao PLD, com os encargos do cenário base, teria pago mais que no cativo em **7 dos 15 anos** (5 sem encargos); o pior ano foi 2014 (−164%). O benefício da migração depende fortemente do regime hidrológico.

## Justificativa da escolha das técnicas

A ferramenta de inteligência computacional central é a rede neural recorrente **LSTM**, escolhida porque a projeção de consumo é um problema de série temporal: cada valor depende dos meses anteriores e do mesmo mês em anos passados. O LSTM foi concebido para aprender dependências de longo prazo em sequências e, por ser não linear, pode capturar rupturas como a recessão de 2015–2016, a pandemia de 2020 e a queda de 2025. O **Gradient Boosting** foi adotado como comparação (segunda técnica) de aprendizado de máquina (abordagem não neural, de menor custo), e o **Holt-Winters** como referência estatística — uma técnica de IA só se justifica se superar um método clássico bem ajustado.

O trabalho não pressupõe a superioridade da IA: o LSTM é tratado como hipótese a ser testada, por validação walk-forward e teste de Wilcoxon, e não por uma única divisão treino/teste. O resultado indicou, para esta simulação, que o modelo Holt-Winters é mais preciso e estável, o que é coerente com a série: apenas 376 observações mensais, volume reduzido para redes profundas, e tendência e sazonalidade fortes, que um modelo de decomposição explícita captura de forma eficiente. O LSTM foi mantido na projeção por ser uma ferramenta a ser avaliada; essa escolha não altera a economia percentual, que depende apenas da razão entre as componentes tarifárias e é invariante ao modelo de consumo. O LSTM é mais promissor para dados de maior resolução (informação horária, medição inteligente) e/ou com variáveis exógenas (temperatura, atividade econômica, geração distribuída, feriados, tarifas,...).

## Principais limitações

- "Comercial Cativo" é uma aproximação do Subgrupo B3 (a base não tem coluna por subgrupo tarifário).
- Incerteza da projeção cresce ao longo dos 57 meses, especialmente em 2029–2030.
- Encargos do mercado livre estimados por premissa (três cenários), não por dados de mercado; garantias financeiras e penalidades por desvio de contrato não modeladas.
- PLD como referência do preço no ACL, com 100% do consumo exposto a ele.
- Extrapolações simples de tarifa (6% a.a.) e PLD (média sazonal 2021–2026); não capturam choques hidrológicos como o de 2021.
- Geração distribuída (SCEE) reduz o consumo registrado e não é modelada.

## Uso de IA generativa

O desenvolvimento dos códigos e scripts contou com o assistente Claude (Anthropic) como apoio à programação, depuração e revisão. Todas as análises foram executadas e validadas pelo autor; o assistente não integra o método preditivo.

## Licença

Uso acadêmico.
