---
nav_title: Types de distribution et d'entrée
article_title: Types de distribution et d'entrée
page_order: 5
page_type: reference
description: "Cet article de référence décrit les types de distribution pour les campagnes, les types d'entrée pour les Canvas et les fonctionnalités temporelles lors de la configuration d'une campagne ou d'un Canvas."
tool:
    - Campaigns
    - Canvas
---

# Types de distribution et d'entrée {#delivery-and-entry-types}

> Dans Braze, il existe trois façons différentes de planifier votre message : planifié, par événement et déclenché par API. Choisir comment et quand votre message est distribué est essentiel pour développer un message efficace.

Pour les campagnes, le type de distribution détermine quand vos utilisateurs entreront dans votre campagne et quand elle sera envoyée. Comme un Canvas est conçu comme un parcours utilisateur continu, le concept de planification de l'envoi de messages est appelé type d'entrée.

| Types de distribution<nobr> et d'entrée | Description |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Planification** | Ce type de planification est conçu pour les messages ponctuels que vous souhaitez envoyer immédiatement, comme les campagnes relatives à un événement en cours. <br><br>Lors de l'envoi de messages de test destinés uniquement à vous-même ou à votre équipe, cette option vous permet de les distribuer immédiatement. |
| **Livraison par événement** | Les messages de livraison par événement, ou les campagnes et Canvas déclenchés par événement, sont très efficaces pour les messages transactionnels ou basés sur des accomplissements. Vous pouvez les déclencher pour qu'ils soient envoyés après qu'un utilisateur a effectué une certaine action, au lieu d'envoyer votre message à des jours précis. |
| **Déclenché par API** | Les messages déclenchés par API vous permettent de gérer le contenu du message, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze tout en déclenchant la distribution de ce contenu depuis vos propres serveurs et systèmes. <br><br>La requête API pour déclencher le message peut également inclure des données supplémentaires à intégrer dans le message en temps réel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de distribution et d'entrée" }

## Options temporelles {#time-based-options}

{% tabs %}
{% tab campaign %}
Vous pouvez choisir parmi les options suivantes lors de l'utilisation de la distribution planifiée :

- Envoyer dès le lancement de la campagne
- Envoyer à une heure désignée
- [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)
{% endtab %}

{% tab canvas %}
Avec la distribution planifiée, les utilisateurs entreront selon un calendrier, de la même manière que vous planifieriez une campagne. Vous pouvez inscrire les utilisateurs dans un Canvas dès son lancement ou à une heure désignée.

### Heures désignées {#designated-times}

Vous pouvez choisir d'envoyer votre Canvas à une fréquence d'entrée spécifique, y compris une seule fois, quotidiennement, hebdomadairement ou mensuellement. Pour les Canvas avec une distribution planifiée récurrente, vous pouvez définir la récurrence pour permettre aux utilisateurs d'entrer dans le Canvas jusqu'à 30 fois.
{% endtab %}
{% endtabs %}

## Options de livraison par événement {#action-based-options}

{% tabs %}
{% tab campaign %}
La livraison par événement enverra les campagnes aux utilisateurs qui effectuent une action spécifique. Après cette action, vous pouvez décider quand envoyer la campagne : immédiatement, après un délai spécifique, à une heure précise ou à un moment futur.
{% endtab %}

{% tab canvas %}
Les options de livraison par événement déterminent quelles actions (ou déclencheurs) un utilisateur doit effectuer pour entrer dans un Canvas et à quel moment précis il est autorisé à commencer à y entrer. Par exemple, vous pourriez évaluer vos utilisateurs en fonction des actions suivantes :

- Ouverture de votre application
- Ajout d'une adresse e-mail
- Entrée dans un emplacement

### Fenêtre d'entrée {#entry-window}

La fenêtre d'entrée de votre Canvas détermine quels utilisateurs peuvent entrer dans le Canvas à l'heure de début désignée (et à l'heure de fin facultative). Comme pour les campagnes basées sur des événements, vous pouvez choisir d'inscrire les utilisateurs dans leur fuseau horaire local.
{% endtab %}
{% endtabs %}

## Options de déclenchement par API {#api-trigger-options}

{% tabs %}
{% tab campaign %}
Lorsque vous sélectionnez le déclenchement par API comme option de distribution, vous recevrez un ID de campagne pour identifier quelle campagne envoyer avec l'[endpoint `/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites).
{% endtab %}

{% tab canvas %}
Lorsque vous sélectionnez le déclenchement par API comme type d'entrée, vous recevrez un ID de Canvas pour identifier quel Canvas envoyer avec l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/).
{% endtab %}
{% endtabs %}