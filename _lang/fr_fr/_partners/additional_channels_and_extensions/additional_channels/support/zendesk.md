---
nav_title: Zendesk
article_title: Zendesk
description: "Cet article de référence présente le partenariat entre Braze et Zendesk, une suite d'assistance populaire qui vous permet d'utiliser les webhooks Braze pour synchroniser les données d'assistance entre les deux plateformes."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) permet aux entreprises d'avoir des conversations naturelles avec leurs clients grâce à un support omnicanal utilisant l'e-mail, le chat web, la voix ou les applications de messagerie de réseaux sociaux. Zendesk offre un système de gestion des tickets simplifié qui valorise le suivi et la hiérarchisation des interactions, permettant ainsi aux entreprises d'avoir une vue historique unifiée de leurs clients.

L'intégration serveur à serveur entre Braze et Zendesk vous permet d'utiliser :
- Les webhooks Braze pour automatiser la création de tickets d'assistance dans Zendesk suite à l'engagement des messages dans les parcours utilisateurs de Braze. Par exemple, après avoir mis en œuvre et testé avec succès une intégration, Braze peut créer un ticket d'assistance lorsqu'un utilisateur répond négativement à un message in-app « Vous appréciez notre application ? », ce qui permet à votre équipe d'assistance d'assurer le suivi avec le client.
- Les webhooks Zendesk pour prendre en charge les cas d'usage bidirectionnels comme la mise à jour du profil utilisateur dans Braze suite à une activité dans Zendesk. Par exemple, après la résolution d'un ticket, consignez un événement dans le profil de l'utilisateur dans Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Zendesk | Un [compte administrateur Zendesk](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) est nécessaire pour profiter de ce partenariat. |
| Jeton API Zendesk | Un [jeton API](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\) Zendesk est nécessaire pour envoyer des requêtes depuis Braze vers l'endpoint de ticket Zendesk. |
| Identifiant commun (recommandé) | Il est recommandé d'utiliser un [identifiant commun](#common-identifier) entre Braze et Zendesk. |
| Clé API Braze | Une clé API Braze est nécessaire pour envoyer des requêtes depuis Zendesk vers un endpoint Braze. Assurez-vous que la clé API que vous utilisez dispose des autorisations correctes pour l'endpoint Braze que votre webhook Zendesk utilise. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de Braze à Zendesk {#braze-to-zendesk-integration}

### Étape 1 : Créer votre webhook Braze {#step-1-create-your-braze-webhook}

Pour créer un webhook :

- **Campaigns :** Accédez à la page **Campaigns** dans le tableau de bord de Braze. Cliquez sur **Create Campaign** et sélectionnez **Webhook**.
- **Canvas :** À partir d'un Canvas nouveau ou existant, créez une étape complète ou une étape de message dans le générateur de Canvas. Ensuite, cliquez sur **Messages** et sélectionnez **Webhook** dans les options de message.

Dans votre webhook, remplissez les champs suivants :
- **Webhook URL** : `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Request Body** : Raw Text

D'autres cas d'usage peuvent être traités via les [API d'assistance de Zendesk](https://developer.zendesk.com/rest_api/docs/support/introduction), qui modifieraient en conséquence l'endpoint `/api/v2/` à la fin de l'URL du webhook.

#### En-tête et méthode de la requête {#request-header-and-method}

Zendesk requiert un en-tête HTTP pour l'autorisation et une méthode HTTP. Dans l'onglet **Settings**, remplacez le <email_address> par votre e-mail d'administrateur Zendesk et le <api_token> par votre jeton API Zendesk.

- **HTTP Method** : POST
- **Request Headers** :
  - **Authorization** : Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type** : application/json

![Paramètres du webhook Braze avec l'en-tête d'autorisation Zendesk et la méthode POST configurés.]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Corps de la requête {#request-body}

Définissez les détails du ticket comme le type, le sujet et le statut dans le payload de votre webhook. Les détails des tickets sont extensibles et personnalisables sur la base de l'[API des tickets de Zendesk](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket). Utilisez l'exemple suivant pour vous aider à structurer votre payload et à saisir les champs souhaités.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}",
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Étape 2 : Prévisualiser votre requête {#step-2-preview-your-request}

Votre texte brut sera automatiquement mis en évidence s'il s'agit d'une étiquette Braze applicable.

Prévisualisez votre requête dans le panneau **Preview** ou accédez à l'onglet **Test**, où vous pouvez sélectionner un utilisateur aléatoire ou un utilisateur existant, ou personnaliser le vôtre pour tester votre webhook.

Enfin, vérifiez si le ticket a bien été créé du côté de Zendesk.

## Identifiant commun {#common-identifier}

Si vous possédez un identifiant commun entre Braze et Zendesk, il est recommandé de l'utiliser comme `requester_id`. Cela permettra d'unifier les deux groupes d'utilisateurs. Si ce n'est pas le cas, nous vous recommandons de transmettre un ensemble d'attributs d'identification tels que le nom, l'adresse e-mail, le numéro de téléphone ou autres.

## Intégration de Zendesk à Braze {#zendesk-to-braze-integration}

### Étape 1 : Créer un webhook {#step-1-create-a-webhook}

1. Dans le [Centre d'administration](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), cliquez sur **Apps and integrations** dans la barre latérale, puis sélectionnez **Webhooks > Webhooks**.<br><br>
2. Cliquez sur **Create webhook**.<br><br>
3. Sélectionnez **Trigger** ou **Automation** et cliquez sur **Next**.<br>![Écran de création de webhook Zendesk avec les options Trigger et Automation.]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Fournissez les informations suivantes dans votre webhook :
- Saisissez un nom et une description pour le webhook.
- Saisissez l'URL de l'endpoint Braze que votre webhook utilisera. {% raw %}Dans notre exemple, nous utiliserons `https://{{instance_url}}/users/track`.{% endraw %}
- Sélectionnez POST comme méthode de requête du webhook et définissez le format de la requête sur JSON.
- Sélectionnez la méthode d'authentification par jeton porteur pour le webhook et indiquez votre [clé API Braze]({{site.baseurl}}/api/basics#creating-and-managing-rest-api-keys).
  - Assurez-vous que la clé API que vous utilisez dispose des [autorisations correctes]({{site.baseurl}}/api/basics#rest-api-key-permissions) pour l'endpoint Braze que votre webhook utilise.<br><br>
5. (Recommandé) Testez le webhook pour vérifier qu'il fonctionne correctement.<br><br>
6. Pour les webhooks de déclenchement et d'automatisation, vous devez connecter le webhook à un déclencheur ou à une automatisation avant de terminer la configuration. Reportez-vous à l'étape suivante pour notre exemple de création d'un déclencheur pour le webhook. Une fois le déclencheur créé, vous pouvez revenir à cette page et sélectionner **Finish setup**.

### Étape 2 : Créer un déclencheur ou une automatisation {#step-2-create-a-trigger-or-automation}

[Suivez les instructions de Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb) sur la façon de connecter votre webhook à un déclencheur ou à une automatisation.

L'exemple ci-dessous utilise un déclencheur pour invoquer le webhook lorsque le statut d'un cas d'assistance est passé à « Résolu » ou « Fermé ».

1. Dans le **Centre d'administration**, cliquez sur **Objects and rules** dans la barre latérale, puis sélectionnez **Business rules > Triggers**.<br><br>
2. Sélectionnez **Add trigger**.<br><br>
3. Donnez un nom à votre déclencheur et sélectionnez une catégorie.<br><br>
4. Sélectionnez **Add condition** pour définir les conditions qui doivent déclencher le webhook. Par exemple, « Catégorie de statut modifiée en fermée » ou « Catégorie de statut modifiée en résolue ».![Générateur de conditions de déclencheur Zendesk affichant les conditions de catégorie de statut.]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Sélectionnez **Add action**, choisissez **Notify active webhook** et sélectionnez dans la liste déroulante le webhook créé à l'étape précédente.<br><br>
6. Définissez le corps JSON pour qu'il soit conforme à votre endpoint Braze, en utilisant des marques substitutives de variables Zendesk pour remplir dynamiquement les champs pertinents.<br>![Éditeur de payload d'action webhook Zendesk avec les variables du corps JSON.]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Sélectionnez **Create**.<br><br>
8. Retournez à votre webhook et cliquez sur **Finish setup**.