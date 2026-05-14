---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "Este artículo de referencia describe la asociación entre Braze y Transifex, una plataforma de localización que te permite automatizar la traducción, liberando a tus equipos para que se centren en ofrecer experiencias brillantes a los clientes."
page_type: partner
search_tag: Partner

---

# Transifex

> [Transifex](https://www.transifex.com/) habilita una sólida localización en toda tu base de usuarios, sin importar el idioma.

_Esta integración está mantenida por Transifex._

## Sobre la integración {#about-the-integration}

La integración de Braze y Transifex utiliza Contenido conectado para permitirte extraer una colección de cadenas de recursos e incluir las traducciones pertinentes en tus mensajes, en lugar de líneas de formato condicional basadas en el idioma. Esto automatiza la traducción y libera a tus equipos para que se centren en ofrecer experiencias brillantes a los clientes.

{% alert important %}
A partir del 7 de abril de 2022, Transifex ha dejado obsoletas sus versiones 2 y 2.5 de la API para dar paso a la versión 3. Las v2 y v2.5 ya no son operativas, y las solicitudes correspondientes fallarán. <br><br>Las siguientes instrucciones de integración reflejan la actualización de la versión 3. Actualiza tus llamadas a Contenido conectado en consecuencia.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Transifex | Se necesita una [cuenta de Transifex](https://www.transifex.com/signin/) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

La integración de Transifex utiliza la [API de traducción de recursos](https://developers.transifex.com/reference/get_resource-translations) de Transifex. El siguiente cURL te permitirá ver si tu cuenta tiene valores de contenido asociados a traducciones.

En primer lugar, introduce los datos `<ORGANIZATION_NAME>`, `<PROJECT_NAME>` y `<RESOURCE_NAME>` que se encuentran en tu cuenta de Transifex. A continuación, sustituye `<LANGUAGE>` por el código de idioma por el que deseas filtrar las traducciones y `<TRANSIFEX_BEARER_TOKEN>` por tu [token de portador](https://developers.transifex.com/reference/api-authentication) de Transifex.

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSIFEX_BEARER_TOKEN>'
```

Por ejemplo, si tu proyecto de Transifex está ubicado en `https://www.transifex.com/appboy-3/french2/french_translationspo/`, el `project_name` será "french2" y el `resource_name` será "french_translationspo".

## Ejemplo de mensaje de Contenido conectado {#connected-content-message-example}

Este fragmento de código de ejemplo utiliza la API de traducción de recursos de Transifex y el atributo `language` del usuario. En función de tus necesidades, puedes recorrer los objetos de cadena y extraer el contenido pertinente utilizando el siguiente Liquid: `{{strings.data[X].attributes.strings.other}}`.

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