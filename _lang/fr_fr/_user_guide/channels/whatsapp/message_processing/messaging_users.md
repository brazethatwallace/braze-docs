---
nav_title: "Messages des utilisateurs"
article_title: "Messages des utilisateurs WhatsApp"
description: "Cet article de référence explique comment Braze gère les messages des utilisateurs."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Messages des utilisateurs {#user-messages}

> WhatsApp est un canal de communication bidirectionnelle. Non seulement votre marque peut envoyer des messages aux utilisateurs, mais ceux-ci peuvent également engager des conversations à l'aide de Campaigns et de Canvas basés sur des modèles. Il existe plusieurs façons de procéder, notamment les réponses rapides WhatsApp, les messages de liste et les mots déclencheurs. Les appels à l'action (CTA) des réponses rapides et des messages de liste sont un excellent moyen d'encourager l'engagement des utilisateurs avec vos messages WhatsApp.

## Déclencheurs basés sur l'action {#action-based-triggers}

Les Campaigns et les Canvas peuvent démarrer, se ramifier et subir des modifications en cours de parcours à partir d'un message WhatsApp entrant (un utilisateur envoyant un message à votre WhatsApp), comme un mot déclencheur.

Assurez-vous que votre mot déclencheur correspond à ce que vous attendez de la part des utilisateurs.

**Points importants :**
- Chaque lettre de votre mot déclencheur doit être en majuscule lors de la configuration. Braze n'exige pas que les mots déclencheurs entrants envoyés par les utilisateurs soient en majuscules. Par exemple, envoyer « jOin2023 » déclenchera quand même le Canvas ou la Campaign.
- Si aucun mot déclencheur n'est spécifié dans le déclencheur basé sur l'action de la planification d'entrée, la Campaign ou le Canvas s'exécutera pour TOUS les messages WhatsApp entrants. Cela inclut les messages qui correspondent à des phrases dans des Campaigns et des Canvas actifs, auquel cas l'utilisateur recevra deux messages WhatsApp.

{% tabs %}
{% tab Campaign %}

![Options de planification de Campaign basée sur l'action.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![Options de planification de Canvas basé sur l'action.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## Réponses non reconnues {#unrecognized-responses}

Nous vous recommandons d'inclure une option pour les réponses non reconnues dans les Canvas interactifs. Cela guide les utilisateurs pour comprendre quelles sont les invites disponibles et définit les attentes pour le canal. La gestion des attentes peut être particulièrement utile si vous disposez de canaux WhatsApp avec un chat d'agent en direct.
- Dans l'étape d'action, après avoir créé les groupes d'action pour les phrases de filtre personnalisées, ajoutez un groupe d'action supplémentaire pour « Envoyer un message WhatsApp », mais **ne cochez pas Where the message body**. Cela capturera toutes les réponses non reconnues des utilisateurs, de manière similaire à une clause « else ».
- Nous vous recommandons de répondre avec un message WhatsApp informant l'utilisateur que ce canal n'est pas géré par un agent et de le diriger vers un canal d'assistance si nécessaire.

## Réponses rapides {#quick-replies}

![Écran de téléphone montrant qu'un bouton d'appel à l'action répondra avec le texte du bouton cliqué.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Les réponses rapides apparaissent sous forme de boutons cliquables dans la conversation, mais fonctionnent comme si l'utilisateur avait répondu par du texte. Braze les traite ensuite comme des messages entrants et peut renvoyer des réponses prédéfinies en fonction du bouton cliqué. Utilisez l'étape d'action « Message WhatsApp entrant » lors de la création et du filtrage des réponses de vos utilisateurs.

![Un message WhatsApp affichant du texte et trois boutons d'appel à l'action.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configurer l'expérience de réponse rapide dans Canvas {#configure-the-quick-reply-experience-in-canvas}

#### Étape 1 : Créer vos CTA {#step-1-build-out-ctas}

Commencez par créer vos CTA de réponse rapide dans le [gestionnaire de modèles de messages WhatsApp](https://business.facebook.com/wa/manage/message-templates/) au sein d'un modèle de message.

![L'interface du gestionnaire de modèles de messages WhatsApp montrant comment créer un bouton CTA, en fournissant le type de bouton (personnalisé) et le texte du bouton.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Une fois votre modèle soumis et approuvé par WhatsApp, vous pouvez l'utiliser pour créer un Canvas dans Braze.

{% alert tip %}
Vous pouvez créer le Canvas avant de recevoir l'approbation de votre modèle de message.
{% endalert %}

#### Étape 2 : Créer votre Canvas {#step-2-build-your-canvas}

Ensuite, créez un Canvas avec une étape de message qui inclut votre modèle créé.

![Compositeur d'étape de message WhatsApp avec un modèle de réponse rapide rempli.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Créez une étape d'action qui suit l'étape de message. Créez un groupe par option de réponse rapide dans cette étape d'action.

![Un Canvas où l'action d'évaluation est « envoyer un message WhatsApp entrant ».]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

Pour chaque groupe d'options de réponse rapide, spécifiez le texte exact correspondant au bouton que vous souhaitez associer. Notez que les mots-clés doivent être en majuscules.

![Une étape de Canvas où l'action « envoyer un message WhatsApp entrant » est configurée pour s'envoyer lorsqu'un corps de message spécifique est reçu.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

Si vous souhaitez une réponse par défaut pour les utilisateurs qui répondent au message par du texte au lieu de réponses rapides, créez un groupe supplémentaire sans corps de message correspondant.

Continuez à construire le Canvas comme vous le feriez normalement à partir de ce point.

### Réponses {#responses}

Vous souhaiterez très probablement un message de réponse pour chaque réponse. Nous vous recommandons d'avoir une option « fourre-tout » pour les réponses en dehors du cadre des réponses rapides (par exemple pour les clients qui répondent avec un message général plutôt qu'une invite prédéterminée). Par exemple : « Nous sommes désolés, nous n'avons pas reconnu votre réponse. Pour les questions d'assistance, veuillez contacter <canal d'assistance>. »

![Un Canvas construit montrant les réponses pour chaque bouton d'appel à l'action.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Notez que vous pouvez utiliser toutes les actions suivantes offertes par le Canvas de Braze, telles que les messages en réponse, les mises à jour du profil utilisateur ou les webhooks Braze-à-Braze.

## Messages de liste {#list-messages}

Les messages de liste apparaissent sous forme de message avec une liste d'options cliquables. Chaque liste peut comporter plusieurs sections, et chaque liste peut contenir jusqu'à 10 lignes.

![Exemple d'un message de liste WhatsApp avec des lignes pour différents styles de mode.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Configurer l'expérience de message de liste dans Canvas {#configure-the-list-message-experience-in-canvas}

#### Étape 1 : Créer ou modifier un Canvas basé sur l'action existant {#step-1-create-or-edit-an-existing-action-based-canvases}

Vous ne pouvez ajouter des messages de liste WhatsApp qu'aux Canvas basés sur l'action, car ils doivent être envoyés en réponse à un message utilisateur.

#### Étape 2 : Créer une étape de message WhatsApp {#step-2-create-a-whatsapp-message-step}

Ajoutez une [étape de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) WhatsApp, puis sélectionnez la disposition du message de réponse **List Message**.

![Une collection sélectionnable des différents types de messages de réponse WhatsApp que vous pouvez créer, y compris « List Message ».]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Ajoutez un nom de **List button** que les utilisateurs sélectionneront pour afficher votre liste. Ensuite, utilisez les champs dans **List content** pour créer votre liste :

- **Section :** Ajoutez jusqu'à 10 sections pour regrouper et organiser les éléments de votre liste. Par exemple, un détaillant de vêtements pourrait utiliser des sections pour organiser par styles saisonniers (comme printemps, été, automne et hiver) ou par articles vestimentaires (comme hauts, bas et chaussures).
- **Row :** Ajoutez jusqu'à 10 lignes, ou éléments de liste, dans l'ensemble des sections.
- **Row description (optional) :** Ajoutez une description facultative à toutes les lignes (éléments de liste).

![La section « List content » remplie avec deux sections, et plusieurs lignes et descriptions de lignes.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Modifiez l'ordre des sections et des lignes en sélectionnant et en faisant glisser l'icône à côté de leurs noms.

![Glissement d'une section de liste vers un nouvel emplacement.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

De retour dans le compositeur de Canvas, ajoutez un [parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) après l'étape de message avec un groupe pour chaque réponse de liste. Dans chaque groupe :

1. Ajoutez un déclencheur pour **Sent inbound WhatsApp subscription group** et sélectionnez le groupe d'abonnement WhatsApp correspondant.
2. Cochez la case **Where the message body**.
3. Spécifiez le contenu d'une ligne (ou élément de liste).

![Compositeur pour un parcours d'action avec des groupes pour différents styles vestimentaires.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Continuez à construire votre Canvas.

### Créer des parcours d'action pour les descriptions longues {#creating-actions-paths-for-long-descriptions}

Si vous avez des descriptions de lignes, vous devez utiliser **Matches regex** pour spécifier une ligne. Par exemple, si vous souhaitez spécifier une ligne avec la description « Notre nouveau style qui se porte par-dessus votre paire préférée de bottines », vous pourriez utiliser une [expression régulière]({{site.baseurl}}/user_guide/audience/segments/regex) avec « bottines ».

![Un déclencheur WhatsApp utilisant le filtre « Matches regex » pour capturer les messages de réponse contenant « ankle boots ».]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Considérations {#considerations}

### Exigences de délai pour les messages de réponse {#timing-requirements-for-response-messages}

Les messages de réponse doivent être envoyés dans les 24 heures suivant la réception du message d'un utilisateur. Pour aider à créer des expériences réussies, Braze vérifie la logique du message pour confirmer qu'il existe un message entrant de l'utilisateur en amont qui débloque le message de réponse.

Les événements suivants débloquent les messages de réponse :

- Message entrant
  - [Parcours d'action]({{site.baseurl}}/action_paths) ou [entrée basée sur l'action]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) avec le déclencheur **Envoyer un message WhatsApp entrant**.

![Une étape d'entrée basée sur l'action avec le déclencheur « Envoyer un message WhatsApp entrant ».]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [Entrée déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)
- Message produit entrant
  - Événement [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events?tab=ecommerce.cart_updated)

![Un parcours d'action avec le déclencheur d'un événement personnalisé effectué `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

### Filtrage par un attribut de temps personnalisé {#filtering-by-a-custom-time-attribute}

Si l'audience de votre Campaign ou Canvas WhatsApp basé sur l'action dépend d'un attribut de temps personnalisé se situant dans une fenêtre relative (par exemple, entre maintenant et les prochaines 24 heures), combinez deux filtres comme décrit dans [Temps]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#time).

### Stockage des médias entrants et expiration des URL {#inbound-media-storage-and-url-expiration}

Lorsqu'un utilisateur envoie un message WhatsApp contenant un média (comme une image, un fichier audio ou un document), Braze stocke ce média dans Amazon S3 pendant 30 jours à compter de la réception du message.

Cependant, le champ Liquid `inbound_media_urls`, qui référence l'URL de ce média, est valide pendant sept jours à compter de la réception du message entrant par Braze. Comme l'URL est générée une seule fois à la réception et n'est pas régénérée, la fenêtre de sept jours s'applique quel que soit le moment où vous accédez au champ. C'est la plus courte des deux limites qui s'applique, donc en pratique, `inbound_media_urls` doit être considéré comme valide pendant sept jours maximum.

{% alert note %}
Si vous enregistrez une valeur `inbound_media_urls` dans un attribut personnalisé utilisateur pour une utilisation ultérieure, tenez compte de cette expiration de sept jours. Toute tentative d'accès à l'URL après son expiration entraînera un lien cassé.
{% endalert %}