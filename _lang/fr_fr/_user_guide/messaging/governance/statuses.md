---
nav_title: États
article_title: États
page_order: 6
description: "Découvrez les états des Campaigns et des Canvas et comment les utiliser dans le tableau de bord."
tool:
    - Campaigns
    - Canvas
---

# États des Campaigns et des Canvas {#campaign-and-canvas-statuses}

> Découvrez les états des Campaigns et des Canvas et comment les utiliser dans le tableau de bord.

## Filtrer par statut {#filtering-by-status}

Pour filtrer vos Campaigns ou Canvas par statut, sélectionnez **All Statuses**, puis choisissez un statut.

![Le menu déroulant « All Statuses » dans le tableau de bord de Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Modifier le statut {#changing-the-status}

Pour modifier le statut d'une Campaign ou d'un Canvas, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>, puis choisissez un statut.

![Une liste de Canvas dans le tableau de bord de Braze, avec le menu ouvert pour l'un des Canvas.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Statuts disponibles {#available-statuses}

Voici les statuts disponibles pour les Campaigns et les Canvas :

| Statut | Description |
| --- | --- |
| Actif | Les Campaigns et Canvas actifs sont en cours d'envoi. Par défaut, vous verrez les Campaigns et Canvas actifs sur les pages correspondantes. |
| Brouillon | Les brouillons de Campaigns et de Canvas sont enregistrés mais pas encore lancés. Pour continuer à les modifier et commencer l'envoi, vous pouvez sélectionner le brouillon en accédant à **Messaging** dans le tableau de bord de Braze, puis en sélectionnant **Canvas** ou **Campaigns**. |
| Archivé | Les Campaigns et Canvas archivés sont des messages qui ne sont plus envoyés. Ces Campaigns et Canvas sont également retirés des graphiques statistiques sur les pages [**Accueil**]({{site.baseurl}}/user_guide/analytics/dashboards/home) et [**Chiffre d'affaires**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report). |
| Arrêté | Les Campaigns et Canvas arrêtés sont en pause, mais vous pouvez toujours les modifier. Pour reprendre un Canvas, accédez à l'étape **Résumé** du générateur de Canvas et sélectionnez **Reprendre le Canvas**. Pour les Campaigns, sélectionnez le menu <i class="fas fa-ellipsis-vertical" aria-label="Menu d'options"></i>, puis **Reprendre**. Pour plus d'informations, consultez [Comportement d'un Canvas arrêté](#stopped-canvas-behavior). |
| Inactif | Lorsqu'une Campaign ou un Canvas n'envoie plus de messages, Braze lui attribue un statut inactif pour vous aider à trier et gérer votre liste de Campaigns et de Canvas. Vous pouvez voir quelles Campaigns ou quels Canvas seront automatiquement arrêtés ainsi que la date d'arrêt associée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuts disponibles" }

### Comportement d'un Canvas arrêté {#stopped-canvas-behavior}

Lorsqu'un Canvas est arrêté, voici ce qui se produit :

- **Messages planifiés :** Vos messages planifiés ne seront pas envoyés, quel que soit l'emplacement de l'utilisateur dans le Canvas. Cela inclut également les utilisateurs qui étaient en file d'attente en raison de la limitation du débit.
- **Envois d'e-mails :** Les envois d'e-mails peuvent ne pas s'arrêter immédiatement, car votre fournisseur de services d'e-mailing (ESP) peut continuer à traiter vos requêtes existantes.
- **Étapes de délai :** Les utilisateurs dans une [étape de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) y restent normalement, mais quitteront le Canvas lorsque la période définie prendra fin.
- **Modifications en brouillon :** Toute modification en brouillon apportée au Canvas sera supprimée lorsque le Canvas est arrêté.

#### Lorsque vous reprenez un Canvas {#when-you-resume-a-canvas}

Pour reprendre le Canvas, accédez à l'étape **Résumé** du générateur de Canvas et sélectionnez **Reprendre le Canvas**. Lorsque vous reprenez un Canvas, les utilisateurs poursuivent leur parcours là où ils s'étaient arrêtés :

- Utilisateurs dans les étapes de délai : Les utilisateurs qui attendaient dans une étape de délai lorsque le Canvas a été arrêté continuent d'attendre pendant la durée restante du délai. Par exemple, si un utilisateur avait attendu 2 heures sur un délai de 24 heures lorsque le Canvas a été arrêté pendant 3 jours, il attendra encore 22 heures après la reprise du Canvas avant de progresser.
- Utilisateurs en attente de messages : Tous les messages planifiés qui étaient en attente lorsque le Canvas a été arrêté sont envoyés comme prévu lorsque vous reprenez le Canvas, à condition que l'heure planifiée ne soit pas déjà passée.
- Utilisateurs ayant quitté le Canvas : Les utilisateurs qui ont quitté le Canvas pendant la période d'arrêt (par exemple, les utilisateurs qui étaient dans des étapes de délai et ont atteint la fin de leur délai) ne réintégreront pas le Canvas lorsque vous le reprenez.

#### Comportement lié au fuseau horaire local {#local-time-zone-behavior}

Si votre Canvas est configuré pour **faire entrer les utilisateurs dans ce Canvas selon leur fuseau horaire local**, gardez ces considérations à l'esprit lors de l'arrêt et de la reprise :

- Fenêtres d'entrée : Lorsque vous reprenez le Canvas, les utilisateurs entrent en fonction de leur fuseau horaire local tel qu'il a été configuré à l'origine. Braze continue d'évaluer l'éligibilité à l'entrée en fonction du fuseau horaire de chaque utilisateur.
- Fenêtres d'entrée manquées : Si le Canvas a été arrêté pendant une fenêtre d'entrée planifiée pour des utilisateurs dans certains fuseaux horaires, ces utilisateurs n'entreront pas rétroactivement lorsque le Canvas sera repris. L'évaluation de l'entrée reprend pour les périodes à venir.

#### Scénarios courants {#common-scenarios}

**Scénario 1 : Erreur dans le contenu du message**
Vous lancez un Canvas mais remarquez une faute de frappe dans l'un des messages. Arrêtez le Canvas, modifiez le message en mode brouillon, puis reprenez-le. Les utilisateurs qui n'ont pas encore reçu le message recevront la version corrigée. Les utilisateurs qui l'ont déjà reçu ne le recevront pas à nouveau.

**Scénario 2 : Problème de ciblage**
Vous réalisez que le Canvas cible le mauvais Segment. Arrêtez le Canvas immédiatement pour empêcher d'autres utilisateurs d'y entrer. Les utilisateurs actuellement dans des étapes de délai quitteront le Canvas lorsque leur période de délai prendra fin. Vous pouvez ensuite créer un nouveau Canvas avec le ciblage correct.

**Scénario 3 : Scénario de délai prolongé**
Vous avez un Canvas avec une étape de délai de sept jours. Vous arrêtez le Canvas au bout de trois jours. Les utilisateurs qui étaient dans l'étape de délai continuent d'attendre, mais lorsque leur période de délai se termine alors que le Canvas est toujours arrêté, ils quittent le Canvas. Si vous reprenez le Canvas avant la fin de leur délai, ils poursuivent leur parcours.

## Bonnes pratiques {#best-practices}

### Surveillez vos messages par statut {#monitor-your-messages-by-status}

Vous pouvez surveiller vos messages par statut pour examiner les détails de performance. Par exemple, si vous avez une série de Campaigns actives, vous pouvez évaluer la performance de chaque Campaign à l'aide de leurs indicateurs d'engagement et effectuer des ajustements si nécessaire. Si, en revanche, vous avez quelques Canvas arrêtés, vous pouvez déterminer s'ils doivent être repris pour l'envoi de messages ou archivés entièrement.

{% alert tip %}
Vous cherchez d'autres moyens de rester organisé ? Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [tags]({{site.baseurl}}/user_guide/messaging/governance/tags) pour fournir plus de contexte en un coup d'œil.
{% endalert %}

### Auditez vos messages actifs {#audit-your-active-messages}

En effectuant des audits de vos Campaigns et Canvas actifs, vous pouvez évaluer la pertinence et la performance, puis supprimer ou mettre à jour les Campaigns et Canvas obsolètes afin de garder votre communication à jour.