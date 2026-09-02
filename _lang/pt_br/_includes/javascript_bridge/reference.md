Mensagens no app em HTML personalizado e Banners suportam uma "ponte" JavaScript para interagir com o SDK or kit de desenvolvimento de software da Braze, permitindo que você dispare ações personalizadas da Braze quando os usuários clicam em elementos com links ou interagem com seu conteúdo de outra forma. Esses métodos existem com a variável global `brazeBridge` ou `appboyBridge`.

{% alert important %}
A Braze recomenda que você use a variável global `brazeBridge`. A variável global `appboyBridge` está obsoleta, mas continuará a funcionar para os usuários existentes. Se estiver usando `appboyBridge`, sugerimos que migre para `brazeBridge`. <br><br> `appboyBridge` foi descontinuado nas seguintes versões do SDK or kit de desenvolvimento de software:<br><br>
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Por exemplo, para registrar um atributo personalizado e um evento personalizado, e então fechar a mensagem, você poderia usar o seguinte JavaScript dentro do seu HTML personalizado:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### Métodos da ponte JavaScript {#bridge}

Os seguintes métodos JavaScript são suportados dentro do HTML personalizado para mensagens no app e Banners:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% multi_lang_include archive/appboyBridge.md %}

### Rastreamento de cliques em botões {#button-click-tracking}

Use o método `brazeBridge.logClick(button_id)` para rastrear cliques no seu HTML personalizado.

Para mensagens no app, você pode rastrear programaticamente "Button 1", "Button 2" e "Body Clicks" usando `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` ou `brazeBridge.logClick()`, respectivamente.

| Cliques | Método | Com suporte |
| ---------- | ---------------------------- | --------- |
| Clique no corpo | `brazeBridge.logClick()` | Mensagens no app e Banners |
| Button 1 | `brazeBridge.logClick('0')` | Apenas mensagens no app |
| Button 2 | `brazeBridge.logClick('1')` | Apenas mensagens no app |
| Rastreamento de botões personalizados | `brazeBridge.logClick('your custom name here')` | Mensagens no app e Banners |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rastreamento de cliques em botões" }

Para mensagens no app, você pode rastrear múltiplos eventos de cliques em botões por impressão. Por exemplo, para fechar uma mensagem e registrar um clique no Button 2:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

Você também pode rastrear novos nomes de botões personalizados — até 100 nomes exclusivos por campanha. Por exemplo, `brazeBridge.logClick('blue button')` ou `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Ao usar métodos JavaScript dentro de um atributo `onclick`, envolva valores de string em aspas simples para evitar conflitos com o atributo HTML entre aspas duplas.
{% endalert %}

#### Limitações (apenas mensagens no app) {#limitations-in-app-messages-only}

- Você pode ter até 100 IDs de botão exclusivos por campanha.
- Os IDs de botão podem ter até 255 caracteres cada.
- Os IDs de botão só podem incluir letras, números, espaços, traços e sublinhados.