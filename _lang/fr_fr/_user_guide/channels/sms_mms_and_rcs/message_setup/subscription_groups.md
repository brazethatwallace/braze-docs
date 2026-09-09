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

> Les groupes d'abonnement constituent la base de l'envoi de messages SMS, MMS et RCS via Braze. Un groupe d'abonnement est un ensemble d'[entités d'envoi]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) — telles que des expéditeurs vérifiés RCS, des codes courts SMS, des codes longs SMS ou des identifiants d'expéditeur alphanumériques SMS — utilisées dans un but de communication spécifique (par exemple, transactionnel ou promotionnel). Pour un aperçu cross-canal des groupes d'abonnement, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

<a id="subscription-group-states"></a>

## États des groupes d'abonnement {#subscription-group-states}
{: #sms-subscription-states}

Il existe deux états d'abonnement pour les utilisateurs SMS et RCS : `subscribed` et `unsubscribed`. L'état d'abonnement d'un utilisateur est défini au niveau du groupe d'abonnement et n'est pas partagé entre les groupes d'abonnement, ce qui signifie qu'un utilisateur peut être `subscribed` à un groupe d'abonnement transactionnel mais `unsubscribed` d'un groupe promotionnel. Pour les marques, cette séparation des états garantit qu'elles peuvent continuer à envoyer des messages SMS et RCS pertinents à leurs utilisateurs.

| État | Définition |
| --------- | ---------- |
| Abonné | L'utilisateur est abonné pour recevoir des SMS et RCS d'un groupe d'abonnement spécifique. Un utilisateur peut être abonné soit en mettant à jour son état d'abonnement via l'API d'abonnement Braze, soit en envoyant par SMS un mot-clé d'abonnement. Un utilisateur doit être abonné à un groupe d'abonnement SMS ou RCS pour recevoir des SMS, des RCS, ou les deux. Lorsque le [double abonnement]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) est activé, les utilisateurs doivent confirmer leur intention d'abonnement avant que leur statut d'abonnement ne soit mis à jour à `Subscribed`. |
| Désabonné | L'utilisateur s'est explicitement désinscrit de la communication de votre groupe d'abonnement SMS et RCS et des numéros de téléphone d'envoi au sein du groupe d'abonnement. Il peut se désabonner en envoyant par SMS un mot-clé de désabonnement, ou vous pouvez désabonner les utilisateurs via l'[API d'abonnement Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Les utilisateurs désabonnés d'un groupe d'abonnement SMS et RCS ne reçoivent plus aucun SMS ni RCS provenant des numéros de téléphone d'envoi appartenant à ce groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États des groupes d'abonnement" }

### Définir l'état d'un utilisateur {#set-a-users-state}

Lorsqu'un numéro de téléphone est mis à jour sur un profil utilisateur, le nouveau numéro de téléphone hérite du statut du groupe d'abonnement de l'utilisateur. Si le numéro de téléphone est mis à jour avec un numéro qui existe déjà dans Braze, le statut d'abonnement de ce numéro de téléphone existant est hérité.

Par exemple, si l'Utilisateur A possède un numéro de téléphone abonné à plusieurs groupes d'abonnement et que ce numéro de téléphone est ensuite ajouté à l'Utilisateur B, l'Utilisateur B est abonné aux mêmes groupes d'abonnement. Pour éviter qu'un utilisateur n'hérite des abonnements existants, vous pouvez réinitialiser les groupes d'abonnement de l'ancien numéro via la REST API de Braze chaque fois qu'un utilisateur change de numéro. Si plusieurs utilisateurs partagent ce numéro de téléphone, ils sont tous désabonnés.

Pour définir l'état du groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **REST API :** Utilisez l'[endpoint `/subscription/status/set`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) pour définir de manière programmatique les profils utilisateur avec la REST API de Braze. Chaque requête peut inclure entre 1 et 25 groupes d'abonnement.
- **Intégration SDK :** Les utilisateurs peuvent être ajoutés ou retirés d'un groupe d'abonnement e-mail, SMS ou RCS en utilisant `addToSubscriptionGroup` et `removeFromSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup). Les méthodes SDK ne remplacent pas les flux réglementaires d'abonnement ou de désabonnement gérés par les mots-clés et la REST API.
- **Formulaire de capture de numéro de téléphone dans les messages in-app :** Les numéros de téléphone des utilisateurs peuvent être collectés via le modèle de capture de numéro de téléphone dans l'éditeur par glisser-déposer de messages in-app.
- **Gestion automatique lors de l'abonnement/désabonnement de l'utilisateur :** Lorsque les utilisateurs envoient par SMS un [mot-clé]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) d'abonnement ou de désabonnement par défaut, Braze définit et met à jour automatiquement l'état d'abonnement des utilisateurs.
- **Importation d'utilisateurs :** Les utilisateurs peuvent être ajoutés à des groupes d'abonnement e-mail, SMS ou RCS via **Importer des utilisateurs**. Lors de la mise à jour du statut du groupe d'abonnement, vous devez disposer de ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Consultez [Importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) pour plus d'informations.
- **Tableau de bord de Braze :** Sélectionnez **Recherche d'utilisateurs** dans la barre latérale, ouvrez le profil d'un utilisateur et mettez à jour les groupes d'abonnement SMS ou RCS sous **Paramètres de contact** dans l'onglet **Engagement**.
- **Cloud Data Ingestion (CDI) :** Incluez `subscription_group_id` et `subscription_state` dans les lignes synchronisées. Consultez [Configuration des tables Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **Étape de mise à jour de l'utilisateur :** Mettez à jour le statut d'abonnement dans un Canvas avec une étape [Mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Consultez [Mettre à jour l'état d'un utilisateur dans un Canvas](#update-a-users-state-in-a-canvas) pour les considérations de timing.

#### Mettre à jour l'état d'un utilisateur dans un Canvas {#update-a-users-state-in-a-canvas}

Lors de la mise à jour du statut du groupe d'abonnement d'un utilisateur dans le cadre d'un flux Canvas, utilisez une étape [Mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) au lieu d'un webhook. L'étape de mise à jour de l'utilisateur attend la fin du traitement avant de faire avancer l'utilisateur vers l'étape suivante, de sorte que les étapes de communication ultérieures utilisent le statut d'abonnement mis à jour.

Si vous utilisez un webhook pour mettre à jour les groupes d'abonnement, l'utilisateur avance dès que le webhook est envoyé — et non lorsque la modification de l'abonnement a fini d'être traitée. Cela peut créer une condition de concurrence où une étape SMS ultérieure s'exécute avant que l'utilisateur ne soit abonné, ce qui entraîne l'échec du message pour une partie des utilisateurs. Si vous devez utiliser un webhook, ajoutez une étape de délai d'au moins 1 minute avant l'étape de communication suivante.

{% multi_lang_include api/orphaned_subscription_states.md %}

### Vérifier le groupe d'un utilisateur {#check-a-users-group}

Pour vérifier le groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **Profil utilisateur :** Les profils utilisateur individuels sont accessibles via le tableau de bord de Braze en sélectionnant **Recherche d'utilisateurs** dans la barre latérale. Vous pouvez rechercher des profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Dans un profil utilisateur, sous l'onglet Engagement, vous pouvez consulter les groupes d'abonnement SMS et RCS d'un utilisateur.
- **REST API :** Le groupe d'abonnement d'un profil utilisateur individuel peut être consulté via l'[endpoint Lister les groupes d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou l'[endpoint Lister le statut du groupe d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) en utilisant la REST API de Braze.

## Envoyer des messages avec un groupe d'abonnement {#send-messages-with-a-subscription-group}

Pour lancer une campagne SMS ou RCS via Braze, sélectionnez un groupe d'abonnement dans le menu déroulant **SMS/MMS/RCS Variants**. Une fois sélectionné, un filtre d'audience est automatiquement ajouté à votre Campaign ou Canvas, garantissant que seuls les utilisateurs `subscribed` au groupe d'abonnement sélectionné font partie de l'audience cible.

Avant que les utilisateurs puissent recevoir des messages d'une Campaign ou d'un Canvas, ils doivent être abonnés au groupe d'abonnement sélectionné. Si les envois échouent pour des utilisateurs par ailleurs valides, confirmez qu'ils sont abonnés en utilisant l'une des méthodes décrites dans [Définir l'état d'un utilisateur](#set-a-users-state). Pour les exigences de double abonnement, consultez [États des groupes d'abonnement](#sms-subscription-states).

{% alert important %}
Conformément aux [réglementations et directives internationales en matière de télécommunications]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), Braze n'envoie jamais de SMS ou de RCS aux utilisateurs qui ne sont pas abonnés au groupe d'abonnement sélectionné.
{% endalert %}

![Le compositeur SMS avec le menu déroulant du groupe d'abonnement ouvert et « Messaging Service A for SMS » mis en surbrillance par l'utilisateur.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Bonnes pratiques pour les groupes d'abonnement SMS {#sms-subscription-group-best-practices}

Concevez des groupes d'abonnement SMS distincts pour chaque objectif de communication (par exemple, transactionnel versus marketing) et pour chaque espace de travail. Lorsque vous opérez dans plusieurs pays, envisagez des groupes séparés par région pour respecter les règles de conformité locales — par exemple, les restrictions du Brésil sur les fenêtres d'envoi promotionnel.

## Activer les groupes d'abonnement {#enable-subscription-groups}

Pour activer les groupes d'abonnement pour les SMS, MMS ou RCS, consultez les informations suivantes :

{% tabs local %}
{% tab SMS %}
Lors de votre processus d'onboarding SMS, un gestionnaire d'onboarding Braze configure les groupes d'abonnement pour votre compte de tableau de bord. Il travaille avec vous pour déterminer le nombre de groupes d'abonnement dont vous avez besoin et ajoute les numéros de téléphone d'envoi appropriés à vos groupes d'abonnement. Les délais de configuration d'un groupe d'abonnement dépendent du type de numéros de téléphone que vous ajoutez. Par exemple, les demandes de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions concernant la configuration de votre tableau de bord Braze, contactez votre conseiller Braze pour obtenir de l'aide.
{% endtab %}

{% tab MMS %}
Pour envoyer un message MMS, au moins un numéro de votre groupe d'abonnement doit être activé pour l'envoi de MMS. Cela est indiqué par une étiquette située à côté du groupe d'abonnement.

![Menu déroulant du groupe d'abonnement avec « Messaging Service A for SMS » mis en évidence. L'entrée est préfixée par l'étiquette « MMS ».]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Un expéditeur vérifié RCS doit être présent dans votre groupe d'abonnement avant de pouvoir envoyer un message RCS.

Il existe deux façons d'ajouter un expéditeur vérifié RCS :
- L'ajouter à un groupe d'abonnement existant
- Créer un nouveau groupe d'abonnement RCS
Le choix dépend en grande partie des cas d'usage RCS qui vous intéressent.

Selon votre intégration, Braze peut ajouter des expéditeurs vérifiés RCS à vos groupes d'abonnement SMS existants ou configurer de nouveaux groupes d'abonnement pour vous. Dans les deux cas, votre gestionnaire du succès des clients vous guide tout au long d'une mise à niveau du trafic SMS fluide et efficace.
{% endtab %}
{% endtabs %}

## Gérer les désinscriptions en langage naturel dans la console d'agents {#handle-natural-language-opt-outs-in-the-agent-console}

Pour une gestion complète des abonnements, vous pouvez capturer les intentions de désinscription qui ne correspondent pas aux mots-clés standard ou personnalisés (comme « Ne m'envoyez plus de SMS »). En créant un agent IA, vous pouvez utiliser l'analyse de sentiment pour identifier ces demandes et y répondre automatiquement.

### Configuration {#setup}

1. Dans la [console d'agents]({{site.baseurl}}/user_guide/brazeai/agents), créez un « Agent d'analyse de sentiment SMS ».

{% alert tip %}
Utilisez [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) pour vous aider avec la configuration initiale de l'agent.
{% endalert %}

{: start="2"}
2. Créez un Canvas basé sur une action, déclenché par **Envoyer un message SMS entrant**, dans la catégorie de mots-clés **Other**.
3. Ajoutez l'[étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) au Canvas pour identifier l'intention de désinscription.
4. Ajoutez une [étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) SMS ultérieure pour confirmer la demande : « Il semble que vous souhaitiez vous désabonner des SMS, nous allons donc vous désabonner. Si c'est une erreur, envoyez START pour vous réabonner. »
5. Ajoutez une [étape Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) pour modifier le statut de l'utilisateur dans le groupe d'abonnement SMS spécifique en « Désabonné ».

{% alert note %}
L'utilisation de la console d'agents consomme des crédits de messages ou d'actions.
{% endalert %}

## Migrer le trafic SMS vers RCS {#migrate-sms-traffic-to-rcs}

Si vous disposez de groupes d'abonnement SMS et RCS distincts, vous pouvez migrer les utilisateurs du SMS vers le RCS à l'aide d'un Canvas en une seule étape.

Braze recommande de tester d'abord l'envoi de RCS à un volume réduit d'utilisateurs, puis de migrer progressivement davantage d'utilisateurs vers le groupe d'abonnement RCS. Par exemple, si vous avez 1 000 000 d'utilisateurs abonnés à un groupe d'abonnement SMS, vous pourriez d'abord migrer tous les utilisateurs vers le nouveau groupe d'abonnement, puis segmenter sur une audience plus restreinte de 50 000 à 100 000 (5 à 10 %) pour tester les messages RCS.

### Étape 1 : Créer un Canvas et remplir le calendrier d'entrée {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Créez un Canvas et donnez-lui un nom facilement identifiable (par exemple « Transfert d'utilisateurs du groupe d'abonnement SMS vers RCS »). Ensuite, planifiez la campagne au moment qui vous convient.

### Étape 2 : Définir votre audience {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Définissez votre audience en utilisant l'une des méthodes suivantes. Ensuite, passez à l'étape **Send Settings** et sélectionnez **Users who are subscribed or opted-in**.

| Méthode | Description |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Créer un segment** | Créez un segment qui inclut tous les utilisateurs d'un groupe d'abonnement ou un sous-ensemble en utilisant des filtres de segmentation (par exemple, un échantillon aléatoire de 5 à 10 %). Les segments se mettent à jour avant chaque envoi pour refléter votre base d'utilisateurs actuelle. |
| **Appliquer des filtres de campagne ou de Canvas** | Affinez l'audience dans l'étape **Target Audience** de votre campagne ou Canvas. Ajustez les options de ciblage sans quitter la page pour plus de flexibilité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Définir votre audience" }

### Étape 3 : Configurer une étape de mise à jour utilisateur {#step-3-configure-a-user-update-step}

Ajoutez une étape de mise à jour utilisateur à votre Canvas. Dans cette étape, ouvrez l'**Advanced JSON Editor** et saisissez le code suivant (pour le champ d'identifiant utilisateur unique, nous recommandons d'utiliser le champ `braze_id`) :

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

{% alert important %}
Lorsque vous utilisez `use_double_opt_in_logic`, un profil utilisateur doit déjà exister pour que l'état d'abonnement puisse être mis à jour. Si aucun profil utilisateur n'est associé à l'identifiant fourni, l'état d'abonnement n'est pas mis à jour.
{% endalert %}

![Objet de mise à jour utilisateur contenant le code JSON mentionné précédemment.]({% image_buster /assets/img/sms/user_update_object.png %})

### Étape 4 : Tester le Canvas {#step-4-test-the-canvas}

Nous vous recommandons vivement de [tester votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) pour confirmer qu'il fonctionne comme prévu avant de l'envoyer à une audience plus large.

### Étape 5 : Lancer votre Canvas {#step-5-launch-your-canvas}

Une fois que vous avez testé votre Canvas avec succès, lancez-le pour votre sous-ensemble d'utilisateurs !

Pour confirmer que vos utilisateurs ont été migrés avec succès, nous vous recommandons de vérifier quelques profils utilisateur individuels qui ont été mis à jour. Dans l'onglet **Engagement**, recherchez **Contact Settings** et faites défiler pour voir les groupes d'abonnement auxquels l'utilisateur est abonné. Le bouton bascule du groupe d'abonnement RCS devrait maintenant être activé.

Pour la configuration de l'expéditeur RCS et du groupe d'abonnement, consultez également [Configurer le RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Bonnes pratiques {#best-practices}

### Désignez des groupes d'abonnement distincts {#designate-separate-subscription-groups}

- **Type de communication :** Créez des groupes d'abonnement distincts pour chaque type de communication, comme les messages transactionnels et marketing.
- **Espace de travail :** Créez des groupes d'abonnement distincts pour chaque espace de travail afin de maintenir la clarté et l'organisation.

Prenons l'exemple suivant avec quatre groupes d'abonnement répartis sur deux espaces de travail :

- **Espace de travail de production**
  - Marketing - PROD pour SMS
  - Transactionnel - PROD pour SMS
- **Espace de travail de développement (pour les tests)**
  - Marketing - DEV pour SMS
  - Transactionnel - DEV pour SMS

### Utilisez des conventions de nommage claires {#use-clear-naming-conventions}

Choisissez des noms de groupes d'abonnement descriptifs et clairs afin que le bon groupe soit sélectionné lors de la création de Campaigns SMS.

### Séparez les groupes par pays {#separate-groups-by-country}

Les réglementations SMS varient selon les pays. Nous vous suggérons de séparer les groupes d'abonnement SMS par pays. Cela vous aide à respecter les normes de conformité dans toutes les régions où vous envoyez des messages.

Pour chaque groupe d'abonnement, vous pouvez également configurer une liste de pays autorisés sous **Autorisations géographiques** afin que les SMS, MMS et RCS ne soient envoyés que vers des régions approuvées. Pour plus d'informations, consultez [Autorisations géographiques]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

Par exemple, au Brésil, l'envoi de messages marketing en dehors des heures de 9 h à 21 h (heure locale) est interdit, et le pays s'étend sur trois fuseaux horaires. Pour respecter ces réglementations, vous pourriez configurer des groupes distincts pour l'envoi de messages au Brésil et aux États-Unis. Cela empêche les utilisateurs au Brésil de recevoir des messages marketing pendant les heures interdites.