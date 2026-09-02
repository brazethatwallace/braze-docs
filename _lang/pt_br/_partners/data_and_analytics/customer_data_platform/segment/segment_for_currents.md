---
nav_title: Segment or segmento para Currents
article_title: Segment or segmento para Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Este artigo de referência descreve a parceria entre o Braze Currents e a Segment or segmento, uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment or segmento para Currents {#segment-for-currents}

> A [Segment](https://segment.com) é uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente que ajuda você a coletar, limpar e ativar os dados de seus clientes. Este artigo de referência fornecerá uma visão geral da conexão entre o Braze Currents e a Segment e descreverá os requisitos e processos para a implementação e o uso adequados.

A integração da Braze com a Segment or segmento permite que você utilize o Braze Currents para exportar seus eventos da Braze para a Segment or segmento, a fim de gerar análises de dados mais detalhadas sobre conversões, retenção e uso do produto.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Segment | É necessário ter uma [conta da Segment](https://app.segment.com/login) para aproveitar essa parceria. |
| Destino da Braze | Você já deve ter [configurado a Braze como um destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) na sua integração com a Segment.<br><br>Isso inclui fornecer o data center correto da Braze e a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional nas suas [configurações de conexão]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment#connection-settings). |
| Currents | Para exportar dados de volta para a Segment or segmento, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Obter a chave de gravação da Segment or segmento {#step-1-obtain-segment-write-key}

No dashboard da Segment or segmento, selecione sua fonte da Segment or segmento. Em seguida, acesse **Settings > API or interface de programação do aplicativo (API) keys**. Aqui você encontrará a **Segment or segmento Write Key**.

{% alert warning %}
É importante manter sua chave de gravação da Segment or segmento atualizada. Se as credenciais do conector expirarem, ele deixará de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

### Etapa 2: Criar um novo conector Currents {#step-2-create-a-new-currents-connector}

1. Na Braze, navegue até **Integrações de parceiros** > **Exportação de dados**.
2. Clique em **+ Create New Current** > **Segment Data Export**.
3. Em seguida, forneça o nome da integração, e-mail de contato, chave de gravação da Segment or segmento e região da Segment or segmento.

![A página Segment Currents na Braze. Aqui você pode encontrar campos para nome da integração, e-mail de contato, região da Segment e chave de API.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Etapa 3: Exportar eventos de engajamento com mensagens {#step-3-export-message-engagement-events}

Em seguida, selecione os eventos de engajamento com mensagens que você gostaria de exportar. Consulte a tabela de eventos e propriedades de exportação listada a seguir. Todos os eventos enviados para a Segment or segmento incluirão o `external_user_id` do usuário como `userId` e o `braze_id` do usuário como `anonymousId`.

Lembre-se de que a Braze só envia dados de eventos para usuários sem um `external_user_id` se a opção **Include events from anonymous users** estiver marcada.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Anonymous user export' %}

![Lista de todos os eventos de engajamento com mensagens disponíveis na página Segment Currents na Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Por fim, selecione **Launch Current**.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

Para saber mais, visite a [documentação](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) da Segment.

## Como atualizar seu Current {#updating-your-current}

{% multi_lang_include currents/updating_currents.md %}

## Eventos Currents compatíveis {#supported-currents-events}

A Braze suporta a exportação dos seguintes eventos para a Segment or segmento:

- [Eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Para a estrutura da carga útil de cada evento, selecione a guia **Segment or segmento** no [glossário de eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) e no [glossário de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).