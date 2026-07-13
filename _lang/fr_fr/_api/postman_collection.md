---
nav_title: Postman et demandes d'exemples
article_title: Postman et demandes d'exemples
page_order: 3
description: "Cet article de référence couvre la collection Braze Postman, ce qu'elle est, comment la configurer et l'utiliser, ainsi que la façon de modifier et d'envoyer des requêtes."
page_type: reference

---

# Postman et demandes d'exemples {#postman-and-sample-requests}

> Braze vous permet de générer des exemples de requêtes API pour tous nos endpoints grâce à notre collection Postman. Cet article de référence couvre la collection Braze Postman, ce qu'elle est, comment la configurer et l'utiliser, ainsi que la façon de modifier et d'envoyer des requêtes.

## Qu'est-ce que Postman ? {#what-is-postman}

Postman est un outil d'édition visuelle gratuit permettant de créer et de tester des requêtes API. Par rapport à d'autres méthodes (par exemple, l'utilisation de cURL), Postman vous permet de modifier les requêtes API, d'afficher les informations d'en-tête, et bien plus encore. Vous pouvez enregistrer des collections (bibliothèques d'exemples de requêtes API préétablies). Pour accélérer la configuration avec notre REST API, nous fournissons une collection avec des exemples préétablis pour tous les endpoints.

Consultez ou téléchargez notre collection Postman en cliquant sur **Run in Postman** dans notre [documentation Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) pour commencer.

## Utilisation de la collection Braze Postman {#using-the-braze-postman-collection}

Si vous disposez d'un compte Postman (vous pouvez télécharger les versions macOS, Windows et Linux depuis le [site web de Postman](https://www.getpostman.com)), vous pouvez ouvrir notre documentation Postman dans votre propre application Postman en cliquant sur le bouton orange **Run in Postman**. Vous pouvez ensuite [créer un environnement](#setting-up-your-postman-environment), ou utiliser notre environnement REST API de Braze comme modèle, et modifier les requêtes `POST` et `GET` disponibles pour répondre à vos propres besoins.

### Configuration de votre environnement Postman {#setting-up-your-postman-environment}

{% raw %}
La collection Braze Postman utilise une variable de modèle, `{{instance_url}}`, pour remplacer l'URL de REST API de votre instance Braze dans les requêtes prédéfinies, et la variable `{{api_key}}` pour votre clé API. Au lieu de devoir modifier manuellement toutes les requêtes de la collection, vous pouvez configurer cette variable dans votre environnement Postman. Vous pouvez sélectionner notre environnement modèle (Braze REST API Environment Template) dans la liste déroulante, puis remplacer les valeurs des variables par les vôtres, ou créer votre propre environnement.
{% endraw %}

Pour créer votre propre environnement, procédez comme suit :

1. Dans l'onglet **Workspaces**, sélectionnez **Environments**.
2. Cliquez sur le bouton **+** plus pour créer un nouvel environnement.
3. Donnez un nom à cet environnement (par exemple, « Braze API Requests ») et ajoutez des clés pour `instance_url` et `api_key` avec des valeurs correspondant à votre [instance Braze]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) et à votre [clé REST API de Braze]({{site.baseurl}}/api/api_key).
4. Cliquez sur **Save**.

{% alert note %}
Dans les corps de requête `POST`, la `api_key` doit être encadrée par des guillemets : `"MY-API-KEY-EXAMPLE"`. Dans les URL `GET`, elle ne doit pas l'être. Nous avons déjà fourni ce formatage pour les corps de requête `POST`, les URL `GET` et le modèle d'environnement pour `YOUR-API-KEY-HERE` dans cette documentation.
{% endalert %}

![Ajout de variables pour la clé API et l'URL d'instance à l'environnement REST API de Braze dans Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Utiliser les requêtes prédéfinies de la collection {#using-the-pre-built-requests-from-the-collection}

Après avoir configuré votre environnement, vous pouvez utiliser l'une des requêtes prédéfinies de la collection comme modèle pour créer de nouvelles requêtes API. Pour commencer à utiliser l'une des requêtes prédéfinies, cliquez dessus dans le menu **Collections** de Postman. Cela ouvrira la requête sous forme de nouvel onglet dans la fenêtre principale de l'application Postman.

En général, il existe deux types de requêtes que les endpoints API de Braze acceptent : `GET` et `POST`. Selon la méthode `HTTP` utilisée par l'endpoint, vous devrez modifier la requête prédéfinie différemment.

#### Modifier une requête POST {#edit-a-post-request}

Lorsque vous modifiez une requête `POST`, ouvrez la requête et accédez à la section **Body** dans l'éditeur de requête. Pour une meilleure lisibilité, sélectionnez le bouton radio **raw** pour formater le corps de la requête `JSON`.

![Onglet Body lors de la modification d'une requête POST User Track dans Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Modifier une requête GET {#edit-a-get-request}

Lorsque vous modifiez une requête `GET`, modifiez les paramètres transmis dans l'URL de la requête. Pour ce faire, sélectionnez l'onglet **Params** et modifiez les paires clé-valeur dans les champs qui apparaissent.

![Onglet Params lors de la modification d'une requête GET de liste des adresses e-mail désabonnées dans Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Envoyer votre requête {#send-your-request}

Lorsque votre requête API est prête, cliquez sur **Send**. La requête est envoyée et les données de réponse s'affichent dans une section sous l'éditeur de requête. À partir de là, vous pouvez consulter les données brutes renvoyées par l'API de Braze, voir le code de réponse HTTP, vérifier le temps de traitement de la requête et afficher les informations d'en-tête.

![Exemple de données de réponse d'une requête POST avec un statut 201 Created et un temps de réponse de 269 millisecondes.]({% image_buster /assets/img_archive/postman_response.png %})