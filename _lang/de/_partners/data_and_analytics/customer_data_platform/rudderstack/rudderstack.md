---
nav_title: RudderStack
article_title: RudderStack
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und RudderStack, einer Open-Source-Infrastruktur für Kundendaten, die eine nahtlose Integration von Braze für Ihre Android-, iOS- und Internet-Anwendungen bietet. Mit RudderStack können Sie Ihre In-App-Kundenereignisdaten direkt an Braze senden, um sie kontextuell zu analysieren."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) ist eine quelloffene Infrastruktur für Kundendaten zum Sammeln und Weiterleiten von Kundenereignisdaten an Ihr bevorzugtes Data Warehouse und Dutzende anderer Analytics-Anbieter, wie z. B. Braze. Es ist unternehmenstauglich und bietet ein robustes Transformations-Framework, mit dem Sie Ihre Ereignisdaten im Handumdrehen verarbeiten können.

Die Integration von Braze und RudderStack bietet eine native SDK or Software-Development-Kit-Integration für Ihre Android-, iOS- und Internet-Anwendungen sowie eine Server-zu-Server-Integration von Ihren Backend-Diensten.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| RudderStack-Konto | Sie benötigen ein [RudderStack-Konto](https://app.rudderstack.com/), um die Vorteile dieser Partnerschaft zu nutzen. |
| Konfigurierte Quelle | Eine [Quelle](https://www.rudderstack.com/docs/dashboard-guides/sources/) ist im Wesentlichen die Herkunft aller Daten, die an RudderStack gesendet werden, wie z. B. Websites, mobile Apps oder Backend-Server. Sie müssen die Quelle konfigurieren, bevor Sie Braze als Ziel in RudderStack einrichten. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit den Berechtigungen `users.track`, `users.identify`, `users.delete` und `users.alias.new`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-App-Schlüssel | Um Ihren App-Schlüssel im Braze-Dashboard zu finden, navigieren Sie zu **Einstellungen** > **App-Einstellungen** > **Identifikation** und suchen Sie Ihren App-Namen. Speichern Sie den zugehörigen Bezeichner-String. |
| Rechenzentrum | Ihr Rechenzentrum entspricht Ihrer Braze-Dashboard-[Instanz]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Eine Quelle hinzufügen {#step-1-add-a-source}

Um mit dem Senden von Daten an Braze zu beginnen, müssen Sie zunächst sicherstellen, dass eine Quelle in Ihrer RudderStack-App eingerichtet ist. Besuchen Sie [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started), um zu erfahren, wie Sie Ihre Datenquelle einrichten.

### 2. Schritt: Ziel konfigurieren {#step-2-configure-destination}

Da Ihre Datenquelle nun eingerichtet ist, wählen Sie im RudderStack-Dashboard unter **Destinations** die Option **ADD DESTINATION** aus. Wählen Sie aus der Liste der verfügbaren Ziele **Braze** aus und klicken Sie auf **Next**.

Geben Sie im Braze-Ziel den App-Schlüssel, den Braze Representational State Transfer-API-Schlüssel, den Daten-Cluster und die native SDK or Software-Development-Kit-Option (nur im Gerätemodus) an. Die Option „Natives SDK or Software-Development-Kit“ verwendet das native Braze SDK or Software-Development-Kit zum Senden von Ereignissen, wenn sie aktiviert ist.

### 3. Schritt: Wählen Sie die Art der Integration {#step-3-choose-the-type-of-integration}

Sie können die web- und nativen clientseitigen Bibliotheken von RudderStack auf eine der folgenden Arten in Braze integrieren:

- [Side-by-side / Gerätemodus](#device-mode)**:** RudderStack sendet die Ereignisdaten direkt von Ihrem Client (Browser oder mobile Anwendung) an Braze.
- [Server-zu-Server / Cloud-Modus](#cloud-mode)**:** Das Braze SDK or Software-Development-Kit sendet die Ereignisdaten direkt an RudderStack, die dann transformiert und an Braze weitergeleitet werden.
- [Hybrid-Modus](#hybrid-mode)**:** Verwenden Sie den Hybrid-Modus, um automatisch und von Nutzer:innen generierte iOS- und Android-Ereignisse über eine einzige Verbindung an Braze zu senden.

{% alert note %}
Erfahren Sie mehr über die [Verbindungsmodi](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) von RudderStack und die Vorteile der einzelnen Modi.
{% endalert %}

#### Side-by-side-Integration (Gerätemodus) {#device-mode}

In diesem Modus können Sie Ihre Ereignisse mit dem Braze SDK or Software-Development-Kit, das Sie auf Ihrer Website oder in Ihrer mobilen App eingerichtet haben, an Braze senden.

Richten Sie die Abbildungen zum RudderStack SDK or Software-Development-Kit für Ihre Plattform im Braze GitHub Repository ein, wie unter [Unterstützte Methoden](#supported-methods) beschrieben:

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Um die Integration im Gerätemodus abzuschließen, lesen Sie die ausführliche RudderStack-Anleitung zum [Hinzufügen von Braze zu Ihrem Projekt](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Server-zu-Server-Integration (Cloud-Modus) {#cloud-mode}

In diesem Modus sendet das SDK or Software-Development-Kit die Ereignisdaten direkt an den RudderStack-Server. RudderStack transformiert dann diese Daten und leitet sie an das gewünschte Ziel weiter. Diese Transformation wird im RudderStack-Backend mithilfe des Transformer-Moduls von RudderStack durchgeführt.

Um die Integration zu aktivieren, müssen Sie die RudderStack-Methoden auf Braze abbilden, wie unter [Unterstützte Methoden](#supported-methods) beschrieben.

{% alert note %}
Die serverseitigen SDKs von RudderStack (Java, Python, Node.js, Go, Ruby) unterstützen nur den Cloud-Modus. Das liegt daran, dass ihre serverseitigen SDKs im RudderStack-Backend arbeiten und kein Braze-spezifisches SDK or Software-Development-Kit laden können.
{% endalert %}

{% alert important %}
Die Server-zu-Server-Integration unterstützt keine Braze-UI-Features wie Push-Benachrichtigungen oder In-App-Messaging. Diese Features werden jedoch von der Integration im Gerätemodus unterstützt.
{% endalert %}

#### Hybrid-Modus {#hybrid-mode}

Verwenden Sie den Hybrid-Modus, um alle Ereignisse von Ihren iOS- und Android-Quellen an Braze zu senden.

Wenn Sie den Hybrid-Modus wählen, um Ereignisse an Braze zu senden, wird RudderStack:
1. Das Braze SDK or Software-Development-Kit initialisieren.
2. Alle von Nutzer:innen erzeugten Ereignisse (identify, track, page, screen und group) nur über den Cloud-Modus an Braze senden und verhindern, dass sie über den Gerätemodus gesendet werden.
3. Die automatisch generierten Ereignisse (In-App-Nachrichten, Push-Benachrichtigungen, die das Braze SDK or Software-Development-Kit erfordern) über den Gerätemodus senden.

Um [Ereignisse über den Hybrid-Modus zu senden](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), verwenden Sie die Option Hybrid-Modus, während Sie Ihre Quelle mit dem Braze-Ziel verbinden. Fügen Sie dann die Braze-Integration zu Ihrem Projekt hinzu.

## 4. Schritt: Zusätzliche Einstellungen konfigurieren {#step-4-configure-additional-settings}

Konfigurieren Sie nach Abschluss der Ersteinrichtung die folgenden Einstellungen, um Ihre Daten korrekt in Braze zu empfangen:

- **Enable subscription groups in group call**: Aktivieren Sie diese Einstellung, um den Abo-Gruppenstatus in Ihren Gruppenereignissen zu senden. Weitere Informationen finden Sie unter [Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Use angepasste Attribute Operation**: Aktivieren Sie diese Einstellung, wenn Sie die Funktionalität der [verschachtelten angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) in Braze nutzen möchten, um Segmente zu erstellen und Ihre Nachrichten mithilfe eines angepassten Attribut-Objekts zu personalisieren. Weitere Informationen finden Sie unter [Send user traits as nested angepasste Attribute](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Track events for anonymous users**: Aktivieren Sie diese Einstellung, um die Aktivitäten anonymer Nutzer:innen zu verfolgen und diese Informationen an Braze zu senden.

### Einstellungen für den Gerätemodus {#device-mode-settings}

Die folgenden Einstellungen gelten nur, wenn Sie Ereignisse über den [Gerätemodus](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode) an Braze senden:

- **Client-side Events Filtering**: Mit dieser Einstellung können Sie festlegen, welche Ereignisse blockiert oder an Braze durchgelassen werden sollen. Weitere Informationen zu dieser Einstellung finden Sie unter [Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Deduplicate Traits**: Aktivieren Sie diese Einstellung, um die Nutzer-Traits im [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify)-Aufruf zu deduplizieren.
- **Show Braze logs**: Diese Einstellung ist nur bei Verwendung des [JavaScript SDK or Software-Development-Kit](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) als Quelle anwendbar. Aktivieren Sie sie, um Ihren Nutzer:innen die Braze-Logs anzuzeigen.
- **OneTrust Cookie Categories**: Mit dieser Einstellung können Sie die [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/)-Cookie-Zustimmungsgruppen mit Braze verknüpfen.

## Unterstützte Methoden {#supported-methods}

Braze unterstützt die RudderStack-Methoden identify, track, screen, page, group und alias.

{% tabs %}
{% tab Identify %}

Die RudderStack-[`identify`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#identify) verknüpft Nutzer:innen mit ihren Aktionen. RudderStack erfasst eine eindeutige Nutzer-ID und optionale Merkmale, die mit diesen Nutzer:innen verknüpft sind, wie Name, E-Mail, IP-Adresse usw.

**Delta-Management für Identify-Aufrufe**<br>
Wenn Sie Ereignisse im Device-Modus an Braze senden, können Sie Kosten sparen, indem Sie Ihre `identify`-Aufrufe deduplizieren. Aktivieren Sie dazu die Einstellung „Deduplicate Traits“ im Dashboard. RudderStack sendet dann nur die geänderten oder aktualisierten Attribute (Traits) an Braze.

**Nutzer:in löschen**<br>
Sie können Nutzer:innen in Braze mithilfe der [Suppression with Delete regulation](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) der RudderStack-[Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/) löschen.

{% endtab %}
{% tab Track %}

Die RudderStack-[`track`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#track) erfasst alle Nutzeraktivitäten und die damit verbundenen Eigenschaften.

**Order Completed**<br>
Wenn Sie die [RudderStack-E-Commerce-API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) verwenden, um die Track-Methode für ein Ereignis mit dem Namen `Order Completed` aufzurufen, sendet RudderStack die in diesem Ereignis aufgeführten Produkte als [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) an Braze.

{% endtab %}
{% tab Screen %}

Die RudderStack-[`screen`-Methode](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) ermöglicht es Ihnen, die mobilen Bildschirmansichten Ihrer Nutzer:innen zusammen mit zusätzlichen Informationen zum angezeigten Bildschirm aufzuzeichnen.

{% endtab %}
{% tab Page %}

Die RudderStack-[`page`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#page) ermöglicht es Ihnen, die Seitenaufrufe Ihrer Website aufzuzeichnen. Sie erfasst außerdem alle weiteren relevanten Informationen zu dieser Seite.

{% endtab %}
{% tab Group %}

Die RudderStack-[`group`-Methode](https://rudderstack.com/docs/destinations/marketing/braze/#group) ermöglicht es Ihnen, Nutzer:innen einer Gruppe zuzuordnen.

**Abo-Gruppenstatus**<br>
Um den Abo-Gruppenstatus zu Update or aktualisieren or aktualisieren, aktivieren Sie die Einstellung „Enable subscription groups in group call“ im RudderStack-Dashboard und senden Sie den Abo-Gruppenstatus im Group-Aufruf.

{% endtab %}
{% tab Alias %}

Die RudderStack-[`alias`-Methode](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) ermöglicht es Ihnen, verschiedene Identitäten bekannter Nutzer:innen zusammenzuführen. Beachten Sie, dass RudderStack den Alias-Aufruf für Braze nur im Cloud-Modus unterstützt.

{% endtab %}
{% endtabs %}

## Nutzer-Traits als verschachtelte angepasste Attribute senden {#send-user-traits-as-nested-custom-attributes}

Sie können die Nutzer-Traits als verschachtelte angepasste Attribute an Braze senden und Hinzufüge-, Aktualisierungs- und Entfernungsoperationen darauf ausführen. Aktivieren Sie dazu die Einstellung „Use angepasste Attribute Operation dashboard“ in RudderStack, während Sie das Braze-Ziel konfigurieren. Dieses Feature ist nur im Cloud-Modus verfügbar.

Sie können die Nutzer-Traits als verschachtelte angepasste Attribute in Ihren `identify`-Ereignissen im folgenden Format senden:
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

Um die Nutzer-Traits als angepasste Nutzerattribute über die Aufrufe `track`, `page` oder `screen` zu senden, übergeben Sie `traits` als kontextuelles Feld im Ereignis:
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
Für die Aktualisierungs- und Entfernungsoperationen ist `identifier` ein erforderlicher Schlüssel. Wenn Hinzufüge-, Aktualisierungs- oder Entfernungsoperationen im verschachtelten Array nicht vorhanden sind, verwendet RudderStack standardmäßig die Erstellungsoperation, um die Eigenschaften zu erstellen. Weitere Informationen zum Senden verschachtelter angepasster Attribute finden Sie unter [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### In den RudderStack-Logs wird „[Braze Deduplication]: Duplicate user detected, the user is dropped“ angezeigt {#i-see-braze-deduplication-duplicate-user-detected-the-user-is-dropped-in-rudderstack-logs}

Diese Meldung stammt von RudderStack, wenn **Deduplicate Traits** aktiviert ist und RudderStack unveränderte Nutzer:innen-Traits verwirft, bevor sie an Braze weitergeleitet werden. Es handelt sich nicht um einen Braze-Fehler.

RudderStack vergleicht eingehende `identify`- und `track`-Traits mit dem Kundenprofil or Nutzerprofil und überspringt Attribute ohne Änderung, um die Braze-Datenpunkt-Nutzung zu reduzieren. Weitere Informationen finden Sie in der RudderStack-Dokumentation [User Trait Deduplication in Braze](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/).

Wenn Sie möchten, dass bei jedem Aufruf alle Traits gesendet werden, deaktivieren Sie **Deduplicate Traits** in den Einstellungen Ihres RudderStack-Braze-Ziels. Beachten Sie, dass dies den Verbrauch von Braze-Datenpunkten erhöhen kann.