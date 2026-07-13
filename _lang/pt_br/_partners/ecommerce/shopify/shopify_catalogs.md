---
nav_title: Sincronização de produtos da Shopify
article_title: Sincronização de produtos da Shopify
alias: /shopify_catalogs/
page_order: 5
description: "Este artigo de referência aborda como importar seus produtos da Shopify para os catálogos da Braze."
---

# Sincronização de produtos da Shopify {#shopify-product-sync}

> Você pode sincronizar todos os produtos da sua loja Shopify com um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) da Braze para uma personalização mais profunda do envio de mensagens.

Os catálogos da Shopify serão atualizados quase em tempo real à medida que você fizer edições e alterações nos produtos da sua loja Shopify. É possível enriquecer seu carrinho abandonado, a confirmação do pedido e muito mais com os detalhes e as informações mais atualizadas do produto.

Além de oferecer suporte aos [dados principais de produtos da Shopify](#supported-shopify-catalog-data), você pode sincronizar coleções da Shopify, tags de produtos e metacampos de produtos com o seu catálogo da Braze. Esses campos adicionais possibilitam uma personalização mais rica, seleções de catálogo mais precisas e uma segmentação mais poderosa por meio de [extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension).

## Configure sua sincronização de produtos da Shopify {#set-up}

Se você já instalou sua loja Shopify, ainda poderá sincronizar seus produtos seguindo as instruções desta seção.

### Etapa 1: Ativar a sincronização {#step-1-turn-on-the-sync}

Você pode sincronizar seus produtos com um catálogo da Braze por meio do fluxo de instalação da Shopify ou na página de parceiros da Shopify.

![Etapa 3 do processo de configuração com "Shopify Variant ID" como o "Catalog product identifier".]({% image_buster /assets/img/shopify/sync_products_step1.png %})

### Etapa 2: Selecione o identificador do seu produto {#step-2-select-your-product-identifier}

Selecione o identificador de produto a ser usado como ID do catálogo:
- Shopify Variant ID
- SKU

Os valores de ID e de cabeçalho para o identificador de produto que você escolher só podem incluir letras, números, hífens e sublinhados. Se o identificador do produto não seguir esse formato, a Braze o removerá da sincronização do catálogo.

Esse será o identificador principal que você usará para fazer referência às informações do catálogo da Braze.

{% alert note %}
Se estiver selecionando SKU como ID do catálogo, certifique-se de que todos os seus produtos e variantes na sua loja tenham um SKU definido e que sejam exclusivos.<br><br>
- Se um item não tiver um SKU, a Braze não poderá sincronizar esse produto no catálogo.
- Se você tiver mais de um produto com o mesmo SKU, isso pode causar um comportamento inesperado ou fazer com que as informações do produto sejam substituídas involuntariamente pelo SKU duplicado.
{% endalert %}

### Etapa 3: Configure dados adicionais de produtos (opcional) {#step-3}

Opcionalmente, você pode ativar a sincronização de tags de produtos, coleções da Shopify e metacampos. Ative ou modifique essas configurações após a sincronização inicial na página de parceiros da Shopify.

{% alert note %}
Adicione tags de produtos, coleções da Shopify e metacampos na Shopify primeiro. Se eles não existirem na Shopify, não aparecerão na Braze.
{% endalert %}

![Configurações para sincronizar produtos e variantes da Shopify com a Braze.]({% image_buster /assets/img/shopify/additional_product_data.png %})

{% tabs global %}
{% tab Tags de produtos %}

1. Na página **Sync product data to Braze**, marque a caixa de seleção **Sync product tags** para abrir o modal **Select product tags**.
2. Selecione até 20 tags de produtos para sincronizar com o seu catálogo da Braze. Somente as tags selecionadas serão sincronizadas.

![Modal de seleção de tags de produtos com uma seleção de tags.]({% image_buster /assets/img/shopify/select_product_tags.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Metacampos de produtos %}

1. Se você já possui uma integração com a Shopify, reautorize o app Braze Shopify para instalar os novos escopos necessários para sincronizar produtos. Se você é um novo cliente, vá para a próxima etapa.

![Banner solicitando a reautorização do app Braze Shopify.]({% image_buster /assets/img/shopify/banner_to_reauthorize.png %})

{: start="2"}
2. Selecione **Sync product metafields** para abrir o modal de configuração de metacampos.

![Seção de sincronização de dados de produtos com a Braze, com opções para selecionar entre múltiplas configurações, incluindo coleções.]({% image_buster /assets/img/shopify/select_collections.png %})

{: start="3"}
3. Selecione até 20 metacampos pesquisáveis para sincronizar. Cada um se torna uma coluna separada no seu catálogo para uso em recursos como seleções de catálogo ou extensões de segmento.
- Ao nomear metacampos, observe que espaços se tornam "_" e todos os caracteres especiais são removidos para atender às restrições de nomenclatura de campos do catálogo da Braze.

![Modal para selecionar metacampos de produtos.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

{% subtabs %}
{% subtab Metacampos compatíveis %}

A Braze oferece suporte aos seguintes objetos de metacampos e alguns de seus respectivos tipos.

| Tipo de metacampo | Tipo de dado |
|--------------------------------------------------|--------------------------------------------------------|
| `boolean` | Booleano |
| `color`, `list.color` | String (cor hexadecimal, como `#FFF123`), Array de Strings |
| `date`, `list.date` | String (data ISO 8601), Array de Strings (datas ISO 8601) |
| `date_time`, `list.date_time` | String (datetime ISO 8601), Array de Strings (datetimes ISO 8601) |
| `id`, `list.id` | String, Array de Strings |
| `multi_line_text_field` | String |
| `number_decimal` | String |
| `number_integer` | Inteiro |
| `single_line_text_field`, `list.single_line_text_field` | String, Array de Strings |
| `url`, `list.url` | String (URL), Array de Strings (URLs) |
| `metaobject_reference`, `list.metaobject_reference` | String, Array de Strings |
| `mixed_reference`, `list.mixed_reference` | String, Array de Strings |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configure dados adicionais de produtos (opcional)" }

{% endsubtab %}
{% subtab Metacampos não compatíveis %}

A Braze não oferece suporte a objetos de metacampos, incluindo alguns respectivos tipos de lista:

- `dimension` (`list.dimension`)
- `weight` (`list.weight`)
- `link` (`list.link`)
- `json`
- `list.number_decimal`
- `list.number_integer`
- `money`
- `rating` (`list.rating`)
- `volume` (`list.volume`)
- `rich_text_field`

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Coleções %}

1. Selecione **Sync Shopify collections** para abrir o modal de configuração de coleções.
2. Selecione até 20 coleções para sincronizar.
  - O modal fornece uma lista pesquisável de até 5.000 das coleções criadas ou atualizadas mais recentemente na sua loja Shopify.
  - Coleções selecionadas anteriormente que não estão mais entre as 5.000 principais ainda aparecerão na sua seleção.

{% alert note %}
A Braze usa o ID de coleção da Shopify para identificar coleções sincronizadas, que são então usadas ao criar seleções de catálogo e filtros de segmento.
{% endalert %}

![Modal para selecionar coleções em um menu suspenso.]({% image_buster /assets/img/shopify/selected_collections.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para exemplos de como usar cada tipo de dado de produto, consulte [Casos de uso de catálogos da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/?tab=shopify%20product%20metafields#shopify-catalog-use-cases)
{% endalert %}

### Etapa 4: Acompanhe o progresso da sincronização {#step-4-track-your-sync-progress}

Após salvar sua configuração, a Braze começará a sincronizar seus produtos e atualizará o status para **In Progress** na página de parceiros da Shopify. O tempo de sincronização depende do número de produtos e variantes na sua loja.

Você pode sair da página assim que a sincronização estiver em andamento; a Braze enviará uma notificação no dashboard quando a sincronização for concluída. Após a conclusão, o status será atualizado para **Active** e você poderá visualizar seus produtos selecionando o nome do catálogo na página de parceiros da Shopify.

![Página de configurações de integração com o status de sincronização de produtos.]({% image_buster /assets/img/shopify/track_sync_progress.png %})

Você também pode visualizar tags de produtos, metacampos e coleções sincronizados no seu catálogo da Shopify como novas colunas.

![Catálogo da Shopify com dados sincronizados.]({% image_buster /assets/img/shopify/synced_catalog.png %})

{% alert important %}
Se a sincronização exceder o limite de armazenamento do seu catálogo, a Braze interromperá a sincronização e as novas atualizações de produtos não serão mais refletidas. Entre em contato com seu gerente de sucesso do cliente para fazer upgrade do seu nível, se necessário.
{% endalert %}

### Etapa 5: Gerencie sua configuração {#step-5-manage-your-configuration}

Cada tipo de sincronização possui um cartão de resumo na página de parceiros da Shopify mostrando a contagem total sincronizada, o status atual e um link para o seu catálogo. Selecione o ícone de visualização para ver sua configuração ativa e editá-la.

Você pode modificar a sincronização de produtos da Shopify, incluindo o gerenciamento de tags de produtos, coleções e metacampos de produtos a qualquer momento na página de parceiros da Shopify.

![Página de configurações de integração com uma sincronização ativa de catálogo de produtos.]({% image_buster /assets/img/shopify/active_catalog_sync.png %})

{% alert important %}
Alterar suas seleções sincronizadas pode afetar Campaigns, Canvas ou seleções de catálogo ativas que fazem referência a elas. Atualize o conteúdo ativo para que funcione corretamente ao aplicar as alterações.
{% endalert %}

## Dados de catálogo compatíveis com a Shopify {#supported-shopify-catalog-data}

| Campo | Tipo de dado | Exemplos |
|----------------------|----------------|-----------------------------------------------------------------------------------|
| `id` | string | `45264808411274` quando o identificador de produto do catálogo é **Shopify Variant ID**<br><br>`12345` quando o identificador de produto do catálogo é **SKU** (corresponde ao valor que você selecionou na [Etapa 2](#step-2-select-your-product-identifier)) |
| `store_name` | string | "your-store" (subdomínio da loja Shopify, sem `.myshopify.com`) |
| `shopify_product_id` | number | `7939032613002` (armazenado como número no seu catálogo da Braze; as APIs da Shopify podem retornar esse ID como string) |
| `shopify_variant_id` | number | `45264808411274` (armazenado como número no seu catálogo da Braze; as APIs da Shopify podem retornar esse ID como string) |
| `product_title` | string | "Classic leather jacket" |
| `variant_title` | string | "Large / Red", "Medium" ou "Default Title" para produtos com variante única |
| `status` | string | "active", "draft", "archived" |
| `product_image_url` | string | "https://cdn.shopify.com/s/files/1/0641/0970/7402/files/t_shir.jpg?v=1736538760" |
| `variant_image_url` | string | Mesma URL no estilo CDN da imagem do produto quando não existe imagem de variante; caso contrário, uma URL de imagem específica da variante |
| `vendor` | string | "Flash and Thread", "PantsLabyrinth" |
| `product_type` | string | "Outerwear", "T-Shirts" (do campo **Product type** do produto na Shopify) |
| `product_url` | string | "https://your-store.myshopify.com/products/classic-leather-jacket" |
| `product_handle` | string | "classic-leather-jacket" |
| `published_scope` | string | "web", "global" |
| `price` | number | `10.00`, `24.99`<br><br>A Shopify frequentemente retorna preços como strings (por exemplo, `"199.00"` na REST Admin API). A Braze os converte em números para este campo do catálogo. |
| `compare_at_price` | number | `15.00` quando **Compare at price** está definido na Shopify<br><br>`0` quando a Shopify não possui um preço de comparação. As APIs da Shopify normalmente retornam `null` para um preço de comparação não definido; a Braze armazena `0` no catálogo para que o campo seja sempre numérico (esse é um padrão da Braze, não um valor que a Shopify envia como `0`). |
| `inventory_quantity` | number | `20`, `0` ou um valor negativo quando a sobrevenda é permitida (por exemplo, `-18`) |
| `options` | string | "Size,Color"<br><br>A Shopify permite até três tipos de opção por produto (por exemplo, Size, Color, Material). O valor de `options` é uma lista separada por vírgulas desses nomes. |
| `option_values` | string | "Medium,Red", "Large,Red"<br><br>Cada valor corresponde à mesma ordem de `options` (até três valores). |
| `sku` | string | "12345", "SKU-001-RED-L" |
| `product_tags` | array | `["Summer", "Sale", "New"]`<br><br>Requer a sincronização de tags de produtos. |
| `collection_ids` | array | `[123456789012, 987654321098]` (IDs de coleção da Shopify)<br><br>Requer a sincronização de coleções da Shopify. |
| `Metafield columns` | Varia por tipo | Cada metacampo sincronizado aparece como uma coluna separada nomeada pela sua chave. Consulte [Metacampos compatíveis](#step-3) na guia "Metacampos de produtos" da etapa 3 para mais informações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dados de catálogo compatíveis com a Shopify" }

{% alert warning %}
Seu catálogo da Shopify é gerenciado pela Shopify. Para atualizar seu catálogo, faça alterações diretamente na sua loja Shopify e elas serão sincronizadas automaticamente com a Braze. Para excluir seu catálogo da Shopify, acesse a página de parceiros da Shopify na Braze e [desative a sincronização](#deactivate).
{% endalert %}

## Casos de uso de catálogos da Shopify {#shopify-catalog-use-cases}

Esses casos de uso mostram como você pode usar os dados sincronizados do catálogo da Shopify para personalizar mensagens.

{% alert warning %}
A Braze sincroniza até 250 variantes de cada produto da Shopify no seu catálogo. Variantes além desse limite não são sincronizadas. Se você precisar de mais de 250 variantes por produto, entre em contato com seu gerente de sucesso do cliente da Braze.
{% endalert %}

{% tabs %}
{% tab Tags de produtos %}

Use tags de produtos para personalizar mensagens com base em como seus produtos estão categorizados na Shopify. Por exemplo, você pode enviar uma promoção apresentando todos os produtos com a tag "Summer Sale" por meio de uma [seleção de catálogo]({{site.baseurl}}/catalog_selections), ou criar um segmento de usuários que compraram produtos com a tag "Premium".

As tags de produtos são armazenadas como um campo de array em cada item do catálogo. Para configurar a sincronização de tags de produtos, consulte [Tags de produtos da Shopify](#shopify-product-tags).

### Seleção de catálogo {#catalog-selection}

1. Na Shopify, atribua a tag de produto "Women's" aos produtos relevantes.

![Um tipo de produto "Women's - Sweaters" com as tags "Women's", "Sweaters" e "Men".]({% image_buster /assets/img/shopify/product_tag_womens.png %}){: style="max-width:40%;"}

{: start="2"}
2. Na Braze, ative a sincronização de tags e selecione a tag de produto "Women's".

![Modal para selecionar tags de produtos da Shopify, com 15 tags relacionadas a roupas selecionadas, incluindo "Women's".]({% image_buster /assets/img/shopify/select_product_tags_womens.png %}){: style="max-width:80%;"}

### Personalização {#personalization}

{% alert note %}
Ao referenciar tags de produtos ou coleções em seleções de catálogo, use apenas o valor em si, sem os colchetes `[]` ou aspas `""` que aparecem nos dados do catálogo. Por exemplo, se uma tag de produto aparece como `["Women's"]` no seu catálogo, escreva `Women's` no filtro da sua seleção.
{% endalert %}

1. Crie uma seleção de catálogo que filtre produtos que possuam a respectiva tag de produto, como "Women's". Você só pode usar um campo de array único em uma única seleção de catálogo, e até 50 produtos na sua seleção de catálogo.

![Uma seleção de catálogo que filtra tags de produtos que possuem o atributo "Women's".]({% image_buster /assets/img/shopify/edit_product_tags_selection.png %})

{: start="2"}
2. No criador de mensagens, adicione a seleção onde você deseja inserir os produtos da seleção de catálogo com a tag "Women's". Por exemplo, você pode usar um bloco de produto HTML como este:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Ou, se você quiser mencionar produtos específicos com a tag "Women's" em uma notificação por push, pode usar a ferramenta **Add Personalization** e especificar os itens do seu catálogo.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Criador de notificações por push com uma seleção de catálogo trazendo três itens com uma tag de produto.]({% image_buster /assets/img/shopify/add_personalization_product_tags.png %})

### Segmentação por catálogo (SQL) {#catalog-segmentation-sql}

Use [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para criar segmentos com base em usuários que interagiram com uma tag de produto. Por exemplo, para encontrar usuários que se engajaram com itens do catálogo que contêm uma tag de produto específica, use esta consulta:

{% raw %}
```liquid
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific product tag. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'product_tags' AND ARRAY_CONTAINS('<product_tag_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% tab Metacampos de produtos %}

Use metacampos de produtos para personalizar mensagens com detalhes personalizados de produtos além dos campos padrão da Shopify. Por exemplo, inclua instruções de cuidado em uma confirmação de pedido, exiba o país de origem em um e-mail de recomendação ou segmente usuários que compraram um material específico.

Cada metacampo sincronizado se torna uma coluna separada no seu catálogo, com o tipo de dado determinado pelo tipo de metacampo. Para configurar a sincronização de metacampos, consulte [Metacampos de produtos da Shopify](#shopify-product-metafields).

### Seleção de catálogo

1. Na Shopify, defina o metacampo de produto `seasonal` nos produtos relevantes como `summer` (esse é um valor de metacampo, não uma tag de produto).

![Modal para adicionar metacampos de produtos, incluindo o metacampo seasonal com o valor summer.]({% image_buster /assets/img/shopify/summer_product_metafield.png %}){: style="max-width:80%;"}

{: start="2"}
2. Na Braze, ative a sincronização de metacampos e selecione `custom.seasonal` (ou o namespace e a chave que correspondem ao seu metacampo da Shopify).

![Modal para selecionar metacampos de produtos, com um menu suspenso expandido que tem quatro itens selecionados, incluindo custom.seasonal.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

### Personalização

1. Crie uma [seleção de catálogo]({{site.baseurl}}/catalog_selections) que filtre metacampos que incluam o respectivo valor.

![Uma seleção de catálogo que filtra metacampos que possuem o atributo summer.]({% image_buster /assets/img/shopify/metafields_selection.png %})

{: start="2"}
2. No criador de mensagens, adicione a seleção onde você deseja inserir metacampos de produtos. Por exemplo, você pode usar um bloco de produto HTML como este:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Ou, se você quiser mencionar produtos específicos com um valor de metacampo específico em uma notificação por push, pode usar a ferramenta **Add Personalization** e especificar os itens do seu catálogo.

{% raw %}
```liquid
Check out the latest summer products:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Criador de notificações por push com uma seleção de catálogo trazendo três itens usando uma seleção baseada em metacampos.]({% image_buster /assets/img/shopify/add_personalization_metafields.png %})

### Segmentação por catálogo (SQL)

Use [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para criar segmentos com base em usuários que interagiram com um metacampo de produto. Por exemplo, para encontrar usuários que dispararam um evento de e-commerce com um produto cujo array de metacampos contém um valor específico, use esta consulta:

{% raw %}
```sql
-- -----------------------------------------------------------------------------
-- When the metafield is stored as a JSON array in catalog field_value (for example,
-- '["winter","summer"]' or a list-type Shopify metafield serialized to JSON),
-- use ARRAY_CONTAINS like product_tags. Cast the element you search for to
-- VARIANT so types match the parsed array elements.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product whose
-- metafield array contains a specific value (for example, segment on "seasonal").
-- For a date range, add events.time >= $start_date AND events.time <= $end_date.
-- For first/last triggered, reuse the CTE pattern from Template 3 with this
-- ARRAY_CONTAINS predicate instead of items.field_value = '<metafield_value>'.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND ARRAY_CONTAINS('<array_element_value>'::VARIANT, TRY_PARSE_JSON(items.field_value));
```
{% endraw %}

Se você quiser segmentar clientes que fizeram um pedido com metacampos de produto específicos, use um dos seguintes modelos SQL de extensão de segmento (todo o período, período específico, primeiro ou último disparo de um evento).

{% raw %}
```sql
-- =============================================================================
-- Segment Extension: Metafields × Ecommerce Events — Example SQL Templates
-- =============================================================================
-- Metafield column names in CATALOGS_ITEMS_SHARED follow:
--   field_name = 'metafield_<namespace>_<key>'
-- Replace placeholders: app_group_id, catalog_id, event name, and the metafield
-- field_name + value. For array-type metafield values, use ARRAY_CONTAINS
-- with TRY_PARSE_JSON(items.field_value) similar to the product_tags example.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Template 1: Map metafields to event triggers (all time)
-- -----------------------------------------------------------------------------
-- Users who have ever triggered the ecommerce event with a product that has
-- the given metafield value. Event-agnostic: change events.name for the
-- desired event (e.g. ecommerce.order_placed, ecommerce.product_viewed).
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who have engaged with catalog items that have a specific
-- product metafield. Joins the catalog to custom events by matching
-- events.properties.products (e.g. variant_id) to catalog items.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 2: Map metafields to event triggers (for a specific period)
-- -----------------------------------------------------------------------------
-- Same as Template 1, restricted to events within a time window. Use
-- $start_date and $end_date (Segment Extension parameters) or literal
-- Unix timestamps.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product that has
-- the given metafield value within the specified time range.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND events.time >= $start_date
    AND events.time <= $end_date
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 3: Map metafields — first or last triggered an event
-- -----------------------------------------------------------------------------
-- Users for whom the *first* (earliest) or *last* (most recent) matching
-- event (by time) involved a product with the given metafield. Switch
-- ORDER BY to time ASC for first, time DESC for last.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users whose first (or last) occurrence of the ecommerce event
-- involved a catalog item with the specified metafield value.
WITH events_with_catalog_metafield AS (
    SELECT
        events.user_id,
        events.time,
        events.id AS event_id,
        ROW_NUMBER() OVER (
            PARTITION BY events.user_id
            ORDER BY events.time ASC   -- use DESC for "last triggered"
        ) AS rn
    FROM
        USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
        LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
        JOIN CATALOGS_ITEMS_SHARED AS items ON (
            (
                items.field_name = 'id'
                AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
            items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
        )
    WHERE
        events.name = 'ecommerce.order_placed'
        AND events.app_group_id = '<app_group_id>'
        AND items.catalog_id = '<catalog_id>'
        AND items.field_name = '<metafield_name>'
        AND items.field_value = '<metafield_value>'
)
SELECT
    user_id
FROM
    events_with_catalog_metafield
WHERE
    rn = 1;
```
{% endraw %}

{% endtab %}
{% tab Coleções %}

Use coleções da Shopify para trazer agrupamentos de produtos curados para suas mensagens, que também são usados no seu site e experiências de app da Shopify. Por exemplo, destaque "Novidades" em um e-mail promocional, faça venda cruzada de "Mais Vendidos" em um Canvas de carrinho abandonado ou segmente usuários que navegaram por uma coleção sazonal.

### Seleção de catálogo

1. Na Shopify, crie uma coleção "New Women's Products - In Stock" com seus produtos de melhor desempenho.

![Lista de coleções da Shopify, incluindo "New Women's Products - In Stock".]({% image_buster /assets/img/shopify/shopify_collections.png %})

{: start="2"}
2. Na Braze, ative a sincronização de coleções e selecione "Women's Products - In Stock".

![Modal para selecionar coleções, com um menu suspenso expandido que seleciona quatro coleções.]({% image_buster /assets/img/shopify/select_collections_id.png %})

{% alert note %}
Para coleções da Shopify, você deve usar o **Collection ID**, que é encontrado na URL ao visualizar a coleção. Por exemplo, uma URL `https://admin.shopify.com/store/se-team-ecommerce/collections/470645342446` tem o Collection ID `470645342446`.
{% endalert %}

### Personalização

{% alert note %}
Ao referenciar IDs de coleção em seleções de catálogo, use apenas o valor numérico do ID, sem os colchetes `[]` que aparecem nos dados do catálogo. Por exemplo, se os IDs de coleção aparecem como `[123456789012, 987654321098]` no seu catálogo, escreva apenas o ID numérico (como `470645342446`) no filtro da sua seleção.
{% endalert %}

1. Crie uma seleção de catálogo chamada "New Women's Products - In Stock" que filtre produtos que possuam o ID dessa coleção. Você só pode usar um campo de array único em uma única seleção de catálogo, e até 50 produtos na sua coleção.
 - Você também pode criar suas próprias seleções personalizadas filtrando pelo campo **Collections**.

![Uma seleção de catálogo que filtra coleções que possuem o atributo Collection ID "470645342446".]({% image_buster /assets/img/shopify/collections_selection.png %})

{: start="2"}
2. Na sua mensagem, insira sua coleção usando a seleção criada ou referenciando diretamente a coleção. Por exemplo, você pode usar um bloco de produto HTML como este:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
      {% if url == blank %}
      <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      {% else %}
      <a href="{{ url }}" style="text-decoration:none;">
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      </a>
      {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Ou, se você quiser mencionar novos produtos específicos em uma notificação por push, pode usar a ferramenta **Add Personalization** e especificar os itens do seu catálogo.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Criador de notificações por push com uma seleção de catálogo trazendo três itens com uma tag de produto.]({% image_buster /assets/img/shopify/add_personalization_collections.png %})

### Segmentação por catálogo (SQL)

Crie um segmento de usuários que interagiram com uma coleção. Use [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para criar segmentos com base na associação a coleções. Por exemplo, para encontrar usuários que compraram produtos de uma coleção específica no último ano, use esta consulta:

{% raw %}
```json
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific collection ID. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'collection_ids' AND ARRAY_CONTAINS('<collection_ids_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Você também pode configurar [notificações de queda de preço]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) e [notificações de reposição de estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)!<br><br> Note que, para cada caso de uso, você deve criar um evento personalizado que capture o status de inscrição de um usuário no seu catálogo. O evento personalizado requer uma propriedade de evento que mapeie o [SKU ou Shopify Variant ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) que você selecionou como parte da sincronização de produtos da Shopify.
{% endalert %}

## Desativar a sincronização de produtos {#deactivate}

A desativação do recurso de sincronização de produtos da Shopify excluirá o catálogo completo e os produtos. Isso também pode afetar quaisquer mensagens que possam estar usando ativamente os dados do produto desse catálogo. Confirme se você atualizou ou pausou essas Campaigns ou Canvas antes da desativação, pois isso pode resultar no envio de mensagens sem detalhes do produto. Não exclua o catálogo da Shopify diretamente na página de catálogos.

## Solução de problemas {#troubleshooting}

Se a sincronização de produtos da Shopify apresentar um erro, ele pode ser resultado dos seguintes problemas. Siga as instruções sobre como corrigir o problema e resolver a sincronização:

| Erro | Motivo | Solução |
| --- | --- | --- |
| Erro do servidor | Isso ocorre se houver um erro de servidor no lado da Shopify quando tentamos sincronizar seus produtos. | [Desative a sincronização](#deactivate) e sincronize novamente todo o seu inventário de produtos. |
| SKU duplicado | Isso ocorre se você usar um SKU como ID do item do catálogo e tiver produtos com o mesmo SKU. Como o ID do item do catálogo deve ser exclusivo, todos os seus produtos devem ter SKUs exclusivos. | Faça uma auditoria na sua lista completa de produtos e variantes na Shopify para garantir que não haja SKUs duplicados. Se houver SKUs duplicados, atualize-os para que sejam SKUs exclusivos somente na sua conta da loja Shopify. Depois que isso for corrigido, [desative a sincronização](#deactivate) e sincronize novamente todo o seu inventário de produtos. |
| Limite de catálogo excedido | Isso ocorre se você exceder o limite do catálogo. A Braze não poderá concluir a sincronização ou manter a sincronização ativa devido à falta de espaço de armazenamento disponível. | Há duas soluções para esse problema:<br><br>1. Entre em contato com o gerente da sua conta para fazer upgrade do seu nível e aumentar o limite do seu catálogo.<br><br>2. Libere espaço de armazenamento excluindo qualquer um dos seguintes itens:<br>- Itens de catálogo de outros catálogos<br>- Outros catálogos<br>- Seleções criadas<br><br> Depois de usar qualquer uma das soluções, a sincronização deve ser desativada e reativada em seguida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solução de problemas" }