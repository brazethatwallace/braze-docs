---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Transifex, einer Lokalisierungsplattform, mit der Sie Übersetzungen automatisieren können, sodass sich Ihre Teams auf die Bereitstellung hervorragender Kundenerlebnisse konzentrieren können."
page_type: partner
search_tag: Partner

---

# Transifex

> [Transifex](https://www.transifex.com/) ermöglicht eine robuste Lokalisierung für Ihre gesamte Nutzerbasis, unabhängig von der Sprache.

_Diese Integration wird von Transifex gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Transifex nutzt Connected-Content, um Ihnen zu ermöglichen, eine Sammlung von Resource Strings abzurufen und die entsprechenden Übersetzungen in Ihre Nachrichten einzufügen – anstatt Zeilen mit sprachbasierter bedingter Formatierung. Dadurch wird die Übersetzung automatisiert und Ihre Teams können sich auf die Bereitstellung hervorragender Kundenerlebnisse konzentrieren.

{% alert important %}
Seit dem 7. April 2022 hat Transifex die API-Versionen 2 und 2.5 zugunsten von Version 3 eingestellt. v2 und v2.5 sind nicht mehr funktionsfähig, und entsprechende Anfragen werden fehlschlagen. <br><br>Die folgenden Integrationsanweisungen beziehen sich auf das Update auf Version 3. Aktualisieren Sie Ihre Connected-Content-Aufrufe entsprechend.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Transifex-Konto | Um diese Partnerschaft nutzen zu können, ist ein [Transifex-Konto](https://www.transifex.com/signin/) erforderlich. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die Transifex-Integration verwendet die [API für Ressourcenübersetzungen](https://developers.transifex.com/reference/get_resource-translations) von Transifex. Mit dem folgenden cURL-Befehl können Sie prüfen, ob Ihr Konto Inhaltswerte hat, die mit Übersetzungen verknüpft sind.

Geben Sie zunächst die in Ihrem Transifex-Konto hinterlegten Werte für `<ORGANIZATION_NAME>`, `<PROJECT_NAME>` und `<RESOURCE_NAME>` ein. Ersetzen Sie anschließend `<LANGUAGE>` durch den Sprachcode, nach dem Sie die Übersetzungen filtern möchten, und `<TRANSIFEX_BEARER_TOKEN>` durch Ihr Transifex-[Bearer-Token](https://developers.transifex.com/reference/api-authentication).

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSIFEX_BEARER_TOKEN>'
```

Wenn sich Ihr Transifex-Projekt beispielsweise unter `https://www.transifex.com/appboy-3/french2/french_translationspo/` befindet, lautet der `project_name` „french2“ und der `resource_name` „french_translationspo“.

## Beispiel für eine Connected-Content-Nachricht {#connected-content-message-example}

Dieses Code-Snippet verwendet die Transifex-API für Ressourcenübersetzungen und das `language`-Attribut der Nutzer:innen. Je nach Bedarf können Sie dann die String-Objekte in einer Schleife durchlaufen und den entsprechenden Inhalt mit folgendem Liquid abrufen: `{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}


[16]: [success@braze.com](mailto:success@braze.com)