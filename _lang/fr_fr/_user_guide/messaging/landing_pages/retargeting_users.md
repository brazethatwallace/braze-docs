---
nav_title: Recibler les utilisateurs
article_title: Recibler les utilisateurs
description: "Découvrez comment recibler les utilisateurs qui ont soumis un formulaire via une page d'accueil."
page_order: 3
---

# Recibler les utilisateurs via une page d'accueil {#retarget-users-through-a-landing-page}

> Découvrez comment recibler les utilisateurs qui ont soumis un formulaire via une page d'accueil en créant un segment dédié ou en déclenchant un message lors de la soumission du formulaire.

## Conditions préalables {#prerequisites}

Avant de commencer, vous devrez créer une [page d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Reciblage des utilisateurs {#retargeting-users}

Braze suit automatiquement le moment où un utilisateur soumet un formulaire de page d'accueil. Vous pouvez consulter le nombre total de soumissions pour un formulaire dans l'[analytique des pages d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#viewing-analytics). Cependant, pour un reciblage spécifique à l'utilisateur, vous devrez recibler les utilisateurs via le formulaire de votre page d'accueil en utilisant l'une des méthodes suivantes :

- **Utiliser un segment :** vous pouvez créer un nouveau segment pour identifier automatiquement les utilisateurs qui ont ou n'ont pas soumis un formulaire de page d'accueil.
- **Utiliser un déclencheur de message :** vous pouvez configurer un déclencheur de message pour envoyer automatiquement un message aux utilisateurs ou les faire entrer dans un Canvas après la soumission du formulaire.

{% tabs local %}
{% tab Utiliser un segment %}
Lorsque vous [créez un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), dans le groupe « Reciblage », choisissez **Submitted form on Landing Page**.

![Création d'un segment avec le groupe de filtres sélectionné sur « Submitted Form on Landing Page ».]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

À partir de là, vous pouvez segmenter les utilisateurs selon qu'ils ont ou n'ont pas soumis un formulaire de page d'accueil pour votre page d'accueil.
{% endtab %}

{% tab Utiliser un déclencheur de message %}
Lorsque vous choisissez votre option de réception pour votre [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), sélectionnez **Action Based Delivery**, puis **Submitted Landing Page form**.

Tous les utilisateurs qui soumettent un formulaire via cette page d'accueil recevront un message via le canal de communication choisi ou seront intégrés dans le Canvas choisi.

![Action de déclenchement de page d'accueil dans l'envoi de messages.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
L'option de livraison par événement pour les pages d'accueil n'est pas disponible pour les messages in-app. Pour cibler les utilisateurs qui ont soumis un formulaire sur une page d'accueil avec un message in-app, sélectionnez le filtre **Submitted Form on Landing Page** dans les **Options de ciblage** de votre Campaign.
{% endalert %}

{% endtab %}
{% endtabs %}