---
nav_title: Nutzer:innen benachrichtigen
article_title: Nutzer:innen benachrichtigen
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie mit Nutzer:innen über Template-basierte Campaigns und Canvases kommunizieren können."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# LINE-Nutzer:innen benachrichtigen {#message-line-users}

> LINE ist ein Kanal für wechselseitige Kommunikation. Sie können über das reine Senden von Nachrichten hinausgehen und mithilfe von Template-basierten Campaigns und Canvases Gespräche mit Nutzer:innen führen. Dieser Artikel beschreibt die Details der Kommunikation mit Nutzer:innen, z. B. wie Sie Trigger-Wörter für eingehende Nachrichten und nicht erkannte Antworten einrichten.

Es gibt verschiedene Methoden, um über LINE mit Nutzer:innen zu kommunizieren, beispielsweise mithilfe von LINE-Trigger-Wörtern. Sie können auch Calls-to-Action (CTAs) verwenden, um das Engagement der Nutzer:innen mit Ihrem LINE-Messaging zu fördern.

## Aktionsbasierte Trigger {#action-based-triggers}

Sie können Campaigns und Canvases erstellen, die starten, verzweigen und Änderungen während der Journey vornehmen, wenn Sie eine eingehende LINE-Nachricht (eine von einer/einem Nutzer:in gesendete Nachricht) erhalten, die ein Trigger-Wort enthält. Stellen Sie sicher, dass Sie Trigger-Wörter wählen, die dem entsprechen, was Nutzer:innen voraussichtlich senden werden.

### Campaign

Legen Sie Ihre Trigger-Wörter fest, wenn Sie eine Campaign mit aktionsbasierter Zustellung planen.

![Aktionsbasierter Trigger mit „Diese Campaign an Nutzer:innen senden, die eine eingehende LINE-Nachricht an die Abo-Gruppe gesendet haben, bei der der Nachrichtentext“ und einem leeren Feld.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Legen Sie Ihre Trigger-Wörter innerhalb von [Aktionspfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) in Ihrem Canvas fest.

![Aktionspfad mit einem Trigger „Diese Campaign an Nutzer:innen senden, die eine eingehende LINE-Nachricht an die Abo-Gruppe gesendet haben, bei der der Nachrichtentext“ und einem leeren Feld.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Anforderungen {#requirements}

Jeder Buchstabe Ihres Trigger-Worts muss beim Erstellen Ihrer Campaign oder Ihres Canvas großgeschrieben werden, auch wenn Braze nicht verlangt, dass eingehende Trigger-Wörter großgeschrieben sind. Wenn Ihr Trigger-Wort beispielsweise „JOIN2023“ lautet, wird eine eingehende Nachricht mit „jOin2023“ dennoch den Canvas oder die Campaign triggern.

Wenn kein Trigger-Wort angegeben ist, wird die Campaign oder der Canvas für *alle* eingehenden LINE-Nachrichten ausgeführt. Dies schließt Nachrichten ein, die mit Phrasen in aktiven Campaigns und Canvases übereinstimmen – in diesem Fall erhält die/der Nutzer:in zwei LINE-Nachrichten.

## Nicht erkannte Antworten {#unrecognized-responses}

Sie sollten eine Trigger-Option für nicht erkannte Antworten in interaktiven Canvases einbinden. Dies informiert Nutzer:innen über die verfügbaren Eingabeaufforderungen (oder Trigger-Wörter) und setzt ihre Erwartungen für den Kanal.

### Einen Trigger für nicht erkannte Antworten erstellen {#creating-a-trigger-for-unrecognized-responses}

Nachdem Sie Aktionsgruppen für die angepassten Filterphrasen erstellt haben, fügen Sie dem Aktionspfad eine weitere Aktionsgruppe für **Send LINE message** hinzu und aktivieren Sie **nicht** die Option **Where the message body**. Dies fängt alle nicht erkannten Antworten von Nutzer:innen ab, ähnlich wie eine „else“-Klausel.

Für diese Nachricht sollten Sie eine LINE-Nachricht senden, die die/den Nutzer:in darüber informiert, dass dieser Kanal nicht von einer Person überwacht wird, und sie/ihn bei Bedarf an einen Support-Kanal weiterleiten.