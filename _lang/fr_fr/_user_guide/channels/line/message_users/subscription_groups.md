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

> Il existe deux états d'abonnement pour les utilisateurs LINE : abonné et désabonné. Chaque groupe d'abonnement est connecté à son propre canal LINE. Pour un aperçu cross-canal des groupes d'abonnement, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

| État | Définition |
| --- | --- |
| Abonné | L'utilisateur a suivi le canal LINE depuis son application LINE. Les utilisateurs sont automatiquement abonnés lorsqu'ils suivent le canal après que vous avez terminé les étapes d'intégration. |
| Désabonné | L'utilisateur n'a pas suivi le canal LINE depuis son application LINE, ou l'utilisateur a explicitement cessé de suivre le canal LINE. <br><br> Les utilisateurs qui se désabonnent d'un groupe d'abonnement LINE ne recevront plus aucun message LINE provenant des canaux d'envoi appartenant à ce groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Groupes d'abonnement LINE" }

## Définir le groupe d'abonnement LINE d'un utilisateur {#set-a-users-line-subscription-group}

LINE héberge le statut d'abonnement des utilisateurs. Braze traite les événements de suivi et de désabonnement qui mettent à jour le statut d'abonnement.

{% alert important %}
Les groupes d'abonnement LINE ne peuvent pas être déplacés entre les espaces de travail. Si vous réintégrez un canal LINE dans un autre espace de travail après avoir archivé son groupe d'abonnement, Braze crée un nouveau groupe d'abonnement dans l'espace de travail cible — l'original reste dans le premier espace de travail.
{% endalert %}

## Comportement de l'archivage {#archive-behavior}

- **Archivage standard :** Si vous archivez un groupe d'abonnement LINE sans réintégrer le canal dans un autre espace de travail, vous pouvez désarchiver le groupe d'abonnement ultérieurement.
- **Archivage permanent :** Si vous réintégrez le canal LINE dans un espace de travail différent après avoir archivé son groupe d'abonnement, le groupe d'abonnement d'origine est archivé de manière permanente et ne peut pas être désarchivé via le tableau de bord.

Pour les étapes de réintégration du canal, consultez [Configuration de LINE]({{site.baseurl}}/user_guide/channels/line/line_setup#re-integrate-a-line-channel-in-another-workspace).