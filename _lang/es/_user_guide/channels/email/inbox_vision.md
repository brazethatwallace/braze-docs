---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 7
description: "Esta página explica cómo configurar Inbox Vision, una característica que permite a los especialistas en marketing ver sus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles."
tool:
  - Dashboard
channel:
  - email
---

# Inbox Vision {#inbox-vision}

> Inbox Vision te permite ver tus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles. Por ejemplo, puedes probar las diferencias entre el modo oscuro y el modo claro para confirmar que tus correos electrónicos se muestran según lo previsto.

{% alert important %}
Es posible que Inbox Vision no funcione si el contenido de tu correo electrónico se basa en información de plantillas, como los datos del perfil de usuario. Braze crea una plantilla de usuario vacía al enviar correos electrónicos para esta característica.<br><br>Añade valores predeterminados a cualquier Liquid en tu mensaje de correo electrónico. Sin valores predeterminados, es posible que recibas un falso positivo o que la prueba falle.
{% endalert %}

## Consideraciones {#considerations}

En general, tu correo electrónico no funcionará con Inbox Vision si el contenido de tu correo electrónico depende de información con plantillas, como información del perfil de usuario. Esto se debe a que Braze utiliza un usuario vacío como plantilla cuando enviamos correos electrónicos con esta característica.

Puedes resolver esto añadiendo valores predeterminados o cualquier valor al Liquid en tu mensaje de correo electrónico antes de ejecutar Inbox Vision. Cuando termines de probar en Inbox Vision, aparecerá el mensaje de correo electrónico original. Si no se proporcionan valores, la prueba puede no renderizar las vistas previas correctamente.

Tu empresa tiene un límite en la cantidad de correos electrónicos que puedes previsualizar con Inbox Vision. Puedes monitorear esto en la pestaña **Email Previews** de Inbox Vision.

Incluye una línea del asunto y un dominio de envío válido para ver las vistas previas. Ten en cuenta las diferencias de renderización entre escritorio y dispositivo móvil. Usa las vistas previas para confirmar que el correo electrónico aparece como se esperaba.

{% alert note %}
Si al previsualizar una Campaign aparece un error de permisos, limpia tu caché y cookies, o prueba con una ventana de incógnito. Las extensiones del navegador a veces bloquean la vista previa.
{% endalert %}

Para probar tu mensaje de correo electrónico en Inbox Vision:

1. Ve a tu editor de arrastrar y soltar o editor HTML de correo electrónico.
2. En tu editor, selecciona **Preview & Test**.
3. Selecciona **Inbox Vision**.
4. Selecciona **Run Inbox Vision**. Esto tarda hasta diez minutos.
5. A continuación, selecciona un mosaico para ver la vista previa con más detalle. Estas vistas previas se agrupan en estas secciones: **Web Clients**, **Application Clients** y **Mobile Clients**.

![La opción para seleccionar clientes de correo electrónico para previsualizar.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Selecciona **Run Inbox Vision**. Esto puede tardar entre dos y diez minutos en completarse.

{% alert note %}
Inbox Vision no es compatible con mensajes de correo electrónico que incluyan [lógica de cancelación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) porque estos correos electrónicos se renderizan como contenido estático.
{% endalert %}

### Previsualizar como un usuario {#previewing-as-a-user}

Cuando previsualizas como un usuario aleatorio, Inbox Vision no guarda configuraciones ni atributos específicos del usuario (como nombre o preferencias). Cuando seleccionas un usuario personalizado, la vista previa de Inbox Vision puede diferir de otras vistas previas porque utiliza datos de usuario específicos.

## Análisis de código {#code-analysis}

El análisis de código resalta posibles problemas de HTML, muestra el número de ocurrencias e indica los elementos HTML no compatibles.

### Ver información del análisis de código {#viewing-code-analysis-information}

Encuentra esta información en la pestaña **Inbox Vision** seleccionando <i class="fas fa-list"></i> **Vista de lista**. La vista de lista solo está disponible para plantillas de correo electrónico HTML. Para las plantillas de arrastrar y soltar, usa las vistas previas para resolver los problemas en su lugar.

![Ejemplo de análisis de código en la vista previa de Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
El análisis de código puede aparecer más rápido que la vista previa para un cliente en particular, ya que Braze espera hasta que el correo electrónico llegue antes de tomar la captura de pantalla.
{% endalert %}

## Pruebas de correo no deseado {#spam-testing}

Las pruebas de correo no deseado estiman si un correo electrónico podría ser filtrado como correo no deseado. Las pruebas se ejecutan a través de filtros como IronPort, SpamAssassin y Barracuda, y filtros de ISP como Gmail y Outlook, utilizando buzones de entrada de prueba estáticos que no abren ni hacen clic de forma predeterminada.

{% alert important %}
La ubicación en el buzón de entrada depende principalmente de la participación de los destinatarios en vivo. Los resultados de las pruebas de correo no deseado pueden no coincidir con lo que observas en Campaigns reales.
{% endalert %}

Para obtener una lectura más clara sobre la capacidad de entrega, prueba el contenido con pequeñas cohortes en vivo: las aperturas y los clics sólidos son la señal más fiable. Utiliza las pruebas de correo no deseado como una entrada más junto con el monitoreo de la participación.

### Ver los resultados de las pruebas de correo no deseado {#viewing-spam-test-results}

Para consultar los resultados de tus pruebas de correo no deseado:

1. Selecciona la pestaña **Spam Testing** en la sección **Inbox Vision**. La tabla **Spam Test Result** muestra el nombre del filtro de correo no deseado, el estado y el tipo.
2. Revisa estos resultados y realiza los ajustes necesarios en tu campaña de correo electrónico.
3. Selecciona **Re-run Test** para volver a cargar los resultados de tus pruebas de correo no deseado.

## Pruebas de accesibilidad {#accessibility-testing}

Las pruebas de accesibilidad resaltan posibles problemas de accesibilidad en tu correo electrónico y muestran qué elementos no cumplen con los estándares. Braze analiza el contenido en función de las Pautas de Accesibilidad para el Contenido Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un conjunto de estándares reconocidos internacionalmente desarrollados por el W3C para hacer que el contenido web sea más accesible.

### Cómo funciona {#how-it-works}

Cuando ejecutas Inbox Vision, Braze comprueba automáticamente problemas comunes de accesibilidad en el [conjunto de reglas WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (como texto alternativo faltante, contraste de color insuficiente, estructura incorrecta de encabezados) y categoriza la gravedad para ayudarte a priorizar las correcciones. Ten en cuenta que, incluso cuando el texto alternativo está presente, [cómo se muestra]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) depende del cliente de correo electrónico del destinatario, no de Braze.

{% alert important %}
Las pruebas de accesibilidad pueden utilizarse para respaldar los esfuerzos de cumplimiento del cliente con regulaciones o leyes como la [Ley Europea de Accesibilidad](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); sin embargo, el cliente reconoce que Braze no hace representaciones ni garantías respecto a si el uso de las pruebas de accesibilidad satisface las obligaciones de cumplimiento del cliente, y renuncia a toda responsabilidad en relación con ello.
{% endalert %}

### Ver los resultados de las pruebas de accesibilidad {#viewing-accessibility-testing-results}

Las pruebas de accesibilidad generan resultados para cada regla como aprobado, fallido o necesita revisión en la pestaña **Pruebas de accesibilidad**. Braze categoriza cada regla utilizando POUR (Perceptible, Operable, Comprensible, Robusto), los cuatro principios detrás de WCAG.

#### Categorías POUR {#pour-categories}

Inbox Vision categoriza los problemas en los cuatro [principios POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) fundamentales: Perceptible, Operable, Comprensible y Robusto.

| Principio | Definición |
| --- | --- |
| Perceptible | La información y los componentes de la interfaz de usuario deben poder presentarse a los usuarios de maneras que puedan percibir.<br><br>Los usuarios deben ser capaces de percibir la información presentada (no puede ser invisible para todos sus sentidos). |
| Operable | Los componentes de la interfaz de usuario y la navegación deben ser operables.<br><br>Los usuarios deben poder operar la interfaz (la interfaz no puede requerir una interacción que un usuario no pueda realizar). |
| Comprensible | La información y el funcionamiento de la interfaz de usuario deben ser comprensibles.<br><br>Los usuarios deben poder comprender la información así como el funcionamiento de la interfaz de usuario (el contenido o el funcionamiento no pueden estar más allá de su comprensión). |
| Robusto | El contenido debe ser lo suficientemente robusto como para que pueda ser interpretado de manera fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías de asistencia.<br><br>Los usuarios deben poder acceder al contenido a medida que avanzan las tecnologías (a medida que las tecnologías y los agentes de usuario evolucionan, el contenido debe seguir siendo accesible). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Categorías POUR" }

#### Niveles de gravedad {#severity-levels}

Inbox Vision clasifica los problemas de accesibilidad por gravedad para ayudarte a priorizar la corrección.

| Estado | Definición |
| --- | --- |
| Crítico | Problemas que pueden bloquear el acceso al contenido o la funcionalidad para usuarios con discapacidades. Son los más graves y deben priorizarse para su corrección. |
| Grave | Problemas que pueden causar barreras significativas pero que pueden no bloquear completamente el acceso. Deben abordarse con prontitud. |
| Moderado | Problemas que pueden causar cierta dificultad a los usuarios con discapacidades, pero que tienen menos probabilidades de bloquear completamente el acceso. |
| Menor | Problemas que tienen un impacto relativamente bajo en la accesibilidad y que pueden causar solo una molestia menor. |
| Necesita revisión | No es posible detectar si podría haber un problema o no. Esto puede ocurrir cuando no se puede determinar la relación de contraste porque el texto está colocado sobre una imagen de fondo. Debes revisarlo manualmente porque no se puede determinar automáticamente. |
| Aprobado | Superó las prácticas recomendadas de accesibilidad o los niveles WCAG A y AA. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveles de gravedad" }

{% alert important %}
El editor de arrastrar y soltar no admite la configuración de un elemento `<title>` del documento, por lo que el escáner de accesibilidad siempre falla en esta comprobación.<br><br>Esta limitación está registrada para futuras mejoras. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="the drag-and-drop editor document title limitation in Inbox Vision" %}
{% endalert %}

### Comprender las pruebas de accesibilidad automatizadas {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## Buenas prácticas {#best-practices}

### Revisa tu lista de suscriptores de correo electrónico {#review-your-email-subscriber-list}

Consulta el [panel de información de correo electrónico]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-insights-dashboard) para determinar el tipo de dispositivo y los proveedores más populares donde tus suscriptores interactúan.

Si necesitas más granularidad, como el navegador, el modelo de dispositivo y más, puedes aprovechar tus datos de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) o el [generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para obtener este nivel de detalle sobre la interacción reciente de tus usuarios con el correo electrónico.

### Selecciona vistas previas significativas y vistas previas afectadas {#select-meaningful-previews-and-impacted-previews}

Si tu negocio está basado principalmente en EE. UU., puede haber vistas previas específicas, como vistas previas internacionales como GMX.de, que solo son utilizadas por un número nominal de usuarios. Recomendamos priorizar y optimizar para los buzones de entrada con un impacto considerable en los suscriptores y reservar tus vistas previas para buzones de entrada de mayor impacto.

Al realizar correcciones que afecten a vistas previas específicas, asegúrate de seleccionar solo las vistas previas afectadas para evitar consumir vistas previas no utilizadas.

### Ejecuta Inbox Vision en la versión final del correo electrónico {#run-inbox-vision-on-the-final-email-version}

Sugerimos ejecutar Inbox Vision cuando el mensaje de correo electrónico esté listo para producción o cerca de estarlo. Esto te permite reducir la cantidad de vistas previas generadas, ya que el correo electrónico pasa por múltiples iteraciones antes de ser finalizado y estar listo para enviarse a los usuarios.

Ejecutar Inbox Vision cada vez que realizas una sola edición o cambio puede consumir rápidamente las vistas previas. Sugerimos hacer todos los cambios necesarios en el correo electrónico primero y luego ejecutar Inbox Vision para previsualizar cómo todos tus cambios pueden afectar la representación de tu correo electrónico en distintos entornos.

Braze ejecuta pruebas a través de clientes de correo electrónico reales y trabaja para garantizar que las representaciones sean precisas. Braze utiliza de forma predeterminada las 20 vistas previas principales basadas en datos generales de la industria y de expertos, lo que cubre la mayoría de los entornos donde tus usuarios interactúan con tus correos electrónicos. Si tu análisis de datos apunta a otras vistas previas más populares, puedes definir un conjunto predeterminado de vistas previas cada vez que ejecutes Inbox Vision.

Si ves un problema de forma constante con un cliente, abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Solución de problemas con clientes que usan muchos iframes {#troubleshoot-iframe-heavy-clients}

Algunos clientes de correo electrónico, incluido GMX, renderizan los mensajes dentro de iframes y pueden eliminar o ignorar el CSS en los bloques `<style>`. Si Inbox Vision o los envíos en vivo muestran estilos faltantes en estos clientes:

- Usa diseños basados en tablas en lugar de diseños posicionados con CSS.
- Aplica los estilos críticos como atributos `style` en línea en los elementos afectados.
- Ten en cuenta que **Ocultar en escritorio** y **Ocultar en móvil** dependen de media queries en el bloque `<style>`, por lo que pueden no funcionar en estos clientes; el contenido oculto por viewport puede aparecer en ambas vistas.

Antes de enviar, prueba el mensaje actualizado en Inbox Vision con la vista previa del cliente afectado.

### Precisión de las pruebas frente a los buzones de entrada reales {#test-accuracy-versus-live-inboxes}

Un mensaje enviado puede verse diferente a la vista previa del editor porque los proveedores interpretan el mismo HTML de forma distinta. Descarga una copia del HTML enviado para comparar y usa CSS en línea cuando los clientes eliminen los bloques `<style>`.

#### Cuerpos de correo electrónico en blanco {#blank-email-bodies}

Si los destinatarios reportan cuerpos de correo electrónico en blanco pero aún pueden ver el nombre del remitente o la línea del asunto:

1. Confirma qué clientes de correo electrónico están afectados.
2. Usa Inbox Vision para probar la variante en esos clientes e identificar problemas de compatibilidad con HTML o CSS.
3. Si un cliente elimina los bloques `<style>`, agrega atributos `style` a los elementos HTML afectados. Para más información sobre el comportamiento del CSS en línea y sus limitaciones, consulta [CSS en línea]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline). En Gmail, demasiado CSS puede provocar que todo el bloque `<style>` sea descartado, lo cual es una causa común de cuerpos de correo electrónico en blanco.
4. En el editor HTML, también puedes activar **Enable inline CSS** en **Sending Info** > **Advanced** para aplicar las reglas de la hoja de estilos en línea a todo el mensaje. Esta opción no está disponible para correos electrónicos de arrastrar y soltar, que ya son procesados en línea por el editor.
5. Vuelve a probar en Inbox Vision antes de enviar futuras Campaigns.