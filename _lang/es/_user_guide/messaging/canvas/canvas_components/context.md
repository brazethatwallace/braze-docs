---
nav_title: Contexto
article_title: Contexto
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Este artículo de referencia explica cómo crear y usar pasos de Contexto en tu Canvas."
tool: Canvas

---

# Contexto {#context}

> Los pasos de Contexto te permiten crear y actualizar una o más variables para un usuario a medida que avanza por un Canvas. Por ejemplo, si tienes un Canvas que gestiona descuentos de temporada, puedes usar una variable de contexto para almacenar un código de descuento diferente cada vez que un usuario entra en el Canvas.

## Cómo funciona {#how-it-works}

![Un paso de Contexto como primer paso de un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los pasos de Contexto te permiten crear y usar datos temporales durante el recorrido de un usuario a través de un Canvas específico. Estos datos existen solo dentro de ese recorrido del Canvas y no persisten entre diferentes Canvas ni fuera de la sesión.

Las variables de contexto existen solo para ese recorrido específico del Canvas. No cambian el perfil del usuario de forma permanente y no aparecen en otros Canvas. Esto las hace ideales para información temporal que solo es relevante para una campaña o flujo de trabajo específico.

{% alert tip %}
Para una referencia completa sobre las variables de contexto, incluyendo tipos de datos, uso y mejores prácticas, consulta la [referencia de variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).
{% endalert %}

Dentro de un paso de Contexto, puedes definir o actualizar hasta 10 variables de contexto. Estas variables se pueden usar para personalizar retrasos, segmentar usuarios dinámicamente y enriquecer la mensajería a lo largo del Canvas. Por ejemplo, podrías crear una variable de contexto para la hora de vuelo programada de un usuario y luego usarla para establecer retrasos personalizados y enviar recordatorios.

Puedes establecer variables de contexto de dos formas:

- **En la entrada del Canvas:** Las propiedades del evento personalizado o del desencadenador de API se rellenan automáticamente como variables de contexto.
- **En un paso de Contexto:** Define o actualiza variables de contexto manualmente añadiendo un paso de Contexto.

Cada variable de contexto requiere un nombre, un tipo de datos y un valor (establecido usando Liquid o la herramienta Añadir personalización). Una vez definidas, puedes hacer referencia a las variables de contexto en todo el Canvas usando Liquid, como {% raw %}`{{context.${flight_time}}}`{% endraw %}. En el campo **Context variable name**, también puedes introducir el nombre de la variable de contexto o seleccionarlo del menú desplegable en el editor de pasos. Para más detalles, consulta la [referencia de variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

Cada entrada al Canvas redefine las variables de contexto basándose en los datos de entrada más recientes y la configuración del Canvas, lo que permite que los usuarios tengan múltiples recorridos activos con su propio contexto. Por ejemplo, si un cliente tiene dos vuelos próximos, tendrá dos estados de recorrido separados ejecutándose simultáneamente&#8212;cada uno con sus propias variables de contexto específicas del vuelo, como hora de salida y destino. Esto te permite enviar recordatorios personalizados sobre su vuelo de las 2 pm a Nueva York mientras envías actualizaciones diferentes sobre su vuelo de las 8 am a Los Ángeles mañana, de modo que cada mensaje sea relevante para la reserva específica.

### Procesamiento de usuarios y procesamiento por lotes {#user-processing-and-batching}

Los pasos de Contexto procesan usuarios en lotes para optimizar el rendimiento. Cuando los usuarios entran en un paso de Contexto, Braze los procesa en lotes de 1000 usuarios de forma predeterminada. Estos lotes se procesan en paralelo, pero dentro de cada lote, los usuarios se procesan secuencialmente.

Esto significa:

**Ejemplo**: Si 3500 usuarios entran en un paso de Contexto con Contenido conectado que tarda 650 ms por usuario:
- Braze crea 4 lotes de usuarios (1000, 1000, 1000 y 500 usuarios en este ejemplo).
- Cada lote procesa usuarios secuencialmente, por lo que un lote de 1000 usuarios tarda aproximadamente 10,8 minutos (650 segundos; 1000 × 650 ms).
- Los lotes se completan en diferentes momentos, por lo que los usuarios van pasando al siguiente paso a medida que su lote termina.
- Los primeros usuarios pueden llegar al siguiente paso varios minutos antes que los últimos usuarios, dependiendo del tamaño del lote y los tiempos de respuesta del Contenido conectado.

Sin Contenido conectado, los pasos de Contexto se procesan mucho más rápido porque no hay llamadas a API externas que esperar.

## Consideraciones {#considerations}

- Puedes definir hasta 10 variables de contexto por paso de Contexto.
- Cada variable requiere un nombre único (solo letras, números y guiones bajos, hasta 100 caracteres).
- El tamaño total de todas las variables en un paso no puede superar los 50 KB.
- Las variables pasadas mediante desencadenadores de API comparten el mismo espacio de nombres que las creadas en los pasos de Contexto; redefinir una variable en un paso de Contexto sobrescribe el valor de la API.

Para más detalles y uso avanzado, consulta la [referencia de variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

## Crear un paso de Contexto {#creating-a-context-step}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Paso 1: Añadir un paso {#step-1-add-a-step}

Añade un paso a tu Canvas, luego arrastra y suelta el componente desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más y selecciona **Context**.

### Paso 2: Definir las variables {#step-2-define-the-variables}

{% alert note %}
Puedes definir hasta 10 variables de contexto para cada paso de Contexto.
{% endalert %}

Para definir una variable de contexto:

1. Dale un **nombre** a tu variable de contexto.
2. Selecciona un [tipo de datos]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types).
3. Escribe una expresión Liquid manualmente o usa **Add Personalization** para crear un fragmento de código Liquid a partir de atributos preexistentes.
4. Selecciona **Preview** para comprobar el valor de tu variable de contexto.
5. (Opcional) Para añadir variables adicionales, selecciona **Add Context variable** y repite los pasos 1-4.
6. Cuando hayas terminado, selecciona **Done**.

Ahora puedes usar tu variable de contexto en cualquier lugar donde uses Liquid, como en los pasos de Mensaje y Actualización de usuario, seleccionando **Add Personalization**. En el campo **Context variable name**, también puedes introducir el nombre de la variable de contexto o seleccionarlo del menú desplegable en el editor de pasos. Para un recorrido completo, consulta la [referencia de variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

{% alert important %}
Al hacer referencia a variables de contexto, usa siempre el formato {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filtros de variables de contexto {#context-variable-filters}

Puedes crear filtros usando variables de contexto en los pasos de [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) y [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split).

Para enrutar usuarios basándote en la respuesta de un [paso de Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), añade el paso de Agente antes de tu paso de Rutas de audiencia o División de decisiones. El paso de Agente almacena su salida en el contexto del Canvas, que puedes evaluar con filtros de variables de contexto en esos pasos de ramificación.

Si el agente devuelve un objeto y quieres filtrar por una propiedad anidada, introduce la ruta en el campo **Context variable name** usando notación de punto en lugar de solo el nombre de la variable de nivel superior (por ejemplo, `intent_agent.persona` cuando `persona` está anidado bajo `intent_agent`).

Para la configuración de filtros, lógica de comparación y ejemplos avanzados, consulta la [referencia de variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Previsualizar rutas de usuario {#previewing-user-paths}

Recomendamos probar y [previsualizar tus rutas de usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para asegurarte de que tus mensajes se envían a la audiencia correcta y que las variables de contexto se evalúan con los resultados esperados.

{% alert note %}
Si estás previsualizando tu Canvas en la sección **Preview & Test Send** del editor, la marca de tiempo en la vista previa del mensaje de prueba **no** se estandariza a UTC porque este panel genera las vistas previas como cadenas. Esto significa que si un Canvas está configurado para aceptar un objeto `time`, la vista previa del mensaje no refleja con precisión lo que ocurre cuando el Canvas está en vivo. Para probar tu Canvas con la mayor precisión, recomendamos previsualizar las rutas de usuario en su lugar.
{% endalert %}

Asegúrate de observar cualquier escenario común que cree variables de contexto no válidas. Al previsualizar tu ruta de usuario, puedes ver los resultados de los pasos de retraso personalizados que usan variables de contexto, y cualquier comparación de pasos de audiencia o decisión que coincida con usuarios según variables de contexto.

Si la variable de contexto es válida, puedes hacer referencia a la variable en todo tu Canvas. Sin embargo, si la variable de contexto no se creó correctamente, los pasos futuros en tu Canvas tampoco funcionarán correctamente. Por ejemplo, si creas un paso de Contexto para asignar a los usuarios una hora de cita y estableces el valor de la hora de cita con una fecha pasada, el correo electrónico de recordatorio en tu paso de Mensaje no se envía.

## Convertir cadenas de Contenido conectado a JSON {#converting-connected-content-strings-to-json}

Al hacer una [llamada de Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) en un paso de Contexto, el JSON devuelto por la llamada se evalúa como un tipo de datos de cadena para mantener la consistencia y prevenir errores. Si quieres convertir esta cadena a JSON, conviértela usando `as_json_string`. Por ejemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Solución de problemas {#troubleshooting}

### Variables de contexto no válidas {#invalid-context-variables}

Una variable de contexto se considera no válida cuando:

- Una llamada a un Contenido conectado integrado falla.
- La expresión Liquid en tiempo de ejecución devuelve un valor que no coincide con el tipo de datos o está vacío (nulo).

Por ejemplo, si el tipo de datos de la variable de contexto es **Número** pero la expresión Liquid devuelve una cadena, es no válida.

En estas circunstancias:
- El usuario avanza al siguiente paso.
- Los análisis del paso en Canvas cuentan esto como _No actualizado_.

Al solucionar problemas, monitoriza la métrica _No actualizado_ para verificar que tu variable de contexto se está actualizando correctamente. Si la variable de contexto es no válida, tus usuarios pueden continuar en tu Canvas más allá del paso de Contexto, pero pueden no calificar para pasos posteriores.

Consulta [Tipos de datos]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types) para ver las configuraciones de ejemplo para cada tipo de datos.

### Retrasos en el envío con Contenido conectado {#delays-in-sending-with-connected-content}

Todos los usuarios en un lote se procesan antes de que cualquier usuario avance. Después de que se completa el procesamiento del lote, los usuarios exitosos pasan al siguiente paso, mientras que los usuarios fallidos se reintentan por separado; los usuarios exitosos no esperan a que los reintentos tengan éxito antes de avanzar.

#### Comportamiento de reintento {#retry-behavior}

En los pasos de Canvas (incluidos los pasos de Contexto), Braze usa mecanismos de reintento específicos de Canvas en lugar del comportamiento estándar de reintento de Contenido conectado. Si una llamada de Contenido conectado falla:

 - Para los pasos de Mensaje, las llamadas de Contenido conectado pueden reintentarse hasta cinco veces.
 - Para todos los demás pasos, Braze reintenta el paso aproximadamente 13 veces con retirada exponencial.

Si todos los reintentos fallan, el usuario sale del Canvas.

La etiqueta `:retry` usada en el Contenido conectado estándar no se aplica a las llamadas de Contenido conectado realizadas dentro de los pasos de Canvas. Los pasos de Canvas tienen su propia lógica de reintento optimizada para flujos de trabajo de Canvas.

El tiempo que tarda en procesar a todos los usuarios a través de un paso de Contexto depende de:

- El número de usuarios que entran en el paso
- Si se usa Contenido conectado (y su tiempo de respuesta)
- El tamaño del lote (predeterminado: 1000 usuarios por lote)

Si tu punto de conexión de Contenido conectado tiene límites de velocidad, ten en cuenta que los pasos de Contexto procesan usuarios secuencialmente dentro de cada lote, lo que ayuda a respetar los límites de velocidad de forma natural. Sin embargo, múltiples lotes se procesan en paralelo, así que asegúrate de que tu punto de conexión pueda manejar solicitudes concurrentes de múltiples lotes.

## Estandarización de consistencia de zona horaria {#time-zone-consistency-standardization}

Con la disponibilidad general de Canvas Context, todas las propiedades de eventos de marca de tiempo predeterminadas en Canvas basados en acciones están en UTC. Este cambio es parte de un esfuerzo más amplio para garantizar una experiencia más predecible y consistente al editar pasos y mensajes de Canvas. Ten en cuenta que este cambio afecta a todos los Canvas basados en acciones, independientemente de si el Canvas específico está usando un paso de Contexto o no.

{% alert important %}
En todas las circunstancias, recomendamos encarecidamente usar [filtros de zona horaria de Liquid]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) para que las marcas de tiempo se representen en la zona horaria deseada. Puedes consultar esta [pregunta frecuente](#faq-example) para ver un ejemplo.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué ha cambiado desde que Canvas Context está disponible de forma general? {#what-has-changed-since-canvas-context-became-generally-available}

Ahora que Canvas Context está disponible de forma general, se aplican los siguientes detalles:

- Todas las marcas de tiempo con un [tipo datetime]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) de las [propiedades de eventos desencadenadores]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) en Canvas basados en acciones están en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Este cambio afecta a todos los Canvas basados en acciones, independientemente de si el Canvas específico está usando un paso de Contexto o no.

#### ¿Cuál es la razón de este cambio? {#what-is-the-reason-for-this-change}

Este cambio es parte de un esfuerzo más amplio para crear una experiencia más predecible y consistente al editar pasos y mensajes de Canvas.

#### ¿Se ven afectados los Canvas desencadenados por API o planificados por este cambio? {#are-api-triggered-or-scheduled-canvases-impacted-by-this-change}

No.

#### ¿Este cambio afecta a las propiedades de entrada del Canvas? {#does-this-change-impact-canvas-entry-properties}

Sí, esto afecta a `canvas_entry_properties` si la `canvas_entry_property` se está usando en un Canvas basado en acciones y el tipo de propiedad es `time`. En todas las circunstancias, recomendamos usar filtros `time_zone` de Liquid para que las marcas de tiempo se representen en la zona horaria deseada.

Aquí tienes un ejemplo de cómo hacerlo:

| Liquid en el paso de Mensaje | Resultado | ¿Es esta la forma correcta de representar zonas horarias en Liquid? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | No |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | No |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="¿Este cambio afecta a las propiedades de entrada del Canvas?" }

#### ¿Cuál es un ejemplo práctico de cómo el nuevo comportamiento de marcas de tiempo podría afectar mis mensajes? {#faq-example}

Supongamos que tenemos un Canvas basado en acciones que tiene el siguiente contenido en un paso de Mensaje:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Esto produce el siguiente mensaje:

```
Your appointment is scheduled for 2025-08-05 4:15 PM, we’ll see you then!
```

Como no se especifica ninguna zona horaria usando Liquid, la marca de tiempo aquí está en UTC.

Para especificar una zona horaria claramente, podemos usar filtros `time_zone` de Liquid así:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Esto produce el siguiente mensaje:

```
Your appointment is scheduled for 2025-08-05 8:15 AM, we'll see you then!
```

Como la zona horaria America/Los Angeles se especifica usando Liquid, la marca de tiempo aquí está en PST.

La zona horaria preferida también se puede enviar en la carga útil de propiedades del evento y usarse en la lógica de Liquid:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### ¿En qué se diferencian las variables de contexto de las propiedades de entrada del Canvas? {#how-do-context-variables-differ-from-canvas-entry-properties}

Las propiedades de entrada del Canvas se incluyen como variables de contexto del Canvas. Esto significa que puedes enviar propiedades de entrada del Canvas usando la API de Braze y hacer referencia a ellas en otros pasos, de forma similar a usar una variable de contexto con el fragmento de código Liquid.

### ¿Pueden las variables hacer referencia entre sí en un mismo paso de Contexto? {#can-variables-reference-each-other-in-a-singular-context-step}

Sí. Todas las variables en un paso de Contexto se evalúan en secuencia, lo que significa que podrías tener las siguientes variables de contexto configuradas:

| Variable de contexto | Valor | Descripción |
|---|---|---|
| `favorite_cuisine` | {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | El tipo de cocina favorita de un usuario. |
| `promo_code` | {% raw %}`EATFRESH`{% endraw %} | El código de descuento disponible para un usuario. |
| `personalized_message` | {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Un mensaje personalizado que combina las variables anteriores. En un paso de Mensaje, podrías usar el fragmento de código Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para hacer referencia a la variable de contexto y entregar un mensaje personalizado a cada usuario. También podrías usar un paso de Contexto para guardar el valor del [código de promoción]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes#creating-a-promotion-code-list) y usarlo como plantilla en otros pasos a lo largo de un Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="¿Pueden las variables hacer referencia entre sí en un mismo paso de Contexto?" }

Esto también aplica entre múltiples pasos de Contexto. Por ejemplo, imagina esta secuencia:

1. Un paso de Contexto inicial crea una variable llamada `JobInfo` con el valor `job_title`.
2. Un paso de Mensaje hace referencia a {% raw %}`{{context.${JobInfo}}}`{% endraw %} y muestra `job_title` al usuario.
3. Más adelante, un paso de Contexto actualiza la variable de contexto, cambiando el valor de `JobInfo` a `job_description`.
4. Todos los pasos posteriores que hacen referencia a `JobInfo` ahora usan el valor actualizado `job_description`.

Las variables de contexto usan su valor más reciente a lo largo del Canvas, y cada actualización afecta a todos los pasos siguientes que hacen referencia a esa variable.