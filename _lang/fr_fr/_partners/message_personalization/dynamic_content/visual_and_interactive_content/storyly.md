---
nav_title: Storyly
article_title: Storyly
description: "Cet article de référence présente le partenariat entre Braze et Storyly, un SDK léger, qui permet aux propriétaires d'applications de cibler leurs segments et d'alimenter Braze avec davantage de données first-party."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) est un SDK léger qui intègre des stories à votre application ou site web. Avec un studio de conception intuitif, des analyses pertinentes et une connectivité homogène, Storyly est un outil puissant pour enrichir l'expérience de l'audience.

_Cette intégration est maintenue par Storyly._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Storyly vous permet d'utiliser vos segments dans Braze comme audience dans la plateforme Storyly. Grâce à cette intégration, vous pouvez :
- Cibler vos segments avec des stories spécifiques
- Utiliser les attributs utilisateur pour personnaliser le contenu de vos stories

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Storyly | Un compte Storyly est nécessaire pour profiter de ce partenariat. |
| SDK Storyly | Vous devez installer le [SDK Storyly](https://integration.storyly.io/). |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations suivantes : <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation {#use-cases}

Grâce à l'intégration de Braze et de Storyly, les propriétaires d'applications peuvent afficher des stories pour tous les segments dans Braze et personnaliser les stories avec des attributs utilisateur.

Les cas d'utilisation les plus courants sont les suivants :

__Cibler les segments Braze dans Storyly__<br>Une fois l'intégration terminée, vous pouvez créer une audience Storyly basée sur vos segments Braze. Il peut s'agir d'un segment démographique ou comportemental. Par exemple, ciblez les utilisateurs qui vivent dans un emplacement spécifique, ceux qui effectuent une action précise sur votre application, ou ceux qui s'intéressent à des produits spécifiques avec des stories ciblées pour augmenter la conversion.<br>
__Stories personnalisées avec les attributs utilisateur__<br>Les attributs utilisateur de Braze sont également utilisables dans Storyly pour générer des stories dynamiques. Il peut s'agir du nom d'un utilisateur, de produits dans un panier ou même de produits favoris, offrant ainsi aux utilisateurs des stories personnalisées uniques. La personnalisation permet d'augmenter les taux de conversion des stories et le taux d'engagement global des stories.

## Intégration de l'exportation des données {#data-export-integration}

L'intégration Braze Storyly est expliquée dans la vidéo suivante :

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Assurez-vous que votre intégration Storyly contient des paramètres personnalisés. Ces paramètres seront mis en correspondance avec la propriété utilisateur `external id` de Braze. L'implémentation des paramètres personnalisés est expliquée ici pour [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) et [Web](https://integration.storyly.io/web/personalization-customaudience.html).

Vous pouvez également consulter la documentation de [Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) pour plus d'informations.

### Étape 1 : Configurer l'intégration dans le tableau de bord Storyly {#step-1-set-the-integration-on-storyly-dashboard}

Une intégration peut être créée dans **Storyly Dashboard > Settings > Integrations > Connect with Braze**. Vous aurez besoin de votre clé API REST de Braze et de votre endpoint REST de Braze.

### Étape 2 : Récupérer vos segments {#step-2-get-your-segments}

Ensuite, vous pouvez utiliser les segments Braze pour créer une audience Storyly. Celle-ci peut être créée dans **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze**.

Deux options de synchronisation sont disponibles. Sélectionnez **One-time sync** pour des stories de campagne spécifiques, ou **Daily Sync** pour des stories à long terme.