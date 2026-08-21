---
nav_title: Lier les utilisateurs Web SDK entre domaines
article_title: Lier les utilisateurs Web SDK entre domaines via l'ID d'appareil
page_order: 1
page_type: reference
description: "Transmettez l'ID d'appareil du SDK Web Braze depuis le site marketing de Kitchenerie vers un domaine de boutique distinct afin que l'activité anonyme partage un seul profil utilisateur."
---

# Lier les utilisateurs Web SDK entre domaines via l'ID d'appareil {#link-cross-domain-web-sdk-users-through-device-id}

> Transmettez l'ID d'appareil du SDK Web Braze dans l'URL de destination lorsque deux domaines ne peuvent pas partager de cookies, afin que les sessions anonymes sur les deux sites soient associées au même profil utilisateur Braze.

## À propos de cet exemple {#about-this-example}

Kitchenerie, un détaillant fictif d'articles de cuisine, héberge un site marketing (`kitchenerie.com`) et une boutique (`kitchenerie.shop`). Chaque domaine possède sa propre intégration du SDK Web Braze. Les cookies du navigateur ne traversent pas les domaines, de sorte que Braze attribue des ID d'appareil distincts — et des profils anonymes distincts — lorsqu'un même utilisateur passe du site marketing à la boutique.

Ce modèle :

1. Lit l'ID d'appareil sur le domaine source avec `getDeviceId` après l'initialisation du SDK
2. L'ajoute aux liens sortants sous forme de paramètre de requête (par exemple, `brazeDeviceId`)
3. Sur le domaine de destination, lit ce paramètre et le transmet à `braze.initialize` via l'option `deviceId`

Ce transfert est surtout important pour les utilisateurs anonymes. Une fois que l'utilisateur se connecte sur la boutique, `changeUser` avec un `external_id` devient l'identifiant durable entre les appareils. Consultez [Définir les ID utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).

Les deux domaines doivent utiliser la même clé API d'espace de travail Braze et le même endpoint SDK afin que les événements soient enregistrés sur un seul profil.

## Considérations {#considerations}

- L'ID d'appareil est propre à chaque navigateur. Ce modèle ne lie pas l'activité entre différents navigateurs, appareils ou profils. Utilisez `external_id` via `changeUser` pour une identité authentifiée et multi-appareils.
- Récupérez l'ID d'appareil uniquement après l'initialisation du SDK Web sur le domaine source. Appeler `getDeviceId` avant `initialize` ne renvoie aucune valeur.
- Le SDK Web lit `deviceId` une seule fois lors de l'appel à `initialize`. Il n'existe pas de méthode `setDeviceId` post-initialisation permettant de modifier l'ID d'appareil actif. Lisez le paramètre d'URL sur le domaine de destination avant d'appeler `initialize`.
- Les visites directes, les favoris ou les renvois tiers vers la boutique sans `brazeDeviceId` doivent revenir à l'attribution par défaut de l'ID d'appareil — ce qui est attendu lorsqu'il n'y a pas d'ID du domaine source à hériter.
- Les paramètres de requête apparaissent dans l'historique du navigateur et les journaux du serveur.
- Les paramètres de requête peuvent fuiter via les en-têtes de référent. L'ID d'appareil n'est pas une donnée d'identification en soi, mais supprimez le paramètre après consommation si votre équipe chargée de la confidentialité l'exige (voir l'étape 2).
- Testez de bout en bout. Confirmez que les événements du domaine 2 utilisent l'ID d'appareil attendu à l'aide de l'inspection réseau.
- Adaptez les noms d'hôte, les sélecteurs de liens et la gestion des erreurs à votre site. Testez dans votre environnement de développement avant la mise en production.

## Configuration {#setup}

### Étape 1 : Ajouter l'ID d'appareil aux liens inter-domaines sur le domaine source {#step-1-append-the-device-id-to-cross-domain-links-on-the-source-domain}

Sur `kitchenerie.com` (domaine 1), initialisez le SDK Web comme d'habitude, puis ajoutez l'ID d'appareil actuel aux liens pointant vers `kitchenerie.shop` (domaine 2).

Choisissez un nom de paramètre de requête qui n'entre pas en conflit avec votre site (cet exemple utilise `brazeDeviceId`). Le même principe s'applique aux liens générés côté serveur, à la navigation côté client ou aux valeurs `src` d'iframe que vous contrôlez.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});
braze.openSession();

const destinationHost = "kitchenerie.shop";

braze.getDeviceId(function (deviceId) {
  if (!deviceId) {
    return;
  }

  const links = document.querySelectorAll('a[href*="' + destinationHost + '"]');

  links.forEach(function (link) {
    try {
      const url = new URL(link.href);
      url.searchParams.set("brazeDeviceId", deviceId);
      link.href = url.toString();
    } catch (e) {
      // Skip malformed hrefs (for example, javascript:, mailto:, or unparsable relative paths).
    }
  });
});
```

Si votre version du SDK expose `getDeviceId` de manière synchrone (sans rappel), appelez-le après l'initialisation :

```javascript
const deviceId = braze.getDeviceId();
```

Consultez [Guide du dépôt Web SDK — Obtenir l'ID d'appareil]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#get-device-id) et [Options d'initialisation — `deviceId`]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#initialization-options).

### Étape 2 : Lire l'ID d'appareil et initialiser le SDK Web sur le domaine de destination {#step-2-read-the-device-id-and-initialize-the-web-sdk-on-the-destination-domain}

Sur `kitchenerie.shop` (domaine 2), lisez `brazeDeviceId` depuis la chaîne de requête avant `initialize`, et transmettez-le dans les options d'initialisation lorsqu'il est présent.

```javascript
import * as braze from "@braze/web-sdk";

const urlParams = new URLSearchParams(window.location.search);
const passedDeviceId = urlParams.get("brazeDeviceId");

const initOptions = {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
};

if (passedDeviceId) {
  initOptions.deviceId = passedDeviceId;
}

braze.initialize("YOUR-API-KEY-HERE", initOptions);
braze.openSession();

// Optional: remove the parameter from the visible URL after consumption.
if (passedDeviceId) {
  const cleanUrl = new URL(window.location.href);
  cleanUrl.searchParams.delete("brazeDeviceId");
  window.history.replaceState({}, document.title, cleanUrl.toString());
}
```

Lorsque l'utilisateur se connecte, appelez `changeUser` avec son `external_id` afin que l'activité future soit rattachée au profil identifié.

### Étape 3 : Vérifier le transfert {#step-3-verify-the-handoff}

1. Ouvrez le domaine 1 dans un navigateur où vous n'êtes pas connecté.
2. Suivez un lien inter-domaines vers le domaine 2.
3. Dans l'onglet réseau du navigateur, confirmez que le domaine 2 envoie les événements avec le même ID d'appareil que celui utilisé par le domaine 1.
4. Répétez l'opération avec une visite directe sur le domaine 2 (sans paramètre de requête) et confirmez qu'un nouvel ID d'appareil est attribué.

## Articles connexes {#related-articles}

- [Guide du dépôt Web SDK]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)
- [Intégration multi-domaines pour le SDK Web Braze]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)
- [Définir les ID utilisateur via le SDK Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)
- [Utilisateurs anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)
- [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Stockage du SDK Web]({{site.baseurl}}/developer_guide/storage)