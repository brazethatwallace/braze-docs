---
nav_title: Solução de problemas de deep linking
article_title: Solução de problemas de deep linking
description: "Diagnostique problemas de deep linking no iOS usando um índice de sintomas, um caminho de investigação padrão e verificações específicas da plataforma."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Solução de problemas de deep linking {#troubleshoot-deep-linking}

> Use esta página para diagnosticar problemas comuns de deep linking no iOS. Para ajuda na escolha do tipo de link certo, consulte o [guia de deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Para detalhes de implementação, consulte [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift).

## Comece aqui: Identifique seu sintoma {#start-here-match-your-symptom}

Encontre o comportamento que você está observando na tabela e siga as etapas da seção correspondente. Se não tiver certeza de qual seção se aplica, use o [caminho de investigação padrão](#standard-investigation-path).

| Sintoma | Acessar |
| --- | --- |
| Link de esquema personalizado abre o app, mas na tela errada | [Deep link de esquema personalizado não abre a visualização correta](#custom-scheme-deep-link-does-not-open-the-correct-view) |
| Link universal abre o Safari em vez do app | [Link universal abre no Safari em vez do app](#universal-link-opens-in-safari-instead-of-the-app) |
| Link do e-mail não abre o app | [Deep link do e-mail não abre o app](#deep-link-from-email-does-not-open-the-app) |
| Funciona via push, mas não via mensagem no app (ou o contrário) | [Deep link funciona via push, mas não via mensagem no app](#deep-link-works-from-push-but-not-from-in-app-message) |
| "Open Web URL Inside App" mostra WebView em branco | ["Open Web URL Inside App" mostra uma página em branco ou com erro](#open-web-url-inside-app-shows-a-blank-or-broken-page) |
| Link da Branch não abre o app ou não direciona corretamente | [Solução de problemas da Branch com a Braze](#branch) |
| Deep link falha sem causa aparente | [Dicas gerais de depuração](#general-debugging-tips) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de deep linking" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho para cada incidente de deep linking. Comece na etapa 1.

1. Teste o link fora da Braze. Para esquemas personalizados, execute `xcrun simctl openurl booted "<URL>"` no Terminal (por exemplo, `xcrun simctl openurl booted "myapp://products/123"`). Para links universais, cole a URL no app Notas em um dispositivo físico e toque nela.
2. [Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) e reproduza o problema. Procure por entradas `Opening '<URL>':` com `channel`, `useWebView` e `isUniversalLink`.
3. Para links universais, valide seu arquivo AASA e o entitlement de Associated Domains.
4. Para links de e-mail, confirme se o domínio de rastreamento de cliques hospeda um arquivo AASA válido.
5. Se você implementa `BrazeDelegate.braze(_:shouldOpenURL:)`, verifique se ele lida com links de forma consistente em todos os canais.
6. Se o problema persistir, entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support) com os logs detalhados e a URL do link.

## Deep link de esquema personalizado não abre a visualização correta {#custom-scheme-deep-link-does-not-open-the-correct-view}

**Sintoma:** Um deep link de esquema personalizado (por exemplo, `myapp://products/123`) abre seu app, mas não navega até a tela desejada.

1. **Verifique se o esquema está registrado.** No Xcode, confira se o esquema está listado em `CFBundleURLTypes` no `Info.plist`.
2. **Verifique seu handler.** Defina um breakpoint em `application(_:open:options:)` para confirmar que ele está sendo chamado e inspecione o parâmetro `url`.
3. **Teste o link de forma independente.** Execute o seguinte comando no Terminal para testar o deep link fora da Braze:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Se o link não funcionar aqui, o problema está no tratamento de URL do seu app, não na Braze.
4. **Verifique o formato da URL.** Confirme se a URL na sua Campaign corresponde ao que seu handler espera. Erros comuns incluem componentes de caminho ausentes ou uso incorreto de maiúsculas e minúsculas.

## O link universal abre no Safari em vez do app {#universal-link-opens-in-safari-instead-of-the-app}

**Sintoma:** Um link universal (por exemplo, `https://myapp.com/products/123`) abre no Safari em vez do seu app.

### Verifique a permissão de Associated Domains {#verify-the-associated-domains-entitlement}

No Xcode, acesse o alvo do seu app > **Signing & Capabilities** e verifique se `applinks:yourdomain.com` está listado em **Associated Domains**.

### Valide o arquivo AASA {#validate-the-aasa-file}

Seu arquivo Apple App Site Association (AASA) deve estar hospedado em um destes locais:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Verifique o seguinte:

- O arquivo é servido via HTTPS com um certificado válido.
- O `Content-Type` é `application/json`.
- O tamanho do arquivo é inferior a 128 KB.
- O `appID` corresponde ao seu Team ID e Bundle ID (por exemplo, `ABCDE12345.com.example.myapp`).
- O array `paths` ou `components` inclui os padrões de URL que você espera.

Você pode validar seu AASA usando a [ferramenta de validação de busca da Apple](https://search.developer.apple.com/appsearch-validation-tool/) ou executando:

```bash
swcutil dl -d yourdomain.com
```

### Verifique o `AppDelegate` {#check-the-appdelegate}

Verifique se `application(_:continue:restorationHandler:)` está implementado no seu `AppDelegate` e lida com o `NSUserActivity` corretamente:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Verifique a configuração do SDK da Braze {#verify-braze-sdk-configuration}

Se você estiver usando links universais de notificações por push entregues pela Braze, mensagens no app ou Content Cards, confirme que `forwardUniversalLinks` está ativado:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
O encaminhamento de links universais requer acesso aos direitos do aplicativo. Ao executar em um simulador, esses direitos não estão disponíveis diretamente. Para testar em um simulador, adicione o arquivo `.entitlements` à fase de build **Copy Bundle Resources**.
{% endalert %}

### Verifique o problema do toque longo {#check-for-the-long-press-issue}

Se você tocar e segurar um link universal e selecionar **Open**, o iOS pode "quebrar" a associação do link universal para aquele domínio. Esse é um comportamento conhecido do iOS. Para redefinir, toque e segure o link novamente e selecione **Open in [App Name]**.

## Deep link de e-mail não abre o app {#deep-link-from-email-does-not-open-the-app}

**Sintoma:** Um link em um e-mail não abre o app por meio do universal link.

Os links de e-mail passam pelo sistema de rastreamento de cliques do seu provedor de serviços de e-mail, que encapsula os links em um domínio de rastreamento (por exemplo, `https://click.yourdomain.com/...`). Para que os universal links funcionem a partir de e-mails, você precisa configurar o arquivo AASA no domínio de rastreamento de cliques, e não apenas no domínio principal.

### Verificar o AASA do domínio de rastreamento de cliques {#verify-click-tracking-domain-aasa}

1. Identifique o domínio de rastreamento de cliques nas configurações do seu provedor de serviços de e-mail (SendGrid, SparkPost ou Amazon SES).
2. Hospede o arquivo AASA em `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Confirme que o arquivo AASA no domínio de rastreamento de cliques inclui o mesmo `appID` e padrões de caminho válidos.

Para instruções de configuração específicas de cada provedor de serviços de e-mail, consulte [Universal links e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

### Verificar a cadeia de redirecionamento {#check-the-redirect-chain}

Alguns provedores de serviços de e-mail realizam um redirecionamento da URL de rastreamento de cliques para a URL final. Os universal links só funcionam se o iOS reconhecer o domínio *inicial* (o domínio de rastreamento de cliques) como associado ao seu app. Se o redirecionamento ignorar a verificação do AASA, o link será aberto no Safari.

Para testar:

1. Envie um e-mail de teste para você mesmo.
2. Mantenha o link pressionado e inspecione a URL — essa é a URL de rastreamento de cliques.
3. Verifique se esse domínio possui um arquivo AASA válido.

## Deep link funciona a partir de push, mas não de mensagem no app (ou vice-versa) {#deep-link-works-from-push-but-not-from-in-app-message}

**Sintoma:** O mesmo deep link funciona a partir de um canal da Braze, mas não de outro.

### Verifique o BrazeDelegate {#check-the-brazedelegate}

Se você implementa `BrazeDelegate.braze(_:shouldOpenURL:)`, verifique se ele trata os links de forma consistente entre os canais. O parâmetro `context` inclui o canal de origem. Procure por lógica condicional que possa estar filtrando acidentalmente links de canais específicos.

### Ative o registro detalhado {#enable-verbose-logging}

[Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) e reproduza o problema. Procure pela entrada de log `Opening`:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Compare a saída do log do canal que funciona com a do canal que não funciona. Diferenças em `useWebView` ou `isUniversalLink` indicam como o SDK está interpretando o link de forma diferente.

### Verifique se há delegates de exibição personalizados {#check-for-custom-display-delegates}

Se você usa um delegate de exibição personalizado para mensagens no app ou um manipulador de clique de Content Cards, verifique se ele passa corretamente os eventos de link para o SDK da Braze para tratamento.

## "Open Web URL Inside App" mostra uma página em branco ou quebrada {#open-web-url-inside-app-shows-a-blank-or-broken-page}

**Sintoma:** Selecionar **Open Web URL Inside App** resulta em uma WebView em branco ou quebrada.

1. **Verifique se a URL usa HTTPS.** A WebView do SDK requer URLs compatíveis com ATS. Links HTTP falham silenciosamente.
2. **Verifique os cabeçalhos de Content Security Policy.** Se a página web de destino definir `X-Frame-Options: DENY` ou um `Content-Security-Policy` restritivo, isso bloqueia a renderização em uma WebView.
3. **Verifique se há redirecionamentos para esquemas personalizados.** Se a página web redirecionar para um esquema personalizado (por exemplo, `myapp://`), a WebView não consegue lidar com isso.
4. **Teste a URL no Safari.** Se a página não carregar no Safari no dispositivo, ela também não carregará na WebView.

## Solução de problemas do Branch com a Braze {#branch}

Se você usar o [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) como seu provedor de links:

### Verifique se o BrazeDelegate encaminha para o Branch {#verify-the-brazedelegate-routes-to-branch}

Seu `BrazeDelegate` deve interceptar links do Branch e passá-los para o SDK do Branch. Verifique o seguinte:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Se `shouldOpenURL` retornar `true` para links do Branch, a Braze os manipula diretamente em vez de encaminhá-los para o Branch.

### Verifique o domínio do link do Branch {#check-branch-link-domain}

Verifique se o domínio do Branch no seu `BrazeDelegate` corresponde ao seu domínio real do link do Branch. O Branch usa vários formatos de domínio:

- `yourapp.app.link` (padrão)
- `yourapp-alternate.app.link` (alternativo)
- Domínios personalizados (se configurados no dashboard do Branch)

### Ative o registro de ambos os SDKs {#enable-both-sdks-logging}

Para diagnosticar onde o link quebra na cadeia:

1. Ative o [registro detalhado da Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Procure entradas `Opening '<URL>':` para verificar se o SDK recebeu o link.
2. Ative o [modo de teste do Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Verifique o dashboard do Branch para eventos de clique em links.
3. Se a Braze registrar o link, mas o Branch não detectar um clique, a lógica de roteamento do `BrazeDelegate` é provavelmente o problema.

### Verifique a configuração do dashboard do Branch {#check-branch-dashboard-configuration}

No dashboard do Branch, verifique:

- O **Bundle ID** e o **Team ID** do seu app correspondem ao seu projeto Xcode.
- Seus **Associated Domains** incluem o domínio do link do Branch.
- Seu arquivo AASA do Branch é válido (o Branch hospeda isso automaticamente em domínios `app.link`).

### Teste os links do Branch de forma independente {#test-branch-links-independently}

Teste o link do Branch fora da Braze para isolar o problema:

1. Abra o link do Branch no Safari no seu dispositivo. Se não abrir o app, o problema está na sua configuração do Branch ou AASA — não na Braze.
2. Cole o link do Branch no app Notas e toque nele. Links universais funcionam de forma mais confiável a partir do Notas do que da barra de endereços do Safari.

## Dicas gerais de depuração {#general-debugging-tips}

### Use o registro detalhado {#use-verbose-logging}

[Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) para ver exatamente como o SDK processa os links. Entradas importantes a serem observadas:

| Entrada de registro | O que significa |
|---|---|
| `Opening '<URL>': - channel: notification` | O SDK está processando um link de uma notificação por push |
| `Opening '<URL>': - channel: inAppMessage` | O SDK está processando um link de uma mensagem no app |
| `Opening '<URL>': - channel: contentCard` | O SDK está processando um link de um Content Cards |
| `useWebView: true` | O SDK abre a URL na WebView do app |
| `isUniversalLink: true` | O SDK identificou a URL como um universal link |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use o registro detalhado" }

Para mais detalhes sobre como ler esses registros, consulte [Leitura de registros detalhados]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

### Teste os links isoladamente {#test-links-in-isolation}

Antes de testar pela Braze, verifique se o seu deep link ou universal link funciona por conta própria:

- **Esquema personalizado**: Execute `xcrun simctl openurl booted "myapp://path"` no Terminal.
- **Universal link**: Cole a URL no app Notas em um dispositivo físico e toque nela. Não teste pela barra de endereço do Safari, pois o iOS trata URLs digitadas de forma diferente de links tocados.
- **Link do Branch**: Abra o link do Branch pelo app Notas em um dispositivo.

### Teste em um dispositivo físico {#test-on-a-physical-device}

Os universal links têm suporte limitado no simulador do iOS. Sempre teste em um dispositivo físico para obter resultados precisos. Se for necessário testar no simulador, adicione o arquivo `.entitlements` à fase de build **Copy Bundle Resources**.