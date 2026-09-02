---
nav_title: Vue d'ensemble architecturale
article_title: Vue d'ensemble architecturale
page_order: 3
description: "Cet article traite des différentes parties et composants de la pile technologique Braze, avec des liens vers des articles pertinents."
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

# Démarrage : Vue d'ensemble architecturale {#getting-started-architectural-overview}

> Cet article traite des différentes parties et composants de la pile technologique Braze, avec des liens vers des articles pertinents.

Globalement, Braze est une plateforme orientée données. La plateforme Braze, alimentée par le SDK, la REST API et les intégrations partenaires, vous permet d'agréger et d'exploiter vos données.

![Braze comporte différentes couches. De manière générale, la plateforme se compose du SDK, de l'API, du tableau de bord et des intégrations partenaires. Chacun de ces éléments contribue à une couche d'ingestion de données, une couche de classification, une couche d'orchestration, une couche de personnalisation et une couche d'action. La couche d'action dispose de différents canaux, notamment les notifications push, les messages in-app, le catalogue connecté, le webhook, les SMS et les e-mails.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Ingestion de données](#ingestion) : Braze tire des données de diverses sources.
* [Classification](#classification) : Votre équipe marketing segmente dynamiquement votre base d'utilisateurs en utilisant ces indicateurs.
* [Orchestration](#orchestration) : Braze coordonne intelligemment les messages à différents segments d'audience au moment idéal.
* [Action](#action) : Votre équipe marketing exploite les données en créant du contenu à travers une variété de canaux de communication, tels que les SMS et les e-mails.
* [Personnalisation](#personalization) : Les données sont transformées en temps réel avec des informations personnalisées sur votre audience.
* [Exportation](#exporting-data) : Ensuite, Braze suit l'engagement de vos utilisateurs avec ces messages et le renvoie dans la plateforme, créant une boucle. Vous obtenez des informations sur ces données grâce à des rapports et des analyses en temps réel.

Tout cela fonctionne ensemble pour créer des interactions réussies entre votre base d'utilisateurs et votre marque afin que vous puissiez atteindre vos objectifs. Braze fait tout cela dans le contexte de ce que nous appelons notre pile intégrée verticalement. Examinons chaque couche, une à la fois.

## Ingestion de données {#ingestion}

La plateforme Braze s'appuie sur une architecture de flux de données en continu, exploitant Snowflake, Kafka, MongoDB et Redis. Les données provenant de diverses sources peuvent être intégrées à Braze via le SDK et l'API. La plateforme est capable de gérer toutes les données en temps réel, quelle que soit leur imbrication ou leur structure. Les données dans Braze sont stockées sur le profil utilisateur.

{% alert tip %}
Braze peut suivre les données d'un utilisateur tout au long de son parcours avec vous, depuis le moment où il est anonyme jusqu'au moment où il est connecté à votre application et identifié. Les identifiants d'utilisateur, appelés `external_id`s dans Braze, doivent être définis pour chacun de vos utilisateurs. Ces identifiants doivent être immuables et accessibles lorsque l'utilisateur ouvre l'application, vous permettant de suivre vos utilisateurs sur différents appareils et plateformes. Consultez l'[article sur le cycle de vie des utilisateurs]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) pour connaître les bonnes pratiques.
{% endalert %}

![Braze importe des sources de données backend depuis l'API, des sources de données frontend depuis le SDK, des données d'entrepôt de données à partir de l'ingestion de données cloud de Braze, et depuis des intégrations partenaires. Ces données sont exportées via l'API Braze.]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
Cette base de données de profils utilisateur centrée sur la personne permet une vitesse interactive en temps réel. Braze pré-calcule les valeurs lorsque les données arrivent et stocke les résultats dans un format de document léger pour une récupération rapide. Et comme la plateforme a été conçue de cette manière dès le départ, elle est idéale pour la plupart des cas d'usage de communication, en particulier en combinaison avec d'autres concepts de données tels que le contenu connecté, les catalogues de produits et les attributs imbriqués.
{% endalert %}

### Répartition des sources de données {#data-source-breakdown}

Braze utilise différents systèmes de stockage de données pour diverses fonctionnalités. Il est essentiel de comprendre quelles fonctionnalités utilisent quelles sources de données pour la gestion des données et la résolution des problèmes.

#### Fonctionnalités basées sur MongoDB {#mongodb-powered-features}
- Événements personnalisés (suivis par le SDK et l'API)
- Attributs personnalisés
- Profils utilisateur
- Événements d'achat
- La plupart des fonctionnalités de segmentation et de ciblage

#### Fonctionnalités optimisées par Snowflake {#snowflake-powered-features}
- [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Suite de prédiction]({{site.baseurl}}/user_guide/brazeai)
- [Recommandations d'articles personnalisées par l'IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai)
- [Taux d'ouverture réel estimé]({{site.baseurl}}/user_guide/channels/email/reporting#estimated-real-open-rate) (n'utilise pas les événements personnalisés)

{% alert important %}
**Considérations relatives à la suppression des données :** Les événements personnalisés sont stockés dans MongoDB et sont distincts des données Snowflake. Si vous devez supprimer des données d'événements personnalisés erronées, vous devez le faire dans MongoDB. Les fonctionnalités optimisées par Snowflake (telles que les extensions de segments SQL et d'autres fonctionnalités optimisées par Snowflake) utilisent les données de Snowflake, qui sont traitées séparément. La suppression de données d'un système ne les supprime pas automatiquement de l'autre.
{% endalert %}

### Sources de données backend via l'API Braze {#backend-data-sources-through-the-braze-api}
Braze peut extraire des données des bases de données utilisateur, des transactions hors ligne et des entrepôts de données par le biais de notre [REST API]({{site.baseurl}}/api/endpoints/user_data).

### Sources de données frontend via le SDK Braze {#frontend-data-sources-through-braze-sdk}
Braze capture automatiquement des données first-party à partir de sources de données frontend, telles que les appareils des utilisateurs, par le biais du [SDK Braze]({{site.baseurl}}/user_guide/get_started/sdk_overview). Le SDK gère les nouveaux utilisateurs (anonymes) et gère les données de leur profil utilisateur tout au long de leur cycle de vie.

### Intégrations partenaires {#partner-integrations}
Braze compte plus de 150 partenaires technologiques, que nous appelons « Alloys ». Vous pouvez compléter vos flux de données par un réseau solide de [technologies interopérables et d'API de données.]({{site.baseurl}}/partners/home)

### Connexion directe à l'entrepôt via l'ingestion de données cloud de Braze {#direct-warehouse-connection-through-braze-cloud-data-ingestion}
Vous pouvez transmettre des données clients de votre entrepôt de données à la plateforme via l'[ingestion de données cloud de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) en quelques minutes seulement, ce qui vous permet de synchroniser les attributs, les événements et les achats pertinents des utilisateurs. L'intégration de l'ingestion de données cloud prend en charge des structures de données complexes, y compris des JSON imbriqués et des tableaux d'objets.

L'ingestion de données cloud peut synchroniser les données de Snowflake, Amazon Redshift, Databricks et Google BigQuery.

## Classification {#classification}
La couche de classification permet à votre équipe de classer et de créer dynamiquement des audiences, appelées [segments]({{site.baseurl}}/user_guide/audience/segments), en fonction des données qui transitent par Braze.

{% alert note %}
Les couches de classification, d'orchestration et de personnalisation sont celles où votre équipe marketing effectuera une grande partie de son travail. Elle interagit avec ces couches le plus souvent via le tableau de bord de Braze, notre interface web. Les développeurs ont un rôle dans la configuration et la personnalisation de ces couches.
{% endalert %}

De nombreux types courants d'attributs utilisateur, tels que le nom, l'e-mail, la date de naissance, le pays et d'autres, font l'objet d'un suivi automatique par le SDK par défaut. En tant que développeur, vous travaillerez avec votre équipe pour définir quelles données supplémentaires et personnalisées il est pertinent de suivre pour votre cas d'usage. Vos données personnalisées auront un impact sur la façon dont votre base d'utilisateurs sera classée et segmentée. Vous mettrez en place ce modèle de données au cours du processus de déploiement.

En savoir plus sur les [données collectées automatiquement et les données personnalisées]({{site.baseurl}}/developer_guide/analytics).

## Orchestration {#orchestration}
La couche d'orchestration permet à votre équipe marketing de concevoir des parcours utilisateur basés sur vos données utilisateur et vos engagements antérieurs. Ce travail s'effectue principalement via notre interface de tableau de bord, mais vous avez également la possibilité de lancer des [campagnes via l'API]({{site.baseurl}}/api/api_campaigns). Par exemple, vous pouvez demander à votre backend d'indiquer à Braze quand envoyer les messages et les campagnes que vos marketeurs ont conçus dans le tableau de bord, et de les déclencher selon la logique de votre backend. Un exemple de message déclenché par une API pourrait être des réinitialisations de mot de passe ou des confirmations d'expédition.

{% alert note %}
Les campagnes déclenchées par API sont idéales pour des cas d'usage transactionnels plus avancés. Elles permettent aux marketeurs de gérer le texte des campagnes, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze, tout en déclenchant la distribution de ce contenu depuis vos serveurs et systèmes. La requête API pour déclencher le message peut également inclure des données supplémentaires à intégrer dans le message en temps réel.
{% endalert %}


### Indicateurs de fonctionnalité {#feature-flags}
Braze vous permet d'activer ou de désactiver à distance des fonctionnalités pour une sélection d'utilisateurs au moyen d'[indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags). Cela permet à vos marketeurs de cibler le bon segment de votre base d'utilisateurs avec des messages pour des fonctionnalités que vous n'avez pas encore déployées à l'ensemble de votre audience. Mais plus que cela, les indicateurs de fonctionnalité peuvent être utilisés pour activer et désactiver une fonctionnalité en production sans déploiement de code supplémentaire ni mises à jour de la boutique d'applications. Cela vous permet de déployer de nouvelles fonctionnalités en toute sécurité et en toute confiance.

## Personnalisation {#personalization}
La couche de personnalisation représente la capacité à fournir du contenu dynamique dans vos messages. En utilisant Liquid, un langage de personnalisation largement utilisé, votre équipe peut extraire dynamiquement des données existantes pour afficher le message adapté à chaque destinataire. De plus, vous pouvez insérer toute information accessible sur votre serveur web ou via une API directement dans les messages que vous envoyez, tels que les notifications push ou les e-mails, en utilisant le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Le contenu connecté s'appuie sur Liquid et utilise une syntaxe familière.

De plus, étant donné que ce contenu dynamique est programmable, les marketeurs peuvent inclure des valeurs calculées, des réponses d'autres appels ou des éléments du catalogue de produits. Après avoir mis en place ces systèmes lors du déploiement, votre équipe marketing pourra le faire avec peu ou pas de soutien des équipes techniques.

## Action {#action}
La couche d'action permet de transmettre vos messages réels à vos utilisateurs. Le but de la couche d'action est d'envoyer le bon message au bon utilisateur au bon moment, en fonction des données disponibles à travers toutes les couches précédemment décrites. L'envoi de messages se fait à l'intérieur de votre application ou site (comme l'envoi de messages in-app ou via des éléments graphiques tels que des carrousels de Content Cards et des bannières) ou en dehors de votre expérience sur l'application (comme l'envoi de notifications push ou d'e-mails).

### Canaux de communication {#messaging-channels}
Braze a été conçu pour gérer un paysage technologique en évolution avec son modèle de données centré sur l'utilisateur et indépendant des canaux. Le tableau de bord gère la distribution des messages et les déclencheurs transactionnels. Par exemple, vos marketeurs peuvent déclencher un message SMS offrant un bon de réduction dans l'une de vos nouvelles boutiques lorsqu'un utilisateur entre dans le géorepérage situé près de cet emplacement, ou envoyer un e-mail à un utilisateur pour lui faire savoir que son émission préférée a une nouvelle saison.

Le [SDK Braze]({{site.baseurl}}/user_guide/get_started/sdk_overview) alimente des canaux de communication supplémentaires : push, messages in-app et Content Cards. Vous intégrez le SDK à votre application ou site pour permettre à votre équipe marketing d'utiliser le tableau de bord de Braze pour coordonner ses campagnes sur tous les canaux de communication pris en charge.

![Schéma des canaux de communication Braze disponibles via le SDK.]({% image_buster /assets/img/getting_started/channels.png %})

## Exportation des données {#exporting-data}
De manière essentielle, toutes les interactions des utilisateurs finaux avec Braze sont suivies afin que vous puissiez mesurer votre engagement et votre portée. Une fois que Braze a agrégé vos données provenant de toutes ces sources, elles peuvent être réexportées vers votre tech stack à l'aide de divers outils, bouclant ainsi la boucle.

### Currents
[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) est un module complémentaire optionnel de Braze qui fournit une exportation granulaire en flux continu alimentant en permanence d'autres destinations de votre stack. Currents est un flux de données brutes par utilisateur et par événement qui exporte les données toutes les cinq minutes ou tous les 15 000 événements, selon ce qui se produit en premier. Parmi les exemples de destinations en aval pour Currents, on trouve Segment, S3, Redshift et Mixpanel, entre autres.

### Partage de données Snowflake {#snowflake-data-sharing}
La fonctionnalité de [partage sécurisé de données]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) de Snowflake permet à Braze de vous donner un accès sécurisé aux données sur notre portail Snowflake, sans vous soucier des frictions de workflow, des points de défaillance et des coûts inutiles liés aux relations classiques avec les fournisseurs de données. Tout le partage s'effectue via la couche de services et le magasin de métadonnées propres à Snowflake : aucune donnée n'est réellement copiée ou transférée entre les comptes. Il s'agit d'un concept important, car les données partagées n'occupent aucun espace de stockage dans un compte consommateur et ne contribuent donc pas à vos frais mensuels de stockage de données. Les seuls frais pour les consommateurs concernent les ressources de calcul (c'est-à-dire les entrepôts virtuels) utilisées pour interroger les données partagées.

### API d'exportation Braze {#braze-export-apis}
La REST API de Braze fournit des [endpoints]({{site.baseurl}}/api/endpoints/export) qui vous permettent d'exporter de manière programmatique des analyses agrégées, ainsi que des données utilisateur individuelles. Ces données peuvent être exportées pour des audiences et des Segments de toute taille.

### CSV {#csvs}
Enfin, il est possible de télécharger vos données au niveau agrégé directement depuis le tableau de bord sous forme de [CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data). L'option CSV permet facilement aux membres de votre équipe d'exporter des données depuis Braze.

{% alert tip %}
Bien que l'exportation CSV ait une limite de base de 500 000 lignes, les API n'ont aucune limite à cet égard.
{% endalert %}

## Tout assembler {#putting-it-all-together}
L'un de vos utilisateurs, appelons-le Mel, vient de recevoir votre annonce de produit. En coulisses, toutes les couches de la plateforme Braze ont travaillé ensemble pour que ce processus se déroule sans accroc.

Les informations de Mel ont été importées dans Braze depuis votre ancienne plateforme d'engagement client via un import CSV. Chaque fois que Mel a interagi avec votre application après l'intégration, de nouvelles données ont été ajoutées à son profil utilisateur.

Votre annonce de produit a été envoyée à tous les clients qui ont aimé un article similaire dans votre application. Vous avez défini cette donnée comme un événement personnalisé. Le SDK a suivi cet événement et segmenté votre base d'utilisateurs en conséquence. Braze a orchestré le meilleur moment de la journée pour envoyer cette annonce, et l'a personnalisée en appelant Mel par son prénom préféré.

Lorsque Mel ouvre l'annonce, elle ajoute votre nouveau produit à sa liste de souhaits. Braze suit automatiquement le fait qu'elle a cliqué sur l'e-mail. Le SDK enregistre qu'elle a ajouté votre nouveau produit à ses favoris. Chaque fois qu'ils interagissent avec votre marque, vous et vos utilisateurs en apprenez davantage les uns sur les autres.

![Diagramme montrant comment Braze suit les actions des utilisateurs à travers les canaux de communication.]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})