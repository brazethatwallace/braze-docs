---
nav_title: Códigos de desconto exclusivos
article_title: Enviar códigos de desconto exclusivos
alias: /shopify_discount_codes/
page_order: 7
description: "Este artigo de referência aborda um caso de uso enviado pela comunidade sobre o uso de códigos de promoção da Braze com o Shopify Bulk Discount Code Bot para enviar códigos de desconto exclusivos por meio de suas Campaigns e Canvas."
---

# Envie códigos de desconto exclusivos por meio da Shopify {#send-unique-discount-codes-through-shopify}

> Esse caso de uso enviado pela comunidade mostra como usar os [códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) da Braze com o Shopify Bulk Discount Code Bot para gerar códigos de desconto exclusivos para suas Campaigns e Canvas. Os códigos de desconto exclusivos ajudam a evitar a exploração de códigos promocionais genéricos.

{% alert important %}
Essa é uma integração enviada pela comunidade e não é diretamente suportada pela Braze. O Bulk Discount Code Bot é suportado diretamente pela Shopify. Somente os códigos de promoção da Braze são suportados pela Braze.
{% endalert %}

## Requisitos {#requirements}

| Requisito | Descrição |
| --- | --- |
| Configurar uma loja Shopify | Confirme que você já [configurou uma loja Shopify com a Braze]({{site.baseurl}}/shopify_overview). |
| Instalar o app Bulk Discount Code Bot | Baixe o app [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) na loja de apps da Shopify. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Gerando códigos de desconto exclusivos {#generating-unique-discount-codes}

### Etapa 1: Configure seus códigos de desconto {#step-1-configure-your-discount-codes}

Use o Bulk Discount Code Bot para configurar seus códigos de desconto com base no número de códigos a serem gerados, comprimento do código, valor do desconto e mais.

![As opções de configuração para um conjunto de descontos.][1]{: width="1203" height="677" style="max-width:100%;"}

### Etapa 2: Exporte seus códigos {#step-2-export-your-codes}

Encontre seu conjunto de descontos na barra de pesquisa do Bulk Discount Code Bot e selecione **Export Codes** > **Download Codes** para baixar um arquivo CSV na sua pasta de Downloads.

![Barra de pesquisa com um menu suspenso exibindo o conjunto de descontos e uma linha de botões para seleção.][2]{: width="1163" height="858" style="max-width:70%;"}

No arquivo CSV, exclua a linha 1 para remover o cabeçalho da coluna "Promo". Isso evita que "Promo" se torne um código de desconto na Braze.

![Um fluxograma mostrando a remoção do cabeçalho de linha "Promo" em um arquivo CSV.][3]{: width="448" height="222" style="max-width:60%;"}

### Etapa 3: Adicione seus códigos de desconto à Braze {#step-3-add-your-discount-codes-to-braze}

Na Braze, acesse **Data Settings** > **Promotion Codes** > **Create Promotion Code List** e [configure sua lista de códigos de desconto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create). Certifique-se de que a data de expiração corresponda à que foi configurada pelo Bulk Discounts Code Bot.

Em seguida, faça upload do seu arquivo CSV e selecione **Save List**.

### Etapa 4: Adicione seus códigos de desconto a uma Campaign ou etapa do Canvas da Braze {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

Se você quiser usar seus códigos de desconto exclusivos em uma Campaign de envio único, ou não se importar que os usuários recebam vários códigos exclusivos em diferentes Campaigns ou etapas do Canvas, copie o snippet Liquid da lista de códigos de promoção que você salvou.

![Um snippet de código Liquid com um botão para copiá-lo.][4]{: width="958" height="295" style="max-width:60%;"}

Cole o snippet Liquid em uma Campaign ou etapa do Canvas.

<video autoplay muted loop playsinline loading="lazy" width="800" height="540" style="max-width:100%;height:auto;aspect-ratio:800/540;" aria-label="Um vídeo mostrando o snippet Liquid sendo adicionado a uma etapa do Canvas.">
  <source src="{% image_buster /assets/img/shopify/liquid_promo_code.mp4 %}" type="video/mp4">
</video>

Se você quiser que os usuários recebam um único código de desconto exclusivo independentemente de quantas vezes o código de desconto for referenciado em Campaigns ou Canvas, crie uma etapa de [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) diretamente antes da primeira etapa de mensagem que atribui o código de desconto a um atributo personalizado, como "Promo Code".

{% alert tip %}
Você também pode [criar um atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) acessando **Data Settings** > **Custom Attributes**.
{% endalert %}

Na etapa de User Update, faça o seguinte para cada campo:
- **Attribute Name:** Selecione **Promo Code**.
- **Action:** Selecione **Update**.
- **Key Value:** Cole o snippet de código Liquid.

![Uma etapa de User Update que atualiza um atributo "Promo Code" com o snippet Liquid.][6]{: width="2464" height="1322" style="max-width:100%;"}

Agora, você pode adicionar o atributo personalizado {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} a qualquer mensagem, e o código de desconto será inserido automaticamente.

## Comportamento do código de desconto {#discount-code-behavior}

{% details Campaign multicanal ou etapa do Canvas %}

Quando um snippet de código de desconto é usado em uma Campaign multicanal ou etapa do Canvas, os usuários sempre recebem um código exclusivo. Se um usuário for elegível para receber um código por mais de um canal, ele receberá o mesmo código em cada canal. Em outras palavras, um usuário elegível receberia apenas um código em todas as mensagens enviadas por essa Campaign ou etapa do Canvas.

{% enddetails %}

{% details Diferentes etapas do Canvas ou Campaigns separadas %}

Quando um código de desconto é referenciado por várias etapas no mesmo Canvas ou por Campaigns separadas, um usuário elegível receberá vários códigos de promoção exclusivos (um código para cada etapa do Canvas ou Campaign).

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}