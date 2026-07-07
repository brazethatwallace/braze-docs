---
nav_title: Começar
article_title: Primeiros passos com o Decisioning Studio
layout: dev_guide
guide_top_header: "Primeiros passos com o Decisioning Studio"
guide_top_text: ""
page_order: 0
search_rank: 2
page_type: landing
description: "Esta seção apresenta uma introdução ao Decisioning Studio e como você pode usá-lo para projetar e implantar agentes de decisão que otimizam qualquer métrica de negócios."

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Projete seu agente
    link: /docs/user_guide/brazeai/decisioning_studio/design_agents
    image: /assets/img/braze_icons/settings-01.svg
  - name: Prepare seus dados
    link: /docs/user_guide/brazeai/decisioning_studio/prepare_data
    image: /assets/img/braze_icons/database-01.svg
  - name: Defina seu público
    link: /docs/user_guide/brazeai/decisioning_studio/audience
    image: /assets/img/braze_icons/users-01.svg
  - name: Configure a orquestração
    link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "Recursos adicionais"
guide_menu_list:
  - name: Sobre o Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio
    image: /assets/img/braze_icons/info-circle.svg
  - name: Perguntas frequentes sobre o Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

O BrazeAI Decisioning Studio™ permite que você projete e implante agentes de decisão que otimizam qualquer métrica de negócios.

Esta referência oferece uma visão geral das etapas envolvidas na configuração do Decisioning Studio, incluindo o design do seu agente, a configuração e conexão de fontes de dados, a configuração da orquestração e a avaliação de desempenho.

## Principais decisões de design {#key-design-decisions}

Trabalhe com a equipe de AI Decisioning Services para tomar as seguintes decisões:

| Decisão | Descrição | Exemplos |
|---------|-----------|----------|
| **Métrica de sucesso** | O que o agente vai maximizar ao personalizar o engajamento do cliente? | Receita, LTV, ARPU, conversões, retenção |
| **Público** | Para quem o agente do Decisioning Studio tomará decisões de engajamento do cliente? | Todos os clientes, membros de fidelidade, assinantes em risco |
| **Grupos de experimento** | Como os testes controlados randomizados do Decisioning Studio devem ser estruturados? | Decisioning Studio, Controle aleatório, BAU, Holdout |
| **Dimensões** | Quais decisões o agente deve personalizar? | Horário do dia, linha de assunto, frequência, ofertas, canal |
| **Opções** | Quais opções o agente tem para trabalhar? | Modelos específicos, ofertas, períodos |
| **Restrições** | Quais decisões o agente nunca deve tomar? | Restrições geográficas, limites de orçamento, regras de elegibilidade |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Principais decisões de design" }

Cada uma dessas decisões tem implicações sobre quanto incremento adicional o agente pode gerar e com que rapidez. Nossa equipe de AI Decisioning Services trabalhará com você para projetar um agente que gere o máximo de valor, respeitando todas as suas regras de negócios.

![Diagrama mostrando como métricas de sucesso, público, grupos de experimento, dimensões, opções e restrições alimentam o design de um agente do Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Capacidades do Decisioning Studio {#decisioning-studio-capabilities}

| Capacidade | Informações |
|------------|-------------|
| **Qualquer métrica de sucesso** | Otimize para receita, conversões, ARPU, LTV ou qualquer KPI de negócios |
| **Dimensões ilimitadas** | Personalize por oferta, canal, timing, frequência, criativo e muito mais |
| **Qualquer CEP** | Integrações nativas com a Braze, Salesforce Marketing Cloud ou integrações personalizadas para qualquer plataforma |
| **AI Decisioning Services** | Suporte dedicado da equipe de ciência de dados da Braze |
| **Design avançado de experimentos** | Grupos de tratamento e holdouts totalmente personalizáveis |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Capacidades do Decisioning Studio" }

## Práticas recomendadas {#best-practices}

Algumas práticas recomendadas para projetar agentes do Decisioning Studio:

- **Maximize a riqueza dos dados:** quanto mais informações os agentes tiverem sobre seus clientes, melhor será o desempenho deles.
- **Diversifique as ações:** quanto mais diverso for o conjunto de ações que o agente pode realizar, mais ele poderá personalizar sua estratégia para cada usuário.
- **Minimize as restrições:** quanto menos restrições nos seus agentes, melhor. As restrições devem ser projetadas para respeitar as regras de negócios, ao mesmo tempo em que liberam ao máximo a experimentação conduzida pelo agente.