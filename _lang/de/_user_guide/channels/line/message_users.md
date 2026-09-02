---
nav_title: Nutzer:innen benachrichtigen
article_title: Nutzer:innen benachrichtigen
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie mit Nutzer:innen über Template-basierte Campaigns und Canvase kommunizieren können."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# LINE-Nutzer:innen benachrichtigen {#message-line-users}

> LINE ist ein Kanal für wechselseitige Kommunikation. Sie können über das reine Senden von Nachrichten hinausgehen und mithilfe von Template-basierten Campaigns und Canvase Gespräche mit Nutzer:innen führen. Dieser Artikel beschreibt die Details der Kommunikation mit Nutzer:innen, z. B. wie Sie Trigger or triggern-Wörter für eingehende Nachrichten und nicht erkannte Antworten einrichten.

Es gibt verschiedene Methoden, um über LINE mit Nutzer:innen zu kommunizieren, beispielsweise mithilfe von LINE-Trigger or triggern-Wörtern. Sie können auch Calls-to-Action (CTAs) verwenden, um das Engagement der Nutzer:innen mit Ihrem LINE-Messaging zu fördern.

## Aktionsbasierte Trigger or triggern {#action-based-triggers}

Sie können Campaigns und Canvase erstellen, die starten, verzweigen und Änderungen während der Journey vornehmen, wenn Sie eine eingehende LINE-Nachricht (eine von einer/einem Nutzer:in gesendete Nachricht) erhalten, die ein Trigger or triggern-Wort enthält. Stellen Sie sicher, dass Sie Trigger or triggern-Wörter wählen, die dem entsprechen, was Nutzer:innen voraussichtlich senden werden.

### Campaign

Legen Sie Ihre Trigger or triggern-Wörter fest, wenn Sie eine Campaign mit aktionsbasierter Zustellung planen.

![Aktionsbasierter Trigger mit „Diese Campaign an Nutzer:innen senden, die eine eingehende LINE-Nachricht an die Abo-Gruppe gesendet haben, bei der der Nachrichtentext“ und einem leeren Feld.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Legen Sie Ihre Trigger or triggern-Wörter innerhalb von [Aktionspfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) in Ihrem Canvas fest.

![Aktionspfad mit einem Trigger „Diese Campaign an Nutzer:innen senden, die eine eingehende LINE-Nachricht an die Abo-Gruppe gesendet haben, bei der der Nachrichtentext“ und einem leeren Feld.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Anforderungen {#requirements}

Jeder Buchstabe Ihres Trigger or triggern-Worts muss beim Erstellen Ihrer Campaign oder Ihres Canvas großgeschrieben werden, auch wenn Braze nicht verlangt, dass eingehende Trigger or triggern-Wörter großgeschrieben sind. Wenn Ihr Trigger or triggern-Wort beispielsweise „JOIN2023“ lautet, wird eine eingehende Nachricht mit „jOin2023“ dennoch den Canvas oder die Campaign Trigger or triggern or triggern.

Wenn kein Trigger or triggern-Wort angegeben ist, wird die Campaign oder der Canvas für *alle* eingehenden LINE-Nachrichten ausgeführt. Dies schließt Nachrichten ein, die mit Phrasen in aktiven Campaigns und Canvase übereinstimmen – in diesem Fall erhält die/der Nutzer:in zwei LINE-Nachrichten.

## Nicht erkannte Antworten {#unrecognized-responses}

Sie sollten eine Trigger or triggern-Option für nicht erkannte Antworten in interaktiven Canvase einbinden. Dies informiert Nutzer:innen über die verfügbaren Eingabeaufforderungen (oder Trigger or triggern-Wörter) und setzt ihre Erwartungen für den Kanal.

### Einen Trigger or triggern für nicht erkannte Antworten erstellen {#creating-a-trigger-for-unrecognized-responses}

Nachdem Sie Aktionsgruppen für die angepassten Filterphrasen erstellt haben, fügen Sie dem Aktionspfad eine weitere Aktionsgruppe für **LINE-Nachricht senden** hinzu und aktivieren Sie **nicht** die Option **Nachrichtentext enthält**. Dies fängt alle nicht erkannten Antworten von Nutzer:innen ab, ähnlich wie eine „else“-Klausel.

Für diese Nachricht sollten Sie eine LINE-Nachricht senden, die die/den Nutzer:in darüber informiert, dass dieser Kanal nicht von einer Person überwacht wird, und sie/ihn bei Bedarf an einen Support-Kanal weiterleiten.