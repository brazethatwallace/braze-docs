---
nav_title: Importação por CSV
article_title: Importação por CSV
description: "Saiba como registrar e atualizar atributos de usuários e eventos personalizados usando a importação por CSV."
page_order: 1.2
---

# Importação por CSV {#csv-import}

> Saiba como registrar e atualizar atributos de usuários e eventos personalizados usando a importação por CSV.

## Sobre a importação por CSV {#about-csv-import}

Você pode usar a importação por CSV para registrar e atualizar os seguintes atributos de usuários e eventos personalizados. A Braze aceita esses dados como arquivos CSV padrão dentro dos tamanhos máximos indicados na tabela a seguir.

| Tipo | Definição | Exemplo | Tamanho máximo do arquivo |
|---|---|---|---|
| Atributos padrão | Atributos de usuário reservados reconhecidos pela Braze. | `first_name`, `email` | 500 MB |
| Atributos personalizados | Atributos de usuário exclusivos do seu negócio. | `last_destination_searched` | 500 MB |
| Eventos personalizados | Eventos exclusivos do seu negócio que representam ações dos usuários. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sobre a importação por CSV" }

## Usando a importação por CSV {#using-csv-import}

### Etapa 1: Baixar um modelo de CSV {#step-1-download-a-csv-template}

Para abrir a importação por CSV, acesse **Audiences** > **Import Users**. Lá, você encontrará uma tabela com detalhes sobre as importações mais recentes, como a data do upload, o nome de quem fez o upload, o nome do arquivo, a disponibilidade de direcionamento, o número de linhas importadas e o status da importação.

Para começar, selecione **Attributes** ou **Events** e baixe o modelo apropriado para ajudá-lo a construir seu arquivo CSV para upload.

![A página "Import Users" no dashboard da Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Etapa 2: Escolher um identificador {#choose-an-identifier}

O arquivo CSV que você importar precisa de um identificador dedicado. Escolha um dos seguintes tipos de identificador para sua importação:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Ao importar os dados dos seus clientes, você pode usar um `external_id` como identificador único de cada cliente. Quando você fornece um `external_id` na importação, a Braze atualiza qualquer usuário existente com o mesmo `external_id` ou cria um novo usuário identificado com esse `external_id` definido, caso nenhum seja encontrado.

- Download: [Modelo de importação de atributos por CSV: External ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Download: [Modelo de importação de eventos por CSV: External ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Se você estiver fazendo upload de uma combinação de usuários com `external_id` e usuários sem, será necessário criar um CSV para cada importação. Um CSV não pode conter tanto `external_ids` quanto aliases de usuário.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Para direcionar usuários que não possuem um `external_id`, você pode importar uma lista de usuários com aliases de usuário. Um alias funciona como um identificador único alternativo e pode ser útil se você estiver tentando alcançar usuários anônimos que não se cadastraram ou criaram uma conta no seu app.

Se você estiver fazendo upload ou atualizando perfis de usuário que são apenas alias, é necessário ter as duas colunas a seguir no seu CSV:

- `user_alias_name`: Um identificador único de usuário; uma alternativa ao `external_id`
- `user_alias_label`: Um rótulo comum para agrupar aliases de usuário

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@example.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@example.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Etapa 2: Escolher um identificador" }

Quando você fornece tanto um `user_alias_name` quanto um `user_alias_label` na importação, a Braze atualiza qualquer usuário existente com o mesmo `user_alias_name` e `user_alias_label`. Se nenhum usuário for encontrado, a Braze cria um novo usuário identificado com esse `user_alias_name` definido.

{% alert important %}
Não é possível usar uma importação por CSV para atualizar um usuário existente com um `user_alias_name` se ele já tiver um `external_id`. Em vez disso, isso cria um novo perfil de usuário com o `user_alias_name` associado. Para associar um usuário somente alias a um `external_id`, use o [endpoint Identificar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).
{% endalert %}

Download: [Modelo de importação de atributos por CSV: User Alias]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Para atualizar perfis de usuário existentes na Braze usando um valor interno de Braze ID em vez de um `external_id` ou `user_alias_name` e `user_alias_label`, especifique `braze_id` como cabeçalho de coluna.

Isso pode ser útil se você exportou dados de usuários da Braze por meio da opção de exportação CSV na segmentação e deseja adicionar um novo atributo personalizado a esses usuários existentes.

{% alert important %}
Não é possível usar uma importação por CSV para criar um novo usuário usando `braze_id`. Esse método só pode ser usado para atualizar usuários pré-existentes na plataforma Braze.
{% endalert %}

{% alert tip %}
O valor `braze_id` pode aparecer como `Appboy ID` nas exportações CSV do dashboard da Braze. Esse ID será o mesmo que o `braze_id` de um usuário, então você pode renomear essa coluna para `braze_id` ao reimportar o CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
Você pode omitir um ID externo ou alias de usuário e usar um endereço de e-mail ou número de telefone para importar usuários. Antes de importar um arquivo CSV com endereços de e-mail ou números de telefone, verifique o seguinte:

- Confirme que você não possui IDs externos ou aliases de usuário para esses perfis no seu arquivo CSV. Se tiver, a Braze priorizará o uso do ID externo ou alias de usuário antes do endereço de e-mail para identificar perfis.
- Confirme que seu arquivo CSV está formatado corretamente.

{% alert note %}
Se você incluir tanto endereços de e-mail quanto números de telefone no seu arquivo CSV, o endereço de e-mail será priorizado em relação ao número de telefone na busca de perfis.
{% endalert %}

Se um perfil existente tiver esse endereço de e-mail ou número de telefone, esse perfil será atualizado e a Braze não criará um novo perfil. Se houver vários perfis com o mesmo endereço de e-mail, a Braze usará a mesma lógica do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), onde o perfil atualizado mais recentemente será atualizado.

Se um perfil com esse endereço de e-mail ou número de telefone não existir, a Braze criará um novo perfil com esse identificador. Você pode usar o [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) para identificar esse perfil posteriormente. Para excluir um perfil de usuário, você também pode usar o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).
{% endtab %}
{% endtabs %}

### Etapa 3: Construir seu arquivo CSV {#step-3-build-your-csv-file}

Você pode fazer upload de qualquer um dos seguintes tipos de dados como um único arquivo CSV. Para fazer upload de mais de um tipo de dado, faça upload de vários arquivos CSV.

- **Atributos de usuário:** Inclui tanto atributos de usuário padrão quanto personalizados. Atributos de usuário padrão são chaves reservadas na Braze (como `first_name` ou `email`) e atributos personalizados são atributos de usuário exclusivos do seu negócio (como `last_destination_searched`).
- **Eventos personalizados:** São exclusivos do seu negócio e refletem ações que um usuário realizou, como `trip_booked` para um app de reservas de viagens.

Quando estiver pronto para começar a construir seu arquivo CSV, consulte as informações a seguir:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identificadores obrigatórios {#required-identifiers-attributes}

Embora `external_id` não seja obrigatório, seu arquivo CSV deve incluir um identificador de usuário que possa ser mapeado para **um** dos seguintes identificadores. Para detalhes sobre cada um, consulte [Escolher um identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **e** `user_alias_label`
- `email`
- `phone`

#### Atributos personalizados {#custom-attributes}

Os seguintes tipos de dados podem ser usados como atributos personalizados na importação por CSV. Cabeçalhos de coluna que não correspondam exatamente a um [atributo padrão](#default-attributes) são importados como atributos personalizados na Braze, a menos que sejam alterados durante a etapa de mapeamento.

| Tipo de dado | Descrição |
|---|---|
| Datetime | Deve ser armazenado no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Booleano | Aceita `true` ou `false`. |
| Número | Deve ser um inteiro ou float sem espaços ou vírgulas. Floats devem usar um ponto (`.`) como separador decimal. |
| String | Pode conter vírgulas se o valor estiver entre aspas duplas (`""`). |
| Em branco | Valores em branco não sobrescrevem valores existentes no perfil do usuário, e você não precisa incluir todos os atributos de usuário existentes no seu arquivo CSV. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

{% alert important %}
Arrays, tokens por push e tipos de dados de eventos personalizados não são suportados na importação de usuários, pois vírgulas no seu arquivo CSV serão interpretadas como separadores de coluna e causarão erros ao analisar o arquivo.<br><br>Para fazer upload desses tipos de valores, use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou a [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
{% endalert %}

#### Atributos padrão {#default-attributes}

{% alert important %}
Ao importar atributos padrão, os cabeçalhos de coluna que você usar devem corresponder exatamente à ortografia e capitalização dos atributos de usuário padrão. Caso contrário, a Braze os detectará como [atributos personalizados](#custom-attributes).
{% endalert %}

{% alert tip %}
Para a lista completa de atributos padrão que a Braze reconhece (via SDK, API, CSV e Ingestão de dados na nuvem), consulte [Atributos padrão]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes). A tabela a seguir abrange apenas o subconjunto que pode ser definido por meio da importação por CSV.
{% endalert %}

Os seguintes atributos padrão estão disponíveis para importação de usuários.

| Campo do perfil de usuário | Tipo de dado | Descrição | Obrigatório? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Um identificador único de usuário para o seu cliente. | Condicional. Consulte [Identificadores obrigatórios](#required-identifiers-attributes). |
| `user_alias_name` | String | Um identificador único de usuário para usuários anônimos, alternativo ao `external_id`. Deve ser usado com `user_alias_label`. | Condicional. Consulte [Identificadores obrigatórios](#required-identifiers-attributes). |
| `user_alias_label` | String | Um rótulo comum para agrupar aliases de usuário. Deve ser usado com `user_alias_name`. | Condicional. Consulte [Identificadores obrigatórios](#required-identifiers-attributes). |
| `first_name` | String | O nome dos seus usuários conforme indicado por eles (por exemplo, `Jane`). | Não |
| `last_name` | String | O sobrenome dos seus usuários conforme indicado por eles (por exemplo, `Doe`). | Não |
| `email` | String | O e-mail dos seus usuários conforme indicado por eles (por exemplo, `jane.doe@example.com`). | Não |
| `country` | String | Os códigos de país devem ser passados para a Braze no padrão ISO-3166-1 alpha-2 (por exemplo, `GB`). | Não |
| `dob` | String | Deve ser passado no formato "AAAA-MM-DD" (por exemplo, `1980-12-21`). Isso importa a data de nascimento do seu usuário e permite direcionar usuários cujo aniversário é "hoje". | Não |
| `gender` | String | "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nil (desconhecido). | Não |
| `home_city` | String | A cidade natal dos seus usuários conforme indicado por eles (por exemplo, `London`). | Não |
| `language` | String | O idioma deve ser passado para a Braze no padrão ISO-639-1 (por exemplo, `en`). Consulte nossa [lista de idiomas aceitos]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes). | Não |
| `phone` | String | Um número de telefone conforme indicado pelos seus usuários, no formato `E.164` (por exemplo, `+442071838750`). Consulte [Números de telefone dos usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers) para orientações de formatação. | Não |
| `email_open_tracking_disabled` | Booleano | Aceita true ou false. Defina como true para desativar a adição do pixel de rastreamento de abertura em todos os e-mails futuros enviados a este usuário. Disponível apenas para SparkPost e SendGrid. | Não |
| `email_click_tracking_disabled` | Booleano | Aceita true ou false. Defina como true para desativar o rastreamento de cliques em todos os links de e-mails futuros enviados a este usuário. Disponível apenas para SparkPost e SendGrid. | Não |
| `email_subscribe` | String | Os valores disponíveis são `opted_in` (registrou-se explicitamente para receber mensagens de e-mail), `unsubscribed` (optou explicitamente por não receber mensagens de e-mail) e `subscribed` (nem optou por receber nem por não receber). | Não |
| `push_subscribe` | String | Os valores disponíveis são `opted_in` (registrou-se explicitamente para receber mensagens push), `unsubscribed` (optou explicitamente por não receber mensagens push) e `subscribed` (nem optou por receber nem por não receber). | Não |
| `time_zone` | String | O fuso horário deve ser passado para a Braze no mesmo formato do banco de dados de fusos horários IANA (por exemplo, `America/New_York` ou `Eastern Time (US & Canada)`). | Não |
| `date_of_first_session`  `date_of_last_session` | String | Pode ser passado em um dos seguintes formatos ISO 8601: "AAAA-MM-DD" "AAAA-MM-DDTHH:MM:SS+00:00" "AAAA-MM-DDTHH:MM:SSZ" "AAAA-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) | Não |
| `subscription_group_id` | String | O `id` do seu grupo de inscrições. Esse identificador pode ser encontrado na página do grupo de inscrições no seu dashboard. | Não |
| `subscription_state` | String | O estado da inscrição para o grupo de inscrições especificado por `subscription_group_id`. Os valores permitidos são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições). | Não, mas fortemente recomendado se `subscription_group_id` for usado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos padrão" }

#### Atualizar o status do grupo de inscrições (opcional) {#updating-subscription-group-status-optional}

Além disso, você pode adicionar usuários a grupos de inscrições de e-mail ou SMS por meio da importação de usuários. Isso é particularmente útil para SMS, pois um usuário precisa estar inscrito em um grupo de inscrições de SMS para receber mensagens pelo canal de SMS. Para saber mais, consulte [Grupos de inscrições de SMS]({{site.baseurl}}/sms_rcs_subscription_groups#subscription-group-mms-enablement).

Se você estiver atualizando os status dos grupos de inscrições, é necessário ter as duas colunas a seguir no seu CSV:

- `subscription_group_id`: O `id` do [grupo de inscrições]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups).
- `subscription_state`: Os valores disponíveis são `unsubscribed` (não está no grupo de inscrições) ou `subscribed` (está no grupo de inscrições).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atualizar o status do grupo de inscrições (opcional)" }

{% alert note %}
Apenas um único `subscription_group_id` pode ser definido por linha na importação de usuários. Linhas diferentes podem ter valores de `subscription_group_id` diferentes. No entanto, se você precisar inscrever os mesmos usuários em vários grupos de inscrições, será necessário fazer várias importações.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identificadores obrigatórios {#required-identifiers-custom-events}

Embora `external_id` não seja obrigatório, você **deve** incluir **um** dos seguintes identificadores como cabeçalho no seu arquivo CSV. Para detalhes sobre cada um, consulte [Escolher um identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **e** `user_alias_label`
- `email`
- `phone`

#### Campos de eventos personalizados {#custom-event-fields}

Além dos campos a seguir, seu CSV também pode conter cabeçalhos de coluna adicionais para propriedades de eventos. Essas propriedades devem ter um cabeçalho de coluna no formato `<event_name>.properties.<property name>.`

Por exemplo, o evento personalizado `trip_booked` pode ter as propriedades `destination` e `duration`. Elas podem ser importadas usando os cabeçalhos de coluna `trip_booked.properties.destination` e `trip_booked.properties.duration`.

| Campo do perfil de usuário | Tipo de dado | Informações | Obrigatório? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Um identificador único de usuário para o seu usuário. | Condicional. Consulte [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `braze_id` | String | Um identificador atribuído pela Braze para o seu usuário. | Condicional. Consulte [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `user_alias_name` | String | Um identificador único de usuário para usuários anônimos, alternativo ao `external_id`. Deve ser usado com `user_alias_label`. | Condicional. Consulte [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `user_alias_label` | String | Um rótulo comum para agrupar aliases de usuário. Deve ser usado com `user_alias_name`. | Condicional. Consulte [Identificadores obrigatórios](#required-identifiers-custom-events). |
| `email` | String | O e-mail dos seus usuários conforme indicado por eles (por exemplo, `jane.doe@example.com`). | Não, e só pode ser usado na ausência de outros identificadores. Consulte a nota a seguir. |
| `phone` | String | Um número de telefone conforme indicado pelos seus usuários, no formato `E.164` (por exemplo, `+442071838750`). Consulte [Números de telefone dos usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers) para orientações de formatação. | Não, e só pode ser usado na ausência de outros identificadores. Consulte a nota a seguir. |
| `name` | String | Um evento personalizado dos seus usuários. | Sim |
| `time` | String | O horário do evento. Pode ser passado em um dos seguintes formatos ISO-8601: "AAAA-MM-DD" "AAAA-MM-DDTHH:MM:SS+00:00" "AAAA-MM-DDTHH:MM:SSZ" "AAAA-MM-DDTHH:MM:SS" (por exemplo, 2019-11-20T18:38:57) | Sim |
| `<event name>.properties.<property name>` | Múltiplos | Uma propriedade de evento associada a um evento personalizado. Um exemplo é `trip_booked.properties.destination` | Não |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campos de eventos personalizados" }

#### Requisitos de formato para eventos personalizados {#format-requirements-for-custom-events}

Ao importar eventos personalizados usando CSV, você deve formatar seu arquivo de acordo com os seguintes requisitos para uma importação de dados bem-sucedida.

##### Entendendo a formatação de eventos personalizados {#understanding-custom-event-formatting}

É importante formatar corretamente o CSV de eventos personalizados usando notação de ponto para que cada propriedade seja mapeada para o evento correto. Se o formato estiver incorreto, as propriedades podem ser descartadas ou a importação pode falhar, especialmente quando vários tipos de eventos estão incluídos em um único arquivo.

##### Use notação de ponto para propriedades de eventos {#use-dot-notation-for-event-properties}

A notação de ponto é usada para definir a relação hierárquica entre um evento personalizado e suas propriedades. Essa convenção de formatação permite importar dados de eventos estruturados que incluem atributos específicos para cada evento.

O formato de notação de ponto segue esta estrutura: `event_name.properties.property_name`

A notação de ponto funciona na seguinte sequência:

1. O nome do evento vem primeiro
2. Seguido por `.properties.` para indicar que o que vem a seguir é uma propriedade do evento
3. Por fim, o nome específico da propriedade

**Exemplo:**

Para um evento personalizado chamado `rented_movie` com as propriedades `movie_name` e `genre`, os cabeçalhos de coluna do seu CSV seriam:

- `rented_movie.properties.movie_name`
- `rented_movie.properties.genre`

Essa notação informa à Braze para criar um evento personalizado chamado `rented_movie` e anexar as propriedades `movie_name` e `genre` a essa instância específica do evento.

##### Um evento por linha {#one-event-per-row}

Cada linha no seu CSV representa um único evento personalizado para um único usuário. Se um usuário tiver vários eventos, você deve incluir uma linha separada para cada evento, mesmo que compartilhem o mesmo identificador de usuário.

{% alert important %}
Quando uma linha contém dados para um evento específico, preencha apenas as colunas das propriedades desse evento. Deixe as colunas de outros eventos em branco.
{% endalert %}

##### Exemplo de estrutura CSV {#example-csv-structure}

A tabela a seguir demonstra a formatação correta para importar eventos personalizados com propriedades. Este exemplo mostra dois usuários que realizaram eventos diferentes: um alugou um filme e outro comprou um filme.

| external_id | name | time | rented_movie.properties.movie_name | rented_movie.properties.genre | bought_movie.properties.movie_name | bought_movie.properties.genre |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 123 | rented_movie | 2024-06-10T12:00:00Z | Ghostbusters | Action | | |
| 456 | bought_movie | 2024-06-12T12:00:00Z | | | Ghostbusters | Action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Exemplo de estrutura CSV" }

Neste exemplo:

- O usuário `123` disparou o evento `rented_movie` com as propriedades `movie_name` (Ghostbusters) e `genre` (Action)
- O usuário `456` disparou o evento `bought_movie` com as propriedades `movie_name` (Ghostbusters) e `genre` (Action)
- Cada evento preenche apenas as colunas de propriedades relevantes, deixando as colunas de propriedades de outros eventos em branco

{% endtab %}
{% endtabs %}

### Etapa 4: Fazer upload do seu arquivo {#step-4-upload-your-file}

Para fazer upload do seu arquivo, selecione **Attributes** ou **Events**, clique em **Browse Files** e faça upload do seu CSV. A Braze exibe uma prévia das primeiras linhas e um resumo dos campos detectados.

Para arquivos grandes (até 500 MB para atributos padrão e atributos personalizados, ou 50 MB para eventos personalizados), o dashboard pode parecer temporariamente sem resposta enquanto o arquivo é carregado e a Braze calcula a importação. Esses uploads e cálculos podem levar mais tempo para serem concluídos do que para arquivos menores. Aguarde a conclusão desta etapa. Para mais contexto sobre limites de arquivo e tempo, consulte [Construindo seu CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#constructing-your-csv).

Antes de fazer upload do seu arquivo CSV, renomeie-o com o nome de importação que você deseja ver na Braze. Não é possível editar o nome da importação após o upload.

{% alert note %}
A prévia do arquivo mostra apenas as primeiras linhas do seu arquivo. Para verificar todas as linhas antes de importar, use a [validação de arquivo](#file-validation).
{% endalert %}

### Etapa 5: Mapear seus campos (para atributos) {#csv-data-mapping}

Após a prévia, você pode mapear os cabeçalhos do seu CSV para atributos da Braze. A Braze mapeia automaticamente os campos do seu arquivo CSV para atributos com nomes idênticos e cria novos atributos quando necessário. Você também terá a flexibilidade de ajustar manualmente as sugestões ou selecionar atributos diferentes para qualquer coluna.

![A página de mapeamento de colunas.]({% image_buster /assets/img/csv_import/column_mapping_mapped.png %})

#### Status de mapeamento {#mapping-statuses}

A coluna de status de mapeamento indica a ação que ocorre quando seu arquivo CSV é importado e pode ser qualquer um dos seguintes.

| Status de mapeamento | O que significa |
|:---|:---|
| **Mapeado** | Campo mapeado para um atributo ou identificador existente. |
| **Novo atributo** | A Braze cria um novo atributo na importação. Você pode editar esse atributo selecionando o botão **Edit new attribute**. |
| **Incompatibilidade de tipo de dado** | O tipo de dado detectado da coluna CSV não corresponde ao tipo de dado do atributo ou identificador existente. A Braze tenta converter o tipo de dado na importação para corresponder ao atributo existente. O valor é descartado se isso não for possível. |
| **Atributo na lista de bloqueio** | O campo CSV corresponde ao nome de um atributo na lista de bloqueio. Selecione um atributo diferente para mapear ou a coluna não será importada. |
| **Atributo duplicado** | Há um ou mais campos com o mesmo nome no seu arquivo CSV. Mapeie as colunas com o mesmo nome para atributos diferentes ou apenas a primeira coluna será importada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status de mapeamento" }


#### Editando novos atributos {#editing-new-attributes}

Quando um atributo correspondente não existe no seu espaço de trabalho, a Braze tenta criar um novo atributo na importação usando o nome do campo CSV e o tipo de dado detectado. Você pode editar esse novo atributo antes da importação selecionando o botão **Edit new attribute** ao lado do status de mapeamento.

![O botão de editar novo atributo na página de mapeamento de colunas.]({% image_buster /assets/img/csv_import/column_mapping_edit_attribute_button.png %})


{% alert note %}
Você não pode prosseguir além da etapa de mapeamento até que um identificador seja mapeado. A Braze mapeia automaticamente um identificador quando possível. Consulte a seção **Required fields** para verificar se um identificador está mapeado.
{% endalert %}

### Etapa 6: Escolher preferências de direcionamento {#targeting-preferences}

Após o mapeamento, você pode escolher entre as seguintes preferências de direcionamento na página de configurações de importação. Se você não precisar criar um novo filtro de direcionamento ou segmento a partir da sua importação, selecione **Do not make this list available as a targeting filter**.

| Opção | Descrição |
|---|---|
| Filtro de direcionamento | Para converter seu arquivo CSV em uma opção de redirecionamento ao construir segmentos de usuários, escolha seu arquivo no dropdown **Updated/Imported from CSV** e selecione **Create targeting filter**. |
| Novos segmentos | Para também criar um novo segmento a partir do seu novo filtro de direcionamento, selecione **Create targeting filter and add to new segment**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 6: Escolher preferências de direcionamento" }

![Um grupo de filtros com o filtro "Updated/Imported from CSV" incluindo um arquivo CSV intitulado "Halloween season fun".]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Etapa 7: Validar seu arquivo (opcional) {#file-validation}

Antes de iniciar sua importação, você pode executar a validação de arquivo para verificar todas as linhas em busca de erros e avisos. Para validar seu arquivo, selecione **Validate file before importing** na página de configurações de importação e clique em **Next**.

A validação pode levar até 2 minutos para arquivos no tamanho máximo permitido. Enquanto a validação é executada, você pode selecionar **Skip validation** para ignorá-la e prosseguir imediatamente.

#### Resultados da validação {#validation-results}

Quando a validação for concluída, um dos seguintes resultados será exibido.

| Resultado | O que significa | Próxima etapa |
|---|---|---|
| **Validação concluída** | Nenhum problema encontrado. | Selecione **Import data**. |
| **Problemas encontrados** | Algumas linhas têm erros ou avisos. | Baixe o relatório de erros para revisá-los e selecione **Import anyway** para prosseguir ou **Cancel** para corrigir seu arquivo primeiro. |
| **Validação expirou** | A validação esgotou o tempo. As linhas verificadas não apresentaram problemas. | Selecione **Import data**. Um relatório completo estará disponível em alguns minutos. |
| **Validação expirou com problemas** | A validação esgotou o tempo e encontrou erros em algumas das linhas verificadas. | Baixe o relatório parcial para revisar o que foi encontrado e selecione **Import anyway** ou **Cancel**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Resultados da validação" }

![A página de resumo mostrando a seção de problemas encontrados, com a contagem de linhas com erros e avisos, e opções para voltar, baixar o relatório de erros ou iniciar a importação.]({% image_buster /assets/img/csv_import/summary_page_validation_results.png %})

#### Entendendo o relatório de erros {#understanding-the-error-report}

O relatório de erros é um arquivo CSV que contém todas as linhas sinalizadas junto com seus dados originais e uma descrição do problema.

| Tipo de problema | Descrição |
|---|---|
| **Erro** | A linha será ignorada completamente durante a importação. |
| **Aviso** | A linha será importada, mas alguns valores serão descartados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo o relatório de erros" }

Após revisar o relatório, você pode corrigir os problemas no seu arquivo original e fazer upload novamente, ou prosseguir com a importação e aceitar os resultados parciais.



### Etapa 8: Iniciar sua importação por CSV {#step-8-start-your-csv-import}

Quando estiver pronto, selecione **Start Import**. Você pode acompanhar o progresso atual na página **Import Users**, que é atualizada automaticamente a cada 5 segundos.
O processamento pode levar de alguns minutos a algumas horas, dependendo do tamanho do seu CSV. Durante esse tempo, o dashboard pode parecer sem resposta ou responder lentamente, mas a importação ainda está em execução.

{% alert note %}
Você pode importar mais de um CSV ao mesmo tempo. As importações por CSV são executadas simultaneamente, então a ordem das atualizações não é garantida como serial. Se você precisar que as importações por CSV sejam executadas uma após a outra, aguarde até que uma importação por CSV seja concluída antes de fazer upload de uma segunda.
{% endalert %}

#### Status da importação {#import-statuses}

Após iniciar sua importação, você pode verificar o status na página **Import Users**.

| Status | Descrição |
|---|---|
| **Concluída** | Todas as linhas foram importadas com sucesso. |
| **Sucesso parcial** | Algumas linhas falharam. Selecione o menu de três pontos ao lado da importação para baixar um relatório de erros ou o CSV original enviado. |
| **Em andamento** | A importação está em execução. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status da importação" }

![A página Import Users mostrando um status de sucesso parcial com o menu de contexto aberto, exibindo as opções de baixar relatório de erros e baixar CSV enviado.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

O relatório de erros pós-importação inclui linhas que falharam por motivos que a validação não cobre, como quando um usuário não existe na Braze.

{% alert important %}
Arquivos CSV enviados anteriormente ficam disponíveis para download na página **Import Users** por 14 dias após a data do upload. Após 14 dias, o arquivo é excluído permanentemente e não pode mais ser acessado.
{% endalert %}

## Considerações sobre pontos de dados {#data-point-considerations}

Cada dado de cliente importado de um arquivo CSV sobrescreve o valor existente nos perfis de usuário e registra um ponto de dados, exceto IDs externos e valores em branco. Se você tiver dúvidas sobre as nuances dos pontos de dados da Braze, seu gerente de conta da Braze pode esclarecê-las.

| Consideração | Detalhes |
|---|---|
| IDs externos | Fazer upload de um CSV contendo apenas `external_id` não registra pontos de dados. Isso permite segmentar usuários existentes da Braze sem impactar os limites de dados. No entanto, incluir campos como `email` ou `phone` sobrescreve dados de usuário existentes e **registra** pontos de dados. <br><br>Importações por CSV usadas apenas para segmentação não registram pontos de dados, como aquelas contendo apenas `external_id`, `braze_id` ou `user_alias_name`. |
| Valores em branco | Valores em branco no seu CSV não sobrescrevem dados existentes no perfil do usuário. Você não precisa incluir todos os atributos de usuário ou eventos personalizados ao importar. |
| Estados de inscrição | Atualizar `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` **não** conta para o uso de pontos de dados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considerações sobre pontos de dados" }

{% alert important %}
Definir `language` ou `country` em um usuário por meio de importação por CSV ou API impede que a Braze capture automaticamente essas informações pelo SDK.
{% endalert %}

## Solução de problemas {#troubleshooting}

Se você usou a [validação de arquivo](#file-validation), comece pelo relatório de erros, pois ele inclui o problema específico de cada linha sinalizada e uma descrição de como corrigi-lo. Para linhas que falharam durante a importação e não na validação, baixe o relatório de erros passando o cursor sobre a linha e selecionando o botão <i class="fas fa-download" title="Download"></i> na página **Import Users**.

Para solucionar problemas de importação por CSV, revise os problemas comuns nas seções a seguir.

### Usar e-mail como `external_id` {#use-email-as-external_id}

A Braze não recomenda usar um endereço de e-mail como `external_id`. Se você usar e-mail como `external_id`, inclua as colunas `external_id` e `email` no seu CSV para que os usuários continuem direcionáveis pelo canal de e-mail. Use uma vírgula (`,`) como delimitador de coluna — não dois pontos (`:`).

### Caracteres de aspas em valores de `external_id` {#quote-characters-in-external_id-values}

Se uma célula de `external_id` contiver aspas duplas, escape-as duplicando o caractere (`""`), conforme descrito em [Aspas duplas não escapadas ou desbalanceadas](#missing-row). A importação por CSV não usa escape com barra invertida.

### A importação por CSV não está disponível como filtro de segmento {#csv-import-isnt-available-as-a-segment-filter}

Você pode usar uma importação por CSV como filtro de segmento apenas se tiver ativado uma preferência de direcionamento durante o upload.

Para verificar se a disponibilidade de direcionamento está ativada para uma importação existente:

1. Na página **Import Users**, encontre sua importação por CSV.
2. Verifique se **Go to Segment** aparece para essa importação.
3. Se **Go to Segment** aparecer, seu CSV está disponível no filtro de segmento `Updated/Imported from CSV`.
4. Se **Go to Segment** não aparecer, a disponibilidade de direcionamento não foi ativada para essa importação.

Não é possível ativar a disponibilidade de direcionamento após a conclusão de um upload de CSV. Para usar esse CSV como filtro de segmento, faça upload do arquivo novamente e, na [Etapa 6: Escolher preferências de direcionamento](#step-6-choose-targeting-preferences), selecione **Create targeting filter** ou **Create targeting filter and add to new segment**.

Se seu objetivo é criar um segmento sem atualizar dados de perfil, faça upload de um CSV que inclua apenas colunas de identificadores (por exemplo, `external_id` ou colunas de identificadores de alias) e selecione **Create targeting filter and add to new segment**.

### Problemas de formatação de arquivo {#file-formatting-issues}

#### Linha malformada {#malformed-row}

Se o seu upload foi concluído com erros, pode haver uma linha malformada no seu arquivo CSV.

Para importar dados corretamente, deve haver uma linha de cabeçalho. Cada linha deve ter o mesmo número de células que a linha de cabeçalho. Linhas com mais ou menos valores que a linha de cabeçalho serão excluídas da importação. Vírgulas em um valor serão interpretadas como separador e podem causar esse erro.

Além disso, todos os dados devem ser codificados em UTF-8. Se o arquivo for salvo com uma codificação legada (por exemplo, alguns padrões do Excel), caracteres especiais e URLs nas células podem ser corrompidos e aparecer como pontos de interrogação (`?`) na Braze ou nas mensagens enviadas.

Se o seu arquivo CSV tiver linhas em branco e importar menos linhas do que o total de linhas no arquivo CSV, isso pode não indicar um problema com a importação, já que as linhas em branco não precisariam ser importadas. Verifique o número de linhas que foram importadas corretamente e confirme se corresponde ao número de usuários que você está tentando importar.

#### Linha ausente {#missing-row}

Existem alguns motivos pelos quais o número de usuários importados pode não corresponder ao total de linhas no seu arquivo CSV:

| Problema | Resolução |
|---|---|
| IDs externos, aliases de usuário, Braze IDs, endereços de e-mail ou números de telefone duplicados | Se houver colunas de ID externo duplicadas, isso pode causar linhas malformadas ou não importadas, mesmo que as linhas estejam formatadas corretamente. Em alguns casos, isso pode não reportar um erro específico. Verifique se há duplicatas e remova-as antes de fazer upload novamente. |
| Caracteres acentuados | Seu CSV pode incluir nomes ou atributos com acentos. Certifique-se de que o arquivo esteja codificado em UTF-8 para evitar problemas de importação. |
| O Braze ID pertence a um usuário órfão | Se um usuário foi mesclado com outro e a Braze não consegue associar o Braze ID ao perfil restante, a linha não será importada. |
| Linha vazia | Linhas em branco no CSV podem causar erros de dados malformados. Verifique usando um editor de texto simples, não o Excel ou o Sheets. |
| Aspas duplas (`"`) não escapadas ou desbalanceadas | Aspas duplas envolvem valores de string que contêm vírgulas. Se um valor contiver aspas duplas, escape-as duplicando-as (`""`). Aspas duplas não escapadas ou desbalanceadas causam uma linha malformada. |
| Quebras de linha inconsistentes | Quebras de linha mistas (por exemplo, `\n` e `\r\n`) podem fazer com que a primeira linha de dados seja tratada como parte do cabeçalho. Use um editor hexadecimal ou de texto avançado para inspecionar e corrigir. |
| Arquivo codificado incorretamente | Mesmo que acentos sejam permitidos, o arquivo deve ser codificado em UTF-8. Outras codificações podem funcionar parcialmente, mas não são totalmente suportadas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Linha ausente" }

#### Aspas em strings {#string-quotation}

Valores encapsulados em aspas simples (`''`) ou duplas (`""`) serão lidos como strings na importação.

#### Datas formatadas incorretamente {#incorrectly-formatted-dates}

Datas que não estejam no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) não serão lidas como `datetimes` na importação.

### Problemas de estrutura de dados {#data-structure-issues}

#### Endereços de e-mail inválidos {#invalid-email-addresses}

Se o seu upload foi concluído com erros, pode haver um ou mais endereços de e-mail criptografados inválidos. Confirme que todos os endereços de e-mail estão criptografados corretamente antes de importá-los para a Braze.

- **Ao [atualizar ou importar endereços de e-mail]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption#step-3-import-and-update-users)** na Braze, use o valor de e-mail com hash sempre que um e-mail for incluído. Esses valores de e-mail com hash são fornecidos pela sua equipe interna.
- **Ao criar um novo usuário**, você deve adicionar `email_encrypted` com o valor de e-mail criptografado do usuário. Caso contrário, a Braze não criará o usuário. Da mesma forma, se você estiver adicionando um endereço de e-mail a um usuário existente que não possui e-mail, deve adicionar `email_encrypted`. Caso contrário, a Braze não atualizará o usuário.

#### Dados importados como atributo personalizado {#data-imported-as-custom-attribute}

Se um dado de usuário padrão (como `email` ou `first_name`) for importado como atributo personalizado, verifique a capitalização e o espaçamento do seu arquivo CSV. Por exemplo, `First_name` é importado como atributo personalizado, enquanto `first_name` é importado corretamente no campo "first name" do perfil do usuário.

#### Alterar o tipo de dado de um atributo personalizado {#change-a-custom-attributes-data-type}

Se você precisar alterar o tipo de dado de um atributo personalizado existente (por exemplo, de string para booleano), atualize o tipo de dado na página [**Custom Attributes**]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) no dashboard antes de importar seu CSV. Se o tipo de dado no seu CSV não corresponder ao tipo de dado atualmente definido para o atributo, a importação falhará com um erro.

#### Múltiplos tipos de dados {#multiple-data-types}

A Braze espera que cada valor em uma coluna seja do mesmo tipo de dado. Valores que não correspondem ao tipo de dado do seu atributo causam erros na segmentação.

Além disso, iniciar um atributo numérico com zero causará problemas, pois números que começam com zeros são considerados strings. Quando a Braze converte essa string, ela pode ser tratada como um valor octal (que usa dígitos de zero a sete), o que significa que é convertida para seu valor decimal correspondente. Por exemplo, se o valor no arquivo CSV for 0130, o perfil da Braze mostrará 88. Para evitar esse problema, use atributos com tipo de dado string. No entanto, esse tipo de dado não está disponível na comparação numérica de segmentação.

#### Tipos de atributos padrão {#default-attribute-types}

Alguns atributos padrão aceitam apenas determinados valores como válidos para atualizações de usuário. Para orientações, consulte [Construindo seu CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

Espaços à direita e diferenças na capitalização podem fazer com que um valor seja interpretado como inválido. Por exemplo, no arquivo CSV a seguir, apenas o usuário na primeira linha (`brazetest1`) terá seus status de e-mail e push atualizados com sucesso, pois os valores aceitos são `unsubscribed`, `subscribed` e `opted_in`.

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@example.com,unsubscribed,unsubscribed
brazetest2,test2@example.com,Unsubscribed,Unsubscribed
```

### "Select CSV File" não está funcionando {#select-csv-file-is-not-working}

Existem vários motivos pelos quais o botão **Select CSV File** pode não funcionar:

| Problema | Resolução |
|---|---|
| Bloqueador de pop-ups | Isso pode impedir que a página seja exibida. Confirme que seu navegador está permitindo pop-ups no site do dashboard da Braze. |
| Navegador desatualizado | Certifique-se de que seu navegador está atualizado; caso contrário, atualize-o para a versão mais recente. |
| Processos em segundo plano | Feche todas as instâncias do navegador e reinicie o computador. |
{: .reset-td-br-1 .reset-td-br-2 aria-label=""Select CSV File" não está funcionando" }