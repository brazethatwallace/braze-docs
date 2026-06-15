---
nav_title: Talkable
article_title: Talkable
description: "Cet article de référence décrit le partenariat entre Braze et Talkable, une plateforme de marketing de recommandation qui synchronise les abonnements marketing par e-mail issus de campagnes de recommandation vers Braze en temps réel."
alias: /partners/talkable/
page_type: partner
search_tag: Partner
---

# Talkable

> [Talkable](https://www.talkable.com/) aide les marques grand public à transformer leurs clients satisfaits en un canal de recommandation évolutif. Grâce à l'intégration avec Braze, les abonnements marketing par e-mail capturés dans les campagnes de recommandation Talkable sont transmis à Braze en temps réel, fournissant à votre équipe le consentement, le contexte et les données de campagne nécessaires pour accueillir, segmenter et engager chaque nouvel ambassadeur et ami.

_Cette intégration est maintenue par Talkable._

## À propos de l'intégration {#about-the-integration}

Talkable intègre l'acquisition par ambassadeurs dans le parcours client que Braze alimente. L'intégration transfère chaque abonnement de recommandation capturé par Talkable vers le profil Braze correspondant en temps réel, afin que les flux de bienvenue, les parcours de recommandation, la segmentation et les messages de cycle de vie puissent se déclencher à partir d'un consentement vérifié et d'un contexte de recommandation — le tout sans exports manuels de listes ni synchronisations par lots.

Talkable capture les abonnements marketing dans deux scénarios :

* **Inscription d'un ambassadeur :** Un ambassadeur s'inscrit à une campagne de recommandation Talkable et consent à recevoir des e-mails marketing.
* **Vérification par e-mail d'un ami :** Un ami complète l'étape de vérification par e-mail de Talkable et s'abonne aux e-mails marketing.

Dans les deux cas, Talkable crée ou met à jour le profil utilisateur Braze correspondant en temps réel et définit l'état d'abonnement e-mail de l'utilisateur sur **Opted In**.

### Comportement par défaut {#default-behavior}

Talkable envoie des données à Braze uniquement lors d'un événement d'abonnement explicite de la part d'une personne ayant donné son consentement dans Talkable — qu'il s'agisse d'un ambassadeur s'inscrivant à une campagne ou d'un ami s'abonnant lors de la vérification par e-mail. Talkable n'effectue pas de synchronisations nocturnes, de synchronisations complètes ni de mises à jour implicites de profils. Talkable n'envoie jamais à Braze de profils n'ayant pas donné leur consentement.

## Cas d'utilisation {#use-cases}

- Déclencher un Canvas de bienvenue Braze dès qu'un ambassadeur s'inscrit à une campagne de recommandation Talkable.
- Activer les amis recommandés avec un Canvas spécifique et une offre personnalisée de premier achat dès qu'un ami s'abonne.
- Segmenter par contexte de recommandation en utilisant les indicateurs d'ambassadeur et d'ami ainsi que les métadonnées de campagne envoyées comme attributs personnalisés Braze.
- Diriger les abonnements de recommandation vers un groupe d'abonnement Braze dédié pour un envoi de newsletter conforme à la réglementation.

## Conditions préalables {#prerequisites}

Avant de commencer, vous avez besoin des éléments suivants :

| Condition préalable | Description |
| --- | --- |
| Un compte Talkable | Un site Talkable avec au moins une campagne configurée est requis pour bénéficier de ce partenariat. |
| Une clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. Créez cette clé dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. Pour plus d'informations, consultez [Création de clés API REST]({{site.baseurl}}/api/basics/#creating-rest-api-keys). |
| Un endpoint REST Braze | L'URL de votre endpoint REST Braze (par exemple, `https://rest.iad-01.braze.com`). Les clusters Braze US (`.com`) et EU (`.eu`) sont pris en charge. Pour plus d'informations, consultez [Endpoints de la REST API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Installer l'application Braze dans Talkable {#step-1-install-the-braze-app-in-talkable}

1. Connectez-vous à votre interface d'administration Talkable et ouvrez le menu, puis accédez à **All Site Settings** > **App Store**.
2. Localisez **Braze** et sélectionnez **Install**.
3. Saisissez votre endpoint REST Braze et une clé API REST avec les autorisations `users.track`, puis sélectionnez **Save**.

### Étape 2 : Configurer l'action d'abonnement par e-mail {#step-2-configure-the-email-opt-in-action}

1. Dans l'application Braze de Talkable, ouvrez l'action **Email opt-in**.
2. (Facultatif) Saisissez un identifiant de groupe d'abonnement Braze, ajoutez des attributs personnalisés et/ou configurez un alias d'utilisateur. Pour plus d'informations, consultez [Personnaliser Talkable](#customizing-talkable).
3. Sélectionnez **Save**. Laissez l'action désactivée afin de pouvoir vérifier la configuration avec un payload de test avant que les événements d'abonnement en production ne commencent à se synchroniser.

### Étape 3 : Tester avec un payload d'exemple {#step-3-test-with-a-sample-payload}

1. Dans Talkable, sélectionnez **Send sample payload** sur l'action **Email opt-in** pour envoyer une requête de test à Braze.
2. Dans Braze, accédez à **Audience** > **Recherche d'utilisateurs** et recherchez par l'adresse e-mail de test.
3. Confirmez que le profil existe avec **Email Subscribe** défini sur **Opted In** et que tous les attributs personnalisés, l'inscription au groupe d'abonnement ou l'alias d'utilisateur que vous avez configurés apparaissent comme prévu.

### Étape 4 : Activer l'action pour le trafic en production {#step-4-enable-the-action-for-live-traffic}

Lorsque le profil de test est correct dans Braze, retournez dans Talkable et activez l'action **Email opt-in**.

À partir de ce moment, chaque événement d'abonnement Talkable synchronise le profil correspondant vers Braze en temps réel.

## Attributs utilisateur par défaut envoyés à Braze {#default-user-attributes-sent-to-braze}

À chaque événement d'abonnement, Talkable crée ou met à jour le profil utilisateur Braze correspondant avec les attributs utilisateur standard Braze suivants. Les valeurs vides sont omises.

| Attribut Braze | Type | Notes |
| --- | --- | --- |
| `email_subscribe` | Chaîne de caractères | Défini sur **Opted In** à chaque événement d'abonnement Talkable. |
| `email` | Chaîne de caractères | Identifiant principal utilisé pour faire correspondre le profil Braze. |
| `phone` | Chaîne de caractères | Capturé comme attribut utilisateur uniquement. Braze attend le format E.164 ; envoyé tel que stocké dans Talkable. |
| `first_name` | Chaîne de caractères | Le prénom de la personne. |
| `last_name` | Chaîne de caractères | Le nom de famille de la personne. |
| Inscription au groupe d'abonnement | Non applicable | Ajouté uniquement lorsqu'un groupe d'abonnement est configuré. L'utilisateur est inscrit comme abonné. |
| Alias d'utilisateur | Non applicable | Ajouté uniquement lorsqu'un alias d'utilisateur est configuré. Pour plus d'informations, consultez [Personnaliser Talkable](#customizing-talkable). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Attributs utilisateur par défaut envoyés à Braze" }

## Personnaliser Talkable {#customizing-talkable}

Les personnalisations facultatives suivantes sont disponibles. Configurez n'importe quelle combinaison ; elles sont indépendantes.

### Inscrire les abonnements dans un groupe d'abonnement Braze {#enroll-opt-ins-in-a-braze-subscription-group}

1. Dans Braze, copiez un identifiant de groupe d'abonnement depuis **Audience** > **Gestion des groupes d'abonnement**. Pour plus d'informations, consultez [Gestion des abonnements utilisateur]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).
2. Dans l'action **Email opt-in** de Talkable, collez-le dans le champ **Subscription group identifier**.

Talkable inscrit chaque abonnement dans ce groupe d'abonnement comme abonné, limitant les abonnements de recommandation à ce groupe plutôt qu'à un abonnement global. Talkable ajoute uniquement des abonnements ; il ne les supprime jamais.

### Envoyer des attributs personnalisés {#send-custom-attributes}

Ajoutez n'importe quelle paire clé-valeur dans l'éditeur de payload de l'action. La clé que vous saisissez devient le nom de l'attribut sur le profil utilisateur Braze.

Les valeurs utilisent des modèles Liquid. Les variables suivantes sont disponibles :

{% raw %}
| Variable | Contenu |
| --- | --- |
| `{{ person }}` | L'ambassadeur ou l'ami qui s'est abonné (`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties`, et plus). |
| `{{ ip }}` | L'adresse IP à partir de laquelle l'abonnement a eu lieu. |
| `{{ campaign }}` | La campagne Talkable d'origine (`name`, `type`, `tag_names`, et plus). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variables de modèle Liquid" }
{% endraw %}

{% raw %}
Exemple : ajoutez `talkable_is_advocate` = `{{ person.is_advocate }}` et `talkable_campaign_name` = `{{ campaign.name }}` pour segmenter par contexte de recommandation dans Braze.
{% endraw %}

### Identifier les utilisateurs avec des alias d'utilisateur Braze {#identify-users-with-braze-user-aliases}

Dans l'éditeur de payload, ajoutez `user_alias.alias_name` (par exemple, {% raw %}`{{ person.username }}`{% endraw %}) et `user_alias.alias_label` (par exemple, `username`). Pour plus d'informations, consultez [Objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/).

Lorsque les deux champs sont renseignés, le système identifie l'utilisateur par l'alias en plus de l'e-mail, et Braze crée un nouveau profil avec alias si aucune correspondance n'existe.

{% alert note %}
Les deux champs d'alias sont requis. Si seul l'un des deux champs `alias_name` ou `alias_label` est renseigné, Talkable n'envoie pas d'alias d'utilisateur et le profil est identifié uniquement par e-mail.
{% endalert %}

## Rechercher et créer des utilisateurs dans Braze {#find-and-create-users-in-braze}

* Par défaut, Braze fait correspondre le profil par adresse e-mail. Si aucun profil correspondant n'existe, Braze en crée un nouveau.
* Lorsqu'un alias d'utilisateur est configuré, Braze fait également correspondre par cet alias et crée un nouveau profil avec alias si aucune correspondance n'existe.
* Les ID externes ne sont pas utilisés par cette intégration. Pour rattacher les abonnements Talkable à un profil existant identifié de manière externe, configurez un alias d'utilisateur dont le libellé correspond à l'alias connu de ce profil.

## Utiliser Talkable avec Braze {#use-talkable-with-braze}

### Trouver un utilisateur synchronisé {#find-a-synced-user}

Accédez à **Audience** > **Recherche d'utilisateurs** et recherchez par e-mail pour afficher un profil créé ou mis à jour par Talkable.

Les champs standard (e-mail, téléphone, prénom ou nom de famille) et tous les attributs personnalisés que vous avez configurés apparaissent sur le profil ; **Email Subscribe** affiche **Opted In**.

### Créer un segment de recommandation {#build-a-referral-segment}

1. Créez un segment filtré sur **Email Subscribe** est **Opted In**.
2. Affinez avec les attributs personnalisés envoyés par Talkable — par exemple, `talkable_is_advocate` égal à `true` pour cibler les ambassadeurs, ou `talkable_campaign_name` égal à votre campagne pour cibler un programme de recommandation spécifique.

### Déclencher des messages de cycle de vie {#trigger-lifecycle-messaging}

1. Créez un Canvas ou une Campaign avec une livraison par événement. Les types de déclencheurs Braze suivants fonctionnent avec cette intégration :
* **Update Subscription Status** (par exemple, l'abonnement e-mail passe à **Opted In**)
* **Update Subscription Group Status** (lorsqu'un groupe d'abonnement est configuré)
* **Change Custom Attribute Value** (pour tout attribut personnalisé Talkable que vous envoyez).
2. Personnalisez les messages avec les attributs personnalisés Talkable présents sur le profil (nom de la campagne, valeur de la récompense, parrain, etc.).

## Considérations {#considerations}

* **Abonnement e-mail uniquement :** Les numéros de téléphone sont capturés comme attribut utilisateur standard, mais l'intégration ne définit pas d'état d'abonnement SMS. Talkable ne synchronise pas les abonnements SMS.
* **Format téléphonique :** Braze attend les numéros de téléphone au format international (E.164).
* **Synchronisation en temps réel, pilotée par événement :** Talkable envoie une requête par événement d'abonnement (un utilisateur par requête). Il n'y a pas de traitement par lots ni de synchronisation complète périodique ; le volume suit celui de vos abonnements de recommandation.
* **Livraison fiable :** Si Braze renvoie temporairement une erreur, Talkable effectue automatiquement de nouvelles tentatives. Les échecs persistants déclenchent une alerte par e-mail à l'administrateur du site.

## Résolution des problèmes {#troubleshooting}

| Erreur | Cause probable | Correction |
| --- | --- | --- |
| 401 Unauthorized | La clé API REST ne dispose pas des autorisations `users.track`, ou l'endpoint pointe vers le mauvais cluster. | Régénérez la clé avec les autorisations `users.track` et confirmez que l'endpoint REST correspond à votre cluster Braze. |
| Endpoint REST rejeté lors de l'installation | L'URL n'est pas un endpoint REST Braze. | Utilisez l'endpoint REST de votre cluster, par exemple `https://rest.iad-01.braze.com`. Une URL de tableau de bord ne fonctionne pas. |
| Profil créé mais absent du groupe d'abonnement | Aucun identifiant de groupe d'abonnement configuré. | Saisissez l'identifiant du groupe d'abonnement dans l'action **Email opt-in**. |
| Alias d'utilisateur non appliqué | Un seul des deux champs d'alias (nom ou libellé) est renseigné. | Renseignez les deux champs dans l'action : nom d'alias et libellé d'alias. |
| Profil non visible | La requête d'exemple n'a pas encore été envoyée, ou l'action est désactivée. | Sélectionnez **Send sample payload** dans Talkable et assurez-vous que l'action **Email opt-in** est activée. |
| Les requêtes ont cessé d'être envoyées après une rotation de clé | La clé API stockée a été révoquée ou remplacée dans Braze. | Dans l'**App Store** de Talkable, ouvrez l'application Braze, collez la nouvelle clé API REST et sélectionnez **Save** ; testez à nouveau avec **Send sample payload**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Résolution des problèmes" }

Pour plus d'informations sur l'intégration Talkable, consultez la [documentation d'intégration Talkable Braze](https://docs.talkable.com/email_marketing_and_automation/braze/). Pour contacter l'assistance Talkable, envoyez un e-mail à [support@talkable.com](mailto:support@talkable.com).