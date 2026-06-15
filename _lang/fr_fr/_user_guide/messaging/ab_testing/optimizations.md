---
nav_title: Optimisations
article_title: Optimisez les tests A/B avec une variante gagnante ou des variantes personnalisées
page_order: 1
page_type: reference
description: "Découvrez comment utiliser la variante gagnante ou la variante personnalisée lors de la création de tests multivariés et de tests A/B."
---

# Optimisez les tests A/B avec la variante gagnante ou les variantes personnalisées {#optimize-ab-tests-with-winning-variant-or-personalized-variants}

> Découvrez comment utiliser la variante gagnante ou la variante personnalisée lors de la création de tests multivariés et de tests A/B.

Lors de la [création d'un test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) pour des Campaigns par e-mail, push, webhook, SMS et WhatsApp planifiées pour un envoi unique, vous pouvez sélectionner une optimisation. Il existe deux options d'optimisation : **Variante gagnante** et **Variante personnalisée**.

![Options d'optimisation présentées dans la section de test A/B lorsque vous choisissez votre audience cible. Trois options sont présentées : pas d'optimisation, variante gagnante et variante personnalisée. Variante personnalisée est sélectionnée.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Les deux options fonctionnent en envoyant un test initial à un pourcentage de votre segment cible. Après la fin du test, les utilisateurs restants de votre audience reçoivent soit la variante la plus efficace (variante gagnante), soit la variante avec laquelle ils ont le plus de chances d'interagir (variante personnalisée).

{% alert tip %}
Les optimisations sont situées dans l'étape **Target Audiences** de la création de la Campaign, sous **A/B Testing**.
{% endalert %}

## Variante gagnante {#winning-variant}

L'envoi de la variante gagnante est similaire à un test A/B standard. Les utilisateurs de ce groupe recevront la variante gagnante une fois le test initial terminé.

1. Sélectionnez **Winning Variant**, puis indiquez le pourcentage de l'audience de votre Campaign à affecter au groupe de la variante gagnante.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- |
| Determine Winning Variant | L'indicateur à optimiser. Choisissez entre *Unique Opens* ou *Clicks* pour l'e-mail, *Opens* pour les notifications push, ou *Primary Conversion Rate* pour tous les canaux. Sélectionner *Opens* ou *Clicks* pour déterminer la variante gagnante n'affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) que vous avez définis pour la Campaign. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs de ce groupe ne peuvent pas générer d'*Opens* ou de *Clicks*, ce qui signifie que la performance du groupe de contrôle sera forcément de `0`. Par conséquent, le groupe de contrôle ne peut pas remporter le test A/B. Vous pouvez toutefois utiliser un groupe de contrôle pour suivre d'autres indicateurs pour les utilisateurs qui ne reçoivent pas de message. |
| Winning Variant Send Time | La date et l'heure d'envoi de la variante gagnante. |
| If No Winning Variant Can Be Determined | Ce qui se passe si aucune variante ne l'emporte avec une marge statistiquement significative. Choisissez entre envoyer quand même la variante la plus performante, ou mettre fin au test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Winning Variant" }

## Variante personnalisée {#personalized-variant}

Utilisez les variantes personnalisées pour envoyer à chaque utilisateur de votre segment cible la variante avec laquelle il est le plus susceptible d'interagir.

Pour déterminer la meilleure variante pour chaque utilisateur, Braze envoie un test initial à une partie de votre audience cible afin d'identifier des corrélations entre les caractéristiques des utilisateurs et leurs préférences en matière de messages. En fonction des réponses des utilisateurs à chaque variante lors du test initial, ces caractéristiques servent à déterminer quelle variante sera envoyée à chacun des utilisateurs restants. Si aucune corrélation n'est trouvée et qu'aucune personnalisation ne peut être effectuée, la variante gagnante est automatiquement envoyée aux utilisateurs restants. Pour en savoir plus sur la façon dont les variantes personnalisées sont déterminées, consultez [Analyse des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#personalized-variant).

1. Sélectionnez **Personalized Variant**, puis indiquez le pourcentage de l'audience de votre Campaign à affecter au groupe de la variante personnalisée.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- |
| Determine Personalized Variant | L'indicateur à optimiser. Choisissez entre *Unique Opens* ou *Clicks* pour l'e-mail, *Opens* pour les notifications push, ou *Primary Conversion Rate* pour tous les canaux. Sélectionner *Opens* ou *Clicks* pour déterminer la variante gagnante n'affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) que vous avez définis pour la Campaign. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs de ce groupe ne peuvent pas générer d'*Opens* ou de *Clicks*, ce qui signifie que la performance du groupe de contrôle sera forcément de `0`. Par conséquent, le groupe de contrôle ne peut pas remporter le test A/B. Vous pouvez toutefois utiliser un groupe de contrôle pour suivre d'autres indicateurs pour les utilisateurs qui ne reçoivent pas de message. |
| Personalized Variant Send Time | La date et l'heure d'envoi de la variante personnalisée. |
| If No Personalized Variant Can Be Determined | Ce qui se passe si aucune variante personnalisée n'est trouvée. Choisissez entre envoyer la variante gagnante à la place, ou mettre fin au test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalized Variant" }

## Analyse {#analytics}

Pour en savoir plus sur les résultats de votre test A/B avec une optimisation, consultez [Analyse des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).