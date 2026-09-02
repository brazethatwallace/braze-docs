---
nav_title: Crear bloques de formulario personalizados
article_title: Crear bloques de formulario personalizados en páginas de destino
page_order: 6
page_type: reference
description: "Aprende a crear entradas de formulario interactivas personalizadas en las páginas de destino de Braze para que sus valores se validen y envíen junto con los bloques de formulario estándar."
---

# Crear bloques de formulario personalizados en páginas de destino {#create-custom-form-blocks-on-landing-pages}

> Los [bloques de formulario]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) de las páginas de destino de Braze capturan entradas estándar, como campos de texto, casillas de verificación y menús desplegables. Los bloques de formulario personalizados amplían las posibilidades al permitirte crear tus propios elementos interactivos, como una calificación con estrellas, un SELECTOR de sentimiento con emojis o una tarjeta de rasca y gana.

Cuando un visitante envía el formulario personalizado, el valor que seleccionó se valida y guarda junto con tus campos estándar, y luego se envía a Braze como un atributo de usuario personalizado. Esto te permite recopilar datos más ricos y atractivos sin salir del editor de páginas de destino.

Los bloques de formulario personalizados se crean con un único helper de JavaScript, `window.brazeHelpers.forms.registerFormInput`, al que llamas desde un bloque de **Custom Code** en la página de destino.

{% alert note %}
Los cuestionarios y los mensajes dentro de la aplicación tienen sus propios bloques de formulario, pero `registerFormInput` —la API de JavaScript para conectar una interfaz codificada de forma personalizada a un bloque de formulario— solo está disponible en las páginas de destino.
{% endalert %}

## Cómo funciona {#how-it-works}

Una entrada de formulario personalizada es cualquier elemento en tu página de destino cuyo valor deseas capturar y enviar con el formulario. Conectas ese elemento al sistema de formularios de Braze registrándolo. El registro le indica a Braze qué elemento observar, cómo leer su valor actual y qué hacer con ese valor cuando se envía el formulario.

1. Crea tu interfaz personalizada dentro de un bloque de **Custom Code** en la página de destino y asígnale un SELECTOR CSS estable, como un `id`.
2. Registra el elemento llamando a `window.brazeHelpers.forms.registerFormInput` con un objeto de configuración.
3. Braze llama a tu función `getValue` para leer el valor actual cuando lo necesita.
4. Si el campo es obligatorio, o proporcionas una función `onValidate`, Braze bloquea el envío hasta que el valor pase la validación, y marca un elemento no válido con una clase CSS que puedes estilizar. Consulta [Validación y campos obligatorios](#validation-and-required-fields).
5. Cuando el formulario se envía y la validación pasa, Braze llama a tu función `onSubmit`, donde puedes llamar al SDK or kit de desarrollo de software de Braze para registrar información como un atributo de usuario personalizado.

Como tú proporcionas las funciones que leen, validan y envían el valor, este enfoque funciona con prácticamente cualquier elemento de formulario personalizado, por lo que no estás limitado a los tipos de campo estándar del editor.

## Marco básico {#basic-framework}

El registro más sencillo apunta a un elemento, lo trata como obligatorio, lee su valor de un atributo de datos y escribe ese valor en un atributo de usuario personalizado cuando se envía el formulario. Envuelve la llamada en un listener `DOMContentLoaded`, como en los ejemplos de esta página, para que el elemento exista antes de que se ejecute `registerFormInput`:

```js
document.addEventListener("DOMContentLoaded", () => {
  window.brazeHelpers.forms.registerFormInput({
    selector: "#my-custom-input",
    isRequired: true,
    getValue: (element) => element.dataset.value ?? null,
    onSubmit: (value) => {
      window.brazeBridge.getUser().setCustomUserAttribute("my_attribute", value);
    },
  });
});
```

Llama a `registerFormInput` una vez por cada entrada personalizada en la página. Los campos de formulario estándar colocados a través del editor de páginas de destino no necesitan ser registrados; el registro es solo para las entradas personalizadas que creas en un bloque de **Custom Code**.

## Referencia de configuración {#configuration-reference}

`registerFormInput` acepta un único objeto de configuración. Expresado como firma de función, la forma completa es:

```js
window.brazeHelpers.forms.registerFormInput({
  // Provide exactly one of `selector` or `element` to identify the input.
  selector?: string,
  element?: HTMLElement,
  isRequired?: boolean | Promise<boolean>,
  getValue: (element: HTMLElement) => value,
  onValidate?: (value, element: HTMLElement) => boolean | Promise<boolean>,
  onSubmit?: (value, element: HTMLElement) => void | Promise<void>,
});
```

Como mínimo, debes proporcionar una forma de localizar el elemento (`selector` o `element`) y una función `getValue`. Todo lo demás es opcional.

| Propiedad | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `selector` | `string` | Sí (o `element`) | Un SELECTOR CSS que coincida con tu elemento personalizado, por ejemplo `"#scratch-card"`. Braze lo resuelve de forma diferida con `querySelector` en el momento de la validación y el envío, por lo que puede coincidir con un elemento añadido al DOM después de que se ejecute `registerFormInput`. |
| `element` | `HTMLElement` | Sí (o `selector`) | Una referencia directa al elemento, utilizada en lugar de `selector`. Solo se usa mientras el elemento permanece adjunto a la página, y tiene prioridad sobre `selector` cuando se proporcionan ambos. |
| `isRequired` | `boolean \| Promise<boolean>` | No | Cuando es `true`, el formulario no se puede enviar hasta que la entrada tenga un valor no vacío: `null`, `undefined`, cadenas vacías (incluidas las que solo contienen espacios en blanco) y arrays vacíos cuentan como vacíos. También puede ser una promesa que se resuelve a un booleano, que Braze reevalúa cada vez que se valida la entrada, para que puedas decidir el estado de obligatoriedad en tiempo de ejecución. El valor predeterminado es `false`. Consulta [Validación y campos obligatorios](#validation-and-required-fields) para el orden completo de validación. |
| `getValue` | `function` | Sí | Devuelve el valor actual de la entrada. Braze pasa el elemento coincidente como argumento, para que puedas leer el valor del DOM, por ejemplo `element.dataset.sentiment`, o de una variable en tu propio código. Devuelve `null` cuando aún no hay un valor. |
| `onValidate` | `function` | No | Recibe el valor actual y el elemento coincidente, y debe devolver `boolean \| Promise<boolean>` —el mismo tipo de retorno que `isRequired`— donde `true` significa que el valor es válido y `false` que no lo es. Úsalo para aplicar reglas más allá de tener un valor, por ejemplo que el valor sea uno de un conjunto permitido. Si se omite, solo se aplican `isRequired` y la validación de restricciones nativa. |
| `onSubmit` | `function` | No | Se ejecuta cuando el formulario se envía y la validación pasa. Recibe el valor actual y el elemento coincidente. Aquí es donde registras el valor en Braze, normalmente con `setCustomUserAttribute`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Referencia de configuración" }

### Actuar sobre el valor en onSubmit {#act-on-the-value-in-onsubmit}

`onSubmit` es un callback de JavaScript simple, por lo que puedes actuar sobre el valor capturado de la forma que tu integración necesite. Como `onSubmit` se ejecuta como parte del envío del formulario, las llamadas a `brazeBridge` realizadas dentro de él funcionan como se espera, incluso para un visitante que abrió la página de destino de forma anónima. Consulta [Disponibilidad del bridge]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#bridge-availability) para la otra situación en la que las llamadas al bridge funcionan.

El patrón más común es escribir el valor capturado en el perfil de usuario con el [bridge de JavaScript de Braze]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) disponible en las páginas de destino:

```js
window.brazeBridge.getUser().setCustomUserAttribute("attribute_name", value);
```

Usa un nombre de atributo personalizado que ya exista, o uno que desees crear, en tu espacio de trabajo. El valor que pasas se almacena en el perfil del usuario y luego se puede usar para segmentación, personalización y para desencadenar mensajes de seguimiento.

No estás limitado a atributos personalizados. Desde el mismo callback, puedes llamar a cualquier [método de `brazeBridge.getUser()`]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#supported-methods). Por ejemplo, para añadir al usuario a un grupo de suscripción, establecer un atributo estándar, registrar un evento personalizado o enviar el valor a tu propio endpoint de API.

{% alert note %}
No necesitas llamar a `requestImmediateDataFlush` dentro de `onSubmit`. El proceso de envío del formulario vacía automáticamente todos los datos a Braze después de que tu callback `onSubmit` se complete.
{% endalert %}

## Ejemplos {#examples}

Los siguientes ejemplos son completos y autónomos. Cada uno es un bloque único que contiene marcado, una etiqueta `<script>` y una etiqueta `<style>` que pegas en un bloque de **Custom Code** (HTML) en tu página de destino. La llamada a `registerFormInput` cerca del final de cada script conecta la entrada personalizada al formulario de Braze. Pasa el cursor sobre un ejemplo de código y selecciona el icono de copiar para copiarlo.

{% alert important %}
Estos ejemplos se ejecutan completamente en el navegador del visitante. Para el ejemplo de rasca y gana, el "premio" es elegido por JavaScript en el navegador del visitante, por lo que un visitante con conocimientos técnicos podría modificar ese código para obtener el resultado que desee. No confíes en este patrón para recompensas, descuentos u otros resultados que requieran una aplicación estricta por visitante. Valida cualquier cosa sensible en términos de seguridad o ingresos en tus propios servidores.
{% endalert %}

<div class="scrollable-code-examples" markdown="1">

{% tabs local %}
{% tab SELECTOR de sentimiento %}

**Objetivo:** El visitante selecciona una cara feliz o triste, y su elección se escribe en un atributo personalizado de tipo cadena llamado `feedback_sentiment`.

Pega lo siguiente en un único bloque de **Custom Code** (HTML):

```html
<div id="sentiment-picker" class="sentiment-picker">
  <button type="button" data-sentiment="positive" aria-label="Happy">🙂</button>
  <button type="button" data-sentiment="negative" aria-label="Unhappy">🙁</button>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const picker = document.getElementById("sentiment-picker");

    picker.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => {
        picker.dataset.sentiment = button.dataset.sentiment;
        picker.querySelectorAll("button").forEach((b) => b.classList.remove("selected"));
        button.classList.add("selected");
      });
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#sentiment-picker",
      isRequired: true,
      getValue: (element) => element.dataset.sentiment ?? null,
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("feedback_sentiment", value);
      },
    });
  });
</script>

<style>
  .sentiment-picker {
    display: flex;
    gap: 16px;
    justify-content: center;
    font-size: 40px;
  }

  .sentiment-picker button {
    background: none;
    border: 2px solid transparent;
    border-radius: 12px;
    cursor: pointer;
    line-height: 1;
    padding: 8px;
  }

  .sentiment-picker button.selected {
    border-color: #1f2933;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .sentiment-picker.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**Cómo funciona:** Al seleccionar un botón, se almacena su valor `data-sentiment` en el elemento contenedor. `getValue` lee ese valor del elemento contenedor que Braze le pasa. Como `isRequired` es `true`, el formulario no se envía hasta que el visitante elige una cara, y el contenedor se marca con la clase `bz-validation-error` mientras está vacío. Al enviar, el valor elegido (`"positive"` o `"negative"`) se escribe en `feedback_sentiment`.

{% endtab %}
{% tab Rasca y gana %}

**Objetivo:** El visitante rasca una tarjeta para revelar uno de tres descuentos (10% Off, 20% Off o 25% Off), y el descuento se escribe en un atributo personalizado de tipo cadena llamado `scratch_off_reward`.

Este ejemplo dibuja una tarjeta de rasca y gana en un Canvas HTML. Se elige una recompensa al azar cuando se carga la página y se oculta bajo una capa opaca que el visitante rasca. Puedes sustituir el enfoque de Canvas por cualquier widget de rasca y gana que prefieras; solo la llamada a `registerFormInput` lo conecta a Braze. Pega lo siguiente en un único bloque de **Custom Code** (HTML):

```html
<div id="scratch-card" class="scratch-card" data-reward="">
  <span class="scratch-card__reward"></span>
  <canvas class="scratch-card__surface" width="300" height="150"></canvas>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const rewards = ["10% Off", "20% Off", "25% Off"];

    const card = document.getElementById("scratch-card");
    const label = card.querySelector(".scratch-card__reward");
    const canvas = card.querySelector(".scratch-card__surface");
    const ctx = canvas.getContext("2d");

    // Randomly assign which reward this visitor will reveal.
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    label.textContent = reward;

    // Paint the opaque scratch layer over the reward.
    ctx.fillStyle = "#b3b3b3";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = "destination-out";

    let isScratching = false;

    function scratchAt(event) {
      const rect = canvas.getBoundingClientRect();
      ctx.beginPath();
      ctx.arc(event.clientX - rect.left, event.clientY - rect.top, 18, 0, Math.PI * 2);
      ctx.fill();
    }

    canvas.addEventListener("pointerdown", () => { isScratching = true; });
    canvas.addEventListener("pointermove", (event) => {
      if (isScratching) scratchAt(event);
    });
    canvas.addEventListener("pointerup", () => {
      isScratching = false;
      // The visitor has scratched the card, so record the revealed reward.
      card.dataset.reward = reward;
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#scratch-card",
      isRequired: true,
      getValue: (element) => element.dataset.reward || null,
      onValidate: (value) => rewards.includes(value),
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("scratch_off_reward", value);
      },
    });
  });
</script>

<style>
  .scratch-card {
    position: relative;
    width: 300px;
    height: 150px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }

  /* The reward sits underneath and is revealed as the canvas is scratched away. */
  .scratch-card__reward {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    color: #1f2933;
  }

  .scratch-card__surface {
    position: absolute;
    inset: 0;
    border-radius: 12px;
    cursor: pointer;
    touch-action: none;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .scratch-card.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**Cómo funciona:** Cuando se carga la página, el script elige al azar una de las tres recompensas y pinta una capa opaca sobre ella en el Canvas. A medida que el visitante arrastra sobre el Canvas, el modo compuesto `"destination-out"` borra esa capa y revela la recompensa debajo. En `pointerup`, la recompensa revelada se escribe en el atributo `data-reward` de la tarjeta. `getValue` lo lee desde ahí, `onValidate` confirma que es una de las tres recompensas definidas, e `isRequired` impide el envío hasta que la tarjeta haya sido rascada. Al enviar, el descuento revelado (por ejemplo, `"20% Off"`) se escribe en `scratch_off_reward`.

{% endtab %}
{% tab Atribución de Campaign %}

**Objetivo:** Capturar la Campaign que refirió al visitante a la página de destino y registrarla como una propiedad de evento personalizado para informes y atribución posteriores.

Este ejemplo demuestra cómo atribuir el envío de un formulario de página de destino a una Campaign específica. Al añadir una variable Liquid como {% raw %}`{{campaign.${api_id}}}`{% endraw %} a la URL de tu página de destino en mensajes de correo electrónico, servicio de mensajes cortos o WhatsApp, puedes pasar el identificador de la Campaign a la página de destino. El bloque de formulario personalizado luego lee este parámetro de la URL y lo registra como un evento personalizado con el ID de API de la Campaign como propiedad del evento, lo que facilita el seguimiento de qué Campaigns están generando envíos de formularios.

Pega lo siguiente en un único bloque de **Custom Code** (HTML):

```html
<input type="hidden" id="campaign-attribution" value="" />

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const hiddenInput = document.getElementById("campaign-attribution");
    const campaignApiId = new URLSearchParams(window.location.search).get("campaign_api_id");

    if (campaignApiId) {
      hiddenInput.value = campaignApiId;
    }

    window.brazeHelpers.forms.registerFormInput({
      selector: "#campaign-attribution",
      isRequired: false,
      getValue: (element) => element.value || null,
      onSubmit: async (value) => {
        if (!value) {
          return;
        }

        await window.brazeBridge.logCustomEvent("landing_page_form_submitted", {
          campaign_api_id: value,
        });
      },
    });
  });
</script>
```

**Cómo funciona:** Cuando creas un mensaje de correo electrónico, servicio de mensajes cortos o WhatsApp que enlaza a tu página de destino, añade el identificador de la Campaign a la URL usando plantillas Liquid: {% raw %}`https://your-landing-page.com?campaign_api_id={{campaign.${api_id}}}`{% endraw %}. Cuando un visitante llega a la página de destino desde ese mensaje, el script lee el parámetro `campaign_api_id` de la URL y lo almacena en un campo de entrada oculto. Al enviar el formulario, si hay un ID de Campaign presente, el callback `onSubmit` registra un evento personalizado llamado `landing_page_form_submitted` con el ID de API de la Campaign como propiedad del evento. Este evento aparece en Currents y se puede usar para informes, segmentación y análisis de atribución.

{% alert tip %}
Puedes extender este patrón para capturar parámetros de URL adicionales como la variación del mensaje, el paso en Canvas o cualquier otra variable Liquid que desees pasar a la página de destino con fines de atribución.
{% endalert %}

{% endtab %}
{% endtabs %}

</div>

## Validación y campos obligatorios {#validation-and-required-fields}

Una entrada debe pasar todas las siguientes capas que le apliquen antes de que el formulario pueda enviarse:

1. **`isRequired`** condiciona el envío a la presencia de un valor no vacío. Devuelve `null` desde `getValue` cuando la entrada aún no tiene un valor para que Braze pueda saber que está vacía. Las cadenas vacías (incluidas las que solo contienen espacios en blanco) y los arrays vacíos también se tratan como vacíos, mientras que `0` y `false` cuentan como valores presentes. `isRequired` puede ser un booleano o una promesa que se resuelve a uno, y se reevalúa cada vez que se valida la entrada.
2. **Validación de restricciones nativa.** Si el elemento coincidente soporta la API estándar de HTML `checkValidity()`, por ejemplo un `<input>` nativo con `required`, `pattern`, `min` o `max`, Braze la ejecuta y bloquea el envío cuando falla. Para elementos completamente personalizados y no nativos (un `div`, un `canvas`, etc.), esta comprobación siempre pasa, por lo que nunca interfiere con tu propia lógica.
3. **`onValidate`** condiciona el envío a tus propias reglas. Recibe el valor actual y el elemento coincidente, y debe devolver `boolean \| Promise<boolean>` —el mismo tipo de retorno que `isRequired`— donde `true` significa que el valor es válido y `false` que no lo es. Úsalo para comprobaciones de valores permitidos, comprobaciones de formato, rangos o cualquier lógica que puedas expresar en JavaScript.

### Estilo de errores {#error-styling}

Cada vez que una entrada falla la validación, Braze añade la clase CSS `bz-validation-error` al elemento coincidente por tu `selector` o `element`, y elimina la clase cuando la entrada vuelve a ser válida. Estiliza el estado no válido como prefieras, por ejemplo un contorno o borde que llame la atención sobre la entrada problemática, añadiendo una regla que apunte a tu elemento combinado con la clase `bz-validation-error`:

```css
#my-custom-input.bz-validation-error {
  outline: 3px solid #f94144;
  outline-offset: 4px;
}
```

Estilizar el estado de error es opcional pero recomendado, para que los visitantes puedan ver qué entrada personalizada está bloqueando el envío. Cada [ejemplo](#examples) en esta página incluye una regla `bz-validation-error`.

## Mejores prácticas {#best-practices}

- Usa un SELECTOR estable y único. Un `id` es la opción más segura. Evita selectores que puedan coincidir con más de un elemento.
- Devuelve `null`, no una cadena vacía o `undefined`, cuando no hay valor, para que las comprobaciones de obligatoriedad se comporten de forma predecible. Las cadenas vacías y los arrays vacíos también se tratan como vacíos, pero `null` es la señal más clara de "sin valor".
- Mantén `getValue` ligero y síncrono. Braze puede llamarlo más de una vez, por lo que debería leer y devolver el valor actual en lugar de realizar trabajo pesado.
- Estiliza el estado `bz-validation-error` para que los visitantes puedan ver qué entrada personalizada está bloqueando el envío.
- Define los nombres de tus atributos personalizados con anticipación y mantenlos consistentes para que puedas segmentar de forma fiable con los datos posteriormente.
- Prueba el envío completo. Confirma que el atributo aparece en el perfil de usuario después de enviar, y que las reglas de obligatoriedad y validación bloquean el envío como se espera.

## Solución de problemas {#troubleshooting}

### El formulario se envía aunque no se seleccionó nada {#the-form-submits-even-though-nothing-was-selected}
Asegúrate de que `isRequired` esté establecido en `true`. Braze trata `null`, `undefined`, cadenas vacías (incluidas las que solo contienen espacios en blanco) y arrays vacíos como sin valor; si `getValue` está devolviendo algo diferente (por ejemplo, un valor predeterminado no vacío o un marcador de posición) cuando no se ha seleccionado nada, la comprobación de obligatoriedad no lo detectará.

### El valor no aparece en el perfil {#the-value-doesnt-appear-on-the-profile}
Confirma que `onSubmit` llama a `window.brazeBridge.getUser().setCustomUserAttribute` con el nombre de atributo correcto, y que el bloque de **Custom Code** está en la misma página de destino que el formulario.

### El registro parece no hacer nada {#registration-seems-to-do-nothing}
Verifica que el SELECTOR coincida con un elemento que exista en el DOM cuando se ejecuta `registerFormInput`, y que el script se ejecute después de que ese elemento se haya renderizado. Luego abre la consola para desarrolladores de tu navegador: `registerFormInput` valida su configuración y, cuando algo está mal (por ejemplo, falta `getValue`, un SELECTOR que no es un SELECTOR CSS válido o una propiedad del tipo incorrecto), ignora el registro y muestra una advertencia con el prefijo `[brazeHelpers.forms.registerFormInput]` describiendo qué era inválido.

## Contenido relacionado {#related-content}

- [Bridge de JavaScript para páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) cubre la referencia completa de `brazeBridge` utilizada en `onSubmit`.
- [Crear páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)