---
nav_title: Optimisations
article_title: Optimiser les tests A/B
page_order: 1
page_type: reference
description: "Découvrez comment optimiser les tests multivariés et les tests A/B de campagnes avec BrazeAI."
---

# Optimiser les tests A/B {#optimizing-ab-tests}

> Utilisez **Optimiser avec BrazeAI<sup>TM</sup>** pour optimiser automatiquement une campagne comportant plusieurs variantes.

À l'étape **Audiences cibles**, accédez à **test A/B**, puis activez **Optimiser avec BrazeAI<sup>TM</sup>**.

Pour une campagne à envoi unique, BrazeAI<sup>TM</sup> envoie un test initial, puis envoie la variante la plus performante au reste de l'audience. Pour une campagne à envois multiples, BrazeAI<sup>TM</sup> analyse les performances toutes les 12 heures et oriente davantage d'utilisateurs vers les variantes les plus performantes.

Pour les prérequis, les options de configuration et les détails de reporting, consultez [Optimiser les tests A/B avec BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

{% alert note %}
Les campagnes existantes qui utilisent la variante personnalisée continuent de prendre en charge cette optimisation et ses analyses. La variante personnalisée n'est pas disponible lors de la création d'une nouvelle campagne.
{% endalert %}

Braze vérifie à nouveau l'éligibilité des utilisateurs avant le second envoi dans le cadre d'une optimisation à envoi unique. Les utilisateurs qui n'étaient pas éligibles pour le test initial peuvent intégrer l'audience restante, tandis que les utilisateurs qui ne sont plus éligibles ne reçoivent pas l'envoi de suivi.

Pour en savoir plus sur les résultats de campagne, consultez [Analyse des tests A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).