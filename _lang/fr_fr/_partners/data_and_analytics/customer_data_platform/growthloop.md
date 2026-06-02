---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "Cet article de référence présente le partenariat entre Braze et GrowthLoop, une plateforme qui vous permet de segmenter les données clients directement à partir des entrepôts de données et de les envoyer à Braze."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) aide les équipes marketing à activer les données clients depuis l'entrepôt de données dans le cloud vers Braze et d'autres canaux. Automatisez, développez et mesurez vos programmes marketing à partir de votre entrepôt de données dans le cloud, en conservant les données dans un emplacement unique et centralisé.

_Cette intégration est maintenue par GrowthLoop._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et GrowthLoop vous permet de segmenter les données clients directement depuis l'entrepôt de données et de les envoyer à Braze, garantissant ainsi que les utilisateurs peuvent exploiter l'ensemble des fonctionnalités avancées de Braze en parallèle avec leur source unique de vérité. Rationalisez vos efforts marketing pour la segmentation et l'activation des clients, en réduisant le temps nécessaire pour segmenter, lancer, tester et mesurer les résultats des campagnes ciblées envoyées à Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte GrowthLoop croissance ou entreprise | Un compte GrowthLoop est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec toutes les autorisations.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Envoyez des listes de clients depuis votre entrepôt de données vers Braze, en ciblant les campagnes d'e-mail et de notification push en un seul clic, et gardez-les toujours synchronisées.

- E-mails basés sur l'activation de l'inscription — envoyez des e-mails pour aider les utilisateurs qui abandonnent votre flux d'inscription et les convertir en utilisateurs actifs.
- E-mails basés sur n'importe quel comportement utilisateur — envoyez des e-mails en fonction du comportement de l'utilisateur, par exemple « Ajouter au panier ».
- E-mails aux clients désabonnés — réengagez les clients désabonnés par e-mail en leur proposant une offre.

## Intégration {#integration}

### Configurer la connexion Braze dans GrowthLoop {#configure-braze-connection-in-growthloop}

Lorsque vous vous connectez à la plateforme de segmentation dans GrowthLoop, accédez à l'onglet **Destinations** dans la barre latérale gauche et cliquez sur **New Destination** dans le coin supérieur droit.

Faites défiler la page jusqu'à trouver Braze, puis cliquez sur **Add Braze**.

Une fenêtre contextuelle s'affiche pour configurer la connexion à la destination.

- **Destination name** : nom qui sera attribué à la destination et utilisé comme référence dans l'application.
- **Sync frequency** : sélectionnez Daily ou Hourly ; cela détermine la fréquence à laquelle GrowthLoop exporte les audiences vers Braze.
- **API key** : clé API créée dans les conditions préalables, avec les autorisations nécessaires.
- **API URL** : URL telle que définie dans les conditions préalables.

Cliquez sur **Create**, et vous pourrez exporter votre première audience vers Braze ! Pour créer une audience dans GrowthLoop, consultez la page [Créer une audience](https://www.growthloop.com/help-center-articles/create-an-audience).

### Après l'exportation {#post-export}

Une fois votre audience exportée, toutes les 15 minutes, GrowthLoop génère une version actualisée de vos listes de clients et l'envoie à Braze.

Simultanément, GrowthLoop supprime de votre audience les utilisateurs qui ne sont plus qualifiés et ajoute les utilisateurs nouvellement qualifiés.

Braze associe les utilisateurs et crée un indicateur signalant qu'ils font partie d'une audience GrowthLoop.

Lorsque vous créez une campagne dans Braze, vous pouvez sélectionner les clients appartenant à cette audience GrowthLoop.

## Résolution des problèmes {#troubleshooting}

Contactez l'équipe GrowthLoop à l'adresse solutions@growthloop.com pour obtenir des informations supplémentaires ou de l'aide.