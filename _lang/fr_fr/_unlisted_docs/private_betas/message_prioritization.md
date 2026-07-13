---
article_title: Priorisation des messages
permalink: /message_prioritization/
toc_headers: h2
description: "Cet article de référence décrit la priorisation des messages au niveau supérieur et comment la configurer pour votre espace de travail."
---

# Priorisation des messages {#message-prioritization}

> Utilisez la priorisation des messages pour vous assurer que vos utilisateurs reçoivent les Campaigns qui comptent le plus.

{% alert important %}
La priorisation des messages est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cette bêta.<br><br>Cet article reflète la version de la priorisation des messages prévue pour la mise en production fin juillet 2026. Certains comportements décrits ici peuvent ne pas encore être disponibles dans tous les espaces de travail bêta.
{% endalert %}

Seuls les administrateurs peuvent configurer les paramètres de priorisation des messages au niveau supérieur. Les utilisateurs avec des droits limités peuvent consulter chaque page de cette section, mais ne peuvent pas effectuer de modifications.

Pour accéder aux paramètres de priorisation des messages au niveau supérieur, allez dans **Paramètres** > **Priorisation des messages**.

## Fonctionnement {#how-it-works}

Utilisez la priorisation des messages pour créer des [catégories](#categories) et des [règles de priorisation](#prioritization-rules) afin de classer l'ordre d'envoi de vos messages.

Imaginons qu'une marque de beauté gère des promotions par e-mail pour des partenariats payants et des programmes de fidélité. Avec la priorisation des messages, elle crée deux catégories nommées « Partenariats payants » et « Fidélité ». La marque classe ces catégories en fonction de leur importance stratégique. Pendant la période des fêtes, elle classe « Fidélité » plus haut que « Partenariats payants » pour donner la priorité aux clients qui font partie du programme d'adhésion depuis plus d'un an.

![Un exemple de règles de priorisation pour deux catégories : Partenariats payants et Fidélité.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

Au moment de l'envoi, Braze compare le message en cours d'envoi avec les autres messages que l'utilisateur pourrait recevoir et qui sont activés pour la priorisation, ont une catégorie de priorité définie et comptent dans la même règle de limite de fréquence au sein de la même fenêtre de limite de fréquence. Si l'envoi du message actuel empêcherait un message de priorité supérieure d'être envoyé plus tard, Braze dépriorise le message de priorité inférieure. Selon la fenêtre de nouvelle tentative configurée, ce message de priorité inférieure est soit réessayé plus tard, soit non envoyé.

La priorisation des messages peut évaluer :

- Les Campaigns planifiées
- Les Campaigns déclenchées par une action
- Les Canvas

Braze utilise sa prédiction du moment où chaque message devrait être envoyé pour évaluer si l'envoi d'un message maintenant pourrait empêcher un message de priorité supérieure d'être envoyé plus tard. Pour plus d'informations sur la façon dont Braze prédit le moment d'envoi futur des Campaigns et des Canvas, consultez [Comment Braze prédit-il le moment d'envoi d'un futur message ?](#how-does-braze-predict-when-a-future-message-sends)

### Types de messages pris en charge {#supported-message-types}

La priorisation des messages prend en charge les mêmes canaux que la limite de fréquence :

- Notifications push
- E-mail
- SMS
- Webhooks
- WhatsApp
- LINE

Pour la priorisation et la limite de fréquence, les notifications push iOS, Android, web et les autres plateformes de notifications push sont traitées comme un seul canal push partagé, et non comme des canaux séparés.

## Catégories {#categories}

Les règles de priorisation reposent sur un classement de catégories, qui est un libellé que vous pouvez attribuer à une Campaign ou un Canvas donné (similaire à une [étiquette]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). Vous pouvez créer jusqu'à 20 catégories à un moment donné.

Pour ajouter une nouvelle catégorie :

1. Allez dans **Paramètres** > **Priorisation des messages** > **Catégories**.
2. Sélectionnez **Créer une nouvelle catégorie**.

![Le bouton « Créer une nouvelle catégorie » dans la section Priorisation des messages.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Donnez un nom à la catégorie et une description facultative.
4. Sélectionnez **Créer la catégorie**.

![Un exemple de catégorie nommée « P3 » avec la description « Ceci est ma troisième catégorie de priorité la plus élevée. »]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Pour modifier ou supprimer une catégorie, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>.

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

Pour réorganiser les règles, sélectionnez et faites glisser l'icône <i class="fa-solid fa-grip-vertical"></i> sur une règle. Pour supprimer une règle, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i> puis **Supprimer la règle**.

N'oubliez pas de sélectionner **Enregistrer** pour que vos modifications soient appliquées.

## Paramètres au niveau de la Campaign {#campaign-level-settings}

### Activation {#opt-in}

Pour activer la priorisation d'une Campaign, cochez la case **Activer la priorisation des messages** dans les paramètres de réception de la Campaign.

![La case à cocher « Activer la priorisation des messages ».]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Ensuite, attribuez la Campaign à une catégorie en en sélectionnant une dans le menu déroulant **Catégorie**.

![Le menu déroulant de catégorie de priorisation des messages dans les paramètres de réception d'une Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

La priorisation des messages prend en charge les Campaigns planifiées et les Campaigns déclenchées par une action.

### Timing intelligent {#intelligent-timing}

Pour les Campaigns qui utilisent le timing intelligent, la priorisation des messages compare les messages en utilisant l'heure d'envoi que Braze sélectionne pour chaque utilisateur au lieu de se baser uniquement sur la planification initiale de la Campaign. Cela permet à Braze de prendre en compte le message le plus susceptible d'être envoyé en premier à cet utilisateur.

Pour les Campaigns récurrentes avec timing intelligent, Braze peut utiliser l'heure d'envoi connue sélectionnée pour la récurrence en cours lorsqu'il compare cette Campaign avec d'autres messages priorisés éligibles.

### Fenêtre de nouvelle tentative {#retry-window}

Une fenêtre de nouvelle tentative permet aux messages activés de réessayer pendant un maximum de trois jours si la première tentative n'a pas une priorité suffisamment élevée pour être envoyée. Chaque jour suivant, à la même heure que le message était initialement planifié ou déclenché, une nouvelle tentative d'envoi est effectuée. Après le dernier jour de la fenêtre de nouvelle tentative, si le message n'a toujours pas été envoyé, il n'est plus réessayé et est définitivement dépriorisé.

Pour les Campaigns planifiées récurrentes, la fenêtre de nouvelle tentative doit être plus courte que l'intervalle minimum entre les envois de cette Campaign. Les nouvelles tentatives ont toujours lieu un jour à la fois à partir de l'heure d'envoi initiale, même si la Campaign n'est normalement pas planifiée pour être envoyée ce jour-là. Par exemple, si vous avez une Campaign qui envoie tous les lundis et mercredis, la tentative de nouvelle tentative a lieu le mardi, donc la fenêtre de nouvelle tentative doit être définie à un jour. Si vous avez une Campaign qui envoie tous les lundis, mercredis et vendredis, et que l'envoi du vendredi est réessayé avec une fenêtre de nouvelle tentative d'un jour, la tentative de nouvelle tentative a lieu le samedi, pas le lundi.

![Le paramètre « Fenêtre de nouvelle tentative » défini à 1 jour.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Pour les Campaigns déclenchées par une action, les nouvelles tentatives sont basées sur l'heure à laquelle le message déclenché devait initialement être envoyé.

Les Campaigns déclenchées par une action qui utilisent des événements d'exception ne prennent pas en charge les fenêtres de nouvelle tentative.

Les fenêtres de nouvelle tentative pour les messages Canvas sont configurées au niveau de l'étape. Pour les étapes de message Canvas prises en charge, si une étape de message Canvas est dépriorisée et qu'une fenêtre de nouvelle tentative est configurée, Braze peut réessayer cette étape plus tard dans sa fenêtre de nouvelle tentative.

## Paramètres au niveau du Canvas {#canvas-level-settings}

Pour activer la priorisation des messages pour un Canvas, activez la priorisation des messages dans les paramètres du Canvas et attribuez le Canvas à une catégorie.

Lorsqu'un utilisateur est éligible pour plusieurs messages priorisés, Braze évalue les Campaigns activées et les étapes de message Canvas éligibles ensemble sur les canaux pris en charge.

Pour les Campaigns, cela inclut les envois planifiés et déclenchés par une action éligibles.

Pour les Canvas, cela inclut :

- Les Canvas planifiés futurs auxquels l'utilisateur est éligible pour entrer
- Les Canvas dans lesquels l'utilisateur se trouve actuellement

La priorisation Canvas n'est pas en tout ou rien. Une Campaign de priorité supérieure peut entraîner la dépriorisation d'une étape Canvas tandis que des étapes éligibles ultérieures dans ce même Canvas peuvent toujours être envoyées, en fonction du classement des catégories, du moment d'envoi et des règles de limite de fréquence.

### Comment Braze évalue les futurs messages {#how-braze-evaluates-future-messages}

Braze évalue les Campaigns et les Canvas différemment selon le type de message.

#### Campaigns

Braze compare chaque message de Campaign éligible en utilisant l'heure à laquelle ce message devrait être envoyé.

#### Canvas {#canvases}

Braze parcourt le Canvas pour déterminer quels futurs messages un utilisateur pourrait recevoir, en commençant par :

- L'entrée dans le Canvas, pour les Canvas planifiés futurs
- L'étape actuelle de l'utilisateur, si l'utilisateur est déjà dans le Canvas

Braze évalue ensuite les étapes Canvas de la manière suivante.

##### Étapes de messagerie {#messaging-steps}

Ces étapes sont comptabilisées pour la priorisation et ajoutées à l'ensemble des messages éligibles lorsqu'elles envoient sur un canal pris en charge.

- Étape Message
- Étape Content Optimizer

##### Étapes de continuation {#continuation-steps}

Ces étapes sont ignorées pour la priorisation et n'affectent pas l'anticipation.

- Étape Mise à jour du contexte
- Étape Mise à jour de l'utilisateur
- Étape Audience Sync
- Étape Feature Flag
- Étape Délai avec un délai fixe

##### Étapes de limite {#boundary-steps}

Braze arrête l'anticipation à ces étapes jusqu'à ce que l'utilisateur progresse réellement à travers elles dans le Canvas.

- Étape Délai avec un délai personnalisé
- Étape Délai qui suit une étape de branchement
- Étape Parcours d'action
- Étape Expérience

##### Étapes de branchement {#branching-steps}

Ces étapes divisent le Canvas en plusieurs parcours possibles.

- Étape Arbre décisionnel
- Étape Parcours d'audience

Lorsqu'un parcours de priorisation contient des étapes de branchement, Braze suppose que tous les parcours sont viables et prend en compte toutes les étapes de message parallèles sur les canaux pris en charge pour la priorisation. Étant donné que les règles de limite de fréquence peuvent être spécifiques à un canal, les étapes de message parallèles sont dédupliquées par canal si nécessaire.

Par exemple, si une branche peut envoyer un e-mail et qu'une autre branche peut également envoyer un e-mail, Braze les traite comme un seul envoi d'e-mail possible pour la priorisation prospective. Si une autre branche peut envoyer une notification push, Braze prend également en compte cet envoi push possible séparément.

Pour les étapes de message Canvas qui utilisent le timing intelligent, Braze prédit le moment d'envoi au mieux jusqu'à ce que l'utilisateur atteigne réellement cette étape. Une fois que l'utilisateur entre dans l'étape de timing intelligent et que Braze calcule l'heure d'envoi par utilisateur, la priorisation des messages utilise cette heure d'envoi calculée pour l'étape en cours. Sur les parcours déterministes, Braze reflète également ce moment mis à jour dans les étapes de message suivantes lors de la détermination de leurs heures d'envoi prévues.

Les étapes Content Optimizer sont traitées comme des étapes de messagerie car elles envoient toujours sur un canal spécifié. Cependant, les fenêtres de nouvelle tentative ne s'appliquent pas aux étapes Content Optimizer car une nouvelle tentative interférerait avec l'expérience. Les autres étapes de messagerie Canvas prises en charge peuvent utiliser des fenêtres de nouvelle tentative. Les étapes Canvas sur des canaux non pris en charge ne participent pas à la priorisation des messages.

## Limites de fréquence {#frequency-caps}

La priorisation des messages fonctionne dans le cadre de vos règles de limite de fréquence existantes. Un message priorisé ne peut être envoyé que si :

1. La règle de limite de fréquence concernée n'a pas encore été atteinte pour cet utilisateur, et
2. L'envoi de ce message ne provoquerait pas l'atteinte d'une limite par l'utilisateur avant qu'un message ultérieur de priorité supérieure ne puisse être envoyé.

Les messages qui ne sont pas soumis à la limite de fréquence ne sont pas éligibles à la priorisation des messages. Si vous souhaitez qu'un message soit toujours envoyé, désactivez la limite de fréquence pour celui-ci. Cela le retire également de la priorisation des messages.

### Pour les Campaigns et étapes Canvas prises en charge {#for-supported-campaigns-and-canvas-steps}

Pour être éligible à la priorisation des messages, la Campaign ou l'étape Canvas doit utiliser un canal pris en charge et être évaluée dans le cadre de votre configuration de limite de fréquence.

![Un exemple de règle de limite de fréquence.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Règles de limite de fréquence {#frequency-capping-rules}

Braze optimise la priorité dans le cadre de vos règles de limite de fréquence existantes. Les messages priorisés ne sont comparés que lorsqu'ils partagent la même règle de limite de fréquence applicable.

Par exemple, deux Campaigns e-mail qui comptent dans la même règle de limite de fréquence e-mail peuvent être priorisées l'une par rapport à l'autre. Une Campaign e-mail de priorité inférieure n'est pas dépriorisée en faveur d'un message SMS de priorité supérieure, sauf si les deux messages comptent dans la même règle de limite de fréquence.

Vous pouvez utiliser des règles de limite de fréquence spécifiques à un canal, des règles spécifiques à une catégorie, des filtres par étiquette ou des règles qui s'appliquent à tous les canaux. La priorisation des messages fonctionne avec toutes les règles qui s'appliquent à vos messages activés.

Vous pouvez créer des règles de limite de fréquence par catégorie pour gérer le nombre de messages qu'un utilisateur reçoit d'une catégorie donnée. Cela permet d'éviter qu'une catégorie de haute priorité n'envoie trop de messages. Sélectionnez **Catégorie de priorisation des messages** sous **Filtres supplémentaires**, puis sélectionnez une catégorie dans le menu déroulant.

![Un exemple de règle de limite de fréquence avec le menu déroulant du champ « Catégorie » pour sélectionner P2 ou P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Les messages en dehors de la priorisation des messages partagent les limites de fréquence avec les messages priorisés, de sorte que même un message de haute priorité peut être annulé en raison d'un message en dehors de la priorisation des messages.

## Exemples {#examples}

### Campaign de priorité supérieure contre Campaign de priorité inférieure {#higher-priority-campaign-versus-lower-priority-campaign}

Supposons qu'un utilisateur est éligible pour deux Campaigns e-mail le même jour, et que les deux Campaigns comptent dans la même règle de limite de fréquence. Si la Campaign de priorité supérieure devrait être envoyée plus tard dans la journée, Braze peut déprioriser la Campaign de priorité inférieure afin que la Campaign de priorité supérieure puisse être envoyée à la place. Si la Campaign de priorité inférieure dispose d'une fenêtre de nouvelle tentative, Braze peut la réessayer plus tard.

### Campaign déclenchée par une action de priorité supérieure contre message de priorité inférieure {#higher-priority-action-based-campaign-versus-lower-priority-message}

Supposons qu'un utilisateur déclenche une Campaign déclenchée par une action de priorité supérieure qui est configurée pour être envoyée deux heures plus tard. Pendant ce délai, Braze peut prendre en compte cette Campaign déclenchée par une action à venir lorsqu'il décide si un autre message priorisé doit être envoyé en premier. Cela permet d'éviter qu'un message de priorité inférieure ne soit envoyé maintenant si la Campaign déclenchée par une action de priorité supérieure devrait être envoyée bientôt.

### Canvas de priorité supérieure contre Campaign de priorité inférieure {#higher-priority-canvas-versus-lower-priority-campaign}

Supposons qu'un utilisateur est éligible pour une Campaign de priorité inférieure, mais qu'il devrait également recevoir un message Canvas de priorité supérieure plus tard dans la journée. Si Braze peut déjà évaluer ce futur message Canvas, il peut déprioriser la Campaign de priorité inférieure afin que le message Canvas de priorité supérieure puisse être envoyé à la place.

### Canvas de priorité supérieure avec une étape de limite contre Campaign de priorité inférieure {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Supposons qu'un Canvas de priorité supérieure inclut une étape Parcours d'action, une expérience ou un délai personnalisé avant sa prochaine étape de message. Tant que l'utilisateur n'a pas atteint et dépassé cette étape, Braze n'anticipe pas le message Canvas de priorité supérieure en aval. Dans ce cas, une Campaign de priorité inférieure peut tout de même être envoyée en premier.

### Canvas de branchement de priorité supérieure contre message de priorité inférieure {#higher-priority-branching-canvas-versus-lower-priority-message}

Supposons qu'un Canvas de priorité supérieure peut envoyer différents messages selon la branche que suit un utilisateur. Braze évalue ces futurs parcours possibles de manière conservatrice lors de la comparaison des messages. Cela permet d'éviter qu'un message de priorité inférieure ne soit envoyé maintenant si une branche Canvas de priorité supérieure pourrait utiliser cette même limite de fréquence plus tard.

### Étape Canvas avec timing intelligent et étapes en aval {#canvas-intelligent-timing-step-and-downstream-steps}

Supposons qu'un utilisateur entre dans une étape de message Canvas de priorité supérieure qui utilise le timing intelligent. Une fois que Braze calcule l'heure d'envoi de cet utilisateur pour l'étape de timing intelligent, la priorisation des messages utilise cette heure d'envoi par utilisateur pour l'étape en cours et pour les étapes de message ultérieures sur le même parcours déterministe. Cela permet à Braze de comparer les messages Canvas en aval avec d'autres envois priorisés en utilisant le moment mis à jour au lieu de se baser uniquement sur l'estimation de parcours antérieure.

## Limitations

La priorisation des messages présente les limitations suivantes :

- Jusqu'à 20 catégories par espace de travail
- Jusqu'à 10 règles de priorisation par espace de travail
- Jusqu'à 25 éléments planifiés actifs activés pour la priorisation à la fois
- Jusqu'à 25 éléments déclenchés par une action actifs activés pour la priorisation à la fois
- Fenêtres de nouvelle tentative de 3 jours maximum

La limite d'éléments planifiés est un total combiné entre les Campaigns planifiées et les Canvas planifiés activés. La limite d'éléments déclenchés par une action est un total combiné entre les Campaigns déclenchées par une action et les Canvas déclenchés par une action activés.

## Questions fréquemment posées {#frequently-asked-questions}

### Comment les égalités sont-elles départagées entre les messages d'une même catégorie ? {#how-are-ties-broken-between-messages-in-the-same-category}

Lors de la priorisation de deux Campaigns de la même catégorie, Braze donne une priorité plus élevée à celle dont l'heure d'envoi est la plus proche. Si une fenêtre de nouvelle tentative est configurée, Braze utilise la fin de cette fenêtre de nouvelle tentative lors de la comparaison des Campaigns au sein de la même règle de priorité. Pour les Campaigns récurrentes, l'heure d'envoi est calculée comme la prochaine occurrence à partir de minuit, heure de l'entreprise. Pour les Campaigns planifiées en heure locale, Braze suppose une heure d'envoi en heure de l'entreprise.

Pour les Canvas de la même catégorie, Braze utilise le moment d'entrée dans le Canvas comme critère de départage afin que toutes les étapes d'un même Canvas conservent la même priorité relative par rapport aux autres Campaigns et Canvas.

### Comment puis-je m'assurer qu'un message est toujours envoyé ? {#how-can-i-make-sure-a-message-is-always-sent}

Il peut y avoir des scénarios où vous souhaitez qu'un message soit toujours envoyé, comme dans le cas de notifications transactionnelles ou juridiques. Dans ce cas, vous devriez désactiver la limite de fréquence pour ce message, ce qui le rend également inéligible à la priorisation des messages. Cela enverra le message chaque fois qu'il est planifié ou déclenché, sans tenir compte des autres envois en cours.

### Quand les messages sont-ils réellement priorisés ? Y a-t-il un calendrier ? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Chaque message est priorisé en fonction de son moment d'envoi prévu. Il n'y a pas de moment d'évaluation universel pour les messages priorisés.

### Comment Braze prédit-il le moment d'envoi d'un futur message ? {#how-does-braze-predict-when-a-future-message-sends}

Braze prédit le moment d'envoi futur différemment pour chaque type de message :

- **Campaigns planifiées :** Braze utilise l'heure à laquelle chaque Campaign devrait être envoyée. Pour les Campaigns planifiées qui utilisent le timing intelligent, Braze utilise l'heure d'envoi optimale de chaque utilisateur pour cette occurrence de Campaign.
- **Campaigns déclenchées par une action :** Braze utilise l'heure à laquelle chaque message déclenché devrait être envoyé, y compris tout délai configuré entre le déclenchement et l'envoi.
- **Étapes Canvas :** Braze utilise l'entrée de l'utilisateur dans le Canvas ou sa position actuelle dans le Canvas, plus le moment des étapes en aval. Pour les étapes de message Canvas qui utilisent le timing intelligent, une fois qu'un utilisateur entre dans cette étape, Braze utilise l'heure d'envoi par utilisateur qu'il calcule pour cet utilisateur. Pour les étapes de message suivantes sur le même parcours de priorisation déterministe, Braze utilise cette heure d'envoi du timing intelligent pour déterminer le moment d'envoi prévu ultérieur. Avant qu'un utilisateur n'atteigne l'étape de timing intelligent, la prédiction reste au mieux.

### Mon message était planifié pour être envoyé, mais il ne l'a pas encore été en raison d'une limitation du débit ou d'autres retards. Qu'est-ce que cela signifie pour la priorisation des autres Campaigns ? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Braze suppose que votre message a été envoyé à l'heure initialement planifiée s'il est encore en cours de traitement, ce qui détermine s'il faut envoyer d'autres messages priorisés à venir. Lorsque ce message est finalement envoyé, Braze utilise l'heure d'envoi réelle.

### Mon message a été priorisé mais annulé à la dernière minute. Qu'est-ce que cela signifie pour la priorisation ? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Lorsqu'un message est priorisé, Braze suppose qu'il a été envoyé à l'heure initialement planifiée. De manière générale pour la priorisation des messages, nous ne recommandons pas d'utiliser les abandons Liquid. Si un message est abandonné en raison de la [logique Liquid `abort_message`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), nous supposerons qu'il a été envoyé à cet utilisateur et prioriserons les futures Campaigns en conséquence.

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

### Comment les étapes de limite affectent-elles la priorisation Canvas ? {#how-do-boundary-steps-affect-canvas-prioritization}

Les étapes de limite arrêtent l'anticipation à travers le Canvas jusqu'à ce que l'utilisateur atteigne ou termine réellement ce point dans le Canvas. Par exemple, si un message de priorité supérieure se trouve après une étape Parcours d'action, un délai personnalisé ou une étape d'expérience, Braze n'utilise pas ce message en aval pour bloquer une Campaign de priorité inférieure tant que l'utilisateur n'a pas dépassé cette limite.

### Comment fonctionne le branchement dans la priorisation Canvas ? {#how-does-branching-work-in-canvas-prioritization}

Lorsqu'un Canvas contient des parcours de branchement, Braze suppose que chaque parcours est viable et compare le volume d'envoi futur le plus élevé possible par canal. Cela permet d'éviter d'envoyer un message de priorité inférieure maintenant si un parcours Canvas de priorité supérieure pourrait consommer cette même limite de fréquence plus tard.

### Que se passe-t-il si un utilisateur a plusieurs parcours à travers un Canvas priorisé en même temps ? {#what-happens-if-a-user-has-multiple-paths-through-a-prioritized-canvas-at-the-same-time}

Braze traite chaque parcours viable comme un futur parcours possible et évalue les étapes de message éligibles sur ces parcours de manière indépendante. Lorsque plusieurs parcours peuvent envoyer sur le même canal, Braze déduplique ces envois possibles par canal si nécessaire.

### Comment fonctionne le timing intelligent dans la priorisation Canvas ? {#how-does-intelligent-timing-work-in-canvas-prioritization}

Avant qu'un utilisateur n'atteigne une étape de message Canvas avec timing intelligent, Braze prédit le moment d'envoi de cette étape au mieux. Une fois que l'utilisateur entre dans l'étape et que Braze calcule l'heure d'envoi par utilisateur, la priorisation des messages utilise cette heure d'envoi calculée pour l'étape en cours et pour les étapes de message suivantes sur le même parcours de priorisation déterministe.

### Existe-t-il des fonctionnalités de reporting ou d'analytique spécifiques à la priorisation des messages ? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze fournit des événements liés à la priorisation des messages dans Currents et le partage de données pour les canaux pris en charge, notamment l'e-mail, LINE, les notifications push, le SMS, les webhooks et WhatsApp. Ceux-ci incluent les événements de dépriorisation et de limitation de fréquence, enregistrés dans la table `users.messages.<channel>.abort`, ainsi que les événements de nouvelle tentative qui indiquent quand un message a été réessayé ultérieurement dans la fenêtre de nouvelle tentative configurée, enregistrés dans la table `user_messages_<channel>_retry`.

Pour les Campaigns, vous pouvez également utiliser le tableau de bord de diagnostic de messagerie, les statistiques quotidiennes existantes de dépriorisation et de nouvelle tentative, ainsi que les [fonctionnalités de reporting existantes de Braze]({{site.baseurl}}/user_guide/analytics/reporting) pour surveiller la santé et les performances de vos Campaigns et Canvas priorisés.