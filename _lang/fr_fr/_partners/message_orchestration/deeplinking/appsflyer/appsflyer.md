---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Cet article de référence décrit le partenariat entre Braze et AppsFlyer, une plateforme d'analyse et d'attribution de marketing mobile qui vous aide à analyser et à optimiser vos applications."
page_type: partner
search_tag: Partner
---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [AppsFlyer](https://www.appsflyer.com/) est une plateforme d'analyse et d'attribution de marketing mobile qui vous aide à analyser et à optimiser vos applications grâce à l'analyse marketing, l'attribution mobile et la création de liens profonds.

L'intégration de Braze et AppsFlyer vous permet de mieux comprendre comment optimiser et créer des campagnes plus complètes en tirant parti des données d'attribution d'installation mobile d'AppsFlyer.

Vous pouvez également transmettre vos audiences AppsFlyer (cohortes) directement à Braze avec l'intégration [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences), ce qui vous permet de créer des campagnes d'engagement client puissantes ciblant les bons utilisateurs au bon moment.

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte AppsFlyer | Un compte AppsFlyer est nécessaire pour tirer parti de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, des extraits de code peuvent être nécessaires dans votre application. Les détails sur ces exigences se trouvent à l'étape 1 du processus d'intégration. |
| SDK AppsFlyer | En plus du SDK Braze requis, vous devez installer le [SDK AppsFlyer](https://dev.appsflyer.com/hc/docs/getting-started).
| Configuration du domaine e-mail terminée | Vous devez avoir terminé l'[étape de configuration des IP et domaines]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains) lors de la configuration de votre e-mail pendant l'onboarding de Braze. |
| Certificat SSL | Votre [certificat SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) doit être configuré. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Mapper l'ID de l'appareil {#step-1-map-device-id}

{% tabs local %}
{% tab Android %}
Si vous avez une application Android, vous devez transmettre un identifiant d'appareil Braze unique à AppsFlyer.

Assurez-vous que les lignes de code suivantes sont insérées au bon endroit — après le lancement du SDK Braze et avant le code d'initialisation du SDK AppsFlyer. Consultez le [guide d'intégration du SDK Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) d'AppsFlyer pour plus d'informations.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
Avant février 2023, notre intégration d'attribution AppsFlyer utilisait l'identifiant du fournisseur (IDFV) comme identifiant principal pour faire correspondre les données d'attribution iOS. Il n'est pas nécessaire pour les clients Braze utilisant Objective-C de récupérer le `device_id` Braze et de l'envoyer à AppsFlyer lors de l'installation, car il n'y a pas d'interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser l'IDFV comme identifiant commun, vous devez confirmer que le champ `useUUIDAsDeviceId` est défini sur `false` afin d'éviter une interruption de l'intégration.

S'il est défini sur `true`, vous devez implémenter le mappage de l'ID de l'appareil iOS pour Swift afin de transmettre le `device_id` Braze à AppsFlyer lors de l'installation de l'application, pour que Braze puisse correctement faire correspondre les attributions iOS.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab unity %}
Pour mapper l'ID de l'appareil dans Unity, utilisez le code suivant :

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation des données Braze {#step-2-get-the-braze-data-import-key}

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **AppsFlyer**.

Vous y trouverez l'endpoint REST et pourrez générer votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez en créer une nouvelle ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'AppsFlyer.<br><br>![La boîte « Importation des données pour l'attribution d'installation » disponible sur la page technologique AppsFlyer. Cette boîte contient la clé d'importation des données et l'endpoint REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Étape 3 : Configurer Braze dans le tableau de bord d'AppsFlyer {#step-3-configure-braze-in-appsflyers-dashboard}

1. Dans AppsFlyer, accédez à la page **Integrated Partners** depuis le menu de navigation. Recherchez ensuite **Braze** et sélectionnez le logo Braze pour ouvrir une fenêtre de configuration.
2. Dans l'onglet **Integration**, activez **Activate Partner**.
3. Fournissez la clé d'importation des données et l'endpoint REST que vous avez trouvés dans le tableau de bord de Braze.
4. Désactivez **Advanced Privacy** et enregistrez votre configuration.

{% alert important %}
Lorsque vous saisissez l'endpoint REST de Braze dans l'onglet Integration d'AppsFlyer, entrez uniquement le domaine (par exemple, `rest.fra-02.braze.eu`) sans le protocole `https://` et sans le chemin `/attribution/appsflyer`. AppsFlyer ajoute automatiquement le protocole en préfixe et le chemin en suffixe. Inclure l'un ou l'autre dans votre saisie provoque des échecs de postback.
{% endalert %}

Des informations supplémentaires sur ces instructions sont disponibles dans la [documentation d'AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Étape 4 : Confirmer l'intégration {#step-4-confirm-the-integration}

Sur la page des partenaires technologiques AppsFlyer dans Braze, l'indicateur de connexion affiche **Not Connected** jusqu'à ce que vous génériez une clé API d'importation des données à l'étape 2. Après avoir généré la clé, l'indicateur passe à **Connected** et affiche un horodatage. Cet horodatage reflète le moment où l'intégration a été initialement configurée dans Braze (lorsque la clé d'importation des données a été créée), et non la dernière fois qu'AppsFlyer a envoyé un postback.

Pour confirmer que les données d'attribution d'installation circulent depuis AppsFlyer, utilisez l'étape 5 pour vérifier que les données d'installation non organique apparaissent dans les filtres Segment de Braze. Braze ignore les installations organiques provenant des postbacks AppsFlyer et ne les stocke pas comme données d'installation attribuées.

### Étape 5 : Visualiser les données d'attribution des utilisateurs {#step-5-viewing-user-attribution-data}

#### Champs de données disponibles {#available-data-fields}

Si votre intégration a réussi, Braze mappe toutes les données d'installation non organique vers les filtres Segment.

| Champ de données AppsFlyer | Filtre Segment Braze |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs de données disponibles" }

Vous pouvez segmenter votre base d'utilisateurs par données d'attribution dans le tableau de bord de Braze en utilisant les filtres d'attribution d'installation.

![Quatre filtres disponibles. Le premier est « Install Attribution Source is network_val_0 ». Le deuxième est « Install Attribution Source is campaign_val_0 ». Le troisième est « Install Attribution Source is adgroup_val_0 ». Le quatrième est « Install Attribution Source is creative_val_0 ». À côté des filtres listés, vous pouvez voir comment ces sources d'attribution seront ajoutées au profil utilisateur. Dans la boîte « Install Attribution » sur la page d'informations d'un utilisateur, Install Source est listé comme network_val_0, campaign est listé comme campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

De plus, les données d'attribution pour un utilisateur particulier sont disponibles sur le profil de chaque utilisateur dans le tableau de bord de Braze.

{% alert note %}
Les données d'attribution pour les Campaigns Facebook et X (anciennement Twitter) ne sont pas disponibles via nos partenaires. Ces sources média ne permettent pas à leurs partenaires de partager les données d'attribution avec des tiers, et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.
{% endalert %}

## Intégrer AppsFlyer avec Braze pour la création de liens profonds {#integrate-appsflyer-with-braze-for-deep-linking}

Les deep links&#8212;des liens qui dirigent les utilisateurs vers une page ou un emplacement spécifique au sein d'une application ou d'un site web&#8212;sont utilisés pour créer une expérience utilisateur sur mesure.

Bien que largement utilisés, des problèmes peuvent survenir lors de l'utilisation de deep links dans des e-mails avec le suivi des clics&#8212;une autre fonctionnalité importante utilisée pour collecter les données utilisateur. Ces problèmes sont dus au fait que les fournisseurs de services d'e-mail marketing or e-mailing (fournisseur de services d'e-mailing) encapsulent les deep links dans un domaine d'enregistrement des clics, ce qui casse le lien original. Par conséquent, la prise en charge des deep links nécessite une configuration supplémentaire.

AppsFlyer fournit un [service](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) qui évite ces problèmes, en permettant à AppsFlyer de servir d'intermédiaire entre le serveur fournisseur de services d'e-mailing et votre nom de domaine. Son rôle de proxy permet de fournir des fichiers d'association (AASA/asset links), ce qui facilite la création de liens profonds.

## Étape 1 - Créer un domaine de suivi des clics {#step-1-create-a-click-tracking-domain}

En suivant les éléments initiaux du [guide de configuration des e-mails de Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate), créez un domaine d'envoi d'e-mails et un domaine de suivi des clics. Pour obtenir de l'aide, vous pouvez créer un ticket via le tableau de bord de Braze afin de lancer la configuration du nouveau domaine de suivi des clics avec l'équipe e-mail de Braze.

![L'interface de Braze montrant le bouton « Get Help » sous le bouton « Support » dans la barre de navigation supérieure.]({% image_buster /assets/img/attribution/appsflyer/1.png %})

La création d'un nouveau domaine de suivi des clics est obligatoire, même si vous en utilisez déjà un. Cela garantit qu'il n'y a aucun impact sur le trafic des Campaigns d'e-mails en cours.

{% alert important%}
AppsFlyer crée le certificat SSL. À ce stade, les liens des e-mails ne sont probablement pas sécurisés, ce qui signifie que le préfixe de l'URL est HTTP au lieu de HTTPS. Ce problème est résolu dans les étapes suivantes.
{%endalert%}

## Étape 2 - Créer un modèle OneLink dans AppsFlyer {#step-2-create-a-onelink-template-in-appsflyer}
Créez un [modèle OneLink](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) et configurez les Universal Links/App Links sous « When app is installed ». Ce modèle sera utilisé ultérieurement pour créer des liens OneLink pour vos Campaigns par e-mail.

{% alert note%} Si vous disposez déjà d'un modèle OneLink existant configuré pour activer les Universal Links/App Links, vous pouvez l'utiliser.
{%endalert%}

## Étape 3 - Configurer votre intégration Braze dans AppsFlyer {#step-3-set-up-your-braze-integration-in-appsflyer}
Il est maintenant temps de configurer votre intégration Braze dans AppsFlyer. Cette étape et la suivante (« Configurer votre application ») peuvent être effectuées simultanément.
Pour configurer votre intégration Braze dans AppsFlyer :

### 1. Dans AppsFlyer, depuis le menu latéral, sélectionnez Engage > fournisseur de services d'e-mailing integration. {#1-in-appsflyer-from-the-side-menu-select-engage-esp-integration}
![Interface AppsFlyer montrant le bouton « ESP Integration » dans le menu de navigation.]({% image_buster /assets/img/attribution/appsflyer/2.png %})


### 2. Sélectionnez Braze. {#2-select-braze}
![Interface AppsFlyer montrant la liste des intégrations ESP, y compris Braze.]({% image_buster /assets/img/attribution/appsflyer/3.png %})


### 3. Sélectionnez le modèle OneLink que vous souhaitez utiliser pour les Campaigns par e-mail, puis cliquez sur Next. {#3-select-the-onelink-template-you-want-to-use-for-email-campaigns-then-click-next}
![Interface AppsFlyer montrant le menu déroulant permettant aux utilisateurs de sélectionner leur modèle.]({% image_buster /assets/img/attribution/appsflyer/4.png %})


### 4. Saisissez votre domaine de suivi des clics et la valeur « Braze endpoint », qui a été fournie avec le nouveau CTD créé à l'étape 1, puis cliquez sur Validate connection. {#4-enter-your-click-tracking-domain-and-braze-endpoint-value-which-was-provided-with-the-new-ctd-created-in-step-1-then-click-validate-connection}

Cela permet de vérifier que le domaine de suivi des clics pointe vers l'endpoint que vous avez saisi.

![Interface AppsFlyer indiquant où les clients doivent ajouter leur domaine de suivi des clics et les informations associées.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

Par « Braze Endpoint », AppsFlyer demande les informations fournies par Braze à l'étape 1 de ce guide, en particulier le nouveau CTD.

Cliquez ensuite sur **Validate connection**, ce qui vérifie que le domaine de suivi des clics pointe vers l'endpoint que vous avez saisi.
Une fois terminé, cliquez sur **Next**.

### 5. Acheminer le trafic des liens vers AppsFlyer : {#5-route-link-traffic-to-appsflyer}

#### a. Copiez et envoyez les instructions préfabriquées personnalisées dans AppsFlyer à votre administrateur informatique ou de domaine. {#a-copy-and-send-the-customized-pre-fabricated-instructions-in-appsflyer-to-your-it-or-domain-administrator}

Votre administrateur doit rediriger le trafic de vos Campaigns par e-mail des serveurs fournisseur de services d'e-mailing vers les serveurs AppsFlyer en mettant à jour vos enregistrements DNS CNAME avec le nouveau domaine fourni par AppsFlyer.

Ainsi, chaque fois qu'un lien est cliqué, le clic est redirigé vers AppsFlyer, qui à son tour le redirige vers l'endpoint fournisseur de services d'e-mailing.

![Diagramme illustrant comment les données de clics transitent depuis votre domaine vers AppsFlyer, puis vers votre endpoint ESP.]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. Après avoir copié et envoyé les instructions, cliquez sur Done. {#b-after-copying-and-sending-the-instructions-click-done}
Votre intégration Braze a été créée.

{%alert important%}
Le statut de votre intégration Braze est en attente et ne commence à fonctionner qu'après le mappage de l'enregistrement CNAME. Il peut s'écouler jusqu'à 24 heures après le mappage pour qu'une nouvelle intégration commence à fonctionner et devienne active.
{%endalert%}

## Étape 4 : Configurer votre application (tâche développeur) {#step-4-configure-your-app-developer-task}
AppsFlyer [propose des instructions](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) sur la configuration correcte de l'application, que vos équipes web ou applicatives doivent suivre pour prendre en charge les liens universels.

## Étape 5 : Confirmer que le suivi des clics SSL est activé avec Braze {#step-5-confirm-ssl-click-tracking-is-enabled-with-braze}

À ce stade, après avoir partagé et validé les détails CTD dans AppsFlyer, nous vous recommandons d'effectuer un envoi test pour vérifier si votre domaine d'envoi OneLink dispose d'un certificat SSL. Cela est conforme à notre guide de [configuration des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).

Vous pouvez effectuer l'assurance qualité et la résolution des problèmes en envoyant un deep link à l'aide de OneLink. Consultez la [documentation AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) pour plus de détails sur l'utilisation de OneLink.

Si les liens CTD sont identifiés comme HTTP, contactez l'équipe Email Ops de Braze pour activer le suivi des clics SSL. Cela garantit que tous les liens HTTP sont automatiquement convertis en HTTPS.
Vous pouvez utiliser le texte de message suivant lorsque vous contactez votre gestionnaire du succès des clients, ou en créant un ticket dans le tableau de bord de Braze comme à l'étape 1 :

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS.
```

### URL de suivi des clics AppsFlyer dans Braze (facultatif) {#appsflyer-click-tracking-urls-in-braze-optional}

Vous pouvez utiliser les [liens d'attribution OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) d'AppsFlyer dans les Campaigns Braze pour les notifications push, les e-mails et d'autres canaux. Cela vous permet de renvoyer les données d'attribution d'installation ou de réengagement de vos Campaigns Braze vers AppsFlyer. Vous pouvez ainsi mesurer vos efforts marketing plus efficacement et prendre des décisions basées sur les données.

Vous pouvez simplement créer votre URL de suivi OneLink dans AppsFlyer et l'insérer directement dans vos Campaigns Braze. AppsFlyer utilise ensuite ses [méthodologies d'attribution probabiliste](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter un identifiant d'appareil à vos liens de suivi AppsFlyer afin d'améliorer la précision des attributions de vos Campaigns Braze. Cela permet d'attribuer de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients d'activer la [collecte de l'identifiant publicitaire Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id). L'intégration du SDK AppsFlyer collecte également le GAID. Vous pouvez inclure le GAID dans vos liens de suivi des clics AppsFlyer en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et AppsFlyer collectent automatiquement l'IDFV de manière native via nos intégrations SDK. Vous pouvez utiliser l'IDFV comme identifiant d'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics AppsFlyer en utilisant la logique Liquid suivante :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}