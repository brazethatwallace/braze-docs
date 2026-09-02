---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 3
description: "Cet article de référence décrit les étapes nécessaires à la création d'un message WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows est une amélioration du canal WhatsApp existant, vous permettant de créer des expériences de communication interactives et dynamiques. Cette page fournit des instructions étape par étape pour utiliser WhatsApp Flows.

## Configuration des WhatsApp Flows {#setting-up-whatsapp-flows}

1. Connectez-vous à votre compte Meta.
2. Créez des Flows à partir de l'un des deux emplacements principaux :
    - **Account tools :** Accédez à l'onglet **Flows** pour afficher l'identifiant du Flow et créer un nouveau Flow.
    - **Manage templates :** Il s'agit de la méthode recommandée pour créer des Flows. Ici, vous pouvez générer des modèles et sélectionner une option Flow lors du processus de création du modèle.

![WhatsApp Manager avec une page pour créer un modèle Flows.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{% alert tip %}
Vous pouvez également créer un modèle de Flow Marketing ou Utilitaire dans Braze avec le [générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder). Créez et gérez le Flow lui-même dans le WhatsApp Manager de Meta, puis sélectionnez ce Flow lorsque vous construisez le modèle dans Braze.
{% endalert %}

{: start="3"}
3. Sélectionnez un Flow existant ou créez-en un. Si vous créez un Flow, choisissez entre deux options :
  - **Custom Form :** Pour des exigences spécifiques
  - **Pre-designed Elements :** Pour une configuration plus rapide

## Configuration des messages et réponses WhatsApp Flow {#configuring-whatsapp-flow-messages-and-responses}

{% tabs local %}
{% tab Message de modèle %}

1. Dans un Canvas Braze, créez une étape de message WhatsApp qui utilise le message de modèle contenant le Flow correspondant.
2. Continuez à créer votre modèle. Si nécessaire, ajoutez des médias, du contenu variable, ou les deux à votre message. Votre sélection de Flow est déterminée lors de la création du modèle, aucune information supplémentaire pour l'expérience de flow n'est donc requise.

![Compositeur de message WhatsApp utilisant un modèle WhatsApp Flow.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Message de réponse %}

1. Dans un Canvas Braze, créez une étape de message WhatsApp qui utilise un message de réponse et un message de flow.

![Une étape de message pour un type de message de réponse WhatsApp et une disposition de message Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Sélectionnez le Flow correspondant, puis continuez à créer votre message.

![Un compositeur de message de réponse Flow avec un menu déroulant étendu pour sélectionner un Flow.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Prévisualiser le Flow {#preview-flow}

Avant de lancer un Canvas avec un Flow, vous pouvez sélectionner **Preview Flow** pour prévisualiser le Flow directement dans Braze et confirmer qu'il se comporte comme prévu. Vous pouvez également interagir avec le Flow dans la prévisualisation pour vivre l'expérience de navigation d'un utilisateur, puis effectuer des ajustements en temps réel. Si un Flow contient plusieurs pages, vous pouvez interagir avec chaque page.

![Fenêtre de prévisualisation affichant un formulaire permettant à un utilisateur de finaliser son inscription.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Enregistrer la réponse complète du Flow {#full-flow}

Lorsque vous intégrez un message WhatsApp Flow dans un Canvas ou une campagne Braze, vous pouvez souhaiter capturer et utiliser des informations spécifiques que les utilisateurs soumettent via le Flow. Braze doit recevoir des informations supplémentaires concernant la structure de la réponse utilisateur, en particulier la forme attendue de la réponse JSON, afin de générer le schéma d'attribut personnalisé imbriqué (NCA) requis.

### Étape 1 : Générer l'attribut personnalisé du Flow {#step-1-generate-the-flow-custom-attribute}

{% tabs local %}
{% tab Méthode recommandée %}

La manière la plus simple de fournir à Braze les informations sur la structure de la réponse est d'enregistrer la réponse du Flow en tant qu'attribut personnalisé et d'effectuer un envoi test.

#### Utiliser un Flow qui n'a pas encore été utilisé dans Braze {#using-a-flow-that-hasnt-been-used-in-braze}

Si vous utilisez un Flow qui n'a pas été précédemment utilisé dans Braze, lorsque vous consultez la section **Flow Custom Attribute** dans **Compose Messages**, vous ne verrez peut-être aucune information. Cela signifie que le schéma n'a pas encore été généré.

![Section Meta Flow avec une option pour afficher l'attribut personnalisé du Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Pour résoudre ce problème, procédez comme suit :

1. Terminez la configuration de votre étape de message WhatsApp.
2. Confirmez que vous avez coché **Save Flow responses as a custom attribute**.
3. Envoyez-vous un message test et complétez le Flow en tant qu'utilisateur.

Braze dispose maintenant de la forme de la réponse JSON du Flow et peut générer l'attribut personnalisé.

{% endtab %}
{% tab Méthodes alternatives %}

Utilisez l'éditeur JSON avancé pour enregistrer les attributs de la réponse du Flow dans des attributs personnalisés, ou utilisez un Canvas multi-étapes pour enregistrer la réponse dans un attribut personnalisé imbriqué.

{% subtabs %}
{% subtab Éditeur JSON avancé %}

Dans l'éditeur JSON avancé, saisissez {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, où « flow_1 » est l'attribut personnalisé dans lequel vous souhaitez enregistrer le Flow.

![Étape de mise à jour utilisateur avec un éditeur JSON avancé.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab Éditeur d'interface %}

1. Confirmez que vous avez déjà créé un attribut personnalisé avec le type de données objet (« flow_1 » dans cet exemple) dans les paramètres des données de votre espace de travail.
2. Dans l'éditeur d'interface, utilisez le Liquid {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} pour remplir l'attribut personnalisé et enregistrer l'intégralité de la réponse du Flow de l'utilisateur. Vous devez remplir la valeur de la clé avec {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} avant de sélectionner l'attribut personnalisé que vous avez créé.

![Étape de mise à jour utilisateur utilisant l'éditeur d'interface.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Une fois que Braze reçoit une réponse du Flow, l'attribut personnalisé imbriqué sera enregistré avec le nom prescrit dans le profil utilisateur. Cet attribut personnalisé peut être utilisé lors de la création de Canvas.

![Une fenêtre affichant le contenu d'un attribut personnalisé « flow_1 ».]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 2 : Afficher la réponse enregistrée du Flow {#step-2-view-the-saved-flow-response}

Lorsque le Flow est terminé, Braze crée automatiquement un attribut personnalisé du Flow avec un nom basé sur l'ID du Flow. Vous pouvez ensuite accéder au profil utilisateur pour afficher la réponse enregistrée du Flow en tant qu'objet imbriqué dans la section **Custom Attributes**.

Une fois le schéma généré, la section **Custom Attribute** du Flow affichera la structure attendue, y compris les types de données anticipés pour chaque réponse (par exemple, « String » ou « String Array »).

![Fenêtre de détails des attributs personnalisés du Flow avec un menu déroulant de schéma.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Considérations {#considerations}

- **Attributs existants :** Si un attribut personnalisé pour un Flow particulier est déjà généré, le Flow se chargera avec les informations d'attribut disponibles. Dans ces cas, vous n'avez pas besoin d'envoyer un message test pour générer le schéma, car Braze reconnaît déjà les messages de réponse attendus.
- **Modifications du Flow :** Si vous apportez des modifications au Flow après la génération du schéma, vous devez envoyer un message test supplémentaire afin que Braze puisse comprendre que la forme de la réponse du Flow a changé et ajuster la structure de l'attribut en conséquence. Cette action est limitée à une fois toutes les 24 heures.
- **Cohérence :** L'attribut personnalisé du Flow généré est cohérent et sera le même attribut pour ce Flow spécifique, quel que soit le Canvas dans lequel il est utilisé.
- **Option manuelle :** Vous n'êtes pas obligé de cocher la case **Save Flow responses as a custom attribute**. Vous pouvez générer manuellement l'attribut personnalisé en [enregistrant des champs spécifiques des réponses du Flow dans un attribut personnalisé spécifique](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), ce qui évite de dupliquer les étapes utilisateur.

## Enregistrer des champs spécifiques des réponses de Flow dans un attribut personnalisé spécifique {#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute}

### Étape 1 : Créer un parcours d'action {#step-1-create-an-action-path}

Créez une étape Canvas de [parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) ou une campagne basée sur une action. Sélectionnez un déclencheur **Send a WhatsApp inbound message** et la condition **Responded to Flow**, puis sélectionnez le Flow concerné ou **Any Flow**.

![Un déclencheur pour les utilisateurs ayant envoyé un message WhatsApp entrant et répondu à n'importe quel Flow.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Étape 2 : Extraire des champs des réponses de Flow {#step-2-extract-fields-from-flow-responses}

Vous pouvez utiliser des attributs personnalisés imbriqués ou l'étiquette Liquid `json_parse` pour extraire des champs spécifiques des réponses de Flow.

{% tabs %}
{% tab Attributs personnalisés imbriqués %}

Pour enregistrer des parties spécifiques de la réponse de Flow de l'utilisateur, suivez toutes les étapes de la section [Enregistrer la réponse complète du Flow](#full-flow), **y compris le lancement du Canvas**. Le Canvas doit être lancé pour créer l'attribut personnalisé imbriqué que vous allez référencer. Après avoir lancé le Canvas et complété un Flow, procédez comme suit :

1. Créez une étape de mise à jour utilisateur ultérieure qui utilise l'éditeur d'interface.
2. Sélectionnez **Add Personalization**, puis sélectionnez **Nested Custom Attribute** et l'attribut de premier niveau correspondant où le Flow est stocké.

![Étape de mise à jour utilisateur avec une personnalisation d'attributs personnalisés imbriqués.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3. Sélectionnez l'attribut clé que vous souhaitez enregistrer et insérez le Liquid dans le champ **Key Value**.

![Fenêtre pour « flow_1 » avec les attributs à sélectionner.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. Choisissez l'attribut dans lequel vous souhaitez le stocker.
5. Envoyez un message de test pour tester le Flow.

{% endtab %}
{% tab Fonction d'analyse %}

Utilisez l'étiquette Liquid `json_parse` pour extraire des réponses spécifiques du Flow. Par exemple, vous pouvez récupérer le jeton du Flow et les options sélectionnées pour personnaliser un message de suivi.

Dans l'éditeur d'interface, sélectionnez les éléments suivants :

- **Attribute Name :** YOUR_CUSTOM_ATTRIBUTE (dans cet exemple : « First_name »)
- **Action :** Update
- **Key Value :** {% raw %} `{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}`{% endraw %}

![Composeur de messages WhatsApp avec un composant « Add Personalization » pour insérer une personnalisation de propriétés WhatsApp avec l'attribut personnalisé `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Lorsque vous êtes prêt, envoyez un message de test pour tester le Flow. Ensuite, lancez le Canvas !

{% endtab %}
{% endtabs %}

{% alert note %}
Un nouveau message WhatsApp « efface » la capacité du Canvas à utiliser (et réutiliser) la réponse Liquid du Flow. Assurez-vous donc que les messages de suivi interviennent après toutes les étapes de mise à jour utilisateur, les webhooks ou les autres étapes qui utilisent la réponse Liquid du Flow.
{% endalert %}

## Ajouter une étiquette de personnalisation Flow {#adding-a-flow-personalization-tag}

Pour utiliser la réponse Flow via Liquid avec les [étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), suivez les étapes suivantes :

1. Lors de la rédaction de votre message WhatsApp, sélectionnez <i class="fas fa-plus-circle"></i> **Ajouter une personnalisation** pour ouvrir la fenêtre **Ajouter une personnalisation**.
2. Sélectionnez **WhatsApp Properties** comme type de personnalisation et **inbound_flow_response** comme attribut personnalisé. Cela peut être utilisé pour enregistrer des informations dans les profils utilisateur, les inclure dans des messages ou les transmettre à d'autres services, comme les webhooks.

![Compositeur de messages WhatsApp avec un composant « Ajouter une personnalisation » permettant d'insérer une personnalisation de propriétés WhatsApp avec l'attribut personnalisé inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Pour toute question ou assistance supplémentaire, contactez le [support]({{site.baseurl}}/user_guide/administer/personal/braze_support).