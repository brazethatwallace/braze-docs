---
nav_title: Projection de test A/B
article_title: Projection de test A/B
page_order: 20
hidden: true
page_type: reference
description: "Cet article explique comment fonctionne la projection de test A/B, comment exécuter une projection et comment Braze utilise vos données."
---

# Projection de test A/B {#ab-test-projection}

> La projection de test A/B utilise des réseaux neuronaux pour prédire les lignes d'objet les plus performantes. Notre modèle extrait les caractéristiques linguistiques des tests A/B gagnants réalisés sur Braze et utilise ces schémas linguistiques statistiques pour apprendre à notre intelligence artificielle ce qui fait de meilleures lignes d'objet.

{% alert important %}
Cette fonctionnalité est actuellement disponible en accès anticipé. Si vous souhaitez participer à l'accès anticipé, contactez votre gestionnaire de satisfaction client ou votre gestionnaire de compte Braze.
{% endalert %}

## Exécution d'une projection {#running-a-projection}

Dans la composition de la campagne, insérez vos variantes de messages et leurs lignes d'objet dans l'éditeur. Lorsque vous êtes prêt, passez à l'étape **Target Audience** du flux de création de la campagne. Dans le panneau **test A/B**, sélectionnez **Run Projection**.

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Une fenêtre modale s'ouvre avec les lignes d'objet des variantes de messages que vous avez déjà créées. Vous avez également la possibilité d'insérer des lignes d'objet supplémentaires (maximum dix) en en saisissant une manuellement dans le champ, puis en exécutant la projection. Sélectionnez **Run Projection**.

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

La ligne d'objet que notre intelligence artificielle prédit comme étant la meilleure sera mise en évidence avec le libellé **Projected Winner**.

{% alert note %}
Pour les [campagnes push multiplateformes]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push), le test A/B est pris en charge lorsque vous sélectionnez plusieurs plateformes.
{% endalert %}

### Quelle est la précision des projections ? {#how-accurate-are-the-projections}

Lors de nos tests, nous avons constaté que les projections étaient précises à environ 70 % pour choisir entre des paires de messages dans de véritables tests A/B. Gardez cela à l'esprit lorsque vous interprétez les messages que le modèle projette comme gagnants.

### Comment utilisons-nous vos données ? {#how-do-we-use-your-data}

Cette fonctionnalité apprend à partir des tests A/B précédemment réalisés sur Braze. Le contenu réel de vos messages ou de ceux de tout autre client de Braze n'est jamais fourni au modèle. Nous extrayons d'abord les schémas linguistiques de haut niveau qui prédisent les messages gagnants dans les tests A/B. Ensuite, nous fournissons ces schémas à notre intelligence artificielle pour lui apprendre à discerner quelles caractéristiques linguistiques constituent de meilleures lignes d'objet.