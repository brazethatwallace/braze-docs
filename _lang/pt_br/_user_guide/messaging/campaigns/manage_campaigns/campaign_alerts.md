---
nav_title: Alertas de campanha
article_title: Alertas de campanha
page_order: 6

page_type: reference
description: "Este artigo de referência oferece uma visão geral dos alertas de campanha, seus benefícios e como configurá-los para garantir sua tranquilidade."
tool: Campaigns
channel:
- email
- webhooks

---

# Alertas de campanha {#campaign-alerts}

> Queremos alertar você quando algo não parecer como esperado e garantir a tranquilidade de que tudo está funcionando bem. Os alertas de limite de campanha oferecem essa tranquilidade — seja a primeira pessoa a saber se uma campanha importante envia mais ou menos mensagens do que o esperado.

Procurando a mesma funcionalidade em um Canvas? Consulte [Alertas de limite de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

Os alertas de campanha estão disponíveis para as seguintes campanhas:

- Campanhas agendadas recorrentes
- Campanhas baseadas em ação
- Campanhas disparadas por API or interface de programação do aplicativo (API)

## Configurando o alerta da sua campanha {#setting-up-your-campaign-alert}

Acesse a página de análise de dados da sua Campaign para começar a configurar o alerta. Ao selecionar **Set Up Alert**, você poderá especificar limites superiores e inferiores para o alerta, bem como os destinatários e canais de alerta.

![Caixa de diálogo de monitoramento de Campaign com dois botões: Cancel e Save.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Para uma Campaign recorrente agendada, você pode definir limites superiores e inferiores para as mensagens enviadas a cada disparo da Campaign. Para uma Campaign disparada, você pode definir limites superiores e inferiores para o número de mensagens enviadas por hora e por dia.

Você pode configurar um alerta por e-mail, um alerta por webhook ou ambos. Alertas por webhook podem ser muito úteis, pois permitem enviar um alerta para um canal do Slack. Para saber mais sobre a integração de alertas de Campaign com o Slack, consulte a documentação do Slack sobre [Envio de mensagens usando webhooks de entrada](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

{% alert note %}
Ao configurar alertas de Campaign para Campaigns futuras, você pode receber atualizações antes do início da Campaign e após o seu término. Isso acontece porque os alertas de Campaign continuarão sendo enviados até que a Campaign seja interrompida manualmente.
{% endalert %}

## Carga útil do webhook de alerta de Campaign {#campaign-alert-webhook-payload}

A seguir está um exemplo de carga útil para o corpo de um webhook de alerta de Campaign. Este exemplo usa um alerta configurado para enviar quando o número de mensagens enviadas fica abaixo de 500 para um determinado envio de Campaign.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

