---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Radar, einer Geofencing-Plattform, mit der Sie Ihren iOS- und Android-Apps Standort-Kontext und Tracking hinzufügen können."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.radar.com/) ist die führende Plattform für Geofencing und Standort-Tracking. Die Radar-Plattform besteht aus drei Kernprodukten: [Geofences](https://radar.com/product/geofencing), [Trip Tracking](https://radar.com/product/trip-tracking) und [Geo APIs](https://radar.com/product/api). Die Kombination der branchenführenden Engagement-Plattform von Braze mit den branchenführenden Geofencing-Funktionen von Radar erlaubt es Ihnen, durch eine breite Palette von standortbasierten Produkt- und Diensterlebnissen Ihren Umsatz zu steigern und die Kundenbindung zu stärken. Dazu gehören das Tracking von Abholungen und Zustellungen, durch den Standort getriggerte Benachrichtigungen, kontextuelle Personalisierung, Standortüberprüfung, Shop-Locators, automatische Adressvervollständigung und mehr.

_Diese Integration wird von Radar gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Radar erlaubt Ihnen den Zugriff auf ausgefeilte standortbasierte Kampagnen-Trigger or triggern und die Anreicherung von Nutzerprofilen mit umfangreichen First-Party-Standortdaten. Wenn Radar-Geofence- oder Trip-Tracking-Events generiert werden, werden angepasste Events und Nutzerattribute in Realtime an Braze gesendet. Diese Events und Attribute können dann verwendet werden, um standortbezogene Campaigns zu Trigger or triggern or triggern, Abhol- und Zustellvorgänge auf der letzten Meile zu unterstützen, die Flotten- und Versandlogistik zu überwachen oder Nutzer:innen-Segmente auf der Grundlage von Standortmustern zu erstellen.

Darüber hinaus können die Radar Geo APIs verwendet werden, um Ihre Marketingkampagnen durch [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) anzureichern oder zu personalisieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Radar-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Radar-Konto. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| App-Bezeichner | Ihren [App-Bezeichner]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) finden Sie im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| iOS-API-Schlüssel<br>Android-API-Schlüssel | Diese API-Schlüssel finden Sie im Braze-Dashboard unter **Einstellungen** > **App-Einstellungen**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Um Daten zwischen den SDKs von Braze und Radar abzubilden, müssen Sie in beiden Systemen dieselben Nutzer-IDs oder Nutzer-Aliase festlegen. Dies kann mit der Methode `changeUser()` im Braze SDK or Software-Development-Kit und der Methode `setUserId()` im Radar SDK or Software-Development-Kit geschehen.

So aktivieren Sie die Integration:

1. Suchen Sie in Radar auf der Seite [Integrations](https://radar.com/documentation/integrations) nach Braze.
1. Setzen Sie **Enabled** auf **Yes**.
3. Geben Sie Ihren App-Bezeichner und Ihre API-Schlüssel ein.

{% alert note %}
Sie können separate API-Schlüssel für Test- und Live-Umgebungen festlegen.
{% endalert %}

{:start="4"}
4. Wählen Sie Ihren Braze-Endpunkt aus.
5. Geben Sie beliebige Filter für Events oder Event-Attribute ein, um sicherzustellen, dass nur relevante Daten an Braze für das Engagement-Marketing gesendet werden. Wann immer Radar-Events generiert werden, sendet Radar angepasste Events und Nutzerattribute an Braze. Events von iOS-Geräten werden mit Ihren iOS-API-Schlüsseln gesendet; Events und Nutzerattribute von Android-Geräten werden mit Ihren Android-API-Schlüsseln gesendet.

{% alert note %}
Standardmäßig wird Radar `userId` auf Braze `external_id` für angemeldete Nutzer:innen abgebildet. Sie können jedoch abgemeldete Nutzer:innen tracken oder angepasste Abbildungen festlegen, indem Sie Radar `metadata.brazeAlias` oder `metadata.brazeExternalId` einstellen. Wenn Sie `metadata.brazeAlias` einstellen, müssen Sie auch einen passenden Alias in Braze mit dem Label `radarAlias` hinzufügen.
{% endalert %}

## Event- und attributbasierte Anwendungsfälle {#event-and-attribute-based-use-cases}

Sie können angepasste Events und Nutzerattribute verwenden, um standortbezogene Segmente zu erstellen oder standortbezogene Campaigns zu Trigger or triggern or triggern.

### Benachrichtigung über die Ankunft im Shop für die Abholung am Straßenrand Trigger or triggern or triggern {#trigger-a-store-arrival-notification-for-curbside-pickup}

Senden Sie eine Push-Benachrichtigung mit Ankunftsanweisungen an die Nutzer:innen, wenn sie in Ihrem Shop für eine Abholung am Straßenrand eintreffen.

![Eine Campaign mit aktionsbasierter Zustellung, die anzeigt, dass die Campaign zugestellt wird, wenn das angepasste Event „arrived_at_trip_destination“ eintritt und „trip_metadata“ gleich „curbside“ ist.]({% image_buster /assets/img_archive/radar-campaign.png %})

### Ein Zielgruppen-Segment der letzten Shop-Besucher:innen erstellen {#build-an-audience-segment-of-recent-store-visitors}

Stellen Sie zum Beispiel alle Nutzer:innen zusammen, die Ihren Shop innerhalb der letzten 7 Tage besucht haben, unabhängig davon, ob sie einen Kauf getätigt haben oder nicht.

![Ein Segment, in dem „radar_geofence_tags“ den Wert my_store enthält und „radar_updated_at“ weniger als 7 Tage zurückliegt.]({% image_buster /assets/img_archive/radar-segment.png %})

## Connected-Content

Das folgende Beispiel zeigt, wie Sie eine Aktion durchführen, um Nutzer:innen in der Nähe mit einem digitalen Angebot in den Shop zu locken.

![Ein Android-Bild einer Connected-Content-Push-Nachricht, die „New In Store Deals, Walmart and Target near you“ anzeigt.]({% image_buster /assets/img/radar_example.png %}){: style="float:right;max-width:30%;border:0;"}

Um loszulegen, benötigen Sie Ihren öffentlichen Radar-API-Schlüssel, den Sie in Ihren Anfrage-URLs verwenden können.

Als Nächstes stellen Sie innerhalb eines `connected_content`-Tags eine GET-Anfrage an die [Search Places API](https://radar.com/documentation/api#search-places). Die Search Places API liefert Standorte in der Nähe, die auf [Radar Places](https://radar.com/documentation/places) basieren: eine Datenbank mit Standorten für Orte, Ketten und Kategorien, die einen umfassenden Überblick über die Welt bietet.

Das folgende Code-Snippet ist ein Beispiel dafür, was Radar als JSON-Objekt vom API-Aufruf zurückgibt:

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

Um die gezielte und personalisierte Connected-Content-Nachricht in Braze zu erstellen, können Sie das Braze-Attribut `most_recent_location` als Eingabe für den Parameter `near` in der URL der API-Anfrage verwenden. Das Attribut `most_recent_location` wird über die Radar-Event-Integration oder direkt über das Braze SDK or Software-Development-Kit erfasst.

Im folgenden Beispiel wird der Radar-Kettenfilter für Target- und Walmart-Standorte angewendet, und der Suchradius für nahe gelegene Standorte wird auf 2 km festgelegt.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Wie Sie am `connect_content`-Tag erkennen können, wird das JSON-Objekt in der lokalen Variable `nearbyplaces` gespeichert, indem `:save nearbyplaces` nach der URL hinzugefügt wird.
Sie können testen, wie die Ausgabe aussehen sollte, indem Sie auf {% raw %}`{{nearbyplaces.places}}`{% endraw%} verweisen.

Wenn wir unseren Anwendungsfall zusammenführen, sieht die Syntax der Campaign wie folgt aus. Der folgende Code iteriert durch das Objekt `nearbyplaces.places`, extrahiert eindeutige Werte und verkettet sie mit den richtigen, für Menschen lesbaren Trennzeichen für die Nachricht.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }}
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }}
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
In der [Radar-Dokumentation](https://radar.com/documentation/api) finden Sie alle Radar-APIs, die in Connected-Content verwendet werden können.
{% endalert %}