---
nav_title: "Configuration"
article_title: Configuration de LINE
description: "Cet article explique comment configurer le canal LINE dans Braze, y compris les conditions préalables et les prochaines étapes suggérées."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuration de LINE {#line-setup}

> Cet article explique comment configurer le canal LINE dans Braze, y compris comment configurer les utilisateurs, réconcilier les ID utilisateur et créer des utilisateurs test LINE dans Braze.

## Conditions préalables {#prerequisites}

Vous aurez besoin des éléments suivants pour intégrer LINE à Braze :

- [Compte professionnel LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Statut de compte premium ou vérifié (nécessaire pour synchroniser les abonnés existants)
   - Consultez les [directives relatives aux comptes LINE](https://terms2.line.me/official_account_guideline_oth)
- [Compte développeur LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal API de messagerie LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

L'envoi de messages LINE depuis Braze consomme les crédits de messages ou d'actions de votre compte.

{% alert note %}
**Définir `native_line_id`** : Vous pouvez définir `native_line_id` en envoyant des mises à jour utilisateur à Braze (par exemple, avec l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), l'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)). Si votre SDK côté client ne dispose pas d'un champ dédié pour `native_line_id`, envoyez-le dans les mises à jour utilisateur côté serveur en utilisant l'une de ces méthodes.
{% endalert %}

## Types de comptes LINE {#types-of-line-accounts}

| Type de compte | Description |
| --- | --- |
| Compte non vérifié | Un compte non examiné que n'importe qui (particulier ou entreprise) peut obtenir. Ce compte est représenté par un badge gris et n'apparaîtra pas dans les résultats de recherche de l'application LINE. |
| Compte vérifié | Un compte qui a passé la vérification LINE Yahoo. Ce compte est représenté par un badge bleu et apparaîtra dans les résultats de recherche de l'application LINE.<br><br>Ce compte est uniquement disponible pour les comptes basés au Japon, à Taïwan, en Thaïlande et en Indonésie. |
| Compte premium | Un compte qui a passé la vérification LINE Yahoo. Ce compte est représenté par un badge vert et apparaîtra dans les résultats de recherche de l'application LINE. Ce type de compte est automatiquement accordé lors de la vérification, à la discrétion de LINE. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de comptes LINE" }

### Type de compte requis {#required-account-type}

Pour synchroniser les abonnés dans Braze, votre compte LINE doit être vérifié ou premium. Lorsque vous créez un compte, son statut par défaut est non vérifié. Vous devrez demander la vérification du compte.

### Demander un compte LINE vérifié {#applying-for-a-verified-line-account}

{% alert important %}
Les comptes vérifiés sont uniquement disponibles pour les comptes basés au Japon, à Taïwan, en Thaïlande et en Indonésie.
{% endalert %}

1. Sur la page **Official Account** de LINE, sélectionnez **Settings**.
2. Sous **Information Disclosure Verification Status**, sélectionnez **Request Account Verification**.
3. Saisissez les informations requises.
4. Attendez une notification avec les résultats de l'examen.

## Intégration de LINE {#integrating-line}

Pour configurer des mises à jour utilisateur cohérentes, importer les ID LINE des utilisateurs existants et les synchroniser avec les états d'abonnement de LINE :

1. [Importer ou mettre à jour les utilisateurs LINE existants](#step-1-import-or-update-existing-line-users)
2. [Intégrer le canal LINE](#step-2-integrate-line-channel)
3. [Réconcilier les ID utilisateur](#step-3-reconcile-user-ids)
4. [Modifier les méthodes de mise à jour utilisateur](#step-4-change-your-user-update-methods)
5. [(Facultatif) Fusionner les profils utilisateur](#step-5-merge-profiles-optional)

{% alert note %}
Vous ne pouvez avoir qu'un seul compte LINE dans un même espace de travail. Si vous avez plusieurs comptes LINE, nous vous recommandons d'utiliser chacun dans un espace de travail différent.
{% endalert %}

## Étape 1 : Importer ou mettre à jour les utilisateurs LINE existants {#step-1-import-or-update-existing-line-users}

Cette étape est nécessaire si vous avez un utilisateur LINE existant et identifié, car Braze récupérera automatiquement son état d'abonnement et mettra à jour le profil utilisateur correspondant. Si vous n'avez pas encore réconcilié les utilisateurs avec leur ID LINE, passez cette étape.

Vous pouvez importer ou mettre à jour les utilisateurs en utilisant l'une des méthodes prises en charge par Braze, y compris l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), l'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Quelle que soit la méthode utilisée, mettez à jour le `native_line_id` pour fournir l'ID LINE de l'utilisateur. Pour en savoir plus sur le `native_line_id`, consultez [Configuration des utilisateurs](#user-setup).

{% alert note %}
L'état du groupe d'abonnement ne doit pas être spécifié et sera ignoré. LINE est la source de vérité pour le statut d'abonnement des utilisateurs, qui sera synchronisé avec Braze soit par l'outil de synchronisation des abonnements, soit par les mises à jour d'événements.
{% endalert %}

## Étape 2 : Intégrer le canal LINE {#step-2-integrate-line-channel}

Une fois le processus d'intégration terminé, Braze récupérera automatiquement les abonnés LINE de ce canal dans Braze. Pour tous les ID LINE déjà associés à un profil utilisateur Braze, chaque profil sera mis à jour avec le statut « abonné », et tous les ID LINE restants généreront des utilisateurs anonymes. De plus, les nouveaux abonnés de votre canal LINE auront des profils utilisateur non identifiés créés lorsqu'ils suivront le canal.

### Étape 2.1 : Modifier les paramètres du webhook {#step-21-edit-webhook-settings}

1. Dans LINE, accédez à l'onglet **Messaging API** et modifiez vos **Webhook settings** :
   - Définissez l'**URL du webhook** sur `https://anna.braze.com/line/events`.
      - Braze changera automatiquement cette URL lors de l'intégration, en fonction de votre cluster de tableau de bord.
   - Activez **Use webhook** et **Webhook redelivery**. <br><br> ![Page des paramètres du webhook pour vérifier ou modifier l'URL du webhook, activer ou désactiver « Use webhook », « Webhook redelivery » et « Error statistics aggregation ».]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Notez les informations suivantes dans l'onglet **Providers** :

| Type d'information | Emplacement |
| --- | --- |
| ID du fournisseur | Sélectionnez votre fournisseur puis accédez à **Settings** > **Basic information** |
| ID du canal | Sélectionnez votre fournisseur puis accédez à **Channels** > votre canal > **Basic settings** |
| Secret du canal | Sélectionnez votre fournisseur puis accédez à **Channels** > votre canal > **Basic settings** |
| Jeton d'accès au canal | Sélectionnez votre fournisseur puis accédez à **Channels** > votre canal > **Messaging API**. S'il n'y a pas de jeton d'accès au canal, sélectionnez **Issue**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2.1 : Modifier les paramètres du webhook" }

{% alert note %}
Si vous devez mettre à jour ou renouveler le secret du canal pour un canal LINE déjà intégré, contactez l'[assistance Braze]({{site.baseurl}}/braze_support) pour demander une mise à jour.
{% endalert %}

{: start="3"}
3. Accédez à votre page **Settings** > **Response settings** et procédez comme suit :
   - Désactivez **Greeting message**. Cela peut être géré dans Braze via un déclencheur lors du suivi.
   - Désactivez **Auto-response messages**. Tous les messages déclenchés doivent passer par Braze. Cela ne vous empêchera pas d'envoyer directement depuis la console LINE.
   - Activez **Webhooks**.

![Page des paramètres de réponse avec des bascules pour gérer la façon dont votre compte traite les conversations.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Étape 2.2 : Générer les groupes d'abonnement LINE dans Braze {#step-22-generate-line-subscription-groups-in-braze}

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Accédez à la page Partenaires technologiques de Braze pour LINE et saisissez les informations que vous avez notées depuis l'onglet **Providers** de LINE :
   - ID du fournisseur
   - ID du canal
   - Secret du canal
   - Jeton d'accès au canal

Si vous souhaitez ajouter une liste blanche d'adresses IP dans votre compte LINE, ajoutez toutes les adresses IP répertoriées pour votre cluster dans [Liste d'autorisation IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) à votre liste d'autorisation.

{% alert important %}
Lors de l'intégration, assurez-vous de vérifier que votre secret de canal est correct. S'il est incorrect, il peut y avoir des incohérences dans le statut d'abonnement.
{% endalert %}

![Page d'intégration de la messagerie LINE avec la section d'intégration LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. Après la connexion, Braze générera automatiquement un groupe d'abonnement Braze pour chaque intégration LINE ajoutée avec succès à votre espace de travail. <br><br> Toute modification de votre liste d'abonnés (comme de nouveaux abonnés ou des désabonnements) sera automatiquement transmise à Braze.

![Section des groupes d'abonnement LINE affichant un groupe d'abonnement pour le canal « LINE ».]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Étape 3 : Réconcilier les ID utilisateur {#step-3-reconcile-user-ids}

Combinez les ID LINE de vos utilisateurs avec leurs profils utilisateur Braze existants en suivant les étapes de la section [Réconciliation des ID utilisateur](#user-id-reconciliation).

## Étape 4 : Modifier vos méthodes de mise à jour utilisateur {#step-4-change-your-user-update-methods}

En supposant que vous disposez déjà d'une méthode pour fournir des mises à jour utilisateur à Braze, vous devrez la mettre à jour pour inclure le nouveau champ `native_line_id` afin que les mises à jour utilisateur ultérieures envoyées à Braze incluent ce champ.

Des profils utilisateur non identifiés avec un `native_line_id` peuvent exister dans Braze, créés dans le cadre du processus de synchronisation du statut d'abonnement ou lorsqu'un nouvel abonné a suivi votre canal.

Lorsqu'un utilisateur LINE est identifié dans votre application via la [réconciliation utilisateur](#user-id-reconciliation) ou d'autres moyens, vous pouvez cibler un profil utilisateur non identifié potentiel dans Braze en utilisant l'endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Chaque profil utilisateur non identifié avec un `native_line_id` possède également un alias d'utilisateur `line_id` qui peut être utilisé pour cibler le profil utilisateur à identifier.

Voici un exemple de payload pour `/users/identify` qui cible un profil utilisateur non identifié par l'alias d'utilisateur `line_id` :

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Si aucun profil utilisateur existant ne correspond à l'`external_id` fourni, il sera ajouté au profil utilisateur non identifié, le rendant identifié. Si un profil utilisateur existe pour l'`external_id`, tous les attributs qui sont exclusivement sur le profil utilisateur non identifié seront copiés vers le profil utilisateur connu, y compris `native_line_id` et le statut d'abonnement de l'utilisateur.

Vous pouvez mettre à jour les utilisateurs LINE connus dans votre application via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) en transmettant leurs identifiants externes et `native_line_id`. Si un profil utilisateur non identifié existe déjà pour un utilisateur et que le même `native_line_id` est ajouté à un profil utilisateur différent via `/users/track`, il héritera de tous les états d'abonnement du profil utilisateur non identifié. Cependant, des profils utilisateur en double existeront avec le même `native_line_id`. Toute mise à jour d'abonnement ultérieure provenant de mises à jour d'événements mettra à jour tous les profils en conséquence.

{% alert note %}
Les états d'abonnement LINE sont suivis par `native_line_id`, et non par `external_id`. Par exemple, si le profil utilisateur de l'utilisateur B est créé avec le même `native_line_id` que l'utilisateur A, mais pas le même `external_id`, l'utilisateur B hérite du statut d'abonnement LINE de l'utilisateur A.
{% endalert %}

Voici un exemple de payload pour `/users/track` qui met à jour un profil utilisateur par l'ID utilisateur externe pour ajouter un `native_line_id` :

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Étape 5 : Fusionner les profils (facultatif) {#step-5-merge-profiles-optional}

Comme décrit précédemment dans cette section, il est possible que plusieurs profils utilisateur existent avec le même `native_line_id`. Si vos méthodes de mise à jour créent des profils utilisateur en double, vous pouvez fusionner les profils utilisateur non identifiés avec les profils utilisateur identifiés à l'aide de l'endpoint `/user/merge`.

Voici un exemple de payload pour `/users/merge` qui cible un profil utilisateur non identifié par l'alias d'utilisateur `line_id` :

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Pour en savoir plus sur la gestion des utilisateurs en double dans Braze, consultez [Utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).
{% endalert %}

## Configuration des utilisateurs {#user-setup}

LINE est la source de vérité pour les états d'abonnement des utilisateurs. Même si vous disposez de l'ID LINE d'un utilisateur (`native_line_id`), si cet utilisateur n'a pas suivi le canal LINE depuis lequel vous envoyez, LINE ne lui délivrera pas de messages.

Pour faciliter la gestion, Braze propose des outils et une logique qui prennent en charge une base d'utilisateurs bien intégrée, y compris la synchronisation des abonnements et les mises à jour d'événements pour les suivis et désabonnements LINE.

### Synchronisation des abonnements et logique des événements {#subscription-syncing-and-event-logic}

1. **Outil de synchronisation des abonnements :** Cet outil est automatiquement déployé après une intégration réussie du canal LINE. Utilisez-le pour mettre à jour les profils existants et créer de nouveaux profils.<br><br>Tous les profils utilisateur Braze qui ont un `native_line_id` suivant le canal LINE seront mis à jour avec un statut de groupe d'abonnement `subscribed`. Tout abonné du canal LINE qui n'a pas de profil utilisateur Braze avec le `native_line_id` aura :<br><br>- Un profil utilisateur anonyme créé avec `native_line_id` défini sur l'ID LINE de l'utilisateur suivant le canal <br>- Un alias d'utilisateur `line_id` défini sur l'ID LINE de l'utilisateur suivant le canal <br>- Un statut de groupe d'abonnement `subscribed`

{: start="2"}
2. **Mises à jour d'événements :** Elles sont utilisées pour mettre à jour le statut d'abonnement d'un utilisateur. Lorsque Braze reçoit des mises à jour d'événements utilisateur pour le canal LINE intégré et que l'événement est un suivi, le profil utilisateur aura un statut de groupe d'abonnement `subscribed`. Si l'événement est un désabonnement, le profil utilisateur aura un statut de groupe d'abonnement `unsubscribed`.<br><br>- Tous les profils utilisateur Braze avec un `native_line_id` correspondant seront automatiquement mis à jour. <br>- Si aucun profil utilisateur correspondant n'existe pour un événement, Braze [créera un utilisateur anonyme]({{site.baseurl}}/line/user_management).

## Cas d'usage {#use-cases}

Voici des cas d'usage montrant comment les utilisateurs peuvent être mis à jour après avoir suivi les étapes de configuration.

### Un profil utilisateur Braze existant suit déjà le canal LINE {#existing-braze-user-profile-already-follows-line-channel}

1. Le profil utilisateur Braze est mis à jour avec un attribut `native_line_id`. Son statut d'abonnement par défaut est `unsubscribed`.
2. L'outil de synchronisation des abonnements est exécuté, détecte que l'utilisateur suit le canal LINE, puis met à jour le profil utilisateur avec le statut d'abonnement `subscribed`.
3. Si des changements de statut d'abonnement surviennent (comme le blocage, la suppression d'ami ou le réabonnement au canal par l'utilisateur), Braze reçoit la mise à jour de LINE et met à jour le profil utilisateur avec le `native_line_id` en conséquence.

#### Un profil utilisateur existant a bloqué, supprimé ou ne suit plus le canal LINE {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Le profil utilisateur Braze est mis à jour avec un attribut `native_line_id`. Son statut d'abonnement par défaut est `unsubscribed`.
2. L'outil de synchronisation des abonnements ne détecte pas que l'utilisateur suit le canal LINE et le statut d'abonnement de l'utilisateur reste `unsubscribed`.
3. Si l'utilisateur suit ultérieurement le canal, Braze reçoit la mise à jour de LINE et met à jour le profil utilisateur avec le statut d'abonnement `subscribed`.

##### La création du profil utilisateur intervient après le suivi LINE {#user-profile-creation-occurs-after-line-follow}

1. Le canal obtient un nouvel abonné LINE.
2. Braze crée un profil utilisateur anonyme avec l'attribut `native_line_id` défini sur l'ID LINE de l'abonné, et un alias d'utilisateur `line_id` défini sur l'ID LINE de l'abonné. Le profil a un statut d'abonnement `subscribed`.
3. L'utilisateur est identifié comme possédant l'ID LINE via la [réconciliation utilisateur](#user-id-reconciliation).
  - Le profil utilisateur anonyme peut être identifié en utilisant l'endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Les mises à jour ultérieures (via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), l'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) de ce profil utilisateur peuvent cibler l'utilisateur par cet `external_id` connu.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Un nouveau profil utilisateur peut être créé (via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), l'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) en définissant le `native_line_id`. Ce nouveau profil héritera de l'état d'abonnement du profil utilisateur anonyme existant. Notez que cela entraînera l'existence de plusieurs profils partageant le même `native_line_id`. Ceux-ci peuvent être fusionnés à tout moment en utilisant l'endpoint `/users/merge` dans le processus décrit à l'[étape 5](#step-5-merge-profiles-optional).

##### La création du profil utilisateur intervient avant le suivi LINE {#user-profile-creation-occurs-before-line-follow}

1. Vous acquérez un nouvel utilisateur et envoyez les informations à Braze. Un nouveau profil utilisateur est créé (profil 1).
2. L'utilisateur suit votre compte LINE.
3. Braze reçoit un événement de suivi et crée un profil utilisateur anonyme (profil 2).
4. L'utilisateur est identifié comme possédant l'ID LINE via la [réconciliation utilisateur](#user-id-reconciliation).
5. Vous mettez à jour le profil 1 pour définir l'attribut `native_line_id`. Ce profil hérite de l'état d'abonnement du profil 2.
  - Il y a maintenant deux profils utilisateur avec le même `native_line_id`. Ceux-ci peuvent être fusionnés à tout moment en utilisant l'endpoint `/users/merge` dans le processus décrit à l'[étape 5](#step-5-merge-profiles-optional).

## Réconciliation des ID utilisateur {#user-id-reconciliation}

Les ID LINE sont automatiquement reçus par Braze lorsqu'un utilisateur suit votre canal, ou lorsque vous utilisez le flux de travail unique « synchroniser les abonnés ». Les ID LINE sont également spécifiques au canal que les utilisateurs suivent, il est donc peu probable que les utilisateurs puissent fournir leurs ID LINE.

Il existe deux façons de combiner un ID LINE avec un profil utilisateur Braze existant :

- [Connexion LINE](#line-login)
- [Liaison de compte utilisateur](#user-account-linking)

### Connexion LINE {#line-login}

Cette méthode utilise les connexions via les réseaux sociaux pour la réconciliation. Lorsqu'un utilisateur se connecte à votre application, il a la possibilité d'utiliser [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) pour créer un compte utilisateur ou se connecter.

{% alert note %}
Pour obtenir l'ID LINE correct pour chaque utilisateur, configurez LINE Login sous le même fournisseur que votre compte officiel LINE ou canal intégré à Braze.
{% endalert %}

1. Accédez à la console développeur LINE et [demandez l'autorisation d'obtenir les adresses e-mail des utilisateurs](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) qui se connectent à votre application via LINE Login.

2. Suivez les étapes appropriées fournies par LINE pour implémenter LINE Login :<br><br>
  - [Instructions pour les applications web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Instructions pour les applications natives](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Assurez-vous d'inclure `email` dans la [configuration du scope](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) pour les demandes de vérification.

{: start="3"}
3. Utilisez l'[appel de vérification du jeton d'ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) pour obtenir l'adresse e-mail de l'utilisateur.

4. Enregistrez l'ID LINE de l'utilisateur (`native_line_id`) dans le profil de l'utilisateur avec une adresse e-mail correspondante dans votre base de données, ou créez un nouveau profil utilisateur avec l'adresse e-mail et l'ID LINE de l'utilisateur.

5. Envoyez les informations utilisateur nouvelles ou mises à jour à Braze en utilisant l'[endpoint `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users), l'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

#### Flux de travail {#workflows}

##### Un abonné existant utilise LINE Login {#existing-follower-uses-line-login}

**Scénario :** Un utilisateur anonyme a été créé lors de la synchronisation initiale des abonnés ou après l'intégration via un événement « suivi ».

1. L'utilisateur se connecte à votre application en utilisant LINE Login.
2. LINE vous fournit l'adresse e-mail de l'utilisateur.
3. Vous envoyez à Braze l'utilisateur mis à jour (le profil utilisateur existant avec cette adresse e-mail pour ajouter l'ID LINE) ou vous mettez à jour l'utilisateur anonyme avec l'adresse e-mail.

##### Un nouvel abonné utilise LINE Login {#new-follower-uses-line-login}

**Scénario :** Aucun profil utilisateur n'existe dans Braze avec l'ID LINE de l'utilisateur.

1. L'utilisateur se connecte à votre application en utilisant LINE Login.
2. LINE vous fournit l'adresse e-mail de l'utilisateur.
3. Vous pouvez soit :
  - Mettre à jour un profil utilisateur existant avec cette adresse e-mail pour y ajouter l'ID LINE de l'utilisateur.
  - Créer un nouveau profil utilisateur avec l'adresse e-mail et l'ID LINE.
4. Lorsque l'utilisateur suit votre compte officiel LINE, Braze reçoit un événement de suivi et met à jour le statut d'abonnement de l'utilisateur à `subscribed`.

### Liaison de compte utilisateur {#user-account-linking}

Cette méthode permet aux utilisateurs de lier leur compte LINE au compte utilisateur de votre application. Vous pouvez ensuite utiliser Liquid dans Braze, comme {% raw %}`{{line_id}}`{% endraw %}, pour créer une URL personnalisée pour l'utilisateur qui transmet l'ID LINE de l'utilisateur à votre site web ou application, où il peut ensuite être associé à un utilisateur connu.

1. Créez un Canvas basé sur une action qui se déclenche lors d'un changement d'état d'abonnement et qui se déclenche lorsqu'un utilisateur s'abonne à votre canal LINE.<br>![Canvas qui se déclenche lorsqu'un utilisateur s'abonne au canal LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Créez un message incitant les utilisateurs à se connecter à votre site web ou application, en transmettant l'ID LINE de l'utilisateur comme paramètre de requête (via Liquid), par exemple :

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Créez un message de suivi qui délivre le code de réduction.
4. (Facultatif) Créez une Campaign ou un Canvas basé sur une action qui se déclenche lorsque l'utilisateur LINE est identifié pour lui envoyer son code de réduction. <br>![Campaign basée sur une action qui se déclenche lorsque l'utilisateur LINE est identifié.]({% image_buster /assets/img/line/account_link_2.png %})

#### Fonctionnement {#how-it-works}

Après la connexion de l'utilisateur, une modification est effectuée sur votre site web ou application afin que l'ID utilisateur soit renvoyé à Braze pour l'associer à l'ID LINE transmis dans l'URL, avec un exemple de code tel que :

```javascript
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Flux de travail

##### Un utilisateur existant suit votre canal LINE {#existing-user-follows-your-line-channel}

**Scénario :** Un utilisateur existant dans Braze suit votre canal sur LINE.

1. LINE envoie un événement de suivi à Braze.
2. Braze crée un profil utilisateur anonyme avec l'ID LINE, l'alias d'utilisateur `line_id` et le statut de groupe d'abonnement LINE `subscribed`.
3. L'utilisateur reçoit un message LINE avec un lien vers votre site web et application et se connecte. Son profil utilisateur est maintenant connu.
4. Le profil utilisateur anonyme qui a été créé est identifié et fusionné via l'[endpoint /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) avec le profil utilisateur connu de l'utilisateur. Le profil utilisateur connu contient maintenant l'ID LINE et a un statut d'abonnement `subscribed`.
5. (Facultatif) L'utilisateur reçoit un message LINE avec le code de réduction et Braze enregistre l'envoi dans le profil utilisateur Braze.

## Création d'utilisateurs test LINE dans Braze {#creating-line-test-users-in-braze}

Vous pouvez tester votre canal LINE avant de configurer la [réconciliation des ID utilisateur](#user-id-reconciliation) en créant un Canvas ou une Campaign « Qui suis-je ».

1. Configurez un Canvas qui renvoie l'ID utilisateur Braze d'un utilisateur sur un mot déclencheur spécifique. <br><br>Exemple de déclencheur <br><br>![Déclencheur pour envoyer la Campaign aux utilisateurs qui ont envoyé un message LINE entrant à un groupe d'abonnement spécifique.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Exemple de message<br><br>![Message LINE indiquant l'ID utilisateur Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Dans Braze, vous pouvez utiliser l'ID Braze pour rechercher des utilisateurs spécifiques et les modifier selon vos besoins.

{% alert important %}
Assurez-vous que le Canvas ne dispose pas de contrôle global ou de groupes de contrôle empêchant les envois.
{% endalert %}