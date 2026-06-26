---
nav_title: Télévision et OTT
article_title: Intégrations TV et OTT pour Braze
page_order: 15

description: "Cet article vous présente en détail les fonctionnalités TV et OTT de Braze, les intégrations, les plateformes disponibles et d'autres capacités."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# Intégrations TV et OTT {#tv-and-ott-integrations}

> À mesure que la technologie évolue vers de nouvelles plateformes et de nouveaux appareils, votre communication peut suivre le mouvement avec Braze ! Braze propose différents canaux d'engagement pour un certain nombre de systèmes d'exploitation télévisuels et de méthodes de diffusion de contenu Over-the-Top (OTT).

## Plateformes et fonctionnalités {#platforms-and-features}

Voici la liste des fonctionnalités et canaux de communication pris en charge aujourd'hui.

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table aria-label="Plateformes et fonctionnalités" id="tv-feature-table">
  <caption>Plateformes et fonctionnalités</caption>
    <thead>
        <tr>
            <th>Type d'appareil</th>
            <th>Données et analyses</th>
            <th>Messages in-app</th>
            <th>Content Cards</th>
            <th>Notifications push</th>
            <th>Canvas</th>
            <th>Indicateurs de fonctionnalité</th>
            <th>Bannières</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-times text-warning"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
          <td for="banners"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Pris en charge
- <i class="fa-solid fa-minus"></i> = Prise en charge partielle
- <i class="fas fa-times text-warning"></i> = Non pris en charge par Braze
- S.O. = Non pris en charge par la plateforme OTT

## Guides d'intégration {#integration-guides}

### Amazon Fire TV {#fire-tv}

Utilisez le SDK Fire OS de Braze pour l'intégration avec les appareils Amazon Fire TV.

Les fonctionnalités comprennent :

- Collecte de données et d'analyses pour l'engagement cross-canal
- Notifications push (connues sous le nom de [« Heads Up Notifications »](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - La priorité doit être définie sur « HIGH » pour qu'elles apparaissent. Toutes les notifications apparaissent dans le menu des paramètres Fire TV.
- Content Cards
- Indicateurs de fonctionnalité
- Messages in-app
  - Pour afficher les messages HTML dans des environnements non tactiles tels que les téléviseurs, définissez `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` sur `false` (disponible à partir du [SDK Android v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- Bannières
  - Utilisez les [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements/) pour intégrer des messages directement dans votre application Fire TV.

Pour plus d'informations, consultez le [guide d'intégration Fire OS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

### Kindle Fire {#kindle-fire}

Utilisez le SDK Fire OS de Braze pour l'intégration avec les appareils Amazon Kindle Fire.

Les fonctionnalités comprennent :

- Collecte de données et d'analyses pour l'engagement cross-canal
- Notifications push
- Content Cards
- Indicateurs de fonctionnalité
- Messages in-app
- Bannières
  - Utilisez les [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements/) pour intégrer des messages directement dans votre Kindle Fire.

Pour plus d'informations, consultez le [guide d'intégration Fire OS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

### Android TV {#android-tv}

Utilisez le SDK Android de Braze pour l'intégration avec les appareils Android TV.

Les fonctionnalités comprennent :

- Collecte de données et d'analyses pour l'engagement cross-canal
- Content Cards
- Indicateurs de fonctionnalité
- Messages in-app
  - Pour afficher les messages HTML dans des environnements non tactiles tels que les téléviseurs, définissez `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` sur `false` (disponible à partir du [SDK Android v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Notifications push (intégration manuelle requise)
  - Les notifications push ne sont pas prises en charge nativement sur Android TV. Pour en savoir plus, consultez les [directives de conception](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) de Google. Vous pouvez toutefois **procéder à une intégration manuelle de l'interface utilisateur des notifications push pour y parvenir**. Consultez notre [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android%20tv) pour savoir comment procéder.
- Bannières
  - Utilisez les [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements/) pour intégrer des messages directement dans votre application Android TV.

Pour plus d'informations, consultez le [guide d'intégration du SDK Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

{% alert note %}
Veillez à créer une nouvelle application Android dans le tableau de bord pour votre intégration Android OTT.
{% endalert %}

### LG webOS {#lg-webos}

Utilisez le SDK Web de Braze pour l'intégration avec les [téléviseurs LG webOS](https://webostv.developer.lge.com/discover).

Les fonctionnalités comprennent :

- Collecte de données et d'analyses pour l'engagement cross-canal
- Content Cards (via l'[interface utilisateur Headless](#custom-ui))
- Indicateurs de fonctionnalité
- Messages in-app (via l'[interface utilisateur Headless](#custom-ui))
- Bannières
  - Utilisez les [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements/) pour intégrer des messages directement dans votre application webOS.

Pour plus d'informations, consultez le [guide d'intégration TV connectée Web]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/).

### Samsung Tizen {#tizen}

Utilisez le SDK Web de Braze pour l'intégration avec les [téléviseurs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Les fonctionnalités comprennent :

- Collecte de données et d'analyses pour l'engagement cross-canal
- Content Cards (via l'[interface utilisateur Headless](#custom-ui))
- Indicateurs de fonctionnalité
- Messages in-app (via l'[interface utilisateur Headless](#custom-ui))
- Bannières
  - Utilisez les [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements/) pour intégrer des messages directement dans votre application Tizen.

Pour plus d'informations, consultez le [guide d'intégration TV connectée Web]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/).

### Roku {#roku}

Utilisez le SDK Roku de Braze pour l'intégration avec les [téléviseurs Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Les fonctionnalités comprennent :

- Collecte de données et d'analyses pour l'engagement cross-canal
- Messages in-app (via l'[interface utilisateur Headless](#custom-ui))
  - Les webviews ne sont pas prises en charge par la plateforme Roku. Par conséquent, les messages in-app HTML ne sont pas pris en charge.
- Indicateurs de fonctionnalité

Pour plus d'informations, consultez le [guide d'intégration Roku]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=roku).

### Apple TV OS {#tvos}

Utilisez le SDK Swift de Braze pour l'intégration avec tvOS. Gardez à l'esprit que le SDK Swift n'inclut aucune interface utilisateur ou vue par défaut pour tvOS ; vous devrez donc implémenter les vôtres.

Les fonctionnalités comprennent :

- Collecte de données et d'analyses pour l'engagement cross-canal
- Content Cards (via l'[interface utilisateur Headless](#custom-ui))
- Indicateurs de fonctionnalité
- Messages in-app (via l'[interface utilisateur Headless](#custom-ui))
  - Les webviews ne sont pas prises en charge par la plateforme tvOS. Par conséquent, les messages in-app HTML ne sont pas pris en charge.
  - Consultez notre [exemple d'application](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) pour en savoir plus sur l'utilisation d'une interface utilisateur Headless pour un envoi de messages personnalisé sur tvOS.
- Notifications push silencieuses et mise à jour des badges
- Bannières
  - Utilisez les [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements/) pour intégrer des messages directement dans votre application tvOS.

Pour plus d'informations, consultez le [guide d'intégration du SDK Swift pour iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Pour éviter d'afficher des messages in-app mobiles à vos utilisateurs TV, veillez à configurer soit le [ciblage des applications](#app-targeting), soit des paires clé-valeur pour filtrer les messages. Par exemple, n'affichez les messages tvOS que s'ils contiennent une paire clé-valeur spéciale `tv = true`.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Utilisez le SDK Swift de Braze pour l'intégration avec visionOS. La plupart des fonctionnalités disponibles sur iOS sont également disponibles sur visionOS, notamment :

- Analyses (sessions, événements personnalisés, achats, etc.)
- Messages in-app (modèles de données et interface utilisateur)
- Content Cards (modèles de données et interface utilisateur)
- Notifications push (visibles par l'utilisateur avec boutons d'action et notifications silencieuses)
- Indicateurs de fonctionnalité
- Analyse de localisation
- Bannières
  - Utilisez les [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements/) pour intégrer des messages directement dans votre application visionOS.

Pour plus d'informations, consultez le [guide d'intégration du SDK Swift pour iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Certaines fonctionnalités iOS sont partiellement prises en charge ou non prises en charge. Pour obtenir la liste complète, consultez la [prise en charge de visionOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/visionos/).
{% endalert %}

## Ciblage des applications {#app-targeting}

Pour cibler les applications OTT avec vos messages, nous vous recommandons de créer un segment spécifique à votre application OTT.

![Un segment créé à l'aide de l'application Android OTT.]({% image_buster /assets/img/android_ott.png %})

## Interface utilisateur Headless {#custom-ui}

{% alert important %}
Les plateformes qui prennent en charge les messages in-app ou les Content Cards via une interface utilisateur Headless **n'incluent pas** d'interface utilisateur ou de vues par défaut. Créez votre propre interface utilisateur personnalisée (par exemple pour les messages in-app), puis utilisez les modèles de données fournis par le SDK pour alimenter ces interfaces.
{% endalert %}

Avec l'interface utilisateur Headless, Braze fournit un modèle de données, tel que du JSON, que votre application peut lire et utiliser au sein d'une interface contrôlée par votre application. Ces données contiennent les champs configurés dans le tableau de bord (titre, corps, texte du bouton, couleurs, etc.) que votre application peut lire et afficher en conséquence. Pour plus d'informations sur la gestion personnalisée des messages, consultez les ressources suivantes :

**SDK Android**
- [Personnalisation des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)
- [Personnalisation des Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

**SDK Swift**
- [Personnalisation des messages in-app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Exemple d'application Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Personnalisation des Content Cards](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**SDK Web**
- [Personnalisation des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
- [Personnalisation des Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)