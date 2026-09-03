---
page_order: 1.1
nav_title: Guide sur la création de liens profonds iOS
article_title: Guide sur la création de liens profonds iOS
description: "Découvrez quel type de lien profond utiliser pour votre application iOS, quand vous avez besoin d'un fichier AASA et quelles méthodes de délégation d'application implémenter."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Guide sur la création de liens profonds iOS {#ios-deep-linking-guide}

> Ce guide vous aide à choisir la stratégie de création de liens profonds la mieux adaptée à votre application iOS, en fonction du canal de communication que vous utilisez et de votre recours ou non à un fournisseur de liens tiers tel que Branch.

Pour plus de détails sur l'implémentation, consultez [Création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Pour la résolution des problèmes, consultez [Résolution des problèmes de création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Choisir un type de lien {#choosing-a-link-type}

Il existe trois façons de gérer les liens provenant des messages Braze dans votre application iOS. Chacune fonctionne différemment et convient à des canaux et des cas d'usage différents.

| Type de lien | Exemple | Idéal pour | S'ouvre sans l'application installée ? |
|---|---|---|---|
| **Schéma personnalisé** | `myapp://products/123` | Notifications push, messages in-app, Content Cards | Non — le lien échoue |
| **Lien universel** | `https://myapp.com/products/123` | E-mail, SMS, canaux avec suivi des clics | Oui — bascule vers le web |
| **Ouvrir l'URL web dans l'application** | Toute URL `https://` | Afficher du contenu web dans une WebView modale | N/A — s'affiche dans la WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Choisir un type de lien" }

### Deep links à schéma personnalisé {#custom-scheme-deep-links}

Les deep links à schéma personnalisé (par exemple, `myapp://products/123`) ouvrent votre application directement sur un écran spécifique. C'est l'option la plus simple pour les canaux où les liens ne sont pas modifiés par un tiers.

**Utilisez les deep links à schéma personnalisé lorsque :**
- Vous envoyez des notifications push, des messages in-app ou des Content Cards
- Vous n'avez pas besoin que le lien fonctionne si l'application n'est pas installée
- Vous n'avez pas besoin de suivi des clics (encapsulation des liens par l'ESP d'e-mail)

**N'utilisez pas les deep links à schéma personnalisé lorsque :**
- Vous envoyez des e-mails — les ESP encapsulent les liens pour le suivi des clics, ce qui casse les schémas personnalisés
- Vous avez besoin que le lien bascule vers une page web si l'application n'est pas installée

### Liens universels {#universal-links}

Les liens universels (par exemple, `https://myapp.com/products/123`) sont des URL HTTPS standard qu'iOS peut rediriger vers votre application au lieu de les ouvrir dans un navigateur. Ils nécessitent une configuration côté serveur (un fichier AASA) et côté application (l'entitlement Associated Domains).

**Utilisez les liens universels lorsque :**
- Vous envoyez des e-mails. Votre ESP encapsule les liens pour le suivi des clics, les liens doivent donc être en HTTPS.
- Vous envoyez des SMS ou utilisez d'autres canaux où les liens sont encapsulés ou raccourcis.
- Vous avez besoin que le lien bascule vers une page web lorsque l'application n'est pas installée.
- Vous utilisez un fournisseur de liens tiers comme Branch ou AppsFlyer.

**N'utilisez pas les liens universels lorsque :**
- Vous avez uniquement besoin de deep links à partir de notifications push, de messages in-app ou de Content Cards. Les schémas personnalisés sont plus simples.

### « Ouvrir l'URL web dans l'application » {#open-web-url-inside-app}

Cette option ouvre une page web dans une WebView modale au sein de votre application. Elle est entièrement gérée par le SDK Braze via `Braze.WebViewController` — vous n'avez pas besoin d'écrire de code de gestion des URL.

**Utilisez « Ouvrir l'URL web dans l'application » lorsque :**
- Vous souhaitez afficher une page web (comme une promotion ou un article) sans quitter votre application.
- L'URL est une page web HTTPS standard, pas un deep link vers un écran spécifique de l'application.

**N'utilisez pas « Ouvrir l'URL web dans l'application » lorsque :**
- Vous devez naviguer vers une vue spécifique dans votre application. Utilisez plutôt un schéma personnalisé ou un lien universel.
- La page web nécessite une authentification ou comporte des en-têtes Content Security Policy qui bloquent l'intégration.

## Ce dont vous avez besoin pour chaque type de lien {#what-you-need-for-each-link-type}

### Deep links avec schéma personnalisé

| Exigence | Détails |
|---|---|
| Fichier AASA | Non requis |
| `Info.plist` | Enregistrez votre schéma sous `CFBundleURLTypes` et ajoutez-le à `LSApplicationQueriesSchemes` |
| Méthode du délégué d'application | Implémentez `application(_:open:options:)` pour analyser l'URL et naviguer |
| Configuration du SDK Braze | Aucune — le SDK ouvre les URL avec schéma personnalisé par défaut |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deep links avec schéma personnalisé" }

### Liens universels

| Exigence | Détails |
|---|---|
| Fichier AASA | Requis — hébergez-le à l'adresse `https://yourdomain.com/.well-known/apple-app-site-association` |
| Associated Domains | Ajoutez `applinks:yourdomain.com` dans Xcode sous **Signing & Capabilities** |
| Méthode du délégué d'application | Implémentez `application(_:continue:restorationHandler:)` pour gérer `NSUserActivity` |
| Configuration du SDK Braze | Définissez `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (optionnel) | Implémentez `braze(_:shouldOpenURL:)` pour un routage personnalisé (par exemple, Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liens universels" }

{% alert important %}
Si vous envoyez des e-mails via Braze, votre fournisseur de services de messagerie (Sendgrid, SparkPost ou Amazon SES) encapsule les liens dans un domaine de suivi des clics. Vous devez également héberger le fichier AASA sur votre domaine de suivi des clics, et pas uniquement sur votre domaine principal. Pour une configuration complète, consultez [Liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links). Si chaque lien d'e-mail ouvre l'application, consultez [Chaque lien d'e-mail ouvre l'application]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting#every-email-link-opens-the-app).
{% endalert %}

### « Open Web URL Inside App »

| Exigence | Détails |
|---|---|
| Fichier AASA | Non requis |
| Méthode du délégué d'application | Non requise — le SDK gère cela automatiquement |
| Configuration du SDK Braze | Aucune — sélectionnez **Open Web URL Inside App** dans le composeur de Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label="« Open Web URL Inside App »" }

## Quand avez-vous besoin d'un fichier AASA {#when-aasa}

Un fichier Apple App Site Association (AASA) n'est requis que lorsque vous utilisez des **liens universels**. Il indique à iOS quelles URL votre application peut gérer.

Vous avez besoin d'un fichier AASA lorsque :

- Vous envoyez des deep links dans des Campaigns par e-mail (car les ESP encapsulent les liens dans des URL HTTPS de suivi des clics).
- Vous envoyez des deep links dans des Campaigns SMS (car les liens peuvent être raccourcis en URL HTTPS).
- Vous utilisez Branch, AppsFlyer ou un autre fournisseur de liens (car ils utilisent leurs propres domaines HTTPS).
- Vous utilisez des liens universels depuis des notifications push, des messages in-app ou des Content Cards (moins courant, mais possible avec `forwardUniversalLinks = true`).

Vous n'avez pas besoin d'un fichier AASA lorsque :

- Vous n'utilisez que des deep links avec schéma personnalisé (par exemple, `myapp://`) depuis des notifications push, des messages in-app ou des Content Cards.
- Vous utilisez l'option **Ouvrir l'URL web dans l'application**.

Pour les instructions de configuration AASA, consultez [Liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Quand avez-vous besoin de code applicatif pour gérer les liens {#when-app-code}

La méthode déléguée que vous implémentez dépend du type de lien que vous utilisez :

| Méthode déléguée | Gère | Quand l'implémenter |
|---|---|---|
| `application(_:open:options:)` | Liens profonds avec schéma personnalisé (`myapp://`) | Vous utilisez des liens profonds avec schéma personnalisé depuis n'importe quel canal |
| `application(_:continue:restorationHandler:)` | Liens universels (`https://`) | Vous utilisez des liens universels depuis des e-mails, des SMS ou avec `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Toutes les URL ouvertes par le SDK | Vous avez besoin d'une logique de routage personnalisée (par exemple, Branch, traitement conditionnel, analytique) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Quand avez-vous besoin de code applicatif pour gérer les liens" }

{% alert tip %}
Si vous utilisez un fournisseur de liens tiers tel que Branch, implémentez `BrazeDelegate.braze(_:shouldOpenURL:)` pour intercepter les URL et les transmettre au SDK du fournisseur. Consultez [Branch pour la création de liens profonds]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) pour un exemple complet.
{% endalert %}

## Utiliser Branch avec Braze {#branch}

Si vous utilisez [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) comme fournisseur de liens, votre configuration nécessite quelques étapes supplémentaires par rapport à une configuration de lien universel standard :

1. **SDK Branch** : intégrez le SDK Branch en suivant [la documentation de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Domaines associés** : ajoutez votre domaine Branch (par exemple, `applinks:yourapp.app.link`) dans Xcode sous **Signing & Capabilities**.
3. **BrazeDelegate** : implémentez `braze(_:shouldOpenURL:)` pour router les liens Branch vers le SDK Branch au lieu de laisser Braze les gérer directement.
4. **Transfert des liens universels** : définissez `configuration.forwardUniversalLinks = true` dans la configuration du SDK Braze.

Pour plus de détails sur l'implémentation et des conseils de débogage, consultez [Branch pour la création de liens profonds]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking).