---
nav_title: Usar códigos
article_title: Usar códigos de promoção
page_order: 0.2
description: "Saiba como usar códigos de promoção e visualizar o uso nas suas campanhas e Canvas."
---

# Usar códigos de promoção

> Saiba como usar códigos de promoção e visualizar o uso nas suas campanhas e Canvas.

## Pré-requisitos

Antes de usar códigos de promoção, você precisa [criar uma lista de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/).

## Usando códigos de promoção

Para enviar um código de promoção em uma mensagem, selecione **Copy Snippet** ao lado da lista de códigos de promoção [que você criou anteriormente]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/#create).

![Uma opção para copiar o snippet e colar na sua mensagem.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Cole os snippets de código em uma das suas mensagens na Braze e use o [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) para inserir um dos códigos de promoção únicos da sua lista. Esse código é marcado como enviado, garantindo que nenhuma outra mensagem envie o mesmo código.

![Um exemplo de mensagem "Treat yourself to something nice this spring with our exclusive offer" seguido do snippet de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Entre etapas do Canvas

Quando um snippet de código é usado em uma campanha ou Canvas com mensagens multicanal, cada usuário recebe um código único. Em um Canvas com várias etapas que referenciam códigos de promoção, o usuário recebe um novo código para cada etapa em que entra.

Para atribuir um código de promoção em um Canvas e reutilizá-lo entre etapas:

1. Atribua o código de promoção como um atributo personalizado na primeira etapa (Atualização de usuário).
2. Use Liquid nas etapas seguintes para referenciar esse atributo personalizado em vez de gerar um novo código.

Quando um usuário se qualifica para um código em vários canais, ele recebe o mesmo código em cada canal. Por exemplo, se ele recebe mensagens por e-mail e push, o mesmo código é enviado para ambos. O relatório também reflete um único código.

{% alert note %}
Se não houver códigos de promoção disponíveis, mensagens de teste ou ao vivo que dependem de códigos não serão enviadas.
{% endalert %}

### Campanhas de mensagens no app {#promotion-codes-iam-campaigns}

Depois de criar uma [campanha de mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages), você pode inserir um [snippet de lista de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#using-promotion-codes-1) no corpo da sua mensagem no app. Os códigos de promoção em mensagens no app são deduzidos e usados somente quando o usuário aciona a exibição da mensagem no app.

### Mensagens de teste

Envios de teste e envios de e-mail para grupos de teste consomem códigos de promoção, a menos que solicitado de outra forma. Fale com o gerente da sua conta na Braze para atualizar esse comportamento para que os códigos de promoção não sejam usados durante envios de teste e envios de e-mail para grupos de teste.

### Com extras de mensagem para Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Salvando códigos de promoção nos perfis de usuário {#save-to-profile}

Para referenciar o mesmo código de promoção em mensagens subsequentes, o código precisa ser salvo no perfil de usuário como um atributo personalizado. Isso pode ser feito por meio de uma [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) que atribui o código de desconto a um atributo personalizado, como "Promo Code", diretamente antes de uma etapa de Mensagem.

Primeiro, selecione o seguinte para cada campo na etapa de Atualização de usuário:

- **Attribute Name:** Promo Code
- **Action:** Update
- **Key Value:** O snippet de código Liquid do código de promoção, como {% raw %}`{% promotion('spring25') %}`{% endraw %}

Segundo, adicione o atributo personalizado (neste exemplo, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) a uma mensagem. O código de desconto é inserido automaticamente pelo template.

## Visualizando o uso de códigos de promoção

Você pode encontrar a contagem de códigos restantes na coluna **Remaining** da lista de códigos de promoção na página **Promotion Codes**.

![Um exemplo de código de promoção com códigos não utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Essa contagem de códigos também pode ser encontrada ao revisitar uma página de lista de códigos de promoção existente. Você também pode exportar os códigos não utilizados como um arquivo CSV.

![Um código de promoção chamado "Black Friday Sale" com 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envios multicanal e de canal único

Para campanhas e Canvas multicanal e de envio único, todos os códigos de promoção referenciados no Liquid de uma mensagem são deduzidos para uso **antes** de a mensagem ser enviada, garantindo o seguinte:

- Os mesmos códigos de promoção são usados entre canais em uma mensagem multicanal.
- Códigos de promoção extras não são usados se uma mensagem falhar ou for abortada.

Se um usuário tiver duas listas de códigos de promoção referenciadas em uma mensagem que é dividida por uma tag de lógica condicional Liquid, todos os códigos de promoção ainda são deduzidos, independentemente de qual fluxo condicional o usuário seguir.

Se um usuário entrar em uma nova etapa do Canvas ou reentrar em um Canvas, e o snippet Liquid do código de promoção for aplicado novamente para uma mensagem a esse usuário, um novo código de promoção será usado.

### Exemplo

No exemplo a seguir, ambas as listas de códigos de promoção `vip-deal` e `regular-deal` são deduzidas. Veja o Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}

A Braze recomenda fazer upload de mais códigos de promoção do que o estimado para uso. Se uma lista de códigos de promoção expirar ou ficar sem códigos, as mensagens subsequentes serão abortadas.

{% alert tip %}
**Aqui vai uma analogia de como os códigos de promoção são consumidos na Braze.** <br><br>Imagine que enviar sua mensagem é como enviar uma carta no correio. Você entrega a carta a um atendente, e ele percebe que sua carta deve incluir um cupom. O atendente pega o primeiro cupom da pilha e o adiciona ao envelope. O atendente envia a carta, mas por algum motivo, a carta se perde no caminho (e o cupom também se perde). <br><br>Nesse cenário, a Braze é o atendente do correio, e seu código de promoção é o cupom. Não é possível recuperá-lo depois que ele foi retirado da pilha de códigos de promoção, independentemente do resultado do webhook.
{% endalert %}