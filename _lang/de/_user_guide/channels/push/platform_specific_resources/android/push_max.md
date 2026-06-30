---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max verstärkt Android-Push-Benachrichtigungen, indem fehlgeschlagene Push-Benachrichtigungen nachverfolgt und erneut gesendet werden, wenn die Nutzer:innen die Push-Benachrichtigung mit höherer Wahrscheinlichkeit empfangen."

permalink: /user_guide/channels/push/platform_specific_resources/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Erfahren Sie mehr über Push Max und wie Sie dieses Feature nutzen können, um die Zustellbarkeit von Android-Push-Benachrichtigungen an [chinesische OEM-Geräte]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability) potenziell zu verbessern.

## Was ist Push Max? {#what-is-push-max}

Push Max verstärkt Android-Push-Benachrichtigungen, indem fehlgeschlagene Push-Benachrichtigungen nachverfolgt und erneut gesendet werden, wenn die Nutzer:innen die Push-Benachrichtigung mit höherer Wahrscheinlichkeit empfangen.

Einige Android-Geräte, die von chinesischen Originalgeräteherstellern (OEMs) wie Xiaomi, OPPO und Vivo hergestellt werden, verwenden ein umfangreiches Batterieoptimierungsschema, um die Akkulaufzeit zu verlängern. Dieses Verhalten kann die unbeabsichtigte Folge haben, dass die Hintergrundverarbeitung von Apps beendet wird, was die Zustellbarkeit von Push-Benachrichtigungen auf diesen Geräten verringert, wenn die App nicht im Vordergrund ist. Dieser Umstand tritt am häufigsten in den Märkten des asiatisch-pazifischen Raums (APAC) auf.

## Verfügbarkeit {#availability}

- Nur für Android-Push-Benachrichtigungen verfügbar
- Nicht unterstützt für aktionsbasierte oder API-getriggerte Nachrichten
- Nicht unterstützt, wenn die Option [nur an das zuletzt verwendete Gerät senden]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#device-options) ausgewählt ist

## Voraussetzungen {#prerequisites}

Push-Benachrichtigungen, die mit Push Max gesendet werden, werden nur an Geräte zugestellt, die mindestens die folgende [SDK-Mindestversion]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions) haben:

{% sdk_min_versions android:29.0.1 %}

## Push Max verwenden {#using-push-max}

{% tabs %}
{% tab Campaigns %}

So verwenden Sie Push Max in Ihrer Campaign:

1. Erstellen Sie eine Push-Campaign.
2. Wählen Sie **Android Push** als Plattform aus.
3. Gehen Sie zum Schritt **Schedule Delivery**.
4. Wählen Sie **Send using Push Max** aus.

![Abschnitt „Android Push Deliverability“ im Schritt „Schedule Delivery“ mit der Option „Send using Push Max“.]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

So verwenden Sie Push Max in Ihrem Canvas:

1. Fügen Sie Ihrem Canvas einen Nachrichtenschritt hinzu.
2. Wählen Sie **Android Push** als Plattform aus.
3. Gehen Sie zum Tab **Delivery Settings**.
4. Wählen Sie **Send using Push Max** aus.

![Tab „Delivery Settings“ eines Android-Push-Nachrichtenschritts mit der Option „Send using Push Max“.]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Die folgenden beiden Features, intelligentes Timing und Time to Live, können in Kombination mit Push Max verwendet werden, um die Zustellbarkeit Ihrer Android-Push-Benachrichtigungen potenziell zu erhöhen.

### Intelligentes Timing {#intelligent-timing}

Push Max funktioniert am besten, wenn [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) aktiviert ist. Intelligentes Timing kann den optimalen Zeitpunkt berechnen und die Push-Benachrichtigung dann senden, wenn die Nutzer:innen die App am wahrscheinlichsten verwenden und die Push-Benachrichtigung am wahrscheinlichsten zugestellt wird.

### Time to Live (TTL) {#time-to-live-ttl}

Time to Live (TTL) kann fehlgeschlagene Push-Benachrichtigungen an Firebase Cloud Messaging (FCM) nachverfolgen und die Benachrichtigung erneut senden, wenn die Nutzer:innen sie wahrscheinlich empfangen.

Standardmäßig ist Time to Live auf 28 Tage eingestellt, was dem Maximum entspricht. Sie können den Standard-TTL-Wert für alle neuen Android-Push-Nachrichten unter **Einstellungen** > **Workspace-Einstellungen** > **Push-Einstellungen** verringern oder die Anzahl der Tage pro Nachricht im Tab **Settings** beim Erstellen einer Android-Push-Benachrichtigung konfigurieren.

![Feld „Time to Live“ auf 28 Tage eingestellt.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Wissenswertes {#things-to-know}

### Aktionscodes {#promotion-codes}

Wir empfehlen, keine Braze-[Aktionscodes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) in Nachrichten zu verwenden, bei denen Push Max aktiviert ist.

Der Grund dafür ist, dass Aktionscodes eindeutig sind. Wenn eine Push-Benachrichtigung, die einen Aktionscode enthält, nicht zugestellt werden kann und diese Benachrichtigung aufgrund von Push Max erneut gesendet wird, wird ein neuer Aktionscode gesendet. Dies kann dazu führen, dass Aktionscodes schneller als erwartet verbraucht werden.

### Canvas-Event-Eigenschaften und Eingangs-Eigenschaften {#canvas-event-properties-and-entry-properties}

Push Max funktioniert möglicherweise nicht wie erwartet, wenn Sie Liquid-Referenzen auf [Canvas-Eingangs-Eigenschaften oder Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) in Ihrer Nachricht verwenden. Dies liegt daran, dass die Eingangs- und Event-Eigenschaften nicht verfügbar sind, wenn Push Max versucht, die Nachricht erneut zu senden.