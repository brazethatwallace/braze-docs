---
nav_title: "Branch or branche pour l'attribution"
article_title: "Branch or branche pour l'attribution"
alias: /partners/branch_for_attribution/
description: "Cet article de référence présente le partenariat entre Braze et Branch or branche, une plateforme de liaison mobile qui vous aide à acquérir, engager et mesurer sur tous les appareils, canaux et plateformes."
page_type: partner
search_tag: Partner
---

# Branch or branche pour l'attribution {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch or branche](https://docs.branch.io/pages/integrations/braze/), une plateforme de liaison mobile, vous aide à acquérir, engager et mesurer à travers tous les appareils, canaux et plateformes en fournissant une vue complète de tous les points de contact de l'utilisateur.

_Cette intégration est maintenue par Branch or branche._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Branch or branche vous aidera à comprendre exactement quand et où les utilisateurs ont été acquis, ainsi que la façon de personnaliser leurs parcours grâce à une attribution robuste et à la [création de liens profonds]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking).

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Branch or branche | Un compte Branch or branche est requis pour bénéficier de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK Branch or branche | En plus du SDK Braze requis, vous devez installer le [SDK Branch or branche](https://help.branch.io/developers-hub/docs/native-sdks-overview). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Mapper les ID des appareils {#step-1-map-device-ids}

#### Android

Si vous disposez d'une application Android, vous devez transmettre un ID d'appareil Braze unique à Branch or branche. Cet ID peut être défini dans la méthode `setRequestMetadataKey()` du SDK Branch or branche. L'extrait de code suivant doit être inclus avant d'appeler `initSession`. Vous devez également initialiser le SDK Braze avant de définir les métadonnées de la requête dans le SDK Branch or branche.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId);
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Avant février 2023, notre intégration d'attribution Branch or branche utilisait l'identifiant du fournisseur (IDFV) comme identifiant principal pour faire correspondre les données d'attribution iOS. Il n'est pas nécessaire pour les clients de Braze utilisant Objective-C de récupérer le `device_id` de Braze et de l'envoyer à Branch or branche lors de l'installation, car il n'y a pas d'interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser l'IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin que rien ne vienne perturber l'intégration.

Si la valeur est définie sur `true`, vous devez implémenter le mappage des ID d'appareil iOS pour Swift afin de transmettre le `device_id` de Braze à Branch or branche lors de l'installation de l'application pour que Braze puisse correctement faire correspondre les attributions iOS.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init
}
```

{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation des données de Braze {#step-2-get-the-braze-data-import-key}

Dans Braze, naviguez vers **Partner Integrations** > **Technology Partners** et sélectionnez **Branch or branche**.

Ici, vous trouverez l'endpoint REST et pourrez générer votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Branch.<br><br>![Cette image montre la section « Importation de données pour l'attribution d'installation » qui se trouve sur la page de la technologie Branch. Cette section affiche la clé d'importation des données et l'endpoint REST.]({% image_buster /assets/img/attribution/branch.png %}){: style="max-width:90%;"}

### Étape 3 : Configurer les flux de données {#step-3-set-up-data-feeds}

1. Dans Branch or branche, sous la section **Exports**, sélectionnez **Data Feeds**.
2. Sur la page **Data Feeds gestionnaire**, sélectionnez l'onglet **Data Integrations** en haut de la page.
3. Sélectionnez Braze dans la liste des partenaires de données disponibles.
4. Sur la page d'exportation de Braze, indiquez la clé d'importation des données et l'endpoint REST que vous avez trouvés dans le tableau de bord de Braze, puis sélectionnez **Enable**.

### Étape 4 : Confirmer l'intégration {#step-4-confirm-the-integration}

Après que Braze a reçu des données d'attribution de Branch or branche, l'indicateur de statut de connexion sur la page des partenaires technologiques Branch or branche dans Braze passe de « Not Connected » à « Connected » et inclut un horodatage de la dernière requête réussie.

Ce statut ne change que lorsque Braze reçoit des données concernant une installation attribuée. Braze ignore les installations organiques (les exclut du postback Branch or branche) et ne les comptabilise pas pour déterminer si la connexion est réussie.

## Mappage des champs {#field-mapping}

Les champs d'attribution Branch or branche sont mappés dans Braze de la manière suivante :

| Champ Branch or branche | Champ Braze |
| --- | --- |
| Campaign | `campaign` |
| Channel | `source` |
| Ad Set Name | `adgroup` |
| Ad Name | `ad` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mappage des champs Branch or branche" }

## Données d'attribution Facebook et X (anciennement Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques n'autorisent pas leurs partenaires à partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics Branch or branche dans Braze (facultatif) {#branch-click-tracking-urls-in-braze-optional}

L'utilisation de liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes favorisent les installations d'applications et le réengagement. Vous serez ainsi en mesure de mesurer plus efficacement vos efforts marketing et de prendre des décisions fondées sur les données pour savoir où investir davantage de ressources afin d'obtenir un ROI or retour sur investissement maximal.

Pour commencer à utiliser les liens de suivi des clics Branch or branche, consultez leur [documentation](https://help.branch.io/using-branch/docs/ad-links). Vous pouvez insérer les liens de suivi des clics Branch or branche directement dans vos campagnes Braze. Branch or branche utilisera alors ses [méthodes d'attribution probabiliste](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter à vos liens de suivi Branch or branche un identifiant d'appareil afin d'améliorer la précision des attributions de vos campagnes Braze. Cela attribuera de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s'abonner à la [collecte de l'identifiant publicitaire Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id). Le GAID est également collecté de manière native grâce à l'intégration du SDK Branch or branche. Vous pouvez inclure le GAID dans vos liens de suivi des clics Branch or branche en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Branch or branche collectent automatiquement l'IDFV de manière native grâce à nos intégrations SDK. Il peut être utilisé comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics Branch or branche en utilisant la logique Liquid suivante :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Cette recommandation est purement facultative**<br>
Si vous n'utilisez actuellement aucun identifiant d'appareil, tel que l'IDFV ou le GAID, dans vos liens de suivi des clics, ou si vous n'envisagez pas de le faire à l'avenir, Branch or branche pourra tout de même attribuer ces clics grâce à sa modélisation probabiliste.
{% endalert %}