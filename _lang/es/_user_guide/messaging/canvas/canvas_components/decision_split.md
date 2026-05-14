---
nav_title: División de decisiones
article_title: División de decisiones
alias: /decision_split/
page_order: 7
page_type: reference
description: "Este artículo de referencia explica cómo crear y usar divisiones de decisiones en tu Canvas."
tool: Canvas

---

# División de decisiones {#decision-split}

> El componente de división de decisiones en Canvas te permite ofrecer experiencias personalizadas y en tiempo real a tus usuarios.

![Un paso de división de decisiones llamado "¿Push habilitado?" para usuarios que no tienen push habilitado y usuarios que sí lo tienen.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Este componente se puede usar para crear ramas en Canvas en función de si un usuario coincide con una consulta.

## Crear una división de decisiones {#create-a-decision-split}

Para crear una división de decisiones en tu flujo de trabajo, añade un paso a tu Canvas. Luego, arrastra y suelta el componente desde la barra lateral, o selecciona el botón de signo más <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **División de decisiones**.

### Define tu división {#define-your-split}

¿Cómo quieres dividir a tus usuarios? Puedes usar [Segments]({{site.baseurl}}/user_guide/audience/segments/) y filtros para trazar la línea. Básicamente, estás creando una consulta de `true` o `false` que evaluará a tus usuarios y luego los dirigirá a un paso u otro. Debes usar al menos un segmento o un filtro. No necesitas usar tanto un segmento como un filtro.

![Un paso de división de decisiones con el filtro "Foreground Push Enabled is true" seleccionado.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
De forma predeterminada, los segmentos y filtros de un paso de división de decisiones se verifican justo después de recibir un paso anterior, a menos que añadas un retraso.
{% endalert %}

## Usa tu división {#use-your-split}

Usar una división de decisiones puede ayudarte a distinguir caminos para tus usuarios en función de su segmento o sus atributos, ¡e incluso de si utilizan ciertos canales de mensajería para recibir tus mensajes!

Supongamos que estás creando un flujo de incorporación. Podrías empezar con un correo electrónico de bienvenida al registrarse. Luego, dos días después, quieres enviar un mensaje push, pero solo a los usuarios que tienen push habilitado. Después de eso, todos los usuarios reciben otro correo electrónico tres días después de haberse registrado. También podrías usar tu división de decisiones para enviar un mensaje dentro de la aplicación a los usuarios que no tienen push habilitado para animarlos a activarlo.

Si no hay un paso después de uno de los caminos, los usuarios que sigan ese camino saldrán del Canvas.

![Un paso de división de decisiones llamado "¿Push habilitado?" para usuarios que no tienen push habilitado y los que sí. Para los usuarios que no tienen push habilitado, experimentarán un retraso de 3 días y luego recibirán un mensaje de correo electrónico. Para los usuarios que tienen push habilitado, experimentarán un retraso de 1 día, recibirán una notificación push seguida de un retraso de 2 días, y luego recibirán el mismo mensaje de correo electrónico que los usuarios que no tienen push habilitado.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Análisis {#analytics}

Consulta la siguiente tabla para ver las descripciones de los análisis de este paso:

| Métrica | Descripción |
|---|---|
| _Ingresaron_ | El número total de veces que se ingresó al paso. Si tu Canvas tiene reelegibilidad y un usuario ingresa a un paso de división de decisiones dos veces, se registrarán dos entradas. |
| _Sí_ | El número de entradas que cumplieron los criterios especificados y continuaron por el camino "sí". |
| _No_ | El número de entradas que no cumplieron los criterios especificados y continuaron por el camino "no". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }