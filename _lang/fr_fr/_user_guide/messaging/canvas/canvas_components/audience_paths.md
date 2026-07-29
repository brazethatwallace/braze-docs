---
nav_title: Parcours d'audience
article_title: Parcours d'audience
alias: /audience_paths/
page_order: 3
page_type: reference
description: "Cet article de référence explique comment utiliser les parcours d'audience dans votre Canvas pour filtrer et segmenter intuitivement les utilisateurs à grande échelle en envoyant chaque utilisateur dans la première branche correspondante."
tool: Canvas

---

# Parcours d'audience {#audience-paths}

> Les parcours d'audience de Canvas vous permettent de filtrer et de segmenter intuitivement les utilisateurs à grande échelle en envoyant chaque utilisateur dans le premier parcours dont il remplit les critères.

Ce composant Canvas remplace la nécessité de créer un nombre excessif d'étapes complètes basées sur l'audience, en vous permettant de combiner ce qui aurait pu être huit composants complets en un seul. Cela simplifie le ciblage des utilisateurs tout en allégeant vos Canvas d'une complexité inutile.

## Fonctionnement {#how-it-works}

![Un parcours d'audience avec deux groupes : les utilisateurs engagés et tous les autres.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Les utilisateurs progressent dans la première branche dont ils remplissent les critères : placez donc le parcours le plus important en premier. Cela réduit l'ambiguïté quant à la destination des utilisateurs et aux messages qu'ils reçoivent. Notez que cet ordre n'est pas [modifiable après le lancement]({{site.baseurl}}/post-launch_edits).

Avec les parcours d'audience, vous pouvez :

- Envoyer les utilisateurs dans différents parcours Canvas en fonction de critères d'audience.
- Placer vos groupes d'audience les plus importants en premier ; les utilisateurs empruntent le premier parcours pour lequel ils sont éligibles.
- Cibler précisément les utilisateurs à grande échelle.
  - Vous pouvez créer jusqu'à huit groupes d'audience (deux par défaut et six groupes supplémentaires) par étape de parcours d'audience, mais vous pouvez aussi connecter plusieurs étapes de parcours d'audience pour affiner davantage le tri de vos utilisateurs.

Au sein d'une même étape de parcours d'audience, les utilisateurs sont évalués par rapport aux groupes d'audience dans l'ordre et progressent dans le premier parcours pour lequel ils sont éligibles. Si vous connectez plusieurs étapes de parcours d'audience dans un Canvas, les utilisateurs sont réévalués à chaque fois qu'ils atteignent une nouvelle étape de parcours d'audience.

### Comment les utilisateurs sont évalués {#how-users-are-evaluated}

![Canvas montrant un délai de 24 heures après une étape Message, suivi d'un parcours d'audience.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les utilisateurs sont évalués par rapport aux filtres et à l'appartenance aux Segments **au moment où ils atteignent l'étape de parcours d'audience**, et non au moment de leur entrée dans le Canvas. Après l'évaluation, ils progressent immédiatement vers le parcours correspondant. Lorsqu'un utilisateur est placé dans un groupe d'audience, il reste dans ce groupe même si son profil utilisateur change par la suite.

<div style="clear: both;"></div>

{% alert important %}
Les parcours d'audience évaluent les utilisateurs en fonction de leurs attributs actuels, de leurs filtres et de leur appartenance aux Segments au moment de l'évaluation. Ils ne se basent pas sur l'événement spécifique qui a déclenché l'entrée dans le Canvas. Pour orienter les utilisateurs en fonction d'une action qu'ils effectuent (comme un événement personnalisé), utilisez plutôt les [parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths).
{% endalert %}

### Laisser du temps pour l'évaluation des utilisateurs {#allowing-time-for-user-evaluations}

L'évaluation étant immédiate, il est important d'ajouter un délai avant le parcours d'audience si les critères du parcours dépendent d'une interaction de l'utilisateur avec une étape précédente.

Par exemple, si les utilisateurs reçoivent le Message A et que l'étape suivante est un parcours d'audience qui évalue s'ils ont interagi avec ce message, tous les utilisateurs progresseront vers l'étape destinée à ceux qui n'ont pas interagi avec le message. En effet, les utilisateurs progressent immédiatement vers l'étape de parcours d'audience sans avoir eu le temps d'interagir avec le message. Autrement dit, les utilisateurs sont évalués pour une interaction avec le message presque immédiatement après son envoi.

Pour laisser aux utilisateurs le temps d'interagir avec un message envoyé, ajoutez un délai entre l'étape Message et le parcours d'audience. Par exemple, un délai de 24 heures donne aux utilisateurs 24 heures après l'envoi du message pour interagir avec le Message A avant l'évaluation.

## Créer un parcours d'audience {#creating-an-audience-path}

Pour ajouter une étape de parcours d'audience, procédez comme suit :

1. Ajoutez une étape à votre Canvas.
2. Glissez-déposez le composant depuis la barre latérale, ou sélectionnez <i class="fas fa-plus-circle"></i> **Ajouter** en bas d'une étape et sélectionnez **Parcours d'audience**.

Le composant de parcours d'audience par défaut contient deux groupes d'audience : **Groupe 1** et **Tous les autres**. Le groupe **Tous les autres** inclut tout utilisateur qui ne correspond à aucun groupe d'audience défini. Ce groupe est toujours le dernier dans l'ordre.

### Définir les groupes d'audience {#defining-audience-groups}

La capture d'écran suivante montre la disposition d'une étape de parcours d'audience développée. Vous pouvez y définir jusqu'à huit groupes d'audience (un prédéfini et sept personnalisables). Pour définir un groupe d'audience, sélectionnez le nom du groupe dans l'éditeur de parcours d'audience. Vous pouvez renommer votre groupe d'audience, choisir les filtres et Segments qui s'appliquent à votre groupe, et ajouter ou supprimer des groupes. Par exemple, si vous souhaitez cibler des messages d'onboarding pour un groupe d'utilisateurs, vous pourriez sélectionner des filtres de reciblage, tels que « A cliqué sur un e-mail » et « A cliqué sur un message in-app ».

![Un parcours d'audience développé avec les groupes « Aime la cuisine asiatique », « Aime la cuisine latino-américaine », « Aime la cuisine européenne » et « Tous les autres ».]({% image_buster /assets/img/audience_path/audience_path3.png %})

Une fois l'étape de parcours d'audience terminée, chaque groupe d'audience disposera d'une branche distincte. Vous pouvez continuer à utiliser les parcours d'audience pour affiner davantage votre audience, ou poursuivre votre parcours Canvas avec les étapes Canvas standard.

![Deux parcours d'audience avec différents groupes basés sur l'engagement.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Utiliser des filtres de comparaison avec les variables de contexte {#using-comparison-filters-with-context-variables}

Lorsque vous segmentez sur une variable de contexte contenant une date, consultez [Filtres Jour de l'année et Heure pour les variables de contexte de type date]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables) pour choisir le bon type de comparaison.

### Tester les groupes d'audience {#testing-audience-groups}

Après avoir ajouté des Segments et des filtres à votre audience, vous pouvez vérifier que vos groupes d'audience sont configurés comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pour confirmer qu'il correspond aux critères d'audience.

![La section « Recherche d'utilisateur ».]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Utiliser les parcours d'audience {#using-audience-paths}

La véritable puissance des parcours d'audience réside dans le fait de placer les parcours qui vous importent le plus **en premier**. Bien que cette fonctionnalité n'ait pas besoin d'être utilisée de manière stratégique, certains marketeurs peuvent souhaiter mettre en avant certains produits auprès des utilisateurs, comme des offres spéciales ou des éditions limitées.

En plaçant ces Segments en premier dans la liste, vous pouvez cibler les utilisateurs correspondant à des filtres et Segments spécifiques tout en ciblant également les utilisateurs qui ne répondent pas à ces critères précis — le tout en une seule étape Canvas.

![Un parcours d'audience avec les groupes « Aime les chaussures Big Brand », « Aime Big Brand » et « Tous les autres ».]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Par exemple, imaginons que vous souhaitiez envoyer à un groupe d'utilisateurs des publicités pour de nouveaux produits. Vous commenceriez par placer les filtres correspondant à ces produits **en premier** dans le parcours d'audience. Si vous créiez une campagne marketing pour l'entreprise « Big Brand » et qu'une nouvelle marque venait d'être lancée, vous pourriez sélectionner des filtres comme « Aime les chaussures Big Brand » ou « Aime les sacs Big Brand », et envoyer différents e-mails en fonction du groupe filtré auquel ils appartiennent.

Lorsque les utilisateurs entrent dans ce composant de parcours d'audience, ils sont d'abord évalués pour le Groupe d'audience 1 « Aime les chaussures Big Brand » — le premier parcours de la liste. Si c'est le cas, ils continuent vers le composant suivant défini dans votre Canvas. S'ils n'« Aiment pas les chaussures Big Brand », ils sont alors évalués pour le groupe d'audience suivant, le Groupe d'audience 2 « Aime les sacs Big Brand », et continuent vers l'étape suivante si les critères sont remplis. Enfin, les utilisateurs qui ne correspondent à aucun des groupes précédents sont dirigés vers le groupe « Tous les autres » et continuent également vers l'étape Canvas suivante que vous avez définie pour ce parcours.

Vous pouvez également consulter les performances de cette étape grâce à l'[analytique Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization).

### Segmenter les parcours d'audience avec des numéros de compartiment aléatoires {#segmenting-audience-paths-with-random-bucket-numbers}

Si votre Canvas utilise une [limite de débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) (par exemple, en limitant le nombre total d'utilisateurs qui recevront le Canvas), Braze recommande de ne pas utiliser de numéros de compartiment aléatoires pour segmenter vos parcours d'audience.

Un [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) est un attribut utilisateur qui peut être utilisé pour créer des Segments uniformément distribués d'utilisateurs aléatoires. Braze utilise le numéro de compartiment aléatoire pour regrouper les utilisateurs pendant la phase de segmentation à l'entrée du Canvas, et chaque groupe est traité séparément. Selon les groupes qui terminent le traitement en premier, certains utilisateurs peuvent être bloqués à l'entrée en raison de la limite de débit, ce qui pourrait entraîner une distribution inégale des utilisateurs lorsqu'ils atteignent l'étape de parcours d'audience.

Dans ce cas, essayez plutôt d'utiliser les [chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).

### Utiliser le filtre Canal intelligent avec les parcours d'audience {#using-intelligent-channel-filter-with-audience-paths}

En combinant les étapes de parcours d'audience et les filtres de canal intelligent, vous pouvez adapter votre expérience de communication aux préférences et comportements de chaque utilisateur. Ainsi, vos utilisateurs recevront les messages les plus pertinents via les canaux appropriés.

Par exemple, dans une étape de parcours d'audience, vous pouvez créer trois audiences : E-mail, Push mobile et Tous les autres. Pour l'audience E-mail, ajoutez le filtre `Intelligent Channel is Email`. Pour l'audience Push mobile, ajoutez le filtre `Intelligent Channel is Mobile Push`. Ensuite, vous pouvez ajouter une étape Message pour chacun des parcours d'audience afin de délivrer des messages personnalisés et pertinents.

{% alert tip %}
Consultez nos [modèles de Canvas Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) pour découvrir des exemples de personnalisation de ces modèles prédéfinis.
{% endalert %}