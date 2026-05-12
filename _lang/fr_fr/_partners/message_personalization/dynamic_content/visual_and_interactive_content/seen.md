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
> L'intégration entre Braze et Seen vous permet d'envoyer les données des utilisateurs de Braze à Seen, de générer dynamiquement des vidéos personnalisées et de renvoyer les ressources vidéo — telles qu'une URL de lecteur unique et une vignette — dans Braze pour les utiliser dans des Campaigns et des Canvas.


## Cas d'utilisation {#use-cases}

Seen prend en charge la distribution automatisée et personnalisée de vidéos tout au long du cycle de vie du client, notamment :

- **Onboarding** : accueillez les nouveaux utilisateurs avec des vidéos personnalisées en fonction de leur profil ou de leur contexte d'inscription.
- **Conversion et activation** : renforcez les actions clés grâce à des messages vidéo contextuels.
- **Fidélisation et vente incitative** : mettez en avant des offres personnalisées ou des jalons d'utilisation.
- **Reconquête et prévention de l'attrition** : réengagez les utilisateurs inactifs avec du contenu vidéo sur mesure.


## Conditions préalables {#prerequisites}

Avant de commencer, vous devez disposer des éléments suivants :

| Prérequis | Description |
|--------------|-------------|
| Accès à la plateforme Seen | Vous avez besoin d'un abonnement à la plateforme Seen ou d'une Campaign Seen active. Vous devez accéder aux paramètres de votre espace de travail pour récupérer votre ID d'espace de travail et générer un jeton API. |
| URL du webhook de Transformation des données Braze | La Transformation des données de Braze reformate les données entrantes de Seen afin qu'elles puissent être acceptées par l'endpoint /users/track de Braze. |
| Données utilisateur Braze | La personnalisation des vidéos nécessite des données au niveau de l'utilisateur. Assurez-vous que les attributs pertinents sont disponibles dans Braze et que vous transmettez **braze_id** comme identifiant unique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }




## Fonctionnement des Seen Journeys {#how-seen-journeys-work}

Seen utilise les [Journeys](https://docs.seen.io/journey) pour contrôler la manière dont les données entrantes sont traitées et dont les sorties vidéo sont générées.

Un Journey est un flux de travail configurable qui :
- reçoit des données de systèmes externes (tels que Braze)
- applique des règles de logique et de personnalisation
- génère une vidéo et des ressources associées
- renvoie un payload de réponse configurable

Les Journeys sont composés de **nœuds**, chacun ayant une fonction spécifique :

- **Nœud déclencheur** : définit comment et quand un Journey démarre (pour les intégrations Braze, utilisez un déclencheur `On Create`)
- **Nœud conditionnel** : achemine les utilisateurs vers différents chemins logiques en fonction des valeurs des données
- **Nœud projet** : applique une personnalisation dynamique de la vidéo en utilisant les données entrantes
- **Nœud lecteur** : génère une URL unique pour le lecteur vidéo
- **Nœud webhook** : définit le payload de réponse renvoyé à Braze

Les réponses de Journey étant configurables, assurez-vous que les champs de sortie renvoyés par Seen correspondent aux attributs attendus par votre Transformation des données Braze.


## Limite de débit {#rate-limit}
L'API Seen accepte jusqu'à 100 appels toutes les 10 secondes.


## Intégration {#integration}

Dans cet exemple, Braze envoie les données de l'utilisateur à Seen pour générer une vidéo personnalisée. Seen renvoie ensuite une URL de lecteur vidéo unique et une URL de vignette, qui sont stockées en tant qu'attributs personnalisés dans Braze pour être utilisées dans l'envoi de messages.

Si vous avez plusieurs campagnes vidéo avec Seen, répétez le processus pour connecter Braze à toutes les campagnes vidéo.

### Étape 1 : Créer une Campaign webhook pour envoyer des données à Seen {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Créez une nouvelle [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks/) dans Braze.

Configurez le webhook comme suit :

- **URL du webhook** :
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`
  Trouvez votre ID d'espace de travail dans les paramètres de la plateforme Seen.

- **Méthode HTTP** : POST
- **Corps de la requête** : Raw Text
  Utilisez l'exemple suivant comme point de départ. Pour plus d'informations, consultez la [documentation de Seen sur la création de données](https://docs.seen.io/create-data).

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

  > Générez un [jeton API](https://docs.seen.io/authorization) dans la plateforme Seen sous les paramètres de l'espace de travail. Vous pouvez contacter votre gestionnaire de la satisfaction client Seen pour obtenir de l'aide.

- Pour tester le webhook avec un utilisateur, passez à l'onglet **Test**.
- Après avoir confirmé que le test fonctionne comme prévu, terminez la configuration du webhook.


### Étape 2 : Configurer un Journey dans la plateforme Seen {#step-2-configure-a-journey-in-the-seen-platform}

Seen utilise les [Journeys](https://docs.seen.io/journey) pour définir comment les données entrantes sont traitées, personnalisées et renvoyées à Braze.
Chaque Journey est un flux de travail configurable composé de nœuds qui vous permettent de contrôler à la fois la logique de génération de la vidéo et le payload de réponse.

Pour configurer votre Journey :

1. Créez un nouveau Journey dans la plateforme Seen.
2. Ajoutez un **nœud déclencheur** et sélectionnez le déclencheur `On Create`.
   Cela garantit que le Journey démarre lorsque Braze envoie des données à Seen. Créez et ajoutez toute logique de [segmentation](https://docs.seen.io/segments) dans votre espace de travail si nécessaire.
3. Construisez votre logique en utilisant les nœuds suivants selon vos besoins :
   - **Nœud conditionnel** : acheminer les utilisateurs en fonction des valeurs des attributs (par exemple, le type de forfait ou la région)
   - **Nœud projet** : appliquer la personnalisation dynamique des vidéos en utilisant les données entrantes
   - **Nœud lecteur** : générer une URL unique pour le lecteur vidéo
4. Ajoutez un **nœud webhook** pour définir la réponse renvoyée à Braze.

#### Exigences relatives à la réponse du nœud webhook {#webhook-node-response-requirements}

Le payload de réponse étant configurable, assurez-vous que les champs suivants sont renvoyés pour prendre en charge la Transformation des données Braze décrite à l'étape suivante :

| Champ | Description |
|------|-------------|
| `id` | Doit correspondre au `braze_id` envoyé depuis Braze |
| `player_url` | URL unique pour le lecteur vidéo personnalisé |
| `email_thumbnail_url` | URL de la vignette vidéo générée |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exigences relatives à la réponse du nœud webhook" }

Si votre cas d'utilisation nécessite des attributs supplémentaires, incluez-les dans la réponse et mappez-les dans Braze.


### Étape 3 : Créer une Transformation des données pour recevoir les données de Seen {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Utilisez les Transformations des données Braze pour ingérer la réponse du Journey Seen et stocker les ressources vidéo sur le profil utilisateur.

1. Créez les [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) suivants dans Braze :
   - `player_url`
   - `email_thumbnail_url`
2. Accédez à **Paramètres des données** → **Transformation des données** et cliquez sur **Créer une transformation**.
3. Configurez la transformation :
   - **Partir de zéro**
   - **Destination** → POST : Track users
4. Partagez l'URL du webhook généré avec Seen, ou ajoutez-la directement au **nœud webhook** du Journey.
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
6. Envoyez un payload de test à l'endpoint fourni. Envoyez des données à la plateforme Seen pour exécuter votre Journey, ou envoyez le payload directement à Braze avec [Postman](https://www.postman.com/) ou un autre service similaire.
7. Sélectionnez **Validate** pour vous assurer que tout fonctionne comme prévu.
8. Sélectionnez **Enregistrer** puis **Activer**.