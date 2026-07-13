---
nav_title: Treasure Data para Currents
article_title: Treasure Data para Currents
description: "Este artigo de referência descreve a parceria entre o Braze Currents e o Treasure Data, uma plataforma de dados do cliente corporativo que permite que você escreva os resultados do trabalho diretamente na Braze."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data para Currents {#treasure-data-for-currents}

> O [Treasure Data](https://www.treasuredata.com/) é uma plataforma de dados do cliente (CDP) que coleta e encaminha informações de várias fontes para uma variedade de outros locais na sua pilha de marketing.

A integração entre a Braze e o Treasure Data permite que você controle perfeitamente o fluxo de informações entre os dois sistemas. Com o Currents, você também pode conectar dados ao Treasure Data para torná-los acionáveis em toda a growth stack.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Treasure Data | É necessário ter uma [conta do Treasure Data](https://console.treasuredata.com/users/sign_in) para aproveitar essa parceria. |
| Currents | Para exportar dados de volta para o Treasure Data, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado na sua conta. |
| URL do Treasure Data | Pode ser obtido navegando até o dashboard do Treasure Data e copiando o URL de ingestão.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert note %}
O Treasure Data registra cada evento em lotes. Para saber mais sobre como consultar o Treasure Data para obter contagens de eventos, consulte [Consulta de dados](https://docs.treasuredata.com/articles/int/braze-currents-import-integration/a/h2__592056238).<br><br>Se você deseja integrar com o novo conector de streaming do Treasure Data para a Braze, consulte as etapas de configuração detalhadas em [Integração de importação de streaming do Braze Currents](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration/q/braze/qid/72364/qp/4). Em caso de dúvidas sobre a integração ou a configuração na Braze, entre em contato com a equipe da sua conta Braze.
{% endalert %}

## Integração {#integration}

A abordagem recomendada para se conectar ao Treasure Data é pela API de Postback. Esse método não requer um conector padrão, e os dados podem ser recebidos por uma abordagem de push. Todos os eventos enviados em um lote de dados estão dentro de um campo de uma linha em um array JSON, que precisa ser analisado para obter os dados necessários.

{% alert important %}
Atualmente, a ingestão no Treasure Data por meio do coletor de eventos não ocorre em tempo real e pode levar até cinco minutos.
{% endalert %}

### Etapa 1: configure a API de Postback do Treasure Data com a Braze {#step-1-setup-treasure-data-postback-api-with-braze}

As instruções para criar uma API de Postback podem ser encontradas no [site do Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API). A Braze enviará diretamente os eventos atualizados para o Treasure Data em tempo real, com exceção da ingestão por meio do coletor de eventos. Quando concluído, o Treasure Data fornecerá um URL da fonte de dados para copiar e usar na próxima etapa.

### Etapa 2: crie um Current {#step-2-create-current}

Na Braze, navegue até **Currents** > **+ Create Current** > **Treasure Data Export**. Forneça um nome de integração, e-mail de contato e o URL do Treasure Data. Em seguida, selecione o que deseja rastrear na lista de eventos disponíveis e clique em **Launch Current**.

Todos os eventos enviados ao Treasure Data incluirão o `external_user_id` do usuário. No momento, a Braze não envia dados de eventos ao Treasure Data para usuários que não definiram o `external_user_id`.

{% alert important %}
Mantenha o URL do Treasure Data atualizado. Se o URL do seu conector estiver incorreto, a Braze não poderá enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

#### Exemplo de valor de campo de evento {#example-event-field-value}
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### Exemplo de visualização ingerida {#example-of-the-ingested-view}

![4]{: style="max-width:70%;"}

## Detalhes da integração {#integration-details}

A Braze oferece suporte à exportação de todos os dados listados nos [glossários de eventos do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) (incluindo todas as propriedades nos eventos de [engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) e de [comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)) para o Treasure Data.

A estrutura de carga útil para dados exportados é a mesma que a estrutura de carga útil para conectores HTTP personalizados, que pode ser visualizada no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}