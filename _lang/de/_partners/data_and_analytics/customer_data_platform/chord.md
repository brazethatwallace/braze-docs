---
nav_title: Chord
article_title: Chord
description: "Verbinden Sie die Chord geschäftskunden Data Platform (CDP) mit Braze, um E-Commerce-Ereignisse und Identitätsaktualisierungen für Messaging, Segmentierung und Journeys weiterzuleiten."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> [Chord](https://www.chord.co/) bietet eine geschäftskunden Data Platform, die Ereignisse aus Ihrem E-Commerce-Shop erfasst und standardisiert. Wenn Sie Chord mit Braze verbinden, fließen Kaufaktivitäten, Verhaltensereignisse und Identitätsaktualisierungen in Braze, sodass Sie Campaigns triggern und Profile aktuell halten können, ohne diese Pipelines selbst aufbauen zu müssen.

_Diese Integration wird von Chord gepflegt._

Weitere Informationen zu Einrichtung, Verbindungsoptionen und Feldlisten finden Sie unter [Chord-Braze-Integration](https://docs.chord.co/braze#chord-x-braze-integration).

## Über die Integration {#about-the-integration}

Chord fungiert als Datenschicht zwischen Ihrem Shop und Braze. Nachdem Sie Braze als Ziel in der Chord CDP verbunden haben, bildet Chord Ereignisse aus seinem Tracking-Plan auf Braze ab. Nutzen Sie diese Daten in Segments, Canvases und der Nachrichtenpersonalisierung, um widerzuspiegeln, was Ihre Verbraucher:innen auf Ihrer Website tun.

## Voraussetzungen {#prerequisites}

Bevor Sie Chord und Braze verbinden, stellen Sie sicher, dass Folgendes vorhanden ist:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Chord-Konto | Ein Chord-Konto ist erforderlich, um diese Integration zu nutzen. |
| Braze-API-Zugangsdaten | Die benötigten Zugangsdaten hängen von Ihrem [Verbindungsmodus](#connection-modes) ab. Der Cloud-Modus verwendet einen Braze-REST-API-Schlüssel. Der Gerätemodus verwendet den Web-Kanal-API-Schlüssel für das Braze SDK, der sich von Ihrem REST-API-Schlüssel unterscheidet. |
| Braze-REST-Endpunkt | Chord sendet serverseitige Daten an die Endpunkte [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) und [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). Ihre Basis-URL richtet sich nach Ihrer Braze-Instanz, zum Beispiel `https://rest.iad-01.braze.com`. Weitere Informationen finden Sie unter [Braze-REST-API-Endpunkte]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Verbindungsmodi {#connection-modes}

Chord unterstützt den Cloud-Modus (Server-zu-Server-Aufrufe über die Braze-REST-APIs) und den Gerätemodus (Chord initialisiert das Braze Web SDK und leitet zugeordnete Aufrufe weiter). Wählen Sie den Modus, der am besten dazu passt, ob Sie die vollständigen Web-SDK-Features benötigen (zum Beispiel In-App-Nachrichten) oder nur serverseitige Ereignisweiterleitung.

### Cloud-Modus {#cloud-mode}

1. Öffnen Sie in der Chord-Datenplattform die CDP und navigieren Sie zu **Destinations**.
2. Wählen Sie **Add** neben den Zielen, wählen Sie **Braze** aus dem Katalog und geben Sie einen Zielnamen sowie Ihren Braze-REST-API-Schlüssel ein.
3. Erstellen Sie das Ziel, um die Verbindung abzuschließen.

Erstellen Sie den REST-API-Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Wenn Sie die ältere Navigation verwenden, gehen Sie zu **Entwicklungskonsole** > **API-Einstellungen**. Sofern Chord keine anderen Anforderungen für Ihren Workspace dokumentiert, benötigt der Schlüssel die Berechtigungen `users.track` und `users.identify`. Weitere Informationen finden Sie unter [API-Schlüssel]({{site.baseurl}}/api/api_key/).

### Gerätemodus {#device-mode}

1. Öffnen Sie in der Chord-Datenplattform die CDP und navigieren Sie zu **Destinations**.
2. Wählen Sie **Add** neben den Zielen, wählen Sie **Braze (device mode)** aus dem Katalog und geben Sie einen Zielnamen sowie Ihren Web-Kanal-API-Schlüssel ein.
3. Erstellen Sie das Ziel, um die Verbindung abzuschließen.

Verwenden Sie den Web-Kanal-API-Schlüssel unter **Einstellungen** > **App-Einstellungen** > **Web** > **API Key** im Braze-Dashboard. Verwenden Sie Ihren REST-API-Schlüssel nicht für den Gerätemodus.

### Konfiguration des Gerätemodus {#device-mode-configuration}

Konfigurieren Sie in den Chord-Zieleinstellungen Folgendes:

- **Braze Web SDK-Version:** Chord bietet auswählbare SDK-Versionen in der CDP an; bestätigen Sie den verfügbaren Bereich in der Chord-Dokumentation.
- **SDK-Endpunkt:** Muss mit Ihrer Braze-Instanz übereinstimmen. Weitere Informationen finden Sie unter [API- und SDK-Endpunkte]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/).
- **Ereignis- und SDK-Optionen:** Zum Beispiel, welche Track- oder Identify-Verhaltensweisen gesendet werden sollen, Seitenereignis-Handling, In-App-Nachrichtenverhalten, SDK-Initialisierungszeitpunkt und Einwilligungseinstellungen.

## Ereigniszuordnung (Gerätemodus) {#event-mapping-device-mode}

Wenn Sie den Gerätemodus verwenden, ordnet Chord Ereignisse wie in dieser Tabelle dargestellt Braze zu:

| Chord | Braze |
| ----- | ----- |
| Order completed | `logPurchase` |
| Andere `track`-Ereignisse | `logCustomEvent` |
| Identify | Nutzeraktualisierungen (zum Beispiel Attribute über das SDK-Nutzerobjekt) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nur Ereignisse, die in Ihrem Chord-Tracking-Plan enthalten und für das Braze-Ziel konfiguriert sind, werden weitergeleitet.

## Nutzung der Integration {#using-the-integration}

### 1. Schritt: Ereignisse in Braze bestätigen {#step-1-confirm-events-in-braze}

Nachdem Daten fließen, öffnen Sie Nutzerprofile oder Ihre Ereignis-Tools in Braze, um zu bestätigen, dass Ereignisse und Attribute wie erwartet ankommen.

### 2. Schritt: Zielgruppen und Journeys erstellen {#step-2-build-audiences-and-journeys}

Verwenden Sie synchronisierte Ereignisse und Attribute in [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) und Campaigns, um Verbraucher:innen basierend auf dem Shop-Verhalten anzusprechen.

## Anwendungsfälle {#use-cases}

- **Post-Purchase-Messaging:** Lösen Sie Bestätigungen, Cross-Sell- oder Bewertungsanfragen aus, wenn Chord abgeschlossene Bestellungen empfängt.
- **Profilanreicherung:** Halten Sie Braze-Attribute mit den neuesten Verbraucherprofildaten aus Chord synchron, um eine sauberere Segmentierung zu ermöglichen.
- **Verhaltensbasiertes Retargeting:** Sprechen Sie Verbraucher:innen erneut an, die in letzter Zeit nicht gekauft oder konvertiert haben, indem Sie Chord-Verhaltensereignisse nutzen.

## Hinweise {#considerations}

{% alert important %}
Wenn ein anderes Tool bereits dieselben Ereignisse an Braze sendet, stimmen Sie sich mit den Verantwortlichen dieser Integration ab, bevor Sie Braze über die Chord CDP verbinden. Parallele Ziele können nachgelagert doppelte Ereignisse erzeugen.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Wenn Ereignisse nicht in Braze erscheinen:

1. Bestätigen Sie in der Chord CDP, dass Live-Ereignisse von Ihren Quellen eintreffen.
2. Überprüfen Sie, ob das Braze-Ziel den korrekten API-Schlüssel, die richtige SDK-Version (Gerätemodus) und den richtigen REST- oder SDK-Endpunkt für Ihre Instanz verwendet.
3. Bestätigen Sie, dass das Ziel in Chord mit der erwarteten Quelle verbunden ist.
4. Überprüfen Sie in Chord die API-Ziel- oder Funktionsprotokolle auf erfolgreiche Aufrufe an `/users/track` und `/users/identify` und prüfen Sie dann erneut in Braze.

Für Chord-spezifische Protokollstandorte und UI-Schritte siehe [Chord-Braze-Integration](https://docs.chord.co/braze#chord-x-braze-integration).