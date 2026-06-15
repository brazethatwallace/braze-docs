---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "Cet article de référence présente le partenariat entre Braze et Infillion, qui vous permet de perfectionner la pertinence de votre marketing grâce aux données de localisation."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) vous permet de perfectionner la pertinence de votre marketing grâce aux données de localisation. Leur SDK de localisation, associé à un logiciel de géorepérage et à des balises, permet d'offrir des expériences mobiles pertinentes, personnalisées et sensibles à la proximité.

Combinez votre prise en charge des balises ou du géorepérage avec les fonctionnalités de ciblage et d'envoi de messages de Braze pour en savoir plus sur les actions physiques de vos utilisateurs et leur envoyer des messages en conséquence. Cette intégration de partenariat ouvre de nombreux cas d'utilisation pour :

- **Marketing :** Envoyez des messages contextuels pertinents et créez des parcours consommateurs expérientiels.
- **Analyse concurrentielle :** Configurez des déclencheurs autour d'emplacements concurrents pour comprendre les tendances et les habitudes de consommation.
- **Informations sur l'audience :** Comprenez les comportements de visite de vos utilisateurs et segmentez davantage en fonction de ces connaissances.

{% alert note %}
Cette intégration fonctionne de la même manière pour les balises Infillion et les solutions de géorepérage Infillion.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| [Compte gestionnaire Infillion](https://manager.gimbal.com/login/users/sign_in) | Un compte gestionnaire Infillion est nécessaire pour profiter de ce partenariat. |
| [SDK de localisation Infillion](https://docs.gimbal.com/index.html) | Le SDK de localisation Infillion alimente des expériences mobiles macro et micro basées sur la localisation en utilisant des balises de proximité et des géorepérages qui vous permettent de communiquer plus efficacement avec les utilisateurs de votre application. Le SDK doit être implémenté et les géorepérages (ou balises) configurés. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration SDK {#sdk-integration}

Pour intégrer Braze et Infillion, vous devez implémenter le SDK de localisation Infillion et créer un compte gestionnaire Infillion. Les intégrations suivantes pour Android, FireOS et iOS créeront un événement personnalisé unique pour chaque nouvel endroit dans lequel un utilisateur entre. Ces événements pourront ensuite être utilisés pour le déclenchement et le reciblage dans vos Campaigns et Canvas.

Si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement personnalisé générique `Places Entered` et d'ajouter le nom du lieu en tant que propriété de l'événement.

1. Intégrez le [SDK Infillion](https://manager.gimbal.com/sdk_downloads) pour Android et iOS dans votre application en suivant les instructions de la [documentation Infillion](https://docs.gimbal.com/).
2. Utilisez l'[API REST place](https://docs.gimbal.com/rest.html) d'Infillion pour obtenir les `places` de l'utilisateur.
3. Reliez votre compte Infillion à Braze en saisissant la [clé API REST](https://manager.gimbal.com/apps) de Braze.
4. Configurez des [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) dans le SDK de Braze. Vous pouvez intégrer Infillion avec Braze pour [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons).
5. Consignez les propriétés de ces événements (nom du lieu, durée du séjour).
6. Utilisez ces propriétés et ces événements pour déclencher des Campaigns et des Canvas dans Braze.