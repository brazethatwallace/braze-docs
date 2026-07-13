---
nav_title: Nexla
article_title: Nexla
description: "Cet article de référence décrit le partenariat entre Braze et Nexla, une plateforme unifiée d'opérations de données qui permet aux utilisateurs de Braze Currents d'extraire, de transformer et de charger des données de lacs de données vers d'autres emplacements dans un format personnalisé."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) est un leader des opérations de données unifiées et figure parmi les Gartner Cool Vendors 2021. La plateforme Nexla fournit des outils pour créer des flux de données évolutifs, offrant des opérations de données gouvernées, une collaboration et une agilité pour les équipes métier et data. Les équipes qui travaillent avec des données bénéficient d'une expérience unifiée no-code/low-code pour intégrer, transformer, provisionner et surveiller les données pour tous les cas d'usage.

L'intégration de Braze et Nexla permet aux clients qui utilisent [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents) de tirer parti de Nexla pour extraire, transformer et charger les données des lacs de données vers d'autres emplacements dans un format personnalisé, rendant ainsi les données facilement accessibles dans l'ensemble de votre écosystème.

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte Nexla | Un [compte Nexla](https://www.nexla.com/get-demo) est nécessaire pour profiter de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Cas d'usage {#use-cases}

[Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), le concept de données en tant que produit de Nexla, permet de travailler avec des données de n'importe quel format sans avoir à gérer les métadonnées. Lorsque vous mettez en place des flux de données vers ou depuis Braze avec Nexla, des outils no-code sont disponibles en quelques minutes. Une fois que le flux de données est défini sur une destination, Nexla surveille le flux et s'adapte à n'importe quel volume de données.

## Intégration {#integration}

### Étape 1 : Créer un compte Nexla {#step-1-create-a-nexla-account}

Si vous n'avez pas encore de compte Nexla, rendez-vous sur le [site web](https://www.nexla.com) de Nexla pour demander une démonstration et un essai gratuits. Ensuite, connectez-vous sur [www.dataops.nexla.io](https://www.dataops.nexla.io) avec vos nouveaux identifiants.

### Étape 2 : Ajouter votre source {#step-2-add-your-source}

#### Si Braze est votre source de données {#if-braze-is-your-data-source}
1. Sur la plateforme Nexla, accédez à **Flows > Create a New Flow** dans la barre de navigation.
2. Cliquez sur **Create New Source**, sélectionnez le connecteur Braze, puis cliquez sur **Next**.
3. Sélectionnez **Add a New Credential**, nommez l'identifiant, ajoutez votre clé API Braze et votre endpoint REST, puis cliquez sur **Save**.
4. Enfin, sélectionnez vos données et cliquez sur **Save**.

Nexla recherchera dans la source les données disponibles et générera un [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) à transformer ou à envoyer vers une destination.

#### Si Braze est votre destination {#if-braze-is-your-destination}

Consultez la documentation de Nexla sur la [connexion de sources à Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Étape 3 : Transformer (facultatif) {#step-3-transform-optional}

Si vous souhaitez effectuer des [transformations](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) personnalisées sur vos données ou utiliser les connecteurs prédéfinis de Nexla, cliquez sur le bouton **Transform** du jeu de données pour accéder au Transform Builder. Vous trouverez des conseils sur l'utilisation du Transform Builder dans la [documentation de Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Étape 4 : Envoyer vers une destination {#step-4-send-to-destination}

Pour envoyer des données vers une destination, cliquez sur la flèche **Send to Destination** du jeu de données et sélectionnez l'un des connecteurs de destination de Nexla ou Braze si vous aviez une autre source. Saisissez vos identifiants, configurez les options de destination, puis cliquez sur **Save**. Les données commenceront instantanément à circuler dans le format que vous avez spécifié vers la destination de votre choix.

## Utilisation de cette intégration {#using-this-integration}

Une fois le flux configuré, vous n'avez plus rien à faire. Nexla gérera toutes les modifications apportées aux données sources, s'adaptera à toutes les nouvelles données et vous informera de toute modification du schéma ou de toute erreur nécessitant une intervention. Si vous souhaitez apporter des modifications aux transformations, à la source ou à la destination, vous pouvez cliquer sur ces options et effectuer la modification ; Nexla mettra à jour le flux instantanément.