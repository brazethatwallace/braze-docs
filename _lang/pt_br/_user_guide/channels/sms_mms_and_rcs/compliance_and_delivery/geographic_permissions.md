---
nav_title: "Permissões geográficas"
article_title: "Permissões geográficas"
description: "Este artigo aborda a lista de permissões de países para permissões geográficas, que permite escolher para quais países SMS, MMS e RCS podem ser entregues."
page_order: 4
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Permissões geográficas {#geographic-permissions}

> As permissões geográficas aumentam a segurança e protegem contra tráfego fraudulento de SMS, MMS e RCS, aplicando controles sobre os países para os quais você pode enviar mensagens. Você pode especificar uma lista de permissões de países para garantir que mensagens SMS, MMS e RCS sejam enviadas apenas para regiões aprovadas. Somente administradores podem fazer alterações na lista de permissões de países. Usuários não administradores têm acesso a uma versão somente leitura da lista de permissões, que indica para quais países um grupo de inscrições pode enviar mensagens.

Se você é administrador, pode configurar os países que estão na lista de permissões. A lista de permissões de países é configurada no nível do [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/). Você pode acessá-la em **Audience** > **Subscriptions** e selecionando um grupo de inscrições de SMS, MMS ou RCS. A lista de permissões está em **Geographic Permissions**.

![A seção editável de permissões geográficas de SMS para um administrador, com vários países selecionados na "Country allowlist".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Selecionando países {#selecting-countries}

Adicione países à lista de permissões usando o menu suspenso. Os países mais comuns para SMS e RCS aparecem no topo, com os demais logo abaixo. Você também pode pesquisar países digitando no campo de texto.

![O menu suspenso "Country allowlist" com os países mais comuns exibidos no topo.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Remova países selecionados anteriormente desmarcando as respectivas caixas ao lado deles.

### Salvando suas alterações {#saving-your-changes}

As alterações entrarão em vigor após você selecionar **Save**. Remover países da sua lista de permissões impedirá que todas as mensagens SMS, MMS e RCS sejam enviadas para números nesses países.

![Modal de aviso confirmando os países que serão excluídos da lista de permissões.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países de risco alto {#high-risk-countries}

Alguns países apresentam um risco maior de bombeamento de tráfego de SMS e RCS. Esses países são indicados por uma tag **High Risk** no menu suspenso de países.

![O menu suspenso de países com o Azerbaijão exibindo uma tag "High Risk".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Se você permitir o envio para esses países, primeiro deverá reconhecer o risco antes que o país seja adicionado à sua lista de permissões.

{% alert note %}
Limite os países na sua lista de permissões apenas àqueles necessários para atender às necessidades do seu negócio. Isso minimizará seu potencial de tráfego fraudulento. Para mais orientações sobre como prevenir o bombeamento de tráfego de SMS, consulte as [Perguntas frequentes sobre fraude de bombeamento de tráfego de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilidade de envios bloqueados {#visibility-of-blocked-sends}

Tentativas de envio para países que não estão na sua lista de permissões serão abortadas. Mensagens abortadas serão registradas no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) e no [evento de engajamento com mensagem de SMS abortado]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

Mensagens abortadas causadas por envios bloqueados aparecem como **Aborted Message Errors** e exibem a mensagem "The recipient's phone number is in a blocked country".

![Registro de abortos mostrando vários envios de SMS que foram bloqueados porque o número de telefone está em um país bloqueado.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}