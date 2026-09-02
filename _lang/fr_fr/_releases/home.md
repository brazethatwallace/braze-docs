---
nav_title: Accueil
article_title: Quoi de neuf dans Braze ?
description: "Les notes de mise à jour de Braze sont publiées mensuellement afin que vous puissiez vous tenir au courant des versions majeures du produit, des améliorations continues du produit et des partenariats de Braze."
page_order: 0
search_rank: 1
page_type: reference
---

# Quoi de neuf dans Braze ? {#whats-new-in-braze}

{% alert tip %}
Pour plus d'informations sur l'une des mises à jour énumérées sur cette page, contactez votre gestionnaire de compte ou [ouvrez un ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support). Vous pouvez également consulter nos [journaux des modifications du SDK]({{site.baseurl}}/developer_guide/changelogs) pour plus d'informations sur les versions mensuelles du SDK, les améliorations et les changements majeurs.
{% endalert %}

{% details 20 août 2026 %}

## Publication du 20 août 2026 {#august-20-2026-release}

### Données et rapports {#data-reporting}

#### Éditeur SQL de l'ingestion de données cloud {#cloud-data-ingestion-sql-editor}

{% multi_lang_include release_type.md release="General availability" %}

L'[éditeur SQL]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor) vous permet de créer et de modifier des synchronisations d'ingestion de données cloud (CDI) en écrivant une requête SQL sur n'importe quelle table ou vue de votre entrepôt de données, plutôt que de créer et de maintenir une table dédiée spécifique à Braze. Il est disponible pour tous les types de données de synchronisation sur toutes les sources d'entrepôt de données CDI : Snowflake, Redshift, BigQuery, Databricks et Fabric.

#### Mappeur visuel de l'ingestion de données cloud {#cloud-data-ingestion-visual-mapper}

{% multi_lang_include release_type.md release="Beta" %}

Le [mappeur visuel]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/visual_mapper) vous permet de créer une synchronisation d'ingestion de données cloud (CDI) en mappant les colonnes d'une table d'entrepôt de données existante aux champs Braze directement dans le tableau de bord, sans SQL ni table dédiée. Cette version bêta prend en charge les synchronisations d'attributs utilisateur sur toutes les sources d'entrepôt de données CDI. Le mappeur visuel et l'éditeur SQL sont complémentaires : utilisez le mappeur visuel pour un mappage direct colonne-champ, et l'éditeur SQL pour les cas avancés comme les transformations, les jointures et la logique conditionnelle.

#### Ingestion de données cloud pour Google Cloud Storage et Azure Blob Storage {#cloud-data-ingestion-for-google-cloud-storage-and-azure-blob-storage}

{% multi_lang_include release_type.md release="General availability" %}

L'ingestion de données cloud (CDI) prend en charge deux nouvelles sources de stockage de fichiers : Google Cloud Storage, disponible dès maintenant, et Azure Blob Storage, disponible la semaine du 31 août 2026. Les deux sources fonctionnent comme la source Amazon S3 existante — Braze ingère les fichiers dès qu'ils sont écrits dans le compartiment ou le conteneur — de sorte que les clients sur Google Cloud ou Azure bénéficient de la même vitesse et fiabilité sans avoir à répliquer les fichiers dans S3 ou à construire une intégration personnalisée.

#### Ingestion de données cloud vers BrazeAI Decisioning Studio {#cloud-data-ingestion-to-brazeai-decisioning-studio}

{% multi_lang_include release_type.md release="Early access" %}

L'ingestion de données cloud (CDI) peut désormais synchroniser les données d'entrepôt de données directement vers BrazeAI Decisioning Studio pour les clients utilisant les deux produits, vous permettant d'intégrer des données au-delà de votre espace de travail Braze pour l'apprentissage par renforcement et la prise de décision par IA sans avoir à construire des tâches ETL personnalisées. Cette version en accès anticipé prend en charge les sources Snowflake, avec des sources d'entrepôt de données supplémentaires à venir prochainement.

### BrazeAI<sup>TM</sup>

#### Operator peut naviguer dans le tableau de bord pour vous {#operator-can-navigate-the-dashboard-for-you}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) peut naviguer vers une page différente du tableau de bord pour répondre à votre demande. Lorsqu'une invite nécessite une autre partie du tableau de bord, Operator identifie la destination, propose la navigation et vous y emmène avant de poursuivre son travail.

Cela permet à Operator d'enchaîner un travail en plusieurs étapes à partir d'une seule invite. Par exemple, si vous demandez à Operator depuis la page d'accueil de configurer les paramètres de votre éditeur glisser-déposer pour correspondre à vos directives de marque, il vous dirige vers les paramètres d'e-mail pertinents et continue à vous aider à partir de là.

Par défaut, Operator vous demande d'approuver une navigation proposée avant de vous déplacer vers une nouvelle page. Pour permettre à Operator de naviguer sans attendre votre approbation à chaque fois, activez l'[approbation automatique des actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions).

#### Operator peut agir sur davantage de pages du tableau de bord {#operator-can-act-on-more-dashboard-pages}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) peut effectuer des tâches depuis des pages supplémentaires du tableau de bord lorsque vous décrivez le résultat souhaité en langage naturel. Les exemples incluent la création de rapports et de tableaux de bord, le travail depuis les pages de liste de modèles d'e-mail et de Content Blocks, l'importation ou la gestion d'utilisateurs, la création de prédictions et la mise à jour de davantage de surfaces d'administration et de paramètres.

Par exemple, sur la page du générateur de rapports, demandez à Operator de créer un rapport montrant l'engagement SMS de l'espace de travail au cours des 30 derniers jours.

Pour une couverture représentative, consultez [Ce que vous pouvez faire avec Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Demandez à Operator sur la page où vous vous trouvez pour obtenir la réponse la plus à jour.

#### Operator peut créer et modifier des Canvas {#operator-can-create-and-edit-canvases}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) peut créer un brouillon de Canvas à partir d'une description en langage naturel, et modifier un Canvas existant de la même manière. Décrivez le parcours que vous souhaitez — critères d'entrée, délais et messages — et Operator assemble un brouillon que vous révisez et affinez avant de le lancer.

Par exemple, demandez à Operator de créer un parcours d'abandon de panier qui attend une heure après l'abandon du panier, envoie un rappel par e-mail, puis une notification push après 24 heures si l'utilisateur n'a toujours pas effectué d'achat.

Pour les étapes prises en charge et les limitations, consultez [Ce que vous pouvez faire avec Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities).

#### Mises à jour de l'étape Optimiseur de contenu {#content-optimizer-step-updates}

{% multi_lang_include release_type.md release="Beta" %}

L'étape [Optimiseur de contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer) inclut les mises à jour suivantes :

- **États de l'étape :** les étapes de l'Optimiseur de contenu indiquent si elles sont en **Apprentissage**, **Optimisation** ou **Action recommandée**, afin que vous puissiez voir où en est chaque étape.
- **Vérifications de configuration avant le lancement :** l'Optimiseur de contenu vérifie les erreurs de configuration clés pendant la rédaction, afin que vous puissiez détecter les problèmes avant le lancement.
- **Suivi de la combinaison reçue par chaque utilisateur :** une nouvelle étiquette Liquid et une visibilité sur le profil utilisateur vous permettent de suivre quelle combinaison de variantes chaque utilisateur a reçue, de bout en bout.
- **Nouvelles données Currents :** trois nouveaux types d'événements vous permettent d'extraire les données de l'Optimiseur de contenu dans votre entrepôt : `users.canvas.costep.Send`, `users.canvas.costep.Conversion` et `contentoptimizer.ComponentStore`.

Pour les détails de configuration, consultez [Étape Optimiseur de contenu]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

### Orchestration

#### Heures calmes de l'espace de travail {#workspace-quiet-hours}

{% multi_lang_include release_type.md release="Early access" %}

Les [heures calmes de l'espace de travail]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) vous permettent de définir une fenêtre d'heures calmes par défaut pour un canal de communication sur l'ensemble de votre espace de travail. Chaque Campaign et Canvas sur ce canal respecte la fenêtre dans le fuseau horaire local de chaque destinataire. Vous pouvez conserver la valeur par défaut de l'espace de travail, ou vous en exclure et appliquer une fenêtre spécifique à la Campaign ou au Canvas à la place.

Les messages qui seraient envoyés pendant la fenêtre sont retenus pour une distribution ultérieure ou annulés, selon le type de Campaign. Les heures calmes de l'espace de travail ne modifient jamais le contenu des messages.

#### Alertes de seuil Canvas {#canvas-threshold-alerts}

{% multi_lang_include release_type.md release="Early access" %}

Les [alertes de seuil Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts) vous notifient lorsque les entrées d'utilisateurs ou les messages envoyés sortent du volume attendu. Définissez un seuil, choisissez la fréquence à laquelle Braze le vérifie (toutes les 3 à 12 heures, ou toutes les 24 heures), et soyez notifié par e-mail, webhook, ou les deux lorsqu'une règle est atteinte. Vous pouvez créer plusieurs alertes pour le même Canvas, y compris sur les brouillons — l'alerte commence à vérifier après le lancement du Canvas.

#### Attribution automatique de Teams {#automatic-team-assignment}

{% multi_lang_include release_type.md release="General availability" %}

Pour les utilisateurs disposant uniquement d'autorisations au niveau de l'équipe, Braze peut attribuer automatiquement une [équipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams#automatic-team-assignment) lors de la création d'un objet.

### Canaux et points de contact {#channels-touchpoints}

#### Débogueur de contenu connecté {#connected-content-debugger}

{% multi_lang_include release_type.md release="Early access" %}

Le [débogueur de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) affiche la requête et la réponse en direct pour chaque appel de contenu connecté dans **Aperçu et test**, afin que vous puissiez vérifier votre endpoint, vos en-têtes et vos étiquettes Liquid avant de lancer une Campaign ou un Canvas. Ouvrez **Voir les détails** pour inspecter l'URL, la méthode, le code de statut, les en-têtes de requête et de réponse, le payload, la durée et si la réponse a été servie depuis le cache.

Pendant l'accès anticipé, le débogueur est disponible pour les Content Cards, les e-mails, les messages in-app, les notifications push, les SMS/MMS/RCS, les webhooks et WhatsApp.

#### Sondages dans les messages in-app et les pages de destination {#in-app-message-and-landing-page-surveys}

{% multi_lang_include release_type.md release="General availability" %}

Les sondages Braze collectent des retours dans les [messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) et les [pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) que vous pouvez analyser et utiliser dans les messages de suivi.

#### Message carrousel KakaoTalk {#kakaotalk-carousel-message}

{% multi_lang_include release_type.md release="General availability" %}

Un [message carrousel KakaoTalk]({{site.baseurl}}/user_guide/channels/kakaotalk/create_kakaotalk_message#step-2-compose-your-kakaotalk-message) comprend jusqu'à six cartes défilables. Chaque carte possède une image, un en-tête, un message, une URL de site web optionnelle et au moins un bouton.

#### Améliorations du générateur de modèles WhatsApp {#whatsapp-template-builder-improvements}

{% multi_lang_include release_type.md release="General availability" %}

Le [générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder) prend en charge davantage de chemins de création et d'options de modèles :

- **Créer des modèles lors de la création de Campaigns et de Canvas :** créez un nouveau modèle WhatsApp directement dans le compositeur au lieu de sélectionner uniquement des modèles existants depuis le contenu.
- **Messages de réponse en carrousel :** créez des mises en page en carrousel comme messages de réponse, et pas seulement comme modèles sortants.
- **Nouveaux types de modèles : Utilitaire et Flux :** le générateur de modèles prend en charge les modèles Utilitaire et les modèles Flux, y compris lorsque vous créez des modèles depuis des Campaigns, des Canvas ou l'expérience autonome de modèles de contenu.

#### Blocs de formulaire personnalisés et pont JavaScript pour les pages de destination {#custom-form-blocks-and-javascript-bridge-for-landing-pages}

{% multi_lang_include release_type.md release="General availability" %}

Les pages de destination prennent désormais en charge les [blocs de formulaire personnalisés]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) et un [pont JavaScript]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge), vous permettant de capturer des entrées de formulaire personnalisées et de synchroniser les événements et attributs côté client via votre expérience de page de destination.

#### Formulaires de page de destination en plusieurs étapes {#multi-step-landing-page-forms}

{% multi_lang_include release_type.md release="General availability" %}

Les [formulaires de page de destination en plusieurs étapes]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) vous permettent de diviser un long formulaire en plusieurs étapes dans une seule ligne **Formulaire**, avec une étape de confirmation intégrée après la soumission.

#### Bloc Gérer les abonnements pour les pages de destination {#manage-subscriptions-block-for-landing-pages}

{% multi_lang_include release_type.md release="General availability" %}

Le bloc [Gérer les abonnements]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions) permet aux utilisateurs de consulter, de s'abonner et de mettre à jour les groupes d'abonnement e-mail sur une page de destination.

### Partenariats {#partnerships}

#### Audience Sync : Google Data gestionnaire API

{% multi_lang_include release_type.md release="Early access" %}

[Audience Sync vers Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) prend en charge l'API Google Data gestionnaire en accès anticipé.

#### Amazon Bedrock - Fournisseur de modèles IA {#amazon-bedrock-ai-model-provider}

[Amazon Bedrock](https://aws.amazon.com/bedrock/) est un service AWS entièrement géré qui fournit un accès aux modèles de fondation des principales entreprises d'intelligence artificielle via une API unifiée, permettant aux marques de créer et de faire évoluer des applications d'intelligence artificielle générative sur AWS.

Pour plus d'informations, consultez [Amazon Bedrock]({{site.baseurl}}/partners/amazon_bedrock).

#### Bynder - Orchestration des messages - CMS et DAM {#bynder-message-orchestration-cms-and-dam}

[Bynder](https://www.bynder.com) est une plateforme de gestion des ressources numériques (DAM) qui aide les clients à créer, gérer, trouver et distribuer des ressources numériques approuvées (images, vidéos et autres créations) à partir d'une source unique de vérité. Lorsqu'elle est intégrée à Braze, l'extension Google Chrome Universal Compact View (UCV) de Bynder permet aux marketeurs de rechercher et de sélectionner des ressources Bynder sans quitter le tableau de bord de Braze. Insérez des liens vers ces ressources directement dans les Campaigns et les Canvas.

Pour plus d'informations, consultez [Bynder]({{site.baseurl}}/partners/bynder).

#### Multiplied Media - Personnalisation des messages - Contenu visuel et interactif {#multiplied-media-message-personalization-visual-and-interactive-content}

[Multiplied Media](https://multiplied.media) est un studio de création et d'automatisation qui utilise vos données CRM pour créer des images, des GIF et des vidéos personnalisés — une ressource unique pour chaque client. L'intégration de Multiplied Media et Braze vous permet d'envoyer ces médias par e-mail, notifications push, messages in-app, Content Cards et WhatsApp.

Pour plus d'informations, consultez [Multiplied Media]({{site.baseurl}}/partners/multiplied_media).

### SDK

Les mises à jour SDK suivantes ont été publiées. Pour plus de détails, consultez les [journaux des modifications du SDK]({{site.baseurl}}/developer_guide/changelogs).

#### Mises à jour majeures du SDK {#sdk-breaking-updates}

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

- Unity SDK 12.0.0
    - Mise à jour du pont iOS natif [de Braze Swift SDK 14.1.0 à 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/14.1.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Mise à jour du pont Android natif [de Braze Android SDK 42.2.0 à 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.2.0...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Flutter SDK 22.0.0
    - Mise à jour du pont Android natif [de Braze Android SDK 42.3.1 à 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.3.1...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Mise à jour du pont iOS natif [de Braze Swift SDK 17.0.0 à 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/17.0.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Swift SDK 18.0.0-18.1.0
    - Renomme `Braze.Ecommerce.ProductViewedEvent.typeIdentifiers` en `type` sur les surfaces API Swift et Objective-C.
    Renomme les événements de mise à jour push-to-start des en direct Activities sur `Braze.LiveActivities.UpdateEvent.ActivityType`, qui sont émis lors de l'utilisation de `Braze.LiveActivities.subscribeToStateUpdates(_:)` :
        - `pushToStartOptedOut` en `pushToStartUnregistered`
        - `pushToStartOptOutFlushed` en `pushToStartUnregisterFlushed`

#### Résumé des fonctionnalités et correctifs récents du SDK {#summary-of-recent-sdk-features-and-fixes}

- **Swift SDK v18.1.0 :** ajoute des méthodes de déconnexion de jeton push, en plus de la méthode de déconnexion push existante, pour prendre en charge des cas d'usage de déconnexion supplémentaires. Met également à jour le type d'événement eCommerce.
- **Flutter SDK v22.0.0 :** met à jour le pont natif pour hériter des fonctionnalités des SDK Android et Swift.
- **Unity SDK v12.0.0 :** met à jour le pont natif pour hériter des fonctionnalités des SDK Android et Swift.

Pour plus de détails, consultez les [journaux des modifications du SDK]({{site.baseurl}}/developer_guide/changelogs).
{% enddetails %}
{% details 23 juillet 2026 %}

## Publication du 23 juillet 2026 {#july-23-2026-release}

### Données et rapports

#### Tableau de bord de diagnostic des messages {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="General availability" %}

Le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) fournit une ventilation de haut niveau des résultats d'envoi de messages, vous permettant de repérer les tendances et de diagnostiquer les problèmes potentiels dans votre configuration de messagerie. Ce tableau de bord peut vous aider à comprendre pourquoi les messages de vos Campaigns ou Canvas n'ont peut-être pas été envoyés comme prévu. Contactez votre gestionnaire du succès des clients pour accéder à cette fonctionnalité.

#### Mappeur CSV d'événements personnalisés {#csv-custom-events-mapper}

{% multi_lang_include release_type.md release="General availability" %}

Le [flux d'importation CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#about-csv-import) pour les événements personnalisés inclut désormais un mappeur qui vous permet de mapper les noms d'événements et les en-têtes de propriétés d'événements aux champs Braze avant l'importation. Cette mise à jour aligne l'expérience des événements personnalisés sur le flux des attributs personnalisés et réduit le besoin de reformater les fichiers avant le téléchargement. Le flux comprend le téléchargement d'un CSV, le mappage des champs et événements requis, le mappage des propriétés d'événements, puis la sélection des préférences de ciblage avant l'importation. Si votre fichier correspond déjà au format attendu, vous pouvez poursuivre le flux sans effectuer de modifications de mappage.

#### Le stockage gratuit des catalogues prend désormais en charge jusqu'à 500 Mo {#catalogs-free-storage-now-supports-up-to-500-mb}

{% multi_lang_include release_type.md release="General availability" %}

La version gratuite des [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers) prend désormais en charge jusqu'à 500 Mo de stockage pour l'ensemble des fichiers CSV.

### BrazeAI<sup>TM</sup>

#### Operator peut désormais mettre à jour les pages de paramètres pour vous {#operator-can-now-update-settings-pages-for-you}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) peut désormais effectuer des modifications directement sur davantage de pages de paramètres, vous permettant de décrire un changement en langage naturel au lieu de naviguer dans les écrans de configuration. Les pages prises en charge incluent :

- Heures calmes
- Paramètres push
- Limites de débit de messagerie
- Règles de messagerie et flux d'approbation permanents
- Autres identifiants et limites d'API
- Coordonnées

Par exemple, sur la page Heures calmes, demandez à Operator de définir les heures calmes de 21 h à 8 h pour les SMS.

#### Serveur MCP Braze distant {#remote-braze-mcp-server}

{% multi_lang_include release_type.md release="Early access" %}

Le [serveur MCP Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) est une connexion hébergée à distance qui vous permet de connecter des agents d'intelligence artificielle tels que Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity et Claude Code directement à Braze. En langage naturel, les agents peuvent lire les analyses de Campaigns, Canvas et Segments, les attributs personnalisés, les événements, les KPI et les catalogues, et créer ou mettre à jour des modèles d'e-mail, des Content Blocks et des ressources de la bibliothèque multimédia. Aucune donnée personnelle de profil utilisateur n'est exposée.

Pour vous connecter, collez une seule URL d'endpoint dans votre client MCP — `https://mcp.braze.com/mcp` pour les États-Unis ou `https://mcp.braze.eu/mcp` pour l'UE — puis connectez-vous avec OAuth, y compris le authentification unique. Le serveur se lance avec les outils disponibles.

### Orchestration

#### Portée d'audience Teams {#teams-audience-scoping}

{% multi_lang_include release_type.md release="General availability" %}

La configuration d'audience de [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) prend désormais en charge plusieurs filtres.

### Canaux et points de contact

#### Échelle de notation pour les sondages dans les messages in-app et les pages de destination {#survey-rating-scale-for-in-app-messages-and-landing-pages}

{% multi_lang_include release_type.md release="Early access" %}

Ajoutez une échelle de notation numérique à un bloc de formulaire dans les [sondages de pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) et les [sondages de messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) pour capturer le sentiment, la satisfaction et la probabilité de recommandation sans code personnalisé. Trois plages sont prises en charge : 1–10, 1–5 et 0–10 (la plage NPS standard).

#### Modèles d'offres à durée limitée WhatsApp {#whatsapp-limited-time-offer-templates}

{% multi_lang_include release_type.md release="General availability" %}

Les [modèles d'offres à durée limitée WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates) affichent une offre promotionnelle limitée dans le temps avec un compte à rebours optionnel à l'approche de l'expiration. Utilisez cette mise en page pour les promotions à durée limitée, telles que les ventes saisonnières ou les offres personnalisées en fonction d'un attribut utilisateur.

#### Mise à niveau en libre-service de la version SDK Shopify {#shopify-self-serve-sdk-version-upgrade}

{% multi_lang_include release_type.md release="General availability" %}

Les nouveaux clients [Shopify]({{site.baseurl}}/partners/ecommerce/shopify) sont provisionnés avec les dernières versions du SDK Web Braze et du SDK JavaScript lors de la configuration. Les clients existants peuvent consulter leur version actuelle du SDK dans les paramètres d'intégration, être notifiés lorsqu'une version plus récente est disponible et effectuer les mises à niveau en libre-service depuis les paramètres d'intégration.

#### Éditeur HTML pour les bannières {#html-editor-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Lorsque vous composez une bannière, vous pouvez désormais la créer [à l'aide de l'éditeur HTML]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner). L'éditeur HTML est idéal pour les équipes qui maintiennent déjà leurs propres modèles HTML ou qui souhaitent un contrôle total sur le balisage et le style des bannières. Vous pouvez écrire ou coller du HTML personnalisé directement dans l'éditeur.

#### Remplacer un fichier dans la bibliothèque multimédia {#replace-a-file-in-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez désormais [remplacer le fichier d'une ressource existante de la bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file) tout en conservant son URL et son ID de ressource stables. Comme l'URL ne change pas, toute Campaign, Canvas, Content Block ou modèle qui référence cette ressource reflète automatiquement le fichier mis à jour, vous n'avez donc pas besoin de le re-télécharger ou de le re-lier manuellement partout où il est utilisé.

#### Vue en grille pour la bibliothèque multimédia {#grid-view-for-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

La bibliothèque multimédia et certaines bibliothèques de modèles offrent désormais une vue en grille en plus de la vue en liste existante. La vue en grille affiche les ressources sous forme de vignettes avec des métadonnées clés (nom, type, dernière modification), ce qui permet de trouver plus rapidement les images et les créations visuellement plutôt que par nom de fichier. Le filtrage et la recherche fonctionnent de la même manière dans les deux vues.

#### Prise en charge de l'aperçu partageable pour davantage de canaux {#shareable-preview-support-for-more-channels}

{% multi_lang_include release_type.md release="General availability" %}

L'[aperçu partageable]({{site.baseurl}}/user_guide/channels/email/html_editor#step-3b-preview-and-test-your-message) prend désormais en charge les canaux supplémentaires suivants :

- SMS, MMS et RCS
- WhatsApp
- Push
- Content Cards
- LINE

Depuis une Campaign ou un message, générez un lien et partagez-le avec des réviseurs qui n'ont pas accès au tableau de bord de Braze — marque, juridique ou une agence externe, par exemple. Les destinataires ouvrent le lien dans n'importe quel navigateur pour voir le message rendu comme un client le verrait, y compris toute personnalisation de test.

#### API de mise à jour des identifiants push {#push-credentials-update-api}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez désormais mettre à jour les identifiants push de manière programmatique avec l'[endpoint de mise à jour des identifiants push]({{site.baseurl}}/api/endpoints/apps/post_update_push_credential). Chaque requête met à jour une application et une plateforme (`apple`, `firebase`, `huawei` ou `kindle`) et accepte les payloads d'identifiants sous forme de valeurs encodées en Base64. Cela aide les équipes à gérer de grands portefeuilles d'applications et les politiques de rotation des identifiants sans dépendre de téléchargements manuels dans le tableau de bord.

### Partenariats

#### Refiner - Sondages {#refiner-surveys}

[Refiner](https://refiner.io) est une plateforme de sondages in-app pour les applications SaaS et mobiles. Elle permet aux équipes produit et voix du client de lancer des sondages in-app ciblés et de collecter en continu des données NPS, CSAT, CES, des retours produit et des données zero-party.

#### Stayfilm - Contenu visuel et interactif {#stayfilm-visual-and-interactive-content}

[Stayfilm](https://www.stayfilm.com/) est une API REST pour la production vidéo automatisée et personnalisée à grande échelle. La plateforme intègre des données, des images, du texte, des bandes sonores, de la narration et des effets visuels pour générer du contenu vidéo personnalisé pour le commerce électronique, les places de marché, les flux de travail CRM et les campagnes marketing.

#### Validity - Données et analyse {#validity-data-and-analytics}

[Validity Everest](https://www.validity.com/everest/) est une plateforme de livrabilité des e-mails qui vous aide à mesurer le placement en boîte de réception et à protéger votre réputation d'envoi. L'intégration de Braze et Validity synchronise votre liste de seeds Everest avec Braze, ensemence automatiquement les Campaigns et Canvas éligibles, et récupère les indicateurs d'engagement dans Validity Inbox afin que vous puissiez comparer le placement basé sur les seeds avec l'engagement réel des abonnés.

### SDK

Les mises à jour SDK suivantes ont été publiées. Pour plus de détails, consultez les [journaux des modifications du SDK]({{site.baseurl}}/developer_guide/changelogs).

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

- [SDK Android 43.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v43.0.0)
    - Ajoute les méthodes `unregisterPush` et logout.
    - Ajoute des champs supplémentaires aux événements eCommerce.
    - Ajoute des délais exponentiels pour le chargement des images de notifications push.
- [SDK Swift 17.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Ajoute des champs supplémentaires aux événements eCommerce.
    - Rend les états de données prévisibles après l'initialisation.
    - Ajoute des accesseurs non bloquants pour les identifiants d'appareil et d'utilisateur.
    - Supprime l'API de mise à jour push-to-start obsolète sur `Braze.LiveActivities`.
- [SDK Web 6.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Ajoute les méthodes `unregisterPush` et logout.
    - Ajoute des champs supplémentaires aux événements eCommerce.
    - Corrige un problème de bannière et de Content Card lié aux actualisations redondantes au démarrage.
    - Ajoute une méthode publique pour la fermeture des bannières.
- [SDK Flutter 21.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/v21.0.0)
    - Met à jour le pont iOS natif.
    - Supprime les méthodes obsolètes.
    - Met à jour les gestionnaires `changeUser`, `enableSDK` et `disableSDK` pour renvoyer les résultats de complétion.
- [SDK Expo 5.2.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/v5.2.0)
    - Met à jour l'application exemple vers Expo SDK 56.
- [SDK React Native 22.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/22.0.0)
    - Ajoute la prise en charge de la fermeture des bannières.
    - Inclut des mises à jour de liaisons.

{% enddetails %}
{% details 25 juin 2026 %}

## Publication du 25 juin 2026 {#june-25-2026-release}

### Données et rapports

#### Mise à jour du nom de l'indicateur pour les Content Cards et les bannières {#metric-name-update-for-content-cards-and-banners}

L'indicateur _Destinataires uniques_ a été renommé en _Impressions quotidiennes uniques_ pour les Content Cards et les bannières. Les _impressions quotidiennes uniques_ font référence au nombre reçu de Braze et sont basées sur le `user_id`. Les impressions quotidiennes uniques sont comptabilisées au niveau de la Campaign ou de l'étape Canvas. Pour plus de détails, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

#### Suppression d'utilisateurs {#user-deletion}

{% multi_lang_include release_type.md release="General availability" %}

La [suppression d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) vous permet de gérer votre base de données en supprimant les profils qui ne sont plus nécessaires, créés par erreur ou devant être supprimés pour des raisons de conformité (comme le RGPD ou le CCPA).

#### Exclusions de points de données {#data-point-exclusions}

{% multi_lang_include release_type.md release="General availability" %}

Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) ne sont plus comptabilisés dans les points de données facturables. Vous pouvez adopter les événements eCommerce Braze (`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`) sans consommation de points de données.

#### Onglet Historique des événements {#event-history-tab}

{% multi_lang_include release_type.md release="General availability" %}

L'onglet **Historique des événements** sur les [profils utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) répertorie les événements personnalisés et les achats de l'utilisateur au cours des 30 derniers jours (jusqu'aux 100 plus récents). Utilisez-le pour confirmer qu'une intégration SDK ou API envoie les événements comme prévu, déboguer pourquoi un utilisateur est (ou n'est pas) entré dans une Campaign ou un Canvas déclenché par un événement, ou enquêter sur une escalade de support concernant un utilisateur spécifique.

#### Le Centre de livrabilité affiche les données Microsoft SNDS pour les clients Amazon SES {#deliverability-center-surfaces-microsoft-snds-data-for-amazon-ses-customers}

Pour les espaces de travail qui envoient des e-mails via Amazon SES, le [Centre de livrabilité]({{site.baseurl}}/deliverability_center) affiche les indicateurs Microsoft SNDS pour vos adresses IP d'envoi dédiées. Braze rétroalimente jusqu'à 90 jours de données SNDS historiques lorsque cette fonctionnalité est activée pour votre espace de travail.

### BrazeAI<sup>TM</sup>

#### Assistants BrazeAI unifiés dans Operator {#unified-brazeai-assistants-in-operator}

Les assistants BrazeAI autonomes présents dans le tableau de bord sont unifiés dans [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator), faisant d'Operator l'assistant IA unique pour l'assistance en intelligence artificielle générative destinée aux marketeurs dans l'ensemble du tableau de bord. Les assistants suivants passent désormais par Operator :

{% multi_lang_include releases/brazeai_operator_legacy_assistants.md %}

Les points d'entrée existants restent là où se trouvait chaque bouton d'assistant précédent. Au lieu d'ouvrir un assistant autonome, ces points d'entrée ouvrent désormais le panneau Operator avec des invites dynamiques pré-adaptées à votre tâche. Ces points d'entrée fournissent un accès direct à Operator afin que vous puissiez utiliser ces capacités sans modifier vos flux de travail existants.

#### Prise en charge d'Operator pour la création et la modification de Campaigns {#operator-support-for-campaign-creation-and-editing}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator) peut désormais créer et modifier des Campaigns entières, et pas seulement composer des messages. À partir d'une seule invite en langage naturel ou d'un brief de Campaign, Operator construit une Campaign prête à être examinée de bout en bout — composant le message, planifiant la distribution, ciblant une audience et assignant des événements de conversion — puis récapitule ce qu'il a construit lors de l'étape de révision. Auparavant, Operator pouvait composer le message (l'une des cinq étapes de création de Campaign) ; il a désormais une visibilité et un contrôle sur les étapes restantes de planification, de ciblage, d'assignation et de révision.

Cette fonctionnalité est disponible depuis la page **Campaigns** ou depuis n'importe quelle Campaign existante. En conséquence, Operator peut :

{% multi_lang_include releases/brazeai_operator_campaign_creation_prompts.md %}

#### Prise en charge d'Operator pour les Content Blocks {#operator-support-for-content-blocks}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator) peut désormais créer et modifier des [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) — les extraits réutilisables que vous créez une fois et référencez dans plusieurs messages — directement à partir d'une invite en langage naturel. Depuis la page **Content Blocks**, demandez à Operator de créer un nouveau Content Block à partir de zéro ou de modifier un existant, et Operator génère ou met à jour le contenu pour que vous puissiez le réviser.

#### Modèles de la Console des agents créés avec Operator {#agent-console-templates-built-with-operator}

Lors de la création d'un agent dans la **Console des agents**, vous pouvez choisir de créer un agent personnalisé ou de sélectionner une option dans **Créer un agent avec Operator** pour utiliser BrazeAI Operator afin d'appliquer un modèle de départ. Operator peut pré-configurer les instructions, les champs de sortie et le contexte pour les modèles de départ suivants de la Console des agents.

Pour plus de détails, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

#### Améliorations de la Console des agents {#agent-console-enhancements}

Vous pouvez effectuer les actions suivantes dans la [Console des agents]({{site.baseurl}}/user_guide/brazeai/agents) :

{% multi_lang_include releases/brazeai_agent_console_enhancements.md %}

#### Modifier une étape Optimiseur de contenu lancée {#edit-a-launched-content-optimizer-step}

{% multi_lang_include release_type.md release="Beta" %}

Après le lancement de votre Canvas, vous pouvez désormais [mettre à jour une étape Optimiseur de contenu]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step) pour :

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

### Canaux et points de contact

#### Fermeture par l'utilisateur pour les bannières {#user-dismissals-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez permettre aux utilisateurs de fermer manuellement une bannière en sélectionnant **La bannière peut être fermée** lors de la configuration du comportement de fermeture. Cette option est utile dans les scénarios où vous souhaitez promouvoir une vente à durée limitée pour tous les utilisateurs de l'application, tout en leur permettant de fermer le message s'ils ne sont pas intéressés.

Consultez [Configurer le comportement de fermeture]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) pour plus de détails sur l'activation de la fermeture et la personnalisation du bouton de fermeture.

#### Suivi des clics personnalisé pour les bannières {#custom-click-tracking-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Pour un suivi des clics plus granulaire pour les bannières, vous pouvez [attribuer un identifiant personnalisé]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) à chaque élément interactif en utilisant le champ **Identifiant pour les rapports** dans son panneau de propriétés.

#### Rééligibilité pour les bannières {#re-eligibility-for-banners}

Lorsque la rééligibilité est activée pour les Campaigns de bannières, les utilisateurs qui ferment une bannière peuvent redevenir éligibles après une fenêtre de temporisation configurable qui commence à la fermeture. Si la rééligibilité n'est pas activée, les utilisateurs ayant fermé la bannière restent inéligibles. Pour configurer la rééligibilité, consultez [Configurer la rééligibilité]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Notez que les étapes de bannière Canvas utilisent les paramètres de réentrée Canvas à la place.

#### Test A/B Quick Push {#quick-push-ab-testing}

{% multi_lang_include release_type.md release="General availability" %}

Le test A/B Quick Push prend désormais en charge les Campaigns push multiplateformes et les étapes Canvas via des groupes de variantes, vous permettant de tester des variations de messages iOS et Android alignées dans un seul flux de travail. Pour plus d'informations, consultez [Messages push multiplateformes]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push#use-cases).

#### Optimiser avec BrazeAI<sup>TM</sup> {#optimize-with-brazeai}

{% multi_lang_include release_type.md release="Early access" %}

**Optimiser avec BrazeAI<sup>TM</sup>** s'active automatiquement lorsque vous ajoutez plusieurs variantes push, applique les paramètres d'expérience recommandés par défaut et optimise vers la variante la plus performante. Vous pouvez le désactiver si vous devez envoyer immédiatement. Pour plus d'informations, consultez [Optimiser les tests A/B avec BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

#### Résultats d'envoi test WhatsApp {#whatsapp-test-send-results}

Après l'envoi d'un message WhatsApp de test, vous pouvez consulter un [rapport de distribution détaillé]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-4-view-test-send-results) directement dans le compositeur de messages. Cela vous aide à confirmer que votre message a atteint le destinataire prévu et à résoudre les échecs avant le lancement.

### Partenariats

#### Convercus - Données et analyse - Fidélisation {#convercus-data-and-analytics-loyalty}

[Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus) est une plateforme SaaS de fidélisation et de coupons qui aide les marques et les détaillants à augmenter la fréquence d'achat, la valeur du panier et les taux de rachat grâce à des programmes de fidélisation omnicanaux et des campagnes de coupons personnalisées.

#### Copy Pastd - Orchestration des messages - Modèles {#copy-pastd-message-orchestration-templates}

[Copy Pastd]({{site.baseurl}}/partners/copy_pastd) Building Blocks est un générateur d'e-mails par glisser-déposer qui pousse des Content Blocks alimentés par Liquid et des modèles complets directement dans votre espace de travail Braze. Concevez une fois, synchronisez avec Braze et réutilisez les mêmes composants dans les Campaigns, les Canvas et les flux déclenchés sans reconstruire le HTML à chaque fois.

#### Databricks Mosaic - Fournisseurs de modèles IA {#databricks-mosaic-ai-model-providers}

[Databricks Mosaic]({{site.baseurl}}/partners/ai_model_providers/databricks_mosaic) est la plateforme unifiée de Databricks pour créer, déployer et gérer des modèles d'intelligence artificielle et de machine learning à grande échelle sur la plateforme Databricks Data Intelligence.

#### DinMo - Données et analyse - Reverse ETL {#dinmo-data-and-analytics-reverse-etl}

[DinMo]({{site.baseurl}}/partners/dinmo) est une plateforme de données client (CDP) composable qui connecte votre entrepôt de données cloud à Braze via un processus ETL inversé (ETL). Les équipes marketing peuvent créer des segments d'audience à partir des données de l'entrepôt, synchroniser les attributs et événements utilisateur dans Braze et maintenir les statuts d'abonnement à jour sans téléchargements CSV ni support d'ingénierie.

#### EmailShepherd - Orchestration des messages - Modèles {#emailshepherd-message-orchestration-templates}

[EmailShepherd]({{site.baseurl}}/partners/emailshepherd) est une plateforme de création d'e-mails agentique construite sur votre système de design d'e-mails qui permet à toute votre équipe marketing — et aux agents d'intelligence artificielle — de produire des e-mails conformes à la marque et prêts pour la production sans goulots d'étranglement. L'intégration Braze publie les e-mails approuvés directement dans votre espace de travail Braze, afin que les marketeurs puissent faire évoluer la production d'e-mails dans Braze sans sacrifier la cohérence de la marque.

#### Talkable - Personnalisation des messages - Recommandations {#talkable-message-personalization-referrals}

[Talkable]({{site.baseurl}}/partners/talkable) aide les marques grand public à transformer les clients satisfaits en un canal de recommandation évolutif. Grâce à l'intégration Braze, les opt-ins d'e-mails marketing capturés dans les campagnes de recommandation Talkable sont transmis à Braze en temps réel, fournissant à votre équipe le consentement, le contexte et les données de campagne nécessaires pour accueillir, segmenter et engager chaque nouvel ambassadeur et ami.

### SDK

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_6_25_26_updates.md %}

{% enddetails %}

{% details 28 mai 2026 %}

## Publication du 28 mai 2026 {#may-28-2026-release}

### Données et rapports

#### Tableau de bord des performances push {#push-performance-dashboard}

Le [tableau de bord des performances push]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) vous offre une vue unique au niveau du canal de l'engagement push, incluant les envois, les rebonds, les distributions et les taux d'ouverture directs, influencés et totaux sur une fenêtre temporelle configurable. Utilisez-le pour comprendre la santé globale de votre canal push sans avoir à agréger les données de Campaigns ou de Canvas individuels.

#### Champs de géolocalisation dans les sélections de catalogue {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

Les catalogues prennent désormais en charge le filtrage basé sur la distance grâce au nouveau type de champ de géolocalisation et aux opérateurs de sélection de catalogue. Cela vous aide à créer des expériences plus pertinentes et sensibles à la localisation, comme montrer à chaque utilisateur le restaurant le plus proche, filtrer les propriétés disponibles dans un rayon de 50 km pour une campagne immobilière, ou cibler les magasins proches d'un événement spécifique. Au lieu d'approximer le ciblage géographique avec des codes de ville ou de région, vous pouvez filtrer les éléments du catalogue par proximité à un point central, y compris un attribut utilisateur Liquid tel que la localisation la plus récente d'un utilisateur. Pour plus d'informations, consultez [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

#### Banner et RCS pour le générateur de rapports {#banner-and-rcs-for-report-builder}

Le [générateur de rapports]({{site.baseurl}}/report_builder) prend en charge Banner comme canal et RCS comme sous-catégorie sous SMS, vous permettant de mesurer les performances des deux directement dans vos rapports personnalisés aux côtés de tous les autres canaux Braze.

#### Actions de l'événement `ecommerce.cart_updated` {#ecommercecart_updated-event-actions}

L'[événement `ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples) prend en charge les actions `add` et `remove` en plus de `replace`, vous permettant d'envoyer des modifications incrémentales du panier au lieu d'un instantané complet du panier à chaque mise à jour.

### BrazeAI<sup>TM</sup>

#### Optimiseur de contenu pour les messages SMS, MMS et RCS {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

Vous pouvez utiliser l'[Optimiseur de contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer) pour optimiser les accroches, les corps de message et les CTA pour les messages SMS, MMS et RCS. L'Optimiseur de contenu vous aide à tester et optimiser le contenu des messages à grande échelle, en utilisant l'intelligence artificielle pour générer et évaluer automatiquement de grands volumes de variantes de contenu.

### Orchestration

#### Fuseaux horaires de l'espace de travail {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

Utilisez les [fuseaux horaires de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone) pour définir des fuseaux horaires spécifiques pour chaque espace de travail. Cela permet aux Campaigns et Canvas planifiés (qui n'utilisent pas l'heure locale ou le timing intelligent) d'être envoyés selon le fuseau horaire désigné de l'espace de travail, plutôt que le fuseau horaire global de l'entreprise.

Les fuseaux horaires de l'espace de travail pour l'envoi de messages sont déployés progressivement, il est donc possible que vous ne voyiez pas encore ces paramètres dans votre tableau de bord.

### Canaux et points de contact

#### WhatsApp `inbound_profile_name`

Vous pouvez capturer automatiquement le nom d'affichage WhatsApp d'un utilisateur à partir du webhook de messagerie entrante de Meta et l'écrire dans le profil Braze de l'utilisateur. Lorsqu'un message WhatsApp entrant est reçu, Braze expose le nom du profil en tant que nouvel attribut Liquid WhatsApp, [{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), que vous pouvez référencer dans une étape de mise à jour utilisateur Canvas pour l'enregistrer dans un champ de profil.

#### États d'abonnement SMS orphelins {#orphaned-sms-subscription-states}

Braze [gère automatiquement les enregistrements d'état d'abonnement orphelins]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#how-braze-handles-orphaned-subscription-states) (données d'abonnement stockées pour un numéro de téléphone ou une adresse e-mail non liés à un profil utilisateur) pour empêcher l'héritage involontaire d'état d'abonnement. Cela protège les utilisateurs des scénarios où un profil utilisateur nouvellement créé hérite incorrectement de l'état d'abonnement d'un utilisateur précédemment supprimé ou sans rapport.

### Partenariats

#### Chord - Plateforme de données client {#chord-customer-data-platform}

[Chord](https://www.chord.co/) fournit une plateforme de données client qui capture et standardise les événements de votre vitrine eCommerce. Lorsque vous connectez Chord à Braze, les activités d'achat, les événements comportementaux et les mises à jour d'identité sont transmis à Braze afin que vous puissiez déclencher des Campaigns et maintenir les profils à jour sans avoir à construire ces pipelines vous-même.

Pour plus d'informations, consultez [Chord]({{site.baseurl}}/partners/chord).

#### Better Email - Modèles {#better-email-templates}

[Better Email](https://www.betteremail.dev) est une plateforme collaborative de création d'e-mails construite autour d'un système de design d'e-mails. Les équipes peuvent concevoir, gérer et exporter des e-mails prêts pour la production à partir d'un système partagé de blocs et de styles, garantissant la cohérence de la marque à grande échelle sans dépendre de développeurs ou d'agences.

Pour plus d'informations, consultez [Better Email]({{site.baseurl}}/partners/better_email).

#### DailyPlay - Contenu dynamique {#dailyplay-dynamic-content}

[DailyPlay](https://dailyplay.ai/) est une plateforme de gamification. Utilisez-la pour lancer des jeux personnalisés et de marque ainsi que des systèmes de récompenses intégrés qui approfondissent l'engagement et améliorent la rétention.

Pour plus d'informations, consultez [DailyPlay]({{site.baseurl}}/partners/dailyplay).

### SDK

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_5_28_26_updates.md %}

{% enddetails %}
{% details 30 avril 2026 %}

## Publication du 30 avril 2026 {#april-30-2026-release}

### Données et rapports

#### Ajout rapide d'utilisateur pour la création de profils individuels {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez désormais créer un profil utilisateur individuel depuis **Importer des utilisateurs** en sélectionnant **Ajout rapide d'utilisateur** et en saisissant un e-mail ou un ID externe.

Auparavant, la création d'utilisateurs à partir de ce flux de travail nécessitait un téléchargement CSV ou une méthode d'ingestion automatisée.

Pour plus d'informations, consultez [Importation CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

#### Synchronisations CDI sans copie pour les déclencheurs Canvas {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

CDI prend désormais en charge le type de données `Canvas triggers` pour la personnalisation sans copie. Vous pouvez déclencher des Canvas à partir de données d'entrepôt ou S3 et transmettre des champs de contexte sans conserver ces champs dans les profils utilisateur de Braze.

Auparavant, les synchronisations CDI nécessitaient que les données soient écrites dans les profils Braze pour ce type de flux de personnalisation.

Pour plus d'informations, consultez [Personnalisation sans copie avec CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync).

#### Événements recommandés pour le commerce électronique {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/events/recommended_events) couvrent six étapes du parcours d'achat : `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` et `order_refunded`. Lorsque vous envoyez ces événements avec succès, Braze valide les données et les rend disponibles pour un ensemble croissant de fonctionnalités de la plateforme.

### Currents et Datashare {#currents-and-datashare}

#### Nouvelles mises à jour Currents pour les canaux Banner et WhatsApp {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

Currents et Datashare incluent désormais un nouvel événement `Banner.Dismiss` et des champs supplémentaires pour les événements WhatsApp existants.

Auparavant, ces événements de fermeture de bannière et ces champs WhatsApp n'étaient pas disponibles dans les données d'export.

Pour plus d'informations, consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

### Orchestration

#### Traductions multilingues {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

Composez des [messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) avec une configuration de locale rapide et ponctuelle qui ne nécessite pas de code complexe et vous permet d'envoyer à tous vos marchés en toute confiance.

#### Migration des autorisations granulaires {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

Gérer qui peut accéder à votre compte et effectuer des actions spécifiques est essentiel pour la sécurité et l'efficacité opérationnelle. Pour vous donner plus de contrôle, Braze introduit les [autorisations granulaires]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), un moyen plus flexible et précis de gérer l'accès des utilisateurs à votre compte.

#### Composant Canvas Envoyer vers une destination {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

L'[étape Envoyer vers une destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) vous permet d'envoyer des utilisateurs d'un Canvas à un autre. Par exemple, si vous avez deux Canvas qui partagent des messages pour des offres promotionnelles, vous pouvez utiliser Envoyer vers une destination pour connecter ces Canvas.

#### Améliorations de Canvas Context {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

Dans Canvas, vous pouvez désormais référencer des variables de contexte pour définir :

- Un événement de suppression pour les Content Cards
- L'expiration des Content Cards

Pour plus de détails, consultez [Création de cartes]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas).

#### Comportement d'avancement de la validation de distribution pour les étapes Message {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

Les [validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) fournissent une vérification supplémentaire pour confirmer que votre audience répond aux critères de distribution au moment de l'envoi du message. Si un utilisateur ne répond pas aux validations de distribution définies pour une étape Message, vous pouvez utiliser le paramètre **Comportement d'avancement des validations de distribution** pour déterminer si l'utilisateur doit avancer à l'étape suivante ou quitter le Canvas.

#### Limites de débit de messagerie de l'espace de travail {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

Utilisez les [limites de débit de messagerie de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) pour réguler le débit de distribution de vos messages sortants depuis votre plateforme afin de vous assurer que vos utilisateurs reçoivent les messages dont ils ont besoin. Les limites de débit de messagerie de l'espace de travail sont déployées progressivement, il est donc possible que vous ne voyiez pas encore ces paramètres dans votre tableau de bord.

### Canaux et points de contact

#### Générateur de modèles WhatsApp {#whatsapp-template-builder}

{% multi_lang_include release_type.md release="Early access" %}

Le [générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization) vous permet de créer et de soumettre des modèles de messages WhatsApp directement dans Braze, sans avoir à basculer entre Braze et le Meta Business gestionnaire. Une fois que Meta a approuvé votre modèle, utilisez-le dans autant de Campaigns et de Canvas que vous le souhaitez.

#### Étiquettes de produits, métachamps et collections Shopify {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez désormais [synchroniser les étiquettes de produits, les collections et les métachamps Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs) de votre boutique Shopify dans votre catalogue Braze. Cela fournit des données produit plus riches pour la personnalisation, la segmentation et la messagerie basée sur le catalogue sans solutions de contournement personnalisées.

### Partenariats

#### GRAVITY - Données et analyse - Fidélisation {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/) est une plateforme de fidélisation de niveau entreprise de Loyalty Juggernaut Inc. (LJI) qui permet aux marques du commerce de détail, du voyage, de la restauration (y compris la restauration rapide) et des services financiers de concevoir, gérer et faire évoluer des programmes de nouvelle génération, stimulant une croissance mesurable de l'engagement, de la rétention et de la valeur vie client grâce à des expériences personnalisées et axées sur les données.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

Les mises à jour SDK suivantes ont été publiées. Pour plus de détails, consultez les [journaux des modifications du SDK]({{site.baseurl}}/releases/sdk_changelogs).

#### Mises à jour majeures du SDK

{% multi_lang_include release_type.md release="General availability" %}

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_4_30_26_updates.md %}

{% enddetails %}
{% details 2 avril 2026 %}

## Publication du 2 avril 2026 {#april-2-2026-release}

### Données et rapports

#### Nouveaux champs du canal Banner dans les événements Currents et Datashare {#new-banner-channel-fields-in-currents-and-datashare-events}

Braze a ajouté des champs pour les événements existants du canal Banner dans les exports Currents et Datashare. Pour une liste de ces mises à jour d'événements et de champs, consultez [Changements dans la version 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-for-storage).

#### Prise en charge des centres de données Mixpanel UE et Inde pour Currents {#mixpanel-eu-and-india-data-center-support-for-currents}

L'intégration Currents Mixpanel prend désormais en charge les centres de données UE et Inde de Mixpanel. Lorsque vous configurez une intégration Mixpanel, vous pouvez choisir vers quelle région Mixpanel Braze envoie vos données. Cette mise à jour prend en charge l'empreinte internationale croissante de Mixpanel pour les clients communs. Pour plus d'informations, consultez [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

#### Sources et synchronisations réutilisables pour l'ingestion de données cloud (CDI) {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

L'ingestion de données cloud (CDI) dispose d'un nouveau design qui sépare les sources et les synchronisations, vous permettant de réutiliser une source pour plusieurs synchronisations. Les synchronisations existantes migrent automatiquement vers le nouveau modèle sources et synchronisations sans temps d'arrêt. Accédez à **Cloud Data Ingestion** > **Sources** pour afficher, modifier ou créer des sources, puis sélectionnez une source dans le menu déroulant lors de la création d'une synchronisation. Ce changement réduit les configurations répétitives et crée une base pour les améliorations futures. Pour plus d'informations, consultez [Configuration des intégrations d'entrepôt de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### Soumettre des tickets d'assistance depuis BrazeAI Operator<sup>TM</sup> {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) inclut désormais un flux pour soumettre des tickets d'assistance Braze sans quitter le tableau de bord. Pour les étapes, le contexte automatiquement inclus et les conseils pour une résolution plus rapide, consultez [Soumettre des tickets d'assistance avec BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets).

### Orchestration

#### Traductions multilingues

{% multi_lang_include release_type.md release="General availability" %}

Après avoir ajouté des locales à votre espace de travail, utilisez les [traductions multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) pour cibler des utilisateurs dans différentes langues au sein d'un seul push, e-mail, bannière, message in-app ou Content Block.

![Aperçus des locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Améliorations de Canvas Context

{% multi_lang_include release_type.md release="General availability" %}

Dans Canvas, vous pouvez désormais référencer des variables de contexte pour définir :

- Une [expiration]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) pour les bannières et les messages in-app dans une étape Message
- Des [délais personnalisés]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) pour les étapes Parcours d'action

Dans le champ du nom de la variable de contexte, vous pouvez également saisir le nom de la variable de contexte ou le sélectionner dans le menu déroulant de l'éditeur d'étape. Pour plus de détails, consultez [Contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) et [Variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

### Canaux et points de contact

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk) est un canal de communication qui permet l'envoi de messages diffusés et le chat 1:1 avec les utilisateurs. Créez une expérience utilisateur personnalisée en utilisant Liquid et d'autres contenus dynamiques pour construire un environnement qui favorise et enrichit une expérience utilisateur riche avec votre marque.

![Un message de type liste KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Bannières dans Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez utiliser les [bannières]({{site.baseurl}}/user_guide/channels/banners) comme canal de communication dans les [étapes Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de Canvas. Les bannières vous permettent de personnaliser dynamiquement le contenu de votre application ou site web, en reflétant l'éligibilité et le comportement de l'utilisateur en temps réel.

### Partenariats

#### CataBoom - Personnalisation des messages - Contenu visuel et interactif {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom) est une plateforme de gamification. Les marques l'utilisent pour créer et lancer des expériences numériques interactives, notamment des jeux de type roue de la fortune, des quiz et des jeux à gain instantané. Ces expériences approfondissent l'engagement et collectent des données first-party.

#### Denada - Orchestration des messages - Modèles {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada) est une plateforme créative marketing alimentée par l'intelligence artificielle qui permet aux experts métier de créer des supports marketing conformes à la marque par le biais d'une conversation naturelle. Avec Denada, les équipes peuvent passer de l'idéation au contenu e-mail finalisé sans avoir besoin d'expertise en design.

#### Poq - eCommerce - Plateforme d'applications mobiles {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq) permet aux entreprises de lancer, gérer et faire évoluer rapidement des applications iOS et Android entièrement natives, offrant des expériences mobiles performantes qui stimulent le commerce et donnent vie à la promesse de votre marque.

#### The Trade Desk – Canvas Audience Sync

Grâce à [Braze Audience Sync vers The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync), vous pouvez synchroniser dynamiquement vos données utilisateur first-party de Braze directement dans The Trade Desk pour le reciblage publicitaire, la modélisation de sosies et la suppression.

### SDK

#### Connecter votre environnement de développement intégré (IDE) au Docs MCP {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

Utilisez des assistants de codage IA pour accélérer votre flux de travail d'intégration Braze en connectant votre environnement de développement intégré (IDE) au Braze Docs MCP via Context7. Cela donne à votre assistant un accès direct à la documentation Braze actuelle, afin qu'il puisse générer des conseils SDK plus précis, des exemples de code et une aide au dépannage dans votre environnement de développement. Pour les étapes de configuration dans Cursor, Claude Desktop et VS Code, consultez [Développer avec un LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm#connecting-to-the-braze-docs-mcp).

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_4_2_26_updates.md %}

{% enddetails %}

{% details 5 mars 2026 %}

## Publication du 5 mars 2026 {#march-5-2026-release}

### Données et rapports

#### Nouveau centre de données {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Braze a lancé un nouveau [centre de données]({{site.baseurl}}/user_guide/data/infrastructure/data_centers) : JP-01. Vous pouvez vous inscrire à des centres de données spécifiques à une région lors de la configuration de votre compte Braze.

#### Variables de contexte {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

Les [variables de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) sont des données temporaires que vous pouvez créer et utiliser dans le parcours d'un utilisateur à travers un Canvas spécifique. Chaque fois qu'un utilisateur entre dans le Canvas, même s'il y est déjà entré auparavant, les variables de contexte seront redéfinies en fonction des dernières données d'entrée et de la configuration du Canvas. Cette approche permet à chaque entrée dans le Canvas de maintenir son propre contexte indépendant, permettant aux utilisateurs d'avoir plusieurs états actifs au sein du même parcours tout en conservant le contexte spécifique de chaque état.

#### Sources d'ingestion de données cloud {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

L'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze) dispose d'une nouvelle interface qui sépare les sources des synchronisations, vous permettant de réutiliser une seule source pour un nombre illimité de synchronisations. Cela réduit les configurations en double et simplifie la mise en place lorsque vous avez plusieurs synchronisations. Si vous avez des synchronisations existantes, elles sont automatiquement migrées vers la nouvelle structure sources-et-synchronisations sans temps d'arrêt. Pour commencer, accédez à **Cloud Data Ingestion** > **Sources** pour afficher, modifier ou créer des sources, puis sélectionnez une source dans le menu déroulant lors de la création d'une synchronisation.

#### Champs supplémentaires pour les événements Currents et Data Share {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

Les [événements Currents et Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) incluent désormais les nouveaux champs suivants pour approfondir les données disponibles pour l'analyse et les systèmes en aval :

{% multi_lang_include releases/currents/2026_3_5_26_field_changes.md %}

#### Champs Campaign et Canvas pour Snowflake Data Share {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) inclut désormais des champs supplémentaires reflétant les informations de Campaign et Canvas dans 66 tables existantes, notamment :

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validation pré-importation CSV et rapport d'erreurs {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

Les [importations d'utilisateurs par CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) prennent désormais en charge la validation pré-importation et le rapport d'erreurs détaillé. Avant l'importation, sélectionnez **Valider le fichier avant l'importation** sur la page **Importer des utilisateurs** — Braze analysera votre fichier et générera un rapport identifiant les lignes qui échoueront entièrement (erreurs) et les lignes qui réussiront avec certaines valeurs ignorées (avertissements). Vous pouvez télécharger le rapport, corriger votre CSV et le re-télécharger, ou procéder tel quel. Après la fin de l'importation, un rapport téléchargeable des lignes ayant échoué est également disponible, avec la raison exacte de chaque problème.

#### Tableau de bord de diagnostic des messages

{% multi_lang_include release_type.md release="Early access" %}

Le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) fournit une ventilation de haut niveau des résultats d'envoi de messages, vous permettant de repérer les tendances et de diagnostiquer les problèmes potentiels dans votre configuration de messagerie. Ce tableau de bord peut vous aider à comprendre pourquoi les messages de vos Campaigns ou Canvas n'ont peut-être pas été envoyés comme prévu.

### BrazeAI<sup>TM</sup>

#### Braze Agents dans la Console des agents {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

Les [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) sont des assistants alimentés par l'intelligence artificielle que vous pouvez créer dans Braze. Les agents peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées. Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous pour son comportement. Une fois en production, l'agent peut être [déployé]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) dans Braze pour générer du texte personnalisé, prendre des décisions en temps réel ou mettre à jour les champs du catalogue.

### Orchestration

#### Autorisations granulaires des utilisateurs {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze introduit les [autorisations granulaires]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), un moyen plus flexible de gérer l'accès des utilisateurs. Consultez [Migration vers les autorisations granulaires]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) pour en savoir plus sur le processus de migration, y compris la correspondance entre les autorisations héritées et les autorisations granulaires.

#### Limitation de débit basée sur le canal {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

Lors de la définition d'une limite de débit de vitesse de distribution pour une Campaign ou un Canvas multicanal, vous pouvez choisir de définir soit une limite de débit partagée, soit une [limite basée sur le canal]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases). Lorsqu'une Campaign ou un Canvas multicanal utilise une limitation de débit basée sur le canal, la limite de débit s'applique à chacun des canaux sélectionnés. Par exemple, vous pouvez configurer votre Campaign ou Canvas pour envoyer un maximum de 5 000 webhooks et 2 500 messages SMS par minute sur l'ensemble de la Campaign ou du Canvas.

#### Étape Canvas Context {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

Les [étapes Canvas Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) vous permettent de créer et de mettre à jour une ou plusieurs variables pour un utilisateur au fur et à mesure qu'il progresse dans un Canvas. Par exemple, si vous avez un Canvas qui gère des remises saisonnières, vous pouvez utiliser une variable de contexte pour stocker un code de remise différent chaque fois qu'un utilisateur entre dans le Canvas.

### Canaux et points de contact

#### Traduire les locales dans les Content Blocks {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

Après avoir ajouté des locales à votre espace de travail, vous pouvez [cibler des utilisateurs dans différentes langues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) au sein d'un Content Block.

### Partenariats

#### Algolia - Recherche et recommandations {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) est une plateforme de recherche et de découverte qui aide les développeurs à créer des expériences de recherche rapides, pertinentes et évolutives. Grâce à une approche API-first puissante, Algolia combine des algorithmes de classement avancés avec des informations pilotées par l'intelligence artificielle pour une recherche sur site, une navigation et une découverte de contenu personnalisée fluides.

#### Anthropic - Fournisseur de modèles IA {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) est une entreprise de recherche et de sécurité en intelligence artificielle qui développe Claude, un assistant IA de nouvelle génération conçu pour être utile, honnête et sûr pour un large éventail de tâches linguistiques.

#### Canva - Personnalisation des messages - Studio créatif {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva) synchronise vos images dans Canva directement avec la bibliothèque multimédia de Braze, rationalisant votre flux de travail créatif et maintenant vos ressources visuelles à jour sur tous vos canaux de communication.

#### DOTS.ECO - Récompenses {#dotseco-rewards}

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) vous permet de récompenser les utilisateurs avec un impact environnemental réel grâce à des certificats numériques traçables. Chaque certificat peut inclure des métadonnées comme une URL de certificat partageable et une URL d'image, afin que les utilisateurs puissent voir (et revoir) leur preuve d'impact.

#### Figma - Personnalisation des messages - Studio créatif {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma) est une plateforme de design collaborative qui vous permet de créer, concevoir et prototyper des produits. Utilisez cette intégration pour envoyer des images et des ressources visuelles de Figma directement dans la bibliothèque multimédia de Braze.

#### Flybuy - Personnalisation des messages - Localisation {#flybuy-message-personalization-location}

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy) de Radius Networks est la principale plateforme de localisation omnicanale exploitant une technologie alimentée par l'intelligence artificielle pour optimiser la vitesse de service pour le retrait, la livraison, le drive et la restauration sur place. Grâce à sa suite marketing intégrée, Flybuy permet également aux marques de diffuser des messages hyper-ciblés et basés sur le moment, contribuant à stimuler l'engagement, augmenter le panier moyen et soutenir des initiatives de fidélisation plus larges.

#### Google Gemini - Fournisseur de modèles IA {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) est la famille de modèles d'intelligence artificielle de Google qui combine un raisonnement avancé sur le texte, le code et les images pour aider les marques à offrir des expériences plus intelligentes et plus personnalisées.

#### Limbik - Personnalisation des messages - Moteurs de personnalisation {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) est votre couche de résonance IA — prédisant comment les audiences réelles interprètent et réagissent aux messages, concepts et résultats d'IA avant qu'ils n'atteignent le marché. Alimenté par une recherche primaire continue dans plus de 60 pays et 25 langues, Limbik fournit des audiences synthétiques validées par l'humain — des populations numériques qui simulent la réponse d'une audience réelle à la vitesse de la machine et avec une précision de niveau recherche (95 % de confiance, 1,5 % à 3 % de marge d'erreur). Limbik vous donne la capacité de vous assurer immédiatement que votre message résonne avec ce que votre audience cible croit et ressent.

#### Linkrunner - Orchestration des messages - Attribution {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) est une plateforme d'attribution mobile et d'analyse qui vous aide à suivre et analyser vos campagnes d'acquisition d'utilisateurs.

#### Mailizio - Orchestration des messages - Modèles {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) est une plateforme de création et de gestion d'e-mails qui facilite la conception de contenus réutilisables et conformes à la marque à l'aide d'un éditeur visuel intuitif. Grâce à l'intégration de Mailizio à Braze, vous pouvez exporter vos blocs de contenu et vos modèles d'e-mail, puis générer automatiquement des messages in-app à partir de ces mêmes ressources, permettant un déploiement rapide et entièrement contrôlé des campagnes.

#### Open Loyalty - Données et analyse - Fidélisation {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) est une plateforme de programmes de fidélisation basée sur le cloud qui vous permet de créer et de gérer des programmes de fidélisation et de récompenses pour vos clients. L'intégration de Braze et d'Open Loyalty synchronise les données de fidélisation — telles que le solde de points, les changements de niveau et les avertissements d'expiration — directement dans Braze en temps réel. Cela vous permet de déclencher des messages personnalisés (e-mail, push, SMS) lorsque le statut de fidélité d'un utilisateur change.

#### OpenAI - Fournisseur de modèles IA {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) crée des modèles d'intelligence artificielle avancés, comme GPT, qui permettent la compréhension et la génération du langage naturel, donnant aux marques les moyens de créer et de faire évoluer des interactions client significatives.

#### Shopgate - Canaux {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) est une plateforme de commerce mobile et omnicanale qui aide les commerçants à créer des applications d'achat et à améliorer l'efficacité des magasins physiques grâce à des outils de traitement des commandes et de clienteling, c'est-à-dire un support client personnalisé en magasin basé sur les données client.

#### Splio - Données et analyse - Importation de cohortes {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) est un outil de construction d'audiences qui vous permet d'augmenter le nombre de campagnes et le chiffre d'affaires sans nuire à l'expérience client, et fournit des analyses pour suivre les performances des campagnes CRM en ligne et hors ligne.

### SDK

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_3_5_26_updates.md %}

{% enddetails %}

{% details 5 février 2026 %}

## Publication du 5 février 2026 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### Optimiseur de contenu {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

L'[Optimiseur de contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer) est une étape Canvas de test de contenu continu et à haute variante qui offre une optimisation automatisée de l'engagement. À l'aide d'une interface de type glisser-déposer similaire à l'étape Message, définissez les composants à tester, générez des variantes à l'aide de l'intelligence artificielle (ou saisissez-les manuellement) et utilisez les étiquettes Liquid pour mapper ces composants au contenu de votre message.

Créé à partir d'un optimiseur de bandits multi-bras non contextuel, l'Optimiseur de contenu envoie un seul message par utilisateur, déterminant la combinaison de variantes de composants à fournir sur la base de recommandations prédictives. À mesure que l'étape recueille des données au fil du temps, les variantes performantes augmentent naturellement leur allocation d'envoi tandis que les variantes peu performantes diminuent. L'Optimiseur de contenu fonctionne mieux avec les Canvas à envoi répété qui ont un volume d'utilisateurs quotidien constant (au moins quelques milliers d'utilisateurs par jour) pour permettre une optimisation continue.

### Données et rapports

#### Événements recommandés pour le commerce électronique

{% multi_lang_include release_type.md release="Early access" %}

Pour faire correspondre les événements recommandés pour le commerce électronique avec l'événement d'achat existant, nous avons ajouté l'[événement de conversion « Passe une commande »]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases#conversions-dashboard), qui est similaire à « Effectue un achat ».

### Canaux et points de contact

#### Traduire les locales dans les bannières {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

Après avoir ajouté des locales à votre espace de travail, [ciblez des utilisateurs dans différentes langues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#use-locales) au sein d'une même bannière.

#### Configurer la largeur des Content Blocks en glisser-déposer {#configure-width-for-drag-and-drop-content-blocks}

[Ajustez la largeur de votre Content Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) en sélectionnant le bouton dans le menu de navigation. La largeur par défaut est de 100 % si elle n'est pas spécifiée dans les paramètres de style globaux de votre e-mail ; dans le cas contraire, les paramètres globaux seront respectés.

![Une flèche double face avec une option permettant de modifier la largeur.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Utiliser le réchauffement d'adresses IP automatisé {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

Utilisez le [réchauffement d'adresses IP automatisé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#automated-ip-warming) pour augmenter progressivement votre volume d'envoi quotidien, permettant aux fournisseurs de boîtes de réception d'apprendre et de faire confiance à vos habitudes d'envoi. Braze envoie d'abord à vos abonnés les plus engagés, ce qui permet au volume quotidien d'augmenter à un rythme correspondant aux meilleures pratiques.

### Partenariats

#### LinkedIn – Canvas Audience Sync

Grâce à [Braze Audience Sync vers LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync), ajoutez les données utilisateur de votre intégration Braze aux listes de clients LinkedIn pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tous les critères que vous utiliseriez normalement pour déclencher un message (tel que push, e-mail, SMS et webhook) dans un Canvas Braze sur la base de vos données utilisateur peuvent désormais déclencher une publicité pour cet utilisateur dans vos listes de clients LinkedIn.

#### Oracle Crowdtwist - Données et analyse {#oracle-crowdtwist-data-analytics}

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) est une solution de fidélisation des clients native dans le cloud qui permet aux marques d'offrir des expériences client personnalisées. Leur solution offre plus de 100 chemins d'engagement prêts à l'emploi, permettant aux marketeurs d'obtenir rapidement une vue plus complète du client.

#### Fullstory - Contenu dynamique {#fullstory-dynamic-content}

La plateforme de données comportementales de [Fullstory]({{site.baseurl}}/partners/fullstory) aide les leaders technologiques à prendre de meilleures décisions, plus éclairées. En injectant des données comportementales numériques dans leur pile analytique, la technologie brevetée de Fullstory libère la puissance des données comportementales de qualité à grande échelle — transformant chaque visite numérique en informations exploitables.

#### Open Loyalty - Données et analyse {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty) est une plateforme de programmes de fidélisation basée sur le cloud qui vous permet de créer et de gérer des programmes de fidélisation et de récompenses pour vos clients. L'intégration de Braze et d'Open Loyalty synchronise les données de fidélisation — telles que le solde de points, les changements de niveau et les avertissements d'expiration — directement dans Braze en temps réel. Cela vous permet de déclencher des messages personnalisés (e-mail, push, SMS) lorsque le statut de fidélité d'un utilisateur change.

#### DOTS.ECO - Extensions

[DOTS.ECO]({{site.baseurl}}/partners/dots.eco) vous permet de récompenser les utilisateurs avec un impact environnemental réel grâce à des certificats numériques traçables. Chaque certificat peut inclure des métadonnées telles qu'une URL de certificat et une URL d'image partageables, afin que les utilisateurs puissent voir (et revoir) leur preuve d'impact.

#### Mailizio - Orchestration des messages {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio) est une plateforme de création et de gestion d'e-mails qui facilite la conception de contenus réutilisables et conformes à la marque à l'aide d'un éditeur visuel intuitif. Grâce à l'intégration de Mailizio à Braze, exportez vos blocs de contenu et vos modèles d'e-mail, puis générez automatiquement des messages in-app à partir de ces mêmes ressources, permettant un déploiement rapide et entièrement contrôlé des campagnes.

### API {#apis}

#### API POST de la bibliothèque multimédia {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

Les ressources de la bibliothèque multimédia peuvent désormais être ajoutées via l'API, permettant aux clients, partenaires et agences d'automatiser une plus grande partie de leurs flux de travail de création de messages. Utilisez l'[API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) pour télécharger directement un fichier de ressource ou copier un fichier à partir d'une URL existante. Cette fonctionnalité débloque des capacités d'intégration et d'automatisation.

### Currents et Datashare

#### Événements de la Console des agents pour les destinations de stockage et le Datashare {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

Deux nouveaux [événements]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) sont désormais disponibles pour les destinations de stockage (AWS S3, GCS et Azure Blob Storage) et Snowflake Datashare : `agentconsole.AgentExecuted` et `agentconsole.ToolInvocation`. Ces événements vous permettent d'analyser l'utilisation de la Console des agents et les détails dans vos systèmes en aval, vous aidant à comprendre et à tirer le meilleur parti de l'utilisation de vos agents. Les agents vous permettent de créer et de déployer des agents intelligents capables d'effectuer des tâches spécifiques dans Braze, notamment de générer du contenu dans des Canvas ou des catalogues et d'acheminer les utilisateurs vers différents chemins sur la base d'une prise de décision intelligente. Pour plus d'informations, consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Nouveaux événements « Retry » pour les canaux individuels {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

De nouveaux [événements de réessai]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) sont désormais disponibles pour les e-mails, LINE, les notifications push, les SMS, les webhooks et les canaux WhatsApp. Ces événements permettent de savoir quand la limitation de fréquence entraîne le report d'un message planifié au lieu de son annulation. Lorsqu'un message est dépriorisé ou soumis à une limite de fréquence, il peut désormais être réessayé dans une fenêtre de réessai configurée, vous offrant de meilleures informations sur les modèles de distribution des messages et l'impact de la limitation de fréquence. Pour plus d'informations, consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Ajout d'un nouveau champ `time_ms` à l'événement TokenStateChange {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

Un nouveau champ `time_ms` a été ajouté à l'événement [`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), fournissant une granularité de l'ordre de la milliseconde pour le suivi des changements d'état du jeton push. Cette précision accrue vous aide à comprendre le dernier statut d'un jeton push lorsque plusieurs changements se produisent au cours de la même seconde, vous donnant confiance dans les systèmes en aval quant au statut correct de l'abonnement. Pour plus d'informations, consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Envoyer un utilisateur anonyme vers les destinations Tealium {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

Les événements pour lesquels aucun ID utilisateur externe n'a été défini peuvent désormais être diffusés vers les destinations [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1). Lorsque vous cochez la case « Inclure les événements des utilisateurs anonymes » dans votre intégration Currents, les événements sans ID utilisateur externe seront envoyés à la destination au lieu d'être supprimés. Cette capacité est essentielle pour les analyses en aval et les cas d'usage impliquant des utilisateurs non identifiés et anonymes.

##### Envoyer un utilisateur anonyme vers des destinations CustomHTTP {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

Les événements pour lesquels aucun ID utilisateur externe n'a été défini peuvent désormais être diffusés vers des destinations CustomHTTP. Lorsque vous cochez la case « Inclure les événements des utilisateurs anonymes » dans votre intégration Currents, les événements sans ID utilisateur externe seront envoyés à la destination au lieu d'être supprimés. Cette capacité est essentielle pour les analyses en aval et les cas d'usage impliquant des utilisateurs non identifiés et anonymes.

#### Événement d'ouverture d'e-mail — champ « machine_open » {#email-open-event-machine_open-field}

L'[événement d'ouverture d'e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) génère désormais la valeur du champ « machine_open » pour établir un rapport sur l'indicateur [_Ouverture machine_]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

### SDK

Les mises à jour SDK suivantes ont été publiées. La version 14.0.1 du SDK Swift corrige un problème lié à la gestion des liens universels. La version 40.2.0 du SDK Android corrige une fuite de mémoire potentielle et résout un problème lié à l'ouverture de plusieurs sessions en présence d'activités transparentes. La version 3.2.0 du SDK Expo ajoute l'option `forwardUniversalLinks` (par défaut : false) pour configurer la gestion native des liens universels par le SDK Swift.

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_2_5_26_updates.md %}

{% enddetails %}