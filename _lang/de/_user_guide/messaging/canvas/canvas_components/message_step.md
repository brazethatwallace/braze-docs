---
nav_title: Nachricht
article_title: Nachricht
alias: "/message_step/"
page_order: 11
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie mit dem Nachrichten-Schritt eine eigenständige Nachricht erstellen."
tool: Canvas

---

# Nachricht {#message}

> Mit Nachrichten-Schritten können Sie an jeder gewünschten Stelle in Ihrem Canvas eine eigenständige Nachricht hinzufügen.

![Ein Nachrichten-Schritt namens „Lunch promo“ mit dem Push-Kanal.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Eine Nachricht erstellen {#create-a-message}

Um eine Nachrichten-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Nachricht**.

### 1. Schritt: Messaging-Kanal auswählen {#step-1-select-your-messaging-channel}

Sie können aus den folgenden Messaging-Kanälen auswählen:
- Banner
- Content Cards
- E-Mail
- LINE
- Push-Benachrichtigungen
- SMS/MMS/RCS
- In-App-Nachrichten
- Webhook
- WhatsApp

![Eine Liste der verfügbaren Messaging-Kanäle zur Auswahl für den Nachrichten-Schritt.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### 2. Schritt: Zustellungseinstellungen bearbeiten {#step-2-edit-delivery-settings}

Als Nächstes können Sie die Einstellungen für intelligentes Timing, Ruhezeiten-Überschreibungen und Zustellungsvalidierung bearbeiten.

#### Intelligentes Timing {#intelligent-timing}

Sie können [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) mit einer Fallback-Option aktivieren, wenn das Profil einer Nutzerin oder eines Nutzers nicht genügend Daten enthält, um eine optimale Zeit zu berechnen. Wir empfehlen, intelligentes Timing und [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) als zusätzliche Prüfung für eventuelle Verzögerungen zwischen dem Eintritt der Nutzer:innen in den Nachrichten-Schritt und dem tatsächlichen Nachrichtenversand zu aktivieren.

Wählen Sie **Using Intelligent Timing** im Tab **Delivery Settings**. Hier können Sie entweder die beliebteste Zeit oder eine bestimmte Fallback-Zeit auswählen. Wenn Ruhezeiten aktiviert sind, ermöglicht der Nachrichten-Schritt auch die Überschreibung dieser Einstellung.

![Der Tab „Delivery Settings“ für die Einstellungen der Nachrichten-Komponente. Ruhezeiten sind aktiviert, und das Kontrollkästchen „Using Intelligent Timing“ ist ausgewählt, um die Nachricht zur optimalen Zeit zuzustellen.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

#### Zustellungsvalidierungen {#delivery-validations}

Zustellungsvalidierungen bieten eine zusätzliche Prüfung beim Nachrichtenversand, um zu bestätigen, dass Ihre Zielgruppe Ihre Kriterien noch erfüllt. Wir empfehlen die Verwendung, wenn Ruhezeiten, intelligentes Timing oder Rate-Limiting aktiviert sind. Wählen Sie **Validate audience at message send** und fügen Sie dann ein Segment oder zusätzliche Filter hinzu. Wenn Nutzer:innen die Validierungen nicht erfüllen, wählen Sie, ob sie den Canvas verlassen oder zum nächsten Schritt weitergeleitet werden.

Zustellungsvalidierungen bewerten die Nutzerprofil-Kriterien zum Zeitpunkt des Versands. App-bezogene Filter prüfen, ob Nutzer:innen eine bestimmte App kürzlich oder jemals verwendet haben, bestätigen aber nicht, welche App Nutzer:innen in ihrer aktuellen Sitzung verwenden.

Wenn Ihr Workspace mehrere Apps enthält und ein Nachrichten-Schritt auf eine bestimmte App abzielen soll, verwenden Sie stattdessen einen der folgenden Ansätze:

- Beim Erstellen der Nachricht [geben Sie Ihre Zustellungsplattformen an]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#step-2-specify-delivery-platforms), wie z. B. **Mobile Apps** oder **Web Browsers**.
- Verwenden Sie Liquid, um das Zielgerät oder die App zum Zeitpunkt des Versands zu prüfen:
  - {% raw %}`{{targeted_device.${platform}}}`{% endraw %} wertet die Plattform für die aktuelle Sitzung der Nutzer:innen aus. Weitere Informationen finden Sie unter [Informationen zum Zielgerät]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information).
  - {% raw %}`{{app.${api_id}}}`{% endraw %} wertet aus, welche App die Nachricht anfordert. Kombinieren Sie diesen Tag mit `abort_message()`, um Sendungen an die falsche App zu verhindern. Weitere Informationen finden Sie unter [Informationen zur Ziel-App]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-app-information).

![Zustellungsvalidierungen sind aktiviert, um die Zielgruppe beim Nachrichtenversand zu validieren. Das Fortschrittsverhalten der Zustellungsvalidierungen ist so eingestellt, dass Nutzer:innen zum nächsten Schritt im Canvas weitergeleitet werden, wenn die Zustellungsvalidierungen nicht erfüllt sind.]({% image_buster /assets/img/canvas_components/message_step5.png %}){: style="max-width:90%;"}

## Wie Nutzer:innen vorangebracht werden {#how-users-advance}

Alle Nutzer:innen, die den Nachrichten-Schritt betreten, werden zum nächsten Schritt weitergeleitet, wenn eine der folgenden Bedingungen erfüllt ist:

- Eine Nachricht wird gesendet
- Eine Nachricht wird durch Frequency Capping begrenzt und nicht gesendet
- Eine Nachricht wird abgebrochen
- Eine Nutzerin oder ein Nutzer ist über den Kanal nicht erreichbar, sodass die Nachricht nicht gesendet wird
- Eine Nutzerin oder ein Nutzer erfüllt die Kriterien in den **Zustellungsvalidierungen** nicht

{% raw %}
Wenn ein aktionsbasierter Canvas durch eine eingehende SMS-Nachricht getriggert wird, können Sie SMS-Eigenschaften im ersten Schritt (Nachrichten-Schritt) oder in einem Nachrichten-Schritt referenzieren, der unter einem Aktionspfade-Schritt verschachtelt ist. Zum Beispiel könnten Sie im Nachrichten-Schritt `{{sms.${inbound_message_body}}}` oder `{{sms.${inbound_media_urls}}}` verwenden.
{% endraw %}

## Kontext-Eigenschaften referenzieren {#reference-context-properties}

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Entry-Eigenschaften werden im Schritt **Entry-Zeitplan** bei der Erstellung eines Canvas konfiguriert und geben den Trigger an, der Nutzer:innen in einen Canvas eintreten lässt. Diese Eigenschaften können auch auf die Eigenschaften von Entry-Payloads in API-getriggerten Canvases zugreifen. Beachten Sie, dass das `context`-Objekt eine maximale Größenbeschränkung von 50 KB hat.

Entry-Eigenschaften können in Liquid in jedem Nachrichten-Schritt verwendet werden. Verwenden Sie das folgende Liquid, wenn Sie diese Entry-Eigenschaften referenzieren: {% raw %}``{context.${property_name}}``{% endraw %}. Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise verwendet werden zu können.

{% alert note %}
Speziell für In-App-Nachrichten-Kanäle kann `context` nur in Canvas referenziert werden.
{% endalert %}

Verwenden Sie das folgende Liquid, wenn Sie diese Entry-Eigenschaften referenzieren: {% raw %}``context.${property_name}``{% endraw %}. Beachten Sie, dass die Events angepasste Events oder Kauf-Events sein müssen, um auf diese Weise verwendet werden zu können.

{% raw %}
Betrachten Sie zum Beispiel die folgende Anfrage: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Sie könnten das Wort „shoes“ mit dem Liquid `{{context.${product_name}}}` zu einer Nachricht hinzufügen.
{% endraw %}

Sie können auch [persistente Entry-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) in jedem Nachrichten-Schritt nutzen, um Ihre Nutzer:innen durch personalisierte Schritte in Ihrem Canvas-Workflow zu führen.

### Event-Eigenschaften {#event-properties}

Event-Eigenschaften beziehen sich auf die Eigenschaften, die Sie für angepasste Events und Kauf-Events festlegen. Diese Event-Eigenschaften können in Campaigns mit aktionsbasierter Zustellung sowie in Canvases verwendet werden.

In Canvas können Event-Eigenschaften von angepassten Events und Kauf-Events in Liquid in jedem Nachrichten-Schritt verwendet werden, der auf einen [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)-Schritt folgt. Verwenden Sie zum Beispiel beim Referenzieren von `event_properties` dieses Liquid-Snippet: {% raw %}``{{event_properties.${property_name}}}``{% endraw %}

{% alert important %}
`event_properties` können nicht unabhängig von Aktionspfade-Schritten verwendet werden.
{% endalert %}

Im ersten Nachrichten-Schritt nach einem Aktionspfade-Schritt können Sie `event_properties` verwenden, die sich auf das in diesem Aktionspfade-Schritt referenzierte Event beziehen. Zwischen diesem Aktionspfade-Schritt und dem Nachrichten-Schritt können andere Schritte (die keine weiteren Aktionspfade- oder Nachrichten-Schritte sind) liegen. Beachten Sie, dass Sie nur Zugriff auf `event_properties` haben, wenn Ihr Nachrichten-Schritt auf einen Nicht-„Alle anderen“-Pfad in einem Aktionspfade-Schritt zurückverfolgt werden kann.

{% alert important %}
Sie können `event_properties` nicht im ersten Nachrichten-Schritt verwenden. Stattdessen müssen Sie `context` verwenden oder einen Aktionspfade-Schritt mit dem entsprechenden Event vor dem Nachrichten-Schritt hinzufügen, der `event_properties` enthält.
{% endalert %}

{% details Für den ursprünglichen Canvas-Editor erweitern %}

Sie können keine Canvases mehr mit dem ursprünglichen Editor erstellen oder duplizieren. Dieser Abschnitt dient nur als Referenz.

- `event_properties` können nicht in geplanten vollständigen Schritten verwendet werden. Sie können jedoch `event_properties` im ersten vollständigen Schritt eines aktionsbasierten Canvas verwenden, auch wenn der vollständige Schritt geplant ist.
- `context` kann nur im ersten vollständigen Schritt eines Canvas referenziert werden.
- Speziell für In-App-Nachrichten-Kanäle kann `context` im ursprünglichen Canvas-Editor referenziert werden, wenn Sie persistente Entry-Eigenschaften als Teil des vorherigen Early Access aktiviert haben.

{% enddetails %}

## Analytics {#analytics}

In der folgenden Tabelle finden Sie Definitionen der Metriken der Nachrichten-Komponente:

| Metrik | Beschreibung |
| --- | --- |
| *Eintritte* | Die Anzahl der Male, die der Schritt betreten wurde. Wenn Ihr Canvas eine erneute Berechtigung hat und Nutzer:innen einen Nachrichten-Schritt zweimal betreten, werden zwei Eintritte erfasst. |
| *Zum nächsten Schritt weitergeleitet* | Die Anzahl der Eintritte, die zum nächsten Schritt im Canvas weitergeleitet wurden. |
| *Sendungen* | Die Gesamtzahl der Nachrichten, die der Schritt gesendet hat. Wenn Ihr Canvas eine erneute Berechtigung hat und Nutzer:innen einen Nachrichten-Schritt zweimal betreten, werden zwei Eintritte erfasst. |
| *Eindeutige Empfänger:innen* | Die Anzahl der Nutzer:innen, die Nachrichten von diesem Schritt erhalten haben. |
| *Primäres Konversions-Event* | Die Anzahl der Male, die ein definiertes Event nach der Interaktion mit oder dem Anzeigen einer empfangenen Nachricht aus einer Braze-Campaign aufgetreten ist. Sie definieren dieses Event beim Erstellen der Campaign. |
| *Umsatz* | Der Gesamtumsatz in Dollar von Campaign-Empfänger:innen innerhalb des festgelegten primären Konversions-Fensters. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }