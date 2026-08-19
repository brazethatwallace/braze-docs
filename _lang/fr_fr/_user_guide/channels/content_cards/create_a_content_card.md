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

Utilisez les campagnes pour des communications simples et ponctuelles (comme informer les utilisateurs d'un produit avec un seul message). Utilisez les Canvas pour des parcours utilisateur en plusieurs étapes (comme l'envoi de suggestions de produits personnalisées en fonction du comportement des utilisateurs au fil du temps).

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **Content Cards** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) si nécessaire.
   * Les tags facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder), vous pouvez filtrer par les tags pertinents.
5. Ajoutez et nommez autant de variantes que vous le souhaitez pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour en savoir plus sur les variantes, consultez [Test multivarié et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite sélectionner **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) à l'aide du compositeur Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape Message dans le générateur Canvas. Donnez à votre étape un nom clair et significatif.
3. Sélectionnez **Content Cards** comme canal de communication.
4. Choisissez quand Braze calcule l'éligibilité de l'audience et la personnalisation pour la Content Card. Cela peut être à l'entrée dans l'étape ou à la première impression (recommandé). Les étapes contenant des Content Cards peuvent être planifiées ou basées sur une action.
5. Choisissez si vous souhaitez supprimer les Content Cards lorsque les utilisateurs effectuent un achat ou réalisent un événement personnalisé.
6. Définissez une expiration pour la Content Card (durée dans le flux). Cela peut être après une certaine durée ou à un moment précis.
7. Filtrez votre audience, ou les destinataires, pour cette étape si nécessaire dans les **Delivery Settings**. Vous pouvez affiner davantage votre audience en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience sont vérifiées après le délai, au moment de l'envoi des messages.
8. Choisissez tout autre canal de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifier vos types de messages {#step-2-specify-your-message-types}

Sélectionnez l'un des trois types essentiels de Content Cards : **Classique**, **Image légendée** et **Image uniquement**.

Pour en savoir plus sur le comportement attendu et l'apparence de chaque type, consultez les [Détails créatifs]({{site.baseurl}}/user_guide/channels/content_cards/creative_details), ou consultez les liens dans le tableau suivant. Ces types de Content Cards sont acceptés à la fois par les applications mobiles et les applications web.

| Type de message | Exemple | Description |
|---|---|---|
| [Classique]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Une Content Card classique avec une petite icône et du texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | La carte classique présente une mise en page simple avec un titre en gras, un texte de message et une image optionnelle placée au début du titre et du texte. Il est préférable d'utiliser une image carrée ou une icône avec la carte classique. |
| [Image légendée]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Une Content Card de type image légendée avec une image d'un haltérophile et du texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La carte image légendée met en valeur votre contenu avec du texte et une image accrocheuse. |
| [Image uniquement]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Une Content Card de type image uniquement avec du texte seulement.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La carte image uniquement attire l'attention avec un espace dédié aux images, GIF et autres contenus créatifs non textuels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Spécifier vos types de messages" }

## Étape 3 : Composer une Content Card {#step-3-compose-a-content-card}

Vous pouvez modifier tous les aspects du contenu et du comportement de votre message dans l'onglet **Compose** de l'éditeur de messages.

![Exemple de détails d'une Content Card dans l'onglet Compose de l'éditeur de messages.]({% image_buster /assets/img/content_card_compose.png %})

Le contenu ici varie en fonction du **type de carte** choisi à l'étape précédente, mais peut inclure l'une des options suivantes :

### Langue {#language}

Sélectionnez **Add Languages** pour ajouter les langues souhaitées à partir de la liste fournie. Cela insère du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte aux emplacements appropriés dans le Liquid. Pour consulter notre liste complète des langues disponibles, voir [Langues prises en charge]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

![Une fenêtre avec l'anglais, l'espagnol et le français sélectionnés pour les langues, et le titre, la description et le texte du lien sélectionnés pour les champs à internationaliser.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### Créer des messages de droite à gauche {#create-right-to-left-messages}

L'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les affichent. Pour connaître les bonnes pratiques de création de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Titre et message {#title-and-message}

Rédigez ce que vous souhaitez. Il n'y a pas de limites, mais plus vite vous transmettez votre message et incitez votre client à cliquer, mieux c'est ! Nous recommandons des titres et un contenu de message clairs et concis. Notez que ces champs ne sont pas fournis pour les cartes de type Image uniquement.

#### Image {#image}

Pour ajouter une image à votre Content Card, vous pouvez sélectionner **Add Image** ou fournir une URL d'image. Sélectionner **Add Image** ouvre la **bibliothèque multimédia**, où vous pouvez choisir une image précédemment téléchargée ou en ajouter une nouvelle.

Chaque type de message et chaque plateforme peut avoir ses propres proportions et exigences suggérées, alors assurez-vous de vérifier ces informations avant de commander ou de créer une image à partir de zéro. Gardez à l'esprit que les champs de message des Content Cards sont limités à 2&nbsp;Ko au total.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Épingler en haut {#pin-to-top}

Braze affiche une carte épinglée en haut du flux d'un utilisateur et celui-ci ne peut pas la rejeter. Si le flux d'un utilisateur contient plusieurs cartes épinglées, Braze les classe par ordre chronologique. Lorsque Braze distribue une Content Card, elle est soit épinglée, soit non épinglée, et ce statut ne change pas pendant toute la durée de vie de la carte. Si vous modifiez le paramètre d'épinglage d'une campagne, la mise à jour s'applique uniquement aux cartes envoyées après la modification. Elle ne modifie pas le statut d'épinglage des cartes déjà présentes dans le flux d'un utilisateur.

![Aperçu côte à côte de la Content Card dans Braze pour mobile et web avec l'option « Épingler cette carte en haut du flux » sélectionnée.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportement au clic {#on-click-behavior}

Lorsque votre client clique sur un lien présenté dans la carte, votre lien peut soit le diriger plus profondément dans votre application, soit vers un autre site. Si vous choisissez un comportement au clic pour votre Content Card, n'oubliez pas de mettre à jour votre **texte du lien** en conséquence.

Les actions suivantes sont disponibles pour les liens des Content Cards :

| Action | Description |
|---|---|
| Rediriger vers une URL web | Ouvrir une page web non native. |
| [Deep link dans l'application]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Créer un deep link vers un écran existant de votre application. |
| Enregistrer un événement personnalisé | Choisir un [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) à déclencher. Peut être utilisé pour afficher une autre Content Card ou déclencher des messages supplémentaires. |
| Enregistrer un attribut personnalisé | Choisir un [attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) à définir pour l'utilisateur actuel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportement au clic" }

Les options **Enregistrer un événement personnalisé** et **Enregistrer un attribut personnalisé** nécessitent la compatibilité avec les versions suivantes du SDK :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Étape 4 : Configurer les paramètres supplémentaires (facultatif) {#step-4-configure-additional-settings-optional}

Vous pouvez utiliser des [paires clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) pour créer des catégories pour vos cartes, créer [plusieurs flux de Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds) et personnaliser la façon dont les cartes sont triées.

Pour ajouter des paires clé-valeur à votre message, accédez à l'onglet **Settings** et sélectionnez **Add New Pair**.

## Étape 5 : Construire le reste de votre campagne ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre campagne. Poursuivez avec les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des Content Cards.

### Choisir un calendrier de livraison ou un déclencheur {#choose-a-delivery-schedule-or-trigger}

Les Content Cards peuvent être envoyées selon un horaire planifié, une action ou un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours), ainsi que déterminer l'expiration de la Content Card. Définissez une date d'expiration spécifique ou le nombre de jours avant l'expiration d'une carte, jusqu'à 30 jours. Toutes les variantes doivent utiliser la même expiration (durée ou heure spécifique).

Le compte à rebours de l'expiration commence à partir de l'heure d'envoi de la carte :

- **Campagnes planifiées :** Le compte à rebours commence à l'heure de lancement planifiée.
- **Campagnes par événement :** Le compte à rebours commence lorsque l'utilisateur effectue l'action déclencheuse.

Par exemple, si une Content Card par événement est envoyée à 14 h aujourd'hui avec une expiration d'un jour, elle expire à 14 h le lendemain.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Pour la livraison par événement, il y a un court délai attendu avant que la Content Card n'apparaisse. Pour en savoir plus sur les raisons de ce délai et comment le minimiser, consultez [Pourquoi les Content Cards n'apparaissent-elles pas immédiatement après un événement déclencheur ?]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event).

#### Livraison planifiée {#scheduled-delivery}

Pour les campagnes de Content Cards avec livraison planifiée, vous pouvez choisir le moment où Braze évalue l'éligibilité de l'audience et la personnalisation pour les nouvelles campagnes de Content Cards en spécifiant quand la carte est créée. Pour en savoir plus, consultez [Création de carte]({{site.baseurl}}/card_creation).

#### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative de ce segment. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

{% multi_lang_include audience/target_audiences.md %}

#### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, mettre en œuvre les [tests multivariés]({{site.baseurl}}/user_guide/messaging/ab_testing) et la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection), et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la création de votre campagne ou de votre Canvas, vérifiez ses détails, [testez-la]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), puis envoyez-la. Pour plus d'informations, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card).

{% alert note %}
Bien que les Content Cards ne nécessitent pas de notifications push en production, les envois de test requièrent que les notifications push soient activées sur vos appareils de test, car la carte est transmise dans le payload push. Les Content Cards de test expirent environ cinq minutes après leur envoi.
{% endalert %}

{% alert warning %}
Une fois qu'une Content Card est lancée, elle ne peut plus être modifiée. Elle peut uniquement être retirée de l'envoi aux nouveaux utilisateurs et supprimée des flux des utilisateurs. Consultez [Mettre à jour les cartes envoyées]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) pour comprendre comment aborder ce scénario.
{% endalert %}

Consultez ensuite les [rapports sur les Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/reporting) pour découvrir comment accéder aux résultats de vos campagnes de Content Cards.

## Ce qu'il faut savoir {#things-to-know}

### Limitations de payload et de flux {#payload-and-feed-limitations}

Pour garantir les performances, les Content Cards sont soumises à deux contraintes principales : une limite de taille du payload pour chaque carte et un nombre maximum de cartes pouvant apparaître dans un flux.

#### Limitations de taille des Content Cards {#size-limitations-for-content-cards}

Le payload total d'une seule Content Card ne peut pas dépasser 2 Ko **après** le rendu de toute personnalisation Liquid. Cela inclut :

* Le titre
* Le message
* L'URL de l'image (la longueur de la chaîne de l'URL elle-même, pas la taille du fichier image)
* Le texte du lien
* Les URL de lien pour toutes les plateformes spécifiées (les URL distinctes pour iOS, Android et Web comptent toutes dans le total)
* Les paires clé-valeur (les noms des clés et leurs valeurs)

L'utilisation de Liquid pour récupérer de longues chaînes de texte (par exemple à partir d'attributs personnalisés) peut vous amener à dépasser la limite.

Le compositeur de campagne affiche un avertissement si votre contenu statique dépasse la limite. La taille du contenu dynamique utilisant Liquid n'est pas prédite. Si la taille du message dépasse 2 Ko, il est abandonné au moment de l'envoi. Vous pouvez voir ces abandons dans le journal d'activité des messages avec la raison `Content card maximum size exceeded`.

{% alert important %}
Lors des envois de test, les Content Cards dépassant 2 Ko peuvent tout de même être livrées et affichées correctement.
{% endalert %}

Voici quelques bonnes pratiques pour gérer la taille du payload des Content Cards :

* Utilisez des raccourcisseurs d'URL pour les liens longs. Les URL, en particulier celles comportant de nombreux paramètres de suivi, peuvent poser des problèmes de limite de taille. L'utilisation d'un service de raccourcissement d'URL peut réduire considérablement le nombre de caractères et libérer de l'espace dans le payload.
* Tronquez le contenu dynamique avec Liquid. Lorsque vous personnalisez des cartes avec du texte dynamique provenant d'attributs utilisateur ou d'appels API, la longueur du contenu peut être imprévisible. Utilisez de manière proactive des filtres Liquid comme `truncate` pour limiter la longueur de tout texte dynamique.
* Soyez efficace avec les URL multi-plateformes. La limite de 2 Ko inclut les URL de toutes les plateformes que vous définissez. L'utilisation d'URL longues et uniques pour chaque plateforme peut multiplier la taille du payload. Si possible, utilisez un lien unique fonctionnant sur toutes les plateformes, ou utilisez des raccourcisseurs d'URL si nécessaire.
* Envisagez les Banners pour du contenu plus riche. Pour les cas d'usage nécessitant systématiquement de grandes quantités de contenu, les Content Cards ne sont peut-être pas le bon canal. Les Banners n'ont pas la même limitation de payload de 2 Ko et sont mieux adaptés pour intégrer du contenu plus riche directement dans une application ou une expérience web.

#### Nombre de cartes dans le flux {#number-of-cards-in-feed}

Chaque utilisateur peut avoir jusqu'à 250 Content Cards non expirées dans son flux à tout moment. Lorsque cette limite est dépassée, Braze cesse de renvoyer les cartes les plus anciennes, même si elles n'ont pas été lues. Les cartes rejetées comptent également dans cette limite, ce qui signifie qu'un nombre élevé de cartes rejetées peut réduire l'espace disponible pour les plus anciennes.

Pour éviter les problèmes liés à la limite de cartes, nous recommandons les bonnes pratiques suivantes :

- **Utilisez des dates d'expiration plus courtes :** pour les Campaigns sensibles au temps (comme une vente de fin de semaine), définissez une date d'expiration spécifique. Ainsi, les cartes sont automatiquement retirées du flux et ne comptent plus dans la limite une fois qu'elles ne sont plus pertinentes.
- **Tirez parti de la suppression par événement :** configurez des événements de suppression pour les cartes transactionnelles ou basées sur des objectifs. Par exemple, une carte invitant un utilisateur à compléter son profil devrait être supprimée dès qu'un événement `profile_completed` est enregistré.
- **Auditez les Campaigns de longue durée :** passez en revue les Campaigns récurrentes ou en cours pour vous assurer qu'elles ne créent pas une mauvaise expérience pour vos utilisateurs en remplissant le flux avec trop de cartes au fil du temps.

### Comprendre la rééligibilité pour les Content Cards {#understanding-re-eligibility-for-content-cards}

La rééligibilité détermine si et quand un utilisateur peut recevoir un message de la même Campaign plus d'une fois. Pour les Content Cards, comprendre ce fonctionnement est essentiel pour gérer les Campaigns récurrentes et s'assurer que les utilisateurs ne reçoivent pas de messages en double ou obsolètes.

{% alert tip %}
Vous souhaitez que votre contenu dure plus de 30 jours ? Essayez les [Banners]({{site.baseurl}}/user_guide/channels/banners).
{% endalert %}

#### Comment la rééligibilité est calculée {#how-re-eligibility-is-calculated}

Si vous activez la rééligibilité, le compte à rebours pour qu'un utilisateur puisse « réintégrer » une Campaign commence après l'envoi du message. Le moment précis où ce compte à rebours démarre dépend de vos paramètres de création de carte :

- Les Content Cards utilisant [à la première impression]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) utilisent le moment de l'impression pour calculer la rééligibilité.
- Les Content Cards créées au lancement de la Campaign, dans les Campaigns multicanales ou à l'entrée dans l'étape du Canvas utilisent le moment d'envoi ou d'impression le plus récent.

#### L'expiration de 30 jours et la rééligibilité {#the-30-day-expiration-and-re-eligibility}

Une source fréquente de confusion est l'interaction entre la rééligibilité de la Campaign et l'expiration automatique de 30 jours de toutes les Content Cards.

Toutes les Content Cards sont automatiquement purgées des systèmes de Braze 30 jours après leur envoi ou leur suppression. Si vous avez une Campaign récurrente de longue durée avec la rééligibilité **désactivée**, un utilisateur peut tout de même recevoir la même carte après 30 jours. Lorsque la carte originale est purgée, le système ne voit plus de trace indiquant que cet utilisateur a reçu la Campaign, ce qui le rend à nouveau éligible lors de sa prochaine session.

Pour que les utilisateurs ne reçoivent un message d'une Campaign spécifique qu'une seule fois, ajoutez un filtre d'audience à votre Campaign ou étape du Canvas pour les utilisateurs qui n'ont pas reçu de message de cette Campaign. Ce filtre est le moyen le plus fiable d'empêcher les envois en double des Campaigns de longue durée.

### Gérer les Content Cards en direct {#managing-live-content-cards}

Après l'envoi des Content Cards, elles restent en attente dans une « boîte de réception » prêtes à être livrées à l'utilisateur (de manière similaire à ce qui se passe pour les e-mails). Une fois que le contenu est intégré dans la Content Card (au moment de l'affichage), il ne peut plus être modifié pendant sa durée de vie. Cela s'applique même si vous appelez une API via le contenu connecté et que les données de l'endpoint changent. Ces données ne sont pas mises à jour. L'envoi peut uniquement être arrêté pour les nouveaux utilisateurs et les cartes peuvent être retirées des flux des utilisateurs. Si vous modifiez une Campaign, seules les cartes envoyées après la modification incluent la mise à jour.

#### Mettre à jour les cartes lancées {#updating-launched-cards}

Pour modifier une carte pour les utilisateurs qui l'ont déjà reçue, vous devez utiliser l'une des méthodes suivantes :

##### Option 1 : Dupliquer la Campaign (recommandé pour les modifications immédiates) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
Nous recommandons cette option pour les messages où vous affichez le contenu le plus récent dans la carte, où les modifications doivent être visibles immédiatement, ou lorsque la rééligibilité est désactivée.
{% endalert %}

La première approche consiste à archiver la Campaign et à lancer une nouvelle Campaign dupliquée :

1. Arrêtez la Campaign d'origine et, lorsque vous y êtes invité, sélectionnez `Remove card after the next sync`.
2. Dupliquez la Campaign, effectuez vos modifications et lancez la nouvelle version.

Lorsque vous dupliquez la Campaign, vous devez définir l'audience pour la nouvelle version. Utilisez les filtres de segmentation pour contrôler qui reçoit la carte mise à jour :
* Si les utilisateurs ne doivent jamais être rééligibles pour une Content Card, vous pouvez filtrer les utilisateurs qui n'ont pas reçu la version précédente de la Content Card en définissant le filtre `Received Message from Campaign` sur la condition `Has Not`.
* Si les utilisateurs ayant reçu la carte précédente doivent être rééligibles dans X jours, vous pouvez définir le filtre `Last Received Message from specific campaign` à plus de X jours **OU** `Received Message from Campaign` avec la condition `Has Not`.

###### Impact {#impact}

- **Destinataires existants :** les nouveaux destinataires et les destinataires existants voient la carte mise à jour lors de la prochaine actualisation du flux s'ils sont éligibles.
- **Reporting :** chaque version de la carte dispose d'analyses séparées.

Supposons que vous ayez configuré une Campaign déclenchée par le démarrage d'une session, avec une rééligibilité fixée à 30 jours. Un utilisateur a reçu la Campaign il y a deux jours et vous souhaitez modifier le texte. Commencez par archiver la Campaign et supprimer les cartes du flux. Ensuite, dupliquez la Campaign et relancez-la avec le nouveau texte. Si l'utilisateur a une autre session, il reçoit immédiatement la nouvelle carte.

##### Option 2 : Arrêter et relancer la même Campaign {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
Nous recommandons cette option pour les messages uniques dans un centre de notifications ou une boîte de réception de messages (comme les promotions), lorsqu'il est important que les analyses soient unifiées, ou lorsque l'urgence du message n'est pas un critère (par exemple, les destinataires existants peuvent attendre la fenêtre d'éligibilité avant de voir les cartes mises à jour).
{% endalert %}

Cette approche conserve toutes vos analyses unifiées dans une seule Campaign. Les utilisateurs nouvellement éligibles reçoivent la nouvelle carte, mais la mise à jour est retardée pour les destinataires existants jusqu'à ce qu'ils soient rééligibles :

1. Arrêtez votre Campaign et, lorsque vous y êtes invité, sélectionnez **Remove card after the next sync**.
2. Modifiez votre Campaign selon vos besoins.
3. Redémarrez votre Campaign.

###### Impact

* **Destinataires existants :** les utilisateurs qui ont déjà reçu la carte ne reçoivent pas les cartes mises à jour tant qu'ils ne sont pas rééligibles. Si la rééligibilité est désactivée, ils ne reçoivent jamais la nouvelle carte.
* **Reporting :** une seule Campaign contient toutes les analyses de reporting pour les versions de cartes lancées. Braze ne différencie pas les versions lancées.

Supposons que vous ayez une Campaign déclenchée par le démarrage d'une session avec une rééligibilité fixée à 30 jours. Un utilisateur a reçu la Campaign il y a deux jours et vous souhaitez modifier le texte. Commencez par arrêter la Campaign et supprimer la carte du flux. Ensuite, republiez la Campaign avec le nouveau texte. Si l'utilisateur a une autre session, il reçoit la nouvelle carte dans 28 jours.

{% alert note %}
Si vous arrêtez une Campaign, modifiez les paramètres d'événement de suppression et redémarrez la Campaign sans supprimer les cartes du flux, toutes les cartes existantes dans les flux des utilisateurs utilisent les paramètres d'événement de suppression mis à jour. Les cartes ne conservent pas la configuration d'événement de suppression d'origine du moment où elles ont été envoyées.
{% endalert %}

#### Supprimer et faire expirer les cartes {#removing-and-expiring-cards}

##### Suppression manuelle des cartes {#manual-card-removal}

Vous pouvez supprimer manuellement les cartes des flux de tous les utilisateurs à tout moment en arrêtant la Campaign.

1. Ouvrez la Campaign de Content Card et sélectionnez Stop Campaign.
2. Lorsque vous y êtes invité, sélectionnez **Remove card after the next sync**. La carte est supprimée lors de la prochaine actualisation du flux.

##### Suppression automatique des cartes {#action-based-card-removal}

Vous pouvez supprimer automatiquement une carte lorsqu'un utilisateur effectue une action spécifique, comme finaliser un achat ou activer une fonctionnalité.

Dans votre Campaign ou étape du Canvas, spécifiez un événement de suppression. Lorsqu'un utilisateur effectue cet événement, la carte est supprimée de son flux lors d'une actualisation ultérieure après que Braze a traité l'événement.

{% alert note %}
Cette suppression n'est pas instantanée. Il y a un délai de traitement, il peut donc s'écouler plusieurs minutes et plus d'une actualisation du flux avant que la carte ne disparaisse.
{% endalert %}

{% alert tip %}
Vous pouvez spécifier plusieurs événements personnalisés et achats qui doivent supprimer une carte du flux d'un utilisateur. Lorsque l'une de ces actions est effectuée par l'utilisateur, toutes les cartes existantes envoyées par les cartes de la Campaign sont supprimées. Les cartes éligibles continuent d'être envoyées selon la planification du message.
{% endalert %}

![Panneau des conditions de suppression de Content Card avec l'option d'événement de suppression de Content Card.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiration des cartes {#card-expiration}

Les Content Cards restent disponibles jusqu'à 30 jours après leur envoi ; après 30 jours, Braze les supprime des flux des utilisateurs et les purge de ses systèmes.

#### Faire durer les cartes plus de 30 jours {#making-cards-last-longer-than-30-days}

{% alert tip %}
Pour les cas d'usage nécessitant que les messages persistent au-delà de la limite de 30 jours des Content Cards, envisagez d'utiliser les Banners. Les Banners sont conçus pour la persistance et n'ont pas de date d'expiration obligatoire, ce qui leur permet de rester visibles aussi longtemps que nécessaire.
{% endalert %}

Si vous souhaitez qu'une carte semble toujours disponible, vous pouvez créer une Campaign récurrente qui remplace effectivement la carte tous les 30 jours :

1. Définissez la durée de la Content Card à 30 jours.
2. Définissez la rééligibilité de la Campaign à 30 jours.
3. Configurez la Campaign pour se déclencher au « démarrage de session ».

### Synchronisation et actualisation des Content Cards {#content-card-sync-and-refresh}

Les Content Cards se synchronisent selon un calendrier et lorsque votre application actualise le flux. Le comportement de synchronisation diffère entre les synchronisations complètes et partielles, et votre intégration SDK affecte le moment où les cartes s'actualisent au démarrage de la session. Pour les détails d'implémentation, consultez [Personnaliser le flux de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) et [Créer des Content Cards]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

### Impact de l'arrêt des Campaigns de Content Cards {#impact-of-stopping-content-cards-campaigns}

Lorsque vous arrêtez une Campaign et sélectionnez **Remove card after the next sync**, Braze supprime la carte des flux des utilisateurs lors de la prochaine actualisation. Le nombre d'impressions peut être inférieur au nombre d'envois, car les utilisateurs ne peuvent pas enregistrer d'impression sur des cartes supprimées avant qu'ils ne les aient vues.

## Résolution des problèmes {#troubleshooting}

### Pourquoi les Content Cards n'apparaissent-elles pas immédiatement après un événement déclencheur ? {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

Pour les campagnes à livraison par événement (comme le démarrage de session), il existe un court délai attendu entre l'événement déclencheur et la disponibilité de la carte. Ce délai s'explique par le fait que :

- L'événement déclencheur est transmis aux serveurs de Braze
- La campagne est déclenchée et l'éligibilité de l'utilisateur est enregistrée
- La Content Card est créée dans la base de données pour cet utilisateur
- Le SDK se synchronise et récupère toutes les cartes disponibles sur l'appareil

Si la synchronisation du SDK a lieu avant que l'éligibilité de l'utilisateur ne soit enregistrée, celui-ci ne reçoit pas la carte.

Pour les nouveaux utilisateurs lors de leur première session, ce délai est inévitable. Pour les utilisateurs existants qui ont besoin d'une disponibilité immédiate, envisagez d'utiliser la livraison planifiée à la place.

Si vous devez minimiser les délais pour les nouveaux utilisateurs comme pour les utilisateurs existants, vous pouvez créer deux campagnes :

- **Utilisateurs existants avec un nombre de sessions supérieur à 0 :** Utilisez une campagne à livraison planifiée. Les cartes sont pré-créées et immédiatement disponibles.
- **Nouveaux utilisateurs avec un nombre de sessions égal à 0 :** Utilisez une campagne déclenchée par événement. Les cartes sont créées après le premier déclencheur de session.

Cette approche garantit que les utilisateurs existants voient les cartes instantanément, tout en atteignant les nouveaux utilisateurs après un bref délai lors de leur première session. Pour des stratégies supplémentaires visant à améliorer la latence, consultez [Améliorer la faible latence pour les Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements).

### Pourquoi les horodatages d'impression ou de rejet se situent-ils en dehors de la planification de la campagne ? {#why-do-impression-or-dismiss-timestamps-fall-outside-the-campaign-schedule}

Les horodatages d'impression et de rejet dans les analyses et Currents reflètent le moment où un utilisateur consulte ou rejette une Content Card, et non le moment où Braze crée ou envoie la carte. Une carte peut rester dans le flux d'un utilisateur jusqu'à ce que les Content Cards soient actualisées, de sorte que les horodatages d'impression et de rejet peuvent se situer après la fenêtre d'envoi de la campagne.

Si les horaires semblent toujours inattendus :

- Vérifiez si vous consultez les analyses dans le fuseau horaire de votre entreprise par rapport au fuseau horaire de l'utilisateur dans Currents.
- Vérifiez que l'utilisateur a effectivement consulté ou rejeté la carte après l'avoir reçue, plutôt que de comparer uniquement avec l'heure d'envoi.

Pour en savoir plus sur les indicateurs des Content Cards, consultez [Rapports sur les Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/reporting).

### Erreur « All expiration values for a campaign must match » {#all-expiration-values-for-a-campaign-must-match-error}

Cette erreur apparaît lorsqu'une campagne de Content Cards multivariée utilise des paramètres d'expiration différents selon les variantes. Définissez la même expiration (durée ou heure spécifique) sur chaque variante, ou réduisez la campagne à une seule variante, puis enregistrez à nouveau. Pour savoir comment définir l'expiration lors de la création d'une campagne, consultez [Choisir une planification de livraison ou un déclencheur](#choose-a-delivery-schedule-or-trigger).