---
nav_title: Treasure Data
article_title: Importação de coortes do Treasure Data
description: "Este artigo de referência descreve a funcionalidade de importação de coortes do Treasure Data."
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# Importação de coortes do Treasure Data {#treasure-data-cohort-import}

> Este artigo descreve como importar coortes de usuários do Treasure Data para a Braze para que você possa enviar campanhas direcionadas com base em dados que podem existir apenas no seu data warehouse.

{% alert important %}
Esse recurso está em beta. Para saber mais, entre em contato com os representantes do Treasure Data e da Braze.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Treasure Data | É necessário ter uma conta do [Treasure Data](https://www.treasuredata.com/) para aproveitar essa parceria. |
| Chave de importação de dados da Braze | Isso pode ser obtido no dashboard da Braze em **Integrações de parceiros** > **Parceiros de tecnologia** e, em seguida, selecione **Treasure Data**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Endereço IP estático do Treasure Data | O endereço IP estático do Treasure Data é o ponto de acesso e a origem da vinculação para essa integração. Para determinar o endereço IP estático, entre em contato com o representante de sucesso do cliente do Treasure Data ou com o suporte técnico do Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integração de importação de dados {#data-import-integration}

### Etapa 1: Obtenha sua chave de importação de dados da Braze {#step-1-get-your-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Treasure Data**. Aqui você encontrará o endpoint REST e poderá gerar sua chave de importação de dados da Braze. Depois que a chave for gerada, você pode criar uma nova ou invalidar uma existente.

### Etapa 2: Criar uma conexão de dados {#step-2-create-a-data-connection}

Antes de criar sua conexão de dados no Treasure Data, você precisará se autenticar. Primeiro, selecione **Integrations Hub** e, em seguida, **Catalog**.

![Catálogo do hub de integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %})

Procure a integração da Braze no **Catalog**, passe o mouse sobre o ícone e selecione **Create Authentication**. Insira suas credenciais, dê um nome à sua autenticação e selecione **Done**.

![Catálogo do hub de integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %})

### Etapa 3: Defina o público da sua coorte {#step-3-define-your-cohort-audience}

Sincronize suas coortes com a Braze por meio de uma ativação no **Audience Studio** ou executando uma consulta no **Data Workbench**.

{% alert important %}
Somente os usuários que já existem na Braze são adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### Etapa 3.1: Defina sua consulta {#step-31-define-your-query}

{% alert note %}
As colunas da consulta devem ser especificadas com os nomes exatos das colunas e o tipo de dados. As colunas da consulta devem incluir pelo menos uma das colunas: `user_ids`, `device_ids` ou a coluna de alias da Braze correspondente à configuração na interface. Somente os perfis de usuário existentes na Braze serão adicionados a uma coorte. A importação de coorte não criará novos perfis de usuário.
{% endalert %}

1. Navegue até **Data Workbench** > **Queries**.
2. Selecione **New Query**.
3. Execute a consulta para validar o conjunto de resultados.

![Catálogo do hub de integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Caso de uso: sincronização de coortes por identificador {#use-case-syncing-cohorts-by-identifier}

{% subtabs local %}
{% subtab Syncing External IDs %}
Aqui está um exemplo de tabela no Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
O nome da coluna deve ser `user_ids` ou a sincronização falhará.
{% endalert %}

Para sincronizar coortes usando o ID externo, execute a seguinte consulta:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Depois de executar a consulta, estes aliases de usuário serão adicionados à coorte na Braze:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Aqui está um exemplo de tabela no Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

Para sincronizar coortes usando o alias de usuário, execute a seguinte consulta:

```sql
SELECT
  email
FROM
  example_cohort_table
```

Depois de executar a consulta, estes aliases de usuário serão adicionados à coorte na Braze:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Aqui está um exemplo de tabela no Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
O nome da coluna deve ser `device_ids` ou a sincronização falhará.
{% endalert %}

Para sincronizar coortes usando o ID do dispositivo, execute a seguinte consulta:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Depois de executar a consulta, estes IDs de dispositivo serão adicionados à coorte na Braze:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Etapa 3.2: Especifique o destino da exportação de resultados {#step-32-specify-the-result-export-target}

Depois que a consulta tiver sido criada, selecione **Export Results**. Você pode selecionar uma autenticação existente, como a criada nas etapas anteriores, ou criar uma nova autenticação para ser usada na saída.

![Catálogo do hub de integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %})


| Mapeamento de resultados de exportação | Descrição |
| ----------- | ----------- |
| ID da coorte | Esse é o identificador de coorte de backend que será enviado à Braze. |
| Nome da coorte (opcional) | Esse é o nome que aparecerá no filtro de coorte na ferramenta de segmentação da Braze. Se não for definido, o `Cohort ID` será usado como `Cohort Name`. |
| Operação | Usado para determinar se a consulta deve adicionar ou remover perfis da coorte na Braze. |
| Aliases (opcional) | Quando definido, o nome da coluna correspondente na sua consulta será enviado como `alias_label`, e os valores de cada linha na coluna serão enviados como `alias_name`. |
| Contagem de threads | Número de chamadas simultâneas à API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Specify the result export target" }

Siga [as etapas do Treasure Data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) para configurar sua exportação de acordo com o seu caso de uso.

#### Etapa 3.3: Execute a consulta {#step-33-execute-the-query}

Salve a consulta com um nome e execute, ou simplesmente execute a consulta. Após a conclusão bem-sucedida da consulta, o resultado é automaticamente exportado para a Braze.

{% endtab %}
{% tab Audience Studio %}
#### Etapa 3.1: Crie uma ativação {#step-31-create-an-activation}

Crie um novo segmento ou escolha um segmento existente para sincronizar com a Braze como uma coorte. Dentro do segmento, selecione **Create activation**.

#### Etapa 3.2: Preencha os detalhes da ativação {#step-32-fill-out-your-activation-details}

![Detalhes de ativação das integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %})

| Configuração de detalhes da ativação | Descrição |
| ----------- | ----------- |
| Nome da ativação | O nome da sua ativação. |
| Descrição da ativação | Uma breve descrição da ativação. |
| Autenticação | Selecione a autenticação de coorte da Braze criada na etapa 2. |
| ID da coorte | Esse é o identificador de coorte de backend que será enviado à Braze. |
| Nome da coorte (opcional) | Esse é o nome que aparecerá no filtro de coorte na ferramenta de segmentação da Braze. Se não for definido, o `Cohort ID` será usado como `Cohort Name`. |
| Operação | Usado para determinar se a consulta deve adicionar ou remover perfis da coorte na Braze. |
| Aliases (opcional) | Quando definido, o nome da coluna correspondente na sua consulta será enviado como `alias_label`, e os valores de cada linha na coluna serão enviados como `alias_name`. |
| Contagem de threads | Número de chamadas simultâneas à API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Fill out your activation details" }

#### Etapa 3.3: Configure o mapeamento de saída {#step-33-set-up-output-mapping}

![Mapeamento de saída de ativação das integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %})

| Mapeamento de saída da ativação | Descrição |
| ----------- | ----------- |
| Colunas de atributo | Determine as colunas do seu banco de dados de segmentos que serão mapeadas como identificadores ao sincronizar perfis com uma coorte da Braze. |
| Construtor de strings | O construtor de strings não é necessário para a integração com a Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.3: Set up output mapping" }

{% alert important %}
 - Ao usar `device_id` como identificador, o **nome da coluna de saída** deve ser `device_ids`.
 - Ao usar aliases como identificador, o **nome da coluna de saída** deve ser o nome da coluna correspondente na sua consulta, que será enviado como `alias_label`, e os valores de cada linha na coluna serão enviados como `alias_name`.
 - Ao usar `external_id` como identificador, o **nome da coluna de saída** deve ser `user_ids`.
{% endalert %}

Todos os nomes de colunas não relevantes ou com nomes incorretos serão ignorados. Você pode optar por usar mais de um identificador nas suas sincronizações.

#### Etapa 3.4: Defina o cronograma de ativação {#step-34-define-your-activation-schedule}

Defina o cronograma de sincronização desejado e salve a ativação.

![Cronograma de ativação das integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### Etapa 4: Crie um segmento da Braze a partir da Exportação do Treasure Data {#step-4-create-a-braze-segment-from-the-treasure-data-export}

Na Braze, navegue até **Segments**, crie um novo segmento e selecione **Treasure Data Cohorts** como seu filtro. A partir daqui, você pode escolher qual coorte do Treasure Data deseja incluir. Depois que o segmento de coorte do Treasure Data for criado, você poderá selecioná-lo como um filtro de público ao criar uma Campaign ou um Canvas.

![Catálogo do hub de integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %})

## Correspondência de usuários {#user-matching}

Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.