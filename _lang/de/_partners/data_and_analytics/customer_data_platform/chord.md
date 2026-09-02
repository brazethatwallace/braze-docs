---
nav_title: Chord
article_title: Chord
description: "Verbinden Sie die Chord Customer Data Platform (Customer Data Platform (CDP)) mit Braze, um E-Commerce-Ereignisse und Identitätsaktualisierungen für Messaging, Segmentierung und Journeys weiterzuleiten."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> [Chord](https://www.chord.co/) bietet eine Customer Data Platform, die Ereignisse aus Ihrem E-Commerce-Shop erfasst und standardisiert. Wenn Sie Chord mit Braze verbinden, fließen Kaufaktivitäten, Verhaltensereignisse und Identitätsaktualisierungen in Braze, sodass Sie Campaigns Trigger or triggern or triggern und Profile aktuell halten können, ohne diese Pipelines selbst aufbauen zu müssen.

_Diese Integration wird von Chord gepflegt._

Weitere Informationen zu Einrichtung, Verbindungsoptionen und Feldlisten finden Sie unter [Chord-Braze-Integration](https://docs.chord.co/braze#chord-x-braze-integration).

## Über die Integration {#about-the-integration}

Chord fungiert als Datenschicht zwischen Ihrem Shop und Braze. Nachdem Sie Braze als Ziel im Chord Customer Data Platform (CDP) verbunden haben, bildet Chord Ereignisse aus seinem Tracking-Plan auf Braze ab. Verwenden Sie diese Daten in Segments, Canvase und der Personalisierung von Nachrichten, um widerzuspiegeln, was Ihre Verbraucher:innen auf Ihrer Website tun.

## Voraussetzungen {#prerequisites}

Bevor Sie Chord und Braze verbinden, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Chord-Konto | Ein Chord-Konto ist erforderlich, um diese Integration zu nutzen. |
| Braze-API-Zugangsdaten | Die benötigten Zugangsdaten hängen von Ihrem [Verbindungsmodus](#connection-modes) ab. Der Cloud-Modus verwendet einen Braze-Representational State Transfer-API-Schlüssel. Der Gerätemodus verwendet den Internet-Kanal-API-Schlüssel für das Braze SDK or Software-Development-Kit, der sich von Ihrem Representational State Transfer-API-Schlüssel unterscheidet. |
| Braze-Representational State Transfer-Endpunkt | Chord sendet serverseitige Daten an die Endpunkte [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) und [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Ihre Basis-URL richtet sich nach Ihrer Braze-Instanz, zum Beispiel `https://rest.iad-01.braze.com`. Weitere Informationen finden Sie unter [Braze-Representational State Transfer-API-Endpunkte]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Verbindungsmodi {#connection-modes}

Chord unterstützt den Cloud-Modus (Server-zu-Server-Aufrufe über die Braze Representational State Transfer APIs) und den Gerätemodus (Chord initialisiert das Braze Web SDK or Software-Development-Kit und leitet zugeordnete Aufrufe weiter). Wählen Sie den Modus, der am besten zu Ihren Anforderungen passt – je nachdem, ob Sie den vollen Funktionsumfang des Web SDK or Software-Development-Kit benötigen (zum Beispiel In-App Messages) oder nur serverseitige Ereignisweiterleitung.

### Cloud-Modus {#cloud-mode}

1. Öffnen Sie in der Chord-Datenplattform die Customer Data Platform (CDP) und navigieren Sie zu **Destinations**.
2. Wählen Sie **Add** neben „Destinations“, wählen Sie **Braze** aus dem Katalog und geben Sie dann einen Zielnamen und Ihren Braze Representational State Transfer-API-Schlüssel ein.
3. Erstellen Sie das Ziel, um die Verbindung abzuschließen.

Erstellen Sie den Representational State Transfer-API-Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Falls Sie die ältere Navigation verwenden, navigieren Sie zu **Entwicklungskonsole** > **API Settings**. Sofern Chord keine anderen Anforderungen für Ihren Workspace dokumentiert, benötigt der Schlüssel die Berechtigungen `users.track` und `users.identify`. Weitere Informationen finden Sie unter [API-Schlüssel]({{site.baseurl}}/api/basics).

### Gerätemodus {#device-mode}

1. Öffnen Sie in der Chord-Datenplattform die Customer Data Platform (CDP) und navigieren Sie zu **Destinations**.
2. Wählen Sie **Add** neben „Destinations“, wählen Sie **Braze (device mode)** aus dem Katalog und geben Sie dann einen Zielnamen und Ihren Web-Kanal-API-Schlüssel ein.
3. Erstellen Sie das Ziel, um die Verbindung abzuschließen.

Verwenden Sie den Web-Kanal-API-Schlüssel aus **Einstellungen** > **App-Einstellungen** > **Web** > **API Key** im Braze-Dashboard. Verwenden Sie für den Gerätemodus nicht Ihren Representational State Transfer-API-Schlüssel.

### Konfiguration des Gerätemodus {#device-mode-configuration}

Konfigurieren Sie in den Chord-Zieleinstellungen die folgenden Optionen:

- **Braze Web SDK or Software-Development-Kit-Version:** Chord stellt in der Customer Data Platform (CDP) auswählbare SDK or Software-Development-Kit-Versionen zur Verfügung. Überprüfen Sie den verfügbaren Versionsbereich in der Chord-Dokumentation.
- **SDK or Software-Development-Kit-Endpunkt:** Muss mit Ihrer Braze-Instanz übereinstimmen. Weitere Informationen finden Sie unter [API- und SDK or Software-Development-Kit-Endpunkte]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).
- **Ereignis- und SDK or Software-Development-Kit-Optionen:** Zum Beispiel, welche Track- oder Identify-Verhaltensweisen gesendet werden sollen, Seitenereignis-Handling, In-App-Nachricht-Verhalten, Zeitpunkt der SDK or Software-Development-Kit-Initialisierung und Einstellungen zur Einwilligung.

## Event-Abbildung (Gerätemodus) {#event-mapping-device-mode}

Wenn Sie den Gerätemodus verwenden, bildet Chord Ereignisse wie in dieser Tabelle dargestellt auf Braze ab:

| Chord | Braze |
| ----- | ----- |
| Order completed | `logPurchase` |
| Andere `track`-Ereignisse | `logCustomEvent` |
| Identify | Nutzer:innen-Aktualisierungen (z. B. Attribute über das SDK or Software-Development-Kit-Nutzerobjekt) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Es werden nur Ereignisse weitergeleitet, die in Ihrem Chord-Tracking-Plan enthalten und für das Braze-Ziel konfiguriert sind.

## Integration verwenden {#using-the-integration}

### Schritt 1: Ereignisse in Braze bestätigen {#step-1-confirm-events-in-braze}

Nachdem der Datenfluss begonnen hat, öffnen Sie Nutzerprofile oder Ihre Ereignis-Tools in Braze, um zu bestätigen, dass Ereignisse und Attribute wie erwartet ankommen.

### Schritt 2: Zielgruppen und Journeys erstellen {#step-2-build-audiences-and-journeys}

Verwenden Sie synchronisierte Ereignisse und Attribute in [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), [Canvase]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) und Campaigns, um Verbraucher:innen auf Basis ihres Shop-Verhaltens anzusprechen.

## Anwendungsfälle {#use-cases}

- **Nachrichten nach dem Kauf:** Lösen Sie Bestätigungen, Cross-Selling oder Bewertungsanfragen aus, wenn Chord abgeschlossene Bestellungen empfängt.
- **Profilanreicherung:** Halten Sie Braze-Attribute mit den neuesten Verbraucher:innenprofildaten aus Chord synchron, um eine sauberere Segmentierung zu ermöglichen.
- **Verhaltensbasiertes Retargeting:** Sprechen Sie Verbraucher:innen erneut an, die in letzter Zeit nicht gekauft oder konvertiert haben, indem Sie Verhaltens-Events von Chord nutzen.

## Überlegungen {#considerations}

{% alert important %}
Wenn ein anderes Tool bereits dieselben Events an Braze sendet, stimmen Sie sich mit den Verantwortlichen dieser Integration ab, bevor Sie Braze über die Chord Customer Data Platform (CDP) verbinden. Parallele Ziele können nachgelagert doppelte Events erzeugen.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Wenn Ereignisse nicht in Braze erscheinen:

1. Bestätigen Sie im Chord Customer Data Platform (CDP), dass Live-Ereignisse von Ihren Quellen eingehen.
2. Überprüfen Sie, ob das Braze-Ziel den richtigen API-Schlüssel, die richtige SDK or Software-Development-Kit-Version (Device-Modus) und den richtigen Representational State Transfer- oder SDK or Software-Development-Kit-Endpunkt für Ihre Instanz verwendet.
3. Bestätigen Sie, dass das Ziel in Chord mit der erwarteten Quelle verknüpft ist.
4. Überprüfen Sie in Chord die API-Ziel- oder Funktionsprotokolle auf erfolgreiche Aufrufe an `/users/track` und `/users/identify` und prüfen Sie dann erneut in Braze.

Für Chord-spezifische Protokollstandorte und UI-Schritte siehe [Chord-Braze-Integration](https://docs.chord.co/braze#chord-x-braze-integration).