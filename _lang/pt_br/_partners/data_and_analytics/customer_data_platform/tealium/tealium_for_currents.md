---
nav_title: Tealium para Currents
article_title: Tealium para Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Este artigo de referência descreve a parceria entre o Braze Currents e a Tealium, uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium para Currents {#tealium-for-currents}

> A [Tealium](https://www.tealium.com) é uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente que coleta e encaminha informações de várias fontes para uma variedade de outros locais em sua pilha de marketing.

A integração da Braze com a Tealium permite que você controle perfeitamente o fluxo de informações entre os dois sistemas. Com o Currents, você também pode conectar dados à Tealium para torná-los acionáveis em todo o growth stack.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Tealium EventStream ou Tealium AudienceStream | É necessário ter uma [conta da Tealium](https://my.tealiumiq.com/) para usar essa parceria. |
| Currents | Para exportar dados de volta para a Tealium, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
| URL da Tealium | Pode ser obtida navegando até o dashboard da Tealium e copiando a URL de ingestão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar uma fonte de dados para a Braze na Tealium {#step-1-create-a-data-source-for-braze-within-tealium}

As instruções para a criação de uma fonte de dados podem ser encontradas no site da [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Quando concluído, a Tealium fornecerá uma URL da fonte de dados para copiar, que você usará na próxima etapa.

### Etapa 2: Criar um Current {#step-2-create-current}

Na Braze, navegue até **Currents** > **+ Create Current** > **Tealium Export**. Forneça um nome de integração, e-mail de contato e a URL da Tealium.

Em seguida, selecione o que deseja rastrear na lista de eventos disponíveis. Por padrão, todos os eventos enviados à Tealium incluem o `external_user_id` do usuário. No entanto, é possível marcar a caixa de seleção **Include events from anonymous users** para também enviar eventos que não tenham um `external_user_id` para a Tealium.

Depois de configurar sua integração, selecione **Launch Current**.

{% alert important %}
É importante manter a URL da Tealium atualizada. Se a URL do seu conector estiver incorreta, a Braze não conseguirá enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

## Detalhes da integração {#integration-details}

A Braze oferece suporte à exportação de todos os dados listados nos [glossários de eventos do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) (incluindo todas as propriedades dos eventos de [engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) e de [comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)) para a Tealium.

A estrutura da carga útil para dados exportados é a mesma que a estrutura da carga útil para conectores HTTP personalizados, que pode ser visualizada no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).