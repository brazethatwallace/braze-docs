---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Cet article de référence décrit le partenariat entre Braze et Knak, une plateforme de création de campagnes qui vous permet de créer des e-mails entièrement responsive en quelques minutes ou heures au lieu de jours ou de semaines, et de les exporter en tant que modèles Braze prêts à l'emploi."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) est la première plateforme de création de campagnes conçue pour être utilisée en interne par les équipes marketing d'entreprise. Sa plateforme de glisser-déposer permet à n'importe qui de créer de magnifiques e-mails et pages d'accueil conformes à l'image de marque en quelques minutes, sans avoir besoin de coder ni de faire appel à une aide extérieure.

_Cette intégration est maintenue par Knak._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Knak vous permet de créer des e-mails entièrement responsive en quelques minutes ou heures au lieu de jours ou de semaines, et de les exporter en tant que modèles Braze prêts à l'emploi. Knak est conçu pour les marketeurs qui veulent améliorer la création de leurs e-mails pour les campagnes gérées dans Braze, sans avoir besoin d'agences externes ou de codage manuel.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Knak | Un compte Knak est requis pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST Braze avec des autorisations complètes sur les **Modèles**. <br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation {#use-cases}

Knak est conçu pour les marketeurs qui veulent améliorer leur création d'e-mails, sans avoir besoin de coder ou de faire appel à une aide extérieure. C'est l'outil idéal pour ceux qui :
- Utilisent actuellement des modèles simples pour les e-mails et souhaitent passer au niveau supérieur
- Comptent sur des agences externes ou des développeurs pour créer des e-mails pour Braze
- Veulent reprendre le contrôle créatif de la création de ressources et arriver sur le marché beaucoup plus rapidement

## Intégration {#integration}

### Étape 1 : Configurer votre intégration {#step-1-configure-your-integration}

Dans Knak, accédez à **Integrations > Platforms > + Add New Integration**.

![Bouton d'ajout d'intégration]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

Ensuite, sélectionnez la plateforme **Braze** et fournissez la clé API Braze ainsi que l'endpoint REST. Cliquez sur **Create New Integration** pour finaliser votre intégration.

![Création d'une nouvelle intégration]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### Étape 2 : Synchroniser vos modèles Knak {#step-2-sync-your-knak-templates}

Dans Knak, localisez un e-mail que vous souhaitez synchroniser avec Braze et sélectionnez **Publish** puis **Sync**.

![Intégration Knak 1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

Ensuite, vérifiez le nom de l'e-mail et cliquez sur **Sync**.

![Intégration Knak 2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## Utilisation de l'intégration {#using-the-integration}

Vous pouvez retrouver vos e-mails Knak importés dans Braze sous **Engagement > Templates & Media**. Ils seront élégants, conformes à l'image de marque et entièrement responsive. La seule limite est votre propre créativité !