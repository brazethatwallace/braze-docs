---
nav_title: Principes de base de Canvas
article_title: Principes de base de Canvas
page_order: 0
page_type: reference
description: "Cet article de référence couvre les principes de base de Canvas, en abordant les différentes questions que vous devriez vous poser lors de la configuration de votre premier Canvas."
tool: Canvas

---

# Principes de base de Canvas {#canvas-basics}

> Cet article de référence couvre les principes de base de Canvas, en abordant les différentes questions que vous devriez vous poser lors de la configuration de votre premier Canvas. Nous expliquerons également les cinq questions clés (quoi, quand, qui, pourquoi et où) de la visualisation et comment elles peuvent façonner et définir la manière dont vous construisez votre Canvas.

## Comprendre la structure d'un Canvas {#understanding-canvas-structure}

Avant d'entrer dans les détails de la [configuration d'un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), identifions les éléments clés qui composent un Canvas.

{% tabs %}
  {% tab Canvas %}
  Canvas est une interface unifiée dans laquelle les marketeurs conçoivent des campagnes comportant plusieurs messages. C'est un peu comme un outil de programmation visuelle qui vous permet de construire un parcours utilisateur cohérent à partir d'une série d'étapes.

  ![Exemple de Canvas avec une étape d'arbre décisionnel menant à deux parcours utilisateur différents selon que l'utilisateur a activé les notifications push ou non.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Parcours %}

  Un parcours, communément appelé parcours client, correspond à l'expérience individuelle d'un utilisateur au sein du Canvas.<br><br> ![Un schéma illustrant le parcours client d'un nouvel utilisateur. Un utilisateur anonyme installe une application, Kat crée un compte, Kat n'ouvre pas l'application pendant une semaine, une notification push ramène Kat dans l'application, puis Kat utilise l'application régulièrement.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Générateur de Canvas %}
  Le générateur de Canvas décrit les étapes à suivre lors de la création de votre Canvas. Cela inclut les éléments de base comme nommer votre Canvas et ajouter des équipes. Le générateur de Canvas est essentiellement la configuration indispensable avant de commencer à construire votre Canvas. Vous pouvez y contrôler la manière dont vos utilisateurs commencent et accomplissent leur parcours client, avec des options pour modifier la [planification d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule), l'[audience cible]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2c-set-your-target-entry-audience) et les [paramètres d'envoi]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2d-select-your-send-settings).<br><br> ![Le générateur de Canvas dans la section Principes de base pour un Canvas nommé « New Canvas ».]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variantes %}
  Une variante est le chemin que chaque client suit dans son parcours. Canvas prend en charge jusqu'à huit variantes avec un groupe de contrôle. Vous décidez quel segment de votre audience suivra chaque variante.<br><br> ![Sélection du bouton « Ajouter une variante ».]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Étapes %}
  Une étape dans Canvas est un point de décision marketing : « si ceci, alors cela ». Utilisez les [composants Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components#about-canvas-components) pour construire les étapes d'un parcours utilisateur.<br><br> ![Exemple d'ajout d'une étape de délai à un Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Lorsqu'un utilisateur entre dans un Canvas, il commence à la première étape. Chaque étape comporte des conditions qui déterminent si un utilisateur peut passer à l'étape suivante. Au sein d'une étape, vous pouvez définir des déclencheurs ou planifier la distribution, affiner le ciblage en ajoutant des filtres ou en marquant des événements d'exception, et spécifier différents canaux comme les notifications push ou les événements webhook. Dans Canvas, les étapes se déroulent de manière séquentielle, ce qui signifie que la première étape doit avoir lieu avant que la deuxième puisse se produire. Prenons l'exemple d'un Canvas avec les étapes suivantes : une étape de délai A avec un délai de 24 heures, une étape de message A avec une notification push et une étape de message B avec un message in-app. L'utilisateur A est maintenu dans un délai de 24 heures, puis, après ces 24 heures, il recevra une notification push, suivie d'un message in-app.

  {% endtab %}
{% endtabs %}

## Construire le parcours client {#building-the-customer-journey}

Utiliser les cinq questions clés (quoi, quand, qui, pourquoi et où) de la visualisation peut vous aider à identifier vos stratégies d'engagement client et à créer un parcours de messages personnalisé pour chacun de vos utilisateurs.

### Le « quoi » : nommez votre Canvas {#the-what-name-your-canvas}

*Qu'essayez-vous d'aider l'utilisateur à faire ou à comprendre ?*

Ne sous-estimez jamais le pouvoir d'un nom. Braze est conçu pour la collaboration, c'est donc le bon moment pour clarifier la manière dont vous communiquerez vos objectifs à votre équipe.

Vous pouvez ajouter des étiquettes et nommer les étapes et les variantes d'un Canvas. Pour en savoir plus sur les parcours clients, consultez notre cours d'apprentissage Braze sur le [mappage des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles).

### Le « pourquoi » : identifiez les événements de conversion {#the-why-identify-conversion-events}

*En partant du « quoi », pourquoi créez-vous ce Canvas ?*

Il est toujours important d'avoir un objectif défini en tête, et Canvas vous aide à comprendre vos performances par rapport à des indicateurs clés de performance comme l'engagement de session, les achats et les événements personnalisés.

Sélectionner au moins un [événement de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) vous permettra de comprendre comment optimiser les performances au sein du Canvas. Et si votre Canvas comporte plusieurs variantes ou un groupe de contrôle, Braze utilisera l'événement de conversion pour déterminer la meilleure variante pour atteindre cet objectif.

* **Démarrer une session** : je veux que mes utilisateurs reviennent et interagissent avec l'application.
* **Effectuer un achat** : je veux que mes utilisateurs achètent.
* **Réaliser un événement personnalisé** : je veux que mes utilisateurs effectuent une action spécifique que je suis en tant qu'événement personnalisé.
* **Mettre à jour l'application** : je veux que mes utilisateurs mettent à jour la version de leur application.

### Le « quand » : créez les conditions de départ {#the-when-create-starting-conditions}

*Quand un utilisateur commencera-t-il cette expérience ?*

Votre réponse déterminera les détails du moment et de la manière dont votre Canvas sera distribué à vos clients. Les utilisateurs peuvent entrer dans votre Canvas de deux façons : par planification ou par déclencheurs basés sur des actions.

{% alert tip %}
Consultez les [fonctionnalités basées sur le temps]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) pour Canvas afin de découvrir davantage de stratégies et de réponses aux questions courantes.
{% endalert %}

La distribution planifiée vous permet d'envoyer un Canvas immédiatement à votre audience cible. Vous pouvez également le configurer pour un envoi régulier ou le planifier pour un moment précis dans le futur. Les Canvas basés sur des actions réagissent à des comportements spécifiques des clients en temps réel. Par exemple, un déclencheur basé sur une action peut inclure l'ouverture d'une application, un achat, une interaction avec une autre Campaign ou le déclenchement d'un événement personnalisé. Au moment où l'action se produit, le Canvas peut être envoyé à vos utilisateurs.

### Le « qui » : sélectionnez une audience {#the-who-select-an-audience}

*Qui essayez-vous d'atteindre ?*

Pour définir votre « qui », vous pouvez utiliser les segments prédéfinis disponibles dans Canvas. Vous pouvez également ajouter des filtres supplémentaires pour affiner davantage le ciblage et vous connecter à votre audience cible. Après avoir construit ces segments, seuls les utilisateurs correspondant aux critères de l'audience cible pourront entrer dans le parcours Canvas, ce qui permet une expérience plus personnalisée. Consultez ce tableau pour découvrir les filtres disponibles et comment ils segmentent vos utilisateurs en fonction de votre cas d'utilisation.

| Filtre | Description |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Données personnalisées | Segmentez les utilisateurs en fonction d'événements et d'attributs que vous définissez. Permet d'utiliser des fonctionnalités spécifiques à votre produit. |
| Activité de l'utilisateur | Segmentez les clients en fonction de leurs actions et de leurs achats. |
| Reciblage | Segmentez les clients qui ont reçu des Canvas précédents ou qui ont interagi avec eux. |
| Activité marketing | Segmentez les clients en fonction de comportements universels comme le dernier engagement. |
| Attributs de l'utilisateur | Segmentez les clients selon leurs attributs et caractéristiques permanents. |
| Attribution d'installation | Segmentez les clients selon leur première source, groupe publicitaire, Campaign ou annonce. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Le « qui » : sélectionnez une audience" }

### Le « où » : trouvez mon audience {#the-where-find-my-audience}

*Où puis-je le mieux atteindre mon audience ?*

C'est ici que nous déterminons quels canaux de communication sont les plus pertinents pour votre parcours utilisateur. Idéalement, vous souhaitez atteindre vos utilisateurs là où ils sont le plus accessibles. Dans cette optique, vous pouvez utiliser n'importe lequel des canaux suivants avec Canvas :
* [E-mail]({{site.baseurl}}/user_guide/channels/email)
* [Push]({{site.baseurl}}/user_guide/channels/push)
* [Messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages)
* [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
* [SMS ou MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
* [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)

### Le « comment » : construisez l'expérience complète {#the-how-build-the-complete-experience}

*Comment construire mon parcours Canvas après avoir identifié les cinq questions clés ?*

Le « comment » résume la manière dont vous allez créer votre Canvas et atteindre vos utilisateurs avec votre message. Par exemple, pour qu'un message soit efficace, vous devez optimiser le timing de vos envois en tenant compte des fuseaux horaires de vos différents utilisateurs.

Répondre au « comment » détermine également la cadence d'envoi d'un Canvas à votre audience (par exemple une fois par semaine ou toutes les deux semaines), ainsi que les canaux de communication à exploiter pour chaque Canvas que vous créez, comme décrit dans le « où ».

## Cas d'utilisation : flux d'onboarding client {#use-case-customer-onboarding-flow}

Prenons un exemple : vous êtes marketeur chez MovieCanon, une société de streaming en ligne, et vous êtes chargé de créer un flux d'onboarding pour les nouveaux utilisateurs de votre application. En vous appuyant sur les cinq questions clés, vous pourriez construire le Canvas de la manière suivante.

* **Quoi** : notre Canvas s'appellera « New Onboarding Journey ».
* **Pourquoi** : l'objectif de notre Canvas est d'accueillir nos utilisateurs et de les inciter à continuer à utiliser l'application.
* **Quand** : après qu'un utilisateur ouvre l'application pour la première fois, nous souhaitons lui envoyer un e-mail de bienvenue.
* **Qui** : nous ciblons les nouveaux utilisateurs qui utilisent notre application pour la première fois.
* **Où** : nous sommes convaincus de pouvoir atteindre les nouveaux utilisateurs par e-mail, ce qui correspond à notre méthode de communication habituelle.
* **Comment** : nous souhaitons définir un délai d'un jour pour ne pas submerger nos nouveaux utilisateurs de notifications. Après ce délai, nous enverrons un e-mail contenant une liste des films et séries les plus populaires pour les inciter à continuer à utiliser l'application.

## Conseils généraux {#general-tips}

### Déterminer quand et comment utiliser les étapes et les variantes {#determine-when-and-how-to-use-steps-and-variants}

Chaque Canvas doit comporter au moins une variante et au moins une étape. Les possibilités sont infinies à partir de là — alors comment décider de la forme de votre Canvas ? C'est là que vos objectifs, vos données et vos hypothèses entrent en jeu. La réflexion sur le « comment » et le « où » vous aidera à définir la forme et la structure appropriées de votre Canvas.

### Raisonner à rebours {#work-backwards}

Certains objectifs comportent des sous-objectifs plus petits. Par exemple, si vous cherchez à convertir un utilisateur gratuit en abonné, vous aurez peut-être besoin d'une page présentant vos offres d'abonnement. Un visiteur doit peut-être voir les options avant d'acheter. Vous pourriez concentrer vos efforts de communication sur l'affichage de cette page avant la page de paiement. Raisonner à rebours pour comprendre le parcours qu'un client doit suivre pour atteindre votre objectif est essentiel pour le guider vers la conversion.

### Varier vos messages {#mix-up-your-messaging}

Avez-vous déjà lancé une Campaign similaire par le passé ? Ou en avez-vous une en cours actuellement ? Essayez de reprendre ce message et d'y ajouter davantage de personnalisation. Testez un nouveau filtre ou ajoutez un message de suivi. En variant vos techniques de communication, surveillez vos performances et continuez à optimiser en apportant des changements progressifs.