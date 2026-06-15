---
nav_title: Oppizi
article_title: Oppizi
alias: /partners/oppizi/
description: "Cet article de référence présente le partenariat entre Braze et Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) est le leader mondial du marketing hors ligne, offrant aux entreprises une solution unique pour mener des campagnes de publipostage et de distribution de flyers mesurables et ciblées.

_Cette intégration est maintenue par Oppizi._

## Conditions préalables {#prerequisites}

| Condition | Description |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Compte Oppizi | Un compte Oppizi actif est nécessaire pour utiliser cette intégration. |
| Clé API Oppizi | Disponible dans votre compte Oppizi sous **Integrations** > **Braze**. |
| ID de flux de travail de publipostage Oppizi | Créez un flux de travail dans Oppizi sur la page **Direct Mail Workflow** pour obtenir un ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Cas d'utilisation {#use-cases}

Avec l'intégration d'Oppizi, vous pouvez :

* **Envoyer des cartes postales automatisées** de publipostage à l'aide de déclencheurs Braze connectés au webhook et aux flux de travail de publipostage d'Oppizi.
* **Configurer des seuils, des vagues et des limites** dans les flux de publipostage d'Oppizi pour contrôler l'envoi de vos campagnes.
* **Créer des cartes postales professionnelles** avec l'outil de conception intégré d'Oppizi — aucune expérience en conception n'est requise.
* **Suivre les performances de votre campagne** en temps réel grâce au tableau de bord d'Oppizi.

## Intégration {#integration}

### Étape 1 : Générer votre clé API Oppizi {#step-1-generate-your-oppizi-api-key}

Pour utiliser votre modèle de webhook dans Braze, vous devrez d'abord générer votre clé API Oppizi.

1. Connectez-vous à Oppizi.
2. Allez dans **Integrations** > **Braze**.
3. Générez votre clé API.

Vous pouvez gérer, révoquer et créer vos clés à partir de cette page si nécessaire.

### Étape 2 : Créer un modèle de webhook Braze {#step-2-create-a-braze-webhook-template}

Ensuite, créez un modèle de webhook pour Oppizi dans Braze afin de l'utiliser dans vos futures campagnes ou Canvas :

1. Dans Braze, allez dans **Contenu** > **Webhook**.
2. Sélectionnez **Créer un modèle de webhook**.
3. Donnez un nom à votre modèle.
4. Dans votre modèle de webhook, remplissez les champs suivants :

- **Webhook URL :** `https://webhooks.oppizi.com/events`
- **Request Body :** **Raw Text**

Pour la méthode de requête et les en-têtes, Oppizi exige qu'une méthode HTTP et les en-têtes HTTP suivants soient inclus dans le modèle. Remplissez les champs suivants :

- **HTTP Method :** POST
- **Request Headers :**
  - **Authorization :** `Bearer <oppiziAPIKey>`
  - **Content-Type :** `application/json`

![Exemple d'en-tête du webhook Oppizi dans Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

Pour le **corps de la requête**, vous devez inclure le champ **oppiziWorkflowID**. Cet ID est généré lors de la création d'un flux de travail dans Oppizi et est nécessaire pour spécifier à quel flux de travail de publipostage vos destinataires doivent être ajoutés. Chaque flux de publipostage dans Oppizi possède un ID unique. Si vous créez un modèle de webhook Oppizi dans Braze, veillez donc à toujours mettre à jour l'ID du flux de travail avec la valeur correcte.

{% alert note %}
Vérifiez que les attributs personnalisés requis sont configurés dans votre compte Braze pour les adresses postales de vos destinataires, car ils sont nécessaires pour l'envoi de publipostage.
{% endalert %}

![Exemple de modèle de webhook Oppizi dans Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

Voici un exemple de corps de requête :

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Étape 3 : Créer un flux de travail de publipostage dans Oppizi {#step-3-create-a-direct-mail-workflow-in-oppizi}

1. Dans Oppizi, allez dans **Direct Mail Workflow** > **Create workflow**.
2. Configurez les détails du flux de travail, y compris les seuils, les vagues, le format des cartes postales et les illustrations.
3. Dans la section des détails du webhook, vous trouverez un corps de requête prêt à l'emploi, comprenant votre ID de flux de travail, que vous pouvez coller directement dans Braze.

### Étape 4 : Prévisualiser et tester votre requête dans Braze {#step-4-preview-and-test-your-request-in-braze}

Après avoir ajouté le corps de votre requête avec l'ID du flux de travail d'Oppizi, exécutez un test pour confirmer que votre configuration fonctionne comme prévu.

Pour exécuter le test, mettez à jour `requestType` de `live` à `test` dans le corps de la requête. Cette étape est cruciale pour éviter d'ajouter des destinataires de test à votre audience de publipostage.

Une fois les tests terminés, remettez `requestType` à `live` et enregistrez votre Canvas. Vous êtes maintenant prêt à lancer vos campagnes de publipostage automatisées.