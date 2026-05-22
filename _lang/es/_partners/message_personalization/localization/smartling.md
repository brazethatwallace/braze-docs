---
nav_title: Smartling
article_title: Smartling
description: "Este artículo de referencia describe la asociación entre Braze y Smartling, un software basado en la nube para la localización. El conector de Braze admite la traducción de plantillas de correo electrónico HTML, Content Blocks, Canvas y mensajes de correo electrónico de Campaign."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) es un software de extremo a extremo de gestión de la traducción en la nube para clientes que buscan automatizar la traducción de sitios web, aplicaciones y experiencias del cliente.

_Esta integración está mantenida por Smartling._

## Sobre la integración {#about-the-integration}

El conector de Braze admite traducciones para mensajes en Campaigns y Canvas (correo electrónico, push, mensajes dentro de la aplicación y banners), plantillas de correo electrónico y Content Blocks. Consulta la tabla siguiente para conocer qué tipos de editor son compatibles con cada canal o característica.

| Canal/Característica | Editor tradicional (ej. HTML) | Editor de arrastrar y soltar |
| --------------- | ----------------------------- | -------------------- |
| [Correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | n/a |
| Plantilla de correo electrónico | ✅ | ✅ |
| Banners | n/a | ✅ |
| Content Blocks | ✅ | ✅ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="About the integration" }


## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cuenta de Smartling | Se necesita una [cuenta de Smartling](https://dashboard.smartling.com/) para beneficiarse de esta asociación. |
| Proyecto de traducción de Smartling | Para conectar tu cuenta de Braze con Smartling, primero debes registrarte y [crear un proyecto de traducción](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Clave de API REST de Braze | Una clave de API REST de Braze con los siguientes permisos: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Se puede crear en el dashboard de Braze desde **Settings > API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto de conexión depende de la URL de Braze de tu instancia. |
| Configuración multilingüe de Braze | [Completa la configuración multilingüe en Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

### Paso 1: Establecer la configuración multilingüe en Braze {#step-1-set-up-multi-language-settings-in-braze}

Consulta [las instrucciones de configuración multilingüe de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) para configurar las localizaciones en Braze.

### Paso 2: Configurar el proyecto de Braze en Smartling TMS {#step-2-set-up-the-braze-project-in-smartling-tms}

Consulta la [documentación de Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) para más detalles sobre la configuración del conector.

### Conexión de Braze a Smartling {#connecting-braze-to-smartling}

1. En tu [cuenta de Smartling](https://dashboard.smartling.com/), crea un tipo de proyecto de [conector de Braze](https://help.smartling.com/hc/en-us/articles/115003074093).

![Conexión de Braze en Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. En este proyecto, selecciona **Settings** > **Braze Settings** > **Connect to Braze**.
3. Rellena los campos obligatorios, como la URL de la API y la clave de API. Si la conexión de prueba se realiza correctamente, guarda la conexión. Si la prueba no tiene éxito, confirma que has introducido la URL y la clave de API correctas.

![Conexión de Braze en la configuración de la API de Smartling.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. Añade idiomas adicionales al proyecto.

![Conexión de Braze en idiomas de proyecto de Smartling.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. En la configuración de Braze, comprueba que los valores de la columna **Target Language (Braze)** coinciden con las localizaciones configuradas en la configuración multilingüe de Braze. La convención de nomenclatura de la localización debe coincidir exactamente.

![Conexión de Braze en la confirmación de idioma de Smartling.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Paso 3: Añadir etiquetas de traducción a tu mensaje de Braze {#step-3-add-translation-tags-to-your-braze-message}

Consulta [las instrucciones de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) sobre cómo añadir etiquetas de traducción a tus mensajes:

- [Correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Aquí tienes un ejemplo de una Campaign de correo electrónico HTML con etiquetas de traducción.

![Correo electrónico de Braze con etiquetas de traducción.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Debes guardar el mensaje como borrador antes de poder seleccionar las localizaciones.

### Paso 4: Gestionar las traducciones en Smartling {#step-4-manage-translations-in-smartling}

Después de conectar y configurar el conector de Braze, busca el contenido de Braze en la pestaña Braze de tu proyecto de Smartling. Para más información, consulta la [documentación de Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

Smartling ofrece funciones avanzadas para buscar y seleccionar contenido por:
- Búsqueda por palabra clave
- Tipo de contenido de Braze
- Etiquetado de Braze

1. En este ejemplo, la Campaign de correo electrónico de promoción de Año Nuevo se creó en el [paso 3](#step-3-add-translation-tags-to-your-braze-message).

![Correo electrónico de Braze con etiquetas de traducción.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. Después de localizar la Campaign que quieres traducir, selecciona la carpeta, elige las variantes y selecciona **Request Translation**.

![Solicitar traducciones.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. Crea un nuevo trabajo para la traducción.

![Crea un nuevo trabajo para la traducción.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. Una vez autorizado el trabajo, edita cada traducción en la herramienta TAO.

![Herramienta TAO de traducción.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. Una vez completadas las traducciones, guárdalas y envíalas a Braze.

![Enviar la traducción a Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Paso 5: Vista previa del mensaje como usuario multilingüe en Braze {#step-5-preview-the-message-as-a-multi-language-user-in-braze}

En Braze, obtén una vista previa de tu Campaign como usuario multilingüe para confirmar que las traducciones se aplican correctamente.

![Vista previa de usuario multilingüe.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Preguntas más frecuentes {#frequently-asked-questions}

### ¿Son compatibles las etiquetas de traducción con el editor de arrastrar y soltar? {#are-translation-tags-supported-for-the-drag-and-drop-editor}

Para el editor de arrastrar y soltar (correo electrónico, bloque de contenido, mensaje dentro de la aplicación), debes añadir manualmente las etiquetas de traducción como etiquetas de Liquid.

### ¿Cómo se traduce el texto dentro de una etiqueta de Liquid? {#how-do-you-translate-text-within-a-liquid-tag}

Smartling reconoce las etiquetas de Liquid y las convierte en variables no editables en el compositor. Cualquier otro texto dentro de la etiqueta de Liquid, como el texto predeterminado o filtros como join, tampoco se puede editar en Smartling. Sin embargo, puedes eliminar la etiqueta de Liquid en Smartling y volver a crear la etiqueta de Liquid con el texto predeterminado traducido. Aparece una advertencia al guardar la traducción.