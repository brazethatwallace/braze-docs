---
nav_title: RudderStack
article_title: RudderStack
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und RudderStack, einer Open-Source-Infrastruktur für Kundendaten, die eine nahtlose Integration von Braze für Ihre Android-, iOS- und Internet-Anwendungen bietet. Mit RudderStack können Sie Ihre In-App-Kundenereignisdaten direkt an Braze senden, um sie kontextuell zu analysieren."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) ist eine quelloffene Infrastruktur für Kundendaten zum Sammeln und Weiterleiten von Kundenereignisdaten an Ihr bevorzugtes Data Warehouse und Dutzende anderer Analytics-Anbieter, wie z. B. Braze. Es ist unternehmenstauglich und bietet ein robustes Transformations-Framework, mit dem Sie Ihre Ereignisdaten im Handumdrehen verarbeiten können.

Die Integration von Braze und RudderStack bietet eine native SDK-Integration für Ihre Android-, iOS- und Internet-Anwendungen sowie eine Server-zu-Server-Integration von Ihren Backend-Diensten.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| RudderStack-Konto | Sie benötigen ein [RudderStack-Konto](https://app.rudderstack.com/), um die Vorteile dieser Partnerschaft zu nutzen. |
| Konfigurierte Quelle | Eine [Quelle](https://www.rudderstack.com/docs/dashboard-guides/sources/) ist im Wesentlichen die Herkunft aller Daten, die an RudderStack gesendet werden, wie Websites, mobile Apps oder Backend-Server. Bevor Sie Braze als Ziel in RudderStack einrichten, müssen Sie die Quelle konfigurieren. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track`, `users.identify`, `users.delete` und `users.alias.new`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-App-Schlüssel | Um Ihren App-Schlüssel im Braze-Dashboard zu erhalten, gehen Sie zu **Einstellungen** > **App Settings** > **Identification** und suchen Sie den Namen Ihrer App. Speichern Sie den zugehörigen Bezeichner-String.
| Datenzentrum | Ihr Datenzentrum stimmt mit Ihrer Braze-Dashboard-[Instanz]({{site.baseurl}}/api/basics#endpoints) überein.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Eine Quelle hinzufügen {#step-1-add-a-source}

Um mit dem Senden von Daten an Braze zu beginnen, müssen Sie zunächst sicherstellen, dass eine Quelle in Ihrer RudderStack-App eingerichtet ist. Besuchen Sie [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started), um zu erfahren, wie Sie Ihre Datenquelle einrichten.

### 2. Schritt: Ziel konfigurieren {#step-2-configure-destination}

Da Ihre Datenquelle nun eingerichtet ist, wählen Sie im RudderStack-Dashboard unter **Destinations** die Option **ADD DESTINATION** aus. Wählen Sie aus der Liste der verfügbaren Ziele **Braze** aus und klicken Sie auf **Next**.

Geben Sie im Braze-Ziel den App-Schlüssel, den Braze REST-API-Schlüssel, den Daten-Cluster und die native SDK-Option (nur im Gerätemodus) an. Die Option „Natives SDK“ verwendet das native Braze SDK zum Senden von Ereignissen, wenn sie aktiviert ist.

### 3. Schritt: Wählen Sie die Art der Integration {#step-3-choose-the-type-of-integration}

Sie können die web- und nativen clientseitigen Bibliotheken von RudderStack auf eine der folgenden Arten in Braze integrieren:

- [Side-by-side / Gerätemodus](#device-mode)**:** RudderStack sendet die Ereignisdaten direkt von Ihrem Client (Browser oder mobile Anwendung) an Braze.
- [Server-zu-Server / Cloud-Modus](#cloud-mode)**:** Das Braze SDK sendet die Ereignisdaten direkt an RudderStack, die dann transformiert und an Braze weitergeleitet werden.
- [Hybrid-Modus](#hybrid-mode)**:** Verwenden Sie den Hybrid-Modus, um automatisch und von Nutzer:innen generierte iOS- und Android-Ereignisse über eine einzige Verbindung an Braze zu senden.

{% alert note %}
Erfahren Sie mehr über die [Verbindungsmodi](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) von RudderStack und die Vorteile der einzelnen Modi.
{% endalert %}

#### Side-by-side-Integration (Gerätemodus) {#device-mode}

In diesem Modus können Sie Ihre Ereignisse mit dem Braze SDK, das Sie auf Ihrer Website oder in Ihrer mobilen App eingerichtet haben, an Braze senden.

Richten Sie die Abbildungen zum RudderStack SDK für Ihre Plattform im Braze GitHub Repository ein, wie unter [Unterstützte Methoden](#supported-methods) beschrieben:

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Um die Integration im Gerätemodus abzuschließen, lesen Sie die ausführliche RudderStack-Anleitung zum [Hinzufügen von Braze zu Ihrem Projekt](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Server-zu-Server-Integration (Cloud-Modus) {#cloud-mode}

In diesem Modus sendet das SDK die Ereignisdaten direkt an den RudderStack-Server. RudderStack transformiert dann diese Daten und leitet sie an das gewünschte Ziel weiter. Diese Transformation wird im RudderStack-Backend mithilfe des Transformer-Moduls von RudderStack durchgeführt.

Um die Integration zu aktivieren, müssen Sie die RudderStack-Methoden auf Braze abbilden, wie unter [Unterstützte Methoden](#supported-methods) beschrieben.

{% alert note %}
Die serverseitigen SDKs von RudderStack (Java, Python, Node.js, Go, Ruby) unterstützen nur den Cloud-Modus. Das liegt daran, dass ihre serverseitigen SDKs im RudderStack-Backend arbeiten und kein Braze-spezifisches SDK laden können.
{% endalert %}

{% alert important %}
Die Server-zu-Server-Integration unterstützt keine Braze-UI-Features wie Push-Benachrichtigungen oder In-App-Messaging. Diese Features werden jedoch von der Integration im Gerätemodus unterstützt.
{% endalert %}

#### Hybrid-Modus {#hybrid-mode}

Verwenden Sie den Hybrid-Modus, um alle Ereignisse von Ihren iOS- und Android-Quellen an Braze zu senden.

Wenn Sie den Hybrid-Modus wählen, um Ereignisse an Braze zu senden, wird RudderStack:
1. Das Braze SDK initialisieren.
2. Alle von Nutzer:innen erzeugten Ereignisse (identify, track, page, screen und group) nur über den Cloud-Modus an Braze senden und verhindern, dass sie über den Gerätemodus gesendet werden.
3. Die automatisch generierten Ereignisse (In-App-Nachrichten, Push-Benachrichtigungen, die das Braze SDK erfordern) über den Gerätemodus senden.

Um [Ereignisse über den Hybrid-Modus zu senden](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), verwenden Sie die Option Hybrid-Modus, während Sie Ihre Quelle mit dem Braze-Ziel verbinden. Fügen Sie dann die Braze-Integration zu Ihrem Projekt hinzu.

## 4. Schritt: Zusätzliche Einstellungen konfigurieren {#step-4-configure-additional-settings}

Nach Abschluss der Ersteinrichtung konfigurieren Sie die folgenden Einstellungen, um Ihre Daten in Braze korrekt zu empfangen:

- **Enable subscription groups in group call**: Aktivieren Sie diese Einstellung, um den Abo-Gruppenstatus in Ihren Gruppenereignissen zu senden. Weitere Informationen finden Sie unter [Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Use Custom Attributes Operation**: Aktivieren Sie diese Einstellung, wenn Sie die Funktionalität der [verschachtelten angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) in Braze nutzen möchten, um Segmente zu erstellen und Ihre Nachrichten mithilfe eines angepassten Attributobjekts zu personalisieren. Weitere Informationen finden Sie unter [Send user traits as nested custom attributes](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Track events for anonymous users**: Aktivieren Sie diese Einstellung, um anonyme Nutzer:innen-Aktivitäten zu tracken und diese Informationen an Braze zu senden.

### Einstellungen des Gerätemodus {#device-mode-settings}

Die folgenden Einstellungen gelten nur, wenn Sie Ereignisse über den [Gerätemodus](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode) an Braze senden:

- **Client-side Events Filtering**: Mit dieser Einstellung können Sie festlegen, welche Ereignisse für Braze gesperrt oder zugelassen werden sollen. Weitere Informationen zu dieser Einstellung finden Sie unter [Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Deduplicate Traits**: Aktivieren Sie diese Einstellung, um die Nutzer:innen-Traits im [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify)-Aufruf zu deduplizieren.
- **Show Braze logs**: Diese Einstellung gilt nur, wenn Sie das [JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) als Quelle verwenden. Aktivieren Sie sie, um die Braze-Protokolle für Ihre Nutzer:innen anzuzeigen.
- **OneTrust Cookie Categories**: Mit dieser Einstellung können Sie die [OneTrust-Cookie-Zustimmungsgruppen](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) mit Braze verknüpfen.

## Unterstützte Methoden {#supported-methods}

Braze unterstützt die RudderStack-Methoden identify, track, screen, page, group und alias.

{% tabs %}
{% tab Identify %}

Die RudderStack-[`identify`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#identify) verknüpft Nutzer:innen mit ihren Aktionen. RudderStack erfasst eine eindeutige Nutzer-ID und optionale Traits wie Name, E-Mail, IP-Adresse usw.

**Delta-Verwaltung für identify-Aufrufe**<br>
Wenn Sie Ereignisse über den Gerätemodus an Braze senden, können Sie Kosten sparen, indem Sie Ihre `identify`-Aufrufe deduplizieren. Aktivieren Sie dazu die Dashboard-Einstellung **Deduplicate Traits**. RudderStack sendet dann nur die geänderten oder modifizierten Attribute (Traits) an Braze.

**Nutzer:in löschen**<br>
Sie können eine:n Nutzer:in in Braze mit der [Verordnung „Suppression with Delete“](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) der RudderStack [Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/) löschen.

{% endtab %}
{% tab Track %}

Die [`track`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#track) von RudderStack erfasst alle Nutzer:innen-Aktivitäten und die mit diesen Aktivitäten verbundenen Eigenschaften.

**Bestellung abgeschlossen**<br>
Wenn Sie die [RudderStack E-Commerce API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) verwenden, um die track-Methode für ein Ereignis mit dem Namen `Order Completed` aufzurufen, sendet RudderStack die in diesem Ereignis aufgeführten Produkte an Braze als [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

{% endtab %}
{% tab Screen %}

Mit der [`screen`-Methode](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) von RudderStack können Sie die mobilen Bildschirmansichten Ihrer Nutzer:innen mit allen zusätzlichen Informationen über den betrachteten Bildschirm aufzeichnen.

{% endtab %}
{% tab Page %}

Mit der [`page`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#page) von RudderStack können Sie die Seitenaufrufe Ihrer Website aufzeichnen. Außerdem werden alle anderen relevanten Informationen über diese Seite erfasst.

{% endtab %}
{% tab Group %}

Mit der [`group`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#group) von RudderStack können Sie eine:n Nutzer:in mit einer Gruppe verknüpfen.

**Abo-Gruppenstatus**<br>
Um den Abo-Gruppenstatus zu aktualisieren, aktivieren Sie im RudderStack-Dashboard die Einstellung „Enable subscription groups in group call“ und senden Sie den Abo-Gruppenstatus im Gruppenaufruf.

{% endtab %}
{% tab Alias %}

Die [`alias`-Methode](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) von RudderStack erlaubt es Ihnen, verschiedene Identitäten einer/eines bekannten Nutzer:in zusammenzuführen. Beachten Sie, dass RudderStack den alias-Aufruf für Braze nur im Cloud-Modus unterstützt.

{% endtab %}
{% endtabs %}

## Nutzer:innen-Traits als verschachtelte angepasste Attribute senden {#send-user-traits-as-nested-custom-attributes}

Sie können die Nutzer:innen-Traits als verschachtelte angepasste Attribute an Braze senden und Hinzufüge-, Aktualisierungs- und Entfernungsoperationen darauf ausführen. Aktivieren Sie dazu die Einstellung „Use Custom Attributes Operation“ im Dashboard in RudderStack, während Sie das Braze-Ziel konfigurieren. Dieses Feature ist nur im Cloud-Modus verfügbar.

Sie können die Nutzer:innen-Traits als verschachtelte angepasste Attribute in Ihren `identify`-Ereignissen im folgenden Format senden:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Alex"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Um die Nutzer:innen-Traits als angepasste Nutzerattribute über die Aufrufe `track`, `page` oder `screen` zu senden, übergeben Sie `traits` als kontextuelles Feld im Ereignis:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Alex"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Für die Operationen „Aktualisieren“ und „Entfernen“ ist `identifier` ein erforderlicher Schlüssel. Wenn im verschachtelten Array keine Operationen zum Hinzufügen, Aktualisieren oder Entfernen vorhanden sind, verwendet RudderStack standardmäßig die Operation „Erstellen“, um die Eigenschaften zu erstellen. Weitere Informationen zum Senden von verschachtelten angepassten Attributen finden Sie unter [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
{% endalert %}