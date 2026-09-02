---
nav_title: Évaluation de la qualité et limites d'envoi de messages
article_title: Évaluation de la qualité et limites d'envoi de messages
description: "Cet article de référence explique comment Meta influence votre évaluation de la qualité et vos limites d'envoi de messages pour le canal WhatsApp."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
---

# Évaluation de la qualité et limites d'envoi de messages {#quality-rating-and-messaging-limits}

> Meta influence votre évaluation de la qualité et vos [limites d'envoi de messages](https://developers.facebook.com/docs/whatsapp/messaging-limits) dès que vous commencez à utiliser le canal WhatsApp, et continuera de les influencer en fonction de votre utilisation de WhatsApp.

## Définitions {#definitions}

| Terme | Définition |
| --- | --- |
| Évaluation de la qualité | Une évaluation basée sur les messages récents que vos clients ont reçus au cours des sept derniers jours. Cette évaluation est déterminée par les retours de vos clients, tels que les raisons de bloquer votre numéro de téléphone et d'autres signalements. Consultez la documentation de Meta pour en savoir plus [sur votre évaluation de la qualité](https://www.facebook.com/business/help/896873687365001). |
| Limite d'envoi de messages | Le nombre maximum de conversations initiées par l'entreprise que vous pouvez démarrer avec chacun de vos numéros de téléphone sur une période glissante de 24 heures. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définitions" }

## Onboarding {#onboarding}

Lorsqu'un nouveau compte WhatsApp Business est créé, Meta utilise divers facteurs pour déterminer la limite d'envoi initiale. Vous pouvez trouver cette limite dans votre WhatsApp Business gestionnaire, ainsi que des détails supplémentaires sur votre page Phone Number Insights.

Consultez la documentation de Meta pour en savoir plus sur la [vérification de votre limite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) et les [exigences relatives aux numéros de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Débit {#throughput}

Meta attribue à chaque numéro de téléphone professionnel enregistré un débit initial de 80 messages par seconde. Les mises à niveau vers 1 000 messages par seconde peuvent se faire automatiquement ou sur demande.

Consultez la documentation de Meta pour en savoir plus sur votre [débit](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Régulation du rythme des modèles {#template-pacing}

Les modèles marketing récemment créés et les modèles marketing mis en pause puis réactivés sont potentiellement soumis à une régulation du rythme d'envoi. Les critères de sélection de la régulation par Meta sont principalement déterminés par l'historique de qualité de vos modèles. Lorsque vous utilisez un modèle marketing récemment créé ou récemment réactivé, les messages sont envoyés normalement jusqu'à ce qu'un seuil non spécifié soit atteint. Une fois ce seuil atteint, les messages suivants utilisant ce modèle sont retenus afin de laisser suffisamment de temps pour recueillir les retours des clients.

Consultez la documentation de Meta pour en savoir plus sur la [régulation du rythme des modèles](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).