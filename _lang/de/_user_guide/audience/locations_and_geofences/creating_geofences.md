---
nav_title: Geofences erstellen
article_title: Geofences erstellen
page_order: 1
page_type: reference
toc_headers: h2
description: "Erfahren Sie, wie Sie Standortberechtigungen einrichten, einen Standortberechtigungs-Primer erstellen und Geofences für standortbasierte Campaigns erstellen."
tool:
  - Location
search_rank: 9
---

# Geofences {#geofences}

> Ein Geofence ist ein virtuelles geografisches Gebiet, das durch Breiten- und Längengrad in Kombination mit einem Radius dargestellt wird und einen Kreis um eine bestimmte globale Position bildet. Geofences können von der Größe eines Gebäudes bis zur Größe einer ganzen Stadt variieren. Sie können Geofences verwenden, um Campaigns in Echtzeit auszulösen, wenn Nutzer:innen deren Grenzen betreten oder verlassen, oder um Follow-up-Campaigns Stunden oder Tage später zu senden.

{% alert tip %}
Eine geführte Anleitung finden Sie im Braze-Lernkurs [Geofence erstellen](https://learning.braze.com/create-a-geofence).
{% endalert %}

## So funktioniert es {#how-it-works}

Geofences sind in Geofence-Sets organisiert – einer Gruppe von Geofences, die Sie verwenden können, um Nutzer:innen auf der gesamten Plattform zu segmentieren oder anzusprechen. Jedes Geofence-Set kann maximal 10.000 Geofences enthalten. Sie können eine unbegrenzte Anzahl von Geofences erstellen oder hochladen.

Nutzer:innen, die Ihre Geofences betreten oder verlassen, fügen eine neue Ebene von Nutzerdaten hinzu, die Sie für Segmentierung und Retargeting verwenden können.

Beachten Sie die folgenden Gerätelimits:

- Android-Apps können bis zu 100 Geofences gleichzeitig lokal speichern. Braze ist so konfiguriert, dass nur bis zu 20 Geofences lokal pro App gespeichert werden.
- iOS-Geräte können bis zu 20 Geofences gleichzeitig pro App überwachen. Braze überwacht bis zu 20 Standorte, wenn Platz verfügbar ist.
- Wenn Nutzer:innen für mehr als 20 Geofences berechtigt sind, lädt Braze die maximale Anzahl von Standorten basierend auf der Nähe zu den Nutzer:innen beim Sitzungsstart herunter.
- Damit Geofences korrekt funktionieren, stellen Sie sicher, dass Ihre App nicht alle verfügbaren Geofence-Plätze verwendet.

Die folgende Tabelle beschreibt gängige Geofence-Begriffe:

| Begriff | Beschreibung |
|---|---|
| Breiten- und Längengrad | Das geografische Zentrum des Geofence. |
| Radius | Der Radius des Geofence in Metern, gemessen vom geografischen Zentrum. Legen Sie einen Mindestradius von 100 bis 150 Metern für alle Geofences fest. |
| Cooldown | Nutzer:innen erhalten Geofence-getriggerte Benachrichtigungen, nachdem sie Eintritts- oder Austrittsübergänge an einzelnen Geofences durchgeführt haben. Nach einem Übergang gibt es einen vordefinierten Zeitraum, in dem diese Nutzer:innen denselben Übergang an diesem einzelnen Geofence nicht erneut durchführen können. Dieser „Cooldown“ ist von Braze vordefiniert und dient hauptsächlich dazu, unnötige Netzwerkanfragen zu verhindern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="So funktioniert es" }

## Voraussetzungen {#prerequisites}

### SDK or Software-Development-Kit- und Plattformanforderungen {#sdk-and-platform-requirements}

Geofence-getriggerte Campaigns sind auf iOS und Android verfügbar. Um Geofences zu unterstützen, ist Folgendes erforderlich:

* Braze-Geofences oder Standorterfassung müssen aktiviert sein.
* Nutzer:innen müssen den Standortzugriff „Immer erlauben“ gewähren.

{% alert important %}
Die Braze-Standorterfassung ist standardmäßig deaktiviert. Um zu überprüfen, ob sie auf Android aktiviert ist, bestätigen Sie, dass `com_braze_enable_location_collection` in Ihrer `braze.xml` auf `true` gesetzt ist.
{% endalert %}

Plattformspezifische Einrichtungsanweisungen finden Sie unter [Geofences]({{site.baseurl}}/developer_guide/geofences) im Entwicklerhandbuch.

### Standortberechtigungen {#location-permissions}

Bevor Ihre Geofences funktionieren können, müssen Nutzer:innen Ihrer App die Berechtigung zum Zugriff auf ihren Standort erteilen. Das Verständnis der verschiedenen Berechtigungsstufen und ihrer Auswirkungen auf Geofencing ist entscheidend für den Aufbau einer effektiven standortbasierten Strategie.

## Standortberechtigungen verstehen {#understanding-location-permissions}

Sowohl iOS als auch Android bieten mehrere Stufen des Standortzugriffs. Die Berechtigungsstufe, die Nutzer:innen gewähren, beeinflusst direkt, ob Geofencing funktioniert und wie genau die Standortdaten sind.

### Berechtigungsstufen {#permission-levels}

{% tabs local %}
{% tab iOS %}

| Berechtigung | Beschreibung | Geofencing-Unterstützung |
|---|---|---|
| **Einmal erlauben** | Gewährt Standortzugriff für eine einzelne Sitzung. Die Aufforderung erscheint erneut, wenn Nutzer:innen die App das nächste Mal öffnen. | Nein. Hintergrund-Tracking ist deaktiviert, sodass das Gerät nur Standort-Updates erhält, wenn die App geöffnet ist. |
| **Bei Verwendung der App erlauben** | Gewährt Standortzugriff, wenn die App im Vordergrund ist. Nachdem dies gewährt wurde, kann iOS eine Folgeaufforderung anzeigen, die Nutzer:innen auffordert, auf „Immer erlauben“ zu upgraden. | Ja. iOS aktiviert die Hintergrund-Standortüberwachung, einschließlich Geofence-Übergänge, für Apps mit dieser Berechtigung. |
| **Immer erlauben** | Gewährt kontinuierlichen Standortzugriff, auch im Hintergrund und wenn die App geschlossen ist. | Ja. Dies bietet die zuverlässigste Geofence-Überwachung. |
| **Nicht erlauben** | Verweigert jeglichen Standortzugriff. | Nein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungsstufen" }

{% endtab %}
{% tab Android %}

| Berechtigung | Beschreibung | Geofencing-Unterstützung |
|---|---|---|
| **Bei Verwendung der App** | Gewährt Standortzugriff, während die App im Vordergrund ist. | Nein. Auf Android ist der Hintergrund-Standortzugriff für die Geofence-Überwachung erforderlich. |
| **Immer erlauben** | Gewährt kontinuierlichen Standortzugriff, auch im Hintergrund. Auf Android 10 und höher erfordert dies eine separate Aufforderung, nachdem die anfängliche Berechtigung „Bei Verwendung der App“ gewährt wurde. | Ja. Dies ist für Geofencing auf Android erforderlich. |
| **Nicht erlauben** | Verweigert jeglichen Standortzugriff. Auf Android 13 und höher blockiert das Betriebssystem weitere In-App-Aufforderungen, wenn Nutzer:innen die Standortaufforderung zweimal ablehnen. | Nein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungsstufen" }

{% endtab %}
{% endtabs %}

### Genauer versus ungefährer Standort {#precise-versus-approximate-location}

Auf iOS 14+ und Android 12+ können Nutzer:innen zwischen genauem und ungefährem Standort wählen.

| Einstellung | Genauigkeit | Auswirkung auf Geofencing |
|---|---|---|
| **Genauer Standort (ein)** | Genauigkeit im Bereich von 5 bis 50 Metern, unter Verwendung von GPS, WLAN und Mobilfunk-Triangulation. | Geofences funktionieren wie erwartet. Empfohlen für alle Geofence-basierten Anwendungsfälle. |
| **Ungefährer Standort (aus)** | Genauigkeit von etwa 3 Quadratkilometern (ungefähr 1 Quadratmeile). Das Gerät gibt einen allgemeinen Bereich statt exakter Koordinaten zurück. | Geofences werden nicht zuverlässig ausgelöst. Das Gerät kann nicht genau bestimmen, ob sich Nutzer:innen innerhalb oder außerhalb einer Geofence-Grenze befinden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Genauer versus ungefährer Standort" }

{% alert important %}
Damit Geofencing zuverlässig funktioniert, müssen Nutzer:innen den genauen Standort aktivieren. Nehmen Sie diese Anleitung in Ihre Standortberechtigungs-Primer-Nachrichten auf, damit Nutzer:innen verstehen, warum der genaue Standort wichtig ist.
{% endalert %}

## Einen Standortberechtigungs-Primer einrichten {#setting-up-a-location-permission-primer}

Ein Standortberechtigungs-Primer ist eine In-App-Nachricht, die den Wert der Standortdatenfreigabe erklärt, bevor Nutzer:innen die native Betriebssystem-Berechtigungsaufforderung sehen. Da die native Standortaufforderung nur einmal (auf iOS) oder eine begrenzte Anzahl von Malen (auf Android) angezeigt werden kann, erhöht das vorherige Priming der Nutzer:innen die Opt-in-Raten.

### Schritt 1: Mit Ihrem Entwicklungsteam zusammenarbeiten {#step-1-work-with-your-development-team}

Da Braze In-App-Nachrichten keine integrierte Button-Aktion zum Aufrufen der nativen Standortberechtigungsaufforderung enthalten, muss Ihr Entwicklungsteam die Standortberechtigungen auf der Geräteseite handhaben. Bevor Sie die In-App-Nachricht in Braze erstellen, koordinieren Sie sich mit Ihrem Entwicklungsteam, um Deeplinks einzurichten, die Ihre In-App-Nachricht aufrufen kann. Die spezifische Implementierung hängt von der Architektur Ihrer App ab, aber gängige Ansätze umfassen:

- Einen Deeplink, der die native Standortberechtigungsaufforderung innerhalb Ihrer App auslöst.
- Einen Deeplink, der die Standorteinstellungsseite der App in den Betriebssystemeinstellungen des Geräts öffnet, was nützlich ist, um Nutzer:innen erneut aufzufordern, die zuvor ihre Berechtigungen verweigert oder eingeschränkt haben.

Weitere Informationen zu Deeplinks finden Sie unter [Deeplinking zu In-App-Inhalten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls). Plattformspezifische Anleitungen zur Standort- und Geofence-Integration finden Sie unter [Geofences]({{site.baseurl}}/developer_guide/geofences) im Entwicklerhandbuch.

### Schritt 2: Die Standort-Primer-In-App-Nachricht erstellen {#step-2-build-the-location-primer-in-app-message}

Erstellen Sie eine In-App-Nachricht-Campaign, die den Wert des Standortzugriffs erklärt. Alle In-App-Nachrichtentypen unterstützen dieses Opt-in, einschließlich Drag-and-Drop.

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Kampagne erstellen** > **In-App-Nachricht**.
2. Wählen Sie einen Nachrichtentyp und ein Layout. Ein **Modal**- oder **Full**-Layout gibt Ihnen mehr Platz, um die Vorteile zu erläutern.
3. Verfassen Sie eine Nachricht, die klar erklärt, warum der Standortzugriff für die Nutzer:innen von Vorteil ist. Zum Beispiel:
    - „Aktivieren Sie den Standort, um über Angebote in Ihrer Nähe benachrichtigt zu werden.“
    - „Schalten Sie den Standort ein, damit wir Sie informieren können, wenn Ihre Bestellung zur Abholung in Ihrem nächsten Shop bereit ist.“
4. Fügen Sie einen primären Call-to-Action-Button hinzu (z. B. **Standort aktivieren**) und setzen Sie das Klickverhalten auf **Deeplink in App**, wobei Sie den Deeplink verwenden, den Ihr Entwicklungsteam erstellt hat, um die native Standortaufforderung auszulösen.
5. Fügen Sie einen sekundären Button hinzu (z. B. **Nicht jetzt**), der die Nachricht schließt.

### Schritt 3: Die richtige Zielgruppe ansprechen {#step-3-target-the-right-audience}

Für beste Ergebnisse zeigen Sie den Standort-Primer, wenn Nutzer:innen engagiert sind und wahrscheinlich einen Mehrwert in der Standortfreigabe sehen.

- **Sprechen Sie Nutzer:innen an, die noch keinen Standortzugriff gewährt haben.** Arbeiten Sie mit Ihrem Entwicklungsteam zusammen, um die beste Methode zu bestimmen, Nutzer:innen basierend auf ihrem Standortberechtigungsstatus zu tracken und zu segmentieren.
- **Zeigen Sie den Primer nach einer hochwertigen Aktion,** wie dem Abschluss eines Kaufs, dem Speichern eines Shops als Favorit oder dem Durchsuchen von Ereignissen in der Nähe. Nutzer:innen sind eher bereit, sich anzumelden, wenn sie den Vorteil verstehen.
- **Vermeiden Sie es, den Primer beim ersten Start zu zeigen.** Warten Sie, bis Nutzer:innen genug Mehrwert aus der App erfahren haben, um ein personalisierteres Erlebnis zu wünschen.

### Schritt 4: Die empfohlene Berechtigungsstufe fördern {#step-4-encourage-the-recommended-permission-level}

Ihre Primer-Nachrichten sollten Nutzer:innen ermutigen, die Berechtigungsstufe zu gewähren, die Geofencing ermöglicht:

- **Auf iOS** ermutigen Sie Nutzer:innen, mindestens **Bei Verwendung der App erlauben** auszuwählen. iOS kann Nutzer:innen später von sich aus auffordern, auf **Immer erlauben** zu upgraden. Sie können auch mit einer separaten Campaign nachfassen, um zu erklären, warum „Immer erlauben“ das beste Erlebnis bietet.
- **Auf Android** ermutigen Sie Nutzer:innen, **Immer erlauben** zu gewähren. Auf Android 10 und höher müssen Nutzer:innen zuerst „Bei Verwendung der App“ gewähren und dann „Immer erlauben“ in einer separaten Folgeaufforderung gewähren. Führen Sie sie durch beide Schritte.

In beiden Fällen erinnern Sie Nutzer:innen daran, **Genauer Standort** für das beste Erlebnis aktiviert zu lassen.

## Nutzer:innen zu den Betriebssystemeinstellungen weiterleiten {#redirecting-users-to-os-settings}

Wenn Nutzer:innen zuvor den Standortzugriff verweigert oder eine eingeschränkte Berechtigung ausgewählt haben, können Sie die native Aufforderung auf den meisten Betriebssystemversionen nicht erneut aus der App heraus auslösen. Leiten Sie sie stattdessen weiter, um ihre Berechtigungen in den Geräteeinstellungen zu Update or aktualisieren or aktualisieren.

Verwenden Sie einen Deeplink in einer benutzerdefinierten [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), um Nutzer:innen zur Standorteinstellungsseite der App im Betriebssystem zu navigieren. Ihr Entwicklungsteam kann einen Deeplink dafür als Teil der Standortberechtigungsbehandlung Ihrer App einrichten (siehe [Schritt 1](#step-1-work-with-your-development-team)).

Beachten Sie beim Erstellen dieser In-App-Nachricht Folgendes:

- **Wann anzeigen:** Sprechen Sie Nutzer:innen an, die die Berechtigung „Bei Verwendung der App“ haben, wenn Sie „Immer erlauben“ benötigen, oder Nutzer:innen, die zuvor den Standortzugriff verweigert haben.
- **Nachrichtenbeispiel:** „Um das Beste aus standortbasierten Features herauszuholen, Update or aktualisieren or aktualisieren Sie Ihre Standorteinstellungen auf „Immer erlauben“. Tippen Sie unten, um zu den Einstellungen zu gelangen."

{% alert tip %}
Sie können diese In-App-Nachricht an jedem Punkt der User Journey auslösen – nach einem Kauf, beim Durchsuchen von Inhalten in der Nähe oder als Teil eines Canvas-Flows. Seien Sie selektiv beim erneuten Auffordern: Beschränken Sie diese Campaigns auf loyale oder stark engagierte Nutzer:innen, um Opt-in-Müdigkeit zu vermeiden.
{% endalert %}

## Beispielstrategien für Standort-Priming {#example-location-priming-strategies}

### „Bei Verwendung der App“-Primer {#while-using-the-app-primer}

Eine Einzelhandels-App zeigt eine modale In-App-Nachricht an, nachdem Nutzer:innen einen Shop als Favorit gespeichert haben:

- **Überschrift:** „Erhalten Sie Benachrichtigungen über Angebote im Shop“
- **Text:** „Schalten Sie den Standort ein, damit wir Ihnen exklusive Angebote senden können, wenn Sie in der Nähe Ihrer Lieblingsshops sind. Auf Ihren Standort wird nur bei Verwendung der App zugegriffen.“
- **CTA:** **Standort aktivieren** verlinkt per Deeplink zur nativen Standortberechtigungsaufforderung
- **Schließen:** **Vielleicht später** schließt die Nachricht

Dieser Ansatz ist effektiv, weil Nutzer:innen bereits Interesse an einem bestimmten Shop gezeigt haben, was einen natürlichen Kontext für die Standortberechtigungsanfrage schafft.

### „Immer erlauben“-Nachfassung {#always-allow-follow-up}

Nachdem Nutzer:innen die Berechtigung „Bei Verwendung der App“ gewährt haben, zeigen Sie eine Nachfass-In-App-Nachricht während der nächsten Sitzung:

- **Überschrift:** „Verpassen Sie nie ein Angebot in der Nähe“
- **Text:** „Update or aktualisieren or aktualisieren Sie Ihre Standorteinstellungen auf „Immer“, damit wir Sie über Angebote benachrichtigen können, auch wenn Sie die App nicht nutzen. Wir senden nur relevante Benachrichtigungen, wenn Sie in der Nähe teilnehmender Standorte sind."
- **CTA:** **Einstellungen Update or aktualisieren or aktualisieren** verlinkt per Deeplink zur Standorteinstellungsseite der App im Betriebssystem
- **Schließen:** **Aktuelle Einstellungen beibehalten** schließt die Nachricht

Diese Nachfassung gibt Nutzer:innen Kontext, warum das Upgrade or upgraden auf „Immer erlauben“ zusätzlichen Mehrwert über die anfängliche Berechtigungsstufe hinaus bietet.

## Geofences manuell erstellen {#manually-create-geofences}

### Schritt 1: Ein Geofence-Set erstellen {#step-1-create-a-geofence-set}

Um einen Geofence zu erstellen, erstellen Sie zuerst ein Geofence-Set.

1. Gehen Sie im Braze-Dashboard zu **Audience** > **Locations**.
2. Wählen Sie **Create Geofence Set**.
3. Geben Sie unter **Set name** einen Namen für Ihr Geofence-Set ein.
4. (Optional) Fügen Sie Tags hinzu, um Ihr Set zu filtern.

### Schritt 2: Die Geofences hinzufügen {#step-2-add-the-geofences}

Fügen Sie als Nächstes Geofences zu Ihrem Geofence-Set hinzu.

1. Wählen Sie **Draw Geofence**, um den Kreis auf der Karte zu klicken und zu ziehen. Wiederholen Sie den Vorgang, um bei Bedarf weitere Geofences zu Ihrem Set hinzuzufügen.
2. (Optional) Wählen Sie **Edit** und ersetzen Sie die Geofence-Beschreibung durch einen Namen.
3. (Optional) Wählen Sie **Show Advanced Settings** und verwenden Sie diese Einstellungen, um zu steuern, wie Geofence-Analytics aufgezeichnet werden:
  - Wählen Sie **Enable Analytics for Enter** und **Enable Analytics for Exit**, um Eintritts- und Austrittsaktivitäten in der [`USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED`-SQL-Tabelle]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) für Berichte und Analysen zu protokollieren.
  - Konfigurieren Sie einen Cooldown-Zeitraum, um festzulegen, wie viele Sekunden vergehen müssen, bevor dieselben Nutzer:innen ein weiteres Eintritts- oder Austrittsereignis für diesen Geofence auslösen können. Wenn Sie keinen Cooldown festlegen, beträgt der Standard sechs Stunden.
  - Verwenden Sie **Android Notification Responsiveness**, um die maximale Verzögerung in Sekunden festzulegen, die Android-Geräte bei der Zustellung von Eintritts- oder Austrittsereignissen an Ihre App verwenden.

{: start="4" }
4. Wählen Sie **Save Geofence Set**, um zu speichern.

{% alert tip %}
Erstellen Sie Geofences mit einem Radius von mindestens 200 Metern für optimale Funktionalität. Weitere Informationen finden Sie unter [Geofence-Best-Practices](#geofence-best-practices).
{% endalert %}

![Ein Geofence-Set mit zwei Geofences „EastCoastGreaterNY“ und „WesternRegion“ mit zwei Kreisen auf der Karte.]({% image_buster /assets/img/geofence_example.png %})

## Geofences per Massenupload hochladen {#creating-geofence-sets-via-bulk-upload}

Sie können Geofences als GeoJSON-Objekt vom Typ `FeatureCollection` in großen Mengen hochladen. Jeder Geofence ist ein `Point`-Geometrietyp in der Feature-Sammlung. Die Eigenschaften für jedes Feature erfordern einen `radius`-Schlüssel und einen optionalen `name`-Schlüssel für jeden Geofence.

Um Ihre JSON-Datei hochzuladen, wählen Sie **More** > **Upload JSON**.

Beachten Sie beim Erstellen Ihrer Geofences die folgenden Details:

- Der `coordinates`-Wert im GeoJSON ist als `[Longitude, Latitude]` formatiert.
- Der maximale Geofence-Radius, der hochgeladen werden kann, beträgt 10.000 Meter (etwa 10 Kilometer oder 6,2 Meilen).

### Beispiel {#example}

Das folgende Beispiel zeigt das korrekte GeoJSON-Format für die Angabe von zwei Geofences: einen für die Braze-Zentrale in NYC und einen für die Freiheitsstatue südlich von Manhattan.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.9853689, 40.7434683]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Geofence-Ereignisse verwenden {#using-geofence-events}

Nachdem Sie Ihre Geofences konfiguriert haben, können Sie sie verwenden, um Ihre Kommunikation mit Nutzer:innen zu verbessern und zu bereichern.

### Campaigns und Canvase Trigger or triggern or triggern {#triggering-campaigns-and-canvases}

Um Geofence-Daten als Teil von Campaign- und Canvas-Trigger or triggern or triggern zu verwenden, wählen Sie **Aktionsbasierte Zustellung** als Zustellungsmethode. Fügen Sie dann eine Triggeraktion **Trigger or triggern a Geofence** hinzu. Wählen Sie schließlich das Geofence-Set und die Geofence-Übergangsereignistypen für Ihre Nachricht. Sie können Nutzer:innen auch mithilfe von Geofence-Ereignissen durch einen Canvas voranbringen.

![Eine aktionsbasierte Campaign mit einem Geofence, die ausgelöst wird, wenn Nutzer:innen deutsche Flughäfen betreten.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Nachrichten personalisieren {#personalizing-messages}

Um Geofence-Daten zur Personalisierung einer Nachricht zu verwenden, können Sie die folgende Liquid-Personalisierungssyntax nutzen:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Geofence-Sets Update or aktualisieren or aktualisieren {#updating-geofence-sets}

Das Braze SDK or Software-Development-Kit fordert Geofences nur einmal pro Tag beim Sitzungsstart an. Wenn Sie nach dem Sitzungsstart Änderungen an den Geofence-Sets vornehmen, müssen Sie 24 Stunden ab dem Zeitpunkt warten, an dem die Sets erstmals heruntergeladen wurden, um das aktualisierte Set zu erhalten.

{% alert note %}
Wenn die Geofences nicht lokal auf das Gerät geladen werden, können Nutzer:innen den Geofence nicht auslösen, selbst wenn sie das Gebiet betreten.
{% endalert %}

## Geofence-Best-Practices {#geofence-best-practices}

### Geofence-Konfiguration {#geofence-configuration}

- Verwenden Sie einen Radius von 200 Metern oder mehr für zuverlässiges Trigger or triggern or triggern.
- Vermeiden Sie es, Geofences einzurichten, die sich überlappen oder ineinander verschachtelt sind, da dies Probleme beim Trigger or triggern or triggern verursachen kann.
- Ein Geofence kann ein Eintrittsereignis nur einmal alle sechs Stunden auslösen. Dieser Cooldown-Zeitraum wird lokal durchgesetzt. Wenn Nutzer:innen die App deinstallieren oder App-Daten löschen, werden alle Cooldowns zurückgesetzt.
- Nicht mehr als 20 Geofences insgesamt können auf einem Gerät gespeichert werden. Wenn Nutzer:innen für mehr als 20 berechtigt sind, lädt Braze die nächstgelegenen Standorte basierend auf der Nähe beim Sitzungsstart herunter.
- Braze sendet nur Geofences innerhalb eines Radius von 2.000 Kilometern um die Nutzer:innen an das Gerät.

### Geräteanforderungen {#device-requirements}

- Die Nutzer:innen Ihrer Anwendung müssen Standortberechtigungen erteilen. Weitere Informationen finden Sie im Abschnitt [Standortberechtigungen](#location-permissions).

{% alert note %}
Die grundlegende SDK or Software-Development-Kit-Integration aktiviert nur Standort-Tracking. Geofencing erfordert zusätzliche Einrichtungsschritte sowohl für iOS als auch für Android. Details finden Sie unter [Geofences]({{site.baseurl}}/developer_guide/geofences) im Entwicklerhandbuch.
{% endalert %}

Sie können Geofences auch mit Braze-Technologie-Partnern verwenden, wie [Radar]({{site.baseurl}}/partners/message_personalization/location/radar) und [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare).

## Unterschiede zwischen Geofences und Standort-Tracking {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie genau sind Braze-Geofences? {#how-accurate-are-braze-geofences}

Braze-Geofences verwenden eine Kombination aller auf einem Gerät verfügbaren Standortanbieter, um den Standort der Nutzer:innen zu triangulieren, einschließlich WLAN, GPS und Mobilfunkmasten.

Die typische Genauigkeit liegt im Bereich von 20 bis 50 Metern, und die bestmögliche Genauigkeit liegt im Bereich von 5 bis 10 Metern. In ländlichen Gebieten kann die Genauigkeit erheblich abnehmen und möglicherweise bis zu mehrere Kilometer betragen. Erstellen Sie Geofences mit größeren Radien in ländlichen Gebieten.

Die Genauigkeit hängt auch davon ab, ob Nutzer:innen den genauen Standort aktiviert haben. Bei nur ungefährem Standort sinkt die Genauigkeit auf etwa 3 Quadratkilometer, was Geofences unzuverlässig macht. Weitere Informationen finden Sie unter [Genauer versus ungefährer Standort](#precise-versus-approximate-location).

### Wie wirken sich Geofences auf die Akkulaufzeit aus? {#how-do-geofences-affect-battery-life}

Braze-Geofencing verwendet den nativen Geofence-Systemdienst auf iOS und Android. Er ist so abgestimmt, dass er intelligent zwischen Genauigkeit und Energieverbrauch abwägt, die Akkulaufzeit schont und die Performance verbessert, wenn sich der zugrunde liegende Dienst verbessert.

### Wann sind Geofences aktiv? {#when-are-geofences-active}

Braze-Geofences funktionieren rund um die Uhr, auch wenn Ihre App geschlossen ist. Sie werden aktiv, sobald sie definiert und in das Braze-Dashboard hochgeladen werden. Geofences können jedoch nicht funktionieren, wenn Nutzer:innen das Standort-Tracking deaktiviert haben.

Damit Geofences funktionieren, müssen Nutzer:innen die Standortdienste auf ihrem Gerät aktiviert haben und Ihrer App die erforderliche Standortberechtigungsstufe gewährt haben. Weitere Informationen finden Sie unter [Standortberechtigungen verstehen](#understanding-location-permissions).

### Werden Geofence-Daten in Nutzerprofilen gespeichert? {#is-geofence-data-stored-in-user-profiles}

Nein, Braze speichert keine Geofence-Daten in Nutzerprofilen. Geofences werden von den Standortdiensten von Apple und Google überwacht, und Braze wird nur benachrichtigt, wenn Nutzer:innen einen Geofence auslösen. Zu diesem Zeitpunkt verarbeitet Braze alle zugehörigen Trigger or triggern-Campaigns.

### Kann ich einen Geofence innerhalb eines Geofence einrichten? {#can-i-set-up-a-geofence-within-a-geofence}

Als Best Practice sollten Sie es vermeiden, Geofences einzurichten, die sich gegenseitig überlappen, da dies Probleme beim Trigger or triggern or triggern von Benachrichtigungen verursachen kann.

### Was passiert, wenn Nutzer:innen den Standortzugriff verweigern? {#what-if-a-user-denies-location-access}

Ihr Entwicklungsteam kann einen Deeplink einrichten, der die Standorteinstellungsseite der App im Betriebssystem öffnet, wo Nutzer:innen ihre Berechtigungen Update or aktualisieren or aktualisieren können. Sie können diesen Deeplink in einer benutzerdefinierten In-App-Nachricht an jedem Punkt der User Journey verwenden. Seien Sie selektiv, wann Sie diese Nachricht anzeigen – sprechen Sie Nutzer:innen an, die engagiert sind oder eine hochwertige Aktion durchgeführt haben, um die Chance auf ein Opt-in zu erhöhen. Weitere Informationen finden Sie unter [Nutzer:innen zu den Betriebssystemeinstellungen weiterleiten](#redirecting-users-to-os-settings).