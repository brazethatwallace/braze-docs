---
nav_title: "Messages in-app"
article_title: "Messages in-app"
page_order: 5
page_type: landing
alias: /in-app_messages/
description: "Engagez vos utilisateurs avec des messages in-app personnalisés qui améliorent l'expérience utilisateur grâce à une variété de dispositions et d'outils de personnalisation dans Braze."
channel:
  - in-app messages
search_rank: 5
---

# Messages in-app {#in-app-messages}

> Les messages in-app vous permettent de transmettre du contenu à vos utilisateurs sans interrompre leur journée avec une notification push. Des messages in-app personnalisés et adaptés améliorent l'expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Avec une variété de dispositions et d'outils de personnalisation à votre disposition, les messages in-app engagent vos utilisateurs plus que jamais.

## Conditions préalables {#prerequisites}

Avant de pouvoir envoyer des messages in-app, vous devez intégrer le [SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) dans votre application ou votre site web. Aucune configuration supplémentaire n'est requise.

Pour les versions minimales du SDK et les exigences spécifiques aux fonctionnalités, consultez :
- [Éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [Types de messages]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/)

## Cas d'utilisation {#use-cases}

Grâce au contenu riche offert par les messages in-app, vous pouvez exploiter ce canal pour une variété de cas d'utilisation :

| Cas d'utilisation | Explication |
| --- | --- |
| Amorce push | Lancez une campagne d'[amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) en utilisant un message in-app enrichi pour montrer à vos clients les avantages de s'abonner aux notifications push pour votre application ou site, et présentez-leur une invite à accorder l'autorisation push.
| Ventes et promotions | Utilisez des messages in-app modaux pour accueillir les clients avec des médias visuellement attrayants contenant des codes de promotion statiques ou des offres. Incitez-les à effectuer des achats ou des conversions qu'ils n'auraient pas réalisés autrement. |
| Encourager l'adoption de fonctionnalités | Encouragez les clients à utiliser d'autres parties de votre application ou à profiter d'un service. |
| Campagnes hautement personnalisées | Placez des messages in-app comme la première chose que vos clients voient lorsqu'ils ouvrent votre application ou site. Ajoutez des fonctionnalités de personnalisation Braze, telles que le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), pour inciter les utilisateurs à agir et ainsi rendre votre communication plus efficace.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation" }

Voici d'autres cas d'utilisation à envisager :

- Nouvelles fonctionnalités de l'application
- Gestion de l'application
- Avis
- Mises à jour ou mises à niveau de l'application
- Cadeaux et concours

## Types de messages standard {#standard-message-types}

Les onglets suivants montrent ce que vos utilisateurs voient lorsqu'ils ouvrent l'un de nos types de messages in-app standard : contextuel, fenêtre modale et plein écran.

{% tabs %}
{% tab Contextuel %}

Les messages contextuels apparaissent généralement en haut et en bas de l'écran de l'application (vous pouvez définir cela lors de la création de votre message). Ils sont parfaits pour informer vos utilisateurs de nouvelles conditions d'utilisation, de cookies et d'autres informations brèves.

![Message in-app contextuel apparaissant en bas de l'écran de l'application. Le message contextuel comprend une icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fenêtre modale %}

Les fenêtres modales apparaissent au centre de l'écran de l'appareil avec un overlay qui les fait ressortir par rapport à votre application en arrière-plan. Elles sont parfaites pour suggérer de manière visible à vos utilisateurs de profiter d'une vente ou d'un cadeau.

![Message in-app modal apparaissant au centre d'une application et d'un site web sous forme de boîte de dialogue. La fenêtre modale comprend une image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Plein écran %}

Les messages plein écran sont exactement ce que leur nom indique : ils occupent tout l'écran de l'appareil ! Ce type de message est idéal lorsque vous avez vraiment besoin de l'attention de vos utilisateurs, par exemple pour des mises à jour obligatoires de l'application.

![Message in-app plein écran occupant tout l'écran d'une application. Le message plein écran comprend une grande image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

En plus de ces modèles de messages par défaut, vous pouvez également personnaliser davantage vos messages en utilisant des messages in-app HTML personnalisés, des fenêtres modales web avec CSS ou des formulaires de capture d'e-mail web. Pour en savoir plus, consultez [Personnalisation]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/).

Pour savoir comment la distribution basée sur des modèles au moment de l'affichage affecte la journalisation des **abandons**, consultez la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq/).

## Étapes suivantes {#next-steps}

- [Créer un message in-app avec l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [Créer un message in-app avec l'éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}