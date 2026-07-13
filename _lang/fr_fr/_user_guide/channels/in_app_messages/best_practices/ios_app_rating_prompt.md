---
nav_title: Invite d'évaluation in-app pour iOS
article_title: Invite d'évaluation in-app pour iOS
page_order: 6
description: "Cet article décrit les approches et les implications de l'utilisation de Braze pour demander aux utilisateurs d'évaluer votre application."
channel:
  - in-app messages

---

# Invite d'évaluation in-app pour iOS {#in-app-rating-prompt-for-ios}

> Cet article décrit les approches et les implications de l'utilisation de Braze pour demander aux utilisateurs d'évaluer votre application. Pour des conseils sur la création d'une campagne d'évaluation d'application efficace, consultez [Les bonnes et mauvaises pratiques des évaluations d'applications par les clients](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

Apple propose une invite native, introduite avec iOS 10.3, qui permet aux utilisateurs d'évaluer les applications directement depuis l'application elle-même. Si vous souhaitez demander aux utilisateurs d'évaluer votre application à l'aide d'un message in-app sur iOS, vous devez utiliser l'invite native, car Apple interdit les invites d'évaluation personnalisées (voir les [Directives d'évaluation de l'App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), section 5.6.1).

Conformément aux directives d'Apple, les invites d'évaluation d'application peuvent être affichées à un utilisateur jusqu'à trois fois par an, de sorte que toute campagne d'évaluation d'application devrait tirer parti de la [limite de débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping). Les utilisateurs peuvent également désactiver complètement l'affichage des invites d'évaluation dans les paramètres de leur application. Pour en savoir plus sur les évaluations de l'App Store, consultez l'article d'Apple sur les [Évaluations, avis et réponses](https://developer.apple.com/app-store/ratings-and-reviews/).

## Utiliser Braze pour demander aux utilisateurs d'évaluer l'application {#using-braze-to-ask-users-for-app-reviews}

Bien qu'Apple exige l'utilisation de l'invite native, vous pouvez tout de même tirer parti des campagnes Braze pour demander aux utilisateurs d'évaluer et de donner leur avis sur votre application au bon moment. Deux approches principales s'offrent à vous.

### Approche 1 : lien profond vers l'App Store {#approach-1-deep-linking-to-the-app-store}

Avec cette approche, vous souhaitez encourager les utilisateurs à se rendre sur l'App Store pour laisser un avis. Pour ce faire, créez une campagne de message in-app qui utilise un [lien profond]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) vers l'App Store.

![Deux écrans mobiles côte à côte. Le premier est un message in-app qui demande à l'utilisateur d'évaluer l'application sur l'App Store. Le second est la page iOS de l'App Store pour cette application.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Approche 2 : amorçage en douceur {#approach-2-soft-priming}

Si vous ne souhaitez pas que les utilisateurs quittent votre application, vous pouvez d'abord les préparer avec un message in-app distinct. L'amorçage est une façon de demander la permission aux utilisateurs avant de leur envoyer l'invite native d'évaluation de l'App Store. Pour ce faire, créez une campagne de message in-app et ajoutez un lien profond personnalisé qui appelle la méthode `requestReview` lorsqu'il est cliqué.

Pour les étapes détaillées, consultez [Invite d'évaluation personnalisée de l'App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_customizing-the-app-store-review-prompt).

![Deux messages in-app côte à côte. Le premier prépare l'utilisateur à évaluer l'application en lui demandant s'il a un moment pour la noter. Le second est le message natif d'évaluation iOS de l'App Store, affichant une échelle de cinq étoiles que l'utilisateur peut sélectionner pour évaluer l'application.]({% image_buster /assets/img_archive/prime_app_review.png %})

Les utilisateurs soumettront une évaluation via l'invite native d'évaluation de l'App Store, et pourront rédiger et soumettre un avis sans quitter l'application.

### Considérations {#considerations}

Comme alternative à l'amorçage en douceur, vous pourriez également afficher directement l'invite d'évaluation iOS sans qu'aucun message d'amorçage Braze ne soit affiché au préalable. L'avantage est que si l'utilisateur a désactivé les invites d'évaluation d'application, il n'y aurait pas l'expérience utilisateur sous-optimale de tenter d'évaluer l'application sans qu'aucune invite n'apparaisse pour le faire.

{% alert important %}
Ne créez pas de messages in-app HTML personnalisés qui imitent une invite native d'évaluation iOS, car cela enfreint les directives d'Apple.
{% endalert %}