---
nav_title: Importar dados de usuários e eventos CSV
article_title: Importar dados de usuários e eventos CSV
permalink: "/csv_events/"
description: "Este artigo de referência aborda como importar dados de usuários e como importar eventos personalizados usando arquivos CSV."
page_type: reference
---

# Importando dados de usuários (acesso antecipado a eventos CSV) {#importing-user-data-csv-events-early-access}

> A Braze oferece diversas formas de importar dados de usuários para a plataforma: SDKs, APIs, ingestão de dados na nuvem, integrações com parceiros de tecnologia e arquivos CSV. Este artigo fornece instruções detalhadas sobre como importar dados de usuários, incluindo como [importar eventos personalizados via arquivos CSV (acesso antecipado)](#importing-custom-events).

{% alert important %}
Não envie e-mails de transação legalmente obrigatórios para gateways de SMS, pois há uma grande probabilidade de que esses e-mails não sejam entregues.

Embora e-mails enviados usando um número de telefone e o domínio de gateway de e-mail para SMS do provedor (MM3) possam resultar no e-mail sendo recebido como uma mensagem SMS (texto), alguns provedores de e-mail não suportam esse comportamento. Por exemplo, se você enviar um e-mail para um número de telefone da T-Mobile (como "9999999999@tmomail.net"), sua mensagem SMS seria enviada para quem possui esse número de telefone na rede T-Mobile.

Mesmo que esses e-mails não sejam entregues ao gateway de SMS, eles ainda contam para sua cobrança de e-mail. Para evitar o envio de e-mails para gateways não suportados, consulte a [lista de nomes de domínio de gateway não suportados](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}


Antes de prosseguir, observe que a Braze não sanitiza (valida ou formata corretamente) dados HTML durante a importação. Isso significa que as tags de script devem ser removidas de todos os dados de importação destinados à personalização web.

## REST API

Você pode usar o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para registrar eventos personalizados, atributos de usuário e compras para usuários.

## Importação por CSV {#csv-import}

Você pode fazer upload e atualizar perfis de usuário por meio de arquivos CSV em **Público** > **Importar Usuários**.

A importação de dados de usuários usando arquivos CSV permite registrar e atualizar atributos de usuário, como nome e e-mail, além de atributos personalizados, como tamanho do calçado. Você pode importar um CSV especificando um de dois identificadores exclusivos de usuário: um `external_id` ou um alias de usuário.

{% alert important %}
A importação de usuário também permite registrar e atualizar eventos personalizados de usuário. De forma semelhante aos atributos de usuário, você pode importar com um `external_id`, `braze_id` ou com `user_alias_name` e `user_alias_label`. Para saber mais, consulte [Importação de eventos personalizados](#importing-custom-events).
{% endalert %}

{% alert note %}
Se você estiver fazendo upload de uma combinação de usuários com `external_id` e usuários sem, será necessário criar um arquivo CSV para cada importação. Um arquivo CSV não pode conter tanto `external_ids` quanto aliases de usuário.
{% endalert %}

### Importação com ID externo {#importing-with-external-id}

Ao importar os dados de seus clientes, será necessário especificar o identificador exclusivo de cada cliente, também conhecido como `external_id`. Antes de iniciar a importação por CSV, é importante saber com sua equipe de engenharia como os usuários serão identificados na Braze. Normalmente, trata-se de um ID de banco de dados interno. Esse identificador deve estar alinhado com a forma como os usuários serão identificados pelo SDK da Braze em dispositivos móveis e na web, e é projetado para que cada cliente tenha um único perfil de usuário na Braze em todos os seus dispositivos. Saiba mais sobre o [ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle) da Braze.

Quando você fornece um `external_id` em sua importação, a Braze atualiza qualquer usuário existente com o mesmo `external_id` ou cria um novo usuário identificado com esse `external_id` definido, caso nenhum seja encontrado.

- **Download:** [Modelo de importação de atributos CSV][import_template]
- **Download:** [Modelo de importação de eventos CSV][events_template]

### Importação com alias de usuário {#importing-with-user-alias}

Para direcionar usuários que não possuem um `external_id`, você pode importar uma lista de usuários com aliases de usuário. Um alias serve como um identificador exclusivo alternativo de usuário e pode ser útil quando você está tentando engajar usuários anônimos que não se cadastraram ou criaram uma conta no seu app.

Se você estiver fazendo upload ou atualizando perfis de usuário que são somente alias, é necessário ter as duas colunas a seguir em seu CSV:

- `user_alias_name`: Um identificador exclusivo de usuário; uma alternativa ao `external_id`
- `user_alias_label`: Um rótulo comum para agrupar aliases de usuário

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Quando você fornece tanto um `user_alias_name` quanto um `user_alias_label` em sua importação, a Braze atualiza qualquer usuário existente com o mesmo `user_alias_name` e `user_alias_label`. Se um usuário não for encontrado, a Braze cria um novo usuário identificado com esse `user_alias_name` definido.

{% alert important %}
Não é possível usar uma importação por CSV para atualizar um usuário existente com `user_alias_name` se ele já tiver um `external_id`. Em vez disso, isso criará um novo perfil de usuário com o `user_alias_name` associado. Para associar um usuário somente alias a um `external_id`, use o [endpoint Identificar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).
{% endalert %}

- **Download:** [Modelo de importação de atributos de alias CSV][template_alias_attributes]
- **Download:** [Modelo de importação de eventos de alias CSV][template_alias_events]

### Importação com Braze ID {#importing-with-braze-id}

Para atualizar perfis de usuário existentes na Braze usando um valor interno de Braze ID em vez de um `external_id` ou valores de `user_alias_name` e `user_alias_label`, especifique `braze_id` como cabeçalho de coluna.

Isso pode ser útil se você exportou dados de usuário da Braze por meio da opção de exportação CSV na segmentação e deseja adicionar um novo atributo personalizado a esses usuários existentes.

{% alert important %}
Não é possível usar uma importação por CSV para criar um novo usuário usando `braze_id`. Este método só pode ser usado para atualizar usuários preexistentes na plataforma Braze.
{% endalert %}

{% alert tip %}
O valor `braze_id` pode aparecer como `Appboy ID` em exportações CSV do dashboard da Braze. Esse ID será o mesmo que o `braze_id` de um usuário, então você pode renomear essa coluna para `braze_id` ao reimportar o CSV.
{% endalert %}

### Importação de atributos padrão {#importing-default-attributes}

Para importar atributos padrão de usuários, acesse **Importar Usuários** > **Atributos**. Os atributos padrão de usuário são chaves reservadas na Braze. Por exemplo, `first_name` ou `email`. Atributos personalizados são específicos do seu negócio. Por exemplo, um app de reserva de viagens pode ter um atributo personalizado chamado `last_destination_searched`.

{% alert important %}
Ao importar dados de clientes como atributos, os cabeçalhos de coluna que você usar devem corresponder exatamente à grafia e à capitalização dos atributos padrão de usuário. Caso contrário, a Braze criará automaticamente um atributo personalizado no perfil desse usuário.
{% endalert %}

#### Cabeçalhos de coluna de dados padrão de usuário {#default-user-data-column-headers}

| CAMPO DO PERFIL DE USUÁRIO | TIPO DE DADO | INFORMAÇÃO | OBRIGATÓRIO |
|---|---|---|---|
| `external_id` | String | Um identificador exclusivo de usuário para seu cliente. | Sim, veja a [nota a seguir](#about-external-ids). |
| `user_alias_name` | String | Um identificador exclusivo de usuário para usuários anônimos. Uma alternativa ao `external_id`. | Não, veja a [nota a seguir](#about-external-ids). |
| `user_alias_label` | String | Um rótulo comum para agrupar aliases de usuário. | Sim, se `user_alias_name` for usado. |
| `first_name` | String | O nome dos seus usuários conforme indicado (por exemplo, `Jane`). | Não |
| `last_name` | String | O sobrenome dos seus usuários conforme indicado (por exemplo, `Doe`). | Não |
| `email` | String | O e-mail dos seus usuários conforme indicado (por exemplo, `jane.doe@braze.com`). | Não |
| `country` | String | Os códigos de país devem ser passados para a Braze no padrão ISO-3166-1 alpha-2 (por exemplo, `GB`). | Não |
| `dob` | String | Deve ser passado no formato "AAAA-MM-DD" (por exemplo, `1980-12-21`). Isso importará a data de nascimento do seu usuário e permitirá que você direcione usuários cujo aniversário é "hoje". | Não |
| `gender` | String | "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nil (desconhecido). | Não |
| `home_city` | String | A cidade de residência dos seus usuários conforme indicado (por exemplo, `London`). | Não |
| `language` | String | O idioma deve ser passado para a Braze no padrão ISO-639-1 (por exemplo, `en`). <br>Consulte nossa [lista de idiomas aceitos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes). | Não |
| `phone` | String | Um número de telefone conforme indicado pelos seus usuários, no formato `E.164` (por exemplo, `+442071838750`). <br> Consulte [Números de telefone de usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers) para orientações de formatação. | Não |
| `email_open_tracking_disabled` | Boolean | true ou false aceitos. Defina como true para desativar a adição do pixel de rastreamento de abertura em todos os e-mails futuros enviados a este usuário. | Não |
| `email_click_tracking_disabled` | Boolean | true ou false aceitos. Defina como true para desativar o rastreamento de clique para todos os links em e-mails futuros enviados a este usuário. | Não |
| `email_subscribe` | String | Os valores disponíveis são `opted_in` (optou explicitamente por receber mensagens de e-mail), `unsubscribed` (cancelou explicitamente a inscrição de mensagens de e-mail) e `subscribed` (nem optou nem cancelou). | Não |
| `push_subscribe` | String | Os valores disponíveis são `opted_in` (optou explicitamente por receber mensagens push), `unsubscribed` (cancelou explicitamente a inscrição de mensagens push) e `subscribed` (nem optou nem cancelou). | Não |
| `time_zone` | String | O fuso horário deve ser passado para a Braze no mesmo formato do banco de dados de fusos horários IANA (por exemplo, `America/New_York` ou `Eastern Time (US & Canada)`). | Não |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Pode ser passado em um dos seguintes formatos ISO-8601: {::nomarkdown} <ul> <li> "AAAA-MM-DD" </li> <li> "AAAA-MM-DDTHH:MM:SS+00:00" </li> <li> "AAAA-MM-DDTHH:MM:SSZ" </li> <li> "AAAA-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | Não |
| `subscription_group_id` | String | O `id` do seu grupo de inscrições. Esse identificador pode ser encontrado na página de grupos de inscrições do seu dashboard. | Não |
| `subscription_state` | String | O estado de inscrição para o grupo de inscrições especificado por `subscription_group_id`. Os valores permitidos são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições). | Não, mas fortemente recomendado se `subscription_group_id` for usado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### Sobre IDs externos {#about-external-ids}

Embora `external_id` não seja obrigatório, você **deve** incluir um destes campos:
- `external_id`: Um identificador exclusivo de usuário para seu cliente, **ou**
- `braze_id`: Um identificador exclusivo de usuário obtido para usuários existentes da Braze, **ou**
- `user_alias_name` e `user_alias_label`: Um identificador exclusivo de usuário para um usuário anônimo

### Importação de atributos personalizados {#importing-custom-attributes}

Você pode importar atributos personalizados de usuários acessando **Importar Usuários** > **Atributos**. Qualquer cabeçalho que não corresponda exatamente a atributos padrão criará um atributo personalizado na Braze.

Os seguintes tipos de dados são aceitos na importação de usuário:

| Tipo de dado | Descrição |
|-----------|-------------|
| Datetime | Deve ser armazenado no formato ISO-8601 |
| Boolean | TRUE ou FALSE |
| Número | Inteiro ou float sem espaços ou vírgulas; floats devem usar ponto (.) como separador decimal |
| String | Pode conter vírgulas desde que haja aspas duplas ao redor do valor da coluna |
| Em branco | Valores em branco não substituirão valores existentes no perfil de usuário, e você não precisa incluir todos os atributos de usuário existentes no seu arquivo CSV |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Arrays e tokens por push não são compatíveis com a importação de usuário. Especialmente para arrays, as vírgulas no seu arquivo CSV serão interpretadas como separadores de coluna, então quaisquer vírgulas em valores causarão erros na análise do arquivo. <br>Para fazer upload desses tipos de valores, use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou a [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion).
{% endalert %}

### Atualização do status do grupo de inscrições {#updating-subscription-group-status}

Você pode adicionar usuários a grupos de inscrições de e-mail ou SMS por meio da importação de usuário. Isso é particularmente útil para SMS, pois um usuário deve estar inscrito em um grupo de inscrições SMS para receber mensagens pelo canal de SMS. Para saber mais, consulte [Grupos de inscrições SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#subscription-group-mms-enablement).

Se você estiver atualizando o status do grupo de inscrições, é necessário ter as duas colunas a seguir em seu CSV:

- `subscription_group_id`: O `id` do [grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups).
- `subscription_state`: Os valores disponíveis são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Atualizando o status do grupo de inscrições">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
Apenas um único `subscription_group_id` pode ser definido por linha na importação de usuário. Linhas diferentes podem ter valores diferentes de `subscription_group_id`. No entanto, se você precisar inscrever os mesmos usuários em múltiplos grupos de inscrições, será necessário realizar múltiplas importações.
{% endalert %}

### Importação de eventos personalizados (acesso antecipado) {#importing-custom-events}

{% alert important %}
A importação de eventos personalizados está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar do acesso antecipado.
{% endalert %}

Para importar eventos personalizados dos seus usuários, acesse **Importar Usuários** > **Eventos**.

Eventos personalizados são específicos do seu negócio. Por exemplo, um app de streaming pode ter um evento personalizado chamado rented_movie. Seu CSV deve ter cabeçalhos de coluna para:

- Um dos seguintes:
  - `external_id`, **ou**
  - `braze_id`, **ou**
  - `user_alias_name` e `user_alias_label`
- Name
- Time

Eventos personalizados podem ter propriedades de evento. Por exemplo, o evento personalizado rented_movie pode ter as propriedades title e genre. Essas propriedades de evento devem ter um cabeçalho de coluna no formato `<event_name>.properties.<property name>`. Um exemplo é `rented_movie.properties.title`.

| CAMPO DO PERFIL DE USUÁRIO                      | TIPO DE DADO | INFORMAÇÃO                                                                                                                                                                                                             | OBRIGATÓRIO                                                                                        |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | String    | Um identificador exclusivo de usuário para seu usuário.                                                                                                                                                                                 | Sim, um entre `external_id`, `braze_id` ou `user_alias_name` e `user_alias_label` é obrigatório. |
| `braze_id`                              | String    | Um identificador atribuído pela Braze para seu usuário.                                                                                                                                                                              | Sim, um entre `external_id`, `braze_id` ou `user_alias_name` e `user_alias_label` é obrigatório. |
| `user_alias_name`                       | String    | Um identificador exclusivo de usuário para usuários anônimos. Uma alternativa ao external_id.                                                                                                                                        | Sim, um entre `external_id`, `braze_id` ou `user_alias_name` e `user_alias_label` é obrigatório. |
| `user_alias_label`                      | String    | Um rótulo comum para agrupar aliases de usuário.                                                                                                                                                                          | Sim, um entre `external_id`, `braze_id` ou `user_alias_name` e `user_alias_label` é obrigatório. |
| `name`                                  | String    | Um evento personalizado dos seus usuários.                                                                                                                                                                                           | Sim                                                                                             |
| `time`                                  | String    | O horário do evento. Pode ser passado em um dos seguintes formatos ISO-8601: {::nomarkdown} <ul> <li> "AAAA-MM-DD" </li> <li> "AAAA-MM-DDTHH:MM:SS+00:00" </li> <li> "AAAA-MM-DDTHH:MM:SSZ" </li> <li> "AAAA-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | Sim                                                                                             |
| `<event name>.properties.<property name>` | Múltiplos  | Uma propriedade de evento associada a um evento personalizado. Um exemplo é `rented_movie.properties.title`                                                                                                                        | Não                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Embora external_id em si não seja obrigatório, você deve incluir um dos seguintes campos: <br>- `external_id`: Um identificador exclusivo de usuário para seu cliente <br>- `braze_id`: Um identificador exclusivo de usuário obtido para usuários existentes da Braze <br>- `user_alias_name`: Um identificador exclusivo de usuário para um usuário anônimo
{% endalert %}

#### Tamanho do CSV {#csv-size}

A Braze aceita dados de usuário no formato CSV padrão de arquivos com até 500 MB de tamanho. Para baixar um dos nossos modelos de arquivo CSV, consulte [Importação com ID externo](#importing-with-external-id) ou [Importação com alias de usuário](#importing-with-user-alias).

#### Considerações sobre pontos de dados {#data-point-considerations}

Cada dado de cliente importado via CSV substituirá o valor existente nos perfis de usuário e contará como um ponto de dados, exceto IDs externos e valores em branco.

- IDs externos enviados via importação CSV não consumirão pontos de dados. Se você estiver fazendo upload de um arquivo CSV para segmentar usuários existentes da Braze enviando apenas IDs externos, isso pode ser feito sem consumir pontos de dados. Se você adicionar dados extras, como e-mail ou número de telefone do usuário na importação, isso substituirá os dados existentes do usuário e consumirá seus pontos de dados.
    - Importações CSV para fins de segmentação (importações feitas com `external_id`, `braze_id` ou `user_alias_name` como único campo) não consumirão pontos de dados.
- Valores em branco não substituirão valores existentes no perfil de usuário, e você não precisa incluir todos os atributos de usuário existentes ou eventos personalizados no seu arquivo CSV.
- A atualização de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` não contará para o consumo de pontos de dados.

{% alert important %}
Definir idioma ou país de um usuário via importação CSV ou API impedirá que a Braze capture automaticamente essas informações via SDK.
{% endalert %}

## Importação de um CSV {#importing-a-csv}

Para importar seu arquivo CSV:
1. Acesse **Audience** > **Import Users**.
2. Selecione **Browse Files** e escolha o arquivo desejado, depois selecione **Start import**. A Braze fará o upload do seu arquivo e verificará os cabeçalhos das colunas, bem como os tipos de dados de cada coluna.

{% alert important %}
As importações de CSV diferenciam maiúsculas de minúsculas. Isso significa que letras maiúsculas nas importações de CSV serão gravadas como um atributo personalizado em vez de um atributo padrão. Por exemplo, "email" está correto, mas "Email" seria gravado como um atributo personalizado.
{% endalert %}

![A opção "Events" está selecionada como o tipo de informação do usuário a ser importada.][5]

Após a conclusão do upload, você pode visualizar uma prévia do conteúdo do seu arquivo. As informações na tabela são baseadas nos valores das primeiras linhas do seu arquivo CSV.

Você pode acompanhar o progresso na página **Import Users**, que é atualizada a cada cinco segundos ou quando você seleciona **Refresh table**. Você ainda pode usar o restante do dashboard da Braze durante a importação e receberá notificações quando a importação começar e terminar.

Você também pode visualizar suas importações mais recentes, os nomes dos arquivos, o tipo de CSV, o número de linhas no arquivo, o número de linhas importadas com sucesso, o total de linhas em cada arquivo e o status de cada importação.

É possível importar mais de um arquivo CSV ao mesmo tempo. As importações de CSV serão executadas simultaneamente, o que significa que a ordem das atualizações não é garantida como sequencial. Se você precisar que as importações de CSV sejam executadas uma após a outra, aguarde até que uma importação de CSV seja concluída antes de fazer o upload de uma segunda.

Se o processo de importação encontrar um erro, um ícone de alerta aparecerá ao lado do número total de linhas no arquivo. Você pode passar o cursor sobre o ícone para ver detalhes sobre por que determinadas linhas falharam. Após a conclusão da importação, todos os dados serão adicionados a perfis existentes ou novos perfis serão criados.

![Upload de arquivo CSV concluído com erros envolvendo tipos de dados mistos em uma única coluna][4]{: style="max-width:70%"}

### Considerações {#considerations}

Se a Braze notar algo malformado nas primeiras linhas do seu arquivo durante o upload, esses erros serão mostrados com o resumo. Por exemplo, se o seu arquivo incluir uma linha malformada, esse erro será indicado na prévia quando você importar o arquivo. Embora um arquivo possa ser importado com erros, é recomendável que você corrija esses erros no seu arquivo antes de continuar com a importação.

Além disso, é importante examinar o arquivo CSV completo antes do upload, pois a Braze não verifica cada linha do arquivo de entrada para a prévia. Isso significa que podem existir erros que a Braze não detecta ao gerar essa prévia.

Linhas malformadas e linhas sem um ID externo não serão importadas. Todos os outros erros podem ser importados, mas podem interferir na filtragem ao criar um Segment. Para saber mais, vá para a seção [Solução de problemas](#troubleshooting).

{% alert warning %}
Os erros são baseados exclusivamente no tipo de dados e na estrutura do arquivo. Por exemplo, um endereço de e-mail mal formatado ainda seria importado, pois ainda pode ser interpretado como uma string.
{% endalert %}

### Importação de CSV de usuários via Lambda {#lambda-user-csv-import}

Você pode usar nosso script serverless de importação de CSV via S3 Lambda para fazer o upload de atributos de usuários para a plataforma. Essa solução funciona como um uploader de CSV, no qual você coloca seus CSVs em um bucket S3 e os scripts fazem o upload pela nossa API.

O tempo estimado de execução para um arquivo com um milhão de linhas é de aproximadamente cinco minutos. Para saber mais, consulte [Importação de CSV de atributos de usuários para a Braze]({{site.baseurl}}/user_csv_lambda).

## Segmentação {#segmenting}

A importação de usuário cria e atualiza perfis de usuário, e também pode ser usada para criar Segments. Para criar um Segment, selecione **Gerar automaticamente um segmento a partir dos usuários importados deste CSV** antes de iniciar a importação.

Você pode definir o nome do segmento ou aceitar o padrão, que é o nome do seu arquivo. Os arquivos que foram usados para criar um segmento terão um link para visualizar o segmento após a conclusão da importação.

O filtro usado para criar o segmento seleciona os usuários que foram criados ou atualizados em uma importação selecionada e está disponível com todos os outros filtros na página de edição de segmento.

## Solução de problemas {#troubleshooting}

### Linhas ausentes {#missing-rows}

Existem alguns motivos pelos quais o número de usuários importados pode não corresponder ao total de linhas no seu arquivo CSV:

- **IDs externos duplicados:** Se houver colunas de ID externo duplicadas, isso pode causar linhas malformadas ou não importadas, mesmo que as linhas estejam formatadas corretamente. Em alguns casos, isso pode não reportar um erro específico. Verifique se há IDs externos duplicados no seu CSV. Se houver, remova as duplicatas e tente fazer o upload novamente.
- **Caracteres acentuados:** Seu arquivo CSV pode ter nomes ou atributos que incluem acentos. Certifique-se de que seu arquivo esteja codificado em UTF-8 para evitar problemas.

### Linha malformada {#malformed-row}

Você deve incluir uma linha de cabeçalho no seu arquivo CSV para importar seus dados corretamente. Cada linha deve ter o mesmo número de células que a linha de cabeçalho. Linhas com mais ou menos valores que a linha de cabeçalho serão excluídas da importação. Vírgulas em um valor serão interpretadas como separador e podem causar esse erro. Além disso, todos os dados devem estar codificados em UTF-8.

Se seu arquivo CSV tiver linhas em branco e importar menos linhas que o total de linhas no arquivo CSV, isso pode não indicar um problema com a importação, pois as linhas em branco não precisariam ser importadas. Verifique o número de linhas que foram importadas corretamente e certifique-se de que corresponde ao número de usuários que você está tentando importar.

### Múltiplos tipos de dados {#multiple-data-types}

A Braze espera que cada valor em uma coluna seja do mesmo tipo de dados. Valores que não correspondem ao tipo de dados do seu atributo causarão erros na segmentação.

### Datas formatadas incorretamente {#incorrectly-formatted-dates}

Datas que não estão no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) não serão lidas como datetimes na importação.

### Aspas em strings {#string-quotation}

Valores encapsulados em aspas simples ('') ou duplas ("") serão lidos como strings na importação.

### Dados importados como atributo personalizado {#data-imported-as-custom-attribute}

Se você estiver vendo um dado padrão de usuário (por exemplo, `email` ou `first_name`) importado como um atributo personalizado, verifique a capitalização e o espaçamento do seu arquivo CSV. Por exemplo, `First_name` seria importado como um atributo personalizado, enquanto `first_name` seria importado corretamente no campo "nome" do perfil de um usuário.

[import_template]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/unlisted_docs/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/unlisted_docs/download_file/braze-events-csv-example-user-alias.csv %}
[3]: {% image_buster /assets/unlisted_docs/img/importcsv5.png %}
[4]: {% image_buster /assets/unlisted_docs/img/importcsv2.png %}
[5]: {% image_buster /assets/unlisted_docs/img/importcsv3.png %}
[7]: {% image_buster /assets/unlisted_docs/img/segment-imported-users.png %}
[8]: {% image_buster /assets/unlisted_docs/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/unlisted_docs/img/subscription_group_import.png %}