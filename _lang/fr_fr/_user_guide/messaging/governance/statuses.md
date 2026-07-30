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
| Actif | Les Campaigns et Canvas actifs sont en cours d'envoi. Par défaut, vous verrez les Campaigns et Canvas actifs sur leurs pages respectives. |
| Brouillon | Les brouillons de Campaigns et de Canvas sont enregistrés mais pas encore lancés. Pour continuer à les modifier et commencer l'envoi, vous pouvez sélectionner le brouillon en accédant à **Messagerie** dans le tableau de bord de Braze et en sélectionnant **Canvas** ou **Campaigns**. |
| Archivé | Les Campaigns et Canvas archivés sont des messages qui ne sont plus envoyés. Ces Campaigns et Canvas sont également retirés des graphiques statistiques sur les pages [**Accueil**]({{site.baseurl}}/user_guide/analytics/dashboards/home) et [**Chiffre d'affaires**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report). |
| Arrêté | Les Campaigns et Canvas arrêtés sont en pause, mais vous pouvez toujours les modifier. Pour reprendre un Canvas, accédez à l'étape **Résumé** du générateur de Canvas et sélectionnez **Reprendre le Canvas**. Pour les Campaigns, sélectionnez le menu <i class="fas fa-ellipsis-vertical" aria-label="Menu d'options"></i>, puis **Reprendre**. Pour en savoir plus, consultez [Comportement d'un Canvas arrêté](#stopped-canvas-behavior). |
| Inactif | Lorsqu'une Campaign ou un Canvas n'envoie plus de messages, Braze lui attribue un statut inactif pour vous aider à trier et gérer votre liste de Campaigns et de Canvas. Vous pouvez voir quels Campaigns ou Canvas seront automatiquement arrêtés ainsi que la date d'arrêt associée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuts disponibles" }

### Comportement d'un Canvas arrêté {#stopped-canvas-behavior}

Lorsqu'un Canvas est arrêté, voici ce qui se produit :

- **Messages planifiés :** Vos messages planifiés ne seront pas envoyés, quelle que soit la position de l'utilisateur dans le Canvas. Cela inclut également les utilisateurs mis en file d'attente en raison de la limitation du débit.
- **Envois d'e-mails :** Les envois d'e-mails peuvent ne pas s'arrêter immédiatement, car votre fournisseur de services d'e-mailing (ESP) peut continuer à traiter vos requêtes existantes.
- **Étapes de délai :** Les utilisateurs dans une [étape de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) y resteront normalement, mais quitteront le Canvas lorsque la période définie sera écoulée.
- **Modifications en brouillon :** Toutes les modifications en brouillon apportées au Canvas seront supprimées lorsque le Canvas sera arrêté.

Pour reprendre le Canvas, accédez à l'étape **Résumé** du générateur de Canvas et sélectionnez **Reprendre le Canvas**. Une fois réactivé, tous les messages précédemment arrêtés seront envoyés comme prévu — à condition que l'heure planifiée ne soit pas déjà passée.

## Bonnes pratiques {#best-practices}

### Surveillez vos messages par statut {#monitor-your-messages-by-status}

Vous pouvez surveiller vos messages par statut pour examiner les détails de performance. Par exemple, si vous avez une série de Campaigns actives, vous pouvez évaluer la performance de chaque Campaign à l'aide de leurs indicateurs d'engagement et effectuer des ajustements si nécessaire. Si, en revanche, vous avez quelques Canvas arrêtés, vous pouvez déterminer s'ils doivent être relancés pour l'envoi de messages ou archivés définitivement.

{% alert tip %}
Vous cherchez d'autres moyens de rester organisé ? Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [tags]({{site.baseurl}}/user_guide/messaging/governance/tags) pour fournir davantage de contexte en un coup d'œil.
{% endalert %}

### Auditez vos messages actifs {#audit-your-active-messages}

En réalisant des audits de vos Campaigns et Canvas actifs, vous pouvez évaluer leur pertinence et leur performance, puis supprimer ou mettre à jour les Campaigns et Canvas obsolètes afin de garder votre communication à jour.