---
nav_title: Crowdin
article_title: Crowdin
description: "Usa la integración de Crowdin para traducir Campaigns, experiencias de Canvas, plantillas de correo electrónico y Content Blocks con Translation Memory, glosarios y traducción automática."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/) es una plataforma de gestión de localización impulsada por IA que ayuda a los equipos a automatizar la traducción de su software, aplicaciones y contenido de marketing.

Conecta Crowdin a Braze para gestionar las traducciones de tus Campaigns y experiencias de Canvas. La sincronización automatizada funciona con traducción automática, Translation Memory y glosarios para que los flujos de trabajo humanos y automatizados se mantengan consistentes.

_Esta integración está mantenida por Crowdin._

## Sobre la integración {#about-the-integration}

Crowdin ofrece dos aplicaciones para Braze: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) y [Braze Email Templates](https://store.crowdin.com/braze-app). Elige según las características de Braze que necesites localizar. La siguiente tabla las compara.

### Elige la aplicación de Crowdin adecuada {#choose-the-right-crowdin-app}

| Canal o característica | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campaigns** | ✅ Compatible | ❌ No compatible |
| **Pasos en Canvas** | ✅ Compatible | ❌ No compatible |
| **Plantillas de correo electrónico** | ❌ No compatible | ✅ Compatible |
| **Content Blocks** | ❌ No compatible | ✅ Compatible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Elige la aplicación de Crowdin adecuada" }

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| **Cuenta de Crowdin** | Se necesita una [cuenta en Crowdin.com](https://accounts.crowdin.com/register) o una [cuenta de Crowdin Enterprise](https://accounts.crowdin.com/workspace/create). |
| **Proyecto de Crowdin** | Antes de conectar Braze, [crea un proyecto de traducción](https://support.crowdin.com/creating-project/) en Crowdin o Crowdin Enterprise. |
| **Clave de API REST de Braze** | Una clave de API REST de Braze con permisos para Campaigns, Canvas, Content Blocks, atributos personalizados, correo electrónico y plantillas. |
| **Endpoint REST de Braze** | La URL específica de tu endpoint REST de Braze (por ejemplo, `https://rest.iad-03.braze.com`). |
| **Configuración multilingüe de Braze** | Los locales deben estar configurados en tu panel de Braze en **Configuración** > **Configuración de localización**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de Braze Campaigns & Canvas {#braze-campaigns-canvas-integration}

Si localizas contenido dentro de mensajes en vivo, usa la [aplicación Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) para sincronizar las cadenas traducibles de tus borradores de Campaign y Canvas con el soporte multilingüe de Braze.

Para un recorrido en video, consulta [Integración de Braze Campaigns & Canvas](https://youtu.be/ahG1ET4VRKA).

### Paso 1: Configura los ajustes multilingües en Braze {#step-1-set-up-multi-language-settings-in-braze}

Antes de conectar Crowdin, añade tus idiomas de destino en Braze.

1. En Braze, ve a **Configuración** > **Configuración de localización**.
2. Añade los idiomas que planeas soportar.

![Página de locales de Braze en Configuración, mostrando nombres de locales, claves de locales y Añadir locale.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Anota cada **clave de locale** (por ejemplo, `en-US`, `fr-FR`, `es-ES`). Usarás estos valores cuando mapees los idiomas en Crowdin.

### Paso 2: Configura el proyecto de Braze en Crowdin {#step-2-set-up-the-braze-project-in-crowdin}

1. En tu cuenta de Crowdin Enterprise o Crowdin.com, ve a la **Tienda** en el menú de navegación.
2. Busca **Braze Campaigns & Canvas** y selecciona **Install**.

![Tienda de Crowdin con Braze Campaigns & Canvas seleccionado e Install resaltado.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Selecciona el proyecto (o proyectos) donde quieras usar esta integración.
4. Para abrir la integración, ve a **Integrations** > **Braze Campaigns & Canvas** en tu proyecto.

#### Conectar Braze a Crowdin {#connecting-braze-to-crowdin}

Autoriza la conexión con tus credenciales de API de Braze:

![Formulario de conexión de Crowdin Braze Campaigns & Canvas con clave de API REST, endpoint REST y Log in with Braze Campaigns & Canvas.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Clave de API REST de Braze:** Créala en Braze en **Configuración** > **API e identificadores** > **Claves de API**. Otorga los permisos que necesita esta integración (Campaigns, Canvas, Content Blocks y atributos personalizados).
- **Endpoint REST de Braze:** Introduce la URL de tu instancia de Braze (por ejemplo, `https://rest.iad-03.braze.com`). Para más información, consulta [Endpoints de la REST API]({{site.baseurl}}/api/basics#endpoints).

![Página de claves de API REST de Braze con Crear clave de API y el control de copia del endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Selecciona **Log in with Braze Campaigns & Canvas**.

### Paso 3: Configura el mapeado de idiomas en Crowdin {#step-3-configure-language-mapping-in-crowdin}

Después de conectar tu cuenta, mapea cada idioma del proyecto de Crowdin con el locale correspondiente de Braze.

1. En el panel de la integración **Braze Campaigns & Canvas**, selecciona el icono de engranaje de **Settings** en la barra de acciones superior.

![Pantalla de la integración Braze Campaigns & Canvas con Settings en la barra de acciones superior.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Abre la pestaña **General Settings**.
3. Introduce las claves de locale. Crowdin lista los idiomas de tu proyecto (por ejemplo, francés, italiano). En cada campo, introduce la **clave de locale de Braze** correspondiente.
   - Por ejemplo, si Braze usa `it` para italiano, introduce `it` junto a italiano en Crowdin.
   - Cada entrada debe coincidir exactamente con la **clave de locale** de ese locale en la **Configuración de localización** de Braze.

![Modal de configuración en la pestaña General Settings, mostrando campos de filtro de archivos y filas de mapeado de idiomas (por ejemplo, francés mapeado a fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Selecciona **Save** para confirmar el mapeado.

### Paso 4: Añade etiquetas de traducción a tu mensaje de Braze {#step-4-add-translation-tags-to-your-braze-message}

Crowdin lee las mismas **etiquetas de traducción** Liquid que Braze usa para mensajes multilingües. Añade {% raw %}`{% translation your_id_here %}` y `{% endtranslation %}`{% endraw %} alrededor de cada fragmento de texto, URL de imagen o URL de enlace que quieras traducir. Cada bloque necesita un `id` único (por ejemplo, `greeting` o `welcome_header`).

**Ejemplo:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Para HTML, Liquid en enlaces y otros patrones, sigue las mismas reglas que en [Traducción de locales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) (por ejemplo, mantén las etiquetas alrededor de los segmentos más pequeños posibles y envuelve solo las partes específicas del idioma en las URL al localizar enlaces).

Guarda tu mensaje de Braze como **borrador** antes de que Crowdin pueda detectar y extraer el contenido.

### Paso 5: Gestiona las traducciones en Crowdin {#step-5-manage-translations-in-crowdin}

La pantalla de la integración tiene dos lados:

- **Panel de Braze:** Tus Campaigns y Canvas.
- **Panel de Crowdin:** Contenido ya sincronizado para traducción.

![Paneles de Crowdin y Braze Campaigns & Canvas con carpetas para Campaigns y locales, Sync to Braze y Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Sincronizar contenido {#syncing-content}

1. En el panel de **Braze**, selecciona la casilla de la Campaign o Canvas que quieras traducir.
2. Selecciona **Sync to Crowdin**.
3. Cuando la sincronización se complete, el archivo aparecerá en el panel de **Crowdin**. Los traductores pueden abrir las cadenas en el Editor de Crowdin.

#### Devolver las traducciones a Braze {#returning-translations-to-braze}

1. Cuando las traducciones estén al 100 % en Crowdin, vuelve a la pestaña **Integrations**.
2. Selecciona el contenido completado en el panel de **Crowdin**.
3. Selecciona **Sync to Braze**. Esto envía las cadenas traducidas a las variantes de idioma correspondientes en tu Campaign de Braze.

### Paso 6: Previsualiza el mensaje como un usuario multilingüe en Braze {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

Para confirmar la integración:

1. Abre tu Campaign en el **creador de mensajes de Braze**.
2. Ve a la pestaña **Test**.
3. Selecciona **Preview Message as User**.
4. Busca un perfil de usuario que tenga un atributo `language` que coincida con uno de tus locales traducidos.
5. Confirma que el contenido cambia del idioma de origen a la versión traducida.

## Integración de Braze Email Templates {#braze-email-templates-integration}

Si localizas correo electrónico a nivel de plantilla, usa la [aplicación Braze Email Templates](https://store.crowdin.com/braze-app) para sincronizar el HTML de tu biblioteca de medios de Braze.

Para un recorrido en video, consulta [Integración de Braze Email Templates](https://youtu.be/g0YMKW3jEjk).

### Paso 1: Instala la aplicación {#step-1-install-the-app}

1. En tu proyecto de Crowdin, ve a la pestaña **Store**.
2. Busca **Braze Email Templates** y selecciona **Install**.

![Tienda de Crowdin con Braze Email Templates seleccionado e Install resaltado.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Selecciona el proyecto (o proyectos) donde quieras usar esta integración.
4. Para abrir la integración, ve a **Integrations** > **Braze Email Templates** en tu proyecto.

### Paso 2: Conectar a Braze {#step-2-connect-to-braze}

Autoriza la conexión con tus credenciales de API de Braze:

![Formulario de conexión de Crowdin Braze Email Templates con clave de API REST, endpoint REST y Log in with Braze Email Templates.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Clave de API REST de Braze:** Otorga permisos de `templates.email` y `content_blocks` (lectura y escritura). Crea la clave en Braze en **Configuración** > **API e identificadores** > **Claves de API**.

![Página de claves de API REST de Braze con Crear clave de API y el control de copia del endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Para el **endpoint REST de Braze**, usa la URL específica de tu instancia (por ejemplo, `https://rest.iad-03.braze.com`).
3. Selecciona **Log in with Braze Email Templates**.

### Paso 3: Sincroniza el contenido para traducción {#step-3-sync-content-for-translation}

La pantalla de la integración muestra tu biblioteca de Braze:

- **Panel de Braze:** **Plantillas de correo electrónico** y **Content Blocks** que puedes sincronizar.
- **Panel de Crowdin:** Contenido en traducción.

1. En el panel de **Braze**, selecciona la casilla junto a las plantillas o bloques que quieras localizar.
2. Selecciona **Sync to Crowdin**.
3. Crowdin extrae el código HTML fuente. Los traductores trabajan en el Editor de Crowdin con una **vista previa WYSIWYG** en vivo para que el diseño se mantenga intacto.

![Pestaña de vista previa del Editor de Crowdin mostrando HTML de correo electrónico localizado y cadenas traducibles.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Paso 4: Entrega las plantillas traducidas {#step-4-deliver-translated-templates}

Cuando las traducciones alcancen el 100 % de completitud:

1. Selecciona los archivos completados en el panel de **Crowdin**.
2. Selecciona **Sync to Braze**.
3. Crowdin crea automáticamente versiones localizadas de estos activos en tu biblioteca de medios de Braze (por ejemplo, `Template_Name_fr`).

![Paneles de Crowdin y Braze Email Templates listando plantillas de correo electrónico y Content Blocks, con Sync to Braze y Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})