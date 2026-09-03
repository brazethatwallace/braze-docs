---
nav_title: Créer un message LINE
article_title: Créer un message LINE
page_order: 1
description: "Créez un message LINE et configurez les types de messages, les champs, le suivi des clics, les paramètres de réception et le comportement propres au canal."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - LINE
alias: /line/create/
---

# Créer un message LINE {#create-a-line-message}

> Créez des messages LINE personnalisés dans des Campaigns ou des Canvas. Choisissez parmi les messages texte, image, enrichis et à base de cartes, et combinez jusqu'à cinq messages en un seul envoi.

## Prérequis {#prerequisites}

Avant de commencer, assurez-vous de disposer des éléments suivants :

| Condition | Description |
| --- | --- |
| Connexion LINE | Effectuez la [configuration LINE]({{site.baseurl}}/user_guide/channels/line/line_setup) et consultez les politiques, limites et règles de contenu du canal. |
| Campaign ou Canvas | Utilisez une Campaign pour un message ciblé unique ou un Canvas pour un parcours utilisateur en plusieurs étapes. |
| Plan de message | Préparez votre contenu, vos images, vos liens et votre groupe d'abonnement. |
| Crédits de messages ou d'actions | Vérifiez que votre compte dispose de crédits disponibles. L'envoi de messages LINE depuis Braze utilise ces crédits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis pour les messages LINE" }

## Créer un message {#create-a-message}

### Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campaigns** et sélectionnez **Créer une campagne**.
2. Sélectionnez **LINE** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanale**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) si nécessaire.
   * Les tags facilitent la recherche et l'utilisation de vos campagnes dans les rapports.
5. Ajoutez et nommez les variantes de votre campagne. Chaque variante peut utiliser des types de messages et des mises en page différents. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si les variantes de votre campagne ont un contenu similaire, rédigez le premier message avant d'ajouter d'autres variantes. Vous pouvez ensuite sélectionner **Copier à partir de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Étape 2 : Sélectionner un groupe d'abonnement {#step-2-select-a-subscription-group}

Sélectionnez le **groupe d'abonnement** associé au canal LINE qui envoie le message. Un groupe d'abonnement est requis avant de pouvoir lancer l'éditeur.

Toutes les variantes d'une campagne LINE doivent utiliser le même groupe d'abonnement. Pour en savoir plus sur les états d'abonnement LINE, consultez [Groupes d'abonnement LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

### Étape 3 : Rédiger votre message LINE {#step-3-compose-your-line-message}

Sélectionnez **Lancer l'éditeur**, puis glissez-déposez les types de messages dans l'éditeur. Combinez jusqu'à cinq messages en un seul envoi et organisez-les dans l'ordre dans lequel les utilisateurs les reçoivent.

![Éditeur LINE avec un message affiché dans l'aperçu.]({% image_buster /assets/img/line/line_composer.png %})

#### Types de messages {#message-types}

| Type de message | Champs et paramètres | Limites et comportement |
| --- | --- | --- |
| **Texte** | Corps du message avec emojis, Liquid et URL | Jusqu'à 5 000 caractères. |
| **Image** | Image provenant de la bibliothèque multimédia ou d'une URL, y compris une URL dynamique | Les URL d'images peuvent contenir jusqu'à 2 000 caractères. Les messages image autonomes ne prennent pas en charge les actions au clic. |
| **Message enrichi** | Image, texte alternatif, modèle et zones cliquables avec des actions URI | Le texte alternatif peut contenir jusqu'à 400 caractères. Ajoutez entre une et 50 zones cliquables. Les libellés d'action peuvent contenir jusqu'à 100 caractères, et chaque URI peut contenir jusqu'à 1 000 caractères. |
| **Message à base de cartes** | Jusqu'à 10 cartes avec une image et un en-tête optionnels, un corps obligatoire et des actions URI | Le texte alternatif peut contenir jusqu'à 400 caractères. Un en-tête peut contenir jusqu'à 40 caractères. Un corps peut contenir jusqu'à 60 caractères avec une image ou un en-tête, ou 120 caractères sans l'un ni l'autre. Chaque carte nécessite entre une et trois actions avec des libellés de 20 caractères maximum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Types de messages LINE, champs et limites" }

Les limites de caractères excluent la syntaxe Liquid.

Pour les spécifications d'images, les modèles de messages enrichis, les paramètres d'images de carrousel et les exemples, consultez [Types de messages LINE]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/message_types).

{% alert note %}
Les messages à base de cartes appliquent les mêmes champs optionnels et le même nombre d'actions à chaque carte. Par exemple, si une carte inclut une image et deux actions, chaque carte doit inclure une image et deux actions.
{% endalert %}

#### Comportement au clic {#on-click-behavior}

Pour les zones cliquables dans les messages enrichis et les cartes, sélectionnez **URI** pour le **comportement au clic**, puis saisissez la destination dans **Ouvrir l'URL**. Choisissez si l'URL s'ouvre dans LINE.

#### Personnalisation {#personalization}

Utilisez [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) pour personnaliser le texte, les images et les URL. Incluez une valeur par défaut pour la personnalisation Liquid afin que les profils avec des données incomplètes ne reçoivent pas de contenu vide.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Pour les langues écrites de droite à gauche, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Étape 4 : Configurer le suivi des clics {#step-4-configure-click-tracking}

Dans l'onglet **Paramètres**, utilisez le **suivi des clics** pour raccourcir et suivre les liens au moment de l'envoi. Le suivi des clics est activé par défaut pour les nouveaux messages et s'applique aux URL HTTP et HTTPS dans les messages texte, enrichis et à base de cartes.

Braze utilise `https://brz.ai` ou le domaine personnalisé configuré pour le groupe d'abonnement. Vous pouvez personnaliser les URL suivies avec Liquid. Pour la configuration par type de message, le comportement de test, les domaines personnalisés et le reciblage, consultez [Suivi des clics LINE]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/line_click_tracking).

### Étape 5 : Prévisualiser et tester votre message {#step-5-preview-and-test-your-message}

Accédez à l'onglet **Aperçu et test** pour prévisualiser le message en tant qu'utilisateur ou envoyer un message LINE de test à un groupe de test de contenu ou à un utilisateur individuel.

![L'onglet Aperçu et test affichant un aperçu d'un message de test.]({% image_buster /assets/img/line/test_preview.png %})

Pour les exigences et les étapes de test, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

### Étape 6 : Compléter le reste de votre campagne ou Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Choisir un calendrier de livraison ou un déclencheur {#choose-a-delivery-schedule-or-trigger}

Envoyez des messages LINE à une heure planifiée ou en réponse à une action ou un déclencheur API. Pour les options de planification et de déclenchement, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Configurez les contrôles de livraison tels que la [rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) et la [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Pour la livraison par événement, définissez la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Choisir les utilisateurs à cibler {#choose-users-to-target}

[Ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en sélectionnant des Segments et des filtres. Braze calcule l'appartenance exacte au Segment avant d'envoyer le message.

LINE contrôle le statut d'abonnement de chaque utilisateur. Un utilisateur doit avoir un `native_line_id` et suivre le canal LINE associé au groupe d'abonnement sélectionné pour recevoir le message. Pour en savoir plus, consultez [Statut d'abonnement LINE]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line).

#### Choisir les événements de conversion {#choose-conversion-events}

Utilisez les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) pour mesurer les actions après qu'un utilisateur a reçu la campagne. Définissez une fenêtre de conversion allant jusqu'à 30 jours.

{% endtab %}
{% tab Canvas %}

Complétez les sections restantes de votre Canvas. Pour les calendriers d'entrée, les paramètres d'audience et les contrôles d'envoi, consultez [Créer un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

Vous pouvez utiliser les messages LINE entrants pour démarrer ou bifurquer un Canvas en fonction de mots déclencheurs. Pour les exigences de comportement et de casse, consultez [Envoyer des messages aux utilisateurs LINE]({{site.baseurl}}/user_guide/channels/line/message_users).

{% endtab %}
{% endtabs %}

### Étape 7 : Vérifier et déployer {#step-7-review-and-deploy}

Une fois que vous avez terminé de créer votre campagne ou Canvas, vérifiez ses détails et testez le message avant de l'envoyer.

Après le lancement, utilisez les [rapports LINE]({{site.baseurl}}/user_guide/channels/line/reporting) pour examiner les performances des messages.

## Points à retenir {#things-to-know}

- Un message LINE peut contenir entre un et cinq bulles de messages.
- Un groupe d'abonnement correspond à un canal LINE, et toutes les variantes d'une Campaign doivent utiliser le même groupe d'abonnement.
- LINE est la source de vérité pour le statut d'abonnement. Les utilisateurs qui ne suivent pas le canal LINE sélectionné ne reçoivent pas le message.
- LINE ne calcule les statistiques d'ouverture et de clics que lorsque plus de 20 utilisateurs effectuent l'événement un jour donné.