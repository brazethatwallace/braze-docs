---
nav_title: Melhores práticas
hidden: true
---

# Melhores práticas para ciclo de vida do usuário e identificadores {#user-lifecycle-and-identifiers-best-practices}

## Coleta de dados {#data-collection}

Saiba mais sobre como a Braze coleta dados:
- [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [Melhores práticas de coleta de dados]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [Ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Identificadores da Braze {#braze-identifiers}

- `braze_id`: Um identificador atribuído pela Braze que é imutável e associado a um usuário específico quando criado em nosso banco de dados.
- `external_id`: Um identificador atribuído pelo cliente, normalmente um UUID. Recomendamos que os clientes atribuam o `external_id` quando o usuário puder ser identificado de forma exclusiva. Depois que um usuário é identificado, ele não pode ser revertido para anônimo.
- `user_alias`: Um identificador alternativo exclusivo que o cliente pode atribuir como forma de referenciar o usuário por um ID antes de um `external_id` ser atribuído. Os aliases de usuário podem ser posteriormente mesclados com outros aliases ou com um `external_id` quando um estiver disponível por meio do endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) da Braze.
    - No endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), o campo `merge_behavior` pode ser usado para especificar quais dados do perfil de alias de usuário devem persistir no perfil de usuário conhecido.
    - Observe que, para que o alias de usuário seja um perfil enviável, você ainda deve incluir e-mail e/ou telefone como atributo padrão no perfil.
- `device_id`: Um identificador específico do dispositivo, gerado automaticamente. Um perfil de usuário pode ter vários `device_ids` associados a ele. Por exemplo, um usuário que tenha feito login em sua conta no computador do trabalho, no computador de casa, no tablet e no app iOS teria 4 `device_ids` associados ao seu perfil.
- Endereço de e-mail e número de telefone:
    - Suportado como identificador no endpoint de rastreamento de usuário da Braze.
    - Ao usar o endereço de e-mail ou os números de telefone como identificador em uma solicitação, há três resultados possíveis:
        1. Se um usuário com esse e-mail/telefone não existir na Braze, será criado um perfil de usuário somente de e-mail/telefone e todos os dados da solicitação serão adicionados ao perfil.
        2. Se já existir um perfil com esse e-mail/telefone na Braze, ele será atualizado para incluir todos os dados enviados na solicitação.
        3. Em um caso de uso com mais de um perfil com esse e-mail/telefone, o perfil atualizado mais recentemente será priorizado.
    - Observe que, se existir um perfil de usuário somente de e-mail/telefone e, em seguida, for criado um perfil identificado com o mesmo e-mail/telefone (como outro perfil com o mesmo endereço de e-mail E um ID externo), a Braze criará um segundo perfil. As atualizações subsequentes irão para o perfil com o ID externo.
        - Os dois perfis podem ser mesclados usando o endpoint [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) da Braze

## Tratamento de usuários anônimos {#handling-anonymous-users}

Para um caso de uso em que você precisa criar ou atualizar um perfil de usuário na Braze sem ter acesso a um `external_id`, outro identificador, como um endereço de e-mail ou número de telefone, pode ser passado para o endpoint [Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) da Braze para determinar se existe um perfil para o usuário na Braze.

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Se existir um usuário na Braze com esse e-mail ou telefone, seu perfil será retornado. Caso contrário, será retornado um array "users" vazio. A vantagem de usar o endpoint de exportação para determinar se já existe um usuário com esse endereço de e-mail é que isso permite identificar se algum perfil de usuário anônimo está associado ao usuário. Por exemplo, um perfil anônimo criado pelo SDK (que terá `braze_id`) ou um perfil de alias de usuário criado anteriormente.

Se a solicitação não retornar um perfil de usuário, você pode optar por criar um alias de usuário ou criar um usuário somente de e-mail:

### Alias de usuário {#user-alias}

Use o endpoint de rastreamento de usuário para criar um alias de usuário, usando o identificador escolhido como o nome do alias. Ao incluir `_update_existing_only` como `false` no objeto de atributo, evento ou compra em que o novo alias de usuário é definido, é possível criar o perfil de alias e adicionar atributos, eventos e compras a esse perfil simultaneamente.

Para que o alias de usuário seja um perfil enviável, é necessário incluir o endereço de e-mail no campo `email`, conforme mostrado no exemplo a seguir.

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

Posteriormente, você pode identificar e mesclar esse alias de usuário com um `external_id` quando um estiver disponível por meio do nosso endpoint [Identify users]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

### Criação de um usuário somente de e-mail {#creating-an-email-only-user}

Use o endereço de e-mail como identificador no endpoint de rastreamento de usuário.

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

## Sincronização de dados em perfis de usuários {#syncing-data-to-user-profiles}

[User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- É um endpoint acessível publicamente que pode criar e atualizar usuários na Braze, como registrar atributos no perfil do usuário. Esse endpoint tem um limite de frequência de 50.000 solicitações por minuto aplicado no nível do espaço de trabalho.
- Ao usar esse endpoint, inclua a chave `partner` conforme mostrado na documentação do parceiro.

[Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- Semelhante ao endpoint de rastreamento de usuário, os dados podem ser sincronizados com os perfis de usuário por meio da Ingestão de dados na nuvem. Ao usar essa ferramenta, atributos, eventos e compras são registrados em perfis configurando e conectando a tabela ou a visualização do data warehouse que você deseja sincronizar com o espaço de trabalho Braze desejado.

[Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- A Braze tem um modelo de pontos de dados em que os pontos de dados são registrados por "gravação" no perfil do usuário, independentemente de o valor ter sido alterado. Por esse motivo, recomendamos que apenas os atributos que foram alterados sejam enviados para a Braze.

## Envio de públicos de usuários para a Braze {#sending-audiences-of-users-to-braze}

[Documentação do parceiro de sincronização de importação de coorte]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- Os públicos de usuários podem ser sincronizados com a Braze como uma coorte usando os endpoints da API Braze Cohort Import. Em vez de esses públicos serem armazenados no perfil do usuário como atributos de usuário, os clientes podem criar e direcionar essa coorte por meio de um filtro com a marca do parceiro em nossa ferramenta de segmentação. Isso permite encontrar e direcionar com mais eficiência um segmento específico de usuários.
- Os endpoints de importação de coorte não são públicos e são específicos de cada parceiro. Por esse motivo, as sincronizações com os endpoints de coorte não serão contabilizadas nos limites de frequência do espaço de trabalho do cliente.

[User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- Esse é um endpoint acessível publicamente que pode ser usado imediatamente para criar usuários na Braze, indicando um usuário em um público específico por meio de um atributo de usuário. A principal diferença entre esse endpoint e o endpoint de importação de coorte é que os públicos enviados usando esse endpoint seriam armazenados no perfil do usuário, enquanto o endpoint de importação de coorte seria exibido como um filtro em nossa ferramenta de segmentação. Esse endpoint tem um limite de frequência de 50.000 solicitações por minuto aplicado no nível do espaço de trabalho.
- Ao usar esse endpoint, verifique se você está incluindo a chave `partner`, conforme mostrado na [documentação do parceiro]({{site.baseurl}}/partners/isv_partners/api_partner).

[Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- A Braze tem um modelo de pontos de dados em que os pontos de dados são registrados por "gravação" no perfil do usuário, independentemente de o valor ter sido alterado.
- Os pontos de dados são consumidos tanto pela importação de coorte quanto pelos endpoints de rastreamento de usuário.

## Streaming de análise de dados de engajamento para o parceiro {#engagement-analytics-streaming-to-partner}

### Currents

Currents é uma ferramenta de streaming de análise de dados de engajamento com mensagens quase em tempo real na Braze. Ela transmite dados em nível de usuário sobre todos os envios, entregas, aberturas, cliques, etc., para Campaigns e Canvas enviados a partir do espaço de trabalho do cliente. Algumas observações: o preço do Currents é por conector para o cliente, então todos os novos parceiros do Currents devem passar por um processo de acesso antecipado (EA). Solicitamos que nossos parceiros tenham cinco clientes como parte do EA antes de criarmos a interface com marca personalizada e disponibilizarmos publicamente o conector.
- [Documentação do parceiro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [Eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) — todos os clientes que comprarem um conector Currents terão acesso a esses eventos.
- [Eventos de comportamento do usuário]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) — nem todos os clientes que comprarem um conector Currents comprarão um conector "todos os eventos" que incluirá esses eventos.

### Snowflake Data Share

Os clientes que comprarem um conector Snowflake Data Share terão acesso automático aos eventos de engajamento com mensagens e de comportamento do usuário. Quando o Snowflake Data Share é usado como uma integração com parceiros, a Braze provisionará um compartilhamento para a instância do Snowflake do parceiro em nome do cliente. Como observação, o compartilhamento de dados entre regiões tem um custo mais alto para nossos clientes, então pedimos que os parceiros que desejam se integrar ao Snowflake sigam a orientação de que precisam de uma conta em `US-EAST-1` e/ou `EU-CENTRAL-1`
- [Documentação do parceiro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## Criação e disparo de Campaigns e Canvas {#building-and-triggering-campaigns-and-canvases}

### Criação de ativos na Braze {#creating-assets-in-braze}
A Braze oferece vários endpoints que permitem que clientes e parceiros criem/atualizem modelos de e-mail e Content Blocks no espaço de trabalho do cliente. Esses modelos e Content Blocks podem, por sua vez, ser usados nas Campaigns e Canvas do cliente.
- Modelos de e-mail
    - [Endpoint de criação de modelo]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [Endpoint de atualização de modelo]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks)
    - [Endpoint de criação de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Endpoint de atualização de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### Campaigns e Canvas disparados por API {#api-triggered-campaigns-and-canvases}

Os clientes podem configurar Campaigns e Canvas para serem disparados por API. As solicitações de API para disparar essas Campaigns podem ser usadas para personalizar e segmentar ainda mais a campanha, passando propriedades de disparo de API e parâmetros de público ou destinatário.
- [Disparo de Campaigns via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - Campaigns são mensagens individuais, como e-mails avulsos.
- [Disparo de Canvas via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - Canvas é uma interface unificada na qual profissionais de marketing podem criar campanhas com várias mensagens e etapas para formar uma jornada coesa. Ao disparar um Canvas, você está inserindo um usuário no fluxo do Canvas, onde ele continuará a receber mensagens até que não se encaixe mais nos critérios do Canvas.
- [Propriedades de disparo de API/propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - Dados que podem ser preenchidos dinamicamente na mensagem no momento do envio.

### Campaigns de API {#api-campaigns}
Ao criar Campaigns de API (diferentes das Campaigns disparadas por API mencionadas nesta seção), o dashboard da Braze é usado apenas para gerar um `campaign_id`, que permite ao cliente rastrear a análise de dados para relatórios de campanha. A própria mensagem da campanha é definida na solicitação da API.
- [Enviar Campaign de API imediatamente]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [Agendar uma Campaign de API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### IDs de envio {#send-ids}
Use o endpoint da Braze para gerar um ID de envio que pode ser usado para detalhar a análise de dados da campanha por envio. Por exemplo, se um `campaign_id` (Campaign de API) for criado por localização, um ID de envio pode ser gerado por envio para rastrear o desempenho de diferentes mensagens para uma determinada localização.
- [IDs de envio]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## Conteúdo conectado {#connected-content}

O Conteúdo conectado pode ser usado em qualquer tipo de canal para fazer uma solicitação de API ao endpoint especificado no momento do envio e preencher a mensagem com o que é retornado na resposta.

A versatilidade do Conteúdo conectado faz com que esse seja um recurso usado por muitos de nossos clientes para inserir conteúdo que não está ou não pode estar na Braze. Alguns dos casos de uso mais comuns que vemos são:
- Inserção de conteúdo de blog ou artigo em mensagens
- Recomendações de conteúdo
- Metadados de produto
- Localização e tradução

Pontos importantes:
- A Braze não cobra pelas chamadas de API e elas não serão contabilizadas no seu uso de pontos de dados.
- Há um limite de 1 MB para as respostas do Conteúdo conectado.
- As chamadas do Conteúdo conectado ocorrerão quando a mensagem for enviada, exceto no caso de mensagens no app, que farão essa chamada quando a mensagem for visualizada.
- As chamadas do Conteúdo conectado não seguem redirecionamentos. A Braze exige que o tempo de resposta do servidor seja inferior a 2 segundos por motivos de desempenho; se o servidor demorar mais de 2 segundos para responder, o conteúdo não será inserido.
- Os sistemas da Braze podem fazer a mesma chamada à API de Conteúdo conectado mais de uma vez por destinatário. Isso ocorre porque a Braze pode precisar fazer uma chamada à API de Conteúdo conectado para renderizar uma carga útil de mensagem, e as cargas úteis de mensagem podem ser renderizadas várias vezes por destinatário para validação, lógica de nova tentativa ou outros fins internos.

Consulte estes artigos para saber mais sobre o Conteúdo conectado:
- [Fazendo uma chamada de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Interrupção de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [Novas tentativas de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)