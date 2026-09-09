---
nav_title: Seleções
article_title: Seleções
page_order: 5
alias: /catalog_selections/
description: "Este artigo de referência aborda como criar e usar seleções com seus catálogos para fazer referência a dados em suas Campaigns da Braze."
---

# Seleções {#selections}

> Seleções são grupos de dados que você pode usar para personalizar uma mensagem para cada usuário em sua Campaign. Ao usar uma seleção, você está basicamente configurando filtros personalizados com base em colunas específicas do seu catálogo. Isso pode incluir filtros por marca, tamanho, local, data de adição e muito mais. Isso dá a você controle sobre o que está sendo mostrado aos usuários, permitindo que você defina critérios que os itens devem atender primeiro.<br><br>Esta página aborda como criar e usar seleções com seus catálogos.

Depois de criar um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs), você pode fazer referência adicional aos dados do catálogo incorporando seleções em suas Campaigns ou recomendações da Braze.

![A seção Seleções em um catálogo de exemplo.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## O que você precisa saber {#things-to-know}

- Você pode criar até 30 seleções por catálogo.
- Você pode adicionar até 10 filtros por seleção.
- As seleções são ótimas para refinar recomendações a partir de dados de catálogo da Braze. Se você está procurando inspiração, confira [Sobre recomendação de itens]({{site.baseurl}}/user_guide/brazeai/item_recommendations) para exemplos de casos de uso.

## Filtros de geolocalização {#geolocation-filters}

Se o seu catálogo inclui um [tipo de campo Geolocalização]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types), você pode usar filtros baseados em geolocalização nas suas seleções para exibir itens do catálogo com base na proximidade a um ponto geográfico.

Dois operadores de geolocalização estão disponíveis:

| Operador | Descrição |
| -------- | --------- |
| `geo within` | Retorna itens cujo campo de geolocalização está dentro de um raio especificado a partir de um ponto central. |
| `geo outside` | Retorna itens cujo campo de geolocalização está fora de um raio especificado a partir de um ponto central. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando um filtro de geolocalização é aplicado, os resultados são classificados por distância, com o item mais próximo aparecendo primeiro.

### Definindo o ponto central com Liquid {#setting-the-center-point-with-liquid}

Você pode definir o ponto central dinamicamente usando Liquid. Por exemplo, para filtrar itens em relação à localização mais recente de cada usuário, use o atributo {% raw %}`{{${most_recent_location}}}`{% endraw %} como valor do filtro:

{% raw %}
```
{{${most_recent_location}}}
```
{% endraw %}

### Caso de uso: mostrar as lojas mais próximas {#use-case-show-the-nearest-store-locations}

Digamos que seu catálogo contém um campo `store_location` do tipo Geolocalização. Você pode criar uma seleção que usa o operador `geo within` para retornar locais de lojas dentro de um raio definido a partir da localização mais recente de cada usuário. Defina o valor do filtro como {% raw %}`{{${most_recent_location}}}`{% endraw %} para que o ponto central seja atualizado por usuário. Como os resultados são classificados por distância, o primeiro item retornado é sempre a loja mais próxima.

## Criando uma seleção {#creating-a-selection}

Para criar uma seleção, faça o seguinte.

1. Acesse **Catalogs** e selecione seu catálogo na lista.
2. Selecione a guia **Selection** e clique em **Create Selection**.
3. Dê um nome à sua seleção e uma descrição opcional.
4. Em **Filter Field**, selecione a coluna do catálogo pela qual você deseja filtrar. Campos de string com mais de 1.000 caracteres não podem ser selecionados para filtros.
5. Termine de definir seus critérios de filtro selecionando o operador relevante (por exemplo, "equals" ou "does not equal") e o atributo.
6. Na seção **Sort type**, determine como os resultados são classificados. Por padrão, os resultados são retornados sem uma ordem específica. Para especificar a classificação por um campo específico, desative **Randomize Sort Order** e especifique o **Sort Field** e a **Sort Order** (crescente ou decrescente).
7. Na seção **Results limit**, insira o limite de resultados (até 50).
8. Selecione **Create Selection**.

### Testar e visualizar {#test-and-preview}

Depois de criar uma seleção, você pode usar a seção **prévia for user** para visualizar o que uma seleção retornaria para um usuário aleatório ou um usuário específico. Para seleções que usam personalização, você só pode visualizar a prévia após selecionar um usuário.

### Liquid nos resultados de seleção {#liquid-in-selection-results}

O uso de qualquer Liquid em catálogos, como atributos personalizados e eventos personalizados, pode resultar em resultados diferentes retornados para cada usuário na sua seleção.

{% alert note %}
O Liquid de Connected Content não é compatível com essas configurações de filtro.
{% endalert %}

![Configurações de filtro para seleção de catálogo com o atributo definido como um atributo personalizado Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Usando seleções no envio de mensagens {#using-selections-in-messaging}

Após criar sua seleção, personalize suas mensagens com Liquid para inserir os itens filtrados desse catálogo. Você pode fazer com que a Braze gere o Liquid para você a partir da janela de personalização encontrada nos criadores de mensagens:

1. Em qualquer criador de mensagem que ofereça suporte à personalização, selecione <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Adicionar personalização"></i> **Adicionar personalização** para abrir a janela de personalização.
2. Em **Tipo de personalização**, selecione **Catalog Items**.
3. Selecione o nome do seu catálogo.
4. Em **Método de seleção de itens**, selecione **Usar uma seleção**.
4. Selecione sua seleção na lista.
5. Em **Informações a exibir**, selecione quais campos do catálogo devem ser incluídos para cada item.
6. Selecione o ícone **Copiar** e cole o Liquid onde for necessário na sua mensagem.

![O modal Adicionar personalização com as seguintes seleções: "Catalog Items" para "Tipo de personalização", "Games" para "Nome do catálogo", "Selections" para "Tipo de seleção", "game_selection" para "Seleção" e "title" e "description_en" para "Informações a exibir".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

{% alert note %}
A prévia de personalização no painel de composição Liquid exibe até três seleções de catálogo, independentemente do limite de resultados que você definiu. Esse é o comportamento esperado — a mensagem real enviada aos usuários respeita o limite de resultados configurado.
{% endalert %}

## Caso de uso {#use-case}

Digamos que você tenha um serviço de entrega de refeições e queira enviar uma mensagem personalizada para seus usuários que têm preferências alimentares específicas com base na categoria de alimentos visualizada mais recentemente.

Usando um catálogo com as informações do seu serviço de entrega de refeições para o nome da refeição, preço, imagem e categoria da refeição, você pode criar uma seleção para recomendar três refeições com base na categoria visualizada mais recentemente pelo usuário.

![Um exemplo de seleção para um serviço de entrega de refeições com dois filtros: um que identifica o tipo de produto como refeição e outro que identifica a categoria como a visualizada mais recentemente. A seleção está configurada para randomizar a ordem em que os três resultados são retornados.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Para usar esse catálogo e essa seleção em uma campanha, use o modal **Adicionar personalização** na seção de composição de mensagem ao criar uma campanha. Neste exemplo, selecionamos o catálogo com as informações do seu serviço de entrega de refeições e a seleção para recomendações de refeições com base na categoria visualizada mais recentemente. Isso nos permite exibir o nome e o preço da refeição. Para construir ainda mais sua mensagem, você pode usar a seleção para também adicionar uma imagem da primeira refeição recomendada.

![Um cartão de conteúdo com o cabeçalho "Você vai AMAR essas refeições altamente avaliadas!" com a seleção "recommendations_be_recent_category" na seção de composição de mensagem.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Por exemplo, digamos que você tenha um usuário cuja categoria visualizada mais recentemente é "Frango". Usando a personalização configurada e uma campanha de cartão de conteúdo, você pode enviar três recomendações de refeições que incluem frango para esse usuário.

![Um cartão de conteúdo com uma imagem de frango grelhado com limão e uma lista de três recomendações de refeições que incluem frango com base na categoria visualizada mais recentemente pelo usuário.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Usando a mesma personalização, você também pode enviar três recomendações de refeições para um usuário cuja categoria visualizada mais recentemente é "Carne bovina".

![Um cartão de conteúdo com uma imagem de estrogonofe de carne e uma lista de duas recomendações de refeições que incluem carne bovina com base na categoria visualizada mais recentemente pelo usuário.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}