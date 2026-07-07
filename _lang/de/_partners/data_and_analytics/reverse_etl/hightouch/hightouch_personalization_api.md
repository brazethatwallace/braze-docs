---
nav_title: Hightouch Personalization API
article_title: Hightouch Personalization API
description: "Dieser Referenzartikel beschreibt die Integration zwischen Braze und der Personalization API von Hightouch, einem verwalteten Dienst zum Hosting einer Daten-API mit niedriger Latenz, die auf einem beliebigen Datensatz in Ihrem Cloud Data Warehouse basiert. Dieser Referenzartikel behandelt die Anwendungsfälle, die die Hightouch Personalization API löst, die Daten, mit denen sie arbeitet, wie Sie sie konfigurieren und wie Sie sie mit Braze integrieren."
page_type: partner
search_tag: Partner
---

# Hightouch Personalization API

> Die [Personalization API](https://hightouch.com/docs/destinations/personalization-api) von Hightouch ist ein verwalteter Dienst, mit dem Sie eine Daten-API mit niedriger Latenz hosten können, die auf einem beliebigen Datensatz in Ihrem Cloud Data Warehouse basiert.

![Architekturdiagramm der Hightouch Personalization API, das den Datenfluss von einem Data Warehouse über Hightouch zu mobilen Apps, Web-Erlebnissen und dynamischen E-Mails zeigt.]({% image_buster /assets/img/hightouch/cohort7.png %})

Die Integration von Braze und Hightouch ermöglicht es Ihnen, die API mit [Braze Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) zu nutzen, um aktuelle Kund:innen- oder Objektdaten zum Zeitpunkt des Versands in Ihre Campaigns oder Canvases zu ziehen.

Die Personalization API von Hightouch bietet einen REST-Endpunkt zur Verwendung innerhalb Ihrer Braze-Konfiguration. Konkret können Sie das Braze Connected-Content-Angebot nutzen, um eine GET-Anfrage an die Personalization API zu stellen und alle Informationen zu einem bestimmten Bezeichner abzurufen. Die von dieser API bereitgestellten Daten können Kund:innen-, Produkt- oder andere Objektdaten darstellen.

![Diagramm, das den Datenfluss von Snowflake, BigQuery und Redshift über die Hightouch Personalization API zu Braze Connected-Content zeigt.]({% image_buster /assets/img/hightouch/cohort6.png %})

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| [Hightouch-Konto](https://app.hightouch.com/login) mit aktivierter Personalization API | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Hightouch [Business-Tier-Konto](https://hightouch.com/pricing). |
| Definierte Anwendungsfälle | Bevor Sie die API einrichten, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. In der folgenden Liste finden Sie gängige Anwendungsfälle. |
| In einem Cloud Data Warehouse oder einer anderen Datenquelle gespeicherte Daten | Hightouch lässt sich mit [über 25 Datenquellen](https://hightouch.com/integrations) integrieren. |
| Hightouch-API-Schlüssel | Dieser kann unter **Hightouch > Settings > API keys > Add API key** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% tabs %}
{% tab Anwendungsfälle %}

### Anwendungsfälle {#use-cases}

Bevor Sie beginnen, sollten Sie genau planen, wie Sie die Personalization API verwenden möchten.

Zu den gängigen Anwendungsfällen gehören:
- **Produktempfehlungen**, um die Einbettung personalisierter Produktempfehlungen in E-Mail-Templates, Campaigns oder App-Erlebnisse zu optimieren
- **Personalisierte Marketing-Campaigns** durch Anreicherung von Marketing-Touchpoints mit dynamischen Produktempfehlungen
- **Personalisierung in der App oder im Internet**, z. B. angepasste Suchergebnisse, kohortenbasierte Preisgestaltung und Messaging, Artikelempfehlungen oder nächstgelegene Shop-Standorte
- **Empfehlungen auf Basis finanzieller oder medizinischer Daten** – Finanzdaten unterliegen strengen Anforderungen, die Hightouch durch seine [strengen Richtlinien zur Datensicherheit](https://hightouch.com/docs/security/overview#compliance) erfüllt. Mit Hightouch können Sie Kundensegmente auf der Grundlage finanzieller oder medizinischer Daten erstellen, ohne die zugrunde liegenden Attribute offenzulegen, die in Ihren Segmentierungskriterien verwendet werden.

{% endtab %}
{% tab Datensätze %}

### Datensätze {#datasets}

Die Personalization API fungiert als Cache für ausgewählte Daten in Ihrem Data Warehouse, sodass Sie die Empfehlungsdaten bereits dort gespeichert haben sollten. Sie können Hightouch verwenden, um sie bei Bedarf nach einem Template zu transformieren. Zu dieser Art von Daten gehören:
- Nutzer:innen-Metadaten wie geografische Region, Alter oder andere demografische Informationen
- Nutzer:innen-Aktionen oder -Ereignisse, einschließlich früherer Käufe, Seitenaufrufe, Klicks usw.

{% endtab %}
{% endtabs %}

## Integration

### 1. Schritt: Datenquelle mit Hightouch verbinden {#step-1-connect-data-source-to-hightouch}

[Hightouch-Quellen](https://hightouch.com/docs/getting-started/concepts#sources) sind der Ort, an dem die Geschäftsdaten Ihres Unternehmens gespeichert sind. In diesem Fall ist es der Ort, an dem Ihre Nutzerdaten gespeichert sind.
1. Gehen Sie in Hightouch zu **Sources Overview > Add Source**. Wählen Sie Ihr Data Warehouse als Quelle aus.<br><br>
2. Geben Sie die entsprechenden Zugangsdaten ein; diese unterscheiden sich je nach Quelle.

Weitere Einzelheiten finden Sie in der entsprechenden [Dokumentation](https://hightouch.com/docs).

### 2. Schritt: Daten modellieren {#step-2-model-data}

Hightouch-Modelle definieren, welche Daten aus Ihrer Quelle gezogen werden sollen. Um ein neues Modell einzurichten, gehen Sie folgendermaßen vor:

1. Gehen Sie in Hightouch zu [**Models overview**](https://app.hightouch.com/models) > **Add model** und wählen Sie die Quelle aus, die Sie gerade verbunden haben.<br><br>
2. Wählen Sie als Nächstes eine [Modellierungsmethode](https://hightouch.com/docs/models/creating-models). Da alle Ihre Informationen in einer Tabelle zusammengefasst werden sollten, können Sie den visuellen Tabellenselektor verwenden, um diese zu definieren. Alternativ können Sie SQL schreiben, um nur die gewünschten Spalten einzubeziehen, oder sich auf Ihre vorhandenen dbt-Modelle, Looker Looks oder Sigma-Arbeitsmappen verlassen.<br><br>
3. Bevor Sie fortfahren, zeigen Sie eine Vorschau Ihres Modells an, um sicherzustellen, dass es die gewünschten Daten abfragt. Standardmäßig beschränkt Braze die Vorschau auf die ersten 100 Datensätze. Nachdem Sie Ihre Daten validiert haben, klicken Sie auf **Continue**.<br><br>
4. Benennen Sie Ihr Modell, zum Beispiel „Nutzer:innen-Empfehlungen“.<br><br>
5. Wählen Sie abschließend einen Primärschlüssel aus und klicken Sie auf **Finish**. Ein Primärschlüssel sollte eine Spalte mit eindeutigen Bezeichnern sein. Dies ist auch das Feld, über das Sie die Personalization API aufrufen, um die Empfehlungen einer bestimmten Nutzer:in abzurufen.

### 3. Schritt: Personalization API konfigurieren {#step-3-configure-personalization-api}

Das Vorbereiten der API für den Empfang von Anfragen besteht aus zwei Schritten:
- Aktivieren der Personalization API in den Regionen, die Ihrer Infrastruktur am nächsten liegen
- Erstellen von Syncs, um festzulegen, welche Modelle im von Hightouch verwalteten Cache materialisiert werden sollen

Folgen Sie diesen Anweisungen, um beides abzuschließen:

1. Gehen Sie in Hightouch zu [**Destinations**](https://app.hightouch.com/destinations) und wählen Sie die für Sie erstellte Hightouch Personalization API aus. Wenn Sie dieses Ziel nicht aktiviert haben, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com).<br><br>
2. Wählen Sie dann die entsprechende Region aus. Wenn Sie die Region auswählen, die Ihrer Infrastruktur am nächsten liegt, verkürzen sich Ihre Antwortzeiten. Wenn Sie keine Region in der Nähe Ihrer Infrastruktur sehen, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com).<br><br>
3. Rufen Sie die [Übersichtsseite **Syncs**](https://app.hightouch.com/syncs) auf und klicken Sie auf den Button **Add sync**. Wählen Sie dann das entsprechende Modell und das Ziel aus, das Sie zuvor eingerichtet haben.<br><br>
4. Geben Sie einen alphanumerischen Namen für die Sammlung ein. Sammlungen sind konzeptionell ähnlich wie Datenbanktabellen. Jede sollte einen bestimmten Datentyp repräsentieren, z. B. Kund:innen oder Rechnungen. Die Sammlungsnamen müssen alphanumerisch sein und werden Teil Ihres Personalization-API-Endpunkts.<br><br>
5. Geben Sie als Nächstes an, welche Spalte aus Ihrem Modell als Primärindex für die Datensatzsuche dienen soll. Dieses Feld muss jeden Datensatz in der Sammlung eindeutig identifizieren und ist oft derselbe wie der Primärschlüssel Ihres Modells. Die Personalization API unterstützt Abfragen über mehrere Indizes. Sie könnten zum Beispiel Kundenprofile mit `user_id`, `anonymous_id` oder `email_address` abrufen wollen. Um mehrere Indizes zu aktivieren, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com).<br><br>
6. Verwenden Sie den Feld-Mapper, um festzulegen, welche Spalten aus Ihrem Modell in die API-Antwort-Payload aufgenommen werden sollen. Sie können diese Felder umbenennen und den erweiterten Mapper verwenden, um Transformationen mithilfe der Liquid-Template-Sprache anzuwenden.<br><br>
7. Wählen Sie das passende [Löschverhalten](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) für Ihren Anwendungsfall aus.<br><br>
8. Klicken Sie abschließend auf **Continue** und wählen Sie einen [Sync-Zeitplan](https://hightouch.com/docs/syncs/schedule-sync-ui) aus.

Hightouch synchronisiert jetzt die Daten in Ihrem Data Warehouse mit einer verwalteten Datenbank und stellt sie über die Personalization API zur Verfügung.

### 4. Schritt: Personalization API über Braze Connected-Content aufrufen {#step-4-call-personalization-api-through-braze-connected-content}

Sobald Sie Ihre Personalization-API-Instanz eingerichtet haben, können Sie sie als Braze Connected-Content-Endpunkt verwenden.

Die API ist unter `https://personalization.{region}.hightouch.com` zugänglich, zum Beispiel unter `https://personalization.us-west-2.hightouch.com`.

Die Informationen sind über diesen Endpunkt verfügbar: `/v1/collections/:collection_name/records/:index_key/:index_value`.

Sie können dieses Snippet zum Beispiel in eine Campaign oder ein Canvas einfügen:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Sie können Liquid-Templating verwenden, um die in der JSON-Payload zurückgegebenen Eigenschaften zu referenzieren und sie in Ihrem Messaging zu verwenden.

Für die Beispiel-Payload unten:

```json
{
    "user_id": 12345,
    "full_name": "Alex Smith",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ]
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Alex Lee",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    }
}
```

Die folgenden Liquid-Referenzen würden diese Beispieldaten zurückgeben:

| Liquid-Template | Zurückgegebenes Beispiel |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %} | Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %} | San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %} | Universal Language |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4: Personalization API über Braze Connected-Content aufrufen" }

## Fehlerbehebung {#troubleshooting}

Wenn Sie Fragen haben, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com), um Hilfe zu erhalten.