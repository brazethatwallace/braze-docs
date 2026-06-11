---
nav_title: États
article_title: États
page_order: 5
description: "Découvrez les états des campagnes et des Canvas et comment les utiliser dans le tableau de bord."
tool:
    - Campaigns
    - Canvas
---

# États des campagnes et des Canvas {#campaign-and-canvas-statuses}

> Découvrez les états des campagnes et des Canvas et comment les utiliser dans le tableau de bord.

## Filtrer par état {#filtering-by-status}

Pour filtrer vos campagnes ou Canvas par état, sélectionnez **Tous les états**, puis choisissez un état.

![Le menu déroulant « Tous les états » dans le tableau de bord de Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Modifier l'état {#changing-the-status}

Pour modifier l'état d'une campagne ou d'un Canvas, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>, puis choisissez un état.

![Une liste de Canvas dans le tableau de bord de Braze, avec le menu ouvert pour l'un des Canvas.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## États disponibles {#available-statuses}

Voici les états disponibles pour les campagnes et les Canvas :

| État | Description |
| --- | --- |
| Actif | Les campagnes et Canvas actifs sont en cours d'envoi. Par défaut, vous verrez les campagnes et Canvas actifs sur les pages respectives. |
| Brouillon | Les brouillons de campagnes et de Canvas sont enregistrés mais pas lancés. Pour continuer à les modifier et commencer l'envoi, vous pouvez sélectionner le brouillon en accédant à **Envoi de messages** dans le tableau de bord de Braze et en sélectionnant **Canvas** ou **Campaigns**. |
| Archivé | Les campagnes et Canvas archivés sont des messages qui ne sont plus envoyés. Ces campagnes et Canvas sont également retirés des graphiques statistiques sur les pages [**Accueil**]({{site.baseurl}}/user_guide/analytics/dashboards/home/) et [**Chiffre d'affaires**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/). |
| Arrêté | Les campagnes et Canvas arrêtés sont en pause, mais vous pouvez toujours les modifier. Pour reprendre un Canvas, accédez à l'étape **Résumé** du générateur de Canvas et sélectionnez **Reprendre le Canvas**. Pour les campagnes, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>, puis **Reprendre**. Pour en savoir plus, consultez [Comportement des Canvas arrêtés](#stopped-canvas-behavior). |
| Inactif | Lorsqu'une campagne ou un Canvas n'envoie plus de messages, Braze lui attribue un état inactif pour vous aider à trier et gérer votre liste de campagnes et de Canvas. Vous pouvez voir quelles campagnes ou Canvas seront automatiquement arrêtés ainsi que la date d'arrêt associée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États disponibles" }

### Comportement des Canvas arrêtés {#stopped-canvas-behavior}

Lorsqu'un Canvas est arrêté, voici ce qui se produit :

- **Messages planifiés :** vos messages planifiés ne seront pas envoyés, quelle que soit la position d'un utilisateur dans le Canvas. Cela inclut également les utilisateurs qui étaient en file d'attente en raison d'une limite de débit.
- **Envois d'e-mails :** les envois d'e-mails peuvent ne pas s'arrêter immédiatement, car votre fournisseur de services d'e-mailing (ESP) peut continuer à traiter vos demandes existantes.
- **Étapes de délai :** les utilisateurs dans une [étape de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/) y resteront normalement, mais quitteront le Canvas lorsque la période définie sera écoulée.
- **Modifications de brouillon :** toute modification de brouillon apportée au Canvas sera supprimée lorsque le Canvas sera arrêté.

Pour reprendre le Canvas, accédez à l'étape **Résumé** du générateur de Canvas et sélectionnez **Reprendre le Canvas**. Une fois réactivé, tous les messages précédemment arrêtés seront envoyés comme prévu&#8212;à condition que l'heure planifiée ne soit pas déjà passée.

## Bonnes pratiques {#best-practices}

### Surveiller vos messages par état {#monitor-your-messages-by-status}

Vous pouvez surveiller vos messages par état pour examiner les détails de performance. Par exemple, si vous avez une série de campagnes actives, vous pouvez évaluer la performance de chaque campagne à l'aide de leurs indicateurs d'engagement et effectuer des ajustements si nécessaire. Si vous avez plutôt quelques Canvas arrêtés, vous pouvez déterminer s'ils doivent être repris pour l'envoi de messages ou archivés définitivement.

{% alert tip %}
Vous cherchez d'autres moyens de rester organisé ? Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/messaging/governance/tags/) pour fournir plus de contexte en un coup d'œil.
{% endalert %}

### Auditer vos messages actifs {#audit-your-active-messages}

En effectuant des audits de vos campagnes et Canvas actifs, vous pouvez évaluer la pertinence et la performance, et supprimer ou mettre à jour toute campagne ou tout Canvas obsolète afin de garder vos messages à jour.