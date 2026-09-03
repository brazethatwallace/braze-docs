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

## Utiliser Envoyer à la destination pour déclencher un autre Canvas {#use-send-to-destination-for-triggering-another-canvas}

Pour déclencher un second Canvas depuis un Canvas, utilisez [Envoyer à la destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) plutôt qu'un webhook Braze-à-Braze. Ce composant Canvas est conçu spécifiquement pour connecter des parcours Canvas et offre un moyen plus simple et plus efficace d'envoyer des utilisateurs d'un Canvas à un autre.

Envoyer à la destination évalue les utilisateurs par rapport aux critères d'entrée et d'audience du Canvas de destination lorsqu'ils atteignent l'étape, sans nécessiter de configuration de webhook ni de clés API. Les utilisateurs qui remplissent les critères entrent dans le Canvas de destination et peuvent poursuivre leur parcours dans le Canvas source si des étapes supplémentaires suivent.

{% alert tip %}
Ajoutez [Envoyer à la destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) à votre Canvas pour envoyer des utilisateurs vers un autre parcours Canvas sans configurer de webhooks ni d'appels API.
{% endalert %}

## Utiliser la Mise à jour utilisateur pour les modifications de données utilisateur {#use-user-update-for-user-data-changes}

Pour mettre à jour les profils utilisateur depuis un Canvas, y compris la modification des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), l'enregistrement d'[événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou l'enregistrement d'[achats]({{site.baseurl}}/user_guide/data/activation/events/purchase_events), utilisez la [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) plutôt qu'un webhook Braze-à-Braze.

La Mise à jour utilisateur regroupe plusieurs modifications et les envoie par lots, ce qui est plus rapide que les webhooks. Elle est plus facile à configurer qu'un webhook et prend en charge les mises à jour complexes grâce à son [compositeur JSON avancé]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Par exemple, pour compter le nombre de fois qu'un utilisateur a vu un message, utilisez la fonctionnalité [Incrémenter et décrémenter]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values) de la Mise à jour utilisateur plutôt qu'un webhook Braze-à-Braze.

{% alert tip %}
Ajoutez une [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) à votre Canvas pour mettre à jour les attributs, événements et achats d'un utilisateur à l'aide d'un compositeur JSON.
{% endalert %}

## Quand utiliser un webhook Braze-à-Braze {#when-to-use-a-braze-to-braze-webhook}

La Mise à jour utilisateur peut gérer presque toutes les mêmes tâches qu'un webhook Braze-à-Braze pour la mise à jour des profils utilisateur. Pour les mises à jour complexes allant au-delà des simples attributs personnalisés, vous pouvez utiliser le [compositeur JSON avancé]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor).

Envoyer à la destination offre un moyen plus simple de déclencher un second Canvas depuis un Canvas sans nécessiter de configuration de webhook.

Vous pouvez utiliser un webhook Braze-à-Braze lorsque vous devez appeler la [REST API]({{site.baseurl}}/api/basics) de Braze depuis Braze pour des scénarios qui ne disposent pas d'un composant Canvas dédié. Les exemples courants incluent :

- Déclencher une [Campaign déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) depuis un Canvas
- Appeler d'autres [endpoints de messaging]({{site.baseurl}}/api/endpoints/messaging) pour des schémas d'orchestration où un flux de travail dans Braze doit invoquer une API qui ne dispose pas d'un composant Canvas dédié

Pour les mises à jour d'utilisateurs dans un Canvas, utilisez la [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Pour déclencher un autre Canvas, utilisez [Envoyer à la destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).

## Conditions préalables {#prerequisites}

Pour créer un webhook Braze-à-Braze, vous avez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec les autorisations pour l'endpoint que vous souhaitez atteindre. Par exemple, pour déclencher un Canvas déclenché par API, vous avez besoin d'une clé API avec l'autorisation `canvas.trigger.send`.

## Configurer votre webhook Braze-à-Braze {#setting-up-your-braze-to-braze-webhook}

Le flux de travail général pour créer un webhook Braze-à-Braze suit ces étapes :

1. [Créez un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) en tant que Campaign ou composant Canvas.
2. Choisissez **Modèle vierge**.
3. Dans l'onglet **Composer**, spécifiez l'**URL du webhook** et le **corps de la requête** pour votre cas d'usage API.
4. Dans l'onglet **Paramètres**, spécifiez votre **méthode HTTP** et les **en-têtes de requête** requis par l'endpoint.
5. Configurez les paramètres de distribution supplémentaires (par exemple, le déclenchement à partir d'un événement personnalisé) et finalisez le reste de votre Campaign ou Canvas.

## Déclencher un second Canvas depuis un Canvas initial {#trigger-a-second-canvas-from-an-initial-canvas}

Dans ce cas d'usage, vous créez deux Canvas et utilisez un webhook Braze-à-Braze pour déclencher le second Canvas depuis le premier. Cela agit comme un déclencheur d'entrée lorsqu'un utilisateur atteint un certain point dans un autre Canvas.

{% alert note %}
Le déclencheur **Interact with Canvas Step** n'est disponible que pour les Campaigns, pas pour l'entrée Canvas basée sur une action. Si vous devez déclencher un Canvas en fonction d'un utilisateur atteignant une étape spécifique dans un autre Canvas, utilisez cette approche de webhook Braze-à-Braze ou le composant Canvas [Envoyer à la destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).
{% endalert %}

1. Commencez par créer votre second Canvas — le Canvas qui doit être déclenché par votre Canvas initial.
2. Pour la **planification d'entrée** du Canvas, sélectionnez **API-Triggered**.
3. Notez votre **Canvas ID**. Vous en aurez besoin dans une étape ultérieure.
4. Continuez à construire les étapes de votre second Canvas, puis enregistrez le Canvas.
5. Enfin, créez votre premier Canvas. Trouvez l'étape où vous souhaitez déclencher le second Canvas et créez une nouvelle étape avec un webhook.

Consultez les informations suivantes lors de la configuration de votre webhook :

- **URL du webhook :** Votre [URL d'endpoint REST]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) suivie de `/canvas/trigger/send`. Par exemple, pour l'instance `US-06`, l'URL serait `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corps de la requête :** Raw Text

### En-têtes de requête et méthode {#request-headers-and-method}

Braze nécessite un en-tête HTTP pour l'autorisation qui inclut votre clé API et un autre qui déclare votre type de contenu.

- **En-têtes de requête :**
  - **Authorization :** `Bearer YOUR_API_KEY`
  - **Content-Type :** `application/json`
- **Méthode HTTP :** `POST`

Remplacez `YOUR_API_KEY` par une clé API Braze disposant des autorisations `canvas.trigger.send`. Vous pouvez créer une clé API dans le tableau de bord de Braze en accédant à **Paramètres** > **Clés API**.

![En-têtes de requête pour le webhook montrant les champs Authorization et Content-Type dans le tableau de bord de Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corps de la requête {#request-body}

Ajoutez votre requête `/canvas/trigger/send` dans le champ de texte. Pour plus de détails, consultez [Envoyer des messages Canvas via une distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Voici un exemple de corps de requête pour cet endpoint, où `your_canvas_id` est le Canvas ID de votre second Canvas :

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

Lorsqu'un utilisateur atteint cette étape webhook dans le premier Canvas, Braze déclenche le second Canvas pour cet utilisateur via l'API.

## Considérations {#considerations}

- **Mises à jour utilisateur :** Pour mettre à jour les profils utilisateur depuis un Canvas (attributs, événements, achats), utilisez la [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) plutôt que les webhooks Braze-à-Braze pour une meilleure efficacité et un meilleur rapport coût-efficacité.
- Les webhooks Braze-à-Braze sont soumis aux [limites de débit]({{site.baseurl}}/api/api_limits) des endpoints.
- Les mises à jour du profil utilisateur entraînent des [points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points) qui comptent dans votre consommation globale, tandis que le déclenchement d'un autre message via les endpoints de messaging n'en génère pas.
- Pour cibler les [utilisateurs anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles), utilisez `braze_id` au lieu de `external_id` dans le corps de la requête de votre webhook.
- Vous pouvez enregistrer votre webhook Braze-à-Braze en tant que [modèle de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) pour le réutiliser.
- Vous pouvez consulter le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour visualiser et résoudre les échecs de webhook.