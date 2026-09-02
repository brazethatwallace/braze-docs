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

Para usar o Scuba Analytics com a Braze, você precisará do seguinte:

| Requisito | Descrição |
|---|---|
| Token de API or interface de programação do aplicativo (API) do Scuba | Um token de API or interface de programação do aplicativo (API) do Scuba que pode ser obtido no endpoint `https://{scuba_hostname}/api/create_token`. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | Sua URL de endpoint REST or transferir estado representacional. Seu endpoint dependerá da [URL da Braze para sua instância](https://scuba.io). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Fazendo upload dos seus dados do Scuba para a Braze {#uploading-your-scuba-data-to-braze}

{% alert important %}
A requisição a seguir usa curl. Para um melhor gerenciamento de requisições de API or interface de programação do aplicativo (API), recomendamos usar um cliente de API or interface de programação do aplicativo (API), como o Postman.
{% endalert %}

Para fazer upload dos seus dados do Scuba para a Braze, faça uma requisição POST para `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` usando o tipo de conteúdo `application/json`:

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

Substitua os seguintes valores:

| Placeholder             | Descrição                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | A URL do endpoint REST or transferir estado representacional da Braze da sua instância atual da Braze. Para saber mais, consulte [Chaves da API or interface de programação do aplicativo (API) REST or transferir estado representacional]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). |
| `BRAZE_API_KEY`         | Sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com a permissão `users.track`.                                                                                                                                      |
| `HOSTNAME`              | O hostname da sua instância atual do Scuba.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Seu token de API or interface de programação do aplicativo (API) do Scuba.                                                                                                                                                                           |
| `TABLE_NAME`            | A tabela à qual seu dataset pertence. Para saber mais, consulte [Glossário: tabela de dataset](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | A propriedade de ator à qual seu dataset pertence. Apenas dados que correspondam a esse nome serão retornados. Para saber mais, consulte [Glossário: propriedade de ator](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | O filtro de busca de público para sua propriedade de ator.                                                                                                                                             |
| `ACTOR_ID`              | O ID da propriedade de ator à qual seu dataset pertence. Esse ID corresponde ao seu `external_id` na Braze. Para saber mais, consulte [Glossário: ator](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | O período inicial como uma data compatível com BQL. Para saber mais, consulte [Sintaxe e uso do BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | O período final como uma data compatível com BQL. Para saber mais, consulte [Sintaxe e uso do BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Opcional**: O número máximo de registros a serem retornados. Se `scuba_record_limit` for omitido, o Scuba retornará no máximo 100 registros. Para alterar esse valor, atribua qualquer número não negativo a `scuba_record_limit`.    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fazendo upload dos seus dados do Scuba para a Braze" }

### Comportamento padrão {#default-behavior}

Por padrão, `update_existing_only` é definido como `false`, o que atualiza seus registros existentes na Braze e também cria novos registros para aqueles que ainda não existem. Para evitar que o Scuba crie novos registros, defina `update_existing_only` como `true`.

### Limite de frequência {#rate-limit}

O Scuba aplica um limite de frequência de 50.000 requisições por minuto a esse endpoint.

## Criando segmentos usando dados comportamentais do Scuba {#creating-segments-using-scubas-behavioral-data}

Depois de [fazer upload dos seus dados](#uploading-your-scuba-data-to-braze), você pode criar segmentos de usuários na Braze usando os dados comportamentais do Scuba.

### Etapa 1: Criar um novo Segment or segmento or segmento {#step-1-create-a-new-segment}

Na Braze, acesse **Público** > **Segments** e selecione **Criar Segment or segmento**. Em seguida, insira um nome para o seu Segment or segmento or segmento.

![Criando um novo segmento na Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Etapa 2: Encontrar e selecionar o atributo do Scuba {#step-2-find-and-select-the-scuba-attribute}

Em **Detalhes do Segment or segmento** > **Filtros**, selecione **Atributos Personalizados**.

![Selecionando o filtro 'Atributo Personalizado' em 'Detalhes do Segment'.]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Selecione **Pesquisar atributos personalizados** e escolha o nome da propriedade de ator que você usou na sua solicitação POST anterior.

![Selecionando a propriedade de ator como um atributo personalizado.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Etapa 3: Configurar o atributo {#step-3-configure-the-attribute}

Ao lado do nome da propriedade de ator, escolha um operador e um valor (se aplicável). Esses valores são determinados pelas propriedades de ator que você definiu no Scuba. Quando terminar, selecione **Salvar**.

![Escolhendo um operador e um valor para o atributo selecionado.]({% image_buster /assets/img/scuba/analytics/operator_end.png %})