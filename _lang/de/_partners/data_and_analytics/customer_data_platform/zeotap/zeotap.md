---
nav_title: Zeotap
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zeotap, einer Customer Data Platform der nächsten Generation, die Identitätsauflösung, Insights und Datenanreicherung bietet."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) ist eine Customer Data Platform der nächsten Generation, die Ihnen hilft, Ihre mobile Zielgruppe zu entdecken und zu verstehen, indem sie Identitätsauflösung, Insights und Datenanreicherung bietet.

Mit der Integration von Zeotap und Braze können Sie den Umfang und die Reichweite Ihrer Campaigns erweitern, indem Sie Zeotap-Kundensegmente synchronisieren, um Nutzerdaten Braze-Nutzerkonten zuzuordnen. Sie können dann auf diese Daten reagieren und Ihren Nutzer:innen personalisierte Targeting-Erlebnisse zustellen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Zeotap-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Zeotap-Konto](https://zeotap.com/). |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({% image_buster /assets/img/zeotap/zeotap1.png %}) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Erstellen Sie ein Zeotap-Ziel {#step-1-create-a-zeotap-destination}

1. Navigieren Sie auf der Zeotap Unity Plattform zur Anwendung **DESTINATIONS**.
2. Wählen Sie unter **All Channels** die Option **Braze** aus.
3. Geben Sie in der daraufhin angezeigten Eingabeaufforderung den Namen Ihres Ziels sowie Ihren Client-Namen und den Braze Representational State Transfer-API-Schlüssel an, der mit Ihrem Braze-Konto verknüpft ist.
4. Wählen Sie abschließend Ihre Braze REST-Endpunkt-Instanz aus der Dropdown-Liste aus und speichern Sie das Ziel. <br><br>![Zeotap-Braze-Zielkonfiguration mit Dropdown für die Endpunkt-Instanz.]({% image_buster /assets/img/zeotap/zeotap1.png %})

### 2. Schritt: Erstellen und verknüpfen Sie ein Zeotap-Segment mit Ihrem Ziel {#step-2-create-and-link-a-zeotap-segment-to-your-destination}

1. Navigieren Sie auf der Zeotap Unity Plattform zur Anwendung **CONNECT**.
2. Erstellen Sie ein Segment und wählen Sie das in [Schritt 1](#step-1-create-a-zeotap-destination) erstellte Braze-Ziel aus.
3. Wählen Sie einen unterstützten Ausgabe-Bezeichner aus: MAIDs, mit SHA256 gehashte E-Mail-Adressen oder einen beliebigen 1P-Kundenbezeichner, der von Braze erkannt wird (wenn Sie einen angepassten Bezeichner für Ihr Braze-Konto verwenden möchten, setzen Sie sich mit Zeotap in Verbindung, damit dieser für Ihr Konto aktiviert werden kann). Für die Braze-Integration kann nur ein Ausgabe-Bezeichner verwendet werden. Diese Bezeichner müssen mit der externen ID übereinstimmen, die bei der Erfassung von Braze SDK or Software-Development-Kit-Daten festgelegt wird.
4. Speichern Sie das Segment.

![Zeotap-CONNECT-Segment-Einrichtung, verknüpft mit dem Braze-Ziel.]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Die angezeigten Bezeichner sind sowohl im Segment verfügbar als auch von Braze unterstützt.
{% endalert %}

### 3. Schritt: Braze-Segment erstellen {#step-3-create-braze-segment}

Nachdem Sie ein Segment in Zeotap erfolgreich erstellt, gepusht und verarbeitet haben, erscheinen die Zeotap-Nutzer:innen im Braze-Dashboard. Sie können Nutzer:innen im Braze-Dashboard anhand ihrer Nutzer-ID suchen.

![Ein Braze-Nutzerprofil, in dem unter „Angepasste Attribute“ die Segmente eins bis vier als „true“ aufgeführt sind.]({% image_buster /assets/img/zeotap/zeotap4.png %})

Wenn ein:e Nutzer:in Teil des Zeotap-Segments ist, erscheint der Segmentname als angepasstes Attribut im Kundenprofil or Nutzerprofil mit dem booleschen Wert `true`. Notieren Sie sich den Namen des angepassten Attributs, da Sie ihn bei der Erstellung eines Braze-Segments benötigen.

Als Nächstes müssen Sie dieses Segment in Braze erstellen und definieren:
1. Wählen Sie im Braze-Dashboard **Segments** und dann **Create Segment**.
2. Benennen Sie Ihr Segment und wählen Sie das in Zeotap erstellte Segment mit den angepassten Attributen aus.
3. Speichern Sie Ihre Änderungen.

![Im Braze Segment Builder finden Sie die importierten Segmente, die als angepasste Attribute festgelegt sind.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Sie können dieses neu erstellte Segment nun zu zukünftigen Braze Campaigns und Canvase hinzufügen, um diese Endnutzer:innen zu targetieren.