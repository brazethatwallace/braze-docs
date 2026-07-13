---
nav_title: loplat
article_title: loplat
description: "Cet article de référence décrit le partenariat entre Braze et loplat, une plateforme de marketing hors ligne basée sur la localisation, qui vous permet d'exécuter des campagnes de marketing de proximité en ajoutant un contexte de localisation."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat](https://www.loplat.com/) est la principale plateforme hors ligne basée sur la localisation. Utilisez le SDK loplat pour augmenter intelligemment la fréquentation de votre magasin et exécuter des campagnes marketing qui encouragent les achats en magasin. Vous pouvez mesurer la performance du magasin grâce à l'analyse de la fréquentation une fois la campagne terminée.

_Cette intégration est maintenue par Loplat._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et loplat vous permet d'utiliser les services de localisation de loplat (POI de magasin et géorepérage personnalisé) pour déclencher des campagnes marketing géo-contextuelles et créer des événements personnalisés à l'aide de la segmentation hors ligne. Lorsque les utilisateurs visitent l'emplacement ciblé que vous avez défini dans loplat X, les informations de la campagne et de l'emplacement sont envoyées immédiatement à Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte loplat X | Un compte loplat X est requis pour profiter de cette intégration.<br><br>Envoyez un e-mail à [support@loplat.com](mailto:support@loplat.com) pour demander un compte loplat X. |
| SDK loplat | Le SDK loplat reconnaît les visites des utilisateurs en magasin, traite les événements de localisation et distingue si les utilisateurs restent à un endroit ou se déplacent. Vous pouvez utiliser le SDK loplat pour analyser la fréquentation de votre magasin, envoyer des notifications push lorsque les utilisateurs entrent dans votre magasin, etc.<br><br>Notez que le SDK n'est disponible que pour Android et iOS. |
| Clé API REST Braze | Une clé API REST de Braze avec les autorisations suivantes :<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'usage {#use-cases}

Les informations de localisation de l'événement personnalisé fournies par loplat peuvent être utilisées dans vos campagnes pour répondre à des cas d'usage tels que :

- [Alerte promotion duty-free](https://www.loplat.com/loplat-x#usecase)
    - Envoyez des coupons de réduction duty-free aux utilisateurs qui se trouvent près des portes d'embarquement à l'aéroport.
- Notification push de localisation de station de recharge pour véhicule électrique (VE)
    - Définissez des géorepérages autour des stations de recharge pour véhicules électriques et informez les utilisateurs lorsqu'ils sont à proximité afin de les encourager à recharger leur véhicule.

## Intégration {#integration}

### Étape 1 : Intégrer les SDK {#step-1-integrate-the-sdks}

Intégrez le SDK loplat et le SDK Braze dans votre application en suivant les étapes fournies dans la documentation de l'[intégration loplat-Braze](https://developers.loplat.com/braze/).

### Étape 2 : Synchroniser les tableaux de bord Braze et loplat X et créer une campagne {#step-2-sync-the-braze-and-loplat-x-dashboards-and-create-a-campaign}

Créez une nouvelle clé API dans le tableau de bord de Braze. Copiez la clé API et collez-la dans **Settings > API Settings** dans le tableau de bord loplat X. Consultez le [guide de l'utilisateur loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25) pour plus de détails.

#### Distribution déclenchée par l'API {#api-triggered-delivery}

1. Créez une campagne Braze ou un Canvas configuré avec **API-Triggered Delivery**, et copiez l'ID de la campagne.
2. Lancez la campagne dans Braze après avoir terminé toutes les étapes.
3. Allez sur loplat X et créez une campagne en suivant les instructions du [guide de l'utilisateur loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. Collez l'ID de la campagne Braze sous les **Campaign Message Settings**, puis lancez la campagne.

![Paramètres de campagne loplat X affichant l'ID de campagne Braze pour la distribution déclenchée par l'API.]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### Livraison par événement {#action-based-delivery}

Avec l'intégration, vous pouvez appliquer des conditions de localisation en envoyant des données de géorepérage, de région, de nom de marque ou de nom de magasin. De plus, vous pouvez ajouter des segments ou attribuer une conversion avec l'événement personnalisé que vous avez créé.
1. Créez une campagne loplat X en suivant les instructions du [guide de l'utilisateur loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. Ajoutez un événement personnalisé dans les **Campaign Message Settings** et lancez la campagne.
3. Allez dans le tableau de bord de Braze et créez une campagne ou un Canvas configuré avec **Action-Based Delivery**.
4. Sélectionnez l'événement personnalisé que vous avez créé dans loplat X pour définir une action de déclenchement basée sur la localisation.

![Configuration d'une campagne Braze basée sur les actions utilisant un événement personnalisé loplat comme déclencheur.]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})