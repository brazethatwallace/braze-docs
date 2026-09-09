---
nav_title: Créer un message
article_title: Créer un message SMS, MMS ou RCS
page_order: 1
description: "Créez un message SMS, MMS ou RCS et configurez les types de messages, les champs, le raccourcissement de liens, les paramètres de réception/distribution et le comportement propres à chaque canal."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
  - Canvas
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Créer un message SMS, MMS ou RCS {#create-an-sms-mms-or-rcs-message}

> Créez des messages SMS, MMS et Rich Communication Services (RCS) personnalisés dans des Campaigns ou des Canvas. Le groupe d'abonnement sélectionné détermine les types de messages et les expéditeurs disponibles.

## Prérequis {#prerequisites}

Avant de commencer, assurez-vous de disposer des éléments suivants :

| Exigence | Description |
| --- | --- |
| Configuration de l'expéditeur | Effectuez la [configuration de l'expéditeur]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup). Pour envoyer des MMS, votre groupe d'abonnement doit disposer d'un numéro de téléphone compatible MMS. Pour envoyer des RCS, effectuez la [configuration RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) et ajoutez un expéditeur RCS vérifié. |
| Groupe d'abonnement | Créez un [groupe d'abonnement]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) contenant les expéditeurs pour ce message. |
| Numéros de téléphone et consentement des utilisateurs | Importez les numéros de téléphone des utilisateurs et recueillez les [abonnements SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) appropriés. |
| Campaign ou Canvas | Utilisez une Campaign pour un message ciblé unique ou un Canvas pour un parcours utilisateur en plusieurs étapes. |
| Crédits de messages ou d'actions | Vérifiez que votre compte dispose de crédits disponibles. L'envoi de messages SMS, MMS et RCS depuis Braze consomme ces crédits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis pour les messages SMS, MMS et RCS" }

## Créer un message {#create-a-message}

### Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **SMS/MMS/RCS** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel Campaign**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) selon vos besoins.
  - Les tags facilitent la recherche et l'utilisation de vos campagnes dans les rapports.
5. Ajoutez et nommez les variantes de votre campagne. Vous pouvez inclure des variantes SMS/MMS et RCS dans la même campagne. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si les variantes de votre campagne ont un contenu similaire, composez le premier message avant d'ajouter d'autres variantes. Vous pouvez ensuite sélectionner **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Étape 2 : Sélectionner un groupe d'abonnement et un type de message {#step-2-select-a-subscription-group-and-message-type}

Sélectionnez le **groupe d'abonnement** qui contient l'expéditeur pour ce message. Braze utilise le groupe sélectionné pour calculer l'audience atteignable et déterminer l'éligibilité au moment de l'envoi.

Le groupe d'abonnement que vous sélectionnez détermine les types de messages disponibles dans le composeur :

| Type de groupe d'abonnement | Types de messages disponibles |
| --- | --- |
| SMS uniquement | SMS |
| SMS avec numéros compatibles MMS | SMS et MMS |
| Compatible RCS avec un expéditeur RCS vérifié | RCS et SMS lorsque le groupe contient également un expéditeur SMS. MMS est également disponible lorsque cet expéditeur est compatible MMS. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de messages disponibles par groupe d'abonnement" }

{% alert tip %}
Ajoutez au moins un expéditeur SMS à un groupe d'abonnement RCS afin de pouvoir envoyer un SMS de secours lorsque la livraison RCS échoue.
{% endalert %}

Si le groupe d'abonnement prend en charge les deux protocoles, sélectionnez **SMS/MMS** ou **RCS**. Pour RCS, sélectionnez **Text**, **Media** ou **Card**.

### Étape 3 : Composer votre message {#step-3-compose-your-message}

Les champs et limites du composeur dépendent du type de message que vous avez sélectionné.

{% tabs local %}
{% tab SMS et MMS %}

#### Champs et paramètres SMS et MMS {#sms-and-mms-fields-and-settings}

| Champ ou paramètre | Description |
| --- | --- |
| **Language** | Insérer du contenu spécifique à une langue dans le message. |
| **Message** | Saisissez jusqu'à 1 600 caractères, y compris Liquid, le contenu connecté et les emojis. Le composeur estime l'encodage, le nombre de caractères et le nombre de segments SMS facturables. Un message MMS peut contenir un média sans corps de message. |
| **Media** | Pour un groupe d'abonnement compatible MMS, ajoutez une image PNG, JPEG ou GIF depuis la bibliothèque multimédia ou par URL. Vous pouvez ajouter une vCard au lieu d'une image. |
| **Link shortening** | Raccourcir les URL HTTP et HTTPS et suivre l'engagement. Pour le raccourcissement de liens hérité, sélectionnez le suivi basique ou avancé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs et paramètres SMS et MMS" }

Les messages SMS utilisent l'encodage GSM-7 ou UCS-2 et sont facturés par segment de message. Un seul caractère peut modifier l'encodage et augmenter le nombre de segments facturables. Pour les règles d'encodage, les tailles de segments et le calculateur de segments, consultez [Calculateurs de facturation SMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

![Composeur SMS affichant le texte du message et les estimations de nombre de caractères et de segments.]({% image_buster /assets/img/sms_campaign_compose.png %})

#### Spécifications média MMS {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Pour envoyer des informations professionnelles que les utilisateurs peuvent enregistrer dans les contacts de leur appareil, consultez [Cartes de contact]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card). L'envoi d'une carte de contact est facturé comme un MMS.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

La disponibilité et le rendu des MMS dépendent de l'opérateur du destinataire. Lorsqu'un opérateur ne peut pas accepter les MMS, le média devient un lien dans le corps du SMS via le fournisseur. Évitez d'envoyer des MMS vers des numéros Google Voice car la prise en charge limitée des MMS peut entraîner une livraison peu fiable.

Lorsqu'un utilisateur envoie un média entrant, Braze expose ses URL dans les [événements SMS entrants de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) et via {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} dans Liquid.

{% endtab %}
{% tab RCS %}

#### Types de messages RCS {#rcs-message-types}

| Type de message | Champs et paramètres | Limites et comportement |
| --- | --- | --- |
| **Text** | Corps de message obligatoire, réponses suggérées ou actions Open URL facultatives, SMS de secours facultatif et raccourcissement de liens | Le corps du message peut contenir jusqu'à 1 600 ou 3 072 caractères, selon le fournisseur de services SMS. Ajoutez jusqu'à cinq suggestions. |
| **Media** | Image, vidéo, document ou audio obligatoire ; corps de message facultatif ; suggestions, SMS de secours et raccourcissement de liens facultatifs | Le corps du message peut contenir jusqu'à 1 600 ou 3 072 caractères, selon le fournisseur, et est facturé comme un message RCS supplémentaire. Ajoutez jusqu'à cinq suggestions. Tous les fournisseurs ne prennent pas en charge les messages **Media** autonomes (par exemple, Twilio). |
| **Card** | Carte média ou carte texte uniquement, titre, description, boutons, suggestions facultatives et SMS de secours facultatif | Le titre peut contenir jusqu'à 200 caractères. La description peut contenir jusqu'à 1 600 ou 2 000 caractères, selon le fournisseur. Ajoutez entre un et quatre boutons. Consultez [Prise en charge des messages Card par fournisseur](#provider-support-for-card-messages) pour la mise en page et la disponibilité des champs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Types de messages RCS, champs et limites" }

#### Mises en page des cartes {#card-layouts}

Les messages RCS **Card** combinent média, texte et boutons dans une seule unité. Choisissez une mise en page dans le composeur :

| Mise en page de la carte | Champs obligatoires | Champs facultatifs |
| --- | --- | --- |
| **Texte uniquement** | Titre, description et au moins un bouton de carte | Jusqu'à trois boutons de carte supplémentaires, suggestions en dehors de la carte (si pris en charge) et SMS de secours |
| **Media** | Image, GIF ou vidéo et au moins un bouton de carte | Titre, description, jusqu'à trois boutons de carte supplémentaires, suggestions en dehors de la carte (si pris en charge) et SMS de secours |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mises en page des cartes RCS" }

Utilisez Liquid pour personnaliser les titres, descriptions, médias et boutons des cartes. Les URL saisies en texte brut dans le titre ou la description ne sont pas cliquables — ajoutez plutôt un bouton de carte **Open URL**.

Les suggestions peuvent être des réponses suggérées, qui pré-remplissent la saisie de texte de l'utilisateur, ou des actions Open URL. Ajoutez jusqu'à 25 caractères de texte à chaque suggestion et une URL de 2 048 caractères maximum à chaque action Open URL. Activez **Send SMS if RCS fails** pour ajouter un message de secours de 1 600 caractères maximum lorsque la livraison RCS échoue. Le groupe d'abonnement sélectionné doit contenir un expéditeur SMS. Le raccourcissement de liens s'applique uniquement aux liens dans le corps du SMS de secours, pas aux URL des boutons de carte.

La facturation des messages RCS dépend du type de message et du contenu. Pour les règles de facturation des messages basiques, riches et cartes riches, consultez [Facturation des messages RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing).

#### Prise en charge des messages Card par fournisseur {#provider-support-for-card-messages}

La disponibilité des types de messages RCS et des options Card dépend de votre fournisseur de services SMS. Le composeur n'affiche que les types et champs pris en charge.

| Fonctionnalité | Infobip | Twilio |
| --- | --- | --- |
| Type de message **Media** autonome | Pris en charge | Non pris en charge |
| Mise en page carte texte uniquement | Prise en charge | Non prise en charge |
| Mise en page carte média | Prise en charge | Prise en charge |
| Suggestions en dehors de la carte | Prises en charge | Non prises en charge |
| Boutons de carte | Pris en charge (1–4) | Pris en charge (1–4) |
| Limite de caractères de la description | Jusqu'à 2 000 caractères | Jusqu'à 1 600 caractères |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prise en charge des messages RCS Card par fournisseur" }

#### Spécifications média RCS {#rcs-media-specifications}

Le composeur accepte une URL média de 1 000 caractères maximum. Les formats disponibles et la taille maximale des fichiers dépendent du fournisseur de services SMS.

| Type de fichier | Spécifications |
| --- | --- |
| Tous | La taille maximale du fichier est de 16&nbsp;Mo ou 100&nbsp;Mo, selon le fournisseur. |
| Image | JPEG, JPG, GIF, PNG |
| Vidéo | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| Document | PDF. Disponible pour les messages **Media**, mais pas pour les cartes média. |
| Audio | AAC, MP3, MPEG, MP4, 3GPP, OGG. La prise en charge varie selon le fournisseur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications média RCS" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### Personnalisation {#personalization}

Utilisez [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), les emojis et le contenu spécifique à une langue pour personnaliser votre message. Incluez une valeur par défaut pour la personnalisation Liquid afin que les profils avec des données incomplètes ne reçoivent pas de contenu vide.

Pour créer un texte de message à partir d'une consigne, utilisez [Générer du texte]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) avec Operator.

Pour les langues écrites de droite à gauche, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Créer des flux de conversation (RCS) {#create-conversational-message-workflows-rcs}

Les flux de conversation vous permettent de répondre dynamiquement aux utilisateurs, créant une expérience de messagerie interactive. Pour créer un flux, créez un Canvas, puis combinez les réponses suggérées avec les [parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) pour diriger votre flux en fonction de la réponse sélectionnée par l'utilisateur.

1. Dans le générateur de Canvas, créez une étape de message RCS avec plusieurs réponses suggérées.

![Composeur de messages RCS avec des réponses suggérées.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Connectez ce message à un parcours d'action avec un groupe d'actions pour chaque réponse suggérée.
3. Pour chaque groupe d'actions :
   - Sélectionnez le déclencheur **Send an SMS inbound message**.
   - Définissez le corps du message pour qu'il soit identique à la réponse suggérée correspondante.

![Étape de parcours d'action configurée avec trois groupes d'actions, un pour chaque réponse suggérée.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Connectez chaque groupe d'actions à une étape de message RCS, puis ajoutez du contenu basé sur la réponse suggérée associée.
5. Poursuivez le flux de conversation en ajoutant des réponses suggérées à tous les messages de suivi.
6. Répétez les étapes 2 à 4 jusqu'à ce que le flux soit terminé.

![Canvas montrant un flux de conversation avec deux parcours d'action.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### Étape 4 : Configurer le raccourcissement de liens {#step-4-configure-link-shortening}

Activez **Link shortening** pour raccourcir les URL HTTP et HTTPS et suivre les clics pour les liens SMS, MMS et RCS pris en charge. Selon la version disponible dans votre espace de travail, sélectionnez le suivi basique ou avancé, ou utilisez le raccourcissement de liens unifié.

Le suivi avancé ajoute des données de clics au niveau de l'utilisateur pour la segmentation et le reciblage. Le raccourcissement de liens unifié combine les liens raccourcis SMS et RCS dans un seul format personnalisé. Pour les URL prises en charge, le comportement Liquid, les exigences de test, les domaines personnalisés et le reciblage, consultez [Raccourcissement de liens]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

Braze raccourcit jusqu'à 25 liens dans un message. Une URL de plus de 4 000 caractères ne peut pas être raccourcie et provoquera l'échec du message au moment de l'envoi.

### Étape 5 : Prévisualiser et tester votre message {#step-5-preview-and-test-your-message}

Accédez à l'onglet **Test** pour prévisualiser le message en tant qu'utilisateur ou envoyer un SMS, MMS ou message RCS de test à un [groupe de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à un utilisateur individuel.

{% alert tip %}
Utilisez le [calculateur de segments SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) pour estimer le nombre de segments que contient votre message.
{% endalert %}

![Prévisualisation du texte SMS depuis l'onglet Test du composeur. Dans la section profil, le champ Prénom est défini sur « James ». Dans la section de prévisualisation, le SMS affiche désormais « Hi James, we appreciate your support! »]({% image_buster /assets/img/sms_campaign_test.png %})

Pour les MMS, c'est le téléphone du destinataire qui détermine si le média s'affiche avant ou après le corps du message.

{% alert note %}
Étant donné que le rendu RCS est contrôlé par le système d'exploitation de l'utilisateur, le fabricant de l'appareil, l'opérateur et l'application de messagerie (par exemple, Google Messages vs. Apple Messages), l'apparence du message peut varier. La prévisualisation affichée dans Braze peut ne pas correspondre exactement à ce que l'utilisateur final reçoit. Validez le rendu final sur de vrais appareils autant que possible. Pour en savoir plus sur le rendu RCS sur les appareils iOS, consultez [Pourquoi mon message RCS ne s'affiche-t-il pas correctement sur les appareils iOS ?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices). Pour les GIF dans les cartes riches, consultez [Pourquoi les GIF dans les cartes riches RCS apparaissent-ils statiques sur iOS ?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).
{% endalert %}

Pour en savoir plus, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

### Étape 6 : Construire le reste de votre campagne ou Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Choisir une planification de livraison ou un déclencheur {#choose-a-delivery-schedule-or-trigger}

Livrez les messages à une heure planifiée ou en réponse à une action ou un déclencheur API. Pour les options de planification et de déclenchement, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Configurez les contrôles de livraison tels que la [rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) et la [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Pour la livraison par événement, définissez la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Choisir les utilisateurs à cibler {#choose-users-to-target}

[Ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en sélectionnant des Segments et des filtres. Braze calcule l'appartenance exacte aux Segments avant d'envoyer le message.

Le groupe d'abonnement sélectionné filtre les utilisateurs abonnés. Les destinataires SMS et MMS ont également besoin d'un numéro de téléphone valide. Les destinataires RCS ont besoin d'un appareil et d'une connexion opérateur compatibles RCS ; utilisez un SMS de secours pour atteindre les utilisateurs éligibles lorsque la livraison RCS échoue.

{% multi_lang_include audience/target_audiences.md %}

Pour le ciblage par clic et par interaction, consultez [Reciblage des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).

#### Choisir les événements de conversion {#choose-conversion-events}

Utilisez les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) pour mesurer les actions après qu'un utilisateur a reçu la campagne. Définissez une fenêtre de conversion allant jusqu'à 30 jours.

{% endtab %}
{% tab Canvas %}

Complétez les sections restantes de votre Canvas. Pour les planifications d'entrée, les paramètres d'audience et les contrôles d'envoi, consultez [Créer un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

### Étape 7 : Vérifier et déployer {#step-7-review-and-deploy}

Après avoir terminé la création de votre campagne ou Canvas, vérifiez ses détails et testez le message avant de l'envoyer.

Après le lancement, utilisez les [rapports SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) pour examiner les performances du message.

## À savoir {#things-to-know}

- Les SMS sont facturés par segment de message, les MMS ont leur propre tarification, et les RCS sont facturés par type de message. Consultez les [calculateurs de facturation SMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) avant d'envoyer vos messages.
- Les MMS prennent en charge une image ou une vCard. La compatibilité de l'opérateur détermine si les destinataires reçoivent le média ou un lien vers l'image.
- Les fonctionnalités et limites des RCS varient selon le fournisseur de services SMS. Le composeur affiche uniquement les options disponibles pour le groupe d'abonnement sélectionné.
- Vous pouvez envoyer un message vocal pré-enregistré sous forme d'audio dans un message RCS de type **Média**.
- Le rendu et le comportement d'interaction varient selon l'appareil, l'opérateur, le système d'exploitation et l'application de messagerie.