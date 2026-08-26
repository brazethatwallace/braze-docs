---
nav_title: Présentation de l'intégration
article_title: Présentation de l'intégration
page_order: 2
description: "Cet article donne un aperçu du processus d'onboarding."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"} Premiers pas : présentation de l'intégration {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordergetting-started-integration-overview}

> Cet article donne un aperçu du processus d'onboarding.

![Diagramme de Venn avec quatre cercles (découverte, intégration, assurance qualité et maintenance) centré sur le délai de rentabilisation.]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"}

En tant que ressource technique, vous donnerez à votre équipe les moyens d'agir en intégrant Braze dans votre tech stack. L'onboarding se divise globalement en quatre étapes :
* [Découverte et planification](#discovery) : Travaillez avec votre équipe pour vous aligner sur le périmètre, planifier une structure pour les données et les campagnes, et créer une structure d'espace de travail appropriée.
* [Intégration](#integration) : Exécutez votre plan en intégrant le SDK et l'API, en activant les canaux de communication et en configurant l'importation et l'exportation des données.
* [Assurance qualité](#qa) : Confirmez que la boucle de données et d'envoi de messages entre la plateforme Braze et votre application ou site fonctionne comme prévu.
* [Maintenance](#maintenance) : Une fois que vous aurez transmis Braze à votre équipe marketing, vous continuerez à veiller à ce que tout se passe bien.

<br>
{% alert tip %}
Nous sommes conscients que chaque organisation a des besoins distincts, et Braze est conçu pour répondre à une gamme variée d'options de personnalisation qui peuvent être adaptées à vos exigences spécifiques. Les délais d'intégration varient en fonction de votre cas d'usage.
{% endalert %}

## Découverte et planification {#discovery}

Au cours de cette phase, vous travaillerez avec votre équipe pour définir les tâches d'onboarding et veiller à ce que toutes les parties prenantes s'alignent sur un objectif commun.

Votre équipe effectuera une planification de bout en bout de vos cas d'usage pour s'assurer que tout peut être créé comme prévu, avec les bonnes données disponibles pour le faire. Cette phase inclut votre chef de projet, votre responsable CRM, l'ingénierie front-end et back-end, les propriétaires de produits et les marketeurs.

La phase de découverte et de planification dure en moyenne six semaines. Les responsables de l'ingénierie peuvent s'attendre à passer 2 à 4 heures par semaine au cours de cette phase. Les développeurs qui travaillent avec le produit peuvent s'attendre à passer 10 à 20 heures par semaine sur Braze pendant la phase de découverte et de planification.

{% alert tip %}
Pendant la période d'onboarding de votre entreprise, Braze organisera des séances de présentation technique. Nous recommandons vivement aux ingénieurs de participer à ces sessions. Les séances de présentation technique vous donnent l'occasion d'aborder l'évolutivité de l'architecture de la plateforme et de voir des exemples pratiques de la façon dont certaines entreprises de votre taille ont précédemment réussi avec des cas d'usage similaires.
{% endalert %}

![Icônes pour différents canaux, tels que l'e-mail, le panier d'achat, les images, la géolocalisation, etc.]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

### Planification des campagnes {#campaign-planning}

Votre équipe CRM planifiera les cas d'usage de communication que vous lancerez dans un avenir proche. Ceci inclut les éléments suivants :
* [Canal]({{site.baseurl}}/user_guide/channels) (par exemple, notifications push ou messages in-app)
* [Méthode de réception/distribution]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) (par exemple, livraison planifiée ou livraison par événement)
* [Audience cible]({{site.baseurl}}/user_guide/audience/segments)
* [Indicateurs de réussite]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)

Par exemple, une campagne destinée aux nouveaux clients pourrait consister en un e-mail envoyé tous les jours à 10 heures à un segment de clients qui ont enregistré leur première session hier. L'événement de conversion (l'indicateur de réussite) consiste à enregistrer une session.

<br>
{% alert important %}
L'intégration ne peut pas commencer tant que l'étape de planification des campagnes n'est pas terminée. Cette étape permettra de déterminer quelles parties de Braze doivent être configurées au cours de la phase d'intégration.
{% endalert %}

### Créer des exigences en matière de données {#creating-data-requirements}

Ensuite, votre équipe CRM doit définir les données nécessaires pour lancer les campagnes qu'elle a planifiées, en créant des exigences en matière de données.

De nombreux types courants d'attributs utilisateur, tels que le nom, l'e-mail, la date de naissance, le pays et autres, font automatiquement l'objet d'un suivi après l'intégration du SDK Braze. Les autres types de données devront être définis comme des données personnalisées.

En tant que développeur, vous travaillerez avec votre équipe pour définir les données supplémentaires et personnalisées qu'il serait judicieux de suivre. Vos données personnalisées auront un impact sur la façon dont votre base d'utilisateurs sera classée et segmentée. Vous mettrez en place une taxonomie d'événements à travers vos outils de croissance, en structurant vos données de manière à ce qu'elles soient compatibles avec vos systèmes lorsqu'elles entrent et sortent de Braze.

{% alert tip %}
Veillez à ce que la nomenclature des données soit cohérente d'un outil à l'autre. Par exemple, votre entrepôt de données peut enregistrer « offre d'achat à durée limitée » d'une manière particulière. Vous devrez décider si un événement personnalisé est nécessaire dans Braze pour correspondre à ce format.
{% endalert %}

En savoir plus sur les [données collectées automatiquement et les données personnalisées]({{site.baseurl}}/developer_guide/analytics).

### Planification des personnalisations {#customizations-planning}

Discutez avec vos marketeurs des personnalisations qu'ils souhaitent. Par exemple, souhaitez-vous implémenter les Content Cards par défaut de Braze ? Souhaitez-vous modifier légèrement leur apparence pour qu'elles correspondent à vos directives de marque ? Voulez-vous développer une toute nouvelle interface utilisateur pour un composant et faire en sorte que Braze suive son analytique ? Différents niveaux de personnalisation nécessitent différents niveaux de portée.

### Obtenir l'accès au tableau de bord {#getting-dashboard-access}

Le tableau de bord de Braze constitue notre interface utilisateur sur le Web. Les marketeurs utiliseront le tableau de bord pour faire leur travail et créer du contenu. Les développeurs utilisent le tableau de bord pour gérer les paramètres d'intégration des applications, comme les clés API et les informations d'identification de notifications push.

L'administrateur de votre équipe doit vous ajouter (ainsi que tous les autres membres de l'équipe qui ont besoin d'accéder à Braze) en tant qu'utilisateurs sur votre tableau de bord.

### Espaces de travail et clés API {#workspaces-and-api-keys}

L'administrateur de votre équipe créera également différents [espaces de travail]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces). Les espaces de travail regroupent vos données — utilisateurs, segments, clés API — en un seul emplacement. Nous vous conseillons de ne regrouper que les différentes versions d'une même application ou d'applications très similaires au sein d'un même espace de travail.

Fait important, les espaces de travail fournissent des clés API pour plusieurs plateformes (comme iOS et Android). Vous utiliserez les clés API corrélées pour associer les données du SDK à un espace de travail particulier. Naviguez vers vos espaces de travail pour accéder à la clé API de chacune de vos applications. Assurez-vous que chaque clé API dispose des autorisations nécessaires pour effectuer le travail que vous avez défini. Pour plus de détails, consultez l'[article sur le provisionnement de l'API]({{site.baseurl}}/api/basics#rest-api-key-permissions).

Pour les implémentations Web couvrant plusieurs domaines racines, consultez [Intégration multi-domaine pour le SDK Web de Braze]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration) afin de déterminer s'il convient d'utiliser une seule application ou des applications et clés API distinctes.

{% alert important %}
Il est important que vous mettiez en place des environnements différents pour le développement et la production. La mise en place d'un environnement de test vous évitera de dépenser de l'argent réel lors de l'onboarding et de l'assurance qualité. Pour créer un environnement de test, configurez un espace de travail de test et veillez à utiliser sa clé API afin de ne pas alimenter votre espace de travail de production avec des données de test.
{% endalert %}

## Intégration {#integration}

![Graphique pyramidal abstrait représentant le flux d'informations d'une source de données vers un appareil utilisateur.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"}

Braze prend en charge les applications iOS, les applications Android, les applications web, et bien plus encore. Vous pouvez également opter pour l'utilisation d'un SDK wrapper multiplateforme, comme React Native ou Unity. En règle générale, les clients réalisent l'intégration en 1 à 6 semaines. De nombreux clients ont intégré Braze avec un seul ingénieur, en fonction de l'étendue de ses compétences techniques et de sa disponibilité. Tout dépend de votre périmètre d'intégration spécifique et du temps que votre équipe consacre au projet Braze.

Vous aurez besoin de développeurs capables de :
* Travailler dans la couche native de votre application ou de votre site
* Créer des processus pour utiliser notre REST API
* Effectuer des tests d'intégration
* Gérer l'authentification par jeton web JSON
* Maîtriser les compétences générales en matière de gestion des données
* Configurer des enregistrements DNS

### Partenaires d'intégration CDP {#cdp-integration-partners}

De nombreux clients profitent de l'onboarding de Braze pour réaliser également une intégration avec une plateforme de données client (CDP) en tant que partenaire d'intégration. Braze assure le suivi et l'analytique des données, tandis qu'un CDP peut fournir un acheminement et une orchestration supplémentaires des données. Braze offre une intégration fluide avec de nombreux CDP, tels que [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle) et [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment).

Si vous effectuez une intégration côte à côte avec un CDP, vous mapperez les appels du SDK de votre CDP vers le SDK de Braze. Globalement, vous devrez :
* Mapper les appels d'identification sur `changeUser` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)) et définir les attributs.
* Mapper les appels de vidage de données sur `requestImmediateDataFlush` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)).
* Enregistrer les événements personnalisés ou les achats.

Des exemples d'intégration entre le SDK de Braze et le CDP de votre choix peuvent être disponibles, en fonction de la plateforme que vous avez choisie. Pour plus d'informations, consultez notre [liste de partenaires technologiques CDP]({{site.baseurl}}/partners/data_and_analytics).

### Intégration du SDK Braze {#braze-sdk-integration}

Le SDK de Braze fournit deux fonctionnalités essentielles : il collecte et synchronise les données des utilisateurs dans un profil utilisateur consolidé, et alimente les canaux de communication tels que les notifications push, les messages in-app et les Content Cards.

{% alert tip %}
Lorsqu'il est entièrement intégré à votre application ou à votre site, le SDK de Braze offre un niveau de sophistication marketing pleinement abouti. Si vous différez l'intégration du SDK de Braze, certaines des fonctionnalités décrites dans la documentation ne seront pas disponibles.
{% endalert %}

{% alert note %}
Pour renforcer la sécurité, vous pouvez activer l'[authentification SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication) afin d'empêcher les requêtes SDK non autorisées. Cette fonctionnalité est disponible sur toutes les principales plateformes, notamment Web, iOS, Android, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) et Expo.
{% endalert %}

Au cours du déploiement du SDK, vous devrez :

* Rédiger un code d'intégration SDK pour chaque plateforme que vous souhaitez prendre en charge.
* Activer les canaux de communication pour chaque plateforme, en veillant à ce que le SDK de Braze suive les données issues de vos interactions avec vos clients par e-mail, SMS, notifications push et autres canaux.
* Créer toutes les personnalisations prévues pour les composants de l'interface utilisateur (par exemple, des Content Cards personnalisées). Pour un contenu entièrement personnalisé, vous devrez enregistrer les analyses, car la collecte automatique des données du SDK n'aura pas connaissance de vos nouveaux composants. Vous pouvez reproduire cette implémentation sur la base de nos composants par défaut.

### Utiliser l'API de Braze {#using-the-braze-api}

Vous utiliserez notre REST API pour différentes tâches à différents moments tout au long de votre utilisation de Braze. L'API de Braze est utile pour :

1. Importer des données historiques ; et
2. Effectuer des mises à jour continues qui ne sont pas déclenchées dans Braze. Par exemple, un profil utilisateur passe au niveau VIP sans que l'utilisateur se connecte à une application, l'API doit donc communiquer cette information à Braze.

Commencez à utiliser l'[API de Braze]({{site.baseurl}}/api/basics).

{% alert important %}
Lorsque vous utilisez l'API, veillez à grouper vos requêtes et à n'envoyer que des valeurs delta. Braze réécrit chaque attribut envoyé. Ne mettez pas à jour un attribut personnalisé si sa valeur n'a pas changé.
{% endalert %}

### Mise en place de l'analytique produit {#setting-up-product-analytics}

Braze est une plateforme orientée données. Les données dans Braze sont stockées sur le profil utilisateur.

Les points de données constituent une structure qui vous permet de vous assurer que vous capturez les bonnes données pour vos marketeurs, et pas seulement « n'importe quelle » donnée que vous pourriez aspirer. Familiarisez-vous avec les [points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

### Migration des données utilisateur existantes {#migrating-legacy-user-data}

Vous pouvez utiliser l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze pour migrer des données historiques enregistrées en dehors de Braze. Les jetons de notification push et les achats passés sont des exemples de données couramment importées. Cet endpoint peut être utilisé pour des importations ponctuelles ou des mises à jour régulières par lots.

Vous pouvez également importer des utilisateurs et mettre à jour les valeurs des attributs clients via un [chargement CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) ponctuel dans le tableau de bord. Le chargement de fichiers CSV peut être utile pour les marketeurs, tandis que notre REST API offre une plus grande flexibilité.

### Mise en place du suivi de session {#setting-up-session-tracking}

Le SDK de Braze génère des points de données « ouverture de session » et « fermeture de session ». Le SDK de Braze vide également les données à intervalles réguliers. Consultez ces liens pour connaître les valeurs par défaut du suivi de session, qui peuvent toutes être personnalisées ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)).

### Suivi des événements personnalisés, des attributs et des événements d'achat {#tracking-custom-events-attributes-and-purchase-events}

Coordonnez-vous avec votre équipe pour mettre en place votre schéma de données planifié, incluant les événements personnalisés, les attributs utilisateur et les événements d'achat. Votre [schéma de données personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) sera saisi via le tableau de bord et doit correspondre exactement à ce que vous implémentez lors de l'intégration SDK.

{% alert tip %}
Les identifiants utilisateur, appelés `external_id` dans Braze, doivent être définis pour tous les utilisateurs connus. Ils doivent être immuables et accessibles lorsque l'utilisateur ouvre l'application, vous permettant de suivre vos utilisateurs sur différents appareils et plateformes. Consultez l'article sur le [cycle de vie de l'utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) pour connaître les meilleures pratiques.
{% endalert %}

### Autres outils {#other-tools}

En fonction de votre cas d'usage, il se peut que vous ayez besoin de configurer d'autres outils. Par exemple, vous pourriez avoir besoin de mettre en place un outil comme les [géorepérages]({{site.baseurl}}/user_guide/audience/locations_and_geofences) pour concrétiser vos scénarios utilisateur. Nous avons constaté que les clients qui configurent ces outils supplémentaires après avoir effectué les étapes essentielles de l'intégration sont ceux qui réussissent le mieux.

## Assurance qualité {#qa}
Au fur et à mesure de l'exécution de votre intégration, vous effectuerez une assurance qualité afin de vous assurer que tout ce que vous mettez en place fonctionne comme prévu. Cette assurance qualité se divise en deux catégories générales : l'ingestion de données et les canaux de communication.

{% alert important %}
Assurez-vous que vos environnements de production et de test sont configurés avant de commencer l'assurance qualité.
{% endalert %}

| **Ingestion de données pour l'assurance qualité**  | **Envoi de messages pour l'assurance qualité** |
|---------------------------|---------------------------------------------------------------|
| Vous assurerez la qualité de l'ingestion, du stockage et de l'exportation des données. | Vous vous assurerez que vos messages sont envoyés correctement à vos utilisateurs et que tout se présente bien. |
| Effectuez des tests pour confirmer que les données sont stockées correctement. | Créez des Segments d'utilisateurs. |
| Confirmez que les données de session sont correctement attribuées à l'espace de travail prévu dans Braze. | Lancez des Campaigns et des Canvas avec succès. |
| Confirmez que les débuts et les fins de session sont enregistrés. | Confirmez que les bonnes campagnes sont diffusées aux bons Segments d'utilisateurs. |
| Confirmez que les informations relatives aux attributs des utilisateurs sont correctement enregistrées dans les profils utilisateur. | Confirmez que les jetons de notification push sont correctement enregistrés. |
| Testez que les données personnalisées sont correctement enregistrées par rapport aux profils utilisateur. | Confirmez que les jetons de notification push sont correctement retirés. |
| Créez des profils utilisateur anonymes. | Testez que les campagnes push sont correctement envoyées aux appareils et que l'engagement est enregistré. |
| Confirmez que les profils utilisateur anonymes deviennent des profils utilisateur connus lorsque la méthode `changeUser()` est appelée. | Testez que les messages in-app sont distribués et que les indicateurs sont enregistrés. |
|                           | Vérifiez que les Content Cards sont distribuées et que les indicateurs sont enregistrés. |
|                           | Facilitez le contenu connecté (par exemple, Accuweather). |
|                           | Confirmez que toutes les intégrations des canaux de communication fonctionnent correctement ensemble. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Assurance qualité" }

{% alert note %}
Lors de l'assurance qualité de votre intégration SDK, utilisez le [débogueur SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) pour résoudre les problèmes sans avoir à activer la journalisation détaillée pour votre application.
{% endalert %}

### Transmission de Braze aux marketeurs {#passing-braze-off-to-marketers}

Une fois que vous avez intégré votre plateforme ou votre site, vous voudrez impliquer votre équipe marketing pour lui transmettre la propriété de la plateforme. Ce processus est différent d'une entreprise à l'autre, mais il peut comprendre les éléments suivants :

* Composer une [logique Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) complexe
* Faciliter le [réchauffement d'adresses IP des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)
* S'assurer que les autres parties prenantes comprennent le type de données qui font l'objet d'un suivi

### Développer pour l'avenir {#develop-for-the-future}

Vous est-il déjà arrivé d'hériter d'une base de code et de n'avoir aucune idée de ce à quoi pensait le développeur initial ? Pire encore, avez-vous déjà écrit du code, l'avez compris parfaitement, puis vous êtes senti complètement déconcerté lorsque vous y êtes revenu un an plus tard ?

Lors de l'onboarding de Braze, les décisions collectives que vous prenez concernant les données, les profils utilisateur, les intégrations qui étaient ou non dans le périmètre, la façon dont les personnalisations sont censées fonctionner, et plus encore, vous sembleront fraîches dans votre esprit et donc évidentes. Lorsque votre équipe souhaitera développer Braze ou lorsque d'autres ressources techniques seront affectées à votre projet Braze, ces informations seront obscures.

Créez une ressource pour consolider les informations que vous avez apprises au cours de vos séances de présentation technique. Cette ressource vous aidera à réduire le temps nécessaire à l'onboarding des nouveaux développeurs qui rejoignent votre équipe (ou vous servira d'aide-mémoire lorsque vous devrez étendre votre déploiement actuel de Braze).

## Maintenance {#maintenance}

Après le transfert à vos marketeurs, vous continuerez à servir de ressource pour la maintenance. Vous serez attentif aux mises à jour d'iOS et d'Android susceptibles d'avoir un impact sur le SDK Braze et vous vous assurerez que vos fournisseurs tiers sont à jour.

Vous assurerez le suivi des mises à jour de la plateforme Braze via le [référentiel GitHub](https://github.com/braze-inc/) de Braze. Occasionnellement, votre administrateur recevra également des e-mails concernant des mises à jour urgentes et des corrections de bogues directement de Braze.

## Limites de débit du SDK {#sdk-rate-limits}

### Monthly Active Users CY 24-25, Universal MAU, Web MAU et Mobile MAU {#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau}

Pour les clients ayant acheté les offres Monthly Active Users CY 24-25, Universal MAU, Web MAU et Mobile MAU, Braze applique des limites de débit côté serveur sur les requêtes API utilisées par nos SDK pour mettre à jour les sessions, les attributs utilisateur, les événements et les autres données de profil utilisateur. Cela permet de garantir la stabilité de la plateforme et de maintenir un service rapide et fiable.

* Les limites de débit horaires sont définies en fonction du trafic SDK attendu sur votre compte, qui peut correspondre au nombre d'utilisateurs actifs mensuels (MAU) que vous avez achetés, à votre secteur d'activité, à la saisonnalité ou à d'autres facteurs. Lorsque la limite de débit horaire est atteinte, Braze limite les requêtes jusqu'à l'heure suivante.
* Toutes les requêtes soumises à une limitation de débit sont automatiquement réessayées par le SDK.
* Les requêtes du SDK sont corrélées à la quantité de données personnalisées collectées dans votre déploiement. Si vous êtes régulièrement proche ou à votre limite de débit horaire, envisagez de :
    * Revoir votre intégration SDK pour réduire la collecte excessive de données.
    * Mettre sur liste de blocage les données personnalisées qui ne sont pas essentielles pour vos cas d'usage marketing.
* Les limites de débit en rafale sont des limites de débit de courte durée qui s'appliquent lorsqu'un volume élevé de requêtes arrive dans un laps de temps très court (c'est-à-dire en quelques secondes). Vous n'avez pas besoin d'agir lorsque des limites en rafale se produisent, et le SDK réessaiera peu après.
* Les limites de débit soutenues contrôlent le volume de requêtes soutenu sur une fenêtre glissante plus longue que la fenêtre de rafale (par exemple, plusieurs minutes) et permettent de lisser le trafic continu entre les limites en rafale et votre limite de débit horaire.

### Trouver vos limites de débit {#finding-your-rate-limits}

Pour connaître les limites actuelles basées sur le débit SDK attendu, accédez à **Paramètres** > **API et identifiants** > **Limites API et SDK**.

Pour l'historique d'utilisation, accédez à **Paramètres** > **API et identifiants** > **Tableau de bord API et SDK**.

### Demander des limites de débit plus élevées {#requesting-higher-rate-limits}

Si vous avez besoin d'une limite de débit Braze plus élevée, contactez le support Braze ou votre gestionnaire du succès des clients et incluez les détails suivants :

* Si vous avez besoin d'une augmentation temporaire ou permanente.
* Pourquoi vous avez besoin de cette augmentation.
* Quels endpoints et environnements sont concernés.
* Votre volume de trafic approximatif et le calendrier prévu, y compris la date de début, la durée et les heures de pointe.
* Si vous pouvez regrouper les appels ou répartir le trafic dans le temps.

Après avoir soumis votre demande, Braze l'examine et vous communique le résultat.

### Modifications et support {#changes-and-support}

Braze peut modifier les limites de débit pour protéger la stabilité du système ou permettre un débit de données plus élevé sur votre compte. Contactez le support Braze ou votre gestionnaire du succès des clients pour toute question ou préoccupation concernant les limites de débit et leur impact sur votre activité.