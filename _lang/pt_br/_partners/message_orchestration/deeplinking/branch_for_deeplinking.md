---
nav_title: Branch para deep linking
article_title: Branch para deep linking
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Este artigo de referência descreve a parceria entre a Braze e a Branch e como usá-la para dar suporte às suas práticas de deep linking."
search_tag: Partner

---

# Branch para deep linking {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> A [Branch](https://branch.io/) é uma plataforma de vinculação móvel usada para adquirir, engajar e medir em dispositivos, canais e plataformas, fornecendo uma visão holística dos pontos de contato do usuário.

_Essa integração é mantida pela Branch._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Branch permite oferecer melhores experiências aos seus clientes, pois você pode [atribuir]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) adequadamente o início da jornada do usuário e conectá-los por deep links ao local pretendido.

{% alert tip %}
Para ajuda na escolha da abordagem de deep linking mais adequada ao seu caso de uso, consulte o [guia de deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/).
{% endalert %}

## Integração {#integration}

Siga o [guia de integração de SDK da Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview) para configurar sua integração. Consulte os casos de uso adicionais a seguir.

### Suporte a links universais do iOS {#support-ios-universal-links}

Para dar suporte ao envio de links universais do iOS como deep links na Braze:

#### Etapa 1: Configurar links universais da Branch {#step-1-set-up-branch-universal-links}

Siga a documentação da Branch para configurar [links universais](https://help.branch.io/developers-hub/docs/ios-universal-links). Como parte dessa configuração, a Branch hospeda automaticamente o arquivo AASA no domínio do seu link Branch (por exemplo, `yourapp.app.link`).

#### Etapa 2: Configurar Associated Domains {#step-2-configure-associated-domains}

No Xcode, acesse o target do seu app > **Signing & Capabilities** e adicione o domínio do seu link Branch em **Associated Domains**:

```
applinks:yourapp.app.link
applinks:yourapp-alternate.app.link
```

Se você usa um domínio Branch personalizado, adicione-o também.

#### Etapa 3: Encaminhar links universais na Braze {#step-3-forward-universal-links-in-braze}

Defina `forwardUniversalLinks` como `true` na configuração do SDK da Braze para que o SDK encaminhe links universais ao `AppDelegate` do seu app:

{% tabs %}
{% tab swift %}
```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
let braze = Braze(configuration: configuration)
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
configuration.forwardUniversalLinks = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endtab %}
{% endtabs %}

#### Etapa 4: Rotear links da Branch com BrazeDelegate {#step-4-route-branch-links-with-brazedelegate}

Implemente o [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate) para interceptar links da Branch antes que a Braze os processe. Isso garante que a Branch possa processar o link e realizar seu próprio roteamento:

{% tabs %}
{% tab swift %}
```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host,
     host.contains("app.link") || host.contains("yourdomain.com") {
    // Let Branch handle this link
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle all other links
  return true
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  NSString *host = context.url.host;
  if (host && ([host containsString:@"app.link"] || [host containsString:@"yourdomain.com"])) {
    [[Branch getInstance] handleDeepLink:context.url];
    return NO;
  }
  return YES;
}
```
{% endtab %}
{% endtabs %}

Substitua `yourdomain.com` pelo seu domínio Branch personalizado, se aplicável.

### Deep linking em e-mails {#deep-linking-in-email}

Consulte a documentação sobre [links universais e links de app]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/)
ou veja a [documentação da Branch](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) para configurar deep linking a partir de e-mails enviados pela Braze.

O vínculo a números de telefone (anexando `tel` a `href`) não é compatível com o app Gmail para iOS, a menos que o usuário conceda permissões de chamada ao app.

Dependendo do seu ESP, pode ser necessária uma personalização adicional para dar suporte a links universais com rastreamento de cliques. Essas informações estão descritas em nosso artigo específico. Você também pode consultar as seguintes referências para saber mais:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

## Solução de problemas {#troubleshooting}

Se os links da Branch não estiverem funcionando como esperado em Campaigns da Braze, siga estas etapas.

### Verificar se o link funciona fora da Braze {#verify-the-link-works-outside-of-braze}

Abra o link da Branch pelo app Notas em um dispositivo iOS físico. Se ele não abrir seu app:

- O problema está na configuração da Branch ou do AASA, não na Braze.
- Valide o AASA da Branch em `https://yourapp.app.link/.well-known/apple-app-site-association`.
- Verifique se o Bundle ID e o Team ID correspondem no dashboard da Branch.

### Ativar registro duplo {#enable-dual-logging}

1. **Braze**: [Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) e procure por entradas `Opening '<URL>':`. Isso confirma que o SDK recebeu o link.
2. **Branch**: Ative o [modo de teste da Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) e verifique os eventos de clique no link no dashboard da Branch.
3. **Compare**: Se a Braze registra o link, mas a Branch não detecta um clique, a lógica de roteamento do `BrazeDelegate` provavelmente não está interceptando o link corretamente. Verifique se a correspondência de domínio em `shouldOpenURL` inclui o domínio da Branch.

### Problemas comuns {#common-issues}

| Sintoma | Causa provável | Correção |
|---|---|---|
| O link da Branch abre no Safari | AASA inválido ou ausente no domínio da Branch | Verifique os Associated Domains e o arquivo AASA |
| O link da Branch abre, mas direciona para a tela errada | Dados do link da Branch mal configurados | Verifique as regras de roteamento no dashboard da Branch |
| O link funciona via push, mas não por e-mail | Domínio de rastreamento de cliques sem AASA | Hospede o AASA no domínio de rastreamento de cliques do seu ESP; consulte [Configuração de e-mail](#deep-linking-in-email) |
| `shouldOpenURL` nunca é acionado para links da Branch | `forwardUniversalLinks` não ativado | Defina `configuration.forwardUniversalLinks = true` |
| O link da Branch funciona pelo Notas, mas não pela Braze | `BrazeDelegate` retornando `true` para URLs da Branch | Verifique a correspondência de domínio em `shouldOpenURL` com o domínio da Branch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Common issues" }

Para mais cenários de solução de problemas com deep linking, consulte [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/).