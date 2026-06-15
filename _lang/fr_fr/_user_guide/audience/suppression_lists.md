---
nav_title: Listes de suppression
article_title: Listes de suppression
page_order: 7
page_type: reference
tool: Segments
description: "Cette page explique comment utiliser les listes de suppression pour spécifier quels utilisateurs ne doivent jamais recevoir vos messages."

---

# Listes de suppression {#suppression-lists}

> Les listes de suppression sont des groupes d'utilisateurs qui ne reçoivent automatiquement aucune Campaign ni aucun Canvas. Les listes de suppression sont définies par des filtres de segment, et les utilisateurs entrent et sortent des listes de suppression lorsqu'ils remplissent les critères de filtre. Vous pouvez également définir des étiquettes d'exception afin que la liste de suppression ne s'applique pas aux Campaigns ou Canvas portant ces étiquettes. Les messages provenant de Campaigns ou de Canvas avec des étiquettes d'exception atteindront toujours les utilisateurs de la liste de suppression qui font partie des segments cibles.

## Pourquoi utiliser les listes de suppression ? {#why-use-suppression-lists}

Les listes de suppression sont dynamiques et s'appliquent automatiquement à toutes les formes d'envoi de messages, mais vous pouvez définir des exceptions pour des étiquettes sélectionnées. Si vos étiquettes d'exception sélectionnées sont utilisées dans une Campaign ou un Canvas, alors cette liste de suppression ne s'appliquera pas à cette Campaign ou ce Canvas. Les messages provenant de Campaigns ou de Canvas avec des étiquettes d'exception atteindront toujours les utilisateurs de la liste de suppression qui font partie de vos segments cibles.

### Types de messages et canaux concernés par les listes de suppression {#message-types-and-channels-affected-by-suppression-lists}

Les listes de suppression s'appliquent à tous les types de messages et canaux, à l'exception des [indicateurs de fonctionnalité]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags/). Cela signifie que les listes de suppression s'appliquent par défaut à tous les canaux, Campaigns et Canvas, y compris :
- [Campaigns API]({{site.baseurl}}/api/api_campaigns/)
- Campaigns et Canvas déclenchés par API
- [E-mails transactionnels]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)

Le seul type de message auquel les listes de suppression ne s'appliquent pas est celui des indicateurs de fonctionnalité. Les utilisateurs figurant dans une liste de suppression ne seront pas exclus des indicateurs de fonctionnalité, mais seront exclus de tous les autres canaux.

Vous pouvez utiliser des étiquettes d'exception afin que les utilisateurs de la liste de suppression soient toujours ciblés par des Campaigns et Canvas particuliers. Pour plus de détails, consultez l'étape 4 dans [Configuration des listes de suppression](#setup). Si vous n'ajoutez pas d'étiquettes d'exception à une liste de suppression, les utilisateurs de cette liste de suppression ne seront ciblés par aucun envoi de messages en dehors des indicateurs de fonctionnalité.

{% alert note %}
Les listes de suppression s'appliquent aux Campaigns API créées dans le tableau de bord de Braze avec un `campaign_id`. Les listes de suppression ne s'appliquent pas aux messages envoyés via les [endpoints d'envoi de messages Braze]({{site.baseurl}}/api/endpoints/messaging/) sans `campaign_id` associé.
{% endalert %}

![La section « Paramètres d'exception » avec une case à cocher pour ne pas appliquer la liste de suppression aux Campaigns et Canvas déclenchés par API.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Configuration des listes de suppression {#setup}

{% alert note %}
Tous les utilisateurs peuvent consulter les listes de suppression, mais seuls les utilisateurs disposant des [autorisations d'administrateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions?tab=admin) peuvent créer et gérer les listes de suppression.
{% endalert %}

1. Accédez à **Audience** > **Suppression Lists**.<br><br>![La page « Listes de suppression » avec une liste de trois listes de suppression.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Sélectionnez **Create Suppression List** et ajoutez un nom.<br><br>![Une fenêtre intitulée « Create a Suppression List » avec un champ pour saisir un nom.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Utilisez les filtres de segment pour identifier les utilisateurs de vos listes de suppression. Vous devez en sélectionner au moins un.

{% alert important %}
Bien que le processus de configuration semble similaire à la [création de segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), une liste de suppression est un groupe d'utilisateurs auxquels vous ne souhaitez **pas** envoyer de messages, indépendamment de leur appartenance à un segment.
{% endalert %}

![Un générateur de liste de suppression avec un filtre pour les utilisateurs ayant ouvert un e-mail pour la dernière fois il y a plus de 90 jours.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4. Déterminez si vous souhaitez avoir des exceptions basées sur des étiquettes en cochant la case sous le nom de votre segment (consultez [Pourquoi utiliser les listes de suppression ?](#why-use-suppression-lists) pour plus d'informations), puis ajoutez les étiquettes des Campaigns ou Canvas que les utilisateurs de cette liste de suppression devraient tout de même recevoir. <br><br>En d'autres termes, si vous ajoutez l'étiquette d'exception « Confirmation d'expédition », les utilisateurs de votre liste de suppression seront exclus de tous les envois de messages, sauf ceux qui utilisent l'étiquette « Confirmation d'expédition ».<br><br>![La section « Détails de la liste de suppression » avec une étiquette d'exception appliquée appelée « Confirmation d'expédition ».]({% image_buster /assets/img/exception_tags.png %})<br><br>
5. Enregistrez ou activez votre liste de suppression.
- Lorsque vous enregistrez, votre liste de suppression sera sauvegardée mais ne sera pas activée, ce qui signifie qu'elle ne prendra pas effet. Votre liste de suppression restera inactive jusqu'à ce que vous l'activiez, et les listes de suppression inactives n'auront aucun impact sur l'envoi de messages (les utilisateurs ne seront pas exclus des messages).
- Lorsque vous activez, votre liste de suppression sera sauvegardée et prendra effet immédiatement, ce qui signifie que les utilisateurs de votre liste de suppression seront immédiatement exclus des Campaigns ou Canvas (à l'exception de ceux contenant une étiquette d'exception).

{% alert note %}
Seuls les administrateurs peuvent enregistrer ou activer les listes de suppression. Vous pouvez avoir jusqu'à cinq listes de suppression actives à la fois pendant la bêta.
{% endalert %}

Vous pouvez désactiver ou archiver les listes de suppression lorsque vous n'en avez plus besoin.
- Pour désactiver, sélectionnez une liste de suppression active et sélectionnez **Deactivate**. Les listes de suppression désactivées peuvent être réactivées ultérieurement.
- Pour archiver, faites-le depuis la page **Suppression Lists**.

## Utilisation des listes de suppression {#suppression-list-usage}

Pour vérifier si votre liste de suppression a empêché un utilisateur de recevoir un message, utilisez **User Lookup** dans l'étape **Target Audience** de votre Campaign ou Canvas. Vous pourrez alors voir de quelle liste de suppression il fait partie.

{% alert note %}
Les listes de suppression sont mises à jour avant l'envoi d'un message, et non après le lancement d'une Campaign. Cela signifie qu'un utilisateur ajouté à une liste de suppression après le lancement de la Campaign mais avant l'envoi du message pourrait tout de même recevoir le message.
{% endalert %}

![Fenêtre « User Lookup » montrant qu'un utilisateur fait partie d'une liste de suppression.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Vous pouvez également trouver les listes de suppression appliquées dans l'étape **Summary**.
{% endalert %}

Lors de la création d'une Campaign ou d'un Canvas, utilisez **User Lookup** dans l'étape **Target Audience** pour rechercher un utilisateur. S'il ne fait pas partie de l'audience cible, vous pouvez voir la liste de suppression dont il fait partie.

![Fenêtre « User Lookup » montrant qu'un utilisateur fait partie d'une liste de suppression.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campaign {#campaign}

Si un utilisateur figure dans une liste de suppression, il ne recevra pas la Campaign pour laquelle cette liste de suppression s'applique. Consultez [Types de messages et canaux concernés par les listes de suppression](#message-types-and-channels-affected-by-suppression-lists) pour les cas où une liste de suppression ne s'applique pas.

![La section « Listes de suppression » avec une liste de suppression active, appelée « Low marketing health scores ».]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas {#canvas}

À partir du moment où un utilisateur est ajouté à une liste de suppression, il n'entrera pas dans les Canvas. S'il est déjà entré dans un Canvas, il ne recevra pas les étapes de message. Cela signifie que si un utilisateur se trouve déjà dans un Canvas lorsqu'il est ajouté à une liste de suppression, il progressera dans le Canvas jusqu'à la prochaine étape de message, à laquelle il sortira sans recevoir l'étape de message.

Par exemple, supposons qu'un Canvas comporte une étape Mise à jour utilisateur suivie d'une étape de message. Si un utilisateur entre dans le Canvas puis est ajouté à une liste de suppression, cet utilisateur passera tout de même par l'étape Mise à jour utilisateur (où il pourra être mis à jour), puis sortira à l'étape de message, moment auquel il sera inclus dans les indicateurs de sortie.