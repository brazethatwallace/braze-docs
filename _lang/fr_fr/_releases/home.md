---
nav_title: Accueil
article_title: Quoi de neuf dans Braze ?
description: "Les notes de mise à jour de Braze sont publiées mensuellement afin que vous puissiez vous tenir au courant des versions majeures du produit, des améliorations continues du produit, des partenariats de Braze, des changements majeurs du SDK et de l'abandon de fonctionnalités."
page_order: 0
search_rank: 1
page_type: reference

---

# Quoi de neuf dans Braze ? {#whats-new-in-braze}

{% alert tip %}
Pour plus d'informations sur l'une des mises à jour énumérées sur cette page, contactez votre gestionnaire de compte ou [ouvrez un ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support). Vous pouvez également consulter nos [journaux des modifications du SDK]({{site.baseurl}}/developer_guide/changelogs) pour plus d'informations sur les versions mensuelles du SDK, les améliorations et les changements majeurs.
{% endalert %}

{% details 25 juin 2026 %}

## Publication le 25 juin 2026 {#june-25-2026-release}

### Données et rapports {#data-reporting}

#### Mise à jour du nom de l'indicateur pour les Content Cards et les bannières {#metric-name-update-for-content-cards-and-banners}

L'indicateur _Destinataires uniques_ a été renommé en _Impressions quotidiennes uniques_ pour les Content Cards et les bannières. Les _Impressions quotidiennes uniques_ font référence au nombre reçu de Braze et sont basées sur le `user_id`. Les impressions quotidiennes uniques sont comptabilisées au niveau de la Campaign ou de l'étape Canvas. Pour plus de détails, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

#### Suppression d'utilisateurs {#user-deletion}

{% multi_lang_include release_type.md release="General availability" %}

La [suppression d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) vous permet de gérer votre base de données en supprimant les profils qui ne sont plus nécessaires, créés par erreur ou devant être supprimés pour des raisons de conformité (comme le RGPD ou le CCPA).

#### Exclusions de points de données {#data-point-exclusions}

{% multi_lang_include release_type.md release="General availability" %}

Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) ne sont plus comptabilisés dans les points de données facturables. Vous pouvez adopter les événements de commerce électronique Braze (`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`) sans consommation de points de données.

#### Onglet Historique des événements {#event-history-tab}

{% multi_lang_include release_type.md release="General availability" %}

L'onglet **Event History** sur les [profils utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) répertorie les événements personnalisés et les achats de l'utilisateur au cours des 30 derniers jours (jusqu'aux 100 plus récents). Utilisez-le pour confirmer qu'une intégration SDK ou API envoie les événements comme prévu, déboguer pourquoi un utilisateur est (ou n'est pas) entré dans une Campaign ou un Canvas déclenché par un événement, ou enquêter sur une escalade de support concernant un utilisateur spécifique.

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

Lors de la création d'un agent dans la **Console des agents**, vous pouvez choisir de créer un agent personnalisé ou de sélectionner une option dans **Create an agent with Operator** pour utiliser BrazeAI Operator afin d'appliquer un modèle de départ. Operator peut pré-configurer les instructions, les champs de sortie et le contexte pour les modèles de départ suivants de la Console des agents.

Pour plus de détails, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

#### Améliorations de la Console des agents {#agent-console-enhancements}

Vous pouvez effectuer les actions suivantes dans la [Console des agents]({{site.baseurl}}/user_guide/brazeai/agents) :

{% multi_lang_include releases/brazeai_agent_console_enhancements.md %}

#### Modifier une étape Optimiseur de contenu lancée {#edit-a-launched-content-optimizer-step}

{% multi_lang_include release_type.md release="Beta" %}

Après le lancement de votre Canvas, vous pouvez désormais [mettre à jour une étape Optimiseur de contenu]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step) pour :

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

### Canaux et points de contact {#channels-touchpoints}

#### Fermeture par l'utilisateur pour les bannières {#user-dismissals-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez permettre aux utilisateurs de fermer manuellement une bannière en sélectionnant **Banner can be dismissed** lors de la configuration du comportement de fermeture. Cette option est utile dans les scénarios où vous souhaitez promouvoir une vente à durée limitée pour tous les utilisateurs de l'application, tout en leur permettant de fermer le message s'ils ne sont pas intéressés.

Consultez [Configurer le comportement de fermeture]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) pour plus de détails sur l'activation de la fermeture et la personnalisation du bouton de fermeture.

#### Suivi des clics personnalisé pour les bannières {#custom-click-tracking-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Pour un suivi des clics plus granulaire pour les bannières, vous pouvez [attribuer un identifiant personnalisé]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) à chaque élément interactif en utilisant le champ **Identifier for Reporting** dans son panneau de propriétés.

#### Rééligibilité pour les bannières {#re-eligibility-for-banners}

Lorsque la rééligibilité est activée pour les Campaigns de bannières, les utilisateurs qui ferment une bannière peuvent redevenir éligibles après une fenêtre de temporisation configurable qui commence à la fermeture. Si la rééligibilité n'est pas activée, les utilisateurs ayant fermé la bannière restent inéligibles. Pour configurer la rééligibilité, consultez [Configurer la rééligibilité]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Notez que les étapes de bannière Canvas utilisent les paramètres de réentrée Canvas à la place.

#### Test A/B Quick Push {#quick-push-ab-testing}

{% multi_lang_include release_type.md release="General availability" %}

Le test A/B Quick Push prend désormais en charge les Campaigns push multiplateformes et les étapes Canvas via des groupes de variantes, vous permettant de tester des variations de messages iOS et Android alignées dans un seul flux de travail. Pour plus d'informations, consultez [Messages push multiplateformes]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push#use-cases).

#### Sélection de variante BrazeAI<sup>TM</sup> {#brazeai-variant-selection}

{% multi_lang_include release_type.md release="Early access" %}

La sélection de variante BrazeAI<sup>TM</sup> s'active automatiquement lorsque vous ajoutez plusieurs variantes push, applique les paramètres d'expérience recommandés par défaut et optimise vers la variante la plus performante pour améliorer l'engagement. Vous pouvez la désactiver si vous devez envoyer immédiatement. Pour plus d'informations, consultez [Sélection de variante BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

#### Résultats d'envoi test WhatsApp {#whatsapp-test-send-results}

Après l'envoi d'un message WhatsApp de test, vous pouvez consulter un [rapport de distribution détaillé]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-4-view-test-send-results) directement dans le compositeur de messages. Cela vous aide à confirmer que votre message a atteint le destinataire prévu et à résoudre les échecs avant le lancement.

### Partenariats {#partnerships}

#### Convercus - Données et analyse - Fidélisation {#convercus-data-and-analytics-loyalty}

[Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus) est une plateforme SaaS de fidélisation et de coupons qui aide les marques et les détaillants à augmenter la fréquence d'achat, la valeur du panier et les taux de rachat grâce à des programmes de fidélisation omnicanaux et des Campaigns de coupons personnalisées.

#### Copy Pastd - Orchestration des messages - Modèles {#copy-pastd-message-orchestration-templates}

[Copy Pastd]({{site.baseurl}}/partners/copy_pastd) Building Blocks est un générateur d'e-mails par glisser-déposer qui pousse des Content Blocks alimentés par Liquid et des modèles complets directement dans votre espace de travail Braze. Concevez une fois, synchronisez avec Braze et réutilisez les mêmes composants dans les Campaigns, les Canvas et les flux déclenchés sans reconstruire le HTML à chaque fois.

#### Databricks Mosaic - Fournisseurs de modèles IA {#databricks-mosaic-ai-model-providers}

[Databricks Mosaic]({{site.baseurl}}/partners/databricks_mosaic) est la plateforme unifiée de Databricks pour créer, déployer et gérer des modèles d'intelligence artificielle et de machine learning à grande échelle sur la plateforme Databricks Data Intelligence.

#### DinMo - Données et analyse - Reverse ETL {#dinmo-data-and-analytics-reverse-etl}

[DinMo]({{site.baseurl}}/partners/dinmo) est une plateforme de données client (CDP) composable qui connecte votre entrepôt de données cloud à Braze via un processus ETL inversé (Extract, Transform, Load). Les équipes marketing peuvent créer des segments d'audience à partir des données de l'entrepôt, synchroniser les attributs et événements utilisateur dans Braze et maintenir les statuts d'abonnement à jour sans téléchargements CSV ni support d'ingénierie.

#### EmailShepherd - Orchestration des messages - Modèles {#emailshepherd-message-orchestration-templates}

[EmailShepherd]({{site.baseurl}}/partners/emailshepherd) est une plateforme de création d'e-mails agentique construite sur votre système de design d'e-mails qui permet à toute votre équipe marketing — et aux agents d'intelligence artificielle — de produire des e-mails conformes à la marque et prêts pour la production sans goulots d'étranglement. L'intégration Braze publie les e-mails approuvés directement dans votre espace de travail Braze, afin que les marketeurs puissent faire évoluer la production d'e-mails dans Braze sans sacrifier la cohérence de la marque.

#### Talkable - Personnalisation des messages - Recommandations {#talkable-message-personalization-referrals}

[Talkable]({{site.baseurl}}/partners/talkable) aide les marques grand public à transformer les clients satisfaits en un canal de recommandation évolutif. Grâce à l'intégration Braze, les opt-ins d'e-mails marketing capturés dans les Campaigns de recommandation Talkable sont transmis à Braze en temps réel, fournissant à votre équipe le consentement, le contexte et les données de Campaign nécessaires pour accueillir, segmenter et engager chaque nouvel ambassadeur et ami.

### SDK

#### Mises à jour majeures du SDK {#sdk-breaking-updates}

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_6_25_26_updates.md %}

{% enddetails %}

{% details 28 mai 2026 %}

## Publication le 28 mai 2026 {#may-28-2026-release}

### Données et rapports

#### Tableau de bord des performances push {#push-performance-dashboard}

Le [tableau de bord des performances push]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) vous offre une vue unique au niveau du canal de l'engagement push, incluant les envois, les rebonds, les distributions et les taux d'ouverture directs, influencés et totaux sur une fenêtre temporelle configurable. Utilisez-le pour comprendre la santé globale de votre canal push sans avoir à agréger les données de Campaigns ou de Canvas individuels.

#### Champs de géolocalisation dans les sélections de catalogue {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

Les catalogues prennent désormais en charge le filtrage basé sur la distance grâce au nouveau type de champ de géolocalisation et aux opérateurs de sélection de catalogue. Cela vous aide à créer des expériences plus pertinentes et sensibles à la localisation, comme montrer à chaque utilisateur le restaurant le plus proche, filtrer les propriétés disponibles dans un rayon de 50 km pour une Campaign immobilière, ou cibler les magasins proches d'un événement spécifique. Au lieu d'approximer le ciblage géographique avec des codes de ville ou de région, vous pouvez filtrer les éléments du catalogue par proximité à un point central, y compris un attribut utilisateur Liquid tel que la localisation la plus récente d'un utilisateur. Pour plus d'informations, consultez [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

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

[Chord](https://www.chord.co/) fournit une plateforme de données client qui capture et standardise les événements de votre vitrine e-commerce. Lorsque vous connectez Chord à Braze, les activités d'achat, les événements comportementaux et les mises à jour d'identité sont transmis à Braze afin que vous puissiez déclencher des Campaigns et maintenir les profils à jour sans avoir à construire ces pipelines vous-même.

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

## Publication le 30 avril 2026 {#april-30-2026-release}

### Données et rapports

#### Ajout rapide d'utilisateur pour la création de profils individuels {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez désormais créer un profil utilisateur individuel depuis **Import Users** en sélectionnant **Quick User Add** et en saisissant un e-mail ou un ID externe.

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

Gérer qui peut accéder à votre compte et effectuer des actions spécifiques est essentiel pour la sécurité et l'efficacité opérationnelle. Pour vous donner plus de contrôle, Braze introduit les [autorisations granulaires]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration), un moyen plus flexible et précis de gérer l'accès des utilisateurs à votre compte.

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

Les [validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) fournissent une vérification supplémentaire pour confirmer que votre audience répond aux critères de distribution au moment de l'envoi du message. Si un utilisateur ne répond pas aux validations de distribution définies pour une étape Message, vous pouvez utiliser le paramètre **Delivery validations advancement behavior** pour déterminer si l'utilisateur doit avancer à l'étape suivante ou quitter le Canvas.

#### Limites de débit de messagerie de l'espace de travail {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

Utilisez les [limites de débit de messagerie de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) pour réguler le débit de distribution de vos messages sortants depuis votre plateforme afin de vous assurer que vos utilisateurs reçoivent les messages dont ils ont besoin. Les limites de débit de messagerie de l'espace de travail sont déployées progressivement, il est donc possible que vous ne voyiez pas encore ces paramètres dans votre tableau de bord.

### Canaux et points de contact

#### Générateur de modèles WhatsApp {#whatsapp-template-builder}

{% multi_lang_include release_type.md release="Early access" %}

Le [générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization) vous permet de créer et de soumettre des modèles de messages WhatsApp directement dans Braze, sans avoir à basculer entre Braze et le Meta Business Manager. Une fois que Meta a approuvé votre modèle, utilisez-le dans autant de Campaigns et de Canvas que vous le souhaitez.

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

## Publication le 2 avril 2026 {#april-2-2026-release}

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

Après avoir ajouté des locales à votre espace de travail, utilisez les [traductions multilingues]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) pour cibler des utilisateurs dans différentes langues au sein d'un seul push, e-mail, bannière, message in-app ou Content Block.

![Aperçus des locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Améliorations de Canvas Context

{% multi_lang_include release_type.md release="General availability" %}

Dans Canvas, vous pouvez désormais référencer des variables de contexte pour définir :

- Une [expiration]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#set-an-expiration) pour les bannières et les messages in-app dans une étape Message
- Des [délais personnalisés]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#action-path-delays) pour les étapes Parcours d'action

Dans le champ du nom de la variable de contexte, vous pouvez également saisir le nom de la variable de contexte ou le sélectionner dans le menu déroulant de l'éditeur d'étape. Pour plus de détails, consultez [Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) et [Variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables).

### Canaux et points de contact

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk) est un canal de communication qui permet l'envoi de messages diffusés et le chat 1:1 avec les utilisateurs. Créez une expérience utilisateur personnalisée en utilisant Liquid et d'autres contenus dynamiques pour construire un environnement qui favorise et enrichit une expérience utilisateur riche avec votre marque.

![Un message de type liste KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Bannières dans Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez utiliser les [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners) comme canal de communication dans les [étapes Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) de Canvas. Les bannières vous permettent de personnaliser dynamiquement le contenu de votre application ou site web, en reflétant l'éligibilité et le comportement de l'utilisateur en temps réel.

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

## Publication le 5 mars 2026 {#march-5-2026-release}

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

Les [importations d'utilisateurs par CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) prennent désormais en charge la validation pré-importation et le rapport d'erreurs détaillé. Avant l'importation, sélectionnez **Validate file before importing** sur la page **Import Users** — Braze analysera votre fichier et générera un rapport identifiant les lignes qui échoueront entièrement (erreurs) et les lignes qui réussiront avec certaines valeurs ignorées (avertissements). Vous pouvez télécharger le rapport, corriger votre CSV et le re-télécharger, ou procéder tel quel. Après la fin de l'importation, un rapport téléchargeable des lignes ayant échoué est également disponible, avec la raison exacte de chaque problème.

#### Tableau de bord de diagnostic des messages {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="Early access" %}

Le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) fournit une ventilation de haut niveau des résultats d'envoi de messages, vous permettant de repérer les tendances et de diagnostiquer les problèmes potentiels dans votre configuration de messagerie. Ce tableau de bord peut vous aider à comprendre pourquoi les messages de vos Campaigns ou Canvas n'ont peut-être pas été envoyés comme prévu.

### BrazeAI<sup>TM</sup>

#### Braze Agents dans la Console des agents {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

Les [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) sont des assistants alimentés par l'intelligence artificielle que vous pouvez créer dans Braze. Les agents peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées. Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous pour son comportement. Une fois en production, l'agent peut être [déployé]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) dans Braze pour générer du texte personnalisé, prendre des décisions en temps réel ou mettre à jour les champs du catalogue.

### Orchestration

#### Autorisations granulaires des utilisateurs {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze introduit les [autorisations granulaires]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), un moyen plus flexible de gérer l'accès des utilisateurs. Consultez [Migration vers les autorisations granulaires]({{site.baseurl}}/granular_permissions_migration) pour en savoir plus sur le processus de migration, y compris la correspondance entre les autorisations héritées et les autorisations granulaires.

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

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) est une plateforme d'attribution mobile et d'analyse qui vous aide à suivre et analyser vos Campaigns d'acquisition d'utilisateurs.

#### Mailizio - Orchestration des messages - Modèles {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) est une plateforme de création et de gestion d'e-mails qui facilite la conception de contenus réutilisables et conformes à la marque à l'aide d'un éditeur visuel intuitif. Grâce à l'intégration de Mailizio à Braze, vous pouvez exporter vos blocs de contenu et vos modèles d'e-mail, puis générer automatiquement des messages in-app à partir de ces mêmes ressources, permettant un déploiement rapide et entièrement contrôlé des Campaigns.

#### Open Loyalty - Données et analyse - Fidélisation {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) est une plateforme de programmes de fidélisation basée sur le cloud qui vous permet de créer et de gérer des programmes de fidélisation et de récompenses pour vos clients. L'intégration de Braze et d'Open Loyalty synchronise les données de fidélisation — telles que le solde de points, les changements de niveau et les avertissements d'expiration — directement dans Braze en temps réel. Cela vous permet de déclencher des messages personnalisés (e-mail, push, SMS) lorsque le statut de fidélité d'un utilisateur change.

#### OpenAI - Fournisseur de modèles IA {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) crée des modèles d'intelligence artificielle avancés, comme GPT, qui permettent la compréhension et la génération du langage naturel, donnant aux marques les moyens de créer et de faire évoluer des interactions client significatives.

#### Shopgate - Canaux {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) est une plateforme de commerce mobile et omnicanale qui aide les commerçants à créer des applications d'achat et à améliorer l'efficacité des magasins physiques grâce à des outils de traitement des commandes et de clienteling, c'est-à-dire un support client personnalisé en magasin basé sur les données client.

#### Splio - Données et analyse - Importation de cohortes {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) est un outil de construction d'audiences qui vous permet d'augmenter le nombre de Campaigns et le chiffre d'affaires sans nuire à l'expérience client, et fournit des analyses pour suivre les performances des Campaigns CRM en ligne et hors ligne.

### SDK

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_3_5_26_updates.md %}

{% enddetails %}

{% details 5 février 2026 %}

## Publication le 5 février 2026 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### Optimiseur de contenu {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

L'[Optimiseur de contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer) est une étape Canvas de test de contenu continu et à haute variante qui offre une optimisation automatisée de l'engagement. À l'aide d'une interface de type glisser-déposer similaire à l'étape Message, définissez les composants à tester, générez des variantes à l'aide de l'intelligence artificielle (ou saisissez-les manuellement) et utilisez les étiquettes Liquid pour mapper ces composants au contenu de votre message.

Créé à partir d'un optimiseur de bandits multi-bras non contextuel, l'Optimiseur de contenu envoie un seul message par utilisateur, déterminant la combinaison de variantes de composants à fournir sur la base de recommandations prédictives. À mesure que l'étape recueille des données au fil du temps, les variantes performantes augmentent naturellement l'allocation d'envoi tandis que les variantes peu performantes diminuent. L'Optimiseur de contenu fonctionne mieux avec les Canvas à envoi répété qui ont un volume d'utilisateurs quotidien constant (au moins quelques milliers d'utilisateurs par jour) pour permettre une optimisation continue.

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

[Mailizio]({{site.baseurl}}/partners/mailizio) est une plateforme de création et de gestion d'e-mails qui facilite la conception de contenus réutilisables et conformes à la marque à l'aide d'un éditeur visuel intuitif. Grâce à l'intégration de Mailizio à Braze, exportez vos blocs de contenu et vos modèles d'e-mail, puis générez automatiquement des messages in-app à partir de ces mêmes ressources, permettant un déploiement rapide et entièrement contrôlé des Campaigns.

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

L'[événement d'ouverture d'e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) génère désormais la valeur du champ « machine_open » pour établir un rapport sur l'indicateur [_Ouverture machine_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens).

### SDK

Les mises à jour SDK suivantes ont été publiées. La version 14.0.1 du SDK Swift corrige un problème lié à la gestion des liens universels. La version 40.2.0 du SDK Android corrige une fuite de mémoire potentielle et résout un problème lié à l'ouverture de plusieurs sessions en présence d'activités transparentes. Expo SDK v3.2.0 ajoute l'option `forwardUniversalLinks` (par défaut : false) pour configurer la gestion native des liens universels par le SDK Swift.

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_2_5_26_updates.md %}

{% enddetails %}

{% details 8 janvier 2026 %}
## Publication le 8 janvier 2026 {#january-8-2026-release}

### Données et rapports

#### Mises à jour des événements Currents {#updates-to-currents-events}

{% multi_lang_include release_type.md release="General availability" %}

Les changements suivants ont été apportés à Currents dans la version 4 :

{% multi_lang_include releases/currents/2026_1_8_26_field_changes.md %}

Consultez le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) pour connaître les changements d'événements pour chaque version.

#### Exporter les journaux de synchronisation par toutes les lignes {#export-sync-logs-by-all-rows}

{% multi_lang_include release_type.md release="Early access" %}

Dans le [tableau de bord **Sync Log** de l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs#exporting-sync-logs), choisissez d'exporter les journaux au niveau des lignes pour une exécution de synchronisation par :

* **Lignes avec des erreurs :** télécharge un fichier contenant uniquement les lignes ayant un statut **Error**.
* **Toutes les lignes :** télécharge un fichier contenant toutes les lignes traitées au cours de l'exécution.

### Canaux et points de contact

#### Connecteur WhatsApp BYO (Bring Your Own) {#bring-your-own-byo-whatsapp-connector}

Le [connecteur WhatsApp BYO (Bring Your Own)]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) propose un partenariat entre Braze et Infobip, dans le cadre duquel vous donnez à Braze l'accès à votre gestionnaire WhatsApp Business (WABA) d'Infobip. Cela vous permet de gérer et de payer les coûts de messagerie directement avec Infobip tout en utilisant Braze pour la segmentation, la personnalisation et l'orchestration des Campaigns.

#### Bannières dans Canvas

{% multi_lang_include release_type.md release="Early access" %}

Sélectionnez **Banners** comme canal de communication dans une [étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) pour Canvas. Utilisez l'éditeur par glisser-déposer pour créer des messages en ligne personnalisés, offrant des expériences non intrusives et contextuellement pertinentes qui se mettent à jour automatiquement au début de chaque session utilisateur.

#### CCI dynamique {#dynamic-bcc}

{% multi_lang_include release_type.md release="General availability" %}

Avec la [CCI dynamique]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc), utilisez Liquid dans votre adresse CCI. Notez que cette fonctionnalité n'est disponible que dans les **Préférences des e-mails** et ne peut pas être définie dans la Campaign elle-même. Une seule adresse CCI par destinataire d'e-mail est autorisée.

#### Limites de débit basées sur le canal {#channel-based-rate-limits}

Au lieu d'une limite de débit partagée sur l'ensemble d'une Campaign ou d'un Canvas multicanal, sélectionnez une limite de débit spécifique par canal. Dans ce cas, la limite de débit s'appliquera à chacun des canaux sélectionnés. Par exemple, configurez votre Campaign ou Canvas pour envoyer un maximum de 5 000 webhooks et 2 500 messages SMS par minute sur l'ensemble de la Campaign ou du Canvas. Pour plus de détails, consultez [Limitation de débit et limitation de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Partenariats

#### LILT - Localisation {#lilt-localization}

[LILT]({{site.baseurl}}/partners/lilt) est la solution complète d'intelligence artificielle pour la traduction et la création de contenu en entreprise. LILT permet aux organisations mondiales de mettre à l'échelle et d'optimiser leurs opérations de contenu, de produit, de communication et de support, avec des agents d'intelligence artificielle et des flux de travail entièrement automatisés.

### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

{% multi_lang_include releases/sdk/2026_1_8_26_updates.md %}

{% enddetails %}

{% details 9 décembre 2025 %}

## 9 décembre 2025 {#december-9-2025}

### Données et rapports

#### Ajout du Google Tag Manager à une page de destination {#adding-google-tag-manager-to-a-landing-page}

Pour ajouter Google Tag Manager à vos pages de destination, ajoutez un bloc de code personnalisé à votre page de destination dans l'éditeur par glisser-déposer, puis [insérez le code Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page) dans le bloc.

### Orchestration

#### Cas d'usage SMS Liquid {#sms-liquid-use-case}

Le cas d'usage [Répondre avec des messages différents en fonction du mot-clé du SMS entrant]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#sms-keyword-response) intègre le traitement dynamique des mots-clés SMS pour répondre à des messages entrants spécifiques avec un texte de message différent. Par exemple, vous pouvez envoyer des réponses différentes lorsque quelqu'un envoie « START » ou « JOIN ».

#### Liste d'autorisation pour le contenu connecté {#allowlisting-for-connected-content}

Vous pouvez autoriser des URL spécifiques à être utilisées pour le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call). Pour accéder à cette fonctionnalité, contactez votre gestionnaire de la satisfaction client.

### Canaux et points de contact

#### Codage des caractères SMS {#sms-character-encoding}

Notre [calculateur de segments SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) dispose désormais du codage des caractères ! Sélectionnez **Display Character Encoding** pour identifier les caractères codés en GSM-7 ou UCS-2.

![Calculateur de segments SMS avec un exemple de message SMS saisi dans la zone de texte et le codage des caractères activé.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Messages WhatsApp avec optimisation {#whatsapp-messages-with-optimization}

L'API MM pour WhatsApp n'offrant pas une livrabilité à 100 %, il est important de comprendre comment recibler les utilisateurs qui n'ont peut-être pas reçu votre message sur d'autres canaux.

Pour recibler les utilisateurs, nous vous recommandons de créer un segment d'utilisateurs qui n'ont pas reçu un message spécifique. Pour ce faire, filtrez par le code d'erreur `131049`, qui indique qu'un message de modèle marketing n'a pas été envoyé en raison de l'application de la limite de modèles marketing par utilisateur de WhatsApp. Vous pouvez le faire en [utilisant Braze Currents ou les extensions de segments SQL]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels).

### Partenariats

#### OtherLevels - Contenu dynamique {#otherlevels-dynamic-content}

[OtherLevels]({{site.baseurl}}/partners/otherlevels) est une plateforme d'expérience qui utilise l'intelligence artificielle générative pour transformer la façon dont les marques de sport, les éditeurs et les opérateurs se connectent avec leurs clients en transformant le contenu traditionnel en expériences vidéo et rich media personnalisées à l'échelle de la marque.

### SDK

#### Mises à jour majeures du SDK

Les dernières mises à jour du SDK ont été publiées. Les mises à jour majeures sont répertoriées dans la section des mises à jour du SDK ; toutes les autres mises à jour peuvent être consultées dans les journaux des modifications SDK correspondants.

- [SDK Web 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}