---
nav_title: Propriétés de contexte et d'événement
article_title: Propriétés de contexte et d'événement
page_order: 4.2
page_type: reference
description: "Cet article de référence décrit les différences entre les propriétés de contexte et les propriétés d'événement, et quand utiliser chacune d'entre elles."
tool: Canvas
---

# Propriétés de contexte et d'événement {#context-and-event-properties}

> Cet article de référence couvre les informations relatives à `context` et `event_properties`, notamment quand utiliser chaque propriété et les différences de comportement. <br><br> Pour des informations générales sur les propriétés d'événements personnalisés, consultez [Propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Les propriétés de contexte et les propriétés d'événement fonctionnent différemment au sein de vos workflows Canvas. Les propriétés des événements ou des appels API qui déclenchent l'entrée d'un utilisateur dans un Canvas sont appelées `context`. Les propriétés des événements qui se produisent lorsqu'un utilisateur progresse dans un parcours Canvas sont appelées `event_properties`. La différence principale est que `context` ne se limite pas aux événements : il permet également d'accéder aux propriétés des payloads d'entrée dans les Canvas déclenchés par API.

Consultez le tableau suivant pour un résumé des différences entre les propriétés de contexte et les propriétés d'événement.

| | Propriétés de contexte | Propriétés d'événement |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistance** | Peuvent être référencées par toutes les étapes [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) pendant toute la durée d'un Canvas. | - Ne peuvent être référencées qu'une seule fois. <br> - Ne peuvent pas être référencées par les étapes Message suivantes. |
| **Comportement dans Canvas** | Vous pouvez référencer `context` dans n'importe quelle étape d'un Canvas. Pour le comportement après le lancement, consultez [Modifier les Canvas après le lancement]({{site.baseurl}}/post-launch_edits#canvas-entry-properties). | - Vous pouvez référencer `event_properties` dans la première étape Message **après** une étape [Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) où l'action effectuée est un événement personnalisé ou un événement d'achat. <br> - Ne peut pas se trouver après le parcours Tous les autres de l'étape Parcours d'action. <br> - D'autres composants non-Message peuvent se trouver entre les étapes Parcours d'action et Message. Si l'un de ces composants non-Message est une étape Parcours d'action, l'utilisateur peut emprunter le parcours Tous les autres de ce parcours d'action. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Propriétés de contexte et d'événement" }

{% details Détails de l'éditeur Canvas d'origine %}

Vous ne pouvez plus créer ni dupliquer de Canvas avec l'éditeur d'origine. Notez que le contexte Canvas n'est pas pris en charge dans l'éditeur Canvas d'origine. Cette section est donc disponible à titre de référence pour l'utilisation des propriétés d'entrée Canvas et des propriétés d'événement dans l'ancien workflow Canvas.

**Propriétés d'entrée Canvas :**
- Les propriétés d'entrées persistantes doivent être activées.
- Vous ne pouvez référencer `canvas_entry_properties` que dans la première étape complète d'un Canvas. Le Canvas doit être basé sur une action ou déclenché par API.

**Propriétés d'entrée :**
- Vous pouvez référencer `event_properties` dans n'importe quelle étape complète utilisant la livraison par événement dans un Canvas.
- Ne peuvent pas être utilisées dans les étapes complètes planifiées autres que la première étape complète d'un Canvas basé sur une action. Cependant, si un utilisateur utilise un [composant Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about), le comportement suit les règles actuelles du workflow Canvas pour `event_properties`.

**Propriétés d'événement :**
- Vous ne pouvez pas utiliser `event_properties` dans l'étape Message initiale. Vous devez plutôt utiliser `canvas_entry_properties` ou ajouter une étape Parcours d'action avec l'événement correspondant **avant** l'étape Message qui inclut `event_properties`.

{% enddetails %}

## Points importants {#things-to-know}

- Le contexte n'est disponible que pour référence dans Liquid. Pour filtrer sur les propriétés au sein du Canvas, utilisez plutôt la [segmentation par propriétés d'événement]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).
- Pour les canaux de messages in-app, vous pouvez référencer `context` et `event_properties` dans un Canvas. `event_properties` est accessible lorsqu'il est inclus dans la première étape du Canvas, car celle-ci est basée sur un déclencheur.
- Vous ne pouvez pas utiliser `event_properties` dans l'étape Message initiale. Vous pouvez plutôt utiliser `context` ou ajouter une étape Parcours d'action avec l'événement correspondant **avant** l'étape Message qui inclut `event_properties`.
- Lorsqu'une étape Parcours d'action contient un déclencheur « A envoyé un message entrant SMS » ou « A envoyé un message entrant WhatsApp », les étapes Canvas suivantes peuvent inclure une propriété Liquid SMS ou WhatsApp. Cela reflète le fonctionnement des propriétés d'événement dans les Canvas. Vous pouvez ainsi tirer parti de vos messages pour enregistrer et référencer des données first-party sur les profils utilisateur et la messagerie conversationnelle.

{% alert note %}
L'éligibilité de l'audience est évaluée une seule fois à l'entrée dans le Canvas. Si un utilisateur est fusionné pendant l'entrée, l'utilisateur identifié continue dans le Canvas et n'est pas réévalué par rapport aux critères de Segment du Canvas.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Horodatages pour les déclencheurs {#timestamps-for-triggers}

Si vous utilisez des horodatages avec un [type datetime]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) provenant d'événements qui déclenchent des Canvas basés sur une action, référencés via [context]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), les horodatages sont normalisés en UTC.

Compte tenu de ce comportement, Braze recommande fortement d'utiliser un filtre Liquid de fuseau horaire comme dans l'exemple suivant pour garantir que vos messages sont envoyés avec votre [fuseau horaire préféré]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters).

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

## Cas d'usage {#use-case}

![Une étape Parcours d'action suivie d'une étape Délai et d'une étape Message pour les utilisateurs qui ont ajouté un article à leur liste de souhaits, et un parcours pour tous les autres.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Pour mieux comprendre les différences entre `context` et `event_properties`, considérons ce scénario où les utilisateurs entrent dans un Canvas basé sur une action lorsqu'ils effectuent l'événement personnalisé « ajouter un article à la liste de souhaits ».

Le contexte est configuré dans l'étape [Planification d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) lors de la création d'un Canvas et correspond au moment où un utilisateur entre dans un Canvas. Le contexte peut également être référencé dans n'importe quelle étape Message.

Dans ce Canvas, le parcours utilisateur commence par une étape Parcours d'action pour déterminer si un utilisateur a ajouté un article à sa liste de souhaits. Si c'est le cas, l'utilisateur passe par un délai avant de recevoir le message « Nouvel article dans votre liste de souhaits ! » depuis l'étape Message.

La première étape Message d'un parcours utilisateur a accès aux `event_properties` personnalisées de votre étape Parcours d'action. Dans ce cas, nous pouvons inclure ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` dans cette étape Message comme partie du contenu de notre message. Si un utilisateur n'ajoute pas d'article à sa liste de souhaits, il emprunte le parcours Tous les autres, ce qui signifie que les `event_properties` ne peuvent pas être référencées et génèrent une erreur de paramètres invalides.

Notez que vous n'aurez accès aux `event_properties` que si votre étape Message peut être retracée jusqu'à un parcours autre que Tous les autres dans une étape Parcours d'action. Si l'étape Message est connectée à un parcours Tous les autres mais peut être retracée jusqu'à une étape Parcours d'action dans le parcours utilisateur, vous conservez tout de même l'accès aux `event_properties`. Pour plus d'informations sur ces comportements, consultez [Étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).