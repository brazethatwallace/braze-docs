---
nav_title: GRAVTY®
article_title: GRAVTY® Loyalty Platform
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und GRAVTY®, einer Enterprise-Loyalty-Plattform, mit der Marken datengestützte Kundenbindungs-Programme entwerfen, verwalten und skalieren können, um Customer-Engagement und Bindung zu verbessern."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# GRAVTY® Loyalty Platform

> [GRAVTY®](https://www.lji.io/) ist eine Enterprise-Loyalty-Plattform von Loyalty Juggernaut Inc. (LJI), mit der Marken aus den Bereichen Einzelhandel, Reise, Gastronomie (einschließlich Schnellrestaurants) und Finanzdienstleistungen Programme der nächsten Generation entwerfen, verwalten und skalieren können – für messbares Wachstum bei Engagement, Bindung und LTV durch personalisierte, datengestützte Erlebnisse.

GRAVTY® basiert auf einer flexiblen, API-first-Architektur und unterstützt Realtime-Earn-and-Burn, Partner-Ökosystem-Management und kanalübergreifende Integration. Teams können Programme schneller starten, iterieren und Loyalty-Erlebnisse im großen Maßstab bereitstellen.

_Diese Integration wird von LJI gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und GRAVTY® verbindet Loyalty-Daten und Messaging-Trigger über beide Plattformen hinweg. GRAVTY® sendet Nutzerdaten als Attribute, Events und Käufe an Braze. Braze speichert diese Daten und stellt Nachrichten über Kanäle wie SMS, E-Mail und Push-Benachrichtigungen zu. Sie verwenden die synchronisierten Daten für Segmentierung, Personalisierung und Trigger.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
| :--- | :--- |
| GRAVTY®-Konto | Ein GRAVTY®-Konto mit der Berechtigung, Integrationen zu konfigurieren und Event-Abonnements zu verwalten. |
| Braze-Konto | Ein aktives Braze-Konto mit aktiviertem API-Zugang. |
| Braze-REST-API-Schlüssel | Ein REST-API-Schlüssel mit den Berechtigungen `campaigns.trigger.send`, `canvas.trigger.send` und `users.track`.<br><br> Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Settings** > **API Keys**. |
| Braze-API-Endpunkt | Ihr Braze-REST-Endpunkt (zum Beispiel `https://rest.fra-01.braze.eu`). Weitere Informationen finden Sie unter [Braze-Instanzen und Endpunkte]({{site.baseurl}}/api/basics/#endpoints). |
| Campaign- oder Canvas-IDs | IDs für die **Campaigns**- oder **Canvas**-Workflows, die Sie von GRAVTY® aus triggern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Anwendungsfälle {#use-cases}

Diese Integration unterstützt die folgenden Braze-Funktionen:

- **Nutzerdaten-Synchronisierung (`/users/track`):** Synchronisieren Sie Mitglieder-Attribute, Events und Käufe mit Braze für Segmentierung und Personalisierung.
- **Campaign-Triggering (`/campaigns/trigger/send`):** Triggern Sie einmalige oder transaktionale Nachrichten über Braze Campaigns.
- **Canvas-Triggering (`/canvas/trigger/send`):** Starten Sie mehrstufige Journeys und Lifecycle-Messaging über Braze **Canvas**.
- **Segmentierung und Personalisierung:** Erstellen Sie gezielte Zielgruppen und stellen Sie personalisierte Kommunikation auf Basis synchronisierter Daten bereit.

## Integration

Die Integration von GRAVTY® und Braze ist API-basiert und ermöglicht Echtzeit-Datensynchronisierung und Kommunikations-Triggering zwischen GRAVTY® und Braze.

### 1. Schritt: Braze mit GRAVTY® verbinden {#step-1-connect-braze-with-gravty}

1. Gehen Sie in GRAVTY® zu **Subscriber Setup**, um externe Integrationen zu verwalten.
2. Wählen Sie **Add New Subscriber** aus.
3. Wählen Sie **Braze** als Integrationsanbieter aus.
4. Geben Sie Folgendes ein:
   * **API URL** (Ihr Braze-REST-Endpunkt)
   * **API Key** (Ihr Braze-REST-API-Schlüssel)
5. Speichern Sie die Konfiguration und bestätigen Sie, dass die Verbindung aktiv ist.

![GRAVTY®-Formular „Add Subscriber“ mit ausgewähltem Braze, Feldern für API-URL und API-Schlüssel sowie einem aktiven Subscriber-Toggle.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### 2. Schritt: Event-Trigger konfigurieren {#step-2-configure-event-trigger}

Erstellen Sie ein Event in GRAVTY®, das ausgelöst wird, wenn eine Mitgliederaktivität die von Ihnen definierten Bedingungen erfüllt (zum Beispiel eine Transaktion, gesammelte Punkte, eine Stufenänderung oder eine Programmanmeldung).

1. Navigieren Sie in GRAVTY® zum Abschnitt **Events**.
2. Klicken Sie auf **Create Event**.
3. Definieren Sie die Event-Bedingungen (zum Beispiel Transaktion erstellt, Punkte gesammelt oder Stufen-Upgrade).
4. Konfigurieren Sie die Regeln, die bestimmen, wann das Event getriggert werden soll.
5. Verknüpfen Sie den Braze-Subscriber mit dem Event, um Kommunikations-Trigger zu aktivieren.
6. Speichern Sie die Event-Konfiguration.

Das folgende Beispiel zeigt ein Event, das getriggert wird, wenn ein Mitglied in das Programm aufgenommen wird:

![GRAVTY®-Event-Konfiguration für die Programmanmeldung eines Mitglieds, mit Braze als verknüpftem Subscriber.]({% image_buster /assets/img/lji/event-configuration.png %})

### 3. Schritt: Template-Attribut-Mapping konfigurieren {#step-3-configure-template-attribute-mapping}

Nachdem Sie das Event konfiguriert haben, vervollständigen Sie die Subscriber-Konfiguration, um Datensynchronisierung und Kommunikations-Trigger zu aktivieren:

1. Wählen Sie den in [Schritt 1](#step-1-connect-braze-with-gravty) erstellten **Braze-Subscriber** aus der Subscriber-Dropdown-Liste aus.
2. Wählen Sie den passenden **Kanal** (**Campaign** oder **Canvas**) basierend auf Ihrem Anwendungsfall. Für reine Datensynchronisierungs-Szenarien kann der Kanal leer gelassen werden.
3. Geben Sie die entsprechende **Campaign-ID** oder **Canvas-ID** im Feld **Template Name** ein, sofern zutreffend.
4. Konfigurieren Sie den Kommunikationstyp, um Synchronisierung und/oder triggerbasiertes Messaging zu unterstützen.

So konfigurieren Sie das Feld-Mapping in GRAVTY®:

1. Klicken Sie auf **Add New Field**.
2. Wählen Sie das **GRAVTY®-Attribut** aus der Dropdown-Liste aus.
3. Geben Sie den entsprechenden **Braze-Attributnamen** ein, auf den die Daten abgebildet werden sollen.

{% alert important %}
Sie müssen `external_id` nicht mappen. GRAVTY® generiert diesen Wert intern durch Hashing der Mitglieds-ID (dem eindeutigen Mitglieds-Bezeichner in GRAVTY®), und Braze empfängt diesen gehashten Wert als `external_id` im Kundenprofil.<br><br> Bevor Sie die Integration aktivieren, stellen Sie sicher, dass dies mit der Art übereinstimmt, wie Sie `external_id` heute in Braze setzen. Wenn Braze bereits eine andere `external_id` für dieselben Personen verwendet, arbeiten Sie mit LJI zusammen, um die Bezeichner abzugleichen, bevor Sie Daten synchronisieren.
{% endalert %}

{: start="4"}
4. Wiederholen Sie die Schritte **1–3**, um weitere Mappings hinzuzufügen.
5. Klicken Sie auf **Save**, um die Konfiguration zu übernehmen.

![Attribut-Mapping-Konfiguration für die Braze-Mitglieder-Synchronisierung.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
Die Integration unterstützt alle Braze-Datentypen für angepasste Attribute, einschließlich Zahlen (Integer, Gleitkommazahl), Strings, Arrays, Boolesche Werte, Objekte, Arrays von Objekten und Datumsangaben.
{% endalert %}

### 4. Schritt: Integration testen {#step-4-test-the-integration}

Triggern Sie ein Beispiel-Event in GRAVTY®, um zu überprüfen, ob Synchronisierung, Kommunikations-Trigger und die gesamte Integration wie erwartet funktionieren.

* Mitgliederdaten werden mit Braze synchronisiert und im Mitgliederprofil angezeigt.

![Die Datenfelder werden basierend auf dem konfigurierten Feld-Mapping befüllt.]({% image_buster /assets/img/lji/braze-member-profile.png %})

* Kommunikation wird basierend auf der konfigurierten Campaign oder dem Canvas getriggert.

![Beispiel einer von Braze getriggerten E-Mail.]({% image_buster /assets/img/lji/braze-email-example.png %})

## Support

Für Integrations-Support oder Fehlerbehebung kontaktieren Sie LJI unter [support@lji.io](mailto:support@lji.io).