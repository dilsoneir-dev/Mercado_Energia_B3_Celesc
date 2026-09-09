# Roadmap do Projeto — Energy Market of Santa Catarina

> Documento vivo para orientar a evolução da pesquisa.

---

# Objetivo Geral

Construir um estudo sobre o mercado de energia elétrica de Santa Catarina utilizando dados públicos da CELESC como base para pesquisas relacionadas à Infraestrutura Energética, Economia Digital, Inteligência Artificial e Data Centers.

---

# Fase 1 — Entendimento dos Dados

Objetivo:
Conhecer profundamente a estrutura da base antes de realizar qualquer análise estatística ou visual.

## Etapa 1.1 — Organização do projeto
- [x] Estrutura do repositório
- [x] README
- [x] Organização das pastas
- [x] Ambiente Python
- [x] Git e GitHub

---

## Etapa 1.2 — Aba "Consumo MWh"

Status: Em andamento

Objetivos:

- compreender a estrutura da planilha
- identificar todas as variáveis
- entender a granularidade dos registros
- identificar municípios
- identificar classes de consumo
- identificar consumidores livres e cativos
- compreender o significado de agência, núcleo e unidade

Conclusão esperada:

"Saber exatamente o que representa cada linha do dataset."

---

## Etapa 1.3 — Aba "Número de UC"

Próximo passo.

Objetivos:

- compreender sua estrutura
- comparar com a aba Consumo MWh
- identificar como as duas bases se relacionam
- verificar se podem ser integradas futuramente

---

# Fase 2 — Exploração dos Dados (EDA)

Objetivo:

Responder perguntas utilizando estatísticas descritivas.

Exemplos:

- municípios com maior consumo
- municípios com menor consumo
- consumo por classe
- consumo por tipo de consumidor
- evolução temporal
- crescimento ao longo dos anos
- comparação entre regiões

Produtos esperados:

- tabelas
- gráficos
- mapas
- indicadores

---

# Fase 3 — Conhecimento do Domínio

Objetivo:

Entender o contexto do setor elétrico para interpretar corretamente os resultados.

Temas de estudo:

## Mercado de energia

- consumidor livre
- consumidor cativo
- geração
- transmissão
- distribuição
- comercialização

---

## CELESC

Pesquisar:

- estrutura da empresa
- significado das agências
- significado dos núcleos
- organização operacional

---

## Santa Catarina

Pesquisar:

- economia
- polos industriais
- regiões
- inovação
- tecnologia
- infraestrutura

---

# Fase 4 — Integração com Outras Bases

Somente após dominar completamente a base principal.

Possíveis integrações:

- PIB municipal
- População
- IDH
- Empresas
- Setor industrial
- Ecossistema de inovação
- Startups
- Data Centers
- Infraestrutura digital

---

# Fase 5 — Pesquisa

Perguntas centrais

Como o consumo de energia se distribui em Santa Catarina?

Quais regiões concentram maior demanda?

Existe relação entre atividade econômica e consumo?

Há padrões compatíveis com polos tecnológicos?

Como esses indicadores podem apoiar estudos sobre Inteligência Artificial?

Como podem contribuir para pesquisas sobre Data Centers?

---

# Filosofia do Projeto

Este projeto não busca apenas analisar um conjunto de dados.

Busca compreender como a infraestrutura energética pode servir como indicador do desenvolvimento econômico e tecnológico de Santa Catarina.

O princípio será sempre:

Entender → Explorar → Contextualizar → Integrar → Pesquisar

Nunca o contrário.

# Nosso Método de Trabalho

Antes de escrever código, entender o problema.

Antes de criar gráficos, entender os dados.

Antes de buscar novas bases, dominar a base atual.

Antes de responder perguntas, aprender a formular boas perguntas.

Cada notebook representa uma etapa da investigação.

Cada documento registra o raciocínio desenvolvido.

O repositório deve contar a história da pesquisa, não apenas armazenar códigos.