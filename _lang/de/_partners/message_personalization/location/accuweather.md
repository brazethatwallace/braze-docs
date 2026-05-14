---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und AccuWeather, einer Wetter-API, die Sie zur Personalisierung Ihrer Marketingkampagnen nutzen können."
page_type: partner
search_tag: Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) ist ein Medienunternehmen, das weltweit Dienste zur Wettervorhersage anbietet. Mit AccuWeather können Sie Ihre Marketingkampagnen anreichern und personalisieren sowie Übersetzungen durch den Einsatz von Braze [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) automatisieren.

_Diese Integration wird von AccuWeather gepflegt._

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| AccuWeather API-Schlüssel | Kontaktieren Sie Ihren AccuWeather Account Manager, um kompatible API-Schlüssel für Ihre Anfrage-URLs zu erhalten.<br><br>Weitere Anweisungen finden Sie auf der Seite [AccuWeather Enterprise API](https://apidev.accuweather.com/developers/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Verfügbare AccuWeather APIs {#available-accuweather-apis}

Im Folgenden finden Sie die AccuWeather APIs, die Sie in Ihren Braze Campaigns und Canvases referenzieren können.

| API | Beschreibung |
|---|---|
| [Locations](https://apidev.accuweather.com/developers/locationsAPIguide) | Rufen Sie einen Standortschlüssel für Ihren gewünschten Standort ab. Verwenden Sie den Standortschlüssel, um Wetterdaten von der Forecast- oder Current-Conditions-API abzurufen. |
| [Forecast](https://apidev.accuweather.com/developers/forecastsAPIguide) | Erhalten Sie Vorhersageinformationen für einen bestimmten Standort. |
| [Current Conditions](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | Rufen Sie Daten zu den aktuellen Bedingungen für einen bestimmten Standort ab. |
| [Indices](https://apidev.accuweather.com/developers/indicesApiGuide) | Erhalten Sie tägliche Indexwerte für einen bestimmten Standort. Die Verfügbarkeit des Index variiert je nach Standort. |
| [Weather Alarms](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | Erhalten Sie Wetteralarme für einen bestimmten Standort. AccuWeather Weather Alarms werden anhand der täglichen Vorhersagen für einen Standort ermittelt. Ein Alarm besteht für einen Standort, wenn die Wettervorhersage [bestimmte Schwellenwerte](https://apidev.accuweather.com/developers/weatheralarms) erreicht oder überschreitet. |
| [Alerts](https://apidev.accuweather.com/developers/alertsApiGuide) | Erhalten Sie Unwetterwarnungen von offiziellen staatlichen Wetterdiensten und führenden globalen Wetterwarnungsanbietern. |
| [Imagery](https://apidev.accuweather.com/developers/imageryAPIguide) | Rufen Sie Radar- und Satellitenbilder ab. |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | Erhalten Sie die aktuelle Position, frühere Positionen und Vorhersagen für tropische Wirbelstürme weltweit. |
| [Translations](https://apidev.accuweather.com/developers/translationsApiGuide) | Erhalten Sie eine Liste der verfügbaren Sprachen. Erhalten Sie Übersetzungen für bestimmte Gruppen von Phrasen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare AccuWeather APIs" }

## Connected-Content-Beispiel {#connected-content-example}

Das folgende Beispiel zeigt einen Connected-Content-Aufruf, der zwei verschiedene Arten von Nachrichten basierend auf den aktuellen Wetterbedingungen der Postleitzahl einer Nutzer:in in den USA anzeigt. Die AccuWeather-Endpunkte für Locations und Current Conditions werden verwendet.
{% raw %}

```liquid
{% connected_content http:///dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}

{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}

{% if {{local_weather[0].WeatherText}} == 'Cloudy' %}
No sunscreen needed :)
{% elsif {{local_weather[0].WeatherText}} == 'Rain' %}
It's raining! Grab an umbrella!
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

![Eine Connected-Content-Push-Nachricht mit dem Text „It's raining! Grab an Umbrella!“, angezeigt auf einem Android-Gerät]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){: style="max-width:40%"}

Eine Aufschlüsselung der beiden Connected-Content-Aufrufe finden Sie in den folgenden Beispielen.

{% tabs %}
{% tab Locations %}
#### Locations-API-Beispiel {#locations-api-example}

{% raw %}
Innerhalb des ersten `connected_content`-Tags wird eine GET-Anfrage an die [Locations API](https://apidev.accuweather.com/developers/locationsAPIguide) gestellt. Für dieses Beispiel können Sie alternativ die `{{${city}}}` der Nutzer:in nutzen, wenn Sie kein angepasstes Attribut für die Postleitzahl haben.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Hier sehen Sie ein Beispiel dafür, was AccuWeather als JSON-Objekt zurückgibt:

```json
[
  {
    "Version": 1,
    "Key": "41333_PC",
    "Type": "PostalCode",
    "Rank": 35,
    "LocalizedName": "Seattle",
    "EnglishName": "Seattle",
    "PrimaryPostalCode": "98102",
    "Region": {
      "ID": "NAM",
      "LocalizedName": "North America",
      "EnglishName": "North America"
    },
    "Country": {
      "ID": "US",
      "LocalizedName": "United States",
      "EnglishName": "United States"
    },
    "AdministrativeArea": {
      "ID": "WA",
      "LocalizedName": "Washington",
      "EnglishName": "Washington",
      "Level": 1,
      "LocalizedType": "State",
      "EnglishType": "State",
      "CountryID": "US"
    },
    "TimeZone": {
      "Code": "PDT",
      "Name": "America/Los_Angeles",
      "GmtOffset": -7.0,
      "IsDaylightSaving": true,
      "NextOffsetChange": "2018-11-04T09:00:00Z"
    },
    "GeoPosition": {
      "Latitude": 47.636,
      "Longitude": -122.327,
      "Elevation": {
        "Metric": {
          "Value": 26.0,
          "Unit": "m",
          "UnitType": 5
        },
        "Imperial": {
          "Value": 85.0,
          "Unit": "ft",
          "UnitType": 0
        }
      }
    },
    "IsAlias": false,
    "ParentCity": {
      "Key": "351409",
      "LocalizedName": "Seattle",
      "EnglishName": "Seattle"
    },
    "SupplementalAdminAreas": [
      {
        "Level": 2,
        "LocalizedName": "King",
        "EnglishName": "King"
      }
    ],
    "DataSets": [
      "Alerts",
      "DailyAirQualityForecast",
      "DailyPollenForecast",
      "ForecastConfidence",
      "MinuteCast"
    ]
  }
]
```

Die „Key“-ID ist eine nützliche Variable, da sie in der zweiten GET-Anfrage verwendet wird.
Dieses JSON-Objekt kann in einer lokalen Variable `location_info` gespeichert werden, indem Sie `:save location_info` nach der URL angeben.
{% endtab %}
{% tab Current conditions %}

#### Current-Conditions-API-Beispiel {#current-conditions-api-example}

Für den zweiten `connected_content`-Tag wird eine GET-Anfrage an die [Current Conditions API](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) gestellt. Der **Standortschlüssel** muss der Anfrage-URL hinzugefügt werden. Hier ist ein Beispiel für den `connected_content`-Tag:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Hier ist das zurückgegebene JSON-Objekt:

```json
[
  {
    "LocalObservationDateTime": "2018-04-10T09:35:00-07:00",
    "EpochTime": 1523378100,
    "WeatherText": "Rain",
    "WeatherIcon": 18,
    "IsDayTime": true,
    "Temperature": {
      "Metric": {
        "Value": 11.0,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 52.0,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "MobileLink": "http://m.accuweather.com/en/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us",
    "Link": "http://www.accuweather.com/en/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us"
  }
]
```

Wie im `connected_content`-Tag zu sehen ist, wird das JSON-Objekt in einer lokalen Variable `local_weather` gespeichert, indem `:save local_weather` nach der URL hinzugefügt wird.

Sie können testen, wie die Ausgabe von [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) aussehen soll, indem Sie auf `{{local_weather[0].WeatherText}}` verweisen.

Wenn der API-Aufruf mit `{{local_weather[0].WeatherText}}` antwortet und `Rain` zurückgibt, würde die Nutzer:in den Push erhalten.

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)