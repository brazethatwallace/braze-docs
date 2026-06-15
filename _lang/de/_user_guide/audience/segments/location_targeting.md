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

> Dieser Artikel zeigt Ihnen, wie Sie Standort-Targeting einrichten, um Nutzer:innen nach ihrem letzten Standort zu segmentieren. Dies ist ideal, wenn Sie standortbasierte Campaigns und Strategien planen.

## 1. Schritt: Segment erstellen {#step-1-create-your-segment}

Navigieren Sie zur Seite **Segments** unter **Audience**, um alle Ihre aktuellen Nutzer:innen-Segmente anzuzeigen. Auf dieser Seite können Sie neue Segmente erstellen und benennen. Wählen Sie zunächst **Segment erstellen** und geben Sie Ihrem Segment einen Namen.

![Modal zum Erstellen eines Segments.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## 2. Schritt: Standort anpassen {#step-2-customize-your-location}

Nachdem Sie Ihr Segment erstellt haben, fügen Sie einen Filter **Most Recent Location** hinzu, um Nutzer:innen nach dem letzten Ort zu filtern, an dem sie Ihre App verwendet haben. Sie haben die Möglichkeit, Nutzer:innen innerhalb oder außerhalb einer standardmäßigen kreisförmigen Region oder einer anpassbaren polygonalen Region hervorzuheben.

![Filter für den letzten Standort innerhalb eines Kreises.]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab Kreisförmig %}

### Kreisförmige Regionen {#circular-regions}

Bei kreisförmigen Regionen können Sie die Herkunft verschieben und den Standortradius für Ihre Segmentierung anpassen.

![Ein kreisförmiger Umriss von Städten zwischen New Jersey und New York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonal %}

### Polygonale Regionen {#polygonal-regions}

Bei polygonalen Regionen können Sie genauer festlegen, welche Bereiche in Ihr Segment einbezogen werden sollen.

![Ein Umriss des Bundesstaates New York als ausgewählte polygonale Region.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Partner-Support für Beacons und Geofences {#partnership-support-for-beacon-and-geofence}

Die Kombination bestehender Beacon- oder Geofence-Unterstützung mit unseren Targeting- und Messaging-Features liefert Ihnen mehr Informationen über die physischen Aktionen Ihrer Nutzer:innen, sodass Sie ihnen entsprechende Nachrichten senden können. Sie können Standort-Tracking mit einigen unserer Partner nutzen:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)