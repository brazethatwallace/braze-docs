---
nav_title: "Groupes d'abonnement"
article_title: "Groupes d'abonnement"
page_order: 4
description: "Cet article décrit les groupes d'abonnement WhatsApp, les états d'abonnement proposés et la manière dont les groupes d'abonnement sont configurés."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp


---

# Groupes d'abonnement WhatsApp {#whatsapp-subscription-groups}

> Les groupes d'abonnement WhatsApp sont créés lors de l'intégration de WhatsApp à votre application via le **portail des partenaires technologiques**. Pour un aperçu cross-canal des groupes d'abonnement, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## États d'abonnement WhatsApp {#whatsapp-subscription-states}
{: #whatsapp-subscription-states}

Pour les définitions des états d'abonnement WhatsApp et leur relation avec les exigences d'abonnement de Meta, consultez [Statut d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp).

### Définir les groupes d'abonnement WhatsApp des utilisateurs {#setting-users-whatsapp-subscription-groups}

- **REST API :** Les profils utilisateur peuvent être définis de manière programmatique via l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) en utilisant la REST API de Braze.
- **SDK Web :** Les utilisateurs peuvent être ajoutés à un groupe d'abonnement e-mail, SMS ou WhatsApp en utilisant la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Importation d'utilisateurs :** Les utilisateurs peuvent être ajoutés à des groupes d'abonnement e-mail ou SMS via **Importer des utilisateurs**. Lors de la mise à jour du statut du groupe d'abonnement, vous devez disposer de ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Consultez [Importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) pour plus d'informations.

### Vérifier le groupe d'abonnement WhatsApp d'un utilisateur {#checking-a-users-whatsapp-subscription-group}

- **Profil utilisateur :** Les profils utilisateur individuels sont accessibles via le tableau de bord de Braze depuis **Audience** > **Rechercher des utilisateurs**. Vous pouvez y rechercher des profils utilisateur par adresse e-mail, numéro de téléphone ou identifiant utilisateur externe. Une fois dans un profil utilisateur, sous l'onglet **Engagement**, vous pouvez consulter le groupe d'abonnement WhatsApp d'un utilisateur et son statut.

- **REST API :** Le groupe d'abonnement d'un profil utilisateur individuel peut être consulté via l'[endpoint Lister les groupes d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou l'[endpoint Lister le statut du groupe d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) en utilisant la REST API de Braze.

## Archiver des groupes d'abonnement {#archive-subscription-groups}

Si vous devez cesser d'utiliser un groupe d'abonnement WhatsApp, vous pouvez l'archiver pour le marquer comme inactif.

L'archivage d'un groupe d'abonnement le marque comme inactif, mais ne le supprime pas de votre espace de travail. Si vous devez supprimer entièrement un numéro de téléphone WhatsApp ou un groupe d'abonnement, vous devez d'abord archiver le groupe d'abonnement dans le gestionnaire des groupes d'abonnement avant de demander la suppression auprès du support Braze.

Pour archiver un groupe d'abonnement :

1. Allez dans **Audience** > **Gestion des groupes d'abonnement**.
2. Trouvez le groupe d'abonnement WhatsApp que vous souhaitez archiver.
3. Survolez le statut du groupe d'abonnement et sélectionnez <i class="fa-solid fa-box-archive" aria-label="Archiver"></i> **Archiver**.

## Processus d'abonnement et de désabonnement WhatsApp {#whatsapp-opt-in-and-opt-out-process}

Pour un aperçu du statut d'abonnement WhatsApp, des exigences d'abonnement et du comportement de désabonnement, consultez [Statut d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp).

Actuellement, les utilisateurs peuvent s'abonner et [s'abonner ou se désabonner]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) de la communication WhatsApp de différentes manières, notamment par [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), via un site web, un fil de discussion WhatsApp, par téléphone ou en personne. Notez que l'abonnement est obligatoire.

Les mots-clés d'abonnement ne sont actuellement pas pris en charge pour le canal WhatsApp, vous êtes donc responsable de la gestion de votre liste d'utilisateurs. WhatsApp applique une approche rétrospective en matière d'abonnements et de limites de débit : si les utilisateurs commencent à vous signaler ou à vous bloquer, votre limite de débit sera abaissée.

## Mettre à jour le statut d'abonnement d'un utilisateur vers un Canvas WhatsApp {#update-subscription-status}

Quelles que soient les méthodes d'abonnement et de désabonnement que vous utilisez, vous pouvez mettre à jour le statut d'abonnement des profils utilisateur avec l'une des méthodes de mise à jour suivantes :

- Créez un [webhook Braze-à-Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#considerations) qui met à jour le statut d'abonnement via la REST API, comme dans l'exemple suivant :

![Composeur de webhook avec un message utilisant la méthode POST.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Pour éviter les conditions de concurrence, tout message de suivi après le webhook doit être contenu dans un second Canvas déclenché par les résultats du premier Canvas (par exemple, un utilisateur est entré dans une variante de Canvas et fait partie d'un groupe d'abonnement WhatsApp).

- Utilisez l'éditeur JSON avancé pour mettre à jour le profil utilisateur avec le modèle suivant :

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![Étape de mise à jour utilisateur avec une étape d'éditeur JSON avancé.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
Les mises à jour du statut d'abonnement d'un utilisateur peuvent prendre jusqu'à 60 secondes.
{% endalert %}