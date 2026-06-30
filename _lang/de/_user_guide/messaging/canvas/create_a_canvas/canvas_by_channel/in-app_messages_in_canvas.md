---
nav_title: In-App-Nachrichten
article_title: In-App-Nachrichten in Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt Features und Besonderheiten von In-App-Nachrichten, die Sie Ihrem Canvas hinzufügen können, um reichhaltiges Messaging anzuzeigen."
tool: Canvas
channel: in-app messages

---

# In-App-Nachrichten in Canvas {#in-app-messages-in-canvas}

> Sie können In-App-Nachrichten als Teil Ihrer Canvas-Journey hinzufügen, um reichhaltiges Messaging anzuzeigen, wenn Ihre Kund:innen mit Ihrer App interagieren.

## So funktioniert es {#how-it-works}

Bevor Sie In-App-Nachrichten in Ihrem Canvas verwenden können, stellen Sie sicher, dass ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit Verzögerungs- und Zielgruppenoptionen eingerichtet ist.

Fügen Sie im Canvas-Builder einen [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)-Schritt hinzu und wählen Sie **In-App Message** als Ihren **Messaging Channel**. Sie können anpassen, [wann Ihre Nachricht abläuft](#in-app-message-expiration) und welches [Fortschrittsverhalten](#advancement-behavior) sie haben soll.

Wenn Ihr Workspace mehrere Apps hat, sprechen Sie die richtige App über **Zustellungsplattformen**, {% raw %}`{{targeted_device.${platform}}}`{% endraw %} oder {% raw %}`{{app.${api_id}}}`{% endraw %} Liquid-Tags an – nicht über Zustellungsvalidierungen. In-App-Nachrichten werden nur angezeigt, wenn Nutzer:innen die Ziel-App öffnen und die Trigger-Kriterien des Schritts erfüllen. Weitere Informationen finden Sie unter [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).

## Eine In-App-Nachricht zu Ihrer User-Journey hinzufügen {#adding-an-in-app-message-to-your-user-journey}

Um eine In-App-Nachricht zu Ihrem Canvas hinzuzufügen, gehen Sie wie folgt vor:

1. Fügen Sie einen [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)-Schritt zu Ihrer User-Journey hinzu.
2. Wählen Sie **In-App Message** als Ihren **Messaging Channel**.
3. Legen Sie fest, [wann Ihre Nachricht abläuft](#in-app-message-expiration) und welches [Fortschrittsverhalten](#advancement-behavior-options) sie haben soll.

## Getriggerte In-App-Nachrichten {#triggered-in-app-messages}

Sie können einen Trigger für Ihre In-App-Nachrichten auswählen, der bei Sitzungsstart oder durch angepasste Events und Käufe ausgelöst wird.

Nachdem alle Verzögerungen abgelaufen sind und die Zielgruppenoptionen geprüft wurden, werden In-App-Nachrichten aktiviert, wenn Nutzer:innen den Nachrichten-Schritt erreichen. Wenn Nutzer:innen eine Sitzung starten und das Trigger-Event für die In-App-Nachricht ausführen, wird ihnen die In-App-Nachricht angezeigt.

Für Canvas-Schritte mit aktionsbasiertem Eintritt können Nutzer:innen den Canvas mitten in einer Sitzung betreten. In-App-Nachrichten werden erst aktiviert, wenn eine Sitzung startet. Wenn sich Nutzer:innen also mitten in einer Sitzung befinden, wenn sie den Nachrichten-Schritt erreichen, erhalten sie die In-App-Nachricht erst, wenn sie eine weitere Sitzung starten und den entsprechenden Trigger ausführen.

## Ablauf von In-App-Nachrichten {#in-app-message-expiration}

Sie können festlegen, wann die In-App-Nachricht abläuft. Während dieser Zeit wartet die In-App-Nachricht darauf, angesehen zu werden, bis das Ablaufdatum erreicht ist. Nachdem die In-App-Nachricht gesendet wurde, kann sie einmal angesehen werden.

![Der Abschnitt „Nachrichtensteuerung“ eines Nachrichten-Schritts für eine In-App-Nachricht. Die In-App-Nachricht läuft drei Tage nach Verfügbarkeit des Schritts ab.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Option | Beschreibung | Beispiel |
|---|---|---|
| **Eine Dauer nach Verfügbarkeit des Schritts** | Legt fest, dass die In-App-Nachricht relativ zum Zeitpunkt abläuft, an dem der Schritt für die Nutzer:innen verfügbar wird. | Eine In-App-Nachricht mit einem Ablauf von zwei Tagen wird verfügbar, wenn Nutzer:innen den Nachrichten-Schritt betreten und die Zielgruppenoptionen geprüft werden. Eventuelle Verzögerungen vor Erreichen dieses Schritts stammen aus vorhergehenden Verzögerungsschritten in Ihrem Canvas. Die In-App-Nachricht wäre dann 2 Tage (48 Stunden) ab dem Zeitpunkt verfügbar, an dem die Nutzer:innen den Schritt betreten, und während dieser zwei Tage können Nutzer:innen die In-App-Nachricht sehen, wenn sie die App öffnen. |
| **Zu einem bestimmten Datum und Uhrzeit** | Wählen Sie ein bestimmtes Datum und eine Uhrzeit, ab der die In-App-Nachricht nicht mehr verfügbar ist. | Wenn Sie einen Sale haben, der am 30. November 2024 endet, wählen Sie diese Option, damit Nutzer:innen die zugehörige In-App-Nachricht nicht mehr sehen, wenn der Sale endet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ablauf von In-App-Nachrichten" }

Wenn Nutzer:innen eine Sitzung starten, prüft Braze, ob sich ihre Berechtigung oder der Ablauf für In-App-Nachrichten geändert hat, und sendet aktualisierte Ablaufinformationen an ihr Gerät.

Wenn eine In-App-Nachricht so eingestellt ist, dass sie zu einem bestimmten Datum und einer bestimmten Uhrzeit abläuft, die bereits vergangen ist, wenn Nutzer:innen den Nachrichten-Schritt erreichen, erhalten diese Nutzer:innen die In-App-Nachricht nicht. Sie durchlaufen den Canvas weiterhin gemäß Ihrem [Fortschrittsverhalten](#advancement-behavior) für diesen Schritt.

Dies passiert häufig, wenn ein vorhergehender Schritt, wie z. B. ein [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), Nutzer:innen auf einem längeren Pfad hält. Wenn Sie beispielsweise am 22. Mai einen Canvas mit einer 72-stündigen Verzögerung starten, gefolgt von einer In-App-Nachricht, die am 23. Mai um Mitternacht abläuft, erreichen Nutzer:innen den Nachrichten-Schritt nach der Ablaufzeit und sehen die In-App-Nachricht nicht.

## Anwendungsfälle {#use-cases}

Braze empfiehlt, dieses Feature in Ihren Werbe- und Onboarding-Canvases zu verwenden.

{% tabs %}
  {% tab Werbeaktionen %}

Aktionen, Gutscheine und Sales haben oft feste Ablaufdaten. Der folgende Canvas sollte Ihre Nutzer:innen zu den günstigsten Zeitpunkten darauf aufmerksam machen, dass es eine Aktion gibt, die sie nutzen können, und möglicherweise einen Kauf beeinflussen. Diese Aktion läuft am 28. Februar 2019 um 11:15 Uhr in der Zeitzone Ihres Unternehmens ab.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Anwendungsfälle" class="tg">
  <caption>Anwendungsfälle</caption>
<thead>
  <tr>
    <th>Canvas-Schritt</th>
    <th>Verzögerung</th>
    <th>Zielgruppe</th>
    <th>Kanal</th>
    <th>Ablauf</th>
    <th>Fortschritt</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Tag 1: 50 % Rabatt</td>
    <td>Keine</td>
    <td>Alle ab Eintritt</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Zielgruppe nach Verzögerung voranbringen</td>
    <td>Erste Push-Benachrichtigung, die Ihre Nutzer:innen auf die Aktion aufmerksam macht. Diese soll Nutzer:innen in Ihre App bringen, um die Aktion zu nutzen.</td>
  </tr>
  <tr>
    <td>In-App: 50 % Rabatt</td>
    <td>Keine</td>
    <td>Alle ab Eintritt</td>
    <td>In-App-Nachricht</td>
    <td><b>Läuft ab:</b> 28.02.2019 11:15 Uhr Unternehmenszeit</td>
    <td>In-App-Nachricht angesehen</td>
    <td>Die Nutzer:innen haben nun die App geöffnet und erhalten diese Nachricht, unabhängig davon, ob dies aufgrund der vorherigen Push-Benachrichtigung geschah oder nicht.</td>
  </tr>
  <tr>
    <td>50 %-Rabatt-Erinnerung</td>
    <td>1 Tag nachdem die Nutzer:innen den vorherigen Schritt erhalten haben</td>
    <td>Alle ab Eintritt <br><br><b>Filter:</b> Letzter Kauf vor mehr als einer Woche</td>
    <td>In-App-Nachricht</td>
    <td><b>Läuft ab:</b> 28.02.2019 11:15 Uhr Unternehmenszeit</td>
    <td>Keine (letzte Nachricht im Canvas)</td>
    <td>Die Nutzer:innen haben die In-App-Nachricht im vorherigen Schritt erhalten, aber trotz Nutzung der App keinen Kauf getätigt. <br><br>Diese Nachricht soll die Nutzer:innen weiter dazu bewegen, die Aktion für einen Kauf zu nutzen.</td>
  </tr>
</tbody>
</table>

Die In-App-Nachrichten laufen ab, wenn die Aktion endet, um Diskrepanzen zwischen dem Messaging und dem Kundenerlebnis zu vermeiden.

  {% endtab %}
  {% tab Nutzer:innen-Onboarding %}

Ihr erster Eindruck bei Nutzer:innen ist möglicherweise der wichtigste. Er kann über zukünftige Besuche in Ihrer App entscheiden. Ihre erste Kommunikation mit Ihren Nutzer:innen sollte sinnvoll getimed sein und häufige Besuche in Ihrer App fördern, um die Nutzung zu steigern.

<table aria-label="Anwendungsfälle" class="tg">
  <caption>Anwendungsfälle</caption>
<thead>
  <tr>
    <th>Canvas-Schritt</th>
    <th>Verzögerung</th>
    <th>Zielgruppe</th>
    <th>Kanal</th>
    <th>Ablauf</th>
    <th>Fortschritt</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Willkommens-E-Mail</td>
    <td>Keine</td>
    <td>Alle ab Eintritt</td>
    <td>E-Mail</td>
    <td>N/A</td>
    <td>Zielgruppe nach Verzögerung voranbringen</td>
    <td>Erste E-Mail, die Ihre Nutzer:innen in einem Projekt, einer Mitgliedschaft oder einem anderen Onboarding-Programm willkommen heißt. <br><br>Diese soll Nutzer:innen in Ihre App bringen, um mit dem Onboarding zu beginnen.</td>
  </tr>
  <tr>
    <td>Tag 3–6 In-App-Nachricht</td>
    <td>3 Tage nachdem die Nutzer:innen den vorherigen Schritt erhalten haben</td>
    <td>Alle ab Eintritt</td>
    <td>In-App-Nachricht</td>
    <td><b>Läuft ab:</b> 3 Tage nach Verfügbarkeit des Schritts</td>
    <td>In-App-Nachricht aktiv</td>
    <td>Wenn die Nutzer:innen auf die E-Mail reagiert haben und in die App gelangt sind, erhalten sie die gewünschte In-App-Nachricht, um ihr Onboarding fortzusetzen oder sie daran zu erinnern, einschließlich aller damit verbundenen Anforderungen.</td>
  </tr>
  <tr>
    <td>Tag 5 Push</td>
    <td>2 Tage nachdem die Nutzer:innen den vorherigen Schritt erhalten haben</td>
    <td>Alle ab Eintritt</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Nachricht gesendet</td>
    <td>Nachdem Nutzer:innen ihre In-App-Nachricht erhalten haben, bekommen sie eine Follow-up-Push-Benachrichtigung, um ihr Onboarding fortzusetzen.</td>
  </tr>
</tbody>
</table>

Diese Push-Benachrichtigungen sind um eine In-App-Nachricht herum platziert, um sicherzustellen, dass die Nutzer:innen die App besucht und ihr Onboarding begonnen haben. Dies hilft, Spam oder Nachrichten in falscher Reihenfolge zu vermeiden, die Nutzer:innen davon abhalten könnten, Ihre App zu besuchen, und schafft stattdessen einen fließenden, sinnvollen Ablauf für ihre ersten Erfahrungen mit Ihrer App.

  {% endtab %}
{% endtabs %}


## Priorisierung von In-App-Nachrichten {#prioritizing-in-app-messages}

Nutzer:innen können zwei In-App-Nachrichten innerhalb Ihres Canvas gleichzeitig triggern. In diesem Fall hält sich Braze an die folgende Prioritätsreihenfolge, um zu bestimmen, welche In-App-Nachricht angezeigt wird.

Wählen Sie **Genaue Priorität festlegen** und ziehen Sie verschiedene Canvas-Schritte per Drag-and-Drop, um ihre Priorität für den Canvas neu zu ordnen. Standardmäßig werden Schritte, die früher in einer Canvas-Variante erscheinen, vor späteren Schritten angezeigt. Nachdem Ihre Schritte in der gewünschten Prioritätsreihenfolge sind, wählen Sie **Sortierung anwenden**.

![Der Prioritäts-Sortierer mit zwei Schritten „Welcome IAM“ und „Followup IAM“.]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Änderungen an Entwürfen aktiver Canvases vornehmen {#making-changes-to-drafts-of-active-canvases}

Wenn Sie Änderungen an der In-App-Nachrichten-Priorität in den **Sendeeinstellungen** eines Entwurfs eines aktiven Canvas vornehmen, werden diese Änderungen direkt auf den aktiven Canvas angewendet, wenn der Prioritäts-Sortierer geschlossen wird. In einem Nachrichten-Schritt wird der Prioritäts-Sortierer jedoch erst aktualisiert, wenn der Entwurf gestartet wird, da Canvas-Schritt-Einstellungen auf Schrittebene gelten.

## Fortschrittsverhalten {#advancement-behavior}

Nachrichten-Schritte bringen automatisch alle Nutzer:innen voran, die den Schritt betreten. Es wird nicht darauf gewartet, dass die In-App-Nachricht getriggert oder angezeigt wird. Es ist nicht erforderlich, ein Nachrichtenfortschrittsverhalten festzulegen, was die Konfiguration des gesamten Schritts vereinfacht.

Wenn Nutzer:innen einen In-App-Nachrichten-Schritt betreten, werden sie sofort weitergeleitet, anstatt für das Ablaufzeitfenster gehalten zu werden. In diesem Fall kann ein Verzögerungsschritt in Ihrer User-Journey hilfreich sein.

Um die Option **Fortschritt bei gesendeter Nachricht** zu verwenden, fügen Sie einen separaten [Zielgruppenpfad]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) hinzu, um Nutzer:innen zu filtern, die den vorherigen Schritt nicht erhalten haben.

{% details Originaler Canvas-Editor %}

Sie können keine Canvases mehr mit dem originalen Editor erstellen oder duplizieren. Dieser Abschnitt dient als Referenz, um zu verstehen, wie das Fortschrittsverhalten für Schritte mit In-App-Nachrichten funktioniert.

Canvases, die im originalen Editor erstellt wurden, müssen ein Fortschrittsverhalten angeben – die Kriterien für den Fortschritt durch Ihre Canvas-Komponente. [Schritte mit ausschließlich In-App-Nachrichten](#steps-iam-only) haben andere Fortschrittsoptionen als [Schritte mit mehreren Nachrichtentypen](#steps-multiple-channels) (wie Push oder E-Mail). Für In-App-Nachrichten im aktuellen Canvas-Workflow ist diese Option so eingestellt, dass die Zielgruppe immer sofort vorangebracht wird.

Aktionsbasierte Zustellung ist für Canvas-Schritte mit In-App-Nachrichten nicht verfügbar. Canvas-Schritte mit In-App-Nachrichten müssen geplant werden. Stattdessen erscheinen Canvas-In-App-Nachrichten beim ersten Mal, wenn Ihre Nutzer:innen die App öffnen (getriggert durch den Sitzungsstart), nachdem die geplante Nachricht in der Canvas-Komponente an sie gesendet wurde.

Wenn Sie mehrere In-App-Nachrichten innerhalb eines Canvas haben, müssen Nutzer:innen mehrere Sitzungen starten, um jede dieser einzelnen Nachrichten zu erhalten.

{% alert important %}
Wenn **Fortschritt bei aktiver In-App-Nachricht** ausgewählt ist, bleibt die In-App-Nachricht bis zu ihrem Ablauf verfügbar, auch wenn die Nutzer:innen zu nachfolgenden Schritten übergegangen sind. Wenn Sie nicht möchten, dass die In-App-Nachricht aktiv ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass der Ablauf kürzer ist als die Verzögerung bei nachfolgenden Schritten.
{% endalert %}

### Schritte mit mehreren Kanälen {#steps-multiple-channels}

Schritte mit einer In-App-Nachricht und einem weiteren Kanal haben die folgenden Fortschrittsoptionen:

| Option | Beschreibung |
|---|---|
| Fortschritt bei gesendeter Nachricht | Nutzer:innen müssen eine E-Mail, einen Webhook oder eine Push-Benachrichtigung erhalten oder die In-App-Nachricht angesehen haben, um zu nachfolgenden Schritten im Canvas fortzuschreiten. <br> <br> Wenn die In-App-Nachricht abläuft und die Nutzer:innen keine E-Mail, keinen Webhook oder keine Push-Benachrichtigung erhalten haben oder die In-App-Nachricht nicht angesehen haben, verlassen sie den Canvas und schreiten nicht zu nachfolgenden Schritten fort. |
| Zielgruppe sofort voranbringen | Alle in der Zielgruppe des Schritts schreiten zu den nächsten Schritten fort, nachdem die Verzögerung abgelaufen ist, unabhängig davon, ob sie die genannte Nachricht gesehen haben oder nicht. <br> <br> Nutzer:innen müssen die Segment- und Filterkriterien des Schritts erfüllen, um zu den nächsten Schritten fortzuschreiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritte mit mehreren Kanälen" }

{% alert important %}
Wenn **Gesamte Zielgruppe** ausgewählt ist, bleibt die In-App-Nachricht bis zu ihrem Ablauf verfügbar, auch wenn die Nutzer:innen zu nachfolgenden Schritten übergegangen sind. Wenn Sie nicht möchten, dass die In-App-Nachricht aktiv ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass der Ablauf kürzer ist als die Verzögerung bei nachfolgenden Schritten.
{% endalert %}

{% enddetails %}

## Trigger-Aktionen {#trigger-actions}

Sie können aus den folgenden Trigger-Aktionen wählen, um Ihre Nutzer:innen anzusprechen:

- **Kauf tätigen:** Sprechen Sie Nutzer:innen an, die einen beliebigen oder einen bestimmten Kauf tätigen.
- **Sitzung starten:** Sprechen Sie Nutzer:innen an, die eine Sitzung in einer beliebigen oder einer bestimmten App starten.
- **Angepasstes Event ausführen:** Sprechen Sie Nutzer:innen an, die das ausgewählte angepasste Event ausführen (das angepasste Event muss über das SDK gesendet werden).

Nutzer:innen müssen den Canvas-Schritt betreten, eine Sitzung starten und dann den Trigger ausführen, um eine In-App-Nachricht zu erhalten. Das bedeutet, dass Updates mitten in einer Sitzung nicht unterstützt werden. Wenn der Trigger beispielsweise das Starten einer Sitzung ist, müssen die Nutzer:innen nur den Canvas-Schritt betreten und eine Sitzung starten, um die In-App-Nachricht zu erhalten. Wenn der Trigger nicht das Starten einer Sitzung ist, müssen die Nutzer:innen den Canvas-Schritt betreten, eine Sitzung starten und dann den Trigger ausführen, um die In-App-Nachricht zu erhalten.

![„Einen bestimmten Kauf tätigen“ als Trigger-Aktion ausgewählt.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Die folgenden Canvas-Features sind bei In-App-Nachrichten nicht verfügbar und werden daher nicht auf Ihre In-App-Nachrichten angewendet, auch wenn sie aktiviert sind.

- Intelligentes Timing
- Rate-Limiting
- Frequency-Capping
- Ausstiegskriterien
- Ruhezeiten

## Angepasste Event-Eigenschaften in einem Canvas {#custom-event-properties-in-a-canvas}

Angepasste Event-Eigenschaften in In-App-Nachrichten für Canvas werden unterstützt. Diese Eigenschaften stammen jedoch vom angepassten Event oder Kauf, der die In-App-Nachricht triggert, die sich im Nachrichten-Schritt befindet, nicht vom vorhergehenden Aktions-Pfad.

## Hinweise {#considerations}

Hier sind einige Hinweise zum Senden von In-App-Nachrichten in einem Canvas.

- Wenn die Nutzer:innen die App nie neu starten oder nie eine Sitzung starten, kann die App nicht feststellen, ob die Nutzer:innen für die In-App-Nachricht berechtigt sind, was bedeutet, dass keine In-App-Nachricht gesendet wird.
- Wenn der erste Klick erfolgt und eine Canvas-Kontextvariable (Canvas-Eingangs-Eigenschaften) vorhanden ist und Nutzer:innen einen Canvas fünfmal erneut betreten, verwendet Braze den fünften Eintritt und nutzt diese Kontextvariable in der In-App-Nachricht.
- Nutzer:innen können für bis zu 10 In-App-Nachrichten innerhalb desselben Canvas-Schritts berechtigt sein. Wenn ein Canvas beispielsweise den erneuten Eintritt erlaubt und Nutzer:innen den Canvas 11 Mal betreten, werden ihnen nur 10 In-App-Nachrichten gesendet, sofern keine abgelaufen sind.