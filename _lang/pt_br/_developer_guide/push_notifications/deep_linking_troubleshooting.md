---
nav_title: Solução de problemas de deep linking
article_title: Solução de problemas de deep linking
description: "Problemas comuns de deep linking no iOS e como diagnosticá-los, incluindo links de esquema personalizado, links universais, links de e-mail e provedores de terceiros como o Branch."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Solução de problemas de deep linking {#deep-linking-troubleshooting}

> Esta página cobre problemas comuns de deep linking no iOS e como diagnosticá-los. Para ajuda na escolha do tipo de link certo, consulte o [guia de deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/). Para detalhes de implementação, consulte [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## O deep link de esquema personalizado não abre a visualização correta {#custom-scheme-deep-link-doesnt-open-the-correct-view}

Se um deep link de esquema personalizado (por exemplo, `myapp://products/123`) abrir seu app, mas não navegar para a tela pretendida:

1. **Verifique se o esquema está registrado.** No Xcode, verifique se seu esquema está listado em `CFBundleURLTypes` no `Info.plist`.
2. **Verifique seu manipulador.** Defina um ponto de interrupção em `application(_:open:options:)` para confirmar se está sendo chamado e inspecione o parâmetro `url`.
3. **Teste o link de forma independente.** Execute o seguinte comando no Terminal para testar o deep link fora da Braze:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Se o link não funcionar aqui, o problema está no tratamento de URL do seu app — não na Braze.
4. **Verifique o formato da URL.** Verifique se a URL na sua Campaign corresponde ao que seu manipulador espera. Erros comuns incluem componentes de caminho ausentes ou capitalização incorreta.

## O link universal abre no Safari em vez do app {#universal-link-opens-in-safari-instead-of-the-app}

Se um link universal (por exemplo, `https://myapp.com/products/123`) abrir no Safari em vez do seu app:

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

## O deep link do e-mail não abre o app {#deep-link-from-email-doesnt-open-the-app}

Os links de e-mail passam pelo sistema de rastreamento de cliques do seu ESP, que envolve os links em um domínio de rastreamento (por exemplo, `https://click.yourdomain.com/...`). Para que os links universais funcionem a partir do e-mail, você deve configurar o arquivo AASA no seu domínio de rastreamento de cliques — não apenas no seu domínio principal.

### Verifique o AASA do domínio de rastreamento de cliques {#verify-click-tracking-domain-aasa}

1. Identifique seu domínio de rastreamento de cliques nas configurações do seu ESP (SendGrid, SparkPost ou Amazon SES).
2. Hospede o arquivo AASA em `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Certifique-se de que o arquivo AASA no domínio de rastreamento de cliques inclua o mesmo `appID` e padrões de caminho válidos.

Para instruções de configuração específicas do ESP, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/).

### Verifique a cadeia de redirecionamento {#check-the-redirect-chain}

Alguns ESPs realizam um redirecionamento da URL de rastreamento de cliques para sua URL final. Links universais só funcionam se o iOS reconhecer o domínio *inicial* (o domínio de rastreamento de cliques) como associado ao seu app. Se o redirecionamento contornar a verificação do AASA, o link será aberto no Safari.

Para testar:

1. Envie um e-mail de teste para você mesmo.
2. Toque e segure o link e inspecione a URL — essa é a URL de rastreamento de cliques.
3. Verifique se esse domínio possui um arquivo AASA válido.

## O deep link funciona a partir de push, mas não a partir de mensagens no app (ou vice-versa) {#deep-link-works-from-push-but-not-from-in-app-messages-or-vice-versa}

### Verifique o BrazeDelegate {#check-the-brazedelegate}

Se você implementar `BrazeDelegate.braze(_:shouldOpenURL:)`, verifique se ele lida com links de forma consistente entre os canais. O parâmetro `context` inclui o canal de origem. Procure lógica condicional que possa filtrar acidentalmente links de canais específicos.

### Ative o registro detalhado {#enable-verbose-logging}

[Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) e reproduza o problema. Procure a entrada de registro `Opening`:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Compare a saída do registro para o canal que funciona vs. o canal que não funciona. Diferenças em `useWebView` ou `isUniversalLink` indicam como o SDK está interpretando o link de forma diferente.

### Verifique se há delegates de exibição personalizados {#check-for-custom-display-delegates}

Se você usar um delegate de exibição de mensagem no app personalizado ou um manipulador de clique de Content Card personalizado, verifique se ele passa corretamente os eventos de link para o SDK da Braze para tratamento.

## "Open Web URL Inside App" mostra uma página em branco ou quebrada {#open-web-url-inside-app-shows-a-blank-or-broken-page}

Se selecionar **Open Web URL Inside App** resultar em uma WebView em branco ou quebrada:

1. **Verifique se a URL usa HTTPS.** A WebView do SDK requer URLs compatíveis com ATS. Links HTTP falham silenciosamente.
2. **Verifique os cabeçalhos de Content Security Policy.** Se a página da web de destino definir `X-Frame-Options: DENY` ou um `Content-Security-Policy` restritivo, isso bloqueia a renderização em uma WebView.
3. **Verifique se há redirecionamentos para esquemas personalizados.** Se a página da web redirecionar para um esquema personalizado (por exemplo, `myapp://`), a WebView não consegue lidar com isso.
4. **Teste a URL no Safari.** Se a página não carregar no Safari no dispositivo, ela também não carregará na WebView.

## Solução de problemas do Branch com a Braze {#branch}

Se você usar o [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) como seu provedor de links:

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

1. Ative o [registro detalhado da Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) — procure entradas `Opening '<URL>':` para verificar se o SDK recebeu o link.
2. Ative o [modo de teste do Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) — verifique o dashboard do Branch para eventos de clique em links.
1. Ative o [registro detalhado da Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/). Procure entradas `Opening '<URL>':` para verificar se o SDK recebeu o link.
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

[Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) para ver exatamente como o SDK processa os links. Entradas-chave a serem observadas:

| Entrada de registro | O que significa |
|---|---|
| `Opening '<URL>': - channel: notification` | O SDK está processando um link de uma notificação por push |
| `Opening '<URL>': - channel: inAppMessage` | O SDK está processando um link de uma mensagem no app |
| `Opening '<URL>': - channel: contentCard` | O SDK está processando um link de um Content Card |
| `useWebView: true` | O SDK abre a URL na WebView do app |
| `isUniversalLink: true` | O SDK identificou a URL como um link universal |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Usar registro detalhado" }

Para mais detalhes sobre como ler esses registros, consulte [Lendo registros detalhados]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/).

### Teste links em isolamento {#test-links-in-isolation}

Antes de testar pela Braze, verifique se seu deep link ou link universal funciona por conta própria:

- **Esquema personalizado**: Execute `xcrun simctl openurl booted "myapp://path"` no Terminal.
- **Link universal**: Cole a URL no app Notas em um dispositivo físico e toque nela. Não teste a partir da barra de endereços do Safari, pois o iOS trata URLs digitadas de forma diferente de links tocados.
- **Link do Branch**: Abra o link do Branch a partir do app Notas em um dispositivo.

### Teste em um dispositivo físico {#test-on-a-physical-device}

Links universais têm suporte limitado no simulador iOS. Sempre teste em um dispositivo físico para resultados precisos. Se você precisar testar em um simulador, adicione o arquivo `.entitlements` à fase de build **Copy Bundle Resources**.