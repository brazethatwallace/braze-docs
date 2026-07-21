---
nav_title: Cancelar mensagens
article_title: Cancelar mensagens com Liquid
page_order: 7
description: "Este artigo de referência aborda o cancelamento de mensagens com Liquid e alguns exemplos de casos de uso."

---

# Cancelar mensagens {#abort-messages}

> Opcionalmente, você pode usar a tag Liquid `abort_message("optional reason for aborting")` dentro de condicionais para impedir o envio de uma mensagem a um usuário. Este artigo de referência lista alguns exemplos de como esse recurso pode ser usado em campanhas de marketing.

{% alert note %}
Se uma etapa de mensagem for cancelada em um Canvas, o usuário **não** sairá do Canvas e **continuará** para a próxima etapa.
{% endalert %}

## Envios de teste com `abort_message()` {#test-sends-with-abort_message}

`abort_message()` interrompe o envio para usuários que não atendem à sua condição. A mensagem não aparecerá no perfil deles e não será contabilizada nas entregas ou no limite de frequência.

Se os envios de teste nunca chegarem, faça a pré-visualização como um usuário que satisfaz a condição de cancelamento e, em seguida, em **Test Send**, ative **Override recipients' attributes with current preview user's attributes** (ou adicione um membro do Content Test Group que se qualifique).

## Cancelar mensagem se "Number Games Attended" = 0 {#abort-message-if-number-games-attended-0}

Por exemplo, digamos que você não queira enviar uma mensagem para clientes que não participaram de um jogo:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Essa mensagem será enviada apenas para clientes que comprovadamente participaram de um jogo.

## Enviar mensagens apenas para clientes que falam inglês {#message-english-speaking-customers-only}

Você pode enviar mensagens apenas para clientes que falam inglês criando uma instrução "if" que corresponda quando o idioma do cliente for inglês e uma instrução "else" que cancele a mensagem para qualquer pessoa que não fale inglês ou que não tenha um idioma definido no perfil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Por padrão, a Braze registrará uma mensagem de erro genérica no seu Registro de atividades de envio de mensagem:

```text
{% abort_message %} called
```

Você também pode fazer com que a mensagem de cancelamento registre algo no seu Registro de atividades de envio de mensagem incluindo uma string dentro dos parênteses:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Registro de erros de mensagem no console de desenvolvedor com uma mensagem de cancelamento "language was nil".]({% image_buster /assets/img_archive/developer_console.png %})

## Consultar mensagens de cancelamento {#query-for-abort-messages}

Você pode usar o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) ou seu próprio data warehouse, se estiver conectado à Braze, para consultar mensagens de cancelamento específicas que são disparadas quando a lógica Liquid faz com que uma mensagem seja cancelada.

## Quando a lógica de cancelamento é avaliada {#when-abort-logic-is-evaluated}

O momento da avaliação da lógica de cancelamento depende do canal da mensagem.

### Push, e-mail, SMS, webhooks e Content Cards {#push-email-sms-webhooks-and-content-cards}

A lógica de cancelamento é avaliada no momento do envio, quando a Braze processa a mensagem para entrega.

### Mensagens no app {#in-app-messages}

A lógica de cancelamento é avaliada para [mensagens no app com template]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated) apenas no momento em que a mensagem no app é disparada (por exemplo, quando o usuário realiza o evento-gatilho ou inicia uma sessão), e não quando a mensagem é inicialmente enviada ao dispositivo. As mensagens no app são entregues ao SDK no início da sessão e armazenadas em cache localmente; o Liquid — incluindo quaisquer chamadas `abort_message()` — é executado quando a condição de gatilho é atendida.

## Solução de problemas para altas taxas de cancelamento {#troubleshooting-high-abort-rates}

Se uma Campaign ou etapa do Canvas mostra muitos usuários que entraram, mas poucos envios, ou se as entregas parecem menores do que o esperado, a lógica de cancelamento é uma causa comum — especialmente quando o Liquid exige atributos, dados de catálogo ou valores de lista que estão ausentes no momento da avaliação.

### Verificar o Registro de atividades de envio de mensagem {#check-the-message-activity-log}

1. No dashboard da Braze, abra o [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) da Campaign ou da etapa de mensagem do Canvas.
2. Filtre por entradas relacionadas a cancelamento. Por padrão, a Braze registra {% raw %}`{% abort_message %}`{% endraw %} called. Se você passou uma string de motivo para `abort_message()`, esse texto aparecerá no lugar.
3. Observe se os cancelamentos se concentram em um canal (por exemplo, apenas e-mail) ou em vários canais na mesma etapa do Canvas.

### Verificar atributos e Liquid no momento do envio {#verify-attributes-and-liquid-at-send-time}

Para push, e-mail, SMS, webhooks e Content Cards, a lógica de cancelamento é executada quando a Braze processa a mensagem para entrega — não quando o usuário entrou no Canvas ou quando um evento-gatilho foi disparado anteriormente.

- Confirme que os [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes), propriedades de eventos ou campos de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) necessários estão definidos no usuário antes que a etapa de mensagem seja executada.
- Adicione verificações explícitas de nil ou vazio antes de chamar `abort_message()`. Uma ramificação `else` que cancela quando um valor está ausente interrompe o envio para qualquer usuário sem esses dados.
- Se a personalização depende de uma lista, segmento ou resposta de Connected Content, confirme que os dados estão disponíveis quando a etapa de mensagem é executada. Um usuário pode entrar em um Canvas antes que a associação à lista ou os dados downstream estejam prontos.

### Comportamento específico do Canvas {#canvas-specific-behavior}

Se uma etapa de mensagem for cancelada em um Canvas, o usuário não sai do Canvas. Em vez disso, ele segue para a próxima etapa. Os cancelamentos afetam apenas a contagem de envios daquela etapa de mensagem.

Ao diagnosticar cancelamentos no Canvas:

- Compare os usuários que entraram na etapa de mensagem com os usuários que receberam o envio na mesma etapa.
- Se apenas um canal está sendo cancelado, revise o Liquid específico do canal ou o status de inscrição para aquela etapa.
- Se os cancelamentos aumentam após uma atualização de lista ou catálogo, verifique se a etapa de mensagem foi executada antes da conclusão da atualização.

### Validar com pré-visualização e envios de teste {#validate-with-preview-and-test-sends}

Faça a pré-visualização como um usuário no criador de mensagem cujo perfil corresponda a um destinatário afetado. Para envios de teste, ative **Override recipients' attributes with current preview user's attributes** quando sua lógica de cancelamento depender de dados do perfil.

Para mais exemplos de cancelamento, consulte [Consultar mensagens de cancelamento](#query-for-abort-messages).

## Considerações {#considerations}

A tag Liquid `abort_message()` impede que mensagens sejam enviadas aos usuários, o que significa que a mensagem não será exibida nos perfis dos usuários e não será contabilizada nas entregas ou no limite de frequência.