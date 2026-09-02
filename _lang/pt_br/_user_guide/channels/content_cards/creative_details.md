---
nav_title: Detalhes criativos
article_title: Detalhes criativos para Content Cards
page_order: 2
description: "Este artigo aborda detalhes criativos, como recomendações de tamanho de imagem e comportamento de descarte nos três tipos padrão de Content Cards."
channel:
  - content cards
tool: Media

---

# Detalhes criativos para Content Cards {#creative-details-for-content-cards}

> A personalização dos Content Cards e do feed em que eles estão localizados não pode ser feita durante o processo de criação da campanha — você precisa trabalhar com seus engenheiros e desenvolvedores para criar e personalizar seus cartões. Para detalhes técnicos, visite nossa [documentação para desenvolvedores]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Tipos de Content Cards {#content-card-types}

{% tabs %}
{% tab Clássico %}

O cartão clássico é ótimo para mensagens e notificações padrão ou até para categorizar visualmente mensagens com ícones. A imagem é opcional, mas deve ter proporção de 1:1.

![Imagem de um cartão clássico com detalhes recomendados e um exemplo de cartão clássico]({% image_buster /assets/img/content_card_classic.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Capacidade do cartão | Detalhes |
| --- | ---|
| Texto do cabeçalho | 18px; Negrito <br> Uma linha de texto é o ideal. <br> Você pode usar Liquid aqui para personalizar sua mensagem. |
| Texto da mensagem | 13px; Peso normal <br> Duas a quatro linhas de texto é o ideal. <br> Você pode usar Liquid aqui para personalizar sua mensagem. |
| Texto do link | Opcional. <br> 13&nbsp;px <br> Link para página web ou deep link para dentro do seu app. |
| Imagem | Opcional. <br> Deve ter proporção 1:1. <br> Recomendamos uma qualidade de imagem de 60 x 60&nbsp;px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de Content Cards" }

{% endtab %}
{% tab Imagem com legenda %}

O cartão de imagem com legenda é uma ótima maneira de destacar e atrair atenção para conteúdos importantes, como uma grande promoção ou um novo recurso do app.

![Imagem de um cartão de imagem com legenda com detalhes recomendados e um exemplo de cartão de imagem com legenda]({% image_buster /assets/img/content_card_captioned.png %}){: width="2880" height="2877" style="max-width:90%;border:0;"}

| Capacidade do cartão | Detalhes |
| --- | ---|
| Texto do cabeçalho | 18px; Negrito <br> Uma linha de texto é o ideal. <br> Você pode usar Liquid aqui para personalizar sua mensagem. |
| Texto da mensagem | 13px; Peso normal <br> Duas a quatro linhas de texto é o ideal. <br> Você pode usar Liquid aqui para personalizar sua mensagem. |
| Texto do link | Opcional. <br> 13&nbsp;px <br> Link para página web ou deep link para dentro do seu app. |
| Imagem | Proporção sugerida de 4:3. <br> Largura mínima de 600&nbsp;px. <br> Compatível com PNG, JPEG e GIF de alta resolução. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de Content Cards" }

{% endtab %}
{% tab Somente imagem %}

Se você quer mais controle criativo, o cartão somente imagem é para você. Crie sua imagem usando qualquer ferramenta que preferir e faça o upload da imagem nesse tipo de cartão.

![Imagem de um Content Card somente imagem com detalhes recomendados e um exemplo de somente imagem]({% image_buster /assets/img/content_card_banner.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Capacidade do cartão | Detalhes |
| --- | ---|
| Cartão com link | Opcional. <br> 13&nbsp;px <br> Comportamento ao clicar com link para uma página web ou deep link para dentro do seu app. |
| Imagem | Qualquer proporção é compatível. <br> Largura mínima de 600&nbsp;px. <br> Compatível com PNG, JPEG e GIF de alta resolução. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de Content Cards" }

{% endtab %}
{% endtabs %}

## Detalhes criativos gerais {#general}

Os Content Cards suportam texto e imagens, incluindo GIFs, nativamente. No momento, estilos personalizados para o cartão, como cores de fonte diferentes ou múltiplas imagens, não podem ser feitos no dashboard. Você pode personalizar o estilo do seu cartão de conteúdo e do feed durante a integração. Para mais detalhes, consulte [Personalizar cartões]({{site.baseurl}}/developer_guide/content_cards/customizing_cards) para o SDK da Braze.

### Comportamento de descarte {#dismissal-behavior}

Para descartar um cartão, o usuário pode deslizá-lo para o lado no celular ou usar a função `close X`, conforme mostrado na captura de tela a seguir. O `x` aparecerá ao passar o mouse apenas no SDK para web.

![Imagem que mostra os comportamentos de descarte por deslizar ou fechar para um cartão]({% image_buster /assets/img/dismissal-cc.png %}){: width="1800" height="504"}

Se um usuário descartou todos os seus cartões ou você não enviou nenhuma nova atualização, o feed do usuário geralmente ficará assim:

![Imagem de um feed de Content Cards vazio]({% image_buster /assets/img/empty-cc.png %}){: width="832" height="1478" style="max-width:45%"}

{% alert tip %}
Mantenha os Content Cards relevantes configurando-os para serem descartados quando o usuário realizar ações relevantes. Por exemplo, configure Content Cards promocionais para serem descartados assim que os usuários fizerem uma compra, para que eles não continuem vendo uma oferta de algo que já compraram.
{% endalert %}

### Usando GIFs em Content Cards {#using-gifs-in-content-cards}

| Content Cards para Android | Content Cards para iOS | Content Cards para web |
| --- | --- |---|
| O SDK para Android não oferece suporte a GIFs animados por padrão. Para mais detalhes sobre como ativar o suporte a GIFs, consulte [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs?sdktab=android). | O SDK Swift não oferece suporte a GIFs animados por padrão. Para mais detalhes sobre como ativar o suporte a GIFs, consulte o [tutorial de suporte a GIFs](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | O suporte a GIFs está incluído por padrão na integração do SDK para web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Usando GIFs em Content Cards" }