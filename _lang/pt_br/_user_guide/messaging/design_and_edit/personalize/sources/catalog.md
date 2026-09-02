---
nav_title: Catálogo
article_title: Catálogo
page_order: 2
description: "Saiba como usar catálogos como fonte de dados para personalizar suas mensagens da Braze com dados que não são de usuários, como detalhes de produtos, feeds de conteúdo e preços."
---

# Catálogo {#catalog}

> Faça referência a dados que não são de usuários em suas mensagens conectando-se a catálogos. Os catálogos armazenam conjuntos de dados estruturados — como informações de produtos, listagens de restaurantes ou feeds de conteúdo — que você pode acessar por meio de Liquid para personalizar qualquer mensagem.

## Como funciona {#how-it-works}

{% raw %}
Após importar dados para um catálogo (por CSV ou API), faça referência aos itens do catálogo em suas mensagens usando a Liquid tag `items`. Por exemplo, para buscar o nome de um produto de um catálogo chamado `products`:

```liquid
{% catalog_items products {{${product_id}}} %}
{{items[0].name}} is back in stock!
```
{% endraw %}

Os catálogos suportam até 1.000 campos por item e podem armazenar milhões de linhas, o que os torna adequados para grandes inventários de produtos e bibliotecas de conteúdo.

## Casos de uso comuns {#common-use-cases}

| Caso de uso | Descrição |
| --- | --- |
| Detalhes de produtos | Insira nomes, descrições, preços e imagens de um catálogo de produtos |
| Listagens de restaurantes ou lojas | Personalize mensagens com detalhes específicos de cada local |
| Recomendações de conteúdo | Faça referência a artigos, vídeos ou outros itens de mídia |
| Informações de eventos | Insira datas de eventos, locais e descrições nas mensagens |
| Ofertas por nível | Associe promoções ao nível de associação ou Segment de um usuário |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso comuns" }

## Gatilhos de catálogo {#catalog-triggers}

Os catálogos também possibilitam o envio de mensagens automatizadas por meio de gatilhos de catálogo. Configure notificações de volta ao estoque e notificações de queda de preço para enviar mensagens automaticamente aos usuários quando os itens do catálogo mudarem.

Para saber mais, consulte [Gatilhos de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers).

## Seleções {#selections}

Use seleções para agrupar itens do catálogo por filtros que você definir. Por exemplo, crie uma seleção de itens abaixo de US$ 20 ou itens em uma categoria específica e, em seguida, faça referência ao conjunto filtrado em suas mensagens.

Para saber mais, consulte [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Primeiros passos {#getting-started}

Para criar e gerenciar catálogos, consulte [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs). Para saber como fazer referência a dados de catálogo em suas mensagens, consulte [Usando catálogos em uma mensagem]({{site.baseurl}}/user_guide/data/activation/catalogs/use).