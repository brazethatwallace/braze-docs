---
nav_title: "Campaigns et Canvas inactifs"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Campaigns et Canvas inactifs {#idle-campaigns-and-canvases}

> Cet article de référence explique le statut inactif des Campaigns et des Canvas et répond aux questions fréquemment posées.

{% alert note %}
En 2024, les Canvas seront marqués comme **Inactifs** et arrêtés, de manière similaire aux Campaigns. Lorsque les Canvas sont inactifs ou arrêtés, ils suivront la logique décrite dans ce document.
{% endalert %}

Les Campaigns et les Canvas se voient attribuer un statut inactif lorsqu'ils n'ont pas envoyé de messages ou n'ont pas admis d'utilisateurs depuis un certain temps. Ces Campaigns et Canvas seront automatiquement arrêtés à leurs dates d'arrêt associées. Vous pouvez filtrer les Campaigns et Canvas inactifs pour vous aider à trier et gérer votre liste de Campaigns et de Canvas.

Les Campaigns et Canvas avec des dates de fin et des envois uniques sont inactifs pendant 7 jours avant l'arrêt automatique. Les Campaigns et Canvas qui n'ont pas envoyé de message depuis 11 mois sont inactifs pendant 1 mois avant l'arrêt automatique.

## Campaigns inactives {#idle-campaigns}

De manière continue, les Campaigns inactives répondant aux critères suivants seront arrêtées :

- Un envoi unique planifié dont la date d'envoi est dépassée de sept jours
- Une Campaign planifiée ou basée sur une action dont la date de fin est dépassée de sept jours
- Une Campaign sans date de fin qui n'a pas envoyé de messages depuis un an

Pour les Campaigns sans date de fin, si un message est envoyé ou si la Campaign est mise à jour, le compte à rebours d'un an pour l'arrêt de la Campaign sera réinitialisé. Lorsque les Campaigns sont arrêtées, Braze en informera les clients dans leur tableau de bord et par e-mail.

Les Campaigns seront arrêtées à la date la plus tardive entre la date d'arrêt par défaut et un jour après leur dernière échéance de conversion. Les envois résultant d'une variante gagnante ou personnalisée sont traités comme des envois planifiés et seront arrêtés sept jours après l'envoi de la variante gagnante ou personnalisée. Toutes les Campaigns seront arrêtées à 4 h UTC chaque jour pour tous les utilisateurs de Braze.

Les Content Cards ne seront pas arrêtées avant leur date d'expiration et respecteront également les critères mentionnés ci-dessus ainsi que la règle relative à l'échéance de conversion.

Consultez ce tableau pour savoir comment maintenir une Campaign inactive en activité :

| Raison du statut inactif                                                                              | Étapes pour rendre la Campaign active                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campaigns qui sont des envois uniques planifiés et dont la date d'envoi est dépassée                 | Planifier un envoi futur                            |
| Campaigns planifiées ou basées sur une action, avec des dates de fin, et dont la date de fin est dépassée | Prolonger la date de fin                               |
| Campaigns sans date de fin qui n'ont pas envoyé de messages depuis un an                                | Envoyer un message ou apporter une modification à la Campaign |
| Campaigns avec des dates de fin et des envois uniques | Planifier un envoi futur |
| Campaigns qui n'ont pas envoyé de message depuis 11 mois | Envoyer un message ou apporter une modification à la Campaign |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Campaigns de messages in-app {#in-app-message-campaigns}

Si une Campaign de messages in-app n'a aucune impression et n'a pas été modifiée depuis plus de 30 jours, elle devient une Campaign inactive. Une Campaign de messages in-app inactive continue de diffuser selon sa configuration, mais le message in-app devient un message in-app modélisé.

Si vos utilisateurs déclenchent un événement d'impression ou si le marketeur modifie la Campaign, celle-ci retrouve le statut actif et le compteur de 30 jours est réinitialisé.

## Canvas inactifs {#idle-canvases}

De manière continue, les Canvas inactifs répondant aux critères suivants seront arrêtés :

- Un envoi unique planifié dont la date d'envoi et la durée maximale sont dépassées de plus de 7 jours
- Un Canvas planifié ou basé sur une action dont la date de fin et la durée maximale sont dépassées de plus de 7 jours
- Un Canvas sans date de fin qui n'a pas admis d'utilisateurs ou n'a pas été modifié depuis plus de 12 mois et dont la durée maximale est écoulée

Pour les Canvas sans date de fin, si un utilisateur est admis ou si le Canvas est mis à jour, le compte à rebours d'un an pour l'arrêt du Canvas sera réinitialisé. Lorsque les Canvas sont arrêtés, Braze en informera les clients dans leur tableau de bord et par e-mail.

La [durée maximale]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) d'un Canvas est la durée la plus longue possible qu'un utilisateur peut mettre pour terminer un Canvas donné. Cette durée inclut les expirations des Content Cards et des messages in-app.

Consultez ce tableau pour savoir comment maintenir un Canvas inactif en activité :

| Raison du statut inactif                                                                                                  | Étapes pour rendre le Canvas actif                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Canvas qui sont des envois uniques planifiés et dont la durée maximale dépasse la date d'envoi                 | Planifier un envoi futur                          |
| Canvas planifiés ou basés sur une action, avec des dates de fin, et dont la durée maximale dépasse la date de fin | Prolonger la date de fin                             |
| Canvas sans date de fin qui n'ont pas envoyé de messages depuis un an                                                      | Envoyer un message ou apporter une modification au Canvas |
| Canvas avec des dates de fin et des envois uniques | Planifier un envoi futur |
| Canvas qui n'ont pas envoyé de message depuis 11 mois | Envoyer un message ou apporter une modification au Canvas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

S'il n'y a pas d'option pour restaurer les données d'interaction, cela peut être dû au fait que :

- La restauration ou une autre opération liée aux données d'interaction est actuellement en cours.
- Aucune donnée d'interaction n'existait pour ce Canvas.
- Si le Canvas a été créé avant 2021, les données peuvent avoir été définitivement supprimées conformément à l'ancienne politique.

## Questions fréquemment posées {#frequently-asked-questions}

### À quelles Campaigns ou quels Canvas cela s'applique-t-il ? {#what-campaigns-or-canvases-does-this-apply-to}

Cela s'appliquera aux Campaigns et Canvas qui répondent déjà aux critères précédemment listés, ainsi qu'aux Campaigns et Canvas qui répondront à ces critères à l'avenir.

### Comment savoir si une Campaign ou un Canvas est inactif ? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Les Campaigns et Canvas inactifs seront affichés dans les pages de liste des Campaigns et Canvas sous la catégorie **Idle**. La date à laquelle la Campaign ou le Canvas sera arrêté est indiquée sous forme de colonne dans la liste.

![Le filtre « Idle » sur la page « Campaigns ».][1]{: style="max-width:60%;"}

### Que se passe-t-il si une Campaign ou un Canvas inactif est mis à jour ? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Si une Campaign qui n'a pas envoyé de message ou un Canvas qui n'a pas admis d'utilisateurs est mis à jour, le compte à rebours sera réinitialisé.

### Que se passe-t-il pour les Campaigns qui n'ont pas envoyé de message depuis un an (ou les Canvas qui n'ont pas admis d'utilisateurs depuis un an), mais qui ont une date de fin dans le futur ? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Nous arrêterons ces Campaigns et Canvas sept jours après la date de fin à 4 h UTC.

#### Puis-je empêcher les Campaigns d'être automatiquement arrêtées ? {#can-i-stop-campaigns-from-automatically-stopping}

Non. Cela permet de ne garder actives que les Campaigns nécessaires afin de réduire l'encombrement des tableaux de bord et d'améliorer les performances. Si vous souhaitez obtenir une liste de toutes les Campaigns arrêtées automatiquement, [soumettez un ticket d'assistance]({{site.baseurl}}/help/support/) pour en recevoir une.

### Qui recevra les notifications par e-mail concernant les Campaigns et Canvas arrêtés ? {#who-will-receive-email-notifications-about-stopped-campaigns-and-canvases}

Par défaut, tous les utilisateurs disposant d'autorisations d'administrateur sont inscrits aux notifications par e-mail concernant l'arrêt automatique des Campaigns et des Canvas. Le créateur de la Campaign ou du Canvas sera toujours notifié lorsque celle-ci ou celui-ci est arrêté. Les utilisateurs peuvent gérer leurs préférences de notification par e-mail en accédant à **Paramètres de l'entreprise** > **Préférences de notification**, puis en ajoutant ou en supprimant des destinataires de la notification **Campaign Automatically Stopped** et de la notification **Canvas Automatically Stopped**.

### Comment fonctionne l'arrêt des Content Cards ? {#how-does-stopping-content-cards-work}

Les Content Cards dans les Campaigns ne seront pas arrêtées avant leur date d'expiration et la période tampon appropriée. Elles seront arrêtées à la date la plus tardive entre la période tampon (correspondant au fait que la Campaign soit un envoi unique, ait une date de fin ou n'ait pas de date de fin) et la date d'expiration.

Par exemple, si une Content Card expire le 1er avril, est un envoi unique et a une échéance de conversion de 10 jours, elle sera arrêtée le 12 avril (10 jours après l'échéance de conversion, plus un jour). Si une Content Card expire le 1er avril, est déclenchée par API et n'a pas envoyé de messages depuis le 15 mars, elle expirera le 15 mars de l'année suivante.

Les Canvas ne sont arrêtés qu'après l'arrêt des Content Cards, ce qui signifie que leur durée maximale est écoulée.

### J'ai une expérience d'indicateur de fonctionnalité dans mon Canvas. Après la configuration de mon indicateur de fonctionnalité, le Canvas restera-t-il actif ? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-will-the-canvas-remain-active}

Les Canvas comportant des étapes d'indicateur de fonctionnalité ne sont pas automatiquement arrêtés et ne deviennent pas inactifs.

### Pourquoi est-ce que je vois des Campaigns inactives affichées dans ma liste de Campaigns alors que j'ai appliqué un filtre pour n'afficher que les Campaigns actives ? {#why-am-i-seeing-idle-campaigns-displayed-in-my-campaigns-list-when-i-applied-a-filter-to-show-active-campaigns-only}

Les Campaigns inactives sont considérées comme actives jusqu'à ce qu'elles soient arrêtées.

### Une Campaign serait-elle listée comme inactive alors qu'elle envoie encore des notifications push ? {#would-a-campaign-be-listed-as-idle-when-its-still-sending-push-notifications}

Non. Une Campaign sera listée comme inactive lorsqu'elle n'envoie plus activement de messages.

[1]: {% image_buster /assets/unlisted_docs/img/idle_filter.png %}