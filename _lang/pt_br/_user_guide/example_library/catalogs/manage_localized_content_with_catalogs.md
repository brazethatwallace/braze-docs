---
nav_title: Conteúdo localizado em catálogos
article_title: Gerenciar conteúdo localizado com catálogos da Braze
page_order: 3
page_type: reference
description: "Armazene textos, preços e URLs de imagens localizados em catálogos da Braze e resolva o idioma correto no momento do envio."
---

# Gerenciar conteúdo localizado com catálogos da Braze {#manage-localized-content-with-braze-catalogs}

> Armazene strings e URLs localizados em catálogos para que cada usuário receba o conteúdo no seu idioma a partir de uma única Campaign ou Canvas, sem precisar de variantes separadas por localidade.

## Sobre este exemplo {#about-this-example}

PantsLabyrinth, um varejista de roupas fictício, vende seus produtos na América do Norte e na Europa. Nomes de produtos, preços e imagens principais variam por idioma, mas o marketing quer um único modelo de e-mail ou push que personalize no momento do envio.

Este exemplo cobre três padrões de catálogo que leem o {% raw %}`${language}`{% endraw %} [atributo padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) do usuário (coletado pelo SDK a partir da localidade do dispositivo):

- Campos de objeto JSON: todas as localidades em uma única linha por item
- Colunas planas por idioma: `header_en`, `header_fr` e assim por diante
- Catálogo separado por idioma: nome dinâmico do catálogo, como `pantslabyrinth-promo-en`

Use catálogos quando o conteúdo localizado for dados estruturados (produtos, promoções, URLs de imagens). Para textos livres de mensagens em e-mail ou push, prefira [mensagens multi-idioma]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) quando seus canais as suportarem. Para comparar padrões de localização de forma mais ampla, consulte [Gerenciamento de tradução]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management).

## Considerações {#considerations}

- Os exemplos são ilustrativos. Confirme a formatação e o uso de maiúsculas/minúsculas de {% raw %}`${language}`{% endraw %} na sua base de usuários antes de nomear chaves ou sufixos do catálogo.
- Para os Métodos 1 e 2, se {% raw %}`${language}`{% endraw %} estiver em branco ou não corresponder a uma chave ou campo do catálogo, a saída localizada pode ficar vazia — verifique cada campo de forma independente e recorra a um padrão (por exemplo, inglês).
- Para o Método 3, crie uma lista de permissão dos códigos de idioma suportados antes de construir o nome do catálogo; um catálogo ausente interrompe a mensagem.
- [Objetos JSON]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types) em catálogos podem ser criados ou atualizados pela API ou por [Cloud Data Ingestion (CDI) para catálogos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data), e não por upload de CSV.
- O Método 2 suporta manutenção por CSV, mas multiplica as colunas conforme os idiomas aumentam. Arquivos CSV suportam até [1.000 colunas]({{site.baseurl}}/user_guide/data/activation/catalogs/create#step-1-review-your-csv-file).
- O Método 3 requer um catálogo para cada código de idioma que chega à tag `catalog_items`. Se o catálogo não existir, a Braze interrompe a mensagem. Um ID de item ausente em um catálogo existente retorna um array de itens vazio.
- Liquid tags de catálogo não podem ser usadas [recursivamente]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- [Seleções de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) suportam até 10 filtros e retornam até 50 itens — valide os filtros contra o schema do seu catálogo.
- Revise os [níveis de armazenamento de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers) se você mantiver feeds de produtos grandes com múltiplas localidades.

## Configuração {#setup}

### Etapa 1: Escolha uma estrutura de catálogo {#step-1-choose-a-catalog-structure}

Escolha uma estrutura de catálogo usando a orientação desta tabela.

| Método | Melhor quando | Compensação |
| --- | --- | --- |
| Campos de objeto JSON | Catálogo de tamanho médio; uma linha por item; atualizações via API ou CDI | Adicionar um idioma atualiza cada item via API; sem CSV para campos JSON |
| Campos planos por idioma | Poucos idiomas e campos; equipes não técnicas usam CSV | Cada novo idioma adiciona colunas; a nomenclatura dos campos precisa ser consistente |
| Catálogo por idioma | Feeds grandes por localidade ou responsáveis separados por localidade; CSV por idioma | Cada código de idioma na lista de permissão precisa de um catálogo; catálogos ausentes interrompem o envio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Escolha uma estrutura de catálogo" }

### Etapa 2: Crie o catálogo e os itens {#step-2-create-the-catalog-and-items}

1. Acesse **Data Settings** > **Catalogs** e crie um catálogo (ou vários catálogos para o Método 3).
2. Adicione campos e itens com base na estrutura escolhida. Consulte [Criar um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create).
3. (Opcional) Crie uma [seleção de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para filtrar itens — por exemplo, por `category` correspondente a um atributo personalizado do usuário.

{% tabs local %}
{% tab Método 1: Campos JSON %}
Exemplo de item no catálogo `PantsLabyrinth_Product_Copy`:

| Item | Valor |
| --- | --- |
| `id` | `trail-runner-001` |
| `name` | `{"EN":"Trail Runner","FR":"Chaussure de trail","DE":"Trailrunner"}` |
| `category` | `footwear` |
| `url` | `https://pantslabyrinth.shop/products/trail-runner-001` |
| `price` | `{"EN":"$120 USD","FR":"112 EUR","DE":"112 EUR"}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemplo de item de catálogo com campos JSON de localidade" }

{% endtab %}
{% tab Método 2: Campos planos %}
Exemplo de item no catálogo `PantsLabyrinth_Promo_Copy`:

| Item | Valor |
| --- | --- |
| `id` | `spring-sale` |
| `header_en` | `Spring trail sale` |
| `header_fr` | `Soldes de printemps` |
| `body_en` | `Save on trail runners this week.` |
| `body_fr` | `Économisez sur les chaussures de trail cette semaine.` |
| `cta_text_en` | `Shop now` |
| `cta_text_fr` | `Acheter` |
| `img_src_en` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
| `img_src_fr` | `https://cdn.pantslabyrinth.shop/fr/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemplo de item de catálogo com campos planos por idioma" }

{% endtab %}
{% tab Método 3: Catálogo por idioma %}
Crie um catálogo por idioma com os mesmos campos. Por exemplo, repita o mesmo `id` e campos em `pantslabyrinth-promo-fr` e `pantslabyrinth-promo-de` com valores localizados.

Exemplo de item em `pantslabyrinth-promo-en`:

| Item | Valor |
| --- | --- |
| `id` | `spring-sale` |
| `header` | `Spring trail sale` |
| `body` | `Save on trail runners this week.` |
| `cta_text` | `Shop now` |
| `img_src` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemplo de item em um catálogo por idioma em inglês" }

{% endtab %}
{% endtabs %}

### Etapa 3: Adicione Liquid à sua mensagem {#step-3-add-liquid-to-your-message}

Selecione o padrão Liquid que corresponde à estrutura de catálogo escolhida na Etapa 1.

{% tabs local %}
{% tab Método 1: Campos JSON %}
Armazene todas as localidades em campos de objeto JSON em uma única linha do catálogo e use o filtro `property_accessor` para ler as chaves `name` e `price` que correspondem a {% raw %}`${language}`{% endraw %} (normalizado para maiúsculas). Verifique cada campo de forma independente e recorra a `EN` quando o campo estiver em branco, para que uma localidade com nome mas sem preço ainda receba um preço em inglês.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Product_Copy trail-runner-001 %}
{% assign lang = ${language} | upcase %}
{% assign localized_name = items[0].name | property_accessor: lang %}
{% assign localized_price = items[0].price | property_accessor: lang %}
{% if localized_name == blank %}
  {% assign localized_name = items[0].name | property_accessor: 'EN' %}
{% endif %}
{% if localized_price == blank %}
  {% assign localized_price = items[0].price | property_accessor: 'EN' %}
{% endif %}
Product: {{ localized_name }}
Price: {{ localized_price }}
```
{% endraw %}

Consulte [Filtro property accessor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter).
{% endtab %}
{% tab Método 2: Campos planos %}
Construa nomes de campo dinâmicos a partir de {% raw %}`${language}`{% endraw %} (normalizado para minúsculas) e leia esses campos do item com busca por colchetes. Por exemplo, {% raw %}`items[0][header_field]`{% endraw %} lê o cabeçalho para o idioma resolvido. Verifique cada campo de forma independente e recorra à coluna em inglês quando o campo estiver em branco, para que uma localidade com cabeçalho mas sem corpo ainda receba o texto do corpo em inglês.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Promo_Copy spring-sale %}
{% assign lang = ${language} | downcase %}
{% assign header_field = 'header_' | append: lang %}
{% assign body_field = 'body_' | append: lang %}
{% assign cta_field = 'cta_text_' | append: lang %}
{% assign img_field = 'img_src_' | append: lang %}
{% assign header_val = items[0][header_field] %}
{% assign body_val = items[0][body_field] %}
{% assign cta_val = items[0][cta_field] %}
{% assign img_val = items[0][img_field] %}
{% if header_val == blank %}
  {% assign header_val = items[0].header_en %}
{% endif %}
{% if body_val == blank %}
  {% assign body_val = items[0].body_en %}
{% endif %}
{% if cta_val == blank %}
  {% assign cta_val = items[0].cta_text_en %}
{% endif %}
{% if img_val == blank %}
  {% assign img_val = items[0].img_src_en %}
{% endif %}
<img src="{{ img_val }}" alt="" />
<h2>{{ header_val }}</h2>
<p>{{ body_val }}</p>
<a href="#">{{ cta_val }}</a>
```
{% endraw %}
{% endtab %}
{% tab Método 3: Catálogo por idioma %}
{% alert warning %}
Se o nome do catálogo que você passa para `catalog_items` não existir, a Braze interrompe a mensagem. Crie uma lista de permissão dos códigos de idioma suportados antes de construir o nome do catálogo. Um ID de item ausente em um catálogo existente retorna um array de itens vazio — nesse caso, você pode recorrer ao catálogo em inglês.
{% endalert %}

Crie uma lista de permissão dos códigos de idioma que possuem catálogos correspondentes (aqui `en`, `fr` e `de`), defina valores não suportados ou em branco como `en` e consulte o item. Se o ID do item estiver ausente naquele catálogo, recorra ao catálogo em inglês.

{% raw %}
```liquid
{% assign lang = ${language} | downcase %}
{% assign supported = 'en,fr,de' | split: ',' %}
{% if supported contains lang %}{% else %}{% assign lang = 'en' %}{% endif %}
{% assign theCatalog = 'pantslabyrinth-promo-' | append: lang %}
{% catalog_items {{ theCatalog }} spring-sale %}
{% if items[0] == blank %}
  {% catalog_items pantslabyrinth-promo-en spring-sale %}
{% endif %}
<img src="{{ items[0].img_src }}" alt="" />
<h2>{{ items[0].header }}</h2>
<p>{{ items[0].body }}</p>
<a href="#">{{ items[0].cta_text }}</a>
```
{% endraw %}

Consulte [Usando modelos em nomes de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create#template-catalog-names) e [Interrupção de mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).
{% endtab %}
{% endtabs %}

#### Seleção opcional de catálogo por categoria {#optional-catalog-selection-by-category}

Filtre itens antes da personalização — por exemplo, promoções de calçados para usuários com `preferred_category = footwear`:

{% raw %}
```liquid
{% catalog_selection_items PantsLabyrinth_Product_Copy footwear_promos %}
{% for item in items %}
  {{ item.name }}
{% endfor %}
```
{% endraw %}

Defina a seleção no dashboard com filtros na sua coluna `category` e atributos de usuário conforme necessário.

### Etapa 4: Prévia e teste {#step-4-preview-and-test}

1. Use **Preview as User** com perfis de usuário que tenham diferentes valores de {% raw %}`${language}`{% endraw %}.
2. Confirme o conteúdo de fallback quando o idioma estiver ausente ou não for suportado, incluindo localidades parciais (por exemplo, um nome sem preço).
3. Para o Método 3, confirme que cada idioma na lista de permissão possui um catálogo correspondente e que códigos de idioma não suportados mapeiam para o seu catálogo padrão sem interromper o envio.

## Artigos relacionados {#related-articles}

- [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Usar catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Criar um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Filtros avançados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)
- [Localização]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Mensagens multi-idioma]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Sincronizar e excluir dados de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)
- [Interromper mensagens Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)