---
page_order: 1.1
nav_title: Guia de deep linking para iOS
article_title: Guia de deep linking para iOS
description: "Saiba qual tipo de deep link usar para seu app iOS, quando você precisa de um arquivo AASA e quais métodos de delegado de app implementar."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Guia de deep linking para iOS {#ios-deep-linking-guide}

> Este guia ajuda você a escolher a estratégia de deep linking certa para seu app iOS, dependendo do canal de envio de mensagens que você está usando e se você usa um provedor de links de terceiros, como o Branch.

Para detalhes de implementação, consulte [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift). Para solução de problemas, consulte [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/).

## Escolhendo um tipo de link {#choosing-a-link-type}

Existem três maneiras de lidar com links de mensagens da Braze em seu app iOS. Cada uma funciona de maneira diferente e é adequada para diferentes canais e casos de uso.

| Tipo de link | Exemplo | Ideal para | Abre sem o app instalado? |
|---|---|---|---|
| **Esquema personalizado** | `myapp://products/123` | Push, mensagens no app, Content Cards | Não — o link falha |
| **Link universal** | `https://myapp.com/products/123` | E-mail, SMS, canais com rastreamento de cliques | Sim — volta para a web |
| **Abrir URL da web dentro do app** | Qualquer URL `https://` | Exibir conteúdo da web em um WebView modal | N/A — exibe no WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Choosing a link type" }

### Deep links com esquema personalizado {#custom-scheme-deep-links}

Deep links com esquema personalizado (por exemplo, `myapp://products/123`) abrem seu app diretamente em uma tela específica. São a opção mais simples para canais em que os links não são modificados por terceiros.

**Use deep links com esquema personalizado quando:**
- Enviar notificações por push, mensagens no app ou Content Cards
- Você não precisa que o link funcione se o app não estiver instalado
- Você não precisa de rastreamento de cliques (encapsulamento de link por ESP de e-mail)

**Não use deep links com esquema personalizado quando:**
- Enviar e-mails — os ESPs encapsulam links para rastreamento de cliques, o que quebra esquemas personalizados
- Você precisa que o link volte para uma página da web se o app não estiver instalado

### Links universais {#universal-links}

Links universais (por exemplo, `https://myapp.com/products/123`) são URLs HTTPS padrão que o iOS pode encaminhar para o seu app em vez de abrir em um navegador. Eles exigem configuração no lado do servidor (um arquivo AASA) e configuração no lado do app (direito de Associated Domains).

**Use links universais quando:**
- Enviar e-mails. Seu ESP encapsula links para rastreamento de cliques, então os links devem ser HTTPS.
- Enviar SMS ou outros canais em que os links são encapsulados ou encurtados.
- Você precisa que o link volte para uma página da web quando o app não estiver instalado.
- Você está usando um provedor de links de terceiros, como Branch ou AppsFlyer.

**Não use links universais quando:**
- Você só precisa de deep links de push, mensagens no app ou Content Cards. Os esquemas personalizados são mais simples.

### "Abrir URL da web dentro do app" {#open-web-url-inside-app}

Esta opção abre uma página da web dentro de um WebView modal no seu app. É totalmente gerenciada pelo SDK da Braze usando `Braze.WebViewController` — você não precisa escrever nenhum código de tratamento de URL.

**Use "Abrir URL da web dentro do app" quando:**
- Você deseja exibir uma página da web (como uma promoção ou artigo) sem sair do seu app.
- A URL é uma página web HTTPS padrão, não um deep link para uma tela específica do app.

**Não use "Abrir URL da web dentro do app" quando:**
- Você precisa navegar para uma visualização específica no seu app. Em vez disso, use um esquema personalizado ou um link universal.
- A página da web requer autenticação ou possui cabeçalhos de Content Security Policy que bloqueiam a incorporação.

## O que você precisa para cada tipo de link {#what-you-need-for-each-link-type}

### Deep links com esquema personalizado

| Requisito | Informações |
|---|---|
| Arquivo AASA | Não é necessário |
| `Info.plist` | Registre seu esquema em `CFBundleURLTypes` e adicione-o a `LSApplicationQueriesSchemes` |
| Método delegado do app | Implemente `application(_:open:options:)` para analisar a URL e navegar |
| Configuração do SDK da Braze | Nenhuma — o SDK abre URLs de esquema personalizado por padrão |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom scheme deep links" }

### Links universais

| Requisito | Informações |
|---|---|
| Arquivo AASA | Obrigatório — hospede em `https://yourdomain.com/.well-known/apple-app-site-association` |
| Associated Domains | Adicione `applinks:yourdomain.com` no Xcode em **Signing & Capabilities** |
| Método delegado do app | Implemente `application(_:continue:restorationHandler:)` para lidar com `NSUserActivity` |
| Configuração do SDK da Braze | Defina `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (opcional) | Implemente `braze(_:shouldOpenURL:)` para roteamento personalizado (por exemplo, Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Universal links" }

{% alert important %}
Se você enviar e-mails pela Braze, seu ESP (SendGrid, SparkPost ou Amazon SES) encapsulará os links em um domínio de rastreamento de cliques. Você também deve hospedar o arquivo AASA no seu domínio de rastreamento de cliques, não apenas no seu domínio principal. Para a configuração completa, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/).
{% endalert %}

### "Abrir URL da web dentro do app"

| Requisito | Informações |
|---|---|
| Arquivo AASA | Não é necessário |
| Método delegado do app | Não é necessário — o SDK lida com isso automaticamente |
| Configuração do SDK da Braze | Nenhuma — selecione **Open Web URL Inside App** no criador de Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label=""Open Web URL Inside App"" }

## Quando você precisa de um arquivo AASA {#when-aasa}

Um arquivo Apple App Site Association (AASA) só é necessário quando você usa **links universais**. Ele informa ao iOS quais URLs seu app pode processar.

Você precisa de um arquivo AASA quando:

- Você envia deep links em campanhas de e-mail (porque os ESPs encapsulam os links em URLs de rastreamento de cliques HTTPS).
- Você envia deep links em campanhas de SMS (porque os links podem ser encurtados para URLs HTTPS).
- Você usa Branch, AppsFlyer ou outro provedor de links (porque eles usam seus próprios domínios HTTPS).
- Você usa links universais de push, mensagens no app ou Content Cards (menos comum, mas possível com `forwardUniversalLinks = true`).

Você não precisa de um arquivo AASA quando:

- Você só usa deep links com esquema personalizado (por exemplo, `myapp://`) de push, mensagens no app ou Content Cards.
- Você usa a opção **Open Web URL Inside App**.

Para instruções de configuração do AASA, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links).

## Quando você precisa de código no app para lidar com links {#when-app-code}

O método delegado que você implementa depende do tipo de link que está usando:

| Método delegado | Processa | Quando implementar |
|---|---|---|
| `application(_:open:options:)` | Deep links com esquema personalizado (`myapp://`) | Você usa deep links com esquema personalizado de qualquer canal |
| `application(_:continue:restorationHandler:)` | Links universais (`https://`) | Você usa links universais de e-mail, SMS ou com `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Todas as URLs abertas pelo SDK | Você precisa de lógica de roteamento personalizada (por exemplo, Branch, tratamento condicional, análise de dados) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="When you need app code to handle links #when-app-code" }

{% alert tip %}
Se você usar um provedor de links de terceiros, como o Branch, implemente `BrazeDelegate.braze(_:shouldOpenURL:)` para interceptar URLs e encaminhá-las para o SDK do provedor. Consulte [Branch para deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) para um exemplo completo.
{% endalert %}

## Usando o Branch com a Braze {#branch}

Se você usar o [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) como seu provedor de links, sua configuração exigirá algumas etapas adicionais além da configuração padrão de link universal:

1. **SDK do Branch**: Integre o SDK do Branch seguindo a [documentação do Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Associated Domains**: Adicione seu domínio do Branch (por exemplo, `applinks:yourapp.app.link`) no Xcode em **Signing & Capabilities**.
3. **BrazeDelegate**: Implemente `braze(_:shouldOpenURL:)` para encaminhar os links do Branch para o SDK do Branch, em vez de permitir que a Braze os processe diretamente.
4. **Encaminhar links universais**: Defina `configuration.forwardUniversalLinks = true` na configuração do SDK da Braze.

Para detalhes de implementação e orientações sobre depuração, consulte [Branch para deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).