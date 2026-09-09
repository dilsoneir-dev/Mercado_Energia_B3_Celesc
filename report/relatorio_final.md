# 📄 Relatório Técnico Final — Mestrado Profissional IFSC

**Título**: Aplicação de IA e Séries Temporais para Apoio à Decisão de Migração ao Mercado Livre de Energia: Um Estudo de Caso para Consumidores do Grupo B em Santa Catarina  
**Autor**: Eng. Dilson Eijo Rigotti  
**Disciplina**: Técnicas de Inteligência Artificial Aplicadas a Sistemas de Energia  
**Programa**: Programa de Pós-Graduação em Engenharia Elétrica / Mestrado Profissional  
**Instituição**: Instituto Federal de Santa Catarina (IFSC)  
**Data**: Setembro de 2026  

---

## 📌 Resumo

Este relatório apresenta a solução desenvolvida para a avaliação prática da disciplina de Técnicas de IA Aplicadas a Sistemas de Energia no Mestrado Profissional do IFSC. O trabalho cumpre o objetivo pedagógico de vivenciar o ciclo completo de análise de dados em engenharia de energia: formulação do problema real, reunião e limpeza de dados públicos, aplicação de técnicas e bibliotecas preditivas de IA, e interpretação crítica dos resultados. O problema abordado é a previsão de carga e o apoio à decisão para a migração dos consumidores de baixa tensão (Grupo B) para o Mercado Livre de Energia em Santa Catarina, em conformidade com o cronograma estabelecido pela **Lei nº 15.269/2025** (novembro/2027 para comercial/industrial B3 e novembro/2028 para residencial/rural B1 e B2). Utilizando uma base histórica representativa de **387 meses contínuos (1994 a 2026)** da CELESC Distribuição S.A., contendo 2,98 milhões de registros, realizou-se a decomposição estatística via STL e a modelagem preditiva via **SARIMAX** e **Gradient Boosting**. O modelo SARIMAX $(1,1,1) \times (1,1,1)_{12}$ obteve Erro Percentual Absoluto Médio (**MAPE**) de **6,03%** em validação fora da amostra (27 meses). Na elaboração deste projeto, o estudante de mestrado utilizou assistentes de IA Generativa como ferramenta de suporte computacional para acelerar o desenvolvimento do pipeline em Python e a documentação. Os resultados fornecem uma base previsível e robusta para subsidiar estratégias de contratação de energia no setor.

**Palavras-chave**: Sistemas de Energia; Mercado Livre de Energia; Grupo B; Séries Temporais; SARIMAX; Decomposição STL; Inteligência Artificial Generativa; IFSC.

---

## 1. Formulação do Problema e Motivação

Em conformidade com a proposta pedagógica da disciplina de Técnicas de IA Aplicadas a Sistemas de Energia do Mestrado Profissional do IFSC, a avaliação consiste na resolução prática de um problema real do setor elétrico utilizando ferramentas de inteligência artificial e análise de dados. O foco principal não se restringe à busca por inéditos teóricos ou à complexidade matemática isolada, mas sim ao domínio prático da experiência completa: desde o entendimento do problema físico-econômico, a reunião e estruturação de bases de dados representativas, até a aplicação de bibliotecas de aprendizado e a discussão crítica da solução sob a ótica da engenharia.

O problema real selecionado é o **planejamento da demanda e apoio à decisão para a migração ao Mercado Livre de Energia pelos consumidores de baixa tensão (Grupo B)** no Estado de Santa Catarina. O marco regulatório foi consolidado pela **Lei nº 15.269/2025**, que determinou o cronograma oficial de expansão do Ambiente de Contratação Livre (ACL):
- **Novembro de 2027**: Abertura do mercado livre para os consumidores comerciais e industriais atendidos em baixa tensão (Subgrupo B3);
- **Novembro de 2028**: Abertura para a totalidade dos demais consumidores de baixa tensão, incluindo a classe residencial (Subgrupo B1) e a classe rural (Subgrupo B2).

Por que optar por uma abordagem baseada em dados em vez de um modelo analítico determinístico? Em sistemas elétricos de distribuição, o comportamento de consumo do Grupo B envolve a agregação de milhões de pequenas unidades consumidoras com forte sensibilidade a fatores climáticos (temperatura estival e uso de climatização) e dinâmicas socioeconômicas. Um modelo analítico puro torna-se inviável devido à impossibilidade de equacionar deterministicamente as variáveis comportamentais e sazonais. A abordagem por séries temporais e modelos preditivos de IA permite extrair os padrões determinísticos de tendência e sazonalidade a partir do histórico real, oferecendo suporte quantitativo para comercializadoras e agentes de mercado.

---

## 2. Base de Dados, Representatividade e Processamento (ETL)

### 2.1. Origem dos Dados e Critério de Representatividade
Como destacado nas diretrizes da disciplina, a qualidade e a representatividade da base de dados são preceitos fundamentais para garantir que a modelagem capture a realidade do sistema elétrico. Coletar apenas um curto período de dados (como um único ano) impede que os algoritmos identifiquem dinâmicas de longo prazo, ciclos sazonais e sensibilidades a eventos extremos.

Para este estudo, utilizou-se a base de dados histórica oficial da **CELESC Distribuição S.A.**, auditada pela ANEEL através do Sistema de Acompanhamento do Mercado de Distribuição (SAMP), disponibilizada publicamente no repositório `mlsfinternacional-cpu/03_Mercado_Energia_SC`. A base contempla **387 meses contínuos de registros (de janeiro de 1994 a março de 2026)**, abrangendo 32 anos de histórico real do mercado elétrico de Santa Catarina. Esse amplo horizonte temporal garante que o modelo aprenda com múltiplos ciclos econômicos, expansão da infraestrutura e variações climáticas históricas.

### 2.2. Engenharia de Recursos e Estruturação (Pipeline ETL em Python)
A planilha bruta (`Municipio_Mensal_1T_2026.xlsx`) apresentava formato pivoteado (*wide format*) com 395 colunas. O estudante de mestrado desenvolveu um pipeline computacional em Python (utilizando as bibliotecas `pandas` e `numpy`) para descarte de inconsistências, conversão dos cabeçalhos temporais e unpivot (*melt*) da matriz. O resultado foi a geração de um banco de dados estruturado no formato longo com **2.986.092 registros**, contendo o consumo em MWh, o número de Unidades Consumidoras (UC) e o consumo específico (kWh/UC/mês) segregados por município e classe de consumo.

---

## 3. Metodologia de Séries Temporais e Uso de IA Generativa

### 3.1. Transparência sobre o Uso de IA Generativa no Desenvolvimento
Em consonância com as práticas modernas de pesquisa científica no mestrado, declara-se que o aluno utilizou assistentes de **Inteligência Artificial Generativa (Antigravity / LLM)** como ferramenta de suporte computacional e produtividade. A IA foi empregada nas seguintes etapas do trabalho:
1. Auxílio na escrita e otimização dos scripts de manipulação de dados em Python (tratamento de exceções e unpivot do arquivo Excel de 36 MB);
2. Apoio no enquadramento sintático das bibliotecas estatísticas (`statsmodels` e `scikit-learn`) para treinamento dos modelos SARIMAX e Gradient Boosting;
3. Suporte na formatação automatizada do relatório final segundo as normas ABNT.

Cabe ressaltar que a concepção do problema, a definição da estratégia de negócio do Mercado Livre, a interpretação crítica das métricas preditivas e a validação dos resultados foram conduzidas rigorosamente sob a responsabilidade e supervisão direta do estudante de mestrado.

### 3.2. Decomposição STL (Seasonal-Trend decomposition using LOESS)
Para separar a tendência determinística de longo prazo do ciclo sazonal de verão, aplicou-se a decomposição aditiva STL: $Y_t = T_t + S_t + R_t$. As forças de tendência ($F_T$) e sazonalidade ($F_S$) foram calculadas a partir das variâncias dos componentes decompostos.

### 3.3. Modelagem Preditiva: SARIMAX vs Machine Learning
Foram implementadas duas abordagens preditivas concorrentes:
- **Modelo SARIMAX $(1,1,1) \times (1,1,1)_{12}$**: Modelo estatístico clássico de séries temporais parametrizado via análise de autocorrelação (ACF/PACF), capturando a inércia autorregressiva e o ciclo sazonal de 12 meses;
- **HistGradientBoostingRegressor (ML)**: Modelo de aprendizado baseado em árvores de decisão impulsionadas, alimentado com 12 variáveis de defasagem (*lags*) e codificadores de calendário.

---

## 4. Resultados e Discussão dos Modelos

A tabela abaixo apresenta o diagnóstico estatístico da decomposição STL para as três principais classes de consumo do Grupo B catarinense:

| Classe do Grupo B | Força Tendência ($F_T$) | Força Sazonalidade ($F_S$) | Consumo Médio (MWh) | Consumo Máximo (MWh) |
|-------------------|-------------------------|----------------------------|---------------------|----------------------|
| **Residencial (B1)** | **0,9816** | **0,8325** | 374.368,19 | 866.634,57 |
| **Comercial (B3)** | **0,9758** | **0,8252** | 208.631,87 | 382.136,78 |
| **Rural (B2)** | **0,9241** | **0,6737** | 102.276,39 | 154.303,63 |

Como discutido nas orientações da disciplina, a identificação clara da força de tendência ($F_T > 92\%$) e sazonalidade ($F_S > 82\%$) justifica a elevada previsibilidade da demanda. A tabela a seguir apresenta o confronto de acurácia preditiva na janela de teste fora da amostra (27 meses, de jan/2024 a mar/2026):

| Modelo de IA / Estatístico | RMSE (MWh) | MAE (MWh) | **MAPE (%)** |
|----------------------------|------------|-----------|--------------|
| **SARIMAX $(1,1,1) \times (1,1,1)_{12}$** | **52.040,77** | **42.435,58** | **6,03%** |
| **HistGradientBoosting (ML)** | 86.599,07 | 63.708,02 | 8,40% |

O modelo **SARIMAX obteve um MAPE de apenas 6,03%**, demonstrando um alinhamento preditivo robusto. A projeção continuada até o final de 2028 indica que no marco de **Novembro de 2028** (abertura B1 Residencial), a demanda nos meses estivais ultrapassará **950.000 MWh/mês**, exigindo que comercializadoras estabeleçam contratos de perfil de acompanhamento de carga (*load-following*).

---

## 5. Conclusões e Aplicabilidade Prática

O presente trabalho cumpriu integralmente o objetivo da disciplina de proporcionar a experiência prática completa de análise de dados aplicada a sistemas de energia. Ao focar em um problema real de relevante impacto regulatório e econômico no estado de Santa Catarina, o estudo demonstrou que:
1. A estruturação adequada de um longo histórico de dados (32 anos da CELESC) é o pilar fundamental que viabilizou o treinamento preciso dos algoritmos, superando análises restritas a curto prazo;
2. O modelo SARIMAX $(1,1,1) \times (1,1,1)_{12}$ forneceu uma projeção de altíssima acurácia (MAPE de 6,03%), permitindo prever que a demanda residencial em SC superará 950.000 MWh/mês nos picos estivais de 2028;
3. O uso de assistentes de IA Generativa atuou como um catalisador de produtividade para o mestrando, agilizando o tratamento de dados complexos em Python e a documentação acadêmica, enquanto o julgamento técnico de engenharia conduziu a interpretação dos resultados.

---

## 6. Referências Bibliográficas

1. **ANEEL**. *Sistema de Acompanhamento do Mercado de Distribuição de Energia Elétrica (SAMP)*. Agência Nacional de Energia Elétrica. Disponível em: <https://dadosabertos.aneel.gov.br/>. Acesso em: 2026.
2. **BRASIL**. *Lei nº 15.269, de 2025*. Altera a legislação do setor elétrico para a expansão do mercado livre de energia a consumidores de baixa tensão. Brasília, DF, 2025.
3. **CELESC DISTRIBUIÇÃO S.A.** *Dados Históricos de Vendas de Energia por Município (1994-2026)*. Florianópolis, SC, 2026.
4. **GOLDBERG, D. E.** *Genetic Algorithms in Search, Optimization, and Machine Learning*. New York: Addison-Wesley, 1989.
5. **HAYKIN, S.** *Redes Neurais: Princípios e Práticas*. 2ª ed. Porto Alegre: Artmed Editora, 2002.
6. **HYNDMAN, R. J.; ATHANASOPOULOS, G.** *Forecasting: principles and practice*. 3rd ed. Melbourne: OTexts, 2021.
