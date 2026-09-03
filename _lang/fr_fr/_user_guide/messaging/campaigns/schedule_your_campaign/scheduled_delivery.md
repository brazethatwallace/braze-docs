---
nav_title: Réception planifiée
article_title: Réception planifiée
page_order: 0
page_type: reference
description: "Cet article de référence décrit les différences entre les options de planification basées sur le temps pour la réception des campagnes."
tool: Campaigns
---

# Réception planifiée {#scheduled-delivery}

> Les campagnes envoyées à l'aide d'une réception planifiée basée sur le temps sont distribuées à des jours spécifiés.

## Option 1 : Envoyer dès le lancement de la campagne {#option-1-send-as-soon-as-the-campaign-is-launched}

Si vous choisissez d'envoyer un message dès son lancement, votre message commencera à être envoyé dès que vous aurez terminé la création de votre Campaign.

![La section « Réception » avec « Planifié » sélectionné et l'option de planification basée sur le temps pour envoyer dès le lancement de la campagne.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Ce type de planification est conçu pour les Campaigns ponctuelles que vous souhaitez envoyer immédiatement, comme des messages concernant un événement en cours. Une application sportive, par exemple, peut planifier des notifications push sur les mises à jour de scores en utilisant cette option. De plus, lorsque vous envoyez des messages de test destinés uniquement à vous-même ou à votre équipe, cette option vous permet de les distribuer immédiatement.

Si vous prévoyez de modifier la Campaign et de la renvoyer après avoir consulté le test, assurez-vous de cocher la case qui rend les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) pour recevoir la Campaign. Par défaut, Braze n'envoie une Campaign à un utilisateur qu'une seule fois, sauf si cette case est cochée.

## Option 2 : Envoyer à une heure désignée {#option-2-send-at-a-designated-time}

La planification d'une Campaign pour une heure désignée vous permet de spécifier les jours et les heures d'envoi de votre Campaign. Vous pouvez envoyer un message une seule fois, quotidiennement, hebdomadairement ou mensuellement à une certaine heure de la journée, et également spécifier quand votre Campaign doit commencer et se terminer. Cette date de fin est inclusive, ce qui signifie que le dernier envoi a lieu à la date de fin.

Si vous sélectionnez une planification récurrente mensuelle, notez que certains mois peuvent ne pas comporter le jour sélectionné. Par exemple, supposons que vous configurez une Campaign pour un envoi mensuel le 31e jour. Dans ce scénario, Braze envoie le dernier jour de ce mois, comme le 30 avril, car le 31 avril n'existe pas.

Si vous sélectionnez **Scheduled Delivery** et ne choisissez pas d'envoyer selon le fuseau horaire local de l'utilisateur, votre Campaign sera envoyée selon le fuseau horaire spécifié sur votre page **Company Settings**.

![Les options de planification basées sur le temps pour envoyer une Campaign à une heure désignée.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campaigns en fuseau horaire local {#local-time-zone-campaigns}

Vous pouvez distribuer le message dans les fuseaux horaires locaux des utilisateurs afin que les membres de votre audience internationale ne reçoivent pas de notification à des heures inopportunes. Les Campaigns en fuseau horaire local doivent être planifiées 24 heures à l'avance pour garantir que les utilisateurs éligibles de tous les fuseaux horaires puissent les recevoir. Consultez la [FAQ sur les Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) pour comprendre le fonctionnement des Campaigns en fuseau horaire local et les règles de distribution associées.

Les Segments ciblés par des Campaigns en fuseau horaire local doivent inclure, au minimum, une fenêtre de 2 jours pour prendre en compte les utilisateurs de tous les fuseaux horaires. Par exemple, si votre Campaign est planifiée pour un envoi en soirée mais ne dispose que d'une fenêtre d'un jour, certains utilisateurs peuvent être sortis du Segment lorsque leur fuseau horaire est atteint. Parmi les exemples de filtres créant une fenêtre de 2 jours, on trouve « dernière utilisation il y a plus d'un jour » et « dernière utilisation il y a moins de 3 jours », ou « premier achat il y a plus de 7 jours » et « premier achat il y a moins de 9 jours ».

### Cas d'usage {#use-cases}

Les planifications à heure désignée sont les mieux adaptées aux messages planifiés à l'avance et aux Campaigns récurrentes, telles que l'onboarding et la rétention, qui s'exécutent régulièrement pour tous les utilisateurs qualifiés.

## Option 3 : Timing intelligent {#option-3-intelligent-timing}

Le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) vous permet de distribuer une Campaign à chaque utilisateur à un moment différent. Braze calcule l'heure optimale de chaque individu en fonction du moment où cet utilisateur interagit habituellement avec votre application et ses notifications. Vous pouvez éventuellement spécifier que les Campaigns à timing intelligent n'envoient que pendant une certaine partie de la journée. Par exemple, si vous informez les utilisateurs d'une promotion qui se termine à minuit, vous pouvez souhaiter que vos messages soient envoyés au plus tard à 22 h.

![Les options de planification basées sur le temps pour utiliser le timing intelligent afin d'envoyer une Campaign au moment le plus populaire d'utilisation de l'application parmi tous les utilisateurs.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Règles de distribution {#delivery-rules}

Étant donné que l'heure optimale d'un utilisateur peut correspondre à n'importe quel moment sur une période de 24 heures dans tous les fuseaux horaires mondiaux, toutes les Campaigns à timing intelligent doivent être planifiées 48 heures à l'avance. Planifier 48 heures à l'avance permet de prendre en compte la distribution à tous les utilisateurs dans le monde, car une seule journée couvre environ 48 heures sur l'ensemble des fuseaux horaires. De plus, comme pour les Campaigns à heure désignée, les messages avec une fenêtre d'un jour manquent les utilisateurs qui sortent du Segment avant que leur heure optimale dans leur fuseau horaire ne soit atteinte. Les Segments pour les Campaigns à timing intelligent devraient intégrer au minimum une fenêtre de 3 jours pour tenir compte de cela.

Si le profil d'un utilisateur ne contient pas suffisamment de données pour calculer une heure optimale, vous pouvez choisir une méthode de secours pour envoyer soit au moment le plus populaire d'utilisation de l'application parmi tous les utilisateurs, soit à une heure de repli personnalisée définie.

### Cas d'usage

Les Campaigns à timing intelligent fonctionnent le mieux pour les messages ponctuels et récurrents où il existe une certaine flexibilité concernant l'heure de distribution, par exemple lorsqu'ils ne sont pas adaptés aux actualités de dernière minute ou aux annonces à horaire fixe.

## Évaluation des critères d'audience avec des délais {#audience-criteria-evaluation-with-delays}

Pour les Campaigns qui utilisent la distribution planifiée, les critères d'audience sont toujours évalués au moment de l'envoi planifié, et non au lancement de la campagne. Cela s'applique à tout délai entre la planification et l'envoi, par exemple la limitation du débit, le fuseau horaire local, le timing intelligent ou une planification déclenchée.

### Moment des modifications de Segment {#timing-of-segment-changes}

Si vous modifiez un Segment utilisé comme audience pour une Campaign planifiée, les modifications effectuées peu avant l'heure d'envoi planifiée sont généralement prises en compte lors de l'évaluation de l'audience. Le seuil exact varie, mais les modifications sont généralement incluses si leur traitement se termine avant que Braze ne constitue l'audience pour cet envoi.

Par exemple, si vous mettez à jour un Segment à 15 h 50 pour une Campaign planifiée à 16 h, Braze utilise les critères de Segment mis à jour lors de l'évaluation de l'audience, à condition que les modifications aient fini d'être traitées avant le début de l'exécution de la campagne.

#### Bonnes pratiques {#best-practices}

Pour laisser aux modifications de Segment le temps de finir leur traitement avant l'envoi de vos Campaigns planifiées :

- **Anticipez :** Effectuez les modifications de Segment bien avant l'heure d'envoi planifiée afin qu'elles aient le temps d'être traitées.
- **Testez d'abord :** Dans la mesure du possible, testez les modifications dans une Campaign plus petite avant de les appliquer à des Campaigns plus importantes et plus critiques.

Pour en savoir plus sur les options de distribution planifiée, consultez [Types de distribution et d'entrée]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#time-based-options).

## Résolution des problèmes {#troubleshooting}

### Pourquoi ma campagne d'e-mail planifiée n'a-t-elle pas atteint l'ensemble de l'audience estimée ? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

Les envois peuvent être inférieurs à l'audience estimée lorsque des utilisateurs ne disposent pas d'adresse e-mail, ne sont pas abonnés aux e-mails ou sont exclus par les filtres de livrabilité au moment de l'envoi. Un changement récent de l'adresse e-mail d'un utilisateur peut également affecter l'éligibilité lorsque les critères d'audience sont réévalués à l'envoi. Pour en savoir plus, consultez [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size).

### Pourquoi ma campagne a-t-elle été envoyée un jour avant l'heure planifiée ? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

Si une campagne est envoyée plus tôt que la planification définie dans **Paramètres de l'entreprise**, activez **Envoyer dans le fuseau horaire local** ou ajoutez une fenêtre de distribution pour les Campaigns à timing intelligent. Sans ces paramètres, l'évaluation des fuseaux horaires peut mettre en file d'attente les envois pour les utilisateurs situés dans des fuseaux horaires plus avancés avant l'heure de planification prévue. Pour plus d'informations, consultez [Campaigns en fuseau horaire local](#local-time-zone-campaigns) et [Quand Braze évalue-t-il les utilisateurs pour la distribution en fuseau horaire local ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery).