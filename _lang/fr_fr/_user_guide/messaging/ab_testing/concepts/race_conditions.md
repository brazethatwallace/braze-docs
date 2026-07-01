---
nav_title: Conditions de concurrence
article_title: Conditions de concurrence
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Cet article aborde les meilleures pratiques à suivre pour éviter les conditions de concurrence qui affectent vos campagnes de communication."
toc_headers: h2
---

# Conditions de concurrence {#race-conditions}

> Une condition de concurrence se produit lorsqu'un résultat dépend de la séquence ou de la synchronisation de plusieurs événements. Par exemple, si la séquence d'événements souhaitée est « événement A » puis « événement B », mais que parfois « événement A » arrive en premier, et d'autres fois « événement B » arrive en premier, il s'agit d'une condition de concurrence. Cela peut entraîner des résultats inattendus ou des erreurs, car ces événements sont en concurrence pour l'accès aux ressources ou aux données partagées.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

Dans Braze, des conditions de concurrence peuvent se produire lorsque plusieurs actions sont déclenchées en même temps sur la base de données ou d'événements utilisateur. Par exemple, si un utilisateur déclenche plusieurs campagnes (comme l'inscription à une lettre d'information ou un achat), il se peut qu'il ne reçoive pas les messages dans le bon ordre.

## Types de conditions de concurrence {#types-of-race-conditions}

Les types de conditions de concurrence les plus courants peuvent se produire lorsque vous effectuez les opérations suivantes :

- Cibler de nouveaux utilisateurs
- Utiliser plusieurs endpoints API
- Correspondance entre les déclencheurs basés sur l'action et les filtres d'audience
- Utiliser le déclencheur « Interagir avec l'étape »

Examinez les scénarios suivants et mettez en œuvre les meilleures pratiques pour éviter ces conditions de concurrence.

## Scénario 1 : Cibler de nouveaux utilisateurs {#scenario-1-targeting-new-users}

Dans Braze, l'une des conditions de concurrence les plus courantes concerne les messages ciblant des utilisateurs nouvellement créés. L'ordre attendu des événements est le suivant :

1. Un utilisateur est créé ;
2. Ce même utilisateur est immédiatement ciblé pour un message, effectue un événement personnalisé ou enregistre un attribut personnalisé.

Cependant, dans certains cas, le deuxième événement se déclenche en premier. Cela signifie qu'un message tente d'être envoyé à un utilisateur qui n'existe pas encore. Par conséquent, l'utilisateur ne le reçoit jamais. Cela s'applique également aux événements ou aux attributs, lorsque l'événement ou l'attribut tente d'être enregistré sur un profil utilisateur qui n'a pas encore été créé.

Dans le cas des messages in-app, le message in-app doit être chargé sur l'appareil de l'utilisateur avant d'être déclenché. Si l'événement déclencheur fait partie du processus d'onboarding, ou si l'utilisateur sort du segment pour l'événement personnalisé lors de sa première session, il est probable que l'utilisateur ne verra pas le message in-app.

### Messages in-app {#in-app-messages}

Avec les messages in-app, la situation peut être plus nuancée. Un message in-app doit être distribué et mis en cache dans le SDK, généralement au début d'une session, avant de pouvoir être déclenché. Si l'événement déclencheur fait partie du processus de création de l'utilisateur, ou si la campagne de message in-app est distribuée avant que l'utilisateur ne remplisse (ou après qu'il ne remplisse plus) les critères d'audience lors de sa première session, il se peut qu'il ne voie pas le message in-app.

### Meilleures pratiques {#best-practices}

#### Introduire des délais {#introduce-delays}

Après la création d'un nouvel utilisateur, vous pouvez ajouter un délai avant d'envoyer des campagnes ou des Canvas ciblés. Ce délai permet au profil utilisateur d'être créé et aux attributs pertinents d'être mis à jour, ce qui peut déterminer son éligibilité à recevoir le message.

Par exemple, après qu'un utilisateur s'est inscrit sur votre application, vous pouvez envoyer une offre promotionnelle après 24 heures. Ou, si vous créez un utilisateur ou enregistrez un attribut personnalisé, vous pouvez ajouter un délai d'une minute avant de poursuivre votre processus pour éviter cette condition de concurrence.

Vous pouvez également ajouter ce délai dans le [SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration) pour l'événement personnalisé spécifique qui déclenche l'entrée d'un nouvel utilisateur dans un Canvas.

## Scénario 2 : Utilisation de plusieurs endpoints API {#scenario-2-using-multiple-api-endpoints}

{% alert important %}
Nous utilisons un traitement asynchrone pour maximiser la vitesse et la flexibilité. Cela signifie que lorsque des appels API nous sont envoyés séparément, nous ne pouvons pas garantir qu'ils seront traités dans l'ordre dans lequel ils ont été envoyés.
{% endalert %}

Il existe plusieurs scénarios dans lesquels l'utilisation de plusieurs endpoints API peut également entraîner cette condition de concurrence, par exemple lorsque :

- Des endpoints API distincts sont utilisés pour créer des utilisateurs et déclencher des Canvas ou des campagnes
- Plusieurs appels séparés sont effectués vers l'endpoint `/users/track` pour mettre à jour des attributs personnalisés, des événements ou des achats

Lorsque les informations utilisateur sont envoyées à Braze via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), le traitement peut parfois prendre quelques secondes. Cela signifie que lorsque des requêtes sont effectuées simultanément vers `/users/track` et vers des endpoints d'envoi de messages comme `/campaign/trigger/send`, il n'y a aucune garantie que les informations utilisateur soient mises à jour avant l'envoi du message.

{% alert note %}
Si les attributs et les événements utilisateur sont envoyés dans la même requête (que ce soit via `/users/track` ou via le SDK), Braze traite les attributs avant les événements ou avant de tenter d'envoyer un message.
{% endalert %}

### Meilleures pratiques

#### Lorsque vous utilisez plusieurs endpoints, envoyez vos requêtes une par une {#when-using-multiple-endpoints-send-your-requests-one-at-a-time}

Si vous utilisez plusieurs endpoints, vous pouvez essayer d'échelonner vos requêtes afin que chacune soit terminée avant que la suivante ne commence. Cela peut réduire le risque de condition de concurrence. Par exemple, si vous devez mettre à jour des attributs utilisateur et envoyer un message, attendez d'abord que le profil utilisateur soit entièrement mis à jour avant d'envoyer un message via un endpoint.

Si vous envoyez une requête API de message planifié, ces requêtes doivent être séparées, et l'utilisateur doit être créé avant l'envoi de la requête API planifiée.

#### Inclure les données clés avec le déclencheur {#include-key-data-with-the-trigger}

Au lieu d'utiliser plusieurs endpoints, vous pouvez inclure les [attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) et les [propriétés de déclenchement]({{site.baseurl}}/api/objects_filters/trigger_properties_object) dans un seul appel API en utilisant l'[endpoint `campaign/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

Lorsque ces objets sont inclus avec le déclencheur, les attributs sont traités en premier, avant que le message ne soit déclenché, ce qui élimine les conditions de concurrence potentielles. Notez que les propriétés de déclenchement ne mettent pas à jour le profil utilisateur, mais sont utilisées uniquement dans le contexte du message.

#### Utiliser l'endpoint POST : Suivre les utilisateurs (synchrone) {#use-the-post-track-users-sync-endpoint}

Utilisez l'[endpoint `/users/track/sync/`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) pour enregistrer des événements personnalisés et des achats, et mettre à jour les attributs du profil utilisateur de manière synchrone. L'utilisation de cet endpoint pour mettre à jour les profils utilisateur en même temps et dans un seul appel peut aider à prévenir les conditions de concurrence potentielles.

{% multi_lang_include alerts/early_access_beta_alert.md feature='This endpoint' type='beta' %}

## Scénario 3 : Correspondance entre les déclencheurs basés sur l'action et les filtres d'audience {#scenario-3-matching-action-based-triggers-and-audience-filters}

Une autre condition de concurrence courante peut survenir lorsque vous configurez une campagne ou un Canvas basé sur les actions avec le même déclencheur que le filtre d'audience (comme un attribut modifié ou un événement personnalisé effectué). L'utilisateur peut ne pas faire partie de l'audience au moment où il effectue l'événement déclencheur, ce qui signifie qu'il ne recevra pas la campagne ou n'entrera pas dans le Canvas.

### Meilleures pratiques

#### Vérifier votre audience après un délai {#check-your-audience-after-a-delay}

Pour éviter d'utiliser des filtres d'audience contenant les critères de déclenchement, nous recommandons de vérifier votre audience avant la distribution. Par exemple, vous pouvez [utiliser les validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#edit-delivery-settings) dans les étapes de message Canvas comme vérification supplémentaire pour confirmer que votre audience remplit les critères de distribution au moment de l'envoi du message. Vous pouvez également tirer parti des critères de sortie du Canvas pour faire sortir les utilisateurs à tout moment du parcours s'ils remplissent vos critères.

Pour les campagnes, vous pouvez utiliser des événements de sortie pour permettre aux campagnes avec un événement déclencheur d'annuler les messages destinés aux utilisateurs qui effectuent l'événement de sortie pendant le délai.

#### Utiliser des filtres distincts de l'événement déclencheur {#use-unique-filters-with-the-trigger-event}

Lors de la configuration de vos filtres, vous pourriez être tenté d'ajouter un filtre redondant « au cas où ». Cependant, cette redondance peut entraîner davantage de problèmes. Évitez plutôt d'utiliser tout filtre contenant le déclencheur lorsque c'est possible. C'est la méthode la plus sûre pour éviter une condition de concurrence.

Par exemple, si le déclencheur de votre campagne est « A effectué un achat » et que votre filtre d'audience est « A effectué un achat quelconque », cette redondance peut provoquer une condition de concurrence.

#### Éviter les filtres d'audience qui supposent que l'événement déclencheur a été mis à jour {#avoid-audience-filters-that-assume-the-trigger-event-has-been-updated}

Cette bonne pratique est similaire à celle consistant à éviter les filtres redondants avec l'événement déclencheur. En général, un filtre qui suppose que l'événement déclencheur est mis à jour dans le profil utilisateur échoue.

#### Utiliser les abandons Liquid (attributs uniquement) {#use-liquid-aborts-attributes-only}

Dans les campagnes et les étapes Canvas, utilisez les abandons Liquid pour éviter d'utiliser des filtres d'audience contenant les attributs de déclenchement dans la planification d'entrée. Par exemple, supposons que vous ayez un attribut de type tableau « couleurs préférées » et que vous souhaitiez cibler tout utilisateur qui met à jour ce tableau avec n'importe quelle valeur, et qui a également la couleur « bleu » dans le tableau après la mise à jour. Si vous utilisez les filtres d'audience dans cet exemple, vous rencontrerez une condition de concurrence et manquerez les utilisateurs ajoutant « bleu » dans le tableau pour la première fois.

Dans ce cas, vous pouvez implémenter un délai de déclenchement dans une campagne ou utiliser une étape de délai dans un Canvas pour laisser le temps au profil utilisateur de se mettre à jour, puis utiliser la logique d'abandon Liquid suivante :

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Vérifier comment les données utilisateur sont gérées {#confirm-how-user-data-is-being-managed}

S'il y a une condition de concurrence lors de l'évaluation de l'entrée dans le Canvas, les utilisateurs peuvent entrer dans un Canvas dans lequel ils n'étaient pas censés entrer. Par exemple, le profil de l'utilisateur pourrait être configuré pour être inclus dans l'audience, puis mis à jour après que le Canvas a mis les utilisateurs en file d'attente, de sorte qu'ils ne sont plus éligibles pour l'audience.

Si un utilisateur déclenche l'événement d'entrée du Canvas plusieurs fois dans la même seconde, Braze n'autorise qu'une seule entrée pour cette seconde (même si la réentrée est activée). Cela empêche les entrées en double, de sorte que le nombre total d'entrées dans le Canvas peut être inférieur au nombre total d'événements déclencheurs.

Nous recommandons de vérifier comment les données utilisateur sont gérées et mises à jour, en particulier quand et comment des attributs spécifiques sont mis à jour, que ce soit par le SDK, l'API, l'API par lots ou d'autres méthodes. Cela peut aider à identifier et clarifier pourquoi un utilisateur est entré dans une campagne ou un Canvas par rapport au moment où son profil a été mis à jour.

## Scénario 4 : Utilisation du déclencheur « Interagir avec l'étape » {#scenario-4-using-the-interact-with-step-trigger}

Dans un Canvas, lorsqu'une étape de message est immédiatement suivie d'une étape de parcours d'action qui utilise le déclencheur « Interagir avec l'étape », une condition de concurrence peut se produire. Étant donné que les utilisateurs peuvent interagir avec un message dès qu'il est distribué, il est possible qu'un utilisateur effectue l'action suivie avant d'entrer officiellement dans l'étape de parcours d'action.

Dans ce cas, l'étape de parcours d'action n'enregistre pas l'interaction, car elle n'évalue que les événements qui se produisent après l'entrée dans l'étape, ce qui signifie que l'utilisateur peut être dirigé vers un chemin non prévu.

Un Canvas envoie une notification push dans une étape de message, suivie d'une étape de parcours d'action qui vérifie si l'utilisateur ouvre cette notification push. Si un utilisateur ouvre la notification push immédiatement après l'avoir reçue (avant d'entrer dans l'étape de parcours d'action), l'événement d'ouverture peut ne pas être capturé. L'utilisateur pourrait alors être incorrectement dirigé vers le chemin « n'a pas ouvert », même s'il a interagi avec le message.

### Meilleures pratiques

#### Suivre l'engagement à l'aide d'un événement personnalisé {#track-engagement-using-a-custom-event}

Évitez de vous appuyer sur « Interagir avec l'étape » immédiatement après une étape de message lorsque les interactions utilisateur sont susceptibles de se produire rapidement. Suivez plutôt l'engagement à l'aide d'un événement personnalisé (par exemple, déclenché depuis l'application ou le site web après l'interaction) et évaluez cet événement dans une étape ultérieure. Cela garantit que l'événement est enregistré après que l'utilisateur est entré dans l'étape.

#### Éviter les branches dépendantes de l'interaction {#avoid-branches-that-are-dependent-on-interaction}

Concevez votre Canvas de sorte que l'absence d'une interaction immédiate ne compromette pas l'expérience utilisateur. Par exemple, évitez les décisions de branchement critiques qui dépendent uniquement de la capture de l'interaction dans l'étape suivante, ou ajoutez une logique de suivi capable de corriger le parcours des utilisateurs.