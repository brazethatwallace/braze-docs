---
nav_title: Falhas de envio
article_title: Investigar falhas de envio do WhatsApp
page_order: 22
page_type: reference
description: "Use a análise de dados de campaigns, o registro de atividades de mensagens e o Currents para investigar falhas de envio do WhatsApp e códigos de erro comuns da Meta."
tool:
  - Reports
channel:
  - WhatsApp
---

# Investigar falhas de envio do WhatsApp {#investigate-whatsapp-send-failures}

> Use esta página quando as entregas ou leituras do WhatsApp estiverem abaixo do esperado, ou quando as **Falhas** na análise de dados da campaign parecerem elevadas.

## Fluxo de investigação {#investigation-workflow}

Siga as etapas abaixo na ordem indicada.

1. **Confirme as falhas na análise de dados da campaign ou do Canvas.** Abra a etapa de mensagem e revise a contagem de **Falhas** e a taxa de falha. Se as falhas parecerem elevadas em comparação com os envios ou entregas, prossiga para a próxima etapa.
2. **Encontre o código de erro no registro de atividades de mensagens.** Abra o [Registro de atividades de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para o mesmo envio, filtre por mensagens com falha e anote o código de erro do provedor (por exemplo, `131049` para limites de marketing por usuário). Use os [Códigos de falha comuns](#common-failure-codes) para interpretar o código e decidir os próximos passos.
3. **Exporte as falhas com o Currents para análise ou redirecionamento.** Depois de identificar o código de erro, exporte os eventos de falha de envio do WhatsApp por meio do Currents. Use esses dados para analisar tendências de falha no seu data warehouse ou para criar segmentos e redirecionar usuários em outro canal.

## Códigos de falha comuns {#common-failure-codes}

| Código de erro | Causa típica | Próxima etapa |
|---|---|---|
| `131049` | Limite de frequência de marketing por usuário da Meta ou pausa de marketing nos EUA | Consulte [Recursos da Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources) e [Redirecionar usuários em outros canais da Braze]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels) |
| `130472` | Grupo de controle de experimento de marketing da Meta | Consulte [FAQ de recursos da Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources#faq) |
| `131026` | Diversos motivos de não entrega (a Meta não divulga detalhes específicos) | Evite novas tentativas imediatas; consulte a [solução de problemas da Meta Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Códigos de falha comuns do WhatsApp" }