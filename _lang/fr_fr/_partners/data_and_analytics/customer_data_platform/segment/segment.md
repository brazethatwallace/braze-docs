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

- Synchroniser [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage/) avec Braze pour une utilisation dans la segmentation de Campaign et Canvas de Braze.
- [Importer des données entre les deux plateformes](#integration-options). Nous proposons une intégration SDK côte à côte pour vos applications Android, iOS et web, ainsi qu'une intégration serveur à serveur pour la synchronisation de vos données avec les REST API de Braze.
- [Connecter les données à Segment via Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/).

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Source installée et [bibliothèques](https://segment.com/docs/sources/) source Segment | L'origine de toutes les données envoyées à Segment, telles que les applications mobiles, les sites web ou les serveurs backend.<br><br>Vous devez installer les bibliothèques dans votre application, votre site ou votre serveur avant de pouvoir configurer un flux `Source > Destination` fonctionnel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

Pour intégrer Braze et Segment, vous devez définir [Braze comme destination](#connection-settings) conformément au [type d'intégration que vous avez choisi](#integration-options) (mode de connexion). Si vous êtes un nouveau client de Braze, vous pouvez transmettre des données historiques à Braze à l'aide des [rediffusions Segment](#segment-replays). Ensuite, vous devez configurer des [mappages](#methods) et [tester votre intégration](#step-4-test-your-integration) pour garantir un flux de données fluide entre Braze et Segment.

### Étape 1 : Créer une destination Braze {#connection-settings}

Après avoir configuré vos sources avec succès, vous devrez configurer Braze comme [destination](https://segment.com/docs/destinations/) pour chaque source (iOS, Android, web, etc.). Vous disposerez de nombreuses options pour personnaliser le flux de données entre Braze et Segment à l'aide des paramètres de connexion.

### Étape 2 : Choisir le framework de destination et le type de connexion {#integration-options}

Dans Segment, accédez à **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![La page de configuration de la source. Cette page inclut des paramètres permettant de définir le framework de destination comme « actions » ou « classic » et de définir le mode de connexion comme « cloud mode » ou « device mode ».]({% image_buster /assets/img/segment/setup.png %})

Vous pouvez intégrer la source web (Analytics.js) et les bibliothèques natives côté client de Segment à Braze à l'aide d'une intégration côte à côte (mode appareil) ou d'une intégration serveur à serveur (mode cloud).

Votre choix de mode de connexion sera déterminé par le type de source pour lequel la destination est configurée.

| Intégration | Détails |
| ----------- | ------- |
| [Côte à côte<br>(mode appareil)](#side-by-side-sdk-integration) | Utilise le SDK de Segment pour traduire les événements en appels natifs de Braze, ce qui permet d'accéder à des fonctionnalités plus avancées et à une utilisation plus complète de Braze que l'intégration serveur à serveur.<br><br>Notez que Segment ne prend pas en charge toutes les méthodes Braze (par exemple, Content Cards). Pour utiliser une méthode Braze qui n'est pas mappée via un mappage correspondant, vous devrez invoquer la méthode en ajoutant du code Braze natif à votre base de code. |
| [Serveur à serveur<br>(mode cloud)](#server-to-server-integration) | Transfère les données de Segment vers les endpoints REST API de Braze.<br><br>Ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze telles que les messages in-app, Content Cards ou les notifications push. Il existe également des données capturées automatiquement, telles que les champs au niveau de l'appareil, qui ne sont pas disponibles via cette méthode.<br><br>Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Choose destination framework and connection type #integration-options" }

{% alert note %}
Consultez [Segment](https://segment.com/docs/destinations/#connection-modes) pour en savoir plus sur les deux options d'intégration (modes de connexion), y compris les avantages de chacune.
{% endalert %}

#### Intégration SDK côte à côte {#side-by-side-sdk-integration}

Également appelée mode appareil, cette intégration associe le SDK et les [méthodes](#methods) de Segment au SDK Braze, ce qui permet d'accéder à toutes les fonctionnalités fournies par notre SDK, telles que le push, les messages in-app et d'autres méthodes natives de Braze.

{% alert note %}
Lorsque vous utilisez le mode appareil de Segment, vous n'avez pas besoin d'intégrer directement le SDK Braze. Lors de l'ajout de Braze en tant que destination en mode appareil pour Segment, le SDK Segment initialise le SDK Braze et appelle les méthodes Braze mappées pertinentes.
{% endalert %}

{% alert important %}
Pour les intégrations en mode appareil sur mobile, vous devez ajouter le plugin de destination Braze à votre application en plus de configurer la destination dans le tableau de bord Segment. Le SDK Segment n'inclut pas le plugin Braze par défaut — sans celui-ci, le SDK Segment ne peut pas transmettre les données ou les appels de méthodes mappées à Braze, et les fonctionnalités telles que le push, les messages in-app et Content Cards ne fonctionneront pas. Consultez les onglets spécifiques à chaque plateforme ci-dessous pour les instructions d'installation.
{% endalert %}

Lorsque vous utilisez une connexion en mode appareil, comme si vous intégriez le SDK Braze de manière native, le SDK Braze attribuera un `device_id` et un identifiant backend, `braze_id`, à chaque utilisateur. Cela permet à Braze de capturer l'activité anonyme de l'appareil en faisant correspondre ces identifiants plutôt que `userId`.

{% alert note %}
Si vous utilisez des [filtres de destination](https://segment.com/docs/connections/destinations/destination-filters/) avec des destinations en mode appareil (Kotlin ou Swift), vous devez configurer le plugin de destination avec la prise en charge des filtres activée. Consultez la [documentation sur les filtres de destination](https://segment.com/docs/connections/destinations/destination-filters/) de Segment pour plus de détails sur les versions de plugins prises en charge.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
Le code source de l'intégration en mode appareil Android est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

<br>
Le SDK Braze que vous utilisez dépend du SDK Segment que vous utilisez :

| | SDK Segment | SDK Braze |
| - | ----------- | --------- |
| Recommandé | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Hérité | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Side-by-side SDK integration" }


{% endalert %}

Pour configurer Braze comme destination en mode appareil pour votre source Android, choisissez **Actions** comme **Destination framework**, puis sélectionnez **Save**.

Pour terminer l'intégration côte à côte, vous devez ajouter le [plugin de destination Braze Kotlin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) à votre application Android. Ce plugin fait le lien entre le SDK Segment et le SDK Braze, permettant aux données en mode appareil de circuler vers Braze. Suivez les instructions d'installation de Segment pour ajouter la dépendance du plugin et l'initialiser avec votre instance d'analyse Segment.

Le code source de l'intégration en [mode appareil Android](https://github.com/braze-inc/braze-segment-kotlin) est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

{% endtab %}
{% tab iOS %}

{% alert important %}
Le code source de l'intégration en mode appareil iOS est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

<br>
Le SDK Braze que vous utilisez dépend du SDK Segment que vous utilisez :

| | SDK Segment | SDK Braze |
| - | ----------- | --------- |
| Recommandé | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Hérité | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Side-by-side SDK integration" }
{% endalert %}

Pour configurer Braze comme destination en mode appareil pour votre source iOS, choisissez **Actions** comme **Destination framework**, puis sélectionnez **Save**.

Pour terminer l'intégration côte à côte, vous devez ajouter le [plugin de destination Braze Swift](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) à votre application iOS. Ce plugin fait le lien entre le SDK Segment et le SDK Braze, permettant aux données en mode appareil de circuler vers Braze. Suivez les instructions d'installation de Segment pour ajouter la dépendance du plugin (via Swift Package Manager ou CocoaPods) et l'initialiser avec votre instance d'analyse Segment.

Le code source de l'intégration en [mode appareil iOS](https://github.com/braze-inc/braze-segment-swift) est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

{% endtab %}
{% tab Web ou JavaScript %}

Le framework Braze Web Mode (Actions) de Segment est recommandé pour configurer Braze en tant que destination en mode appareil pour votre source web.

Dans Segment, sélectionnez **Actions** comme framework de destination et **Device Mode** comme mode de connexion.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
Le code source du [plugin React Native Braze](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) est maintenu par Segment et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

Lorsque vous connectez une source Segment React Native à Braze, vous devez configurer une source et une destination par système d'exploitation. Par exemple, vous devez configurer une destination iOS et une destination Android.

Dans la base de code de votre application, initialisez de manière conditionnelle le SDK Segment par type d'appareil, à l'aide de la clé d'écriture source associée à chaque application.

Lorsqu'un jeton de notification push est enregistré depuis un appareil et envoyé à Braze, il est associé à l'identifiant de l'application utilisé lors de l'initialisation du SDK. L'initialisation conditionnelle par type d'appareil permet de confirmer que tous les jetons push envoyés à Braze sont associés à l'application concernée.

{% alert important %}
Si l'application React Native initialise Braze avec le même identifiant d'application Braze pour tous les appareils, tous les utilisateurs React Native seront considérés comme des utilisateurs Android ou iOS dans Braze, et tous les jetons push seront associés à ce système d'exploitation.
{% endalert %}

Pour configurer Braze comme destination en mode appareil pour chaque source, choisissez **Actions** comme **Destination framework**, puis sélectionnez **Save**.

{% endtab %}
{% endtabs %}

#### Intégration serveur à serveur {#server-to-server-integration}

Également appelée mode cloud, cette intégration transmet les données de Segment aux REST API de Braze. Utilisez le framework [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) de Segment pour configurer une destination en mode cloud pour n'importe laquelle de vos sources.

Contrairement à l'intégration côte à côte, l'intégration serveur à serveur ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze, telles que les messages in-app, Content Cards ou l'enregistrement automatique des jetons push. Il existe également des données [capturées automatiquement]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection) (telles que les utilisateurs anonymes et les champs au niveau de l'appareil) qui ne sont pas disponibles via le mode cloud.

Si vous souhaitez utiliser ces données et ces fonctionnalités, envisagez d'utiliser l'intégration SDK côte à côte (mode appareil).

Le code source de la [destination Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) est maintenu par Segment.

### Étape 3 : Paramètres {#step-3-settings}

Définissez les paramètres de votre destination. Tous les paramètres ne s'appliqueront pas à tous les types de destinations.

{% tabs local %}
{% tab Mobile Device-Mode %}

| Paramètre | Description |
| ------- | ----------- |
| Identifiant de l'application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Il figure dans le tableau de bord de Braze sous **Gérer les paramètres**. |
| Endpoint d'API personnalisé<br>(endpoint du SDK) | Votre endpoint du SDK Braze qui correspond à votre instance (par exemple `sdk.iad-01.braze.com`). |
| Région de l'endpoint | Votre instance Braze (par exemple US 01, US 02, EU 01, etc.). |
| Activer l'enregistrement automatique des messages in-app | Désactivez cette option si vous souhaitez enregistrer manuellement les messages in-app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Settings" }

{% endtab %}
{% tab Web Device-Mode %}

| Paramètre | Description |
| ------- | ----------- |
| Identifiant de l'application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Il figure dans le tableau de bord de Braze sous **Gérer les paramètres**. |
| Endpoint d'API personnalisé<br>(endpoint du SDK) | Votre endpoint du SDK Braze qui correspond à votre instance (par exemple `sdk.iad-01.braze.com`). |
| ID push du site Safari | Si vous prenez en charge les notifications push Safari, vous devez spécifier cette option avec l'ID push du site web que vous avez fourni à Apple lors de la création de votre certificat push Safari (commence par `web`, par exemple `web.com.example.domain`). |
| Version du SDK Web de Braze | La version du SDK Web Braze que vous souhaitez utiliser. |
| Envoyer automatiquement les messages in-app | Par défaut, tous les messages in-app auxquels un utilisateur est éligible sont automatiquement envoyés à l'utilisateur. Désactivez cette option si vous souhaitez afficher manuellement les messages in-app. |
| Ne pas charger Font Awesome | Braze utilise Font Awesome pour les icônes de messages in-app. Par défaut, Braze chargera automatiquement FontAwesome depuis le CDN FontAwesome. Pour désactiver ce comportement (par exemple, parce que votre site utilise une version personnalisée de FontAwesome), définissez cette option sur `TRUE`. Notez que dans ce cas, vous êtes responsable de vous assurer que FontAwesome est chargé sur votre site — sinon, les messages in-app risquent de ne pas s'afficher correctement. |
| Activer les messages in-app HTML | L'activation de cette option permettra aux utilisateurs du tableau de bord de Braze d'utiliser des messages in-app HTML. |
| Ouvrir les messages in-app dans un nouvel onglet | Par défaut, les liens issus de clics sur un message in-app sont chargés dans l'onglet actuel ou dans un nouvel onglet, comme indiqué dans le tableau de bord, message par message. Définissez cette option sur `TRUE` pour forcer l'ouverture de tous les liens des messages in-app dans un nouvel onglet ou une nouvelle fenêtre. |
| Index Z des messages in-app | Indiquez une valeur pour cette option afin de remplacer les index Z par défaut de Braze. |
| Exiger le rejet explicite des messages in-app | Par défaut, lorsqu'un message in-app s'affiche, le message peut être fermé en appuyant sur la touche Échap ou en cliquant sur l'arrière-plan grisé de la page. Définissez cette option sur true pour empêcher ce comportement et exiger un clic explicite sur un bouton pour fermer les messages. |
| Intervalle minimal entre les actions de déclenchement en secondes | La valeur par défaut est 30.<br>Par défaut, une action de déclenchement ne se déclenche que si au moins 30 secondes se sont écoulées depuis la dernière action de déclenchement. Indiquez une valeur pour cette option de configuration afin de remplacer cette valeur par défaut par une valeur personnalisée. Nous vous déconseillons de définir cette valeur en dessous de 10 pour éviter de spammer l'utilisateur avec des notifications. |
| Emplacement du service de traitement | Par défaut, lors de l'enregistrement des utilisateurs pour les notifications push web, Braze recherche le fichier de service de traitement requis dans le répertoire racine de votre serveur web à l'adresse `/service-worker.js`. Si vous souhaitez héberger votre service de traitement à un autre chemin sur ce serveur, indiquez une valeur pour cette option correspondant au chemin absolu vers le fichier (par exemple `/mycustompath/my-worker.js`). Notez que définir une valeur ici limite la portée des notifications push sur votre site. Par exemple, dans l'exemple ci-dessus, étant donné que le fichier du service de traitement se trouve dans le répertoire `/mycustompath/`, `requestPushPermission` ne peut être appelé qu'à partir de pages web commençant par `http://yoursite.com/mycustompath/`. |
| Désactiver la maintenance des jetons push | Par défaut, les utilisateurs qui ont déjà accordé l'autorisation push web synchroniseront automatiquement leur jeton push avec le backend Braze lors des nouvelles sessions afin de garantir la livrabilité. Pour désactiver ce comportement, définissez cette option sur `FALSE`. |
| Gérer le service de traitement de manière externe | Si vous avez votre propre service de traitement dont vous enregistrez et contrôlez le cycle de vie, définissez cette option sur `TRUE`, et le SDK Braze n'enregistrera pas ou ne désenregistrera pas de service de traitement. Si vous définissez cette option sur `TRUE`, pour que le push fonctionne correctement, vous devez enregistrer vous-même le service de traitement avant d'appeler `requestPushPermission` et vous assurer qu'il contient le code du service de traitement de Braze, soit avec `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');`, soit en incluant directement le contenu de ce fichier. Lorsque cette option est `TRUE`, l'option `serviceWorkerLocation` est ignorée. |
| Nonce de sécurité du contenu | Si vous indiquez une valeur pour cette option, le SDK Braze ajoutera le nonce à tous les éléments `<script>` et `<style>` créés par le SDK. Cela permet au SDK Braze de fonctionner avec la politique de sécurité du contenu de votre site web. En plus de définir ce nonce, vous devrez peut-être également autoriser le chargement de FontAwesome, ce que vous pouvez faire en ajoutant `use.fontawesome.com` à la liste d'autorisation de votre politique de sécurité du contenu ou en utilisant l'option `doNotLoadFontAwesome` et en le chargeant manuellement. |
| Autoriser l'activité des robots d'exploration | Par défaut, le SDK Web de Braze ignore l'activité des robots ou robots d'exploration connus, tels que Google, en fonction de la chaîne de caractères de l'agent utilisateur. Cela permet d'économiser des points de données, de rendre l'analyse plus précise et peut améliorer le classement des pages. Toutefois, si vous souhaitez que Braze enregistre l'activité de ces robots d'exploration, vous pouvez définir cette option sur `TRUE`. |
| Activer la journalisation | Définissez sur `TRUE` pour activer la journalisation par défaut. Notez que cela obligera Braze à écrire dans la console JavaScript, qui est visible par tous les utilisateurs. Avant de publier votre page en production, vous devez supprimer cela ou fournir un autre enregistreur avec `setLogger`. |
| Autoriser le JavaScript fourni par l'utilisateur | Par défaut, le SDK Web de Braze n'autorise pas les actions de clic JavaScript fournies par l'utilisateur, car cela permet aux utilisateurs du tableau de bord de Braze d'exécuter du JavaScript sur votre site. Pour indiquer que vous faites confiance aux utilisateurs du tableau de bord de Braze pour écrire des actions de clic JavaScript non malveillantes, définissez cette propriété sur `TRUE`. Si `enableHtmlInAppMessages` est `TRUE`, cette option sera également définie sur `TRUE`. |
| Version de l'application | Si vous fournissez une valeur pour cette option, les événements utilisateur envoyés à Braze seront associés à la version donnée, qui peut être utilisée pour la segmentation des utilisateurs. |
| Délai d'expiration de la session en secondes | La valeur par défaut est 30.<br>Par défaut, les sessions expirent après 30 minutes d'inactivité. Indiquez une valeur pour cette option de configuration afin de remplacer cette valeur par défaut par une valeur personnalisée. |
| Liste autorisée des propriétés de l'appareil | Par défaut, le SDK Braze détecte et collecte automatiquement toutes les propriétés de l'appareil dans `DeviceProperties`. Pour modifier ce comportement, fournissez un tableau de `DeviceProperties`. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la distribution dans le fuseau horaire local ne fonctionnera pas sans le fuseau horaire. |
| Localisation | Par défaut, tous les messages visibles par l'utilisateur générés par le SDK seront affichés dans la langue du navigateur de l'utilisateur. Indiquez une valeur pour cette option afin de modifier ce comportement et de forcer l'utilisation d'une langue spécifique. La valeur de cette option doit être un code de langue ISO 639-1. |
| Pas de cookies | Par défaut, le SDK Braze stocke de petites quantités de données (identifiants d'utilisateur, identifiants de session) dans des cookies. Ceci permet à Braze de reconnaître les utilisateurs et les sessions dans les différents sous-domaines de votre site. Si cela vous pose un problème, transmettez `TRUE` pour cette option afin de désactiver le stockage des cookies et de s'appuyer entièrement sur HTML 5 localStorage pour identifier les utilisateurs et les sessions. |
| Suivre toutes les pages | **Mode appareil web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Web Actions où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela enverra tous les [appels de page](https://segment.com/docs/spec/page/) à Braze sous la forme d'un événement « Page chargée/consultée ». |
| Suivre uniquement les pages nommées | **Mode appareil web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Web Actions où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela enverra uniquement les appels de page à Braze avec un nom qui leur est associé. |
| Enregistrer l'achat lorsque le chiffre d'affaires est présent | **Mode appareil web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Web Actions où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Lorsque cette option est activée, tous les appels Track avec la propriété de chiffre d'affaires déclencheront un événement d'achat. |
| Suivre uniquement les utilisateurs connus | **Mode appareil web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Web Actions où ce paramètre peut être activé via des mappages.<br><br>S'il est activé, ce nouveau paramètre retarde l'appel de `window.braze.initialize` jusqu'à ce qu'il y ait un `userId` valide. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Settings" }

{% endtab %}
{% tab Cloud-Mode %}

| Paramètre | Description |
| ------- | ----------- |
| Identifiant de l'application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Il figure dans le tableau de bord de Braze sous **Gérer les paramètres**. |
| Clé REST API | Vous pouvez la trouver dans le tableau de bord de Braze sous **Paramètres** > **Clés API**. |
| Endpoint REST API personnalisé | Votre endpoint REST Braze qui correspond à votre instance (par exemple rest.iad-01.braze.com). |
| Mettre à jour les utilisateurs existants uniquement | **Mode cloud de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Cloud Actions où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Détermine s'il faut uniquement mettre à jour les utilisateurs existants. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Settings" }

{% endtab %}
{% endtabs %}

### Étape 4 : Mapper les méthodes {#methods}

Braze prend en charge les méthodes Segment [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) et [Track](https://segment.com/docs/spec/track/). Les types d'identifiants utilisés dans ces méthodes varient selon que les données sont envoyées via une intégration serveur à serveur (mode cloud) ou côte à côte (mode appareil). Dans les destinations Braze Web Mode Actions et Cloud Mode Actions, vous pouvez également choisir de configurer un mappage pour un [appel d'alias Segment](https://segment.com/docs/connections/spec/alias/).

{% alert note %}
Bien que les alias d'utilisateur soient pris en charge en tant qu'identifiant dans la destination Braze Cloud Mode (Actions), il convient de noter que l'appel d'alias de Segment n'est pas directement lié aux alias d'utilisateur Braze.
{% endalert %}

| Type d'identifiant | Destination prise en charge |
| --------------- | --------------------- |
| `userId` (`external_id`) | Toutes |
| Utilisateur anonyme | Destinations en mode appareil |
| Alias d'utilisateur | Destinations en mode cloud |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Map methods #methods" }

La destination Cloud Mode (Actions) propose une [action Créer un alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) qui peut être utilisée pour créer un utilisateur uniquement avec un alias ou pour ajouter un alias à un profil `external_id` existant. L'[action Identifier l'utilisateur](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) peut être utilisée conjointement avec l'action Créer un alias pour fusionner un utilisateur uniquement avec un alias avec un `external_id` une fois que celui-ci est devenu disponible pour l'utilisateur.

Il est également possible de concevoir une solution de contournement et d'utiliser `braze_id` pour envoyer des données utilisateur anonymes en mode cloud. Cela nécessite d'inclure manuellement le `braze_id` de l'utilisateur dans tous vos appels d'API Segment. Pour en savoir plus sur la configuration de cette solution de contournement, consultez la [documentation de Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Les données de destination envoyées à Braze peuvent être regroupées par lots dans Cloud Mode Actions. La taille des lots est limitée à 75 événements, et ces lots s'accumuleront sur une période de 30 secondes avant d'être vidés. Le traitement par lots des requêtes est effectué par action. Par exemple, les appels Identify (attributs) seront regroupés dans une requête et les appels Track (événements personnalisés) seront regroupés dans une seconde requête. Braze recommande d'activer cette fonctionnalité car elle réduira le nombre de requêtes envoyées de Segment à Braze. Cela réduira à son tour le risque que la destination atteigne les limites de débit de Braze et retente les requêtes.

Vous pouvez activer le traitement par lots pour une action en accédant à votre destination Braze > **Mappings**. À partir de là, cliquez sur l'icône à 3 points à droite du mappage et sélectionnez **Edit Mapping**. Faites défiler vers le bas de la section **Select mappings** et assurez-vous que **Batch Data to Braze** est défini sur **Yes**.


{% tabs local %}
{% tab Identify %}
#### Identify

L'appel [Identify](https://segment.com/docs/spec/identify/) vous permet de lier un utilisateur à ses actions et d'enregistrer des attributs le concernant.

Certains traits spéciaux de Segment correspondent à des champs de profil d'attributs standard dans Braze :

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

D'autres champs de profil Braze réservés tels que `email_subscribe` et `push_subscribe` peuvent être envoyés en utilisant la convention de nommage Braze pour ces champs et en les transmettant en tant que traits dans un appel Identify.

##### Ajouter un utilisateur à un groupe d'abonnement {#adding-a-user-to-a-subscription-group}

Vous pouvez également abonner ou désabonner un utilisateur d'un groupe d'abonnement donné à l'aide des champs suivants dans le paramètre traits.

Utilisez le champ de profil Braze réservé appelé `braze_subscription_groups`, qui peut être associé à un tableau d'objets. Chaque objet du tableau doit avoir deux clés réservées :

1. `subscription_group_state` : indique si l'utilisateur est `"subscribed"` ou `"unsubscribed"` d'un groupe d'abonnement spécifique.
2. `subscription_group_id` : représente l'ID unique du groupe d'abonnement. Vous pouvez trouver cet ID dans le tableau de bord de Braze sous **Gestion des groupes d'abonnement**.

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

Tous les autres traits seront enregistrés en tant qu'[attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| Identify avec un ID utilisateur | Définir un ID externe | Segment : `analytics.identify("dawei");`<br>Braze : `Braze.changeUser("dawei")` |
| Identify avec des traits réservés | Définir les attributs de l'utilisateur | Segment : `analytics.identify({email: "dawei@braze.com"});`<br> Braze : `Braze.getUser().setEmail("dawei@braze.com");`
| Identify avec des traits personnalisés | Définir des attributs personnalisés | Segment : `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze : `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify avec un ID utilisateur et des traits | Segment : définir un ID externe et un attribut | Combinez les méthodes précédentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom attributes" }

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) et [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), les mappages ci-dessus peuvent être définis à l'aide de l'action Update User Profile.

{% alert important %}
Lorsque vous transmettez des données d'attributs utilisateur, vérifiez que vous ne transmettez que des valeurs pour les attributs qui ont changé depuis la dernière mise à jour. Vous éviterez ainsi d'enregistrer inutilement des points de données. Pour les sources côté client, utilisez l'outil [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) open source de Segment pour optimiser votre intégration et limiter l'utilisation des points de données en supprimant les appels `identify()` dupliqués provenant de Segment.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

Lorsque vous suivez un événement, nous l'enregistrons en tant qu'[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) en utilisant le nom fourni.

Les métadonnées envoyées dans l'objet de propriétés de l'appel Track seront enregistrées dans Braze en tant que propriétés d'événement personnalisées pour l'événement associé. Tous les [types de données de propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/) sont pris en charge.

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) et [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), les mappages ci-dessus peuvent être définis à l'aide de l'action Track Event.

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Enregistré en tant qu'[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events). | Segment : `analytics.track("played_game");` <br>Braze : `Braze.logCustomEvent("played_game");`|
| [Track avec propriétés](https://segment.com/docs/spec/track/) | Enregistré en tant que [propriété d'événement]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/). | Segment : `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze : `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track avec produit](https://segment.com/docs/spec/track/) | Enregistré en tant qu'[événement d'achat]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment : `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze : `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### Commande terminée {#order-completed}

Lorsque vous suivez un événement portant le nom `Order Completed` en utilisant le format décrit dans l'[API eCommerce](https://segment.com/docs/spec/ecommerce/v2/) de Segment, nous enregistrons les produits que vous avez répertoriés en tant qu'[achats]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) et [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), le mappage par défaut peut être personnalisé via l'action Track Purchase.

{% endtab %}

{% tab Page %}
#### Page {#page}

L'appel [Page](https://segment.com/docs/spec/page/) vous permet d'enregistrer chaque fois qu'un utilisateur voit une page de votre site web, ainsi que toutes les propriétés facultatives relatives à cette page.

Ce type d'événement peut être utilisé comme déclencheur dans les destinations Web Mode Actions et Cloud Actions pour enregistrer un événement personnalisé dans Braze.
{% endtab %}

{% endtabs %}

### Étape 5 : Tester votre intégration {#step-5-test-your-integration}

Lorsque vous utilisez l'intégration côte à côte (mode appareil), vos indicateurs d'[aperçu]({{site.baseurl}}/user_guide/analytics/dashboards/home/) (sessions à vie, MAU, DAU, adhérence, sessions quotidiennes et sessions quotidiennes par MAU) peuvent être utilisés pour vérifier que Braze reçoit des données de Segment.

Vous pouvez consulter vos données sur les pages des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data) ou du [chiffre d'affaires]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data), ou en [créant un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment). La page **Événements personnalisés** du tableau de bord vous permet de consulter le nombre d'événements personnalisés au fil du temps. Notez que vous ne pourrez pas utiliser de [formules]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula) incluant les statistiques MAU et DAU lors de l'utilisation d'une intégration serveur à serveur (mode cloud).

Si vous envoyez des données d'achat à Braze (voir la commande terminée dans l'onglet **Track** de l'[étape 3](#methods)), la page du [chiffre d'affaires]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) vous permet de consulter les données relatives aux revenus ou aux achats sur des périodes spécifiques ou le chiffre d'affaires total de votre application.

[Créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) vous permet de filtrer vos utilisateurs en fonction des données d'événements personnalisés et d'attributs.

{% alert important %}
Si vous utilisez une intégration serveur à serveur (mode cloud), les filtres liés aux données de session collectées automatiquement (tels que « première utilisation de l'application » et « dernière utilisation de l'application ») ne fonctionneront pas. Utilisez une intégration côte à côte (mode appareil) si vous souhaitez les utiliser dans votre intégration Segment et Braze.
{% endalert %}

## Suppression et blocage d'utilisateurs {#user-deletion-and-suppression}

Si vous devez supprimer ou bloquer des utilisateurs, notez que la [fonctionnalité de suppression d'utilisateurs de Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **est** mappée à l'endpoint Braze [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). Notez que la vérification de ces suppressions peut prendre jusqu'à 30 jours.

Vous devez vous assurer de sélectionner un identifiant utilisateur commun entre Braze et Segment (comme `external_id`). Une fois que vous avez lancé une requête de suppression avec Segment, vous pouvez consulter son état dans l'onglet des requêtes de suppression de votre tableau de bord Segment.

## Rediffusions Segment {#segment-replays}

Segment fournit un service aux clients qui leur permet de « retransmettre » toutes les données historiques à un nouveau partenaire technologique. Les nouveaux clients de Braze qui souhaitent importer toutes les données historiques pertinentes peuvent le faire via Segment. Adressez-vous à votre représentant Segment si cela vous intéresse.

Segment se connectera à notre [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour importer les données utilisateur dans Braze en votre nom.

{% alert important %}
Tous les identifiants pris en charge dans la destination Cloud Mode Actions sont pris en charge dans le cadre des rediffusions Segment.
{% endalert %}

## Bonnes pratiques {#best-practices}

{% details Passez en revue les cas d'utilisation pour éviter les dépassements de données. %}

Segment **ne limite pas** le nombre d'éléments de données que les clients leur envoient. Segment vous permet de tout envoyer ou de décider quels événements vous enverrez à Braze. Plutôt que d'envoyer tous vos événements via Segment, nous vous suggérons de passer en revue les cas d'utilisation avec vos équipes marketing et éditoriales afin de déterminer quels événements vous enverrez à Braze pour éviter les dépassements de données.

{% enddetails %}

{% details Comprenez la différence entre l'endpoint d'API personnalisé et l'endpoint REST API personnalisé dans les paramètres de destination en mode appareil mobile. %}

| Terminologie Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | Endpoint d'API personnalisé |
| Endpoint REST de Braze | Endpoint REST API personnalisé |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best practices" }

Votre endpoint d'API Braze (appelé « endpoint d'API personnalisé » dans Segment) est l'endpoint du SDK que Braze configure pour votre SDK (par exemple `sdk.iad-03.braze.com`). Votre endpoint REST API Braze (appelé « endpoint REST API personnalisé » dans Segment) est l'endpoint REST API (par exemple `https://rest.iad-03.braze.com`).
{% enddetails %}

{% details Assurez-vous que votre endpoint d'API personnalisé est correctement saisi dans les paramètres de destination en mode appareil mobile. %}

| Terminologie Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | Endpoint d'API personnalisé |
| Endpoint REST de Braze | Endpoint REST API personnalisé |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best practices" }

Le format approprié doit être respecté pour vous assurer de saisir correctement votre endpoint du SDK Braze. Votre endpoint du SDK Braze ne doit pas inclure `https://` (par exemple `sdk.iad-03.braze.com`), sinon l'intégration de Braze sera interrompue. Cela est nécessaire car Segment ajoute automatiquement le préfixe `https://` à votre endpoint, ce qui entraînerait l'initialisation de Braze avec un endpoint non valide `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Nuances du mappage des données. %}

Scénarios dans lesquels les données ne sont pas transmises comme prévu :

1. Attributs personnalisés imbriqués
  - Bien que les [attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/) puissent techniquement être envoyés à Braze via Segment, le **payload complet** sera envoyé à chaque fois. Cela entraînera des [points de données]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points) par clé transmise dans l'objet imbriqué chaque fois que le payload est envoyé.<br><br> Pour ne dépenser qu'un sous-ensemble de points de données lors de l'envoi du payload, vous pouvez utiliser la fonctionnalité de [fonctions de destination](https://segment.com/docs/connections/functions/destination-functions/) personnalisées appartenant à Segment. Cette fonctionnalité de la plateforme Segment vous permet de personnaliser la manière dont les données sont envoyées vers les destinations en aval.

  {% alert note %}
  Les fonctions de destination personnalisées sont contrôlées dans Segment, et Braze a une visibilité limitée sur les fonctions configurées en externe.
  {% endalert %}

{: start="2"}
2. Transmission de données anonymes de serveur à serveur.
  - Les clients peuvent utiliser les bibliothèques serveur à serveur de Segment pour transmettre des données anonymes vers d'autres systèmes. Consultez la section sur les méthodes de mappage pour en savoir plus sur l'envoi d'utilisateurs sans `external_id` vers Braze via une intégration serveur à serveur (mode cloud).

{% enddetails %}

{% details Personnalisation de l'initialisation de Braze. %}

Braze peut être personnalisé de différentes manières : push, messages in-app, Content Cards et initialisation. Grâce à une intégration côte à côte, vous pouvez toujours personnaliser le push, les messages in-app et Content Cards comme vous le feriez avec une intégration directe de Braze.

Cependant, il peut être difficile, voire impossible, de personnaliser le moment où le SDK Braze est intégré ou de spécifier des configurations d'initialisation. En effet, Segment initialisera le SDK Braze pour vous lors de l'initialisation de Segment.

{% enddetails %}

{% details Envoi des deltas à Braze. %}

Lorsque vous transmettez des données d'attributs utilisateur, vérifiez que vous ne transmettez que des valeurs pour les attributs qui ont changé depuis la dernière mise à jour. Vous éviterez ainsi l'enregistrement de points de données inutiles. Pour les sources côté client, utilisez l'outil [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) open source de Segment pour optimiser votre intégration et limiter l'utilisation des points de données en supprimant les appels `identify()` dupliqués provenant de Segment.

{% enddetails %}

{% details Utilisez le bon centre de données Braze. %}

Segment utilise votre centre de données Braze pour récupérer l'endpoint REST Braze approprié (par exemple `https://rest.iad-01.braze.com`) pour effectuer les appels serveur à serveur.

{% enddetails %}

{% details Supprimez l'endpoint REST API personnalisé lors de l'utilisation de l'Event Tester de Segment. %}

L'Event Tester de Segment envoie des événements à l'endpoint REST API `/users/track` de Braze et renvoie une erreur `401 Invalid API Key` si un endpoint REST API personnalisé est défini dans les paramètres de destination Braze, même lorsque cet endpoint est correct. Supprimez la valeur de l'endpoint REST API personnalisé dans Segment pour permettre à l'Event Tester de fonctionner correctement.

{% enddetails %}

{% details Prévoyez un délai pour les mises à jour après la configuration d'une nouvelle source. %}

Segment conserve vos paramètres de configuration en cache pendant une longue période. Ainsi, lors de la configuration d'une nouvelle source (par exemple, le passage du mode cloud au mode appareil), votre application peut ne pas afficher le nouveau comportement ou les nouvelles données tant que le cache n'est pas renouvelé. Gardez ce délai à l'esprit lorsque vous prévoyez d'ajouter une source.

{% enddetails %}