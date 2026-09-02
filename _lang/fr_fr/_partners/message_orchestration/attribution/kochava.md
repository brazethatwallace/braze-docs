---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Cet article de référence décrit le partenariat entre Braze et Kochava, une plateforme d'attribution mobile qui propose des informations d'attribution et d'analyse pour vous aider à exploiter vos données et renforcer votre croissance."
page_type: partner
search_tag: Partner

---

# Kochava

> [Kochava](https://www.kochava.com/) propose l'attribution et l'analyse mobile pour vous aider à exploiter vos données et favoriser votre croissance. La plateforme d'audience de Kochava vous permet de planifier, cibler, activer, mesurer et optimiser vos campagnes d'applications.

_Cette intégration est maintenue par Kochava._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Kochava contribue à une compréhension plus globale de vos campagnes en envoyant des données d'attribution à Braze afin de mieux comprendre quelles campagnes génèrent des installations, des activités in-app, et plus encore.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Kochava | Un compte Kochava est nécessaire pour bénéficier de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des informations détaillées sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK Kochava | En plus du SDK Braze requis, vous devez installer le [SDK Kochava](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

### Étape 1 : Mapper les ID utilisateur {#step-1-map-user-ids}

#### Android

Le SDK [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) génère un identifiant unique global (GUID) en tant qu'ID Braze au démarrage de la session. Cet identifiant doit être transmis à la méthode Kochava `IdentityLink` afin que Braze puisse réconcilier les données avec le profil utilisateur correct. Récupérez l'ID Braze à l'aide de la méthode suivante :

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Avant février 2023, notre intégration d'attribution Kochava utilisait l'identifiant du fournisseur (IDFV) comme identifiant principal pour faire correspondre les données d'attribution iOS. Il n'est pas nécessaire pour les clients de Braze utilisant Objective-C de récupérer le `device_id` de Braze et de l'envoyer à Kochava lors de l'installation, car il n'y a pas d'interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0 et versions ultérieures, si vous souhaitez continuer à utiliser l'IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin de ne pas perturber l'intégration. Si ce paramètre est défini sur `true`, vous devez implémenter le mappage des ID d'appareils iOS pour Swift afin de transmettre le `device_id` Braze à Kochava lors de l'installation de l'application pour que Braze puisse correctement faire correspondre les attributions iOS.

Braze possède deux API qui produiront la même valeur, l'une avec un gestionnaire de complétion et l'autre avec le nouveau support de concurrence Swift. Notez que vous devrez modifier les extraits de code suivants pour vous conformer aux instructions du [SDK iOS](https://support.kochava.com/sdk-integration/ios-sdk-integration/) de Kochava. Pour obtenir de l'aide supplémentaire, contactez le service d'assistance de Kochava.

##### Gestionnaire de complétion {#completion-handler}
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Concurrence Swift {#swift-concurrency}
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Étape 2 : Obtenir la clé d'importation des données Braze {#step-2-get-the-braze-data-import-key}

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Kochava**.

Vous y trouverez l'endpoint REST et pourrez générer votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Kochava.<br><br>![Cette image montre la zone « Importation de données pour l'attribution d'installation » qui se trouve sur la page technologique de Kochava. Dans cette zone, vous pouvez voir la clé d'importation des données et l'endpoint REST.]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### Étape 3 : Configurer un postback depuis Kochava {#step-3-set-up-a-postback-from-kochava}

[Ajoutez un postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) dans votre tableau de bord de Kochava. Vous serez invité à indiquer la clé d'importation des données et l'endpoint REST que vous avez trouvés dans le tableau de bord de Braze.

### Étape 4 : Confirmer l'intégration {#step-4-confirm-the-integration}

Après que Braze a reçu des données d'attribution de Kochava, l'indicateur de statut de connexion sur la page des partenaires technologiques de Kochava dans Braze passe de « Not Connected » à « Connected » et inclut un horodatage de la dernière requête réussie.

Ce statut ne change que lorsque Braze reçoit des données concernant une installation attribuée. Braze ignore les installations organiques (il les exclut du postback de Kochava) et ne les comptabilise pas pour déterminer si la connexion est réussie.

## Données d'attribution Facebook et X (anciennement Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques n'autorisent pas leurs partenaires à partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics Kochava dans Braze (facultatif) {#kochava-click-tracking-urls-in-braze-optional}

L'utilisation de liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes génèrent des installations d'applications et du réengagement. Ainsi, vous serez en mesure de mesurer vos efforts marketing de manière plus efficace et de prendre des décisions fondées sur les données pour investir davantage de ressources là où le ROI or retour sur investissement est maximal.

Pour démarrer avec les liens de suivi des clics Kochava, consultez leur [documentation](https://support.kochava.com/reference-information/attribution-overview/). Vous pouvez insérer les liens de suivi des clics Kochava directement dans vos campagnes Braze. Kochava utilisera ensuite [ses méthodologies d'attribution probabilistes](https://www.kochava.com/getting-prepared-for-ios-14/) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter un identifiant d'appareil à vos liens de suivi Kochava afin d'améliorer la précision des attributions issues de vos campagnes Braze. Cela permettra d'attribuer de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s'abonner à la [collecte de l'identifiant publicitaire Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté de manière native via l'intégration du SDK Kochava. Vous pouvez inclure le GAID dans vos liens de suivi des clics Kochava en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Kochava collectent automatiquement l'IDFV de manière native via nos intégrations SDK. Celui-ci peut être utilisé comme identifiant d'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics Kochava en utilisant la logique Liquid suivante :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Cette recommandation est purement facultative**<br>
Si vous n'utilisez actuellement aucun identifiant d'appareil, tel que l'IDFV ou le GAID, dans vos liens de suivi des clics, ou si vous ne prévoyez pas de le faire à l'avenir, Kochava pourra toujours attribuer ces clics grâce à sa modélisation probabiliste.
{% endalert %}