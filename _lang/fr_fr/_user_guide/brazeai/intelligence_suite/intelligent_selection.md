---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1.0
description: "Cet article décrit la sélection intelligente, une fonctionnalité qui analyse deux fois par jour les performances d'une campagne ou d'un Canvas récurrent et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message."
search_rank: 10
toc_headers: h2
---

# Sélection intelligente {#intelligent-selection}

> La sélection intelligente est une fonctionnalité qui analyse deux fois par jour les performances d'une campagne ou d'un Canvas récurrent et ajuste automatiquement le pourcentage d'utilisateurs qui reçoivent chaque variante de message.

## Conditions préalables {#prerequisites}

{% tabs %}
{% tab Campaign %}
Avant d'ajouter la sélection intelligente à votre campagne, assurez-vous d'avoir correctement configuré les éléments suivants :

- Votre campagne est envoyée selon une planification récurrente. Les campagnes à envoi unique ne sont pas prises en charge.
- Vous avez ajouté au moins deux variantes de message.
- Vous avez défini un événement de conversion pour mesurer les performances des variantes.
- La fenêtre de rééligibilité est fixée à 24 heures ou plus. Les fenêtres plus courtes ne sont pas prises en charge, car elles affecteraient l'intégrité de la variante de contrôle. Pour en savoir plus, consultez [cette FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
Pour utiliser la sélection intelligente dans un Canvas, confirmez les points suivants :
- Votre Canvas comprend au moins deux variantes de message dans une étape de message.
- Vous avez ajouté au moins un événement de conversion.
{% endtab %}
{% endtabs %}

## À propos de la sélection intelligente {#about-intelligent-selection}

Une variante qui semble être plus performante que les autres sera envoyée à un plus grand nombre d'utilisateurs, tandis que les variantes moins performantes cibleront moins d'utilisateurs. Chaque ajustement est effectué à l'aide d'un [algorithme statistique](https://en.wikipedia.org/wiki/Multi-armed_bandit) qui garantit que Braze s'adapte à de réelles différences de performances et pas seulement au hasard.

![Section de test A/B d'une campagne où la sélection intelligente est activée.]({% image_buster /assets/img/intelligent_selection1.png %})

La sélection intelligente va :
- Examiner à plusieurs reprises les données de performance et déplacer progressivement le trafic de la campagne vers les variantes gagnantes.
- Vérifier que davantage d'utilisateurs reçoivent votre variante la plus performante sans sacrifier la confiance statistique.
- Exclure les variantes moins performantes et identifier les variantes très performantes plus rapidement qu'un [test A/B traditionnel]({{site.baseurl}}/user_guide/messaging/ab_testing).
- Tester plus fréquemment et avec une plus grande confiance que vos utilisateurs verront votre meilleur message.

La sélection intelligente fonctionne mieux pour les campagnes envoyées plusieurs fois. Elle a besoin de données de performance précoces pour commencer à optimiser, de sorte que les campagnes à envoi unique n'en bénéficieront pas. Pour ces campagnes, nous vous recommandons plutôt d'utiliser un [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) traditionnel.


Vous pouvez ajouter la sélection intelligente à vos campagnes et à vos Canvas.

{% tabs %}
{% tab Campaign %}
La sélection intelligente peut être ajoutée à n'importe quelle campagne multi-envoi dans l'étape **Audiences cibles** du compositeur de campagne de Braze. Les campagnes qui n'envoient qu'une seule fois ne peuvent pas bénéficier de cette fonctionnalité.

{% alert note %}
La sélection intelligente ne peut pas être utilisée dans les campagnes dont la période de rééligibilité est inférieure à 24 heures, car elle affecterait l'intégrité de la variante de contrôle. Pour en savoir plus, consultez la [FAQ sur l'intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Ajoutez au moins un événement de conversion et deux variantes à votre Canvas. Ensuite, sélectionnez l'un des pourcentages de variante dans l'étape de création.

![Un Canvas avec deux variantes, chacune définie à 50 % de distribution de variante, permettant l'activation de la sélection intelligente.]({% image_buster /assets/img/intelligent_selection.png %})

Vous pouvez ainsi modifier la répartition des variantes et activer la sélection intelligente.

![Option de sélection intelligente activée pour un Canvas.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La sélection intelligente ne sera pas disponible si vous n'avez pas encore ajouté d'événements de conversion à votre Canvas ou si votre Canvas est composé d'une seule variante.

{% alert note %}
Les Canvas peuvent utiliser la sélection intelligente avec la rééligibilité activée, mais Braze ne peut pas garantir qu'un utilisateur recevra la même variante lors d'une nouvelle entrée, car l'allocation optimale évolue au fil du temps. Les campagnes nécessitent une fenêtre de rééligibilité de 24 heures ou plus lorsque la sélection intelligente est activée. Pour en savoir plus, consultez [Pourquoi la rééligibilité dans moins de 24 heures n'est-elle pas disponible lorsqu'elle est associée à la sélection intelligente ?](#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}
{% endtabs %}

## Durée d'exécution {#run-time}

Pour les campagnes et les Canvas, la sélection intelligente s'exécutera jusqu'à ce qu'elle rassemble suffisamment de preuves des taux de conversion « réels » des variantes. Le niveau « suffisant » est déterminé par un indicateur spécial appelé « regret ». Vous pouvez l'assimiler à la confiance, dans la mesure où la sélection intelligente se désactive lorsqu'il y a suffisamment de données pour savoir quelle variante est la meilleure.

Dans la plupart des cas, la sélection intelligente choisira l'une des variantes comme variante gagnante. Cette variante sera envoyée à 100 % de l'audience pour les envois futurs.

{% alert note %}
Il est possible que la sélection intelligente cesse d'optimiser sans avoir choisi un seul gagnant clair. La sélection intelligente cesse d'optimiser lorsqu'elle est sûre à 95 % que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport au taux actuel.
{% endalert %}

## Distribution des variantes avec la sélection intelligente {#intelligent-selection-variant-distribution}

La sélection intelligente fonde la distribution des variantes sur l'état actuel des conversions de la campagne. Elle détermine uniquement les distributions finales après la période de formation.

Cela signifie qu'au début de la campagne, les sélections intelligentes à 99 % et à 1 % peuvent recevoir environ le même nombre d'envois, mais que les pourcentages finaux pour l'attribution des variantes peuvent être fixés à 99 %–1 %.

Si vous ne souhaitez pas que la sélection intelligente envoie à parts égales au début de la campagne, nous vous recommandons d'utiliser un test A/B traditionnel avec des variantes fixes.

## Questions fréquentes {#faq}

### Pourquoi la rééligibilité dans moins de 24 heures n'est-elle pas disponible lorsqu'elle est associée à la sélection intelligente ? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection}

Nous ne permettons pas aux campagnes avec sélection intelligente d'avoir une rééligibilité dans une fenêtre trop courte, car cela affecterait l'intégrité de la variante de contrôle. En créant un intervalle de 24 heures, nous contribuons à garantir que l'algorithme disposera d'un ensemble de données statistiquement valide.

Normalement, les campagnes avec rééligibilité amèneront les utilisateurs à recevoir de nouveau la même variante qu'auparavant. Avec la sélection intelligente, Braze ne peut pas garantir qu'un utilisateur recevra la même variante de campagne, car la distribution des variantes aurait changé en raison de l'aspect d'allocation optimale de cette fonctionnalité. Si l'utilisateur était autorisé à entrer de nouveau avant que la sélection intelligente ne réexamine les performances de la variante, les données pourraient être biaisées en raison des utilisateurs réentrés.

Par exemple, si une campagne utilise ces variantes :

- Variante A : 20 %
- Variante B : 20 %
- Contrôle : 60 %

La distribution des variantes pourrait alors être la suivante au deuxième tour :

- Variante A : 15 %
- Variante B : 25 %
- Contrôle : 60 %

### Pourquoi mes variantes de sélection intelligente affichent-elles des envois égaux au début de ma campagne ? {#why-are-my-intelligent-selection-variants-showing-equal-sends-during-the-early-stages-of-my-campaign}

La sélection intelligente alloue les variantes à envoyer en fonction de l'état actuel des conversions de la campagne. Elle détermine uniquement les attributions de variantes finales après une période de formation durant laquelle les envois sont répartis de manière uniforme entre les variantes. Si vous ne souhaitez pas que la sélection intelligente envoie de manière uniforme au début de votre campagne, utilisez des variantes fixes pour un test A/B traditionnel.

### La sélection intelligente cessera-t-elle d'optimiser sans choisir un gagnant clair ? {#will-intelligent-selection-stop-optimizing-without-picking-a-clear-winner}

La sélection intelligente cessera d'optimiser lorsqu'elle sera sûre à 95 % que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport à son taux actuel.

### Pourquoi ne puis-je pas activer la sélection intelligente dans mon Canvas ou ma campagne (option grisée) ? {#why-cant-i-enable-intelligent-selection-in-my-canvas-or-campaign-grayed-out}

La sélection intelligente ne sera pas disponible si :

- Vous n'avez pas ajouté d'événements de conversion à votre campagne ou Canvas
- Vous créez une campagne à envoi unique
- Votre campagne a la rééligibilité activée avec une fenêtre de moins de 24 heures
- Votre Canvas est composé d'une seule variante sans variantes supplémentaires ni groupes de contrôle ajoutés
- Votre Canvas est composé d'un seul groupe de contrôle, sans variantes ajoutées