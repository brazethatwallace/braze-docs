---
nav_title: Extensões de navegador
article_title: Integração de extensões de navegador para a Web
platform: Web
page_order: 20
page_type: reference
description: "Este artigo descreve como usar o Braze Web SDK or kit de desenvolvimento de software em suas extensões de navegador (Google Chrome, Firefox)."

---

# Extensão do navegador {#browser-extension}

> Este artigo descreve como usar o Braze Web SDK or kit de desenvolvimento de software em suas extensões de navegador (Google Chrome, Firefox).

Integre o Braze Web SDK or kit de desenvolvimento de software em sua extensão de navegador para coletar dados analíticos e exibir mensagens personalizadas para os usuários. Isso inclui tanto **extensões do Google Chrome** quanto **complementos do Firefox**.

## O que é suportado {#whats-supported}

Em geral, como as extensões são HTML e JavaScript, você pode usar a Braze para o seguinte:

* **Analytics**: Capture eventos personalizados, atributos e até mesmo identifique usuários recorrentes em sua extensão. Use essas características de perfil para potencializar o envio de mensagens entre canais.
* **In-App Messages**: Dispare mensagens no app quando os usuários realizarem uma ação em sua extensão, usando nosso envio de mensagens HTML nativo ou personalizado.
* **Content Cards**: Adicione um feed de cartões nativos à sua extensão para integração ou conteúdo promocional.
* **Web push**: Envie notificações oportunas mesmo quando sua página da web não estiver aberta no momento.

## O que não é suportado {#whats-not-supported}

* O uso do Braze SDK or kit de desenvolvimento de software a partir de um service worker não é suportado. Você ainda pode usar o Braze SDK or kit de desenvolvimento de software na página de popup ou na página de configurações da sua extensão. {% multi_lang_include product_feedback_cta.md context="gap" feature="service worker support in the Braze Web SDK or kit de desenvolvimento de software" %}

## Tipos de extensão {#extension-types}

A Braze pode ser incluída nas seguintes áreas de sua extensão:

| Área | Detalhes | O que é suportado |
|--------|-------|------|
| Página pop-up | A página [Popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) é uma caixa de diálogo que pode ser mostrada aos usuários quando eles clicam no ícone da sua extensão na barra de ferramentas do navegador. | Análise de dados, mensagens no app e Content Cards |
| Scripts em segundo plano | [Scripts em segundo plano](https://developer.chrome.com/extensions/background_pages) (somente Manifest v2) permitem que sua extensão inspecione e interaja com a navegação do usuário ou modifique páginas da web (por exemplo, como os bloqueadores de anúncios detectam e alteram o conteúdo das páginas). | Análise de dados, mensagens no app e Content Cards.<br><br>Os scripts em segundo plano não são visíveis para os usuários, portanto, para o envio de mensagens, seria necessário comunicar-se com as guias do navegador ou com a página pop-up ao exibir mensagens. |
| Páginas de opções | A [página de opções](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) permite que os usuários alternem as configurações na extensão. É uma página HTML autônoma que abre uma nova guia. | Análise de dados, mensagens no app e Content Cards |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 aria-label="Tipos de extensão" }

## Permissões {#permissions}

Não são necessárias permissões adicionais no seu `manifest.json` ao integrar o SDK or kit de desenvolvimento de software da Braze (`braze.min.js`) como um arquivo local empacotado com sua extensão.

No entanto, se você usar o [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), ou fizer referência ao SDK or kit de desenvolvimento de software da Braze a partir de uma URL externa, ou tiver definido uma política de segurança de conteúdo rigorosa para sua extensão, será necessário ajustar a configuração [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) no `manifest.json` para permitir fontes de script remotas.

## Primeiros passos {#getting-started}

{% alert tip %}
Antes de começar, leia o [guia de configuração inicial do Web SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) para saber mais sobre a integração de JavaScript em geral.  <br><br>Pode ser interessante marcar a [referência do JavaScript SDK or kit de desenvolvimento de software](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) para obter detalhes completos sobre todos os diferentes métodos e opções de configuração do SDK or kit de desenvolvimento de software.
{% endalert %}

Para integrar o Braze Web SDK or kit de desenvolvimento de software, você primeiro precisará baixar uma cópia da biblioteca JavaScript mais recente. Isso pode ser feito usando NPM ou baixando diretamente do [Braze CDN](https://js.appboycdn.com/web-sdk/latest/braze.min.js).

Como alternativa, se você preferir usar o [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) ou usar uma cópia hospedada externamente do Braze SDK or kit de desenvolvimento de software, lembre-se de que o carregamento de recursos externos exigirá que você ajuste a configuração [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) no seu `manifest.json`.

Depois de baixar, copie o arquivo `braze.min.js` em algum lugar do diretório da sua extensão.

### Popups de extensão {#popup}

Para adicionar a Braze a um popup de extensão, faça referência ao arquivo JavaScript local no seu `popup.html`, como faria em um site normal. Se estiver usando o Google Tag Manager, você pode adicionar a Braze usando nossos [modelos do Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/).

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Script em segundo plano (somente Manifest v2) {#background-script}

Para usar a Braze no script em segundo plano da sua extensão, adicione a biblioteca Braze ao `manifest.json` no array `background.scripts`. Isso tornará a variável global `braze` disponível no contexto do seu script em segundo plano.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ]
    }
}
```

### Página de opções {#options-page}

Se você usar uma página de opções (por meio das propriedades do manifesto `options` ou `options_ui`), poderá incluir a Braze da mesma forma que faria nas [instruções do `popup.html`](#popup).

## Inicialização {#initialization}

Depois que o SDK or kit de desenvolvimento de software for incluído, você poderá inicializar a biblioteca como de costume.

Como não há suporte para cookies em extensões de navegador, você pode desativar os cookies inicializando com `noCookies: true`.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

Para saber mais sobre as opções de inicialização suportadas, visite a [referência do Web SDK or kit de desenvolvimento de software](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

## Push {#push}

As caixas de diálogo popup de extensão não permitem solicitações de push (elas não têm a barra de URL na navegação). Portanto, para registrar e solicitar permissão de push na caixa de diálogo popup de uma extensão, será necessário usar uma solução alternativa de domínio, conforme descrito em [Domínio push alternativo]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).