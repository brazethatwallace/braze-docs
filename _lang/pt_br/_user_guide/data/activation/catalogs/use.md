---
nav_title: Usando catálogos
article_title: Usando catálogos
page_order: 1.5
description: "Este artigo de referência aborda como usar catálogos para fazer referência a dados de não usuários em suas Campaigns da Braze por meio do Liquid."
---

# Usando catálogos {#using-catalogs}

> Depois de criar um catálogo, você pode fazer referência a dados de não usuários em suas Campaigns da Braze por meio do [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Você pode usar catálogos em todos os seus canais de envio de mensagens, inclusive em qualquer lugar do editor de arrastar e soltar em que o Liquid seja compatível.

## Usando catálogos em uma mensagem {#using-catalogs-in-a-message}

O vídeo a seguir mostra como usar catálogos em uma mensagem.

{% multi_lang_include video.html id="4yc2jkyn6w" source="wistia" %}

### Etapa 1: Adicionar tipo de personalização {#step-one-personalization}

No criador de mensagem de sua escolha, selecione <i class="fas fa-plus-circle"></i> **Adicionar personalização** e selecione **Catalog Items** para o **Tipo de personalização**. Em seguida, selecione o nome do seu catálogo. Usando nosso exemplo anterior, vamos selecionar o catálogo "Games".

![Modal Adicionar personalização com Catalog Items selecionado, catálogo Games escolhido e uma prévia do Liquid mostrando a tag catalog_items.]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Podemos ver imediatamente a seguinte prévia do Liquid:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Etapa 2: Selecionar itens do catálogo {#step-2-select-catalog-items}

Em seguida, é hora de adicionar seus itens do catálogo! Usando o menu suspenso, selecione os itens do catálogo e as informações a serem exibidas. Essas informações correspondem às colunas do arquivo CSV que você fez upload para gerar seu catálogo.

Por exemplo, para referenciar o título e o preço do nosso jogo Tales, podemos selecionar o `id` de Tales (1234) como o item do catálogo e solicitar `title` e `price` para as informações exibidas.

{% raw %}
```liquid
{% catalog_items Games 1234 %}

Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Isso é renderizado da seguinte forma:

> Get Tales for just 7.49!

## Exportando catálogos {#exporting-catalogs}

Existem duas formas de exportar catálogos a partir do dashboard:

- Passe o cursor sobre a linha do catálogo na seção **Catalogs**. Em seguida, selecione o botão **Export catalog**.
- Selecione seu catálogo. Em seguida, selecione o botão **Export catalog** na guia **prévia** do catálogo.

Você receberá um e-mail para baixar o arquivo CSV após iniciar a exportação. Você terá até quatro horas para recuperar esse arquivo.

## Casos de uso adicionais {#additional-use-cases}

### Múltiplos itens {#multiple-items}

Você não está limitado a um único item em uma mensagem. Use o modal **Adicionar personalização** para adicionar até três itens de catálogo por vez. Para adicionar mais, selecione **Adicionar personalização** novamente no criador e selecione itens de catálogo e informações adicionais para exibir.

Confira este exemplo em que adicionamos o `id` de três jogos — Tales, Teslagrad e Acaratus — em **Itens do catálogo** e selecionamos `title` em **Informações para exibir**.

![Modal Adicionar personalização mostrando três IDs de itens de catálogo selecionados e título escolhido para Informações para exibir, com uma prévia do Liquid listando o título de cada item.]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Podemos personalizar ainda mais nossa mensagem adicionando algum texto ao redor do nosso Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Isso retorna o seguinte:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

Neste exemplo, a tag `catalog_items` busca o item `1234` do catálogo `Games`, e então a instrução `if` verifica o campo `on_sale` para exibir mensagens diferentes.

#### Com seleções de catálogo

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters.
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer.
{% else %}
{% abort_message('no venue_name') %}
{% endif %}
```
{% endraw %}

Neste exemplo, mensagens diferentes são exibidas com base no fato de o campo `venue_name` ter mais ou menos de 10 caracteres. Se `venue_name` estiver em branco, a mensagem será interrompida.

Para exibir quantos itens uma seleção retorna, use o filtro `size` do Liquid no array `items` após a tag, e não em um campo individual:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}{{ items | size }}
```
{% endraw %}

{% alert tip %}
Para evitar erros de sintaxe do Liquid, selecione o botão **+** (mais) no criador de mensagem para inserir automaticamente as Liquid tags de catálogo.
{% endalert %}

### Usando imagens {#using-images}

Você também pode referenciar imagens no catálogo para usar no envio de mensagens. Para isso, use a tag `catalogs` e o objeto `item` no campo Liquid para imagens.

Por exemplo, para adicionar o `image_link` do nosso catálogo Games à nossa mensagem promocional de Tales, selecione o `id` no campo **Itens do catálogo** e `image_link` no campo **Informações para exibir**. Isso adiciona as seguintes Liquid tags ao nosso campo de imagem:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Criador de cartão de conteúdo com Liquid tag de catálogo usada no campo de imagem.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Veja como isso fica quando o Liquid é renderizado:

![Exemplo de cartão de conteúdo com Liquid tags de catálogo renderizadas.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

{% alert important %}
Em canais **HTML**, como e-mail, evite espaços extras ou quebras de linha entre a tag de fechamento `{% raw %}{% catalog_items ... %}{% endraw %}` e o Liquid que imprime a URL da imagem (por exemplo, `{% raw %}{{ items[0].image_link }}{% endraw %}`). Espaços em branco extras no modelo podem impedir que a URL da imagem seja resolvida corretamente na mensagem renderizada. Mantenha a expressão da URL imediatamente adjacente à tag de catálogo, como em: `{% raw %}<img src="{% catalog_items Games 1234 %}{{ items[0].image_link }}">{% endraw %}`.
{% endalert %}

### Usando modelos com itens de catálogo

Você também pode usar modelos para buscar dinamicamente itens de catálogo com base em atributos personalizados. Por exemplo, digamos que um usuário tenha o atributo personalizado `wishlist`, que contém um array de IDs de jogos do seu catálogo.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
Objetos JSON em catálogos são ingeridos apenas pela API. Não é possível fazer upload de um objeto JSON usando um arquivo CSV.
{% endalert %}

Usando modelos Liquid, você pode extrair dinamicamente os IDs da lista de desejos e usá-los na sua mensagem. Para isso, [atribua uma variável]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables) ao seu atributo personalizado e, em seguida, use o modal **Adicionar personalização** para buscar um item específico do array. Variáveis referenciadas como o ID do item de catálogo devem estar envolvidas em chaves para serem referenciadas corretamente, como `{{result}}`.

{% alert tip %}
Lembre-se de que arrays começam em `0`, não em `1`.
{% endalert %}

Por exemplo, para informar a um usuário que Tales (um item do nosso catálogo que ele desejou) está em promoção, podemos adicionar o seguinte ao nosso criador de mensagem:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Isso será exibido da seguinte forma:
> Get Tales now for just 7.49!

Com modelos, você pode renderizar um item de catálogo diferente para cada usuário com base em seus atributos personalizados individuais, propriedades de evento ou qualquer outro campo que aceite modelos.

### Fazendo upload de um CSV

Você pode fazer upload de um CSV com novos itens de catálogo para adicionar ou itens de catálogo para atualizar. Para excluir uma lista de itens, faça upload de um CSV com os IDs dos itens para excluí-los.

### Usando Liquid

Você também pode montar catálogos manualmente com lógica Liquid. No entanto, note que se você digitar um ID que não existe, a Braze ainda retornará um array de itens sem objetos. Recomendamos que você inclua tratamento de erros, como verificar o tamanho do array e usar uma instrução `if` para lidar com o caso de um array vazio.

#### Usando modelos com itens de catálogo incluindo Liquid

De forma semelhante ao [Conteúdo Conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), você deve usar a flag `:rerender` em uma Liquid tag para renderizar o conteúdo Liquid de um item de catálogo. Note que a flag `:rerender` funciona apenas em um nível de profundidade, ou seja, ela não se aplica a chamadas aninhadas de Liquid tags.

Se um item de catálogo contém campos de perfil de usuário (dentro de uma Liquid tag de personalização), esses valores devem ser definidos no Liquid anteriormente na mensagem e antes do modelo, para que o Liquid seja renderizado corretamente. Se a flag `:rerender` não for fornecida, o conteúdo Liquid bruto será renderizado.

Por exemplo, se um catálogo chamado "Messages" tiver um item com este Liquid:

![Linha de tabela de catálogo com id greet_msg e coluna Welcome_Message contendo uma saudação de boas-vindas à loja com uma variável Liquid de nome.]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Para renderizar o seguinte conteúdo Liquid:

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Isso será exibido da seguinte forma:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Liquid tags de catálogo não podem ser usadas recursivamente dentro de catálogos.
{% endalert %}

## Solução de problemas de personalização de catálogo

Se o Liquid de catálogo ou seleção não for exibido como esperado em uma mensagem ou etapa do Canvas, verifique o seguinte:

| Sintoma | O que verificar |
| --- | --- |
| A prévia mostra itens, mas os envios em tempo real ficam vazios | Confirme que os **IDs dos itens** do catálogo existem no momento do envio. Se o ID no seu Liquid não corresponder a uma linha, a Braze retornará um array de itens vazio — consulte [Usando Liquid](#using-liquid). Verifique se há erros de digitação e se as fontes de ID (como propriedades de eventos) estão presentes no disparador ou no perfil de usuário. |
| A prévia do criador funciona em uma Campaign, mas não no Canvas | Confirme que você está usando o contexto Liquid correto — **propriedades de contexto do Canvas** versus **propriedades de eventos** — e que esses campos existem no disparador. Consulte [Propriedades de contexto e eventos]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties). |
| Uma seleção não retorna itens | Revise os [filtros de seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) e limites; confirme que os dados do catálogo estão sincronizados e que os nomes das colunas correspondem aos seus filtros. |
| `:rerender` ou entrega com modelo parece incorreto | Para Liquid aninhado dentro de campos do catálogo, você precisa de `:rerender` e da ordenação correta das variáveis — consulte [Usando modelos de itens de catálogo com Liquid](#templating-catalog-items-including-liquid). Mensagens no app com modelo são resolvidas no momento do disparo; consulte [O que são mensagens no app com modelo?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages). Alguns canais restringem tags de catálogo (por exemplo, certos usos de **:rerender** com Banners) — consulte [Todas as Liquid tags são suportadas?]({{site.baseurl}}/user_guide/channels/banners/faq#are-all-liquid-tags-supported) no FAQ de Banners. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas de personalização de catálogo" }

Para o comportamento geral do Liquid, consulte [Casos de uso do Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) e [Usando Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

## Estruturando os dados do seu catálogo

Ao planejar como estruturar os dados do seu catálogo, comece pelo caso de uso pretendido e projete o catálogo em torno dele. Cada linha no catálogo representa um item (com um `id` exclusivo). As colunas devem conter os atributos desse item, como URLs, texto de descrição, URLs de imagem, preço, avaliação, tamanho ou cor.

### Quando usar chamadas de catálogo padrão

Com chamadas de catálogo padrão, você faz a correspondência de um valor com a coluna `id`. Ao inserir um atributo personalizado ou propriedade de evento (como uma string de ID) na Liquid tag do catálogo, você pode trazer múltiplos atributos de um único item para a sua mensagem. Casos de uso comuns incluem:

- Produto ou serviço visualizado recentemente
- Itens da lista de desejos
- Ofertas por localização
- Produto comprado
- Conteúdo por estágio do ciclo de vida
- Produto ou serviço pesquisado mais recentemente

### Quando usar seleções de catálogo

As [seleções de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) permitem filtrar por qualquer coluna do catálogo e retornar até 50 itens correspondentes. Ao inserir atributos personalizados ou propriedades de evento nos filtros de seleção, os resultados são personalizados para cada usuário. Casos de uso comuns incluem:

- Itens cuja categoria corresponde à preferência do usuário
- Itens que correspondem à marca, culinária ou tamanho preferido do usuário
- Conteúdo por tipo de inscrição ou nível de fidelidade
- Produtos dentro da faixa de valor médio de pedido do usuário

A diferença principal é que chamadas de catálogo padrão buscam um único item conhecido pelo `id`, enquanto seleções de catálogo consultam todo o catálogo e retornam múltiplos itens que correspondem aos seus critérios de filtro.

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}