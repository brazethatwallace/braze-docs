---
nav_title: Création de carte
article_title: Création de carte
alias: /card_creation/
description: "Cet article décrit les différences entre la création de Content Cards au lancement de la campagne ou à l'entrée dans l'étape du Canvas, et la création à la première impression."
page_order: 0
tool: Campaigns
channel:
  - content cards
toc_headers: h2
---

# Création de carte {#card-creation}

> Vous pouvez choisir le moment où Braze évalue l'éligibilité de l'audience et la personnalisation pour les nouvelles campagnes de Content Cards et les étapes du Canvas, en spécifiant quand la carte est créée.

## Prérequis {#prerequisites}

Pour tirer parti de cette fonctionnalité, vous devez effectuer la mise à niveau vers les versions minimales suivantes du SDK :

{% sdk_min_versions swift:5.2.0 objc:4.5.0 android:23.0.0 web:4.2.0 %}

Sur iOS, le SDK Swift prend en charge cette fonctionnalité à partir de la version 5.2.0, et l'ancien SDK Objective-C la prend en charge à partir de la version 4.5.0. Les versions 5.0.0 à 5.1.x du SDK Swift ne la prennent pas en charge.

Après la mise à niveau du SDK, vos utilisateurs mobiles doivent mettre à jour leur application. Vous pouvez filtrer l'audience de votre Campaign ou Canvas pour [cibler uniquement les utilisateurs disposant de ces versions minimales de l'application]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

## Aperçu {#overview}

{% tabs %}
{% tab Campaign %}

Vous pouvez choisir le moment où Braze crée une carte à l'étape **Réception** lors de la création d'une nouvelle [campagne de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) avec une distribution planifiée.

![Section Contrôles des Content Cards lors de la modification de la distribution d'une Content Card planifiée.]({% image_buster /assets/img_archive/card_creation.png %})

Les options suivantes sont disponibles :

- **Au lancement de la campagne :** le comportement par défaut précédent pour les Content Cards. Braze évalue l'éligibilité de l'audience et la personnalisation au moment du lancement de la campagne, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre application.
- **À la première impression (recommandé) :** lorsque l'utilisateur ouvre ensuite votre application (démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze détermine les Content Cards auxquelles l'utilisateur est éligible, applique les modèles de personnalisation comme Liquid ou le contenu connecté, puis crée la carte. Cette option offre généralement de meilleures performances.

Quelle que soit l'option sélectionnée, le compte à rebours de la date d'expiration de la Content Card commence au lancement de la campagne.

{% endtab %}
{% tab Canvas %}

Vous pouvez choisir le moment où Braze crée une carte dans l'onglet **Canaux de communication** d'une [étape de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) Content Card.

![Section Contrôles des Content Cards lors de la modification de la distribution d'une Content Card planifiée.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Les options suivantes sont disponibles :

- **À l'entrée de l'étape :** le comportement par défaut précédent pour les Content Cards. Braze évalue l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape Canvas, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre application.
- **À la première impression (recommandé) :** Braze évalue l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape Canvas. Lorsque l'utilisateur ouvre ensuite votre application (démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze applique les modèles de personnalisation comme Liquid ou le contenu connecté, puis crée la carte. Cette option offre de meilleures performances dans la distribution des cartes et une personnalisation plus à jour.

Quelle que soit l'option sélectionnée, le compte à rebours de la date d'expiration de la Content Card commence lorsque l'utilisateur entre dans l'étape Canvas.

{% alert tip %}
Si vous souhaitez que des utilisateurs anonymes voient une Content Card lors de leur toute première session, utilisez une campagne plutôt qu'un Canvas. En effet, lorsqu'un utilisateur anonyme entre dans un Canvas, sa session a déjà commencé, il ne recevra donc pas la Content Card avant de démarrer une nouvelle session.
{% endalert %}

### Événement de suppression {#removal-event}

Sélectionnez l'option permettant de supprimer les Content Cards lorsque les utilisateurs effectuent un achat ou réalisent un événement personnalisé. Pour utiliser **Réaliser un événement personnalisé** comme événement de suppression, sélectionnez des variables de contexte ou des attributs personnalisés pour les comparaisons lors de l'utilisation de filtres de propriétés.

![Paramètres d'événement de suppression des Content Cards avec l'option Réaliser un événement personnalisé sélectionnée et des filtres de propriétés utilisant des variables de contexte ou des attributs personnalisés.]({% image_buster /assets/img/content_card_removal_event.png %})

### Expiration {#expiration}

Dans les paramètres **Expiration (durée dans le fil)**, vous pouvez sélectionner **Personnaliser la durée** pour définir l'expiration de la Content Card à l'aide de variables de contexte.

![Paramètres d'expiration montrant l'option Personnaliser la durée configurée avec une variable de contexte pour l'expiration de la Content Card.]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Les Content Cards ont une expiration maximale de 30 jours, même en utilisant une durée personnalisée avec des variables de contexte. Toute valeur définie au-delà de 30 jours est plafonnée à 30 jours. Pour plus de détails, consultez [Expiration de la carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-expiration).
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Pour les deux options, une fois la carte créée, Braze ne recalcule pas l'éligibilité de l'audience ni la personnalisation.
{% endalert %}

### Différences entre la création de cartes au lancement ou à l'entrée et à la première impression {#differences}

Cette section décrit les principales différences entre la création de cartes au lancement de la campagne ou à l'entrée de l'étape et la création à la première impression.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="Différences entre la création de cartes au lancement ou à l'entrée et à la première impression" class="tg">
  <caption>Différences entre la création de cartes au lancement ou à l'entrée et à la première impression</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Au lancement de la campagne / À l'entrée de l'étape Canvas</th>
    <th class="tg-0pky">À la première impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quand utiliser cette option</td>
    <td class="tg-0pky">Si vous avez besoin que le contenu soit figé à un moment précis (l'heure de lancement).</td>
    <td class="tg-0pky"><ul><li>Si vous devez afficher des cartes à de nouveaux utilisateurs ou des utilisateurs anonymes qui peuvent entrer dans le segment après le lancement (<a href="#campaign_note">campagnes uniquement*</a>).</li><li>Si vous utilisez la personnalisation et souhaitez que le contenu le plus récent soit disponible sur la carte.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Audience</td>
    <td class="tg-0pky">Braze évalue l'appartenance à l'audience lorsque la campagne est envoyée.<br><br>Les nouveaux utilisateurs ou les utilisateurs anonymes ne seront pas évalués pour l'éligibilité s'ils tentent de voir la carte après l'envoi de la campagne. Pour les campagnes récurrentes, ce sera au prochain intervalle de récurrence.</td>
    <td class="tg-0pky">Braze évalue l'appartenance lorsque l'utilisateur ouvre ensuite votre application (démarre une session, <a href="#campaign_note">campagnes uniquement*</a>).<br><br> Ce paramètre offre une portée d'audience plus large, car tout nouvel utilisateur ou utilisateur anonyme sera toujours évalué pour l'éligibilité lorsqu'il tente de voir la carte. <br><br>De plus, la limitation du débit (limiter le nombre de personnes qui recevront la carte) ne s'applique pas lorsque l'option est définie sur la première impression.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personnalisation</td>
    <td class="tg-0pky">Braze évalue Liquid, le contenu connecté et les Content Blocks au moment du lancement de la campagne ou lorsqu'un utilisateur entre dans l'étape Canvas. Pour les campagnes récurrentes, ce sera au prochain intervalle de récurrence.</td>
    <td class="tg-0pky">Braze évalue Liquid, le contenu connecté et les Content Blocks au moment de la première impression ou après le prochain intervalle de récurrence.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analyse</td>
  <td class="tg-0pky"><em>Messages envoyés</em> fait référence au nombre de cartes que Braze a créées et rendues disponibles. Cela ne comptabilise pas si les utilisateurs ont vu la carte.</td>
  <td class="tg-0pky"><em>Messages envoyés</em> fait référence au nombre de cartes que Braze envoie à un utilisateur après le début d'une session. Dans Canvas, si un utilisateur entre dans l'étape sans démarrer de session, Braze n'envoie pas de carte, cette métrique peut donc ne pas correspondre au nombre d'utilisateurs entrant dans une étape.<br><br>Bien que les utilisateurs joignables et les impressions ne changent pas, attendez-vous à un volume d'envoi plus faible (<em>Messages envoyés</em>) lorsque vous créez une carte à la première impression par rapport au lancement de la campagne ou à l'entrée de l'étape Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Temps de traitement</td>
  <td class="tg-0pky">Braze crée des cartes pour chaque utilisateur éligible du segment au moment du lancement. Pour les audiences importantes, sélectionnez <b>À la première impression</b> afin que les cartes soient disponibles plus rapidement après le lancement.</td>
  <td class="tg-0pky">Braze crée une carte la première fois qu'un utilisateur tente de la voir, ce qui peut prendre 1 à 2 secondes pour s'afficher lors de la première impression.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Ce scénario s'applique uniquement aux campagnes, car l'audience Canvas est évaluée à l'entrée du Canvas, et non au niveau de l'étape.</sup></p>

## Considérations {#considerations}

### Campaigns multicanales {#multichannel-campaigns}

Les Campaigns multicanales ne prennent pas en charge les cartes à la première impression, de sorte que toutes les Content Cards sont envoyées au lancement de la campagne.

### Utiliser les propriétés de contexte Canvas {#using-canvas-context-properties}

Lors de la personnalisation des Content Cards avec les [propriétés de contexte Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), utilisez la syntaxe `${...}` (par exemple, {%raw%}`{{context.${property_name}}}`{%endraw%}). La notation par points sans cette syntaxe (par exemple, {%raw%}`{{context.property_name}}`{%endraw%}) peut ne pas se résoudre correctement dans les Content Cards, même si elle fonctionne dans d'autres canaux comme les notifications push et l'e-mail.

### Modifier la création de cartes après le lancement {#changing-card-creation-after-launch}

Braze recommande de ne pas modifier la façon dont les cartes sont créées après le lancement d'une campagne. En raison des différences dans le calcul des Messages envoyés entre les deux types de création de cartes, modifier la méthode de création après le lancement de la campagne peut affecter la précision de votre volume d'envoi.

### Temps de traitement potentiel {#potential-processing-time}

Pour les audiences importantes, sélectionnez l'option de création des cartes à la première impression afin qu'elles soient disponibles rapidement après le lancement. Les Campaigns déclenchées au démarrage de session peuvent également bénéficier du passage à la création à la première impression (disponible via la distribution planifiée) pour améliorer les performances.

Lorsque les cartes sont créées à la première impression, leur traitement peut prendre quelques secondes. La durée de ce traitement dépend de divers facteurs, tels que la taille de la carte et la complexité des options de modélisation du message. Par exemple, le temps de traitement des cartes utilisant le contenu connecté est au moins aussi long que le temps de réponse du contenu connecté.

### Versions précédentes du SDK {#previous-sdk-versions}

Si l'application d'un utilisateur fonctionne avec une version précédente du SDK, il recevra toujours les Content Cards que vous envoyez. Cependant, les cartes mettent plus de temps à apparaître et peuvent ne s'afficher qu'à la prochaine synchronisation des Content Cards.