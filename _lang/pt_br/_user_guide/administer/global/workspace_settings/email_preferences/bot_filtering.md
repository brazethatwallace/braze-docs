---
nav_title: Filtragem de bots para e-mails
article_title: Filtragem de bots para e-mails
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Este artigo fornece uma visão geral da filtragem de bots para e-mail."
---

# Filtragem de bots para e-mails {#bot-filtering-for-emails}

> Configure a filtragem de bots em suas [Preferências de e-mail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) para excluir todos os cliques suspeitos de máquinas ou bots. Um "clique de bot" em e-mail refere-se a um clique em hiperlinks em um e-mail gerado por um programa automatizado. Ao filtrar esses cliques de bots, você pode disparar intencionalmente e entregar mensagens para destinatários que estejam engajados.

{% alert important %}
A partir de 9 de julho de 2025, todos os novos espaços de trabalho criados terão a configuração de filtragem de bots ativada para gerar relatórios de cliques mais precisos na Braze.
{% endalert %}

## Sobre cliques de bots {#about-bot-clicks}

A Braze possui um sistema de detecção que utiliza múltiplas entradas para identificar cliques suspeitos de bots, também conhecidos como interações não humanas (NHI). Os cliques de bots podem distorcer suas métricas de engajamento de e-mail ao inflar artificialmente as taxas de cliques. Essa abordagem nos permite diferenciar entre interações humanas genuínas e atividades suspeitas de bots, mantendo a integridade das métricas e dos insights de engajamento de cliques.

## Métricas afetadas por cliques de bots {#metrics-affected-by-bot-clicks}

{% alert note %}
A filtragem de bots bloqueia ativamente cliques automatizados suspeitos para melhorar a precisão das suas métricas de engajamento. No entanto, scanners e bots evoluem continuamente ao longo do tempo, então a Braze não pode garantir a remoção de todas as interações não humanas.
{% endalert %}

As seguintes métricas da Braze podem ser afetadas por cliques de bots:

- Taxa de cliques total
- Taxa de cliques únicos
- Taxa de clique por abertura
- Taxa de conversão (se "Cliques na Campaign" for selecionado como evento de conversão)
- Mapa de calor
- Determinados filtros de Segment

Quando a filtragem de bots está ativada, cliques suspeitos de bots são excluídos dos dados de cliques. Os seguintes [recursos de inteligência da Braze]({{site.baseurl}}/user_guide/brazeai/intelligence_suite) podem refletir volumes menores relacionados a cliques como resultado:

- Seleção inteligente
- Canal inteligente
- Intelligent Timing
- Etapa de experimento
    - Jornada vencedora
    - Jornada personalizada
- Campaign
    - Variante vencedora
    - Variante personalizada
- Taxa real estimada de abertura

Os cancelamentos de inscrição provenientes de cliques suspeitos de bots não serão afetados. A Braze continuará processando todas as solicitações de cancelamento de inscrição normalmente. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Filtros de segmentação afetados pela filtragem de bots {#segmentation-filters-affected-by-bot-filtering}

Os seguintes [filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) podem ser afetados pela filtragem de bots para mensagens de e-mail:

- [Clicked/Opened Campaign or Canvas With Tag]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Clicked/Opened Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Clicked Alias in Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [Clicked Alias in Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Clicked Alias in Any Campaign or Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Last Engaged with Message]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [Intelligent Channel]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## Ativando a filtragem de bots {#turning-on-bot-filtering}

Acesse **Settings** > **Email Preferences**. Em seguida, selecione **Remove bot clicks**. Essa configuração é aplicada no nível do espaço de trabalho.

Quaisquer cliques suspeitos de bots só serão removidos após a ativação da configuração, e isso não se aplica retroativamente às métricas do seu espaço de trabalho.

![Configuração de filtragem de bots ativada em Email Preferences.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Se você ativar essa configuração e depois desativá-la, a Braze não poderá restaurar nenhuma atividade de bot previamente removida na sua análise de dados.
{% endalert %}

## Campos em eventos de clique de e-mail para Currents e Snowflake {#fields-in-email-click-events-for-currents-and-snowflake}

A Braze enviará os campos `is_suspected_bot_click` e `suspected_bot_click_reason` no Currents e no Snowflake para um evento de clique de e-mail.

| Campo | Tipo de dados | Descrição |
| `is_suspected_bot_click` | Boolean | Indica que este é um clique suspeito de bot. Será enviado como valores nulos até que você ative a configuração de espaço de trabalho **Remover cliques de bots**. Essa abordagem permite que você entenda programaticamente quando a filtragem de cliques suspeitos de bots começou no seu espaço de trabalho, para que possa comparar com precisão os dados no Currents e no Snowflake. |
| `suspected_bot_click_reason` | Array | Indica o motivo pelo qual este é um clique suspeito de bot. Será preenchido com valores, como `user_agent` e `ip_address`, mesmo que a configuração de espaço de trabalho de filtragem de bots esteja desativada. Este campo pode fornecer insights sobre o impacto potencial de ativar essa configuração, comparando o número de cliques provenientes de cliques suspeitos de bots com interações humanas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos em eventos de clique de e-mail para Currents e Snowflake" }

## Perguntas frequentes {#frequently-asked-questions}

### Como a filtragem de bots vai impactar o desempenho da minha campanha? {#how-will-bot-filtering-impact-my-campaigns-performance}

Isso não vai impactar as métricas de nenhuma campanha anterior já enviada. Quando a filtragem de bots é ativada no seu espaço de trabalho, a Braze começa a filtrar cliques suspeitos de bots de todos os cliques. Você pode notar uma queda nas taxas de cliques, mas a taxa de cliques será uma representação mais precisa do engajamento dos seus usuários com suas mensagens de e-mail.

### A filtragem de bots vai impedir que bots que clicam no link de cancelamento de inscrição da Braze cancelem a inscrição? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

Não. Todas as solicitações de cancelamento de inscrição continuarão sendo processadas.

### As aberturas por máquina são consideradas na filtragem de cliques de bots? {#are-machine-opens-considered-in-the-bot-click-filtering}

Não.