---
nav_title: Zustellungs- und Eingangstypen
article_title: Zustellungs- und Eingangstypen
page_order: 5
page_type: reference
description: "Dieser Referenzartikel beschreibt die Zustellungstypen für Kampagnen, Eingangstypen für Canvase und die zeitbasierten Features beim Einrichten einer Kampagne oder eines Canvas."
tool:
    - Campaigns
    - Canvas
---

# Zustellungs- und Eingangstypen {#delivery-and-entry-types}

> In Braze gibt es drei verschiedene Möglichkeiten, Ihre Nachricht zu planen: geplant, aktionsbasiert und API-getriggert. Die Wahl, wie und wann Ihre Nachricht zugestellt wird, ist entscheidend für die Entwicklung einer effektiven Nachricht.

Bei Kampagnen bestimmt der Zustellungstyp, wann Ihre Nutzer:innen in Ihre Kampagne eintreten und wann sie gesendet wird. Da ein Canvas als fortlaufende User Journey aufgebaut ist, wird das Messaging-Konzept eines Zeitplans als Eingangstyp bezeichnet.

| Zustellungs-<nobr> und Eingangstypen | Beschreibung |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Geplant** | Dieser Zeitplantyp ist für einmalige Nachrichten konzipiert, die Sie sofort senden möchten, z. B. Kampagnen zu einem aktuellen Ereignis. <br><br>Wenn Sie Testnachrichten senden, die nur an Sie selbst oder Ihr Team gerichtet sind, können Sie diese mit dieser Option sofort zustellen. |
| **Aktionsbasiert** | Aktionsbasierte Zustellungsnachrichten oder ereignisgetriggerte Kampagnen und Canvase sind sehr effektiv für transaktionale oder leistungsbasierte Nachrichten. Sie können sie so Trigger or triggern or triggern, dass sie gesendet werden, nachdem ein:e Nutzer:in eine bestimmte Aktion abgeschlossen hat, anstatt Ihre Nachricht an bestimmten Tagen zu senden. |
| **API-getriggert** | API-getriggerte Nachrichten ermöglichen es Ihnen, Nachrichteninhalte, multivariate Tests und Regeln zur erneuten Berechtigung im Braze-Dashboard zu verwalten und gleichzeitig die Zustellung dieser Inhalte über Ihre eigenen Server und Systeme zu Trigger or triggern or triggern. <br><br>Die API-Anfrage zum Trigger or triggern or triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Realtime in die Nachricht eingebunden werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zustellungs- und Eingangstypen" }

## Zeitbasierte Optionen {#time-based-options}

{% tabs %}
{% tab Campaign %}
Bei der geplanten Zustellung können Sie aus den folgenden Optionen wählen:

- Sofort nach dem Start der Kampagne senden
- Zu einem festgelegten Zeitpunkt senden
- [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
{% endtab %}

{% tab Canvas %}
Bei der geplanten Zustellung treten Nutzer:innen nach einem Zeitplan ein, ähnlich wie Sie eine Kampagne planen würden. Sie können Nutzer:innen in einen Canvas aufnehmen, sobald er gestartet wird, oder zu einem festgelegten Zeitpunkt.

### Festgelegte Zeitpunkte {#designated-times}

Sie können wählen, Ihren Canvas mit einer bestimmten Eingangshäufigkeit zu senden, einschließlich einmalig, täglich, wöchentlich oder monatlich. Für Canvase mit einer wiederkehrenden geplanten Zustellung können Sie die Wiederholung so einstellen, dass Nutzer:innen den Canvas bis zu 30 festgelegte Male betreten können.
{% endtab %}
{% endtabs %}

## Aktionsbasierte Optionen {#action-based-options}

{% tabs %}
{% tab Campaign %}
Die aktionsbasierte Zustellung sendet Kampagnen an Nutzer:innen, die eine bestimmte Aktion ausführen. Nachdem diese Aktion stattgefunden hat, können Sie entscheiden, wann die Kampagne gesendet wird: sofort, nach einer bestimmten Zeit, zu einem bestimmten Zeitpunkt oder zu einem Zeitpunkt in der Zukunft.
{% endtab %}

{% tab Canvas %}
Die aktionsbasierten Optionen bestimmen, welche Aktionen (oder Trigger or triggern) ein:e Nutzer:in ausführen muss, um in einen Canvas einzutreten, und zu welchem genauen Zeitpunkt der Eintritt möglich ist. Sie könnten Ihre Nutzer:innen beispielsweise anhand der folgenden Aktionen bewerten:

- Öffnen Ihrer App
- Hinzufügen einer E-Mail-Adresse
- Betreten eines Standorts

### Eingangsfenster {#entry-window}

Das Eingangsfenster Ihres Canvas bestimmt, welche Nutzer:innen den Canvas zur festgelegten Startzeit (und optionalen Endzeit) betreten können. Ähnlich wie bei aktionsbasierten Kampagnen können Sie wählen, Nutzer:innen in ihrer Ortszeit eintreten zu lassen.
{% endtab %}
{% endtabs %}

## API-Trigger or triggern-Optionen {#api-trigger-options}

{% tabs %}
{% tab Campaign %}
Wenn Sie API-getriggert als Zustellungsoption auswählen, erhalten Sie eine Campaign-ID, um zu identifizieren, welche Kampagne mit dem [`/campaigns/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#prerequisites) gesendet werden soll.
{% endtab %}

{% tab Canvas %}
Wenn Sie API-getriggert als Eingangstyp auswählen, erhalten Sie eine Canvas-ID, um zu identifizieren, welcher Canvas mit dem [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) gesendet werden soll.
{% endtab %}
{% endtabs %}