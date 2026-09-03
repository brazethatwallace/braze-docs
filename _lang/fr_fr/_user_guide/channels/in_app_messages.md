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

> Les messages in-app diffusent du contenu au sein de votre application ou de votre site web sans interrompre les utilisateurs par une notification push. Des messages in-app personnalisés améliorent l'expérience utilisateur et aident votre audience à tirer davantage de valeur de votre produit grâce à des dispositions, des outils de personnalisation et de ciblage. Ce hub couvre les types de messages, l'éditeur par glisser-déposer, les prérequis et les cas d'usage courants tels que l'onboarding et les promotions. Intégrez le [SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) avant de créer votre premier message in-app, puis choisissez une disposition standard ou personnalisée pour votre Campaign.

## Prérequis {#prerequisites}

Avant de pouvoir envoyer des messages in-app, vous devez intégrer le [SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) dans votre application ou votre site web. Aucune configuration supplémentaire n'est requise.

Pour les versions minimales du SDK et les exigences spécifiques à chaque fonctionnalité, consultez :
- [Éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Types de messages]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## Cas d'usage {#use-cases}

Grâce à la richesse du contenu offert par les messages in-app, vous pouvez tirer parti de ce canal pour divers cas d'usage :

| Cas d'usage | Explication |
| --- | --- |
| Amorce push | Lancez une Campaign d'[amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) en utilisant un message in-app enrichi pour montrer à vos clients l'intérêt d'activer les notifications push pour votre application ou site, et présentez-leur une invite à accorder l'autorisation push.
| Ventes et promotions | Utilisez des messages in-app modaux pour accueillir vos clients avec des contenus visuellement attractifs contenant des codes de promotion statiques ou des offres. Incitez-les à effectuer des achats ou des conversions qu'ils n'auraient pas faits autrement. |
| Encourager l'adoption de fonctionnalités | Encouragez vos clients à utiliser d'autres parties de votre application ou à profiter d'un service. |
| Campaigns hautement personnalisées | Placez des messages in-app comme la première chose que vos clients voient lorsqu'ils accèdent à votre application ou site. Ajoutez des fonctionnalités de personnalisation de Braze, telles que le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), pour inciter les utilisateurs à agir et ainsi rendre votre communication plus efficace.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

Autres cas d'usage à considérer :

- Nouvelles fonctionnalités de l'application
- Gestion de l'application
- Avis
- Mises à niveau ou mises à jour de l'application
- Cadeaux et jeux-concours

## Types de messages standard {#standard-message-types}

Les onglets suivants montrent ce que vos utilisateurs voient lorsqu'ils ouvrent l'un de nos types de messages in-app standard : contextuel, fenêtre modale et plein écran.

{% tabs %}
{% tab Contextuel %}

Les messages contextuels apparaissent généralement en haut et en bas de l'écran de l'application (vous pouvez définir cela lors de la création de votre message). Ils sont parfaits pour informer vos utilisateurs de nouvelles conditions d'utilisation, de cookies et d'autres extraits d'information.

![Message in-app contextuel apparaissant en bas de l'écran de l'application. Le message contextuel comprend une icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fenêtre modale %}

Les fenêtres modales apparaissent au centre de l'écran de l'appareil avec un voile d'arrière-plan qui les fait ressortir par rapport à votre application. Elles sont parfaites pour suggérer de manière visible à vos utilisateurs de profiter d'une promotion ou d'un cadeau.

![Message in-app modal apparaissant au centre d'une application et d'un site web sous forme de boîte de dialogue. La fenêtre modale comprend une image, un titre, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Plein écran %}

Les messages plein écran sont exactement ce que leur nom indique : ils occupent la totalité de l'écran de l'appareil ! Ce type de message est idéal lorsque vous avez véritablement besoin de capter l'attention de vos utilisateurs, par exemple pour des mises à jour obligatoires de l'application.

![Message in-app plein écran occupant la totalité de l'écran de l'application. Le message plein écran comprend une grande image, un titre, un corps de message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

En plus de ces modèles de messages par défaut, vous pouvez également personnaliser davantage vos communications à l'aide de messages in-app HTML personnalisés, de fenêtres modales web avec CSS ou de formulaires de capture d'e-mail web. Pour en savoir plus, consultez [Personnaliser]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

Pour comprendre comment la distribution basée sur des modèles au moment de l'affichage affecte la journalisation des **abandons**, consultez la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Étapes suivantes {#next-steps}

- [Créer un message in-app avec l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Créer un message in-app avec l'éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}