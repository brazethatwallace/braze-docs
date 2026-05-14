---
nav_title: Guide de mise à niveau iOS 14
article_title: Guide de mise à jour SDK iOS 14
page_order: 7
platform: iOS
description: "Cet article de référence couvre la mise à jour du SDK iOS 14, mettant en évidence les changements tels que les géorepérages, le ciblage géographique, l'IDFA, et plus encore."
hidden: true
noindex: true
---

# Guide de mise à jour SDK iOS 14 {#ios-14-sdk-upgrade-guide}

> Ce guide décrit les modifications liées à Braze introduites dans iOS 14 et les étapes de mise à niveau requises pour votre intégration SDK Braze pour iOS. Pour obtenir une liste complète des nouvelles mises à jour d'iOS 14, consultez la [page iOS 14](https://www.apple.com/ios/ios-14/) d'Apple.

{% alert tip %}
À partir d'iOS 14.5, la collecte d'**IDFA** et [certains partages de données](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) nécessiteront la nouvelle invite de permission du framework [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) ([en savoir plus](#idfa)).
{% endalert %}

#### Résumé des changements majeurs d'iOS 14 {#summary-of-ios-14-breaking-changes}

- Les applications ciblant iOS 14 / Xcode 12 doivent utiliser notre [version officielle d'iOS 14](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0).
- Les géorepérages [ne sont plus pris en charge par iOS](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) pour les utilisateurs qui choisissent la nouvelle autorisation de _localisation approximative_.
- L'utilisation des fonctionnalités de ciblage « Dernière localisation connue » nécessite une mise à niveau vers le SDK Braze pour iOS v3.26.1+ pour la compatibilité avec l'autorisation de _localisation approximative_. Notez que si vous utilisez Xcode 12, vous devrez passer au moins à la version v3.27.0.
- À partir d'iOS 14.5, la collecte d'IDFA et [certains partages de données](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) nécessitent la nouvelle invite de permission du framework [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency).
- Si vous utilisez le champ « Ad Tracking Enabled » pour le ciblage de Campaign ou l'analyse, vous devrez passer à Xcode 12 et utiliser le nouveau framework AppTrackingTransparency pour signaler le statut d'abonnement des utilisateurs.

## Résumé de la mise à jour {#upgrade-summary}

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

| Si votre application utilise : | Recommandation de mise à jour | Description |
|------|--------|---|
| Xcode 12 | **Mise à jour vers le SDK iOS v3.27 ou version ultérieure** | Les clients utilisant Xcode 12 doivent utiliser la version v3.27.0+ pour la compatibilité. Si vous rencontrez des problèmes ou si vous avez des questions concernant notre compatibilité avec iOS 14, ouvrez un nouveau [ticket sur GitHub](https://github.com/Appboy/appboy-ios-sdk/issues). |
| Localisation la plus récente | **Mise à jour vers le SDK iOS v3.26.1 ou version ultérieure** | Si vous utilisez la fonctionnalité de ciblage de la localisation la plus récente et que vous utilisez toujours Xcode 11, vous devez passer au moins au SDK iOS v3.26.1 qui prend en charge la nouvelle fonctionnalité de _localisation approximative_. Les anciens SDK ne pourront pas collecter de manière fiable la localisation lorsqu'un utilisateur passe à iOS 14 _et_ choisit la localisation approximative.<br><br>Même si votre application ne cible pas iOS 14, il se peut que vos utilisateurs passent à iOS 14 et commencent à utiliser la nouvelle option de précision de la localisation. Les applications qui ne passent pas à la version v3.26.1+ du SDK iOS ne pourront pas collecter de manière fiable les attributs de localisation lorsque les utilisateurs fournissent leur _localisation approximative_ sur les appareils iOS 14. |
| ID de suivi publicitaire IDFA | **Une mise à jour vers Xcode 12 et le SDK iOS v3.27 peut être nécessaire** | En 2021, Apple commencera à exiger une invite d'autorisation pour la collecte de l'IDFA. À ce moment-là, les applications devront être mises à niveau vers Xcode 12 et utiliser le nouveau framework `AppTrackingTransparency` afin de continuer à collecter l'IDFA. Si vous transmettez l'IDFA au SDK Braze, vous devrez également passer à la version v3.27.0+ à ce moment-là.<br><br>Les applications qui n'utilisent pas les nouvelles API d'iOS 14 ne pourront pas collecter l'IDFA, et collecteront à la place un ID vierge (`00000000-0000-0000-0000-000000000000`) après qu'Apple aura commencé à appliquer ce changement en 2021. Pour savoir si cela s'applique ou non à votre application, consultez les [détails sur l'IDFA](#idfa). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Upgrade summary" }


## Changements de comportement iOS 14 {#ios-14-behavior-changes}

### Autorisation de localisation approximative {#approximate-location-permission}

![Localisation précise]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Aperçu {#overview}

Lors de la demande d'autorisation de localisation, les utilisateurs auront désormais le choix entre fournir leur _localisation précise_ (comportement précédent), ou la nouvelle _localisation approximative_. La localisation approximative renvoie un rayon plus large dans lequel l'utilisateur se trouve, au lieu de ses coordonnées exactes.

#### Géorepérages {#geofences}

Les géorepérages [ne sont plus pris en charge par iOS](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) pour les utilisateurs qui choisissent la nouvelle autorisation de _localisation approximative_. Bien qu'aucune mise à jour ne soit nécessaire pour votre intégration SDK Braze, vous devrez peut-être ajuster votre [stratégie de marketing basé sur la localisation](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) pour les Campaigns qui s'appuient sur les géorepérages.

#### Ciblage de localisation {#location-tracking}

Pour continuer à collecter la _dernière localisation connue_ des utilisateurs lorsque la _localisation approximative_ est accordée, votre application devra être mise à niveau vers au moins la v3.26.1 du SDK iOS de Braze. Gardez à l'esprit que la localisation sera moins précise et que, d'après nos tests, elle peut dépasser 12 000 mètres (plus de 7 miles). Lorsque vous utilisez les options de ciblage de la _dernière localisation connue_ dans le tableau de bord de Braze, veillez à augmenter le rayon de la localisation pour tenir compte des nouvelles _localisations approximatives_ (nous recommandons un rayon d'au moins 1 mile/1,6 km).

Les applications qui ne mettent pas à niveau le SDK Braze pour iOS vers au moins la version v3.26.1 ne pourront plus utiliser le suivi de la localisation lorsque la _localisation approximative_ est accordée sur les appareils iOS 14.

Les utilisateurs qui ont déjà autorisé l'accès à la localisation continueront à fournir leur _localisation précise_ après la mise à niveau.

Notez que si vous utilisez Xcode 12, vous devrez passer au moins à la version v3.27.0.

Pour plus d'informations sur la localisation approximative, consultez la vidéo WWDC d'Apple sur [les nouveautés en matière de localisation](https://developer.apple.com/videos/play/wwdc2020/10660/).

### Transparence du suivi des applications et IDFA {#idfa}

#### Aperçu

L'IDFA (Identifier for Advertisers) est un identifiant fourni par Apple pour une utilisation avec des partenaires publicitaires et d'attribution pour le suivi inter-appareils, et est lié à l'identifiant Apple d'une personne.

À partir d'iOS 14.5, une nouvelle invite d'autorisation (lancée par le nouveau framework `AppTrackingTransparency`) doit être affichée pour recueillir le consentement explicite de l'utilisateur pour l'IDFA. Cette invite d'autorisation pour « vous suivre via les applications et les sites web appartenant à d'autres sociétés » sera demandée de la même manière que lorsque vous invitez les utilisateurs à partager leur localisation.

Si un utilisateur n'accepte pas l'invite, ou si vous ne procédez pas à la mise à niveau vers le framework `AppTrackingTransparency` de Xcode 12, alors une valeur IDFA vide (`00000000-0000-0000-0000-000000000000`) sera renvoyée, et votre application ne sera pas autorisée à inviter à nouveau l'utilisateur.

{% alert important %}
Ces mises à jour de l'IDFA prendront effet après que les utilisateurs finaux auront mis à jour leur appareil vers iOS 14.5. Assurez-vous que votre application utilise le nouveau `AppTransparencyFramework` avec Xcode 12 si vous prévoyez de recueillir l'IDFA.
{% endalert %}

#### Modifications apportées au recueil de l'IDFA par Braze {#changes-to-braze-idfa-collection}
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze continuera à autoriser les applications à fournir la valeur IDFA d'un utilisateur _au_ SDK de Braze.

2. La macro de compilation `ABK_ENABLE_IDFA_COLLECTION`, qui compilait de manière conditionnelle le recueil automatique facultatif de l'IDFA, ne fonctionnera plus dans iOS 14 et a été supprimée dans la version 3.27.0.

3. Si vous utilisez le champ « Ad Tracking Enabled » pour le ciblage de Campaign ou l'analyse, vous devrez passer à Xcode 12 et utiliser le nouveau framework AppTrackingTransparency pour signaler le statut d'abonnement de vos utilisateurs. La raison de cette modification est que dans iOS 14, l'ancien champ [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) renverra toujours No.

4. Si votre application a utilisé l'IDFA ou l'IDFV comme ID externe Braze, nous vous recommandons vivement de délaisser ces identifiants au profit d'un UUID. Pour plus d'informations sur la migration des ID externes, consultez nos [endpoints d'API de migration des ID externes]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

Pour en savoir plus, consultez les [mises à jour de la protection de la vie privée](https://developer.apple.com/app-store/user-privacy-and-data-use/) d'Apple et le nouveau [framework de transparence du suivi des applications](https://developer.apple.com/documentation/apptrackingtransparency).

### Autorisation push {#push-provisional-auth}

{% alert important %}
Aucune modification de l'autorisation push provisoire n'est incluse dans iOS 14. Dans une version bêta antérieure d'iOS 14, Apple a introduit une modification qui a depuis été rétablie au comportement antérieur.
{% endalert %}

## Nouvelles fonctionnalités iOS 14 {#ios-14-new-features}

### Présentation de la confidentialité et de la collecte de données de l'application {#app-privacy}

Depuis le 8 décembre 2020, toutes les soumissions à l'App Store nécessitent des étapes supplémentaires pour adhérer aux [nouvelles normes d'Apple en matière de confidentialité des applications](https://developer.apple.com/app-store/app-privacy-details/).

#### Questionnaire sur le portail développeur d'Apple {#apple-developer-portal-questionnaire}

Sur le _portail des développeurs Apple_ :
* Il vous sera demandé de remplir un questionnaire pour décrire comment votre application ou des partenaires tiers collectent des données.
  * Le questionnaire doit toujours être à jour avec votre version la plus récente dans l'App Store.
  * Le questionnaire peut être mis à jour même sans nouvelle soumission d'application.
* Vous devrez coller un lien vers l'URL de la politique de confidentialité de votre application.

Lorsque vous remplissez votre questionnaire, consultez votre équipe juridique et réfléchissez à la manière dont votre utilisation de Braze dans les domaines suivants peut affecter vos exigences de divulgation.

#### Collecte de données par défaut de Braze {#braze-default-data-collection}
**Identifiants** - Un identifiant d'appareil anonyme est toujours collecté par le SDK Braze. Ce paramètre est actuellement défini sur l'IDFV (identifiant du fournisseur).

**Données d'utilisation** - Il peut s'agir des données de session de Braze, ainsi que de toute collecte d'événements ou d'attributs que vous utilisez pour mesurer l'interaction avec le produit.

#### Collecte de données facultative {#optional-data-collection}
Données que vous pouvez éventuellement collecter via votre utilisation de Braze :

**Localisation** - La localisation approximative et la localisation précise peuvent être collectées de manière facultative par le SDK Braze. Ces fonctionnalités sont désactivées par défaut.

**Coordonnées** - Il peut s'agir d'événements et d'attributs liés à l'identité de l'utilisateur.

**Achats** - Il peut s'agir d'événements et d'achats enregistrés au nom de l'utilisateur.

{% alert important %}
Notez qu'il ne s'agit pas d'une liste exhaustive. Si vous collectez manuellement d'autres informations sur vos utilisateurs dans Braze qui s'appliquent à d'autres catégories du questionnaire sur la confidentialité de l'application, vous devrez également les divulguer.
{% endalert %}

Pour en savoir plus sur cette fonctionnalité, consultez la page [Confidentialité et utilisation des données](https://developer.apple.com/app-store/user-privacy-and-data-use/) d'Apple.