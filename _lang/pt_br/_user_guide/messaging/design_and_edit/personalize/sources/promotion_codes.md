---
nav_title: Códigos de promoção
article_title: Códigos de promoção
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Saiba mais sobre listas de códigos de promoção para adicioná-las às suas campanhas e Canvas."
---

# Códigos de promoção

> Saiba mais sobre listas de códigos de promoção para adicioná-las às suas campanhas e Canvas.

## Sobre códigos de promoção

Os códigos de promoção permitem inserir valores únicos e com prazo limitado nas mensagens para impulsionar conversões. Cada lista pode conter até 20 milhões de códigos, e cada código pode durar até seis meses antes de expirar.

Quando a Braze envia uma mensagem com um código de promoção, o código é deduzido antes de a mensagem ser enviada. Para garantir que os códigos sejam consistentes, únicos e nunca reutilizados:

- Uma mensagem com falha ainda consome o código.
- Em envios multicanal, o mesmo código é aplicado em todos os canais.
- Com Liquid condicional, todas as listas referenciadas têm códigos deduzidos, mesmo que apenas uma ramificação seja exibida.
- Entrar ou reentrar em uma etapa do Canvas consome um novo código.

Se você inserir vários trechos da mesma lista em uma mensagem, a Braze aplicará o mesmo código em todos os trechos. Para evitar ficar sem códigos, recomendamos fazer upload de mais códigos do que você espera usar.

{% tabs local %}
{% tab Exemplo %}
Pense nos códigos de promoção como cupons em uma agência dos correios. Quando o atendente retira um cupom da pilha para a sua carta, ele já foi usado — mesmo que a carta nunca chegue ao destino.

Por exemplo, no seguinte Liquid condicional, os códigos de ambas as listas (`vip-deal` e `regular-deal`) são deduzidos, mesmo que cada usuário veja apenas uma ramificação:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Códigos de promoção não podem ser enviados em mensagens no app no Canvas.
{% endalert %}

## Próximas etapas

Procurando os próximos passos? Comece aqui:

- [Criando uma lista de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/)
- [Usando códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#using-promotion-codes)
- [Visualizando o uso de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#viewing-promotion-code-usage)

## Perguntas frequentes

### Quais canais de envio de mensagens posso usar com códigos de promoção?

Atualmente, os códigos de promoção são compatíveis com e-mail, push para celular, push para a web, Cartões de conteúdo, webhook, SMS e WhatsApp. Campanhas de E-mail de transação da Braze e mensagens no app não são compatíveis com códigos de promoção no momento.

### Envios de teste e envios para grupos de teste contam no uso?

Por padrão, envios de teste e envios de e-mail para grupos de teste usam códigos de promoção por usuário, por envio de teste. No entanto, você pode entrar em contato com o gerente de conta da Braze para atualizar esse comportamento e não usar códigos de promoção durante os testes.

### O que acontece quando vários canais de envio de mensagens usam o mesmo trecho de código de promoção?

Se um determinado usuário for elegível para receber um código por meio de vários canais, ele receberá o mesmo código em cada canal. Apenas um código de promoção será usado, independentemente dos canais recebidos.

### Posso usar vários trechos Liquid para referenciar a mesma lista de códigos de promoção em uma mensagem?

Sim. A Braze aplicará o mesmo código de promoção em todas as instâncias desse trecho na mensagem, garantindo que o usuário receba apenas um código único.

### O que acontece quando uma lista de códigos de promoção está expirada ou vazia?

Os códigos expirados são excluídos após seis meses.

Se a mensagem deveria conter um código de promoção de uma lista vazia ou expirada, a mensagem será cancelada.

Se a mensagem contiver lógica Liquid que insere condicionalmente um código de promoção, a mensagem só será cancelada se deveria conter um código de promoção. Se a mensagem não deveria conter um código de promoção, ela será enviada normalmente.

### Se eu fiz upload dos códigos de promoção errados, posso atualizá-los?

Sim. Você pode resolver isso descontinuando a lista inteira ou usando um espaço reservado para excluir a lista. Para saber mais, consulte [Atualizando uma lista de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/#updating-a-promotion-code-list).

### Posso salvar um código de promoção no perfil de um usuário para mensagens futuras?

Sim. Você pode salvar códigos de promoção no perfil de um usuário por meio de uma etapa de Atualização de usuário. Para saber mais, consulte [Salvando códigos de promoção em perfis de usuário]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#save-to-profile).