---
nav_title: Demora
article_title: Demora
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Este artículo de referencia explica cómo añadir una demora a tu Canvas sin necesidad de agregar un mensaje asociado."
tool: Canvas

---

# Demora {#delay}

> Los componentes de demora te permiten añadir una demora independiente a un Canvas. Puedes añadir una demora a tu Canvas sin necesidad de agregar un mensaje asociado.

Las demoras pueden hacer que tu Canvas se vea más limpio. También puedes usar este componente para retrasar un paso diferente hasta una fecha exacta, hasta un día específico o hasta un día específico de la semana. Un componente de demora puede conectarse como máximo a un paso posterior. <br> ![Un paso de demora con una demora de 1 día como primer paso de un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Crear un retraso {#create-a-delay}

Para crear un retraso, añade un paso a tu Canvas. Arrastra y suelta el componente de retraso desde la barra lateral, o selecciona el botón de suma <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y luego elige **Retraso**.

### Retrasos extendidos {#extended-delays}

Puedes extender los pasos de retraso hasta dos años (730 días). Por ejemplo, si estás incorporando nuevos usuarios para tu aplicación, puedes añadir un retraso extendido de dos meses antes de enviar un paso de mensaje para incentivar a los usuarios que no han iniciado una sesión.

## Tipos de retraso {#time-delay-types}

Puedes elegir el tipo de retraso antes del siguiente mensaje en tu Canvas. Puedes establecer un retraso para que tus usuarios esperen durante un período de tiempo designado, o retrasar a tus usuarios hasta una fecha y hora específicas.

Si hay un retraso, es de esperar que algunos usuarios pasen al siguiente paso del Canvas solo después de que finalice el retraso. Los usuarios que estén en el retraso no se añadirán a la métrica _Proceeded to Next Step_. Para más información, consulta [Análisis de retraso](#delay-analytics).

{% tabs %}
{% tab Duración %}

Seleccionar **Duración** te permite retrasar a los usuarios durante un número determinado de segundos, minutos, horas, días o semanas, y a una hora específica. Por ejemplo, puedes retrasar a los usuarios durante cuatro horas o durante un día.

Ten en cuenta la diferencia entre cómo se calculan los "días" y los "días de calendario".

- Un "día" equivale a 24 horas y se calcula desde el momento en que el usuario entra en el paso de retraso.
- Un "día de calendario" define el tiempo de espera hasta la siguiente hora especificada, que podría ser inferior a 24 horas. Puedes elegir retrasar en la hora de la empresa o en la hora local del usuario. Si no se especifica una hora, el usuario se retrasa hasta la medianoche del día siguiente en la hora de la empresa.

### Comportamiento del retraso: "días de calendario" a una hora específica frente a "días" {#delay-behavior-calendar-days-at-a-specific-time-versus-days}

Cuando seleccionas **días de calendario** como unidad y habilitas **A una hora específica** (por ejemplo, **1 día de calendario a las 9 AM**), Canvas calcula primero la fecha del calendario objetivo y luego aplica la hora programada. Por ejemplo, si un paso de Canvas se envía a las 9 PM del lunes y el paso de retraso está configurado como **1 día de calendario a las 9 AM**, el siguiente paso se envía a las 9 AM del martes. Canvas calcula lunes + 1 día de calendario = martes y luego aplica la hora de las 9 AM.

Por el contrario, cuando seleccionas **días** como unidad sin **A una hora específica** (por ejemplo, **Después de 1 día**), Canvas espera un período completo de 24 horas desde el momento en que el usuario entra en el paso de retraso. Por ejemplo, si un paso se envía a las 9:35 AM del 13 de octubre y el paso de retraso es **Después de 1 día**, el siguiente paso se envía a las 9:35 AM del 14 de octubre.

También puedes seleccionar **A una hora específica** para especificar cuándo avanzan los usuarios en el Canvas. Esta opción tiene en cuenta la hora en que el usuario entró en el paso de retraso. Si esta hora es posterior a la hora configurada en los ajustes, Braze añade más horas al retraso.

Como ejemplo, supongamos que hoy es 11 de diciembre y nuestro paso de retraso está configurado como **Duración** de una semana a las 8 am UTC. Si un usuario entra en el paso de retraso el 4 de diciembre, se libera del paso de retraso para continuar su recorrido hoy si originalmente entró en el paso de retraso antes de las 8 am UTC. Si entró en el paso de retraso después de esta hora, el usuario se retrasa hasta el día siguiente (la siguiente ocurrencia de esta hora).

{% endtab %}
{% tab Fecha del calendario %}

Seleccionar **Fecha del calendario** te permite retener a los usuarios en el paso hasta una fecha y hora específicas.

### Consideraciones {#considerations}

#### Los usuarios no recibirán pasos o mensajes con fechas pasadas {#users-wont-receive-past-dated-steps-or-messages}

Si la fecha y hora seleccionadas ya han pasado cuando los usuarios llegan al paso de retraso, los usuarios salen del Canvas. Puede haber hasta 31 días entre el inicio del Canvas y las fechas elegidas para los pasos de "esperar hasta un día exacto".

{% alert important %}
Si estás participando en el [acceso anticipado a Canvas Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context), puedes establecer retrasos de hasta 2 años.
{% endalert %}

Por ejemplo, los usuarios no recibirán pasos o mensajes en estos escenarios:

- Un mensaje está programado para enviarse el 3 de mayo a las 9 pm, pero el paso de retraso expira el 3 de mayo a las 9 am.
- Un paso de Canvas se retrasa hasta una hora específica en la zona horaria local del usuario, pero los usuarios no tienen una zona horaria configurada en su perfil de usuario. El retraso entonces toma como valor predeterminado la zona horaria de la empresa para estos usuarios, la cual ya ha pasado la hora especificada.

#### Los usuarios salen si un paso de retraso posterior está dentro del plazo de un paso de retraso anterior {#users-exit-if-a-subsequent-delay-step-is-within-a-prior-delay-steps-timeline}

Si el Canvas tiene dos pasos de retraso pero el primer paso de retraso es más largo que el segundo paso de retraso, los usuarios también salen del Canvas.

Por ejemplo, supongamos que un Canvas tiene estos pasos:
- Paso 1: paso de mensaje
- Paso 2: paso de retraso hasta el 13 de diciembre a las 10 pm
- Paso 3: paso de mensaje
- Paso 4: paso de retraso hasta el 13 de diciembre a las 7 pm
- Paso 5: paso de mensaje

Los usuarios que entran en el paso 4 salen del Canvas antes de recibir el paso 5 porque el retraso del paso 4 forma parte del plazo del paso 2.

{% endtab %}
{% tab Día de la semana %}

Seleccionar **Día de la semana** te permite retener a los usuarios en el paso hasta un día específico de la semana, a una hora específica. Por ejemplo, puedes retrasar a los usuarios hasta la próxima vez que llegue el jueves a las 4 pm en la zona horaria de la empresa.

Para configurar esto correctamente, también debes seleccionar qué sucede si el usuario entra en el Canvas en el día de la semana seleccionado (por ejemplo, jueves), pero después de la hora especificada. Puedes elegir avanzar al usuario el mismo día o retenerlo hasta la semana siguiente.
{% endtab %}
{% endtabs %}

### Actualizaciones de perfil durante los retrasos {#profile-updates-during-delays}

Si un usuario entra en un Canvas y añade una dirección de correo electrónico válida durante el paso de retraso antes de que termine, recibe el correo electrónico en el siguiente paso. Esto también se aplica a otras actualizaciones de perfil. Cualquier cambio en los atributos del usuario o en la información de contacto durante el retraso se refleja cuando el usuario avanza a los pasos posteriores.

## Uso de los pasos de demora {#using-delay-steps}

Digamos que es 10 de junio. El 11 de junio, te gustaría que los usuarios entren en el Canvas y reciban un mensaje sobre una promoción próxima. Luego, quieres retener a los usuarios en el Canvas hasta el 17 de junio a las 3 pm en hora local. A las 3 pm en hora local del 17 de junio, quieres enviar a los usuarios un mensaje de recordatorio sobre la promoción.

La secuencia de pasos en Canvas podría verse de la siguiente manera:

1. Comienza agregando un paso de mensaje que se envía inmediatamente después de que los usuarios entran en el Canvas el 11 de junio.
2. Crea un paso de demora que retiene a los usuarios hasta la 1 pm en hora local del 17 de junio.
3. Vincula el paso de demora a otro paso de mensaje que envía su mensaje inmediatamente.

### Componentes de demora al final de un Canvas {#delay-as-last-step}

Si agregas un componente de demora a tu Canvas y no hay pasos posteriores, cualquier usuario que llegue al último paso avanza automáticamente fuera del Canvas. Esto es cierto incluso si el tiempo del paso de demora aún no se ha alcanzado. Esto significa que los usuarios que ya llegaron al paso de demora no reciben ningún mensaje que agregues después de este paso. Sin embargo, si un usuario no ha llegado al paso de demora y se agrega un mensaje, recibe ese mensaje.

### Demoras personalizadas {#personalized-delays}

Selecciona la opción **Personalizar demora** para configurar una demora personalizada para tus usuarios. Puedes usar esto con un [paso de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) para seleccionar la variable de contexto por la cual aplicar la demora. Esto anula la hora del día establecida en el atributo o propiedad seleccionados. Esto es útil cuando se aplica un desfase en días o semanas y quieres que los usuarios avancen a una hora específica. La zona horaria proviene del atributo o propiedad, o usa la alternativa si no hay ninguna disponible.

#### Comportamiento de zona horaria para "A una hora específica" {#time-zone-behavior-for-at-a-specific-time}

Cuando seleccionas la casilla de verificación **A una hora específica**, la hora de entrega que configuras usa la misma zona horaria que Braze utiliza para la fecha de calendario personalizada. Braze no aplica una zona horaria separada para la fecha y la hora. Ambas usan la zona horaria de tu atributo o variable de contexto, o la zona horaria alternativa cuando la variable es una cadena sin información de zona horaria.

Qué zona horaria se aplica depende del tipo de datos de tu atributo o variable de contexto:

- **Tipo de datos cadena con zona horaria:** Si el atributo o variable de contexto es un tipo de datos cadena que incluye información de zona horaria, se ajusta a la zona horaria especificada en la cadena. Por ejemplo, `2025-06-10T10:00:00-08:00` usa UTC-8.
- **Tipo de datos cadena sin zona horaria:** Si el atributo o variable de contexto es un tipo de datos cadena sin información de zona horaria, se ajusta a la zona horaria alternativa. Por ejemplo, `2025-06-10` usa la zona horaria alternativa.
- **Tipo de datos hora:** Si el atributo o variable de contexto es un tipo de datos hora, se ajusta a UTC. Esto se debe a que el tipo de datos hora siempre se convierte a UTC cuando se guarda en la base de datos, por lo que "a una hora específica" siempre hace referencia a UTC cuando la variable está configurada como tipo de datos hora. Por ejemplo, `2025-06-10T10:00:00-08:00` usa UTC+0.

{% alert note %}
Es posible que un atributo personalizado o una variable de contexto no tenga ni una hora específica ni una zona horaria si es un tipo de datos cadena. Si es un tipo de datos hora, necesitarás especificar la hora y la zona horaria. Sin embargo, si el atributo personalizado o la variable de contexto es una cadena "irrelevante" (como "product_name"), el usuario sale del Canvas.
{% endalert %}

#### Caso de uso {#use-case}

Digamos que quieres recordar a tus clientes que compren pasta de dientes dentro de 30 días. Usando una combinación de un paso de contexto y un paso de demora, puedes seleccionar esta variable de contexto para aplicar la demora. En este caso, tu paso de contexto tendría los siguientes campos:

- **Nombre de la variable de contexto:** product_reminder_interval
- **Tipo de datos:** Hora
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![El "product_reminder_interval" y su valor.]({% image_buster /assets/img/context_step1.png %})

A continuación, como quieres recordar a tus clientes dentro de 30 días, seleccionarás **Hasta un día específico** como la opción de demora y seleccionarás **Personalizar demora** para usar la información de tu paso de contexto. Esto significa que tus usuarios se retrasan hasta la variable de contexto seleccionada.

## Análisis de retrasos {#delay-analytics}

Los componentes de retraso tienen las siguientes métricas disponibles en la vista de análisis de un Canvas activo o previamente activo.

| Métrica | Descripción |
|---|---|
| _Ingresados_ | Refleja la cantidad de veces que se ha ingresado al paso. Si tu Canvas tiene reelegibilidad y un usuario ingresa a un paso de retraso dos veces, se registran dos entradas. |
| _Procedieron al siguiente paso_ | Refleja la cantidad de entradas que procedieron al siguiente paso en el Canvas. |
| _Salieron del Canvas_ | Refleja la cantidad de entradas que salieron del Canvas y no procedieron al siguiente paso. |
| _Error en la personalización_ | Refleja la cantidad de veces que un mensaje personalizado o contenido destinado a un usuario no pudo entregarse debido a lo siguiente:<br> {::nomarkdown}<ul><li>El valor del retraso está en el pasado</li><li>El valor del retraso es superior a 2 años en el futuro</li><li>El valor de <b>Después de una duración</b> no es un número</li><li>El valor de <b>Hasta un día específico</b> no es una fecha ni una cadena con formato de fecha</li></ul>{:/} <br>Consulta [Errores de personalización fallida](#personaliztion-failed-errors) para más detalles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análisis de retrasos" }

Las series temporales para estos análisis están disponibles en la vista expandida del componente.

## Solución de problemas {#troubleshooting}

### Errores de personalización fallida {#personalization-failed-errors}

Si los usuarios no están activando un retraso personalizado, podría deberse a que el paso de contexto que configuraste para calificarlos para el paso de retraso no está funcionando como esperabas. Cuando una [variable de contexto no es válida]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#troubleshooting), el usuario continúa a través de tu Canvas sin que el paso de contexto haya establecido su contexto. Esto puede hacer que no califique para pasos posteriores en tu Canvas, como los retrasos personalizados.

## Solución de problemas

### Usuarios en un paso de retraso cuando se detiene un Canvas {#users-in-a-delay-step-when-a-canvas-is-stopped}

Cuando [detienes un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases), los usuarios que ya están esperando en un paso de retraso no salen de inmediato. Braze aún programa la finalización del retraso, pero **no se envían más mensajes** mientras el Canvas esté detenido.

Si vuelves a habilitar el Canvas antes de que transcurra el retraso de un usuario, este puede avanzar al siguiente paso según lo programado. Si la ventana de retraso ya pasó mientras el Canvas estaba detenido, esos usuarios salen del Canvas en lugar de recibir el siguiente paso. Para ver ejemplos, consulta [¿Qué sucede cuando detienes un Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) y [Detener Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).