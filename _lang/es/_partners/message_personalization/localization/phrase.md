---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Este artículo de referencia describe la alianza entre Braze y Phrase, un software basado en la nube para la localización. Esta integración permite traducir plantillas de correo electrónico y Content Blocks sin salir de la interfaz de Braze."
page_type: partner
search_tag: Partner

---

# Phrase

> [Phrase](https://phrase.com/) es un software basado en la nube para la gestión de la localización. Phrase permite automatizar los flujos de trabajo de traducción y facilita la localización continua para equipos ágiles.

_Esta integración está mantenida por Phrase._

## Sobre la integración {#about-the-integration}

La integración de Phrase y Braze permite traducir plantillas de correo electrónico y Content Blocks sin salir de la interfaz de Braze. Con la integración de Phrase TMS para Braze, puedes aumentar la interacción con los clientes e impulsar el crecimiento en nuevos mercados con una localización perfecta.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta Phrase TMS | Se requiere una cuenta Phrase TMS Ultimate o Enterprise para beneficiarse de esta alianza. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con todos los permisos. <br><br> Puede crearse en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

## Paso 1: Configuración de Phrase TMS {#step-1-phrase-tms-settings}

En Phrase, ve a **Settings > Integrations > Connectors > New**.

1. Introduce un nombre para la conexión y cambia el tipo a **Braze**.<br><br>
2. Introduce la clave de API REST or transferencia de estado representacional y el punto de conexión REST or transferencia de estado representacional de Braze. <br><br>
3. Selecciona cómo debe importar el conector las plantillas de correo electrónico con Content Blocks vinculados.
- Solo plantilla de correo electrónico seleccionada
- Incluir Content Blocks<br><br>
4. Selecciona cómo debe exportar el conector las traducciones de las plantillas de correo electrónico.
- Crear un nuevo elemento
- Elemento original
  - El elemento original exporta traducciones a la misma plantilla/bloque. Los segmentos lingüísticos se definen mediante el atributo proporcionado.<br><br>
    {% raw %}
    Proporciona el atributo de idioma si se selecciona el elemento original. El atributo de idioma define el idioma del argumento if/elsif. Si utilizas la opción de elemento original, debe estructurarse como se muestra a continuación:

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    O utilizando el mapeado de claves/valores con assign:
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    El Liquid anterior debe seguirse estrictamente, pero el atributo de idioma y el idioma, las claves y el valor son ajustables.<br><br>
    Cada código de idioma solo puede utilizarse una vez. Sin embargo, pueden utilizarse varios idiomas para un mismo segmento, por ejemplo:
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Haz clic en **Test connection**. Si la conexión se realiza correctamente, aparecerá una marca de verificación. Pasa el cursor sobre el icono para ver más detalles.<br><br>
7. Por último, haz clic en **Save**. Este conector estará disponible en la página **Connectors**.

## Paso 3: Enviar contenido a Phrase y exportarlo de nuevo a Braze {#step-3-send-content-to-phrase-and-export-back-to-braze}

1. En primer lugar, configura el [portal de remitentes](https://support.phrase.com/hc/en-us/articles/5709602111132) para que puedan añadir archivos a las solicitudes directamente desde el repositorio en línea.<br><br>
2. Utiliza la [creación automática de proyectos (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) para que Phrase TMS cree automáticamente nuevos proyectos cuando se detecte un cambio en los estados especificados del flujo de trabajo.<br><br>
3. Los elementos de contenido seleccionados se importan la primera vez que se ejecuta APC.

La [API del conector](https://cloud.memsource.com/web/docs/api#) puede automatizar pasos que de otro modo se realizarían manualmente a través de la interfaz de usuario. Los [webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) pueden utilizarse para que Phrase TMS notifique a sistemas de terceros determinados eventos (por ejemplo, un cambio de estado de un trabajo).