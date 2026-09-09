---
nav_title: Créer un message WhatsApp
article_title: Créer un message WhatsApp
page_order: 1
description: "Cet article de référence explique comment créer un message WhatsApp et configurer les champs, paramètres et comportements spécifiques à WhatsApp."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - WhatsApp
search_rank: 1
---

# Créer un message WhatsApp {#create-a-whatsapp-message}

> Utilisez les Campaigns WhatsApp pour contacter directement vos clients. Utilisez Liquid et d'autres contenus dynamiques pour personnaliser chaque message et créer une expérience de marque cohérente.

## Prérequis {#prerequisites}

Avant de commencer, assurez-vous de disposer des éléments suivants :

| Condition | Description |
| --- | --- |
| Campaign ou Canvas | Configurez une [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) avant de rédiger votre message WhatsApp. |
| Configuration du canal WhatsApp | Effectuez le [flux de configuration WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) : acceptez les politiques, configurez votre connexion et paramétrez l'infrastructure d'envoi. |
| Modèles approuvés | Pour les envois initiés par l'entreprise, créez et faites approuver des modèles dans Meta. Pour plus de détails, consultez l'[étape 3 de la configuration WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis pour les messages WhatsApp" }

## Type de message {#message-type}

WhatsApp prend en charge deux types de messages dans Braze :

- **Message modèle :** Utilisé pour les conversations initiées par l'entreprise. Les modèles doivent être approuvés par Meta avant l'envoi.
- **Message de réponse :** Utilisé pour répondre aux messages entrants des utilisateurs pendant une fenêtre de conversation active de 24 heures.

## Groupe d'abonnement {#subscription-group}

Sélectionnez un groupe d'abonnement WhatsApp pour chaque variante de message ou étape de message Canvas. Le groupe d'abonnement détermine quelle configuration d'expéditeur est utilisée et quels utilisateurs sont éligibles pour recevoir le message.

## Langues pour les messages modèles {#languages-for-template-messages}

Chaque modèle approuvé est associé à une langue spécifique. Configurez des variantes ou des étapes Canvas distinctes lorsque vous devez prendre en charge plusieurs langues de modèles.

Si vous ajoutez du texte dans une langue s'écrivant de droite à gauche, consultez la section [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Composition {#step-2-compose-your-whatsapp-message}

Composez votre contenu WhatsApp dans le compositeur de messages. Pour les options de configuration spécifiques à WhatsApp, utilisez la référence de champs suivante.

| Champ ou paramètre | Ce qu'il contrôle | Notes |
| --- | --- | --- |
| **Groupe d'abonnement** | L'expéditeur WhatsApp et l'audience éligible pour le message. | Le numéro de téléphone d'envoi associé apparaît dans l'alerte de l'onglet **Test**. |
| **Type de message** | Indique si la variante envoie un message modèle ou un message de réponse. | Les envois initiés par l'entreprise nécessitent un modèle. Les messages de réponse nécessitent une fenêtre de conversation active. |
| **Modèle** (Messages modèles) | Le modèle Meta approuvé utilisé pour envoyer le message. | Les champs désactivés dans le compositeur proviennent du modèle approuvé et ne peuvent être modifiés que dans Meta puis réapprouvés. |
| **Langue** (Messages modèles) | La langue du modèle sélectionnée pour la variante ou l'étape. | Créez une variante de campagne ou une étape du Canvas par langue pour faire correspondre correctement les destinataires. |
| **Variables** (Messages modèles) | Valeurs insérées dans les marques substitutives des variables du modèle. | Utilisez Liquid ou du texte brut entre doubles accolades. Incluez des valeurs par défaut pour Liquid afin que les envois n'échouent pas lorsque les données du profil sont manquantes. |
| **Liens dynamiques** | URL d'appel à l'action personnalisées. | Meta exige que les variables apparaissent à la fin des URL d'appel à l'action. |
| **Images dynamiques** | URL média ou image de la bibliothèque multimédia utilisée dans les messages modèles ou de réponse. | Les images dynamiques prennent en charge Liquid et le contenu connecté dans les URL. |
| **Disposition de réponse** (Messages de réponse) | Le format du contenu de la réponse. | Les dispositions prises en charge sont Quick Reply, Text Message, Media Message, Call-to-action Button, List Message, Flow Message, Meta Product Messages et Carousel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Champs et paramètres spécifiques à WhatsApp" }

{% tabs %}
{% tab Messages modèles %}

### Messages modèles {#template-messages}

Utilisez les [messages modèles WhatsApp approuvés]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates) pour initier des conversations sur WhatsApp. Les approbations de modèles sont gérées par Meta et peuvent prendre jusqu'à 24 heures. Si vous modifiez le contenu d'un modèle, mettez-le à jour dans Meta et soumettez-le à nouveau pour approbation.

Pour créer et soumettre un nouveau modèle sans quitter le compositeur de la campagne ou du Canvas, sélectionnez **Créer un nouveau modèle**. Pour les catégories, les types et le processus de création complet, consultez le [Générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder).

Les champs de texte désactivés (surlignés en gris) ne peuvent pas être modifiés car ils font partie du modèle WhatsApp approuvé. Pour mettre à jour le texte désactivé, vous devez modifier votre modèle et le faire réapprouver.

#### Champs de contenu {#content-fields}

Utilisez le tableau de référence des champs pour les définitions des variables, des liens dynamiques et des images dynamiques. Cette section couvre le comportement et les exemples spécifiques aux modèles.

![Liste de modèles incluant des aperçus de leurs messages, leurs langues assignées et leur statut d'approbation.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

{% alert tip %}
Si vous utilisez Liquid, incluez des valeurs par défaut pour les champs de personnalisation. Les messages avec des valeurs de personnalisation manquantes ne sont pas envoyés par WhatsApp.
{% endalert %}

![L'outil d'ajout de personnalisation avec l'attribut « first_name » et la valeur par défaut « you ».]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Images dynamiques {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Messages de réponse %}

### Messages de réponse {#response-messages}

Utilisez les messages de réponse pour répondre aux messages entrants des utilisateurs pendant la fenêtre de conversation active de 24 heures. Ces messages sont créés dans Braze et peuvent être modifiés à tout moment.

Les messages de réponse prennent en charge les dispositions suivantes :
- Quick Reply
- Text Message
- Media Message
- Call-to-action Button
- List Message
- Flow Message
- Meta Product Messages
- Carousel

![Le compositeur de messages de réponse pour un message de réponse qui accueille les nouveaux utilisateurs avec un code de réduction.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

## Résultats de l'envoi test WhatsApp {#step-4-view-test-send-results}

Après l'envoi d'un message test WhatsApp, vous pouvez consulter un rapport de réception détaillé directement dans le composeur de messages. Cela vous permet de confirmer que votre message a bien atteint le destinataire prévu et de résoudre les éventuels échecs avant le lancement.

Le bouton **Voir les résultats du test** apparaît lorsque des données d'envoi test sont disponibles pour la Campaign ou l'étape du Canvas en cours. Sélectionnez-le pour ouvrir le panneau de résultats.

Le panneau de résultats affiche chaque étape par laquelle votre message est passé avant d'atteindre le destinataire :
- **Braze :** si Braze a traité et envoyé le message avec succès
- **Meta :** si Meta a accepté le message pour la distribution
- **Appareil de l'utilisateur :** si le message a été distribué sur l'appareil du destinataire

Chaque étape affiche son statut actuel. Si une étape a échoué, le panneau indique l'erreur rencontrée et fournit des recommandations pour la résoudre. Les résultats sont conservés si vous fermez puis rouvrez la même Campaign ou le même Canvas.

![Panneau de résultats de test montrant deux envois tests réussis et un envoi test échoué.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

### Nouvelles tentatives et tentatives précédentes {#retries-and-past-attempts}

Si un envoi test échoue, Braze relance automatiquement la distribution pendant une durée pouvant aller jusqu'à 24 heures. Le panneau de résultats reflète ce comportement avec deux onglets :

- **Dernière :** la tentative de distribution la plus récente, mise à jour en temps réel au fur et à mesure des nouvelles tentatives
- **Tentatives précédentes :** un historique des tentatives précédentes, chacune affichant les statuts des étapes et les erreurs rencontrées

Lorsque le résultat final est déterminé (distribution réussie, tentatives épuisées ou échec qu'une nouvelle tentative ne résoudra pas), les onglets sont respectivement renommés **Résultat** et **Historique des tentatives**.

{% alert note %}
Étant donné que les nouvelles tentatives peuvent se poursuivre pendant 24 heures, il est possible que vous ne voyiez pas de résultat final immédiatement après un envoi échoué.
{% endalert %}

### Résoudre les échecs {#troubleshoot-failures}

Si une étape affiche un échec, le panneau présente l'erreur et les prochaines étapes suggérées. Voici les raisons courantes pour lesquelles un envoi test peut échouer :

- Le modèle de message est en pause ou n'a pas encore été approuvé dans Meta
- Le numéro de téléphone du destinataire est soumis à une limitation de débit
- Les variables Liquid du message n'ont pas été renseignées pour l'utilisateur test sélectionné

En cas de problèmes persistants, vérifiez le statut de votre modèle dans Meta Business gestionnaire ou assurez-vous que votre destinataire test dispose des attributs utilisateur requis renseignés dans Braze.

## Ce qu'il faut savoir {#supported-whatsapp-features}

### Messages sortants {#outbound-messages}

Les fonctionnalités suivantes sont prises en charge pour les messages WhatsApp sortants que vous envoyez via Braze :

| Fonctionnalité | Détails | Taille max. | Formats pris en charge |
| ------- | ------- | ------------- | ---------------------- |
| Texte d'en-tête | Les chaînes de caractères et les paramètres variables sont pris en charge. | — | —
| Corps du texte | Les chaînes de caractères et les paramètres variables sont pris en charge. | — | — |
| Texte de pied de page | Les chaînes de caractères et les paramètres variables sont pris en charge. | — | — |
| Liens CTA | Différents types d'appels à l'action (CTA) sont pris en charge. Pour plus de détails, consultez [Types d'appels à l'action](#ctas). | — | — |
| Images | Les images peuvent être intégrées dans le corps du texte. Elles doivent être en 8 bits et utiliser un modèle de couleur RVB ou RVBA. | < 5 Mo | `.png`, `.jpg`, `.jpeg` |
| Documents | Les documents peuvent être intégrés dans le corps du texte. Les fichiers doivent être hébergés via une URL. | < 100 Mo | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Vidéos | Les vidéos peuvent être intégrées dans le corps du texte. Les fichiers doivent être hébergés via une URL ou dans la [bibliothèque multimédia de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). | < 16 Mo | `.3gp`, `.mp4` |
| Audio | L'audio n'est pris en charge que via les messages de réponse. Les fichiers doivent être hébergés via une URL. | < 16 Mo | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Messages sortants" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Messages entrants {#inbound-messages}

Les fonctionnalités suivantes sont prises en charge pour les messages WhatsApp entrants que vous recevez via Braze :

| Fonctionnalité | Détails | Formats pris en charge |
| ------- | ------- | ------------------ |
| Corps du texte | Seules les chaînes de caractères standard sont prises en charge. | — |
| Images | Les images doivent être en 8 bits et utiliser un modèle de couleur RVB ou RVBA. Les fichiers doivent faire moins de 5 Mo. | `.jpg`, `.png` |
| Audio | Seuls les fichiers Ogg encodés avec le codec Opus sont pris en charge. Les autres formats Ogg ne le sont pas. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documents | Les documents sont pris en charge via les pièces jointes. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Vidéo | Seuls le codec vidéo H.264 et le codec audio AAC sont pris en charge. Les vidéos doivent contenir un seul flux audio ou aucun flux audio. | `.mp4`, `.3gp` |
| Liens CTA | Différents types d'appels à l'action (CTA) sont pris en charge. Pour plus de détails, consultez [Types d'appels à l'action](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages entrants" }

### Types d'appels à l'action {#ctas}

Les types d'appels à l'action suivants sont pris en charge pour les messages WhatsApp que vous envoyez via Braze :

| Type de CTA | Détails |
| ----------- |---------------- |
| Visiter un site web | Un bouton maximum (y compris les paramètres variables). |
| Appeler un numéro de téléphone | Disponible uniquement pour les messages modèles. <br>Un bouton maximum. |
| Boutons de réponse rapide personnalisés | Trois boutons maximum. |
| Bouton de désinscription marketing | Par défaut, les statuts d'abonnement ne sont pas automatiquement mis à jour. Pour un guide complet, consultez [Abonnements et désinscriptions]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection). |
| Messages modèles avec code promotionnel | Disponible uniquement pour les messages modèles. <br>Ils peuvent être ouverts et modifiés comme les autres messages modèles, et sont compatibles avec Liquid et les codes de promotion Braze. |
| Messages de réponse avec CTA | Créez un message de réponse incluant un bouton d'appel à l'action. |
| [Messages de réponse sous forme de liste]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | Créez un message de réponse incluant une liste de 10 options maximum parmi lesquelles les utilisateurs peuvent choisir. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types d'appels à l'action" }

## Étapes suivantes {#next-steps}

Après avoir composé votre message WhatsApp, poursuivez la création et la validation de votre envoi :

{% article_tiles %}
- name: Créer un Canvas
  link: /docs/user_guide/messaging/canvas/create_a_canvas
- name: Planifier votre campagne
  link: /docs/user_guide/messaging/campaigns/schedule_your_campaign
- name: Cibler les utilisateurs
  link: /docs/user_guide/messaging/messaging_fundamentals/target_users
- name: Événements de conversion
  link: /docs/user_guide/messaging/messaging_fundamentals/conversion_events
- name: Envoyer des messages test
  link: /docs/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp
- name: Reporting WhatsApp
  link: /docs/user_guide/channels/whatsapp/reporting
{% endarticle_tiles %}