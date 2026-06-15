---
nav_title: Résolution des problèmes de création de liens profonds
article_title: Résolution des problèmes de création de liens profonds
description: "Problèmes courants liés à la création de liens profonds sur iOS et comment les diagnostiquer, y compris les liens de schéma personnalisé, les liens universels, les liens e-mail et les fournisseurs tiers comme Branch."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Résolution des problèmes de création de liens profonds {#deep-linking-troubleshooting}

> Cette page traite des problèmes courants liés à la création de liens profonds sur iOS et explique comment les diagnostiquer. Pour obtenir de l'aide afin de choisir le type de lien approprié, consultez le [guide de création de liens profonds iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/). Pour les détails d'implémentation, consultez [Création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## Le lien profond de schéma personnalisé n'ouvre pas la vue correcte {#custom-scheme-deep-link-doesnt-open-the-correct-view}

Si un lien profond de schéma personnalisé (par exemple, `myapp://products/123`) ouvre votre application mais ne navigue pas vers l'écran souhaité :

1. **Vérifiez que le schéma est enregistré.** Dans Xcode, vérifiez que votre schéma est répertorié sous `CFBundleURLTypes` dans `Info.plist`.
2. **Vérifiez votre gestionnaire.** Définissez un point d'arrêt dans `application(_:open:options:)` pour confirmer qu'il est bien appelé et inspectez le paramètre `url`.
3. **Testez le lien de manière indépendante.** Exécutez la commande suivante depuis le terminal pour tester le lien profond en dehors de Braze :
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Si le lien ne fonctionne pas ici, le problème provient de la gestion des URL de votre application, et non de Braze.
4. **Vérifiez le format de l'URL.** Vérifiez que l'URL de votre campagne correspond à ce que votre gestionnaire attend. Les erreurs courantes incluent des composants de chemin manquants ou une casse incorrecte.

## Le lien universel s'ouvre dans Safari au lieu de l'application {#universal-link-opens-in-safari-instead-of-the-app}

Si un lien universel (par exemple, `https://myapp.com/products/123`) s'ouvre dans Safari au lieu de votre application :

### Vérifier le droit Associated Domains {#verify-the-associated-domains-entitlement}

Dans Xcode, accédez à la cible de votre application > **Signing & Capabilities** et vérifiez que `applinks:yourdomain.com` est répertorié sous **Associated Domains**.

### Valider le fichier AASA {#validate-the-aasa-file}

Votre fichier Apple App Site Association (AASA) doit être hébergé à l'un des emplacements suivants :

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Vérifiez les éléments suivants :

- Le fichier est servi via HTTPS avec un certificat valide.
- Le `Content-Type` est `application/json`.
- La taille du fichier est inférieure à 128 Ko.
- L'`appID` correspond à votre Team ID et Bundle ID (par exemple, `ABCDE12345.com.example.myapp`).
- Le tableau `paths` ou `components` inclut les modèles d'URL attendus.

Vous pouvez valider votre AASA à l'aide de [l'outil de validation de recherche d'Apple](https://search.developer.apple.com/appsearch-validation-tool/) ou en exécutant :

```bash
swcutil dl -d yourdomain.com
```

### Vérifier l'`AppDelegate` {#check-the-appdelegate}

Vérifiez que `application(_:continue:restorationHandler:)` est implémenté dans votre `AppDelegate` et gère correctement le `NSUserActivity` :

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

### Vérifier la configuration du SDK Braze {#verify-braze-sdk-configuration}

Si vous utilisez des liens universels à partir de notifications push, de messages in-app ou de Content Cards envoyés par Braze, vérifiez que `forwardUniversalLinks` est activé :

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
Le transfert de liens universels nécessite l'accès aux droits de l'application. Lors de l'exécution dans un simulateur, ces droits ne sont pas directement disponibles. Pour tester dans un simulateur, ajoutez le fichier `.entitlements` à la phase de build **Copy Bundle Resources**.
{% endalert %}

### Vérifier le problème lié à l'appui long {#check-for-the-long-press-issue}

Si vous appuyez longuement sur un lien universel et sélectionnez **Open**, iOS peut « rompre » l'association du lien universel pour ce domaine. Il s'agit d'un comportement connu d'iOS. Pour le réinitialiser, appuyez longuement sur le lien à nouveau et sélectionnez **Open in [App Name]**.

## Le lien profond provenant d'un e-mail n'ouvre pas l'application {#deep-link-from-email-doesnt-open-the-app}

Les liens contenus dans les e-mails passent par le système de suivi des clics de votre ESP, qui encapsule les liens dans un domaine de suivi (par exemple, `https://click.yourdomain.com/...`). Pour que les liens universels fonctionnent à partir des e-mails, vous devez configurer le fichier AASA sur votre domaine de suivi des clics, et pas uniquement sur votre domaine principal.

### Vérifier le fichier AASA du domaine de suivi des clics {#verify-click-tracking-domain-aasa}

1. Identifiez votre domaine de suivi des clics à partir des paramètres de votre ESP (SendGrid, SparkPost ou Amazon SES).
2. Hébergez le fichier AASA à l'adresse `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Assurez-vous que le fichier AASA sur le domaine de suivi des clics contient le même `appID` et des modèles de chemin valides.

Pour obtenir des instructions de configuration spécifiques à chaque ESP, consultez [Liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/).

### Vérifier la chaîne de redirection {#check-the-redirect-chain}

Certains ESP effectuent une redirection de l'URL de suivi des clics vers votre URL finale. Les liens universels ne fonctionnent que si iOS reconnaît le domaine *initial* (le domaine de suivi des clics) comme étant associé à votre application. Si la redirection contourne la vérification AASA, le lien s'ouvre dans Safari.

Pour tester :

1. Envoyez-vous un e-mail de test.
2. Appuyez longuement sur le lien et inspectez l'URL — il s'agit de l'URL de suivi des clics.
3. Vérifiez que ce domaine dispose d'un fichier AASA valide.

## Le lien profond fonctionne depuis les notifications push mais pas depuis les messages in-app (ou inversement) {#deep-link-works-from-push-but-not-from-in-app-messages-or-vice-versa}

### Vérifier le BrazeDelegate {#check-the-brazedelegate}

Si vous implémentez `BrazeDelegate.braze(_:shouldOpenURL:)`, vérifiez qu'il gère les liens de manière cohérente sur tous les canaux. Le paramètre `context` inclut le canal source. Recherchez toute logique conditionnelle susceptible de filtrer accidentellement les liens provenant de canaux spécifiques.

### Activer la journalisation détaillée {#enable-verbose-logging}

[Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) et reproduisez le problème. Recherchez l'entrée de journal `Opening` :

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Comparez les résultats du journal pour le canal fonctionnel et le canal non fonctionnel. Les différences dans `useWebView` ou `isUniversalLink` indiquent comment le SDK interprète le lien différemment.

### Vérifier les délégués d'affichage personnalisés {#check-for-custom-display-delegates}

Si vous utilisez un délégué d'affichage de messages in-app personnalisé ou un gestionnaire de clics sur les Content Cards, vérifiez qu'il transmet correctement les événements de lien au SDK Braze pour traitement.

## « Ouvrir l'URL Web dans l'application » affiche une page vide ou défectueuse {#open-web-url-inside-app-shows-a-blank-or-broken-page}

Si la sélection de **Open Web URL Inside App** affiche une WebView vide ou défectueuse :

1. **Vérifiez que l'URL utilise HTTPS.** La WebView du SDK nécessite des URL conformes à ATS. Les liens HTTP échouent silencieusement.
2. **Vérifiez les en-têtes Content Security Policy.** Si la page Web cible définit `X-Frame-Options: DENY` ou une `Content-Security-Policy` restrictive, elle bloque le rendu dans une WebView.
3. **Vérifiez les redirections vers des schémas personnalisés.** Si la page Web redirige vers un schéma personnalisé (par exemple, `myapp://`), la WebView ne peut pas le gérer.
4. **Testez l'URL dans Safari.** Si la page ne se charge pas dans Safari sur l'appareil, elle ne se chargera pas non plus dans la WebView.

## Résolution des problèmes de Branch avec Braze {#branch}

Si vous utilisez [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) comme fournisseur de liens :

### Vérifier que le BrazeDelegate route vers Branch {#verify-the-brazedelegate-routes-to-branch}

Votre `BrazeDelegate` doit intercepter les liens Branch et les transmettre au SDK Branch. Vérifiez les éléments suivants :

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

Si `shouldOpenURL` retourne `true` pour les liens Branch, Braze les traite directement au lieu de les acheminer vers Branch.

### Vérifier le domaine du lien Branch {#check-branch-link-domain}

Vérifiez que le domaine Branch dans votre `BrazeDelegate` correspond à votre domaine de lien Branch réel. Branch utilise plusieurs formats de domaine :

- `yourapp.app.link` (par défaut)
- `yourapp-alternate.app.link` (alternatif)
- Domaines personnalisés (s'ils sont configurés dans le tableau de bord Branch)

### Activer la journalisation des deux SDK {#enable-both-sdks-logging}

Pour diagnostiquer où le lien se rompt dans la chaîne :

1. Activez la [journalisation détaillée Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) — recherchez les entrées `Opening '<URL>':` pour vérifier que le SDK a bien reçu le lien.
2. Activez le [mode test Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) — consultez le tableau de bord Branch pour les événements de clic sur les liens.
1. Activez la [journalisation détaillée Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/). Recherchez les entrées `Opening '<URL>':` pour vérifier que le SDK a bien reçu le lien.
2. Activez le [mode test Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Consultez le tableau de bord Branch pour les événements de clic sur les liens.
3. Si Braze enregistre le lien mais que Branch ne détecte aucun clic, la logique de routage du `BrazeDelegate` est probablement en cause.

### Vérifier la configuration du tableau de bord Branch {#check-branch-dashboard-configuration}

Dans le tableau de bord Branch, vérifiez :

- Le **Bundle ID** et le **Team ID** de votre application correspondent à votre projet Xcode.
- Vos **Associated Domains** incluent le domaine du lien Branch.
- Votre fichier AASA Branch est valide (Branch l'héberge automatiquement sur les domaines `app.link`).

### Tester les liens Branch de manière indépendante {#test-branch-links-independently}

Testez le lien Branch en dehors de Braze pour isoler le problème :

1. Ouvrez le lien Branch dans Safari sur votre appareil. S'il n'ouvre pas l'application, le problème provient de votre configuration Branch ou AASA, et non de Braze.
2. Collez le lien Branch dans l'application Notes et appuyez dessus. Les liens universels fonctionnent de manière plus fiable depuis Notes que depuis la barre d'adresse de Safari.

## Conseils généraux de débogage {#general-debugging-tips}

### Utiliser la journalisation détaillée {#use-verbose-logging}

[Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) pour observer précisément comment le SDK traite les liens. Entrées clés à rechercher :

| Entrée de journal | Signification |
|---|---|
| `Opening '<URL>': - channel: notification` | Le SDK traite un lien provenant d'une notification push |
| `Opening '<URL>': - channel: inAppMessage` | Le SDK traite un lien provenant d'un message in-app |
| `Opening '<URL>': - channel: contentCard` | Le SDK traite un lien provenant d'une Content Card |
| `useWebView: true` | Le SDK ouvre l'URL dans la WebView intégrée à l'application |
| `isUniversalLink: true` | Le SDK a identifié l'URL comme un lien universel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Utiliser la journalisation détaillée" }

Pour plus de détails sur la lecture de ces journaux, consultez [Lecture des journaux détaillés]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/).

### Tester les liens de manière isolée {#test-links-in-isolation}

Avant de tester via Braze, vérifiez que votre lien profond ou lien universel fonctionne de manière autonome :

- **Schéma personnalisé** : Exécutez `xcrun simctl openurl booted "myapp://path"` dans le terminal.
- **Lien universel** : Collez l'URL dans l'application Notes sur un appareil physique et appuyez dessus. Ne testez pas depuis la barre d'adresse de Safari, car iOS traite les URL saisies différemment des liens sur lesquels on appuie.
- **Lien Branch** : Ouvrez le lien Branch depuis l'application Notes sur un appareil.

### Tester sur un appareil physique {#test-on-a-physical-device}

Les liens universels ont une prise en charge limitée dans le simulateur iOS. Testez toujours sur un appareil physique pour obtenir des résultats précis. Si vous devez tester dans un simulateur, ajoutez le fichier `.entitlements` à la phase de build **Copy Bundle Resources**.