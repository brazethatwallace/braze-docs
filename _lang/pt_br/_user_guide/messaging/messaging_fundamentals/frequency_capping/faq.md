---
nav_title: FAQ
article_title: FAQ sobre limite de taxa e limite de frequência
page_order: 0
page_type: FAQ
description: "Este artigo fornece respostas para algumas perguntas frequentes sobre limite de taxa e limite de frequência."
tool: Campaigns

---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre limite de taxa e limite de frequência.

## Se eu alterar a limitação de envio em um Canvas ativo, isso afeta os usuários que já estão no Canvas? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Sim. Quando você aumenta ou diminui o limite de taxa de um Canvas, o limite atualizado entra em vigor para novas mensagens. Pode haver um breve atraso antes que a atualização seja refletida em todo o Canvas.

### O que acontece se um usuário chega a uma etapa de Mensagem do Canvas, mas já ultrapassou o limite de frequência global? {#what-happens-if-a-user-reaches-a-canvas-message-step-but-is-over-the-global-frequency-cap}

O usuário não recebe o envio para o canal limitado, mas ainda segue as regras de avanço da etapa de Mensagem. As etapas de Mensagem avançam os usuários quando uma mensagem não é enviada por causa do limite de frequência global, então eles continuam para a próxima etapa do Canvas. Para a lista completa de casos de avanço, consulte [Como os usuários avançam]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance).

### Como posso identificar usuários que foram limitados por frequência em um Canvas? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Usuários que são limitados por frequência não geram um evento de envio para aquela etapa. Para identificar esses usuários, você pode usar o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para rastrear eventos de mensagem abortada onde `abort_type` é `frequency_capped`. Como alternativa, você pode criar uma [extensão de Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para analisar usuários que entraram no Canvas, mas não receberam a mensagem esperada.

### Como os dias do calendário e fusos horários são usados para limites de frequência globais "por dia"? {#how-are-calendar-days-and-time-zones-used-for-per-day-global-frequency-caps}

O limite de frequência global usa o fuso horário do usuário e conta por dia do calendário, não por períodos contínuos de 24 horas. Para ver um exemplo, consulte [Regras de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules).

### O limite de frequência global se aplica a mensagens no app disparadas? {#does-global-frequency-capping-apply-to-triggered-in-app-messages}

Não. O limite de frequência global se aplica apenas a mensagens push, e-mail, SMS, webhook, WhatsApp e LINE.

### O limite de frequência limita Campaigns recebidas ou mensagens individuais dentro de um envio? {#does-frequency-capping-limit-campaigns-received-or-individual-messages-inside-a-send}

O limite de frequência se aplica por despacho — cada envio de Campaign ou etapa do Canvas conta para seus limites, não cada variante ou plataforma dentro de um envio. Para saber mais, consulte [Regras de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules).

### Se várias mensagens são elegíveis ao mesmo tempo e apenas algumas cabem dentro do limite, quais mensagens são enviadas? {#if-several-messages-are-eligible-at-the-same-time-and-only-some-fit-under-the-cap-which-messages-send}

A Braze envia até o limite. Quando vários envios competem na mesma janela, as mensagens processadas primeiro são as que contam para o limite. Os envios restantes naquela janela são limitados.

### Webhooks com falha contam para o limite de frequência global? {#do-failed-webhooks-count-toward-the-global-frequency-cap}

Não. Um webhook conta para o limite quando a Braze registra uma entrega bem-sucedida. Respostas de webhook malsucedidas (por exemplo, códigos de status `4xx` ou `5xx`) não contam para o limite.