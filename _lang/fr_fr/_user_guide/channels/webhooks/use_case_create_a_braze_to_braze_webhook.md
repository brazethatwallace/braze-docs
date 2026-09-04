---
nav_title: "Cas d'usage : Créer un webhook Braze-à-Braze"
article_title: "Cas d'usage : Créer un webhook Braze-à-Braze"
page_order: 2
channel:
  - webhooks
description: "Cet article de référence explique quand utiliser la Mise à jour utilisateur par rapport aux webhooks Braze-à-Braze et comment créer un webhook Braze-à-Braze."
---

# Créer un webhook Braze-à-Braze {#create-a-braze-to-braze-webhook}

> Les webhooks Braze-à-Braze vous permettent d'appeler la [REST API de Braze]({{site.baseurl}}/api/basics) depuis Braze en utilisant un [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) dans une [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas). Utilisez-les pour des tâches d'orchestration comme le déclenchement d'un [Canvas déclenché par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Pour mettre à jour les [attributs utilisateur]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), les [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou les [achats]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) depuis un Canvas, utilisez plutôt la [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Elle est conçue pour les modifications de profil utilisateur et traite les mises à jour de manière plus efficace.

Pour tirer le meilleur parti de cet article, vous devez être familier avec [le fonctionnement des webhooks]({{site.baseurl}}/user_guide/channels/webhooks) et savoir comment [créer un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) dans Braze.

## Utiliser Envoyer vers une destination pour déclencher un autre Canvas {#use-send-to-destination-for-triggering-another-canvas}

Pour déclencher un second Canvas depuis un Canvas, utilisez [Envoyer vers une destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) au lieu d'un webhook Braze-to-Braze. Ce composant Canvas est spécialement conçu pour connecter les parcours Canvas et offre un moyen plus simple et plus efficace d'envoyer des utilisateurs d'un Canvas à un autre.

Envoyer vers une destination évalue les utilisateurs par rapport aux critères d'entrée et d'audience du Canvas de destination lorsqu'ils atteignent l'étape, sans nécessiter de configuration de webhook ni de clés API. Les utilisateurs qui remplissent les critères entrent dans le Canvas de destination et peuvent poursuivre leur parcours dans le Canvas source si des étapes supplémentaires suivent.

{% alert tip %}
Ajoutez [Envoyer vers une destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) à votre Canvas pour envoyer des utilisateurs vers un autre parcours Canvas sans configurer de webhooks ni d'appels API.
{% endalert %}

## Utiliser User Update pour les modifications de données utilisateur {#use-user-update-for-user-data-changes}

Pour mettre à jour les profils utilisateur depuis un Canvas, y compris la modification d'[attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), l'enregistrement d'[événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou l'enregistrement d'[achats]({{site.baseurl}}/user_guide/data/activation/events/purchase_events), utilisez [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) plutôt qu'un webhook Braze-vers-Braze.

User Update regroupe plusieurs modifications et les envoie par lots, ce qui est plus rapide que les webhooks. Il est plus facile à configurer qu'un webhook et prend en charge les mises à jour complexes grâce à son [composeur JSON avancé]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Par exemple, pour compter le nombre de fois qu'un utilisateur a vu un message, utilisez la [fonctionnalité d'incrémentation et de décrémentation]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values) de User Update plutôt qu'un webhook Braze-vers-Braze.

{% alert tip %}
Ajoutez [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) à votre Canvas pour mettre à jour les attributs, événements et achats d'un utilisateur à l'aide d'un composeur JSON.
{% endalert %}

## Quand utiliser un webhook Braze-à-Braze {#when-to-use-a-braze-to-braze-webhook}

User Update peut gérer pratiquement toutes les mêmes tâches qu'un webhook Braze-à-Braze pour la mise à jour des profils utilisateur. Pour des mises à jour complexes allant au-delà de simples attributs personnalisés, vous pouvez utiliser le [compositeur JSON avancé]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor).

Send to Destination offre un moyen plus simple de déclencher un second Canvas depuis un Canvas sans avoir besoin de configurer un webhook.

Vous pouvez utiliser un webhook Braze-à-Braze lorsque vous devez appeler la [REST API]({{site.baseurl}}/api/basics) de Braze depuis Braze pour des scénarios qui ne disposent pas d'un composant Canvas dédié. Parmi les exemples courants :

- Déclencher une [Campaign déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) depuis un Canvas
- Appeler d'autres [endpoints de messaging]({{site.baseurl}}/api/endpoints/messaging) pour des schémas d'orchestration où un workflow dans Braze doit invoquer une API qui ne dispose pas d'un composant Canvas dédié

Pour les mises à jour d'utilisateurs dans Canvas, utilisez [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Pour déclencher un autre Canvas, utilisez [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).

## Prérequis {#prerequisites}

Pour créer un webhook Braze-à-Braze, vous avez besoin d'une [clé API]({{site.baseurl}}/api/basics) disposant des permissions pour l'endpoint que vous souhaitez atteindre. Par exemple, pour déclencher un Canvas déclenché par API, vous avez besoin d'une clé API avec la permission `canvas.trigger.send`.

## Configuration de votre webhook Braze vers Braze {#setting-up-your-braze-to-braze-webhook}

Le workflow général pour créer un webhook Braze vers Braze suit ces étapes :

1. [Créez un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) en tant que Campaign ou composant Canvas.
2. Choisissez **Modèle vierge**.
3. Dans l'onglet **Composer**, spécifiez l'**URL du webhook** et le **corps de la requête** pour votre cas d'usage d'API.
4. Dans l'onglet **Paramètres**, spécifiez votre **méthode HTTP** et les **en-têtes de requête** selon les exigences de l'endpoint.
5. Configurez tous les paramètres de distribution supplémentaires (par exemple, le déclenchement à partir d'un événement personnalisé) et finalisez le reste de votre Campaign ou Canvas.

## Déclencher un second Canvas à partir d'un Canvas initial {#trigger-a-second-canvas-from-an-initial-canvas}

Dans ce cas d'usage, vous créez deux Canvas et utilisez un webhook Braze-to-Braze pour déclencher le second Canvas à partir du premier. Cela agit comme un déclencheur d'entrée lorsqu'un utilisateur atteint un certain point dans un autre Canvas.

{% alert note %}
Le déclencheur **Interact with Canvas Step** est uniquement disponible pour les Campaigns, pas pour l'entrée par action dans un Canvas. Si vous devez déclencher un Canvas lorsqu'un utilisateur atteint une étape spécifique dans un autre Canvas, utilisez cette approche de webhook Braze-to-Braze ou le composant Canvas [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).
{% endalert %}

1. Commencez par créer votre second Canvas, celui qui doit être déclenché par votre Canvas initial.
2. Pour la **planification d'entrée** du Canvas, sélectionnez **API-Triggered**.
3. Notez votre **Canvas ID**. Vous en aurez besoin dans une étape ultérieure.
4. Continuez à construire les étapes de votre second Canvas, puis enregistrez le Canvas.
5. Enfin, créez votre premier Canvas. Trouvez l'étape où vous souhaitez déclencher le second Canvas et créez une nouvelle étape avec un webhook.

Référez-vous aux éléments suivants lors de la configuration de votre webhook :

- **URL du webhook :** L'[URL de votre endpoint REST]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) suivi de `/canvas/trigger/send`. Par exemple, pour l'instance `US-06`, l'URL serait `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corps de la requête :** texte brut

### En-têtes de requête et méthode {#request-headers-and-method}

Braze nécessite un en-tête HTTP pour l'autorisation qui inclut votre clé API et un autre qui déclare votre type de contenu.

- **En-têtes de requête :**
  - **Authorization :** `Bearer YOUR_API_KEY`
  - **Content-Type :** `application/json`
- **Méthode HTTP :** `POST`

Remplacez `YOUR_API_KEY` par une clé API Braze disposant des permissions `canvas.trigger.send`. Vous pouvez créer une clé API dans le tableau de bord de Braze en accédant à **Paramètres** > **Clés API**.

![En-têtes de requête pour le webhook montrant les champs Authorization et Content-Type dans le tableau de bord de Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corps de la requête {#request-body}

Ajoutez votre requête `/canvas/trigger/send` dans le champ de texte. Pour plus de détails, consultez [Envoi de messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Voici un exemple de corps de requête pour cet endpoint, où `your_canvas_id` est le Canvas ID de votre second Canvas :

{% raw %}
```json
{
  "canvas_id": "your_canvas_id",
  "recipients": [
    {
      "external_user_id": "{{${user_id}}}"
    }
  ]
}
```
{% endraw %}

Lorsqu'un utilisateur atteint cette étape de webhook dans le premier Canvas, Braze déclenche le second Canvas pour cet utilisateur via l'API.

## Considérations {#considerations}

- **Mise à jour des utilisateurs :** Pour mettre à jour les profils utilisateur depuis un Canvas (attributs, événements, achats), utilisez la fonctionnalité [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) plutôt que des webhooks Braze-à-Braze, pour une meilleure efficacité et un meilleur rapport coût-efficacité.
- Les webhooks Braze-à-Braze sont soumis aux [limites de débit]({{site.baseurl}}/api/api_limits) des endpoints.
- Les mises à jour du profil utilisateur consomment des [points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points) qui sont comptabilisés dans votre consommation globale, tandis que le déclenchement d'un autre message via les endpoints de messaging ne les consomme pas.
- Pour cibler des [utilisateurs anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles), utilisez `braze_id` au lieu de `external_id` dans le corps de la requête de votre webhook.
- Vous pouvez enregistrer votre webhook Braze-à-Braze en tant que [modèle de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) pour le réutiliser.
- Vous pouvez consulter le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour visualiser et résoudre les échecs de webhooks.