---
nav_title: Importation de cohortes Heap
article_title: Importation de cohortes Heap
description: "Cet article de référence détaille l'intégration entre Braze et Heap, une plateforme d'informations numériques, qui vous permet d'importer des données Heap vers Braze, de créer des cohortes d'utilisateurs, ainsi que d'exporter des données Braze vers Heap pour créer des segments."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Importation de cohortes Heap {#heap-cohort-import}

> [Heap](https://heap.io/), une plateforme d'informations numériques, vous permet de vous concentrer sur les opportunités de votre expérience numérique ayant le plus d'impact sur votre entreprise, en éliminant les frictions, en satisfaisant vos clients et en accélérant le chiffre d'affaires.

L'intégration de Braze et Heap vous permet d'[importer des données Heap vers Braze](#data-import-integration), de créer des cohortes d'utilisateurs, ainsi que d'[exporter des données Braze vers Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap) pour créer des segments.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Heap | Un compte [Heap](https://heap.io/about) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'importation des données Braze | Elle peut être récupérée dans le tableau de bord de Braze depuis **Intégrations partenaires** > **Partenaires technologiques**, puis sélectionnez **Heap**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Braze Currents | Pour pouvoir exporter des données de Braze vers Heap, vous devez activer [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) sur votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'usage {#use-cases}
- Réengager les utilisateurs qui ont abandonné un entonnoir : déclenchez des messages de réengagement lorsque les utilisateurs abandonnent l'entonnoir d'achat ou d'abonnement.
- Personnaliser l'expérience d'essai : identifiez les points de friction dans votre expérience d'essai et envoyez des rappels au bon moment pour réengager les utilisateurs pendant un essai et les aider à en tirer de la valeur.
- Augmenter l'engagement sur les annonces et les offres : ciblez les promotions, les mises à jour et les annonces de nouveaux services auprès des audiences concernées.

## Intégration de l'importation de données {#data-import-integration}

Utilisez l'intégration Heap vers Braze pour synchroniser automatiquement les cohortes définies dans Heap vers Braze.

### Étape 1 : Obtenir la clé d'importation des données Braze {#step-1-get-the-braze-data-import-key}

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques**, puis sélectionnez **Heap**.

Sur cette page, vous trouverez votre clé d'importation des données et un endpoint REST. Prenez note de ces deux valeurs et fournissez-les à votre gestionnaire de compte Heap pour terminer la configuration de l'intégration.

![Page du partenaire technologique Heap dans Braze affichant la clé d'importation des données et l'endpoint.]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### Étape 2 : Segmenter les utilisateurs importés dans Braze {#step-2-segment-imported-users-in-braze}

Dans Braze, naviguez vers **Segments**, nommez votre segment de cohorte Heap et sélectionnez **Heap Cohorts** comme filtre. À partir de là, vous pouvez choisir la cohorte Heap que vous souhaitez inclure. Une fois votre segment de cohorte Heap créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une Campaign ou d'un Canvas.

![Dans le générateur de segments de Braze, le filtre d'attributs utilisateur « Heap cohort » est défini sur « includes » et « Heap Test Cohort ».]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### Utilisation de cette intégration {#using-this-integration}

Pour utiliser votre segment Heap, créez une Campaign ou un Canvas Braze et sélectionnez le segment comme audience cible.

![Dans le générateur de Campaign de Braze, à l'étape de ciblage, le filtre « Cibler des utilisateurs par segment » est défini sur « Heap cohort ».]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation de cohortes ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

## Détails de l'intégration {#integration-details}

La structure du payload des données exportées est la même que celle des connecteurs HTTP personnalisés, consultable dans le [référentiel d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être associés par leur `external_id` ou leur `alias`. Les utilisateurs anonymes peuvent être mis en correspondance par leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent être identifiés par leur `external_id` ou leur `alias`.