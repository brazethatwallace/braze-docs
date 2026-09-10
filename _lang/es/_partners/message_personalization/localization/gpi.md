---
nav_title: GPI
article_title: Globalization Partners International
date_published: "2026-09-09"
description: "Este artículo de referencia describe la asociación entre Braze y Globalization Partners International (GPI), un proveedor de servicios de traducción. El conector GPI Translation Services Connector extrae contenido de Braze para su traducción e importa las traducciones completadas a través de la API de traducción de Braze."
alias: /partners/gpi/
page_type: partner
search_tag: Partner
---

# Globalization Partners International

> [Globalization Partners International](https://www.globalizationpartners.com/) (GPI) proporciona el conector GPI Translation Services Connector para Braze. El conector extrae contenido de Campaigns, Canvas, plantillas de correo electrónico y Content Blocks para su traducción, y luego importa las traducciones completadas de vuelta a Braze a través de la API de traducción. GPI admite traducción humana, traducción impulsada por IA y traducción con IA con posedición experta en más de 200 idiomas.

_Esta integración es mantenida por Globalization Partners International._

## Acerca de la integración {#about-the-integration}

El conector GPI Translation Services Connector se integra con el modelo multilingüe nativo de Braze y la API de traducción. Puedes extraer contenido traducible desde el portal de traducción de GPI, enviarlo a GPI para su traducción e importar las traducciones terminadas de vuelta a Braze sin necesidad de copiar y pegar manualmente. GPI preserva las etiquetas de Liquid y la personalización durante todo el flujo de trabajo.

## Ejemplos {#use-cases}

### Lanzamiento de campaña global {#global-campaign-launch}

Selecciona Campaigns, Canvas o plantillas de correo electrónico en Braze, establece los idiomas de origen y destino, y envía el contenido a GPI para traducción profesional humana. GPI se encarga de la localización y el aseguramiento de calidad en vistas previas de borrador antes del lanzamiento.

### Localización urgente o de alto volumen {#time-sensitive-or-high-volume-localization}

Envía ventas flash, mensajes de ciclo de vida urgentes o grandes lotes de Content Blocks a través del conector para recibir traducciones importadas de vuelta a Braze automáticamente. El tiempo de entrega depende del flujo de trabajo que elijas y puede variar desde semanas hasta minutos.

### Soporte de internacionalización {#internationalization-support}

GPI proporciona orientación sobre formato y mejores prácticas para la localización de Braze, incluyendo idiomas de derecha a izquierda (RTL) como árabe, hebreo y persa.

### Localización continua a escala {#ongoing-localization-at-scale}

GPI utiliza memoria de traducción para reutilizar traducciones anteriores y mantener la consistencia terminológica y de estilo, y para reducir costos en coincidencias exactas, repetidas y parciales. Actualiza las campañas en el idioma de origen en Braze y envía el contenido revisado a GPI para actualizar las traducciones correspondientes.

## Requisitos previos {#prerequisites}

Antes de comenzar, necesitas lo siguiente:

| Requisito previo | Descripción |
| --- | --- |
| Una cuenta de Globalization Partners International | Se requiere una cuenta de GPI para usar esta integración. |
| Una clave de API REST de Braze | Una clave de API REST de Braze con los siguientes permisos:<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br>- `content_blocks.list`<br>- `content_blocks.info`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.list`<br>- `templates.email.info`<br>- `templates.email.translations.get`<br>- `templates.email.translations.update`<br><br>Crea esta clave en el panel de Braze desde **Configuración** > **APIs e identificadores** > **Claves de API**. Para más información, consulta [Crear claves de API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Un endpoint REST de Braze | [La URL de tu endpoint REST]({{site.baseurl}}/api/basics#endpoints). Tu endpoint depende de la URL de Braze para tu instancia. |
| Configuración multilingüe de Braze | Los idiomas de destino deben estar configurados en Braze en **Configuración** > **Configuración de localización**. Para más información, consulta [Configuración multilingüe]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear una clave de API REST de Braze {#step-1-create-a-braze-rest-api-key}

1. En Braze, ve a **Configuración** > **APIs e identificadores** > **Claves de API**.
2. Crea una clave de API REST con los permisos listados en [Requisitos previos](#prerequisites).
3. Copia la clave de API y anota el endpoint REST de tu instancia.

### Paso 2: Enviar la configuración a GPI {#step-2-send-settings-to-gpi}

1. Envía tu clave de API y el endpoint REST a tu director de cuentas de GPI.
2. Envía la lista de usuarios que necesitan acceso al conector para que GPI pueda habilitarlo para ellos.
3. GPI configura el conector con tus credenciales y valida la conexión.

### Paso 3: Configurar los ajustes de localización en Braze {#step-3-configure-localization-settings-in-braze}

1. En Braze, ve a **Configuración** > **Configuración de localización** y confirma que tus idiomas de destino estén habilitados.
2. Confirma que el contenido que envías para traducción tenga los idiomas requeridos habilitados. El contenido sin idiomas habilitados no puede recibir traducciones importadas.
3. Agrega [etiquetas de Liquid para traducción]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) alrededor del contenido que necesita traducción.
4. Para idiomas RTL, agrega etiquetas de Liquid para admitir la dirección del contenido según el idioma. Evita directivas de estilo de alineación a menos que confirmes que no afectan la representación RTL.

## Usar GPI con Braze {#use-gpi-with-braze}

Solo el contenido en estado de borrador o borrador posterior al lanzamiento puede traducirse en Braze.

### Paso 1: Exportar contenido para traducción {#step-1-export-content-for-translation}

1. En el [portal de traducción de GPI](https://www.translationportal.com), abre el conector **Braze** y selecciona **New Request**.
2. Completa la pestaña **Information** y luego abre la pestaña **Content**. Desde **Categories**, selecciona **Campaign**, **Canvas**, **Email Template** o **Content Block**, y luego selecciona los elementos a exportar.
3. Selecciona **Submit** para enviar una solicitud de cotización a GPI. Tu director de cuentas de GPI te contactará cuando la cotización esté lista para revisión y aprobación.

### Paso 2: Importar traducciones a Braze {#step-2-import-translations-into-braze}

1. En el conector **Braze**, localiza el proyecto que deseas importar.
2. Selecciona el icono **Import** en la columna **Actions**.
3. Espera el mensaje de confirmación de importación. Consulta el estado del trabajo de importación en la página **Jobs**.

### Paso 3: Verificar el estado de la solicitud de traducción {#step-3-check-translation-request-status}

1. Ve al [portal de traducción de GPI](https://www.translationportal.com).
2. Selecciona **Sign In** e ingresa tus credenciales.
3. En la navegación del portal de traducción de GPI, selecciona **Braze** para abrir el panel del conector. Revisa las tablas **Quotes** y **Projects** para ver el estado de solicitudes y proyectos.

### Paso 4: Previsualizar traducciones en Braze {#step-4-preview-translations-in-braze}

Después de importar las traducciones, previsualízalas en Braze:

1. Abre la pantalla **Edit** de la campaña o el mensaje que tradujiste.
2. En el **creador de mensajes**, ve a la pestaña **Preview and Test** o **Test**.
3. En **Preview message as user**, selecciona **Multi-language user** y luego selecciona el idioma que deseas ver.
4. Confirma la vista previa en el idioma de destino. Para compartir con revisores externos, genera un enlace de vista previa.

## Consideraciones {#considerations}

- El conector GPI Translation Services Connector para Braze se distribuye sin costo.

## Solución de problemas {#troubleshooting}

Para obtener asistencia con el conector GPI Translation Services Connector para Braze o cualquier proyecto de traducción de GPI, contacta a tu gestor de proyectos de GPI, llama al +1-866-272-5874 o envía un correo electrónico a [support@globalizationpartners.com](mailto:support@globalizationpartners.com).