---
nav_title: Dispatch ID
article_title: Comportement du Dispatch ID
page_order: 5.2
page_type: reference
description: "Cet article de référence décrit le comportement du dispatch ID pour les Campaigns, Canvas, Liquid et Currents."
---

# Comportement du Dispatch ID {#dispatch-id-behavior}

> Le `dispatch_id` est un ID unique pour chaque envoi de message, ou « transmission », envoyé depuis Braze.

## Comportement du dispatch ID dans les campagnes {#dispatch-id-behavior-in-campaigns}

Les messages de Campaign planifiés reçoivent le même `dispatch_id`. Les messages de Campaign déclenchés par une action ou par l'API peuvent recevoir un `dispatch_id` unique par utilisateur, ou le `dispatch_id` peut être identique pour plusieurs utilisateurs lorsqu'ils sont envoyés à des moments rapprochés ou dans le même appel API. Par exemple, deux utilisateurs dans l'audience de votre Campaign planifiée ont le même `dispatch_id` chaque fois que la Campaign est planifiée. Cependant, deux utilisateurs dans l'audience d'une Campaign déclenchée par l'API peuvent avoir des dispatch ID différents si les Campaigns ont été envoyées dans des appels API distincts et non à des moments rapprochés.

Les Campaigns multicanales ont le même comportement pour leur type de distribution.

{% alert warning %}
Un `dispatch_id` est généré aléatoirement pour toutes les étapes Canvas, car Braze traite les étapes Canvas comme des événements déclenchés, même lorsqu'elles sont « planifiées ». Cela peut entraîner des incohérences dans la génération des ID. Parfois, un composant Canvas a un `dispatch_id` unique par utilisateur et par envoi, ou il peut avoir des dispatch ID partagés entre les utilisateurs par envoi.
{% endalert %}

## Intégrer le dispatch ID dans les messages avec Liquid {#template-dispatch-id-into-messages-with-liquid}

Si vous souhaitez suivre l'envoi d'un message depuis l'intérieur même du message (dans une URL, par exemple), vous pouvez intégrer le `dispatch_id` via un template Liquid. Vous trouverez le format correspondant sous les attributs Canvas dans la liste des [tags de personnalisation pris en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Ce fonctionnement est similaire à celui de l'`api_id` : comme l'`api_id` n'est pas disponible au moment de la création de la Campaign, Braze l'intègre sous forme de marque substitutive qui s'affiche en aperçu sous la forme `dispatch_id_for_unsent_campaign`. L'ID est généré avant l'envoi du message et est inclus au moment de l'envoi.

{% alert warning %}
Le templating Liquid de `dispatch_id_for_unsent_campaign` ne fonctionne pas avec les In-App Messages, car ceux-ci ne possèdent pas de `dispatch_id`.
{% endalert %}

## Champ `dispatch_id` de Currents pour les e-mails {#dispatch-id-currents-field-for-email}

Le champ `dispatch_id` est disponible dans les événements e-mail Currents pour tous les types de connecteurs. Le `dispatch_id` est l'ID unique généré pour chaque transmission, ou envoi, effectué depuis la plateforme Braze.

Bien que tous les clients qui reçoivent un message planifié obtiennent le même `dispatch_id`, les clients qui reçoivent des messages déclenchés par une action ou par l'API reçoivent un `dispatch_id` unique par message. Le champ `dispatch_id` vous permet d'identifier quelle instance d'une Campaign récurrente est responsable de la conversion, afin de déterminer quels types de Campaigns génèrent des résultats.

Vous pouvez utiliser `dispatch_id` comme [tag de personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), dans les [événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), ou lorsque vous utilisez [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents), [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel#supported-currents-events) ou [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents) pour Currents.