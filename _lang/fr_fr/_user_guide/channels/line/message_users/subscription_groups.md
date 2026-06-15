---
nav_title: Groupes d'abonnement
article_title: Groupes d'abonnement
page_order: 1
description: "Cet article traite des groupes d'abonnement aux messages LINE."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# Groupes d'abonnement LINE {#line-subscription-groups}

> Il existe deux états d'abonnement pour les utilisateurs LINE : abonné et désabonné. LINE peut avoir jusqu'à 100 groupes d'abonnement par espace de travail, chaque groupe d'abonnement étant connecté à son propre canal LINE.

| État | Définition |
| --- | --- |
| Abonné | L'utilisateur a suivi le canal LINE depuis son application LINE. Les utilisateurs sont automatiquement abonnés lorsqu'ils suivent le canal après que vous avez terminé les étapes d'intégration. |
| Désabonné | L'utilisateur n'a pas suivi le canal LINE depuis son application LINE, ou l'utilisateur a explicitement cessé de suivre le canal LINE. <br><br> Les utilisateurs qui se désabonnent d'un groupe d'abonnement LINE ne recevront plus aucun message LINE provenant des canaux d'envoi appartenant à ce groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE subscription groups" }

## Définir le groupe d'abonnement LINE d'un utilisateur {#setting-a-users-line-subscription-group}

LINE héberge le statut d'abonnement des utilisateurs. Braze traite les événements de suivi et de désabonnement qui mettent à jour le statut d'abonnement.