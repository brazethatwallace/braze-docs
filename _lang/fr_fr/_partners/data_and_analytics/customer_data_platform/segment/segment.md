---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Cet article de référence décrit le partenariat entre Braze et Segment, une plateforme de données clients qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com) est une plateforme de données clients qui vous aide à collecter, nettoyer et activer vos données clients.

L'intégration de Braze et Segment vous permet de suivre vos utilisateurs et d'acheminer les données vers différents fournisseurs d'analyse des utilisateurs. Segment vous permet de :

- Synchroniser [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage) avec Braze pour une utilisation dans la segmentation de Campaign et Canvas de Braze.
- [Importer des données entre les deux plateformes](#integration-options). Nous proposons une intégration SDK côte à côte pour vos applications Android, iOS et web, ainsi qu'une intégration serveur à serveur pour la synchronisation de vos données avec les REST API de Braze.
- [Connecter les données à Segment via Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents).

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Source installée et [bibliothèques](https://segment.com/docs/sources/) de source Segment | L'origine de toute donnée envoyée dans Segment, telle que les applications mobiles, les sites web ou les serveurs backend.<br><br>Vous devez installer les bibliothèques dans votre application, site ou serveur avant de pouvoir configurer un flux `Source > Destination` fonctionnel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour intégrer Braze et Segment, vous devez configurer [Braze comme destination](#connection-settings) conformément au [type d'intégration choisi](#integration-options) (mode de connexion). Si vous êtes un nouveau client Braze, vous pouvez transmettre des données historiques à Braze en utilisant les [replays Segment](#segment-replays). Ensuite, vous devez configurer les [mappages](#methods) et [tester votre intégration](#step-4-test-your-integration) pour garantir un flux de données fluide entre Braze et Segment.

### Étape 1 : Créer une destination Braze {#connection-settings}

Après avoir configuré vos sources avec succès, vous devrez configurer Braze comme [destination](https://segment.com/docs/destinations/) pour chaque source (iOS, Android, web, etc.). Vous disposerez de nombreuses options pour personnaliser le flux de données entre Braze et Segment à l'aide des paramètres de connexion.

### Étape 2 : Choisir le framework de destination et le type de connexion {#integration-options}

Dans Segment, naviguez vers **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![La page de configuration de la source. Cette page inclut des paramètres pour définir le framework de destination comme « actions » ou « classic » et le mode de connexion comme « cloud mode » ou « device mode ».]({% image_buster /assets/img/segment/setup.png %})

Vous pouvez intégrer la source web de Segment (Analytics.js) et les bibliothèques clientes natives avec Braze en utilisant soit une intégration côte à côte (device-mode), soit une intégration serveur à serveur (cloud-mode).

Votre choix de mode de connexion sera déterminé par le type de source pour laquelle la destination est configurée.

| Intégration | Détails |
| ----------- | ------- |
| [Côte à côte<br>(device-mode)](#side-by-side-sdk-integration) | Utilise le SDK de Segment pour traduire les événements en appels natifs Braze, permettant l'accès à des fonctionnalités plus avancées et une utilisation plus complète de Braze que l'intégration serveur à serveur.<br><br>Notez que Segment ne prend pas en charge toutes les méthodes Braze (par exemple, les Content Cards). Pour utiliser une méthode Braze qui n'est pas mappée via un mappage correspondant, vous devrez invoquer la méthode en ajoutant du code natif Braze à votre base de code. |
| [Serveur à serveur<br>(cloud-mode)](#server-to-server-integration) | Transfère les données de Segment vers les endpoints de la REST API de Braze.<br><br>Ne prend pas en charge les fonctionnalités de l'interface Braze telles que les messages in-app, les Content Cards ou les notifications push. Il existe également des données capturées automatiquement, comme les champs au niveau de l'appareil, qui ne sont pas disponibles via cette méthode.<br><br>Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Choisir le framework de destination et le type de connexion" }

{% alert note %}
Consultez [Segment](https://segment.com/docs/destinations/#connection-modes) pour en savoir plus sur les deux options d'intégration (modes de connexion), y compris les avantages de chacune.
{% endalert %}

#### Intégration SDK côte à côte {#side-by-side-sdk-integration}

Également appelée device-mode, cette intégration mappe le SDK et les [méthodes](#methods) de Segment au SDK de Braze, permettant l'accès à toutes les fonctionnalités fournies par notre SDK, telles que le push, les messages in-app et d'autres méthodes natives de Braze.

{% alert note %}
Lorsque vous utilisez le device-mode de Segment, laissez Segment initialiser Braze. N'initialisez pas également le SDK Braze dans votre application. Le plugin de destination configure Braze et ouvre des sessions ; une seconde initialisation native peut enregistrer des sessions en double. Utilisez `identify` de Segment pour définir l'ID utilisateur. Le plugin mappe cet appel vers `changeUser()`.
{% endalert %}

{% alert important %}
Pour les intégrations en device-mode sur mobile, vous devez ajouter le plugin de destination Braze à votre application en plus de configurer la destination dans le tableau de bord Segment. Le SDK de Segment n'inclut pas le plugin Braze par défaut — sans celui-ci, le SDK de Segment ne peut pas transmettre les données ou les appels de méthodes mappés à Braze, et les fonctionnalités telles que le push, les messages in-app et les Content Cards ne fonctionneront pas. Consultez les onglets spécifiques à chaque plateforme dans cette section pour les instructions d'installation.
{% endalert %}

Lors de l'utilisation d'une connexion en device-mode, de manière similaire à l'intégration native du SDK Braze, le SDK Braze attribuera un `device_id` et un identifiant backend, `braze_id`, à chaque utilisateur. Cela permet à Braze de capturer l'activité anonyme depuis l'appareil en faisant correspondre ces identifiants au lieu du `userId`.

{% alert note %}
Si vous utilisez des [filtres de destination](https://segment.com/docs/connections/destinations/destination-filters/) avec des destinations en device-mode (Kotlin ou Swift), vous devez configurer le plugin de destination avec le support des filtres activé. Consultez la [documentation sur les filtres de destination](https://segment.com/docs/connections/destinations/destination-filters/) de Segment pour plus de détails sur les versions de plugins prises en charge.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
Le code source de l'intégration Android en device-mode est maintenu par Braze et est régulièrement mis à jour pour refléter les nouvelles versions du SDK Braze.

<br>
Le SDK Braze que vous utilisez dépendra du SDK Segment que vous utilisez :

| | SDK Segment | SDK Braze |
| - | ----------- | --------- |
| Recommandé | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Ancien | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Intégration SDK côte à côte" }


{% endalert %}

Pour configurer Braze comme destination en device-mode pour votre source Android, choisissez **Actions** comme **Destination framework**, puis sélectionnez **Save**.

Pour compléter l'intégration côte à côte, vous devez ajouter le [plugin de destination Braze Kotlin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) à votre application Android. Ce plugin fait le lien entre le SDK Segment et le SDK Braze, permettant aux données en device-mode de circuler vers Braze. Suivez les instructions d'installation de Segment pour ajouter la dépendance du plugin et l'initialiser avec votre instance d'analytique Segment.

Le code source de l'intégration [Android en device-mode](https://github.com/braze-inc/braze-segment-kotlin) est maintenu par Braze et est régulièrement mis à jour pour refléter les nouvelles versions du SDK Braze.

{% endtab %}
{% tab iOS %}

{% alert important %}
Le code source de l'intégration iOS en device-mode est maintenu par Braze et est régulièrement mis à jour pour refléter les nouvelles versions du SDK Braze.

<br>
Le SDK Braze que vous utilisez dépendra du SDK Segment que vous utilisez :

| | SDK Segment | SDK Braze |
| - | ----------- | --------- |
| Recommandé | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Ancien | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Intégration SDK côte à côte" }
{% endalert %}

Pour configurer Braze comme destination en device-mode pour votre source iOS, choisissez **Actions** comme **Destination framework**, puis sélectionnez **Save**.

Pour compléter l'intégration côte à côte, vous devez ajouter le [plugin de destination Braze Swift](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) à votre application iOS. Ce plugin fait le lien entre le SDK Segment et le SDK Braze, permettant aux données en device-mode de circuler vers Braze. Suivez les instructions d'installation de Segment pour ajouter la dépendance du plugin (via le gestionnaire de paquets Swift ou CocoaPods) et l'initialiser avec votre instance d'analytique Segment.

Le code source de l'intégration [iOS en device-mode](https://github.com/braze-inc/braze-segment-swift) est maintenu par Braze et est régulièrement mis à jour pour refléter les nouvelles versions du SDK Braze.

{% endtab %}
{% tab Web ou JavaScript %}

Le framework Web Mode (Actions) de Braze de Segment est recommandé pour configurer Braze comme destination en device-mode pour votre source web.

Dans Segment, sélectionnez **Actions** comme framework de destination et **Device Mode** comme mode de connexion.

![Configuration de la destination Segment montrant le framework Actions et le Device Mode sélectionnés.]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
Le code source du [plugin React Native Braze](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) est maintenu par Segment et est régulièrement mis à jour pour refléter les nouvelles versions du SDK Braze.

Lors de la connexion d'une source React Native Segment à Braze, vous devez configurer une source et une destination par système d'exploitation. Par exemple, configurer une destination iOS et une destination Android.

Dans votre base de code d'application, initialisez conditionnellement le SDK Segment par type d'appareil, en utilisant la clé d'écriture source respective associée à chaque application.

Lorsqu'un jeton push est enregistré depuis un appareil et envoyé à Braze, il est associé à l'identifiant d'application utilisé lors de l'initialisation du SDK. L'initialisation conditionnelle par type d'appareil permet de confirmer que les jetons push envoyés à Braze sont associés à l'application appropriée.

{% alert important %}
Si l'application React Native initialise Braze avec le même identifiant d'application Braze pour tous les appareils, alors tous les utilisateurs React Native seront considérés comme des utilisateurs Android ou iOS dans Braze, et tous les jetons push seront associés à ce système d'exploitation.
{% endalert %}

Pour configurer Braze comme destination en device-mode pour chaque source, choisissez **Actions** comme **Destination framework**, puis sélectionnez **Save**.

{% endtab %}
{% endtabs %}

#### Intégration serveur à serveur {#server-to-server-integration}

Également appelée cloud-mode, cette intégration transfère les données de Segment vers les REST API de Braze. Utilisez le framework [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) de Segment pour configurer une destination en cloud-mode pour n'importe laquelle de vos sources.

Contrairement à l'intégration côte à côte, l'intégration serveur à serveur ne prend pas en charge les fonctionnalités de l'interface Braze, telles que les messages in-app, les Content Cards ou l'enregistrement automatique des jetons push. Il existe également des données [capturées automatiquement]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection) (comme les utilisateurs anonymes et les champs au niveau de l'appareil) qui ne sont pas disponibles via le cloud-mode.

Si vous souhaitez utiliser ces données et ces fonctionnalités, envisagez d'utiliser l'intégration SDK côte à côte (device-mode).

Le code source de la [destination Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) est maintenu par Segment.

### Étape 3 : Paramètres {#step-3-settings}

Définissez les paramètres de votre destination. Tous les paramètres ne s'appliquent pas à tous les types de destination.

{% tabs local %}
{% tab Device-mode mobile %}

| Paramètre | Description |
| ------- | ----------- |
| Identifiant d'application | L'identifiant d'application utilisé pour référencer l'application spécifique. Il se trouve dans le tableau de bord de Braze sous **Gérer les paramètres**. |
| Endpoint API personnalisé<br>(endpoint SDK) | Votre endpoint SDK Braze qui correspond à votre instance (par exemple `sdk.iad-01.braze.com`). |
| Région de l'endpoint | Votre instance Braze (par exemple US 01, US 02, EU 01, etc.). |
| Activer l'enregistrement automatique des messages in-app | Désactivez cette option si vous souhaitez enregistrer manuellement les messages in-app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Paramètres" }

{% endtab %}
{% tab Device-mode web %}

| Paramètre | Description |
| ------- | ----------- |
| Identifiant d'application | L'identifiant d'application utilisé pour référencer l'application spécifique. Il se trouve dans le tableau de bord de Braze sous **Gérer les paramètres**. |
| Endpoint API personnalisé<br>(endpoint SDK) | Votre endpoint SDK Braze qui correspond à votre instance (par exemple `sdk.iad-01.braze.com`). |
| ID push web Safari | Si vous prenez en charge le push Safari, vous devez spécifier cette option avec l'ID push web que vous avez fourni à Apple lors de la création de votre certificat push Safari (commence par `web`, par exemple `web.com.example.domain`). |
| Version du SDK Web Braze | La version du SDK Web Braze que vous souhaitez utiliser. |
| Envoyer automatiquement les messages in-app | Par défaut, tous les messages in-app auxquels un utilisateur est éligible sont automatiquement envoyés à l'utilisateur. Désactivez cette option si vous souhaitez afficher manuellement les messages in-app. |
| Ne pas charger Font Awesome | Braze utilise Font Awesome pour les icônes des messages in-app. Par défaut, Braze charge automatiquement FontAwesome depuis le CDN FontAwesome. Pour désactiver ce comportement (par exemple, parce que votre site utilise une version personnalisée de FontAwesome), définissez cette option sur `TRUE`. Notez que si vous le faites, vous êtes responsable de vous assurer que FontAwesome est chargé sur votre site — sinon, les messages in-app pourraient ne pas s'afficher correctement. |
| Activer les messages in-app HTML | L'activation de cette option permettra aux utilisateurs du tableau de bord de Braze d'utiliser les messages in-app HTML. |
| Ouvrir les messages in-app dans un nouvel onglet | Par défaut, les liens provenant des clics sur les messages in-app se chargent dans l'onglet actuel ou dans un nouvel onglet tel que spécifié dans le tableau de bord pour chaque message. Définissez cette option sur `TRUE` pour forcer tous les liens des clics sur les messages in-app à s'ouvrir dans un nouvel onglet ou une nouvelle fenêtre. |
| Index z des messages in-app | Fournissez une valeur pour cette option afin de remplacer les index z par défaut de Braze. |
| Exiger la fermeture explicite des messages in-app | Par défaut, lorsqu'un message in-app s'affiche, appuyer sur la touche Échap ou cliquer sur l'arrière-plan grisé de la page fermera le message. Définissez cette option sur true pour empêcher ce comportement et exiger un clic explicite sur un bouton pour fermer les messages. |
| Intervalle minimum entre les actions de déclenchement en secondes | Par défaut, 30.<br>Par défaut, une action de déclenchement ne se déclenche que si au moins 30 secondes se sont écoulées depuis la dernière action de déclenchement. Fournissez une valeur pour cette option de configuration pour remplacer cette valeur par défaut par votre propre valeur. Nous ne recommandons pas de rendre cette valeur inférieure à 10 pour éviter de submerger l'utilisateur avec des notifications. |
| Emplacement du service de traitement | Par défaut, lors de l'inscription des utilisateurs aux notifications push web, Braze cherchera le fichier de service de traitement requis dans le répertoire racine de votre serveur web à `/service-worker.js`. Si vous souhaitez héberger votre service de traitement à un chemin différent sur ce serveur, fournissez une valeur pour cette option qui est le chemin absolu vers le fichier (par exemple `/mycustompath/my-worker.js`). Notez que définir une valeur ici limite la portée des notifications push sur votre site. Par exemple, dans cet exemple, parce que le fichier de service de traitement se trouve dans le répertoire `/mycustompath/`, `requestPushPermission` ne peut être appelé qu'à partir de pages web qui commencent par `http://yoursite.com/mycustompath/`. |
| Désactiver la maintenance des jetons push | Par défaut, les utilisateurs qui ont déjà accordé l'autorisation push web synchroniseront automatiquement leur jeton push avec le backend Braze lors de nouvelles sessions pour assurer la livrabilité. Pour désactiver ce comportement, définissez cette option sur `FALSE`. |
| Gérer le service de traitement de manière externe | Si vous avez votre propre service de traitement que vous enregistrez et dont vous contrôlez le cycle de vie, définissez cette option sur `TRUE`, et le SDK Braze n'enregistrera ni ne désenregistrera de service de traitement. Si vous définissez cette option sur `TRUE`, pour que le push fonctionne correctement, vous devez enregistrer le service de traitement vous-même avant d'appeler `requestPushPermission` et vous assurer qu'il contient le code du service de traitement Braze, soit avec `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` soit en incluant directement le contenu de ce fichier. Lorsque cette option est `TRUE`, l'option `serviceWorkerLocation` n'est pas pertinente et est ignorée. |
| Nonce de sécurité du contenu | Si vous fournissez une valeur pour cette option, le SDK Braze ajoutera le nonce à tous les éléments `<script>` et `<style>` créés par le SDK. Cela permet au SDK Braze de fonctionner avec la politique de sécurité du contenu de votre site web. En plus de définir ce nonce, vous devrez peut-être également autoriser le chargement de FontAwesome, ce que vous pouvez faire en ajoutant `use.fontawesome.com` à la liste d'autorisation de votre politique de sécurité du contenu ou en utilisant l'option `doNotLoadFontAwesome` et en le chargeant manuellement. |
| Autoriser l'activité des robots d'exploration | Par défaut, le SDK Web Braze ignore l'activité des robots d'exploration ou des spiders connus, tels que Google, en se basant sur la chaîne de l'agent utilisateur. Cela économise des points de données, rend les analyses plus précises et peut améliorer le classement des pages. Cependant, si vous souhaitez que Braze enregistre l'activité de ces robots, vous pouvez définir cette option sur `TRUE`. |
| Activer la journalisation | Définissez sur `TRUE` pour activer la journalisation par défaut. Notez que cela amènera Braze à écrire dans la console JavaScript, qui est visible par tous les utilisateurs. Avant de mettre votre page en production, vous devriez supprimer cela ou fournir un logger alternatif avec `setLogger`. |
| Autoriser le JavaScript fourni par l'utilisateur | Par défaut, le SDK Web Braze n'autorise pas les actions de clic JavaScript fournies par l'utilisateur, car cela permet aux utilisateurs du tableau de bord de Braze d'exécuter du JavaScript sur votre site. Pour indiquer que vous faites confiance aux utilisateurs du tableau de bord de Braze pour écrire des actions de clic JavaScript non malveillantes, définissez cette propriété sur `TRUE`. Si `enableHtmlInAppMessages` est `TRUE`, cette option sera également définie sur `TRUE`. |
| Version de l'application | Si vous fournissez une valeur pour cette option, les événements utilisateur envoyés à Braze seront associés à la version donnée, qui peut être utilisée pour la segmentation des utilisateurs. |
| Délai d'expiration de session en secondes | Par défaut, 30.<br>Par défaut, les sessions expirent après 30 minutes d'inactivité. Fournissez une valeur pour cette option de configuration pour remplacer cette valeur par défaut par votre propre valeur. |
| Liste d'autorisation des propriétés d'appareil | Par défaut, le SDK Braze détecte et collecte automatiquement toutes les propriétés d'appareil dans `DeviceProperties`. Pour remplacer ce comportement, fournissez un tableau de `DeviceProperties`. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la distribution par fuseau horaire local ne fonctionnera pas sans le fuseau horaire. |
| Localisation | Par défaut, tous les messages visibles par l'utilisateur générés par le SDK seront affichés dans la langue du navigateur de l'utilisateur. Fournissez une valeur pour cette option pour remplacer ce comportement et forcer une langue spécifique. La valeur de cette option doit être un code de langue ISO 639-1. |
| Pas de cookies | Par défaut, le SDK Braze stocke de petites quantités de données (identifiants utilisateur, identifiants de session) dans des cookies. Cela permet à Braze de reconnaître les utilisateurs et les sessions sur différents sous-domaines de votre site. Si cela pose un problème pour vous, passez `TRUE` pour cette option afin de désactiver le stockage par cookies et vous appuyer entièrement sur le localStorage HTML 5 pour identifier les utilisateurs et les sessions. |
| Suivre toutes les pages | **Destination classique Web Device-Mode (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination Web Actions framework où ce paramètre peut être [activé via les mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela enverra tous les [appels de page](https://segment.com/docs/spec/page/) à Braze en tant qu'événement « Loaded/Viewed a Page ». |
| Suivre uniquement les pages nommées | **Destination classique Web Device-Mode (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination Web Actions framework où ce paramètre peut être [activé via les mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela n'enverra que les appels de page à Braze auxquels un nom est associé. |
| Enregistrer un achat lorsqu'un revenu est présent | **Destination classique Web Device-Mode (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination Web Actions framework où ce paramètre peut être [activé via les mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Lorsque cette option est activée, tous les appels Track avec la propriété revenue déclencheront un événement d'achat. |
| Suivre uniquement les utilisateurs connus | **Destination classique Web Device-Mode (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination Web Actions Framework où ce paramètre peut être activé via les mappages.<br><br>Si activé, ce nouveau paramètre retarde l'appel de `window.braze.initialize` jusqu'à ce qu'un `userId` valide soit disponible. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Paramètres" }

{% endtab %}
{% tab Cloud-mode %}

| Paramètre | Description |
| ------- | ----------- |
| Identifiant d'application | L'identifiant d'application utilisé pour référencer l'application spécifique. Il se trouve dans le tableau de bord de Braze sous **Gérer les paramètres**. |
| Clé REST API | Elle se trouve dans votre tableau de bord de Braze sous **Paramètres** > **Clés API**. |
| Endpoint REST API personnalisé | Votre endpoint REST Braze qui correspond à votre instance (par exemple rest.iad-01.braze.com). |
| Mettre à jour uniquement les utilisateurs existants | **Destination classique Cloud-Mode (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination Cloud Actions Framework où ce paramètre peut être [activé via les mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Détermine si seuls les utilisateurs existants doivent être mis à jour. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Paramètres" }

{% endtab %}
{% endtabs %}

### Étape 4 : Mapper les méthodes {#methods}

Braze prend en charge les méthodes Segment [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) et [Track](https://segment.com/docs/spec/track/). Les types d'identifiants utilisés dans ces méthodes dépendront de la transmission des données via une intégration serveur à serveur (cloud-mode) ou côte à côte (device-mode). Dans les destinations Braze Web Mode Actions et Cloud Mode Actions, vous pouvez également choisir de configurer un mappage pour un [appel alias Segment](https://segment.com/docs/connections/spec/alias/).

{% alert note %}
Bien que les alias utilisateur soient pris en charge comme identifiant dans la destination Braze Cloud Mode (Actions), il convient de noter que l'appel alias de Segment n'est pas directement lié aux alias d'utilisateur Braze.
{% endalert %}

| Type d'identifiant | Destination prise en charge |
| --------------- | --------------------- |
| `userId` (`external_id`) | Toutes |
| Utilisateur anonyme | Destinations en device-mode |
| Alias utilisateur | Destinations en cloud-mode |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4 : Mapper les méthodes" }

La destination Cloud Mode (Actions) offre une [action Create Alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) qui peut être utilisée pour créer un utilisateur avec alias uniquement ou pour ajouter un alias à un profil `external_id` existant. L'[action Identify User](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) peut être utilisée conjointement avec l'action Create Alias pour fusionner un utilisateur avec alias uniquement avec un `external_id` une fois que celui-ci est disponible pour l'utilisateur.

Il est également possible d'élaborer une solution de contournement et d'utiliser `braze_id` pour envoyer des données d'utilisateurs anonymes en cloud-mode. Cela nécessite d'inclure manuellement le `braze_id` de l'utilisateur dans tous vos appels API Segment. Vous pouvez en apprendre davantage sur la configuration de cette solution de contournement dans la [documentation de Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Les données de destination envoyées à Braze peuvent être regroupées en lots dans Cloud Mode Actions. La taille des lots est plafonnée à 75 événements, et ces lots s'accumulent sur une période de 30 secondes avant d'être envoyés. Le regroupement des requêtes est effectué par action. Par exemple, les appels Identify (attributs) seront regroupés dans une requête et les appels Track (événements personnalisés) seront regroupés dans une seconde requête. Braze recommande d'activer cette fonctionnalité car elle réduira le nombre de requêtes envoyées de Segment à Braze. En retour, cela réduira le risque que la destination atteigne les limites de débit de Braze et doive retenter les requêtes.

Vous pouvez activer le regroupement pour une action en naviguant vers votre destination Braze > **Mappings**. De là, cliquez sur l'icône à 3 points à côté du mappage et sélectionnez **Edit Mapping**. Faites défiler jusqu'au bas de la section **Select mappings** et assurez-vous que **Batch Data to Braze** est défini sur **Yes**.


{% tabs local %}
{% tab Identify %}
#### Identify

L'appel [Identify](https://segment.com/docs/spec/identify/) vous permet d'associer un utilisateur à ses actions et d'enregistrer des attributs le concernant.

Certains traits spéciaux de Segment sont mappés vers des champs de profil d'attributs standard dans Braze :

| Traits spéciaux Segment | Attributs standard Braze |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identify" }

D'autres champs de profil réservés de Braze tels que `email_subscribe` et `push_subscribe` peuvent être envoyés en utilisant la convention de nommage Braze pour ces champs et en les transmettant comme traits dans un appel Identify.

##### Ajouter un utilisateur à un groupe d'abonnement {#adding-a-user-to-a-subscription-group}

Vous pouvez également abonner ou désabonner un utilisateur d'un groupe d'abonnement donné en utilisant les champs suivants dans le paramètre traits.

Utilisez le champ de profil réservé de Braze appelé `braze_subscription_groups`, qui peut être associé à un tableau d'objets. Chaque objet du tableau doit contenir deux clés réservées :

1. `subscription_group_state` : indique si l'utilisateur est `"subscribed"` ou `"unsubscribed"` d'un groupe d'abonnement spécifique.
2. `subscription_group_id` : représente l'ID unique du groupe d'abonnement. Vous pouvez trouver cet ID dans le tableau de bord de Braze sous **Subscription Group Management**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Attributs personnalisés {#custom-attributes}

Tous les autres traits seront enregistrés comme [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| Identify avec ID utilisateur | Définir l'ID externe | Segment : `analytics.identify("dawei");`<br>Braze : `Braze.changeUser("dawei")` |
| Identify avec traits réservés | Définir les attributs utilisateur | Segment : `analytics.identify({email: "dawei@braze.com"});`<br> Braze : `Braze.getUser().setEmail("dawei@braze.com");`
| Identify avec traits personnalisés | Définir les attributs personnalisés | Segment : `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze : `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify avec ID utilisateur et traits | Segment : définir l'ID externe et l'attribut | Combinez les méthodes précédentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Attributs personnalisés" }

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) et [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), ces mappages peuvent être configurés à l'aide de l'action Update User Profile.

{% alert important %}
Lors de la transmission de données d'attributs utilisateur, vérifiez que vous ne transmettez que les valeurs des attributs qui ont changé depuis la dernière mise à jour. Cela garantira que vous n'enregistrez pas inutilement des points de données. Pour les sources côté client, utilisez l'outil open source [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de Segment pour optimiser votre intégration et limiter l'utilisation des points de données en dédupliquant les appels `identify()` identiques provenant de Segment.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

Lorsque vous suivez un événement, nous enregistrerons cet événement comme un [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) en utilisant le nom fourni.

Les métadonnées envoyées dans l'objet properties de l'appel Track seront enregistrées dans Braze comme propriétés de l'événement personnalisé pour l'événement associé. Tous les [types de données de propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) sont pris en charge.

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) et [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), ces mappages peuvent être configurés à l'aide de l'action Track Event.

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Enregistré comme [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events). | Segment : `analytics.track("played_game");` <br>Braze : `Braze.logCustomEvent("played_game");` |
| [Track avec propriétés](https://segment.com/docs/spec/track/) | Enregistré comme [propriété d'événement]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties). | Segment : `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze : `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track avec produit](https://segment.com/docs/spec/track/) | Enregistré comme [événement d'achat]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment : `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze : `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### Commande terminée {#order-completed}

Lorsque vous suivez un événement avec le nom `Order Completed` en utilisant le format décrit dans l'[API eCommerce](https://segment.com/docs/spec/ecommerce/v2/) de Segment, nous enregistrerons les produits que vous avez listés comme des [achats]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) et [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), le mappage par défaut peut être personnalisé via l'action Track Purchase.

{% endtab %}

{% tab Page %}
#### Page {#page}

L'appel [Page](https://segment.com/docs/spec/page/) vous permet d'enregistrer chaque fois qu'un utilisateur voit une page de votre site web, ainsi que des propriétés optionnelles concernant la page.

Ce type d'événement peut être utilisé comme déclencheur dans les destinations Web Mode Actions et Cloud Actions pour enregistrer un événement personnalisé dans Braze.
{% endtab %}

{% endtabs %}

### Étape 5 : Tester votre intégration {#step-5-test-your-integration}

Lors de l'utilisation de l'intégration côte à côte (device-mode), vos indicateurs d'[aperçu]({{site.baseurl}}/user_guide/analytics/dashboards/home) (sessions à vie, MAU, DAU, adhérence, sessions quotidiennes et sessions quotidiennes par MAU) peuvent être utilisés pour vérifier que Braze reçoit les données de Segment.

Vous pouvez consulter vos données sur les pages des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data) ou des [revenus]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data), ou en [créant un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment). La page **Custom Events** du tableau de bord vous permet de visualiser le nombre d'événements personnalisés au fil du temps. Notez que vous ne pourrez pas utiliser les [formules]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula) qui incluent les statistiques MAU et DAU lors de l'utilisation d'une intégration serveur à serveur (cloud-mode).

Si vous envoyez des données d'achat à Braze (voir la commande terminée dans l'onglet **Track** de l'[étape 3](#methods)), la page des [revenus]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) vous permet de visualiser les données sur les revenus ou les achats sur des périodes spécifiques ou le chiffre d'affaires total de votre application.

[Créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) vous permet de filtrer vos utilisateurs en fonction des données d'événements personnalisés et d'attributs.

{% alert important %}
Si vous utilisez une intégration serveur à serveur (cloud-mode), les filtres liés aux données de session capturées automatiquement (tels que « première utilisation de l'application » et « dernière utilisation de l'application ») ne fonctionneront pas. Utilisez une intégration côte à côte (device-mode) si vous souhaitez les utiliser dans votre intégration Segment et Braze.
{% endalert %}

## Suppression et blocage des utilisateurs {#user-deletion-and-suppression}

Si vous devez supprimer ou bloquer des utilisateurs, notez que la [fonctionnalité de suppression d'utilisateurs de Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **est** mappée sur l'[endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze. Notez que la vérification de ces suppressions peut prendre jusqu'à 30 jours.

Vous devez vous assurer de sélectionner un identifiant utilisateur commun entre Braze et Segment (comme `external_id`). Après avoir initié une demande de suppression avec Segment, vous pouvez consulter le statut dans l'onglet des demandes de suppression de votre tableau de bord Segment.

## Relecture de Segment {#segment-replays}

Segment propose à ses clients un service de « relecture » de l'ensemble des données historiques vers un nouveau partenaire technologique. Les nouveaux clients Braze qui souhaitent importer toutes les données historiques pertinentes peuvent le faire via Segment. Contactez votre représentant Segment si cette fonctionnalité vous intéresse.

Segment se connectera à notre [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour importer les données utilisateur dans Braze en votre nom.

{% alert important %}
Tous les identifiants pris en charge dans la destination Cloud Mode Actions sont pris en charge dans le cadre des relectures Segment.
{% endalert %}

## Bonnes pratiques {#best-practices}

{% details Examinez les cas d'usage pour éviter les dépassements de données. %}

Segment **ne limite pas** le nombre d'éléments de données que les clients lui envoient. Segment vous permet d'envoyer la totalité ou de choisir quels événements vous enverrez à Braze. Plutôt que d'envoyer tous vos événements via Segment, nous vous suggérons d'examiner les cas d'usage avec vos équipes marketing et éditoriales pour déterminer quels événements vous enverrez à Braze afin d'éviter les dépassements de données.

{% enddetails %}

{% details Comprenez la différence entre l'endpoint API personnalisé et l'endpoint REST API personnalisé dans les paramètres de destination en mode appareil mobile. %}

| Terminologie Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint SDK Braze | Custom API endpoint |
| Endpoint REST Braze | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bonnes pratiques" }

Votre endpoint API Braze (appelé « Custom API Endpoint » dans Segment) est l'endpoint SDK que Braze configure pour votre SDK (par exemple, `sdk.iad-03.braze.com`). Votre endpoint REST API Braze (appelé « Custom REST API Endpoint » dans Segment) est l'endpoint REST API (par exemple, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Assurez-vous que votre endpoint API personnalisé est correctement saisi dans les paramètres de destination en mode appareil mobile. %}

| Terminologie Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint SDK Braze | Custom API endpoint |
| Endpoint REST Braze | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bonnes pratiques" }

Le format approprié doit être respecté pour vous assurer de saisir correctement votre endpoint SDK Braze. Votre endpoint SDK Braze ne doit pas inclure `https://` (par exemple, `sdk.iad-03.braze.com`), sinon l'intégration Braze ne fonctionnera pas. Cela est nécessaire car Segment ajoute automatiquement `https://` devant votre endpoint, ce qui entraînerait l'initialisation de Braze avec un endpoint non valide `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Nuances de mappage des données. %}

Scénarios dans lesquels les données ne seront pas transmises comme prévu :

1. Attributs personnalisés imbriqués
  - Bien que les [attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) puissent techniquement être envoyés à Braze via Segment, l'**intégralité du payload** sera envoyée à chaque fois. Cela engendrera des [points de donnée]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points) par clé transmise dans l'objet imbriqué à chaque envoi du payload.<br><br> Pour ne consommer qu'un sous-ensemble de points de donnée lors de l'envoi du payload, vous pouvez utiliser la fonctionnalité personnalisée de [fonctions de destination](https://segment.com/docs/connections/functions/destination-functions/) proposée par Segment. Cette fonctionnalité de la plateforme Segment vous permet de personnaliser la manière dont les données sont envoyées aux destinations en aval.

  {% alert note %}
  Les fonctions de destination personnalisées sont gérées au sein de Segment, et Braze dispose d'une visibilité limitée sur les fonctions qui ont été configurées de manière externe.
  {% endalert %}

{: start="2"}
2. Transmission de données anonymes de serveur à serveur.
  - Les clients peuvent utiliser les bibliothèques serveur à serveur de Segment pour acheminer les données anonymes vers d'autres systèmes. Consultez la section sur les méthodes de mappage pour en savoir plus sur l'envoi d'utilisateurs sans `external_id` à Braze via une intégration serveur à serveur (mode cloud).

{% enddetails %}

{% details Personnalisation de l'initialisation de Braze. %}

Il existe plusieurs façons de personnaliser Braze : les notifications push, les messages in-app, les Content Cards et l'initialisation. Avec une intégration côte à côte, vous pouvez toujours personnaliser les notifications push, les messages in-app et les Content Cards comme vous le feriez avec une intégration Braze directe.

Cependant, personnaliser le moment où le SDK Braze est intégré ou spécifier les configurations d'initialisation peut s'avérer difficile et parfois impossible. En effet, Segment initialisera le SDK Braze pour vous lorsque l'initialisation de Segment aura lieu.

{% enddetails %}

{% details Envoi de deltas à Braze. %}

Lors de la transmission de données d'attributs utilisateur, vérifiez que vous ne transmettez que les valeurs des attributs qui ont changé depuis la dernière mise à jour. Cela évitera la journalisation de points de donnée inutiles. Pour les sources côté client, utilisez l'outil open source [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de Segment pour optimiser votre intégration et limiter l'utilisation des points de donnée en éliminant les appels `identify()` en double provenant de Segment.

{% enddetails %}

{% details Utilisez le bon centre de données Braze. %}

Segment utilise votre centre de données Braze pour récupérer l'endpoint REST Braze approprié (tel que `https://rest.iad-01.braze.com`) pour effectuer des appels de serveur à serveur.

{% enddetails %}

{% details Supprimez l'endpoint REST API personnalisé lorsque vous utilisez l'Event Tester de Segment. %}

L'Event Tester de Segment envoie des événements à l'endpoint REST API `/users/track` de Braze et renvoie une erreur `401 Invalid API Key` si un endpoint REST API personnalisé est défini dans les paramètres de destination Braze, même lorsque cet endpoint est correct. Supprimez la valeur de l'endpoint REST API personnalisé dans Segment pour permettre à l'Event Tester de fonctionner correctement.

{% enddetails %}

{% details Prévoyez un temps de mise à jour après la configuration d'une nouvelle source. %}

Segment conserve vos paramètres de configuration dans le cache pendant une longue durée. Ainsi, lors de la configuration d'une nouvelle source (comme le passage du mode cloud au mode appareil), votre application peut ne pas afficher le nouveau comportement ou les nouvelles données tant que le cache ne s'est pas renouvelé. Gardez ce délai à l'esprit lorsque vous prévoyez d'ajouter une source.

{% enddetails %}