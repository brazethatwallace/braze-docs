---
nav_title: Deep links de ações da Braze
article_title: Deep links de ações da Braze
page_order: 100
description: "Este artigo de referência aborda como usar os deep links de ações da Braze para executar ações do SDK or kit de desenvolvimento de software nos botões do canal de envio de mensagens."
hidden: true
---

# Deep links de ações da Braze {#braze-actions-deeplinks}

> As ações da Braze permitem que você use "deep links" para executar a funcionalidade nativa do SDK or kit de desenvolvimento de software.<br><br>O dashboard da Braze inclui várias ações padrão ao clicar (Solicitar permissão para push, Registrar evento personalizado e Registrar atributo personalizado) que podem ser usadas em mensagens no app e Content Cards.<br><br>Para todas as outras ações, ou para combinar várias ações, use este guia para construir seu próprio deep link de Braze Action.

## Suporte do SDK or kit de desenvolvimento de software {#sdk-support}

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

O esquema de deeplink `brazeActions://` pode ser usado em qualquer lugar onde exista uma opção de deeplink ou redirecionamento dentro de In-App Messages e Content Cards.

Para In-App Messages em HTML, use o [`Javascript Bridge`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), pois deeplinks não são compatíveis com tipos de mensagem HTML.

## Schema {#schema}

Você pode incluir várias `steps` de ação dentro de um tipo de ação `container`. Uma única etapa sem um `container` também é válida.

```json
{
    "type": "container",
    "steps": []
}
```

Uma `step` individual contém um `type` de ação e um array `args` opcional:

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI

O esquema de URI das Braze Actions é `brazeActions://v1/{base64encodedJsonString}`.

O JavaScript a seguir mostra como codificar e decodificar a string JSON:

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

## Ações suportadas {#supported-actions}

|Tipo|Argumentos|
|--|--|
|`container`|Um array de outras ações a serem executadas|
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ações suportadas" }

## Codificador JSON {#json-encoder}

Insira uma string JSON para ver o URI `brazeActions://` resultante. Ou insira um URI `brazeActions://` para decodificar seu JSON.

<div><h4>Entrada JSON</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>Saída de Deeplink</h4></div>
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