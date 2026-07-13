---
nav_title: Scuba
article_title: Scuba Analytics
description: "Esta referência técnica da Scuba e da Braze descreve como ativar o insight de dados em tempo real da Scuba usando Braze Segments."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io) é uma plataforma de colaboração de dados full-stack, com machine learning, projetada para dados de séries temporais de alta velocidade. A Scuba permite exportar usuários (também chamados de atores) de forma seletiva e carregá-los na plataforma Braze. Na Scuba, as propriedades de atores personalizados são usadas para analisar tendências comportamentais, ativar seus dados em várias plataformas e realizar modelagem preditiva usando machine learning.

_Esta integração é mantida pela Scuba Analytics._

## Pré-requisitos {#prerequisites}

Para usar a Scuba Analytics com a Braze, você precisará do seguinte:

| Requisito | Descrição |
|---|---|
| Token da API da Scuba | Um token da API da Scuba que você pode recuperar do endpoint `https://{scuba_hostname}/api/create_token`. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância](https://scuba.io). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Como fazer upload dos seus dados da Scuba para a Braze {#uploading-your-scuba-data-to-braze}

{% alert important %}
A solicitação a seguir usa curl. Para um melhor gerenciamento de solicitações de API, recomendamos o uso de um cliente de API, como o Postman.
{% endalert %}

Para fazer upload dos seus dados da Scuba para a Braze, faça uma solicitação POST para `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` usando o content-type `application/json`:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Substitua o seguinte:

| Placeholder             | Descrição                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | A URL do endpoint REST da Braze da sua instância atual. Para saber mais, consulte [Chaves da API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Sua chave da API REST da Braze com a permissão `users.track`.                                                                                                                                      |
| `HOSTNAME`              | O hostname da sua instância atual da Scuba.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Seu token da API da Scuba.                                                                                                                                                                           |
| `TABLE_NAME`            | A tabela à qual seu conjunto de dados pertence. Para saber mais, consulte [Glossário: Tabela do conjunto de dados](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | A propriedade de ator à qual seu conjunto de dados pertence. Somente os dados correspondentes a esse nome serão retornados. Para saber mais, consulte [Glossário: Propriedade do ator](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | O filtro de pesquisa de público para sua propriedade de ator.                                                                                                                                             |
| `ACTOR_ID`              | O ID da propriedade do ator à qual seu conjunto de dados pertence. Esse ID corresponde ao seu `external_id` na Braze. Para saber mais, consulte [Glossário: Ator](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | O período inicial como uma data compatível com BQL. Para saber mais, consulte [Sintaxe e uso do BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | O período final como uma data compatível com BQL. Para saber mais, consulte [Sintaxe e uso do BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Opcional**: O número máximo de registros a serem retornados. Se `scuba_record_limit` for omitido, a Scuba retornará um máximo de 100 registros. Para alterar isso, atribua qualquer número não negativo a `scuba_record_limit`.    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Uploading your Scuba data to Braze" }

### Comportamento padrão {#default-behavior}

Por padrão, `update_existing_only` é definido como `false`, o que atualiza os registros existentes na Braze, bem como cria novos registros para aqueles que não existem. Para evitar que a Scuba crie novos registros, defina `update_existing_only` como `true`.

### Limite de taxa {#rate-limit}

A Scuba aplica um limite de taxa de 50.000 solicitações por minuto a esse endpoint.

## Criação de segmentos usando os dados comportamentais da Scuba {#creating-segments-using-scubas-behavioral-data}

Depois de [fazer upload dos seus dados](#uploading-your-scuba-data-to-braze), você pode criar segmentos de usuários na Braze usando os dados comportamentais da Scuba.

### Etapa 1: Criar um novo segmento {#step-1-create-a-new-segment}

Na Braze, acesse **Público** > **Segments** e selecione **Create Segment**. Em seguida, digite um nome para o seu segmento.

![Criação de um novo segmento na Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Etapa 2: Encontrar e selecionar o atributo da Scuba {#step-2-find-and-select-the-scuba-attribute}

Em **Segment Details** > **Filters**, selecione **Custom Attributes**.

![Selecionando o filtro "Custom Attributes" em "Segment Details".]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Selecione **Search custom attributes** e escolha o nome da propriedade do ator que você usou na solicitação POST anterior.

![Selecionando a propriedade do ator como um atributo personalizado.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Etapa 3: Configurar o atributo {#step-3-configure-the-attribute}

Ao lado do nome da propriedade do ator, escolha um operador e um valor (se aplicável). Esses valores são determinados pelas propriedades do ator que você definiu na Scuba. Quando terminar, selecione **Save**.

![Escolhendo um operador e um valor para o atributo selecionado.]({% image_buster /assets/img/scuba/analytics/operator_end.png %})