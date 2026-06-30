---
nav_title: Lokale Connected-Content-Variablen
article_title: Lokale Connected-Content-Variablen
page_order: 1
description: "Dieser Referenzartikel behandelt die Verwendung und Speicherung lokaler Connected-Content-Variablen."
search_rank: 1
---

# Lokale Connected-Content-Variablen {#local-connected-content-variables}

> Diese Seite bietet eine Übersicht über lokale Connected-Content-Variablen und deren Verwendung und Speicherung.

Braze führt zum Sendezeitpunkt eine Standard-GET-Anfrage an den im `connected_content`-Tag angegebenen Endpunkt durch. Wenn der Endpunkt JSON zurückgibt, wird die Antwort automatisch geparst und in einer Variablen namens `connected` gespeichert. Wenn der Endpunkt Text zurückgibt, wird dieser direkt in die Nachricht anstelle des `connected_content`-Tags eingefügt.

Wenn Sie Ihre Antwort in einer Variablen speichern möchten, wird empfohlen, JSON-Objekte zurückzugeben. Und wenn Sie möchten, dass die Antwort von Connected-Content den Tag durch den Text ersetzt, stellen Sie sicher, dass die Antwort kein gültiges JSON ist (wie von [json.org](http://www.json.org) definiert).

Sie können auch `:save your_variable_name` nach der URL angeben, um die Daten unter einem anderen Namen zu speichern. Zum Beispiel speichert der folgende `connected_content`-Tag die Antwort in einer lokalen Variablen namens `localweather` (Sie können mehrere `connected_content`-JSON-Variablen speichern):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather ist eine kostenlose Wetter-API, die eine „Where-on-Earth ID“ verwendet, um das Wetter in einem Gebiet zurückzugeben. Verwenden Sie diesen Code nur zu Test- und Lernzwecken.

Auf die gespeicherte Variable kann nur innerhalb des Feldes zugegriffen werden, das die `connected_content`-Anfrage enthält. Wenn Sie beispielsweise die Variable `localweather` sowohl im Nachrichtenfeld als auch im Titelfeld verwenden möchten, sollten Sie die `connected_content`-Anfrage in beiden Feldern durchführen.

GET-Anfragen werden in der Regel standardmäßig zwischengespeichert, mit einigen Ausnahmen (z. B. URLs, die hochkardinalige Nutzer:innen-Attribute enthalten, `:no_cache` oder Antwort-Bodys größer als 1 MB). Wenn identische GET-Anfragen in mehr als einem Feld vorkommen, verwendet Braze die zwischengespeicherte Antwort, anstatt den Endpunkt erneut aufzurufen. Einzelheiten zum Cache-Verhalten finden Sie unter [Antworten zwischenspeichern]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

Connected-Content-Aufrufe über HTTP POST werden standardmäßig nicht zwischengespeichert. Um POST-Antworten zwischenzuspeichern, fügen Sie `:cache_max_age` zum Tag hinzu. Siehe [Standard-Cache-Einstellungen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses#default-cache-settings).

## JSON-Parsing {#json-parsing}

Connected-Content interpretiert alle JSON-formatierten Ergebnisse als lokale Variable, wenn Sie `:save` angeben. Zum Beispiel gibt ein wetterbezogener Connected-Content-Endpunkt das folgende JSON-Objekt zurück, das Sie durch Angabe von `:save localweather` in einer lokalen Variablen `localweather` speichern.
{% raw %}

```js
{
  "consolidated_weather": [
    {
      "id": 5.8143475362693e+15,
      "weather_state_name": "Clear",
      "weather_state_abbr": "c",
      "wind_direction_compass": "WSW",
      "created": "2017-06-12T14:14:46.268110Z",
      "applicable_date": "2017-06-12",
      "min_temp": 22.511666666667,
      "max_temp": 31.963333333333,
      "the_temp": 27.803333333333,
      "wind_speed": 6.8884690250312,
      "wind_direction": 251.62921994166,
      "air_pressure": 1021.335,
      "humidity": 50,
      "visibility": 14.945530601288,
      "predictability": 68
    },
    .
    .
    .
    "title": "New York",
    "location_type": "City",
    "woeid": 2459115,
    "latt_long": "40.71455,-74.007118",
    "timezone": "US\/Eastern"
  }
```

Sie können testen, ob es regnet, indem Sie `{{localweather.consolidated_weather[0].weather_state_name}}` referenzieren, was bei diesem Objekt `Clear` zurückgeben würde. Wenn Sie auch mit dem resultierenden Standortnamen personalisieren möchten, gibt `{{localweather.title}}` den Wert `New York` zurück.
{% endraw %}

Das folgende Bild zeigt die Art der Syntaxhervorhebung, die Sie im Dashboard sehen sollten, wenn Sie alles korrekt eingerichtet haben. Es zeigt auch, wie Sie die Beispiel-`connected_content`-Anfrage nutzen können!

{% raw %}
```liquid
{% connected_content https://www.metaweather.com/api/location/search/?query={{custom_attribute.${customCity}}} :save locationjson %}
{% connected_content https://www.metaweather.com/api/location/{{locationjson[0].woeid}}/ :save localweather %}

{% if {{localweather.consolidated_weather[0].weather_state_name}} == 'Rain' %}
It's raining! Grab an umbrella!
{% elsif {{localweather.consolidated_weather[0].weather_state_name}} == 'Clouds' %}
No sunscreen needed :)
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

Wenn die API mit {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} den Wert `Rain` zurückgibt, würden die Nutzer:innen dann diese Push-Benachrichtigung erhalten.

![Push-Benachrichtigung mit der Nachricht „It's raining! Grab an umbrella!“]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content/sections.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content/sections.md section='http post' %}

### Bereitstellung eines JSON-Bodys {#providing-json-body}

Wenn Sie Ihren eigenen JSON-Body bereitstellen möchten, können Sie ihn inline schreiben, sofern keine Leerzeichen vorhanden sind. Wenn Ihr Body Leerzeichen enthält, sollten Sie eine Assign- oder Capture-Anweisung verwenden. Das heißt, alle drei folgenden Varianten sind zulässig:

{% raw %}
##### Inline: keine Leerzeichen zulässig {#inline-spaces-not-allowed}

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Body in einer Capture-Anweisung: Leerzeichen zulässig {#body-in-a-capture-statement-spaces-allowed}

```js
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

{% raw %}
```js
{% capture postbody %}
{
"ids":[ca_57832,ca_75869],"include":{"attributes":{"withKey":["daily_deals"]}}
}
{% endcapture %}

{% connected_content
    https://example.com/api/endpoint
    :method post
    :headers {
      "Content-Type": "application/json"
  }
  :body {{postbody}}
  :save result
%}
```
{% endraw %}

{% raw %}
##### Body in einer Assign-Anweisung: Leerzeichen zulässig {#body-in-an-assign-statement-spaces-allowed}

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## HTTP-Statuscodes {#http-status-codes}

Sie können den HTTP-Status eines Connected-Content-Aufrufs nutzen, indem Sie ihn zunächst als lokale Variable speichern und dann den Schlüssel `__http_status_code__` verwenden. Zum Beispiel:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Dieser Schlüssel wird dem Connected-Content-Objekt nur dann automatisch hinzugefügt, wenn der Endpunkt ein gültiges JSON-Objekt und eine `2XX`-Antwort zurückgibt. Wenn der Endpunkt ein Array oder einen anderen Typ zurückgibt, kann dieser Schlüssel nicht automatisch in der Antwort gesetzt werden.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)