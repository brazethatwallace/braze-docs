---
nav_title: Collecte de données SDK
article_title: Collecte de données SDK
page_order: 1
page_type: reference
description: "Cet article de référence traite des données collectées par le SDK via une intégration personnalisée, une intégration avec collecte automatique et une intégration minimale."
---

# Collecte de données SDK {#sdk-data-collection}

> Lorsque vous intégrez le SDK de Braze à votre application ou à votre site, Braze collecte automatiquement certains types de données. Certaines de ces données sont essentielles à nos processus, tandis que d'autres peuvent être activées ou désactivées en fonction de vos besoins. Vous pouvez également configurer Braze pour collecter d'autres types de données afin d'enrichir votre segmentation et votre envoi de messages.

Braze est conçu pour offrir une collecte de données flexible. Vous pouvez intégrer le SDK de Braze de plusieurs manières :

- **[Intégration minimale](#minimum-integration) :** Braze collecte automatiquement les données nécessaires à la communication avec les services de Braze.
- **[Données facultatives collectées par défaut](#optional-data-collected-by-default) :** Braze capture automatiquement certaines données utiles pour la plupart de vos cas d'usage. Vous pouvez désactiver la collecte automatique de ces données si elles ne sont pas indispensables à la communication avec les services de Braze.
- **[Données facultatives non collectées par défaut](#data-not-collected-by-default) :** Braze capture certaines données utiles pour des cas d'usage spécifiques, mais n'active pas automatiquement leur collecte pour des raisons de conformité générale. Vous pouvez choisir de collecter ces données lorsque cela correspond à vos besoins.
- **[Intégration personnalisée](#personalized-integration) :** Braze vous offre la possibilité de collecter des données supplémentaires en plus des données facultatives par défaut.

## Intégration minimale {#minimum-integration}

Ce qui suit répertorie les données strictement nécessaires générées et reçues par Braze lorsque vous initialisez le SDK. Ces données ne sont pas configurables et sont essentielles au fonctionnement des fonctions principales de la plateforme. À l'exception du début de session et de la fin de session, toutes les autres données suivies automatiquement ne sont pas comptabilisées dans votre consommation de points de donnée.

| Attribut | Description | Raison de la collecte |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | La version la plus récente de l'application | Cet attribut est utilisé pour envoyer des messages liés à la compatibilité de version de l'application aux appareils appropriés. Il peut être utilisé pour notifier les utilisateurs d'interruptions de service ou de bugs. |
| Country | Pays identifié par la géolocalisation de l'adresse IP. Si la géolocalisation de l'adresse IP n'est pas disponible, il est identifié par les [paramètres régionaux de l'appareil](#optional-data-collected-by-default). La valeur peut également être celle définie directement par les SDK avec `setCountry`, mais notez que le passage d'une valeur d'attribut via le SDK ou l'API consomme des points de donnée. **Une fois le pays défini manuellement (via la méthode du SDK, la REST API ou un import CSV), le SDK ne met plus automatiquement à jour cette valeur.** | Cet attribut est utilisé pour cibler les messages en fonction de la localisation. |
| Device ID | Identifiant de l'appareil, une chaîne de caractères générée aléatoirement | Cet attribut est utilisé pour différencier les appareils des utilisateurs et envoyer les messages au bon appareil. |
| OS and OS version | L'appareil ou le navigateur actuellement signalé et la version de l'appareil ou du navigateur | Cet attribut est utilisé pour envoyer les messages uniquement aux appareils compatibles. Il peut également être utilisé dans la segmentation pour cibler les utilisateurs afin de mettre à jour les versions de l'application. |
| Session start and session end | Moment où l'utilisateur commence à utiliser votre application ou site intégré | Le SDK de Braze transmet les données de session utilisées par le tableau de bord de Braze pour calculer l'engagement des utilisateurs et d'autres analyses essentielles à la compréhension de vos utilisateurs. Le moment exact où le début et la fin de session sont déclenchés par votre application ou site est configurable par un développeur ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)). |
| SDK message interaction data | Ouvertures directes de notifications push, interactions avec les messages in-app, interactions avec les Content Cards | Cet attribut est utilisé à des fins de contrôle qualité, par exemple pour vérifier qu'un message a bien été reçu et que l'envoi n'est pas dupliqué. |
| SDK version | La version actuelle du SDK | Cet attribut est utilisé pour envoyer les messages uniquement aux appareils compatibles et éviter les interruptions de service. |
| Session ID and session timestamp | Identifiant de session, une chaîne de caractères générée aléatoirement et horodatage de session | Utilisé pour déterminer si l'utilisateur démarre une nouvelle session ou poursuit une session existante, et pour déterminer la rééligibilité des messages destinés à cet utilisateur.<br><br>Certains canaux de communication tels que les messages in-app et les Content Cards sont synchronisés sur l'appareil au début de la session. Notre back-end utilise ensuite les données relatives au dernier contact avec les serveurs de Braze (que l'appareil stocke et renvoie) pour savoir si l'utilisateur est éligible à de nouveaux messages. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Intégration minimale" }

### Indicateurs calculés {#calculated-metrics}

Braze génère des indicateurs calculés à partir de trois sources : les [données suivies par le SDK](#minimum-integration) (par exemple, [le début et la fin de session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)), les [données d'interaction des messages pour les canaux non SDK]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) et les [champs de reporting dérivés par Braze]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Ces valeurs sont générées par les services Braze, de sorte qu'un profil utilisateur peut contenir à la fois des données suivies par le SDK et des données générées par Braze.

Les indicateurs calculés comprennent des indicateurs basés sur les canaux (répertoriés dans le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary)) et les attributs suivants.

| Attribut                                       | Description                                                          |
|------------------------------------------------|----------------------------------------------------------------------|
| First used app                                 | Horodatage                                                           |
| Last used app                                  | Horodatage                                                           |
| Total session count                            | Nombre                                                               |
| Clicked card                                   | Nombre                                                               |
| Last received any message                      | Horodatage                                                           |
| Last received email campaign                   | Horodatage                                                           |
| Last received push campaign                    | Horodatage                                                           |
| Number of feedback items                       | Nombre                                                               |
| Number of sessions in the last Y days          | Nombre et horodatage                                                 |
| Received message from campaign                 | Booléen. Ce filtre cible les utilisateurs selon qu'ils ont reçu ou non une Campaign précédente. |
| Received message from campaign with tag        | Booléen. Ce filtre cible les utilisateurs selon qu'ils ont reçu ou non une Campaign comportant actuellement une étiquette. |
| Retarget campaign                              | Booléen. Ce filtre cible les utilisateurs selon qu'ils ont ouvert ou cliqué sur un e-mail, une notification push ou un message in-app spécifique dans le passé. |
| Uninstalled                                    | Booléen et horodatage                                                |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs calculés" }

L'intégration minimale signifie que vous ne collectez que les données requises répertoriées dans [Intégration minimale](#minimum-integration) et que vous désactivez les [données facultatives collectées par défaut](#optional-data-collected-by-default) en [bloquant la collecte de données facultatives du SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview).

{% alert important %}
Si vous souhaitez une intégration minimale et que vous utilisez mParticle, Segment, Tealium ou GTM, notez les points suivants :
- **Plateformes mobiles** : vous devez mettre à jour manuellement le code pour ces configurations. mParticle et Segment ne proposent pas de moyen de le faire via leur plateforme.
- **Web** : l'intégration Braze doit être effectuée nativement pour permettre la configuration d'intégration minimale. Les gestionnaires de balises ne proposent pas de moyen de le faire via leur plateforme.
{% endalert %}

## Données optionnelles collectées par défaut {#optional-data-collected-by-default}

En plus des données d'intégration minimales, les attributs suivants sont automatiquement capturés par Braze lorsque vous initialisez l'intégration SDK. Vous pouvez [désactiver]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) la collecte de ces attributs pour permettre une intégration minimale.

| Attribut               | Plateforme          | Description                                                                        | Raison de la collecte                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nom du navigateur            | Web               | Nom du navigateur                                                                | Cet attribut est utilisé pour envoyer des messages uniquement aux navigateurs compatibles. Il peut également être utilisé pour la segmentation par navigateur.                                     |
| Paramètres régionaux de l'appareil           | Android, iOS, Web | Les paramètres régionaux par défaut de l'appareil                                                   | Cet attribut est utilisé pour traduire les messages dans la langue préférée de l'utilisateur.                                                                                            |
| Paramètres régionaux les plus récents de l'appareil           | Android, iOS, Web | Les paramètres régionaux par défaut les plus récents de l'appareil                                                   | Cet attribut provient des paramètres de l'appareil de l'utilisateur et est utilisé pour traduire les messages dans la langue préférée de l'utilisateur. Il est indépendant de l'attribut `Most Recent Location`.                                                                                            |
| Modèle de l'appareil            | Android, iOS      | Le matériel spécifique de l'appareil                                                | Cet attribut est utilisé pour envoyer des messages uniquement aux appareils compatibles. Il peut également être utilisé dans la segmentation.                                                 |
| Marque de l'appareil            | Android           | La marque de l'appareil (par exemple, Samsung)                                         | Cet attribut est utilisé pour envoyer des messages uniquement aux appareils compatibles.                                                                                          |
| Opérateur sans fil de l'appareil | Android, iOS      | L'opérateur mobile                                                                 | Cet attribut est utilisé de manière optionnelle pour le ciblage des messages.<br><br>**Remarque :** Ce champ est obsolète depuis iOS 16 et sera défini par défaut à `--` dans une future version d'iOS. |
| Langue                | Android, iOS, Web | Langue de l'appareil ou du navigateur, dérivée des paramètres régionaux de l'appareil.                                                           | Cet attribut est utilisé pour traduire les messages dans la langue préférée de l'utilisateur. Il est basé sur les paramètres régionaux de l'appareil.                                                                                            |
| Paramètres de notification   | Android, iOS, Web | Si cette application a les notifications push activées.                                   | Cet attribut est utilisé pour activer les notifications push.                                                                                                                    |
| Résolution              | Android, iOS, Web | Résolution de l'appareil ou du navigateur                                                          | Utilisé de manière optionnelle pour le ciblage des messages par appareil. Le format de cette valeur est « `<width>`x`<height>` ».                                                                 |
| Fuseau horaire               | Android, iOS, Web | Fuseau horaire de l'appareil ou du navigateur                                                           | Cet attribut est utilisé pour envoyer les messages au moment approprié, en fonction du fuseau horaire local de chaque utilisateur.                                                   |
| Agent utilisateur              | Web               | [Agent utilisateur](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Cet attribut est utilisé pour envoyer des messages uniquement aux appareils compatibles. Il peut également être utilisé dans la segmentation.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Données optionnelles collectées par défaut" }

Pour en savoir plus sur le suivi des propriétés au niveau de l'appareil (telles que l'opérateur sans fil, le fuseau horaire, la résolution, etc.), consultez la documentation spécifique à chaque plateforme : [Android]({{site.baseurl}}/developer_guide/storage?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage#cookies).

## Données non collectées par défaut {#data-not-collected-by-default}

Par défaut, les attributs suivants ne sont pas collectés. Chaque attribut doit être intégré manuellement.

| Attribut                  | Plateforme     | Description                                                                                                                                                                                                                                                                                                               | Raison de la non-collecte                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Suivi publicitaire activé sur l'appareil | Android, iOS | Sur iOS :<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Sur Android :<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Cette propriété nécessite des autorisations supplémentaires au niveau de l'application, qui doivent être accordées par l'intégrateur.                                                                                                                                                                                                      |
| IDFA de l'appareil                | iOS          | Identifiant de l'appareil pour les annonceurs                                                                                                                                                                                                                                                                                         | Cela nécessite le framework Ad Tracking Transparency, qui déclenchera un examen supplémentaire de la confidentialité par l'App Store. Pour plus de détails, consultez [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| Google Advertising ID      | Android      | Identifiant publicitaire au sein des applications Google Play                                                                                                                                                                                                                                                                        | Cela nécessite que l'application récupère le GAID et le transmette à Braze. Pour plus de détails, consultez [Google Advertising ID facultatif]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Localisation la plus récente | Android, iOS | Il s'agit de la dernière position GPS connue de l'appareil de l'utilisateur. Elle est mise à jour au démarrage de la session et stockée dans le profil de l'utilisateur. | Cela nécessite que l'utilisateur accorde l'autorisation de localisation à votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Données non collectées par défaut" }

{% alert note %}
Le SDK Braze ne stocke aucune adresse IP localement.
{% endalert %}

## Intégration personnalisée {#personalized-integration}

Pour tirer le meilleur parti de Braze, nos intégrateurs SDK implémentent souvent les SDK Braze et enregistrent des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes), des [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events#logging-custom-events) et des [événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#log-purchase-events) pertinents pour leur activité, en complément des données collectées automatiquement.

Une intégration personnalisée permet une communication sur mesure, adaptée à l'expérience de vos utilisateurs.

{% alert important %}
Braze bloque les profils utilisateur (« utilisateurs factices ») ayant plus de 5 000 000 de sessions, plus de 20 000 noms d'événements personnalisés distincts ou plus de 20 000 noms de produits distincts dans les achats, et cesse d'ingérer toutes les données entrantes pour ce profil, que ce soit depuis les SDK ou la REST API. Pour en savoir plus, consultez [Blocage du spam]({{site.baseurl}}/user_archival).
{% endalert %}