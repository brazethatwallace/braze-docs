---
nav_title: Comportement du Dispatch ID
article_title: Comportement du Dispatch ID
page_order: 0

page_type: solution
description: "Cet article d'aide couvre le comportement du dispatch ID, y compris son utilisation, ses implications et ses limites."
---

# Comportement du Dispatch ID {#dispatch-id-behavior}

Un `dispatch_id` est l'identifiant de la transmission du message — un ID unique pour chaque « dispatch » envoyé par Braze. Les utilisateurs qui reçoivent un message planifié reçoivent le même `dispatch_id`. En règle générale, les messages basés sur une action ou déclenchés par une API recevront un `dispatch_id` unique par utilisateur, mais les messages envoyés à proximité d'un autre peuvent partager le même `dispatch_id` entre plusieurs utilisateurs.

Ainsi, deux utilisateurs différents peuvent avoir des dispatch ID différents pour une même Campaign si les messages ont été envoyés à deux moments différents. Ceci est souvent dû au fait que les requêtes API ont été effectuées séparément. Si les deux utilisateurs faisaient partie de la même audience de Campaign lors d'un envoi unique, leurs dispatch ID seraient les mêmes.

## Comportement du dispatch ID dans les Campaigns {#dispatch-id-behavior-in-campaigns}

Les messages de Campaign planifiés ont le même `dispatch_id`. Les messages de Campaign basés sur des actions ou déclenchés par l'API peuvent obtenir un `dispatch_id` unique par utilisateur, ou le `dispatch_id` peut être le même pour plusieurs utilisateurs lorsqu'il est envoyé à proximité immédiate ou dans le cadre du même appel API, comme décrit ci-dessus. Par exemple, deux utilisateurs faisant partie de l'audience de votre Campaign planifiée auront le même `dispatch_id` chaque fois que la Campaign est planifiée. Toutefois, deux utilisateurs faisant partie de l'audience d'une Campaign déclenchée par une API peuvent avoir des dispatch ID différents s'ils ont été envoyés lors d'appels API distincts et ne se trouvent pas à proximité l'un de l'autre.

Les Campaigns multicanal auront le comportement décrit pour leur type de distribution.

{% alert warning %}
Un `dispatch_id` est généré de manière aléatoire pour toutes les étapes du Canvas, car Braze considère les étapes du Canvas comme des événements déclenchés, même lorsqu'elles sont « planifiées ». Cela peut entraîner des incohérences dans la génération des ID. Il arrive qu'un composant Canvas ait un `dispatch_id` unique par utilisateur et par envoi, ou qu'il ait des dispatch ID partagés entre les utilisateurs par envoi.
{% endalert %}

## Intégrer le dispatch ID dans les messages avec Liquid {#template-dispatch-id-into-messages-with-liquid}

Si vous souhaitez suivre l'envoi d'un message à partir du message lui-même (dans une URL, par exemple), vous pouvez intégrer le `dispatch_id`. Vous trouverez le formatage correspondant sous les attributs Canvas dans notre liste des [balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

Le comportement est exactement identique à celui de `api_id` : comme `api_id` n'est pas disponible lors de la création de la Campaign, il est intégré sous forme de marque substitutive et sera prévisualisé comme `dispatch_id_for_unsent_campaign`. L'ID est généré avant l'envoi du message et sera inclus au moment de l'envoi.

{% alert warning %}
Le templating Liquid de `dispatch_id_for_unsent_campaign` ne fonctionne pas avec les messages in-app, car les messages in-app n'ont pas de `dispatch_id`.
{% endalert %}

## Champ dispatch ID Currents pour l'e-mail {#dispatch-id-currents-field-for-email}

Dans le but de continuer à améliorer nos capacités Currents, `dispatch_id` est également un champ dans les événements d'e-mail Currents pour tous les types de connecteurs. Le `dispatch_id` est l'ID unique généré pour chaque transmission (« dispatch ») envoyée depuis la plateforme Braze.

Alors que tous les clients qui reçoivent un message planifié reçoivent le même `dispatch_id`, les clients qui reçoivent des messages basés sur des actions ou déclenchés par une API auront un `dispatch_id` unique par message. Le champ `dispatch_id` vous permet d'identifier quelle instance d'une Campaign récurrente est responsable de la conversion, ce qui vous fournit davantage d'informations sur les types de campagnes qui contribuent à atteindre vos objectifs métier.

Vous pouvez utiliser `dispatch_id` comme [balise de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), dans les [événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) ou lorsque vous utilisez [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) ou [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) pour Currents.

_Dernière mise à jour le 15 juillet 2021_