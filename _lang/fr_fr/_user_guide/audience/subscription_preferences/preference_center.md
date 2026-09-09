---
nav_title: Centre de préférences
article_title: Centre de préférences
page_order: 8
layout: dev_guide
guide_top_header: "Centre de préférences"
guide_top_text: "Un centre de préférences e-mail permet aux utilisateurs de gérer leurs préférences de notification pour les campagnes d'e-mail et les newsletters depuis une page personnalisée dans votre application ou votre site web. Consultez ces articles pour découvrir comment créer et gérer un centre de préférences via l'<a href=\"/docs/api/endpoints/preference_center\">API du centre de préférences Braze</a> ou grâce à l'éditeur par glisser-déposer, y compris les groupes d'abonnement, les états d'abonnement et la personnalisation de la page hébergée."
description: "Cette page d'accueil répertorie les articles sur le centre de préférences e-mail de Braze et sur l'utilisation de l'API du centre de préférences."
channel:
  - email

guide_featured_title: "Articles de la section"
guide_featured_list:
- name: Centre de préférences des e-mails via API
  link: /docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
  image: /assets/img/braze_icons/list.svg
- name: Centre de préférences e-mail par glisser-déposer
  link: /docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
  image: /assets/img/braze_icons/mail-01.svg

---

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

## Questions fréquemment posées {#frequently-asked-questions}

### Qu'est-ce qu'un centre de préférences des e-mails ? {#what-is-an-email-preference-center}

Un centre de préférences des e-mails est une page hébergée permettant aux utilisateurs de mettre à jour leur statut d'abonnement aux e-mails et de choisir des catégories de messages. Braze prend en charge les centres de préférences créés via API et par glisser-déposer.

### Dois-je utiliser l'API du centre de préférences ou l'éditeur par glisser-déposer ? {#should-i-use-the-preference-center-api-or-the-drag-and-drop-editor}

Utilisez le [centre de préférences par glisser-déposer]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center) pour une configuration plus rapide avec moins de code. Utilisez le [centre de préférences des e-mails via API]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/api_preference_center) lorsque vous avez besoin d'un contrôle total sur la mise en page, l'hébergement et la logique personnalisée.