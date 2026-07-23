---
nav_title: Rastrear desinstalações
article_title: Rastrear desinstalações através do SDK da Braze
page_order: 3.5
description: "Aprenda como rastrear desinstalações através do SDK da Braze."

---

# Rastrear desinstalações {#track-uninstalls}

> Aprenda como configurar o rastreamento de desinstalações através do SDK da Braze. Para informações gerais, consulte [Guia do Usuário: Rastreamento de desinstalações]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

{% sdktabs %}
{% sdktab android %}
## Configuração do rastreamento de desinstalação {#setting-up-uninstall-tracking}

### Etapa 1: Configurar a FCM {#step-1-set-up-fcm}

O SDK do Android da Braze usa o Firebase Cloud Messaging (FCM) para enviar notificações por push silenciosas, que são usadas para coletar análises de dados de rastreamento de desinstalação. Caso ainda não o tenha feito, [configure]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#android_setting-up-push-notifications) ou [migre para a]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) API Firebase Cloud Messaging para notificações por push.

### Etapa 2: Detectar manualmente o rastreamento de desinstalação (opcional) {#step-2-manually-detect-uninstall-tracking-optional}

Por padrão, o SDK do Android da Braze detecta e ignora automaticamente as notificações por push silenciosas relacionadas ao rastreamento de desinstalação. No entanto, se você optar por detectar manualmente o rastreamento de desinstalação, use o método [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html).

{% alert important %}
Como as notificações silenciosas para rastreamento de desinstalação não são encaminhadas para nenhum retorno de chamada por push da Braze, você só pode usar esse método antes de passar uma notificação por push para a Braze.
{% endalert %}

### Etapa 3: Remover pings automáticos do servidor {#step-3-remove-automatic-server-pings}

Uma notificação por push silenciosa ativa seu app e instancia o componente `Application` se o app ainda não estiver em execução. Portanto, se você tiver uma subclasse [`Application`](https://developer.android.com/reference/android/app/Application) personalizada, remova qualquer lógica que faça pings automáticos nos seus servidores durante o método de ciclo de vida [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()).

### Etapa 4: Ativar o rastreamento de desinstalação {#step-4-enable-uninstall-tracking}

Por fim, ative o rastreamento de desinstalação na Braze. Para um passo a passo completo, consulte [Ativar o rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
O rastreamento de desinstalações pode ser impreciso. As métricas que você vê na Braze podem estar atrasadas ou imprecisas.
{% endalert %}

{% endsdktab %}

{% sdktab swift %}
## Configuração do rastreamento de desinstalação

### Etapa 1: Ativar push em segundo plano {#step-1-enable-background-push}

Em seu projeto Xcode, acesse **Capabilities** e verifique se **Background Modes** está ativado. Para saber mais, consulte [notificação por push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Etapa 2: Ignorar notificações por push internas {#step-2-ignore-internal-push-notifications}

O SDK do Swift da Braze usa notificações por push em segundo plano para coletar análises de dados de rastreamento de desinstalação. Certifique-se de que seu app [ignore as notificações por push internas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) para que ele não realize ações indesejadas quando elas forem enviadas.

### Etapa 3: Enviar um push de teste (opcional) {#step-3-send-a-test-push-optional}

Em seguida, envie a si mesmo uma notificação por push de teste pelo dashboard da Braze (não se preocupe&#8212;ela não atualiza seu perfil de usuário).

1. Acesse **Messaging** > **Campaigns** e crie uma campanha de notificação por push usando a plataforma relevante.
2. Acesse **Settings** > **App Settings** e adicione a chave `appboy_uninstall_tracking` com o valor `true` relevante e, em seguida, marque **Add Content-Available Flag**.
3. Use a página de **prévia** para enviar a si mesmo um push de teste de rastreamento de desinstalação.
4. Verifique se o seu app não realiza nenhuma ação automática indesejada ao receber uma notificação por push.

{% alert note %}
Um número de badge é enviado junto com a notificação por push de teste&#8212;no entanto, um push real de rastreamento de desinstalação não envia nenhum número de badge.
{% endalert %}

### Etapa 4: Ativar o rastreamento de desinstalação

Por fim, ative o rastreamento de desinstalação na Braze. Para um passo a passo completo, consulte [Ativar o rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
O rastreamento de desinstalações pode ser impreciso. As métricas que você vê na Braze podem estar atrasadas ou imprecisas.
{% endalert %}

{% endsdktab %}
{% endsdktabs %}