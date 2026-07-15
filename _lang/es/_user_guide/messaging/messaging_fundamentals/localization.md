---
nav_title: Localización
article_title: Localización
page_order: 8
description: "Este artículo de referencia cubre los conceptos básicos de la localización, enumera los beneficios de los diferentes enfoques de orquestación en Campaigns y Canvas, y presenta las distintas formas en que los usuarios pueden gestionar la personalización en su mensajería."
tool:
    - Campaigns
    - Canvas
---

# Localización {#localization}

> Para las empresas con clientes en muchos países, gestionar la localización de forma temprana en tu recorrido con Braze puede ahorrar tiempo y recursos a tu empresa.

## Cómo funciona {#how-it-works}

La información de configuración regional se almacena en el perfil de un usuario a partir de los datos que recopilas mediante un [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration) (automáticamente) o la [REST API]({{ site.baseurl }}/api/endpoints/user_data/post_user_track). La configuración regional contiene el idioma y un identificador de región. Esta información está disponible en la herramienta de segmentación de Braze en **País** e **Idioma**.

{% alert tip %}
Para obtener detalles técnicos sobre cómo nuestros SDK recopilan la configuración regional, consulta la documentación oficial de [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html), [Android](http://developer.android.com/reference/java/util/Locale.html) y [Web](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language).
{% endalert %}

## Gestión de traducciones {#translation-management}

Considera los siguientes enfoques para gestionar tus traducciones.

{% tabs local %}
{% tab campaign %}
### Una plantilla para todos {#one-template-for-all}

En este enfoque, la localización se aplica a una única plantilla en Braze utilizando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Después del envío, el dashboard proporciona análisis agregados de la Campaign. La interacción a nivel de usuario se puede medir mediante embudos de Segments personalizados, por ejemplo, combinando los filtros **País** y **Campaign recibida**.

| Ventajas | Consideraciones |
| --- | --- |
| - Enfoque centralizado<br>- Tiempo de creación de correo electrónico reducido, sin necesidad de crear un correo electrónico varias veces | - Creación manual de informes<br>- El informe de Campaign muestra métricas agregadas en lugar de métricas por país<br>- Es necesario probar exhaustivamente Liquid para asegurarse de que se rellena como se espera<br>- Dependiendo de cómo obtengas el valor del país o cuántos países tengas configurados, puede ser complicado probar cada país<br>- Más difícil programar envíos para horarios específicos en diferentes zonas horarias<br>- Más difícil de usar si quieres enviar contenido diferente por país. |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Una plantilla para todos" }

### Una plantilla por país {#one-template-per-country}

Este enfoque separa las plantillas en diferentes configuraciones regionales de envío. Después del envío, el dashboard muestra los análisis de envío basados en cada país por separado, y cualquier evento de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#access-currents) a nivel de usuario posterior también estará vinculado a una Campaign específica.

- Las plantillas se benefician de implementar [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags#tags) con fines de mantenimiento y seguimiento.
- Las Campaigns pueden heredar las configuraciones de la misma [plantilla de Braze]({{site.baseurl}}/user_guide/messaging/templates) y [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) (como las [plantillas de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates) que contienen Liquid).
- Las Campaigns y plantillas preexistentes se pueden [duplicar]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating) para permitir un tiempo de obtención de valor más rápido.

| Ventajas | Consideraciones |
| --- | --- |
| - Escalable a múltiples ubicaciones<br>- Informes de ingresos por país dentro de Braze (como por Campaign)<br>- Flexibilidad si hay contenido drásticamente diferente por país | - Requiere una estructuración estratégica<br>- Se requiere más esfuerzo de creación (como Campaigns separadas para cada país) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Una plantilla por país" }
{% endtab %}

{% tab canvas %}
### Un recorrido para todos {#one-journey-for-all}

En este enfoque, la localización se gestiona dentro de los [conceptos básicos de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_basics#building-the-customer-journey) y Liquid para definir la mensajería para cada usuario.

Después de enviar un Canvas, el dashboard proporciona [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) agregados, mientras que la interacción a nivel de usuario se puede medir mediante [embudos de Segments]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size) personalizados, como la combinación de los filtros [**País**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#country) y [**Paso de Canvas recibido**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-canvas-step).

| Ventajas | Consideraciones |
| --- | --- |
| - Enfoque centralizado<br>- Tiempo de creación de correo electrónico reducido: no es necesario crear un correo electrónico varias veces. | - Creación manual de informes<br>- El informe de Canvas muestra métricas agregadas en lugar de métricas por país<br>- Es necesario probar exhaustivamente Liquid para asegurarse de que se rellena como se espera<br>- Dependiendo de cómo obtengas el valor del país o cuántos países tengas configurados, puede ser complicado probar cada país<br>- Más difícil programar envíos para horarios específicos en diferentes zonas horarias<br>- Más difícil de usar si quieres enviar contenido diferente por país. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Un recorrido para todos" }

### Un recorrido por país {#one-journey-per-country}

En este enfoque, el constructor de recorridos de [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) proporciona la flexibilidad de crear recorridos de usuario a través de múltiples [componentes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components). Estos componentes se pueden [duplicar]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating) a nivel de componente y de recorrido general.

La localización se puede lograr con los siguientes métodos:

- Canvas separados por país, esto asegura que los recorridos de usuario complejos se definan en la parte superior del embudo utilizando filtros de audiencia
- Recorridos de usuario personalizados por país, la implementación de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) para segmentar intuitivamente a los usuarios a gran escala para cada recorrido creando hilos de mensajes separados para cada país en un solo Canvas

Una vez enviado, el dashboard proporciona análisis dinámicos por país y dentro de los eventos de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#access-currents) a nivel de usuario basados en la ubicación actual del cliente.

| Ventajas | Consideraciones |
| --- | --- |
| - Informes de ingresos por país dentro de Braze (como por Canvas, variante o paso)<br>- Flexibilidad si hay contenido drásticamente diferente por país<br>- Se pueden añadir otros canales como parte del recorrido en el futuro | - Requiere una estructuración estratégica<br>- Se requiere más esfuerzo de creación (como pasos de mensaje separados para cada país)<br>- El Canvas puede volverse grande y difícil de leer si tienes recorridos personalizados y complejos para cada país en un solo Canvas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Un recorrido por país" }
{% endtab %}
{% endtabs %}

## Envío de mensajes traducidos {#sending-translated-messages}

Para enviar mensajes personalizados basados en el idioma, la configuración regional o los atributos personalizados de un usuario, utiliza uno de los siguientes métodos.

### Etiquetas de Liquid de traducción (recomendado) {#translation-liquid-tag}

Braze admite una etiqueta de Liquid {% raw %}`{% translation salutation %}Hello!{% endtranslation %}`{% endraw %} para dirigirse a los usuarios en diferentes idiomas con un solo mensaje.

Para un tutorial completo, consulta la [guía sobre el uso de etiquetas de traducción]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

### Enfoques alternativos {#alternative-approaches}

{% tabs local %}
{% tab Custom Liquid %}
Puedes pegar manualmente tu contenido en el cuerpo de tu mensaje y usar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) para mostrar [condicionalmente]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) el idioma correcto al destinatario. Para hacer esto:

1. Redacta tu mensaje, luego selecciona **Idioma** para generar lógica condicional de Liquid para cada uno de tus idiomas seleccionados.
2. Puedes usar la siguiente plantilla de Liquid para ayudar a construir tu mensaje. Para cada campo con plantilla, debes introducir las variaciones después del segmento entre corchetes de la plantilla. La variación debe corresponder al código de idioma referenciado en los corchetes antes de ella.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. Prueba tu mensaje antes de enviarlo introduciendo el ID o correo electrónico de un usuario para comprobar cómo aparecería un mensaje a una persona dependiendo de su idioma.

{% alert tip %}
Siempre recomendamos incluir una declaración {% raw %}`{% else %}`{% endraw %} en tu mensajería. Aunque la mayoría de los usuarios verán mensajes en su idioma específico, el texto será visible para aquellos que:
- No tienen un idioma seleccionado
- Tienen un idioma que Braze no admite
- Tienen un dispositivo en el que el idioma no es detectable
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Los [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) de Braze son bloques de contenido reutilizables. Cuando se modifica un bloque, todas las referencias a ese bloque cambian. Por ejemplo, las actualizaciones en un encabezado o pie de página de correo electrónico se reflejarán en todos los correos electrónicos o para alojar traducciones. Estos bloques también se pueden [crear]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block#create-content-block) y [actualizar]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) usando la REST API, y los usuarios pueden cargar traducciones de forma programática.

Al crear una Campaign en el dashboard, se puede hacer referencia a los Content Blocks usando la etiqueta {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. Estos bloques podrían contener todas las traducciones alojadas dentro de lógica condicional para cada idioma, como se muestra en la opción 1, o se puede usar un bloque separado para cada idioma.

Los Content Blocks también se pueden utilizar como un proceso de gestión de traducciones donde el contenido que requiere traducción se aloja dentro de un Content Block, se obtiene, se traduce y luego se actualiza:
1. Crea manualmente un Content Block en el dashboard con la etiqueta "Needs Translation".
2. Tu servicio realiza una obtención nocturna de todos los Content Blocks usando el [punto de conexión `/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks).
3. Tu servicio obtiene detalles de cada Content Block a través del [punto de conexión `/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) para ver qué bloques están etiquetados para traducción.
4. Tu servicio de traducción traduce el cuerpo de todos los Content Blocks con "Needs Translation".
5. Tu servicio llama al [punto de conexión `/content_block/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) para actualizar el contenido traducido y actualizar la etiqueta a "Translation Complete".
{% endtab %}

{% tab Catalogs %}
Los [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) te permiten acceder a datos de objetos JSON importados a través de API y archivos CSV para enriquecer tus mensajes, de forma similar a los atributos personalizados o las propiedades de eventos personalizados a través de Liquid. Por ejemplo:

{% subtabs local %}
{% subtab API %}

Crea un catálogo a través de la siguiente llamada a la API:
```bash
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

Añade elementos a través de la siguiente llamada a la API:

```bash
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
Crea un CSV en el siguiente formato:

| id | context | language | body |
| --- | --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Enfoques alternativos" }
{% endsubtab %}
{% endsubtabs %}

Estos elementos del catálogo se pueden referenciar usando [personalización]({{site.baseurl}}/user_guide/data/activation/catalogs/create#using-catalogs-in-a-message), como se muestra a continuación, o [selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) que te permiten crear grupos de datos.

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}}
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Braze partners %}
Muchos socios de Braze ofrecen soluciones de localización, incluyendo [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex#about-transifex) y [Crowdin](https://crowdin.com/). Normalmente, los usuarios utilizan la plataforma junto con un equipo interno y una agencia de traducción. Estas traducciones se cargan allí y luego son accesibles a través de la REST API. Estos servicios también suelen aprovechar el [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), lo que permite a los usuarios obtener las traducciones a través de la API.

Por ejemplo, las siguientes llamadas de contenido conectado llaman a Transifex y Crowdin para obtener una traducción, aprovechando {% raw %}`{{${language}}}`{% endraw %} para identificar la traducción correcta para un usuario determinado. Esta traducción se guarda luego en el bloque JSON "strings" y se referencia.

{% subtabs local %}
{% subtab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Spreadsheets %}
Aloja las traducciones en una hoja de cálculo y luego usa uno de los siguientes métodos para enviar tu mensaje en el idioma correspondiente.

{% subtabs local %}
{% subtab Connected Content %}
Puedes trabajar con una agencia de traducción para almacenar traducciones en una hoja de cálculo de Google y luego consultar este contenido usando el [contenido conectado de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Cuando envías un mensaje, la traducción correspondiente para cada usuario se incorporará al cuerpo de tu Campaign según su idioma seleccionado.

{% alert note %}
La API de Google Sheets tiene un límite de 500 solicitudes por cada 100 segundos por proyecto. Las llamadas de contenido conectado se pueden almacenar en caché, pero esta solución no es escalable para una Campaign de alto tráfico.
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
Esta opción proporciona un método alternativo para transformar Google Sheets en objetos JSON consultados a través de contenido conectado. Al convertir una hoja de cálculo en una API JSON a través de SheetDB, puedes elegir entre [múltiples niveles de suscripción](https://sheetdb.io/pricing) dependiendo de la cadencia de las llamadas a la API.

La estructura de la hoja de cálculo sigue los pasos de la opción 4, pero SheetDB también proporciona [filtros adicionales](https://docs.sheetdb.io/#sheetdb-api) para consultar los objetos.

Algunos usuarios pueden preferir implementar SheetDB con menos dependencias de Liquid y bloques conectados implementando el [método de búsqueda](https://docs.sheetdb.io/#get-search-in-document) de SheetDB en llamadas de solicitud GET para filtrar los objetos JSON basándose en la etiqueta de Liquid {% raw %}`{{${language}}}`{% endraw %} para devolver automáticamente los resultados de un solo idioma en lugar de construir grandes bloques condicionales.

#### Paso 1: Formatea la hoja de Google {#step-1-format-the-google-sheet}

Primero, construye la hoja de Google de modo que los idiomas sean objetos diferentes:

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Paso 1: Formatea la hoja de Google" }

#### Paso 2: Usa la etiqueta de Liquid de idioma en una llamada de contenido conectado {#step-2-use-the-language-liquid-tag-in-a-connected-content-call}

A continuación, implementa la etiqueta de Liquid {% raw %}`{{${language}}}`{% endraw %} dentro de una llamada de contenido conectado. Ten en cuenta que SheetDB generará automáticamente el `sheet_id` al crear la hoja de cálculo.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Paso 3: Crea plantillas para tus mensajes {#step-3-template-your-messages}

Por último, usa Liquid para crear plantillas de tus mensajes:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Consideraciones {#considerations}

- El campo {% raw %}`{{${language}}}`{% endraw %} debe estar definido para todos los usuarios; de lo contrario, se debe incluir un bloque condicional de Liquid como controlador alternativo para los usuarios sin un idioma.
- El modelado de datos dentro de Google Sheets debe seguir una estructura vertical orientada por idioma, a diferencia de tener objetos de mensaje.
- SheetDB ofrece una cuenta gratuita limitada y múltiples opciones de pago que deben considerarse según tu estrategia de Campaign.
- Las llamadas de contenido conectado se pueden almacenar en caché. Recomendamos medir la cadencia proyectada de las llamadas a la API e investigar un enfoque alternativo de llamar al punto de conexión principal de SheetDB en lugar de usar el método de búsqueda.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}