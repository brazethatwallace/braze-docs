---
nav_title: Règles d'envoi de messages
article_title: Règles d'envoi de messages
page_order: 1
page_type: reference
description: "Cette page explique comment utiliser les règles d'envoi de messages dans le flux de travail d'approbation pour les Campaigns et les Canvas avec un volume d'envoi important."
---

# Règles d'envoi de messages {#messaging-rules}

> Utilisez les règles d'envoi de messages dans votre flux de travail d'approbation pour limiter le nombre d'utilisateurs pouvant être atteints avant qu'une approbation supplémentaire ne soit requise — de cette façon, vous pouvez vérifier vos Campaigns et Canvas avant de cibler une audience plus large.

## Conditions préalables {#prerequisites}

Seuls les administrateurs Braze peuvent définir des règles d'envoi de messages, mais tout utilisateur Braze peut être un approbateur de règle d'envoi de messages (y compris les utilisateurs sans autorisations d'approbation générales).

## Fonctionnement {#how-it-works}

Les règles d'envoi de messages s'appliquent à un espace de travail et sont composées d'un type de message et d'un nombre maximum d'utilisateurs pouvant être atteints.

- **Type de message :** définit le type de message auquel la règle s'applique : Campaign, Canvas, ou à la fois Canvas et Campaigns.
- **Nombre maximum d'utilisateurs pouvant être atteints :** détermine la taille d'audience nécessitant une approbation supplémentaire.

### Approbateurs distincts {#separate-approvers}

Deux règles peuvent partager le même maximum d'utilisateurs afin que vous puissiez organiser et séparer vos règles par approbateurs. Par exemple, vous créez les deux règles suivantes :

- Règle A pour Canvas avec un maximum de 100 000 utilisateurs avec des approbateurs de votre équipe juridique
- Règle B pour Canvas avec un maximum de 100 000 utilisateurs avec des approbateurs de votre équipe marketing

### Pas de chevauchement d'utilisateurs pouvant être atteints {#no-overlapping-reachable-users}

Pour éviter toute confusion, vous ne pouvez pas définir des règles identiques avec un nombre d'utilisateurs qui se chevauche pour le même type de message et les mêmes approbateurs. Par exemple, la règle d'envoi de messages suivante **ne peut pas** être définie :

- Règle C pour Canvas avec un maximum de 10 000 utilisateurs
- Règle D pour Canvas avec un maximum de 1 000 000 d'utilisateurs

## Créer une règle d'envoi de messages {#creating-a-messaging-rule}

### Étape 1 : Ajouter une règle {#step-1-add-a-rule}

{% alert note %}
Vous pouvez créer jusqu'à cinq règles d'envoi de messages.
{% endalert %}

1. Accédez à **Paramètres** > **Flux de travail d'approbation** > **Règles d'envoi de messages**.
2. Sélectionnez **Créer une règle**.
3. Donnez un nom à cette règle (par exemple, « Tous les abonnements utilisateurs »).
4. Pour **Type de message**, sélectionnez **Campaign**, **Canvas** ou **Les deux : Canvas et Campaigns** pour appliquer la règle d'approbation.
5. Saisissez un nombre pour **Nombre maximum d'utilisateurs pouvant être atteints**. Pour plus d'informations, consultez [Statistiques d'audience]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users#audience-statistics).
6. Sélectionnez **Enregistrer**.

![Un exemple de règle d'envoi de messages « Règle 1 » pour les Campaigns avec 100 000 utilisateurs comme maximum. Un utilisateur peut approuver le Canvas et la Campaign pour le lancement.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Étape 2 : Déterminer le lancement avec approbation (facultatif) {#step-2-determine-launching-with-approval-optional}

Sélectionnez **Autoriser le lancement avec approbation**. Ensuite, pour **Avec l'approbation de**, sélectionnez les approbateurs qui ont l'autorisation d'approuver le Canvas ou la Campaign si le maximum est atteint.

Notez les détails suivants concernant le lancement de messages avec approbation :

- Si le maximum est atteint et qu'un approbateur est sélectionné, l'utilisateur Braze disposant de l'autorisation d'approbation peut sélectionner **Approuvé** dans le menu déroulant d'approbation **Audience cible**.
- Si le maximum est atteint et qu'aucun approbateur n'est sélectionné, le Canvas ou la Campaign ne peut pas être lancé(e).

![L'étape « Résumé » du flux de travail Canvas qui montre qu'une approbation est nécessaire pour le lancement.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Questions fréquemment posées {#frequently-asked-questions}

### Dois-je reconfigurer mes autorisations pour utiliser les règles d'envoi de messages ? {#do-i-have-to-reconfigure-my-permissions-to-use-messaging-rules}

Non. Tout utilisateur, quelles que soient ses autorisations actuelles, peut être sélectionné comme approbateur de population cible.

### Quel est le lien entre les règles d'envoi de messages et l'étape Audience cible ? {#how-do-messaging-rules-relate-to-the-target-audience-step}

Les règles d'envoi de messages ne prennent pas en compte des détails tels que les événements déclencheurs. Par exemple, une Campaign peut cibler tous vos utilisateurs. Cependant, la Campaign est déclenchée par un événement, de sorte que le nombre réel d'utilisateurs qui la reçoivent est inférieur.

### Y aura-t-il des changements automatiques lorsque les règles d'envoi de messages seront activées ? {#will-anything-automatically-change-when-messaging-rules-are-turned-on}

Non. Une fois cette fonctionnalité activée, vous devez saisir manuellement le nombre maximum d'utilisateurs et sélectionner des approbateurs pour utiliser la fonctionnalité.