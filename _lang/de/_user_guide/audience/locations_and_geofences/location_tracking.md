---
nav_title: Standort-Tracking
article_title: Standort-Tracking
page_order: 0
page_type: reference
description: "Dieser Referenzartikel erklärt, wie Sie Standort-Tracking und Standort-Targeting in Ihren Apps nutzen und welche Partner Standort-Tracking unterstützen."
tool: Location
search_rank: 2
---

# Standort-Tracking {#location-tracking}

> Die Standorterfassung erfasst den letzten Standort eines Nutzers bzw. einer Nutzerin beim Öffnen der App mithilfe von GPS-Standortdaten. Sie können diese Informationen nutzen, um Daten basierend auf Nutzer:innen zu segmentieren, die sich an einem bestimmten Standort befanden.

## Standort-Tracking aktivieren {#enabling-location-tracking}

Um die Standorterfassung in Ihrer App zu aktivieren, lesen Sie den Entwicklerleitfaden für die von Ihnen verwendete Plattform:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Internet]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

Im Allgemeinen verwenden mobile Apps den GPS-Chip des Geräts und andere Systeme (wie Wi-Fi-Scanning), um den Standort von Nutzer:innen zu verfolgen. Web-Apps verwenden WPS (Wi-Fi Positioning System), um den Standort von Nutzer:innen zu verfolgen. Alle diese Plattformen erfordern, dass Nutzer:innen dem Standort-Tracking zustimmen. Die Genauigkeit Ihrer Standort-Tracking-Daten kann davon beeinflusst werden, ob Ihre Nutzer:innen Wi-Fi auf ihren Geräten aktiviert haben oder nicht. Android-Nutzer:innen können auch verschiedene Standortmodi wählen – Nutzer:innen, die den Modus „Batteriesparen“ oder „Nur Gerät“ verwenden, können ungenaue Daten aufweisen.

### SDK-Nutzerstandort nach IP-Adresse {#sdk-user-location-by-ip-address}

Braze erkennt Nutzerstandorte anhand des geolokaliserten Landes über die IP-Adresse zu Beginn der ersten SDK-Sitzung.

Zuvor verwendete Braze den Ländercode aus der Geräte-Locale bei der SDK-Nutzererstellung und für die Dauer der ersten Sitzung. Erst nach der Verarbeitung des ersten Sitzungsstarts wurde die IP-Adresse verwendet, um das zuverlässigere Land für die Nutzer:in festzulegen. Das bedeutete, dass das Land der Nutzer:in erst ab der zweiten Sitzung mit höherer Genauigkeit festgelegt wurde, nachdem der erste Sitzungsstart verarbeitet worden war.

Jetzt verwendet Braze die IP-Adresse, um den Länderwert in Nutzerprofilen festzulegen, die über das SDK erstellt wurden, und diese IP-basierte Ländereinstellung ist während und nach der ersten Sitzung verfügbar.

#### Automatische Standorterfassung {#automatic-location-collection}

Wenn aktiviert, ist die automatische Standorterfassung im SDK unabhängig vom IP-basierten Länderverhalten. Sie bezieht sich auf Geräte-Standortsignale wie GPS, wenn die Nutzer:in die Berechtigung erteilt hat, und ermöglicht Filter wie `Most Recent Location`. Sie füllt nicht automatisch detaillierte Felder wie den Ort allein aus der IP-Adresse.

Für Orts- oder Postleitzahl-basiertes Targeting verwenden Sie [`setLastKnownLocation()`]({{site.baseurl}}/developer_guide/analytics/tracking_location/) (siehe den SDK-Artikel für Ihre Plattform), Ihren eigenen IP-Geolocation-Dienst, der angepasste Attribute schreibt, oder [Standort-Targeting]({{site.baseurl}}/user_guide/audience/segments/location_targeting/) mit den von Ihnen erfassten Daten.

## Standort-Targeting {#location-targeting}

Mithilfe von Standort-Tracking-Daten und Segmenten können Sie standortbasierte Campaigns und Strategien einrichten. Beispielsweise möchten Sie vielleicht eine Werbeaktion für Nutzer:innen durchführen, die in einer bestimmten Region leben, oder Nutzer:innen in einer Region mit strengeren Vorschriften ausschließen.

Weitere Informationen zum Erstellen eines Standort-Segments finden Sie unter [Standort-Targeting]({{site.baseurl}}/user_guide/audience/segments/location_targeting/).

## Festes Setzen des Standard-Standortattributs {#hard-setting-the-default-location-attribute}

Sie können auch den [`users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) in unserer API verwenden, um das Standardattribut [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) zu aktualisieren. Ein Beispiel:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Partnerunterstützung für Beacons und Geofences {#partnership-support-for-beacon-and-geofence}

Die Kombination bestehender Beacon- oder Geofence-Unterstützung mit unseren Targeting- und Messaging-Features gibt Ihnen mehr Informationen über die physischen Aktionen Ihrer Nutzer:innen, sodass Sie ihnen entsprechend Nachrichten senden können. Sie können Standort-Tracking mit einigen unserer Partner nutzen:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Unterschiede zwischen Geofences und Standort-Tracking {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wann erfasst Braze Standortdaten? {#when-does-braze-collect-location-data}

Braze erfasst den Standort nur, wenn die Anwendung im Vordergrund geöffnet ist. Daher zielt unser Filter `Most Recent Location` auf Nutzer:innen basierend darauf ab, wo sie die Anwendung zuletzt geöffnet haben (auch als Sitzungsstart bezeichnet).

Sie sollten auch die folgenden Besonderheiten beachten:

- Wenn der Standort deaktiviert ist, zeigt der Filter `Most Recent Location` den zuletzt aufgezeichneten Standort an.
- Wenn eine Nutzer:in jemals einen Standort in ihrem Profil gespeichert hatte, qualifiziert sie sich für den Filter `Location Available`, auch wenn sie seitdem das Standort-Tracking deaktiviert hat.

### Was ist der Unterschied zwischen den Filtern „Most Recent Device Locale“ und „Most Recent Location“? {#whats-the-difference-between-the-most-recent-device-locale-and-most-recent-location-filters}

`Most Recent Device Locale` stammt aus den Geräteeinstellungen der Nutzer:in. Für iPhone-Nutzer:innen erscheint dies beispielsweise auf ihrem Gerät unter **Settings** > **General** > **Language & Region**. Dieser Filter wird verwendet, um Sprache und regionale Formatierung wie Datumsangaben und Adressen zu erfassen, und ist unabhängig vom Filter `Most Recent Location`.

`Most Recent Location` ist der letzte bekannte GPS-Standort des Geräts. Dieser wird beim Sitzungsstart aktualisiert und im Profil der Nutzer:in gespeichert.

### Werden die vorherigen Standortdaten einer Nutzer:in aus Braze entfernt, wenn sie das Standort-Tracking deaktiviert? {#if-a-user-opts-out-of-location-tracking-is-their-previous-location-data-removed-from-braze}

Nein. Wenn eine Nutzer:in jemals einen Standort in ihrem Profil gespeichert hatte, werden diese Daten nicht automatisch entfernt, wenn sie später das Standort-Tracking deaktiviert.

## Fehlerbehebung {#troubleshooting}

### Keine Nutzer:innen haben verfügbare Standorte {#no-users-have-available-locations}

Braze erfasst standardmäßig den letzten Standort von Nutzer:innen über das SDK. Das bedeutet in der Regel, dass der „letzte Standort“ der Standort ist, von dem aus Ihre Nutzer:innen Ihre App zuletzt verwendet haben. Wenn Sie Braze Hintergrund-Standortdaten senden, stehen Ihnen möglicherweise detailliertere Daten zur Verfügung.

Wenn keine Nutzer:innen verfügbare Standorte haben, können zwei schnelle Überprüfungen helfen, die Datenerfassung und Datenübertragung zu bestätigen.

#### Datenerfassung {#data-collection}

Bestätigen Sie, dass Ihre App Standortdaten erfasst:

- Für iOS bedeutet dies, dass Nutzer:innen an einem Punkt in der User Journey über eine Aufforderung der Weitergabe ihrer Standortdaten zustimmen.
- Für Android bestätigen Sie, dass Ihre App bei der Installation um Berechtigungen für den genauen oder ungefähren Standort bittet.

Um zu sehen, ob Nutzerstandortdaten an Braze gesendet werden, verwenden Sie den Filter **Location Available**. Dieser Filter ermöglicht es Ihnen, den Prozentsatz der Nutzer:innen mit einem „letzten Standort“ zu sehen.

![Ein Segment „Test Location“, das den Filter „Location Available“ verwendet.]({% image_buster /assets/img_archive/trouble7.png %})

#### Datenübertragung {#data-transfer}

Bestätigen Sie, dass Ihre Entwickler:innen Standortdaten an Braze übergeben. Normalerweise wird die Übergabe von Standortdaten automatisch vom SDK gehandhabt, nachdem die Nutzer:in die Berechtigungen erteilt hat, aber Ihre Entwickler:innen haben möglicherweise das Standort-Tracking in Braze deaktiviert. Weitere Informationen zum Standort-Tracking finden Sie für:
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)