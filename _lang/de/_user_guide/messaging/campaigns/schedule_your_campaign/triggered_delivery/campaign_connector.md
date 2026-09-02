---
nav_title: Campaign Connector
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Dieser Artikel erklärt, was Campaign Connector ist und wie Sie damit zielgerichtete, relevante Inhalte zum richtigen Zeitpunkt bereitstellen können."

---
# Campaign Connector

> Mit Campaign Connector können Sie Kampagnen erstellen, die getriggert werden, wenn Nutzer:innen mit aktiven Kampagnen interagieren. So können Sie zielgerichtete, relevante Inhalte zum richtigen Zeitpunkt bereitstellen.

## So funktioniert es {#how-it-works}

Mit diesem Feature können Sie Nutzer:innen ansprechen, die folgende Interaktionen mit aktiven Kampagnen durchführen:

- In-App-Nachricht ansehen
- In-App-Nachricht anklicken
- Buttons in In-App-Nachrichten anklicken
- E-Mail anklicken
- Alias in E-Mail anklicken
- E-Mail öffnen
- Push-Benachrichtigung direkt öffnen
- Button einer Push-Benachrichtigung anklicken
- Push-Story-Seite anklicken
- Konversions-Event durchführen
- E-Mail erhalten
- SMS erhalten
- Gekürzten SMS-Link anklicken
- Push-Benachrichtigung erhalten
- Webhook erhalten
- In eine Kontrollgruppe aufgenommen werden
- Content-Card ansehen
- Content-Card anklicken
- Content-Card schließen

{% alert important %}
Campaign-Connector-Trigger können nicht verwendet werden, um In-App-Nachricht-Kampagnen zu triggern. In-App-Nachrichten können nur durch SDK-Events getriggert werden, wie z. B. angepasste Events oder Sitzungsstart. Weitere Informationen finden Sie unter [In-App-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).
{% endalert %}

### Zustellungsregeln {#delivery-rules}

Beachten Sie, dass Sie Campaign Connector nicht verwenden können, um einer Nutzerin oder einem Nutzer eine Nachricht zu senden, nachdem sie oder er eine Interaktion mit einer Kampagne abgeschlossen hat. Wenn Sie beispielsweise eine Marketing-Kampagne über neun Wochen durchführen und zu Beginn der vierten Woche eine Folgekampagne mit Campaign Connector einrichten, wird die Folgekampagne nur Nachrichten an Nutzer:innen zustellen, die nach der Veröffentlichung der Folgekampagne mit der Marketing-Kampagne interagiert haben (Wochen 4–9). Um sicherzustellen, dass Ihre Folgekampagnen alle Nutzer:innen erreichen, die Sie ansprechen möchten, sollten Sie daher:

- Ihre ursprüngliche Kampagne als Entwurf einrichten
- Ihre Folgekampagne einrichten und veröffentlichen
- Die ursprüngliche Kampagne veröffentlichen

Diese Zustellungsregeln sind besonders relevant, wenn Sie Nutzer:innen ansprechen, die in eine Kontrollgruppe aufgenommen werden, eine E-Mail erhalten oder eine Push-Benachrichtigung erhalten. Da Nutzer:innen in die Kontrollgruppe aufgenommen werden, sobald Sie die ursprüngliche Kampagne veröffentlichen, müssen Sie die Folgekampagne vor der ursprünglichen Kampagne veröffentlichen. Ebenso gilt: Wenn Sie die ursprüngliche Kampagne vor der Folgekampagne veröffentlichen, können viele Nutzer:innen Ihre E-Mail und/oder Push-Benachrichtigung erhalten, bevor die Folgekampagne veröffentlicht ist.

## Campaign Connector mit Ihren Kampagnen verwenden {#using-campaign-connector-with-your-campaigns}

### 1. Schritt: Neue Kampagne erstellen {#step-1-create-a-new-campaign}

Verfassen Sie die Nachrichten, die Sie an Ihre Nutzer:innen senden möchten. Je nach Anwendungsfall können Sie eine Einzelkanal- oder Multichannel-Kampagne auswählen.

### 2. Schritt: Interaktion und Zielkampagne auswählen {#step-2-select-interaction-and-target-campaign}

1. Wählen Sie [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) und fügen Sie den Trigger „Mit Kampagne interagieren“ hinzu, um Nutzer:innen anzusprechen, die mit einer aktiven Kampagne interagieren.
2. Wählen Sie die Trigger-Interaktion aus.
3. Wählen Sie anschließend die aktive Kampagne aus, die Sie als Ziel verwenden möchten.

![Auswahl der aktiven Kampagne, die als Ziel verwendet werden soll.]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### 3. Schritt: Delay planen und Ausnahmen hinzufügen (optional) {#step-3-set-schedule-delay-and-add-exceptions-optional}

Wenn Sie einen Delay planen, können Sie eine Ausnahme zur Trigger-Aktion hinzufügen. Beispielsweise möchten Sie vielleicht eine E-Mail-Kampagne erneut an Nutzer:innen senden, die die ursprüngliche E-Mail nicht geöffnet haben. In diesem Szenario können Sie „E-Mail erhalten“ als Trigger wählen und einen Delay von einer Woche festlegen. Dann können Sie „E-Mail öffnen“ als Ausnahme hinzufügen. Jetzt wird die E-Mail erneut an Nutzer:innen gesendet, die die ursprüngliche E-Mail innerhalb einer Woche nach Erhalt nicht geöffnet haben.

![Beispiel für einen geplanten Delay mit einer Ausnahme zur Trigger-Aktion, bei dem „E-Mail erhalten“ als Trigger und „E-Mail öffnen“ als Ausnahme festgelegt ist.]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Ausnahme-Events werden nur getriggert, während eine Nutzerin oder ein Nutzer auf den Erhalt der zugehörigen Nachricht wartet. Wenn die Aktion ausgeführt wird, bevor die Nachricht zugestellt werden soll, wird das Ausnahme-Event nicht getriggert.

### 4. Schritt: Kampagnenerstellung fortsetzen {#step-4-proceed-with-campaign-creation}

Fahren Sie mit der Erstellung Ihrer Kampagne wie gewohnt fort. Beachten Sie: Wenn Sie sicherstellen möchten, dass Sie eine Nachricht an alle Nutzer:innen senden, die mit einer bestimmten Kampagne interagieren werden, sollten Sie am besten ein Segment ansprechen, das alle Nutzer:innen Ihrer App enthält.

## Anwendungsfälle {#use-cases}

Sie können Campaign Connector verwenden, um Nutzer:innen anzusprechen, die mit aktiven Kampagnen interagieren oder nicht interagieren.

Beispielsweise könnten Sie Nutzer:innen ansprechen, die auf eine Push-Benachrichtigung mit einer Aktion für kostenlosen Versand geklickt haben, um ihnen eine weitere Push-Benachrichtigung mit 15 % Rabatt auf einen Kauf zu senden.

Campaign Connector kann auch Nutzer:innen ansprechen, die eine Push-Benachrichtigung erhalten, die sie an ihren Warenkorb-Abbruch erinnert. Beispielsweise möchten Sie die Benachrichtigung erneut an Nutzer:innen senden, die sie nicht direkt geöffnet haben. Allerdings möchten Sie wahrscheinlich Nutzer:innen ausschließen, die seit dem Versand der ursprünglichen Benachrichtigung einen Kauf getätigt haben, auch wenn sie die Benachrichtigung nicht direkt geöffnet haben. Sie können diesen Anwendungsfall umsetzen, indem Sie einen Trigger „Push-Benachrichtigung erhalten“ für die Kampagne „Warenkorb-Abbruch“ hinzufügen, einen Delay planen und „Kauf tätigen“ sowie „Push-Benachrichtigung direkt geöffnet“ als Ausnahmen hinzufügen.