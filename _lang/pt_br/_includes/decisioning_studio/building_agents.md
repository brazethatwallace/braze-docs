# Criação de agentes de decisão de IA {#building-ai-decisioning-agents}

> Saiba como criar um agente para o BrazeAI Decisioning Studio™, para que você possa automatizar a experimentação personalizada e otimizar resultados como conversões, retenção ou receita, sem testes A/B manuais.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## Sobre agentes {#about-agents}

Um agente de decisão de IA é uma configuração personalizada para o mecanismo de decisão do BrazeAI<sup>TM</sup>, feita sob medida para atender a uma meta comercial específica.

Por exemplo, você pode criar um agente de recompra para aumentar as conversões de acompanhamento após uma venda inicial. Você define o público e a mensagem na Braze, enquanto seus agentes de decisão executam experimentos diários e testam automaticamente diferentes combinações de ofertas de produtos, horários de envio de mensagens e frequência para cada cliente. Com o tempo, o BrazeAI<sup>TM</sup> aprende o que funciona melhor e orquestra envios personalizados por meio da Braze para maximizar as taxas de recompra.

Para criar um bom agente, você vai:

- Escolher uma métrica de sucesso para o BrazeAI<sup>TM</sup> otimizar, como receita, conversões ou ARPU.
- Definir quais dimensões testar, como oferta, linha de assunto, criativo, canal ou horário de envio.
- Selecionar as opções para cada dimensão, como e-mail versus SMS, ou frequência diária versus semanal.

![Diagrama de exemplo de um agente do Decisioning Studio para e-mails de indicação.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Exemplos de agentes {#sample-agents}

Aqui estão alguns exemplos de agentes que você pode criar com o BrazeAI Decisioning Studio™. Seus agentes de decisão de IA aprenderão com cada interação do cliente e aplicarão esses insights nas ações do dia seguinte.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Criação de um agente {#building-an-agent}

### Pré-requisitos {#prerequisites}

Antes de criar um agente, você precisará [integrar o BrazeAI Decisioning Studio™]({{site.baseurl}}/developer_guide/decisioning_studio/integration).

### Etapa 1: Entre em contato com o AI Expert Services {#step-1-contact-ai-expert-services}

A equipe do AI Expert Services trabalhará em estreita colaboração com você para definir o escopo, projetar e criar seu agente de decisão. Se ainda não fez isso, [entre em contato conosco](https://www.braze.com/get-started/) para começar.

Vocês completarão as etapas a seguir juntos para criar um agente personalizado que seja ideal para você.

### Etapa 2: Projete seu agente {#step-2-design-your-agent}

Junto com a equipe do AI Expert Services, você vai definir:

- um público-alvo,
- a métrica comercial a ser otimizada,
- as ações para o agente de decisão do BrazeAI<sup>TM</sup> e
- quaisquer dados primários de clientes que o agente deve alavancar para impulsionar seus resultados de negócios.

Com o design em mãos, a equipe trabalhará com você para identificar e concluir quaisquer requisitos de integração adicionais.

### Etapa 3: Configure sua plataforma de entrega {#step-3-set-up-your-delivery-platform}

Em seguida, a equipe do AI Expert Service ajudará você a configurar sua plataforma de engajamento com clientes. Embora o Decisioning Studio funcione melhor com a Braze, diversas outras plataformas são compatíveis — entre em contato com sua equipe do AI Expert Service para obter recursos adicionais.

{% tabs local %}
{% tab Braze %}
Para configurar a Braze:

1. Crie uma [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) ou um [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=api-triggered%20delivery#step-12-determine-your-canvas-entry-schedule). O BrazeAI Decisioning Studio™ usará esse método de entrega para enviar eventos de ativação personalizados 1:1 aos usuários do seu público definido.
2. Certifique-se de não incluir um [grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) da Braze, para que o BrazeAI<sup>TM</sup> possa atuar como o grupo de controle dedicado.
3. Dependendo das suas dimensões, você pode configurar Liquid tags no seu conteúdo criativo para preencher dinamicamente suas mensagens com recomendações do BrazeAI<sup>TM</sup>. O BrazeAI<sup>TM</sup> passará conteúdo específico do cliente para as Liquid tags nos seus modelos usando a API da Braze.
{% endtab %}
{% endtabs %}

### Etapa 4: Lance e monitore {#step-4-launch-and-monitor}

Após lançar seu agente, a equipe do AI Expert Services continuará monitorando e ajustando-o de acordo com o design combinado. Eles também ajudarão você a fazer quaisquer ajustes, expansões ou modificações no agente, se necessário.