---
nav_title: Merkury
article_title: Merkury
description: "Cet article de référence décrit le partenariat entre Braze et Merkury, une plateforme d'identité d'entreprise pour vos applications, qui vous permet de tirer parti du `MerkuryID` pour augmenter les taux de reconnaissance des visiteurs du site pour les clients de Braze."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) est la plateforme d'identité d'entreprise de Merkle qui aide les marques à optimiser l'engagement et l'expérience client ainsi que leur chiffre d'affaires grâce à des fonctionnalités d'identité sans cookies first party. Le `MerkuryID` unifie les enregistrements des clients et prospects connus et inconnus d'une marque, les visites du site ou de l'application et les données sur les consommateurs en un seul identifiant personnel persistant.

_Cette intégration est maintenue par Merkury._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Merkury vous permet de tirer parti du `MerkuryID` pour augmenter les taux de reconnaissance des visiteurs du site pour les clients de Braze. Lorsqu'il reconnaît que des visiteurs sont abonnés à un service d'e-mail de la marque, Merkury met à jour le profil Braze pour y inclure l'adresse e-mail de l'abonné. Les capacités de reconnaissance accrues du `MerkuryID` améliorent les opportunités d'engagement et de personnalisation et augmentent immédiatement le nombre d'envois d'e-mails liés à l'abandon du site et le chiffre d'affaires associé.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Merkle | Un compte Merkle est nécessaire pour bénéficier de ce partenariat. |
| ID client Merkle | Obtenez votre ID client auprès de votre conseiller Merkle. |
| Balise Merkury | Placez la balise Merkury de Merkle sur votre site web. |
| Endpoint REST et SDK de Braze | Votre URL d'endpoint REST ou SDK. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Cette clé peut être créée dans **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Les requêtes du connecteur d'identité Merkury adressées à Braze fonctionnent dans le respect des spécifications de limite de débit de l'API Braze. Contactez Braze ou votre gestionnaire de compte Merkle si vous avez des questions.<br><br>Merkury envoie au moins une requête à la fin d'une session qualifiée.
{% endalert %}

## Intégration SDK côte à côte {#side-by-side-sdk-integration}

Utilise la balise Merkury côté client de Merkle pour capturer les appareils Braze et les transmettre à l'endpoint du connecteur d'identité Merkury pour identification.

### Étape 1 : Configurer la balise du SDK web de Braze {#step-1-setup-braze-web-sdk-tag}

Le [SDK web de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) doit être déployé sur votre site web pour utiliser cette intégration.

### Étape 2 : Déployer la balise Merkury de Merkle {#step-2-deploy-merkles-merkury-tag}

Déployez la balise Merkury sur votre site web pour rendre le connecteur d'identité Merkury disponible sur votre site web. Votre gestionnaire de compte Merkle vous fournira un guide détaillé avec des instructions.

### Étape 3 : Créer des attributs personnalisés {#step-3-create-custom-attributes}

Le connecteur d'identité Merkury renseigne les champs suivants, que vous devez créer dans Braze en tant qu'[attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes).

| Nom de l'attribut | Type de données | Description |
| --- | --- | --- |
| `hmid` | Chaîne de caractères | Identifiant Merkury de Merkle |
| `confidence_score` | Nombre | Le degré de confiance avec lequel Merkury a pu identifier l'utilisateur (1 à 8, plus le score est bas, mieux c'est) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 4 : Fournir à Merkle l'univers d'e-mails utilisateur {#step-4-provide-merkle-with-user-email-universe}

Merkle recommande une exportation par segmentation de votre univers d'e-mails autorisé. Cela peut être suivi par des exportations quotidiennes des utilisateurs autorisés actifs.

Les champs suivants sont requis :

- `braze_id`
- `external_id`
- adresse e-mail

Consultez votre conseiller Braze pour plus d'informations.