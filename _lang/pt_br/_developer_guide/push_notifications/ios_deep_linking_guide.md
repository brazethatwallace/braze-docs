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

Para detalhes de implementação, consulte [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Para solução de problemas, consulte [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Escolhendo um tipo de link {#choosing-a-link-type}

Existem três formas de lidar com links de mensagens da Braze no seu app iOS. Cada uma funciona de maneira diferente e é adequada para canais e casos de uso distintos.

| Tipo de link | Exemplo | Melhor para | Abre sem o app instalado? |
|---|---|---|---|
| **Esquema personalizado** | `myapp://products/123` | Push, mensagens no app, Content Cards | Não — o link falha |
| **Link universal** | `https://myapp.com/products/123` | E-mail, SMS, canais com rastreamento de cliques | Sim — abre a versão web como fallback |
| **Abrir URL da web dentro do app** | Qualquer URL `https://` | Exibir conteúdo web em uma WebView modal | N/A — exibe na WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Escolhendo um tipo de link" }

### Deep links com esquema personalizado {#custom-scheme-deep-links}

Deep links com esquema personalizado (por exemplo, `myapp://products/123`) abrem seu app diretamente em uma tela específica. Eles são a opção mais simples para canais onde os links não são modificados por terceiros.

**Use deep links com esquema personalizado quando:**
- Enviar notificações por push, mensagens no app ou Content Cards
- Você não precisa que o link funcione se o app não estiver instalado
- Você não precisa de rastreamento de cliques (encapsulamento de links pelo provedor de serviços de e-mail)

**Não use deep links com esquema personalizado quando:**
- Enviar e-mails — os provedores de serviços de e-mail encapsulam links para rastreamento de cliques, o que quebra esquemas personalizados
- Você precisa que o link abra uma página web como fallback se o app não estiver instalado

### Links universais {#universal-links}

Links universais (por exemplo, `https://myapp.com/products/123`) são URLs HTTPS padrão que o iOS pode direcionar para seu app em vez de abrir no navegador. Eles exigem configuração do lado do servidor (um arquivo AASA) e configuração do lado do app (entitlement de Associated Domains).

**Use links universais quando:**
- Enviar e-mails. Seu provedor de serviços de e-mail encapsula links para rastreamento de cliques, então os links precisam ser HTTPS.
- Enviar SMS ou outros canais onde os links são encapsulados ou encurtados.
- Você precisa que o link abra uma página web como fallback quando o app não estiver instalado.
- Você está usando um provedor de links de terceiros como Branch ou Appsflyer.

**Não use links universais quando:**
- Você precisa apenas de deep links a partir de push, mensagens no app ou Content Cards. Esquemas personalizados são mais simples.

### "Abrir URL da web dentro do app" {#open-web-url-inside-app}

Essa opção abre uma página web dentro de uma WebView modal no seu app. Ela é gerenciada inteiramente pelo SDK da Braze usando `Braze.WebViewController` — você não precisa escrever nenhum código de tratamento de URL.

**Use "Abrir URL da web dentro do app" quando:**
- Você quer exibir uma página web (como uma promoção ou artigo) sem sair do seu app.
- A URL é uma página web HTTPS padrão, não um deep link para uma tela específica do app.

**Não use "Abrir URL da web dentro do app" quando:**
- Você precisa navegar para uma view específica no seu app. Em vez disso, use um esquema personalizado ou link universal.
- A página web exige autenticação ou tem cabeçalhos de Content Security Policy que bloqueiam a incorporação.

## O que é necessário para cada tipo de link {#what-you-need-for-each-link-type}

### Deep links de esquema personalizado

| Requisito | Detalhes |
|---|---|
| Arquivo AASA | Não é necessário |
| `Info.plist` | Registre seu esquema em `CFBundleURLTypes` e adicione-o a `LSApplicationQueriesSchemes` |
| Método app delegate | Implemente `application(_:open:options:)` para analisar a URL e navegar |
| Configuração do SDK da Braze | Nenhuma — o SDK abre URLs de esquema personalizado por padrão |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deep links de esquema personalizado" }

### Links universais

| Requisito | Detalhes |
|---|---|
| Arquivo AASA | Necessário — hospede em `https://yourdomain.com/.well-known/apple-app-site-association` |
| Associated Domains | Adicione `applinks:yourdomain.com` no Xcode em **Signing & Capabilities** |
| Método app delegate | Implemente `application(_:continue:restorationHandler:)` para manipular `NSUserActivity` |
| Configuração do SDK da Braze | Defina `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (opcional) | Implemente `braze(_:shouldOpenURL:)` para roteamento personalizado (por exemplo, Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Links universais" }

{% alert important %}
Se você envia e-mails pela Braze, seu provedor de serviços de e-mail (SendGrid, SparkPost ou Amazon SES) encapsula os links em um domínio de rastreamento de cliques. Você deve hospedar o arquivo AASA também no seu domínio de rastreamento de cliques, e não apenas no seu domínio principal. Para a configuração completa, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links). Se todos os links de e-mail abrem o app, consulte [Todos os links de e-mail abrem o app]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting#every-email-link-opens-the-app).
{% endalert %}

### "Open Web URL Inside App"

| Requisito | Detalhes |
|---|---|
| Arquivo AASA | Não é necessário |
| Método app delegate | Não é necessário — o SDK gerencia isso automaticamente |
| Configuração do SDK da Braze | Nenhuma — selecione **Open Web URL Inside App** no criador de Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Open Web URL Inside App" }

## Quando você precisa de um arquivo AASA {#when-aasa}

Um arquivo Apple App Site Association (AASA) só é necessário quando você usa **links universais**. Ele informa ao iOS quais URLs seu app pode processar.

Você precisa de um arquivo AASA quando:

- Você envia deep links em campanhas de e-mail (porque os provedores de serviços de e-mail encapsulam os links em URLs de rastreamento de cliques HTTPS).
- Você envia deep links em campanhas de SMS (porque os links podem ser encurtados para URLs HTTPS).
- Você usa Branch, AppsFlyer ou outro provedor de links (porque eles usam seus próprios domínios HTTPS).
- Você usa links universais de push, mensagens no app ou Content Cards (menos comum, mas possível com `forwardUniversalLinks = true`).

Você não precisa de um arquivo AASA quando:

- Você só usa deep links com esquema personalizado (por exemplo, `myapp://`) de push, mensagens no app ou Content Cards.
- Você usa a opção **Open Web URL Inside App**.

Para instruções de configuração do AASA, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Quando você precisa de código no app para lidar com links {#when-app-code}

O método delegado que você implementa depende do tipo de link que está usando:

| Método delegado | Processa | Quando implementar |
|---|---|---|
| `application(_:open:options:)` | Deep links com esquema personalizado (`myapp://`) | Você usa deep links com esquema personalizado de qualquer canal |
| `application(_:continue:restorationHandler:)` | Links universais (`https://`) | Você usa links universais de e-mail, SMS ou com `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Todas as URLs abertas pelo SDK | Você precisa de lógica de roteamento personalizada (por exemplo, Branch, tratamento condicional, análise de dados) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Quando você precisa de código no app para lidar com links" }

{% alert tip %}
Se você usar um provedor de links de terceiros, como o Branch, implemente `BrazeDelegate.braze(_:shouldOpenURL:)` para interceptar URLs e encaminhá-las para o SDK do provedor. Consulte [Branch para deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) para um exemplo completo.
{% endalert %}

## Usando o Branch com a Braze {#branch}

Se você usar o [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) como seu provedor de links, sua configuração exigirá algumas etapas adicionais além da configuração padrão de link universal:

1. **SDK do Branch**: Integre o SDK do Branch seguindo a [documentação do Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Associated Domains**: Adicione seu domínio do Branch (por exemplo, `applinks:yourapp.app.link`) no Xcode em **Signing & Capabilities**.
3. **BrazeDelegate**: Implemente `braze(_:shouldOpenURL:)` para encaminhar os links do Branch para o SDK do Branch, em vez de permitir que a Braze os processe diretamente.
4. **Encaminhar links universais**: Defina `configuration.forwardUniversalLinks = true` na configuração do SDK da Braze.

Para detalhes de implementação e orientações sobre depuração, consulte [Branch para deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking).