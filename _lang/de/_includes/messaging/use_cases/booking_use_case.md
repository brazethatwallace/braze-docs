# Anwendungsfall: Buchungserinnerungs-E-Mail-System {#use-case-booking-reminder-email-system}

> Braze ist eine umfassende Customer-Engagement-Plattform, die so konzipiert ist, dass sie in hohem Maße programmgesteuert werden kann. In diesem Anwendungsfall zeigen wir Ihnen einige Möglichkeiten, wie Sie die Funktionen von Braze in Anwendungsfälle integrieren können, die an der Schnittstelle zwischen Produkt und Marketing liegen – wie z. B. Buchungssysteme.

Dieser Anwendungsfall zeigt, wie Sie die Features von Braze nutzen können, um einen E-Mail-Messaging-Dienst für Buchungserinnerungen aufzubauen. Der Dienst ermöglicht es Nutzer:innen, Termine zu buchen, und sendet ihnen Erinnerungen an bevorstehende Termine. Obwohl in diesem Anwendungsfall E-Mail-Nachrichten verwendet werden, können Sie Nachrichten in einem beliebigen oder mehreren Kanälen auf der Grundlage eines einzigen Updates eines Nutzerprofils versenden.

Weitere Vorteile der Erstellung dieses Dienstes sind:
- Gesendete Nachrichten werden vollständig getrackt und in Berichten erfasst.
- Nicht-technische Unternehmensnutzer:innen können den Inhalt von Nachrichten aktualisieren.
- Nachrichten berücksichtigen den Opt-in- und Opt-out-Status von Nutzerprofilen gemäß der Campaign-Konfiguration.
- Sie können sowohl Buchungsdaten als auch Daten zur Nachrichteninteraktion verwenden, um Nutzer:innen zu segmentieren und für zusätzliche Nachrichten anzusprechen. Beispielsweise können Sie diejenigen, die die erste Erinnerungsnachricht nicht öffnen, mit einer zusätzlichen Erinnerung vor ihrem Termin erneut ansprechen.

Folgen Sie diesen Schritten, um diesen Anwendungsfall umzusetzen:
1. [Anstehende Buchungsdaten in ein Braze-Nutzerprofil schreiben](#step-1)
2. [Buchungserinnerung einrichten und starten](#step-2)
3. [Aktualisierte Buchungen und Stornierungen verarbeiten](#step-3)

## 1. Schritt: Anstehende Buchungsdaten in ein Braze-Nutzerprofil schreiben {#step-1}

Verwenden Sie den Braze-Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um bei jeder Buchung ein [verschachteltes angepasstes Attribut]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support) in ein Nutzerprofil zu schreiben. Stellen Sie sicher, dass das verschachtelte angepasste Attribut alle Informationen enthält, die Sie zum Versenden und Personalisieren der Erinnerungsnachricht benötigen. In diesem Anwendungsfall nennen wir das verschachtelte angepasste Attribut „trips“.

### Buchung hinzufügen {#add-booking}

Wenn ein:e Nutzer:in eine Buchung erstellt, verwenden Sie die folgende Struktur für das Array von Objekten, um die Daten über den Endpunkt `/users/track` an Braze zu senden.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

Das verschachtelte angepasste Attribut „trips“ wird im Nutzerprofil wie folgt angezeigt.

![Zwei verschachtelte angepasste Attribute für eine Reise nach London und eine Reise nach Sydney.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### Buchung aktualisieren {#update-booking}
Wenn ein:e Nutzer:in eine Buchung aktualisiert, verwenden Sie die folgende Struktur für das Array von Objekten, um die Daten über den Endpunkt `/users/track` an Braze zu senden.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### Buchung entfernen {#remove-booking}

{% tabs %}
{% tab /users/track endpoint %}
#### Daten über den Endpunkt `/users/track` senden {#send-data-through-the-userstrack-endpoint}
Wenn ein:e Nutzer:in eine Buchung löscht, verwenden Sie die folgende Struktur für das Array von Objekten, um die Daten über den Endpunkt `/users/track` an Braze zu senden.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### Verschachtelte Attribute über das SDK in Nutzerprofile schreiben {#write-nested-attributes-to-user-profiles-through-the-sdk}

Wenn Sie Terminbuchungen über Ihre App, Website oder beides erfassen und diese Daten direkt in ein Nutzerprofil schreiben möchten, können Sie das Braze SDK verwenden, um diese Daten zu übertragen. Hier ist ein Beispiel mit dem Web SDK:

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

Braze entfernt die angegebene Buchung aus dem verschachtelten angepassten Attribut im Nutzerprofil und zeigt alle verbleibenden Buchungen an.

![Ein verschachteltes angepasstes Attribut für eine Reise nach London.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## 2. Schritt: Buchungserinnerung einrichten und starten {#step-2}

### Schritt 2a: Zielgruppe erstellen {#step-2a-create-a-target-audience}
Erstellen Sie eine Zielgruppe für den Empfang von Erinnerungen mithilfe einer Segmentierung nach mehreren Kriterien. Wenn Sie beispielsweise zwei Tage vor dem Buchungsdatum eine Erinnerung senden möchten, wählen Sie Folgendes aus:

- Ein Startdatum **in mehr als 1 Tag** und
- Ein Startdatum **in weniger als 2 Tagen**

![Ein verschachteltes angepasstes Attribut „trips“ mit Kriterien für ein Startdatum, das mehr als einen Tag und weniger als zwei Tage entfernt ist.]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### Schritt 2b: Nachricht erstellen {#step-2b-create-your-message}

Erstellen Sie die Erinnerungs-E-Mail, indem Sie die Schritte unter [E-Mail mit angepasstem HTML erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor) befolgen. Verwenden Sie Liquid, um die Nachricht mit Daten aus dem von Ihnen erstellten angepassten Attribut („trips“) zu personalisieren, wie in diesem Beispiel.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}}
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### Schritt 2c: Campaign starten {#step-2c-launch-your-campaign}

Starten Sie die Campaign für die Erinnerungs-E-Mail. Jedes Mal, wenn Braze das angepasste Attribut „trips“ erhält, plant Braze eine Nachricht entsprechend den Daten, die im jeweiligen Buchungsobjekt enthalten sind.

## 3. Schritt: Aktualisierte Buchungen und Stornierungen verarbeiten {#step-3}

Da Sie nun Erinnerungsnachrichten versenden, können Sie auch Bestätigungsnachrichten einrichten, die gesendet werden, wenn Buchungen aktualisiert oder storniert werden.

### Schritt 3a: Aktualisierte Daten senden {#step-3a-send-updated-data}

{% tabs %}
{% tab /users/track %}

#### Daten über den Endpunkt `/users/track` senden
Verwenden Sie den Braze-Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um ein angepasstes Event zu senden, wenn ein:e Nutzer:in eine Buchung aktualisiert oder storniert. Geben Sie in diesem Event die erforderlichen Daten als Event-Eigenschaften an, die die Änderung bestätigen.

Nehmen wir an, dass in diesem Anwendungsfall ein:e Nutzer:in das Datum der Reise nach Sydney aktualisiert hat. Das Event würde wie folgt aussehen:

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### Angepasste Events über das SDK senden

Senden Sie angepasste Events über das SDK an das Nutzerprofil. Wenn Sie beispielsweise das Web SDK verwenden, könnten Sie Folgendes senden:

{% raw %}
```json
braze.logCustomEvent("trip_updated", {
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Schritt 3b: Bestätigungsnachricht für das Update erstellen {#step-3b-create-a-message-to-confirm-the-update}

Erstellen Sie eine [aktionsbasierte Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), um der bzw. dem Nutzer:in eine Bestätigung der aktualisierten Buchung zu senden. Sie können [Liquid verwenden, um Event-Eigenschaften als Template einzusetzen]({{site.baseurl}}/user_guide/data/custom_data/custom_events), die den Namen, die alte Zeit und die neue Zeit der Buchung (oder nur den Namen bei einer Stornierung) in der Nachricht selbst wiedergeben.

Sie könnten beispielsweise die folgende Nachricht verfassen:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Schritt 3c: Nutzerprofil entsprechend dem Update anpassen {#step-3c-modify-the-user-profile-to-reflect-the-update}

Um die Buchungserinnerungen aus [Schritt 1](#step-1) und [Schritt 2](#step-2) auf Basis der aktuellsten Daten zu versenden, aktualisieren Sie abschließend die verschachtelten angepassten Attribute, um die Änderung oder Stornierung der Buchung widerzuspiegeln.

#### Aktualisierte Buchung {#updated-booking}

Wenn die bzw. der Nutzer:in in diesem Anwendungsfall die Reise nach Sydney aktualisiert hat, verwenden Sie den Endpunkt `/users/track`, um das Datum mit einem Aufruf wie diesem zu ändern:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### Stornierte Buchung {#cancelled-booking}

Wenn die bzw. der Nutzer:in in diesem Anwendungsfall die Reise nach Sydney storniert hat, senden Sie den folgenden Aufruf an den Endpunkt `/users/track`:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

Nach dem Versenden dieser Aufrufe und dem Update des Nutzerprofils spiegeln die Buchungserinnerungen die aktuellsten Daten zu den Buchungsterminen der bzw. des Nutzer:in wider.