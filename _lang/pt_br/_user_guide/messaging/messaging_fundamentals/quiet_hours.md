---
nav_title: Horário de silêncio
article_title: Horário de silêncio
page_order: 4
page_type: reference
description: "Este artigo de referência aborda o que é o horário de silêncio, como a Braze lida com mensagens durante esse período e como o horário de silêncio interage com o Intelligent Timing."
---

# Horário de silêncio {#quiet-hours}

> O horário de silêncio impede que mensagens sejam enviadas durante um período específico. Você pode usá-lo para evitar contatar usuários em horários inconvenientes (como durante a noite ou de manhã cedo) e ainda assim enviar mensagens em um horário ideal fora dessa janela.

O horário de silêncio é configurado no nível da Campaign ou do Canvas. Você também pode definir um [horário de silêncio do espaço de trabalho]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) como padrão para um canal de envio de mensagens em todo o seu espaço de trabalho (acesso antecipado).

## Como funciona o horário de silêncio {#how-quiet-hours-work}

Quando o horário de silêncio está ativado e uma mensagem seria enviada durante a janela restrita, a Braze retém a mensagem e a entrega no próximo horário disponível após o término do horário de silêncio.

Por exemplo, se o horário de silêncio vai das 22h às 6h e uma mensagem está agendada para as 5h30, a Braze a entrega às 6h.

{% alert note %}
O horário de silêncio se aplica no fuso local de cada usuário.
{% endalert %}

## Horário de silêncio e Intelligent Timing {#quiet-hours-and-intelligent-timing}

O horário de silêncio e o Intelligent Timing operam de forma independente. Ativar o horário de silêncio não exige que o Intelligent Timing esteja ativado, e o mesmo vale no sentido inverso. De modo geral, recomendamos escolher um ou outro em vez de usar ambos juntos, a menos que haja requisitos de política, conformidade ou outros que tornem o horário de silêncio necessário junto com o Intelligent Timing.

- **Sem Intelligent Timing:** O horário de silêncio funciona como uma janela de bloqueio de envio para o horário de envio agendado. Se o horário agendado cair dentro do horário de silêncio, a mensagem é retida e enviada quando a janela se encerra.
- **Com Intelligent Timing:** A Braze ainda calcula o horário ideal de envio de cada usuário. Se esse horário cair dentro do horário de silêncio, a mensagem é retida e entregue na borda mais próxima da janela de silêncio.

Para saber mais sobre como configurar o horário de silêncio em uma Campaign com Intelligent Timing, consulte [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

## Considerações {#considerations}

- **As mensagens são enviadas ao mesmo tempo quando o horário de silêncio termina.** Se um grande público tem mensagens retidas durante o horário de silêncio, todas essas mensagens são enviadas de uma vez quando a janela se encerra. Para Campaigns sensíveis ao tempo, considere como isso afeta o momento da entrega.
- **O horário de silêncio não é o mesmo que a interrupção de uma mensagem.** A interrupção de uma mensagem a descarta completamente. O horário de silêncio retém a mensagem e a entrega depois.
- **O horário de silêncio não reavalia a associação ao Segment or segmento para um envio retido.** A Braze verifica a associação ao Segment or segmento quando a mensagem é disparada. Se o usuário for elegível nesse momento, a Braze retém a mensagem e a envia quando o horário de silêncio terminar. Isso é separado da [reavaliação da associação ao Segment or segmento no momento do envio]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#audience-criteria-evaluation) ou das [validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) do Canvas.
- **O horário de silêncio é separado do limite de frequência.** Cada um desses controles de entrega se aplica de forma independente. Uma mensagem que passa pelos limites de frequência e de taxa ainda pode ser retida pelo horário de silêncio, e uma mensagem retida pelo horário de silêncio é avaliada em relação aos limites de taxa quando é finalmente enviada. Para saber mais, consulte [Limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

## Artigos relacionados {#related-articles}

- [Horário de silêncio do espaço de trabalho]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours)