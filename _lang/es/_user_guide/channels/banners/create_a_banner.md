---
nav_title: "Crear un banner"
article_title: "Crear un banner"
page_order: 1
description: "Este artículo de referencia explica cómo crear, redactar, configurar y enviar banners usando Campaigns y Canvas de Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Crear un banner {#create-a-banner}

> Aprende a crear banners cuando construyes Campaigns y Canvas en Braze. Para información más general, consulta [Acerca de los banners]({{site.baseurl}}/user_guide/channels/banners).

## Requisitos previos {#prerequisites}

Antes de poder lanzar tu Banner, tu equipo de desarrollo debe [configurar las ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements). Mientras tanto, puedes redactar el borrador de tu campaña de Banner, pero no podrás lanzar la campaña hasta que las ubicaciones estén configuradas.

## Crea un mensaje Banner {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Paso 2: Elige dónde crear tu mensaje {#step-2-choose-where-to-build-your-message}

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las Campaigns son mejores para campañas de mensajería únicas y segmentadas, mientras que los Canvas son mejores para recorridos de usuario con múltiples pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **Banner**.
3. Nombra tu campaña de forma clara y significativa.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario. Las etiquetas facilitan encontrar tus campañas y crear informes a partir de ellas. Por ejemplo, al usar el generador de informes, puedes filtrar por las etiquetas relevantes.
5. Selecciona la ubicación que creaste previamente para asociarla a tu campaña.
6. Añade variantes según sea necesario. Puedes elegir un tipo de mensaje y diseño diferente para cada una. Para más información sobre variantes, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Elige una fecha y hora de inicio para tu campaña de Banner. De forma predeterminada, los Banners duran indefinidamente. Puedes cambiar esto seleccionando **Hora de finalización** y especificando una fecha y hora de finalización.

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o tienen el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando el creador de Canvas.
2. Después de configurar tu Canvas, añade un paso de mensaje en el constructor de Canvas. Nombra tu paso de forma clara y significativa.
3. Selecciona **Banner** como tu canal de mensajería.
4. Selecciona una ubicación para el Banner.
5. Establece la prioridad. La [prioridad de Banner]({{site.baseurl}}/user_guide/channels/banners#priority) determina el orden en que se muestran los Banners si comparten la misma ubicación.
6. Establece una expiración para el Banner. Puede ser después de un periodo de tiempo tras la disponibilidad del paso o en una fecha y hora específicas. La duración máxima de expiración es de 31 días después de que el paso esté disponible para el usuario.

{% endtab %}
{% endtabs %}

### Paso 3: Redacta un Banner {#compose-a-banner}

A continuación, elige cómo quieres empezar a construir:

- **Editor de arrastrar y soltar:** Comienza con un Banner en blanco y construye visualmente con bloques y filas.
- **Editor HTML:** Comienza con un Banner en blanco y trabaja directamente en HTML.
- **Plantillas:** Abre la biblioteca de plantillas y selecciona un diseño de **Plantillas de Braze** o **Tus plantillas**. Las plantillas se abren en el editor de arrastrar y soltar para su personalización.

![Opciones para elegir el editor de arrastrar y soltar, el editor HTML o las plantillas para tu Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Paso 3.1: Aplica estilos al Banner {#step-31-style-the-banner}

{% tabs %}
{% tab Editor de arrastrar y soltar %}

Puedes arrastrar y soltar bloques y filas en el área del lienzo para empezar a construir tu mensaje. Para una referencia de los bloques del editor de Banner y enlaces a los detalles de propiedades compartidas, consulta [Bloques de editor (Banners)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para personalizar las propiedades de fondo de tu mensaje, la configuración de bordes y más, selecciona **Estilos**. Si solo quieres personalizar el estilo de un bloque o fila específica, selecciónalo para hacer cambios.

![Panel de estilos del creador de Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='banner' %}

{% endtab %}
{% tab Editor HTML %}

El editor HTML es ideal para equipos que ya mantienen sus propias plantillas HTML o que desean tener control total sobre el marcado y los estilos. Puedes escribir o pegar HTML personalizado directamente en el editor. Las etiquetas de personalización Liquid son totalmente compatibles, por lo que puedes hacer referencia a atributos de usuario, atributos personalizados, elementos de catálogo y más.

{% alert tip %}
¿Necesitas ayuda para crear el HTML de tu Banner? Selecciona **Ask Operator** en el editor HTML y describe el Banner que deseas. [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) genera HTML que puedes revisar e insertar en el editor. Para más información, consulta [Generar mensajes]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).
{% endalert %}

Para el seguimiento de clics y descartes en tu HTML personalizado, debes llamar a los métodos del puente JavaScript de forma explícita. Para la referencia completa, consulta [Código personalizado y puente JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code).

{% endtab %}
{% endtabs %}

{% alert note %}
Para dirigirte a usuarios en diferentes idiomas dentro de una sola campaña de Banner, consulta [Mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Paso 3.2: Define el comportamiento al hacer clic (opcional) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab Editor de arrastrar y soltar %}

Cuando un usuario hace clic en un enlace del Banner, puedes elegir navegarlo más profundamente en tu aplicación o redirigirlo a otra página web. Además, puedes elegir [registrar un atributo o evento personalizado]({{site.baseurl}}/developer_guide/analytics), lo que actualiza el perfil de tu usuario con datos personalizados cuando hace clic en el Banner. Para un seguimiento de clics más granular, asigna un identificador personalizado a cada elemento interactivo usando el campo **Identificador para informes** en su panel de propiedades.

{% alert important %}
{::nomarkdown}
El comportamiento al hacer clic puede ser anulado si un elemento específico (como un botón, enlace o imagen del Banner) tiene su propio comportamiento al hacer clic. Por ejemplo, dados los siguientes comportamientos al hacer clic:<br><ul><li>Un Banner tiene un comportamiento al hacer clic que redirige a la página de inicio de un sitio web.</li><li>Una imagen en el Banner tiene un comportamiento al hacer clic que redirige a la página de productos de un sitio web.</li></ul>Si un usuario hace clic en la imagen, es redirigido a la página de productos. Sin embargo, hacer clic en el área circundante del Banner lo redirige a la página de inicio.
{:/}
{% endalert %}

{% endtab %}
{% tab Editor HTML %}

En el editor HTML, el seguimiento de clics no es automático. Debes llamar a `brazeBridge.logClick()` desde tu HTML para cada elemento clicable que desees rastrear. Por ejemplo:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

Para la referencia completa del puente JavaScript, consulta [Código personalizado y puente JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Paso 3.3: Configura el comportamiento de descarte (opcional) {#dismiss-behavior}

{% alert important %}
Los descartes de Banner requieren las siguientes versiones mínimas del SDK or kit de desarrollo de software. Las versiones anteriores del SDK or kit de desarrollo de software no renderizan Banners con el descarte habilitado.
{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 reactnative:22.0.0 flutter:20.0.0 %}
{% endalert %}

{% tabs %}
{% tab Editor de arrastrar y soltar %}

Selecciona la casilla **El Banner puede ser descartado** en la sección **Comportamiento de descarte** para permitir que los usuarios descarten el Banner. Esto es útil cuando deseas promover una oferta por tiempo limitado a una audiencia amplia, pero aún así permitir que los usuarios no interesados oculten el mensaje.

Cuando el descarte está activado, puedes personalizar el botón de descarte en la sección **Comportamiento de descarte**:

| Configuración | Descripción |
|---------|-------------|
| **Tamaño del botón** | El tamaño del botón de descarte que se muestra en el Banner. |
| **Color del botón** | El color del botón de descarte. |
| **Etiqueta ARIA** | La etiqueta accesible para el botón de descarte, utilizada por lectores de pantalla. Si se deja en blanco, el valor predeterminado es "Cerrar". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración del botón de descarte" }

Cuando un usuario descarta un Banner, este no aparece de nuevo para ese usuario, incluso si aún cumple con los criterios de segmentación de la campaña.

{% endtab %}
{% tab Editor HTML %}

En el editor HTML, el descarte se gestiona en tu HTML usando `brazeBridge.closeMessage()`. Combínalo con `brazeBridge.logClick()` para también rastrear la acción de descarte como un evento de clic. Por ejemplo:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

Cuando un usuario descarta un Banner de esta forma, este no aparece de nuevo para ese usuario, incluso si aún cumple con los criterios de segmentación de la campaña.

Para la referencia completa del puente JavaScript, consulta [Código personalizado y puente JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Paso 3.4: Añade propiedades personalizadas (opcional) {#custom-properties}

Puedes añadir propiedades personalizadas a un Banner para adjuntar metadatos estructurados, como cadenas u objetos JSON. Estas propiedades no afectan cómo se muestra el Banner, pero se pueden [acceder a través del SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/banners/placements) para modificar el comportamiento o la apariencia de tu aplicación. Por ejemplo, podrías:

{% multi_lang_include banners/metadata_use_cases.md %}

Las propiedades personalizadas funcionan de la misma forma tanto en el editor de arrastrar y soltar como en el editor HTML. Para añadir una propiedad personalizada, selecciona **Configuración** > **Propiedades** > **Añadir propiedad**.

![La página de propiedades mostrando la opción de añadir la primera propiedad personalizada a una campaña de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propiedad que desees añadir, completa lo siguiente:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Tipo de propiedad | El tipo de datos para la propiedad. Los tipos compatibles incluyen cadena, booleano, número, marca de tiempo, URL de imagen y objeto JSON. | String |
| Clave de propiedad | El identificador único para la propiedad. Esta clave se utiliza en el SDK or kit de desarrollo de software para acceder a la propiedad. | `color` |
| Valor | El valor asignado a la propiedad. Debe coincidir con el tipo de propiedad seleccionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 3.4: Añade propiedades personalizadas (opcional)" }

Cuando hayas terminado, selecciona **Listo**.

![La página de propiedades con una propiedad de tipo cadena con una clave de color y un valor de #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

#### Paso 3.5: Personaliza con contenido conectado (opcional) {#step-35-personalize-with-connected-content-optional}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Debido a que los Banners se renderizan de forma integrada durante una actualización de sesión, el contenido conectado en este canal funciona de manera diferente que en otros canales:

- Solo se admiten solicitudes GET.
- Todas las ubicaciones en una sola actualización (hasta 10) comparten un presupuesto de renderizado de aproximadamente dos segundos. Si una llamada es lenta, se agota el tiempo o se excede el presupuesto, el resultado del contenido conectado para esa ubicación se trata como nulo. Los Banners no reintentan.

Para obtener los mejores resultados:

- Mantén tus endpoints rápidos y [almacena en caché las respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) siempre que sea posible.
- Limita el número de URLs únicas de contenido conectado en las ubicaciones que se renderizan juntas.
- Evita encadenar llamadas donde una respuesta de contenido conectado determina la URL para la siguiente. Cada llamada adicional se suma al presupuesto compartido.
- Usa instrucciones de protección Liquid o el [filtro `default`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) para manejar resultados nulos y evitar Banners en blanco.

### Paso 4: Construye el resto de tu campaña o Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Establece la prioridad del Banner (opcional) {#set-banner-priority-optional}

La [prioridad de Banner]({{site.baseurl}}/user_guide/channels/banners#priority) determina el orden en que se muestran los Banners si comparten la misma ubicación. Para establecer la prioridad manualmente:

1. Selecciona **Set exact priority**.
2. Arrastra y suelta las campañas para ordenarlas con la prioridad correcta.
3. Selecciona **Apply Sort**.

{% alert tip %}
Si tienes múltiples campañas de Banner que usan el mismo ID de ubicación, te recomendamos usar el ordenador de prioridad de arrastrar y soltar para definir la prioridad exacta.
{% endalert %}

#### Configura la reelegibilidad (opcional) {#re-eligibility}

De forma predeterminada, los usuarios que descartan un Banner nunca vuelven a ser elegibles para esa campaña. Para permitir que los usuarios que descartaron el Banner lo vean de nuevo, ve al paso **Controles de entrega** y selecciona **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña**. Cuando esté habilitado, establece un periodo de espera en minutos, horas, días o semanas.

La cuenta regresiva comienza cuando el usuario descarta el Banner. Una vez que expira el periodo, el usuario vuelve a ser elegible automáticamente, sin necesidad de reiniciar la campaña. La reelegibilidad se rastrea por usuario y por campaña.

#### Elige tu audiencia {#choose-your-audience}

1. En **Públicos objetivo**, elige Segments o filtros para restringir tu audiencia. Recibirás automáticamente una vista previa de la población aproximada del segmento. La pertenencia exacta al segmento se calcula antes de que se envíe el mensaje.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. En **Asignar conversiones**, rastrea con qué frecuencia los usuarios realizan acciones específicas después de recibir una campaña definiendo eventos de conversión con un periodo de hasta 30 días para contar la acción como una conversión.

#### Elige eventos de conversión {#choose-conversion-events}

Braze te permite rastrear [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), es decir, con qué frecuencia los usuarios realizan acciones específicas después de recibir una campaña. Tienes la opción de permitir un periodo de hasta 30 días durante el cual una conversión se cuenta si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes del componente de tu Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, incluyendo pruebas multivariante y [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulta [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

Para controlar la reelegibilidad en los pasos de Banner de Canvas, usa la configuración de reingreso de Canvas. Para más información, consulta [Reelegibilidad para Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### Paso 5: Prueba tu mensaje (opcional) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Paso 6: Revisa y despliega {#step-6-review-and-deploy}

Cuando hayas terminado de construir tu campaña o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) y luego envíala cuando estés listo.