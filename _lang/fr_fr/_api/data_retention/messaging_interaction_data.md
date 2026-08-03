---
nav_title: "Données d'interaction de messagerie"
article_title: "Données d'interaction de messagerie"
alias: "/messaging_interaction_data/"
page_order: 1
description: "Cet article de référence couvre les données d'interaction des campagnes et Canvas ainsi que leur disponibilité."
page_type: reference
---

# À propos de la disponibilité des données d'interaction de messagerie {#about-messaging-interaction-data-availability}

> Découvrez les données d'interaction de messagerie pour les campagnes et Canvas, notamment la durée de conservation par Braze et les fonctionnalités qui les utilisent pour le reciblage.

## Qu'est-ce que les données d'interaction de messaging ? {#what-is-messaging-interaction-data}

Les données d'interaction de messaging font référence à la manière dont un utilisateur interagit avec une Campaign ou un Canvas qu'il a reçu (par exemple, lorsqu'un utilisateur ouvre la Campaign A ou qu'un utilisateur reçoit la variante A). Ces données sont utilisées pour le reciblage.

## Quand les données d'interaction de messagerie sont-elles disponibles ? {#when-is-messaging-interaction-data-available}

Les données d'interaction sont toujours disponibles. Pour les Campaigns et Canvas actifs, les données d'interaction sont toujours disponibles en temps réel.

Pour les Campaigns et Canvas arrêtés, leurs données d'interaction expirent après trois mois, sauf si elles sont utilisées dans des filtres de reciblage par des Campaigns ou Canvas actifs. Les données d'interaction expirées sont déplacées vers un stockage à long terme et ne sont pas disponibles à l'utilisation, sauf si elles sont restaurées à l'aide du processus décrit.

Les données d'interaction expirées ne sont jamais supprimées et peuvent être restaurées à tout moment.

### Fonctionnalités qui utilisent les données d'interaction {#features-that-use-interaction-data}

Les fonctionnalités suivantes utilisent les données d'interaction de messagerie :

- Les filtres de reciblage qui reciblent sur une Campaign ou un Canvas spécifique
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- Les filtres de reciblage qui reciblent sur des Campaigns ou Canvas avec une certaine étiquette
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- Les listes **Campaigns Received** et **Canvas Messages Received** sur le profil utilisateur
- L'endpoint `/users/export`
- Les exports CSV de **User Data** sur les pages de résumé des Campaigns et Canvas

Ces fonctionnalités n'incluent pas les données d'interaction expirées dans leurs résultats. Pour inclure les données d'interaction expirées dans les résultats de ces fonctionnalités, restaurez la Campaign ou le Canvas dont les données ont expiré.

Par exemple, les Canvas ne peuvent pas être lancés si les données d'interaction ont expiré, ce qui signifie qu'une modification comme l'ajout d'une équipe au Canvas ne peut pas être enregistrée.

### Fonctionnalités qui n'utilisent pas les données d'interaction {#features-that-dont-use-interaction-data}

Les fonctionnalités suivantes **n'utilisent pas** les données d'interaction de messagerie, ce qui signifie qu'elles ne sont pas affectées par l'expiration des données d'interaction de messagerie :

- Configuration des Campaigns et Canvas
- Analyse des Campaigns et Canvas
- Rapports d'analyse (tels que le générateur de rapports, le Query Builder et les rapports d'engagement)
- Currents
- Snowflake Data Share
- Extensions de segments
- Points de donnée
- Les filtres de reciblage suivants :
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

## Comment restaurer les données d'interaction de messagerie ? {#how-do-i-restore-messaging-interaction-data}

Pour restaurer vos données d'interaction, suivez ces étapes :

1. Accédez à la Campaign ou au Canvas expiré(e).
2. En haut de la page de destination de la Campaign ou du Canvas, sélectionnez **Restaurer les données d'interaction** dans la bannière.

Vous pouvez également restaurer les données d'interaction pour plusieurs Campaigns depuis la page **Campaigns** en sélectionnant les Campaigns, puis en sélectionnant **Restaurer les données d'interaction**.

Le temps de restauration des données d'interaction peut varier, mais dans la plupart des cas, ce processus peut prendre de 5 à 15 minutes. Une fois la restauration terminée, vous recevrez un e-mail.

### Restauration par étiquette {#restoring-by-tag}

Vous pouvez également restaurer les données d'interaction pour les Campaigns ou Canvas expirés ayant une étiquette donnée.

1. Accédez à la page **Campaigns** ou **Canvas** et recherchez par l'étiquette correspondante.
2. Sélectionnez vos Campaigns ou Canvas.
3. Sélectionnez **Restaurer les données d'interaction** pour restaurer les données de ces Campaigns ou Canvas.

Après trois mois supplémentaires d'inactivité, ces Campaigns ou Canvas expirent à nouveau.

### Reciblage par étiquette {#retargeting-by-tag}

Les Campaigns qui utilisent des filtres de reciblage ciblant par étiquette ne sont pas exemptées de l'expiration. Les filtres de reciblage ciblant par étiquette incluent :

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

## Quand les données d'interaction de messaging étaient-elles disponibles par le passé ? {#when-was-messaging-interaction-data-available-in-the-past}

Auparavant, les données d'interaction de messaging étaient supprimées lorsqu'une Campaign ou un Canvas :

- N'avait pas envoyé de messages depuis 25 mois calendaires, ET
- N'était pas utilisé pour le reciblage dans des Campaigns, Canvas ou Content Cards actifs.

Les Campaigns et Canvas dont les données d'interaction de messaging ont été précédemment supprimées ne peuvent pas être utilisés dans les filtres de reciblage pour les Campaigns, Canvas et Segments.

## Résolution des problèmes {#troubleshooting}

### Pourquoi la date d'expiration d'une campagne ou d'un Canvas continue-t-elle d'afficher demain ? {#why-does-a-campaign-or-canvas-expiration-date-keep-showing-tomorrow}

Si une campagne ou un Canvas arrêté(e) est encore référencé(e) par un filtre de reciblage actif (par exemple, dans un Segment, une campagne, un Canvas ou une Content Card actif(ve)), Braze ne décharge pas encore ses données d'interaction.

Dans ce cas, la date d'expiration affichée dans l'interface reflète la prochaine exécution de nettoyage planifiée. Elle peut donc apparaître comme « demain » et continuer à avancer tant que des références existent encore.

Une fois que vous avez supprimé toutes les références de reciblage actives, les données d'interaction sont déchargées lors du prochain cycle de nettoyage (généralement le lendemain).

Vous pouvez rencontrer les messages d'erreur suivants lorsque vous essayez de reprendre ou de désarchiver des Campaigns, des Canvas ou des Content Cards dont les données d'interaction ont expiré :

| Message d'erreur | Quand il apparaît | Résolution des problèmes |
| --- | --- | --- |
| « Can't resume Canvases because at least one Canvas is using filters or segments that have expired data. Remove these and try again. » | Lorsque vous essayez de reprendre un ou plusieurs Canvas (action groupée) qui utilisent des filtres ou des Segments avec des données d'interaction expirées | [Restaurer les données d'interaction](#how-do-i-restore-messaging-interaction-data) pour les Campaigns ou Canvas référencés dans les filtres, ou supprimer les filtres concernés du Canvas |
| « Can't resume {name} because it is using filters or segments that have expired data. Remove these and try again. » | Lorsque vous essayez de reprendre un seul Canvas qui utilise des filtres ou des Segments avec des données d'interaction expirées | [Restaurer les données d'interaction](#how-do-i-restore-messaging-interaction-data) pour les Campaigns ou Canvas référencés dans les filtres, ou supprimer les filtres concernés du Canvas |
| « Resume is only available for stopped Canvases with available interaction data » | Lorsque vous essayez de reprendre un Canvas depuis le menu d'action groupée, mais que le Canvas a des données d'interaction expirées | [Restaurer les données d'interaction](#how-do-i-restore-messaging-interaction-data) pour le Canvas |
| « You can't resume these Campaigns. One or more Campaigns include expired filters. » | Lorsque vous essayez de reprendre une ou plusieurs Campaigns qui utilisent des filtres avec des données d'interaction expirées | [Restaurer les données d'interaction](#how-do-i-restore-messaging-interaction-data) pour les Campaigns ou Canvas référencés dans les filtres, ou supprimer les filtres concernés de la campagne |
| « You can't unarchive these Cards. One or more Cards include expired filters. » | Lorsque vous essayez de désarchiver une ou plusieurs Content Cards qui utilisent des filtres avec des données d'interaction expirées | [Restaurer les données d'interaction](#how-do-i-restore-messaging-interaction-data) pour les Campaigns ou Canvas référencés dans les filtres, ou supprimer les filtres concernés de la Card |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages d'erreur courants" }