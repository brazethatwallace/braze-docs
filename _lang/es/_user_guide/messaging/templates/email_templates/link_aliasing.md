---
nav_title: Aliasing de enlaces
article_title: Aliasing de enlaces
alias: /link_aliasing/
page_order: 3
description: "Este artículo describe cómo funciona el aliasing de enlaces y proporciona ejemplos de cómo se verán tus enlaces."
channel:
  - email

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Aliasing de enlaces {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> Usa el aliasing de enlaces para crear nombres reconocibles, generados por el usuario, que identifiquen los enlaces enviados en mensajes de correo electrónico desde Braze. Estos enlaces están disponibles para la reorientación por segmentación, la activación basada en acciones y el análisis de enlaces.

## Acerca del aliasing de enlaces {#about-link-aliasing}

Con el aliasing de enlaces, puedes crear nombres generados por el usuario para identificar y rastrear enlaces enviados en correos electrónicos. De esta forma, puedes utilizar de manera eficiente estos alias de enlace reconocibles en tus correos electrónicos para hacer seguimiento de la participación y analizar el rendimiento de la campaña, sin necesidad de hacer referencia al enlace completo.

Con el aliasing de enlaces, puedes:

- **Reorientar a usuarios que han hecho clic en enlaces específicos:** Identificar y segmentar a los usuarios que han hecho clic en un enlace.
- **Crear desencadenantes basados en acciones:** Enviar un correo electrónico cuando un usuario hace clic en un enlace.
- **Analizar métricas:** Comparar cuántos usuarios han hecho clic en el Enlace A frente al Enlace B.

### Cómo funciona {#how-it-works}

Braze identifica de forma única los enlaces dentro de los correos electrónicos añadiendo un parámetro adicional llamado `lid` (también conocido como identificador de enlace) a cada URL de enlace. Este valor `lid` permite a Braze rastrear, monitorizar y agregar las interacciones de los usuarios con el enlace, incluso si el resto de los parámetros de la URL pueden diferir. Esto ayuda a proporcionar información sobre cómo los usuarios interactúan con el contenido de tus campañas de correo electrónico.

Los identificadores de enlace también se actualizarán si se duplica una campaña de correo electrónico, un Canvas con un mensaje de correo electrónico o un Content Block.

## Creación de un alias de enlace {#creating-a-link-alias}

{% alert important %}
**Link Management** aparece en el creador de correo electrónico de la Campaign o Canvas cuando Braze habilita la gestión de enlaces para tu cuenta. Para crear y editar **alias de enlace**, el aliasing de enlaces debe estar activado. Si falta **Link Management**, ponte en contacto con tu director de cuentas para activar el aliasing de enlaces.
{% endalert %}

Para crear un alias de enlace, abre el cuerpo de tu correo electrónico en la Campaign o el componente de Canvas, y luego abre **Link Management** desde el área **Content**. Los creadores de arrastrar y soltar y de HTML utilizan el mismo diseño de barra lateral:

### Editor de arrastrar y soltar {#drag-and-drop-editor}

1. Selecciona **Edit Email Body** para abrir el creador de arrastrar y soltar.
2. En la barra lateral del creador, selecciona **Content** (junto a **Sending Settings** y **vista previa & Test**). Para obtener más información sobre este diseño, consulta [Crear un correo electrónico con arrastrar y soltar]({{site.baseurl}}/user_guide/channels/email/drag_and_drop).
3. En el submenú **Content**, selecciona **Link Management** (aparece debajo de **Design and Build**). Si el submenú está contraído, expándelo usando el control de flecha en la barra lateral.

### Editor HTML {#html-editor}

1. Ve al cuerpo de tu correo electrónico en el creador.
2. En la barra lateral del creador, selecciona **Content**.
3. En el submenú **Content**, selecciona **Link Management** debajo de **Design and Build**.

En **Link Management**:

1. Braze genera automáticamente alias de enlace predeterminados únicos para cada uno de tus enlaces.
2. Dale un nombre al alias. Los alias deben tener un nombre único por variante de campaña de correo electrónico o componente de Canvas.

También puedes establecer un alias que se utilizará para hacer referencia a un enlace específico al trabajar con informes o segmentación.

![Página de Link Management con cuatro alias de enlace.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
El aliasing de enlaces solo es compatible con atributos `href` dentro de etiquetas de anclaje HTML donde sea seguro añadir un parámetro de consulta. Se recomienda incluir un signo de interrogación (?) al final de tu enlace para que Braze pueda añadir fácilmente el valor `lid`. Sin añadir el valor `lid`, Braze no reconocerá la URL para el aliasing de enlaces.
{% endalert %}

{% alert important %}
En el editor de arrastrar y soltar, tu enlace debe incluir un signo de interrogación (`?`) antes del símbolo de almohadilla (`#`) en tu URL para que el alias de enlace aparezca en la pestaña **Link Management**.
{% endalert %}

## Gestión de alias de enlaces {#managing-link-aliases}

Para ver todos tus alias de enlaces rastreados, haz lo siguiente:

1. Ve a **Configuración** > **Preferencias de correo electrónico** en **Configuración del espacio de trabajo**.
2. Selecciona la pestaña **Configuración de aliasing de enlaces**.

Aquí puedes ordenar, buscar y desactivar el seguimiento de los alias de enlaces.

![Página de alias de enlaces rastreados que muestra alias de enlaces activos e inactivos asociados a varias campañas.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Usa los endpoints [Listar alias de enlace para Campaign]({{site.baseurl}}/get_campaign_link_alias) y [Listar alias de enlace para Canvas]({{site.baseurl}}/get_canvas_link_alias) para extraer el `alias` establecido en cada variante de mensaje en una Campaign o un componente de Canvas específico de correo electrónico.
{% endalert %}

Braze recomienda evaluar los enlaces dentro del correo electrónico, añadir plantillas de enlaces y proporcionar una convención de nomenclatura que funcione para fines de segmentación y elaboración de informes. Esto te ayuda a realizar un seguimiento de todos los enlaces.

Cuando el aliasing de enlaces está activado, los mensajes, Content Blocks y plantillas de enlaces no se modifican. Los mensajes existentes que utilizan plantillas de enlaces o Content Blocks seguirán siendo los mismos. Sin embargo, cuando actualices un mensaje, el marcado de alias de enlaces se aplicará a todos los enlaces, por lo que tendrás que volver a aplicar las plantillas de enlaces para que los enlaces sean visibles.

## Cómo se actualizan los enlaces con el aliasing de enlaces {#how-links-are-updated-with-link-aliasing}

Las siguientes tablas proporcionan ejemplos de enlaces en el cuerpo de un correo electrónico, resultados del aliasing de enlaces y explicaciones de cómo se actualiza el enlace original con el aliasing de enlaces.

### Enlace permanente {#permalink}

**Lógica:** Braze inserta un signo de interrogación (?) y añade el primer parámetro de consulta en la URL.

| Enlace en el cuerpo del correo electrónico | Enlace con aliasing |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enlace permanente" }

### Enlace con más parámetros de consulta {#link-with-more-query-parameters}

**Lógica:** Braze detecta otros parámetros de consulta y añade `lid=` al final de la URL.

| Enlace en el cuerpo del correo electrónico | Enlace con aliasing |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enlace con más parámetros de consulta" }

### Enlace HTML {#html-link}

**Lógica:** Braze reconoce que un enlace es una URL y que ya tiene un signo de interrogación (?) presente, por lo que el parámetro de consulta `lid` se añade después del signo de interrogación.

| Enlace en el cuerpo del correo electrónico | Enlace con aliasing |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enlace HTML" }

### Enlace con ancla {#link-with-anchor}

**Lógica:** Braze espera que la URL utilice una estructura estándar donde las anclas (#) estén presentes después de un signo de interrogación (?). Dado que Braze lee de izquierda a derecha, el signo de interrogación y el valor `lid` se añaden antes del ancla.

| Enlace en el cuerpo del correo electrónico | Enlace con aliasing |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enlace con ancla" }

### Enlace con ancla y etiqueta de captura {#link-with-anchor-and-capture-tag}

**Lógica:** Al usar el aliasing de enlaces con URLs que contienen anclas (#), Braze espera que el ancla se coloque después de los parámetros de consulta. Esto significa que el valor `lid` debe añadirse **antes** del ancla para un seguimiento adecuado, y dado que Braze lee la URL de izquierda a derecha, el signo de interrogación (?) y el `lid` deben ir antes del ancla.

| Enlace en el cuerpo del correo electrónico | Enlace con aliasing |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enlace con ancla y etiqueta de captura" }

## Seguimiento de alias de enlaces {#tracking-link-aliases}

En la barra lateral del creador, selecciona **Contenido** > **Gestión de enlaces** (en **Diseño y creación**), y luego selecciona qué alias deseas que estén **rastreados**. Los alias rastreados están disponibles en los filtros de segmentación que hacen referencia a alias de enlaces (consulta [Filtros de segmentación](#segmentation-filters)). También puedes enviar mensajes basados en acciones o mover usuarios a través de un Canvas cuando hacen clic en un alias de enlace en un correo electrónico; consulta [Filtros basados en acciones](#action-based-filters). La configuración de **rastreado** no afecta si los clics en ese enlace se cuentan en los informes de rendimiento de correo electrónico.

{% alert tip %}
Para hacer seguimiento de las métricas de participación en enlaces, asegúrate de que tu enlace comience con HTTP o HTTPS. Para desactivar el seguimiento de clics en enlaces específicos, consulta [Enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

Braze te permite seleccionar un número ilimitado de enlaces para hacer seguimiento, aunque solo puedes reorientar usuarios con los enlaces más recientes que hayan abierto. Los perfiles de usuario incluyen sus 100 enlaces más recientemente clicados. Por ejemplo, si haces seguimiento de 500 enlaces y un usuario hace clic en los 500, puedes reorientar o crear segmentos basados en los 100 enlaces más recientemente clicados.

![La pestaña de Gestión de enlaces con dos enlaces seleccionados.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze solo hace seguimiento de los últimos 100 alias de enlace clicados a nivel de perfil.
{% endalert %}

### Filtros basados en acciones {#action-based-filters}

Cuando el aliasing de enlaces está habilitado para tu espacio de trabajo, puedes crear mensajes basados en acciones que apunten a cualquier enlace (rastreado o no rastreado) o reorientar usuarios en función de si hicieron clic en un alias en cualquier Campaign de correo electrónico o componente de Canvas.

![Opciones basadas en acciones para apuntar a usuarios que han hecho clic en un alias en un componente de Canvas o han interactuado con una Campaign.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

- Si una Campaign se archiva, el seguimiento de enlaces se desactiva y ese alias de enlace no se puede usar en un filtro diferente.
- Si un enlace tiene activado el seguimiento y se hizo clic en una Campaign, puedes encontrar la Campaign como opción disponible en el filtro de segmento, incluso si el seguimiento de enlaces se ha desactivado desde entonces, siempre y cuando al menos un enlace en ese mensaje siga siendo rastreado.
- Solo puedes seleccionar un enlace rastreado como filtro si está en un Canvas activo (lanzado), usando el menú desplegable del filtro **Clicked Alias in Canvas Step**. Si el enlace se está rastreando en un borrador de Canvas, no puedes seleccionar el enlace rastreado como filtro.

Para establecer enlaces como no rastreados, ve a **Configuración** > **Preferencias de correo electrónico** > **Configuración de aliasing de enlaces**.

### Filtros de segmentación {#segmentation-filters}

En Braze, si tienes un alias de enlace en tu correo electrónico y un usuario hace clic en él, el evento se registra en el perfil del usuario con el alias.

Si usas el filtro de segmentación "Clicked Alias in Any Campaign or Canvas Step" y más adelante decides cambiar el nombre de este alias de enlace, los datos de clics anteriores en el perfil del usuario **no** se actualizan, lo que significa que seguirán mostrando el alias de enlace anterior. Por lo tanto, si apuntas a usuarios basándote en el nuevo alias de enlace, no se incluirán los datos del alias de enlace anterior.

Si usas el filtro de segmentación "Clicked Alias in Campaign" o "Clicked Alias in Canvas", este filtro tus usuarios según si hicieron clic en un alias específico en una Campaign o Canvas determinado. Si varios usuarios comparten la misma dirección de correo electrónico y se hace clic en el alias de enlace, todos los demás usuarios que comparten la dirección de correo electrónico tendrán sus perfiles de usuario actualizados. Estos perfiles también se actualizan por eventos de entrega y apertura, no solo por eventos de clic.

Los siguientes filtros de segmentación se aplican a eventos de clic que se rastrean en el momento en que se procesa el evento. Esto significa que los enlaces no rastreados no eliminarán datos existentes y rastrear un enlace no rellenará retroactivamente los datos. Para más detalles, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Dejar de rastrear enlaces {#untracking-links}

Dejar de rastrear un enlace no reasignará los segmentos existentes con el filtro al alias no rastreado. Los datos antiguos permanecerán en los perfiles de usuario hasta que sean reemplazados por datos más recientes.

Los enlaces en mensajes archivados se dejan de rastrear automáticamente. Sin embargo, si los mensajes archivados se desarchivan, los enlaces deberán rastrearse de nuevo. Cuando los alias de enlaces están siendo rastreados, los informes de enlaces se indexan por el alias en lugar de dominios de nivel superior o URLs completas.

Para ver todos los enlaces en tu Campaign de correo electrónico y sus respectivos clics totales, ve a **Análisis de mensajes** > **Rendimiento de correo electrónico** > **Vista previa y mapa de calor**, y selecciona la opción **Mostrar mapa de calor**.

![Panel de tabla de enlaces por total de clics con alias de enlaces y sus clics totales.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### Evento de clics de correo electrónico {#email-clicks-event}

Si exportas tus datos de participación con Currents, un evento de clic de correo electrónico será ligeramente diferente si tienes habilitado el aliasing de enlaces. Tendrá dos campos adicionales para el [evento de clics de correo electrónico]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-click-events) cuando el aliasing de enlaces esté activado: `link_id` y `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
El comportamiento de `dispatch_id` difiere entre Canvas y Campaigns porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden ser programados) como eventos desencadenados, incluso cuando están "programados". Obtén más información sobre el [comportamiento de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) en Canvas y Campaigns.

_Actualización registrada en agosto de 2019._
{% endalert %}

## Aliasing de enlaces en Content Blocks {#link-aliasing-in-content-blocks}

Los nuevos Content Blocks tendrán sus enlaces modificados: Braze añadirá `lid={{placeholder}}` a cada enlace cuando corresponda. Este valor de marcador de posición se resuelve cuando se inserta en una variante de mensaje de correo electrónico.

Para modificar los enlaces dentro de Content Blocks existentes que se crearon antes de que Braze habilitara el aliasing de enlaces, duplica los Content Blocks existentes y luego modifica los enlaces dentro de los Content Blocks duplicados.

Cuando se inserta un Content Block sin un valor `lid` en un mensaje nuevo, los enlaces de ese Content Block no se rastrean con un alias. Cuando se inserta un nuevo Content Block en una variante de mensaje "antigua", los enlaces de esa variante de mensaje serán reconocidos por el aliasing de enlaces. Los enlaces del Content Block también se reconocen. Sin embargo, los Content Blocks "antiguos" no pueden anidar Content Blocks "nuevos".

{% alert tip %}
Para Content Blocks, Braze recomienda crear copias de los Content Blocks existentes para usarlos en mensajes nuevos. Esto se puede hacer mediante duplicación masiva para evitar situaciones en las que podrías hacer referencia a un Content Block que no se ha habilitado para el aliasing de enlaces en un mensaje nuevo.
{% endalert %}

## Aliasing de enlaces para URL generadas por Liquid {#link-aliasing-for-urls-generated-by-liquid}

Para las URL que se generan mediante Liquid (por ejemplo, `assign` en el HTML, valores obtenidos de un Content Block o Liquid en un atributo personalizado), Braze necesita un lugar claro para insertar el parámetro de consulta `lid`. En la mayoría de los casos, cuando Liquid permanece en la URL, Braze no infiere si debe iniciar una nueva cadena de consulta con `?` o unirse a una consulta existente con `&`, a menos que tú añadas ese delimitador.

Haz lo siguiente:

- Si la URL **no** incluye ya una cadena de consulta, añade `?` después del Liquid (por ejemplo, `{{my_url}}?`).
- Si la URL **ya** incluye `?` y parámetros de consulta, añade `&` después del Liquid (por ejemplo, `{{my_url}}&`).

{% alert note %}
Cuando utilizas [plantillas de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template) con URL generadas por Liquid, Braze puede normalizar de forma conservadora la URL renderizada después de que Liquid se ejecute cuando contiene exactamente dos caracteres `?` utilizados como separadores de consulta. El segundo `?` puede reescribirse como `&` para que Braze modifique lo menos posible la URL. <br><br>Braze no intenta corregir todos los patrones de `?` duplicados, y el manejo de URL más complejas permanece intencionalmente limitado. Añade el `?` o `&` correcto en tu marcado primero, y considera cualquier normalización como una protección limitada, no como un sustituto de URL bien formadas ni de que los enlaces sean reconocidos en **Link Management** cuando no hay un delimitador presente.
{% endalert %}

Sin un `?` o `&` final (u otro punto de inserción compatible), el aliasing de enlaces no reconoce la URL, **Link Management** no la lista y las plantillas de enlaces no se aplican.

### Fragmentos de URL (`#`) y parámetros de seguimiento {#url-fragments-and-tracking-parameters}

El fragmento (`#` y todo lo que le sigue) no se envía al servidor en una solicitud de enlace normal. Braze inserta `lid` en la cadena de consulta, que debe aparecer antes del `#`. Si tu `href` tiene Liquid y un fragmento `#` pero no tiene `?` o `&` antes del `#`, Braze no puede añadir `lid` de forma segura, por lo que el enlace podría no aparecer en **Link Management** ni rastrearse como un alias de enlace.

Esto es especialmente común en el editor de arrastrar y soltar cuando la URL de un botón mezcla Liquid con un patrón basado en hash (por ejemplo, una ruta estática, luego `#` y después pares clave-valor adicionales). En ese caso, añade `?` inmediatamente antes del `#` para que la cadena de consulta (incluido `lid`) se analice antes del fragmento.

{% raw %}
```text
https://example.com/campaign/to/abc123?#user_id={{${user_id}}}&source=email
```
{% endraw %}

En el ejemplo anterior, el `?` antes del `#` le da a Braze un segmento de consulta donde añadir `lid`. Sin él, el enlace podría no aparecer en **Link Management**.

Sin identificar dónde añadir parámetros de consulta, el aliasing de enlaces no reconoce estas URL y las plantillas de enlaces no se aplican. Si ves errores como **Failed to be assigned an LID** para una URL dinámica, confirma que el `href` utiliza el patrón `?` o `&` que se muestra en los ejemplos de esta sección.

### Consideraciones del editor de arrastrar y soltar {#drag-and-drop-editor-considerations}

En el editor de arrastrar y soltar, los campos que contienen un enlace (como la **URL** de un botón) validan el `href` subyacente antes de que Liquid se ejecute. Los espacios, saltos de línea y otros caracteres que no son seguros para URL pueden causar comportamientos inesperados cuando Braze añade plantillas de enlaces o parámetros de aliasing de enlaces. Cuando necesites Liquid condicional para el destino, configura la URL en un bloque HTML (consulta la siguiente sección) y haz referencia a una sola variable en el campo de **URL** del editor de arrastrar y soltar, en lugar de poner Liquid complejo directamente en ese campo.

### Ejemplo de Content Block {#content-block-example}

{% raw %}
Si un Content Block contiene un enlace como `https://www.braze.com/{{custom_attribute.${offer_id}}}` sin un `?` o `&` final, Braze no sabe dónde añadir `lid`, por lo que el enlace no se detecta para **Link Management**. Añade `?` o `&` al final de la URL en el Content Block (dependiendo de si ya existe una cadena de consulta), guarda el Content Block y el enlace podrá ser reconocido.
{% endraw %}

### Informes cuando la URL varía por usuario {#reporting-when-the-url-varies-per-user}

Cada `href` distinto en el mensaje se mapea a **un** ID de enlace y un alias de enlace para **Link Management** y los informes basados en alias. Cuando se rastrean los alias de enlaces, los informes de correo electrónico en el panel se indexan por el alias en lugar de por cada posible URL resuelta.

Utiliza los siguientes enfoques en Braze primero:

- **Análisis de correo electrónico de Campaign y Canvas:** Revisa los clics agregados por enlace desde **Message Analytics** > **Email Performance** > **vista previa & Heatmap** con **Show Heatmap** activado, como se describe en [Dejar de rastrear enlaces](#untracking-links).
- **Clics por destinatario en Query Builder:** Ejecuta la [plantilla de Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates#email-templates) **Email URLs clicked** para una Campaign o un Canvas. La plantilla muestra enlaces despersonalizados para conteos resumidos; la exportación CSV incluye los ID de usuario de quienes hicieron clic, el enlace en el que hicieron clic y una marca de tiempo. (Las URL despersonalizadas eliminan las etiquetas de Liquid para la vista resumida; consulta la descripción de la plantilla para más detalles).
- **Desgloses por alias en el creador:** Si necesitas que cada destino (por ejemplo, cada `offer_id`) aparezca como su propia fila en **Link Management** y en los informes basados en alias, utiliza valores de `href` separados (y por lo tanto alias separados), por ejemplo, enlaces distintos por rama, en lugar de un solo enlace cuya ruta cambie por usuario.

Si también utilizas exportaciones de participación por streaming, los eventos de clic en correo electrónico incluyen un campo **`url`**; consulta [Evento de clics en correo electrónico](#email-clicks-event) en esta página para saber cómo se relaciona esa carga útil con el aliasing de enlaces.

### Ejemplo {#example}

Usa este patrón cuando la URL asignada no tiene parámetros de consulta:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Visit Braze</a>
```
{% endraw %}

Si la URL asignada ya contiene `?` y parámetros de consulta, añade `&` después del Liquid en lugar de `?`:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?campaign=test" %}

<a href="{{link_with_params}}&">Visit Braze</a>
```
{% endraw %}

### URL con Liquid condicional {#urls-with-conditional-liquid}

Cuando se utilizan etiquetas de Liquid condicional dentro de un `href` (por ejemplo, para establecer una URL con {% raw %}`{% if %}`, `{% elsif %}` o `{% unless %}`{% endraw %}), el aliasing de enlaces no se aplica a esos enlaces. Esto significa que estos enlaces no aparecen en **Link Management** y no reciben un `lid` para el seguimiento de clics.

**Recomendado:** Construye la URL final en un bloque HTML con `assign` (o {% raw %}`{% capture %}`{% endraw %}), y luego haz referencia a esa variable donde necesites el enlace. En el editor de arrastrar y soltar, pega la variable en el campo **URL** del botón con un `?` o `&` final según corresponda, por ejemplo, `{{url}}?`.

{% raw %}
```liquid
{% if {{custom_attribute.${account_tier}}} == "pro" %}
{% assign url = "https://example.com/pro/verify" %}
{% else %}
{% assign url = "https://example.com/retail/account" %}
{% endif %}
```
{% endraw %}

En el campo **URL** del botón (arrastrar y soltar) o en HTML, apunta el `href` a la variable con un delimitador:

{% raw %}
```liquid
<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

Alternativamente, puedes capturar la URL en una sola variable:

{% raw %}
```liquid
{% capture url %}
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{% endcapture %}

<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

## Solución de problemas {#troubleshooting}

### Destinos que no aceptan el parámetro `lid` {#destinations-that-dont-accept-the-lid-parameter}

Cuando envías un mensaje de prueba desde el editor de correo electrónico, Braze añade {% raw %}`lid={{placeholder}}`{% endraw %} a tus enlaces (el marcador de posición se convierte en un valor único en el momento del envío). Si el sitio o la API de destino no toleran parámetros de consulta adicionales, el enlace puede funcionar en el editor, pero fallar al abrirlo desde el correo electrónico.

Sin el valor `lid`, Braze no trata la URL como un enlace con alias para el seguimiento y la segmentación. Te recomendamos actualizar tu backend o sitio para que ignore el parámetro de consulta `lid` cuando esté presente. Esto preserva el aliasing de enlaces, los informes y los ejemplos de uso de Segments descritos en este artículo.

Alternativamente, puedes desactivar el aliasing de enlaces en el panel mientras planificas un cambio en el backend. Ve a **Configuración** > **Preferencias de correo electrónico** > **Configuración de aliasing de enlaces**.

Si no puedes modificar tus sistemas de destino, contacta con el [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) para desactivar el aliasing de enlaces en tu espacio de trabajo. Ten en cuenta las siguientes consideraciones si el aliasing de enlaces se desactiva en tu espacio de trabajo:

- Los nuevos mensajes de correo electrónico y Content Blocks normalmente no recibirán el marcado de aliasing de enlaces (como el parámetro de consulta `lid`).
- Los mensajes existentes que se crearon mientras el aliasing de enlaces estaba activado aún pueden contener marcado de aliasing de enlaces en el HTML. Es posible que debas eliminar manualmente los parámetros `lid` sobrantes donde ya no los necesites.
- Si editas una Campaign existente, un paso de correo electrónico en Canvas o un Content Block, es posible que debas añadir plantillas de enlaces de nuevo para que los enlaces con plantilla se muestren correctamente.
- Los informes de clics para envíos que se realizaron mientras el aliasing de enlaces estaba activado pueden no coincidir limpiamente con los informes después de que la característica se desactive.
- Los Segments que utilizan filtros basados en aliasing de enlaces (por ejemplo, filtros de **Clicked Alias**) pueden dejar de devolver las audiencias que esperas.