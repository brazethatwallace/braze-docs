---
nav_title: Enlaces profundos de acciones de Braze
article_title: Enlaces profundos de acciones de Braze
page_order: 100
description: "Este artículo de referencia explica cómo utilizar los enlaces profundos de acciones de Braze para realizar acciones del SDK or kit de desarrollo de software dentro de los botones del canal de mensajería."
hidden: true
---

# Enlaces profundos de acciones de Braze {#braze-actions-deeplinks}

> Las acciones de Braze te permiten utilizar "enlaces profundos" para realizar funciones nativas del SDK or kit de desarrollo de software.<br><br>El panel de Braze incluye varias acciones estándar al hacer clic (Solicitar permiso push, Registrar evento personalizado y Registrar atributo personalizado) que pueden utilizarse en mensajes dentro de la aplicación y en Content Cards.<br><br>Para todas las demás acciones, o para combinar varias acciones, utiliza esta guía para construir tu propio enlace profundo de acción de Braze.

## Soporte del SDK or kit de desarrollo de software {#sdk-support}

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

El esquema de enlace profundo `brazeActions://` se puede utilizar en cualquier lugar donde exista una opción de enlace profundo o redirección dentro de los mensajes dentro de la aplicación y Content Cards.

Para los mensajes dentro de la aplicación en HTML, utiliza el [`Javascript Bridge`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge) en su lugar, ya que los enlaces profundos no son compatibles con los tipos de mensajes HTML.

## Esquema {#schema}

Puedes incluir múltiples `steps` de acción dentro de un tipo de acción `container`. Un solo paso sin un `container` también es válido.

```json
{
    "type": "container",
    "steps": []
}
```

Un `step` individual contiene un `type` de acción y un array `args` opcional:

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI

El esquema URI de las acciones de Braze es `brazeActions://v1/{base64encodedJsonString}`.

El siguiente JavaScript muestra cómo codificar y decodificar la cadena JSON:

```javascript
function decode(encoded) {
    const binary = window.atob(encoded.replace(/-/g, '+').replace(/_/g, '/'));
    let bits8 = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
      bits8[i] = binary.charCodeAt(i);
    }
    const bits16 = new Uint16Array(bits8.buffer);
    return String.fromCharCode(...bits16);
}

/**
 * Returns a url-safe base64 encoded string of the input.
 * Unicode inputs are accepted.
 * Converts a UTF-16 string to UTF-8 to comply with base64 encoding limitations.
 */
function encode(input) {
    // Split the original 16-bit char code into two 8-bit char codes then
    // reconstitute a new string (of double length) using those 8-bit codes
    // into a UTF-8 string.
    const codeUnits = new Uint16Array(input.length);
    for (let i = 0; i < codeUnits.length; i++) {
        codeUnits[i] = input.charCodeAt(i);
    }
    const charCodes = new Uint8Array(codeUnits.buffer);
    let utf8String = "";
    for (let i = 0; i < charCodes.byteLength; i++) {
        utf8String += String.fromCharCode(charCodes[i]);
    }
    return btoa(utf8String).replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "");
}
```

## Acciones compatibles {#supported-actions}

|Tipo|Argumentos|
|--|--|
|`container`|Un array de otras acciones a realizar|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (opcional)|
|`setEmailNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`| N/A |
|`openLink`|1. `url`<br>2. `openInNewTab` (booleano)|
|`openLinkInWebview`| `url`|
|`addToSubscriptionGroup`| `subscriptionGroupId`|
|`removeFromSubscriptionGroup`| `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acciones compatibles" }

## Codificador JSON {#json-encoder}

Introduce una cadena JSON para ver la URI `brazeActions://` resultante. O bien, introduce una URI `brazeActions://` para decodificar su JSON.

<div><h4>Entrada JSON</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>Salida de enlace profundo</h4></div>
<textarea id="braze-actions-output" rows="6"></textarea>
<style>
    #braze-actions-input, #braze-actions-output {
        width: 90%;
        border: solid 1px #1f1f1f !important;
        margin-top: 10px;
        border-radius: 4px;
        font-family: courier;
        font-size: 14px;
        padding: 4px;
    }
</style>
<script>
(function(){
    const input = document.getElementById('braze-actions-input');
    const output = document.getElementById('braze-actions-output');
    var debouncer;
    input.oninput = function(event){
        clearTimeout(debouncer);
        debouncer = setTimeout(function(){
            try {
                const jsonString = event.target.value.replace(/^\s+|\s+$/g, '');
                output.value = `brazeActions://v1/${encode(jsonString)}`
            } catch(e){
                output.value = `Invalid JSON`;
            }
        }, 100);
    }
    output.oninput = function(event){
        clearTimeout(debouncer);
        debouncer = setTimeout(function(){
            try {
                const base64 = event.target.value.replace(/^brazeActions:\/\/v\d+\//, '').replace(/\s/g, '');
                const json = JSON.parse(decode(base64));
                input.value = JSON.stringify(json, null, 4);
            } catch(e){
                input.value = `Invalid brazeActions:// link`;
            }
        }, 100);
    }

    input.value = JSON.stringify({
        "type": "container",
        "steps": [{
            "type": "addToSubscriptionGroup",
            "args": ["your-subscription-group-ID-here"]
        }]
    }, null, 2);
    input.dispatchEvent(new Event("input"));

    function decode(encoded) {
        const binary = window.atob(encoded.replace(/-/g, '+').replace(/_/g, '/'));
        let bits8 = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i++) {
        bits8[i] = binary.charCodeAt(i);
        }
        const bits16 = new Uint16Array(bits8.buffer);
        return String.fromCharCode(...bits16);
    }


    function encode(input) {
        const codeUnits = new Uint16Array(input.length);
        for (let i = 0; i < codeUnits.length; i++) {
            codeUnits[i] = input.charCodeAt(i);
        }
        const charCodes = new Uint8Array(codeUnits.buffer);
        let utf8String = "";
        for (let i = 0; i < charCodes.byteLength; i++) {
            utf8String += String.fromCharCode(charCodes[i]);
        }
        return btoa(utf8String).replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "");
    }
})();
</script>