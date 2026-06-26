---
nav_title: Créer un message WhatsApp
article_title: Créer un message WhatsApp
page_order: 1
description: "Cet article de référence couvre les étapes nécessaires à la création d'un message WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Créer un message WhatsApp {#create-a-whatsapp-message}

> Les Campaigns WhatsApp sont idéales pour atteindre directement vos clients et converser avec eux de manière programmatique. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnalisée avec vos utilisateurs et favoriser un environnement qui enrichit l'expérience utilisateur avec votre marque de manière non intrusive.

## Conditions préalables {#prerequisites}

Avant de pouvoir créer des messages WhatsApp, vous devez consulter et compléter les éléments suivants depuis l'[aperçu WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) :
  - Prendre connaissance des politiques, limites et règles de contenu
  - Configurer votre connexion WhatsApp
  - Créer les modèles initiaux dans Meta à utiliser dans vos messages

## Créer un message {#creating-a-message}

### Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

{% alert note %}
WhatsApp crée différents [modèles de messages](#template-messages) pour chaque langue. Créez soit une campagne pour chaque langue avec une segmentation pour servir le bon modèle aux utilisateurs, soit utilisez Canvas.
{% endalert %}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les Campaigns sont plus adaptées aux envois de messages ciblés ponctuels, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Accédez à la page **Campaigns** et cliquez sur <i class="fas fa-plus"></i> **Créer une campagne**.
2. Sélectionnez **WhatsApp** ou, pour les Campaigns ciblant plusieurs canaux, sélectionnez **Campagne multicanale**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) et des [Étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) selon vos besoins.
   * Les étiquettes facilitent la recherche de vos Campaigns et la création de rapports. Par exemple, lorsque vous utilisez le [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), vous pouvez filtrer par étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier depuis la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) à l'aide du compositeur Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le générateur Canvas. Donnez à votre étape un nom clair et significatif.
3. Choisissez une [planification d'étape]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape selon vos besoins. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Choisissez tout autre canal de communication que vous souhaitez associer à votre message.

{% alert tip %}
Si un Canvas basé sur une action est déclenché par un message WhatsApp entrant, vous pouvez référencer les propriétés WhatsApp dans n'importe quelle étape du Canvas jusqu'au prochain parcours d'action.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 2 : Composer votre message WhatsApp {#step-2-compose-your-whatsapp-message}

Choisissez si vous souhaitez créer un [message modèle](#template-messages) WhatsApp ou un message de réponse, selon votre cas d'utilisation. Toute conversation initiée par l'entreprise doit commencer par un modèle approuvé, tandis que les messages de réponse peuvent être utilisés pour répondre aux messages entrants des utilisateurs dans une fenêtre de 24 heures.

![La section Variantes de message vous permet de sélectionner un groupe d'abonnement et l'un des deux types de messages : Message modèle WhatsApp et Message de réponse.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Messages modèles %}

Vous pouvez utiliser des [modèles de messages WhatsApp approuvés]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/#step-3-create-whatsapp-templates
) pour initier des conversations avec vos utilisateurs sur WhatsApp. Ces messages sont soumis à l'avance à WhatsApp pour approbation du contenu, ce qui peut prendre jusqu'à 24 heures. Toute modification que vous apportez au texte doit être éditée et resoumise à WhatsApp.

Les champs de texte désactivés (surlignés en gris) ne peuvent pas être modifiés car ils font partie du modèle WhatsApp approuvé. Pour mettre à jour le texte désactivé, vous devez modifier votre modèle et le faire réapprouver.

#### Langues {#languages}

Chaque modèle a une langue assignée, vous devez donc créer une campagne ou une étape Canvas pour chaque langue afin de configurer correctement la correspondance avec les utilisateurs. Par exemple, si vous créez un Canvas qui utilise des modèles assignés en indonésien et en anglais, vous devez créer une étape Canvas pour le modèle indonésien et une étape Canvas pour le modèle anglais.

![Liste de modèles incluant des aperçus de leurs messages, leurs langues assignées et leur statut d'approbation.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les affichent. Pour les bonnes pratiques de rédaction de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### Variables {#variables}

Si vous avez ajouté des variables lors de la création du modèle WhatsApp dans le Meta Business Manager, ces variables apparaîtront comme des espaces vides dans le compositeur de messages. Remplacez ces espaces vides par du Liquid ou du texte brut. Pour utiliser du texte brut, utilisez le format « texte ici » encadré par des doubles accolades. Si vous avez choisi d'inclure des images lors de la création de votre modèle, vous pouvez télécharger ou ajouter des images depuis la bibliothèque multimédia ou en référençant une URL d'image. Dans la mesure du possible, nous recommandons de télécharger les images directement dans votre bibliothèque multimédia pour garantir la cohérence et la fiabilité.

Notez que les champs de texte désactivés (surlignés en gris) ne peuvent pas être modifiés car ils font partie du modèle WhatsApp approuvé. Si vous souhaitez mettre à jour le texte désactivé, vous devez modifier votre modèle et le faire réapprouver.

{% alert tip %}
{% raw %}
Si vous prévoyez d'utiliser Liquid, assurez-vous d'inclure une valeur par défaut pour la personnalisation choisie afin que, dans le cas où le profil utilisateur du destinataire est incomplet, celui-ci ne reçoive pas de message. Tout message contenant des variables Liquid manquantes ne sera pas envoyé par WhatsApp.
{% endraw %}
{% endalert %}

![L'outil Ajouter une personnalisation avec l'attribut « first_name » et la valeur par défaut « you ».]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Liens dynamiques {#dynamic-links}

Les URL d'appel à l'action peuvent contenir des variables, mais Meta exige qu'elles soient à la fin de l'URL, comme `{% raw %}https://example.com/{{variable}}{% endraw %}`, où la variable peut ensuite être remplacée dans Braze par du Liquid. Les liens peuvent également être inclus dans le corps du texte en tant que partie du modèle. Ces deux types de liens peuvent être raccourcis et suivis grâce au [suivi des clics]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking/).

### Images dynamiques {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Messages de réponse %}

Vous pouvez utiliser les messages de réponse pour répondre aux messages entrants de vos utilisateurs. Ces messages sont créés dans l'application Braze lors de votre expérience de composition et peuvent être modifiés à tout moment. Vous pouvez utiliser Liquid pour adapter la langue du message de réponse aux utilisateurs appropriés.

Il existe cinq dispositions de messages de réponse que vous pouvez utiliser :
- Réponse rapide
- Message texte
- Message multimédia
- Bouton d'appel à l'action
- Message de liste

![Le compositeur de messages de réponse pour un message de réponse qui accueille les nouveaux utilisateurs avec un code de réduction.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Étape 3 : Prévisualiser et tester votre message {#step-3-preview-and-test-your-message}

Braze recommande toujours de prévisualiser et de tester votre message avant de l'envoyer. Passez à l'onglet **Test** pour envoyer un message WhatsApp de test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

![Un aperçu de message pour un utilisateur personnalisé nommé Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
Une fenêtre de conversation est nécessaire pour envoyer des messages de réponse, y compris les messages de test. Pour initier une fenêtre de conversation, envoyez un message WhatsApp au numéro de téléphone associé au groupe d'abonnement que vous utilisez pour ce message. Le numéro de téléphone associé est indiqué dans l'alerte de l'onglet **Test**.
{% endalert %}

![Une alerte indiquant d'ouvrir une fenêtre de conversation en envoyant un message WhatsApp, puis d'envoyer un message à l'utilisateur test.]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

Pour plus d'informations, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=whatsapp).

### Étape 4 : Consulter les résultats de l'envoi test {#step-4-view-test-send-results}

Après avoir envoyé un message WhatsApp de test, vous pouvez consulter un rapport de livraison détaillé directement dans le compositeur de messages. Cela vous aide à confirmer que votre message a bien atteint le destinataire prévu et à résoudre les éventuels échecs avant le lancement.

Le bouton **Voir les résultats du test** apparaît lorsque des données d'envoi test sont disponibles pour la campagne ou l'étape Canvas en cours. Sélectionnez-le pour ouvrir le panneau de résultats.

Le panneau de résultats affiche chaque étape par laquelle votre message est passé pour atteindre le destinataire :
- **Braze :** indique si Braze a correctement traité et envoyé le message
- **Meta :** indique si Meta a accepté le message pour la livraison
- **Appareil de l'utilisateur :** indique si le message a été livré sur l'appareil du destinataire

Chaque étape affiche son état actuel. Si une étape a échoué, le panneau affiche l'erreur rencontrée et des conseils pour la résoudre. Les résultats persistent si vous fermez et rouvrez la même campagne ou le même Canvas.

![Panneau de résultats de test montrant deux envois test réussis et un envoi test échoué.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

#### Nouvelles tentatives et tentatives précédentes {#retries-and-past-attempts}

Si un envoi test échoue, Braze retente automatiquement la livraison pendant 24 heures maximum. Le panneau de résultats reflète cela avec deux onglets :

- **Dernière :** la tentative de livraison la plus récente, mise à jour en temps réel au fur et à mesure des nouvelles tentatives
- **Tentatives précédentes :** un historique des tentatives précédentes, chacune affichant les états des étapes et les erreurs rencontrées

Lorsque le résultat final est déterminé (livraison réussie, tentatives épuisées ou échec qu'une nouvelle tentative ne résoudra pas), les onglets sont respectivement renommés **Résultat** et **Historique des tentatives**.

{% alert note %}
Étant donné que les nouvelles tentatives peuvent se poursuivre pendant 24 heures maximum, il est possible que vous ne voyiez pas de résultat final immédiatement après un envoi échoué.
{% endalert %}

#### Résoudre les échecs {#troubleshoot-failures}

Si une étape affiche un échec, le panneau affiche l'erreur et les prochaines étapes suggérées. Les raisons courantes d'échec d'un envoi test incluent :

- Le modèle de message est en pause ou pas encore approuvé dans Meta
- Le numéro de téléphone du destinataire est soumis à une limitation de débit
- Les variables Liquid du message n'ont pas été renseignées pour l'utilisateur test sélectionné

Pour les problèmes persistants, vérifiez le statut de votre modèle dans le Meta Business Manager ou vérifiez que votre destinataire test possède les attributs utilisateur requis renseignés dans Braze.

### Étape 5 : Construire le reste de votre campagne ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Ensuite, construisez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages WhatsApp.

#### Choisir une planification ou un déclencheur de livraison {#choose-a-delivery-schedule-or-trigger}

Les messages WhatsApp peuvent être envoyés selon un horaire planifié, une action ou un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

Cette étape vous permet également de spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) pour recevoir la campagne, ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

#### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) en choisissant des segments ou des filtres pour affiner votre audience. Vous devriez avoir déjà choisi le groupe d'abonnement, qui restreint les utilisateurs selon le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous. À cette étape, vous sélectionnez l'audience plus large parmi vos segments et affinez davantage ce segment avec nos filtres. Vous recevez automatiquement un aperçu de la population approximative de ce segment. N'oubliez pas que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

#### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous pouvez définir une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Soyez créatif et réfléchissez à la manière dont vous souhaitez véritablement mesurer le succès de cette campagne.

{% endtab %}

{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, d'implémenter les tests multivariés et la Sélection intelligente, et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/) de notre documentation Canvas.

Étant donné que les fenêtres de conversation ne peuvent durer que 24 heures par message entrant, Braze vérifiera qu'il n'y a pas de délais dépassant 24 heures entre un message entrant et un message de réponse.

{% endtab %}
{% endtabs %}

### Étape 5 : Vérifier et déployer {#step-5-review-and-deploy}

Après avoir terminé la construction de votre campagne ou Canvas, vérifiez ses détails, testez-le, puis envoyez-le !

Ensuite, consultez les [rapports WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting/) pour découvrir comment accéder aux résultats de vos Campaigns WhatsApp.

## Fonctionnalités WhatsApp prises en charge {#supported-whatsapp-features}

### Messages sortants {#outbound-messages}

Les fonctionnalités suivantes sont prises en charge pour les messages WhatsApp sortants que vous envoyez via Braze :

| Fonctionnalité | Détails | Taille max. | Formats pris en charge |
| ------- | ------- | ------------- | ---------------------- |
| Texte d'en-tête | Les chaînes de caractères et les paramètres variables sont pris en charge. | — | —
| Corps du texte | Les chaînes de caractères et les paramètres variables sont pris en charge. | — | — |
| Texte de pied de page | Les chaînes de caractères et les paramètres variables sont pris en charge. | — | — |
| Liens CTA | Différents types d'appel à l'action (CTA) sont pris en charge. Pour plus de détails, consultez [Types d'appel à l'action](#ctas). | — | — |
| Images | Les images peuvent être intégrées dans le corps du texte. Elles doivent être en 8 bits et utiliser un modèle de couleur RVB ou RVBA. | < 5 Mo | `.png`, `.jpg`, `.jpeg` |
| Documents | Les documents peuvent être intégrés dans le corps du texte. Les fichiers doivent être hébergés via une URL. | < 100 Mo | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Vidéos | Les vidéos peuvent être intégrées dans le corps du texte. Les fichiers doivent être hébergés via une URL ou dans la [bibliothèque multimédia Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). | < 16 Mo | `.3gp`, `.mp4` |
| Audio | L'audio n'est pris en charge que via les messages de réponse. Les fichiers doivent être hébergés via une URL. | < 16 Mo | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Messages sortants" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Messages entrants {#inbound-messages}

Les fonctionnalités suivantes sont prises en charge pour les messages WhatsApp entrants que vous recevez via Braze :

| Fonctionnalité | Détails | Formats pris en charge |
| ------- | ------- | ------------------ |
| Corps du texte | Seules les chaînes de caractères standard sont prises en charge. | — |
| Images | Les images doivent être en 8 bits et utiliser un modèle de couleur RVB ou RVBA. Les fichiers doivent faire moins de 5 Mo. | `.jpg`, `.png` |
| Audio | Seuls les fichiers Ogg encodés avec le codec Opus sont pris en charge. Les autres formats Ogg ne le sont pas. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus uniquement)` |
| Documents | Les documents sont pris en charge via les pièces jointes de messages. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Vidéo | Seuls le codec vidéo H.264 et le codec audio AAC sont pris en charge. Les vidéos doivent avoir soit un seul flux audio, soit aucun flux audio. | `.mp4`, `.3gp` |
| Liens CTA | Différents types d'appel à l'action (CTA) sont pris en charge. Pour plus de détails, consultez [Types d'appel à l'action](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages entrants" }

### Types d'appel à l'action {#ctas}

Les types d'appel à l'action suivants sont pris en charge pour les messages WhatsApp que vous envoyez via Braze :

| Type de CTA | Détails |
| ----------- | ---------------- |
| Visiter le site web | Un bouton maximum (y compris les paramètres variables). |
| Appeler un numéro de téléphone | Disponible uniquement pour les modèles de messages. <br>Un bouton maximum. |
| Boutons de réponse rapide personnalisés | Trois boutons maximum. |
| Bouton de désinscription marketing | Par défaut, les statuts d'abonnement ne sont pas automatiquement mis à jour. Pour un guide complet, consultez [Abonnements et désinscriptions]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs/#marketing-opt-out-selection). |
| Modèles de messages avec code promo | Disponible uniquement pour les modèles de messages. <br>Ceux-ci peuvent être ouverts et modifiés comme les autres modèles de messages, et sont compatibles avec Liquid et les codes de promotion Braze. |
| Messages de réponse CTA | Créez un message de réponse qui inclut un bouton d'appel à l'action. |
| [Messages de réponse de type liste]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users/#list-messages) | Créez un message de réponse qui inclut une liste de 10 options maximum parmi lesquelles les utilisateurs peuvent choisir. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types d'appel à l'action" }