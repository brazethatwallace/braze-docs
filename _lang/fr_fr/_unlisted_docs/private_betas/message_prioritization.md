---
article_title: Priorisation des messages
permalink: /message_prioritization/
toc_headers: h2
description: "Cet article de référence décrit la priorisation des messages au niveau supérieur et comment la configurer pour votre espace de travail."
---

# Priorisation des messages {#message-prioritization}

> Utilisez la priorisation des messages pour vous assurer que vos utilisateurs reçoivent les Campaigns qui comptent le plus.

{% alert important %}
La priorisation des messages est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cette bêta.
{% endalert %}

Seuls les administrateurs peuvent configurer les paramètres de priorisation des messages au niveau supérieur. Les utilisateurs avec des droits limités peuvent consulter chaque page de cette section, mais ne peuvent pas effectuer de modifications.

Pour accéder aux paramètres de priorisation des messages au niveau supérieur, allez dans **Paramètres** > **Priorisation des messages**.

## Fonctionnement {#how-it-works}

La priorisation des messages vous permet de créer des [catégories](#categories) et des [règles de priorisation](#prioritization-rules) pour classer l'ordre d'envoi de vos messages.

Imaginons que vous gérez des promotions par e-mail pour des partenariats payants et des programmes de fidélité pour une marque de beauté. Avec la priorisation des messages, vous pourriez créer deux catégories nommées « Partenariats payants » et « Fidélité ». Vous pourriez ensuite classer ces catégories en fonction de leur importance stratégique pour votre marque. Par exemple, pendant la période des fêtes, vous pourriez classer « Fidélité » plus haut que « Partenariats payants » pour donner la priorité aux clients de votre marque qui font partie de votre programme d'adhésion depuis plus d'un an.

![Un exemple de règles de priorisation pour deux catégories : Partenariats payants et Fidélité.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

## Catégories {#categories}

Les règles de priorisation reposent sur un classement de catégories, qui est un libellé que vous pouvez attribuer à une Campaign donnée (similaire à une [étiquette](https://www.braze.com/docs/user_guide/administrative/app_settings/tags)). Vous pouvez créer jusqu'à 20 catégories à un moment donné.

Pour ajouter une nouvelle catégorie :

1. Allez dans **Paramètres** > **Priorisation des messages** > **Catégories**.
2. Sélectionnez **Créer une nouvelle catégorie**.

![Le bouton « Créer une nouvelle catégorie » dans la section Priorisation des messages.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Donnez un nom à la catégorie et une description facultative.
4. Sélectionnez **Créer la catégorie**.

![Un exemple de catégorie nommée « P3 » avec la description « Ceci deviendra ma troisième catégorie de priorité la plus élevée. »]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Pour modifier ou supprimer une catégorie, sélectionnez le menu <i class="fas fa-ellipsis-vertical" aria-label="Menu d'options"></i>.

## Règles de priorisation {#prioritization-rules}

Une fois vos catégories configurées, vous pouvez les classer dans un ensemble de règles de priorisation. Les règles sont classées par ordre décroissant de priorité. Vous pouvez créer jusqu'à 10 règles de priorisation à un moment donné.

1. Allez dans **Paramètres** > **Priorisation des messages** > **Règles de priorisation** pour configurer vos règles.

![Section « Règles de priorisation » sans aucune priorité définie pour le moment.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Sélectionnez **Ajouter une règle**.
3. Sélectionnez une catégorie dans le menu déroulant.

![Règle de priorisation « Priorité 1 » avec P1 sélectionné comme catégorie.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continuez à ajouter des règles en sélectionnant **+ Ajouter une règle** sous votre dernière règle.

Pour réorganiser les règles, sélectionnez et faites glisser l'icône <i class="fa-solid fa-grip-vertical" aria-label="Réorganiser"></i> en haut à gauche d'une règle. Pour supprimer une règle, sélectionnez le menu <i class="fas fa-ellipsis-vertical" aria-label="Menu d'options"></i> puis **Supprimer la règle**.

N'oubliez pas de sélectionner **Enregistrer** pour que vos modifications soient appliquées.

## Paramètres au niveau de la Campaign {#campaign-level-settings}

### Activation {#opt-in}

{% alert important %}
Seules les Campaigns planifiées et monocanal peuvent être activées pour la priorisation pour le moment. Les Campaigns déclenchées par une action ou par l'API ainsi que les Canvas ne sont pas pris en charge.
{% endalert %}

Pour activer la priorisation d'une Campaign, cochez la case **Activer la priorisation des messages** dans la page **Planification de l'envoi** de la Campaign.

![La case à cocher « Activer la priorisation des messages ».]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Ensuite, attribuez la Campaign à une catégorie en en sélectionnant une dans le menu déroulant **Catégorie**.

![La case à cocher « Activer la priorisation des messages ».]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

Vous pouvez activer jusqu'à 25 Campaigns actives à un moment donné. Les Campaigns en brouillon, arrêtées ou archivées ne comptent pas dans cette limite.

### Fenêtre de nouvelle tentative {#retry-window}

Une fenêtre de nouvelle tentative permet aux Campaigns activées de réessayer pendant un maximum de trois jours si la première tentative n'a pas une priorité suffisamment élevée pour être envoyée. Chaque jour suivant, à la même heure que le message était initialement planifié, une nouvelle tentative d'envoi est effectuée. Après le dernier jour de la fenêtre de nouvelle tentative, si le message n'a toujours pas été envoyé, il n'est plus réessayé et est définitivement dépriorisé.

La fenêtre de nouvelle tentative doit être plus courte que l'intervalle entre les envois de cette Campaign. Si une Campaign est envoyée tous les lundis et mercredis, la tentative de nouvelle tentative a lieu le mardi. Cela signifie que la fenêtre de nouvelle tentative doit être définie à un jour.

![Le paramètre « Fenêtre de nouvelle tentative » défini à 1 jour.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

## Limites de fréquence {#frequency-caps}

### Pour les Campaigns {#for-campaigns}

Pour être éligible à la priorisation des messages, une Campaign doit être activée pour la limite de fréquence. Vous pouvez confirmer que la Campaign est activée dans la section **Contrôles de l'envoi** de la page **Planification de l'envoi**.

![Un exemple de règle de limite de fréquence pour tout canal applicable et sans filtres supplémentaires.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Règles de limite de fréquence {#frequency-capping-rules}

Nous optimiserons la priorité dans le cadre de vos règles de limite de fréquence existantes. Bien que ce ne soit pas obligatoire, nous vous recommandons vivement de définir au moins une règle de limite de fréquence qui capture tous les messages, quel que soit le canal, l'étiquette ou la catégorie. Cette règle de limite de fréquence capturera chaque message activé pour la priorisation des messages afin que les messages priorisés soient comparés entre eux, et pas seulement avec d'autres messages partageant les mêmes caractéristiques.

Pour configurer cela, allez dans **Paramètres** > **Règles de limite de fréquence**. Créez une règle où le canal est **Tout canal applicable** et les filtres supplémentaires sont **Aucun**.

![Un exemple de règle de limite de fréquence pour tout canal applicable et sans filtres supplémentaires.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization11.png %})

Vous pouvez également créer des règles de limite de fréquence par catégorie. Cela vous permet de gérer vos messages marketing pour éviter d'envoyer trop de messages d'une catégorie donnée simplement parce qu'elle est marquée comme haute priorité. Sélectionnez **Catégorie de priorisation des messages** sous **Filtres supplémentaires**, puis sélectionnez une catégorie dans le menu déroulant.

![Un exemple de règle de limite de fréquence avec le menu déroulant du champ « Catégorie » pour sélectionner P2 ou P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Les messages en dehors de la priorisation des messages partagent les limites de fréquence avec les messages priorisés, de sorte que même un message de haute priorité peut être annulé en raison d'un message en dehors de la priorisation des messages.

## Questions fréquemment posées {#frequently-asked-questions}

### Comment les égalités sont-elles départagées entre les messages d'une même catégorie ? {#how-are-ties-broken-between-messages-in-the-same-category}

Lors de la priorisation de deux messages de la même catégorie, nous donnerons une priorité plus élevée au message dont l'heure d'envoi est la plus proche. Pour les Campaigns récurrentes, l'heure d'envoi est calculée comme la prochaine occurrence à partir de minuit aujourd'hui, heure de l'entreprise. Pour les Campaigns planifiées en heure locale, nous supposerons une heure d'envoi en heure de l'entreprise.

### Quelle est la relation entre la priorisation des messages et la limite de fréquence ? {#what-is-the-relationship-between-message-prioritization-and-frequency-capping}

Au moment de l'envoi, nous comparerons le message en cours d'envoi avec les autres messages que l'utilisateur est éligible à recevoir, qui suivent la même règle de limite de fréquence et qui sont activés pour la priorisation des messages. Le message sera envoyé si :

1. La règle de limite de fréquence concernée n'a pas encore été atteinte pour cet utilisateur, et
2. L'envoi de ce message à cet utilisateur ne provoquerait pas l'atteinte d'une limite avant l'envoi d'un message ultérieur de priorité supérieure.

### Comment puis-je m'assurer qu'un message est toujours envoyé ? {#how-can-i-make-sure-a-message-is-always-sent}

Il peut y avoir des scénarios où vous souhaitez qu'un message soit toujours envoyé, comme dans le cas de notifications transactionnelles ou légales. Dans ce cas, vous devriez désactiver la limite de fréquence pour ce message (ce qui le rend également inéligible à la priorisation des messages). Cela enverra le message chaque fois qu'il est planifié ou déclenché, sans tenir compte des autres envois en cours.

### Quand les messages sont-ils réellement priorisés ? Y a-t-il un calendrier ? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Chaque message est priorisé à son propre moment d'envoi planifié. Il n'y a pas de moment d'évaluation universel pour les messages priorisés.

### Mon message était planifié pour être envoyé, mais il ne l'a pas encore été en raison d'une limite de débit ou d'autres retards. Qu'est-ce que cela signifie pour la priorisation des autres Campaigns ? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Nous supposerons que votre message a été envoyé à l'heure initialement planifiée s'il est encore en cours de traitement. Nous utiliserons cette hypothèse pour déterminer s'il faut envoyer d'autres messages priorisés à venir. Lorsque ce message sera finalement envoyé, nous utiliserons l'heure d'envoi réelle.

### Mon message a été priorisé mais annulé à la dernière minute. Qu'est-ce que cela signifie pour la priorisation ? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Lorsqu'un message est priorisé, Braze supposera qu'il a été envoyé à l'heure initialement planifiée. De manière générale pour la priorisation des messages, nous ne recommandons pas d'utiliser les abandons Liquid. Si un message est abandonné en raison de la [logique Liquid `abort_message`](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), nous supposerons qu'il a été envoyé à cet utilisateur et prioriserons les futures Campaigns en conséquence.

Imaginons que vous avez deux messages : Message 1 et Message 2. Si le Message 1 est abandonné en faveur d'un futur Message 2 de priorité supérieure, cela ne garantit pas que le Message 2 sera effectivement envoyé. Le Message 2 peut toujours être abandonné pour diverses raisons, notamment :

- Les abandons Liquid
- L'utilisateur ne faisant plus partie du segment
- Les limites de fréquence en raison d'un message en dehors des règles de priorisation.

Si le Message 2 est abandonné, il n'y aura pas de nouvelle tentative d'envoi du Message 1.

Notez qu'un utilisateur pourrait recevoir un message de priorité inférieure, mais pas un message de priorité supérieure pour la même règle de limite de fréquence, pour les raisons suivantes :

- Le message de priorité supérieure a été limité en fréquence par une règle différente.
- Le message de priorité supérieure était en conflit avec une autre Campaign future de priorité encore plus élevée pour une règle différente.
- Au moment de l'envoi du message de priorité inférieure, l'utilisateur ne faisait pas partie de l'audience du message de priorité supérieure.
- Les deux messages auraient dû pouvoir être envoyés, mais un message en dehors de la configuration de priorisation a été envoyé avant que le message de priorité supérieure ne puisse être envoyé.

### Puis-je activer les Canvas pour la priorisation des messages ? {#can-i-opt-canvases-into-message-prioritization}

Non. Pour le moment, vous ne pouvez pas activer les Canvas pour la priorisation des messages.

### Qu'en est-il des Campaigns déclenchées par une action ou par l'API ? {#what-about-action-based-or-api-triggered-campaigns}

Pour le moment, la priorisation des messages n'est pas prise en charge pour les Campaigns déclenchées par une action ou par l'API.

### Existe-t-il des fonctionnalités de reporting ou d'analyse spécifiques à la priorisation des messages ? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Pour le moment, il n'existe pas de fonctionnalité de reporting ou d'analyse spécifique à cette fonctionnalité. Nous vous encourageons à utiliser les [fonctionnalités de reporting existantes de Braze](https://www.braze.com/docs/user_guide/analytics/reporting) pour surveiller la santé et les performances de vos Campaigns priorisées.