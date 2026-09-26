# Mercado de Energia de Santa Catarina (Subgrupo B3)

Uma análise exploratória e modelagem preditiva da infraestrutura elétrica de Santa Catarina como ponto de partida para pesquisas em Inteligência Artificial, Mercado Livre de Energia e Apoio à Tomada de Decisão.

---

# Visão Geral

Este projeto analisa dados públicos do mercado de energia elétrica do estado de Santa Catarina, disponibilizados pela CELESC Distribuição S.A., com foco no **Subgrupo B3 Comercial** (baixa tensão).

O objetivo principal é avaliar o comportamento do consumo de eletricidade e desenvolver modelos de **Aprendizado de Máquina (Machine Learning)** para previsão de demanda de longo prazo, em conformidade com o cronograma de abertura de mercado estabelecido pela **Lei nº 15.269/2025**.

Além de explorar o conjunto de dados histórico, este projeto busca compreender como a previsão precisa de carga pode servir como ferramenta estratégica na migração de consumidores para o **Ambiente de Contratação Livre (ACL)**.

Este repositório foi desenvolvido como requisito prático na disciplina de *Técnicas de Inteligência Artificial Aplicadas a Sistemas de Energia* do **Mestrado Profissional em Sistemas de Energia (MPSEE)** do **Instituto Federal de Santa Catarina (IFSC)** — *Campus Florianópolis*.

---

# Objetivo

Analisar a distribuição e o comportamento histórico do consumo de energia elétrica do Subgrupo B3 Comercial em Santa Catarina, desenvolvendo e validando modelos de Inteligência Artificial capazes de fornecer indicadores precisos para mitigação de riscos contratuais e análise de viabilidade econômica no Mercado Livre.

---

# Contexto

A abertura gradual do setor elétrico brasileiro está expandindo o acesso ao Mercado Livre para consumidores comerciais conectados em baixa tensão. Com a perspectiva de abertura total até o final de 2027, a previsão precisa de demanda torna-se um pilar crítico de gestão.

No Mercado Livre, incertezas na estimativa de consumo geram riscos financeiros diretos:

- **Cláusulas de Take-or-Pay:** Penalidades por subcontratação ou sobrecontratação de energia.
- **Volatilidade do PLD:** Exposição aos picos de preço no mercado de curto prazo (*Preço de Liquidação das Diferenças*), principalmente em períodos de escassez hídrica.
- **Sazonalização e Modulação:** Necessidade de adequação dos contratos ao perfil real de consumo ao longo dos meses do ano.

Com base nos dados históricos da CELESC (que abrangem o período de 1994 a 2026 com cerca de 3 milhões de registros), esta pesquisa investiga a força da tendência de crescimento e a sazonalidade estival do comércio catarinense, avaliando o potencial de economia (*savings*) frente às tarifas reguladas (ACR).

---

# Questões de Pesquisa

Este estudo busca responder a perguntas como:

- Quais são os componentes dominantes de tendência e sazonalidade no consumo comercial de Santa Catarina?
- Como os modelos de Machine Learning (como *HistGradientBoosting*) se comparam às abordagens estatísticas clássicas (SARIMAX, Holt-Winters) na previsão fora da amostra?
- Qual é o nível de precisão (MAPE, RMSE) alcançado na previsão de carga comercial de longo prazo?
- Como as oscilações do PLD e os eventos hidrológicos (como a crise de 2021) afetam a viabilidade financeira da migração para o Mercado Livre?
- Como a modelagem preditiva baseada em IA pode apoiar gestores e engenheiros na estruturação de contratos de fornecimento?

---

# Fonte dos Dados

- **CELESC Distribuição S.A.** — Portal de Relações com Investidores e Boletins Operacionais (1994–2026).
- **ANEEL** — Sistema de Acompanhamento do Mercado de Distribuição (SAMP).
- **CCEE** — Câmara de Comercialização de Energia Elétrica (Histórico de PLD e encargos).
- **Lei nº 15.269/2025** — Diretrizes regulatórias para abertura do mercado livre de energia.

---

# Tecnologias

- Python
- Pandas
- NumPy
- Scikit-Learn (*HistGradientBoosting*)
- Statsmodels (*Decomposição STL, SARIMAX*)
- Matplotlib & Seaborn
- Jupyter Notebook
- Git & GitHub
- VS Code

---

# Estrutura do Projeto

```text
Mercado_Energia_B3_Celesc/
├── data/
│   ├── CELESC/        # Consumo por UC 1994–2026 (bruto, .csv.gz) e séries B3 tratadas
│   ├── ANEEL/         # Tarifas homologadas das distribuidoras (bruto, .csv.gz)
│   ├── CCEE/          # PLD médio semanal 2001–2026 (bruto, .csv)
│   ├── processed/     # Dados tratados: saídas do notebook 00 (trilha B3, lidas por 02–04)
│   │                  #   e sc_grupo_b_mensal.csv (base revisada do Grupo B, lida pelo 01)
│   └── SHA256SUMS.txt # Hash do conteúdo original de cada bruto (reprodutibilidade)
├── notebooks/         # Notebooks Jupyter em sequência lógica:
│   ├── 00_tratamento_dados_brutos.ipynb        # Ingestão, saneamento e exportação para data/processed
│   ├── 01_exploratorio_grupo_b_stl.ipynb       # Exploratório do Grupo B: STL, ACF/PACF e forças F_T/F_S por classe
│   ├── 02_comparacao_modelos_b3.ipynb          # B3: Holt-Winters × LSTM × Gradient Boosting (teste único e walk-forward)
│   ├── 03_projecao_consumo_b3_2030.ipynb       # B3: STL e projeção de consumo até dez/2030 (LSTM)
│   └── 04_analise_economica_migracao_acl.ipynb # B3: custo cativo × livre, economia e sensibilidade
├── report/            # Relatórios técnicos finais
├── results/plots/     # Figuras geradas pelos notebooks
├── scripts/
│   └── organizar_dados.py  # Comprime e verifica os brutos para versionamento
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Como Reproduzir

1. Clone o repositório e instale as dependências: `pip install -r requirements.txt`.
2. Os dados brutos já vêm no repositório, comprimidos (`.csv.gz`) nas pastas `data/CELESC`, `data/ANEEL` e `data/CCEE`. O `pandas` lê esses arquivos diretamente, sem descompactar.
3. Execute a trilha B3 em ordem: `00` → `02` → `03` → `04`. O notebook `00` gera os arquivos de `data/processed/` usados pelos demais, e o `03` gera a previsão de consumo usada pelo `04`. O notebook `01` (exploratório do Grupo B) é independente e pode ser executado a qualquer momento.

Para atualizar um bruto (por exemplo, com uma nova versão baixada do portal): salve o `.csv` original na pasta da fonte, rode `python scripts/organizar_dados.py` e faça o commit do `.csv.gz` e do `data/SHA256SUMS.txt` atualizados. Registre a nova data de acesso na seção 1 do notebook `00`.

---

# Roteiro do Projeto (Roadmap)

- [x] Extração e pré-processamento da base histórica da CELESC (1994–2026)
- [x] Decomposição de séries temporais (STL) identificando forças de tendência e sazonalidade
- [x] Comparação de desempenho de modelos preditivos (SARIMAX, Holt-Winters, HistGradientBoosting)
- [x] Seleção do modelo campeão com base nos indicadores MAPE e RMSE
- [x] Análise de viabilidade econômica no ACL sob cenários de volatilidade do PLD (2015–2026)
- [x] Elaboração de documentação e relatório técnico final para o IFSC

---

# Principais Resultados e Desempenho

### 1. Decomposição de Séries Temporais (STL)
- **Força da Tendência ($F_T$):** `0,9758` (refletindo o crescimento estrutural contínuo do comércio catarinense).
- **Força da Sazonalidade ($F_S$):** `0,8252` (picos marcantes no verão impulsionados por refrigeração no varejo e turismo).

> **Nota de validação (set/2026):** as métricas acima foram recalculadas sobre uma versão revisada da base (`sc_grupo_b_mensal.csv`), após identificação e correção de inconsistências na fonte original — ver seção **Qualidade de Dados** abaixo. Os valores atualizados foram $F_T = 0{,}9897$ e $F_S = 0{,}8703$, ligeiramente superiores aos originais. A conclusão qualitativa (tendência muito forte, sazonalidade estival marcante) permanece a mesma; o aumento reflete a redução de ruído residual após a limpeza, não uma mudança de interpretação. Os modelos preditivos (tabela abaixo) ainda não foram reavaliados sobre a base corrigida.

### 2. Confronto de Desempenho dos Modelos (Teste Fora da Amostra)

| Modelo / Algoritmo | RMSE (MWh) | MAE (MWh) | MAPE (%) | Status |
| :--- | :---: | :---: | :---: | :---: |
| **HistGradientBoosting (Machine Learning)** | **22.544,41** | **19.920,69** | **7,46%** | **Campeão 🏆** |
| Holt-Winters Sazonal | 53.820,64 | 47.917,99 | 18,53% | Descartado |
| SARIMAX (1,1,1)x(1,1,1)12 | 55.389,37 | 49.864,36 | 19,45% | Descartado |

---

# Qualidade de Dados

Uma revisão de qualidade de dados foi conduzida sobre a base histórica da CELESC (1994–2026), identificando e corrigindo as seguintes inconsistências antes da modelagem:

| Inconsistência identificada | Tratamento aplicado |
| :--- | :--- |
| Granularidade por unidade consumidora (UC) individual no tipo de contratação "Livre", divergente da granularidade já agregada do tipo "Cativo" | Agregação por soma em `(tipo, classe, município, mês)` |
| Valores negativos em `consumo_mwh`, `numero_uc` e `consumo_medio_kwh_uc` (fisicamente inválidos) | Convertidos para ausente antes de qualquer agregação |
| `numero_uc = 0` simultâneo a `consumo_mwh > 0` (logicamente contraditório) | Convertido para ausente (7.924 casos identificados nas classes Residencial, Comercial e Rural) |
| Anomalia sistêmica concentrada em jan.–mar./2020 (picos pontuais e lacunas), afetando majoritariamente municípios pequenos | Documentada como limitação conhecida; dados mantidos sem alteração |
| Ausência de coluna de grupo tarifário oficial (A/B) — a coluna `classe` reflete atividade econômica, não tensão/demanda contratada | Proxy estimada a partir do tipo de contratação (`Livre` → Grupo A; `Cativo` → Grupo B, com ressalva de que superestima o Grupo B real) |
| Geração distribuída fotovoltaica não contemplada no consumo faturado | Registrada como limitação metodológica; sem tratamento possível com os dados disponíveis |

A base corrigida (`sc_grupo_b_mensal.csv`, classes Residencial/Comercial/Rural) e a base específica do subgrupo B3 Comercial com o detalhamento Cativo/Livre preservado estão documentadas em relatório técnico próprio, disponível para consulta com o autor.

---

# Próximos Passos (alinhamento em andamento)

- [ ] Reavaliar as métricas de erro dos modelos preditivos (RMSE/MAPE, tabela acima) sobre a base corrigida, verificando se as correções aplicadas ao período de teste (2024–2026) alteram o ranking dos modelos.
- [ ] Incorporar ao notebook 03 a segmentação Cativo/Livre (proxy de grupo tarifário A/B) na análise do subgrupo B3 Comercial.
- [ ] Avaliar impacto da geração distribuída fotovoltaica (pós-2016) como variável explicativa complementar.
- [ ] Consolidar a seção de metodologia do artigo/relatório final com o detalhamento de qualidade de dados acima.

---

Este repositório faz parte de uma linha de pesquisa acadêmica contínua voltada para:

- Inteligência Artificial Aplicada a Sistemas de Energia
- Previsão de Carga e Redes Inteligentes (*Smart Grids*)
- Análise de Dados no Mercado Livre de Energia
- Gestão de Riscos e Economia da Energia

O objetivo final é conectar técnicas avançadas de Ciência de Dados com soluções de apoio à decisão para a transição e modernização do setor elétrico em Santa Catarina.

---

# Autor

**Dilsonei José Rigotti**

*Mestrando em Sistemas de Energia (MPSEE) | Engenheiro | Pesquisador em IA e Sistemas de Energia*

*Professor: Sérgio Ávila

*Instituto Federal de Santa Catarina (IFSC) — Campus Florianópolis*

---

### Repositório Oficial

https://github.com/dilsoneir-dev/Mercado_Energia_B3_Celesc