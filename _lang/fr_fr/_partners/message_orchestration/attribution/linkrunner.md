---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "Cet article de référence décrit le partenariat entre Braze et Linkrunner, une plateforme d'attribution mobile et d'analyse qui vous permet d'importer des données d'attribution pour mieux comprendre vos campagnes d'acquisition d'utilisateurs."
page_type: partner
search_tag: Partner

---

# Linkrunner

> [Linkrunner](https://linkrunner.io/) est une plateforme d'attribution mobile et d'analyse qui vous aide à suivre et analyser vos campagnes d'acquisition d'utilisateurs.

_Cette intégration est maintenue par Linkrunner._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Linkrunner vous permet d'importer des données d'attribution pour mieux comprendre quelles campagnes génèrent l'acquisition et l'engagement des utilisateurs.

## Conditions préalables {#prerequisites}

Les éléments suivants sont requis avant de commencer :

| Condition | Description |
|---|---|
| Compte Linkrunner | Un compte Linkrunner est nécessaire pour bénéficier de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, des extraits de code peuvent être nécessaires dans votre application. |
| SDK Linkrunner | Vous devez installer le [SDK Linkrunner](https://docs.linkrunner.io/introduction). |
| SDK Braze | Vous devez intégrer le [SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Mapper les ID utilisateur {#step-1-map-user-ids}

Si vous utilisez la fonction `changeUser` du SDK Braze, transmettez le même ID utilisateur dans le paramètre `userData` de la fonction `signup` du SDK Linkrunner.

Si vous n'utilisez pas `changeUser`, transmettez le `brazeDeviceId` dans le paramètre `userData` de la fonction `signup` du SDK Linkrunner. Obtenez le `brazeDeviceId` à partir du SDK Braze.

{% tabs local %}
{% tab Android (Kotlin) %}
```kotlin
val userData = UserDataRequest(
    id = "123", // Your user ID
    // ...other user fields
    brazeDeviceId = "BRAZE_DEVICE_ID", // Braze device ID from the Braze SDK (Required if you are not using the changeUser function)
)

LinkRunner.getInstance().signup(userData = userData)
```
{% endtab %}

{% tab iOS (Swift) %}
```swift
let userData = UserData(
    id: "123", // Your user ID
    // ...other user fields
    brazeDeviceId: "BRAZE_DEVICE_ID" // Braze Device ID from the Braze SDK (Required if you are not using the changeUser function)
)

try await LinkrunnerSDK.shared.signup(userData: userData)
```
{% endtab %}
{% endtabs %}

### Étape 2 : Créer une clé API dans Braze {#step-2-create-api-key-in-braze}

Dans votre tableau de bord de Braze, accédez à **Paramètres** > **Configuration et test** > **Clés API** > **Clés API**.

1. Sélectionnez **Créer une clé API**.
2. Sous **Données utilisateur**, sélectionnez les autorisations suivantes :
   - `users.track`
   - `users.export.ids`
3. Enregistrez la clé API.
4. Copiez la clé API et l'endpoint REST.

![Cette image montre la page Clés API dans Braze où vous pouvez créer et gérer les clés API, y compris la clé d'importation des données et l'endpoint REST nécessaires pour l'intégration Linkrunner.]({% image_buster /assets/img/attribution/linkrunner/1.png %})

### Étape 3 : Configurer Braze dans le tableau de bord de Linkrunner {#step-3-configure-braze-in-linkrunners-dashboard}

1. Dans Linkrunner, accédez à **Intégration** dans le panneau de gauche.
2. Sous **Analyse**, sélectionnez **Configurer** pour Braze.
3. Saisissez la clé API et l'endpoint REST que vous avez copiés à l'étape 2.

Pour plus d'informations, consultez la [documentation de Linkrunner](https://docs.linkrunner.io/analytics-integrations/braze).

### Étape 4 : Consulter les données d'attribution des utilisateurs {#step-4-view-user-attribution-data}

Linkrunner envoie `lr_campaign` et `lr_ad_network` en tant qu'attributs personnalisés. Consultez ces données dans la section **Attributs personnalisés** du profil utilisateur dans le tableau de bord de Braze.

## Données d'attribution Facebook et X (anciennement Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles via nos partenaires. Ces sources média ne permettent pas à leurs partenaires de partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.