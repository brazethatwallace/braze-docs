---
nav_title: "Liens universels et App Links"
article_title: "Liens universels et App Links"
page_order: 6.4
page_type: reference
description: "Cet article décrit comment configurer les liens universels Apple et les Android App Links."
channel: email
---

# Liens universels et App Links {#universal-links-and-app-links}

> Cet article décrit comment configurer les liens universels Apple et les Android App Links.

{% alert tip %}
Pour une comparaison des types de liens sur tous les canaux de communication et des conseils sur les cas où un fichier AASA est nécessaire, consultez le [guide de création de liens profonds iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide).
{% endalert %}

Les liens universels Apple et les Android App Links sont des mécanismes conçus pour offrir une transition fluide entre le contenu web et les applications mobiles. Alors que les liens universels sont spécifiques à iOS, les Android App Links remplissent la même fonction pour les applications Android.

## Fonctionnement des liens universels et des App Links {#how-universal-links-and-app-links-work}

Les liens universels (iOS) et les App Links (Android) sont des liens web standards (`http://mydomain.com`) qui pointent à la fois vers une page web et vers un contenu à l'intérieur d'une application.

Lorsqu'un lien universel ou un App Link est ouvert, le système d'exploitation vérifie si une application installée est enregistrée pour ce domaine. Si une application est trouvée, elle est lancée immédiatement sans jamais charger la page web. Si aucune application n'est trouvée, l'URL web est chargée dans le navigateur web par défaut de l'utilisateur, qui peut également être configuré pour rediriger vers l'App Store ou le Google Play Store respectivement.

En clair, les liens universels permettent à un site web d'associer ses pages web à des écrans spécifiques de l'application, de sorte que lorsqu'un utilisateur clique sur un lien vers une page web correspondant à un écran de l'application, l'application peut être ouverte directement (si l'application est actuellement installée).

{% alert important %}
Firebase Dynamic Links est obsolète. Braze n'a pas d'intégration directe avec Firebase, et la création de liens profonds est gérée en dehors de la plateforme Braze. Migrez vers des solutions natives de plateforme (liens universels Apple et Android App Links, comme décrit dans cet article) ou vers des fournisseurs de services alternatifs de deep linking. Pour des conseils de migration, consultez la [FAQ de migration de Firebase](https://firebase.google.com/support/dynamic-links-faq).
{% endalert %}

Ce tableau présente les principales différences entre les liens universels et les deep links traditionnels :

|                        | Liens universels et App Links                                  | Deep links                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilité de plateforme | iOS (version 9 et ultérieure) et Android (version 6.0 et ultérieure)  | Utilisés sur divers systèmes d'exploitation mobiles    |
| Objectif               | Relier de façon fluide le contenu web et applicatif sur les appareils iOS et Android | Renvoyer vers un contenu spécifique de l'application |
| Fonction               | Dirige vers des pages web ou du contenu applicatif selon le contexte           | Ouvre des écrans spécifiques de l'application   |
| Installation de l'application       | Ouvre l'application si elle est installée, sinon ouvre le contenu web | Nécessite que l'application soit installée |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fonctionnement des liens universels et des App Links" }

## Cas d'usage {#use-cases}

Les liens universels et les App Links sont le plus souvent utilisés pour les campagnes par e-mail, car les e-mails peuvent être ouverts et consultés aussi bien sur ordinateur que sur appareil mobile.

Certains canaux ne fonctionnent pas bien avec ces liens. Par exemple, les notifications push, les messages in-app et les Content Cards doivent utiliser des deep links basés sur un schéma (`mydomain://`).

{% alert note %}
Les App Links Android nécessitent un `IBrazeDeeplinkHandler` personnalisé avec une logique permettant de gérer les liens provenant de leurs domaines séparément des autres URL web. Il peut être plus simple d'utiliser des deep links à la place et de conserver des pratiques de liens uniformes pour les canaux autres que l'e-mail.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser les liens universels et les App Links :

- Votre site web doit être accessible via HTTPS
- Votre application doit être disponible sur l'App Store (iOS) ou le Google Play Store (Android)

## Configuration des liens universels et des App Links {#setting-up-universal-links-and-app-links}

Pour que les applications prennent en charge les liens universels ou les App Links, iOS et Android nécessitent tous deux qu'un fichier de permissions spécial soit hébergé sur le domaine du lien. Ce fichier contient les définitions des applications autorisées à ouvrir les liens de ce domaine et, pour iOS, les chemins que ces applications sont autorisées à ouvrir :

- **iOS :** fichier Apple App Site Association (AASA)
- **Android :** fichier Digital Asset Links

En plus de ce fichier de permissions, des définitions codées en dur précisent quels domaines de lien l'application est autorisée à ouvrir, configurées au sein de l'application :

- **iOS :** défini comme « Associated Domains » dans Xcode
- **Android :** défini dans le fichier `AndroidManifest.xml` de l'application

Cette association bidirectionnelle domaine-application est nécessaire au fonctionnement d'un lien universel ou d'un App Link et empêche toute application de détourner les liens d'un domaine particulier ou tout domaine d'ouvrir une application particulière.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Ces étapes sont adaptées de la documentation développeur Apple. Pour plus d'informations, consultez [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Étape 1 : Configurer les droits de votre application {#step-1-configure-your-app-entitlements}

{% alert note %}
[À partir de Xcode 13](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), Xcode peut gérer automatiquement le provisionnement des droits pour vous. Vous pouvez probablement passer directement à l'[étape&nbsp;1c](#step-1c) et revenir à ces instructions en cas de problème.
{% endalert %}

#### Étape 1a : Enregistrer votre application {#step-1a}

1. Rendez-vous sur developer.apple.com et connectez-vous.
2. Cliquez sur **Certificates, Identifiers & Profiles**.
3. Cliquez sur **Identifiers**.
4. Si vous n'avez pas encore d'identifiant d'application enregistré, cliquez sur + pour en créer un.
   a. Saisissez un **Name**. Vous pouvez choisir ce que vous voulez.
   b. Saisissez le **Bundle ID**. Vous pouvez trouver votre bundle ID dans l'onglet **General** de votre projet Xcode pour la cible de build appropriée.

#### Étape 1b : Activer les Associated Domains dans votre identifiant d'application {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. Dans votre identifiant d'application existant ou nouvellement créé, localisez la section **App Services**.
2. Sélectionnez **Associated Domains**.
3. Cliquez sur **Save**.

![Section App Services]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Étape 1c : Activer les Associated Domains dans votre projet Xcode {#step-1c}

Avant de continuer, assurez-vous que votre projet Xcode utilise la même équipe que celle où vous venez d'enregistrer votre identifiant d'application.

1. Dans Xcode, accédez à l'onglet **Capabilities** de votre fichier de projet.
2. Activez **Associated Domains**.

##### Conseil de résolution des problèmes {#troubleshooting-tip}

Si vous voyez l'erreur « An App ID with Identifier 'your-app-id' is not available. Please enter a different string », procédez comme suit :

1. Vérifiez que vous avez sélectionné la bonne équipe.
2. Vérifiez que le Bundle ID ([étape 1a](#step-1a)) de votre projet Xcode correspond à celui utilisé pour enregistrer l'identifiant d'application.

#### Étape 1d : Ajouter le droit de domaine {#step-1d-add-the-domain-entitlement}

Dans la section des domaines, ajoutez l'étiquette de domaine appropriée. Vous devez la préfixer avec `applinks:`. Dans cet exemple, nous avons ajouté `applinks:yourdomain.com`.

![Section Associated Domains]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Étape 1e : Confirmer que le fichier de droits est inclus dans le build {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

Dans le navigateur de projet, assurez-vous que votre nouveau fichier de droits est sélectionné sous **Target Membership**.

Xcode devrait gérer cela automatiquement.

### Étape 2 : Configurer votre site web pour héberger le fichier AASA {#step-2-configure-your-website-to-host-the-aasa-file}

Pour associer le domaine de votre site web à votre application native sur iOS, vous devez héberger le fichier Apple App Site Association (AASA) sur votre site web. Ce fichier constitue un moyen sécurisé de vérifier la propriété du domaine auprès d'iOS. Avant iOS 9, les développeurs pouvaient enregistrer n'importe quel schéma d'URI pour ouvrir leurs applications, sans aucune vérification. Cependant, avec l'AASA, ce processus est devenu bien plus sécurisé et fiable.

Le fichier AASA contient un objet JSON avec une liste d'applications et les chemins d'URL du domaine qui doivent être inclus ou exclus en tant que liens universels. Voici un exemple de fichier AASA :

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID` : construit en combinant le **Team ID** de votre application (rendez-vous sur `https://developer.apple.com/account/#/membership/` pour obtenir le team ID) et le **Bundle Identifier**. Dans cet exemple, « JHGFJHHYX » est le team ID et « com.facebook.ios » est le bundle ID.
- `paths` : tableau de chaînes de caractères qui spécifie les chemins inclus ou exclus de l'association. Vous pouvez utiliser `NOT` avant le chemin pour désactiver certains chemins. Dans cet exemple, tous les liens de ce chemin mèneront vers le web au lieu d'ouvrir l'application. Vous pouvez utiliser `*` comme caractère générique pour activer tous les chemins d'un répertoire et `?` pour correspondre à un seul caractère (par exemple /archives/201?/ pour correspondre à tous les nombres de 2010 à 2019).

{% alert note %}
Ces chaînes de caractères sont sensibles à la casse et les chaînes de requête ainsi que les identifiants de fragment sont ignorés.
{% endalert %}

### Étape 3 : Héberger le fichier AASA sur votre domaine {#step-3-host-the-aasa-file-on-your-domain}

Lorsque votre fichier AASA est prêt, vous pouvez l'héberger sur votre domaine à l'adresse `https://<<yourdomain>>/apple-app-site-association` ou `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Téléversez le fichier `apple-app-site-association` sur votre serveur web HTTPS. Vous pouvez placer le fichier à la racine de votre serveur ou dans le sous-répertoire `.well-known`. N'ajoutez pas `.json` au nom du fichier.

{% alert important %}
iOS tentera uniquement de récupérer le fichier AASA via une connexion sécurisée (HTTPS).
{% endalert %}

Lors de l'hébergement du fichier AASA, assurez-vous que le fichier respecte les directives suivantes :

- Est servi via HTTPS.
- Utilise le type MIME `application/json`.
- Ne dépasse pas 128 Ko (exigence à partir d'iOS 9.3.1)

### Étape 4 : Préparer votre application à gérer les liens universels {#step-4-prepare-your-app-to-handle-universal-links}

Lorsqu'un utilisateur appuie sur un lien universel sur un appareil iOS, l'appareil lance l'application et lui envoie un objet [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). L'application peut ensuite interroger l'objet NSUserActivity pour déterminer comment elle a été lancée.

Pour prendre en charge les liens universels dans votre application, suivez les étapes suivantes :

1. Ajoutez un droit qui spécifie les domaines pris en charge par votre application.
2. Mettez à jour le délégué de votre application pour répondre de manière appropriée lorsqu'il reçoit l'objet NSUserActivity.

Dans Xcode, ouvrez la section **Associated Domains** dans l'onglet **Capabilities** et ajoutez une entrée pour chaque domaine pris en charge par votre application, préfixée par `applinks:`. Par exemple, `applinks:www.mywebsite.com`.

{% alert note %}
Apple recommande de limiter cette liste à un maximum de 20 à 30 domaines.
{% endalert %}

### Étape 5 : Tester votre lien universel {#step-5-test-your-universal-link}

Ajoutez le lien universel dans un e-mail et envoyez-le à un appareil de test. Coller un lien universel directement dans le champ URL de Safari ne provoquera pas l'ouverture automatique de l'application. Si vous faites cela, vous devrez tirer manuellement le site web vers le bas pour qu'une invite apparaisse en haut vous demandant d'ouvrir l'application correspondante.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Ces étapes sont adaptées de la documentation développeur Android. Pour plus d'informations, consultez [Add Android App Links](https://developer.android.com/training/app-links#add-app-links) et [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Les Android App Links nécessitent un `IBrazeDeeplinkHandler` personnalisé avec une logique pour gérer les liens de leurs domaines séparément des autres URL web. Il peut être plus simple d'utiliser des deep links à la place et de maintenir des pratiques de liaison uniformes pour les canaux autres que l'e-mail.
{% endalert %}

### Étape 1 : Créer des deep links {#step-1-create-deep-links}

Tout d'abord, vous devez créer des deep links pour votre application Android. Pour ce faire, ajoutez des [filtres d'intention](https://developer.android.com/guide/components/intents-filters) dans votre fichier `AndroidManifest.xml`. Le filtre d'intention doit inclure l'action `VIEW` et la catégorie `BROWSABLE`, ainsi que l'URL de votre site web dans l'élément data.

### Étape 2 : Associer votre application à votre site web {#step-2-associate-your-app-with-your-website}

Vous devez associer votre application à votre site web. Pour ce faire, créez un fichier Digital Asset Links. Ce fichier doit être au format JSON et contenir les informations sur les applications Android autorisées à ouvrir les liens vers votre site web. Il doit être placé dans le répertoire `.well-known` de votre site web.

### Étape 3 : Mettre à jour le fichier manifest de votre application {#step-3-update-your-app-manifest-file}

Dans votre fichier `AndroidManifest.xml`, ajoutez un élément meta-data à l'intérieur de l'élément application. L'élément meta-data doit avoir un attribut `android:name` de « asset_statements » et un attribut `android:resource` qui pointe vers un fichier de ressources contenant un tableau de chaînes de caractères incluant l'URL de votre site web.

### Étape 4 : Préparer votre application à gérer les deep links {#step-4-prepare-your-app-to-handle-deep-links}

Dans votre application Android, vous devez gérer les deep links entrants. Pour ce faire, récupérez l'intention qui a démarré votre activité et extrayez-en les données.

### Étape 5 : Tester vos deep links {#step-5-testing-your-deep-links}

Enfin, vous pouvez tester vos deep links. Envoyez-vous un lien via une application de messagerie ou un e-mail et cliquez dessus. Si tout est correctement configuré, votre application devrait s'ouvrir.

{% endtab %}
{% endtabs %}

## Liens universels, App Links et suivi des clics {#universal-links-app-links-and-click-tracking}

{% alert note %}
Les liens de suivi des clics sont généralement configurés dans le cadre de votre onboarding pour l'e-mail. Si cela n'a pas été effectué lors de l'onboarding client, contactez votre gestionnaire de compte pour obtenir de l'aide.
{% endalert %}

Nos partenaires d'envoi d'e-mails utilisent des domaines de suivi des clics pour envelopper tous les liens et inclure des paramètres d'URL pour le suivi des clics dans les e-mails Braze.

Par exemple, un lien comme `https://www.example.com` devient quelque chose comme `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Pour permettre aux liens d'e-mail avec suivi des clics de fonctionner comme des liens universels ou des App Links, vous devrez effectuer une configuration supplémentaire. Assurez-vous d'ajouter le domaine de suivi des clics (`links.email.example.com`) comme domaine que l'application est autorisée à ouvrir. De plus, le domaine de suivi des clics doit servir les fichiers AASA (iOS) ou Digital Asset Links (Android). Cela garantira que les liens d'e-mail avec suivi des clics fonctionnent de façon fluide.

Si vous ne souhaitez pas que chaque lien de suivi des clics soit un lien universel ou un App Link, vous pouvez spécifier quels liens doivent être des liens universels en fonction du partenaire d'envoi d'e-mails. Consultez les onglets suivants pour plus de détails.

{% tabs %}
{% tab SendGrid %}

Pour traiter un lien de suivi des clics SendGrid comme un lien universel :

1. Configurez vos valeurs AASA ou AndroidManifest pathPrefix pour ne traiter comme liens universels que les liens contenant `/uni/` dans le chemin d'URL.
2. Ajoutez l'attribut `universal="true"` à la balise d'ancrage (`<a>`) de votre lien. Cela modifie le chemin d'URL du lien enveloppé pour inclure `/uni/`.

{% alert note %}
Pour les e-mails AMP, cet attribut doit être data-universal="true".
{% endalert %}

Par exemple :

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. Assurez-vous que votre application est configurée pour gérer correctement les liens enveloppés. Consultez l'article de SendGrid sur la [résolution des liens de suivi des clics SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) et suivez les étapes correspondant à votre système d'exploitation. Cet article contient des exemples de code pour [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) et [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Avec cette configuration, les liens contenant `/uni/` dans le chemin d'URL fonctionneront comme des liens universels, tandis que tous les autres liens fonctionneront comme des liens web.

{% endtab %}
{% tab SparkPost %}

Pour traiter un lien de suivi des clics SparkPost comme un lien universel, ajoutez l'attribut suivant dans la section Attributs de l'éditeur par glisser-déposer pour les e-mails, ou modifiez manuellement le HTML du lien pour inclure l'attribut suivant dans la balise d'ancrage de votre lien : `data-msys-sublink="custom_path"`.

Ce chemin personnalisé vous permet de traiter sélectivement les URL contenant cette valeur comme un lien universel.

Par exemple :

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Ensuite, assurez-vous que votre application est configurée pour gérer correctement le chemin personnalisé. Consultez l'article de SparkPost sur l'[utilisation du suivi des clics SparkPost sur les deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Cet article contient des exemples de code pour [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) et [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

{% endtab %}
{% tab Amazon SES %}

Utilisez des chemins personnalisés pour ajouter des segments de chemin aux URL de suivi des clics d'e-mail. Cela crée des modèles d'URL prévisibles que les systèmes d'exploitation mobiles peuvent reconnaître pour les liens universels et les App Links.

Lorsque les utilisateurs appuient sur des liens d'e-mail sur des appareils mobiles, les chemins personnalisés vous aident à contrôler si les liens s'ouvrent dans votre application mobile principale, une application spécialisée ou le navigateur mobile (par exemple, pages produits, programmes de fidélité, liens de désabonnement ou pages juridiques).

Pour traiter un lien de suivi des clics Amazon SES comme un lien universel ou un App Link :

1. Ajoutez des attributs `ses:custom-path` à vos balises d'ancrage dans le HTML de l'e-mail, ou ajoutez l'attribut dans la section **Attributs** de l'éditeur par glisser-déposer pour les e-mails. Le chemin personnalisé est inséré dans l'URL de suivi des clics enveloppée.

Par exemple :

```html
<!-- Opens main shopping app -->
<a href="https://yourstore.com/product" ses:custom-path="shop">Shop Now</a>
<!-- Opens loyalty app -->
<a href="https://yourstore.com/rewards" ses:custom-path="rewards">My Rewards</a>
<!-- Opens specialized app -->
<a href="https://yourstore.com/limited" ses:custom-path="limited">Limited Edition</a>
<!-- Stays in browser -->
<a href="https://yourstore.com/unsubscribe" ses:no-track>Unsubscribe</a>
```

Assurez-vous que vos chemins personnalisés respectent ces exigences :

- **Format :** caractères alphanumériques, points, tirets bas et tirets uniquement
- **Longueur :** 1 à 32 caractères
- **Sensibilité à la casse :** les chemins sont sensibles à la casse pour correspondre aux exigences des systèmes d'exploitation mobiles

{:start="2"}
2. Vérifiez que vos URL de suivi enveloppées incluent le segment de chemin personnalisé. Les liens suivent ce format : `track.yourstore.com/L1/{customPath}/...`

Par exemple :

- `track.yourstore.com/L1/shop/...`
- `track.yourstore.com/L1/rewards/...`

{:start="3"}
3. Configurez vos fichiers d'association de site sur votre domaine de suivi des clics afin que les chemins correspondent à `/L1/{customPath}/`.

**iOS (Apple App Site Association) :**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/L1/shop/*", "/L1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/L1/limited/*"]
    }]
  }
}
```

**Android (Digital Asset Links) :**

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourcompany.mainapp",
    "sha256_cert_fingerprints": ["..."]
  },
  "include": ["/L1/shop/*", "/L1/rewards/*"]
}]
```

Assurez-vous que votre application est configurée pour gérer ces liens enveloppés. Ajoutez votre domaine de suivi des clics aux domaines associés de votre application (iOS) ou aux filtres d'intention (Android), et hébergez le fichier AASA ou Digital Asset Links sur ce domaine comme décrit précédemment dans cet article.

{% endtab %}
{% endtabs %}

### Désactiver le suivi des clics lien par lien {#turning-off-click-tracking-on-a-link-to-link-basis}

Vous pouvez désactiver le suivi des clics pour des liens spécifiques en ajoutant du code HTML à votre e-mail pour l'éditeur HTML ou à un bloc HTML pour l'éditeur par glisser-déposer.

#### SendGrid

Si votre fournisseur de services d'e-mailing est SendGrid, utilisez le code HTML `clicktracking=off` comme ceci :

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

Si votre fournisseur de services d'e-mailing est SparkPost, utilisez le code HTML `data-msys-clicktrack="0"` comme ceci :

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Si votre fournisseur de services d'e-mailing est Amazon SES, utilisez le code HTML `ses:no-track` comme ceci :

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Éditeur par glisser-déposer {#drag-and-drop-editor}

Lorsque vous utilisez l'éditeur d'e-mail par glisser-déposer, saisissez votre code HTML en tant qu'attribut personnalisé si votre lien est rattaché à du texte, un bouton ou une image.

##### Attribut personnalisé pour un lien texte {#custom-attribute-for-a-text-link}

#### SendGrid

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `clicktracking`
- **Valeur :** `off`

#### SparkPost

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `data-msys-clicktrack`
- **Valeur :** `0`

![Un attribut personnalisé pour un lien texte.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Attribut personnalisé pour un bouton ou une image {#custom-attribute-for-a-button-or-image}

#### SendGrid

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `clicktracking`
- **Valeur :** `off`
- **Type :** Link

#### SparkPost

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `data-msys-clicktrack`
- **Valeur :** `0`
- **Type :** Link

![Un attribut personnalisé pour un bouton.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Résolution des problèmes de liens universels avec suivi des clics {#troubleshooting-universal-links-with-click-tracking}

Si vos liens universels ne fonctionnent pas comme prévu dans vos e-mails, par exemple si le destinataire est redirigé depuis son application d'e-mail vers le navigateur web avant d'être finalement redirigé vers l'application, consultez ces conseils pour résoudre les problèmes de configuration de vos liens universels.

#### Outlook affiche `[?it=` ou du texte d'URL brut au lieu d'un bouton {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

Outlook peut afficher le texte d'appel à l'action sous la forme `[?it=` ou imprimer une partie du `href` lorsqu'un lien n'utilise pas un schéma d'URL valide **`http://` ou `https://`**. Les schémas personnalisés, les schémas manquants ou les URL malformées ne sont pas traités comme des hyperliens, de sorte que le client affiche le texte de l'attribut à la place. Vérifiez que chaque bouton, lien d'image et URL suivie utilise une destination complète `https://` (ou `http://`). Cela s'applique aussi bien aux liens universels qu'aux liens web standard.

#### Vérifier l'emplacement du fichier de liens {#verify-link-file-location}

Assurez-vous que le fichier AASA (iOS) ou le fichier Digital Asset Links (Android) se trouve au bon emplacement :

- **iOS :** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android :** `https://click.tracking.domain/.well-known/assetlinks.json`

Il est important de s'assurer que ces fichiers sont toujours accessibles publiquement. Si vous ne pouvez pas y accéder, vous avez peut-être manqué une étape dans la configuration des liens universels pour les e-mails.

#### Vérifier les définitions de domaines {#verify-domain-definitions}

Assurez-vous d'avoir les bonnes définitions pour les domaines que votre application est autorisée à ouvrir.

- **iOS :** vérifiez les domaines associés configurés dans Xcode pour votre application ([Étape 1c : activer les domaines associés dans votre projet Xcode]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links?tab=ios#step-1c)). Vérifiez que le domaine de suivi des clics est inclus dans cette liste.
- **Android :** ouvrez la page d'informations de l'application (appui long sur l'icône de l'application, puis cliquez sur ⓘ). Dans le menu d'informations de l'application, localisez **Ouvrir par défaut** et appuyez dessus. Un écran devrait s'afficher avec tous les liens vérifiés que l'application est autorisée à ouvrir. Vérifiez que le domaine de suivi des clics est inclus dans cette liste.

#### Tous les liens d'e-mail ouvrent l'application {#every-email-link-opens-the-app}

Si chaque lien d'un e-mail ouvre votre application, y compris les liens que vous vous attendiez à ouvrir dans un navigateur, les valeurs AASA `paths` (iOS) ou Android `pathPrefix` sur votre domaine de suivi des clics correspondent à l'ensemble du domaine (par exemple `*` ou `/*`).

Limitez ces modèles aux URL qui doivent ouvrir l'application. Pour SendGrid, faites correspondre `/uni/` et ajoutez `universal="true"` uniquement sur ces liens. Consultez [Liens universels, App Links et suivi des clics](#universal-links-app-links-and-click-tracking).

#### Le domaine de suivi ne peut pas servir les fichiers .well-known {#tracking-domain-cant-serve-well-known-files}

Dans certains cas, votre domaine de suivi des clics peut ne pas être en mesure d'héberger les fichiers `.well-known` requis en raison de limitations du fournisseur de services d'e-mailing ou de contraintes d'infrastructure. Si vous ne pouvez pas héberger le fichier AASA ou Digital Asset Links sur votre domaine de suivi, envisagez les options suivantes :

- **Désactiver sélectivement le suivi des clics sur les URL de deep links :** vous pouvez désactiver le suivi des clics pour des liens universels spécifiques afin qu'ils pointent directement vers votre domaine principal (où vous pouvez héberger le fichier AASA ou Digital Asset Links). Notez que cette méthode peut entraîner une perte de données analytiques de clics pour ces liens spécifiques. Consultez [Désactiver le suivi des clics lien par lien](#turning-off-click-tracking-on-a-link-to-link-basis) pour les instructions.
- **Placer un CDN devant le sous-domaine de suivi :** si vous avez besoin d'une couverture complète du suivi des clics et de la création de liens profonds, vous pouvez placer un CDN (tel que Cloudflare ou CloudFront) devant votre sous-domaine de suivi. Configurez le CDN pour servir les fichiers `.well-known` localement et rediriger tout le reste du trafic vers votre fournisseur de services d'e-mailing. Cette approche est plus complexe mais vous donne un contrôle total sur le suivi des clics et les liens universels.

#### Les liens fonctionnent dans un espace de travail mais pas dans un autre {#links-working-in-one-workspace-but-not-another}

Si les liens universels ou App Links fonctionnent correctement dans votre espace de travail de production mais échouent dans votre espace de travail de développement ou de test, vérifiez que le domaine de l'adresse e-mail d'envoi correspond au domaine de suivi configuré dans les paramètres e-mail de chaque espace de travail. Une configuration incohérente entre les espaces de travail peut amener les liens à se comporter différemment, même en utilisant les mêmes modèles d'e-mail et les mêmes fichiers AASA ou Digital Asset Links.

Pour vérifier votre configuration e-mail :

1. Accédez à **Paramètres** > **Préférences e-mail** dans le tableau de bord de Braze.
2. Consultez les **Paramètres d'e-mail sortant** sous **Configuration d'envoi**.
3. Vérifiez que votre domaine d'envoi et votre domaine de suivi sont correctement alignés pour l'espace de travail dans lequel les liens ne fonctionnent pas.

Si votre domaine d'envoi diffère entre les espaces de travail, assurez-vous que chaque espace de travail dispose des enregistrements DNS appropriés configurés et que vos fichiers AASA (iOS) ou Digital Asset Links (Android) sont accessibles depuis chaque domaine de suivi.