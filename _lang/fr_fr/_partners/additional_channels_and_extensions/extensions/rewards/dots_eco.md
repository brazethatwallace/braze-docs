---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Cet article de référence décrit l'intégration de Braze et de DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) vous permet de récompenser les utilisateurs avec un impact environnemental réel grâce à des certificats numériques traçables. Chaque certificat peut inclure des métadonnées telles qu'une URL de certificat partageable et une URL d'image, afin que les utilisateurs puissent consulter (et retrouver) leur preuve d'impact.

_Cette intégration est maintenue par DOTS.ECO._

## À propos de cette intégration {#about-this-integration}

Braze et DOTS.ECO connectent les parcours d'engagement client à des récompenses d'impact dans le monde réel. Depuis une étape de Canvas ou de Campaign Braze, vous pouvez déclencher une demande de création de certificat DOTS.ECO à l'aide du Contenu connecté. DOTS.ECO renvoie des métadonnées de certificat (telles que `certificate_url` et `certificate_image_url`) que vous pouvez stocker sur le profil utilisateur en tant qu'attributs personnalisés et réutiliser sur des canaux tels que les messages in-app, les Content Cards et les notifications push.

## Cas d'utilisation {#use-cases}

- Déclenchez un certificat d'impact lorsqu'un utilisateur réalise un événement clé (achat, achèvement d'un niveau, abonnement, recommandation).
- Affichez une image de certificat personnalisée dans un message in-app après la réussite de l'étape de Contenu connecté.
- Ajoutez une Content Card « Voir votre certificat » avec l'URL du certificat pour un accès ultérieur.
- Stockez les métadonnées des certificats (telles que `certificate_url`, `certificate_image_url`, `certificate_header` et `greeting`) en tant qu'attributs personnalisés pour les réutiliser dans de futurs envois de messages.
- Attribuez des certificats à l'aide d'un ID utilisateur distant afin que les utilisateurs puissent réclamer et visualiser leur impact ultérieurement.
- Effectuez des tests A/B sur les messages d'impact (différents textes/images) tout en conservant le même flux de mise à jour utilisateur DOTS.ECO.


## Conditions préalables {#prerequisites}

Avant de commencer, vous devez disposer des éléments suivants :

| Prérequis | Description |
|---|---|
| Compte DOTS.ECO | Accès à un compte DOTS.ECO. |
| Identifiants DOTS.ECO | La demande présentée dans cet article nécessite un jeton d'application DOTS.ECO, une clé API et un ID d'allocation. Pour les récupérer, contactez votre gestionnaire de la satisfaction client DOTS.ECO. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. Créez cette clé dans le tableau de bord de Braze sous **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de DOTS.ECO {#integrating-dotseco}

### Étape 1 : Créer un Canvas et ajouter une étape de mise à jour utilisateur {#step-1-create-a-canvas-and-add-a-user-update-step}

Dans le tableau de bord de Braze, créez un nouveau Canvas qui se déclenche lorsqu'un utilisateur réalise un événement clé (tel qu'un achat, un abonnement ou un jalon).

Ajoutez une étape de mise à jour utilisateur juste après l'étape d'entrée. Cette étape servira à appeler l'API DOTS.ECO via le Contenu connecté et à stocker les données de certificat renvoyées sur le profil utilisateur.

Utilisez cette étape pour appeler l'API DOTS.ECO via le Contenu connecté et stocker les données de certificat renvoyées sur le profil utilisateur.

### Étape 2 : Rédiger du JSON avancé : effectuer une requête POST vers DOTS.ECO à l'aide du Contenu connecté {#step-2-compose-advanced-json-make-a-post-request-to-dotseco-using-connected-content}

Dans l'étape **Mise à jour utilisateur**, passez à l'**Éditeur JSON avancé** et utilisez le Contenu connecté pour effectuer une requête POST vers l'API de certificat DOTS.ECO.

Utilisez la balise `capture` et une requête de Contenu connecté pour appeler l'endpoint de certificat de DOTS.ECO. Enregistrez ensuite la réponse sur le profil utilisateur sous forme d'attributs personnalisés.

**Exemple de Contenu connecté et de mise à jour utilisateur**
{% raw %}
```
{% capture post_body %}
{
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",
  "impact_qty": 1,
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"
}
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk
  :method post
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }
  :body {{post_body}}
  :content_type application/json
  :save result
%}

{
  "attributes": [
    {
      "certificate_image_url": "{{result.certificate_image_url}}",
      "certificate_url": "{{result.certificate_url}}",
      "certificate_id": "{{result.certificate_id}}"
    }
  ]
}
```
{% endraw %}

Envoyez la requête à `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![Étape de mise à jour utilisateur DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}
Cette intégration utilise le Contenu connecté à l'intérieur d'une étape Canvas **Mise à jour utilisateur** pour appeler l'API DOTS.ECO. Testez d'abord les requêtes avec un client API (par exemple, Postman) pour valider votre jeton et votre payload.
{% endalert %}

### Étape 3 : Afficher le certificat dans les messages {#step-3-display-the-certificate-in-messages}

Lorsque les attributs du certificat sont stockés sur le profil utilisateur, ils peuvent être référencés dans les étapes de message Canvas en aval.

![Flux DOTS.ECO.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![Étape de message DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![Section de composition de message DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Par exemple :
- Affichez l'image du certificat dans un message in-app à l'aide de {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}
- Créez un lien vers le certificat hébergé à l'aide de {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![Comportement au clic du message DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Vous pouvez ainsi personnaliser les messages in-app, les Content Cards ou les notifications push avec une confirmation d'impact.

## Résolution des problèmes {#troubleshooting}

Consultez les erreurs de Contenu connecté dans le tableau de bord de Braze sous **Paramètres** > **Journal d'activité des messages**.

- **Le Contenu connecté renvoie un résultat vide** : confirmez que `:save result` est défini et que vous faites référence aux champs de réponse attendus.
- **Les attributs n'apparaissent pas dans l'étape de message** :
  - Confirmez que les noms des attributs personnalisés dans Braze correspondent exactement aux attributs que vous avez définis dans l'étape de mise à jour utilisateur.
  - Dans l'étape de mise à jour utilisateur, utilisez l'onglet **Prévisualisation et test** pour confirmer que les attributs sont bien renseignés. Ensuite, envoyez un test à un utilisateur et confirmez que les attributs sont enregistrés sur son profil utilisateur.
- **Erreur `422` (entité non traitable)** : confirmez que votre jeton d'application et votre quantité d'impact sont valides.
- **Erreur `401`** : confirmez que le jeton d'authentification est présent et correct.
- **Pas de prévisualisation d'image dans l'étape de message** : sélectionnez **Envoyer le test à l'utilisateur** dans l'étape de mise à jour utilisateur, puis prévisualisez le message en utilisant ce même utilisateur.