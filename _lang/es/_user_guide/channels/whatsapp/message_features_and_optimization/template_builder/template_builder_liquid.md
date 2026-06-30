---
nav_title: Liquid
article_title: Liquid en el constructor de plantillas de WhatsApp
description: "Este artículo de referencia cubre Message Extras y la lógica condicional de Liquid en el constructor de plantillas de WhatsApp."
alias: /whatsapp_template_builder_liquid/
page_type: reference
channel:
  - WhatsApp
page_order: 1
---

# Liquid en el constructor de plantillas de WhatsApp {#liquid-in-the-whatsapp-template-builder}

> Puedes usar Liquid para personalizar plantillas en el constructor de plantillas de WhatsApp, pero la estructura de plantillas de Meta crea restricciones que no existen en otros canales de Braze. Dos patrones de Liquid en particular requieren un manejo especial: Message Extras y la lógica condicional de mensajería.

Para Message Extras y la lógica condicional de mensajería, Meta requiere que cada variable en una plantilla contenga contenido renderizado real en el momento del envío. Las variables que devuelven cadenas vacías, o que se comportan como metadatos invisibles en lugar de texto visible, provocan fallos en el envío. Los condicionales que cambian la estructura estática del mensaje en lugar de solo el contenido de la variable también causan un comportamiento inesperado.

{% alert note %}
Las restricciones descritas en este artículo se aplican solo a los mensajes de plantilla (mensajes salientes que usan una plantilla aprobada por Meta). Las restricciones no se aplican a los mensajes de respuesta (enviados dentro de una ventana de mensajería de 24 horas abierta por un usuario), ni a Message Extras, lógica condicional y otros patrones de Liquid en otros canales de Braze.
{% endalert %}

## Resumen {#overview}

| Patrón | ¿Compatible? | Notas |
| ----- | ----- | ----- |
| `message_extras` dentro de una variable con otro contenido visible | ✅ Sí | La etiqueta se captura; el texto visible satisface el requisito de contenido de variable de Meta |
| `message_extras` como único contenido de una variable | ❌ No | Se resuelve como cadena vacía; provoca fallo en el envío |
| Liquid condicional dentro de un espacio de variable | ✅ Sí | Braze evalúa antes del envío; Meta solo ve el valor renderizado final |
| Liquid condicional fuera de un espacio de variable | ❌ No | Las etiquetas de Liquid se renderizan como texto literal; el destinatario ve la sintaxis sin procesar |
| Plantilla que comienza o termina con un espacio de variable | ❌ No | Meta requiere texto estático al inicio y al final de cada plantilla |
| Espacio de variable que se resuelve como cadena vacía | ❌ No | Meta requiere contenido no vacío en cada variable en el momento del envío |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Referencia rápida" }

## Message Extras {#message-extras}

La [etiqueta de Liquid `message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) te permite anotar un mensaje con metadatos de clave-valor en el momento del envío. Estos datos no se renderizan en el cuerpo del mensaje. En su lugar, los datos fluyen hacia Contenido conectado, Currents u otros mecanismos de captura de datos para propósitos como atribución, medición de impacto y enriquecimiento de eventos.

{% raw %}
```liquid
{% message_extras :key campaign_id :value "spring_promo_2025" %}
```
{% endraw %}

### Por qué fallan las variables de Message Extras independientes {#why-standalone-message-extras-variables-fail}

En el constructor de plantillas de WhatsApp, las variables de plantilla (como {% raw %}`{{1}}`, `{{2}}`{% endraw %}) se mapean directamente a expresiones de Liquid. La validación de Meta requiere que cada espacio de variable en la plantilla aprobada contenga contenido no vacío en el momento del envío; debe ser algo que se renderice como texto visible para el destinatario.

Dado que `message_extras` no produce salida renderizada, colocarlo solo dentro de una variable de plantilla envía una cadena vacía para ese espacio de variable. Meta rechaza esto, por lo que el envío del mensaje falla.

{% details Uso incorrecto para el constructor de plantillas de WhatsApp %}

{% raw %}
```
Template variable {{1}}: {% message_extras :key attribution_source :value "canvas_a" %}
```
{% endraw %}

En el momento del envío, {% raw %}`{{1}}`{% endraw %} se resuelve como una cadena vacía, lo que provoca un fallo en el envío.

{% enddetails %}

### Uso correcto {#correct-usage}

Para incluir correctamente una etiqueta `message_extras`, incrusta la etiqueta en una variable existente. Esto significa colocar la etiqueta dentro de un bloque de Liquid que produzca salida visible; específicamente, dentro de la misma expresión que rellena una variable de plantilla real. Meta acepta la variable porque contiene contenido, Braze captura los metadatos y el destinatario solo ve el texto renderizado.

#### Ejemplo {#example}

Supongamos que el cuerpo de la plantilla es:

{% raw %}
```
Hi {{1}}, your order has shipped.
```
{% endraw %}

Y la variable {% raw %}`{{1}}`{% endraw %} está mapeada a:

{% raw %}
```
{{ ${first_name} | default: "there" }}
```
{% endraw %}

Para adjuntar un Message Extra, reescribe la expresión de la variable como:

{% raw %}
```
{{ ${first_name} | default: "there" }}{% message_extras :key order_source :value "canvas_spring" %}
```
{% endraw %}

En el momento del envío, {% raw %}`{{1}}`{% endraw %} se resuelve como algo como `"Alex"`, contenido visible que satisface el requisito de Meta. La etiqueta `message_extras` se evalúa y sus datos se capturan, pero no contribuye nada a la cadena renderizada que ve el destinatario.

### Reglas clave {#key-rules}

- Nunca asignes `message_extras` como el único contenido de una variable de plantilla.
- Siempre adjunta la etiqueta a una variable que se resuelva como texto visible.
- Puedes agregar múltiples etiquetas `message_extras` a la misma expresión de variable sin afectar la salida renderizada.
- Usa este patrón en el cuerpo, el encabezado y cualquier otro espacio de variable.

## Lógica condicional de mensajería {#conditional-messaging-logic}

En los canales de mensajería, los bloques de Liquid `if/elsif/else` pueden incluir o excluir condicionalmente secciones completas de texto. Braze renderiza la salida completa de Liquid antes de enviar, y el resultado es lo que la lógica produzca.

Sin embargo, las plantillas de WhatsApp aprobadas por Meta tienen una estructura fija. Meta piensa en el contenido de las plantillas en dos categorías:

- **Texto estático:** cadenas codificadas que se confirman en la creación de la plantilla y permanecen idénticas para cada destinatario.
- **Espacios de variable:** posiciones de marcador de posición (como {% raw %}`{{1}}`{% endraw %}) cuyo contenido se rellena en el momento del envío.

### Por qué la lógica condicional de mensajería fuera de un espacio de variable falla {#why-conditional-messaging-logic-outside-a-variable-slot-fails}

La proporción de texto estático a espacios de variable en una plantilla aprobada es fija, no puede cambiar por envío y tiene límites estrictos. Meta requiere una cantidad mínima de texto estático por cada espacio de variable en la plantilla; no puedes tener una plantilla que sea mayormente o completamente variables. Esto significa que no puedes incluir Liquid condicional que agregue o elimine texto que Meta considera como contenido estático confirmado.

Si intentas usar un bloque `if/else` para incluir o excluir condicionalmente un fragmento de texto estático, Meta no evalúa la lógica. Las etiquetas de Liquid fuera de un espacio de variable se tratan como texto de salida literal. El destinatario ve las etiquetas de sintaxis de Liquid sin procesar ({% raw %}`{% if %}`, `{% else %}`, `{% endif %}`{% endraw %}) y todo el contenido de las ramas tal cual en su mensaje.

{% details Uso incorrecto para el constructor de plantillas de WhatsApp %}

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}Hi {{1}}, we have an exclusive Gold member offer.{% else %}Hi {{1}}, we have a special offer for you.{% endif %}
```
{% endraw %}

Esto intenta incluir dos plantillas aprobadas diferentes en una sola. El condicional que envuelve texto estático no se comportará como se espera.

{% enddetails %}

### Uso correcto

Los condicionales son válidos y compatibles dentro de un espacio de variable, donde controlan qué valor rellena esa variable. Meta solo ve que {% raw %}`{{1}}`{% endraw %} fue rellenado con contenido; no inspecciona cómo el Liquid interno llegó a ese valor.

#### Ejemplo

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}exclusive Gold member{% else %}valued customer{% endif %}
```
{% endraw %}

Usado como el valor de una variable de plantilla, esto produce `"exclusive Gold member"` o `"valued customer"`. Ambas son cadenas no vacías que satisfacen el requisito de contenido de variable de Meta.

El cuerpo de la plantilla en sí permanece estructuralmente sin cambios:

{% raw %}
```
Hi {{1}}, we have a special offer for you.
```
{% endraw %}

### Coloca la lógica condicional dentro de un espacio de variable {#place-conditional-logic-inside-a-variable-slot}

Hay dos formas de colocar Liquid condicional en un espacio de variable en el constructor de plantillas:

1. **Usa un Content Block (compatible con prerrellenado):** construye tu lógica condicional dentro de un Content Block, luego haz referencia al bloque desde la variable. Este enfoque es compatible con prerrellenado, lo que significa que la variable puede mostrar un valor de vista previa en el constructor de plantillas antes del envío.
2. **Usa un marcador de posición y pega Liquid (sin prerrellenado):** agrega un marcador de posición como {% raw %}`{{1}}`{% endraw %} al crear la plantilla, luego pega tu expresión de Liquid completa directamente en ese espacio de variable. Este enfoque no es compatible con prerrellenado, pero funciona para cualquier lógica de Liquid.

### Otros componentes de Liquid afectados por la misma restricción {#other-liquid-components-affected-by-the-same-constraint}

Cualquier etiqueta de Liquid que no produzca salida visible se renderiza como texto sin procesar si se coloca fuera de una variable. Esto incluye:

- **`catalog_items`:** el Liquid que busca y hace referencia a datos de Catálogo debe estar dentro de un espacio de variable, o las etiquetas aparecen tal cual en el mensaje.
- **`assign`:** las etiquetas de asignación de variables (como {% raw %}{% assign discount = "20%" %}{% endraw %}) no producen salida por sí mismas. Si se usan fuera de un espacio de variable para configurar un valor para uso posterior en el mensaje, la etiqueta `assign` se renderiza literalmente. Incluye cualquier lógica de `assign` al inicio de la expresión de Liquid dentro del espacio de variable donde se necesita su salida.
- **Content Blocks que contienen solo etiquetas de Liquid:** si un Content Block contiene lógica de Liquid pero no produce texto visible (por ejemplo, solo usa etiquetas `assign` o `message_extras`), hacer referencia a él fuera de un espacio de variable hace que el contenido sin procesar del bloque aparezca en el mensaje. Los Content Blocks que no producen salida visible deben incrustarse dentro de un espacio de variable junto con contenido que sí se renderice.

### Restricciones estructurales adicionales {#additional-structural-constraints}

Meta requiere que las plantillas:

- **Comiencen con texto estático.** Las plantillas no pueden abrirse con un espacio de variable (como {% raw %}`{{1}} is ready for you`{% endraw %}).
- **Terminen con texto estático.** Las plantillas no pueden terminar en un espacio de variable.

Estas restricciones existen independientemente de si se usa Liquid. Se aplican a la estructura de la plantilla aprobada en sí.

### Reglas clave

- Usa condicionales libremente dentro de las expresiones de espacios de variable para controlar qué valor se renderiza.
- No uses condicionales para agregar, eliminar o intercambiar texto estático (las partes del mensaje que no son espacios de variable).
- Asegúrate de que cada rama condicional dentro de una variable produzca una cadena no vacía (consulta [Message Extras](#message-extras) para saber por qué las cadenas vacías causan fallos).
- La plantilla debe comenzar y terminar con texto estático tal como se envía a Meta.