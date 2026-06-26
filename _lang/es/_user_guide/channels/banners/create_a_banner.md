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

> Aprende a crear banners cuando construyes Campaigns y Canvas en Braze. Para información más general, consulta [Acerca de los banners]({{site.baseurl}}/user_guide/channels/banners/).

## Requisitos previos {#prerequisites}

Antes de poder lanzar tu banner, tu equipo de desarrollo debe [configurar las ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/). Mientras tanto, puedes redactar el borrador de tu campaña de banner, pero no podrás lanzar la campaña hasta que las ubicaciones estén configuradas.

## Crear un mensaje de banner {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Paso 2: Elige dónde crear tu mensaje {#step-2-choose-where-to-build-your-message}

¿No tienes claro si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y dirigidas, mientras que los Canvas son mejores para recorridos de usuario con múltiples pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear campaña**.
2. Selecciona **Banner**.
3. Dale a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) según sea necesario. Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el Generador de informes, puedes filtrar por las etiquetas relevantes.
5. Selecciona la ubicación que creaste previamente para asociarla con tu campaña.
6. Añade variantes según sea necesario. Puedes elegir un tipo de mensaje y diseño diferente para cada una. Para más información sobre variantes, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).
7. Elige una fecha y hora de inicio para tu campaña de banner. De forma predeterminada, los banners duran indefinidamente. Puedes cambiar esto seleccionando **End Time** y especificando una fecha y hora de fin.

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes seleccionar **Copy from Variant** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso de mensaje en el constructor de Canvas. Dale a tu paso un nombre claro y significativo.
3. Selecciona **Banner** como tu canal de mensajería.
4. Selecciona una ubicación para el banner.
5. Establece la prioridad del banner. La [prioridad del banner]({{site.baseurl}}/user_guide/channels/banners/#priority) determina el orden en que se muestran los banners si comparten la misma ubicación.
6. Establece una expiración para el banner. Puede ser después de un período de tiempo tras la disponibilidad del paso o en una fecha y hora específicas.

{% endtab %}
{% endtabs %}

### Paso 3: Redactar un banner {#compose-a-banner}

Para redactar tu banner, puedes elegir:

- Empezar con una plantilla en blanco
- Usar una plantilla de banner de Braze
- Seleccionar una plantilla de banner guardada

![Opción para elegir un banner en blanco o una plantilla.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Paso 3.1: Dar estilo al banner {#step-31-style-the-banner}

Puedes arrastrar y soltar bloques y filas en el área del lienzo para empezar a construir tu mensaje. Para una referencia de los bloques del editor de banners y enlaces a detalles de propiedades compartidas, consulta [Bloques del editor (banners)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para personalizar las propiedades de fondo, la configuración de bordes y más de tu mensaje, selecciona **Styles**. Si solo quieres personalizar el estilo de un bloque o fila específicos, selecciónalo para hacer cambios.

![Panel de estilos del compositor de banners.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Paso 3.2: Definir el comportamiento al hacer clic (opcional) {#step-32-define-on-click-behavior-optional}

Cuando un usuario hace clic en un enlace del banner, puedes elegir navegar más profundamente dentro de tu aplicación o redirigirlo a otra página web. Además, puedes elegir [registrar un atributo personalizado o evento]({{site.baseurl}}/developer_guide/analytics/), lo que actualiza el perfil del usuario con datos personalizados cuando hace clic en el banner. Para un seguimiento de clics más detallado, asigna un identificador personalizado a cada elemento interactivo usando el campo **Identifier for Reporting** en su panel de propiedades.

{% alert important %}
{::nomarkdown}
El comportamiento al hacer clic puede ser anulado si un elemento específico (como un botón, enlace o imagen del banner) tiene su propio comportamiento al hacer clic. Por ejemplo, dados los siguientes comportamientos al hacer clic:<br><ul><li>Un banner tiene un comportamiento al hacer clic que redirige a la página de inicio de un sitio web.</li><li>Una imagen en el banner tiene un comportamiento al hacer clic que redirige a la página de producto de un sitio web.</li></ul>Si un usuario hace clic en la imagen, es redirigido a la página de producto. Sin embargo, hacer clic en el área circundante del banner lo redirige a la página de inicio.
{:/}
{% endalert %}

#### Paso 3.3: Configurar el comportamiento de descarte (opcional) {#dismiss-behavior}

Selecciona la casilla **Banner can be dismissed** en la sección **Dismiss behavior** para permitir que los usuarios descarten el banner. Esto es útil cuando quieres promocionar una oferta por tiempo limitado a una audiencia amplia, pero permitir que los usuarios no interesados oculten el mensaje.

Cuando el descarte está habilitado, puedes personalizar el botón de descarte en la sección **Dismiss behavior**:

| Configuración | Descripción |
|---------|-------------|
| **Button size** | El tamaño del botón de descarte que se muestra en el banner. |
| **Button color** | El color del botón de descarte. |
| **ARIA label** | La etiqueta accesible para el botón de descarte, utilizada por los lectores de pantalla. De forma predeterminada es "Close" si se deja en blanco. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración del botón de descarte" }

Cuando un usuario descarta un banner, este no vuelve a aparecer para ese usuario, incluso si aún cumple con los criterios de segmentación de la campaña.

#### Paso 3.4: Añadir propiedades personalizadas (opcional) {#custom-properties}

Puedes añadir propiedades personalizadas a un banner para adjuntar metadatos estructurados, como cadenas u objetos JSON. Estas propiedades no afectan cómo se muestra el banner, pero pueden [accederse a través del SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) para modificar el comportamiento o la apariencia de tu aplicación. Por ejemplo, podrías:

- Enviar metadatos para tus análisis de terceros o integraciones.
- Usar metadatos como un `timestamp` u objeto JSON para desencadenar lógica condicional.
- Controlar el comportamiento de un banner basándote en metadatos incluidos como `ratio` o `format`.

Para añadir una propiedad personalizada, selecciona **Settings** > **Properties** > **Add property**.

![La página de propiedades mostrando la opción de añadir la primera propiedad personalizada a una campaña de banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propiedad que quieras añadir, completa lo siguiente:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Tipo de propiedad | El tipo de datos de la propiedad. Los tipos compatibles incluyen cadena, booleano, número, marca de tiempo, URL de imagen y objeto JSON. | Cadena |
| Clave de propiedad | El identificador único de la propiedad. Esta clave se usa en el SDK para acceder a la propiedad. | `color` |
| Valor | El valor asignado a la propiedad. Debe coincidir con el tipo de propiedad seleccionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 3.4: Añadir propiedades personalizadas (opcional) #custom-properties" }

Cuando hayas terminado, selecciona **Done**.

![La página de propiedades con una propiedad de tipo cadena con una clave de color y valor de #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Paso 4: Construir el resto de tu campaña o Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Establecer la prioridad del banner (opcional) {#set-banner-priority-optional}

La [prioridad del banner]({{site.baseurl}}/user_guide/channels/banners/#priority) determina el orden en que se muestran los banners si comparten la misma ubicación. Para establecer la prioridad manualmente:

1. Selecciona **Establece la prioridad exacta**.
2. Arrastra y suelta las campañas para ordenarlas con la prioridad correcta.
3. Selecciona **Apply Sort**.

{% alert tip %}
Si tienes múltiples campañas de banner usando el mismo ID de ubicación, te recomendamos usar el ordenador de prioridad de arrastrar y soltar para definir la prioridad exacta.
{% endalert %}

#### Configurar la reelegibilidad (opcional) {#re-eligibility}

De forma predeterminada, los usuarios que descartan un banner nunca vuelven a ser elegibles para esa campaña. Para permitir que los usuarios que descartaron el banner lo vean de nuevo, ve al paso **Controles de entrega** y selecciona **Allow users to become re-eligible to receive campaign**. Cuando esté habilitado, establece una ventana de espera en minutos, horas, días o semanas.

La cuenta regresiva comienza cuando el usuario descarta el banner. Después de que la ventana expire, el usuario vuelve a ser elegible automáticamente, sin necesidad de reiniciar la campaña. La reelegibilidad se rastrea por usuario y por campaña.

#### Elige tu audiencia {#choose-your-audience}

1. En **Público objetivo**, elige segmentos o filtros para delimitar tu audiencia. Recibirás automáticamente una vista previa de la población aproximada del segmento. La pertenencia exacta al segmento se calcula antes de que se envíe el mensaje.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. En **Asignar conversiones**, realiza un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas después de recibir una campaña definiendo eventos de conversión con una ventana de hasta 30 días para contar la acción como una conversión.

#### Elige eventos de conversión {#choose-conversion-events}

Braze te permite realizar un seguimiento de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), la frecuencia con la que los usuarios realizan acciones específicas, después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se cuenta una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar [pruebas multivariantes]({{site.baseurl}}/user_guide/messaging/ab_testing/) e [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), y más, consulta el paso [Construir tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.

Para controlar la reelegibilidad en los pasos de banner de Canvas, usa la configuración de reentrada de Canvas. Para más información, consulta [Reelegibilidad para Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/).

{% endtab %}
{% endtabs %}

### Paso 5: Probar tu mensaje (opcional) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Paso 6: Revisar y desplegar {#step-6-review-and-deploy}

Después de terminar de construir tu campaña o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) y luego envíala cuando estés listo.