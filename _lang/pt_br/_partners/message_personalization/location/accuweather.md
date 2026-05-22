---
nav_title: AccuWeather
article_title: AccuWeather
alias: /partners/accuweather/
description: "Este artigo de referência descreve a parceria entre a Braze e a AccuWeather, uma API de meteorologia que você pode usar para personalizar suas campanhas de marketing."
page_type: partner
search_tag: Partner

---

# AccuWeather

> A [AccuWeather](https://www.accuweather.com/) é uma empresa de mídia que fornece serviços de previsão do tempo em todo o mundo. Com a AccuWeather, você pode enriquecer e personalizar suas campanhas de marketing, bem como automatizar traduções por meio do uso do [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) da Braze.

_Essa integração é mantida pela AccuWeather._

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Chave de API da AccuWeather | Entre em contato com o gerente da sua conta AccuWeather para obter as chaves de API compatíveis a serem usadas nos URLs de solicitação.<br><br>Mais instruções podem ser encontradas na página da [API AccuWeather Enterprise](https://apidev.accuweather.com/developers/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## APIs AccuWeather disponíveis {#available-accuweather-apis}

A seguir, confira as APIs da AccuWeather que você pode consultar nas suas Campaigns e Canvas da Braze.

| API | Descrição |
|---|---|
| [Locations](https://apidev.accuweather.com/developers/locationsAPIguide) | Obtenha uma chave de localização para o local desejado. Use a chave de local para recuperar dados meteorológicos da API de previsão ou condições atuais. |
| [Forecast](https://apidev.accuweather.com/developers/forecastsAPIguide) | Obtenha informações de previsão para um local específico. |
| [Current Conditions](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) | Obtenha dados de condições atuais para um local específico. |
| [Indices](https://apidev.accuweather.com/developers/indicesApiGuide) | Obtenha valores de índice diários para um local específico. A disponibilidade do índice varia de acordo com o local. |
| [Weather Alarms](https://apidev.accuweather.com/developers/weatheralarmsAPIguide) | Obtenha alarmes meteorológicos para um local específico. Os alarmes meteorológicos da AccuWeather são determinados usando as previsões diárias para um local. Existe um alarme para um local se a previsão do tempo atingir ou exceder os [limites específicos](https://apidev.accuweather.com/developers/weatheralarms). |
| [Alerts](https://apidev.accuweather.com/developers/alertsApiGuide) | Receba alertas de clima severo das agências meteorológicas oficiais do governo e dos principais provedores globais de alertas meteorológicos. |
| [Imagery](https://apidev.accuweather.com/developers/imageryAPIguide) | Obtenha imagens de radar e satélite. |
| [Tropical](https://apidev.accuweather.com/developers/tropicalAPIGuide) | Obtenha a posição atual, as posições anteriores e as previsões de ciclones tropicais em todo o mundo. |
| [Translations](https://apidev.accuweather.com/developers/translationsApiGuide) | Obtenha uma lista dos idiomas disponíveis. Obtenha traduções para grupos específicos de frases. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="APIs AccuWeather disponíveis" }

## Exemplo de Conteúdo conectado {#connected-content-example}

O exemplo a seguir mostra uma chamada de Conteúdo conectado exibindo dois tipos diferentes de mensagens com base nas condições atuais do código postal de um usuário nos EUA. São usados os endpoints da API de locais e condições atuais da AccuWeather.
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

![Uma mensagem push de Conteúdo conectado que diz "It's raining! Grab an Umbrella!" exibida em um dispositivo Android]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){: style="max-width:40%"}

Um detalhamento das duas chamadas de Conteúdo conectado está disponível nos exemplos a seguir.

{% tabs %}
{% tab Locations %}
#### Exemplo de API de locais {#locations-api-example}

{% raw %}
Na primeira tag `connected_content`, é feita uma solicitação GET para a [API de locais](https://apidev.accuweather.com/developers/locationsAPIguide). Para este exemplo, você também pode aproveitar o `{{${city}}}` do usuário se não tiver um atributo personalizado de código postal.

```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}
```
{% endraw %}

Aqui está um exemplo do que a AccuWeather retornará como objeto JSON:

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

O ID "Key" é uma variável útil, pois é usada na segunda solicitação GET.
Esse objeto JSON pode ser armazenado em uma variável local `location_info` especificando `:save location_info` após o URL.
{% endtab %}
{% tab Condições atuais %}

#### Exemplo de API de condições atuais {#current-conditions-api-example}

Para a segunda tag `connected_content`, é feita uma solicitação GET à [API de condições atuais](https://apidev.accuweather.com/developers/currentConditionsAPIGuide). A **chave do local** precisará ser adicionada ao URL da solicitação. Aqui está o exemplo da tag `connected_content`:

{% raw %}
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}
```

Aqui está o objeto JSON retornado:

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

Como visto na tag `connected_content`, o objeto JSON é armazenado em uma variável local `local_weather` adicionando `:save local_weather` após o URL.

Você pode testar qual deve ser a saída do [WeatherText](https://apidev.accuweather.com/developers/currentConditionsAPIGuide) fazendo referência a `{{local_weather[0].WeatherText}}`.

Se a chamada da API responder com `{{local_weather[0].WeatherText}}` retornando `Rain`, o usuário receberá o push.

{% endraw %}
{% endtab %}
{% endtabs %}


[16]: [success@braze.com](mailto:success@braze.com)