---
nav_title: Parcours d'audience
article_title: Parcours d'audience
alias: /audience_paths/
page_order: 3
page_type: reference
description: "Cet article de référence explique comment utiliser les Parcours d'audience dans votre Canvas pour filtrer et segmenter intuitivement les utilisateurs à grande échelle en envoyant chaque utilisateur dans la première branche correspondante."
tool: Canvas

---

# Parcours d'audience {#audience-paths}

> Les Parcours d'audience de Canvas vous permettent de filtrer et de segmenter intuitivement les utilisateurs à grande échelle en envoyant chaque utilisateur dans le premier parcours dont il remplit les critères.

Ce composant Canvas remplace la nécessité de créer un nombre excessif d'étapes complètes basées sur l'audience, en vous permettant de combiner ce qui aurait pu être huit composants complets en un seul. Cela simplifie le ciblage des utilisateurs tout en allégeant vos Canvas d'une complexité inutile.

## Comment ça fonctionne {#how-it-works}

![Un parcours d'audience avec deux groupes : utilisateurs engagés et tous les autres.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Les utilisateurs progressent dans la première branche dont ils remplissent les critères, placez donc le parcours le plus important en premier. Cela réduit l'ambiguïté quant à la direction que prennent les utilisateurs et aux messages qu'ils reçoivent. Notez que cet ordre n'est pas [modifiable après le lancement]({{site.baseurl}}/post-launch_edits).

Avec les parcours d'audience, vous pouvez :

- Envoyer les utilisateurs dans différents parcours Canvas en fonction de critères d'audience.
- Placer vos groupes d'audience les plus importants en premier ; les utilisateurs empruntent le premier parcours pour lequel ils sont éligibles.
- Cibler précisément les utilisateurs à grande échelle.
  - Vous pouvez créer jusqu'à huit groupes d'audience (deux par défaut et six groupes supplémentaires) par étape de parcours d'audience, mais vous pouvez connecter plusieurs étapes de parcours d'audience pour trier davantage vos utilisateurs.

Au sein d'une seule étape de parcours d'audience, les utilisateurs sont évalués par rapport aux groupes d'audience dans l'ordre et progressent dans le premier parcours pour lequel ils sont éligibles. Si vous connectez plusieurs étapes de parcours d'audience dans un Canvas, les utilisateurs sont évalués à nouveau chaque fois qu'ils atteignent une nouvelle étape de parcours d'audience.

### Comment les utilisateurs sont évalués {#how-users-are-evaluated}

![Canvas montrant un délai de 24 heures après une étape Message, suivi d'un parcours d'audience.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les utilisateurs sont évalués par rapport aux filtres et à l'appartenance aux Segments **au moment où ils atteignent l'étape de parcours d'audience**, et non lorsqu'ils sont entrés dans le Canvas. Après l'évaluation, ils progressent immédiatement vers le parcours correspondant. Lorsqu'un utilisateur est placé dans un groupe d'audience, il reste dans ce groupe même si son profil utilisateur change par la suite.

<div style="clear: both;"></div>

{% alert important %}
Les parcours d'audience évaluent en fonction des attributs actuels de l'utilisateur, des filtres et de l'appartenance aux Segments au moment de l'évaluation. Ils n'évaluent pas en fonction de l'événement spécifique qui a déclenché l'entrée dans le Canvas. Pour orienter les utilisateurs en fonction d'une action qu'ils effectuent (comme un événement personnalisé), utilisez plutôt les [parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths).
{% endalert %}

### Laisser du temps pour l'évaluation des utilisateurs {#allowing-time-for-user-evaluations}

Étant donné que l'évaluation est immédiate, il est important d'ajouter un délai avant le parcours d'audience si les critères du parcours dépendent d'une interaction de l'utilisateur avec une étape précédente.

Par exemple, si les utilisateurs reçoivent le Message A et que l'étape suivante est un parcours d'audience qui évalue s'ils ont interagi avec ce message, tous les utilisateurs progresseront vers l'étape correspondant à ceux qui n'ont pas interagi avec ce message. En effet, les utilisateurs ont immédiatement progressé vers l'étape de parcours d'audience sans avoir eu le temps d'interagir avec le message. Autrement dit, les utilisateurs sont évalués pour une interaction avec le message presque immédiatement après l'envoi du message.

Pour donner aux utilisateurs le temps d'interagir avec un message envoyé, ajoutez un délai entre l'étape Message et le parcours d'audience. Par exemple, un délai de 24 heures donne aux utilisateurs 24 heures après l'envoi du message pour interagir avec le Message A avant l'évaluation.

## Créer un parcours d'audience {#creating-an-audience-path}

Pour ajouter une étape de parcours d'audience, procédez comme suit :

1. Ajoutez une étape à votre Canvas.
2. Glissez-déposez le composant depuis la barre latérale, ou sélectionnez <i class="fas fa-plus-circle"></i> **Ajouter** en bas d'une étape et sélectionnez **Audience Paths**.

Le composant de parcours d'audience par défaut contient deux groupes d'audience par défaut, **Group 1** et **Everybody Else**. Le groupe **Everybody Else** inclut tout utilisateur qui ne fait partie d'aucun groupe d'audience défini. Ce groupe est toujours le dernier dans l'ordre.

### Définir les groupes d'audience {#defining-audience-groups}

La capture d'écran suivante montre la disposition d'une étape de parcours d'audience développée. Vous pouvez y définir jusqu'à huit groupes d'audience (un prédéfini et sept personnalisables). Pour définir un groupe d'audience, sélectionnez le nom du groupe dans l'éditeur de parcours d'audience. Vous pouvez renommer votre groupe d'audience, choisir les filtres et Segments qui s'appliquent à votre groupe, et ajouter ou supprimer des groupes. Par exemple, si vous souhaitez cibler des messages d'onboarding vers un groupe d'utilisateurs, vous pouvez sélectionner des filtres de reciblage, tels que « A cliqué sur un e-mail » et « A cliqué sur un message in-app ».

![Un parcours d'audience développé avec des groupes pour « Loves Asian Cuisine », « Loves Latin Cuisine », « Loves European Cuisine » et « Everyone Else ».]({% image_buster /assets/img/audience_path/audience_path3.png %})

Une fois l'étape de parcours d'audience terminée, chaque groupe d'audience disposera d'une branche distincte. Vous pouvez continuer à utiliser les parcours d'audience pour affiner davantage votre audience, ou poursuivre votre parcours Canvas avec les étapes Canvas standard.

![Deux parcours d'audience avec différents groupes basés sur l'engagement.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Utiliser des filtres de comparaison avec des variables de contexte {#using-comparison-filters-with-context-variables}

Lorsque vous effectuez un fractionnement sur une variable de contexte contenant une date, consultez [Filtres Jour de l'année et Heure pour les variables de contexte de type date]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables) pour choisir le type de comparaison approprié.

### Tester les groupes d'audience {#testing-audience-groups}

Après avoir ajouté des Segments et des filtres à votre audience, vous pouvez vérifier que vos groupes d'audience sont configurés comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pour confirmer qu'il correspond aux critères d'audience.

![La section « User Lookup ».]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Utiliser les parcours d'audience {#using-audience-paths}

La véritable puissance des parcours d'audience réside dans le fait de placer les parcours qui vous importent le plus **en premier**. Bien que cette fonctionnalité n'ait pas besoin d'être utilisée de manière stratégique, certains marketeurs peuvent souhaiter mettre en avant certains produits auprès des utilisateurs, comme des offres spéciales ou des éditions limitées.

En plaçant ces Segments en premier dans la liste, vous pouvez cibler les utilisateurs qui correspondent à des filtres et Segments spécifiques tout en ciblant également ceux qui ne répondent pas à ces critères précis, le tout en une seule étape de Canvas.

![Un parcours d'audience avec des groupes « Aime les chaussures Big Brand », « Aime Big Brand » et « Tous les autres ».]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Par exemple, imaginons que vous souhaitiez envoyer à un groupe d'utilisateurs des publicités pour de nouveaux produits. Vous commenceriez par placer les filtres correspondant à ces produits **en premier** dans le parcours d'audience. Si vous créiez une Campaign marketing pour l'entreprise « Big Brand » et qu'une nouvelle marque venait d'être lancée, vous pourriez sélectionner des filtres comme « Aime les chaussures Big Brand » ou « Aime les sacs Big Brand », et envoyer différents e-mails en fonction du groupe filtré auquel ils appartiennent.

Lorsque les utilisateurs entrent dans ce composant de parcours d'audience, ils sont d'abord évalués pour le groupe d'audience 1 « Aime les chaussures Big Brand », le premier parcours de la liste. Si c'est le cas, ils continuent vers le composant suivant défini dans votre Canvas. S'ils n'« aiment pas les chaussures Big Brand », ils sont alors évalués pour le groupe d'audience suivant, le groupe d'audience 2 « Aime les sacs Big Brand », et continuent vers l'étape suivante si les critères sont remplis. Enfin, les utilisateurs qui ne correspondent à aucun des groupes précédents sont placés dans le groupe « Tous les autres » et continuent également vers l'étape de Canvas suivante que vous avez définie pour ce parcours.

Vous pouvez également consulter les performances de cette étape en utilisant l'[analyse Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization).

### Segmenter les parcours d'audience avec des numéros de compartiment aléatoires {#segmenting-audience-paths-with-random-bucket-numbers}

Si votre Canvas utilise une [limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) (comme la limitation du nombre total d'utilisateurs qui recevront le Canvas), Braze recommande de ne pas utiliser de numéros de compartiment aléatoires pour segmenter vos parcours d'audience.

Un [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) est un attribut utilisateur qui peut être utilisé pour créer des Segments d'utilisateurs aléatoires uniformément distribués. Braze utilise le numéro de compartiment aléatoire pour regrouper les utilisateurs pendant la phase de segmentation de l'entrée dans le Canvas, et chaque groupe est traité séparément. Selon les groupes qui terminent le traitement en premier, certains utilisateurs peuvent être limités à l'entrée en raison de la limitation du débit, ce qui pourrait entraîner une distribution inégale des utilisateurs lorsqu'ils atteignent l'étape du parcours d'audience.

Dans ce scénario, essayez plutôt d'utiliser les [chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).

### Utiliser le filtre canal intelligent avec les parcours d'audience {#using-intelligent-channel-filter-with-audience-paths}

En combinant les étapes de parcours d'audience et les filtres de canal intelligent, vous pouvez adapter votre expérience de communication aux préférences et comportements de chaque utilisateur. Ainsi, vos utilisateurs recevront les messages les plus pertinents via les canaux appropriés.

Par exemple, dans une étape de parcours d'audience, vous pouvez créer trois audiences : e-mail, notification push mobile et tous les autres. Pour l'audience e-mail, ajoutez le filtre `Intelligent Channel is Email`. Pour l'audience notification push mobile, ajoutez le filtre `Intelligent Channel is Mobile Push`. Ensuite, vous pouvez ajouter une étape de message pour chacun des parcours d'audience afin de délivrer des messages personnalisés et pertinents.

{% alert tip %}
Consultez nos [modèles Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) pour des exemples sur la façon de personnaliser ces modèles prédéfinis à votre avantage.
{% endalert %}