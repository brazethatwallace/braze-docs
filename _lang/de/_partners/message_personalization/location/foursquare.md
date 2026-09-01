---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Foursquare, einer Plattform für Standortdaten, die das Triggern von Events in Realtime auf der Grundlage des Standorts ermöglicht."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) ist eine Plattform für Standortdaten, die Standort-Targeting in Ihren Braze-Campaigns ermöglicht. Verwenden Sie das Pilgrim SDK von Foursquare für iOS- und Android-Apps, um Events in Realtime auf der Grundlage des Standorts zu triggern. So können Sie die leistungsstarken Geo-Targeting-Funktionen von Foursquare nutzen, um relevante, personalisierte Nachrichten mit Braze zu versenden.

_Diese Integration wird von Foursquare gepflegt._

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Foursquare-Konto | Ein Foursquare-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Workspace- und App-IDs | Die Braze-Workspace- und App-IDs finden Sie in der [Entwicklungskonsole]({{site.baseurl}}/api/api_key). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Um die beiden Plattformen zu integrieren, müssen Sie die beiden SDKs integrieren und die passenden Nutzer:innen-Felder zuordnen. Nach der Integration des Pilgrim SDK erhalten Sie Standort-Events auf dem Gerät oder über einen Webhook.

### 1. Schritt: Nutzer-ID-Felder zuordnen {#step-1-map-user-id-fields}

Um die Felder zwischen den beiden SDKs korrekt zuzuordnen, setzen Sie in beiden Systemen dieselbe Nutzer-ID – mit der [`changeUser`-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#setting-user-ids) im Braze SDK und der `setUserId`-Methode von [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) im Pilgrim SDK.

### 2. Schritt: Pilgrim-Konsole konfigurieren {#step-2-configure-pilgrim-console}
![Ein Bild der Pilgrim-Konsole, die nach der Gruppen-ID, der Android-App-ID und der iOS-App-ID fragt.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Suchen Sie die Workspace- und App-IDs in der Braze-Entwicklungskonsole. Geben Sie anschließend Ihren Braze REST-API-Schlüssel und Ihre App-IDs in der Foursquare-Pilgrim-Konsole ein.

Sobald Sie die Pilgrim-Konsole konfiguriert haben, zeichnet das Pilgrim SDK Standort-Events auf und leitet sie an Braze weiter. So können Sie qualifizierte Kund:innen retargeten und segmentieren. Weitere Informationen finden Sie auf der [Foursquare-Entwicklerseite](https://developer.foursquare.com/).

{% alert important %}
Das Pilgrim SDK setzt voraus, dass Sie die Standortdienste aktivieren.
{% endalert %}

## Nachrichten triggern {#triggering-messages}

Sobald die Integration eingerichtet ist, können Sie eine Campaign oder ein Canvas erstellen, die bzw. das auf Standort-Events reagiert, die vom Pilgrim SDK generiert werden. Dieser Integrationsweg ist ideal für Realtime-Messaging direkt nachdem Nutzer:innen einen relevanten Ort betreten haben, oder für eine verzögerte Folgekommunikation nachdem sie den Ort verlassen haben – zum Beispiel eine Dankesnachricht oder eine Erinnerung.

So senden Sie eine Campaign, die Nachrichten basierend auf einem festgelegten Standort versendet:
- Erstellen Sie eine Braze-Campaign oder ein Canvas mit **aktionsbasierter Zustellung**
- Verwenden Sie als Trigger ein angepasstes Event namens `arrival` mit einem Event-Eigenschaftsfilter für `locationType`, wie im folgenden Screenshot dargestellt.

![Eine aktionsbasierte Campaign im Zustellungsschritt, bei der „arrival“ als Option für „angepasstes Event ausführen“ ausgewählt ist und „locationType“ gleich „home“ ist.]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Retargeting

Um Ihre Nutzer:innen zu retargeten, verwenden Sie das Pilgrim SDK, um ein angepasstes Attribut `last_location` in den Nutzerprofilen Ihrer Braze-Nutzer:innen zu setzen. Sie können dann den `matches regex`-Vergleich verwenden, um Nutzer:innen zu retargeten, die einen bestimmten Standort in der realen Welt aufgesucht haben – zum Beispiel alle Nutzer:innen segmentieren, die kürzlich in einer Pizzeria waren.

![Eine aktionsbasierte Campaign im Schritt „Zielgruppe zusammenstellen“, bei der „last_location“ gleich „Pizza Place“ ist.]({% image_buster /assets/img_archive/last-location-segment.png %})

Sie können in Braze auch Nutzer:innen segmentieren, die in einem bestimmten Zeitfenster eine bestimmte Art von Ort auf der Grundlage von Foursquares `primaryCategoryId` besucht haben. Um diesen Datenpunkt für Ihre Retargeting-Anwendungsfälle zu nutzen, protokollieren Sie `primaryCategoryId` als Event-Eigenschaft während Ihrer Zielgruppen-Segmentierung. Um die Nutzer:innen und Eigenschaften zu identifizieren, die von der Foursquare API und dem Pilgrim SDK verwendet werden, besuchen Sie die [Foursquare-Entwicklerseite](https://developer.foursquare.com/).