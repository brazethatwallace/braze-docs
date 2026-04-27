---
nav_title: GRAVTY®
article_title: GRAVTY® Loyalty Platform
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und GRAVTY®, einer Enterprise-Loyalty-Plattform, mit der Marken datengestützte Kundenbindungs-Programme entwerfen, verwalten und skalieren können, um Customer-Engagement und Bindung zu verbessern."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# GRAVTY® Loyalty Platform

> [GRAVTY®](https://www.lji.io/) ist eine Enterprise-Loyalty-Plattform von Loyalty Juggernaut Inc. (LJI), mit der Marken aus den Bereichen Einzelhandel, Reise, Gastronomie (einschließlich Schnellrestaurants) und Finanzdienstleistungen Programme der nächsten Generation entwerfen, verwalten und skalieren können – für messbares Wachstum bei Engagement, Bindung und Lifetime-Value durch personalisierte, datengestützte Erlebnisse.

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Anwendungsfälle {#use-cases}

Diese Integration unterstützt die folgenden Braze-Funktionen:

- **Nutzerdaten-Synchronisierung (`/users/track`):** Synchronisieren Sie Mitglieder-Attribute, Events und Käufe mit Braze für Segmentierung und Personalisierung.
- **Campaign-Triggering (`/campaigns/trigger/send`):** Triggern Sie einmalige oder transaktionale Nachrichten über Braze Campaigns.
- **Canvas-Triggering (`/canvas/trigger/send`):** Starten Sie mehrstufige Journeys und Lifecycle-Messaging über Braze **Canvas**.
- **Segmentierung und Personalisierung:** Erstellen Sie gezielte Zielgruppen und stellen Sie personalisierte Kommunikation auf Basis synchronisierter Daten bereit.

## Integration

Die Integration von GRAVTY® und Braze ist API-basiert. Sie unterstützt Echtzeit-Datensynchronisierung und Kommunikations-Triggering.

![Flussdiagramm, das zeigt, wie GRAVTY® Daten und Trigger an Braze-APIs sendet, die dann Nachrichten über SMS, E-Mail, Push und WhatsApp zustellen.]({% image_buster /assets/img/lji/braze-gravty-integration.png %})

### 1. Schritt: Braze mit GRAVTY® verbinden {#step-1-connect-braze-with-gravty}

1. Gehen Sie in GRAVTY® zu **Subscriber Setup**, um externe Integrationen zu verwalten.
2. Wählen Sie **Add New Subscriber** aus.
3. Wählen Sie **Braze** als Integrationsanbieter aus.
4. Geben Sie Folgendes ein:
   * **API URL** (Ihr Braze-REST-Endpunkt)
   * **API Key** (Ihr Braze-REST-API-Schlüssel)
5. Speichern Sie die Konfiguration und bestätigen Sie, dass die Verbindung aktiv ist.

![GRAVTY®-Formular „Add Subscriber“ mit ausgewähltem Braze, Feldern für API-URL und API-Schlüssel sowie einem aktiven Subscriber-Toggle.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### 2. Schritt: Template-Attribut-Mapping konfigurieren {#step-2-configure-template-attribute-mapping}

Nachdem Sie den Braze-Subscriber gespeichert haben, öffnet GRAVTY® die Seite **Template Attribute Mapping**. Verwenden Sie diese, um Felder auf Braze abzubilden.

1. Wählen Sie **Add New Field** aus.
2. Wählen Sie ein **GRAVTY®-Attribut** aus der Liste aus.
3. Geben Sie den **Braze-Attributnamen** (angepasstes Attribut) ein, unter dem der Wert in Braze erscheinen soll.

{% alert important %}
Sie müssen `external_id` nicht mappen. GRAVTY® generiert diesen Wert intern durch Hashing der Mitglieds-ID, und Braze empfängt diesen gehashten Wert als `external_id` im Nutzerprofil.<br><br> Bevor Sie die Integration aktivieren, stellen Sie sicher, dass dies mit der Art übereinstimmt, wie Sie `external_id` heute in Braze setzen. Wenn Braze bereits eine andere `external_id` für dieselben Personen verwendet, arbeiten Sie mit LJI zusammen, um die Bezeichner abzugleichen, bevor Sie Daten synchronisieren.
{% endalert %}

{: start="4"}
4. Wiederholen Sie die Schritte 1–3, um weitere Mappings hinzuzufügen.
5. Wählen Sie **Save** aus.

![GRAVTY®-Seite „Subscription Setup“ mit Template-Konfiguration, Sync-Konfiguration und einer Tabelle, die Entity, GRAVTY®-Attribut und Template-Attribut-Felder für Braze abbildet.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
Die Integration unterstützt Braze-Datentypen für angepasste Attribute, einschließlich Zahlen (Integer, Gleitkommazahl), Strings, Arrays, Boolesche Werte, Objekte, Arrays von Objekten und Datumsangaben.
{% endalert %}

### 3. Schritt: Integration testen {#step-3-test-the-integration}

Triggern Sie ein Beispiel-Event in GRAVTY®, um die Synchronisierung, Kommunikations-Trigger und den End-to-End-Ablauf zu bestätigen.

![Braze-Nutzerprofil-Übersicht mit Profil, angepassten Attributen (Stufe, Daten, Land, Ort) und angepassten Events, die aus dem GRAVTY®-Mapping befüllt wurden.]({% image_buster /assets/img/lji/braze-member-profile.png %})

## Support

Für Integrations-Support oder Fehlerbehebung kontaktieren Sie LJI unter [support@lji.io](mailto:support@lji.io).