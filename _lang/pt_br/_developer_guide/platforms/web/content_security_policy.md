---
nav_title: Cabeçalhos de política de segurança de conteúdo
article_title: Cabeçalhos de política de segurança de conteúdo para a Web
platform: Web
page_order: 21
page_type: reference
description: "Este artigo aborda os cabeçalhos de política de segurança de conteúdo necessários com o Braze Web SDK."

---

# Cabeçalhos de política de segurança de conteúdo {#content-security-policy-headers}

> A Content-Security-Policy oferece segurança adicional ao restringir como e onde o conteúdo pode ser carregado em seu site. Este artigo de referência aborda quais cabeçalhos de política de segurança de conteúdo são necessários com o Web SDK.

{% alert important %}
Este artigo é destinado a desenvolvedores que trabalham em sites que aplicam regras de CSP e se integram à Braze. Não se trata de um conselho sobre como você deve abordar a segurança.
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Atributos de nonce {#nonce}

Se você usar um valor `nonce` nas diretivas `script-src` ou `style-src`, passe esse valor para a opção de inicialização `contentSecurityNonce` para propagá-lo para scripts e estilos recém-criados gerados pelo SDK:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## Diretivas {#directives}

### `connect-src` {#connect-src}

{% alert warning %}
Sua URL deve corresponder ao [endpoint de SDK da API]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) da sua opção de inicialização `baseUrl` escolhida.
{% endalert %}

| URL | Informações |
|---|-----------|
| `connect-src https://sdk.iad-01.braze.com` | Permite que o SDK se comunique com as APIs da Braze. Altere essa URL para corresponder ao [endpoint de SDK da API]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) da sua opção de inicialização `baseUrl` escolhida. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="connect-src #connect-src" }

### `script-src` {#script-src}

| URL | Informações |
|---|-----------|
| `script-src https://js.appboycdn.com` | Obrigatória ao usar a integração hospedada por CDN. |
| `script-src 'unsafe-eval'` | Obrigatória ao usar o snippet de integração que contém referência a `appboyQueue`. Para evitar o uso dessa diretiva, [integre o SDK usando o NPM]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup?tab=package%20manager). |
| `script-src 'nonce-...'`<br>ou<br>`script-src 'unsafe-inline'` | Obrigatória para determinadas mensagens no app, como HTML personalizado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="script-src #script-src" }

### `img-src` {#img-src}

| URL | Informações |
|---|-----------|
| `img-src: appboy-images.com braze-images.com cdn.braze.eu` | Obrigatória ao usar imagens hospedadas pelo CDN da Braze. Os nomes de host podem variar de acordo com o cluster do dashboard.<br><br>**Importante:** Se você estiver usando fontes personalizadas, também será necessário incluir `font-src`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="img-src #img-src" }

## Font Awesome {#font-awesome}

Para desativar a inclusão automática do Font Awesome, use a opção de inicialização `doNotLoadFontAwesome`:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Se você optar por usar o Font Awesome, as seguintes diretivas de CSP serão obrigatórias:

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` ou `style-src 'unsafe-inline'`