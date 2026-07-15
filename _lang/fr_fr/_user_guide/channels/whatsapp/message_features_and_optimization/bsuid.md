---
nav_title: Noms d'utilisateur et BSUID
article_title: Noms d'utilisateur WhatsApp et identifiants utilisateur à portée commerciale
page_order: 7
description: "Découvrez comment les noms d'utilisateur WhatsApp et les identifiants utilisateur à portée commerciale (BSUID) affectent l'identification des utilisateurs, l'envoi de messages et le traitement des données dans Braze."
page_type: reference
alias: "/whatsapp_usernames/"
channel:
  - WhatsApp
hidden: true
noindex: true
---

# Noms d'utilisateur WhatsApp et identifiants utilisateur à portée commerciale {#whatsapp-usernames-and-business-scoped-user-ids}

> En juin 2026, WhatsApp prévoit d'introduire les noms d'utilisateur : une fonctionnalité de confidentialité optionnelle qui masque les numéros de téléphone des utilisateurs lorsqu'ils communiquent avec des entreprises. Braze est entièrement préparé à gérer ce changement ; pour la plupart des clients, rien dans vos Campaigns ou Canvas n'a besoin de changer.

{% alert important %}
Les noms d'utilisateur WhatsApp et les identifiants utilisateur à portée commerciale (BSUID) devraient être lancés en juin 2026, avec des mises à jour de Braze synchronisées sur cette version. Les mises à jour de Braze décrites dans cet article **n'ont pas encore** été lancées.
{% endalert %}

Lorsque les utilisateurs WhatsApp adoptent un nom d'utilisateur, leur numéro de téléphone n'est plus automatiquement partagé avec les entreprises auxquelles ils envoient des messages. À la place, WhatsApp fournit aux entreprises un identifiant utilisateur à portée commerciale (BSUID), un identifiant unique spécifique à chaque paire portefeuille commercial/utilisateur.

Braze gérera les BSUID automatiquement. Les utilisateurs qui adoptent un nom d'utilisateur continueront d'apparaître dans votre espace de travail Braze, de recevoir des messages, de déclencher des Canvas et de générer des événements. Certains clients devront peut-être [se préparer au changement](#how-to-prepare-for-the-change).

## Identifiant utilisateur à portée commerciale (BSUID) {#business-scoped-user-id-bsuid}

Un BSUID est un identifiant unique et persistant que WhatsApp attribue pour représenter un utilisateur au sein de votre portefeuille commercial spécifique. Considérez-le comme un numéro de téléphone alternatif pour les utilisateurs qui choisissent de garder leur numéro de téléphone privé.

Les BSUID ont trois caractéristiques clés :

| Caractéristique | Description |
| ----- | ----- |
| Unique | Deux utilisateurs ne partagent jamais le même BSUID au sein de votre portefeuille commercial. |
| À portée commerciale | Le même utilisateur aura un BSUID différent avec chaque entreprise à laquelle il envoie des messages. Les BSUID ne peuvent pas être partagés ou comparés entre différents portefeuilles commerciaux. |
| Disponible dans les webhooks | Les BSUID sont inclus dans tous les mêmes payloads de webhook qui contiennent actuellement le numéro de téléphone de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifiant utilisateur à portée commerciale (BSUID)" }

## Changements des types d'utilisateurs WhatsApp {#changes-to-whatsapp-user-types}

Après le lancement des noms d'utilisateur WhatsApp, il y aura deux types d'utilisateurs WhatsApp :

| Type d'utilisateur | Identification WhatsApp | Ce que Braze reçoit |
| ----- | ----- | ----- |
| Utilisateurs sans nom d'utilisateur | Numéro de téléphone (aucun changement) | Numéro de téléphone (aucun changement) |
| Utilisateurs avec un nom d'utilisateur | Nom d'utilisateur (affiché), BSUID (backend) | BSUID, numéro de téléphone pour les utilisateurs ayant une conversation existante avec votre entreprise |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Changements des types d'utilisateurs WhatsApp" }

La différence clé est qu'un utilisateur qui adopte un nom d'utilisateur ne partage son numéro de téléphone avec votre entreprise que si vous aviez une conversation préalable avec lui ou s'il apparaît dans votre carnet de contacts WhatsApp.

## Comment Braze gérera les BSUID {#how-braze-will-handle-bsuids}

Braze stockera les BSUID en tant qu'[alias d'utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases) avec le libellé `whats_app_bsuid` sur le profil utilisateur. Cela signifie que les utilisateurs identifiés uniquement par BSUID auront des profils utilisateur Braze complets et pourront entrer dans des Canvas, recevoir des messages, générer des événements et être mis à jour via l'API.

### Envoi de messages {#send-messages}

Lorsque Braze envoie un message WhatsApp, il utilisera le numéro de téléphone s'il est disponible. Si l'utilisateur ne possède qu'un BSUID (par exemple, un utilisateur qui vous envoie un message pour la première fois après avoir adopté un nom d'utilisateur), Braze enverra le message en utilisant le BSUID à la place. Aucune modification de vos modèles de messages, Campaigns ou étapes Canvas n'est nécessaire.

### Messages entrants et déclencheurs Canvas {#inbound-messages-and-canvas-triggers}

Lorsqu'un utilisateur avec un nom d'utilisateur vous envoie un message WhatsApp entrant, Braze :

1. Recherchera l'utilisateur par BSUID ou numéro de téléphone (selon ce qui est disponible dans le webhook).
2. Si aucun utilisateur correspondant n'est trouvé, créera un nouveau profil utilisateur anonyme avec le BSUID stocké en tant qu'alias d'utilisateur.
3. Déclenchera tout Canvas ou toute Campaign configuré(e) pour démarrer à la réception d'un message WhatsApp entrant.

### Profil utilisateur {#user-profile}

Vous pourrez voir le BSUID d'un utilisateur sur son profil utilisateur Braze dans la section WhatsApp.

![Profil utilisateur avec une section WhatsApp contenant l'identifiant utilisateur à portée commerciale.]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### Groupes d'abonnement {#subscription-groups}

La gestion des groupes d'abonnement fonctionnera de la même manière pour les utilisateurs BSUID que pour tout utilisateur identifié par un alias d'utilisateur. Vous pouvez mettre à jour le statut d'abonnement des utilisateurs BSUID via :

- L'[endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) en utilisant `user_alias`
- L'étape Canvas [Mise à jour utilisateur]({{site.baseurl}}/user_update) (fonctionne automatiquement)
- L'import CSV

{% alert note %}
L'[endpoint subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) ne prendra pas en charge [`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object). Utilisez l'[endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour mettre à jour le statut d'abonnement des utilisateurs identifiés uniquement par BSUID.
{% endalert %}

### Currents et données d'événements {#currents-and-event-data}

Tous les événements Currents WhatsApp (envoi, réception, lecture, échec, message entrant reçu, abandon, nouvelle tentative) incluront un champ BSUID. Pour les utilisateurs qui possèdent à la fois un numéro de téléphone et un BSUID, les deux champs seront inclus. Pour les utilisateurs ne possédant qu'un BSUID, seul le champ BSUID sera inclus (le champ du numéro de téléphone sera vide).

## Comment se préparer au changement {#how-to-prepare-for-the-change}

Pour la plupart des clients, aucune action n'est requise. Braze gérera automatiquement le routage des BSUID, la création d'utilisateurs et le suivi des événements. Cependant, nous recommandons d'[activer le carnet de contacts WhatsApp](#enable-whatsapp-contact-book) et de [lier les portefeuilles commerciaux](#link-business-portfolios-if-you-use-multiple-wabas) si vous utilisez plusieurs comptes WhatsApp Business (WABA).

### Activer le carnet de contacts WhatsApp {#enable-whatsapp-contact-book}

Le carnet de contacts est une fonctionnalité Meta qui enregistre les numéros de téléphone des utilisateurs avec lesquels vous avez déjà conversé. Lorsqu'un utilisateur adopte un nom d'utilisateur, son numéro de téléphone reste visible pour votre entreprise s'il apparaît dans votre carnet de contacts. Cela signifie que Braze peut continuer à identifier les utilisateurs par numéro de téléphone même après qu'ils ont activé un nom d'utilisateur.

Pour activer le carnet de contacts :

1. Accédez à **Meta Business Suite** > **Business settings** > **Business info**.
2. Confirmez que la fonctionnalité Carnet de contacts est activée.

{% alert tip %}
La fonctionnalité Carnet de contacts est activée par défaut, mais nous vous recommandons de le confirmer dans vos paramètres Meta Business. Si le carnet de contacts est désactivé, les utilisateurs qui adoptent des noms d'utilisateur apparaîtront comme de nouveaux utilisateurs identifiés uniquement par BSUID, même si vous leur aviez précédemment envoyé des messages.
{% endalert %}

### Lier les portefeuilles commerciaux si vous utilisez plusieurs WABA {#link-business-portfolios-if-you-use-multiple-wabas}

Les BSUID sont limités à un seul portefeuille commercial. Si votre organisation gère des WABA provenant de plusieurs portefeuilles commerciaux au sein du même espace de travail Braze, le même utilisateur aura un BSUID différent pour chaque portefeuille. Cela peut entraîner des profils utilisateur Braze en double.

Pour éviter cela, contactez votre interlocuteur Meta pour vérifier si votre entreprise est éligible à la liaison de portefeuilles. Consultez [Lier les portefeuilles commerciaux et les BSUID parents](#link-business-portfolios-and-parent-bsuids) pour plus de détails.

Si tous vos WABA se trouvent dans le même portefeuille commercial, aucune action n'est nécessaire.

## Lier les portefeuilles commerciaux et les BSUID parents {#link-business-portfolios-and-parent-bsuids}

Si votre organisation exploite plusieurs comptes WhatsApp Business (WABA) répartis sur différents portefeuilles commerciaux, vous pouvez demander à votre interlocuteur Meta de vérifier si votre entreprise est éligible à la liaison de ces portefeuilles. L'éligibilité est déterminée par Meta et est disponible pour les entreprises gérées.

### Comportement des portefeuilles liés {#linked-portfolio-behavior}

Lorsque vos portefeuilles commerciaux sont liés, WhatsApp inclura un BSUID parent dans tous les webhooks de messages en plus du BSUID standard. Le BSUID parent sera attribué à une nouvelle propriété `parent_user_id` dans le payload du webhook.

Les BSUID parents ont les mêmes propriétés que les BSUID standard, mais seront partagés entre tous les numéros de téléphone professionnels au sein de votre ensemble de portefeuilles liés. Cela signifie que le même utilisateur aura un identifiant unique et cohérent quel que soit le WABA auquel il envoie des messages, évitant ainsi le risque de profils utilisateur en double.

Un BSUID parent inclut `ENT` entre l'indicatif du pays et l'identifiant alphanumérique. Par exemple :

```
US.ENT.11815799212886844830
```

Un BSUID standard n'inclut pas `ENT`.

### Comment Braze utilise les BSUID parents {#how-braze-uses-parent-bsuids}

Lorsqu'un webhook contient à la fois un BSUID standard et un BSUID parent, Braze utilisera le BSUID parent comme identifiant principal. Cela permet à un utilisateur qui envoie des messages à travers plusieurs WABA dans vos portefeuilles liés d'être systématiquement associé au même profil utilisateur Braze.

Si aucun BSUID parent n'est présent (par exemple, parce que vos portefeuilles ne sont pas liés ou que l'utilisateur envoie un message à un WABA non lié), Braze utilisera le BSUID standard. Les BSUID standard continueront de fonctionner normalement dans tous les cas.

{% alert note %}
Meta gère le processus de liaison des portefeuilles commerciaux. Pour commencer, contactez votre interlocuteur Meta. Vous pourrez toujours envoyer des messages aux utilisateurs en utilisant leur BSUID standard même si vos portefeuilles sont liés ; les BSUID parents sont complémentaires, pas un remplacement.
{% endalert %}

| Scénario | Identifiant utilisé par Braze |
| ----- | ----- |
| Portefeuille commercial unique | BSUID standard |
| Plusieurs portefeuilles liés | BSUID parent (préféré). Si aucun BSUID parent n'existe, utilise le BSUID standard |
| Plusieurs portefeuilles non liés | BSUID standard (peut entraîner des profils utilisateur en double par portefeuille) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comment Braze utilise les BSUID parents" }

## Questions fréquemment posées {#frequently-asked-questions}

### Mes Campaigns et Canvas existants cesseront-ils de fonctionner au lancement des noms d'utilisateur WhatsApp ? {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

Non. Les Campaigns et Canvas existants continueront de fonctionner. Les utilisateurs qui n'adoptent pas de nom d'utilisateur ne sont absolument pas affectés. Pour les utilisateurs qui adoptent un nom d'utilisateur et qui ont un historique de conversation existant avec votre entreprise, Braze continue d'utiliser leur numéro de téléphone comme identifiant principal.

### Que se passe-t-il pour un utilisateur qui adopte un nom d'utilisateur mais qui a déjà envoyé des messages à mon entreprise ? {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

Si votre carnet de contacts WhatsApp est activé et que vous avez eu une conversation préalable avec l'utilisateur (ou que vous lui avez envoyé un message) au cours des 30 derniers jours, son numéro de téléphone continue d'apparaître dans les payloads de webhook aux côtés du BSUID. Braze l'associera à son profil utilisateur existant. Aucun profil en double n'est créé.

### Que se passe-t-il si un utilisateur adopte un nom d'utilisateur et n'a aucune conversation préalable avec mon entreprise ? {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

Braze recevra le BSUID de l'utilisateur dans le webhook entrant et l'associera à un profil utilisateur existant (si vous avez précédemment stocké son BSUID) ou créera un nouveau profil utilisateur anonyme avec le BSUID stocké en tant qu'alias d'utilisateur. Cet utilisateur pourra alors entrer dans des Canvas, recevoir des messages sortants et être identifié ou fusionné avec d'autres profils à l'aide des outils standard de résolution d'identité de Braze.

### Puis-je cibler les utilisateurs BSUID dans des Segments ? {#can-i-target-bsuid-users-in-segments}

Les utilisateurs BSUID sont des profils utilisateur Braze complets, vous pouvez donc les cibler via les filtres d'audience standard (tels que « a reçu un message WhatsApp » ou l'appartenance à un groupe d'abonnement). Cependant, la segmentation spécifiquement sur les valeurs BSUID (comme « le BSUID existe » ou « le BSUID est égal à X ») n'est pas prise en charge.

### Comment fonctionne la tarification WhatsApp pour les utilisateurs BSUID ? {#how-does-whatsapp-pricing-work-for-bsuid-users}

La tarification des conversations WhatsApp est déterminée par le pays de l'utilisateur. Pour les utilisateurs identifiés par numéro de téléphone, Meta détermine le pays à partir de l'indicatif du pays du numéro de téléphone. Pour les utilisateurs identifiés par BSUID, le pays est encodé directement dans le BSUID lui-même ; par exemple, un BSUID commençant par `US` représente un utilisateur aux États-Unis.

Cela signifie que le comportement de tarification est cohérent, que l'utilisateur soit identifié par numéro de téléphone ou par BSUID. Le pays utilisé pour calculer les tarifs de conversation est déterminé par l'identifiant fourni par Meta, et Braze le transmet sans modification. Vous n'avez rien à faire différemment, mais sachez que lorsque vous envoyez des messages à des utilisateurs identifiés uniquement par BSUID, la tarification par pays de Meta est basée sur le pays encodé dans le BSUID de l'utilisateur plutôt que sur un numéro de téléphone.

### Comment référencer un utilisateur BSUID dans les appels API ? {#how-do-i-reference-a-bsuid-user-in-api-calls}

Utilisez le paramètre `user_alias` avec `alias_label: "whats_app_bsuid"` et `alias_name` défini sur la valeur BSUID de l'utilisateur. Par exemple :

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

Cela fonctionne avec `users/track`, `users/identify`, l'import CSV et l'étape Canvas Mise à jour utilisateur.

### Mes pipelines de données Currents seront-ils affectés ? {#will-my-currents-data-pipelines-break}

Les événements Currents pour WhatsApp incluent un champ `bsuid` aux côtés du champ de numéro de téléphone existant. Pour les utilisateurs ne possédant qu'un BSUID, le champ du numéro de téléphone est vide. Si vos pipelines en aval ont des exigences strictes sur le champ du numéro de téléphone, vérifiez qu'elles peuvent gérer une valeur nulle ou vide.

### J'ai plusieurs WABA répartis sur différents portefeuilles commerciaux. Le même utilisateur apparaîtra-t-il sous deux profils différents dans Braze ? {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

Sans portefeuilles liés, oui. Le même utilisateur WhatsApp aura un BSUID différent par portefeuille commercial, et Braze créera des profils distincts pour chacun.

Pour résoudre ce problème, contactez votre interlocuteur Meta pour vérifier l'éligibilité à la liaison de portefeuilles. Une fois liés, Meta fournit un BSUID parent partagé entre tous les portefeuilles, et Braze l'utilisera pour identifier l'utilisateur de manière cohérente à travers vos WABA. Consultez [Lier les portefeuilles commerciaux et les BSUID parents](#link-business-portfolios-and-parent-bsuids) pour plus de détails.

### Puis-je désactiver le carnet de contacts ? {#can-i-disable-the-contact-book}

Nous recommandons fortement de garder le carnet de contacts activé. Si le carnet de contacts est désactivé, tous les enregistrements historiques de numéros de téléphone de vos utilisateurs sont perdus. Les utilisateurs qui ont adopté des noms d'utilisateur apparaîtront alors comme de nouveaux utilisateurs identifiés uniquement par BSUID, même si vous leur aviez précédemment envoyé des messages.

## Ressources supplémentaires {#additional-resources}

* [Configuration de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)
* [Alias d'utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases)
* [Groupes d'abonnement WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
* [Événements Currents WhatsApp]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events#whatsapp)
* [Meta : identifiants utilisateur à portée commerciale](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)