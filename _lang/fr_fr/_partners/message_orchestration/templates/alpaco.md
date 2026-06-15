---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "L'intégration entre Braze et Alpaco vous permet d'exporter vers Braze des modèles d'e-mail et des blocs de contenu conformes à la marque et compatibles avec Liquid, prêts à être utilisés dans les e-mails et les messages in-app."
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/) est un outil de gestion créative en ligne qui offre un éditeur par glisser-déposer permettant de créer du contenu réutilisable et conforme à la marque pour Braze. L'intégration d'Alpaco et de Braze vous permet d'exporter des Content Blocks, des modèles d'e-mail et des modèles de messages in-app.

_Cette intégration est maintenue par Alpaco._

{% alert note %}
Alpaco prend en charge l'[intégralité des variables Liquid](https://shopify.github.io/liquid/) et, à ce titre, prend également en charge toutes les variables Liquid utilisées dans vos configurations Braze.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ------------| ----------- |
| Compte Alpaco | Un compte Alpaco est nécessaire pour tirer parti de ce partenariat. |
| Clé API REST de Braze | Une clé API REST Braze avec l'ensemble des autorisations **Modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze correspond à votre tableau de bord Braze et à votre endpoint REST. <br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

- Exportez des **modèles d'e-mail** entièrement conçus pour les Campaigns Braze et l'envoi de messages transactionnels.
- Créez et gérez des **blocs de contenu modulaires** (par exemple, en-têtes, pieds de page, promotions) réutilisables sur plusieurs canaux.
- Concevez des **messages in-app** attrayants avec la même flexibilité créative que les e-mails, ce qui permet de proposer facilement des expériences cohérentes et conformes à la marque sur l'ensemble des canaux.
- Activez la **personnalisation** en incluant des étiquettes Liquid prises en charge par Braze, telles que `{{first_name}}` ou `{{custom_attribute}}`.
- Maintenez la **cohérence de la marque** en centralisant la conception créative dans Alpaco et en poussant les mises à jour vers Braze en une seule exportation.

## Intégration {#integration}

Fournissez votre clé API REST Braze et votre instance de cluster à l'équipe satisfaction client d'Alpaco. L'équipe mettra ensuite en place l'intégration initiale pour vous.

{% alert note %}
Il s'agit d'une configuration unique et toutes les exportations futures utiliseront automatiquement cette clé API.
{% endalert %}

## Exportation des messages d'Alpaco vers Braze {#exporting-alpaco-messages-to-braze}

### Étape 1 : Créer un modèle dans Alpaco {#step-1-create-a-template-in-alpaco}

Dans Alpaco, créez un modèle qui exprime l'identité de votre marque. Lorsque vous êtes prêt, sélectionnez **Save**.

![Création d'un modèle dans Alpaco]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Étape 2 : Rédiger un message à l'aide du modèle {#step-2-draft-a-message-using-the-template}

Ensuite, rendez-vous dans le lobby d'Alpaco et utilisez votre modèle pour créer un e-mail, un message in-app ou un bloc de contenu. Pour vérifier votre message avant de l'exporter, sélectionnez **Review**.

![Création d'un e-mail dans Alpaco]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Étape 3 : Exporter votre message vers Braze {#step-3-export-your-message-to-braze}

Sélectionnez **Export**, puis choisissez l'intégration Braze et indiquez si vous exportez un modèle d'e-mail ou un bloc de contenu.

Si vous apportez des modifications après l'exportation, vous pouvez réexporter le contenu depuis Alpaco pour le mettre à jour dans Braze.

![Exportation d'un e-mail depuis Alpaco]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Utilisation des modèles et des blocs Alpaco dans Braze {#using-alpaco-templates-and-blocks-in-braze}

Selon le type de contenu que vous exportez, votre modèle apparaîtra dans l'une des sections suivantes :

- **Modèles et médias > Modèles d'e-mail**
- **Modèles et médias > Content Blocks**

Les modèles Alpaco sont idéaux pour les organisations qui souhaitent gérer la cohérence de leur marque de manière centralisée. Ils prennent également en charge les étiquettes intégrées de Braze pour faciliter la catégorisation et la gestion du contenu.