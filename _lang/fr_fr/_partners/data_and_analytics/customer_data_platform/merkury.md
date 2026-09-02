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

L'intégration de Braze et Merkury vous permet de tirer parti du `MerkuryID` pour augmenter les taux de reconnaissance des visiteurs du site pour les clients Braze. Lorsque Merkury reconnaît des visiteurs qui sont des utilisateurs abonnés aux e-mails de la marque, il met à jour le profil Braze pour inclure l'adresse e-mail de l'utilisateur abonné. Les capacités de reconnaissance accrues du `MerkuryID` améliorent les opportunités d'engagement et de personnalisation, et augmentent immédiatement les volumes d'envoi d'e-mails d'abandon de site ainsi que le chiffre d'affaires associé.

## Prérequis {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Merkle | Un compte Merkle est requis pour tirer parti de ce partenariat. |
| ID client Merkle | Obtenez votre ID client auprès de votre conseiller Merkle. |
| Balise Merkury | Placez la balise Merkury de Merkle sur votre site web. |
| Endpoint REST et SDK de Braze | L'URL de votre endpoint REST ou SDK. Votre endpoint dépendra de l'[URL Braze de votre instance]({{site.baseurl}}/api/basics#endpoints). |
| Clé API REST de Braze | Une clé API REST de Braze avec les permissions `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Celle-ci peut être créée dans **Tableau de bord de Braze > Console de développement > Clé API REST > Créer une nouvelle clé API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

{% alert important %}
Les requêtes du connecteur d'identité Merkury vers Braze respectent les spécifications de limitation du débit de l'API Braze. Contactez Braze ou votre gestionnaire de compte Merkle si vous avez des questions.<br><br>Merkury envoie au moins une requête à la fin d'une session qualifiée.
{% endalert %}

## Intégration SDK côte à côte {#side-by-side-sdk-integration}

Utilise le tag Merkury côté client de Merkle pour capturer les appareils Braze et les transmettre à l'endpoint du connecteur d'identité Merkury à des fins d'identification.

### Étape 1 : Configurer le tag du SDK Web de Braze {#step-1-setup-braze-web-sdk-tag}

Le [SDK Web de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-gtm) doit être déployé sur votre site web pour utiliser cette intégration.

### Étape 2 : Déployer le tag Merkury de Merkle {#step-2-deploy-merkles-merkury-tag}

Déployez le tag Merkury sur votre site web pour rendre le connecteur d'identité Merkury disponible sur votre site. Votre gestionnaire de compte Merkle vous fournira un guide détaillé avec les instructions.

### Étape 3 : Créer des attributs personnalisés {#step-3-create-custom-attributes}

Le connecteur d'identité Merkury renseigne les champs suivants, que vous devez créer dans Braze en tant qu'[attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Nom de l'attribut | Type de données | Description |
| --- | --- | --- |
| `hmid` | String | Merkury ID de Merkle |
| `confidence_score` | Number | Niveau de confiance de l'identification par Merkury (1-8, plus la valeur est basse, mieux c'est) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 3 : Créer des attributs personnalisés" }

### Étape 4 : Fournir à Merkle l'univers d'e-mails des utilisateurs {#step-4-provide-merkle-with-user-email-universe}

Merkle recommande une exportation de segmentation de votre univers d'e-mails autorisés. Celle-ci peut être suivie d'exportations quotidiennes des utilisateurs actifs autorisés.

Les champs suivants sont obligatoires :

- `braze_id`
- `external_id`
- adresse e-mail

Consultez votre conseiller Braze pour plus d'informations.