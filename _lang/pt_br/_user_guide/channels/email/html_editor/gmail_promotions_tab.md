---
nav_title: "Guia Promoções do Gmail"
article_title: "Guia Promoções do Gmail"
page_order: 8
description: "Este artigo de referência explica como usar a Braze para criar o cartão de promoções do Gmail para dispositivos móveis a partir da sua campanha de e-mail."
channel:
  - email
toc_headers: h2
---

# Guia Promoções do Gmail {#gmail-promotions-tab}

> A [guia Promoções do Gmail para dispositivos móveis](https://developers.google.com/gmail/promotab/) permite que profissionais de marketing enviem mais informações por meio de anotações em um "cartão", em vez de depender apenas da linha de assunto ou do pré-cabeçalho. A Braze tem uma ferramenta integrada para ajudar você a criar o cartão a partir da sua campanha de e-mail.

## Pré-requisitos {#prerequisites}

Primeiro, encaminhe seus domínios e subdomínios para a equipe de divulgação da guia Promoções do Google em <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> para serem adicionados à lista de permissões do Gmail. Isso permite que você use qualquer recurso que exiba imagens ricas, como o carrossel de produtos da guia Promoções do Gmail.

## Criar o cartão com a Braze {#build-the-card-with-braze}

Siga estas etapas para criar um cartão de promoção do Gmail para uma campanha de e-mail. Observe que navegar para fora da seção **Content** no editor redefinirá os campos e as informações na guia **Gmail Promotion**. Conclua a configuração do seu cartão de promoção e copie o HTML gerado para não perder o código.

### Etapa 1: Criar uma campanha de e-mail {#step-1-create-an-email-campaign}

Primeiro, [crie sua campanha de e-mail]({{site.baseurl}}/user_guide/channels/email/html_editor) e selecione o **editor de código HTML** como sua experiência de edição.

### Etapa 2: Adicionar informações ao cartão de promoção do Gmail {#step-2-add-details-to-gmail-promotion-card}

Em seguida, acesse a seção **Content** do editor de HTML e selecione a guia **Gmail Promotion**. Preencha os campos em **Basic Information** e selecione **Generate HTML Code**. Isso gerará o script para o cartão da guia Promoções do Gmail na seção **Copy and Paste HTML code into `<Head>`**.

![Exemplo de como criar um cartão.]({% image_buster /assets/img/create-gmail-promo.png %})

### Etapa 3: Personalizar o cartão de promoção do Gmail {#step-3-customize-your-gmail-promotion-card}

Escolha se deseja incluir uma oferta de desconto, cartão de oferta, cartão de promoção ou todas as opções para o seu cartão de promoção do Gmail.

{% tabs %}
{% tab Oferta de desconto %}

Configurar uma oferta de desconto permite que você especifique as datas de validade de um desconto.

1. Selecione o botão de alternância **Discount Offer**.
2. Em **Offer**, insira um breve resumo do desconto. Um exemplo é "20% de desconto".
3. Em **Code**, adicione o código promocional que o usuário precisa aplicar no checkout.
4. Em seguida, selecione a data e hora de início da oferta de desconto.
5. Determine se a oferta de desconto deve terminar em um horário específico ou nunca terminar.

![Opções para especificar o valor da oferta, código e data e hora de início de uma oferta de desconto.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Cartões de oferta %}

Use os cartões de oferta para fornecer informações importantes sobre a oferta diretamente no topo do corpo do e-mail. Isso permite que os destinatários entendam rapidamente os detalhes da oferta e tomem uma ação. Por exemplo, você pode usar cartões de oferta para promover ofertas por tempo limitado e reduzir a necessidade de os usuários procurarem detalhes dentro dos e-mails.

1. Selecione o botão de alternância **Deal Card**.
2. Em **Offer**, insira um breve resumo do desconto. Um exemplo é "20% de desconto em todos os sapatos".
3. (opcional) Em **Code**, adicione o código promocional que o usuário precisa aplicar no checkout.
4. Insira pelo menos uma das seguintes URLs.
-  **Offer Page URL:** A URL da landing page específica da oferta. Isso cria um botão "Comprar agora" (ou similar). Recomendamos fornecer essa URL para o seu cartão de oferta.
- **Merchant Homepage URL:** A URL da sua página inicial principal. Use este campo apenas se uma URL de página de oferta específica não estiver disponível.
5. (opcional) Adicione uma data de início para a oferta.
6. Determine se a oferta deve terminar em um horário específico ou nunca terminar.

![Opções para especificar o valor da oferta, código e data e hora de início de um cartão de oferta.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Cartões de promoção %}

Os cartões de promoção no carrossel de produtos são úteis para fornecer imagens à sua oferta. Você também pode personalizar variáveis no carrossel de produtos e incluir até dez pré-visualizações de imagens, sendo cada imagem única.

1. Selecione o botão de alternância **Promotion Cards**.
2. Selecione **Add promotion card**. Cada imagem no carrossel de produtos deve ter uma URL única e usar a mesma proporção (4:5, 1:1, 1.91:1).
3. Inclua uma URL de imagem.
4. Em **Target URL**, adicione o link da sua promoção.

{% alert tip %}
Recomendamos fazer upload das imagens dos seus produtos na Biblioteca de mídia e, em seguida, copiar e colar as URLs nos campos apropriados. Apenas formatos de imagem estáticos (PNG e JPEG) são aceitos. Alguns formatos de imagem (GIF) serão carregados, mas não serão exibidos conforme esperado.
{% endalert %}

{: start="5"}
5. Personalize seu cartão de promoção adicionando um título, moeda, preço e valor do desconto.

| Propriedade personalizável | Descrição |
|---|---|
| Título | (opcional) Uma ou duas frases de descrição da promoção. Exibido abaixo da imagem de pré-visualização. |
| Moeda | (opcional) A moeda do preço. |
| Preço | O preço da promoção. |
| Valor do desconto | O valor descontado do preço original. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Personalizar o cartão de promoção do Gmail" }

![Exemplo de um carrossel de produtos de uma empresa chamada Motto com o título do e-mail "Nossas meias mais vendidas estão em promoção", com três imagens de meias e seus preços com desconto.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Etapa 4: Gerar e colar o código HTML {#step-4-generate-and-paste-html-code}

Após criar seu cartão de promoção do Gmail, selecione **Generate HTML code**. Copie e cole o script no elemento `<head>` do HTML do seu e-mail.

{% alert tip %}
Para o editor de arrastar e soltar, copie e cole o código HTML gerado na seção de [tags de cabeçalho personalizadas]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#custom-head-tags) em **Sending Settings**.
{% endalert %}

{% alert warning %}
O script de promoções só aparece se o seu e-mail chegar à guia Promoções do Gmail. Atualmente, o Gmail usa algoritmos para determinar onde o seu e-mail será exibido. No entanto, se um usuário marcar seu e-mail como promoção, o algoritmo do Gmail será ignorado e seu e-mail será automaticamente direcionado para a guia Promoções dali em diante.
{% endalert %}

### Etapa 5: Testar usando a ferramenta de pré-visualização do Gmail {#step-5-test-using-gmails-preview-tool}

Para testar anotações em envios de baixo volume, você deve usar a [ferramenta de pré-visualização](https://developers.google.com/workspace/gmail/promotab/preview) do Gmail para validar as anotações primeiro. Se você pular esta etapa, o carrossel de produtos e a pré-visualização de imagem única só serão acionados em volumes de envio mais altos.

## Medir os cartões do Gmail {#measure-gmail-cards}

O Gmail não retorna análise de dados sobre esses cartões, e prestadores de serviço de e-mail (ESPs) como a Braze não conseguem inserir rastreamento de links nos links da seção de cabeçalho (incluindo cartões de promoção e carrosséis de produtos). No entanto, você pode adicionar parâmetros UTM ou códigos únicos às URLs durante a configuração. Esses parâmetros permitem que você rastreie o engajamento usando a análise de dados do seu próprio site ou rastreamento de conversão, pois o rastreamento faz parte da própria URL — não é inserido pelo ESP. O rastreamento de cliques no nível do ESP não está disponível para esses links.

### Incorporar imagens {#incorporate-images}

O Gmail obteve melhores resultados com imagens fortes relacionadas à mensagem do e-mail. O Gmail não recomenda usar um design somente com texto, pois esse espaço foi projetado para trazer linguagem visual, que é vital para o marketing por e-mail, à pré-visualização. Não use imagens com texto cortado ou repita imagens em várias campanhas.

### Descrever ofertas {#describe-offers}

O Gmail não sugere usar frases como "Compre 1 e Leve 1 Grátis ou Descontos em Todos os Shorts e Camisetas", pois o texto pode ser cortado, deixar de chamar a atenção e competir com a linha de assunto. Esse espaço deve ser usado apenas para engajar seus clientes com sua mensagem. Portanto, evite qualquer linguagem semelhante a "Abra este e-mail agora" ou "Clique aqui para ofertas". Também é melhor evitar repetir a linha de assunto.

## Práticas recomendadas {#best-practices}

De modo geral, siga as [práticas recomendadas da guia Promoções do Gmail](https://developers.google.com/gmail/promotab/best-practices).

Ao criar seu cartão, considere as seguintes perguntas:

- O script de anotação é válido? [Pré-visualize com o Google](https://developers.google.com/workspace/gmail/promotab/preview).
- A opção **Show original** no Gmail mostra o script na mensagem bruta?
- O e-mail está chegando em **Promotions**? Os cartões só se aplicam lá.
- Você testou no desktop e no celular?

{% alert tip %}
Embora o Liquid no script seja suportado, recomendamos testar minuciosamente para evitar erros.
{% endalert %}

### Pré-visualizar sua anotação {#preview-your-annotation}

Use a [ferramenta de pré-visualização](https://developers.google.com/workspace/gmail/promotab/preview) para pré-visualizar sua anotação. Observe que enviar um e-mail de teste para si mesmo não funcionará para anotações, pois sua anotação só é renderizada se o e-mail for enviado para um número significativo de destinatários. Certifique-se de enviar o e-mail final (com suas URLs de imagem) para pelo menos 100 destinatários do Gmail.

Não use o Google Workspace para enviar e-mails com anotações. Use apenas domínios de e-mail na lista de permissões para enviar anotações para um grande grupo de destinatários.

### Seguir as diretrizes de imagem {#adhere-to-image-guidelines}

Verifique se suas imagens seguem estas diretrizes:
- Use imagens de alta qualidade e alta resolução.
- Todas as imagens anotadas usam a mesma proporção. As proporções suportadas incluem: 4:5, 1:1, 1.91:1.
- Use tamanhos de imagem corretos. O mínimo é 256x256; o máximo é 4096x4096 pixels.

O Gmail recomenda evitar:
- Uso excessivo de texto nas imagens
- Uso de imagens que são apenas ícones
- Uso de imagens com máscaras arredondadas
- Uso de URLs de imagem personalizadas

### Registrar com DMARC {#register-with-dmarc}

Para que suas anotações sejam renderizadas corretamente, confirme que os domínios enviados estão registrados com DMARC e que todas as políticas estão ativadas.

## Perguntas frequentes {#frequently-asked-questions}

### Como adiciono um logotipo do remetente? {#how-do-i-add-a-sender-logo}

Use as [Anotações do Google](https://developers.google.com/workspace/gmail/promotab/overview) para adicionar seu logotipo e cartão de promoção no app do Gmail. A renderização é controlada pelo Gmail, não pela Braze.

### Por que minha mensagem promocional não está exibindo o cartão de promoção ou o carrossel de produtos na caixa de entrada do usuário final? {#why-is-my-promotional-message-not-displaying-the-promotion-card-or-product-carousel-in-the-end-users-inbox}

Existem muitos fatores que determinam se o carrossel de produtos será exibido na guia Promoções do Gmail.

Todas as imagens na anotação ainda precisam passar por um filtro de qualidade. Para que o carrossel de produtos seja preenchido, todas as imagens na anotação devem estar na proporção de imagem recomendada e ser imagens de produtos em close-up de alta qualidade e alta resolução. As imagens devem conter pouco ou nenhum texto. O filtro de qualidade também filtra conteúdo inadequado, então as imagens devem ser apropriadas para toda a família.

Além disso, o Gmail tem um limite de densidade para quantos carrosséis de produtos aparecem na guia Promoções de um usuário. Por exemplo, se um usuário assina muitas marcas que usam carrosséis de produtos em seus e-mails promocionais, o Gmail eventualmente limita quantos carrosséis de produtos são exibidos.

Devido às regulamentações de privacidade e segurança do Google, e-mails com anotações devem ser amplamente enviados para que a anotação funcione. É recomendado lançar uma campanha e enviá-la para pelo menos 100 destinatários para que o sistema do Google a detecte como um "envio em massa". As URLs de imagem não podem variar entre os destinatários.

### Como os cliques em um cartão de promoção ou carrossel de produtos são rastreados? {#how-are-clicks-on-a-promotion-card-or-product-carousel-tracked}

A Braze ou qualquer outro ESP não consegue inserir rastreamento de links nos links da seção de cabeçalho. Isso significa que os cliques não podem ser rastreados em um cartão de promoção ou carrossel de produtos.

### Existe uma maneira de ver quantos usuários receberam um carrossel de produtos? {#is-there-a-way-to-see-how-many-users-received-a-product-carousel}

O Gmail determina quando e para quem exibir o cartão, então não há garantia de que todos os destinatários verão o carrossel de produtos.

### Por que não vejo anotações na minha guia Promoções do Gmail? {#why-dont-i-see-annotations-in-my-gmail-promotions-tab}

As anotações não são suportadas no Google Workspace. Para pré-visualizar anotações, você pode criar um endereço de e-mail pessoal com o Gmail.

Observe que as anotações não são renderizadas na guia **Primary** ou em qualquer outra guia no app do Gmail para dispositivos móveis. As anotações não serão exibidas após um usuário abrir um e-mail ou se você estiver usando o tipo de anotação `DiscountOffer` e a data e hora já tiverem expirado.

{% alert tip %}
Para mais informações sobre solução de problemas, consulte o [guia de solução de problemas do Google para promoções por e-mail](https://developers.google.com/workspace/gmail/promotab/troubleshooting).
{% endalert %}