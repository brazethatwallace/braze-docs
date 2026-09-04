---
nav_title: Melhores práticas
hidden: true
---

# Melhores práticas para ciclo de vida do usuário e identificadores {#user-lifecycle-and-identifiers-best-practices}

## Coleta de dados {#data-collection}

Saiba mais sobre como a Braze coleta dados:
- [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [Melhores práticas de coleta de dados]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Identificadores da Braze {#braze-identifiers}

- `braze_id`: Um identificador atribuído pela Braze que é imutável e associado a um usuário específico quando criado em nosso banco de dados.
- `external_id`: Um identificador atribuído pelo cliente, geralmente um UUID. Recomendamos que os clientes atribuam o `external_id` quando o usuário puder ser identificado de forma única. Depois que um usuário é identificado, ele não pode ser revertido para anônimo.
- `user_alias`: Um identificador alternativo exclusivo que o cliente pode atribuir como forma de referenciar o usuário por um ID antes da atribuição de um `external_id`. Os aliases de usuário podem ser posteriormente mesclados com outros aliases ou um `external_id` quando um se tornar disponível por meio do endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) da Braze.
    - No endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), o campo `merge_behavior` pode ser usado para especificar quais dados do perfil de alias de usuário devem ser mantidos no perfil de usuário conhecido.
    - Observe que, para que o alias de usuário seja um perfil enviável, ainda é necessário incluir e-mail e/ou telefone como atributo padrão no perfil.
- `device_id`: Um identificador específico do dispositivo gerado automaticamente. Um perfil de usuário pode ter vários `device_ids` associados a ele. Por exemplo, um usuário que fez login em sua conta no computador do trabalho, no computador de casa, no tablet e no app iOS teria 4 `device_ids` associados ao seu perfil.
- Endereço de e-mail e número de telefone:
    - Aceitos como identificador no endpoint de rastreamento de usuários da Braze.
    - Ao usar o endereço de e-mail ou o número de telefone como identificador em uma solicitação, há três resultados possíveis:
        1. Se um usuário com esse e-mail/telefone não existir na Braze, um perfil somente com e-mail/telefone será criado e todos os dados da solicitação serão adicionados ao perfil.
        2. Se um perfil com esse e-mail/telefone já existir na Braze, ele será atualizado para incluir todos os dados enviados na solicitação.
        3. Em um caso de uso com mais de um perfil com esse e-mail/telefone, o perfil atualizado mais recentemente terá prioridade.
    - Observe que, se um perfil somente com e-mail/telefone existir e, em seguida, um perfil identificado com o mesmo e-mail/telefone for criado (como outro perfil com o mesmo endereço de e-mail E um ID externo), a Braze criará um segundo perfil. As atualizações subsequentes serão direcionadas ao perfil com o ID externo.
        - Os dois perfis podem ser mesclados usando o endpoint [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) da Braze

## Lidando com usuários anônimos {#handling-anonymous-users}

Para um caso de uso em que você precisa criar ou atualizar um perfil de usuário na Braze sem ter acesso a um `external_id`, outro identificador como um endereço de e-mail ou número de telefone pode ser enviado ao endpoint [Exportar usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) da Braze para determinar se um perfil para o usuário existe na Braze.

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Se um usuário existir na Braze com esse e-mail ou telefone, o perfil dele será retornado. Caso contrário, um array "users" vazio será retornado. O benefício de usar o endpoint de exportação para determinar se um usuário com esse endereço de e-mail já existe é que isso permite identificar se algum perfil de usuário anônimo está associado ao usuário. Por exemplo, um perfil anônimo criado via SDK (que terá um `braze_id`) ou um perfil de alias de usuário criado anteriormente.

Se a requisição não retornar um perfil de usuário, você pode optar por criar um alias de usuário ou criar um usuário somente com e-mail:

### Alias de usuário {#user-alias}

Use o endpoint de rastreamento de usuários para criar um alias de usuário, usando o identificador escolhido como o nome do alias. Ao incluir `_update_existing_only` como `false` dentro do objeto de atributo, evento ou compra onde o novo alias de usuário é definido, você pode criar o perfil de alias e adicionar atributos, eventos e compras a esse perfil simultaneamente.

Para que o alias de usuário seja um perfil com capacidade de envio, você deve incluir o endereço de e-mail no campo `email`, conforme mostrado no exemplo a seguir.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@example.com",
       "alias_label" : "email"
     },
     "email": "test@example.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Posteriormente, você pode identificar e mesclar esse alias de usuário com um `external_id` quando ele estiver disponível por meio do nosso endpoint [Identificar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

### Criando um usuário somente com e-mail {#creating-an-email-only-user}

Use o endereço de e-mail como identificador no endpoint de rastreamento de usuários.

```json
{
    "attributes": [
        {
            "email": "test@example.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Essa funcionalidade está em acesso antecipado.
{% endalert %}

## Sincronização de dados com perfis de usuário {#syncing-data-to-user-profiles}

[User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- Este é um endpoint acessível publicamente que pode criar e atualizar usuários na Braze, como registrar atributos no perfil de usuário. Esse endpoint tem um limite de frequência de 50.000 solicitações por minuto, aplicado no nível do espaço de trabalho.
- Ao usar esse endpoint, inclua a chave `partner` conforme mostrado na nossa documentação de parceiros.

[Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- De forma semelhante ao endpoint user track, os dados podem ser sincronizados com perfis de usuário por meio da ingestão de dados na nuvem. Ao usar essa ferramenta, atributos, eventos e compras são registrados nos perfis configurando e conectando a tabela ou a exibição do data warehouse que você deseja sincronizar com o espaço de trabalho desejado da Braze.

[Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- A Braze possui um modelo de pontos de dados em que os pontos de dados são registrados a cada "gravação" no perfil de usuário, independentemente de o valor ter sido alterado. Por esse motivo, recomendamos que apenas os atributos que foram alterados sejam enviados para a Braze.

## Enviando públicos de usuários para a Braze {#sending-audiences-of-users-to-braze}

[Documentação de parceiros para sincronização de importação de coortes]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- Públicos de usuários podem ser sincronizados com a Braze como uma coorte usando os endpoints da API de importação de coortes da Braze. Em vez de esses públicos serem armazenados no perfil de usuário como atributos de usuário, os clientes podem criar e direcionar essa coorte por meio de um filtro com a marca do parceiro dentro da nossa ferramenta de segmentação. Isso permite que você encontre e direcione um Segment específico de usuários de forma mais eficiente.
- Os endpoints de importação de coortes não são públicos e são específicos para cada parceiro. Por esse motivo, as sincronizações com os endpoints de coorte não contam para os limites de frequência do espaço de trabalho do cliente.

[Rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- Este é um endpoint acessível publicamente que pode ser usado imediatamente para criar usuários na Braze, identificando um usuário em um público específico por meio de um atributo de usuário. A principal diferença entre este endpoint e o endpoint de importação de coortes é que os públicos enviados usando este endpoint seriam armazenados no perfil de usuário, enquanto o endpoint de importação de coortes apareceria como um filtro na nossa ferramenta de segmentação. Este endpoint tem um limite de frequência de 50.000 requisições por minuto aplicado no nível do espaço de trabalho.
- Ao usar este endpoint, certifique-se de incluir a chave `partner` conforme mostrado na nossa [documentação de parceiros]({{site.baseurl}}/partners/isv_partners/api_partner).

[Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- A Braze tem um modelo de pontos de dados em que os pontos de dados são registrados por "gravação" no perfil de usuário, independentemente de o valor ter sido alterado.
- Os pontos de dados são consumidos tanto pela importação de coortes quanto pelos endpoints de rastreamento de usuários.

## Streaming de análise de dados de engajamento para parceiro {#engagement-analytics-streaming-to-partner}

### Currents

O Currents é uma ferramenta de streaming de análise de dados de engajamento com mensagens quase em tempo real na Braze. Ele transmite dados no nível do usuário sobre todos os envios, entregas, aberturas, cliques, etc., para Campaigns e Canvas enviados a partir do espaço de trabalho do cliente. Alguns pontos importantes: o Currents é precificado por conector para o cliente, então todos os novos parceiros do Currents devem passar por um processo de EA. Pedimos que nossos parceiros tenham cinco clientes como parte do EA antes de construirmos a interface personalizada com a marca e disponibilizarmos o conector publicamente.
- [Documentação do parceiro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) — todos os clientes que adquirem um conector do Currents terão acesso a esses eventos.
- [Eventos de comportamento do usuário]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) — nem todos os clientes que adquirem um conector do Currents compram um conector "todos os eventos" que inclui esses eventos.

### Snowflake Data Share

Os clientes que adquirem um conector do Snowflake Data Share terão acesso automaticamente tanto aos eventos de engajamento com mensagem quanto aos eventos de comportamento do usuário. Quando o Snowflake Data Share é usado como integração com parceiros, a Braze provisiona um compartilhamento para a instância do Snowflake do parceiro em nome do cliente. Como observação, o compartilhamento de dados entre regiões tem um custo mais alto para nossos clientes, então pedimos que os parceiros que desejam integrar com o Snowflake sigam a orientação de que precisam de uma conta em `US-EAST-1` e/ou `EU-CENTRAL-1`.
- [Documentação do parceiro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## Criação e disparo de Campaigns e Canvas {#building-and-triggering-campaigns-and-canvases}

### Criando ativos na Braze {#creating-assets-in-braze}
A Braze oferece vários endpoints que permitem que clientes e parceiros criem/atualizem modelos de e-mail e Content Blocks no espaço de trabalho de um cliente. Esses modelos e Content Blocks podem, por sua vez, ser usados nas Campaigns e Canvas do cliente na Braze.
- Modelos de e-mail
    - [Endpoint de criação de modelo]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [Endpoint de atualização de modelo]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
    - [Endpoint de criação de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Endpoint de atualização de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### Campaigns e Canvas disparados por API {#api-triggered-campaigns-and-canvases}

Os clientes podem configurar Campaigns e Canvas para serem disparados por API. As solicitações de API para disparar essas Campaigns podem ser usadas para personalizar e segmentar ainda mais a Campaign, passando propriedades de disparo da API e parâmetros de público ou destinatário.
- [Disparar Campaigns via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - Campaigns são mensagens individuais, como e-mails avulsos.
- [Disparar Canvas via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - Canvas é uma interface unificada onde profissionais de marketing podem criar Campaigns com múltiplas mensagens e etapas para formar uma jornada coesa. Ao disparar um Canvas, você insere um usuário no fluxo do Canvas, onde ele continuará recebendo mensagens até que não atenda mais aos critérios do Canvas.
- [Propriedades de disparo da API / propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - Dados que podem ser preenchidos dinamicamente na mensagem no momento do envio.

### Campaigns de API {#api-campaigns}
Ao criar Campaigns de API (diferentes das Campaigns disparadas por API mencionadas nesta seção), o dashboard da Braze é usado apenas para gerar um `campaign_id`, que permite ao cliente rastrear análises de dados para relatórios de Campaign. A mensagem da Campaign em si é definida na solicitação de API.
- [Enviar Campaign de API imediatamente]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [Agendar uma Campaign de API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### IDs de envio {#send-ids}
Use o endpoint da Braze para gerar um ID de envio que pode ser usado para detalhar a análise de dados da Campaign por envio. Por exemplo, se um `campaign_id` (Campaign de API) for criado por localização, um ID de envio pode ser gerado por envio para rastrear o desempenho de diferentes mensagens para uma localização específica.
- [IDs de envio]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## Connected Content

O Connected Content pode ser usado em qualquer tipo de canal para fazer uma solicitação de API ao endpoint especificado no momento do envio e inserir o conteúdo retornado na resposta dentro da mensagem.

A versatilidade do Connected Content faz dele um recurso utilizado por muitos dos nossos clientes para inserir conteúdo que não existe ou não pode ser armazenado na Braze. Alguns dos casos de uso mais comuns que vemos são:
- Inserção de conteúdo de blogs ou artigos em mensagens
- Recomendações de conteúdo
- Metadados de produtos
- Localização e tradução

Pontos importantes:
- A Braze não cobra pelas chamadas de API e elas não são contabilizadas no seu uso de pontos de dados.
- Há um limite de 1 MB para as respostas do Connected Content.
- As chamadas do Connected Content acontecem quando a mensagem é enviada, exceto para mensagens no app, que fazem essa chamada quando a mensagem é visualizada.
- As chamadas do Connected Content não seguem redirecionamentos. A Braze exige que o tempo de resposta do servidor seja inferior a 2 segundos por motivos de performance. Se o servidor levar mais de 2 segundos para responder, o conteúdo não será inserido.
- Os sistemas da Braze podem fazer a mesma chamada de API do Connected Content mais de uma vez por destinatário. Isso acontece porque a Braze pode precisar fazer uma chamada de API do Connected Content para renderizar a carga útil da mensagem, e as cargas úteis podem ser renderizadas várias vezes por destinatário para validação, lógica de tentativas ou outros fins internos.

Consulte estes artigos para saber mais sobre o Connected Content:
- [Fazendo uma chamada de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Interrompendo o Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [Tentativas do Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)