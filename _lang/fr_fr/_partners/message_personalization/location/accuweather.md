---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "Cet article de référence décrit le partenariat entre Braze et AccuWeather, une API météo que vous pouvez utiliser pour personnaliser vos campagnes marketing."
page_type: partner
search_tag: Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) est une société de médias qui fournit des services de prévisions météorologiques dans le monde entier. Avec AccuWeather, vous pouvez enrichir et personnaliser vos campagnes marketing, ainsi qu'automatiser les traductions grâce au [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) de Braze.

_Cette intégration est maintenue par AccuWeather._

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Clé API AccuWeather | Contactez votre gestionnaire de compte AccuWeather pour obtenir des clés API compatibles à utiliser dans les URL de vos requêtes.<br><br>Vous trouverez des instructions supplémentaires sur la page [AccuWeather Enterprise API](https://apidev.accuweather.com/developers/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## API AccuWeather disponibles {#available-accuweather-apis}

Voici les API AccuWeather que vous pouvez référencer dans vos Campaigns et Canvas Braze.

| API | Description |
|---|---|
| [Localisations](https://apidev.accuweather.com/developers/locationsAPIguide) | Obtenez une clé d'emplacement pour la localisation souhaitée. Utilisez la clé d'emplacement pour récupérer les données météorologiques à partir de l'API des prévisions ou des conditions actuelles. |
| [Prévisions](https://apidev.accuweather.com/developers/forecastsAPIguide) | Obtenez des informations de prévisions pour un emplacement spécifique. |
| [Conditions actuelles](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | Obtenez les données relatives aux conditions actuelles pour un emplacement spécifique. |
| [Indices](https://apidev.accuweather.com/developers/indicesApiGuide) | Obtenez les valeurs d'indice quotidiennes pour un emplacement spécifique. La disponibilité des indices varie en fonction de l'emplacement. |
| [Alarmes météo](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | Recevez des alarmes météorologiques pour un emplacement spécifique. Les alarmes météo AccuWeather sont déterminées à l'aide des prévisions quotidiennes pour un emplacement. Une alarme est déclenchée pour un emplacement si les prévisions météorologiques atteignent ou dépassent des [seuils spécifiques](https://apidev.accuweather.com/developers/weatheralarms). |
| [Alertes](https://apidev.accuweather.com/developers/alertsApiGuide) | Recevez des alertes météorologiques extrêmes de la part des agences météorologiques gouvernementales officielles et des principaux fournisseurs mondiaux d'alertes météorologiques. |
| [Imagerie](https://apidev.accuweather.com/developers/imageryAPIguide) | Obtenez des images radar et satellites. |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | Obtenez la position actuelle, les positions passées et les prévisions des cyclones tropicaux dans le monde entier. |
| [Traductions](https://apidev.accuweather.com/developers/translationsApiGuide) | Consultez la liste des langues disponibles. Obtenez des traductions pour des groupes de phrases spécifiques. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API AccuWeather disponibles" }

## Exemple de Contenu connecté {#connected-content-example}

L'exemple suivant montre un appel de Contenu connecté affichant deux types de messages différents en fonction des conditions actuelles du code postal d'un utilisateur aux États-Unis. Les endpoints de l'API des localisations et des conditions actuelles d'AccuWeather sont utilisés.
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

![Un message push de Contenu connecté indiquant « It's raining! Grab an Umbrella! » affiché sur un appareil Android]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){: style="max-width:40%"}

Vous trouverez le détail des deux appels de Contenu connecté dans les exemples suivants.

{% tabs %}
{% tab Locations %}
#### Exemple d'API de localisation {#locations-api-example}

{% raw %}
Dans la première balise `connected_content`, une requête GET est envoyée à l'[API des localisations](https://apidev.accuweather.com/developers/locationsAPIguide). Pour cet exemple, vous pouvez également utiliser le `{{${city}}}` de l'utilisateur si vous ne disposez pas d'un attribut personnalisé de code postal.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Voici un exemple de ce qu'AccuWeather renverra sous forme d'objet JSON :

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

L'ID « Key » est une variable utile, car elle est utilisée dans la deuxième requête GET.
Cet objet JSON peut être stocké dans une variable locale `location_info` en spécifiant `:save location_info` après l'URL.
{% endtab %}
{% tab Current conditions %}

#### Exemple d'API pour les conditions actuelles {#current-conditions-api-example}

Pour la deuxième balise `connected_content`, une requête GET est envoyée à l'[API des conditions actuelles](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). La **clé d'emplacement** devra être ajoutée à l'URL de la requête. Voici l'exemple de la balise `connected_content` :

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Voici l'objet JSON renvoyé :

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

Comme le montre la balise `connected_content`, l'objet JSON est stocké dans une variable locale `local_weather` en ajoutant `:save local_weather` après l'URL.

Vous pouvez tester la valeur renvoyée par [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) en référençant `{{local_weather[0].WeatherText}}`.

Si l'appel d'API répond avec `{{local_weather[0].WeatherText}}` renvoyant `Rain`, l'utilisateur recevra alors la notification push.

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)