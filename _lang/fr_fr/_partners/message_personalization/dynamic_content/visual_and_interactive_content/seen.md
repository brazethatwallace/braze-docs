---
nav_title: Seen
article_title: Seen
description: "Seen permet des expériences vidéo personnalisées à grande échelle, aidant les marques à susciter un engagement plus fort tout au long du parcours client."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io) permet aux marques de créer et de proposer des expériences vidéo personnalisées à grande échelle. Avec Seen, vous pouvez concevoir une vidéo autour de vos données, la personnaliser à grande échelle dans le cloud, puis la distribuer là où elle fonctionne le mieux.
>
> Cette intégration envoie les données utilisateur de Braze à Seen, génère des vidéos personnalisées et renvoie les ressources — telles qu'une URL de lecteur unique et une vignette — dans Braze pour les utiliser dans des Campaigns et des Canvas.


## Cas d'utilisation {#use-cases}

Seen prend en charge la distribution automatisée et personnalisée de vidéos tout au long du cycle de vie du client, notamment :

- **Onboarding** : accueillez les nouveaux utilisateurs avec des vidéos personnalisées en fonction de leur profil ou de leur contexte d'inscription.
- **Conversion et activation** : renforcez les actions clés grâce à des messages vidéo contextuels.
- **Fidélisation et vente incitative** : mettez en avant des offres personnalisées ou des jalons d'utilisation.
- **Reconquête et prévention de l'attrition** : réengagez les utilisateurs inactifs avec du contenu vidéo sur mesure.


## Conditions préalables {#prerequisites}

Avant de commencer, assurez-vous de disposer des accès et des données indiqués dans le tableau suivant.

| Prérequis | Description |
|--------------|-------------|
| Accès à la plateforme Seen | Vous avez besoin d'un abonnement à la plateforme Seen avec un projet publié, ou d'une campagne Seen active. Vous devez également accéder à votre projet pour récupérer l'endpoint du projet et générer un jeton API. |
| URL du webhook de Transformation des données Braze | Utilisez la Transformation des données Braze pour reformater les données entrantes de Seen afin qu'elles puissent être acceptées par l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Données utilisateur Braze | La personnalisation des vidéos nécessite des données au niveau de l'utilisateur. Assurez-vous que les attributs pertinents sont disponibles dans Braze et transmettez **`braze_id`** comme identifiant unique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }




## Fonctionnement des projets Seen {#how-seen-projects-work}

Seen utilise l'onglet [Run](https://docs.seen.io/run) d'un projet pour contrôler la manière dont les données entrantes sont traitées et dont les sorties vidéo sont générées.

Un flux de travail de projet :

- Reçoit des données de systèmes externes (tels que Braze)
- Applique des règles de logique et de personnalisation
- Génère une vidéo et des ressources associées
- Renvoie un payload de réponse configurable

L'onglet Run comprend les éléments suivants :

- **Create via API** : ouvre les détails de l'API du projet.
- **Import CSV** : importe manuellement les données de personnalisation (non utilisé dans ce guide).
- **Add webhook** : définit le payload de réponse renvoyé à Braze.
- **View videos** : affiche les vidéos générées et l'état des données entrantes.

Les réponses webhook étant configurables, assurez-vous que les champs de sortie renvoyés par Seen correspondent aux attributs attendus par votre Transformation des données Braze.


## Limite de débit {#rate-limit}

L'API Seen accepte 100 appels toutes les 10 secondes.


## Intégration {#integration}

Dans cet exemple, Braze envoie les données utilisateur à Seen pour générer une vidéo personnalisée. Seen renvoie ensuite une URL de lecteur vidéo unique et une URL de vignette, qui sont stockées en tant qu'[attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) dans Braze pour être utilisées dans l'[envoi de messages]({{site.baseurl}}/user_guide/messaging/).

Si vous avez plusieurs campagnes vidéo avec Seen, répétez ce processus pour chaque campagne.

### Étape 1 : Créer une Campaign webhook pour envoyer des données à Seen {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Créez une nouvelle [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks/) dans Braze.

Configurez le webhook comme suit :

- **URL du webhook** :
  `https://next.seen.io/v1/projects/{PROJECT_ID}/data`
  Trouvez l'endpoint de votre projet dans l'onglet Run de votre projet sur la plateforme Seen.

- **Méthode HTTP** : POST

- **Corps de la requête** : Raw Text
  Utilisez l'exemple suivant comme point de départ. Pour les options de champs et les limites, consultez la [documentation de Seen sur la création de données](https://docs.seen.io/create-data).

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}

- **En-têtes de la requête** :
  - `Authorization` : Bearer `{Seen_API_TOKEN}`
  - `Content-Type` : `application/json`

  Générez un [jeton API](https://docs.seen.io/authorization) dans l'onglet Run de votre projet sur la plateforme Seen. Contactez votre gestionnaire de la satisfaction client Seen si vous avez besoin d'aide.

- Testez le webhook avec un utilisateur dans l'onglet **Test**.
- Après un test réussi, terminez la configuration du webhook.


### Étape 2 : Configurer un projet dans la plateforme Seen {#step-2-configure-a-project-in-the-seen-platform}

Dans votre projet Seen, utilisez l'onglet [Run](https://docs.seen.io/run) pour publier votre vidéo et enregistrer le webhook sortant. Pour un aperçu conceptuel de l'onglet Run, consultez [Fonctionnement des projets Seen](#how-seen-projects-work).

1. Dans la plateforme Seen, créez un projet, construisez votre vidéo, puis sélectionnez **Publish**. Les vidéos commencent à être générées à partir des données entrantes dès que le projet est publié.
2. Dans l'onglet Run, sélectionnez **Add a webhook**.

#### Exigences relatives à la réponse webhook {#webhook-response-requirements}

Le payload de réponse est configurable. Renvoyez les champs du tableau suivant afin que la Transformation des données Braze de l'étape suivante puisse les mapper.

| Champ | Description |
|-------|-------------|
| `id` | Doit correspondre au `braze_id` envoyé depuis Braze |
| `player_url` | URL unique pour le lecteur vidéo personnalisé |
| `email_thumbnail_url` | URL de la vignette vidéo personnalisée |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exigences relatives à la réponse webhook" }

Si vous avez besoin d'attributs supplémentaires, ajoutez-les à la réponse et mappez-les dans Braze.


### Étape 3 : Créer une Transformation des données pour recevoir les données de Seen {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Utilisez les Transformations des données Braze pour traiter la réponse de Seen et stocker les ressources vidéo sur le profil utilisateur.

1. Créez les [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) suivants dans Braze :
   - `player_url`
   - `email_thumbnail_url`

2. Accédez à **Paramètres des données** > **Transformation des données**, puis sélectionnez **Créer une transformation**.

3. Configurez la transformation :
   - **Partir de zéro**
   - **Destination** > POST : Track users

4. Partagez l'URL du webhook généré avec Seen, ou ajoutez-la au **Webhook** dans l'onglet Run de votre projet.

5. Utilisez le code de transformation suivant :

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. Envoyez un payload de test à l'endpoint fourni. Vous pouvez envoyer des données à votre projet sur la plateforme Seen (publiez d'abord le projet), ou envoyer un payload directement à Braze avec [Postman](https://www.postman.com/) ou un outil similaire.
7. Sélectionnez **Validate** pour vérifier que la transformation fonctionne comme prévu.
8. Sélectionnez **Enregistrer** puis **Activer**.