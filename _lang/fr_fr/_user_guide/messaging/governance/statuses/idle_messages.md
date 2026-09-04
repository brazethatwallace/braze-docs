---
nav_title: Campaigns et Canvas inactifs
article_title: Campaigns et Canvas inactifs
page_order: 1
page_type: reference
alias: /idle_campaigns/
description: "Cet article de référence traite du statut inactif des Campaigns et des Canvas, y compris les critères d'arrêt automatique et les questions fréquemment posées."
toc_headers: h2
---

# Campaigns et Canvas inactifs {#idle-campaigns-and-canvases}

> Les Campaigns et les Canvas deviennent inactifs lorsqu'ils cessent d'envoyer des messages ou d'inscrire des utilisateurs pendant une période définie.

Braze arrête automatiquement les Campaigns et les Canvas inactifs à leurs dates d'arrêt associées. Ils restent actifs jusqu'à ce que Braze les arrête. Les envois ponctuels et les messages avec des dates de fin deviennent inactifs lorsque cette date est passée, puis s'arrêtent automatiquement après sept jours. Les messages sans date de fin deviennent inactifs après 11 mois sans activité et s'arrêtent automatiquement après un an.

## Campaigns inactives {#idle-campaigns}

Braze arrête les Campaigns inactives qui remplissent l'un de ces critères :

- Un envoi unique planifié a dépassé sa date d'envoi de sept jours
- Une Campaign planifiée ou déclenchée par une action dont la date de fin est dépassée de sept jours
- Une Campaign sans date de fin n'a pas envoyé de message, n'a pas inscrit d'utilisateur dans un groupe de contrôle et n'a pas été modifiée depuis un an

Pour les Campaigns sans date de fin, un envoi, une inscription dans un groupe de contrôle ou une modification réinitialise le compte à rebours d'un an. Lorsque Braze arrête des Campaigns, les utilisateurs de l'entreprise en sont informés dans le tableau de bord et par e-mail.

Braze arrête les Campaigns à la date la plus tardive entre la date d'arrêt par défaut et un jour après la dernière échéance de conversion. Les envois d'une variante gagnante ou personnalisée sont traités comme des envois planifiés, et Braze les arrête sept jours après l'envoi de cette variante. Les Campaigns s'arrêtent chaque jour à 4 h UTC.

Les Content Cards ne sont pas arrêtées avant leur date d'expiration, et elles respectent également les critères d'arrêt des Campaigns inactives ainsi que la règle d'échéance de conversion. Pour plus de détails, consultez [Comment fonctionne l'arrêt des Content Cards ?](#how-does-stopping-content-cards-work).

Utilisez ce tableau pour maintenir une Campaign inactive active. Le statut inactif et l'arrêt automatique utilisent des fenêtres différentes : une Campaign sans date de fin devient inactive après 11 mois sans activité, et Braze l'arrête automatiquement après un an.

| Raison du statut inactif | Étapes pour rendre la Campaign active |
|---|---|
| L'envoi unique planifié a dépassé la date d'envoi | Planifier un envoi futur |
| La Campaign planifiée ou déclenchée par une action a une date de fin dépassée | Prolonger la date de fin |
| La Campaign sans date de fin n'a pas envoyé de message, n'a pas inscrit d'utilisateur dans un groupe de contrôle et n'a pas été modifiée depuis 11 mois | Envoyer un message ou modifier la Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comment maintenir une Campaign inactive active" }

Les Campaigns de feature flags et les expériences de feature flags ne deviennent pas inactives et ne sont pas arrêtées automatiquement.

### Campaigns de messages in-app {#in-app-message-campaigns}

Les Campaigns de messages in-app déclenchées par une action deviennent inactives après 30 jours sans envoi, sans inscription dans un groupe de contrôle ou sans modification. Une Campaign de message in-app inactive continue à être diffusée selon sa configuration. Selon votre espace de travail, Braze peut la diffuser sous forme de [message in-app modélisé]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

Un envoi, une inscription dans un groupe de contrôle ou une modification remet la Campaign en statut actif et réinitialise la fenêtre de 30 jours. L'arrêt automatique suit toujours les règles de sept jours et d'un an décrites dans [Campaigns inactives](#idle-campaigns), et non la fenêtre d'inactivité de 30 jours.

## Canvas inactifs {#idle-canvases}

Braze arrête les Canvas inactifs qui répondent à l'un de ces critères :

- Un envoi unique planifié a dépassé sa date d'envoi et sa [durée maximale]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#maximum-duration) de plus de sept jours
- Un Canvas planifié ou basé sur une action avec une date de fin a dépassé sa date de fin et sa durée maximale de plus de sept jours
- Un Canvas sans date de fin n'a pas reçu d'utilisateurs et n'a pas été modifié depuis plus de 12 mois, auxquels s'ajoute sa durée maximale

Pour les Canvas sans date de fin, une entrée d'utilisateur ou une modification réinitialise le compte à rebours d'un an. Lorsque Braze arrête des Canvas, les utilisateurs de l'entreprise en sont informés dans le tableau de bord et par e-mail.

La durée maximale d'un Canvas correspond au temps le plus long qu'un utilisateur peut prendre pour terminer ce Canvas. Cette durée inclut les expirations des Content Cards et des messages in-app. Si votre Canvas contient des étapes soumises à une limitation du débit, Braze ajoute sept jours supplémentaires à la durée maximale pour tenir compte d'une éventuelle mise en file d'attente liée aux limites de débit.

Utilisez ce tableau pour maintenir un Canvas inactif en activité. Le statut d'inactivité et l'arrêt automatique utilisent des fenêtres différentes : un Canvas sans date de fin devient inactif après 11 mois plus sa durée maximale sans activité, et Braze l'arrête automatiquement après 12 mois plus sa durée maximale.

| Raison du statut inactif | Étapes pour rendre le Canvas actif |
|---|---|
| L'envoi unique planifié a dépassé la date d'envoi et la durée maximale | Planifier un envoi futur |
| Le Canvas planifié ou basé sur une action a une date de fin et une durée maximale qui sont dépassées | Prolonger la date de fin |
| Le Canvas sans date de fin n'a pas reçu d'utilisateurs et n'a pas été modifié depuis 11 mois plus sa durée maximale | Faire entrer un utilisateur ou modifier le Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comment maintenir un Canvas inactif en activité" }

Les Canvas comportant des étapes de feature flag ne deviennent pas inactifs et ne sont pas arrêtés automatiquement.

Pour les données d'interaction de messaging sur les Campaigns et Canvas arrêtés, consultez [À propos de la disponibilité des données d'interaction de messaging]({{site.baseurl}}/messaging_interaction_data).

## Questions fréquemment posées {#frequently-asked-questions}

### À quelles campagnes ou quels Canvas cela s'applique-t-il ? {#what-campaigns-or-canvases-does-this-apply-to}

Cela s'applique aux Campaigns et Canvas qui répondent déjà aux critères de cet article, ainsi qu'à ceux qui répondront à ces critères ultérieurement.

### Comment savoir si une Campaign ou un Canvas est inactif ? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Pour trouver les Campaigns et Canvas inactifs, accédez à la page **Campaigns** ou **Canvas** et filtrez par **Idle**. La date à laquelle Braze arrête la Campaign ou le Canvas est affichée sous forme de colonne dans la liste.

![Le filtre « Idle » sur la page Campaigns.]({% image_buster /assets/img/idle_filter.png %}){: style="max-width:80%;"}

### Que se passe-t-il si une Campaign ou un Canvas inactif est mis à jour ? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Si vous mettez à jour une Campaign qui n'a pas envoyé de message ou un Canvas qui n'a pas inscrit d'utilisateurs, le compte à rebours est réinitialisé.

### Que se passe-t-il pour les Campaigns qui n'ont pas envoyé de message depuis un an (ou les Canvas qui n'ont pas inscrit d'utilisateurs depuis un an), mais dont la date de fin est dans le futur ? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Braze arrête ces Campaigns et Canvas sept jours après la date de fin, à 4 h UTC.

### Puis-je empêcher les Campaigns d'être automatiquement arrêtées ? {#can-i-prevent-campaigns-from-auto-stopping}

Non. L'arrêt automatique ne conserve actives que les Campaigns nécessaires, ce qui réduit l'encombrement du tableau de bord et améliore les performances. Si vous avez besoin d'une liste de toutes les Campaigns automatiquement arrêtées, [soumettez un ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Qui reçoit les notifications par e-mail concernant les Campaigns et Canvas arrêtés ? {#who-receives-email-notifications-about-stopped-campaigns-and-canvases}

Par défaut, tous les utilisateurs disposant de permissions d'administrateur sont inscrits aux notifications par e-mail concernant les Campaigns et Canvas automatiquement arrêtés. Le créateur de la Campaign ou du Canvas est toujours notifié lorsque celle-ci ou celui-ci est arrêté. Pour gérer les destinataires, accédez à **Paramètres** > **Paramètres d'administration** > **Préférences de notification**, puis ajoutez ou supprimez des destinataires dans **Campaign Automatically Stopped** et **Canvas Automatically Stopped**.

### Comment fonctionne l'arrêt des Content Cards ? {#how-does-stopping-content-cards-work}

Les Content Cards dans les Campaigns ne sont pas arrêtées avant leur date d'expiration et la période tampon appropriée. Braze les arrête à la date la plus tardive entre la période tampon (envoi ponctuel, date de fin ou absence de date de fin) et la date d'expiration.

Par exemple, si une Content Card expire le 1er avril, qu'il s'agit d'un envoi ponctuel et que la date limite de conversion est de 10 jours, Braze l'arrête le 12 avril (10 jours après la date limite de conversion, plus un jour). Si une Content Card expire le 1er avril, qu'elle est déclenchée par API et qu'elle n'a pas envoyé de messages depuis le 15 mars, elle expire le 15 mars de l'année suivante.

Les Canvas ne s'arrêtent qu'après l'arrêt de leurs Content Cards, c'est-à-dire une fois que leur durée maximale est écoulée.

### J'ai une expérience de feature flag dans mon Canvas. Une fois mon feature flag défini, le Canvas reste-t-il actif ? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-does-the-canvas-remain-active}

Oui. Les Canvas comportant des étapes de feature flag ne sont pas automatiquement arrêtés et ne deviennent pas inactifs. Les Campaigns de feature flag et les expériences de feature flag suivent la même exception.

### Pourquoi des Campaigns inactives apparaissent-elles lorsque je filtre la liste des Campaigns sur les actives uniquement ? {#why-do-idle-campaigns-appear-when-i-filter-the-campaign-list-to-active-only}

Les Campaigns inactives sont considérées comme actives tant qu'elles ne sont pas arrêtées.

### Une Campaign est-elle inactive si elle envoie encore des notifications push ? {#is-a-campaign-idle-if-its-still-sending-push-notifications}

Non. Une Campaign est considérée comme inactive lorsqu'elle n'envoie plus activement de messages.