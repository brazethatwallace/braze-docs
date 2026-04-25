---
nav_title: "Liens universels et App Links"
article_title: "Liens universels et App Links"
page_order: 6.4
page_type: reference
description: "Cet article décrit comment configurer les liens universels Apple et les Android App Links."
channel: email
---

# Liens universels et App Links

> Cet article décrit comment configurer les liens universels Apple et les Android App Links.

{% alert tip %}
Pour une comparaison des types de liens sur tous les canaux de communication et des conseils sur les cas où un fichier AASA est nécessaire, consultez le [guide de création de liens profonds iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/).
{% endalert %}

Les liens universels Apple et les Android App Links sont des mécanismes conçus pour offrir une transition fluide entre le contenu web et les applications mobiles. Alors que les liens universels sont spécifiques à iOS, les Android App Links remplissent la même fonction pour les applications Android.

## Fonctionnement des liens universels et des App Links {#how-universal-links-and-app-links-work}

Les liens universels (iOS) et les App Links (Android) sont des liens web standard (`http://mydomain.com`) qui pointent à la fois vers une page web et vers un contenu à l'intérieur d'une application.

Lorsqu'un lien universel ou un App Link est ouvert, le système d'exploitation vérifie si une application installée est enregistrée pour ce domaine. Si une application est trouvée, elle est lancée immédiatement sans jamais charger la page web. Si aucune application n'est trouvée, l'URL web est chargée dans le navigateur web par défaut de l'utilisateur, qui peut également être configuré pour rediriger vers l'App Store ou le Google Play Store respectivement.

En d'autres termes, les liens universels permettent à un site web d'associer ses pages web à des écrans spécifiques de l'application, de sorte que lorsqu'un utilisateur clique sur un lien vers une page web correspondant à un écran de l'application, celle-ci peut être ouverte directement (si l'application est actuellement installée).

Ce tableau présente les principales différences entre les liens universels et les liens profonds traditionnels :

|                        | Liens universels et App Links                                  | Liens profonds                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilité des plateformes | iOS (version 9 et ultérieure) et Android (version 6.0 et ultérieure)  | Utilisés sur divers systèmes d'exploitation mobiles    |
| Objectif                | Lier de façon fluide le contenu web et applicatif sur les appareils iOS et Android | Lier vers un contenu spécifique de l'application |
| Fonction               | Dirige vers des pages web ou du contenu applicatif selon le contexte           | Ouvre des écrans spécifiques de l'application   |
| Installation de l'application       | Ouvre l'application si elle est installée, sinon ouvre le contenu web | Nécessite que l'application soit installée |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d'utilisation {#use-cases}

Les liens universels et les App Links sont le plus souvent utilisés pour les campagnes par e-mail, car les e-mails peuvent être ouverts et cliqués depuis des appareils de bureau et mobiles.

Certains canaux ne fonctionnent pas bien avec ces liens. Par exemple, les notifications push, les messages in-app et les Content Cards doivent utiliser des liens profonds basés sur un schéma (`mydomain://`).

{% alert note %}
Les Android App Links nécessitent un `IBrazeDeeplinkHandler` personnalisé avec une logique pour gérer les liens de leurs domaines séparément des autres URL web. Il peut être plus simple d'utiliser des liens profonds à la place et de maintenir des pratiques de liens uniformes pour les canaux autres que l'e-mail.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser les liens universels et les App Links :

- Votre site web doit être accessible via HTTPS
- Votre application doit être disponible sur l'App Store (iOS) ou le Google Play Store (Android)

## Configuration des liens universels et des App Links {#setting-up-universal-links-and-app-links}

Pour que les applications prennent en charge les liens universels ou les App Links, iOS et Android nécessitent tous deux qu'un fichier de permissions spécial soit hébergé sur le domaine du lien. Ce fichier contient les définitions des applications autorisées à ouvrir les liens de ce domaine et, pour iOS, les chemins que ces applications sont autorisées à ouvrir :

- **iOS :** fichier Apple App Site Association (AASA)
- **Android :** fichier Digital Asset Links

En plus de ce fichier de permissions, il existe des définitions codées en dur des domaines de liens que l'application est autorisée à ouvrir, configurées au sein de l'application :

- **iOS :** définis comme « Associated Domains » dans Xcode
- **Android :** définis dans le fichier `AndroidManifest.xml` de l'application

Cette association bidirectionnelle domaine-application est nécessaire pour qu'un lien universel ou un App Link fonctionne et empêche toute application de détourner les liens d'un domaine particulier ou tout domaine d'ouvrir une application particulière.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Ces étapes sont adaptées de la documentation développeur Apple. Pour plus d'informations, consultez [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Étape 1 : Configurer les droits de votre application

{% alert note %}
[Dans Xcode 13 et versions ultérieures](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), Xcode peut gérer automatiquement le provisionnement des droits pour vous. Vous pouvez probablement passer directement à l'[étape&nbsp;1c](#step-1c) et revenir à ces instructions en cas de problème.
{% endalert %}

#### Étape 1a : Enregistrer votre application {#step-1a}

1. Rendez-vous sur developer.apple.com et connectez-vous.
2. Cliquez sur **Certificates, Identifiers & Profiles**.
3. Cliquez sur **Identifiers**.
4. Si vous n'avez pas encore d'identifiant d'application enregistré, cliquez sur + pour en créer un.
   a. Saisissez un **Name**. Vous pouvez choisir ce que vous voulez.
   b. Saisissez le **Bundle ID**. Vous pouvez trouver votre identifiant de bundle dans l'onglet **General** de votre projet Xcode pour la cible de build appropriée.

#### Étape 1b : Activer les Associated Domains dans votre identifiant d'application

1. Dans votre identifiant d'application existant ou nouvellement créé, localisez la section **App Services**.
2. Sélectionnez **Associated Domains**.
3. Cliquez sur **Save**.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Étape 1c : Activer les Associated Domains dans votre projet Xcode {#step-1c}

Avant de continuer, assurez-vous que votre projet Xcode a la même équipe sélectionnée que celle où vous venez d'enregistrer votre identifiant d'application.

1. Dans Xcode, accédez à l'onglet **Capabilities** de votre fichier de projet.
2. Activez **Associated Domains**.

##### Conseil de résolution des problèmes

Si vous voyez l'erreur « An App ID with Identifier 'your-app-id' is not available. Please enter a different string », procédez comme suit :

1. Vérifiez que vous avez sélectionné la bonne équipe.
2. Vérifiez que le Bundle ID ([étape 1a](#step-1a)) de votre projet Xcode correspond à celui utilisé pour enregistrer l'identifiant d'application.

#### Étape 1d : Ajouter le droit de domaine

Dans la section des domaines, ajoutez l'étiquette de domaine appropriée. Vous devez la préfixer avec `applinks:`. Dans ce cas, vous pouvez voir que nous avons ajouté `applinks:yourdomain.com`.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Étape 1e : Confirmer que le fichier de droits est inclus dans le build

Dans le navigateur de projet, assurez-vous que votre nouveau fichier de droits est sélectionné sous **Target Membership**.

Xcode devrait gérer cela automatiquement.

### Étape 2 : Configurer votre site web pour héberger le fichier AASA

Pour associer le domaine de votre site web à votre application native sur iOS, vous devez héberger le fichier Apple App Site Association (AASA) sur votre site web. Ce fichier constitue un moyen sécurisé de vérifier la propriété du domaine auprès d'iOS. Avant iOS 9, les développeurs pouvaient enregistrer n'importe quel schéma URI pour ouvrir leurs applications, sans aucune vérification. Cependant, avec l'AASA, ce processus est devenu beaucoup plus sécurisé et fiable.

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

- `appID` : construit en combinant le **Team ID** de votre application (rendez-vous sur `https://developer.apple.com/account/#/membership/` pour obtenir le Team ID) et le **Bundle Identifier**. Dans l'exemple ci-dessus, « JHGFJHHYX » est le Team ID et « com.facebook.ios » est le Bundle ID.
- `paths` : tableau de chaînes de caractères qui spécifie quels chemins sont inclus ou exclus de l'association. Vous pouvez utiliser `NOT` avant le chemin pour désactiver des chemins. Dans cet exemple, tous les liens de ce chemin iront vers le web au lieu d'ouvrir l'application. Vous pouvez utiliser `*` comme caractère générique pour activer tous les chemins d'un répertoire et `?` pour correspondre à un seul caractère (par exemple /archives/201?/ pour correspondre à tous les nombres de 2010 à 2019).

{% alert note %}
Ces chaînes de caractères sont sensibles à la casse et les chaînes de requête et les identifiants de fragment sont ignorés.
{% endalert %}

### Étape 3 : Héberger le fichier AASA sur votre domaine

Lorsque votre fichier AASA est prêt, vous pouvez l'héberger sur votre domaine soit à `https://<<yourdomain>>/apple-app-site-association`, soit à `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Téléversez le fichier `apple-app-site-association` sur votre serveur web HTTPS. Vous pouvez placer le fichier à la racine de votre serveur ou dans le sous-répertoire `.well-known`. N'ajoutez pas `.json` au nom du fichier.

{% alert important %}
iOS ne tentera de récupérer le fichier AASA que via une connexion sécurisée (HTTPS).
{% endalert %}

Lors de l'hébergement du fichier AASA, assurez-vous que le fichier respecte ces directives :

- Est servi via HTTPS.
- Utilise le type MIME `application/json`.
- Ne dépasse pas 128 Ko (exigence à partir d'iOS 9.3.1)

### Étape 4 : Préparer votre application pour gérer les liens universels

Lorsqu'un utilisateur appuie sur un lien universel sur un appareil iOS, l'appareil lance l'application et lui envoie un objet [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). L'application peut ensuite interroger l'objet NSUserActivity pour déterminer comment elle a été lancée.

Pour prendre en charge les liens universels dans votre application, suivez ces étapes :

1. Ajoutez un droit qui spécifie les domaines pris en charge par votre application.
2. Mettez à jour le délégué de votre application pour répondre de manière appropriée lorsqu'il reçoit l'objet NSUserActivity.

Dans Xcode, ouvrez la section **Associated Domains** dans l'onglet **Capabilities** et ajoutez une entrée pour chaque domaine pris en charge par votre application, préfixé par `applinks:`. Par exemple, `applinks:www.mywebsite.com`.

{% alert note %}
Apple recommande de limiter cette liste à un maximum de 20 à 30 domaines.
{% endalert %}

### Étape 5 : Tester votre lien universel

Ajoutez le lien universel à un e-mail et envoyez-le à un appareil de test. Coller un lien universel directement dans le champ URL de Safari ne provoquera pas l'ouverture automatique de l'application. Si vous faites cela, vous devrez tirer manuellement la page web vers le bas pour qu'une invite apparaisse en haut vous demandant d'ouvrir l'application correspondante.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Ces étapes sont adaptées de la documentation développeur Android. Pour plus d'informations, consultez [Add Android App Links](https://developer.android.com/training/app-links#add-app-links) et [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Les Android App Links nécessitent un `IBrazeDeeplinkHandler` personnalisé avec une logique pour gérer les liens de leurs domaines séparément des autres URL web. Il peut être plus simple d'utiliser des liens profonds à la place et de maintenir des pratiques de liens uniformes pour les canaux autres que l'e-mail.
{% endalert %}

### Étape 1 : Créer des liens profonds

Tout d'abord, vous devez créer des liens profonds pour votre application Android. Pour cela, ajoutez des [filtres d'intention](https://developer.android.com/guide/components/intents-filters) dans votre fichier `AndroidManifest.xml`. Le filtre d'intention doit inclure l'action `VIEW` et la catégorie `BROWSABLE`, ainsi que l'URL de votre site web dans l'élément data.

### Étape 2 : Associer votre application à votre site web

Vous devez associer votre application à votre site web en créant un fichier Digital Asset Links. Ce fichier doit être au format JSON et inclure des détails sur les applications Android pouvant ouvrir les liens vers votre site web. Il doit être placé dans le répertoire `.well-known` de votre site web.

### Étape 3 : Mettre à jour le fichier manifeste de votre application

Dans votre fichier `AndroidManifest.xml`, ajoutez un élément meta-data à l'intérieur de l'élément application. L'élément meta-data doit avoir un attribut `android:name` de « asset_statements » et un attribut `android:resource` qui pointe vers un fichier de ressources contenant un tableau de chaînes de caractères incluant l'URL de votre site web.

### Étape 4 : Préparer votre application pour gérer les liens profonds

Dans votre application Android, vous devez gérer les liens profonds entrants. Vous pouvez le faire en récupérant l'intent qui a démarré votre activité et en extrayant les données de celui-ci.

### Étape 5 : Tester vos liens profonds

Enfin, vous pouvez tester vos liens profonds. Envoyez-vous un lien via une application de messagerie ou un e-mail et cliquez dessus. Si tout est correctement configuré, cela devrait ouvrir votre application.

{% endtab %}
{% endtabs %}

## Liens universels, App Links et suivi des clics {#universal-links-app-links-and-click-tracking}

{% alert note %}
Les liens de suivi des clics sont généralement configurés dans le cadre de votre onboarding pour l'e-mail. Si cela n'a pas été effectué lors de l'onboarding client, contactez votre gestionnaire de compte pour obtenir de l'aide.
{% endalert %}

Nos partenaires d'envoi d'e-mails, SendGrid et SparkPost, utilisent des domaines de suivi des clics pour encapsuler tous les liens et inclure des paramètres d'URL pour le suivi des clics dans les e-mails Braze.

Par exemple, un lien comme `https://www.example.com` devient quelque chose comme `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Pour permettre aux liens d'e-mail avec suivi des clics de fonctionner comme des liens universels ou des App Links, vous devrez effectuer une configuration supplémentaire. Assurez-vous d'ajouter le domaine de suivi des clics (`links.email.example.com`) comme domaine que l'application est autorisée à ouvrir. De plus, le domaine de suivi des clics doit servir les fichiers AASA (iOS) ou Digital Asset Links (Android). Cela contribuera à garantir que les liens d'e-mail avec suivi des clics fonctionnent de façon fluide.

Si vous ne souhaitez pas que chaque lien de suivi des clics soit un lien universel ou un App Link, vous pouvez spécifier quels liens doivent être des liens universels en fonction du partenaire d'envoi d'e-mails. Consultez les sections suivantes pour plus de détails.

### SendGrid

Pour traiter un lien de suivi des clics SendGrid comme un lien universel :

1. Configurez vos valeurs AASA ou AndroidManifest pathPrefix pour ne traiter comme liens universels que les liens contenant `/uni/` dans le chemin d'URL.
2. Ajoutez l'attribut `universal="true"` à la balise d'ancrage (`<a>`) de votre lien. Cela modifie le chemin d'URL du lien encapsulé pour inclure `/uni/`.

{% alert note %}
Pour les e-mails AMP, cet attribut doit être data-universal="true".
{% endalert %}

Par exemple :

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. Assurez-vous que votre application est configurée pour gérer correctement les liens encapsulés. Consultez l'article de SendGrid sur la [résolution des liens de suivi des clics SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) et suivez les étapes correspondant à votre système d'exploitation. Cet article contient des exemples de code pour [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) et [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Avec cette configuration, les liens contenant `/uni/` dans le chemin d'URL fonctionneront comme des liens universels, tandis que tous les autres liens fonctionneront comme des liens web.

### SparkPost

Pour traiter un lien de suivi des clics SparkPost comme un lien universel, ajoutez l'attribut suivant dans la section Attributs de l'éditeur par glisser-déposer pour l'e-mail, ou modifiez manuellement le HTML du lien pour inclure l'attribut suivant dans la balise d'ancrage de votre lien : `data-msys-sublink="custom_path"`.

Ce chemin personnalisé vous permet de traiter sélectivement les URL contenant cette valeur comme un lien universel.

Par exemple :

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Ensuite, assurez-vous que votre application est configurée pour gérer correctement le chemin personnalisé. Consultez l'article de SparkPost sur l'[utilisation du suivi des clics SparkPost sur les liens profonds](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Cet article contient des exemples de code pour [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) et [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Désactiver le suivi des clics lien par lien {#turning-off-click-tracking-on-a-link-to-link-basis}

Vous pouvez désactiver le suivi des clics pour des liens spécifiques en ajoutant du code HTML à votre message e-mail pour l'éditeur HTML ou à un bloc HTML pour l'éditeur par glisser-déposer.

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

#### Éditeur par glisser-déposer

Lorsque vous utilisez l'éditeur d'e-mail par glisser-déposer, saisissez votre code HTML en tant qu'attribut personnalisé si votre lien est attaché à du texte, un bouton ou une image.

##### Attribut personnalisé pour un lien texte

#### SendGrid

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Name :** `clicktracking`
- **Value :** `off`

#### SparkPost

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Name :** `data-msys-clicktrack`
- **Value :** `0`

![Un attribut personnalisé pour un lien texte.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Attribut personnalisé pour un bouton ou une image

#### SendGrid

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Name :** `clicktracking`
- **Value :** `off`
- **Type :** Link

#### SparkPost

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Name :** `data-msys-clicktrack`
- **Value :** `0`
- **Type :** Link

![Un attribut personnalisé pour un bouton.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Résolution des problèmes liés aux liens universels avec suivi des clics {#troubleshooting-universal-links-with-click-tracking}

Si vos liens universels ne fonctionnent pas comme prévu dans vos e-mails, par exemple en redirigeant le destinataire de son application de messagerie vers le navigateur web avant de finalement rediriger vers l'application, consultez ces conseils pour résoudre les problèmes de configuration de vos liens universels.

#### Vérifier l'emplacement du fichier de liens

Assurez-vous que le fichier AASA (iOS) ou le fichier Digital Asset Links (Android) se trouve au bon emplacement :

- **iOS :** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android :** `https://click.tracking.domain/.well-known/assetlinks.json`

Il est important de s'assurer que ces fichiers sont toujours accessibles publiquement. Si vous ne pouvez pas y accéder, vous avez peut-être manqué une étape dans la configuration des liens universels pour l'e-mail.

#### Vérifier les définitions de domaines

Assurez-vous que les définitions des domaines que votre application est autorisée à ouvrir sont correctes.

- **iOS :** vérifiez les Associated Domains configurés dans Xcode pour votre application ([étape 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)). Vérifiez que le domaine de suivi des clics est inclus dans cette liste.
- **Android :** ouvrez la page d'informations de l'application (appui long sur l'icône de l'application et cliquez sur ⓘ). Dans le menu d'informations de l'application, localisez **Ouvrir par défaut** et appuyez dessus. Cela devrait afficher un écran avec tous les liens vérifiés que l'application est autorisée à ouvrir. Vérifiez que le domaine de suivi des clics est inclus dans cette liste.