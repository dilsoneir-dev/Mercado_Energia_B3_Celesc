# Guia de Análise
## Energy Market of Santa Catarina

> "A análise deve responder perguntas de pesquisa, não apenas explorar dados."

---

# Objetivo Geral

Investigar como o consumo de energia elétrica está distribuído em Santa Catarina e identificar padrões que possam subsidiar estudos futuros sobre infraestrutura energética, economia digital, Inteligência Artificial e Data Centers.

Este documento servirá como guia durante toda a Análise Exploratória dos Dados (EDA), garantindo que cada etapa responda às perguntas definidas no README do projeto.

---

# Fluxo da investigação

```text
Conhecer a base
        ↓
Entender sua qualidade
        ↓
Analisar consumo
        ↓
Encontrar padrões
        ↓
Criar indicadores
        ↓
Levantar hipóteses
```

---

# ETAPA 1 — Conhecendo a Base

## Pergunta

Que dados eu possuo?

## Objetivos

- Entender a estrutura da base
- Conhecer as variáveis disponíveis
- Identificar possíveis limitações

## Verificar

- Número de linhas
- Número de colunas
- Tipos das variáveis
- Datas disponíveis
- Municípios
- Classes
- Tipo de mercado
- Valores nulos
- Duplicidades

## Funções úteis

```python
df.shape
df.info()
df.describe()
df.columns
df.isna().sum()
df.nunique()
df.value_counts()
```

## Produto esperado

Conhecimento completo da estrutura da base.

---

# ETAPA 2 — Cobertura da Base

## Pergunta

A base representa adequadamente o mercado de energia de Santa Catarina?

## Buscar

- Quantos municípios existem?
- O período histórico disponível
- Existem municípios faltantes?
- Existem registros duplicados?

## Variáveis

- município
- data

## Produto esperado

Caracterização geral do dataset.

---

# ETAPA 3 — Distribuição do Consumo

## Pergunta do projeto

> Como o consumo de energia está distribuído entre os municípios catarinenses?

## Buscar

- Consumo total por município
- Ranking
- Top 10 municípios
- Bottom 10 municípios

## Variáveis

- município
- consumo_mwh

## Produto esperado

Identificar onde está concentrado o consumo de energia.

---

# ETAPA 4 — Evolução Temporal

## Pergunta

Como o consumo evoluiu ao longo do tempo?

## Buscar

- Crescimento anual
- Crescimento mensal
- Tendência
- Sazonalidade

## Variáveis

- data
- consumo_mwh

## Produto esperado

Primeira visão temporal do consumo.

---

# ETAPA 5 — Perfil Setorial

## Pergunta do projeto

Quais setores concentram maior demanda de energia?

## Buscar

Consumo por:

- Residencial
- Industrial
- Comercial
- Rural
- Serviço Público
- Poder Público
- Iluminação Pública
- Próprio
- Revenda

## Variável

classe

## Produto esperado

Perfil econômico do consumo de energia.

---

# ETAPA 6 — Mercado Livre x Mercado Cativo

## Pergunta

Como está distribuído o mercado de energia?

## Buscar

- Consumo por tipo
- Participação percentual
- Evolução temporal

## Variável

tipo

## Produto esperado

Entender a abertura do mercado de energia.

---

# ETAPA 7 — Polos de Consumo

## Pergunta do projeto

Quais regiões concentram maior demanda de energia?

## Buscar

Identificar os municípios de maior consumo.

Exemplos:

- Joinville
- Florianópolis
- Blumenau
- Itajaí
- Chapecó
- Criciúma
- Lages

Depois regionalizar.

## Produto esperado

Mapa energético de Santa Catarina.

---

# ETAPA 8 — Grande Florianópolis

## Pergunta

Como a Grande Florianópolis se comporta em relação ao restante do estado?

## Buscar

Analisar:

- Florianópolis
- São José
- Palhoça
- Biguaçu

Comparar:

- Consumo
- Crescimento
- Classes
- Mercado Livre

## Produto esperado

Capítulo específico da pesquisa.

---

# ETAPA 9 — Indicadores

Após conhecer a base, desenvolver indicadores.

Exemplos:

- Consumo total
- Consumo por município
- Consumo por classe
- Participação do mercado livre
- Crescimento médio
- Participação regional

---

# ETAPA 10 — Cruzamentos (Fase 2)

Nesta etapa serão integradas outras bases públicas.

Exemplos

- IBGE
- ACATE
- Receita Federal
- Atlas Solar
- PIB Municipal
- Índice de Desenvolvimento Humano
- Centros de inovação
- Parques tecnológicos

Objetivo:

Relacionar infraestrutura energética com desenvolvimento econômico e tecnológico.

---

# ETAPA 11 — Inteligência Artificial e Data Centers

## Pergunta principal do projeto

Existem indícios de concentração energética compatíveis com regiões de maior desenvolvimento tecnológico?

## Buscar

Cruzar:

Energia

+

Economia

+

Tecnologia

+

Infraestrutura

+

Conectividade

## Observação

Esta etapa não busca provar uma hipótese.

Busca levantar evidências para estudos futuros.

---

# Durante toda a análise

Antes de escrever qualquer código, responder:

## 1. Qual pergunta estou tentando responder?

---

## 2. Quais colunas respondem essa pergunta?

---

## 3. Qual gráfico ou indicador melhor representa essa resposta?

---

## 4. O resultado aproxima ou afasta a hipótese inicial?

---

## 5. O que essa descoberta acrescenta ao projeto?

---

# Estrutura recomendada para cada seção do Notebook

```markdown
## Pergunta de Pesquisa
```

Escrever claramente a pergunta.

---

```python
# Código
```

Executar apenas o necessário para responder à pergunta.

---

```markdown
### Interpretação
```

Descrever o que foi encontrado.

---

```markdown
### Conclusão
```

Explicar como esse resultado contribui para responder ao objetivo geral do projeto.

---

# Regra de Ouro

Nem todo código interessante merece entrar no notebook.

Todo código deve responder uma pergunta de pesquisa.

Caso contrário, ele é apenas uma exploração técnica.

---

# Visão Geral do Projeto

```text
                Objetivo Geral
                      │
                      ▼
          Conhecer a estrutura da base
                      │
                      ▼
      Entender como o consumo está distribuído
                      │
                      ▼
      Identificar padrões espaciais e temporais
                      │
                      ▼
        Construir indicadores energéticos
                      │
                      ▼
      Comparar regiões de Santa Catarina
                      │
                      ▼
      Destacar a Grande Florianópolis
                      │
                      ▼
 Integrar dados econômicos e tecnológicos
                      │
                      ▼
 Levantar hipóteses sobre IA, Economia Digital
        e Infraestrutura para Data Centers
```

---

# Lembrete Final

Este projeto não é apenas uma análise do mercado de energia.

É uma investigação sobre como a infraestrutura energética pode revelar padrões associados ao desenvolvimento econômico, tecnológico e digital de Santa Catarina.

A energia é o ponto de partida.

A Ciência de Dados é a ferramenta.

A pergunta de pesquisa é o guia.


# Perguntas que surgirem durante a investigação

- Por que Joinville possui muito mais registros que outros municípios?
- O mercado livre cresce mais nas cidades industriais?
- Florianópolis consome menos energia industrial que Blumenau?
- Existe relação entre PIB municipal e consumo?
- Municípios com polos tecnológicos apresentam perfis energéticos diferentes?
