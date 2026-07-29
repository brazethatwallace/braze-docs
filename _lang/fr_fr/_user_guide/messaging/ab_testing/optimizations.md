---
nav_title: Optimisations
article_title: Optimiser les tests A/B avec la variante gagnante ou les variantes personnalisées
page_order: 1
page_type: reference
description: "Découvrez comment utiliser la variante gagnante ou la variante personnalisée lors de la création de tests multivariés et de tests A/B."
---

# Optimiser les tests A/B {#optimize-ab-tests}

> Découvrez comment utiliser l'optimisation des variantes lors de la création de tests multivariés et de tests A/B.


## Notification push {#push}

Lors de la [création d'un test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) pour les notifications push, une option d'optimisation est disponible : [Sélection de variante BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Cette fonctionnalité permet à vos tests A/B à envoi unique ou récurrents d'exécuter automatiquement une expérience et d'optimiser les meilleurs résultats d'engagement.

## E-mail, webhook, SMS et WhatsApp {#email-webhook-sms-and-whatsapp}

Lors de la [création d'un test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) pour des campagnes par e-mail, webhook, SMS et WhatsApp planifiées pour un envoi unique, vous pouvez choisir entre deux options d'optimisation : **Variante gagnante** et **Variante personnalisée**.

![Options d'optimisation présentées dans la section de test A/B lorsque vous choisissez votre audience cible. Trois options sont présentées : pas d'optimisation, variante gagnante et variante personnalisée. Variante personnalisée est sélectionnée.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Les deux options fonctionnent en envoyant un test initial à un pourcentage de votre segment cible. Une fois le test terminé, les utilisateurs restants de votre audience reçoivent soit la variante la plus performante (variante gagnante), soit la variante avec laquelle ils ont le plus de chances d'interagir (variante personnalisée).

{% alert tip %}
Les optimisations se trouvent à l'étape **Audiences cibles** de la création de campagne, sous **A/B Testing**.
{% endalert %}

## Variante gagnante {#winning-variant}

L'envoi de la variante gagnante est similaire à un test A/B standard. Les utilisateurs de ce groupe recevront la variante gagnante une fois le test initial terminé.

1. Sélectionnez **Variante gagnante**, puis indiquez le pourcentage de l'audience de votre campagne à affecter au groupe de la variante gagnante.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- |
| Déterminer la variante gagnante | L'indicateur à optimiser. Choisissez entre *Ouvertures uniques* ou *Clics* pour l'e-mail, *Ouvertures* pour les notifications push, ou *Taux de conversion principal* pour tous les canaux. Sélectionner *Ouvertures* ou *Clics* pour déterminer la variante gagnante n'affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) que vous avez définis pour la campagne. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs de ce groupe ne peuvent pas générer d'*Ouvertures* ou de *Clics*, ce qui signifie que la performance du groupe de contrôle sera forcément de `0`. Par conséquent, le groupe de contrôle ne peut pas remporter le test A/B. Vous pouvez toutefois utiliser un groupe de contrôle pour suivre d'autres indicateurs pour les utilisateurs qui ne reçoivent pas de message. |
| Heure d'envoi de la variante gagnante | La date et l'heure d'envoi de la variante gagnante. |
| Si aucune variante gagnante ne peut être déterminée | Ce qui se passe si aucune variante ne l'emporte avec une marge statistiquement significative. Choisissez entre envoyer quand même la variante la plus performante, ou mettre fin au test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante gagnante" }

{% alert note %}
Pour les variantes gagnantes et les variantes personnalisées, Braze effectue une nouvelle vérification d'éligibilité lors du second envoi. Les utilisateurs qui ne faisaient pas partie du segment cible (ou qui n'étaient pas joignables) lors du premier envoi peuvent y entrer ultérieurement ; les utilisateurs qui ont quitté le segment peuvent ne plus recevoir le message de suivi. Planifiez votre segment et votre planification de sorte que l'audience que vous souhaitez inclure soit éligible aux deux envois.
{% endalert %}

## Variante personnalisée {#personalized-variant}

Utilisez les variantes personnalisées pour envoyer à chaque utilisateur de votre segment cible la variante avec laquelle il est le plus susceptible d'interagir.

Pour déterminer la meilleure variante pour chaque utilisateur, Braze envoie un test initial à une partie de votre audience cible afin d'identifier des corrélations entre les caractéristiques des utilisateurs et leurs préférences en matière de messages. En fonction des réponses des utilisateurs à chaque variante lors du test initial, ces caractéristiques servent à déterminer quelle variante sera envoyée à chacun des utilisateurs restants. Si aucune corrélation n'est trouvée et qu'aucune personnalisation ne peut être effectuée, la variante gagnante est automatiquement envoyée aux utilisateurs restants. Pour en savoir plus sur la façon dont les variantes personnalisées sont déterminées, consultez [Analyse des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#personalized-variant).

1. Sélectionnez **Variante personnalisée**, puis indiquez le pourcentage de l'audience de votre campagne à affecter au groupe de la variante personnalisée.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- |
| Déterminer la variante personnalisée | L'indicateur à optimiser. Choisissez entre *Ouvertures uniques* ou *Clics* pour l'e-mail, *Ouvertures* pour les notifications push, ou *Taux de conversion principal* pour tous les canaux. Sélectionner *Ouvertures* ou *Clics* pour déterminer la variante gagnante n'affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) que vous avez définis pour la campagne. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs de ce groupe ne peuvent pas générer d'*Ouvertures* ou de *Clics*, ce qui signifie que la performance du groupe de contrôle sera forcément de `0`. Par conséquent, le groupe de contrôle ne peut pas remporter le test A/B. Vous pouvez toutefois utiliser un groupe de contrôle pour suivre d'autres indicateurs pour les utilisateurs qui ne reçoivent pas de message. |
| Heure d'envoi de la variante personnalisée | La date et l'heure d'envoi de la variante personnalisée. |
| Si aucune variante personnalisée ne peut être déterminée | Ce qui se passe si aucune variante personnalisée n'est trouvée. Choisissez entre envoyer la variante gagnante à la place, ou mettre fin au test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante personnalisée" }

## Analyse {#analytics}

Pour en savoir plus sur les résultats de votre test A/B avec une optimisation, consultez [Analyse des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).