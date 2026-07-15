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

Os alertas de campanha estão disponíveis para as seguintes campanhas:

- Campanhas agendadas recorrentes
- Campanhas baseadas em ação
- Campanhas disparadas por API

## Configurando seu alerta de campanha {#setting-up-your-campaign-alert}

Acesse a página de análise de dados da sua campanha para começar a configurar seu alerta. Ao selecionar **Set Up Alert**, você poderá especificar os limites superior e inferior do alerta, bem como os destinatários e canais de alerta.

![Caixa de diálogo de monitoramento de campanha com dois botões: Cancel e Save.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Para uma campanha agendada recorrente, você pode definir limites superiores e inferiores para as mensagens enviadas a cada execução da campanha. Para uma campanha disparada, você pode definir limites superiores e inferiores para o número de mensagens enviadas por hora e por dia.

Você pode configurar um alerta por e-mail, um alerta por webhook ou ambos. Os alertas por webhook podem ser muito úteis, pois permitem enviar um alerta para um canal do Slack. Para saber mais sobre a integração de alertas de campanha com o Slack, consulte a documentação do Slack sobre [Envio de mensagens usando incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

{% alert note %}
Ao configurar alertas de campanha para campanhas futuras, você pode receber atualizações antes do início da campanha e após o término. Isso acontece porque os alertas de campanha continuam sendo enviados até que a campanha seja interrompida manualmente.
{% endalert %}

## Carga útil do webhook de alerta de campanha {#campaign-alert-webhook-payload}

A seguir, um exemplo de carga útil para o corpo de um webhook de alerta de campanha. Este exemplo usa um alerta configurado para ser enviado quando o número de mensagens enviadas fica abaixo de 500 em uma determinada execução de campanha.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

