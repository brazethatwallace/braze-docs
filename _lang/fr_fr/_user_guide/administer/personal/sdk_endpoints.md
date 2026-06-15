---
nav_title: Endpoints API et SDK
article_title: Endpoints API et SDK
page_order: 5
page_type: reference
description: "Recherchez l'URL correcte du tableau de bord, l'endpoint REST API et l'endpoint SDK pour votre instance Braze."

---

# Endpoints API et SDK {#api-and-sdk-endpoints}

> Recherchez l'URL correcte du tableau de bord, l'endpoint REST API et l'endpoint SDK pour votre instance Braze. Vous avez besoin de ces URL pour vous connecter, effectuer des appels API et intégrer le SDK.

Braze gère un certain nombre d'instances différentes pour notre tableau de bord, notre SDK et nos endpoints REST, que nous appelons « clusters ». Votre gestionnaire d'onboarding Braze vous indiquera sur quel cluster vous vous trouvez. Pour en savoir plus sur le SDK Braze, consultez le cours d'apprentissage Braze Learning [Braze 101](https://learning.braze.com/braze-101).

Se connecter sur [dashboard.braze.com](https://dashboard.braze.com) vous redirigera automatiquement vers la bonne adresse de cluster.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Lors de l'intégration de votre SDK, utilisez l'endpoint SDK. Lors d'appels à notre REST API, utilisez l'endpoint REST.
{% endalert %}

Pour plus de détails sur l'accès à l'API, consultez notre [article d'aperçu de l'API]({{site.baseurl}}/api/basics/).