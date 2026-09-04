---
nav_title: Convercus
article_title: Convercus
description: "Cet article de référence décrit le partenariat entre Braze et Convercus, une plateforme de fidélité et de coupons qui enrichit Braze avec des données de fidélité en temps réel et permet aux Campaigns Braze de déclencher des actions de fidélité dans Convercus."
page_type: partner
search_tag: Partner
---

# Convercus

> [Convercus](https://www.convercus.com/en) est une plateforme SaaS de fidélité et de coupons qui aide les marques et les enseignes à augmenter la fréquence d'achat, la valeur du panier et les taux de réachat grâce à des programmes de fidélité omnicanaux et des campagnes de coupons personnalisées.

_Cette intégration est maintenue par Convercus._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Convercus est bidirectionnelle : les données de fidélité sont transmises à Braze en temps réel sous forme d'attributs personnalisés, d'événements personnalisés et d'achats, tandis que les Canvas et les Campaigns Braze peuvent déclencher des actions de fidélité dans Convercus via des webhooks. Utilisez le niveau de membre synchronisé, le solde de points, les achats et l'activité des coupons dans les Segments, Liquid et le contenu connecté. Depuis les parcours Braze, vous pouvez également attribuer des coupons, enregistrer, accumuler et dépenser des transactions de points, et mettre à jour les préférences d'abonnement par e-mail dans Convercus.

Convercus héberge l'intégration, vous n'avez donc pas besoin d'installer d'infrastructure supplémentaire. Là où la plupart des connecteurs de fidélité ne transmettent les données que dans un seul sens, Convercus boucle la boucle : réagissez dans Braze à un événement de fidélité, effectuez une action dans Convercus, et mesurez le résultat directement dans Braze.

## Cas d'usage {#use-cases}

* **Célébration de montée en gamme :** Lorsqu'un membre progresse vers un niveau de fidélité supérieur dans Convercus, déclenchez un Canvas Braze personnalisé avec un message de bienvenue, un avantage exclusif lié au niveau, ainsi que le nouveau niveau et le solde de points du membre.
* **Bonus d'anniversaire et jalons :** Depuis un parcours Braze, créditez des points bonus dans Convercus pour l'anniversaire ou la date anniversaire d'inscription d'un membre, puis envoyez un message de célébration confirmant le nouveau solde.
* **Reconquête des membres inactifs :** Pour les membres inactifs, utilisez Braze pour attribuer un coupon personnalisé dans Convercus via un webhook et le distribuer par e-mail, notification push et messages in-app.
* **Solde de points en direct dans les messages :** Utilisez le contenu connecté pour récupérer le solde de points en temps réel d'un membre dans Braze Liquid, alimentant des cadences telles que « il ne vous reste que X points avant votre prochaine récompense ».

## Prérequis {#prerequisites}

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis | Description |
| --- | --- |
| Un compte Convercus | Un programme Convercus actif. Contactez votre gestionnaire de compte Convercus si vous n'êtes pas encore client. |
| Une clé API REST Braze | Une clé API REST Braze avec la permission `users.track`. Créez cette clé dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

Vous avez besoin d'un identifiant utilisateur cohérent entre les systèmes : la valeur utilisée comme `external_id` (ou le type d'identifiant choisi) dans Braze doit correspondre à l'identifiant membre correspondant dans Convercus. Dans le cas contraire, les événements ne sont pas attribués au bon profil.

## Intégration {#integration}

### Étape 1 : Configurer Braze dans Convercus Selfservice {#step-1-configure-braze-in-convercus-selfservice}

Dans Convercus Selfservice (l'interface d'administration destinée aux clients — ouvrez-la à l'aide de l'URL fournie par votre gestionnaire de compte Convercus), ouvrez le programme que vous souhaitez connecter à Braze et utilisez la **carte d'intégration Braze** pour :

1. Configurer la connexion Braze en complétant le formulaire d'intégration :

   | Champ | Description |
   | --- | --- |
   | `apiKey` | Votre clé API REST Braze (avec la permission `users.track`). |
   | `apiEndpoint` | Votre endpoint REST Braze, par exemple `https://rest.iad-01.braze.com`. |
   | Type d'identifiant | `external_id` ou `user_alias`. Détermine la façon dont les membres Convercus sont mis en correspondance avec les profils utilisateur Braze. |
   | `defaultOptins` | Sélection multiple des canaux d'abonnement du programme (à partir de `membershipOptins`). Utilisé comme valeur par défaut pour le webhook d'abonnement e-mail lorsque la requête ne fournit pas `optins`. La configuration Braze est considérée comme incomplète tant qu'au moins un canal n'a pas été sélectionné. |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1 : Configurer Braze dans Convercus Selfservice" }

2. Créer une clé API pour les appels entrants. Créez un identifiant `X-Convercus-Key` propre à chaque programme. La clé brute n'est affichée qu'une seule fois lors de la création, préfixée `cvc_` (format : `cvc_<base64url>`). Enregistrez-la dans Braze lorsque vous configurez les Campaigns de webhook et les blocs de contenu connecté à l'étape 2. Les clés peuvent être révoquées à tout moment depuis la même carte ; la révocation prend effet immédiatement.

Après l'enregistrement de la connexion Braze, Convercus commence immédiatement à diffuser les événements de fidélité de ce programme vers Braze. Aucune configuration d'infrastructure supplémentaire n'est requise.

{% alert note %}
Chaque programme Convercus est configuré de manière indépendante. Un même tenant Convercus peut connecter différents programmes à différents espaces de travail Braze, chacun avec sa propre clé API.
{% endalert %}

### Étape 2 : Configurer les webhooks dans Braze {#step-2-configure-webhooks-in-braze}

Pour déclencher des actions Convercus depuis un Canvas ou une Campaign, créez des actions de webhook Braze qui appellent le service d'intégration Convercus. Toutes les requêtes doivent inclure les en-têtes suivants :

- `X-Convercus-Key: cvc_…` — la clé API générée à l'étape 1.
- `Content-Type: application/json`

Tous les endpoints se trouvent sous l'URL de base `<SERVICE_HOST>/v1/programs/{programId}`. Remplacez `<SERVICE_HOST>` par l'hôte fourni par votre gestionnaire de compte Convercus et `{programId}` par l'identifiant de votre programme Convercus.

| Action | Endpoint |
| --- | --- |
| Attribuer un coupon à un membre | `POST /campaigns/{couponId}/assign` — renvoie `{ "couponCode": "..." }`. |
| Attribuer un coupon à plusieurs membres | `POST /campaigns/{couponId}/assign/batch` — jusqu'à 500 membres en un seul appel ; le corps accepte les paramètres optionnels `valid_from` / `valid_to`. Renvoie `{ "batchId": "..." }`. |
| Comptabiliser des points (gain / utilisation) | `POST /members/{accountId}/bookings` — crée un `EARNBOOKING` ou un `BURNBOOKING` sur le compte d'un membre. Renvoie `{ "bookingId": "..." }`. |
| Synchroniser les préférences d'abonnement e-mail | `POST /subscriptions/email` — définit les abonnements du membre sur `allowed` ou `declined`. Les canaux d'abonnement se résolvent selon la priorité : `optins` de la requête > `defaultOptins`. Renvoie `200` (tout OK), `207` (partiel — voir `succeeded` / `failed`), ou `400` (abonnements inconnus ou non configurés). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Configurer les webhooks dans Braze" }

Exemple — attribuer un coupon à un membre :

{% raw %}
```text
POST <SERVICE_HOST>/v1/programs/{programId}/campaigns/{couponId}/assign
X-Convercus-Key: cvc_…
Content-Type: application/json

{
  "account_id": "{{custom_attribute.${convercus_account_id}}}",
  "braze_campaign_id": "{{campaign.${api_id}}}"
}
```
{% endraw %}

Les autres actions suivent le même schéma, en ne modifiant que l'endpoint et le corps de la requête. Par exemple, une comptabilisation de points envoie un POST vers `/members/{accountId}/bookings` avec `booking_type` (`EARNBOOKING` ou `BURNBOOKING`), `booking_type_code`, `points` et `reason` ; le webhook d'abonnement e-mail envoie un POST vers `/subscriptions/email` avec `account_id` et `status` (`allowed` ou `declined`).

#### Réponses d'erreur et nouvelles tentatives {#error-responses-and-retries}

| Statut | Signification |
| --- | --- |
| `200` | Succès. |
| `207` | Multi-Status — uniquement pour le webhook d'abonnement e-mail, lorsque certaines adhésions ont été mises à jour et que d'autres ont échoué. |
| `400` | Le corps de la requête n'a pas passé la validation. |
| `401` | `X-Convercus-Key` est manquant ou invalide. |
| `5xx` | L'appel en amont vers Convercus a échoué. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réponses d'erreur et nouvelles tentatives" }

{% alert warning %}
Les réponses 5xx ne peuvent pas être réessayées en toute sécurité sans confirmer le succès — ces opérations ne sont pas idempotentes, et les nouvelles tentatives peuvent entraîner une double attribution de coupons ou un double crédit de points. Désactivez les nouvelles tentatives automatiques de Braze en cas de 5xx pour ces webhooks, ou configurez un nombre maximal de tentatives très faible.
{% endalert %}

### Étape 3 : Vérifier les données dans Braze {#step-3-verify-data-in-braze}

1. Déclenchez un événement de fidélité dans Convercus — par exemple, un changement de niveau de statut, une transaction de points ou l'utilisation d'un coupon.
2. Ouvrez l'utilisateur correspondant dans Braze et confirmez que l'attribut personnalisé, l'événement personnalisé ou l'achat attendu apparaît sur le profil. Les utilisateurs sont mis en correspondance par `external_id` (ou le type d'identifiant choisi à l'étape 1).
3. Pour vérifier le sens inverse, lancez un envoi de test Braze qui appelle l'un des webhooks de l'étape 2 et confirmez l'action dans Convercus (coupon attribué, points comptabilisés ou abonnement mis à jour).

## Utiliser Convercus avec Braze {#use-convercus-with-braze}

### Étape 1 : Personnaliser les messages avec les données de fidélité synchronisées {#step-1-personalize-messages-with-synced-loyalty-data}

Une fois l'intégration en service, les événements Convercus arrivent sur chaque profil utilisateur dans Braze via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) et peuvent être utilisés comme n'importe quelle autre donnée native :

1. Utilisez les attributs personnalisés de fidélité (par exemple, `convercus_status_level`, `convercus_balance`) dans les **Segments** pour cibler les détenteurs d'un palier, les membres à solde élevé ou les utilisateurs récemment rétrogradés.
2. Utilisez les événements personnalisés (par exemple, `convercus_status_level_changed`, événements de coupons et d'adhésion) comme **étapes de déclenchement** dans Canvas ou comme filtres dans les Campaigns de réengagement.
3. Référencez n'importe lequel de ces champs en **Liquid** pour la personnalisation dans les messages (lignes d'objet, corps du message, titres de notification push).
4. Utilisez les événements `purchase` transmis depuis Convercus pour alimenter des parcours orientés produit (réapprovisionnement, montée en gamme par catégorie, demandes d'avis post-achat).

#### Attributs personnalisés {#custom-attributes}

| Attribut | Description |
| --- | --- |
| `convercus_account_id` | L'identifiant de compte Convercus du membre — unique au sein d'un programme Convercus / espace de travail Braze. |
| `convercus_user_id` | L'identifiant utilisateur Convercus identifiant la personne sous-jacente à travers plusieurs programmes Convercus. |
| `convercus_partner_id` | Identifiant du partenaire Convercus (commerçant/marque) par lequel ce membre s'est inscrit. Utile pour la segmentation dans les programmes de coalition. |
| `convercus_member_role` | Le rôle du membre au sein du programme de fidélité. |
| `convercus_status_level` | Le palier ou niveau de statut actuel du membre. |
| `convercus_balance` | Objet contenant les `points`, `lockedPoints` et `statusPoints` actuels du membre. |
| `email_subscribe` | État d'abonnement e-mail dérivé des consentements Convercus (`opted_in`, `subscribed` ou `unsubscribed`). |
| `push_subscribe` | État d'abonnement push dérivé des événements de jeton push Convercus (`opted_in` ou `unsubscribed`). |
| Champs de profil standard | `email`, `phone`, `first_name`, `last_name`, `dob`, `gender`, `home_city`, `country`. |
| Propriétés utilisateur personnalisées | Toutes les propriétés personnalisées définies sur l'objet utilisateur Convercus sont transmises en tant qu'attributs personnalisés Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés" }

{% alert note %}
Au sein d'un espace de travail Braze, les membres sont identifiés de manière unique par `convercus_account_id`. `convercus_user_id` identifie la personne sous-jacente à travers plusieurs programmes Convercus et est fourni pour l'analyse inter-programmes ; pour la segmentation dans Braze, utilisez `convercus_account_id`.
{% endalert %}

**Mappage `email_subscribe`**

| État Convercus | `email_subscribe` Braze |
| --- | --- |
| Entrée `allowedOptins` pour `email consent` ou `newsletter` | `opted_in` |
| Entrée `declinedOptIns` pour ces canaux (et aucune entrée autorisée) | `unsubscribed` |
| Aucun enregistrement dans un sens ou l'autre | `subscribed` (valeur neutre par défaut de Braze) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés" }

#### Événements personnalisés {#custom-events}

| Événement | Déclenché lorsque |
| --- | --- |
| `convercus_account_created` | Un nouveau compte est créé dans Convercus. |
| `convercus_membership_added` | Un compte existant rejoint un programme de fidélité. |
| `convercus_membership_created` | Une nouvelle adhésion est créée. |
| `convercus_membership_changed` | Les données d'une adhésion changent. |
| `convercus_membership_optins_changed` | Les préférences de consentement d'un membre changent. |
| `convercus_membership_terminated` | Une adhésion prend fin. |
| `convercus_status_level_changed` | Le palier ou niveau de statut d'un membre change. |
| `convercus_balance_changed` | Le solde de points d'un membre change. |
| `convercus_account_transaction` | Une transaction de fidélité est évaluée. |
| `convercus_coupon_assigned` | Un coupon est attribué au membre. |
| `convercus_coupon_redeemed` | Le membre utilise un coupon. |
| `convercus_user_logged_in` | Le membre se connecte à une interface propulsée par Convercus. |
| `convercus_user_logged_out` | Le membre se déconnecte. |
| `convercus_user_created` | Un nouvel utilisateur est créé. |
| `convercus_user_changed` | Les données de profil d'un utilisateur changent. |
| `convercus_push_token_created` | Un jeton push est enregistré pour le membre. |
| `convercus_push_token_deleted` | Un jeton push est supprimé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements personnalisés" }

#### Achats {#purchases}

Les transactions Convercus de type `EARNTRANSACTION` (points gagnés à partir des dépenses du client) sont transmises à Braze en tant qu'[achats]({{site.baseurl}}/api/objects_filters/purchase_object) et comptabilisées dans l'analyse des revenus Braze, la segmentation RFM et les fonctionnalités prédictives — en utilisant l'identifiant de transaction comme identifiant produit, et le montant et la devise de la transaction comme prix et devise.

Les transactions de type `PAYWITHPOINTSTRANSACTION` (utilisation de points) ne sont **pas** transmises en tant qu'achats — elles sont envoyées sous forme d'événement personnalisé `convercus_account_transaction` afin de rester disponibles pour la segmentation. Les annulations et les remboursements des transactions de gain sont transmis comme des achats à prix négatif, ce qui maintient l'alignement des revenus Braze avec Convercus.

### Étape 2 : Récupérer les données de fidélité en temps réel avec le contenu connecté {#step-2-fetch-live-loyalty-data-with-connected-content}

Pour les valeurs qui doivent être à jour au moment de l'envoi — solde de points actuel, coupons actifs, dernier palier — appelez Convercus depuis Braze en utilisant le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) au lieu de vous appuyer sur le dernier attribut synchronisé. Les deux endpoints partagent la même URL de base que les webhooks et nécessitent l'en-tête `X-Convercus-Key`.

| Données | Endpoint | Retourne |
| --- | --- | --- |
| Profil du membre | `GET /members/{accountId}/profile` | `member_id`, `first_name`, `last_name`, `email`, `tier_name`, `tier_id`, `points_balance`, `enrollment_date`. |
| Coupons du membre | `GET /members/{accountId}/coupons` | Liste des coupons actifs et échangeables (statut, valeur, période de validité, titre, description). Ajoutez `?lang=<code>` (par exemple, `?lang=de`) pour localiser `title`/`description` ; la valeur par défaut est `en`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Récupérer les données de fidélité en temps réel avec le contenu connecté" }

Les endpoints de contenu connecté renvoient toujours HTTP 200 en cas d'échecs attendus afin que les modèles Liquid puissent se brancher sur le champ `error` :

| Réponse | Signification |
| --- | --- |
| `200` + payload | Succès. |
| `200 { "error": "member_not_found" }` | Le compte n'existe pas dans ce programme. |
| `200 { "error": "internal_error" }` | Échec en amont ou inattendu. |
| `401` | `X-Convercus-Key` est manquant ou invalide (à gérer lors de l'intégration, pas en Liquid). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Récupérer les données de fidélité en temps réel avec le contenu connecté" }

Exemple — afficher le statut de fidélité d'un membre (palier, points et offres actives) :

{% raw %}
```liquid
{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/profile
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 300
  :retry
  :save member
%}

{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/coupons?lang=en
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 0
  :retry
  :save coupon_data
%}

{% unless member.error %}
  <h2>Your Loyalty Status</h2>
  <p>Hi {{member.first_name}}, you're a <strong>{{member.tier_name}}</strong> member.</p>
  <p>Points balance: <strong>{{member.points_balance}}</strong></p>

  {% if coupon_data.coupons.size > 0 %}
    <h3>Your Active Offers</h3>
    {% for coupon in coupon_data.coupons %}
      <p><strong>{{coupon.title}}</strong> — valid until {{coupon.valid_to}}</p>
    {% endfor %}
  {% endif %}
{% endunless %}
```
{% endraw %}

Enveloppez toujours le contenu connecté dans des conditions (vérifiez `member.error` et `coupons` vide) afin qu'un échec temporaire de la recherche n'envoie jamais un message défectueux. Mettez en cache le profil (`cache_max_age 300`) mais pas les coupons (`cache_max_age 0`), car le statut des coupons peut changer entre les envois.

## Considérations {#considerations}

- **Latence :** Les événements Convercus-vers-Braze se propagent via Kafka et atteignent Braze en quelques secondes en charge normale.
- **Limites de débit Braze :** L'intégration réessaie automatiquement en cas de réponse `429`, en respectant l'en-tête `x-ratelimit-retry-after` de Braze avec des délais exponentiels.
- **Mise en cache du contenu connecté :** Braze met en cache les réponses du contenu connecté pendant plusieurs minutes par défaut. Pour les valeurs qui doivent être exactes au moment de l'envoi (comme le solde de points), réduisez ou contournez la fenêtre de cache dans l'appel de contenu connecté.
- **Une configuration par programme :** Chaque programme de fidélité correspond à un seul espace de travail Braze. Pour connecter un second espace de travail, configurez-le sur un programme distinct.
- **Observabilité :** Les statistiques d'appels API par programme et l'historique des erreurs (dans les deux sens) sont conservés pendant 90 jours et accessibles depuis la carte d'intégration Braze dans Selfservice.

## Résolution des problèmes {#troubleshooting}

- **Les événements n'apparaissent pas dans Braze :** Vérifiez que la valeur utilisée comme identifiant (sélectionnée à l'étape 1) correspond à l'`external_id` (ou au type d'identifiant choisi) de l'utilisateur dans Braze. Des identifiants non concordants entraînent l'attribution des événements au mauvais profil ou leur rejet.
- **Le webhook renvoie `401` :** L'en-tête `X-Convercus-Key` est manquant ou la clé API `cvc_…` a été révoquée. Régénérez la clé dans Selfservice et mettez à jour l'action webhook dans Braze.
- **Le webhook renvoie `400` :** La requête ne contient pas `Content-Type: application/json`, ou le payload ne correspond pas au schéma documenté. Pour le webhook d'abonnement e-mail, un `400` signifie également que les opt-ins demandés sont inconnus du programme ou qu'aucun n'est configuré.
- **Débogage approfondi :** Consultez les statistiques d'appels API par programme et l'historique des erreurs sur la carte d'intégration Braze dans Selfservice, ou contactez votre conseiller Convercus.