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

## Conditions préalables {#prerequisites}

Pour profiter de cette fonctionnalité, vous devez effectuer une mise à niveau vers les versions minimales suivantes du SDK :

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Après la mise à niveau du SDK, vos utilisateurs mobiles doivent mettre à jour leur application. Vous pouvez filtrer l'audience de votre campagne ou de votre Canvas pour [cibler uniquement les utilisateurs disposant de ces versions minimales de l'application]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

## Aperçu {#overview}

{% tabs %}
{% tab Campaign %}

Vous pouvez choisir le moment où Braze crée une carte à l'étape **Delivery** lors de la création d'une nouvelle [campagne de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) avec une livraison planifiée.

![Section Contrôles des Content Cards lors de la modification de la livraison d'une Content Card planifiée.]({% image_buster /assets/img_archive/card_creation.png %})

Les options suivantes sont disponibles :

- **At campaign launch :** Le comportement par défaut précédent pour les Content Cards. Braze calcule l'éligibilité de l'audience et la personnalisation au lancement de la campagne, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre application.
- **At first impression (recommended) :** Lorsque l'utilisateur ouvre ensuite votre application (démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze détermine les Content Cards auxquelles l'utilisateur est éligible, applique les modèles de personnalisation comme Liquid ou le Contenu connecté, puis crée la carte. Cette option offre généralement de meilleures performances.

Quelle que soit l'option sélectionnée, le compte à rebours de la date d'expiration de la Content Card commence au lancement de la campagne.

{% endtab %}
{% tab Canvas %}

Vous pouvez choisir le moment où Braze crée une carte dans l'onglet **Messaging Channels** d'une étape [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de type Content Card.

![Section Contrôles des Content Cards lors de la modification de la livraison d'une Content Card planifiée.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Les options suivantes sont disponibles :

- **At step entry :** Le comportement par défaut précédent pour les Content Cards. Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du Canvas, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre application.
- **At first impression (recommended) :** Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du Canvas. Lorsque l'utilisateur ouvre ensuite votre application (démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze applique les modèles de personnalisation comme Liquid ou le Contenu connecté, puis crée la carte. Cette option offre de meilleures performances pour la distribution des cartes et une personnalisation plus à jour.

Quelle que soit l'option sélectionnée, le compte à rebours de la date d'expiration de la Content Card commence lorsque l'utilisateur entre dans l'étape du Canvas.

{% alert tip %}
Si vous souhaitez que les utilisateurs anonymes voient une Content Card dès leur toute première session, utilisez une campagne plutôt qu'un Canvas. En effet, lorsqu'un utilisateur anonyme entre dans un Canvas, sa session a déjà commencé, et il ne recevra donc la Content Card qu'au démarrage d'une nouvelle session.
{% endalert %}

### Événement de suppression {#removal-event}

Sélectionnez l'option permettant de supprimer les Content Cards lorsque les utilisateurs effectuent un achat ou réalisent un événement personnalisé. Pour utiliser **Perform Custom Event** comme événement de suppression, sélectionnez des variables de contexte ou des attributs personnalisés pour les comparaisons lors de l'utilisation de filtres de propriétés.

![Paramètres de l'événement de suppression des Content Cards avec l'option Perform Custom Event sélectionnée et des filtres de propriétés utilisant des variables de contexte ou des attributs personnalisés.]({% image_buster /assets/img/content_card_removal_event.png %})

### Expiration {#expiration}

Dans les paramètres **Expiration (Time in Feed)**, vous pouvez sélectionner **Personalize duration** pour définir l'expiration de la Content Card à l'aide de variables de contexte.

![Paramètres d'expiration affichant l'option Personalize duration configurée avec une variable de contexte pour l'expiration de la Content Card.]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Les Content Cards ont une durée d'expiration maximale de 30 jours, même lorsque vous utilisez une durée personnalisée avec des variables de contexte. Toute valeur définie au-delà de 30 jours est plafonnée à 30 jours. Pour plus de détails, consultez [Expiration de la carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-expiration).
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Pour les deux options, une fois la carte créée, Braze ne recalcule ni l'éligibilité de l'audience ni la personnalisation.
{% endalert %}

### Différences entre la création de cartes au lancement ou à l'entrée et la création à la première impression {#differences}

Cette section décrit les principales différences entre la création de cartes au lancement de la campagne ou à l'entrée dans l'étape, et la création à la première impression.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="Différences entre la création de cartes au lancement ou à l'entrée et la création à la première impression" class="tg">
  <caption>Différences entre la création de cartes au lancement ou à l'entrée et la création à la première impression</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Au lancement de la campagne / À l'entrée dans l'étape du Canvas</th>
    <th class="tg-0pky">À la première impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quand utiliser cette option</td>
    <td class="tg-0pky">Si vous avez besoin que le contenu soit figé à un moment précis (le moment du lancement).</td>
    <td class="tg-0pky"><ul><li>Si vous devez afficher des cartes à de nouveaux utilisateurs ou à des utilisateurs anonymes susceptibles d'entrer dans le segment après le lancement (<a href="#campaign_note">campagnes uniquement*</a>).</li><li>Si vous utilisez la personnalisation et souhaitez que le contenu le plus récent soit disponible sur la carte.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Audience</td>
    <td class="tg-0pky">Braze évalue l'appartenance à l'audience au moment de l'envoi de la campagne.<br><br>Les nouveaux utilisateurs ou les utilisateurs anonymes ne seront pas évalués pour l'éligibilité s'ils tentent de consulter la carte après l'envoi de la campagne. Pour les campagnes récurrentes, l'évaluation se fera au prochain intervalle de récurrence.</td>
    <td class="tg-0pky">Braze évalue l'appartenance lorsque l'utilisateur ouvre ensuite votre application (démarre une session, <a href="#campaign_note">campagnes uniquement*</a>).<br><br>Ce paramètre permet d'atteindre une audience plus large, car tout nouvel utilisateur ou utilisateur anonyme sera toujours évalué pour l'éligibilité lorsqu'il tentera de consulter la carte.<br><br>De plus, la limite de débit (limitation du nombre de personnes qui recevront la carte) ne s'applique pas lorsque l'option est définie sur la première impression.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personnalisation</td>
    <td class="tg-0pky">Braze évalue Liquid, le Contenu connecté et les Content Blocks au moment du lancement de la campagne ou lorsqu'un utilisateur entre dans l'étape du Canvas. Pour les campagnes récurrentes, l'évaluation se fera au prochain intervalle de récurrence.</td>
    <td class="tg-0pky">Braze évalue Liquid, le Contenu connecté et les Content Blocks au moment de la première impression ou après le prochain intervalle de récurrence.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analytique</td>
  <td class="tg-0pky"><em>Messages envoyés</em> correspond au nombre de cartes que Braze a créées et rendues disponibles. Cela ne tient pas compte du fait que les utilisateurs aient consulté la carte ou non.</td>
  <td class="tg-0pky"><em>Messages envoyés</em> correspond au nombre de cartes que Braze envoie à un utilisateur après le démarrage d'une session. Dans Canvas, si un utilisateur entre dans l'étape sans démarrer de session, Braze n'envoie pas de carte, ce qui signifie que cet indicateur peut ne pas correspondre au nombre d'utilisateurs entrant dans une étape.<br><br>Bien que les utilisateurs pouvant être atteints et les impressions ne changent pas, attendez-vous à un volume d'envoi plus faible (<em>Messages envoyés</em>) lorsque vous créez une carte à la première impression par rapport au lancement de la campagne ou à l'entrée dans l'étape du Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Temps de traitement</td>
  <td class="tg-0pky">Braze crée des cartes pour chaque utilisateur éligible du segment au moment du lancement. Pour les audiences volumineuses, sélectionnez <b>At first impression</b> afin que les cartes soient disponibles plus rapidement après le lancement.</td>
  <td class="tg-0pky">Braze crée une carte la première fois qu'un utilisateur tente de la consulter, ce qui peut prendre 1 à 2 secondes pour l'afficher lors de la première impression.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Ce scénario s'applique uniquement aux campagnes, car l'audience du Canvas est évaluée à l'entrée dans le Canvas, et non au niveau de l'étape.</sup></p>

## Considérations {#considerations}

### Campagnes multicanales {#multichannel-campaigns}

Les campagnes multicanales ne prennent pas en charge les cartes à la première impression, de sorte que toutes les Content Cards sont envoyées au lancement de la campagne.

### Utilisation des propriétés de contexte du Canvas {#using-canvas-context-properties}

Lors de la personnalisation des Content Cards avec les [propriétés de contexte du Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), utilisez la syntaxe `${...}` (par exemple, {%raw%}`{{context.${property_name}}}`{%endraw%}). La notation par points sans cette syntaxe (par exemple, {%raw%}`{{context.property_name}}`{%endraw%}) peut ne pas se résoudre correctement dans les Content Cards, même si elle fonctionne dans d'autres canaux comme les notifications push et les e-mails.

### Modification de la création de cartes après le lancement {#changing-card-creation-after-launch}

Braze recommande de ne pas modifier le mode de création des cartes après le lancement d'une campagne. En raison des différences de calcul de la métrique Messages envoyés entre les deux types de création de cartes, modifier le mode de création après le lancement de la campagne peut affecter la précision de votre volume d'envoi.

### Temps de traitement potentiel {#potential-processing-time}

Pour les audiences volumineuses, sélectionnez l'option de création des cartes à la première impression afin que les cartes soient disponibles rapidement après le lancement. Les campagnes déclenchées au démarrage de session peuvent également bénéficier du passage à la création à la première impression (disponible via la livraison planifiée) pour améliorer les performances.

Lorsque les cartes sont créées à la première impression, leur traitement peut prendre quelques secondes. La durée de ce traitement dépend de divers facteurs, tels que la taille de la carte et la complexité des options de modèle de message. Par exemple, le temps de traitement des cartes utilisant le Contenu connecté sera au moins aussi long que le temps de réponse du Contenu connecté.

### Versions antérieures du SDK {#previous-sdk-versions}

Si l'application d'un utilisateur fonctionne avec une version antérieure du SDK, il recevra tout de même les Content Cards que vous envoyez. Cependant, les cartes mettront plus de temps à apparaître et pourraient ne s'afficher qu'à la prochaine synchronisation des Content Cards.