---
nav_title: Contexte
article_title: Contexte
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Cet article de référence explique comment créer et utiliser les étapes Contexte dans votre Canvas."
tool: Canvas

---

# Contexte {#context}

> Les étapes Contexte vous permettent de créer et de mettre à jour une ou plusieurs variables pour un utilisateur au fil de sa progression dans un Canvas. Par exemple, si vous avez un Canvas qui gère des remises saisonnières, vous pouvez utiliser une variable de contexte pour stocker un code de réduction différent à chaque fois qu'un utilisateur entre dans le Canvas.

## Fonctionnement {#how-it-works}

![Une étape Contexte comme première étape d'un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les étapes Contexte vous permettent de créer et d'utiliser des données temporaires pendant le parcours d'un utilisateur dans un Canvas spécifique. Ces données n'existent que dans ce parcours Canvas et ne persistent pas entre différents Canvas ni en dehors de la session.

Les variables de contexte n'existent que pour ce parcours Canvas spécifique. Elles ne modifient pas le profil de l'utilisateur de manière permanente et n'apparaissent pas dans d'autres Canvas. Elles sont donc idéales pour les informations temporaires qui ne sont pertinentes que pour une campagne ou un workflow spécifique.

{% alert tip %}
Pour une référence complète sur les variables de contexte, y compris les types de données, l'utilisation et les bonnes pratiques, consultez la [Référence des variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).
{% endalert %}

Dans une étape Contexte, vous pouvez définir ou mettre à jour jusqu'à 10 variables de contexte. Ces variables peuvent être utilisées pour personnaliser les délais, segmenter les utilisateurs de manière dynamique et enrichir les messages tout au long du Canvas. Par exemple, vous pourriez créer une variable de contexte pour l'heure de vol prévue d'un utilisateur, puis l'utiliser pour définir des délais personnalisés et envoyer des rappels.

Vous pouvez définir des variables de contexte de deux manières :

- **À l'entrée du Canvas :** Les propriétés de l'événement personnalisé ou du déclencheur API sont automatiquement renseignées en tant que variables de contexte.
- **Dans une étape Contexte :** Définissez ou mettez à jour manuellement les variables de contexte en ajoutant une étape Contexte.

Chaque variable de contexte nécessite un nom, un type de données et une valeur (définie à l'aide de Liquid ou de l'outil Ajouter une personnalisation). Une fois définie, vous pouvez référencer les variables de contexte dans tout le Canvas à l'aide de Liquid, par exemple {% raw %}`{{context.${flight_time}}}`{% endraw %}. Dans le champ **Context variable name**, vous pouvez également saisir le nom de la variable de contexte ou le sélectionner dans le menu déroulant de l'éditeur d'étape. Pour plus de détails, consultez la [Référence des variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

Chaque entrée dans le Canvas redéfinit les variables de contexte en fonction des dernières données d'entrée et de la configuration du Canvas, ce qui permet aux utilisateurs d'avoir plusieurs parcours actifs avec leur propre contexte. Par exemple, si un client a deux vols à venir, il aura deux états de parcours distincts s'exécutant simultanément&#8212;chacun avec ses propres variables de contexte spécifiques au vol, comme l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés concernant son vol de 14 h vers New York tout en envoyant des mises à jour différentes concernant son vol de 8 h vers Los Angeles le lendemain, de sorte que chaque message reste pertinent par rapport à la réservation spécifique.

### Traitement des utilisateurs et mise en lots {#user-processing-and-batching}

Les étapes Contexte traitent les utilisateurs par lots pour optimiser les performances. Lorsque les utilisateurs entrent dans une étape Contexte, Braze les traite par lots de 1 000 utilisateurs par défaut. Ces lots sont traités en parallèle, mais au sein de chaque lot, les utilisateurs sont traités séquentiellement.

Cela signifie :

**Exemple** : Si 3 500 utilisateurs entrent dans une étape Contexte avec du contenu connecté qui prend 650 ms par utilisateur :
- Braze crée 4 lots d'utilisateurs (1 000, 1 000, 1 000 et 500 utilisateurs dans cet exemple).
- Chaque lot traite les utilisateurs séquentiellement, donc un lot de 1 000 utilisateurs prend environ 10,8 minutes (650 secondes ; 1 000 × 650 ms).
- Les lots se terminent à des moments différents, de sorte que les utilisateurs arrivent progressivement à l'étape suivante au fur et à mesure que leur lot se termine.
- Les premiers utilisateurs peuvent atteindre l'étape suivante plusieurs minutes avant les derniers utilisateurs, en fonction de la taille du lot et des temps de réponse du contenu connecté.

Sans contenu connecté, les étapes Contexte sont traitées beaucoup plus rapidement car il n'y a pas d'appels API externes à attendre.

## Considérations {#considerations}

- Vous pouvez définir jusqu'à 10 variables de contexte par étape Contexte.
- Chaque variable nécessite un nom unique (lettres, chiffres et underscores uniquement, jusqu'à 100 caractères).
- La taille totale de toutes les variables d'une étape ne peut pas dépasser 50 Ko.
- Les variables transmises via des déclencheurs API partagent le même espace de noms que celles créées dans les étapes Contexte ; redéfinir une variable dans une étape Contexte remplace la valeur de l'API.

Pour plus de détails et des usages avancés, consultez la [Référence des variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

## Créer une étape Contexte {#creating-a-context-step}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Ajoutez une étape à votre Canvas, puis glissez-déposez le composant depuis la barre latérale, ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> et sélectionnez **Context**.

### Étape 2 : Définir les variables {#step-2-define-the-variables}

{% alert note %}
Vous pouvez définir jusqu'à 10 variables de contexte pour chaque étape Contexte.
{% endalert %}

Pour définir une variable de contexte :

1. Donnez un **nom** à votre variable de contexte.
2. Sélectionnez un [type de données]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types).
3. Rédigez une expression Liquid manuellement ou utilisez **Add Personalization** pour créer un extrait de code Liquid à partir d'attributs existants.
4. Sélectionnez **Preview** pour vérifier la valeur de votre variable de contexte.
5. (Facultatif) Pour ajouter des variables supplémentaires, sélectionnez **Add Context variable** et répétez les étapes 1 à 4.
6. Lorsque vous avez terminé, sélectionnez **Done**.

Vous pouvez maintenant utiliser votre variable de contexte partout où vous utilisez Liquid, par exemple dans les étapes Message et Mise à jour utilisateur, en sélectionnant **Add Personalization**. Dans le champ **Context variable name**, vous pouvez également saisir le nom de la variable de contexte ou le sélectionner dans le menu déroulant de l'éditeur d'étape. Pour un guide complet, consultez la [Référence des variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

{% alert important %}
Lorsque vous référencez des variables de contexte, utilisez toujours le format {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filtres de variables de contexte {#context-variable-filters}

Vous pouvez créer des filtres à l'aide de variables de contexte dans les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) et [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split).

Pour orienter les utilisateurs en fonction de la réponse d'une [étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), ajoutez l'étape Agent avant votre étape Parcours d'audience ou Arbre décisionnel. L'étape Agent stocke sa sortie dans le contexte Canvas, que vous pouvez évaluer avec des filtres de variables de contexte dans ces étapes de branchement.

Si l'agent renvoie un objet et que vous souhaitez filtrer sur une propriété imbriquée, saisissez le chemin dans le champ **Context variable name** en utilisant la notation par points au lieu du seul nom de la variable de niveau supérieur (par exemple, `intent_agent.persona` lorsque `persona` est imbriqué sous `intent_agent`).

Pour la configuration des filtres, la logique de comparaison et des exemples avancés, consultez la [Référence des variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Prévisualiser les parcours utilisateur {#previewing-user-paths}

Nous vous recommandons de tester et de [prévisualiser vos parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) pour vous assurer que vos messages sont envoyés à la bonne audience et que les variables de contexte produisent les résultats attendus.

{% alert note %}
Si vous prévisualisez votre Canvas dans la section **Preview & Test Send** de l'éditeur, l'horodatage dans l'aperçu du message de test **n'est pas** standardisé en UTC, car ce panneau génère les aperçus sous forme de chaînes de caractères. Cela signifie que si un Canvas est configuré pour accepter un objet `time`, l'aperçu du message ne reflète pas fidèlement ce qui se passe lorsque le Canvas est en production. Pour tester votre Canvas de la manière la plus précise, nous vous recommandons de prévisualiser les parcours utilisateur à la place.
{% endalert %}

Veillez à observer les scénarios courants qui créent des variables de contexte invalides. Lors de la prévisualisation de votre parcours utilisateur, vous pouvez visualiser les résultats des étapes de délai personnalisées utilisant des variables de contexte, ainsi que toute comparaison d'étape d'audience ou de décision qui associe les utilisateurs à des variables de contexte.

Si la variable de contexte est valide, vous pouvez la référencer dans tout votre Canvas. En revanche, si la variable de contexte n'a pas été créée correctement, les étapes suivantes de votre Canvas ne fonctionneront pas correctement non plus. Par exemple, si vous créez une étape Contexte pour attribuer aux utilisateurs une heure de rendez-vous et que vous définissez la valeur de l'heure de rendez-vous à une date passée, l'e-mail de rappel dans votre étape Message ne sera pas envoyé.

## Convertir les chaînes de contenu connecté en JSON {#converting-connected-content-strings-to-json}

Lorsque vous effectuez un [appel de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) dans une étape Contexte, le JSON renvoyé par l'appel est évalué comme un type de données chaîne de caractères par souci de cohérence et de prévention des erreurs. Si vous souhaitez convertir cette chaîne en JSON, utilisez `as_json_string`. Par exemple :

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Résolution des problèmes {#troubleshooting}

### Variables de contexte invalides {#invalid-context-variables}

Une variable de contexte est considérée comme invalide lorsque :

- Un appel à un contenu connecté intégré échoue.
- L'expression Liquid au moment de l'exécution renvoie une valeur qui ne correspond pas au type de données ou qui est vide (null).

Par exemple, si le type de données de la variable de contexte est **Nombre** mais que l'expression Liquid renvoie une chaîne de caractères, elle est invalide.

Dans ces cas :
- L'utilisateur passe à l'étape suivante.
- L'analytique de l'étape Canvas comptabilise cela comme _Non mis à jour_.

Lors de la résolution des problèmes, surveillez l'indicateur _Non mis à jour_ pour vérifier que votre variable de contexte se met à jour correctement. Si la variable de contexte est invalide, vos utilisateurs peuvent continuer dans votre Canvas au-delà de l'étape Contexte, mais risquent de ne pas être éligibles pour les étapes suivantes.

Consultez [Types de données]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types) pour les exemples de configuration de chaque type de données.

### Délais d'envoi avec le contenu connecté {#delays-in-sending-with-connected-content}

Tous les utilisateurs d'un lot sont traités avant que quiconque ne progresse. Une fois le traitement du lot terminé, les utilisateurs ayant réussi passent à l'étape suivante, tandis que les utilisateurs en échec font l'objet de nouvelles tentatives séparément — les utilisateurs ayant réussi n'attendent pas que les nouvelles tentatives aboutissent avant de progresser.

#### Comportement des nouvelles tentatives {#retry-behavior}

Dans les étapes Canvas (y compris les étapes Contexte), Braze utilise des mécanismes de nouvelles tentatives spécifiques au Canvas plutôt que le comportement standard de nouvelles tentatives du contenu connecté. Si un appel de contenu connecté échoue :

 - Pour les étapes Message, les appels de contenu connecté peuvent être réessayés jusqu'à cinq fois.
 - Pour toutes les autres étapes, Braze réessaie l'étape environ 13 fois avec des délais exponentiels.

Si toutes les tentatives échouent, l'utilisateur quitte le Canvas.

La balise `:retry` utilisée dans le contenu connecté standard ne s'applique pas aux appels de contenu connecté effectués dans les étapes Canvas. Les étapes Canvas disposent de leur propre logique de nouvelles tentatives optimisée pour les workflows Canvas.

Le temps nécessaire pour traiter tous les utilisateurs via une étape Contexte dépend de :

- Le nombre d'utilisateurs entrant dans l'étape
- L'utilisation ou non du contenu connecté (et son temps de réponse)
- La taille du lot (1 000 utilisateurs par lot par défaut)

Si votre endpoint de contenu connecté a des limites de débit, sachez que les étapes Contexte traitent les utilisateurs séquentiellement au sein de chaque lot, ce qui aide à respecter naturellement les limites de débit. Cependant, plusieurs lots sont traités en parallèle, alors assurez-vous que votre endpoint peut gérer les requêtes simultanées provenant de plusieurs lots.

## Standardisation de la cohérence des fuseaux horaires {#time-zone-consistency-standardization}

Avec la disponibilité générale de Canvas Contexte, toutes les propriétés d'événement d'horodatage par défaut dans les Canvas déclenchés par action sont en UTC. Ce changement s'inscrit dans un effort plus large visant à garantir une expérience plus prévisible et cohérente lors de la modification des étapes et des messages Canvas. Notez que ce changement impacte tous les Canvas déclenchés par action, que le Canvas en question utilise ou non une étape Contexte.

{% alert important %}
Dans tous les cas, nous recommandons fortement d'utiliser les [filtres Liquid time_zone]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) pour que les horodatages soient représentés dans le fuseau horaire souhaité. Vous pouvez consulter cette [question fréquente](#faq-example) pour un exemple.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Qu'est-ce qui a changé depuis la disponibilité générale de Canvas Contexte ? {#what-has-changed-since-canvas-context-became-generally-available}

Maintenant que Canvas Contexte est en disponibilité générale, les points suivants s'appliquent :

- Tous les horodatages avec un [type datetime]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) provenant des [propriétés d'événement déclencheur]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) dans les Canvas déclenchés par action sont en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Ce changement impacte tous les Canvas déclenchés par action, que le Canvas en question utilise ou non une étape Contexte.

#### Quelle est la raison de ce changement ? {#what-is-the-reason-for-this-change}

Ce changement s'inscrit dans un effort plus large visant à créer une expérience plus prévisible et cohérente lors de la modification des étapes et des messages Canvas.

#### Les Canvas déclenchés par API ou planifiés sont-ils impactés par ce changement ? {#are-api-triggered-or-scheduled-canvases-impacted-by-this-change}

Non.

#### Ce changement impacte-t-il les propriétés d'entrée Canvas ? {#does-this-change-impact-canvas-entry-properties}

Oui, cela impacte `canvas_entry_properties` si la `canvas_entry_property` est utilisée dans un Canvas déclenché par action et que le type de propriété est `time`. Dans tous les cas, nous recommandons d'utiliser les filtres Liquid `time_zone` pour que les horodatages soient représentés dans le fuseau horaire souhaité.

Voici un exemple de la marche à suivre :

| Liquid dans l'étape Message | Résultat | Est-ce la bonne manière de représenter les fuseaux horaires en Liquid ? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Non |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Non |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ce changement impacte-t-il les propriétés d'entrée Canvas ?" }

#### Quel est un exemple concret de la façon dont le nouveau comportement des horodatages pourrait affecter mes messages ? {#faq-example}

Imaginons un Canvas déclenché par action qui contient le contenu suivant dans une étape Message :

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Cela produit le message suivant :

```
Your appointment is scheduled for 2025-08-05 4:15 PM, we’ll see you then!
```

Comme aucun fuseau horaire n'est spécifié en Liquid, l'horodatage est ici en UTC.

Pour spécifier clairement un fuseau horaire, nous pouvons utiliser les filtres Liquid `time_zone` comme ceci :

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Cela produit le message suivant :

```
Your appointment is scheduled for 2025-08-05 8:15 AM, we'll see you then!
```

Comme le fuseau horaire America/Los Angeles est spécifié en Liquid, l'horodatage est ici en PST.

Le fuseau horaire préféré peut également être envoyé dans le payload des propriétés d'événement et utilisé dans la logique Liquid :

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### En quoi les variables de contexte diffèrent-elles des propriétés d'entrée Canvas ? {#how-do-context-variables-differ-from-canvas-entry-properties}

Les propriétés d'entrée Canvas sont incluses en tant que variables de contexte Canvas. Cela signifie que vous pouvez envoyer des propriétés d'entrée Canvas via l'API Braze et les référencer dans d'autres étapes, de manière similaire à l'utilisation d'une variable de contexte avec l'extrait de code Liquid.

### Les variables peuvent-elles se référencer mutuellement dans une même étape Contexte ? {#can-variables-reference-each-other-in-a-singular-context-step}

Oui. Toutes les variables d'une étape Contexte sont évaluées en séquence, ce qui signifie que vous pourriez avoir les variables de contexte suivantes configurées :

| Variable de contexte | Valeur | Description |
|---|---|---|
| `favorite_cuisine` | {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Le type de cuisine préféré d'un utilisateur. |
| `promo_code` | {% raw %}`EATFRESH`{% endraw %} | Le code de réduction disponible pour un utilisateur. |
| `personalized_message` | {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Un message personnalisé qui combine les variables précédentes. Dans une étape Message, vous pourriez utiliser l'extrait de code Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} pour référencer la variable de contexte et délivrer un message personnalisé à chaque utilisateur. Vous pourriez également utiliser une étape Contexte pour enregistrer la valeur du [code promotionnel]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create) et l'intégrer dans d'autres étapes tout au long d'un Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Les variables peuvent-elles se référencer mutuellement dans une même étape Contexte ?" }

Cela s'applique également entre plusieurs étapes Contexte. Par exemple, imaginez cette séquence :

1. Une étape Contexte initiale crée une variable appelée `JobInfo` avec la valeur `job_title`.
2. Une étape Message référence {% raw %}`{{context.${JobInfo}}}`{% endraw %} et affiche `job_title` à l'utilisateur.
3. Plus tard, une étape Contexte met à jour la variable de contexte en changeant la valeur de `JobInfo` en `job_description`.
4. Toutes les étapes suivantes qui référencent `JobInfo` utilisent désormais la valeur mise à jour `job_description`.

Les variables de contexte utilisent leur valeur la plus récente dans tout le Canvas, chaque mise à jour affectant toutes les étapes suivantes qui référencent cette variable.