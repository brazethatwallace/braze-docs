---
nav_title: Push-Einstellungen
article_title: Push-Einstellungen
page_order: 5
page_type: reference
description: "Dieser Artikel bietet eine Übersicht über die Push-Einstellungen im Braze-Dashboard."
channel: push

---

# Push-Einstellungen {#push-settings}

> Auf der Seite **Push-Einstellungen** können Sie die wichtigsten Einstellungen für Ihre Push-Benachrichtigungen konfigurieren, darunter die Push-Time-to-Live (TTL) und die Standard-FCM-Priorität für Android-Campaigns. Mit diesen Einstellungen können Sie die Zustellung und Effektivität Ihrer Push-Benachrichtigungen optimieren und so ein besseres Erlebnis für Ihre Nutzer:innen gewährleisten.

## Was ist Push TTL? {#what-is-push-ttl}

Die Push-Time-to-Live (TTL) steuert, wie lange Braze versucht, eine Push-Benachrichtigung an Geräte zuzustellen, die zum Zeitpunkt der Versendung der Campaign offline sind. Wenn ein Gerät die Verbindung nach Ablauf der TTL wieder aufnimmt, wird die Nachricht nicht zugestellt. Mit dieser Einstellung wird eine Benachrichtigung nicht entfernt, wenn sie bereits auf dem Gerät der Nutzer:innen eingegangen ist – sie steuert nur, wie lange der Push-Anbieter versucht, eine Benachrichtigung zuzustellen.

## Einstellung der Standard-Push-TTL-Werte {#setting-default-push-ttl-values}

Standardmäßig setzt Braze die Push TTL für jeden Push-Messaging-Dienst auf das Maximum.

| Push-Messaging-Dienst | Maximale TTL |
| --- | --- |
| Internet (über FCM- oder Web-Push-Dienste) | 28 Tage |
| Firebase Cloud Messaging (FCM) | 28 Tage |
| Kindle (ADM) | 31 Tage |
| Huawei (HMS) | 15 Tage |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Diese Einstellungen gelten global für alle Push-Campaigns, sofern für eine bestimmte Nachricht keine andere TTL festgelegt wird. Informationen zum Anpassen der TTL einer Nachricht finden Sie unter [Erweiterte Campaign-Einstellungen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#ttl).

So legen Sie eine andere Standard-Push-TTL fest:

1. Gehen Sie zu **Settings** > **Manage Settings** > **Push Settings**.
2. Definieren Sie für jede Android-Plattform einen Standard-Time-to-Live-Wert. Sie können kleinere Einheiten wie Stunden oder Sekunden für eine präzisere Steuerung verwenden.
3. Wählen Sie **Save**, um Ihre Änderungen zu übernehmen.

![Push-TTL-Einstellungen für Firebase-, Internet-, Kindle- und Huawei-Geräte.]({% image_buster /assets/img/push_ttl.png %})

## Standard-FCM-Priorität für Android-Campaigns {#default-fcm-priority-for-android-campaigns}

Sie können die Standard-Firebase-Cloud-Messaging-Priorität (FCM) für alle Android-Push-Campaigns festlegen. Diese Priorität bestimmt, wie die Push-Benachrichtigung an die Geräte der Nutzer:innen zugestellt wird.

Zu den FCM-Prioritätsoptionen gehören:

| Priorität | Beschreibung | Anwendungsfall |
| --- | --- | --- |
| Normal | Standard-Zustellpriorität, die den Akkuverbrauch optimiert | Inhalte, die keine sofortige Aufmerksamkeit erfordern |
| High | Nachrichten werden sofort gesendet | Zeitkritische Benachrichtigungen, die eine umgehende Zustellung erfordern |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

So legen Sie die Standard-FCM-Priorität fest:

1. Gehen Sie zu **Settings** > **Manage Settings** > **Push Settings**.
2. Wählen Sie im Abschnitt „FCM Priority“ entweder „Normal“ oder „High“ als Standardeinstellung aus.
3. Wählen Sie **Save**, um Ihre Änderungen zu übernehmen.

![Einstellungen für die Android-Zustellpriorität.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Diese Einstellung gilt global für alle neuen Android-Push-Campaigns, sofern beim Erstellen einer bestimmten Campaign keine andere Priorität ausgewählt wird.

{% alert note %}
Wenn FCM feststellt, dass Ihre App häufig Nachrichten mit hoher Priorität sendet, die nicht zu sichtbaren Benachrichtigungen oder Engagement führen, werden diese Nachrichten möglicherweise automatisch auf die normale Priorität herabgestuft.
{% endalert %}

Ausführlichere Informationen zu FCM-Prioritätsstufen und zur Herabstufung finden Sie unter [Erweiterte Campaign-Einstellungen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#fcm-priority).