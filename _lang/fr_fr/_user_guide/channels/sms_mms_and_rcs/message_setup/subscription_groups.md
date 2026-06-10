---
nav_title: "Groupes d'abonnement"
article_title: Groupes d'abonnement SMS et RCS
page_order: 4
description: "Cet article de référence couvre les groupes d'abonnement, les états d'abonnement et le processus de configuration des groupes d'abonnement pour les canaux SMS, MMS et RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS

---

# Groupes d'abonnement SMS, MMS et RCS {#sms-mms-and-rcs-subscription-groups}

> Les groupes d'abonnement constituent la base de l'envoi de messages SMS, MMS et RCS via Braze. Un groupe d'abonnement est un ensemble d'[entités d'envoi]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/) (telles que des expéditeurs vérifiés RCS, des codes courts SMS, des codes longs SMS ou des identifiants d'expéditeur alphanumériques SMS) utilisées pour un type spécifique d'envoi de messages. Par exemple, si une marque prévoit d'envoyer des messages SMS transactionnels et promotionnels, deux groupes d'abonnement avec des pools distincts de numéros de téléphone d'envoi devront être configurés dans votre tableau de bord de Braze.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## États des groupes d'abonnement {#subscription-group-states}

Il existe deux états d'abonnement pour les utilisateurs SMS et RCS : `subscribed` et `unsubscribed`. L'état d'abonnement d'un utilisateur se situe au niveau du groupe d'abonnement et n'est pas partagé entre les groupes d'abonnement, ce qui signifie qu'un utilisateur peut être `subscribed` à un groupe d'abonnement transactionnel mais `unsubscribed` d'un groupe promotionnel. Pour les marques, cette séparation des états garantit qu'elles peuvent continuer à envoyer des messages SMS et RCS pertinents à leurs utilisateurs.

| État | Définition |
| --------- | ---------- |
| Abonné | L'utilisateur est abonné pour recevoir des SMS et RCS d'un groupe d'abonnement spécifique. Un utilisateur peut être abonné soit en ayant son état d'abonnement mis à jour via l'API d'abonnement Braze, soit en envoyant par SMS un mot-clé d'abonnement. Un utilisateur doit être abonné à un groupe d'abonnement SMS ou RCS pour recevoir des SMS, des RCS, ou les deux. Lorsque le [double opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/) est activé, les utilisateurs doivent confirmer leur intention d'abonnement avant que leur statut d'abonnement ne passe à `Subscribed`. |
| Désabonné | L'utilisateur a explicitement refusé de recevoir des messages de votre groupe d'abonnement SMS et RCS et des numéros de téléphone d'envoi au sein du groupe d'abonnement. Il peut se désabonner en envoyant par SMS un mot-clé de désabonnement, ou vous pouvez désabonner les utilisateurs via l'[API d'abonnement Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Les utilisateurs désabonnés d'un groupe d'abonnement SMS et RCS ne recevront plus aucun SMS ou RCS provenant des numéros de téléphone d'envoi appartenant au groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États des groupes d'abonnement" }

### Définir l'état d'un utilisateur {#set-a-users-state}

Lorsqu'un numéro de téléphone est mis à jour sur un profil utilisateur, le nouveau numéro de téléphone hérite du statut du groupe d'abonnement de l'utilisateur. Si le numéro de téléphone est mis à jour vers un numéro qui existe déjà dans Braze, le statut d'abonnement de ce numéro de téléphone existant est hérité.

Par exemple, si l'utilisateur A possède un numéro de téléphone abonné à plusieurs groupes d'abonnement et que ce numéro de téléphone est ensuite ajouté à l'utilisateur B, l'utilisateur B sera abonné aux mêmes groupes d'abonnement. Pour empêcher un utilisateur d'hériter des abonnements existants, vous pouvez réinitialiser les groupes d'abonnement de l'ancien numéro via la REST API Braze chaque fois qu'un utilisateur change de numéro. Si plusieurs utilisateurs partagent ce numéro de téléphone, ils seront tous désabonnés.

Pour définir l'état du groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **REST API :** Les profils utilisateur peuvent être définis de manière programmatique par l'[endpoint `/subscription/status/set`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) en utilisant la REST API Braze.
- **Intégration SDK :** Les utilisateurs peuvent être ajoutés à un groupe d'abonnement e-mail ou SMS et RCS en utilisant la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Formulaire IAM de capture de numéro de téléphone :** Les numéros de téléphone des utilisateurs peuvent être collectés via le modèle de capture de numéro de téléphone dans l'éditeur glisser-déposer de messages in-app.
- **Gestion automatique lors de l'abonnement ou du désabonnement de l'utilisateur :** Lorsque les utilisateurs envoient par SMS un [mot-clé]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/) d'abonnement ou de désabonnement par défaut, Braze définit et met à jour automatiquement l'état d'abonnement des utilisateurs.
- **Importation d'utilisateurs :** Les utilisateurs peuvent être ajoutés à des groupes d'abonnement e-mail ou SMS et RCS via **Importer des utilisateurs**. Lors de la mise à jour du statut du groupe d'abonnement, vous devez avoir ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Consultez [Importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#updating-subscription-group-status) pour plus d'informations.

#### Mettre à jour l'état d'un utilisateur dans un Canvas {#update-a-users-state-in-a-canvas}

Lors de la mise à jour du statut du groupe d'abonnement d'un utilisateur dans le cadre d'un flux Canvas, utilisez une étape [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) au lieu d'un webhook. L'étape Mise à jour utilisateur attend que le traitement soit terminé avant de faire avancer l'utilisateur vers l'étape suivante, de sorte que les étapes de messagerie ultérieures utilisent le statut d'abonnement mis à jour.

Si vous utilisez un webhook pour mettre à jour les groupes d'abonnement, l'utilisateur avance dès que le webhook est envoyé, et non lorsque le changement d'abonnement a fini d'être traité. Cela peut créer une condition de concurrence où une étape SMS de suivi s'exécute avant que l'utilisateur ne soit abonné, entraînant l'échec du message pour une partie des utilisateurs. Si vous devez utiliser un webhook, ajoutez une étape de délai d'au moins 1 minute avant l'étape de messagerie suivante.

#{% multi_lang_include api/orphaned_subscription_states.md %}

### Vérifier le groupe d'un utilisateur {#check-a-users-group}

Pour vérifier le groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **Profil utilisateur :** Les profils utilisateur individuels sont accessibles via le tableau de bord de Braze en sélectionnant **Recherche d'utilisateurs** dans la barre latérale. Vous pouvez rechercher des profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Dans un profil utilisateur, sous l'onglet Engagement, vous pouvez consulter les groupes d'abonnement SMS et RCS d'un utilisateur.
- **REST API :** Le groupe d'abonnement d'un profil utilisateur individuel peut être consulté via l'[endpoint Répertorier les groupes d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou l'[endpoint Afficher le statut du groupe d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) en utilisant la REST API Braze.

## Envoyer des messages avec un groupe d'abonnement {#send-messages-with-a-subscription-group}

Pour lancer une campagne SMS ou RCS via Braze, sélectionnez un groupe d'abonnement dans le menu déroulant **SMS/MMS/RCS Variants**. Une fois sélectionné, un filtre d'audience sera automatiquement ajouté à votre campagne ou Canvas, garantissant que seuls les utilisateurs `subscribed` au groupe d'abonnement sélectionné font partie de l'audience cible.

{% alert important %}
Conformément aux [réglementations et directives internationales en matière de télécommunications]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/), Braze n'enverra jamais de SMS ou de RCS aux utilisateurs qui ne sont pas abonnés au groupe d'abonnement sélectionné.
{% endalert %}

![Compositeur SMS avec le menu déroulant du groupe d'abonnement ouvert et « Messaging Service A for SMS » mis en surbrillance par l'utilisateur.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Bonnes pratiques pour les groupes d'abonnement SMS {#sms-subscription-group-best-practices}

Concevez des groupes d'abonnement SMS distincts pour chaque objectif de messagerie (par exemple, transactionnel versus marketing) et pour chaque espace de travail. Lorsque vous opérez dans plusieurs pays, envisagez des groupes séparés par région pour respecter les règles de conformité locales, par exemple les restrictions du Brésil sur les fenêtres d'envoi promotionnel.

## Activer les groupes d'abonnement {#enable-subscription-groups}

Pour activer les groupes d'abonnement pour SMS, MMS ou RCS, consultez les informations suivantes :

{% tabs local %}
{% tab SMS %}
Lors de votre processus d'onboarding SMS, un responsable d'onboarding Braze configurera les groupes d'abonnement pour votre compte de tableau de bord. Il travaillera avec vous pour déterminer le nombre de groupes d'abonnement dont vous avez besoin et ajoutera les numéros de téléphone d'envoi appropriés à vos groupes d'abonnement. Les délais de configuration d'un groupe d'abonnement dépendent du type de numéros de téléphone que vous ajoutez. Par exemple, les demandes de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions sur la configuration de votre tableau de bord Braze, contactez votre conseiller Braze pour obtenir de l'assistance.
{% endtab %}

{% tab MMS %}
Pour envoyer un message MMS, au moins un numéro de votre groupe d'abonnement doit être activé pour l'envoi de MMS. Cela est indiqué par une étiquette située à côté du groupe d'abonnement.

![Menu déroulant du groupe d'abonnement avec « Messaging Service A for SMS » mis en surbrillance. L'entrée est précédée de l'étiquette « MMS ».]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Un expéditeur vérifié RCS doit être présent dans votre groupe d'abonnement avant de pouvoir envoyer un message RCS.

Il existe deux façons d'ajouter un expéditeur vérifié RCS :
- L'ajouter à un groupe d'abonnement existant
- Créer un nouveau groupe d'abonnement RCS
Le choix dépend en grande partie des cas d'utilisation RCS qui vous intéressent.

Selon votre intégration, Braze peut ajouter des expéditeurs vérifiés RCS à vos groupes d'abonnement SMS existants ou configurer de nouveaux groupes d'abonnement pour vous. Dans les deux cas, votre gestionnaire de la satisfaction client vous guidera à travers une mise à niveau fluide et efficace du trafic SMS.
{% endtab %}
{% endtabs %}

## Gérer les désabonnements en langage naturel dans la console des agents {#handle-natural-language-opt-outs-in-the-agent-console}

Pour une gestion complète des abonnements, vous pouvez capturer les intentions de désabonnement qui ne correspondent pas aux mots-clés standard ou personnalisés (comme « Ne m'envoyez plus de SMS »). En créant un agent IA, vous pouvez utiliser l'analyse de sentiment pour identifier et traiter automatiquement ces demandes.

### Configuration {#setup}

1. Dans la [console des agents]({{site.baseurl}}/user_guide/brazeai/agents/), créez un « Agent d'analyse de sentiment SMS ».

{% alert tip %}
Utilisez [Operator]({{site.baseurl}}/user_guide/brazeai/agents/reference/#canvas-agent-examples) pour vous aider dans la configuration initiale de l'agent.
{% endalert %}

{: start="2"}
2. Créez un Canvas basé sur une action déclenché par **Send an SMS inbound message**, dans la catégorie de mot-clé **Other**.
3. Ajoutez l'[étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/) au Canvas pour identifier l'intention de désabonnement.
4. Ajoutez une [étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) SMS ultérieure pour confirmer la demande : « Il semble que vous souhaitiez vous désabonner des SMS, nous allons donc vous désabonner. Si c'est une erreur, envoyez START pour vous réabonner. »
5. Ajoutez une [étape Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#user-update) pour modifier le statut de l'utilisateur dans le groupe d'abonnement SMS spécifique en « Désabonné ».

{% alert note %}
L'utilisation de la console des agents consomme des crédits de message ou d'action.
{% endalert %}

## Migrer le trafic SMS vers RCS {#migrate-sms-traffic-to-rcs}

Si vous avez des groupes d'abonnement SMS et RCS séparés, vous pouvez migrer les utilisateurs de SMS vers RCS en utilisant un Canvas en une seule étape.

Braze recommande de tester l'envoi de RCS à des volumes d'utilisateurs plus réduits dans un premier temps et de migrer davantage d'utilisateurs vers le groupe d'abonnement RCS au fil du temps. Par exemple, si vous avez 1 000 000 d'utilisateurs abonnés à un groupe d'abonnement SMS, cela pourrait consister à d'abord migrer tous les utilisateurs vers le nouveau groupe d'abonnement, puis à segmenter sur une audience plus restreinte de 50 000 à 100 000 (5‑10 %) pour tester les messages RCS.

### Étape 1 : Créer un Canvas et remplir la planification d'entrée {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Créez un Canvas et donnez-lui un nom facilement identifiable (tel que « Transfert d'utilisateurs du groupe d'abonnement SMS-RCS »). Ensuite, planifiez la campagne au moment qui vous convient.

### Étape 2 : Définir votre audience {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Définissez votre audience en utilisant l'une des méthodes suivantes. Ensuite, accédez à l'étape **Paramètres d'envoi** et sélectionnez **Utilisateurs abonnés ou ayant opté pour la réception**.

| Méthode | Description |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Créer un segment** | Créez un segment qui inclut tous les utilisateurs d'un groupe d'abonnement ou un sous-ensemble en utilisant des filtres de segmentation (comme un échantillon aléatoire de 5‑10 %). Les segments se mettent à jour avant chaque envoi pour refléter votre base d'utilisateurs actuelle. |
| **Appliquer des filtres de campagne ou de Canvas** | Affinez l'audience dans l'étape **Audience cible** de votre campagne ou Canvas. Ajustez les options de ciblage sans quitter la page pour plus de flexibilité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Définir votre audience" }

### Étape 3 : Configurer une étape de mise à jour utilisateur {#step-3-configure-a-user-update-step}

Ajoutez une étape de mise à jour utilisateur à votre Canvas. Dans l'étape, ouvrez l'**éditeur JSON avancé** et saisissez le code suivant (pour le champ d'identifiant utilisateur unique, nous recommandons d'utiliser le champ `braze_id`) :

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![Objet de mise à jour utilisateur contenant le code JSON indiqué précédemment.]({% image_buster /assets/img/sms/user_update_object.png %})

### Étape 4 : Tester le Canvas {#step-4-test-the-canvas}

Nous recommandons vivement de [tester votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases/) pour confirmer qu'il fonctionne comme prévu avant de l'envoyer à votre audience plus large.

### Étape 5 : Lancer votre Canvas {#step-5-launch-your-canvas}

Après avoir testé votre Canvas avec succès, lancez-le pour votre sous-ensemble d'utilisateurs !

Pour confirmer que vos utilisateurs ont été migrés avec succès, nous recommandons de vérifier quelques profils utilisateur individuels qui ont été mis à jour. Dans l'onglet **Engagement**, recherchez **Contact Settings** et faites défiler pour voir les groupes d'abonnement auxquels l'utilisateur est abonné. Le bouton bascule du groupe d'abonnement RCS devrait maintenant être activé.

Pour la configuration de l'expéditeur RCS et du groupe d'abonnement, consultez également [Configurer RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup/).

## Bonnes pratiques {#best-practices}

### Désigner des groupes d'abonnement distincts {#designate-separate-subscription-groups}

- **Type de messagerie :** Créez des groupes d'abonnement distincts pour chaque type de messagerie, comme transactionnel et marketing.
- **Espace de travail :** Créez des groupes d'abonnement distincts pour chaque espace de travail afin de maintenir la clarté et l'organisation.

Considérez l'exemple suivant avec quatre groupes d'abonnement répartis sur deux espaces de travail :

- **Espace de travail de production**
  - Marketing - PROD pour SMS
  - Transactionnel - PROD pour SMS
- **Espace de travail de développement (pour les tests)**
  - Marketing - DEV pour SMS
  - Transactionnel - DEV pour SMS

### Utiliser des conventions de nommage claires {#use-clear-naming-conventions}

Choisissez des noms de groupes d'abonnement descriptifs et clairs afin que le bon groupe soit sélectionné lors de la création de campagnes SMS.

### Séparer les groupes par pays {#separate-groups-by-country}

Les réglementations SMS varient selon les pays. Nous suggérons de séparer les groupes d'abonnement SMS par pays. Cela vous aide à respecter les normes de conformité dans toutes les régions où vous envoyez des messages.

Pour chaque groupe d'abonnement, vous pouvez également configurer une liste de pays autorisés sous **Geographic Permissions** afin que les SMS, MMS et RCS ne soient envoyés qu'aux régions approuvées. Pour en savoir plus, consultez [Autorisations géographiques]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/).

Par exemple, au Brésil, l'envoi de messages marketing en dehors des heures de 9 h à 21 h heure locale est interdit, et le pays couvre trois fuseaux horaires. Pour respecter ces réglementations, vous pourriez configurer des groupes distincts pour l'envoi de messages au Brésil et aux États-Unis. Cela empêche les utilisateurs au Brésil de recevoir des messages marketing pendant les heures interdites.