---
nav_title: Rutas de acción
article_title: Rutas de acción
alias: /action_paths/
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo usar las Rutas de acción, un componente que te permite clasificar a los usuarios en función de sus acciones."
tool: Canvas
---

# Rutas de acción {#action-paths}

> Las Rutas de acción en Canvas te permiten clasificar a tus usuarios en función de sus acciones.

![Un paso de Rutas de acción en un recorrido de usuario de Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Con las Rutas de acción, puedes:

* Personalizar las rutas de los usuarios en función de una acción específica, incluyendo eventos de interacción del usuario y eventos personalizados
* Retener a los usuarios durante un periodo determinado para priorizar su siguiente ruta en función de sus acciones durante este periodo de evaluación

## Crear una ruta de acción {#creating-an-action-path}

Para crear una ruta de acción, añade un componente a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o selecciona el botón de signo más <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **Rutas de acción**.

### Configuración de la acción {#action-settings}

En la **Configuración de la acción**, establece la **Ventana de evaluación** para determinar cuánto tiempo se retiene a los usuarios en el paso. Por defecto, los usuarios se evalúan en un plazo de un día, pero puedes ajustar esta ventana en segundos, minutos, horas, días y semanas según tu Canvas. La ventana de evaluación máxima para una ruta de acción es de 31 días.

Dentro de la **Configuración de la acción**, también puedes activar el orden clasificado para tus componentes activando la opción **Avanzar usuarios según el orden clasificado**.

![La Configuración de la acción con una ventana de evaluación de 1 día.]({% image_buster /assets/img/actionpath_settings.png %})

Por defecto, la **Clasificación** está desactivada. Cuando un usuario entra en la ruta de acción y realiza el evento desencadenante asociado a cualquier grupo de acción, avanza inmediatamente a través del grupo de acción correspondiente en función de la **primera acción que cumpla los requisitos** que realice después de entrar en el paso. Si un usuario realiza una segunda acción que coincide con un grupo de acción diferente, no cambia de ruta: la primera acción determina su recorrido. Si un usuario no realiza un evento desencadenante, avanza a través del grupo predeterminado **El resto** al final del periodo de evaluación.

Cuando **Avanzar usuarios según el orden clasificado** está activado, significa que la **Clasificación** está activa. Así, todos los usuarios se retienen hasta el final de la ventana de evaluación. Al final del periodo de evaluación, los usuarios avanzan a través del grupo de acción de mayor prioridad para el que sean elegibles al final de la ventana de evaluación. Los usuarios que no realicen ninguna de las acciones durante la ventana de evaluación avanzan a través del grupo predeterminado **El resto**.

{% alert tip %}
Para dirigir a los usuarios en función de sus atributos actuales o pertenencia a un segmento en lugar de las acciones que realizan, usa [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) en su lugar.
{% endalert %}

Ten en cuenta que puedes desencadenar una ruta de acción cuando cambia un objeto de atributo personalizado anidado, pero no para matrices de atributos personalizados anidados ni para cambios en tipos de datos de matriz de objetos.

#### Mensajes dentro de la aplicación {#in-app-messages}

Ten en cuenta que cuando el desencadenante del grupo de acción es iniciar una sesión, y el siguiente paso es un mensaje dentro de la aplicación, el usuario debe realizar dos inicios de sesión para recibir el mensaje dentro de la aplicación. La primera sesión asigna al usuario al grupo de acción dentro de la ruta de acción, y la segunda sesión desencadena el mensaje dentro de la aplicación.

#### Ejemplo de estado de clasificación {#ranking-status-example}

Supongamos que tienes una ruta de acción con un periodo de evaluación de un día con dos grupos de acción: Grupo 1 y Grupo 2. El Grupo 1 tiene un evento desencadenante "Iniciar sesión", y el Grupo 2 tiene "Realizar compra". Si la **Clasificación** está activada, todos los usuarios en la ruta de acción se "retienen" durante un día. Al final del día, si un usuario ha iniciado una sesión y ha realizado una compra, avanza por la ruta de mayor clasificación. En este caso, el usuario avanzaría al Grupo 1.

En el ejemplo anterior, si la **Clasificación** está desactivada y un usuario realiza uno de los eventos desencadenantes ("Iniciar sesión" o "Realizar compra"), ese usuario avanza en el grupo de acción correspondiente en función de la acción desencadenante.

Ten en cuenta que las propiedades de entrada de Canvas difieren de las propiedades del evento. Las propiedades de entrada de Canvas son propiedades del evento que desencadenó el Canvas. Estas propiedades solo se pueden usar en el primer paso completo de un Canvas cuando se utiliza el flujo de trabajo original de Canvas. Cuando se usa Canvas, las propiedades de entrada persistentes están habilitadas y permiten reutilizar las propiedades de entrada en todo el Canvas. Por el contrario, las propiedades del evento se originan a partir de un evento o acción que ocurre mientras el usuario avanza por su flujo de trabajo.

### Grupos de acción {#action-groups}

Añade un desencadenante o varios desencadenantes para definir tus grupos de acción. Aquí puedes seleccionar una variedad de desencadenantes, como si los usuarios:

- Realizan una compra
- Inician una sesión
- Realizan un [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- Realizan un evento de conversión
- Añaden una dirección de correo electrónico
- Cambian el valor de un atributo personalizado.
  - Esto incluye añadir un nuevo atributo con un valor a un perfil de usuario por primera vez (cuando el atributo no estaba presente anteriormente).
  - Los desencadenantes de atributos no están disponibles para atributos de tipo matriz.
- Actualizan su estado de suscripción o estado del grupo de suscripción
- Interactúan con una Campaign o tarjeta de contenido
- Entran en una ubicación
- Desencadenan una geovalla
- Envían un mensaje de entrada por SMS o WhatsApp

#### Desencadenante de añadir una dirección de correo electrónico {#add-an-email-address-trigger}

El desencadenante del grupo de acción **Añadir una dirección de correo electrónico** se activa cuando se añade o actualiza una dirección de correo electrónico en un perfil de usuario durante la **Ventana de evaluación** de la ruta de acción. Este comportamiento coincide con otros desencadenantes de actualización de perfil: los usuarios avanzan a través del grupo de acción cuando el cambio de perfil cumple los requisitos de tu configuración, incluyendo cualquier filtro en el desencadenante.

![Un grupo de acción llamado "Grupo 1" para usuarios que realizan cualquier compra.]({% image_buster /assets/img/actionpath_group.png %})

En la configuración de cada grupo de acción, también tienes la opción de seleccionar la casilla **Quiero que este grupo salga del Canvas**, lo que significa que los usuarios de este grupo salen del Canvas al final del periodo de evaluación.

### Canvas con reelegibilidad {#canvases-with-re-eligibility}

Si los usuarios entran en una ruta de acción varias veces y tienen múltiples entradas en la ruta de acción al mismo tiempo, el comportamiento esperado varía según el estado de la **Clasificación**.

| Estado de clasificación | Comportamiento de la ruta de acción |
|---|--------------|
| **Desactivada** | Un usuario puede entrar en una ruta de acción más de una vez. Estas entradas se retienen en la ruta de acción hasta que se registra una acción o evento desencadenante. Si el evento desencadenante no cumple los filtros de propiedades de una entrada (por ejemplo, una [variable de contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables) no coincide con los filtros de propiedades del desencadenante), la entrada permanece en la ruta de acción. <br><br>Si el evento desencadenante cumple más de una entrada, Braze deduplica solo estas entradas y avanza inmediatamente la entrada coincidente más antigua a través del grupo de acción correspondiente. |
| **Activada** | Todas las entradas avanzan al final de la ventana de evaluación correspondiente. No se realiza deduplicación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas con reelegibilidad" }

{% alert warning %}
No cambies **Avanzar usuarios según el orden clasificado** después del lanzamiento cuando los usuarios ya están en el paso. Braze aplica la configuración de clasificación actual al procesar eventos y cuando finaliza la ventana de evaluación, pero el estado de la ruta registrado anteriormente en la ventana puede reflejar una configuración previa. Por ejemplo, si desactivas la clasificación después de que los usuarios realizaron una acción clasificada, es posible que no avancen por la ruta que esperas cuando se cierre la ventana. En su lugar, crea una nueva ruta de acción con la configuración de clasificación deseada, o duplica el Canvas.
{% endalert %}

Ten en cuenta que las clasificaciones no son [editables después del lanzamiento]({{site.baseurl}}/post-launch_edits).