---
nav_title: Corresponder itens do catálogo a um array de atributos
article_title: Corresponder itens do catálogo a um array de atributos personalizados
page_order: 2
page_type: reference
description: "Use uma seleção de catálogo e Liquid para exibir linhas do catálogo cujos nomes ou IDs aparecem em um array de atributos personalizados, como uma lista de desejos."
---

# Corresponder itens do catálogo a um array de atributos personalizados {#match-catalog-items-to-a-custom-attribute-array}

> Quando cada usuário mantém uma lista de nomes de produtos salvos em seu perfil, use uma seleção de catálogo junto com Liquid para exibir apenas as linhas do catálogo que aparecem nessa lista — por exemplo, em um e-mail de lista de desejos.

## Sobre este exemplo {#about-this-example}

A Flash & Thread armazena os nomes de produtos salvos de cada cliente em um atributo personalizado de array de strings (`saved_product_names`). O catálogo contém os detalhes completos dos produtos (categoria, preço, URL da imagem, estoque).

As seleções de catálogo podem filtrar colunas do catálogo com base em valores estáticos ou Liquid, incluindo campos de array nas linhas do catálogo. Elas não filtram uma linha do catálogo com base em valores armazenados em um array do perfil de usuário. Para personalizar a partir da lista do usuário, retorne um conjunto amplo de itens do catálogo com uma seleção e, em seguida, use Liquid para manter apenas as linhas que correspondem ao array do perfil.

Este padrão:

1. Atribui o atributo personalizado de array do usuário a uma variável Liquid.
2. Chama `catalog_selection_items` para uma seleção de catálogo pré-filtrada (até 50 itens).
3. Percorre `items` e usa `contains` para corresponder cada campo do catálogo (por exemplo, `name` ou `id`) ao array.

{% alert important %}
Este padrão funciona apenas quando o conjunto de resultados da seleção (até 50 linhas do catálogo) pode plausivelmente conter os itens salvos de cada usuário — por exemplo, catálogos pequenos ou catálogos em que os filtros restringem a seleção o suficiente para cobrir uma lista típica. Se os itens salvos de um usuário estiverem fora das 50 linhas retornadas, o loop não encontra correspondências e a mensagem não renderiza nada para esses itens — nenhum filtro resolve isso no caso geral, porque a seleção não consegue corresponder ao array do perfil do usuário.
{% endalert %}

## Considerações {#considerations}

- Teste o Liquid e os dados do catálogo em um espaço de trabalho de staging antes de enviar para os clientes.
- Como uma seleção retorna no máximo 50 linhas do catálogo, adicione filtros (por exemplo, em estoque, categoria ativa ou faixa de preço) que mantenham os itens salvos prováveis de cada usuário dentro desse conjunto de resultados.
- Este exemplo usa um array de strings no perfil de usuário.
- Para um array de objetos, faça a correspondência com uma propriedade dentro de cada objeto (por exemplo, `product_id`) e ajuste a verificação `contains` ou use um loop `for` sobre os objetos. Consulte [Array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
- O comportamento de `contains` depende do tipo de atributo; para arrays, use `contains` em vez de `==`. Consulte [Lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
- Faça a correspondência com identificadores estáveis (por exemplo, `id` do catálogo) quando os nomes dos produtos podem mudar ou se duplicar.
- Os snippets Liquid neste artigo são exemplos. Valide a renderização nos seus canais (HTML de e-mail, push e assim por diante).

## Configuração {#setup}

Este exemplo pressupõe:

| Ativo | Detalhes |
| --- | --- |
| Atributo personalizado | `saved_product_names` — array de strings (por exemplo, `["linen_shirt", "trail_jacket", "canvas_tote"]`) |
| Catálogo | `apparel_products` com colunas `id`, `category`, `name`, `price`, `inventory`, `image_url` |
| Seleção | `in_stock_apparel` em `apparel_products`, limite de resultados 50, com filtros que excluem linhas irrelevantes (por exemplo, `inventory` maior que `0`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuração" }

### Etapa 1: Criar o catálogo e a seleção {#step-1-create-the-catalog-and-selection}

1. Importe ou sincronize as linhas de produtos em um catálogo chamado `apparel_products`.
2. Crie uma seleção (por exemplo, `in_stock_apparel`) que retorne o máximo de linhas relevantes que você precisar, até o limite de 50 itens.
3. Adicione filtros à seleção para descartar linhas que você nunca quer na mensagem (fora de estoque, categoria errada e assim por diante).

Para a configuração de seleções, consulte [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

### Etapa 2: Adicionar Liquid na sua mensagem {#step-2-add-liquid-in-your-message}

Atribua o array do perfil, carregue a seleção e faça o loop com `contains`:

{% raw %}
```liquid
{% assign saved_product_names = custom_attribute.${saved_product_names} %}
{% catalog_selection_items apparel_products in_stock_apparel %}
{% for item in items %}
{% if saved_product_names contains item.name %}
Product: {{ item.name }}
Category: {{ item.category }}
Price: ${{ item.price }}
Image: {{ item.image_url }}
{% endif %}
{% endfor %}
```
{% endraw %}

Substitua `item.name` por `item.id` (ou outra coluna) se o seu array armazena IDs em vez de nomes de exibição. Adicione espaçamento ou HTML entre os campos conforme o seu canal. Em {% raw %}`${{ item.price }}`{% endraw %}, o `$` é um símbolo de moeda literal que é impresso antes da saída Liquid — ele não faz parte da sintaxe de personalização {% raw %}`${}`{% endraw %} da Braze.

Para gerar esse Liquid automaticamente, abra o modal **Adicionar personalização** (**Itens do catálogo** > **Usar uma seleção**). Consulte [Usando catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use).

### Etapa 3: Pré-visualizar e testar {#step-3-preview-and-test}

Envie mensagens de teste para perfis com diferentes valores de `saved_product_names`. Confirme que apenas as linhas correspondentes do catálogo aparecem e que um array vazio não produz nenhuma linha de produto.

## Artigos relacionados {#related-articles}

- [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Usando catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
- [Lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)
- [Biblioteca de casos de uso Liquid — encontrar uma string dentro de um array]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#misc-string-in-array)