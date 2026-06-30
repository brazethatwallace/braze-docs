---
nav_title: FAQ
article_title: FAQ do Decisioning Studio
page_order: 8
page_type: FAQ
description: "Esta página fornece respostas para perguntas frequentes sobre o Decisioning Studio."
---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre o Decisioning Studio.

## O que é um agente de decisão? {#what-is-a-decisioning-agent}

Um agente de decisão é uma configuração personalizada para o BrazeAI Decisioning Studio™ feita sob medida para atender a uma meta comercial específica. Ele é definido pela métrica de sucesso, dimensões e opções que você escolher. O agente de decisão descobre automaticamente a ação ideal para cada cliente a fim de maximizar a métrica comercial escolhida.

### Quais métricas posso otimizar? {#what-metrics-can-i-optimize-for}

Você pode otimizar qualquer métrica comercial que esteja alinhada com suas metas, como receita, conversões, receita média por usuário (ARPU), lifetime value do cliente (CLV), lucro, renovações de contrato ou qualquer outro KPI comercial.

### Quais são as dimensões no Decisioning Studio? {#what-are-dimensions-in-decisioning-studio}

Dimensões podem ser pensadas como os *tipos de alavancas* que o agente de decisão pode acionar para maximizar a métrica de sucesso. Dimensões típicas incluem oferta, linha de assunto, criativo, canal ou horário de envio.

### O que é um banco de ações? {#what-is-an-action-bank}

O banco de ações define as *opções específicas* às quais o agente de decisão tem acesso para cada "alavanca" de dimensão. Por exemplo, para uma dimensão de canal, você define os canais específicos aos quais o agente de decisão tem acesso. Para uma dimensão de oferta, você define as ofertas específicas que o agente de decisão pode testar.

### O agente de decisão pode tomar ações que eu não configurei? {#can-the-decisioning-agent-take-actions-i-havent-configured}

Não. O agente de decisão só pode tomar ações que você configurar e adicionar ao banco de ações. Isso significa que todas as ações possíveis são definidas pelas combinações do que você coloca no banco de ações.

### O que são restrições? {#what-are-constraints}

Restrições limitam as ações do agente de decisão para respeitar regras de negócios críticas. Por exemplo, isso pode impedir que uma oferta específica seja selecionada para clientes em uma geografia não elegível, ou definir um orçamento máximo para o agente de decisão gastar.

### Qual é a diferença entre Decisioning Studio Go e Decisioning Studio Pro? {#what-is-the-difference-between-decisioning-studio-go-and-decisioning-studio-pro}

O Decisioning Studio Pro inclui suporte de AI Decisioning Services da equipe de ciência de dados da Braze, que ajudará você a projetar e configurar seu agente para maximizar seus resultados de negócios. Para saber mais, consulte [Decisioning Studio Go versus Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio#decisioning-studio-go-vs-decisioning-studio-pro).