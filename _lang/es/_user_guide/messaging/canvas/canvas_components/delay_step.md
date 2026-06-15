---
nav_title: Demora
article_title: Demora
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Este artículo de referencia explica cómo añadir una demora a tu Canvas sin necesidad de agregar un mensaje asociado."
tool: Canvas

---

# Demora

> Los componentes de demora te permiten añadir una demora independiente a un Canvas. Puedes añadir una demora a tu Canvas sin necesidad de agregar un mensaje asociado.

Las demoras pueden hacer que tu Canvas se vea más limpio. También puedes usar este componente para retrasar un paso diferente hasta una fecha exacta, hasta un día específico o hasta un día específico de la semana. Un componente de demora puede conectarse como máximo a un paso posterior. <br> ![Un paso de demora con una demora de 1 día como primer paso de un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Crear una demora

Para crear una demora, añade un paso a tu Canvas. Arrastra y suelta el componente de demora desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de signo más en la parte inferior de un paso y luego elige **Delay**.

#### Demoras extendidas

Puedes extender los pasos de demora hasta dos años (730 días). Por ejemplo, si estás incorporando nuevos usuarios a tu aplicación, puedes añadir una demora extendida de dos meses antes de enviar un paso de mensaje para animar a los usuarios que no han iniciado una sesión.

## Tipos de demora temporal

Puedes elegir el tipo de demora antes del siguiente mensaje en tu Canvas. Puedes establecer una demora para que tus usuarios esperen un periodo de tiempo determinado, o retrasar a tus usuarios hasta una fecha y hora específicas.

Si hay una demora temporal, es de esperar que algunos usuarios solo avancen al siguiente paso del Canvas después de la demora. Los usuarios que estén en la demora no se añadirán a la métrica _Avanzaron al siguiente paso_. Para más información, consulta [Análisis de demoras](#delay-analytics).

{% tabs %}
{% tab Duración %}

Seleccionar **Duration** te permite retrasar a los usuarios durante un número determinado de segundos, minutos, horas, días o semanas, y a una hora específica. Por ejemplo, puedes retrasar a los usuarios durante cuatro horas o durante un día.

Ten en cuenta la diferencia entre cómo se calculan los "días" y los "días calendario".

- Un "día" son 24 horas y se calcula a partir del momento en que el usuario entra en el paso de demora.
- Un "día calendario" define el tiempo de espera hasta la siguiente hora especificada, que podría ser menos de 24 horas. Puedes elegir retrasar en la hora de la empresa o en la hora local del usuario. Si no se especifica una hora, el usuario será retrasado hasta la medianoche del día siguiente en la hora de la empresa.

También puedes seleccionar **At a specific time** para especificar cuándo los usuarios avanzarán en el Canvas. Esta opción tiene en cuenta la hora en que el usuario entró en el paso de demora. Si esta hora supera la hora configurada en los ajustes, se añadirán más horas a la demora.

Como ejemplo, supongamos que hoy es 11 de diciembre y nuestro paso de demora está configurado con una **Duration** de una semana a las 8 am UTC. Si un usuario entra en el paso de demora el 4 de diciembre, sería liberado del paso de demora para continuar su recorrido hoy si originalmente entró en el paso de demora antes de las 8 am UTC. Si entró en el paso de demora después de esa hora, el usuario será retrasado hasta el día siguiente (la siguiente ocurrencia de esa hora).

{% endtab %}
{% tab Fecha del calendario %}

Seleccionar **Calendar date** te permite retener a los usuarios en el paso hasta una fecha y hora específicas.

#### Consideraciones

##### Los usuarios no recibirán pasos o mensajes con fechas pasadas

Si la fecha y hora seleccionadas ya han pasado cuando los usuarios llegan al paso de demora, los usuarios saldrán del Canvas. Puede haber hasta 31 días entre el inicio del Canvas y las fechas elegidas para los pasos de "esperar hasta un día exacto".

{% alert important %}
Si participas en el [acceso anticipado de Canvas Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/), puedes establecer demoras de hasta 2 años.
{% endalert %}

Por ejemplo, los usuarios no recibirán pasos o mensajes en estos escenarios:

- Un mensaje está programado para enviarse el 3 de mayo a las 9 pm, pero el paso de demora expira el 3 de mayo a las 9 am.
- Un paso en Canvas se retrasa hasta una hora específica en la zona horaria local del usuario, pero los usuarios no tienen una zona horaria configurada en su perfil de usuario. La demora entonces se establece por defecto en la zona horaria de la empresa para estos usuarios, que ya ha pasado la hora especificada.

##### Los usuarios saldrán si un paso de demora posterior está dentro del plazo de un paso de demora anterior

Si el Canvas tiene dos pasos de demora pero el primer paso de demora es más largo que el segundo paso de demora, los usuarios también saldrán del Canvas.

Por ejemplo, supongamos que un Canvas tiene estos pasos:
- Paso 1: Paso de mensaje
- Paso 2: Paso de demora hasta el 13 de diciembre a las 10 pm
- Paso 3: Paso de mensaje
- Paso 4: Paso de demora hasta el 13 de diciembre a las 7 pm
- Paso 5: Paso de mensaje

Los usuarios que entren en el paso 4 saldrán del Canvas antes de recibir el paso 5 porque la demora del paso 4 está dentro del plazo del paso 2.

{% endtab %}
{% tab Día de la semana %}

Seleccionar **Day of the week** te permite retener a los usuarios en el paso hasta un día específico de la semana, a una hora específica. Por ejemplo, puedes retrasar a los usuarios hasta la próxima vez que llegue el jueves a las 4 pm en la zona horaria de la empresa.

Para configurar esto correctamente, también necesitarás seleccionar qué sucede si el usuario entra en el Canvas el día de la semana seleccionado (por ejemplo, jueves), pero después de la hora especificada. Puedes elegir avanzar al usuario el mismo día o retenerlo hasta la semana siguiente.
{% endtab %}
{% endtabs %}

## Uso de los pasos de demora

Supongamos que es 10 de junio. El 11 de junio, te gustaría que los usuarios entraran en el Canvas y recibieran un mensaje sobre una próxima promoción. Luego, quieres retener a los usuarios en el Canvas hasta el 17 de junio a las 3 pm hora local. A las 3 pm hora local del 17 de junio, quieres enviar a los usuarios un mensaje recordatorio sobre la promoción.

La secuencia de pasos del Canvas podría verse así:

1. Comienza añadiendo un paso de mensaje que se envíe inmediatamente después de que los usuarios entren en el Canvas el 11 de junio.
2. Crea un paso de demora que retenga a los usuarios hasta la 1 pm hora local del 17 de junio.
3. Vincula el paso de demora a otro paso de mensaje que envíe su mensaje inmediatamente.

### Componentes de demora al final de un Canvas {#delay-as-last-step}

Si añades un componente de demora a tu Canvas y no hay pasos posteriores, cualquier usuario que llegue al último paso será automáticamente sacado del Canvas. Esto es así incluso si el tiempo del paso de demora aún no se ha alcanzado. Esto significa que los usuarios que ya hayan llegado al paso de demora no recibirán ningún mensaje que añadas después de este paso. Sin embargo, si un usuario no ha llegado al paso de demora y se añade un mensaje, entonces sí recibiría ese mensaje.

### Demoras personalizadas

{% multi_lang_include early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Selecciona el conmutador **Personalize delay** para configurar una demora personalizada para tus usuarios. Puedes usar esto con un [paso de Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) para seleccionar la variable de contexto por la cual retrasar. Esto anulará la hora del día establecida en el atributo o propiedad seleccionados. Esto es útil cuando se aplica un desfase en días o semanas y quieres que los usuarios avancen a una hora específica. La zona horaria proviene del atributo o propiedad, o usa la alternativa si no hay ninguna disponible.

#### Comportamiento de la zona horaria para "a una hora específica"

Al configurar demoras personalizadas con la opción **at specific time**, el comportamiento de la zona horaria depende del tipo de datos de tu atributo o variable de contexto:

- **Tipo de datos cadena con zona horaria:** si el atributo o la variable de contexto es un tipo de datos cadena que incluye información de zona horaria, se ajusta a la zona horaria especificada en la cadena. Por ejemplo, `2025-06-10T10:00:00-08:00` usa UTC-8.
- **Tipo de datos cadena sin zona horaria:** si el atributo o la variable de contexto es un tipo de datos cadena sin información de zona horaria, se ajusta a la zona horaria alternativa. Por ejemplo, `2025-06-10` usa la zona horaria alternativa.
- **Tipo de datos hora:** si el atributo o la variable de contexto es un tipo de datos hora, se ajusta a UTC. Esto se debe a que el tipo de datos hora siempre se convierte a UTC cuando se guarda en la base de datos, por lo que "a una hora específica" siempre hará referencia a UTC cuando la variable esté configurada como tipo de datos hora. Por ejemplo, `2025-06-10T10:00:00-08:00` usa UTC+0.

{% alert note %}
Es posible que un atributo personalizado o una variable de contexto no tenga ni una hora específica ni una zona horaria si es un tipo de datos cadena. Si es un tipo de datos hora, necesitarás especificar la hora y la zona horaria. Sin embargo, si el atributo personalizado o la variable de contexto es una cadena "irrelevante" (como "product_name"), el usuario saldrá del Canvas.
{% endalert %}

#### Caso de uso

Supongamos que quieres recordar a tus clientes que compren pasta de dientes dentro de 30 días. Usando una combinación de un paso de Context y un paso de demora, puedes seleccionar esta variable de contexto para retrasar. En este caso, tu paso de Context tendría los siguientes campos:

- **Context variable name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![La variable "product_reminder_interval" y su valor.]({% image_buster /assets/img/context_step1.png %})

A continuación, como quieres recordar a tus clientes dentro de 30 días, seleccionarás **Until a specific day** como opción de demora y seleccionarás **Personalize delay** para usar la información de tu paso de Context. Esto significa que tus usuarios serán retrasados hasta la variable de Context seleccionada.

## Análisis de demoras {#delay-analytics}

Los componentes de demora tienen las siguientes métricas disponibles en la vista de análisis de un Canvas activo o previamente activo.

| Métrica | Descripción |
|---|---|
| _Entered_ | Refleja el número de veces que se ha entrado en el paso. Si tu Canvas tiene reelegibilidad y un usuario entra en un paso de demora dos veces, se registrarán dos entradas. |
| _Proceeded to Next Step_ | Refleja el número de entradas que avanzaron al siguiente paso en el Canvas. |
| _Exited Canvas_ | Refleja el número de entradas que salieron del Canvas y no avanzaron al siguiente paso. |
| _Personalization Failed_ | Refleja el número de veces que un mensaje o contenido personalizado destinado a un usuario no pudo entregarse debido a lo siguiente:<br> {::nomarkdown}<ul><li>El valor de la demora está en el pasado</li><li>El valor de la demora supera los 2 años en el futuro</li><li>El valor de <b>After a duration</b> no es un número</li><li>El valor de <b>Until a specific day</b> no es una fecha o una cadena con formato de fecha</li></ul>{:/} <br>Consulta [Errores de personalización fallida](#personaliztion-failed-errors) para más detalles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análisis de demoras" }

Las series temporales de estos análisis están disponibles en la vista expandida del componente.

## Solución de problemas

### Errores de personalización fallida {#personaliztion-failed-errors}

Si los usuarios no están desencadenando una demora personalizada, podría ser porque el paso de Context que configuraste para calificarlos para el paso de demora no está funcionando como esperabas. Cuando una [variable de contexto no es válida]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#troubleshooting), un usuario continuará a través de tu Canvas sin que su contexto sea establecido por el paso de Context. Esto puede hacer que no califiquen para pasos posteriores en tu Canvas, como las demoras personalizadas.

### Usuarios en un paso de demora cuando se detiene un Canvas

Cuando [detienes un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#stopping-canvases), los usuarios que ya están esperando en un paso de demora no salen inmediatamente. Braze aún programa la finalización de la demora, pero **no se envían más mensajes** mientras el Canvas está detenido.

Si vuelves a habilitar el Canvas antes de que la demora de un usuario haya transcurrido, puede avanzar al siguiente paso según lo programado. Si la ventana de demora ya ha pasado mientras el Canvas estaba detenido, esos usuarios salen del Canvas en lugar de recibir el siguiente paso. Para ver ejemplos, consulta [¿Qué sucede cuando detienes un Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-happens-when-you-stop-a-canvas) y [Detener Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#stopping-canvases).