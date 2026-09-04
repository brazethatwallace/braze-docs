---
nav_title: Taxi
article_title: Taxi
alias: /partners/taxi_for_email
description: "Cet article de référence décrit le partenariat entre Braze et Taxi, un outil de marketing par e-mail en ligne qui permet aux clients de Braze de créer des modèles d'e-mail intelligents en utilisant leur interface de glisser-déposer et une syntaxe simple mais puissante."
page_type: partner
search_tag: Partner

---

# Taxi

> [Taxi](http://taxiforemail.com/) est un outil de marketing par e-mail en ligne qui offre un éditeur d'e-mails visuel intuitif par glisser-déposer. Taxi encourage les équipes à collaborer facilement sur des campagnes d'e-mail, permettant aux rédacteurs et éditeurs d'avoir l'accès et les ressources dont ils ont besoin pour créer des e-mails, le tout sans code.

_Cette intégration est assurée par Taxi._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Taxi utilise la syntaxe simple mais puissante de Taxi pour créer et exporter des modèles d'e-mails intelligents vers Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ------------| ----------- |
| Compte Taxi | Un compte Taxi est requis pour profiter de ce partenariat. |
| Clé REST API de Braze | Une clé REST API de Braze avec toutes les autorisations **Modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint Braze | [Votre endpoint Braze]({{site.baseurl}}/api/basics/#endpoints) correspond à l'URL de votre tableau de bord de Braze.<br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer un modèle d'e-mail Taxi {#step-1-create-a-taxi-email-template}

Créez un modèle Taxi sur la plateforme Taxi. Une fois le modèle créé, accédez à vos **Organization Settings** et sélectionnez l'onglet **fournisseur de services d'e-mailing Connectors**.

### Étape 2 : Créer un connecteur Braze {#step-2-create-braze-connector}

1. Dans la boîte de dialogue qui s'affiche, cliquez sur le bouton **Add New**, puis sélectionnez **Braze** dans la liste déroulante.
2. Sélectionnez **Braze** pour modifier les paramètres du connecteur Braze.
3. Saisissez votre endpoint Braze et votre clé API Braze.

Votre champ de connecteur changera de couleur une fois que les informations avec les autorisations correctes auront été fournies. Si ce champ ne change pas, vérifiez que vos champs correspondent aux exigences indiquées.

## Utilisation {#usage}

Retrouvez le modèle Taxi que vous avez importé dans la section **Templates & Media > Email Templates** de votre compte Braze. Vous pouvez désormais utiliser ce modèle d'e-mail pour commencer à envoyer des e-mails attrayants à vos clients !