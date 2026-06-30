---
nav_title: Bannières de test
article_title: Bannières de test
page_order: 2
description: "Découvrez comment tester votre message de bannière avant de lancer votre Campaign afin de vous assurer que tous les médias, le texte, la personnalisation et les attributs personnalisés s'affichent correctement."
channel:
  - banners
noindex: true
---

# Bannières de test {#test-banners}

> Découvrez comment tester votre message de bannière avant de lancer votre Campaign afin de vous assurer que tous les médias, le texte, la personnalisation et les attributs personnalisés s'affichent correctement. Pour plus d'informations générales, consultez la section [À propos des bannières]({{site.baseurl}}/developer_guide/banners).

## Conditions préalables {#prerequisites}

Avant de pouvoir tester les messages de bannière dans Braze, vous devez créer une [Campaign de bannière dans Braze]({{site.baseurl}}/user_guide/channels/banners/create_a_banner). Vérifiez également que l'emplacement que vous souhaitez tester est déjà [intégré dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements).

Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou à des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test et des jetons de notification push valides doivent être enregistrés pour l'utilisateur test avant l'envoi.

## Tester une bannière {#test-a-banner}

{% multi_lang_include banners/testing.md page="testing" %}