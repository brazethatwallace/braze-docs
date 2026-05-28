---
nav_title: Branch pour la création de liens profonds
article_title: Branch pour la création de liens profonds
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Cet article de référence décrit le partenariat entre Braze et Branch et comment l'utiliser pour soutenir vos pratiques de création de liens profonds."
search_tag: Partner

---

# Branch pour la création de liens profonds {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/) est une plateforme de liaison mobile utilisée pour acquérir, engager et mesurer à travers les appareils, les canaux et les plateformes en fournissant une vue globale des points de contact utilisateur.

_Cette intégration est maintenue par Branch._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Branch vous permet d'offrir de meilleures expériences à vos clients en [attribuant]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) correctement le début de leur parcours utilisateur et en les connectant par des liens profonds à l'emplacement prévu.

{% alert tip %}
Pour vous aider à choisir la bonne approche de création de liens profonds pour votre cas d'utilisation, consultez le [guide de création de liens profonds iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/).
{% endalert %}

## Intégration {#integration}

Consultez [le guide d'intégration du SDK de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview) pour mettre en place votre intégration Branch. Reportez-vous aux sections suivantes pour des cas d'utilisation supplémentaires.

### Prise en charge des liens universels iOS {#support-ios-universal-links}

Pour prendre en charge l'envoi de liens universels iOS en tant que liens profonds depuis Braze :

#### Étape 1 : Configurer les liens universels Branch {#step-1-set-up-branch-universal-links}

Suivez la documentation de Branch pour configurer les [liens universels](https://help.branch.io/developers-hub/docs/ios-universal-links). Dans le cadre de cette configuration, Branch héberge automatiquement le fichier AASA sur votre domaine de lien Branch (par exemple, `yourapp.app.link`).

#### Étape 2 : Configurer les domaines associés {#step-2-configure-associated-domains}

Dans Xcode, accédez à la cible de votre application > **Signing & Capabilities** et ajoutez votre domaine de lien Branch sous **Associated Domains** :

```
applinks:yourapp.app.link
applinks:yourapp-alternate.app.link
```

Si vous utilisez un domaine Branch personnalisé, ajoutez-le également.

#### Étape 3 : Transférer les liens universels dans Braze {#step-3-forward-universal-links-in-braze}

Définissez `forwardUniversalLinks` sur `true` dans la configuration de votre SDK Braze afin que le SDK transfère les liens universels au `AppDelegate` de votre application :

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

#### Étape 4 : Acheminer les liens Branch avec BrazeDelegate {#step-4-route-branch-links-with-brazedelegate}

Implémentez [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate) pour intercepter les liens Branch avant que Braze ne les traite. Cela permet à Branch de traiter le lien et d'effectuer son propre routage :

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

Remplacez `yourdomain.com` par votre domaine Branch personnalisé, le cas échéant.

### Création de liens profonds dans les e-mails {#deep-linking-in-email}

Consultez la documentation sur les [liens universels et les liens applicatifs]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/)
ou consultez [la documentation de Branch](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) pour mettre en place la création de liens profonds à partir d'e-mails envoyés par l'intermédiaire de Braze.

La liaison avec des numéros de téléphone (en ajoutant `tel` à `href`) n'est pas prise en charge dans l'application Gmail pour iOS, sauf si l'utilisateur accorde des autorisations d'appel à l'application.

En fonction de votre ESP, une personnalisation supplémentaire peut être nécessaire pour prendre en charge les liens universels avec suivi des clics. Ces informations sont détaillées dans notre article dédié. Vous pouvez également consulter les références suivantes pour en savoir plus :

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

## Résolution des problèmes {#troubleshooting}

Si les liens Branch ne fonctionnent pas comme prévu depuis les campagnes Braze, suivez ces étapes.

### Vérifier que le lien fonctionne en dehors de Braze {#verify-the-link-works-outside-of-braze}

Ouvrez le lien Branch depuis l'application Notes sur un appareil iOS physique. S'il n'ouvre pas votre application :

- Le problème se situe dans votre configuration Branch ou AASA, pas dans Braze.
- Validez votre fichier AASA Branch à l'adresse `https://yourapp.app.link/.well-known/apple-app-site-association`.
- Vérifiez que votre Bundle ID et votre Team ID correspondent dans le tableau de bord Branch.

### Activer la double journalisation {#enable-dual-logging}

1. **Braze** : [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) et recherchez les entrées `Opening '<URL>':`. Cela confirme que le SDK a reçu le lien.
2. **Branch** : Activez le [mode test de Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) et vérifiez les événements de clic sur les liens dans le tableau de bord Branch.
3. **Comparez** : Si Braze enregistre le lien mais que Branch ne détecte pas de clic, la logique de routage du `BrazeDelegate` n'intercepte probablement pas le lien correctement. Vérifiez que la correspondance de domaine dans `shouldOpenURL` inclut votre domaine Branch.

### Problèmes courants {#common-issues}

| Symptôme | Cause probable | Correction |
|---|---|---|
| Le lien Branch s'ouvre dans Safari | AASA invalide ou manquant sur le domaine Branch | Vérifiez les domaines associés et le fichier AASA |
| Le lien Branch s'ouvre mais arrive sur le mauvais écran | Données du lien Branch mal configurées | Vérifiez les règles de routage dans le tableau de bord Branch |
| Le lien fonctionne depuis les notifications push mais pas depuis les e-mails | Le domaine de suivi des clics ne dispose pas du fichier AASA | Hébergez le fichier AASA sur le domaine de suivi des clics de votre ESP ; voir [Configuration des e-mails](#deep-linking-in-email) |
| `shouldOpenURL` ne se déclenche jamais pour les liens Branch | `forwardUniversalLinks` non activé | Définissez `configuration.forwardUniversalLinks = true` |
| Le lien Branch fonctionne depuis Notes mais pas depuis Braze | `BrazeDelegate` renvoie `true` pour les URL Branch | Vérifiez la correspondance de domaine dans `shouldOpenURL` avec votre domaine Branch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Problèmes courants" }

Pour plus de scénarios de résolution des problèmes de liens profonds, consultez [Résolution des problèmes de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/).