---
nav_title: Códigos de promoção
article_title: Códigos de promoção
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Saiba mais sobre listas de códigos de promoção para adicioná-las às suas campanhas e Canvas."
---

# Códigos de promoção {#promotion-codes}

> Saiba mais sobre listas de códigos de promoção para adicioná-las às suas campanhas e Canvas.

## Sobre códigos de promoção {#about-promotion-codes}

Os códigos de promoção permitem inserir valores únicos e com prazo limitado nas mensagens para impulsionar conversões. Cada lista pode conter até 20 milhões de códigos, e cada código pode durar até seis meses antes de expirar.

Quando a Braze envia uma mensagem com um código de promoção, o código é deduzido antes de a mensagem ser enviada. Para garantir que os códigos sejam consistentes, únicos e nunca reutilizados:

- Uma mensagem com falha ainda consome o código.
- Em envios multicanal, o mesmo código é aplicado em todos os canais.
- Com Liquid condicional, todas as listas referenciadas têm códigos deduzidos, mesmo que apenas uma Branch seja exibida.
- Entrar ou reentrar em uma etapa do Canvas consome um novo código.

Se você inserir vários snippets da mesma lista em uma mensagem, a Braze aplicará o mesmo código em todos os snippets. Para evitar ficar sem códigos, recomendamos fazer upload de mais códigos do que você espera usar.

{% tabs local %}
{% tab Exemplo %}
Pense nos códigos de promoção como cupons em uma agência dos correios. Quando o atendente retira um cupom da pilha para a sua carta, ele já foi usado — mesmo que a carta nunca chegue ao destino.

Por exemplo, no seguinte Liquid condicional, os códigos de ambas as listas (`vip-deal` e `regular-deal`) são deduzidos, mesmo que cada usuário veja apenas uma Branch:

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
Códigos de promoção estão disponíveis em campanhas de mensagem no app como recurso de acesso antecipado, mas não podem ser enviados em mensagens no app no Canvas.
{% endalert %}

## Próximas etapas {#next-steps}

Procurando os próximos passos? Comece aqui:

- [Criar uma lista de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create)
- [Usar códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes)
- [Visualizar o uso de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#viewing-promotion-code-usage)

## Perguntas frequentes {#frequently-asked-questions}

### Quais canais de envio de mensagens posso usar com códigos de promoção? {#which-messaging-channels-can-i-use-with-promotion-codes}

Códigos de promoção são compatíveis com e-mail, push para celular, push para a web, Content Cards, webhook, SMS e WhatsApp. Campanhas de mensagem no app são compatíveis com códigos de promoção como recurso de acesso antecipado. Campanhas de e-mail de transação da Braze e mensagens no app no Canvas não são compatíveis com códigos de promoção.

### Envios de teste e envios para grupos de teste contam no uso? {#do-test-and-seed-sends-count-towards-usage}

Por padrão, envios de teste e envios de e-mail para grupos de teste usam códigos de promoção por usuário, por envio de teste. No entanto, você pode entrar em contato com o gerente de conta da Braze para atualizar esse comportamento e não usar códigos de promoção durante os testes.

### O que acontece quando vários canais de envio de mensagens usam o mesmo snippet de código de promoção? {#what-happens-when-multiple-messaging-channels-use-the-same-promotion-code-snippet}

Se um determinado usuário for elegível para receber um código por meio de vários canais, ele receberá o mesmo código em cada canal. Apenas um código de promoção será usado, independentemente dos canais recebidos.

### Posso usar vários snippets Liquid para referenciar a mesma lista de códigos de promoção em uma mensagem? {#can-i-use-multiple-liquid-snippets-to-reference-the-same-promotion-code-list-in-one-message}

Sim. A Braze aplicará o mesmo código de promoção em todas as instâncias desse snippet na mensagem, garantindo que o usuário receba apenas um código único.

### O que acontece quando uma lista de códigos de promoção está expirada ou vazia? {#what-happens-when-a-promotion-code-list-is-expired-or-empty}

Os códigos expirados são excluídos após seis meses.

Se a mensagem deveria conter um código de promoção de uma lista vazia ou expirada, a mensagem será cancelada.

Se a mensagem contiver lógica Liquid que insere condicionalmente um código de promoção, a mensagem só será cancelada se deveria conter um código de promoção. Se a mensagem não deveria conter um código de promoção, ela será enviada normalmente.

### Se eu fiz upload dos códigos de promoção errados, posso atualizá-los? {#if-i-uploaded-the-wrong-promotion-codes-can-i-update-them}

Se você fez upload de códigos incorretos, há duas opções para resolver:

- **Descontinuar a lista inteira:** pare de usar a lista atual em qualquer campanha, Canvas ou modelo. Em seguida, faça upload dos códigos corretos em uma nova lista e atualize todas as suas mensagens para usar a nova lista.
- **Esgotar os códigos incorretos:** crie uma campanha que envie códigos da lista incorreta para um usuário de teste até que todos os códigos errados sejam consumidos. Depois disso, faça upload novamente dos códigos corretos na mesma lista, excluindo os incorretos.

Para orientações gerais sobre como atualizar uma lista, consulte [Atualizar uma lista de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#updating-a-promotion-code-list).

### A Braze rastreia quais usuários receberam ou resgataram quais códigos de promoção? {#does-braze-track-which-users-received-or-redeemed-which-promotion-codes}

Quando uma mensagem usa um código de promoção, a Braze marca esse código como consumido para que ele não possa ser enviado novamente e atualiza a contagem restante da lista. A Braze não mantém um relatório dos códigos enviados, não rastreia quais usuários específicos receberam cada código nem se os códigos foram resgatados.

Se você precisar associar códigos a usuários ou rastrear o resgate por conta própria, você pode:

- Salvar códigos de promoção em perfis de usuário por meio de uma etapa de Atualização de usuário. Para saber mais, consulte [Salvar códigos de promoção em perfis de usuário]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile).
- Enviar valores de códigos de promoção para o Currents usando a Liquid tag `message_extras`. Para saber mais, consulte [Enviar informações de códigos de promoção para o Currents]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#sending-promotion-code-information-to-currents).

### Posso salvar um código de promoção no perfil de um usuário para mensagens futuras? {#can-i-save-a-promotion-code-to-a-users-profile-for-future-messages}

Sim. Você pode salvar códigos de promoção no perfil de um usuário por meio de uma etapa de Atualização de usuário. Para saber mais, consulte [Salvar códigos de promoção em perfis de usuário]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile).