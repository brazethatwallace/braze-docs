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

### Que sont les données d'interaction de messagerie ? {#what-is-messaging-interaction-data}

Les données d'interaction de messagerie font référence à la manière dont un utilisateur interagit avec une campagne ou un Canvas qu'il a reçu (par exemple, lorsqu'un utilisateur ouvre la campagne A ou qu'un utilisateur reçoit la variante A). Ces données sont utilisées pour le reciblage.

### Quand les données d'interaction de messagerie sont-elles disponibles ? {#when-is-messaging-interaction-data-available}

Les données d'interaction sont toujours disponibles. Pour les campagnes et Canvas actifs, les données d'interaction sont toujours disponibles en temps réel.

Pour les campagnes et Canvas arrêtés, leurs données d'interaction expirent après trois mois, sauf si elles sont utilisées dans des filtres de reciblage par des campagnes ou Canvas actifs. Les données d'interaction expirées sont déplacées vers un stockage à long terme et ne sont pas disponibles à l'utilisation, sauf si elles sont restaurées en suivant le processus décrit ci-dessous.

Les données d'interaction expirées ne sont jamais supprimées et peuvent être restaurées à tout moment.

#### Fonctionnalités qui utilisent les données d'interaction {#features-that-use-interaction-data}

Les fonctionnalités suivantes utilisent les données d'interaction de messagerie :

- Les filtres de reciblage qui ciblent une campagne ou un Canvas spécifique
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
- Les filtres de reciblage qui ciblent des campagnes ou Canvas avec une certaine étiquette
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- Les listes **Campaigns Received** et **Canvas Messages Received** sur le profil utilisateur
- L'endpoint `/users/export`
- Les exports CSV **User Data** sur les pages de résumé des campagnes et Canvas

Ces fonctionnalités n'incluent pas les données d'interaction expirées dans leurs résultats. Pour inclure les données d'interaction expirées dans les résultats de ces fonctionnalités, restaurez la campagne ou le Canvas dont les données ont expiré.

Par exemple, les Canvas ne peuvent pas être lancés si les données d'interaction ont expiré, ce qui signifie qu'une modification comme l'ajout d'une équipe au Canvas ne peut pas être enregistrée.

#### Fonctionnalités qui n'utilisent pas les données d'interaction {#features-that-dont-use-interaction-data}

Les fonctionnalités suivantes **n'utilisent pas** les données d'interaction de messagerie, ce qui signifie qu'elles ne sont pas affectées par l'expiration des données d'interaction de messagerie :

- Configuration des campagnes et Canvas
- Analyses des campagnes et Canvas
- Rapports d'analyse (tels que le Générateur de rapports, le Générateur de requêtes et les Rapports d'engagement)
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

### Comment restaurer les données d'interaction de messagerie ? {#how-do-i-restore-messaging-interaction-data}

Pour restaurer vos données d'interaction, suivez ces étapes :

1. Accédez à la campagne ou au Canvas expiré.
2. En haut de la page de la campagne ou du Canvas, sélectionnez **Restore interaction data** dans la bannière.

Vous pouvez également restaurer les données d'interaction pour plusieurs campagnes depuis la page **Campaigns** en sélectionnant les campagnes, puis en sélectionnant **Restore interaction data**.

Le temps de restauration des données d'interaction peut varier, mais dans la plupart des cas, ce processus peut prendre de 5 à 15 minutes. Une fois la restauration terminée, vous recevrez un e-mail.

#### Restauration par étiquette {#restoring-by-tag}

Vous pouvez également restaurer les données d'interaction pour les campagnes ou Canvas expirés avec une étiquette donnée.

1. Accédez à la page **Campaigns** ou **Canvas** et recherchez par l'étiquette concernée.
2. Sélectionnez vos campagnes ou Canvas.
3. Sélectionnez **Restore interaction data** pour restaurer les données de ces campagnes ou Canvas.

Après trois mois supplémentaires d'inactivité, ces campagnes ou Canvas expirent à nouveau.

#### Reciblage par étiquette {#retargeting-by-tag}

Les campagnes qui utilisent des filtres de reciblage ciblant par étiquette ne sont pas exemptées de l'expiration. Les filtres de reciblage qui ciblent par étiquette incluent :

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

### Quand les données d'interaction de messagerie étaient-elles disponibles par le passé ? {#when-was-messaging-interaction-data-available-in-the-past}

Auparavant, les données d'interaction de messagerie étaient supprimées lorsqu'une campagne ou un Canvas :

- N'avait pas envoyé de messages depuis 25 mois calendaires, ET
- N'était pas utilisé pour le reciblage dans des campagnes, Canvas ou Content Cards actifs.

Les campagnes et Canvas dont les données d'interaction de messagerie ont été précédemment supprimées ne peuvent pas être utilisés dans les filtres de reciblage pour les campagnes, Canvas et segments.