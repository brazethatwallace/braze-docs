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

`abort_message()` interrompe o envio para usuários que não atendem à sua condição. A mensagem não aparecerá no perfil deles e não contará como entrega nem para o limite de frequência.

Se os envios de teste nunca chegarem, visualize como um usuário que satisfaça a condição de interrupção e, em seguida, em **Test Send**, ative **Override recipients' attributes with current preview user's attributes** (ou adicione um membro de um grupo de teste de conteúdo que se qualifique).

## Interromper mensagem se "Number Games Attended" = 0 {#abort-message-if-number-games-attended-0}

Por exemplo, digamos que você não quisesse enviar uma mensagem para clientes que não participaram de nenhum jogo:

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

Essa mensagem será enviada apenas para clientes que sabidamente participaram de um jogo.

## Enviar mensagens apenas para clientes que falam inglês {#message-english-speaking-customers-only}

Você pode enviar mensagens apenas para clientes que falam inglês criando uma instrução "if" que será correspondida quando o idioma do cliente for inglês e uma instrução "else" que interromperá a mensagem para qualquer pessoa que não fale inglês ou que não tenha um idioma definido em seu perfil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Por padrão, a Braze registrará uma mensagem de erro genérica no seu Log de Atividade de Mensagens:

```text
{% abort_message %} called
```

Você também pode fazer com que a mensagem de interrupção registre algo no seu Log de Atividade de Mensagens incluindo uma string dentro dos parênteses:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Log de erro de mensagens no console de desenvolvedor com uma mensagem de interrupção "language was nil".]({% image_buster /assets/img_archive/developer_console.png %})

## Consultar mensagens de interrupção {#query-for-abort-messages}

Você pode usar o [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) ou seu próprio data warehouse, se estiver conectado à Braze, para consultar mensagens de interrupção específicas que são disparadas quando a lógica Liquid causa a interrupção de uma mensagem.

## Quando a lógica de interrupção é avaliada {#when-abort-logic-is-evaluated}

O momento em que a lógica de interrupção é avaliada depende do canal de mensagem.

### Push, e-mail, SMS, webhooks e Content Cards {#push-email-sms-webhooks-and-content-cards}

A lógica de interrupção é avaliada no momento do envio, quando a Braze processa a mensagem para entrega.

### In-App Messages {#in-app-messages}

A lógica de interrupção é avaliada para [mensagens no app com modelo]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated) somente no momento em que a mensagem no app é disparada (por exemplo, quando o usuário realiza o evento-gatilho ou inicia uma sessão), e não quando a mensagem é enviada inicialmente para o dispositivo. As mensagens no app são entregues ao SDK no início da sessão e armazenadas em cache localmente; o Liquid, incluindo quaisquer chamadas de `abort_message()`, é executado quando a condição de disparo é atendida.

## Solução de problemas para altas taxas de interrupção {#troubleshooting-high-abort-rates}

Se uma campanha ou etapa do Canvas mostra muitos usuários que entraram, mas poucos envios, ou as entregas estão abaixo do esperado, a lógica de interrupção é uma causa comum — especialmente quando o Liquid exige atributos, dados de catálogo ou valores de lista que estão ausentes no momento da avaliação.

### Verifique o registro de atividade de mensagens {#check-the-message-activity-log}

1. No dashboard da Braze, abra o [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para a campanha ou etapa de mensagem do Canvas.
2. Filtre por entradas relacionadas a interrupções. Por padrão, a Braze registra chamadas de {% raw %}`{% abort_message %}`{% endraw %}. Se você passou uma string de motivo para `abort_message()`, esse texto aparecerá no lugar.
3. Observe se as interrupções se concentram em um único canal (por exemplo, apenas e-mail) ou em vários canais no mesmo Canvas.

### Verifique atributos e Liquid no momento do envio {#verify-attributes-and-liquid-at-send-time}

Para push, e-mail, SMS, webhooks e Content Cards, a lógica de interrupção é executada quando a Braze processa a mensagem para entrega — não quando o usuário entrou em um Canvas ou quando um evento-gatilho foi disparado anteriormente.

- Confirme que os [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), propriedades de eventos ou campos de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) necessários estão definidos no usuário antes da execução da etapa de mensagem.
- Adicione verificações explícitas de nil ou vazio antes de chamar `abort_message()`. Um branch `else` que interrompe quando um valor está ausente impede o envio para qualquer usuário sem esses dados.
- Se a personalização depende de uma lista, Segment ou resposta de Connected Content, confirme que os dados estão disponíveis quando a etapa de mensagem é executada. Um usuário pode entrar em um Canvas antes que a associação à lista ou os dados downstream estejam prontos.

### Comportamento específico do Canvas {#canvas-specific-behavior}

Se uma etapa de mensagem é interrompida em um Canvas, o usuário não sai do Canvas. Em vez disso, ele avança para a próxima etapa. As interrupções afetam apenas a contagem de envios daquela etapa de mensagem.

Ao diagnosticar interrupções no Canvas:

- Compare os usuários que entraram na etapa de mensagem com os usuários que receberam envios na mesma etapa.
- Se apenas um canal está sendo interrompido, revise o Liquid específico do canal ou o status de inscrição dessa etapa.
- Se as interrupções aumentam após uma atualização de lista ou catálogo, verifique se a etapa de mensagem foi executada antes da conclusão da atualização.

### Valide com prévia e envios de teste {#validate-with-preview-and-test-sends}

Visualize como um usuário no criador de mensagem cujo perfil corresponde a um destinatário afetado. Para envios de teste, ative **Substituir atributos dos destinatários pelos atributos do usuário de prévia atual** quando sua lógica de interrupção depender de dados do perfil.

Para mais exemplos de interrupção, consulte [Consultar mensagens de interrupção](#query-for-abort-messages).

## Considerações {#considerations}

A tag de mensagem Liquid `abort_message()` impede que as mensagens sejam enviadas aos usuários, o que significa que a mensagem não será exibida nos perfis de usuário e não será contabilizada como entrega nem no limite de frequência.