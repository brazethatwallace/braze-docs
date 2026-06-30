---
nav_title: Créer une carte de contenu
article_title: Créer une carte de contenu
page_order: 1
description: "Cet article de référence explique comment créer, rédiger, configurer et envoyer des Content Cards à l'aide de Campaigns et de Canvas Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Créer une carte de contenu {#create-a-content-card}

> Cet article explique comment créer une carte de contenu dans Braze lors de la création de Campaigns et de Canvas. Nous vous guiderons dans le choix d'un type de message, la rédaction de votre carte et la planification de la distribution de votre message.

## Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

Utilisez les Campaigns pour des messages simples et ponctuels (par exemple, informer les utilisateurs d'un produit avec un seul message). Utilisez les Canvas pour des parcours utilisateur en plusieurs étapes (par exemple, envoyer des suggestions de produits personnalisées en fonction du comportement de l'utilisateur au fil du temps).

{% tabs %}
{% tab Campaign %}

1. Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **Content Cards** ou, pour les Campaigns ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez à votre Campaign un nom clair et explicite.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) si nécessaire.
   * Les étiquettes facilitent la recherche de vos Campaigns et la création de rapports. Par exemple, avec le [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder), vous pouvez filtrer par les étiquettes pertinentes.
5. Ajoutez et nommez autant de variantes que vous le souhaitez pour votre Campaign. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes. Pour en savoir plus sur les variantes, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si tous les messages de votre Campaign sont similaires ou ont le même contenu, rédigez votre message avant d'ajouter des variantes supplémentaires. Vous pourrez ensuite sélectionner **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape Message dans le générateur de Canvas. Donnez à votre étape un nom clair et explicite.
3. Sélectionnez **Content Cards** comme canal de communication.
4. Choisissez quand Braze évalue l'éligibilité de l'audience et la personnalisation de la Content Card. Cela peut se faire à l'entrée de l'étape ou à la première impression (recommandé). Les étapes contenant des Content Cards peuvent être planifiées ou déclenchées par un événement.
5. Choisissez si les Content Cards doivent être supprimées lorsque les utilisateurs effectuent un achat ou réalisent un événement personnalisé.
6. Définissez une expiration pour la Content Card (durée dans le flux). Cela peut être après une certaine durée ou à un moment précis.
7. Filtrez votre audience, c'est-à-dire les destinataires, pour cette étape si nécessaire dans les **Delivery Settings**. Vous pouvez affiner davantage votre audience en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience sont vérifiées après le délai, au moment de l'envoi des messages.
8. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifier vos types de messages {#step-2-specify-your-message-types}

Sélectionnez l'un des trois types essentiels de Content Cards : **Classic**, **Captioned Image** et **Image Only**.

Pour en savoir plus sur le comportement attendu et l'apparence de chaque type, consultez [Détails créatifs]({{site.baseurl}}/user_guide/channels/content_cards/creative_details), ou consultez les liens dans le tableau suivant. Ces types de Content Cards sont acceptés à la fois par les applications mobiles et les applications web.

| Type de message | Exemple | Description |
|---|---|---|
| [Classique]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#classic) | ![Une Content Card classique avec une petite icône et du texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | La carte classique a une disposition simple avec un titre en gras, un texte de message et une image optionnelle placée à gauche du titre et du texte. Il est préférable d'utiliser une image carrée ou une icône avec la carte classique. |
| [Image légendée]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#captioned-image) | ![Une Content Card avec image légendée montrant un haltérophile et du texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La carte avec image légendée met en valeur votre contenu avec du texte et une image accrocheuse. |
| [Image uniquement]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#banner) | ![Une Content Card Image uniquement avec du texte seulement.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La carte Image uniquement attire l'attention avec un espace dédié aux images, GIF et autres contenus créatifs non textuels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Spécifier vos types de messages" }

## Étape 3 : Rédiger une Content Card {#step-3-compose-a-content-card}

Vous pouvez modifier tous les aspects du contenu et du comportement de votre message dans l'onglet **Compose** de l'éditeur de messages.

![Exemple de détails d'une Content Card dans l'onglet Compose de l'éditeur de messages.]({% image_buster /assets/img/content_card_compose.png %})

Le contenu ici varie en fonction du **type de carte** choisi à l'étape précédente, mais peut inclure l'une des options suivantes :

### Langue {#language}

Sélectionnez **Add Languages** pour ajouter les langues souhaitées à partir de la liste proposée. Cela insère du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte aux emplacements appropriés dans le Liquid. Pour consulter la liste complète des langues disponibles, reportez-vous à [Langues prises en charge]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

![Une fenêtre avec l'anglais, l'espagnol et le français sélectionnés comme langues, et le titre, la description et le texte du lien sélectionnés comme champs à internationaliser.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### Créer des messages de droite à gauche {#create-right-to-left-messages}

L'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les affichent. Pour connaître les bonnes pratiques de création de messages de droite à gauche qui s'affichent le plus fidèlement possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Titre et message {#title-and-message}

Écrivez ce que vous voulez. Il n'y a pas de limites, mais plus vite vous transmettez votre message et incitez votre client à cliquer, mieux c'est ! Nous recommandons des titres et des contenus de message clairs et concis. Notez que ces champs ne sont pas disponibles pour les cartes Image uniquement.

#### Image {#image}

Pour ajouter une image à votre Content Card, vous pouvez sélectionner **Add Image** ou fournir une URL d'image. Sélectionner **Add Image** ouvre la **bibliothèque multimédia**, où vous pouvez choisir une image déjà téléchargée ou en ajouter une nouvelle.

Chaque type de message et chaque plateforme peut avoir ses propres proportions et exigences recommandées. Vérifiez-les avant de commander ou de créer une image. Gardez à l'esprit que les champs de message des Content Cards sont limités à 2&nbsp;Ko au total.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Épingler en haut {#pin-to-top}

Braze affiche une carte épinglée en haut du flux de l'utilisateur, et celui-ci ne peut pas la fermer. Si le flux d'un utilisateur contient plusieurs cartes épinglées, Braze les classe par ordre chronologique. Lorsque Braze distribue une Content Card, elle est soit épinglée, soit non épinglée, et ce statut ne change pas pendant toute la durée de vie de la carte. Si vous modifiez le paramètre d'épinglage d'une Campaign, la mise à jour s'applique uniquement aux cartes envoyées à l'avenir. Elle ne modifie pas le statut d'épinglage des cartes déjà présentes dans le flux d'un utilisateur.

![Aperçu côte à côte de la Content Card dans Braze pour mobile et web avec l'option « Pin this card to the top of the feed » sélectionnée.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportement au clic {#on-click-behavior}

Lorsque votre client clique sur un lien présenté dans la carte, votre lien peut soit le diriger plus profondément dans votre application, soit vers un autre site. Si vous choisissez un comportement au clic pour votre Content Card, pensez à mettre à jour votre **Link Text** en conséquence.

Les actions suivantes sont disponibles pour les liens des Content Cards :

| Action | Description |
|---|---|
| Rediriger vers une URL web | Ouvrir une page web non native. |
| [Lien profond vers l'application]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Créer un lien profond vers un écran existant de votre application. |
| Enregistrer un événement personnalisé | Choisir un [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) à déclencher. Peut être utilisé pour afficher une autre Content Card ou déclencher des messages supplémentaires. |
| Enregistrer un attribut personnalisé | Choisir un [attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) à définir pour l'utilisateur actuel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportement au clic" }

Les options **Enregistrer un événement personnalisé** et **Enregistrer un attribut personnalisé** nécessitent la compatibilité avec les versions de SDK suivantes :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Étape 4 : Configurer des paramètres supplémentaires (facultatif) {#step-4-configure-additional-settings-optional}

Vous pouvez utiliser des [paires clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) pour créer des catégories pour vos cartes, créer [plusieurs flux de Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds) et personnaliser le tri des cartes.

Pour ajouter des paires clé-valeur à votre message, accédez à l'onglet **Settings** et sélectionnez **Add New Pair**.

## Étape 5 : Construire le reste de votre Campaign ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre Campaign. Poursuivez avec les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des Content Cards.

### Choisir une planification de distribution ou un déclencheur {#choose-a-delivery-schedule-or-trigger}

Les Content Cards peuvent être distribuées selon une planification, une action ou un déclencheur API. Pour en savoir plus, consultez [Planifier votre Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Vous pouvez également définir la durée de la Campaign et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours), ainsi que l'expiration de la Content Card. Définissez une date d'expiration spécifique ou le nombre de jours avant l'expiration d'une carte, jusqu'à 30 jours. Toutes les variantes ont des dates d'expiration identiques.

Si vous choisissez de faire expirer une carte après une durée définie (par exemple, après deux semaines), l'expiration est calculée à partir du moment de l'envoi de la carte. Pour les Campaigns planifiées, il s'agit de l'heure de lancement planifiée. Pour les Campaigns déclenchées par un événement, il s'agit du moment où l'utilisateur effectue l'action déclencheuse. Par exemple, si une carte déclenchée par un événement est envoyée à 14 h aujourd'hui avec une expiration d'un jour, elle expire à 14 h le lendemain.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Pour la livraison par événement, un court délai est attendu avant l'apparition de la Content Card. Par exemple, lorsqu'une Campaign est déclenchée au démarrage d'une session, cet événement déclencheur doit d'abord être transmis aux serveurs de Braze. Ensuite, l'éligibilité de l'utilisateur à la Campaign est enregistrée. Lorsque le SDK se synchronise, la carte est créée et renvoyée dans la même réponse de synchronisation. Si la synchronisation du SDK a eu lieu avant l'enregistrement de l'éligibilité de l'utilisateur, celui-ci ne reçoit pas la carte. Pour les utilisateurs en première session, ce délai est inévitable. Pour les utilisateurs existants nécessitant une disponibilité immédiate, envisagez plutôt la distribution planifiée.

#### Distribution planifiée {#scheduled-delivery}

Pour les Campaigns de Content Cards avec distribution planifiée, vous pouvez choisir quand Braze évalue l'éligibilité de l'audience et la personnalisation pour les nouvelles Campaigns de Content Cards en spécifiant le moment de création de la carte. Pour en savoir plus, consultez [Création de carte]({{site.baseurl}}/card_creation).

#### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des segments ou des filtres pour affiner votre audience. Vous obtenez automatiquement un aperçu de la population approximative de ce segment. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

{% multi_lang_include audience/target_audiences.md %}

#### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une Campaign. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la construction du reste de votre Canvas, la mise en œuvre de [tests multivariés]({{site.baseurl}}/user_guide/messaging/ab_testing) et de la [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection), et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la construction de votre Campaign ou Canvas, vérifiez ses détails, [testez-la]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), puis envoyez-la quand vous êtes prêt. Pour plus d'informations, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card).

{% alert warning %}
Une fois qu'une Content Card est lancée, elle ne peut plus être modifiée. Elle peut uniquement être arrêtée pour ne plus être envoyée à de nouveaux utilisateurs et supprimée des flux des utilisateurs. Consultez [Mettre à jour les cartes lancées]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) pour comprendre comment aborder ce scénario.
{% endalert %}

Ensuite, consultez [Rapports sur les Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/reporting) pour découvrir comment accéder aux résultats de vos Campaigns de Content Cards.

## Bon à savoir {#things-to-know}

### Limitations de payload et de flux {#payload-and-feed-limitations}

Pour garantir les performances, les Content Cards ont deux contraintes principales : une limite de taille de payload pour chaque carte et un nombre maximum de cartes pouvant apparaître dans un flux.

#### Limitations de taille des Content Cards {#size-limitations-for-content-cards}

La totalité du payload de données d'une seule Content Card ne peut pas dépasser 2 Ko **après** le rendu de toute personnalisation Liquid. Cela inclut :

* Le titre
* Le message
* L'URL de l'image (la longueur de la chaîne de caractères de l'URL elle-même, pas la taille du fichier image)
* Le texte du lien
* Les URL de lien pour toutes les plateformes spécifiées (des URL distinctes pour iOS, Android et Web comptent toutes dans le total)
* Les paires clé-valeur (les noms des clés et leurs valeurs)

L'utilisation de Liquid pour récupérer de longues chaînes de texte (par exemple, à partir d'attributs personnalisés) peut vous faire dépasser la limite.

Le compositeur de Campaign affiche un avertissement si votre contenu statique dépasse la limite. (Nous ne prédisons pas la taille du contenu dynamique utilisant Liquid.) **Si la taille du message dépasse 2 Ko, il est abandonné au moment de l'envoi.** Vous pouvez voir ces abandons dans le Journal d'activité des messages avec la raison `Content card maximum size exceeded`.

{% alert important %}
Lors des envois de test, les Content Cards dépassant 2 Ko peuvent tout de même être distribuées et affichées correctement.
{% endalert %}

Voici quelques bonnes pratiques pour gérer la taille du payload des Content Cards :

* Utilisez des raccourcisseurs d'URL pour les liens longs. Les URL, en particulier celles avec des paramètres de suivi étendus, peuvent poser des problèmes de limite de taille. L'utilisation d'un service de raccourcissement d'URL peut réduire considérablement le nombre de caractères et libérer de l'espace dans le payload.
* Tronquez le contenu dynamique avec Liquid. Lorsque vous personnalisez des cartes avec du texte dynamique provenant d'attributs utilisateur ou d'appels API, la longueur du contenu peut être imprévisible. Utilisez de manière proactive des filtres Liquid comme `truncate` pour limiter la longueur de tout texte dynamique.
* Soyez efficace avec les URL multi-plateformes. La limite de 2 Ko inclut les URL de toutes les plateformes que vous définissez. L'utilisation d'URL longues et uniques pour chaque plateforme peut multiplier la taille du payload. Si possible, utilisez un lien unique fonctionnant sur toutes les plateformes, ou utilisez des raccourcisseurs d'URL si nécessaire.
* Envisagez les bannières pour du contenu plus riche. Pour les cas d'utilisation nécessitant régulièrement de grandes quantités de contenu, les Content Cards ne sont peut-être pas le canal approprié. Les bannières n'ont pas la même limitation de payload de 2 Ko et sont mieux adaptées pour intégrer du contenu plus riche directement dans une application ou une expérience web.

#### Nombre de cartes dans le flux {#number-of-cards-in-feed}

Chaque utilisateur peut avoir jusqu'à 250 Content Cards non expirées dans son flux à tout moment. Lorsque cette limite est dépassée, Braze cesse de renvoyer les cartes les plus anciennes, même si elles n'ont pas été lues. Les cartes fermées comptent également dans cette limite, ce qui signifie qu'un grand nombre de cartes fermées peut réduire l'espace disponible pour les plus anciennes.

Pour éviter les problèmes liés à la limite de cartes, nous recommandons les bonnes pratiques suivantes :

- **Utilisez des dates d'expiration plus courtes :** pour les Campaigns sensibles au temps (comme une vente de week-end), définissez une date d'expiration spécifique. Ainsi, les cartes sont automatiquement supprimées du flux et ne comptent plus dans la limite une fois qu'elles ne sont plus pertinentes.
- **Exploitez la suppression basée sur les actions :** configurez des événements de suppression pour les cartes transactionnelles ou basées sur des objectifs. Par exemple, une carte invitant un utilisateur à compléter son profil devrait être supprimée dès qu'un événement `profile_completed` est enregistré.
- **Auditez les Campaigns de longue durée :** passez en revue les Campaigns récurrentes ou en cours pour vous assurer qu'elles ne dégradent pas l'expérience de vos utilisateurs en remplissant le flux avec trop de cartes au fil du temps.

### Comprendre la rééligibilité pour les Content Cards {#understanding-re-eligibility-for-content-cards}

La rééligibilité détermine si et quand un utilisateur peut recevoir un message de la même Campaign plus d'une fois. Pour les Content Cards, comprendre ce fonctionnement est essentiel pour gérer les Campaigns récurrentes et s'assurer que les utilisateurs ne reçoivent pas de messages en double ou obsolètes.

{% alert tip %}
Vous souhaitez que votre contenu dure plus de 30 jours ? Essayez les [bannières]({{site.baseurl}}/user_guide/channels/banners).
{% endalert %}

#### Comment la rééligibilité est calculée {#how-re-eligibility-is-calculated}

Si vous activez la rééligibilité, le compte à rebours pour qu'un utilisateur puisse « réintégrer » une Campaign commence après l'envoi du message. Le moment précis où ce compte à rebours démarre dépend de vos paramètres de création de carte :

- Les Content Cards utilisant [la première impression]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) utilisent le moment de l'impression pour calculer la rééligibilité.
- Les Content Cards créées au lancement de la Campaign, dans les Campaigns multicanaux ou à l'entrée de l'étape du Canvas utilisent le moment d'envoi ou d'impression le plus récent.

#### L'expiration de 30 jours et la rééligibilité {#the-30-day-expiration-and-re-eligibility}

Une source fréquente de confusion est l'interaction entre la rééligibilité de Campaign et l'expiration automatique de 30 jours de toutes les Content Cards.

Toutes les Content Cards sont automatiquement purgées des systèmes de Braze 30 jours après leur envoi ou leur suppression. Si vous avez une Campaign récurrente de longue durée avec la rééligibilité **désactivée**, un utilisateur peut tout de même recevoir la même carte après 30 jours. Lorsque la carte originale est purgée, le système ne voit plus de trace de la réception de cette Campaign par l'utilisateur, ce qui le rend à nouveau éligible lors de sa prochaine session.

Pour que les utilisateurs ne reçoivent un message d'une Campaign spécifique qu'une seule fois, ajoutez un filtre d'audience à votre Campaign ou étape du Canvas pour les utilisateurs qui n'ont pas reçu de message de cette Campaign. Ce filtre est le moyen le plus fiable d'éviter les envois en double pour les Campaigns de longue durée.

### Gérer les Content Cards en production {#managing-live-content-cards}

Après leur envoi, les Content Cards restent en attente dans une « boîte de réception » prêtes à être distribuées à l'utilisateur (similaire à ce qui se passe pour les e-mails). Une fois que le contenu est chargé dans la Content Card (au moment de l'affichage), il ne peut plus être modifié pendant sa durée de vie. Cela s'applique même si vous appelez une API via du contenu connecté et que les données de l'endpoint changent. Ces données ne seront pas mises à jour. La carte peut uniquement être arrêtée pour ne plus être envoyée à de nouveaux utilisateurs et supprimée des flux des utilisateurs. Si vous modifiez une Campaign, seules les futures cartes envoyées contiendront la mise à jour.

#### Mettre à jour les cartes lancées {#updating-launched-cards}

Pour modifier une carte pour les utilisateurs qui l'ont déjà reçue, vous devez utiliser l'une des méthodes suivantes :

##### Option 1 : Dupliquer la Campaign (recommandé pour les modifications immédiates) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
Nous recommandons cette option pour les messages où vous affichez le contenu le plus récent dans la carte, où les modifications doivent être visibles immédiatement, ou lorsque la rééligibilité est désactivée.
{% endalert %}

La première approche consiste à archiver la Campaign et à lancer une nouvelle Campaign dupliquée :

1. Arrêtez la Campaign originale et, lorsque vous y êtes invité, sélectionnez `Remove card after the next sync`.
2. Dupliquez la Campaign, effectuez vos modifications et lancez la nouvelle version.

Lorsque vous dupliquez la Campaign, vous devez définir l'audience pour la nouvelle version. Utilisez des filtres de segmentation pour contrôler qui reçoit la carte mise à jour :
* Si les utilisateurs ne doivent jamais être rééligibles pour une Content Card, vous pouvez filtrer les utilisateurs qui n'ont pas reçu la version précédente de la Content Card en définissant le filtre `Received Message from Campaign` avec la condition `Has Not`.
* Si les utilisateurs ayant reçu la carte précédente doivent être rééligibles dans X jours, vous pouvez définir le filtre `Last Received Message from specific campaign` à plus de X jours **OU** `Received Message from Campaign` avec la condition `Has Not`.

###### Impact {#impact}

* **Destinataires existants :** les nouveaux destinataires et les destinataires existants verraient la carte mise à jour lors du prochain rafraîchissement du flux s'ils sont éligibles.
* **Rapports :** chaque version de la carte aurait des analyses séparées.

Imaginons que vous avez configuré une Campaign déclenchée au démarrage d'une session, avec une rééligibilité fixée à 30 jours. Un utilisateur a reçu la Campaign il y a deux jours, et vous souhaitez modifier le texte. Premièrement, archivez la Campaign et supprimez les cartes du flux. Deuxièmement, dupliquez la Campaign et relancez-la avec le nouveau texte. Si l'utilisateur ouvre une nouvelle session, il recevra immédiatement la nouvelle carte.

##### Option 2 : Arrêter et relancer la même Campaign {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
Nous recommandons cette option pour les messages uniques dans un centre de notifications ou une boîte de réception de messages (comme les promotions), lorsqu'il est important que les analyses soient unifiées, ou lorsque l'urgence du message n'est pas un critère (les destinataires existants peuvent attendre la fenêtre d'éligibilité avant de voir les cartes mises à jour).
{% endalert %}

Cette approche maintient toutes vos analyses unifiées dans une seule Campaign. Les utilisateurs nouvellement éligibles reçoivent la nouvelle carte, mais la mise à jour est retardée pour les destinataires existants jusqu'à ce qu'ils soient rééligibles :

1. Arrêtez votre Campaign et, lorsque vous y êtes invité, sélectionnez **Remove card after the next sync**.
2. Modifiez votre Campaign selon vos besoins.
3. Redémarrez votre Campaign.

###### Impact

* **Destinataires existants :** les utilisateurs ayant déjà reçu la carte ne recevraient pas les cartes mises à jour tant qu'ils ne seraient pas rééligibles. Si la rééligibilité est désactivée, ils ne recevraient jamais la nouvelle carte.
* **Rapports :** une seule Campaign contient toutes les analyses de rapports pour les versions de cartes lancées. Braze ne différencie pas les versions lancées.

Imaginons que vous avez une Campaign déclenchée au démarrage d'une session avec une rééligibilité fixée à 30 jours. Un utilisateur a reçu la Campaign il y a deux jours, et vous souhaitez modifier le texte. Premièrement, arrêtez la Campaign et supprimez la carte du flux. Deuxièmement, republiez la Campaign avec le nouveau texte. Si l'utilisateur ouvre une nouvelle session, il recevra la nouvelle carte dans 28 jours.

#### Supprimer et faire expirer les cartes {#removing-and-expiring-cards}

##### Suppression manuelle des cartes {#manual-card-removal}

Vous pouvez supprimer manuellement les cartes des flux de tous les utilisateurs à tout moment en arrêtant la Campaign.

1. Ouvrez la Campaign de Content Cards et sélectionnez **Arrêter la Campaign**.
2. Lorsque vous y êtes invité, sélectionnez **Remove card after the next sync**. La carte est supprimée lors du prochain rafraîchissement du flux.

##### Suppression automatique des cartes {#action-based-card-removal}

Vous pouvez supprimer automatiquement une carte lorsqu'un utilisateur effectue une action spécifique, comme finaliser un achat ou activer une fonctionnalité.

Dans votre Campaign ou étape du Canvas, spécifiez un événement de suppression. Lorsqu'un utilisateur effectue cet événement, la carte est supprimée de son flux lors d'un rafraîchissement ultérieur après que Braze a traité l'événement.

{% alert note %}
Cette suppression n'est pas instantanée. Il y a un délai de traitement, et il peut s'écouler plusieurs minutes et plus d'un rafraîchissement du flux avant que la carte ne disparaisse.
{% endalert %}

{% alert tip %}
Vous pouvez spécifier plusieurs événements personnalisés et achats qui doivent supprimer une carte du flux d'un utilisateur. Lorsque **l'une** de ces actions est effectuée par l'utilisateur, toutes les cartes existantes envoyées par la Campaign sont supprimées. Toutes les futures cartes éligibles continuent d'être envoyées selon la planification du message.
{% endalert %}

![Panneau des conditions de suppression de Content Card avec l'option Événement de suppression de Content Card.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiration des cartes {#card-expiration}

Les Content Cards restent disponibles jusqu'à 30 jours après leur envoi ; après 30 jours, Braze les supprime des flux des utilisateurs et les purge de ses systèmes.

#### Faire durer les cartes plus de 30 jours {#making-cards-last-longer-than-30-days}

{% alert tip %}
Pour les cas d'utilisation nécessitant que les messages persistent au-delà de la limite de 30 jours des Content Cards, envisagez d'utiliser les bannières. Les bannières sont conçues pour la persistance et n'ont pas de date d'expiration obligatoire, ce qui leur permet de rester visibles aussi longtemps que nécessaire.
{% endalert %}

Si vous souhaitez qu'une carte semble toujours disponible, vous pouvez créer une Campaign récurrente qui remplace effectivement la carte tous les 30 jours :

1. Définissez la durée de la Content Card à 30 jours.
2. Définissez la rééligibilité de la Campaign à 30 jours.
3. Configurez la Campaign pour se déclencher au « démarrage de session ».

### Synchronisation et rafraîchissement des Content Cards {#content-card-sync-and-refresh}

Les Content Cards se synchronisent selon un calendrier et lorsque votre application rafraîchit le flux. Le comportement de synchronisation diffère entre les synchronisations complètes et partielles, et votre intégration SDK affecte le moment où les cartes se rafraîchissent au démarrage de la session. Pour les détails d'implémentation, consultez [Personnaliser le flux de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) et [Créer des Content Cards]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

### Impact de l'arrêt des Campaigns de Content Cards {#impact-of-stopping-content-cards-campaigns}

Lorsque vous arrêtez une Campaign et sélectionnez **Remove card after the next sync**, Braze supprime la carte des flux des utilisateurs lors du prochain rafraîchissement. Le nombre d'impressions peut être inférieur au nombre d'envois, car les utilisateurs ne peuvent pas voir les cartes supprimées avant qu'ils ne les consultent.