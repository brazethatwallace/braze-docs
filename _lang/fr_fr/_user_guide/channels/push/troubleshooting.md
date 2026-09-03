---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des notifications push
page_order: 5
page_type: reference
description: "Diagnostiquez les problèmes de distribution des notifications push, de comportement au clic et d'identifiants à l'aide d'un index des symptômes et d'un parcours d'investigation standard."
channel: push
---

# Résolution des problèmes des notifications push {#troubleshoot-push}

> Utilisez cette page pour résoudre les problèmes de distribution des notifications push, de comportement au clic et d'identifiants. Pour la configuration spécifique au SDK, consultez [Résolution des problèmes des notifications push pour le SDK Braze]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting). Pour les codes d'erreur, consultez [Messages d'erreur courants des notifications push]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

| Symptôme | Aller à |
| --- | --- |
| L'utilisateur n'a pas reçu de notification push | [Notifications push manquantes](#missing-push-notifications) |
| Les notifications push arrivent en retard | [Notifications push retardées](#delayed-push-notifications) |
| Les envois push sont plus lents que prévu | [Les notifications push s'envoient plus lentement que prévu](#push-notifications-are-sending-slower-than-expected) |
| Erreur `MismatchSenderID` (Android) | [Erreur : MismatchSenderID](#error-mismatch-sender-id) |
| Appuyer sur une notification push n'ouvre pas l'application | [Cliquer sur une notification push n'ouvre pas l'application](#clicking-a-push-notification-does-not-open-the-app) |
| Les liens push s'ouvrent dans l'application au lieu du navigateur | [Les clics push s'ouvrent de manière inattendue dans l'application](#push-clicks-unexpectedly-open-in-app) |
| Problèmes de permissions ou de distribution des notifications push Web | [Les notifications push Web ne fonctionnent pas comme prévu](#web-push-notifications-are-not-behaving-as-expected) |
| Besoin de migrer de `.p12` vers `.p8` (iOS) | [Migrer vers une clé d'authentification .p8](#migrate-to-a-p8-authentication-key) |
| Code d'erreur push spécifique dans les journaux | [Messages d'erreur push](#push-error-messages) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme push" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail lorsqu'un utilisateur ou un appareil de test n'a pas reçu de notification push. Commencez à l'étape 1.

1. Confirmez que l'utilisateur est abonné ou a opté pour les notifications push et qu'il dispose d'un jeton push valide dans l'onglet **Engagement** de son profil.
2. Confirmez que l'utilisateur fait partie de l'audience cible de la Campaign ou du Canvas au moment de l'envoi (les Segments se mettent à jour en temps réel).
3. Vérifiez les limites de fréquence globales, les limites de débit et l'affectation au groupe de contrôle pour la Campaign ou le Canvas.
4. Confirmez que vous utilisez le bon type de notification push pour l'appareil (par exemple, Android, iOS ou Kindle).
5. Pour les tests internes, confirmez que le testeur est connecté à la bonne application sur l'appareil.
6. Si la distribution échoue toujours, consultez les [Messages d'erreur push courants]({{site.baseurl}}/user_guide/channels/push/push_error_codes) ou contactez l'[Assistance Braze]({{site.baseurl}}/braze_support) en fournissant l'ID de la Campaign ou du Canvas, l'ID utilisateur et l'horodatage avec le fuseau horaire.

## Notifications push manquantes {#missing-push-notifications}

**Symptôme :** Un utilisateur n'a pas reçu une notification push attendue.

Si les notifications push n'arrivent pas comme prévu, vérifiez les points suivants :

- [Statut d'abonnement aux notifications push](#push-subscription-status)
- [Segment](#segment)
- [Plafonds de notifications push](#push-notification-caps)
- [Limites de débit](#rate-limits)
- [Statut du groupe de contrôle](#control-group-status)
- [Jeton de notification push valide](#valid-push-token)
- [Type de notification push](#push-notification-type)
- [Application actuelle](#current-app)

### Statut d'abonnement aux notifications push {#push-subscription-status}

Les notifications push ne peuvent être envoyées qu'aux utilisateurs abonnés ou ayant donné leur consentement explicite. Dans le **Profil utilisateur**, ouvrez l'onglet [Engagement]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) et confirmez que vous êtes bien enregistré pour les notifications push dans l'espace de travail que vous testez. Si vous êtes enregistré pour plusieurs applications, elles apparaissent dans le champ **Push Registered For** :

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

Vous pouvez également exporter les profils utilisateurs à l'aide des endpoints d'exportation de Braze :

- [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Ces deux endpoints renvoient un objet de jeton de notification push qui inclut les informations d'activation des notifications push par appareil.

### Segment {#segment}

Assurez-vous que vous faites partie du segment que vous ciblez (s'il s'agit d'une campagne en production et non d'un test). Dans le **Profil utilisateur**, vous pouvez voir les segments auxquels l'utilisateur appartient actuellement. L'appartenance aux segments est mise à jour en temps réel.

![Liste des segments]({% image_buster /assets/img_archive/trouble2.png %})

Vous pouvez également confirmer que l'utilisateur fait partie du segment en utilisant **User Lookup** lors de la création d'un segment. **User Lookup** n'accepte que les `external_id` ou `braze_id`, pas les adresses e-mail ni les numéros de téléphone. Pour effectuer une recherche par e-mail, téléphone, jeton de notification push ou alias d'utilisateur, consultez [**Rechercher des utilisateurs**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

![Section User Lookup avec un champ de recherche.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### Plafonds de notifications push {#push-notification-caps}

Vérifiez les limites de fréquence globales. Il est possible que vous n'ayez pas reçu la notification push parce que votre espace de travail utilise une limite de fréquence globale et que vous avez déjà atteint votre plafond de notifications push pour la période spécifiée.

Sur la page **Analytics** de la campagne, vérifiez la présence d'une bannière de limite de fréquence indiquant approximativement combien d'utilisateurs n'ont pas reçu la campagne au cours des 30 derniers jours. Pour examiner les envois individuels, utilisez le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) et filtrez par **Frequency capped**. Pour consulter ou modifier les règles, voir [limite de fréquence globale]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over).

![Détails de la campagne]({% image_buster /assets/img_archive/trouble3.png %})

### Limites de débit {#rate-limits}

Si vous avez défini une limite de débit pour votre campagne ou Canvas, il est possible que vous ne receviez plus de messages après avoir dépassé cette limite. Pour plus d'informations, consultez [Limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting).

### Statut du groupe de contrôle {#control-group-status}

S'il s'agit d'une campagne à canal unique ou d'un Canvas avec un groupe de contrôle, il est possible que vous fassiez partie du groupe de contrôle.

  1. Vérifiez la [distribution des variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-4-choose-a-segment-and-distribute-your-users-across-variants) pour voir s'il existe un groupe de contrôle.
  2. Si c'est le cas, créez un segment filtrant par [dans le groupe de contrôle de la campagne]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group), puis [exportez le segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details) et vérifiez si votre ID utilisateur figure dans cette liste.

### Jeton de notification push valide {#valid-push-token}

Un jeton de notification push est un identifiant que les expéditeurs utilisent pour cibler un appareil spécifique avec une notification push. Sans jeton de notification push valide, Braze ne peut pas envoyer de notification push à cet appareil.

Braze stocke jusqu'à 20 appareils par profil utilisateur. Lorsqu'un 21e appareil s'enregistre, l'appareil le plus ancien est supprimé (premier entré, premier sorti, ou FIFO). L'appel de [`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids) dans le SDK réenregistre l'appareil actuel sur le profil.

### Type de notification push {#push-notification-type}

Utilisez le type de notification push correspondant à l'appareil ou à la plateforme que vous ciblez. Par exemple, utilisez une notification push Kindle pour Fire TV, et non une campagne push Android. Pour les appareils Android, utilisez une notification push Android plutôt qu'une campagne push iOS.

Pour les flux de résolution des problèmes spécifiques à chaque plateforme, consultez :

- [Résolution des problèmes des notifications push Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Résolution des problèmes de Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

### Application actuelle {#current-app}

Lorsque vous testez les notifications push avec des utilisateurs internes, confirmez que le destinataire prévu est connecté à la bonne application. Sinon, il pourrait ne pas recevoir la notification push, ou recevoir une notification inattendue en raison de la segmentation.

{% alert note %}
Si vous envoyez des notifications push avec des images sur Android, FCM peut parfois ignorer l'image et n'afficher que le texte dans la notification push. Ce problème est généralement causé par des problèmes de connectivité au serveur.
{% endalert %}

## Erreur : MismatchSenderID {#error-mismatch-sender-id}

**Symptôme :** La notification push Android échoue avec une erreur `MismatchSenderID`.

MismatchSenderID indique un échec d'authentification avec Firebase Cloud Messaging (FCM). Vérifiez que votre identifiant d'expéditeur Firebase et votre clé API FCM sont corrects.

Pour trouver la bonne clé serveur Firebase et la remplacer :

1. Accédez à la console Firebase de votre application.
2. Sous **Aperçu du projet**, sélectionnez **Paramètres du projet**.
3. Dans l'onglet **Cloud Messaging**, vérifiez que l'identifiant d'expéditeur indiqué avec les clés API correspond à celui configuré dans Braze (dans **Paramètres** > **Paramètres de l'application** > **Clé API Cloud Messaging**).

{% alert warning %}
Ne modifiez pas votre identifiant d'expéditeur dans votre tableau de bord de Braze. Cela invaliderait les enregistrements push existants. Si l'identifiant d'expéditeur ne correspond pas, vous devez trouver votre projet Firebase avec l'identifiant d'expéditeur correspondant.
{% endalert %}

4. Copiez la **Clé serveur** sous **Identifiants du projet**.
5. Dans Braze, accédez à **Paramètres** > **Paramètres de l'application**, sélectionnez votre application, puis collez la clé serveur dans le champ **Clé API Cloud Messaging** (en remplaçant la clé obsolète).
6. Sélectionnez **Enregistrer**.
7. Pour vérifier, envoyez une notification push de test à un appareil avant et après avoir modifié la clé API sans ouvrir l'application. Cela permet de confirmer que les utilisateurs continuent de recevoir des notifications push sans qu'un nouvel identifiant d'enregistrement push (jeton push) ne doive être généré.

## Scénarios de résolution des problèmes {#troubleshooting-scenarios}

### Notifications push retardées {#delayed-push-notifications}

**Symptôme :** Les notifications push arrivent plus tard que prévu.

Vos notifications push peuvent être retardées pour les raisons suivantes :

- Une connexion de données faible sur l'appareil
- Du code personnalisé dans l'application qui peut supprimer les notifications push de Braze
- Les préférences de l'utilisateur pour les notifications push dans les paramètres de l'appareil
- La priorité du message de la notification push lors de la création dans la Campaign ou le Canvas
- Des retards de trafic ou des problèmes avec les fournisseurs de services push (FCM et APNs)

### Les notifications push s'envoient plus lentement que prévu {#push-notifications-are-sending-slower-than-expected}

**Symptôme :** Les envois push d'une Campaign ou d'un Canvas prennent plus de temps que prévu.

Vérifiez que la configuration de vos notifications push respecte ces bonnes pratiques :

- Si vous envoyez à de larges audiences sans tenir compte du statut d'activation des notifications push, cela peut entraîner une vitesse d'envoi plus lente. Envisagez plutôt d'envoyer uniquement aux utilisateurs ayant activé les notifications push afin de réduire la taille de votre audience.
- Si possible, essayez de planifier vos Campaigns à l'avance plutôt que de les envoyer immédiatement.
- Si vous ciblez un grand nombre d'utilisateurs avec des notifications push dans un Canvas, vous pouvez anticiper que les étapes de message suivantes dans le Canvas nécessiteront des temps de traitement différents par rapport à une Campaign qui envoie aux utilisateurs immédiatement. Dans ce cas, les Campaigns terminent généralement l'envoi avant un Canvas, car la première « étape » d'un Canvas consiste à vérifier si les utilisateurs sont éligibles au parcours utilisateur spécifique.

## Cliquer sur une notification push n'ouvre pas l'application {#clicking-a-push-notification-does-not-open-the-app}

**Symptôme :** Appuyer sur une notification push n'ouvre pas l'application et ne navigue pas comme configuré.

Si cliquer sur une notification push n'ouvre pas votre application, vérifiez les points suivants en fonction de votre plateforme.

### Android

1. **Vérifiez le comportement au clic :** Confirmez que la Campaign est configurée pour ouvrir l'application lorsqu'on clique dessus.
2. **Vérifiez la gestion des deep links :** Dans votre fichier `braze.xml`, vérifiez si `com_braze_handle_push_deep_links_automatically` est défini sur `true` ou `false`.
   - S'il est défini sur `true`, le SDK Braze gère les deep links directement et l'application devrait s'ouvrir comme prévu.
   - S'il est défini sur `false`, votre application a besoin d'un récepteur de diffusion pour écouter et gérer les intentions de notification push reçues et ouvertes. Vérifiez que ce récepteur est correctement implémenté.
3. **Collectez les journaux détaillés :** [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduisez le problème et fournissez les journaux ainsi que vos fichiers `braze.xml` et `AndroidManifest.xml` à l'assistance Braze.

### iOS

1. **Vérifiez le comportement au clic :** Confirmez que la Campaign est configurée pour ouvrir l'application lorsqu'on clique dessus.
2. **Vérifiez l'intégration push :** La création de liens profonds depuis une notification push vers l'application est automatiquement gérée par l'[intégration push standard]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift) de Braze. Confirmez que l'intégration est correctement implémentée, y compris toute gestion de délégué personnalisée.
3. **Collectez les journaux détaillés :** [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduisez le problème et fournissez les journaux à l'assistance Braze.

## Les clics sur les notifications push ouvrent de manière inattendue dans l'application {#push-clicks-unexpectedly-open-in-app}

**Symptôme :** Les liens dans les notifications push s'ouvrent dans l'application au lieu du navigateur web de l'appareil.

Si les liens dans vos notifications push s'ouvrent de manière inattendue dans votre application au lieu de votre navigateur web, il peut y avoir un problème avec la configuration de votre campagne ou le déploiement du SDK. Suivez les étapes ci-dessous pour obtenir de l'aide.

### Vérifiez le comportement au clic {#verify-on-click-behavior}

Dans votre Campaign ou étape Canvas, vérifiez que l'option **Open web URL inside mobile app** n'est pas sélectionnée. Si c'est le cas, désélectionnez-la et relancez.

L'interaction par défaut pour le comportement au clic « Open web URL » diffère selon la version du SDK. Pour les versions du SDK iOS 2.29.0 et Android 2.0.0 et supérieures, cette option est sélectionnée par défaut et les URL web s'ouvrent dans une vue web au sein de l'application. Avant ces versions, cette option est désélectionnée par défaut et les URL web s'ouvrent dans le navigateur web par défaut de l'appareil.

Si ce n'est pas le problème, il peut y avoir un souci avec votre déploiement push.

### Revérifiez l'intégration push {#double-check-push-integration}

Si les liens dans vos notifications push s'ouvrent de manière inattendue dans l'application, cela peut être dû à des problèmes avec votre intégration de notifications push ou vos paramètres de personnalisation. Suivez ces étapes pour résoudre le problème :

1. **Examinez le déploiement du délégué push :** Assurez-vous que le délégué push de Braze est correctement déployé. Pour des instructions détaillées, consultez le guide d'intégration des notifications push pour votre [plateforme]({{site.baseurl}}/developer_guide/home).
2. **Inspectez la gestion personnalisée des liens :** Vérifiez si l'application inclut une gestion personnalisée pour tous les liens `https://`. Les configurations personnalisées peuvent remplacer les comportements par défaut. Collaborez avec votre équipe de développement pour examiner et ajuster ces paramètres si nécessaire.
3. **Vérifiez l'enregistrement push iOS :** Pour iOS, revisitez l'étape 1 du guide d'intégration push sur l'[enregistrement des notifications push auprès d'APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns). Assurez-vous que votre objet délégué est assigné de manière synchrone avant que l'application ne termine son lancement. Cette étape doit être effectuée dans la méthode `application:didFinishLaunchingWithOptions:`.
4. **Testez votre intégration :** Après avoir effectué les ajustements, testez le comportement des notifications push sur les appareils iOS et Android pour confirmer que le problème est résolu.

### Deep links avec l'application toujours en arrière-plan (iOS) {#deep-links-with-app-still-running-in-the-background-ios}

Si les deep links fonctionnent lorsque l'application n'est pas en cours d'exécution ou lorsque le lien est utilisé directement, mais pas lorsque l'application est déjà en arrière-plan, le problème peut être lié à la façon dont l'application gère le lien. Vérifiez si vous utilisez des bibliothèques tierces qui utilisent le method swizzling. Nous recommandons de désactiver le swizzling, car cela peut causer des problèmes avec les déploiements de deep links.

## Migrer vers une clé d'authentification .p8 {#migrate-to-a-p8-authentication-key}

**Symptôme :** Vous devez migrer les identifiants push iOS d'un certificat hérité vers une clé `.p8`, ou la distribution des notifications push a échoué après un changement d'identifiant.

Les clés d'authentification Apple `.p8` sont l'approche requise pour les notifications push APNs dans Braze. Contrairement aux types de fichiers de certificat hérités, les clés `.p8` n'expirent pas et prennent en charge toutes vos applications sous une seule clé, éliminant ainsi le besoin de renouvellements annuels de certificats et réduisant le risque d'échecs de distribution des notifications push.

Si vous utilisez actuellement un certificat `.p12` ou `.pem`, migrez vers une clé `.p8` dès que possible. Pour les instructions sur la création et le téléchargement d'une clé `.p8`, consultez [Télécharger votre certificat push APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). Pour les recommandations d'Apple sur la génération d'une clé `.p8` depuis votre compte développeur, consultez [Communicate with APNs using authentication tokens](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

### Clés .p8 et certificats .p12 {#p8-keys-versus-p12-certificates}

Utilisez le tableau suivant pour comparer les types d'identifiants, leur expiration et leur apparence dans le tableau de bord.

| Identifiant | Expiration | Indicateur de statut dans le tableau de bord |
| --- | --- | --- |
| Clé d'authentification `.p8` | N'expire pas | Pas d'indicateur de statut vert (c'est normal) |
| Certificat push `.p12` | Expire chaque année | Indicateur vert lorsque le certificat est valide |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Clés .p8 et certificats .p12" }

Lorsque vous remplacez un certificat `.p12` par une clé `.p8` (ou téléchargez un nouvel identifiant), la distribution des notifications push peut être brièvement interrompue pendant que Braze traite le changement. Planifiez les mises à jour pendant une fenêtre de maintenance si possible.

Dans **Paramètres** > **Paramètres des applications** > **Paramètres des notifications push**, confirmez que l'**App Bundle ID**, le **Team ID** et le **Key ID** (pour les clés `.p8`) correspondent aux valeurs de votre compte Apple Developer. Plusieurs espaces de travail Braze peuvent utiliser le même identifiant push Apple lorsque le **bundle ID** de l'application iOS est identique ; l'environnement de l'identifiant (développement ou production) doit correspondre à la façon dont l'application a été compilée.

Les applications utilisant le [SDK Swift Braze 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) ou version ultérieure peuvent utiliser la [gestion dynamique de la passerelle APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management), qui achemine automatiquement les jetons vers le bon environnement APNs.

## Les notifications push Web ne se comportent pas comme prévu {#web-push-notifications-are-not-behaving-as-expected}

**Symptôme :** Les notifications push du navigateur ne s'affichent pas, ou les autorisations du site semblent bloquées.

Si vous rencontrez des problèmes avec les notifications push dans votre navigateur, vous devrez peut-être réinitialiser les autorisations de notification de votre site et effacer le stockage de votre site. Suivez les étapes ci-dessous pour obtenir de l'aide.

{% tabs %}
{% tab Chrome %}

### Réinitialiser Chrome sur ordinateur {#reset-chrome-on-desktop}

1. À côté de votre URL dans le navigateur Chrome, sélectionnez l'icône du curseur **Afficher les informations du site**.
2. Sous **Notifications**, sélectionnez **Réinitialiser l'autorisation**.
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

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et testez.

### Réinitialiser Chrome sur Android {#reset-chrome-on-android}

Si vous avez une notification de votre site visible dans le tiroir de notifications Android :

1. Depuis la notification push, sélectionnez <i class="fas fa-cog" title="Paramètres"></i> **Paramètres** et sélectionnez **Paramètres du site**.
2. Depuis **Paramètres du site**, appuyez sur **Effacer et réinitialiser**.

Si vous n'avez pas de notification de votre site ouverte :

1. Ouvrez Chrome sur Android.
2. Appuyez sur le menu <i class="fas fa-ellipsis-vertical"></i>.
3. Accédez à **Paramètres** > **Paramètres du site** > **Notifications**.
4. Vérifiez que les notifications sont définies sur **Demander avant d'envoyer (recommandé)**.
5. Trouvez votre site dans la liste.
6. Sélectionnez l'entrée et appuyez sur **Effacer et réinitialiser**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et testez.

{% endtab %}
{% tab Firefox %}

### Réinitialiser Firefox sur ordinateur {#reset-firefox-on-desktop}

1. À côté de l'URL de votre site, sélectionnez <i class="fa-solid fa-circle-info" alt="icône d'information"></i> ou <i class="fas fa-lock" alt="icône de cadenas"></i>.
2. Sous **Autorisations**, à côté de **Recevoir des notifications**, sélectionnez <i class="fa-solid fa-circle-xmark" title="Effacer cette autorisation et redemander"></i> **Effacer l'autorisation** pour supprimer les autorisations de notification.
3. Dans le même menu, sélectionnez **Effacer les cookies et les données du site**.
4. Dans la boîte de dialogue pour confirmer votre choix, sélectionnez **OK**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et testez.

### Réinitialiser Firefox sur Android {#reset-firefox-on-android}

Pour réinitialiser les autorisations push sur Android, consultez [Supprimer l'historique de navigation et d'autres données personnelles](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) sur le support Mozilla.

{% endtab %}
{% tab Safari %}

### Réinitialiser Safari sur macOS {#reset-safari-on-macos}

{% alert note %}
Ces étapes sont uniquement pour macOS, car Apple ne prend pas en charge le push Web pour Safari sur Windows.
{% endalert %}

1. Ouvrez Safari.
2. Depuis la [barre de menus sur Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), accédez à **Safari** > **Réglages** > **Sites web** > **Notifications**.
3. Sélectionnez votre site dans la liste.
4. Sélectionnez **Supprimer** pour effacer les autorisations de notification du site.
5. Ensuite, accédez à **Confidentialité** > **Gérer les données de sites web**.
6. Sélectionnez votre site dans la liste.
7. Sélectionnez **Supprimer**, ou pour supprimer toutes les données du site, sélectionnez **Tout supprimer**.
8. Sélectionnez **Terminé**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et testez.

{% endtab %}
{% endtabs %}

## Indicateurs d'ouverture push {#push-open-metrics}

Braze enregistre une ouverture directe lorsqu'un utilisateur appuie sur la notification et que votre application démarre une session. Développer une notification push riche sans ouvrir l'application n'enregistre pas d'ouverture directe.

Si un utilisateur ouvre votre application après avoir reçu une notification push sans appuyer dessus, Braze peut enregistrer une ouverture influencée à la place. Pour les définitions et les rapports, consultez [Ouvertures influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

## Messages d'erreur push {#push-error-messages}

**Symptôme :** Vous voyez un code d'erreur push spécifique (par exemple, `DEVICE_UNREGISTERED`, `Unregistered` ou `NotRegistered`).

Pour les définitions des codes d'erreur push courants (y compris `DEVICE_UNREGISTERED`, `NotRegistered` et `Unregistered`), consultez [Messages d'erreur push courants]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

Lorsque FCM renvoie des erreurs telles que `DEVICE_UNREGISTERED` ou `NotRegistered`, Braze supprime généralement le jeton de notification push concerné du profil utilisateur. Cette suppression indique souvent que l'application a été désinstallée ou que le jeton n'est plus valide. Les campagnes de suivi de désinstallation utilisent la même logique de suppression de jeton à grande échelle.