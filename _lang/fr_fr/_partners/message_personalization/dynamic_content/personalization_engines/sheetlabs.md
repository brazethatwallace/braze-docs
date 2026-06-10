---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Cet article de référence décrit le partenariat entre Braze et Sheetlabs, un service qui vous permet de personnaliser vos campagnes marketing avec des données provenant de feuilles de calcul."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/) est une plateforme qui vous permet de transformer des feuilles de calcul en API puissantes et bien documentées. Vous pouvez importer des données depuis Google Sheets ou Excel, les transformer en API, puis utiliser cette API dans d'autres applications, telles que Braze.
_Cette intégration est maintenue par Sheetlabs._

## À propos de l'intégration {#about-the-integration}

L'intégration de Sheetlabs et de Braze vous permet d'utiliser le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) pour inclure les API de Sheetlabs dans vos campagnes marketing Braze. On l'utilise couramment pour faire le lien entre une feuille de calcul Google (mise à jour directement par l'équipe marketing) et les modèles Braze. Cela vous permet d'exploiter pleinement les modèles Braze, par exemple pour gérer des traductions ou des ensembles plus importants d'attributs personnalisés.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Sheetlabs | Un [compte Sheetlabs](https://sheetlabs.com/) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

L'intégration de Braze et Sheetlabs vous permet de réaliser les cas d'utilisation suivants :

1. **Séparer l'accès des marketeurs de l'accès aux campagnes Braze** : certaines équipes souhaitent éviter de donner à tout le personnel l'accès à la configuration directe des modèles et du contenu Braze. Elles préfèrent que le personnel mette à jour le contenu marketing dans une feuille de calcul. Sheetlabs fait le lien entre les feuilles de calcul et Braze, et les mises à jour sont prises en compte en temps réel.
2. **Traductions** : les modèles Braze ne prennent pas en charge nativement les traductions. Si vous souhaitez prendre en charge plusieurs langues, vous devez créer plusieurs modèles. En utilisant Sheetlabs conjointement avec Braze, vous pouvez disposer d'un seul modèle Braze traduit en plusieurs langues.
3. **Extension des attributs personnalisés** : Braze fournit un certain nombre d'attributs personnalisés configurables. En utilisant Sheetlabs conjointement avec Braze, vous pouvez ajouter des attributs personnalisés supplémentaires au-delà de cette allocation initiale.

Consultez la [documentation Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) pour en savoir plus sur ces cas d'utilisation.

## Intégration {#integration}

### Étape 1 : Importer votre feuille de calcul dans Sheetlabs {#step-1-import-your-spreadsheet-into-sheetlabs}

Dans Sheetlabs, téléchargez une feuille de calcul Excel ou liez votre compte Google et importez une feuille Google.

- Pour importer une feuille de calcul Excel, cliquez sur **Data Tables** dans la barre de menu, puis sur **Import from CSV/Excel**.
- Pour importer depuis Google Sheets, cliquez sur **Data Tables** dans la barre de menu, puis sur **Import from Google**. Vous devrez ensuite fournir vos identifiants Google et importer la feuille.

Vous pouvez également choisir de garder votre feuille Google synchronisée, ce qui signifie que Sheetlabs récupérera automatiquement les dernières données de votre feuille Google dès qu'elle est modifiée.

Assurez-vous d'inclure l'ID utilisateur Braze dans votre feuille de calcul, ou tout autre élément que vous pourrez utiliser comme clé de recherche par la suite.

### Étape 2 : Créer une API dans Sheetlabs {#step-2-create-an-api-in-sheetlabs}

Ensuite, dans Sheetlabs, accédez à **APIs > Create API** et donnez un nom à votre API. Vous voudrez probablement autoriser les requêtes via un champ de recherche de votre feuille de calcul, tel que l'ID utilisateur Braze.

À ce stade, vous devriez pouvoir accéder à votre API à l'aide d'un lien du type :<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Étape 3 : Utiliser l'API dans le Contenu connecté de Braze {#step-3-use-the-api-in-braze-connected-content}

Maintenant que votre API est accessible, vous pouvez l'utiliser dans vos appels de Contenu connecté. Voici un exemple de modèle de traductions :

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Pour plus d'exemples et de conseils sur l'intégration avec Sheetlabs, consultez la [documentation de Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}