---
nav_title: NiftyImages
article_title: NiftyImages
description: "Découvrez comment connecter NiftyImages à Braze pour créer des visuels dynamiques personnalisés, synchroniser les propriétés de contact et publier des ressources sous forme de Content Blocks réutilisables."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com) aide les clients Braze à créer du contenu visuel personnalisé et en temps réel pour les e-mails, le mobile et les messages in-app. En connectant les données clients, produits et métier en temps réel à des images et contenus dynamiques, les marques peuvent offrir des expériences pertinentes et opportunes telles que des comptes à rebours, des recommandations personnalisées, des messages localisés, des mises à jour de stock et des offres promotionnelles qui stimulent l'engagement et les conversions.

_Cette intégration est maintenue par NiftyImages._

## À propos de l'intégration {#about-the-integration}

L'intégration NiftyImages pour Braze vous aide à créer des visuels dynamiques et personnalisés à partir des données de contact Braze. Les équipes peuvent créer des ressources telles que des images personnalisées, des comptes à rebours, des cartes, des calendriers, des visuels de fidélité et bien plus encore, puis les publier sous forme de [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) Braze réutilisables pour les utiliser dans les Campaigns et les Canvas. Cela fait gagner du temps, réduit les erreurs et simplifie la gestion du contenu personnalisé.

## Cas d'utilisation {#use-cases}

Vous pouvez utiliser NiftyImages pour :

- **Personnaliser des images :** Créez des images qui incluent le nom de chaque client, son statut de fidélité, son solde de récompenses, sa localisation, ses préférences produit, son niveau d'adhésion, les détails de son compte ou d'autres propriétés de contact Braze.
- **Ajouter des comptes à rebours :** Ajoutez des comptes à rebours en temps réel pour les soldes, les lancements de produits, les événements, les offres à durée limitée, les rendez-vous, les échéances d'onboarding et les dates d'expiration personnalisées.
- **Afficher des cartes dynamiques :** Affichez le magasin le plus proche, le lieu d'un événement, la zone de service, le concessionnaire, le club, l'agence ou le point de retrait en fonction des données de localisation du client ou des propriétés de contact Braze.
- **Afficher des calendriers :** Affichez des dates personnalisées, des événements, des rendez-vous, des périodes de renouvellement, des moments de campagne ou des jalons client directement dans les visuels de campagne.
- **Lancer des sondages en direct or en ligne/en production/instantané :** Ajoutez des sondages interactifs aux Campaigns et affichez les résultats mis à jour en temps réel après le vote des clients.
- **Créer des cartes à gratter :** Créez des expériences ludiques de cartes à gratter qui révèlent une récompense personnalisée, une remise, une offre, une image ou un message.
- **Visualiser les données de fidélité :** Transformez les données client en barres de progression, résumés de compte, visuels de fidélité, graphiques et diagrammes personnalisés pour chaque destinataire.
- **Appliquer du contenu basé sur des règles :** Affichez différents visuels en fonction de l'heure, de la localisation, de l'appareil, des données client, du segment d'audience ou de la logique de campagne.
- **Réutiliser du contenu dynamique :** Publiez les ressources NiftyImages finalisées dans les Content Blocks Braze afin que les équipes puissent les réutiliser dans les e-mails marketing, les modèles, les Campaigns et les ressources de marque partagées.

## Conditions préalables {#prerequisites}

Avant de commencer, vérifiez que vous disposez des éléments suivants :

| Prérequis | Description |
| ------------ | ----------- |
| Compte NiftyImages | Un [compte NiftyImages](https://niftyimages.com/Signup) est requis pour créer et gérer des images personnalisées, des comptes à rebours, des cartes, des calendriers, des cartes à gratter, des graphiques et d'autres visuels dynamiques. |
| Compte Braze | Un compte Braze est requis pour utiliser NiftyImages dans les Campaigns Braze, les Canvas, les modèles d'e-mail et les canaux de communication. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `custom_attributes.get` et `content_blocks.create`.<br><br>Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Connectez votre compte Braze dans NiftyImages pour synchroniser les propriétés de contact et publier des ressources dans les Content Blocks Braze.

### Étape 1 : Ouvrir les intégrations dans NiftyImages {#step-1-open-integrations-in-niftyimages}

1. Dans NiftyImages, accédez à **Settings** > **Integrations**.
2. Sélectionnez **Braze**.
3. Sélectionnez **Connect Braze**.

### Étape 2 : Créer votre clé API REST Braze {#step-2-create-your-braze-rest-api-key}

1. Dans Braze, accédez à **Paramètres** > **Clés API**.
2. Créez ou sélectionnez une clé API REST pour l'intégration NiftyImages.
3. Sous **Custom Attributes**, sélectionnez `custom_attributes.get`.
4. Sous **Content Blocks**, sélectionnez `content_blocks.create`.
5. Enregistrez la clé API, puis copiez la clé API REST et votre [endpoint REST]({{site.baseurl}}/api/basics#endpoints).

### Étape 3 : Connecter votre compte Braze dans NiftyImages {#step-3-connect-your-braze-account-in-niftyimages}

1. Retournez à l'écran d'intégration Braze dans NiftyImages.
2. Collez la clé API REST Braze.
3. Saisissez votre endpoint REST Braze.
4. Confirmez la connexion.
5. Vérifiez que votre compte Braze apparaît sous **Connected Braze accounts** avec un statut **Active** ou **Connected**.

Vous pouvez connecter plusieurs comptes Braze si nécessaire, ce qui est utile pour les agences, les équipes multi-marques ou les organisations gérant plusieurs instances Braze.

## Personnaliser les ressources dans NiftyImages {#customize-assets-in-niftyimages}

Après avoir connecté Braze, utilisez la synchronisation des variables de contact et la publication dans les Content Blocks pour gérer vos visuels personnalisés.

### Utiliser la synchronisation des variables de contact {#use-contact-variable-sync}

La synchronisation des variables de contact vous permet d'utiliser les propriétés de contact Braze existantes directement dans NiftyImages sans avoir à saisir ou recréer manuellement les balises de fusion.

1. Créez ou modifiez une image personnalisée ou une autre ressource NiftyImages.
2. Ouvrez le sélecteur de balises de fusion ou de personnalisation.
3. Sélectionnez **Pick from connected integrations**, puis choisissez les propriétés Braze que vous souhaitez utiliser.
4. Ajoutez ces valeurs aux calques de texte, d'image, de compte à rebours, de carte, de graphique, de calendrier ou de contenu dynamique.
5. Enregistrez l'image.

Les images enregistrées qui utilisent des variables Braze incluent automatiquement ces valeurs de personnalisation dans l'URL de l'image NiftyImages.

### Publier dans les Content Blocks Braze {#publish-to-braze-content-blocks}

1. Finalisez votre ressource NiftyImages.
2. Sélectionnez **Send to Braze**.

## Utiliser NiftyImages dans Braze {#use-niftyimages-in-braze}

Utilisez les Content Blocks publiés dans les modèles d'e-mail, les Campaigns et les Canvas Braze.

### Ajouter une ressource NiftyImages à un e-mail Braze {#add-a-niftyimages-asset-to-a-braze-email}

1. Ouvrez un modèle d'e-mail, une Campaign ou un message e-mail Canvas dans Braze.
2. Dans l'éditeur de message, ouvrez le menu de personnalisation et sélectionnez **Content Blocks** comme type de personnalisation.
3. Sélectionnez le Content Block NiftyImages que vous avez publié depuis NiftyImages.

### Réutiliser les ressources NiftyImages dans Braze {#reuse-niftyimages-assets-across-braze}

1. Utilisez le Content Block publié dans les e-mails marketing, les modèles d'e-mail, les Campaigns, les ressources de marque partagées et les flux automatisés.
2. Lorsqu'une ressource NiftyImages utilise des variables dynamiques, Braze transmet les valeurs de contact en fonction du message et du canal.
3. Mettez à jour la ressource source dans NiftyImages lorsque vous avez besoin de modifications créatives.

### Déconnecter un compte Braze {#disconnect-a-braze-account}

1. Retournez dans **Settings** > **Integrations** dans NiftyImages.
2. Ouvrez la page de connexion Braze.
3. Sélectionnez l'icône de suppression ou de déconnexion pour le compte que vous souhaitez retirer.
4. Confirmez la déconnexion.

## Considérations {#considerations}

- **Autorisations de l'API REST :** La clé API REST Braze doit inclure `custom_attributes.get` pour la synchronisation des propriétés de contact et `content_blocks.create` pour la publication de ressources dans les Content Blocks Braze.
- **Disponibilité des propriétés de contact :** Seules les propriétés de contact disponibles pour le compte Braze connecté peuvent être synchronisées dans NiftyImages.
- **Valeurs de repli :** Utilisez des valeurs de repli lors de la création de visuels personnalisés afin que chaque client voie une image soignée même lorsqu'une propriété de contact est manquante.
- **Content Blocks réutilisables :** La publication dans les Content Blocks Braze aide les équipes à éviter le copier-coller manuel de HTML, à réduire les erreurs de balises de fusion et à réutiliser les ressources dans les Campaigns et les modèles.
- **Comptes Braze multiples :** NiftyImages prend en charge plusieurs comptes Braze connectés, ce qui est utile pour les agences, les équipes multi-marques et les équipes gérant plusieurs instances Braze.
- **Tests :** Testez le message Braze final avec des profils clients d'exemple avant de lancer une Campaign ou un Canvas.

## Résolution des problèmes {#troubleshooting}

Consultez le tableau suivant si vous rencontrez des problèmes avec l'intégration NiftyImages.

| Problème | Résolution |
| ----- | ---------- |
| Le compte Braze ne se connecte pas | Vérifiez que la clé API REST est valide, que l'endpoint REST est correct et que la clé inclut les autorisations requises. |
| Les propriétés de contact Braze n'apparaissent pas dans NiftyImages | Vérifiez que la clé API inclut `custom_attributes.get`. Ensuite, actualisez la connexion Braze dans NiftyImages. |
| La ressource ne se publie pas dans les Content Blocks Braze | Vérifiez que la clé API inclut `content_blocks.create` et que le compte Braze connecté autorise la création de Content Blocks. |
| La personnalisation ne s'affiche pas correctement | Vérifiez que la propriété de contact Braze sélectionnée contient une valeur pour l'utilisateur test. Ajoutez des valeurs de repli dans NiftyImages si nécessaire. |
| L'image ne s'affiche pas dans Braze | Vérifiez que la ressource NiftyImages est enregistrée, active et publiée correctement. Envoyez un message de test Braze pour vérifier l'image dans le canal prévu. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }