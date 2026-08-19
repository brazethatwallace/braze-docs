---
nav_title: Standort-Targeting
article_title: Standort-Targeting
page_order: 7
page_type: tutorial
tool:
- Segments
- Location
description: "Dieser Artikel zeigt Ihnen, wie Sie Standort-Targeting einrichten, um Nutzer:innen nach Standort zu segmentieren."

---

# Standort-Targeting {#location-targeting}

> Dieser Artikel beschreibt, wie Sie Standort-Targeting einrichten, um Nutzer:innen nach ihrem letzten Standort zu segmentieren.

## Schritt 1: Segment erstellen {#step-1-create-your-segment}

Navigieren Sie zur Seite **Segments** unter **Audience**, um alle Ihre aktuellen Nutzer:innen-Segmente anzuzeigen. Auf dieser Seite können Sie neue Segmente erstellen und benennen. Wählen Sie zunächst **Create Segment** aus und geben Sie Ihrem Segment einen Namen.

![Modal zum Erstellen eines Segments.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Schritt 2: Standort anpassen {#step-2-customize-your-location}

Nachdem Sie Ihr Segment erstellt haben, fügen Sie einen Filter `Most Recent Location` hinzu, um Nutzer:innen anhand des letzten Ortes hervorzuheben, an dem sie Ihre App verwendet haben. Sie haben die Möglichkeit, Nutzer:innen innerhalb oder außerhalb einer standardmäßigen kreisförmigen Region oder einer anpassbaren polygonalen Region hervorzuheben.

![Filter für den letzten Standort innerhalb eines Kreises.]({% image_buster /assets/img_archive/filter_recent_location.png %})

### Nutzer:innen ohne Standortdaten {#users-without-location-data}

Nutzer:innen ohne Standortdaten – einschließlich Nutzer:innen, deren Standort zuvor erfasst und später gelöscht wurde – entsprechen Filtern für `most recent location outside of circle` und `most recent location outside of polygon`. Um Nutzer:innen ohne Standortdaten auszuschließen, kombinieren Sie den Filter `Most Recent Location` mit einem Filter `Location Available`.

{% tabs %}
{% tab Kreisförmig %}

### Kreisförmige Regionen {#circular-regions}

Für kreisförmige Regionen können Sie die Herkunft verschieben und den Standortradius für Ihre Segmentierung anpassen.

![Eine kreisförmige Umrisslinie von Städten zwischen New Jersey und New York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonal %}

### Polygonale Regionen {#polygonal-regions}

Für polygonale Regionen können Sie genauer festlegen, welche Bereiche in Ihr Segment einbezogen werden sollen.

![Ein Umriss des Bundesstaates New York als ausgewählte polygonale Region.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Partnerunterstützung für Beacons und Geofences {#partnership-support-for-beacon-and-geofence}

Die Kombination bestehender Beacon- oder Geofence-Unterstützung mit unseren Targeting- und Messaging-Features liefert Ihnen mehr Informationen über die physischen Aktionen Ihrer Nutzer:innen, sodass Sie ihnen entsprechende Nachrichten senden können. Sie können Standort-Tracking mit einigen unserer Partner nutzen:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)