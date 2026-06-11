---
nav_title: Preferências de notificação
article_title: Preferências de notificação
page_order: 1
page_type: reference
description: "Este artigo de referência cobre suas opções disponíveis para monitorar o envio de mensagens e a atividade na conta da sua empresa."

---

# Preferências de notificação {#notification-preferences}

> Se você gostaria de monitorar o envio de mensagens e a atividade na conta da sua empresa, pode optar por configurar notificações específicas e selecionar para onde elas vão.

A página **Preferências de notificação** é onde você pode configurar quem (se alguém) recebe notificações sobre sua empresa. Você pode configurar quem deve receber notificações sobre a entrega de campanhas ou erros técnicos. Você também pode especificar destinatários para o relatório semanal de análise de dados. Para a maioria das notificações, a Braze suporta canais de e-mail e webhook.

![Página de Preferências de notificação no dashboard da Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Para acessar esta página, acesse **Configurações** > **Configurações de administrador** > **Preferências de notificação**.

{% alert tip %}
Você também pode integrar com o Slack para receber notificações. Para ver as etapas, consulte [Envio de mensagens usando webhooks de entrada](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Notificações disponíveis {#available-notifications}

A tabela a seguir descreve as notificações disponíveis e quais canais são usados para entregá-las.

{% alert note %}
Se você excluir o valor padrão de **Destinatários** de **Todos os Usuários do Dashboard** e quiser adicioná-lo novamente, pode inseri-lo manualmente no campo suspenso.
{% endalert %}

| Notificação | Descrição | Canais de notificação disponíveis |
|--------------|-------------|-----------------|
| Alertas de uso da API | Ao selecionar esta opção, você é direcionado ao **Dashboard de Uso da API**, onde pode acessar a guia [**Alertas de Uso da API**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/) e configurar alertas para monitorar os volumes de solicitações de API. | E-mail, Webhook |
| Erros de credenciais da AWS | Notifica os destinatários quando a Braze recebe um erro ao tentar usar suas credenciais da Amazon Web Services para uma exportação de dados. Isso inclui notificações de erros de credenciais para Google Cloud Storage e Azure (Microsoft Cloud Services). | E-mail, Webhook |
| Campaign interrompida automaticamente | Notifica os destinatários quando a Braze interrompe uma Campaign. | E-mail |
| Canvas interrompido automaticamente | Notifica os destinatários quando a Braze interrompe um Canvas. | E-mail |
| Expiração de interação de Campaign | Notifica os destinatários sobre qualquer Campaign cujos dados de interação estão prestes a expirar, junto com informações sobre Segments, Campaigns ou Canvas que fazem referência a ela em um filtro de redirecionamento e que foram usados para enviar uma mensagem nos últimos 30 dias. | E-mail |
| Campaign/Canvas atualizado | Notifica os destinatários quando uma Campaign ou um Canvas ativo é atualizado ou desativado, bem como quando uma Campaign ou um Canvas inativo é reativado ou rascunhos são lançados. | E-mail |
| Limite de volume de envios de Campaign/Canvas atingido | Notifica os destinatários quando uma Campaign ou um Canvas atinge seu limite de volume de envios. | E-mail |
| Expiração de interação de Canvas | Notifica os destinatários sobre qualquer Canvas cujos dados de interação estão prestes a expirar, junto com informações sobre Segments, Campaigns ou Canvas que fazem referência a ele em um filtro de redirecionamento e que foram usados para enviar uma mensagem nos últimos 30 dias. | E-mail |
| Comentários em Canvas | Notifica os destinatários quando um Canvas tem novos comentários. | E-mail |
| Erros de Conteúdo conectado | Notifica os destinatários quando um endpoint de Conteúdo conectado apresenta erros. | E-mail |
| Erros de push | Notifica os destinatários quando um endpoint de push apresenta erros. | E-mail, Webhook |
| Limite de Campaign agendada atingido | Notifica os destinatários quando o limite de uma Campaign agendada recorrente é atingido. | E-mail, Webhook |
| Campaign agendada concluiu o envio | Notifica os destinatários quando uma Campaign agendada termina de enviar. | E-mail, Webhook |
| Erros de webhook | Notifica os destinatários quando um endpoint de webhook apresenta erros. | E-mail |
| Relatório semanal de análise de dados | Envia um resumo da atividade do espaço de trabalho da semana anterior para os destinatários toda segunda-feira. Os destinatários recebem um resumo para cada espaço de trabalho ao qual pertencem. | E-mail |
| Limites diários de volume de entrada de Canvas/Campaign | Envia notificações cada vez que um limite de envio é atingido. | E-mail |
| Erro no Console do agente | Notifica os destinatários quando um agente do [Console do agente]({{site.baseurl}}/user_guide/brazeai/agents/) atingiu seu limite de execução, usa um modelo que se tornou indisponível ou encontra um erro de cobrança com seu provedor de LLM (somente para chave de API própria). | E-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notificações disponíveis" }

{% alert note %}
[Usuários suspensos]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#suspending-company-users) ainda podem receber notificações da Braze.
{% endalert %}

## Relatório semanal de análise de dados {#weekly-analytics-reporting}

A Braze pode enviar opcionalmente um relatório semanal por e-mail para as pessoas que você designar na sua empresa, toda segunda-feira às 5h (horário EST). Você pode selecionar os eventos personalizados a serem incluídos no relatório semanal em **Configurações de dados** > **Eventos personalizados**.

Você pode selecionar até cinco eventos para incluir no seu relatório semanal:

![Seleção de eventos a serem incluídos no relatório de análise de dados]({% image_buster /assets/img_archive/company_analytics_report_new.png %})