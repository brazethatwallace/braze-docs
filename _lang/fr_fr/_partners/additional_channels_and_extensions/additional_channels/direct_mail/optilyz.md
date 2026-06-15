---
nav_title: optilyz
article_title: optilyz
description: "Cet article de référence décrit le partenariat entre Braze et optilyz, qui vous permet de mener des campagnes de publipostage plus orientées client, durables et rentables."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz](https://optilyz.com) est une plateforme d'automatisation du publipostage qui vous permet de mener des campagnes de publipostage plus orientées client, durables et rentables.

_Cette intégration est maintenue par optilyz._

## À propos de l'intégration {#about-the-integration}

Utilisez l'intégration du webhook optilyz et Braze pour envoyer à vos clients du publipostage, tel que des lettres, des cartes postales et des envois automatiques.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte optilyz | Un compte optilyz est nécessaire pour bénéficier de ce partenariat. |
| Clé API optilyz<br><br>`<OPTILYZ_API_KEY>` | Votre gestionnaire de la satisfaction client optilyz vous fournira votre clé API optilyz.<br><br>Cette clé API vous permettra de connecter vos comptes Braze et optilyz. |
| ID d'automatisation optilyz<br><br>`<OPTILYZ_AUTOMATION_ID>` | L'ID d'automatisation se trouve dans un encadré dans l'en-tête de la page.<br><br>Une fois connecté à optilyz, vous pouvez accéder à l'automatisation vers laquelle vous souhaitez envoyer des données.<br>L'automatisation doit d'abord être activée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Gérer le publipostage comme un canal numérique implique d'abandonner les envois de masse et de tirer parti de ce canal dans le cadre de vos parcours clients (numériques). Les avantages d'une approche moderne du publipostage sont les suivants :
- Meilleurs taux de conversion grâce à une pertinence accrue, des cas d'utilisation supplémentaires, des tests A/B simplifiés et des effets cross-canal
- Effort réduit grâce à l'automatisation et à une solution de bout en bout
- Réduction des coûts grâce à des contrats-cadres et à la transparence des coûts

## Intégration {#integration}

Pour intégrer optilyz, utilisez l'[API optilyz](https://www.optilyz.com/doc/api/) pour envoyer les données du destinataire au webhook Braze.

### Étape 1 : Créer votre modèle de webhook Braze {#step-1-create-your-braze-webhook-template}

Pour créer un modèle de webhook optilyz à utiliser dans de futures Campaigns ou Canvas, accédez à **Contenu** > **Webhook** dans la plateforme Braze. Sélectionnez ensuite **Créer un modèle de webhook**.

Si vous souhaitez créer une Campaign webhook optilyz unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle Campaign.

Dans votre nouveau modèle de webhook, renseignez les champs suivants :
- **URL du webhook** : l'URL du webhook est unique pour chaque client et votre gestionnaire de la satisfaction client optilyz vous la fournira.
- **Corps de la requête** : Raw Text

#### En-têtes et méthode de la requête {#request-headers-and-method}

optilyz nécessite également un en-tête HTTP pour l'autorisation et une méthode HTTP. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres**, vous devez remplacer `<OPTILYZ_API_KEY>` par votre clé API optilyz. Cette clé doit inclure un « : » juste après la clé et être encodée en base 64.

- **Méthode HTTP** : POST
- **En-têtes de la requête** :
  - **Authorization** : {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type** : application/json

![Les en-têtes de requête et la méthode HTTP affichés dans le générateur de webhook Braze.]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### Corps de la requête {#request-body}

Dans le corps de requête suivant, vous pouvez utiliser n'importe quelle balise de personnalisation Liquid et créer un modèle de requête personnalisé conformément à la [documentation de l'API](https://www.optilyz.com/doc/api/) d'optilyz.

Le champ `variation` est facultatif et permet de définir quelle conception au sein de l'automatisation doit être utilisée. Si une variation est omise, optilyz attribuera l'une des variations définies de manière aléatoire.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Une image du code du corps de la requête et de l'URL du webhook affichés dans l'onglet de composition du générateur de webhooks Braze.]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### Étape 2 : Prévisualiser votre requête {#step-2-preview-your-request}

Ensuite, prévisualisez votre requête dans le panneau **Prévisualisation** ou accédez à l'onglet **Test**, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook. N'oubliez pas d'enregistrer votre modèle avant de quitter la page !

![Différents champs de test disponibles dans l'onglet de test du générateur de webhooks Braze.]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}