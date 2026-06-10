---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des notifications push
page_order: 5
page_type: reference
description: "Cette page contient des étapes de résolution des problèmes pour divers problèmes liés au canal de communication des notifications push."
channel: push
---

# Résolution des problèmes des notifications push {#troubleshoot-push}

> Utilisez cette page pour résoudre les problèmes liés au canal de communication des notifications push.

## Notifications push manquantes {#missing-push-notifications}

Vous rencontrez des difficultés de distribution avec les notifications push ? Voici un certain nombre d'étapes que vous pouvez suivre pour résoudre ce problème en vérifiant :

- [Le statut d'abonnement aux notifications push](#push-subscription-status)
- [Le segment](#segment)
- [Les plafonds de notifications push](#push-notification-caps)
- [Les limites de débit](#rate-limits)
- [Le statut du groupe de contrôle](#control-group-status)
- [Le jeton de notification push valide](#valid-push-token)
- [Le type de notification push](#push-notification-type)
- [L'application actuelle](#current-app)

#### Statut d'abonnement aux notifications push {#push-subscription-status}

Les notifications push ne peuvent être envoyées qu'aux utilisateurs abonnés ou ayant donné leur consentement explicite. Vérifiez votre profil utilisateur dans l'onglet [Engagement]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) de la section **User Profile** pour confirmer que vous êtes bien enregistré pour les notifications push dans l'espace de travail que vous testez. Si vous êtes enregistré pour plusieurs applications, elles apparaîtront dans le champ **Push Registered For** :

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

Vous pouvez également exporter les profils utilisateurs à l'aide des endpoints d'exportation de Braze :
- [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [Utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

Ces deux endpoints renvoient un objet de jeton de notification push qui inclut les informations d'activation des notifications push par appareil.

#### Segment {#segment}

Assurez-vous que vous faites partie du segment que vous ciblez (s'il s'agit d'une campagne en production et non d'un test). Dans le **User Profile**, vous verrez la liste des segments auxquels l'utilisateur appartient actuellement. N'oubliez pas qu'il s'agit d'une variable en constante évolution, car la segmentation est mise à jour en temps réel.

![List of Segments]({% image_buster /assets/img_archive/trouble2.png %})

Vous pouvez également confirmer que l'utilisateur fait partie du segment en utilisant **User Lookup** lors de la création d'un segment. **User Lookup** n'accepte que les `external_id` ou `braze_id`, pas les adresses e-mail ni les numéros de téléphone. Pour effectuer une recherche par e-mail, téléphone, jeton de notification push ou alias d'utilisateur, utilisez [**Rechercher des utilisateurs**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/).

![Section User Lookup avec un champ de recherche.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Plafonds de notifications push {#push-notification-caps}

Vérifiez les limites de fréquence globales. Il est possible que vous n'ayez pas reçu la notification push parce que votre espace de travail dispose d'une limite de fréquence globale et que vous avez déjà atteint votre plafond de notifications push pour la période spécifiée.

Vous pouvez vérifier cela en consultant la [limite de fréquence globale]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#freq-cap-feat-over) dans le tableau de bord. Si la campagne est configurée pour respecter les règles de limite de fréquence, un certain nombre d'utilisateurs seront impactés par ces paramètres.

![Campaign Details]({% image_buster /assets/img_archive/trouble3.png %})

#### Limites de débit {#rate-limits}

Si vous avez défini une limite de débit pour votre campagne ou Canvas, il est possible que vous ne receviez pas le message en raison du dépassement de cette limite. Pour plus d'informations, consultez [Limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#rate-limiting).

#### Statut du groupe de contrôle {#control-group-status}

S'il s'agit d'une campagne à canal unique ou d'un Canvas avec un groupe de contrôle, il est possible que vous fassiez partie du groupe de contrôle.

  1. Vérifiez la [distribution des variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/#step-5-distribute-users-among-your-variants) pour voir s'il existe un groupe de contrôle.
  2. Si c'est le cas, créez un segment filtrant par [dans le groupe de contrôle de la campagne]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), puis [exportez le segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/#exporting-to-csv) et vérifiez si votre ID utilisateur figure dans cette liste.

#### Jeton de notification push valide {#valid-push-token}
Un jeton de notification push est un identifiant que les expéditeurs utilisent pour cibler des appareils spécifiques avec une notification push. Ainsi, si l'appareil ne dispose pas d'un jeton de notification push valide, il n'y a aucun moyen de lui envoyer une notification push.

#### Type de notification push {#push-notification-type}

Vérifiez que vous utilisez le bon type de notification push. Par exemple, si vous souhaitez cibler un FireTV, vous devez utiliser une notification push Kindle, et non une campagne push Android. De même, si vous souhaitez cibler un appareil Android, utilisez une notification push Android et non une campagne push iOS. Consultez les articles suivants pour en savoir plus sur le flux de travail Braze pour :
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Application actuelle {#current-app}

Lorsque vous testez l'envoi de notifications push avec des utilisateurs internes, assurez-vous que l'utilisateur qui doit recevoir la notification push est actuellement connecté à l'application concernée. Cela peut amener l'utilisateur à ne pas recevoir de notification push ou à recevoir une notification push pour laquelle vous pensez qu'il n'est pas segmenté.

{% alert note %}
Si vous envoyez des notifications push avec des images sur Android, FCM peut parfois ignorer l'image et n'afficher que le texte dans la notification push. Ce problème est généralement causé par des problèmes de connectivité au serveur.
{% endalert %}

## Erreur : MismatchSenderID {#error-mismatchsenderid}

MismatchSenderID indique un échec d'authentification avec Firebase Cloud Messaging (FCM). Confirmez que votre Firebase sender ID et votre clé API FCM sont corrects.

Pour trouver la bonne clé serveur Firebase et la remplacer :

1. Accédez à la console Firebase de votre application.
2. Sous **Project Overview**, sélectionnez **Project Settings**.
3. Dans l'onglet **Cloud Messaging**, vérifiez que le Sender ID sous les clés API correspond à celui dans Braze (dans **Paramètres** > **Paramètres des applications** > **Cloud Messaging API Key**).

{% alert warning %}
Ne modifiez pas votre Sender ID dans votre tableau de bord de Braze. Cela invaliderait les enregistrements push existants. Si le Sender ID ne correspond pas, vous devez trouver votre projet Firebase avec le Sender ID correspondant.
{% endalert %}

{:start="4"}
4. Copiez la **Server Key** sous **Project credentials**.
5. Dans Braze, accédez à **Paramètres** > **Paramètres des applications**, sélectionnez votre application et collez la clé serveur dans le champ **Cloud Messaging API Key** (en remplaçant la clé obsolète).
6. Sélectionnez **Enregistrer**.
7. Pour vérifier, envoyez une notification push de test à un appareil avant et après avoir changé la clé API sans ouvrir l'application. Cela permet de confirmer que les utilisateurs continuent de recevoir des notifications push sans qu'un nouvel ID d'enregistrement push (jeton de notification push) ne doive être généré.

## Scénarios de résolution des problèmes {#troubleshooting-scenarios}

### Notifications push retardées {#delayed-push-notifications}

Vos notifications push peuvent être retardées pour les raisons suivantes :

- Une connexion de données faible sur l'appareil
- Du code personnalisé dans l'application qui peut supprimer les notifications push de Braze
- Les préférences de l'utilisateur pour les notifications push dans les paramètres de l'appareil
- La priorité du message de la notification push lors de la création dans la campagne ou le Canvas
- Des retards de trafic ou des problèmes avec les fournisseurs de services push (FCM et APNs)

### Les notifications push s'envoient plus lentement que prévu {#push-notifications-are-sending-slower-than-expected}

Assurez-vous que la configuration de vos notifications push suit ces bonnes pratiques :

- Si vous envoyez à de larges audiences sans tenir compte du statut d'activation des notifications push, cela peut entraîner une vitesse d'envoi plus lente. Envisagez plutôt d'envoyer uniquement aux utilisateurs ayant les notifications push activées pour réduire la taille de votre audience.
- Si possible, essayez de planifier vos campagnes à l'avance plutôt que de les envoyer immédiatement.
- Si vous ciblez un grand nombre d'utilisateurs avec des notifications push dans un Canvas, vous pouvez anticiper que les étapes de message suivantes dans le Canvas nécessiteront des temps de traitement différents de ceux d'une campagne qui envoie aux utilisateurs immédiatement. Dans ce cas, les campagnes termineraient généralement l'envoi avant un Canvas, car la première « étape » d'un Canvas consiste à vérifier si les utilisateurs sont éligibles au parcours utilisateur spécifique.

## Cliquer sur une notification push n'ouvre pas l'application {#clicking-a-push-notification-doesnt-open-the-app}

Si cliquer sur une notification push n'ouvre pas votre application, vérifiez les points suivants en fonction de votre plateforme.

### Android

1. **Vérifiez le comportement au clic :** Confirmez que la campagne est configurée pour ouvrir l'application lorsqu'on clique dessus.
2. **Vérifiez la gestion des liens profonds :** Dans votre fichier `braze.xml`, vérifiez si `com_braze_handle_push_deep_links_automatically` est défini sur `true` ou `false`.
   - S'il est défini sur `true`, le SDK Braze gère les liens profonds directement et l'application devrait s'ouvrir comme prévu.
   - S'il est défini sur `false`, votre application a besoin d'un récepteur de diffusion pour écouter et gérer les intentions de réception et d'ouverture des notifications push. Vérifiez que ce récepteur est correctement implémenté.
3. **Collectez les journaux détaillés :** [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/), reproduisez le problème et fournissez les journaux ainsi que vos fichiers `braze.xml` et `AndroidManifest.xml` au support Braze.

### iOS

1. **Vérifiez le comportement au clic :** Confirmez que la campagne est configurée pour ouvrir l'application lorsqu'on clique dessus.
2. **Vérifiez l'intégration push :** La création de liens profonds depuis une notification push vers l'application est automatiquement gérée par l'[intégration push standard]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) de Braze. Confirmez que l'intégration est correctement implémentée, y compris toute gestion de délégué personnalisée.
3. **Collectez les journaux détaillés :** [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/), reproduisez le problème et fournissez les journaux au support Braze.

## Les clics sur les notifications push ouvrent de manière inattendue dans l'application {#push-clicks-unexpectedly-open-in-app}

Si les liens dans vos notifications push s'ouvrent de manière inattendue dans votre application au lieu de votre navigateur web, il peut y avoir un problème avec la configuration de votre campagne ou l'implémentation du SDK. Consultez ces étapes pour obtenir de l'aide.

### Vérifiez le comportement au clic {#verify-on-click-behavior}

Dans votre campagne ou étape Canvas, vérifiez que l'option **Open web URL inside mobile app** n'est pas sélectionnée. Si c'est le cas, désélectionnez-la et relancez.

![Champ « Comportement au clic » de la configuration d'une notification push défini sur « Open web URL » avec « Open web URL inside mobile app » décoché.]({% image_buster /assets/img/push_on_click.png %})

L'interaction par défaut pour le comportement au clic « Open web URL » diffère selon la version du SDK. Pour les versions du SDK iOS 2.29.0 et Android 2.0.0 et supérieures, cette option est sélectionnée par défaut et les URL web s'ouvrent dans une vue web au sein de l'application. Avant ces versions, cette option est désélectionnée par défaut et les URL web s'ouvrent dans le navigateur web par défaut de l'appareil.

Si ce n'est pas le problème, il peut y avoir un souci avec votre implémentation push.

### Revérifiez l'intégration push {#double-check-push-integration}

Si les liens dans vos notifications push s'ouvrent de manière inattendue dans l'application, cela peut être dû à des problèmes avec votre intégration de notifications push ou vos paramètres de personnalisation. Suivez ces étapes pour résoudre le problème :

1. **Examinez l'implémentation du délégué push :** Assurez-vous que le délégué push de Braze est correctement implémenté. Pour des instructions détaillées, consultez le guide d'intégration des notifications push pour votre [plateforme]({{site.baseurl}}/developer_guide/home/).
2. **Inspectez la gestion personnalisée des liens :** Vérifiez si l'application inclut une gestion personnalisée pour tous les liens `https://`. Les configurations personnalisées peuvent remplacer les comportements par défaut. Collaborez avec votre équipe de développement pour examiner et ajuster ces paramètres si nécessaire.
3. **Vérifiez l'enregistrement push iOS :** Pour iOS, revisitez l'étape 1 du guide d'intégration push sur l'[enregistrement des notifications push auprès d'APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Assurez-vous que votre objet délégué est assigné de manière synchrone avant que l'application ne termine son lancement. Cette étape doit être effectuée dans la méthode `application:didFinishLaunchingWithOptions:`.
4. **Testez votre intégration :** Après avoir effectué les ajustements, testez le comportement des notifications push sur les appareils iOS et Android pour confirmer que le problème est résolu.

### Liens profonds avec l'application toujours en arrière-plan (iOS) {#deep-links-with-app-still-running-in-the-background-ios}

Si les liens profonds fonctionnent lorsque l'application n'est pas en cours d'exécution ou lorsque le lien est utilisé directement, mais pas lorsque l'application est déjà en arrière-plan, le problème peut être lié à la façon dont l'application gère le lien. Vérifiez si vous utilisez des bibliothèques tierces qui utilisent le method swizzling. Nous recommandons de désactiver le swizzling, car cela peut causer des problèmes avec les implémentations de liens profonds.

## Migrer vers une clé d'authentification .p8 {#migrate-to-a-p8-authentication-key}

Les clés d'authentification Apple `.p8` sont l'approche requise pour les notifications push APNs dans Braze. Contrairement aux types de fichiers de certificat hérités, les clés `.p8` n'expirent pas et prennent en charge toutes vos applications sous une seule clé, éliminant ainsi le besoin de renouvellements annuels de certificats et réduisant le risque d'échecs de distribution des notifications push.

Si vous utilisez actuellement un certificat `.p12` ou `.pem`, migrez vers une clé `.p8` dès que possible. Pour les instructions sur la création et le téléchargement d'une clé `.p8`, consultez [Télécharger votre certificat push APNs]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift). Pour les recommandations d'Apple sur la génération d'une clé `.p8` depuis votre compte développeur, consultez [Communicate with APNs using authentication tokens](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

### Clés .p8 et certificats .p12 {#p8-keys-versus-p12-certificates}

| Identifiant | Expiration | Indicateur de statut dans le tableau de bord |
| --- | --- | --- |
| Clé d'authentification `.p8` | N'expire pas | Pas d'indicateur de statut vert (c'est normal) |
| Certificat push `.p12` | Expire chaque année | Indicateur vert lorsque le certificat est valide |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Clés .p8 et certificats .p12" }

Lorsque vous remplacez un certificat `.p12` par une clé `.p8` (ou téléchargez un nouvel identifiant), la distribution des notifications push peut être brièvement interrompue pendant que Braze traite le changement. Planifiez les mises à jour pendant une fenêtre de maintenance si possible.

Dans **Paramètres** > **Paramètres des applications** > **Paramètres des notifications push**, confirmez que l'**App Bundle ID**, le **Team ID** et le **Key ID** (pour les clés `.p8`) correspondent aux valeurs de votre compte Apple Developer. Plusieurs espaces de travail Braze peuvent utiliser le même identifiant push Apple lorsque le **bundle ID** de l'application iOS est identique ; l'environnement de l'identifiant (développement ou production) doit correspondre à la façon dont l'application a été compilée.

Les applications utilisant le [SDK Swift Braze 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) ou version ultérieure peuvent utiliser la [gestion dynamique de la passerelle APNs]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#dynamic-apns-gateway-management), qui achemine automatiquement les jetons vers le bon environnement APNs.

## Les notifications push web ne fonctionnent pas comme prévu {#web-push-notifications-arent-behaving-as-expected}

Si vous rencontrez des problèmes avec les notifications push dans votre navigateur, vous devrez peut-être réinitialiser les autorisations de notification de votre site et effacer le stockage de votre site. Consultez ces étapes pour obtenir de l'aide.

{% tabs %}
{% tab Chrome %}

### Réinitialiser Chrome sur ordinateur {#reset-chrome-on-desktop}

1. À côté de votre URL dans le navigateur Chrome, sélectionnez l'icône de curseur **View Site Information**.
2. Sous **Notifications**, sélectionnez **Reset permission**.
3. Ouvrez Chrome DevTools. Voici les raccourcis pertinents par système d'exploitation.

<style>
table {
    max-width: 50%;
}
</style>

| OS      | Raccourcis clavier                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réinitialiser Chrome sur ordinateur" }

{:start="4"}
4. Dans DevTools, accédez à l'onglet **Application**.
5. Dans la barre latérale, sélectionnez **Storage**.
6. Sélectionnez **Clear site data**.
7. Chrome vous invitera à recharger la page pour appliquer vos paramètres mis à jour. Sélectionnez **Reload**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

### Réinitialiser Chrome sur Android {#reset-chrome-on-android}

Si vous avez une notification de votre site visible dans le tiroir de notifications Android :

1. Depuis la notification push, appuyez sur <i class="fas fa-cog" title="Paramètres"></i> et sélectionnez **Site settings**.
2. Depuis **Site settings**, appuyez sur **Clear & Reset**.

Si vous n'avez pas de notification de votre site ouverte :

1. Ouvrez Chrome sur Android.
2. Appuyez sur le menu <i class="fas fa-ellipsis-vertical"></i>.
3. Accédez à **Settings** > **Site Settings** > **Notifications**.
4. Vérifiez que les notifications sont définies sur **Ask before sending (recommended)**.
5. Trouvez votre site dans la liste.
6. Sélectionnez l'entrée et appuyez sur **Clear and Reset**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

{% endtab %}
{% tab Firefox %}

### Réinitialiser Firefox sur ordinateur {#reset-firefox-on-desktop}

1. À côté de l'URL de votre site, sélectionnez <i class="fa-solid fa-circle-info" alt="icône d'information"></i> ou <i class="fas fa-lock" alt="icône de cadenas"></i>.
2. Sous **Permissions**, à côté de **Receive Notifications**, sélectionnez <i class="fa-solid fa-circle-xmark" title="Effacer cette autorisation et redemander"></i> pour effacer les autorisations de notification.
3. Dans le même menu, sélectionnez **Clear Cookies and Site Data**.
4. Dans la boîte de dialogue pour confirmer votre choix, sélectionnez **OK**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

### Réinitialiser Firefox sur Android {#reset-firefox-on-android}

Pour réinitialiser les autorisations push sur Android, consultez cet [article du support Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Réinitialiser Safari sur macOS {#reset-safari-on-macos}

{% alert note %}
Ces étapes sont uniquement pour macOS, car Apple ne prend pas en charge le Web Push pour Safari sur Windows.
{% endalert %}

1. Ouvrez Safari.
2. Depuis la [barre de menus sur Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), accédez à **Safari** > **Settings** > **Websites** > **Notifications**.
3. Sélectionnez votre site dans la liste.
4. Sélectionnez **Remove** pour supprimer les autorisations de notification pour le site.
5. Ensuite, accédez à **Privacy** > **Manage Website Data**.
6. Sélectionnez votre site dans la liste.
7. Sélectionnez **Remove**, ou pour supprimer toutes les données du site, sélectionnez **Remove All**.
8. Sélectionnez **Done**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

{% endtab %}
{% endtabs %}

## Messages d'erreur push {#push-error-messages}

Pour des informations détaillées sur les messages d'erreur push courants (tels que `DEVICE_UNREGISTERED`, `Unregistered`, `NotRegistered` et autres), consultez [Messages d'erreur push courants]({{site.baseurl}}/user_guide/channels/push/push_error_codes/).

Vous avez encore besoin d'aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).