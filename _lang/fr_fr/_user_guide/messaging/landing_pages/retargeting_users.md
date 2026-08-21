---
nav_title: Recibler les utilisateurs
article_title: Recibler les utilisateurs
description: "Découvrez comment recibler les utilisateurs qui ont soumis un formulaire via une page de destination."
page_order: 3
---

# Recibler les utilisateurs via une page de destination {#retarget-users-through-a-landing-page}

> Découvrez comment recibler les utilisateurs qui ont soumis un formulaire via une page de destination en créant un segment dédié ou en déclenchant un message lors de la soumission du formulaire.

## Prérequis {#prerequisites}

Avant de commencer, créez une [page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Reciblage des utilisateurs {#retargeting-users}

Braze suit automatiquement les soumissions de formulaire sur une page de destination. Vous pouvez consulter le nombre total de soumissions pour un formulaire dans l'[analyse des pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics). Pour un reciblage spécifique à l'utilisateur, reciblez les utilisateurs via le formulaire de votre page de destination en utilisant l'une des méthodes suivantes :

{% tabs local %}
{% tab Utiliser un segment %}

Créez un nouveau Segment pour identifier automatiquement les utilisateurs qui ont ou n'ont pas soumis un formulaire de page de destination. Lorsque vous [créez un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), dans le groupe « Reciblage », choisissez **Submitted Form on Landing Page**.

![Création d'un Segment avec le groupe de filtres sélectionné sur « Submitted Form on Landing Page ».]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

À partir de là, vous pouvez segmenter les utilisateurs selon qu'ils ont ou non soumis un formulaire de page de destination pour votre page de destination.
{% endtab %}

{% tab Utiliser un déclencheur de message %}

Configurez un déclencheur de message pour envoyer automatiquement un message aux utilisateurs ou les faire entrer dans un Canvas après qu'ils ont soumis le formulaire. Lorsque vous choisissez votre option de réception pour votre [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), sélectionnez **Action Based Delivery**, puis **Submitted a Landing Page form**.

Tous les utilisateurs qui soumettent un formulaire via ce formulaire de page de destination reçoivent un message via le canal de communication choisi ou sont intégrés dans le Canvas choisi.

![Action de déclenchement de page de destination dans la communication.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
L'option de livraison par événement pour les pages de destination n'est pas disponible pour les messages in-app. Pour cibler les utilisateurs ayant soumis un formulaire sur une page de destination avec un message in-app, sélectionnez le filtre **Submitted Form on Landing Page** dans les **Targeting Options** de votre Campaign.
{% endalert %}

{% endtab %}
{% endtabs %}

### Formulaire à plusieurs étapes {#multi-step-form}

Pour un [formulaire à plusieurs étapes]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms), les deux méthodes de reciblage reposent sur l'événement **Submitted a Landing Page form**, qui n'est enregistré qu'après qu'un utilisateur a complété toutes les étapes. Un utilisateur qui soumet certaines étapes mais pas toutes est enregistré dans son profil, mais n'est inclus dans aucune des deux méthodes tant qu'il n'a pas complété l'intégralité du formulaire. Pour en savoir plus, consultez [Suivre les données des formulaires partiellement complétés]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms#track-data-from-partially-completed-forms).