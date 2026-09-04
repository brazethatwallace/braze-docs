---
nav_title: Projetar agentes de decisão
article_title: Projetar agentes de decisão
page_order: 1
page_type: reference
description: "Este artigo de referência aborda conceitos-chave e práticas recomendadas para projetar e configurar seu agente de decisão."
---

# Projetar agentes de decisão {#design-decisioning-agents}

> Este artigo de referência aborda conceitos-chave e práticas recomendadas para projetar e configurar seu agente de decisão.

## Sobre agentes de decisão {#about-decisioning-agents}

Projetar seu agente de decisão é a primeira etapa na configuração do Decisioning Studio. Para que o agente de decisão consiga tomar decisões, você precisa definir qual resultado deseja maximizar e quais ações o agente pode realizar para isso.

### Conceitos-chave {#key-concepts}

Os termos a seguir são referenciados ao longo do guia do Decisioning Studio.

| Termo | Definição |
| --- | --- |
| **Agente de decisão** | Um agente de decisão é uma configuração personalizada do BrazeAI Decisioning Studio™ feita sob medida para atender a uma meta comercial específica. Ele é definido pela métrica de sucesso, dimensões e opções que você escolhe. |
| **Métrica de sucesso** | A métrica de negócio específica que você deseja otimizar, como receita, conversões ou receita média por usuário (ARPU). Essa é a métrica que o agente de decisão buscará maximizar por meio de suas ações. |
| **Dimensões** | As dimensões podem ser entendidas como os *tipos de alavancas* que o agente de decisão pode acionar para maximizar a métrica de sucesso. Dimensões típicas incluem oferta, linha de assunto, criativo, canal ou horário de envio. |
| **Banco de ações** | O banco de ações define as *opções específicas* às quais o agente de decisão tem acesso para cada "alavanca" de dimensão. Por exemplo, para uma dimensão de canal, você define os canais específicos aos quais o agente de decisão tem acesso. Para uma dimensão de oferta, você define as ofertas específicas que o agente de decisão pode testar. |
| **Restrições** | Em geral, o agente de decisão pode realizar qualquer combinação de ações que você colocar no banco de ações. No entanto, você também pode definir restrições para limitar as ações do agente de decisão e respeitar regras de negócio críticas. Por exemplo, isso pode ser impedir que uma oferta específica seja selecionada para clientes em uma região não elegível, ou definir um orçamento máximo para o agente de decisão gastar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceitos-chave" }

![Visão geral de alto nível de um agente de decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
O agente de decisão só pode realizar ações que *você* configurar e adicionar ao banco de ações. Isso significa que todas as ações possíveis são definidas pelas combinações do que você colocar no banco de ações.
{% endalert %}

## Como projetar seu agente de decisão {#how-to-design-your-decisioning-agent}

Ao configurar um agente de decisão, você precisará pensar em quatro elementos principais de design:

### O "objetivo": defina sua métrica de sucesso {#the-goal-define-your-success-metric}

*Qual resultado você quer que o agente maximize?*

Sua métrica de sucesso é o resultado de negócio que o agente vai otimizar. Ela deve estar diretamente alinhada com seus objetivos de negócio — não métricas intermediárias como cliques ou aberturas, mas resultados reais de negócio como receita, conversões, ARPU ou lifetime value do cliente.

### O "quem": selecione seu público {#the-who-select-your-audience}

*Quem o agente de decisão vai engajar?*

Defina o público que seu agente vai atender. Pode ser todos os clientes, um Segment específico (como membros de um programa de fidelidade) ou clientes em uma etapa específica do ciclo de vida (como compradores recentes ou assinantes em risco).

### O "quê": configure seu banco de ações {#the-what-configure-your-action-bank}

*Quais opções o agente pode escolher para impulsionar o resultado?*

O banco de ações define todas as alavancas que o agente pode acionar: as dimensões (como canal, oferta, horário e frequência) e as opções específicas dentro de cada dimensão. O agente experimenta diferentes combinações dessas opções para descobrir o que funciona melhor para cada cliente.

### O "como": configure suas restrições {#the-how-configure-your-constraints}

*Quais regras o agente deve seguir?*

Restrições são as regras que o agente deve seguir. Isso pode ser impedir que uma oferta específica seja selecionada para clientes em uma região não elegível, ou definir um orçamento máximo para o agente de decisão gastar.

## Práticas recomendadas e exemplos {#best-practices-and-examples}

Para maximizar o impacto do seu agente de decisão, você deve:

- Escolher uma métrica de sucesso que esteja diretamente alinhada com suas metas e objetivos de negócio, como receita, conversões ou ARPU.
- Focar nas dimensões, ou "alavancas" a testar, como oferta, linha de assunto, criativo, canal ou horário de envio, que têm maior probabilidade de causar um impacto significativo na métrica de sucesso.
- Selecionar as opções para cada dimensão, como e-mail versus SMS, ou frequência diária versus semanal, que têm maior probabilidade de causar um impacto significativo na métrica de sucesso.

Alguns exemplos de agentes de decisão que você pode criar são:

{% tabs %}
{% tab Agente de recompra %}
Você pode criar um agente de recompra para aumentar as conversões de acompanhamento após uma venda inicial:

- Defina o público e a mensagem na Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes combinações de ofertas de produtos, horários de envio e frequência para cada cliente
- Com o tempo, o BrazeAI<sup>TM</sup> aprende o que funciona melhor para cada cliente
- Orquestra envios personalizados pela Braze para maximizar as taxas de recompra
{% endtab %}
{% tab Agente de cross-sell ou upsell %}
Você pode criar um agente de cross-sell ou upsell para maximizar a receita média por usuário (ARPU) de assinaturas de internet:

- Defina o público e a mensagem na Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes combinações de mensagens, horários de envio, descontos e ofertas de planos para cada cliente
- O BrazeAI<sup>TM</sup> aprende quais clientes são suscetíveis a ofertas de salto de plano e quais precisam de descontos ou outros incentivos para fazer upgrade
- Orquestra envios personalizados pela Braze para maximizar o ARPU
{% endtab %}
{% tab Agente de renovação e retenção %}
Você pode criar um agente de renovação e retenção para garantir renovações de contrato, maximizando tanto a duração do contrato quanto o valor presente líquido (VPL):

- Defina o público e a mensagem na Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes ofertas de renovação para cada cliente
- O BrazeAI<sup>TM</sup> identifica clientes que são menos sensíveis a preço e precisam de descontos menos significativos para renovar
- Orquestra envios personalizados pela Braze para maximizar renovações de contrato e VPL
{% endtab %}
{% tab Agente de reconquista %}
Você pode criar um agente de reconquista para aumentar a reativação incentivando ex-assinantes a se reinscreverem:

- Defina o público e a mensagem na Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando milhares de variáveis ao mesmo tempo, incluindo criativo, mensagem, canal e cadência
- O BrazeAI<sup>TM</sup> descobre a melhor combinação para cada cliente individual
- Orquestra envios personalizados pela Braze para maximizar as taxas de reativação
{% endtab %}
{% tab Agente de indicação %}
Você pode criar um agente de indicação para maximizar novas contas abertas por meio de indicações de cartão de crédito empresarial de clientes existentes:

- Defina o público e a mensagem na Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes e-mails, criativos, horários de envio e ofertas de cartão de crédito para cada cliente
- O BrazeAI<sup>TM</sup> determina a combinação ideal para clientes específicos
- Orquestra envios personalizados pela Braze para maximizar conversões de indicação
{% endtab %}
{% tab Agente de nutrição e conversão de leads %}
Você pode criar um agente de nutrição e conversão de leads para gerar receita incremental e pagar o valor certo por cada cliente:

- Defina o público e a mensagem na Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes segmentos de clientes, metodologia de lances, níveis de lance e criativos
- O BrazeAI<sup>TM</sup> utiliza dados primários robustos para otimizar o desempenho de anúncios pagos à medida que as políticas de privacidade mudam
- Orquestra envios personalizados pela Braze para maximizar a receita enquanto otimiza o custo por cliente
{% endtab %}
{% tab Agente de fidelidade e engajamento %}
Você pode criar um agente de fidelidade e engajamento para maximizar compras de novos inscritos em um programa de fidelidade:

- Defina o público e a mensagem na Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes ofertas por e-mail, horários de envio e frequências para cada cliente
- O BrazeAI<sup>TM</sup> aprende o que funciona melhor para cada novo inscrito no programa de fidelidade
- Orquestra envios personalizados pela Braze para maximizar as taxas de compra e recompra
{% endtab %}
{% endtabs %}

## Próximas etapas {#next-steps}

Pronto para criar seu próprio agente de decisão? Consulte [Primeiros passos com o Decisioning Studio]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) para um guia que orienta você na conexão de fontes de dados, configuração da orquestração, design do seu agente e lançamento em produção.