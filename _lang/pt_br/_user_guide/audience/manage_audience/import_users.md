---
nav_title: Importar usuários
article_title: Importar usuários
page_order: 3
description: "Conheça as diversas opções de importação de usuários da Braze, como importação por CSV, REST API, Ingestão de dados na nuvem e muito mais."

---
# Importar usuários {#import-users}

> Conheça as diversas opções de importação de usuários da Braze, como importação por CSV, REST API, Ingestão de dados na nuvem e muito mais.

## Opções de importação {#import-options}

Você pode fazer o upload de atributos de usuários e eventos por meio de uma importação via CSV na Braze, um script serverless de importação CSV pelo S3 Lambda, chamadas diretas à API ou Cloud Data Ingestion a partir do seu data warehouse.

### Importação via CSV da Braze {#braze-csv-import}

Você pode usar a importação via CSV para registrar e atualizar os seguintes atributos de usuários e eventos personalizados. Para começar, consulte [Importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

| Tipo | Definição | Exemplo | Tamanho máximo do arquivo |
|---|---|---|---|
| Atributos padrão | Atributos de usuário reservados reconhecidos pela Braze. | `first_name`, `email` | 500 MB |
| Atributos personalizados | Atributos de usuário exclusivos do seu negócio. | `last_destination_searched` | 500 MB |
| Eventos personalizados | Eventos exclusivos do seu negócio que representam ações do usuário. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Importação via CSV da Braze" }

#### Construindo seu CSV {#constructing-your-csv}

A Braze aceita dados de usuários no formato CSV padrão. Importações de atributos padrão e personalizados suportam arquivos de até 500 MB; importações de eventos personalizados suportam arquivos de até 50 MB. Para identificadores, cabeçalhos de coluna, regras de validação e exemplos, consulte [Importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

Ao fazer upload de um CSV grande por meio de **Importar Usuários** no dashboard, a página pode parecer sem resposta ou responder lentamente enquanto a Braze recebe o arquivo e executa a etapa de cálculo. Deixe o upload e o cálculo terminarem — o tempo total varia de alguns minutos a algumas horas dependendo do tamanho do arquivo, e arquivos maiores levam mais tempo para calcular.

{% alert note %}
Ao importar eventos personalizados com propriedades, você deve usar notação de ponto nos cabeçalhos de coluna do seu CSV. Para saber mais sobre a formatação de eventos personalizados, consulte [Entendendo a formatação de eventos personalizados]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import?tab=custom%20events#understanding-custom-event-formatting).
{% endalert %}

### Importação de CSV de usuários via Lambda {#lambda-user-csv-import}

Use nosso script serverless de importação CSV pelo S3 Lambda para fazer upload de atributos de usuários na Braze. Essa solução funciona como um uploader de CSV, no qual você coloca seus CSVs em um bucket S3, e os scripts fazem o upload por meio da nossa API.

O tempo estimado de execução para um arquivo com 1.000.000 de linhas é de cerca de cinco minutos. Para saber mais, consulte [Importação de atributos de usuário via CSV para a Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### REST API

Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para registrar eventos personalizados, atributos de usuários e compras.

### Cloud Data Ingestion {#cloud-data-ingestion}

Use o [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) da Braze para importar e manter atributos de usuários.

## Validação de HTML {#html-validation}

Lembre-se de que a Braze não sanitiza, valida ou reformata dados HTML durante a importação, o que significa que as tags de script devem ser removidas de todos os dados de importação que você usa para personalização web.

Ao importar dados para a Braze que são especificamente destinados ao uso de personalização em um navegador web, certifique-se de que estejam livres de HTML, JavaScript ou qualquer outra tag de script que possa ser explorada de forma maliciosa ao ser renderizada em um navegador web.

Como alternativa, para HTML, você pode usar os filtros Liquid da Braze (`strip_html`) para remover o HTML do texto renderizado. Por exemplo:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}