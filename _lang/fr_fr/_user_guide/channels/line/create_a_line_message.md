---
nav_title: Créer un message LINE
article_title: Créer un message LINE
page_order: 1
description: "Cet article explique comment créer une campagne ou un Canvas de messages LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Créer un message LINE {#create-a-line-message}

> Les campagnes LINE peuvent atteindre directement vos clients et discuter avec eux de manière programmatique. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnalisée avec vos utilisateurs et favoriser une expérience utilisateur discrète avec votre marque.

## Conditions préalables {#prerequisites}

Avant de créer un message LINE, procédez comme suit :

1. Lisez l'aperçu de LINE.
2. Prenez connaissance des politiques, limites et règles de contenu.
3. [Configurez votre connexion LINE]({{site.baseurl}}/user_guide/channels/line/line_setup).

L'envoi de messages LINE depuis Braze consomme les crédits de messages ou d'actions de votre compte.

## Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux envois de messages ciblés uniques, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **LINE** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel Campaign**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et la création de rapports.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes ajoutées. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, rédigez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) à l'aide du compositeur Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le générateur Canvas. Donnez à votre étape un nom clair et significatif.
3. Choisissez une [planification d'étape]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Choisissez tout autre canal de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Rédiger votre message LINE {#step-2-compose-your-line-message}

Rédigez votre message en utilisant la personnalisation (comme Liquid ou le contenu connecté) selon vos besoins. LINE autorise jusqu'à cinq bulles de message par message, qui peuvent utiliser n'importe quelle disposition disponible : texte, image, enrichi ou basé sur des cartes.

![Compositeur LINE avec un message affiché dans la prévisualisation.]({% image_buster /assets/img/line/line_composer.png %})

### Conseils {#tips}

#### Utiliser Liquid {#using-liquid}

Si vous prévoyez d'utiliser Liquid, veillez à inclure une valeur par défaut pour votre personnalisation. Cela évitera que les destinataires ayant des profils utilisateur incomplets reçoivent une marque substitutive vide. Par exemple, au lieu qu'un utilisateur reçoive le message « Bonjour, ! », il pourrait recevoir le message « Bonjour, nouvel abonné ! ».

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Créer des messages de droite à gauche {#creating-right-to-left-messages}

L'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les affichent. Pour connaître les bonnes pratiques de rédaction de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Étape 3 : Prévisualiser et tester votre message {#step-3-preview-and-test-your-message}

Passez à l'onglet **Test** pour envoyer un message LINE de test à des groupes de test de contenu ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

![L'onglet « Tests » affichant une prévisualisation d'un message de test.]({% image_buster /assets/img/line/test_preview.png %})

Pour en savoir plus, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

## Étape 4 : Construire le reste de votre campagne ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages LINE.

### Choisir la planification ou le déclencheur de livraison {#choose-delivery-schedule-or-trigger}

Les messages LINE peuvent être envoyés selon un horaire planifié, une action ou un déclencheur API. Pour en savoir plus sur les options de planification et de déclenchement, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Vous pouvez spécifier des contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#campaigns) pour recevoir la campagne, ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping). Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

### Choisir les utilisateurs à cibler {#choose-users-to-target}

[Ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des segments ou des filtres pour affiner votre audience. Vous devriez avoir déjà choisi le groupe d'abonnement, qui restreint les utilisateurs selon le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous.

Sélectionnez l'audience la plus large parmi vos segments, puis affinez éventuellement ce segment davantage avec nos [filtres]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Vous recevez automatiquement un aperçu de la population approximative de ce segment. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple :

- Si vous utilisez le géociblage pour déclencher un message LINE dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur `Purchase`.
- Si vous essayez d'inciter l'utilisateur à ouvrir votre application, définissez l'événement de conversion sur `Starts Session`.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Soyez créatif et réfléchissez à la manière dont vous souhaitez mesurer le succès de cette campagne.

{% endtab %}
{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre Canvas. Pour plus de détails sur la construction du reste de votre Canvas, l'utilisation des tests multivariés et de la sélection intelligente, et plus encore, consultez [Créer un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

## Étape 5 : Vérifier et déployer {#step-5-review-and-deploy}

Après avoir terminé la construction de votre campagne ou Canvas, vérifiez ses détails, testez-le, puis envoyez-le !

Ensuite, consultez les [rapports LINE]({{site.baseurl}}/line/reporting) pour découvrir comment accéder aux résultats de vos campagnes LINE.