---
article_title: Priorisation des messages
permalink: /message_prioritization/
toc_headers: h2
description: "Cet article de référence décrit la priorisation des messages au niveau supérieur et comment la configurer pour votre espace de travail."
---

# Priorisation des messages {#message-prioritization}

> Utilisez la priorisation des messages pour vous assurer que vos utilisateurs reçoivent les messages qui comptent le plus pour votre entreprise, et pas seulement ceux qui sont envoyés en premier.

{% alert important %}
La priorisation des messages est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cette bêta.<br><br>Cet article reflète la version de la priorisation des messages prévue pour la mise en production fin juillet 2026. Certains comportements décrits ici peuvent ne pas encore être disponibles dans tous les espaces de travail bêta.
{% endalert %}

## Pourquoi utiliser la priorisation des messages ? {#why-use-message-prioritization}

Les utilisateurs ne peuvent recevoir qu'un nombre limité de messages avant que le volume ne devienne problématique. Les messages qui leur parviennent doivent être ceux qui comptent le plus pour votre activité. La priorisation des messages garantit que vos messages à plus forte valeur remportent cet espace limité, plutôt que de laisser le hasard décider.

La plupart des équipes contrôlent le volume de messages grâce aux limites de fréquence. Utilisées seules, les limites de fréquence sont un outil grossier. Une fois qu'un utilisateur atteint sa limite, c'est le moment d'envoi qui détermine quels messages passent, et non l'importance commerciale.

Une promotion à faible valeur envoyée en premier peut occuper un créneau qu'une récompense de fidélité ou un message urgent aurait utilisé plus tard dans la journée. Les équipes contournent souvent ce problème avec des règles de limitation distinctes, une planification manuelle et des filtres ad hoc. Ces approches nécessitent une maintenance constante. Elles deviennent plus difficiles à gérer à mesure que les Campaigns et les Canvas évoluent. Et elles ne peuvent toujours pas garantir que le bon message l'emporte.

La priorisation des messages transforme l'allocation des limites de fréquence, passant du **premier arrivé, premier servi** à une logique **consciente des priorités métier** : vous définissez ce qui compte, et Braze prend les décisions d'envoi pour vous.

La priorisation des messages offre plusieurs avantages :

- **Définissez une fois ce qui compte :** Utilisez des catégories et des règles hiérarchisées pour encoder vos priorités, par exemple « Fidélité » avant « Partenariats payants ». Chaque envoi vers un utilisateur abonné respecte automatiquement ces classements.
- **Décisions anticipées :** Braze prédit ce qu'un utilisateur pourrait recevoir plus tard. Il peut retenir un message de priorité inférieure pour préserver l'espace de limitation à un message de priorité supérieure.
- **Fonctionne avec tous les types de messages et canaux :** Les Campaigns planifiées, les Campaigns basées sur une action et les étapes Canvas sont en concurrence dans un même pool hiérarchisé au sein de vos limites de fréquence partagées.
- **Fenêtres de nouvelle tentative :** Un message dépriorisé peut être renvoyé si de la capacité se libère. Cela améliore la répartition des messages sans abandonner totalement les envois de priorité inférieure.

Le résultat : le même volume d'envoi plafonné, automatiquement alloué aux messages qui comptent le plus.

La priorisation des messages est particulièrement précieuse pour les expéditeurs à fort volume qui atteignent régulièrement leurs limites de fréquence. Elle fonctionne au mieux lorsque la valeur des messages est clairement différenciée, par exemple les messages de fidélité ou générateurs de revenus par rapport aux promotions courantes.

## Fonctionnement {#how-it-works}

Utilisez la priorisation des messages pour créer des [catégories](#categories) et des [règles de priorisation](#prioritization-rules) afin de classer l'ordre d'envoi de vos messages.

Pour gérer ces paramètres, accédez à **Paramètres** > **Priorisation des messages**. Seuls les administrateurs peuvent configurer les paramètres de priorisation des messages de niveau supérieur. Les utilisateurs ont besoin de la permission « View Message Prioritization » pour consulter les paramètres de cette section et de la permission « Edit Message Prioritization » pour les modifier.

Par exemple, une marque de cosmétiques qui gère des promotions par e-mail pour des partenariats payants et des programmes de fidélité utilise la priorisation des messages pour créer deux catégories : « Partenariats payants » et « Fidélité ». La marque classe ces catégories par importance commerciale. Pendant la période des fêtes, elle place « Fidélité » en premier et « Partenariats payants » en second afin de privilégier les membres de longue date.

![Un exemple de règles de priorisation pour deux catégories : Partenariats payants et Fidélité.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

Au moment de l'envoi, Braze compare le message en cours d'envoi avec les autres messages que l'utilisateur pourrait recevoir et qui sont inscrits à la priorisation, ont une catégorie de priorité définie et sont soumis à la même règle de limite de fréquence dans la même fenêtre de limite de fréquence. Si l'envoi du message actuel empêcherait un message de priorité supérieure d'être envoyé ultérieurement, Braze dépriorise le message de priorité inférieure. En fonction de la fenêtre de réessai configurée, ce message de priorité inférieure est soit réessayé plus tard, soit non envoyé.

La priorisation des messages peut évaluer :

- Les Campaigns planifiées
- Les Campaigns basées sur une action
- Les Canvas

Actuellement, les Campaigns ou Canvas déclenchés par API ne sont pas pris en charge par la priorisation des messages et ne participent pas à la priorisation.

Braze utilise sa prédiction du moment prévu d'envoi de chaque message pour évaluer si l'envoi d'un message maintenant pourrait empêcher un message de priorité supérieure d'être envoyé plus tard. Pour plus d'informations sur la façon dont Braze prédit le moment d'envoi futur des Campaigns et des Canvas, consultez [Comment Braze prédit-il le moment d'envoi d'un futur message ?](#how-does-braze-predict-when-a-future-message-sends)

### Canaux de messages pris en charge {#supported-message-channels}

La priorisation des messages prend en charge les mêmes canaux que la limite de fréquence :

- Notifications push
- E-mail
- SMS
- Webhooks
- WhatsApp
- LINE

Pour la priorisation et la limite de fréquence, les notifications push iOS, Android, web et les autres plateformes de notifications push sont traitées comme un seul canal push partagé, et non comme des canaux distincts.

Ces canaux ne sont pas éligibles à la priorisation des messages car ils ne sont pas soumis à la limite de fréquence :

- Content Cards
- Messages in-app
- Banners

Les messages in-app et les Banners utilisent leurs propres paramètres de priorité pour décider quel message s'affiche lorsque plusieurs messages sont en concurrence pour le même déclencheur ou le même emplacement. Pour les messages in-app, consultez [Choisir une priorité]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority). Pour les Banners, consultez [Priorité des Banners]({{site.baseurl}}/user_guide/channels/banners#priority).

Si une Campaign ou une étape Canvas n'utilise que des canaux non éligibles, elle ne participera pas à la priorisation.

## Catégories {#categories}

Les règles de priorisation reposent sur un classement de catégories, qui sont des étiquettes que vous pouvez attribuer à une Campaign ou un Canvas donné (similaires à une [étiquette]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)). Il existe une limite au nombre de catégories que vous pouvez créer à un moment donné ; contactez votre gestionnaire de compte si vous souhaitez une limite plus élevée.

Pour ajouter une nouvelle catégorie :

1. Accédez à **Paramètres** > **Priorisation des messages** > **Catégories**.
2. Sélectionnez **Créer une nouvelle catégorie**.

![Le bouton « Créer une nouvelle catégorie » dans la section Priorisation des messages.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Donnez un nom à la catégorie et une description facultative.
4. Sélectionnez **Créer la catégorie**.

![Un exemple de catégorie nommée « P3 » avec la description « Ceci est ma troisième catégorie de priorité la plus élevée. »]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Pour modifier ou supprimer une catégorie, sélectionnez le menu <i class="fas fa-ellipsis-vertical" aria-label="Ouvrir le menu"></i>.

## Règles de priorisation {#prioritization-rules}

Une fois vos catégories configurées, vous pouvez les classer dans un ensemble de règles de priorisation. Les règles sont classées par ordre décroissant de priorité. Il existe une limite au nombre de règles de priorisation que vous pouvez créer à un moment donné ; contactez votre gestionnaire de compte si vous souhaitez une limite plus élevée.

1. Accédez à **Paramètres** > **Priorisation des messages** > **Règles de priorisation** pour configurer vos règles.

![Section « Règles de priorisation » sans aucune priorité définie.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Sélectionnez **Ajouter une règle**.
3. Sélectionnez une catégorie dans le menu déroulant.

![Règle de priorisation « Priorité 1 » avec P1 sélectionné comme catégorie.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continuez à ajouter des règles en sélectionnant **+ Ajouter une règle** sous votre dernière règle.

Pour réorganiser les règles, sélectionnez et faites glisser l'icône <i class="fa-solid fa-grip-vertical" aria-label="Réorganiser la règle"></i> sur une règle. Pour supprimer une règle, sélectionnez le menu <i class="fas fa-ellipsis-vertical" aria-label="Plus d'options"></i>, puis **Supprimer la règle**.

N'oubliez pas de sélectionner **Enregistrer** pour que vos modifications soient appliquées.

## Limites de fréquence {#frequency-caps}

La priorisation des messages fonctionne dans le cadre de vos règles de limite de fréquence existantes. Pour être éligible à la priorisation, une Campaign ou une étape du Canvas doit utiliser un canal pris en charge et être soumise à votre configuration de limite de fréquence. Les messages qui ne sont pas soumis à la limite de fréquence ne sont pas éligibles à la priorisation des messages. Si vous souhaitez qu'un message soit toujours envoyé, excluez-le de la limite de fréquence. Cela le retire également de la priorisation des messages.

Un message priorisé ne peut être envoyé que si :

1. La règle de limite de fréquence concernée n'a pas encore été atteinte pour cet utilisateur, et
2. L'envoi de ce message n'entraînerait pas le dépassement d'un plafond avant qu'un message ultérieur de priorité supérieure puisse être envoyé.

![Un exemple de règle de limite de fréquence.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

Vous pouvez utiliser des règles de limite de fréquence spécifiques à un canal, des règles spécifiques à une catégorie, des filtres par étiquette ou des règles qui s'appliquent à n'importe quel canal. La priorisation des messages fonctionne avec toutes les règles qui s'appliquent à vos messages activés.

Vous pouvez également créer des règles de limite de fréquence par catégorie pour gérer le nombre de messages qu'un utilisateur reçoit d'une catégorie donnée. Cela permet d'empêcher une catégorie de haute priorité d'envoyer trop de messages. Sélectionnez **Message prioritization category** sous **Additional filters**, puis sélectionnez une catégorie dans le menu déroulant.

![Un exemple de règle de limite de fréquence avec le menu déroulant du champ « Category » permettant de sélectionner P2 ou P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

## Abonnement {#opting-in}

### Abonnement d'une Campaign {#campaign-opt-in}

Pour inscrire une Campaign à la priorisation, cochez la case **Opt-in to Message Prioritization** dans les paramètres de réception de la Campaign.

![La case à cocher « Opt-in to Message Prioritization ».]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Ensuite, attribuez une catégorie à la Campaign en en sélectionnant une dans le menu déroulant **Category**.

![Le menu déroulant de catégorie de priorisation des messages dans les paramètres de réception d'une Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

La priorisation des messages prend en charge les Campaigns planifiées et les Campaigns basées sur une action. Les Campaigns déclenchées par API ne sont pas prises en charge.

### Abonnement d'un Canvas {#canvas-opt-in}

L'abonnement d'un Canvas fonctionne de manière similaire aux Campaigns. Pour inscrire un Canvas à la priorisation des messages, activez la priorisation des messages dans les paramètres du Canvas et attribuez-lui une catégorie. Toutes les étapes du Canvas partagent cette catégorie et le même niveau de priorité, ce qui signifie que vous ne pouvez pas définir la priorité individuellement par étape.

La priorisation des messages prend en charge les Canvas planifiés et les Canvas basés sur une action. Les Canvas déclenchés par API ne sont pas pris en charge.

## Timing intelligent {#intelligent-timing}

Avec le timing intelligent, Braze envoie un message au moment optimal d'envoi de chaque utilisateur, de sorte que la même Campaign ou la même étape de message Canvas peut atteindre différents utilisateurs à différents moments. La priorisation des messages en tient compte : au lieu de supposer que le message est envoyé à tout le monde à l'heure planifiée, elle classe les messages concurrents d'un utilisateur en utilisant le moment optimal d'envoi de cet utilisateur.

Pour les Campaigns et les étapes de message Canvas qui utilisent le timing intelligent, Braze prédit le moment d'envoi au mieux jusqu'à ce qu'il calcule le moment d'envoi optimal par utilisateur. Pour les Campaigns, la priorisation des messages utilise le moment optimal d'envoi de cet utilisateur pour l'occurrence en cours lorsqu'elle compare la Campaign aux autres messages prioritaires éligibles de l'utilisateur. Pour les Campaigns récurrentes avec timing intelligent, Braze utilise le moment optimal d'envoi choisi pour cette occurrence.

Pour les étapes de message Canvas, Braze met à jour cette prédiction une fois que l'utilisateur entre dans l'étape et que Braze calcule le moment optimal d'envoi de cet utilisateur pour l'étape. La priorisation des messages utilise ce moment d'envoi calculé pour l'étape en cours. Sur les parcours déterministes (parcours sans embranchement, où la séquence des étapes est fixe), Braze reflète également ce timing mis à jour dans les étapes de message suivantes lors de la détermination de leurs moments d'envoi prévus.

## Fenêtres de nouvelle tentative {#retry-windows}

Une fenêtre de nouvelle tentative permet aux messages ayant reçu l'abonnement de réessayer pendant un nombre limité de jours si la première tentative n'a pas une priorité suffisamment élevée pour être envoyée. La durée maximale de la fenêtre de nouvelle tentative dépend de votre édition de la plateforme Braze. Chaque jour suivant, à la même heure à laquelle le message était initialement planifié ou déclenché pour l'envoi, une nouvelle tentative d'envoi du message est effectuée. Après le dernier jour de la fenêtre de nouvelle tentative, si le message n'a toujours pas été envoyé, aucune nouvelle tentative n'est effectuée et le message est définitivement dépriorisé.

Pour les Campaigns planifiées récurrentes, la fenêtre de nouvelle tentative doit être plus courte que l'intervalle minimal entre les envois de cette Campaign. Les nouvelles tentatives ont toujours lieu un jour à la fois à partir de l'heure d'envoi initiale, même si la Campaign n'est normalement pas planifiée pour un envoi ce jour-là. Par exemple, si vous avez une Campaign qui envoie tous les lundis et mercredis, la nouvelle tentative a lieu le mardi, donc la fenêtre de nouvelle tentative doit être définie sur un jour. Si vous avez une Campaign qui envoie tous les lundis, mercredis et vendredis, et que l'envoi du vendredi fait l'objet d'une nouvelle tentative avec une fenêtre d'un jour, la nouvelle tentative a lieu le samedi, pas le lundi.

![Le paramètre « Fenêtre de nouvelle tentative » défini sur 1 jour.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Pour les Campaigns basées sur une action, les nouvelles tentatives sont basées sur l'heure à laquelle le message déclenché devait initialement être envoyé.

Les Campaigns basées sur une action qui utilisent des événements d'exception ne prennent pas en charge les fenêtres de nouvelle tentative.

Les fenêtres de nouvelle tentative pour les messages Canvas sont configurées au niveau de l'étape. Pour les étapes de messagerie Canvas prises en charge, si une étape de message Canvas est dépriorisée et qu'une fenêtre de nouvelle tentative est configurée, Braze peut réessayer cette étape ultérieurement dans sa fenêtre de nouvelle tentative.

## Comment Braze évalue les messages {#how-braze-evaluates-messages}

{% alert tip %}
Vous n'avez pas besoin de comprendre tous les détails de cette section pour utiliser la Priorisation des messages. Une fois que vous avez défini vos catégories et vos règles et que vous avez activé vos messages, Braze évalue et priorise automatiquement les messages en faisant de son mieux pour envoyer ceux qui comptent le plus. Les informations ci-dessous sont destinées à ceux qui souhaitent comprendre comment ces décisions sont prises.
{% endalert %}

Lorsqu'un utilisateur est éligible à plusieurs messages priorisés, Braze évalue ensemble les Campaigns activées et les étapes de message Canvas éligibles sur les canaux pris en charge.

Pour les Campaigns, cela inclut les envois planifiés et les envois basés sur une action éligibles.

Pour les Canvas, cela inclut :

- Les Canvas planifiés futurs auxquels l'utilisateur est éligible pour entrer
- Les Canvas dans lesquels l'utilisateur se trouve actuellement

La priorisation de Canvas n'est pas un choix tout ou rien. Une Campaign de priorité supérieure peut entraîner la dépriorisation d'une étape de Canvas, tandis que les étapes éligibles suivantes dans ce même Canvas peuvent toujours être envoyées, en fonction du classement des catégories, du moment de l'envoi et des règles de limite de fréquence.

Braze compare les messages priorisés uniquement lorsqu'ils partagent la même règle de limite de fréquence applicable. Par exemple, deux Campaigns e-mail qui comptent pour la même règle de limite de fréquence d'e-mail peuvent être priorisées l'une par rapport à l'autre, mais une Campaign e-mail de priorité inférieure n'est pas dépriorisée en faveur d'un message SMS de priorité supérieure, sauf si les deux comptent pour la même règle. Les messages en dehors de la Priorisation des messages partagent également ces limites de fréquence, de sorte que même un message de haute priorité peut être annulé à cause d'un message en dehors de la Priorisation des messages.

Braze évalue les Campaigns et les Canvas différemment, car un Canvas peut se ramifier et se dérouler au fil du temps.

### Évaluer les Campaigns {#evaluating-campaigns}

Braze compare chaque message de Campaign éligible en utilisant l'heure à laquelle ce message est prévu d'être envoyé.

### Évaluer les Canvas {#evaluating-canvases}

Pour évaluer un Canvas, Braze effectue une **anticipation** : il parcourt le Canvas depuis un point de départ pour prédire quels messages futurs un utilisateur peut recevoir, et à quel moment. L'anticipation démarre à partir de :

- L'entrée dans le Canvas, pour les Canvas planifiés futurs
- L'étape actuelle de l'utilisateur, si l'utilisateur est déjà dans le Canvas

Lors de cette anticipation, Braze traite chaque type d'étape de Canvas différemment. Le type d'étape détermine si l'anticipation la comptabilise, la saute, s'arrête à celle-ci ou se divise en plusieurs parcours :

| Catégorie d'étape | Effet sur l'anticipation |
|---|---|
| Étapes de messagerie | Comptabilisées comme messages éligibles pour la priorisation |
| Étapes de continuation | Sautées ; l'anticipation les traverse |
| Étapes limites | L'anticipation s'arrête jusqu'à ce que l'utilisateur franchisse l'étape |
| Étapes de ramification | L'anticipation suit tous les parcours possibles |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Évaluation des Canvas" }

#### Étapes de messagerie {#messaging-steps}

Ces étapes sont comptabilisées pour la priorisation et ajoutées à l'ensemble des messages éligibles lorsqu'elles envoient sur un canal pris en charge.

- Étape Message
- Étape Content Optimizer

#### Étapes de continuation {#continuation-steps}

Ces étapes sont ignorées pour la priorisation et n'affectent pas l'anticipation.

- Étape Mise à jour du contexte
- Étape Mise à jour de l'utilisateur
- Étape Audience Sync
- Étape Feature Flag
- Étape Délai avec un délai fixe

#### Étapes limites {#boundary-steps}

Braze arrête l'anticipation à ces étapes jusqu'à ce que l'utilisateur progresse réellement à travers elles dans le Canvas.

- Étape Délai avec un délai personnalisé
- Étape Délai qui suit une étape de ramification
- Étape Parcours d'action
- Étape Expérience

#### Étapes de ramification {#branching-steps}

Ces étapes divisent le Canvas en plusieurs parcours possibles.

- Étape Arbre décisionnel
- Étape Parcours d'audience

Lorsqu'un chemin de priorisation contient des étapes de ramification, Braze considère que tous les parcours sont viables et prend en compte toutes les étapes de message parallèles sur les canaux pris en charge pour la priorisation. Comme les règles de limite de fréquence peuvent être spécifiques à un canal, les étapes de message parallèles sont dédupliquées par canal lorsque nécessaire.

Par exemple, si une branche peut envoyer un e-mail et qu'une autre branche peut également envoyer un e-mail, Braze les traite comme un seul envoi d'e-mail possible lors de l'anticipation. Si une autre branche peut envoyer une notification push, Braze considère également cet envoi push possible séparément.

Pour les étapes de message Canvas qui utilisent le timing intelligent, Braze utilise l'heure d'envoi calculée de chaque utilisateur une fois que celui-ci atteint l'étape. Pour plus de détails, consultez [Timing intelligent](#intelligent-timing).

Les étapes Content Optimizer sont traitées comme des étapes de messagerie car elles envoient toujours sur un canal spécifié. Cependant, les fenêtres de réessai ne s'appliquent pas aux étapes Content Optimizer, car un réessai interférerait avec l'expérience. Les autres étapes de messagerie Canvas prises en charge peuvent utiliser des fenêtres de réessai. Les étapes Canvas sur des canaux non pris en charge ne participent pas à la Priorisation des messages.

## Exemples {#examples}

### Campaign de priorité supérieure versus Campaign de priorité inférieure {#higher-priority-campaign-versus-lower-priority-campaign}

Supposons qu'un utilisateur soit éligible à deux Campaigns par e-mail le même jour, et que les deux Campaigns soient soumises à la même règle de limite de fréquence. Si la Campaign de priorité supérieure est prévue pour un envoi plus tard dans la journée, Braze peut déprioriser la Campaign de priorité inférieure afin que la Campaign de priorité supérieure puisse être envoyée à la place. Si la Campaign de priorité inférieure dispose d'une fenêtre de renvoi, Braze peut réessayer plus tard.

### Campaign basée sur une action de priorité supérieure versus message de priorité inférieure {#higher-priority-action-based-campaign-versus-lower-priority-message}

Supposons qu'un utilisateur déclenche une Campaign basée sur une action de priorité supérieure, configurée pour un envoi deux heures plus tard. Pendant ce délai, Braze peut prendre en compte cette Campaign basée sur une action à venir lorsqu'il détermine si un autre message priorisé doit être envoyé en premier. Cela permet d'éviter qu'un message de priorité inférieure ne soit envoyé immédiatement si la Campaign basée sur une action de priorité supérieure est prévue pour un envoi prochain.

### Canvas de priorité supérieure versus Campaign de priorité inférieure {#higher-priority-canvas-versus-lower-priority-campaign}

Supposons qu'un utilisateur soit éligible pour une Campaign de priorité inférieure, mais qu'il soit également prévu qu'il reçoive un message Canvas de priorité supérieure plus tard dans la journée. Si Braze peut déjà évaluer ce futur message Canvas, il peut déprioriser la Campaign de priorité inférieure afin que le message Canvas de priorité supérieure puisse être envoyé à la place.

### Canvas de priorité supérieure avec une étape de limite versus Campaign de priorité inférieure {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Supposons qu'un Canvas de priorité supérieure inclue une étape de parcours d'action, une expérience ou un délai personnalisé avant sa prochaine étape de message. Tant que l'utilisateur n'a pas atteint et dépassé cette étape, Braze n'anticipe pas le message Canvas de priorité supérieure en aval. Dans ce cas, une Campaign de priorité inférieure peut tout de même être envoyée en premier.

### Canvas de priorité supérieure avec embranchements versus message de priorité inférieure {#higher-priority-branching-canvas-versus-lower-priority-message}

Supposons qu'un Canvas de priorité supérieure puisse envoyer différents messages selon la branche suivie par l'utilisateur. Braze évalue ces futurs parcours possibles de manière conservatrice lors de la comparaison des messages. Cela permet d'éviter qu'un message de priorité inférieure ne soit envoyé immédiatement si une branche Canvas de priorité supérieure pourrait utiliser cette même limite de fréquence plus tard.

### Étape Canvas avec timing intelligent et étapes en aval {#canvas-step-with-intelligent-timing-and-downstream-steps}

Supposons qu'un utilisateur entre dans une étape de message Canvas de priorité supérieure qui utilise le timing intelligent. Une fois que Braze a calculé l'heure d'envoi de l'utilisateur pour l'étape avec timing intelligent, la priorisation des messages utilise cette heure d'envoi par utilisateur pour l'étape en cours et pour les étapes de message ultérieures sur le même parcours déterministe. Cela permet à Braze de comparer les messages Canvas en aval avec d'autres envois priorisés en utilisant le calendrier mis à jour plutôt que l'estimation de parcours antérieure uniquement.

## Limitations

La priorisation des messages présente les limites de fonctionnalité suivantes. Les limites spécifiques dépendent de votre édition de la plateforme Braze ; contactez votre gestionnaire de compte Braze pour plus de détails.

- Une limite sur le nombre de Campaigns et de Canvas planifiés actifs et activés (combinés)
- Une limite sur le nombre de Campaigns et de Canvas déclenchés par une action actifs et activés (combinés)
- Une limite sur le nombre de décisions de priorisation par mois
- Une limite sur le nombre de catégories par espace de travail
- Une limite sur le nombre de règles de priorisation par espace de travail
- Une durée maximale de la fenêtre de nouvelle tentative

## Questions fréquentes {#frequently-asked-questions}

### Comment les égalités de priorité sont-elles résolues entre les messages d'une même catégorie ? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

Lorsque deux Campaigns de la même catégorie sont comparées, Braze accorde la priorité la plus élevée à celle dont l'heure d'envoi est la plus précoce. Si une fenêtre de nouvelle tentative est configurée, Braze utilise la fin de cette fenêtre lors de la comparaison des Campaigns au sein de la même règle de priorité. Pour les Campaigns récurrentes, l'heure d'envoi est calculée comme la prochaine occurrence à partir de minuit, heure de l'entreprise. Pour les Campaigns planifiées en heure locale, Braze suppose une heure d'envoi correspondant à l'heure de l'entreprise.

Pour les Canvas de la même catégorie, Braze utilise le moment d'entrée dans le Canvas comme critère de départage, afin que toutes les étapes d'un même Canvas conservent la même priorité relative par rapport aux autres Campaigns et Canvas.

### Comment puis-je m'assurer qu'un message est toujours envoyé ? {#how-can-i-make-sure-a-message-is-always-sent}

Il peut y avoir des scénarios dans lesquels vous souhaitez qu'un message soit toujours envoyé, comme dans le cas de notifications transactionnelles ou juridiques. Dans ce cas, vous devez exclure le message de la limite de fréquence, ce qui le rend également inéligible à la priorisation des messages. Cela envoie le message chaque fois qu'il est planifié ou déclenché, sans tenir compte des autres envois en cours.

### Quand les messages sont-ils réellement priorisés ? Y a-t-il un calendrier ? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Chaque message est priorisé en fonction de son heure d'envoi prévue. Il n'y a pas de moment d'évaluation universel pour les messages priorisés.

### Comment Braze prédit-il l'heure d'envoi d'un futur message ? {#how-does-braze-predict-when-a-future-message-sends}

Braze prédit le moment d'envoi futur différemment selon le type de message :

- **Campaigns planifiées :** Braze utilise l'heure d'envoi prévue de chaque Campaign. Pour les Campaigns planifiées qui utilisent le timing intelligent, Braze utilise l'heure d'envoi optimale de chaque utilisateur pour cette occurrence de Campaign.
- **Campaigns basées sur une action :** Braze utilise l'heure d'envoi prévue de chaque message déclenché, y compris tout délai configuré entre le déclenchement et l'envoi.
- **Étapes de Canvas :** Braze utilise l'entrée de l'utilisateur dans le Canvas ou sa position actuelle dans le Canvas, ainsi que le timing des étapes en aval. Pour les étapes de message Canvas qui utilisent le timing intelligent, une fois qu'un utilisateur entre dans cette étape, Braze utilise l'heure d'envoi calculée par utilisateur. Pour les étapes de message suivantes sur le même parcours déterministe, Braze utilise cette heure d'envoi du timing intelligent pour déterminer l'heure d'envoi prévue ultérieure. Avant qu'un utilisateur n'atteigne l'étape avec le timing intelligent, la prédiction reste approximative.

### Mon message était planifié pour être envoyé, mais il ne l'a pas encore été en raison d'une limitation du débit ou d'autres retards. Qu'est-ce que cela signifie pour la priorisation des autres Campaigns ? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Braze suppose que votre message a été envoyé à l'heure initialement prévue s'il est toujours en cours de traitement, ce qui détermine s'il faut envoyer d'autres messages priorisés à venir. Lorsque ce message est finalement envoyé, Braze utilise l'heure d'envoi réelle.

### Mon message a été priorisé mais annulé au dernier moment. Qu'est-ce que cela signifie pour la priorisation ? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Lorsqu'un message est priorisé, Braze suppose qu'il a été envoyé à l'heure initialement prévue. De manière générale pour la priorisation des messages, nous ne recommandons pas d'utiliser les interruptions Liquid. Si un message est interrompu en raison de la [logique Liquid `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), nous supposons qu'il a été envoyé à cet utilisateur et priorisons les futures Campaigns en conséquence.

Imaginons que vous ayez deux messages : Message 1 et Message 2. Si le Message 1 est interrompu au profit d'un futur Message 2 de priorité plus élevée, cela ne garantit pas que le Message 2 sera effectivement envoyé. Le Message 2 peut toujours être interrompu pour diverses raisons, notamment :

- Les interruptions Liquid
- L'utilisateur ne fait plus partie du Segment
- Les limites de fréquence en raison d'un message en dehors des règles de priorisation.

Si le Message 2 est interrompu, il n'y a pas de nouvelle tentative d'envoi du Message 1.

Notez qu'un utilisateur pourrait recevoir un message de priorité inférieure, mais pas un message de priorité supérieure pour la même règle de limite de fréquence, pour les raisons suivantes :

- Le message de priorité supérieure a été limité en fréquence par une règle différente.
- Le message de priorité supérieure était en conflit avec une autre future Campaign de priorité encore plus élevée pour une règle différente.
- Au moment de l'envoi du message de priorité inférieure, l'utilisateur ne faisait pas partie de l'audience du message de priorité supérieure.
- Les deux messages auraient dû pouvoir être envoyés, mais un message en dehors de la configuration de priorisation a été envoyé avant que le message de priorité supérieure ne puisse l'être.

### Comment le timing intelligent fonctionne-t-il avec la priorisation des messages ? {#how-does-intelligent-timing-work-with-message-prioritization}

Pour les Campaigns, la priorisation des messages utilise l'heure d'envoi optimale de chaque utilisateur pour l'occurrence en cours. Pour les étapes de message Canvas, Braze utilise l'heure d'envoi calculée de chaque utilisateur une fois que celui-ci atteint l'étape, et reflète ce timing dans les étapes de message suivantes sur le même parcours déterministe. Pour plus de détails, consultez [Timing intelligent](#intelligent-timing).

### Existe-t-il des fonctionnalités de reporting ou d'analyse spécifiques à la priorisation des messages ? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze fournit des événements liés à la priorisation des messages dans Currents et le partage de données pour les canaux pris en charge, notamment les e-mails, LINE, les notifications push, les SMS, les webhooks et WhatsApp. Cela inclut les événements de dépriorisation et de limite de fréquence, enregistrés comme l'événement `users.messages.<channel>.Abort`, ainsi que les événements de nouvelle tentative qui indiquent quand un message a été réessayé ultérieurement dans la fenêtre de nouvelle tentative configurée, enregistrés comme l'événement `users.messages.<channel>.Retry`.

Vous pouvez également utiliser le tableau de bord de diagnostic de messagerie, les statistiques quotidiennes existantes de dépriorisation et de nouvelle tentative, ainsi que les [fonctionnalités de reporting de Braze]({{site.baseurl}}/user_guide/analytics/reports) pour surveiller la santé et les performances de vos Campaigns et Canvas priorisés.