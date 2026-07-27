---
nav_title: Shopify pour Currents
article_title: Shopify pour Currents
description: "Cet article de référence décrit le partenariat entre Braze Currents et Shopify, une entreprise de commerce mondial qui vous permet de connecter Braze à votre boutique Shopify de façon fluide pour alimenter les rapports internes et mieux suivre l'attribution au dernier point de contact pour les achats."
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify pour Currents {#shopify-for-currents}

> [Shopify](https://www.shopify.com/) est une entreprise de commerce mondial de premier plan qui fournit des outils fiables pour créer, développer, commercialiser et gérer une entreprise de toute taille. La plateforme et les services de Shopify sont conçus pour offrir une fiabilité optimale tout en proposant une meilleure expérience d'achat aux consommateurs partout dans le monde.

{% alert important %}
Cette intégration est actuellement en version bêta. Pour plus d'informations, contactez votre gestionnaire de la satisfaction client Braze.
{% endalert %}

L'intégration de Braze avec Shopify offre une solution puissante pour les entreprises eCommerce qui souhaitent améliorer leur engagement client et mener des actions marketing personnalisées. Avec [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), vous pouvez connecter des données à Shopify pour alimenter les rapports internes et mieux suivre l'attribution au dernier point de contact pour les achats.

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Currents | Pour exporter des données vers Shopify, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) pour votre compte. |
| Boutique Shopify | Assurez-vous d'avoir déjà [configuré au moins une boutique Shopify avec Braze]({{site.baseurl}}/shopify_standard_integration). |
| Autorisations de propriétaire ou de membre du personnel de la boutique Shopify | {::nomarkdown}<ul><li>Accès à tous les paramètres <b>Général</b> et <b>Boutique en ligne</b>.</li><li> Autorisations d'administrateur supplémentaires :</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

### Étape 1 : Configurer votre boutique Shopify {#step-1-set-up-your-shopify-store}

Si ce n'est pas déjà fait, suivez les étapes de [configuration de l'intégration standard Shopify]({{site.baseurl}}/shopify_standard_integration) pour configurer au moins une boutique Shopify avec Braze.

### Étape 2 : Créer un Braze Current {#step-2-create-braze-current}

1. Dans Braze, accédez à **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**.
2. Indiquez un nom d'intégration et une adresse e-mail de contact.
3. Dans la section **Credentials**, sélectionnez la boutique Shopify que vous avez configurée à l'[étape 1](#step-1-set-up-your-shopify-store).
4. Sélectionnez les événements que vous souhaitez suivre. Une liste des événements disponibles est fournie.
5. Sélectionnez **Launch Current**.

![La page Braze Shopify Currents. Cette page comprend des champs pour le nom de l'intégration, l'adresse e-mail de contact et la boutique Shopify.]({% image_buster /assets/img/shopify/shopify_currents.png %})

## Synchronisation du profil utilisateur {#user-profile-sync}

En plus des données d'événements, l'intégration Shopify peut synchroniser les mises à jour de profils utilisateur de Braze vers votre boutique Shopify. Lorsque le profil d'un utilisateur est mis à jour dans Braze, Currents crée ou met à jour le client correspondant dans votre boutique.

### Correspondance des utilisateurs {#user-matching}

Braze fait correspondre les clients Shopify en utilisant le `user_id` de Braze comme [identifiant personnalisé](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSet) Shopify (`customId`) avec l'espace de noms `braze` et la clé `user_id`. Si aucun client avec cet identifiant n'existe dans votre boutique, un nouveau client est créé. Les utilisateurs anonymes ne sont pas synchronisés.

### Mappage des champs {#field-mapping}

Les champs de profil Braze suivants sont synchronisés vers Shopify :

| Champ Braze | Champ client Shopify | Notes |
| ----------- | -------------------- | ----- |
| `first_name` | `firstName` | Mappé tel quel. Envoyé uniquement lorsqu'il est présent dans la mise à jour du profil. |
| `last_name` | `lastName` | Mappé tel quel. Envoyé uniquement lorsqu'il est présent dans la mise à jour du profil. |
| `email_address` | `email` | Les espaces sont supprimés et le texte est converti en minuscules avant l'envoi. |
| `phone_number` | `phone` | Envoyé au format [E.164](https://en.wikipedia.org/wiki/E.164). |
| `language` | `locale` | Converti en une locale prise en charge par Shopify. Le portugais et le chinois se voient attribuer une variante régionale (telle que `pt-BR`) en fonction du pays de l'utilisateur. Si la langue de l'utilisateur n'est pas prise en charge par Shopify, ce champ est omis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Seuls les champs présents dans une mise à jour de profil sont envoyés. Les champs omis d'une mise à jour restent inchangés dans Shopify — une synchronisation ne supprime ni n'efface jamais un champ de votre client Shopify.

### Champs non synchronisés {#fields-that-are-not-synced}

L'intégration n'écrit pas actuellement de métachamps Shopify, de sorte que les champs de profil qui nécessiteraient un métachamp ne sont pas synchronisés. En particulier, les attributs personnalisés ne sont pas envoyés à Shopify. Les autres champs non envoyés sont `external_user_id`, `gender`, `dob` (date de naissance), `timezone`, `home_city`, `country` et `archived`.

Braze peut créer des définitions de métachamps sous l'espace de noms `braze` dans votre boutique (par exemple, `braze.gender`). Ces définitions sont réservées pour une utilisation future potentielle — Braze n'y écrit actuellement aucune valeur. L'exception est `braze.user_id`, qui stocke l'identifiant utilisé pour faire correspondre vos clients.