---
nav_title: Mandarine
article_title: Mandarine
description: "Cet article présente le partenariat entre Braze et Tangerine Store360, une plateforme omnicanale qui relie les magasins physiques aux boutiques en ligne afin d'offrir des expériences supérieures en magasin aux consommateurs et aux employés des magasins. Grâce à cette intégration, les données brutes de campagne et d'impression de Braze sont disponibles sur Store360 via le partage sécurisé de données Snowflake, et les marques peuvent mesurer l'impact de leurs campagnes sur l'engagement en magasin et le trafic en magasin."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine conçoit, crée et exploite une plateforme omnicanale appelée Store360. Store360 est une plateforme facilitatrice omnicanale connectant les magasins physiques aux boutiques en ligne afin d'améliorer l'expérience des consommateurs et des employés en magasin. Store360 suit et analyse le trafic des visites dans les magasins physiques, y compris les utilisateurs de l'application mobile des commerçants et leur engagement en magasin.

L'intégration de Braze et Tangerine vous permet d'intégrer les données brutes de campagne et d'impression de Braze dans Store360 grâce au partage sécurisé des données Snowflake. Les marques peuvent désormais mesurer l'impact de ces campagnes sur les visites en magasin physique et l'engagement en magasin.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Store360 | Un compte Store360 est nécessaire pour profiter de ce partenariat. |
| ID du compte Braze | Votre ID de groupe d'applications Braze. |
| Mise en correspondance des ID utilisateurs | Vos données clients dans Store360 et Braze doivent avoir des ID utilisateurs correspondants sur les deux plateformes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

### Analyser l'impact d'une campagne sur la fréquentation des magasins physiques {#analyze-campaign-impact-on-physical-store-visit}

Les marques utilisent Braze pour envoyer des messages de campagne aux consommateurs afin d'augmenter les visites en magasin. Pendant la campagne, Store360 capture les visites des utilisateurs de l'application mobile identifiés par leur ID utilisateur.

Grâce à la capacité analytique de Store360 Insight, les marques peuvent visualiser les détails de l'impact de la campagne, depuis les messages envoyés et lus (données de Braze) jusqu'à qui et combien de destinataires ont visité les magasins physiques (données de Store360).

## Intégration {#integration}

### Étape 1 : Activer le partage sécurisé des données Snowflake {#step-1-enable-snowflake-secure-data-share}

Collaborez avec votre équipe Braze pour activer et configurer le partage sécurisé des données Snowflake.

### Étape 2 : Configurer Store360 pour obtenir les données de Braze {#step-2-configure-store360-to-get-braze-data}

Configurez votre ID de groupe d'applications Braze sur votre compte de service Store360 à l'aide de la console web d'administration Store360. L'équipe d'administration de Tangerine devra alors synchroniser les données de Braze avec Store360 en utilisant le partage de données Snowflake.

### Étape 3 : Intégrer les SDK Store360 à l'application mobile {#step-3-integrate-store360-sdks-to-mobile-app}

Pour suivre et analyser les visites des utilisateurs de l'application mobile en magasin et les activités en magasin ainsi que les données de campagne et d'impression de Braze, vous devez intégrer le SDK Store360 dans votre application mobile en suivant les étapes fournies dans la documentation d'installation du SDK Store360. Cette documentation vous sera fournie après la signature d'un contrat client avec Tangerine Store 360.

## Analyser les données de Braze dans Store360 {#analyze-braze-data-in-store360}

Profitez du partage sécurisé des données Snowflake pour partager vos données brutes de campagne et d'impression Braze avec les analyses Store360 Insight, offrant ainsi une image complète du cycle de vie et des activités des utilisateurs, de l'en ligne au hors ligne.

Pour référence, voici tous les [champs Braze](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) disponibles pour être incorporés dans les analyses Store360. Les détails de cette étape sont très spécifiques au client et nécessitent des configurations particulières. Adressez-vous à votre gestionnaire de compte Store360 ou à support@tangerine.io pour en savoir plus.

## Informations importantes et limitations {#important-information-and-limitations}

### Disponibilité du service {#service-availability}

Actuellement, le service Store360 est disponible commercialement au Japon et en Indonésie.

Tangerine prévoit un lancement du produit Store360 dans les pays suivants en 2023.
- États-Unis d'Amérique
- Thaïlande
- Singapour
- Vietnam
- Corée

### Conservation des données {#data-retention}

Il existe une politique de conservation de deux ans pour vos données Braze dans le cadre du partage de données Snowflake.

### Délai de disponibilité des données d'événements Braze {#time-lag-in-populating-braze-event-data}

Les événements Braze sont traités avec une technologie de flux continu et sont disponibles quasiment en temps réel. En général, les événements sont disponibles dans les 30 minutes qui suivent.