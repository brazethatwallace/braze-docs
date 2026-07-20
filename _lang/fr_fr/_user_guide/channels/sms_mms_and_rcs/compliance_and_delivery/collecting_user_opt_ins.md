---
nav_title: "Collecter les abonnements des utilisateurs"
article_title: Bonnes pratiques pour collecter les abonnements SMS des utilisateurs
page_order: 3
description: "Cet article de référence présente trois bonnes pratiques pour collecter les abonnements des utilisateurs."
page_type: reference
channel:
  - SMS

---

# Collecter les abonnements des utilisateurs {#collect-user-opt-ins}

> L'article suivant répertorie quelques méthodes courantes d'abonnement par SMS.

## Option 1 : Demander aux utilisateurs d'envoyer un SMS à votre code court ou code long {#option-1-ask-users-to-text-your-short-or-long-code}

Demandez aux utilisateurs d'envoyer « START », « UNSTOP », « YES » ou un mot-clé d'abonnement personnalisé à votre numéro pour les ajouter automatiquement à votre groupe d'abonnement. Sur votre site web, votre application mobile ou même dans vos publicités, vous pouvez inviter les utilisateurs à le faire pour s'abonner, et vous pouvez proposer une incitation si cela s'avère utile.

## Option 2 : Les utilisateurs s'abonnent via un message in-app {#option-2-users-opt-in-via-in-app-message}

Pour permettre aux utilisateurs de s'abonner aux SMS depuis un message in-app, utilisez le [formulaire de capture de numéro de téléphone]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) fourni par Braze pour créer un formulaire personnalisé qui vous permet de collecter des numéros de téléphone et de développer votre liste SMS.

![Éditeur de messages in-app avec un modèle de capture de numéro de téléphone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze recommande également d'utiliser la fonctionnalité de [double abonnement SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in). Cette fonctionnalité fonctionne automatiquement avec le formulaire de capture de numéro de téléphone du message in-app, en invitant les utilisateurs à confirmer leur intention après avoir soumis leur numéro de téléphone via le formulaire.

## Option 3 : Flux d'inscription {#option-3-sign-up-flow}

Lorsqu'un nouvel utilisateur s'inscrit ou crée un compte sur le site web ou l'application, demandez son numéro de téléphone et son adresse e-mail. Incluez une case à cocher pour recevoir des e-mails promotionnels et des SMS.

Après l'inscription de l'utilisateur, procédez comme suit :

1. Utilisez l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) pour créer l'utilisateur et enregistrer ses attributs.

{% raw %}
```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```
{% endraw %}

{: start="2"}
2. Utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour abonner l'utilisateur aux SMS.

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```
{% endraw %}

{% alert tip %}
Pour faire entrer les utilisateurs dans le flux de [double abonnement SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) lorsque vous les abonnez via la REST API, définissez le paramètre `use_double_opt_in_logic` sur `true` dans votre requête. Si vous omettez ce paramètre, les utilisateurs sont abonnés sans recevoir de confirmation de double abonnement.

Ce paramètre est pris en charge par les endpoints suivants :<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
{% endalert %}