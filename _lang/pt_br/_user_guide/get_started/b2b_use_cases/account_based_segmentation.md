---
nav_title: Segmentação baseada em contas
article_title: Configurar segmentação baseada em conta
page_order: 2
page_type: reference
description: "Saiba como usar vários recursos da Braze para potencializar seus casos de uso de segmentação baseada em contas B2B."
---

# Configurar segmentação baseada em conta {#set-up-account-based-segmentation}

> Esta página mostra como usar vários recursos da Braze para potencializar seus casos de uso de segmentação baseada em contas B2B.

Você pode fazer a segmentação baseada em contas B2B de duas maneiras, dependendo de como você configurou seu [modelo de dados B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/):

- Ao usar [catálogos para seus objetos de negócios](#option-1-when-using-catalogs-for-your-business-objects)
- Ao usar [fontes conectadas para seus objetos de negócios](#option-2-when-using-connected-sources-for-your-business-objects)

## Configuração da segmentação baseada em contas B2B {#setting-up-b2b-account-based-segmentation}

### Opção 1: Ao usar catálogos para seus objetos de negócios {#option-1-when-using-catalogs-for-your-business-objects}

#### Segmentação básica com modelos SQL {#basic-sql-template-segmentation}

Para ajudar você a começar, criamos modelos SQL básicos para segmentação simples baseada em contas.

Digamos que você queira segmentar os usuários que são colaboradores de uma conta corporativa alvo.

1. Acesse **Público** > **Extensões de segmento** > **Criar nova extensão** > **Iniciar com um modelo** e selecione o modelo **Segmento de catálogo para eventos**. <br><br> ![Modal "Selecione um modelo" com opções de segmento de catálogo para eventos ou compras.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>O editor SQL é preenchido automaticamente com um modelo que une os dados de eventos de usuários com os dados do catálogo para segmentar os usuários que se engajam com determinados itens do catálogo. <br><br>![Um editor SQL para uma nova extensão com a guia "Variáveis" aberta.]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. Use a guia **Variáveis** para fornecer os campos necessários para seu modelo antes de gerar seu segmento.<br><br>Para que a Braze identifique os usuários com base no engajamento deles com os itens do catálogo, é necessário fazer o seguinte:
- Selecionar um catálogo que contenha um campo de catálogo
- Selecionar um evento personalizado que contenha uma propriedade de evento
- Corresponder os valores do campo do catálogo e da propriedade do evento

##### Diretrizes de variáveis para casos de uso B2B {#variables-guidelines-for-b2b-use-cases}

Selecione as seguintes variáveis para um caso de uso de segmentação baseada em contas B2B:

| Variável | Propriedade |
| --- | --- |
| Catálogo | Catálogo de contas |
| Campo de catálogo | Id |
| Evento personalizado | account_linked |
| Propriedade do evento personalizado | account_id |
| (Em Filtrar resultados SQL) Campo do catálogo | Classification |
| (Em Filtrar resultados SQL) Valor | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Segmentação SQL sofisticada {#sophisticated-sql-segmentation}

Para uma segmentação mais sofisticada ou complexa, consulte [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/). Para ajudar você a começar, aqui estão alguns modelos SQL que podem dar uma vantagem inicial com a segmentação baseada em contas B2B:

1. Crie um segmento comparando dois filtros em um único catálogo (por exemplo, usuários que trabalham no setor de restaurantes para uma conta de nível empresarial). Você deve incluir o ID do catálogo e o ID do item.

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
;
```

{: start="2"}
2. Crie um segmento comparando dois filtros em dois catálogos separados (como usuários associados a contas corporativas alvo que tenham uma oportunidade aberta de "Stage 3").

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### Opção 2: Ao usar fontes conectadas para seus objetos de negócios {#option-2-when-using-connected-sources-for-your-business-objects}

Para o básico sobre como usar fontes conectadas na segmentação, consulte [Extensões de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/). Use os modelos abordados em [Ao usar catálogos](#option-1-when-using-catalogs-for-your-business-objects) como inspiração para formatar as tabelas de origem, já que você pode formatá-las da maneira que quiser.

## Usando sua extensão baseada em conta em um segmento {#using-your-account-based-extension-in-a-segment}

Depois de criar a segmentação no nível da conta nas etapas acima, você pode incluir diretamente essas extensões de segmento nos seus critérios de direcionamento. Também é fácil acrescentar critérios demográficos incrementais do usuário, como função, engajamento com campanhas anteriores e muito mais. Para saber mais, consulte [Uso de sua extensão em um segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#step-6-use-your-extension-in-a-segment).