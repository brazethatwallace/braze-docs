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

Si vous choisissez d'envoyer un message dès son lancement, l'envoi commencera dès que vous aurez terminé la création de votre campagne.

![La section « Réception » avec « Planification » sélectionnée et l'option de planification basée sur le temps pour envoyer dès le lancement de la campagne.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Ce type de planification est conçu pour les campagnes ponctuelles que vous souhaitez envoyer immédiatement, comme des messages relatifs à un événement en cours. Une application sportive, par exemple, peut planifier des notifications push sur les mises à jour de scores en utilisant cette option. De plus, lorsque vous envoyez des messages de test destinés uniquement à vous-même ou à votre équipe, cette option vous permet de les distribuer immédiatement.

Si vous prévoyez de modifier la campagne et de la renvoyer après avoir consulté le test, veillez à cocher la case qui rend les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) pour recevoir la campagne. Par défaut, Braze n'envoie une campagne à un utilisateur qu'une seule fois, sauf si cette case est cochée.

## Option 2 : Envoyer à un horaire défini {#option-2-send-at-a-designated-time}

Planifier une campagne pour un horaire défini vous permet de spécifier les jours et les heures d'envoi de votre campagne. Vous pouvez envoyer un message une seule fois, quotidiennement, hebdomadairement ou mensuellement à une heure précise, et également définir quand votre campagne doit commencer et se terminer. Cette date de fin est inclusive, ce qui signifie que le dernier envoi a lieu à la date de fin.

Si vous sélectionnez une planification mensuelle récurrente, notez que certains mois peuvent ne pas comporter le jour sélectionné. Par exemple, supposons que vous configurez une campagne pour un envoi mensuel le 31. Dans ce cas, Braze effectue l'envoi le dernier jour du mois, comme le 30 avril, car le 31 avril n'existe pas.

Si vous sélectionnez **Réception planifiée** sans choisir l'envoi à l'heure locale de l'utilisateur, votre campagne sera envoyée selon le fuseau horaire spécifié sur votre page **Paramètres de l'entreprise**.

![Les options de planification basées sur le temps pour envoyer une campagne à un horaire défini.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campagnes en fuseau horaire local {#local-time-zone-campaigns}

Vous pouvez distribuer le message dans les fuseaux horaires locaux des utilisateurs afin que les membres de votre audience internationale ne reçoivent pas de notification à des heures inappropriées. Les campagnes en fuseau horaire local doivent être planifiées 24 heures à l'avance pour garantir que les utilisateurs éligibles de tous les fuseaux horaires puissent les recevoir. Consultez la [FAQ sur les Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) pour comprendre le fonctionnement des campagnes en fuseau horaire local et les règles de distribution associées.

Les segments ciblés par des campagnes en fuseau horaire local doivent inclure, au minimum, une fenêtre de 2 jours pour prendre en compte les utilisateurs de tous les fuseaux horaires. Par exemple, si votre campagne est planifiée pour un envoi en soirée mais ne dispose que d'une fenêtre d'1 jour, certains utilisateurs peuvent être sortis du segment au moment où leur fuseau horaire est atteint. Voici des exemples de filtres créant une fenêtre de 2 jours : « dernière utilisation il y a plus d'1 jour » et « dernière utilisation il y a moins de 3 jours », ou « premier achat il y a plus de 7 jours » et « premier achat il y a moins de 9 jours ».

### Cas d'utilisation {#use-cases}

Les planifications à horaire défini sont particulièrement adaptées aux messages planifiés à l'avance et aux campagnes récurrentes, comme l'onboarding et la rétention, qui s'exécutent régulièrement pour tous les utilisateurs qualifiés.

## Option 3 : Timing intelligent {#option-3-intelligent-timing}

Le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) vous permet de distribuer une campagne à chaque utilisateur à un moment différent. Braze calcule l'heure optimale de chaque individu en fonction du moment où cet utilisateur interagit habituellement avec votre application et ses notifications. Vous pouvez également spécifier que les campagnes à timing intelligent ne soient envoyées que pendant une certaine partie de la journée. Par exemple, si vous informez les utilisateurs d'une promotion qui se termine à minuit, vous pouvez souhaiter que vos messages soient envoyés au plus tard à 22 h.

![Les options de planification basées sur le temps pour utiliser le timing intelligent afin d'envoyer une campagne à l'heure la plus populaire d'utilisation de l'application parmi tous les utilisateurs.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Règles de distribution {#delivery-rules}

Étant donné que l'heure optimale d'un utilisateur peut se situer à n'importe quel moment sur une période de 24 heures, toutes les campagnes à timing intelligent doivent être planifiées 24 heures à l'avance. De plus, comme pour les campagnes à horaire défini, les messages avec une fenêtre d'1 jour manqueront les utilisateurs qui sortent du segment avant que leur heure optimale dans leur fuseau horaire ne soit atteinte. Les segments des campagnes à timing intelligent doivent intégrer au minimum une fenêtre de 3 jours pour en tenir compte.

Si le profil d'un utilisateur ne contient pas suffisamment de données pour calculer une heure optimale, vous pouvez choisir une méthode de secours : envoyer à l'heure la plus populaire d'utilisation de l'application parmi tous les utilisateurs, ou définir une heure de repli personnalisée.

### Cas d'utilisation

Les campagnes à timing intelligent sont idéales pour les messages ponctuels et récurrents où l'heure de distribution est flexible, c'est-à-dire lorsqu'il ne s'agit pas d'actualités de dernière minute ou d'annonces à horaire précis.

## Évaluation des critères d'audience avec des délais {#audience-criteria-evaluation-with-delays}

Pour les campagnes utilisant la réception planifiée, les critères d'audience sont toujours évalués au moment de l'envoi planifié, et non au moment du lancement de la campagne. Cela s'applique à tout délai entre la planification et l'envoi, par exemple la limite de débit, le fuseau horaire local, le timing intelligent ou une planification déclenchée.

## Résolution des problèmes {#troubleshooting}

### Pourquoi ma campagne e-mail planifiée n'a-t-elle pas atteint l'ensemble de l'audience estimée ? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

Les envois peuvent être inférieurs à l'audience estimée lorsque des utilisateurs n'ont pas d'adresse e-mail, ne sont pas abonnés aux e-mails ou sont exclus par les filtres de livrabilité au moment de l'envoi. Une modification récente de l'adresse e-mail d'un utilisateur peut également affecter l'éligibilité lorsque les critères d'audience sont réévalués au moment de l'envoi. Pour en savoir plus, consultez [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size).

### Pourquoi ma campagne a-t-elle été envoyée un jour avant l'horaire prévu ? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

Si une campagne est envoyée avant l'horaire que vous avez défini dans les **Paramètres de l'entreprise**, activez **Envoyer dans le fuseau horaire local** ou ajoutez une fenêtre de distribution pour les campagnes à timing intelligent. Sans ces paramètres, l'évaluation des fuseaux horaires peut mettre en file d'attente les envois pour les utilisateurs situés dans des fuseaux horaires antérieurs avant l'heure prévue. Pour en savoir plus, consultez [Campagnes en fuseau horaire local](#local-time-zone-campaigns) et [Quand Braze évalue-t-il les utilisateurs pour la distribution en fuseau horaire local ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery).