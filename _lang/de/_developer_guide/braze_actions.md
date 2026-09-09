---
nav_title: Braze-Aktionen-Deeplinks
article_title: Braze-Aktionen-Deeplinks
page_order: 100
description: "Dieser Referenzartikel beschreibt, wie Sie Braze-Aktionen-Deeplinks verwenden, um SDK-Aktionen über Buttons in Messaging-Kanälen auszuführen."
hidden: true
---

# Braze-Aktionen-Deeplinks {#braze-actions-deeplinks}

> Mit Braze-Aktionen können Sie „Deeplinks“ verwenden, um native SDK-Funktionen auszuführen.<br><br>Das Braze-Dashboard enthält mehrere standardmäßige On-Click-Aktionen (Push-Berechtigung anfordern, angepasstes Event protokollieren und angepasstes Attribut protokollieren), die in In-App-Nachrichten und Content Cards verwendet werden können.<br><br>Für alle anderen Aktionen oder um mehrere Aktionen zu kombinieren, verwenden Sie diese Anleitung, um Ihren eigenen Braze-Aktionen-Deeplink zu erstellen.

## SDK-Unterstützung {#sdk-support}

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Das Deeplink-Schema `brazeActions://` kann überall dort verwendet werden, wo eine Deeplink- oder Weiterleitungsoption in In-App Messages und Content Cards vorhanden ist.

Verwenden Sie für HTML-In-App-Nachrichten stattdessen die [`Javascript Bridge`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), da Deeplinks in HTML-Nachrichtentypen nicht unterstützt werden.

## Schema {#schema}

Sie können mehrere Aktions-`steps` innerhalb eines `container`-Aktionstyps angeben. Ein einzelner Schritt ohne einen `container` ist ebenfalls gültig.

```json
{
    "type": "container",
    "steps": []
}
```

Ein einzelner `step` enthält einen Aktions-`type` und ein optionales `args`-Array:

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI

Das URI-Schema für Braze-Aktionen lautet `brazeActions://v1/{base64encodedJsonString}`.

Das folgende JavaScript zeigt, wie Sie den JSON-String kodieren und dekodieren:

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

## Unterstützte Aktionen {#supported-actions}

|Typ|Argumente|
|--|--|
|`container`|Ein Array anderer auszuführender Aktionen|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (optional)|
|`setEmailNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`| N/A |
|`openLink`|1. `url`<br>2. `openInNewTab` (boolean)|
|`openLinkInWebview`| `url`|
|`addToSubscriptionGroup`| `subscriptionGroupId`|
|`removeFromSubscriptionGroup`| `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Aktionen" }

## JSON-Encoder {#json-encoder}

Geben Sie einen JSON-String ein, um die resultierende `brazeActions://`-URI zu sehen. Oder geben Sie eine `brazeActions://`-URI ein, um deren JSON zu dekodieren.

<div><h4>JSON-Eingabe</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>Deeplink-Ausgabe</h4></div>
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