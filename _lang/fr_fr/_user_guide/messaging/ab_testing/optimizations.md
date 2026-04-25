---
nav_title: Optimisations
article_title: Optimisez les tests A/B avec une variante gagnante ou des variantes personnalisées
page_order: 1
page_type: reference
description: "Découvrez comment utiliser la variante gagnante ou la variante personnalisée lors de la création de tests multivariés et de tests A/B."
---

# Optimisez les tests A/B avec la variante gagnante ou les variantes personnalisées. {#optimize-ab-tests-with-winning-variant-or-personalized-variants}

> Découvrez comment utiliser la variante gagnante ou la variante personnalisée lors de la création de tests multivariés et de tests A/B.

Lors de la [création d'un test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) pour des campagnes e-mail, push, webhook, SMS et WhatsApp planifiées pour un envoi unique, vous pouvez sélectionner une optimisation. Il existe deux options d'optimisation : **Variante gagnante** et **Variante personnalisée**.

![Options d'optimisation présentées dans la section de test A/B lorsque vous choisissez votre audience cible. Trois options sont présentées : Pas d'optimisation, variante gagnante et variante personnalisée. Variante personnalisée est sélectionnée.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Les deux options fonctionnent en envoyant un test initial à un pourcentage de votre segment cible. Après la fin du test, les utilisateurs restants de votre audience sont envoyés soit à la variante la plus efficace (Variante gagnante) soit à la variante avec laquelle ils ont le plus de chance d'interagir (Variante personnalisée).

{% alert tip %}
Les optimisations sont situées dans l'étape **Audiences cibles** de la création de la campagne, sous **Test A/B**.
{% endalert %}

## Variante gagnante {#winning-variant}

L'envoi de la variante gagnante est similaire à un test A/B standard. Les utilisateurs de ce groupe recevront la variante gagnante une fois le test initial terminé.

1. Sélectionnez **Variante gagnante**, puis indiquez le pourcentage de l'audience de votre campagne à affecter au groupe de la variante gagnante.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- |
| Déterminer la variante gagnante | L'indicateur à optimiser. Choisissez entre *Ouvertures uniques* ou *Clics* pour l'e-mail, *Ouvertures* pour les notifications push, ou *Taux de conversion principal* pour tous les canaux. Sélectionner *Ouvertures* ou *Clics* pour déterminer la variante gagnante n'affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) que vous avez définis pour la campagne. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs de ce groupe ne peuvent pas générer d'*Ouvertures* ou de *Clics*, ce qui signifie que la performance du groupe de contrôle sera forcément de `0`. Par conséquent, le groupe de contrôle ne peut pas remporter le test A/B. Vous pouvez toutefois utiliser un groupe de contrôle pour suivre d'autres indicateurs pour les utilisateurs qui ne reçoivent pas de message. |
| Heure d'envoi de la variante gagnante | La date et l'heure d'envoi de la variante gagnante. |
| Si aucune variante gagnante ne peut être déterminée | Ce qui se passe si aucune variante ne l'emporte avec une marge statistiquement significative. Choisissez entre envoyer quand même la variante la plus performante, ou mettre fin au test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante personnalisée {#personalized-variant}

Utilisez les variantes personnalisées pour envoyer à chaque utilisateur de votre segment cible la variante avec laquelle il est le plus susceptible d'interagir.

Pour déterminer la meilleure variante pour chaque utilisateur, Braze envoie un test initial à une partie de votre audience cible afin d'identifier des corrélations entre les caractéristiques des utilisateurs et leurs préférences en matière de messages. En fonction des réponses des utilisateurs à chaque variante lors du test initial, ces caractéristiques servent à déterminer quelle variante sera envoyée à chacun des utilisateurs restants. Si aucune corrélation n'est trouvée et qu'aucune personnalisation ne peut être effectuée, la variante gagnante est automatiquement envoyée aux utilisateurs restants. Pour en savoir plus sur la façon dont les variantes personnalisées sont déterminées, consultez [Analyse des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#personalized-variant).

1. Sélectionnez **Variante personnalisée**, puis indiquez le pourcentage de l'audience de votre campagne à affecter au groupe de la variante personnalisée.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- |
| Déterminer la variante personnalisée | L'indicateur à optimiser. Choisissez entre *Ouvertures uniques* ou *Clics* pour l'e-mail, *Ouvertures* pour les notifications push, ou *Taux de conversion principal* pour tous les canaux. Sélectionner *Ouvertures* ou *Clics* pour déterminer la variante gagnante n'affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) que vous avez définis pour la campagne. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs de ce groupe ne peuvent pas générer d'*Ouvertures* ou de *Clics*, ce qui signifie que la performance du groupe de contrôle sera forcément de `0`. Par conséquent, le groupe de contrôle ne peut pas remporter le test A/B. Vous pouvez toutefois utiliser un groupe de contrôle pour suivre d'autres indicateurs pour les utilisateurs qui ne reçoivent pas de message. |
| Heure d'envoi de la variante personnalisée | La date et l'heure d'envoi de la variante personnalisée. |
| Si aucune variante personnalisée ne peut être déterminée | Ce qui se passe si aucune variante personnalisée n'est trouvée. Choisissez entre envoyer la variante gagnante à la place, ou mettre fin au test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Analyse {#analytics}

Pour en savoir plus sur les résultats de votre test A/B avec une optimisation, consultez [Analyse des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).