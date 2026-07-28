---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "Este artículo de referencia describe la asociación entre Braze y AccuWeather, una API meteorológica que puedes utilizar para personalizar tus campañas de marketing."
page_type: partner
search_tag: Partner

---

# AccuWeather

> [AccuWeather](https://www.accuweather.com/) es una empresa de medios de comunicación que presta servicios de predicción meteorológica en todo el mundo. Con AccuWeather, puedes enriquecer y personalizar tus campañas de marketing, así como automatizar las traducciones mediante el uso del [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) de Braze.

_Esta integración está mantenida por AccuWeather._

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Clave de API de AccuWeather | Ponte en contacto con tu director de cuentas de AccuWeather para obtener las claves de API compatibles que debes utilizar en tus URL de solicitud.<br><br>Encontrarás más instrucciones en la página de [la API empresarial de AccuWeather](https://apidev.accuweather.com/developers/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## API de AccuWeather disponibles {#available-accuweather-apis}

A continuación se indican las API de AccuWeather a las que puedes hacer referencia en tus Campaigns y Canvas de Braze.

| API | Descripción |
|---|---|
| [Ubicaciones](https://apidev.accuweather.com/developers/locationsAPIguide) | Obtén una clave de ubicación para la ubicación deseada. Utiliza la clave de ubicación para recuperar datos meteorológicos de la API de previsión o de condiciones actuales. |
| [Previsión](https://apidev.accuweather.com/developers/forecastsAPIguide) | Obtén información de previsión para una ubicación específica. |
| [Condiciones actuales](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | Obtén los datos de las condiciones actuales para una ubicación específica. |
| [Índices](https://apidev.accuweather.com/developers/indicesApiGuide) | Obtén los valores diarios del índice para una ubicación específica. La disponibilidad del índice varía según la ubicación. |
| [Alarmas meteorológicas](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | Obtén alarmas meteorológicas para una ubicación específica. Las alarmas meteorológicas de AccuWeather se determinan utilizando las previsiones diarias para una ubicación. Existe una alarma para una ubicación si el tiempo previsto alcanza o supera [unos umbrales específicos](https://apidev.accuweather.com/developers/weatheralarms). |
| [Alertas](https://apidev.accuweather.com/developers/alertsApiGuide) | Recibe alertas de condiciones meteorológicas adversas de las agencias meteorológicas oficiales y de los principales proveedores mundiales de alertas meteorológicas. |
| [Imágenes](https://apidev.accuweather.com/developers/imageryAPIguide) | Obtén imágenes de radar y satélite. |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | Obtén la posición actual, las posiciones anteriores y las previsiones de ciclones tropicales en todo el mundo. |
| [Traducciones](https://apidev.accuweather.com/developers/translationsApiGuide) | Obtén una lista de los idiomas disponibles. Obtén traducciones para grupos específicos de frases. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API de AccuWeather disponibles" }

## Ejemplo de contenido conectado {#connected-content-example}

El siguiente ejemplo muestra una llamada de contenido conectado que muestra dos tipos diferentes de mensajes basados en las condiciones actuales del código postal de un usuario en EE. UU. Se utilizan los endpoints de la API de ubicaciones y condiciones actuales de AccuWeather.
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

![Un mensaje push de contenido conectado que dice "It's raining! Grab an Umbrella!" mostrado en un dispositivo Android]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){: style="max-width:40%"}

En los siguientes ejemplos se desglosan las dos llamadas de contenido conectado.

{% tabs %}
{% tab Ubicaciones %}
### Ejemplo de API de ubicaciones {#locations-api-example}

{% raw %}
Dentro de la primera etiqueta `connected_content`, se realiza una solicitud GET a la [API de ubicaciones](https://apidev.accuweather.com/developers/locationsAPIguide). Para este ejemplo, puedes aprovechar alternativamente la `{{${city}}}` del usuario si no dispones de un atributo personalizado de código postal.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Este es un ejemplo de lo que AccuWeather devolverá como objeto JSON:

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

El ID "Key" es una variable útil, ya que se utiliza en la segunda solicitud GET.
Este objeto JSON puede almacenarse en una variable local `location_info` especificando `:save location_info` después de la URL.
{% endtab %}
{% tab Condiciones actuales %}

### Ejemplo de API de condiciones actuales {#current-conditions-api-example}

Para la segunda etiqueta `connected_content`, se realiza una solicitud GET a la [API de condiciones actuales](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). La **clave de ubicación** deberá añadirse a la URL de la solicitud. Este es el ejemplo de etiqueta `connected_content`:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Este es el objeto JSON devuelto:

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

Como se ve en la etiqueta `connected_content`, el objeto JSON se almacena en una variable local `local_weather` añadiendo `:save local_weather` después de la URL.

Puedes comprobar cuál debería ser la salida de [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) consultando `{{local_weather[0].WeatherText}}`.

Si la llamada a la API responde con `{{local_weather[0].WeatherText}}` devolviendo `Rain`, el usuario recibiría entonces la notificación push.

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)