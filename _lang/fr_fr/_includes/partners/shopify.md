{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
L'intégration standard est conçue pour les boutiques en ligne Shopify, offrant un processus de configuration simple et fluide. Cette option vous permet de connecter rapidement votre boutique Shopify à Braze, vous donnant ainsi les moyens d'exploiter de puissants outils d'engagement client sans disposer d'une expertise technique approfondie. Grâce à cette option d'intégration, vous pouvez synchroniser les données de vos clients, automatiser l'envoi de messages personnalisés et améliorer vos efforts marketing grâce aux fonctionnalités complètes de Braze.

Pour utiliser l'intégration standard Shopify, consultez la [configuration de l'intégration standard Shopify]({{site.baseurl}}/shopify_standard_integration).
{% endtab %}

{% tab custom %}
L'intégration personnalisée offre une solution plus flexible et composable si vous utilisez Shopify Hydrogen ou prenez en charge une boutique headless. Cette option vous donne les moyens d'implémenter les SDK de Braze directement dans votre environnement Shopify, ce qui permet une intégration plus poussée et des fonctionnalités sur mesure. Que vous cherchiez à créer des expériences client uniques ou à optimiser des flux de travail spécifiques, l'intégration personnalisée fournit les outils nécessaires pour exploiter pleinement les capacités de Braze dans une configuration headless.

Pour utiliser l'intégration personnalisée Shopify, consultez la [configuration de l'intégration personnalisée de Shopify]({{site.baseurl}}/shopify_custom_integration).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == 'Custom external ID historical backfill' %}

Si vous prévoyez d'intégrer avec un ID externe personnalisé (que ce soit pour l'[intégration standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-4) ou l'[intégration personnalisée]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-6)), vous devrez ajouter votre ID externe personnalisé en tant que métachamp client Shopify à tous les profils clients Shopify existants, puis effectuer le backfill historique.

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Vous pouvez combiner [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) avec les [codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) pour envoyer des informations relatives à ces codes à Currents. Utilisez la balise `capture` pour enregistrer le code de promotion dans une variable, puis référencez cette variable dans `message_extras` :

{% raw %}
```liquid
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}
```
{% endraw %}

{% endif %}