---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et MyPostcard, qui vous permet d'utiliser le publipostage comme canal supplémentaire pour votre flux de travail CRM."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com), une application mondiale de cartes postales de premier plan, vous permet d'exécuter des campagnes de publipostage en toute simplicité, offrant un moyen fluide et rentable d'entrer en contact avec vos clients.

Utilisez l'intégration de MyPostcard et de Braze pour envoyer sans effort des mailings imprimés à vos clients.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte MyPostcard B2B | L'inscription à MyPostcard est nécessaire pour profiter de cette intégration. |
| Clé API B2B et identifiants | Vous trouverez votre clé API et vos identifiants dans l'outil d'administration MyPostcard B2B. |
| Campaign MyPostcard B2B approuvée | Pour profiter de cette intégration, vous devez configurer une campagne de publipostage dans l'outil MyPostcard B2B. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Cas d'utilisation {#use-cases}

Pour améliorer vos campagnes de publipostage, il est essentiel d'aller au-delà des envois de masse traditionnels et d'intégrer le courrier imprimé de façon fluide dans vos flux de travail. Cette approche vous permet d'atteindre des clients spécifiques qui se sont désabonnés de vos newsletters par e-mail ou dont les e-mails sont marqués comme spam. Avec MyPostcard, vous pouvez envoyer sans effort des campagnes de publipostage directement via Braze.

- Créez des flux de travail intuitifs dans Braze, en intégrant le courrier imprimé comme un nouveau canal puissant, sans aucune expertise technique.
- Libérez le potentiel des mailings imprimés personnalisés en quelques étapes simples.
- Bénéficiez d'une mise en œuvre simple, accompagnée d'une assistance personnalisée de la part d'une équipe dédiée.

## Intégration {#integration}

Pour intégrer MyPostcard, [connectez-vous ou inscrivez-vous](https://www.mypostcard.com/b2b/admin/) et créez votre première campagne pour l'utiliser via les [webhooks de Braze]({{site.baseurl}}/user_guide/channels/webhooks/).

### Étape 1 : Créer votre modèle de webhook Braze {#step-1-create-your-braze-webhook-template}

Pour créer un modèle de webhook MyPostcard à utiliser dans de futures Campaigns ou Canvas, accédez à **Contenu** > **Webhook** dans la plateforme Braze. Sélectionnez ensuite **Créer un modèle de webhook**.

Si vous souhaitez créer une Campaign webhook MyPostcard ponctuelle ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle Campaign. Remplissez les champs suivants :

| Champ | Description |
|---|---|
| **Webhook URL** | L'URL du webhook telle qu'elle apparaît dans l'outil d'administration B2B. |
| **Request Body** | Texte brut (format JSON disponible dans l'outil d'administration B2B). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create your Braze webhook template" }

#### Méthode de requête et en-têtes {#request-method-and-headers}

MyPostcard exige qu'une méthode HTTP ainsi que les en-têtes HTTP suivants soient inclus dans le modèle.

{% raw %}
<table aria-label="Request method and headers">
  <caption>Méthode de requête et en-têtes</caption>
  <thead>
    <tr>
      <th><strong>Champ</strong></th>
      <th><strong>Détails</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTP Method</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Username</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Password</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request method and headers" }

#### Corps de la requête {#request-body}

Copiez le corps de la requête affiché dans l'outil d'administration B2B, puis remplissez les marques substitutives avec du contenu en utilisant les balises de personnalisation Liquid.

![Onglet Rédiger affichant le corps JSON et les informations relatives au webhook.]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### Étape 2 : Prévisualiser votre requête {#step-2-preview-your-request}

Ensuite, prévisualisez votre requête dans le panneau **Prévisualisation** ou accédez à l'onglet **Test**, où vous pouvez choisir un utilisateur aléatoire, un utilisateur existant ou créer un utilisateur personnalisé pour tester votre webhook. N'oubliez pas d'enregistrer votre modèle avant de quitter la page !

![Onglet Test du webhook avec différents champs pour valider la mise en œuvre.]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [Campaign webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}