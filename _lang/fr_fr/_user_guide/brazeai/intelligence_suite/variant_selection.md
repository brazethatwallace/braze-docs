---
nav_title: Sélection de variante
article_title: Sélection de variante
page_order: 1.6
description: "Cet article présente la sélection de variante BrazeAI<sup>TM</sup>, une fonctionnalité qui permet à vos campagnes A/B d'optimiser automatiquement l'engagement."
search_rank: 10
toc_headers: h2
---

# Sélection de variante BrazeAI<sup>TM</sup> {#variant-selection}

> La sélection de variante BrazeAI<sup>TM</sup> est une fonctionnalité qui permet à vos tests A/B à envoi unique ou récurrents d'exécuter automatiquement une expérience et d'optimiser les résultats d'engagement.

{% alert note %}
La sélection de variante BrazeAI<sup>TM</sup> n'est actuellement disponible que pour les notifications push.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser la sélection de variante BrazeAI<sup>TM</sup>, vous devez disposer des éléments suivants dans votre campagne ou Canvas :

{% tabs %}
{% tab Campaign %}
- Ajoutez au moins deux variantes de message.
- Si vous n'utilisez pas l'envoi unique, définissez au moins un événement de conversion et configurez votre fenêtre de rééligibilité à 24 heures ou plus. Les fenêtres plus courtes ne sont pas prises en charge, car elles affecteraient l'intégrité de la variante de contrôle.
{% endtab %}

{% tab Canvas %}
- Incluez au moins deux variantes de message dans une étape Message.
- Si vous n'utilisez pas l'envoi unique, disposez d'au moins un événement de conversion.
{% endtab %}
{% endtabs %}

## Envoi unique {#single-send}

Après l'ajout de votre deuxième variante, la sélection de variante BrazeAI<sup>TM</sup> s'active automatiquement, définit les paramètres optimaux pour l'expérience (nous avons observé une amélioration d'environ 25 % en suivant les paramètres optimaux), exécute votre expérience, puis envoie la variante gagnante. Vous n'avez rien d'autre à faire.

Pour personnaliser votre expérience, nous proposons les options suivantes :

### Objectif d'optimisation {#optimization-goal}

Nous recommandons d'utiliser les ouvertures, sauf si vous disposez d'un événement de conversion solide avec un volume significatif de conversions, afin que l'algorithme ait les données nécessaires pour fournir les meilleurs résultats.
- Ouvertures
- Événements de conversion

### Durée de l'expérience {#experiment-duration}

Nous recommandons d'utiliser la valeur par défaut ; cependant, nous proposons deux autres options, y compris la possibilité d'utiliser votre propre durée personnalisée :
- 4 heures
- 24 heures
- 72 heures
- Personnalisée

### Groupe de contrôle et répartition des variantes {#control-group-and-variant-distributions}

Vous pouvez supprimer un groupe de contrôle ou modifier la répartition des variantes, mais nous recommandons d'utiliser les paramètres optimaux que nous avons définis.

![Options d'optimisation de variante pour l'envoi unique]({% image_buster /assets/img_archive/braze_ai_variant_selection_single_send_options.png %})

## Récurrent {#recurring}

Après l'ajout de votre deuxième variante, la sélection de variante BrazeAI<sup>TM</sup> s'active automatiquement et optimise en continu à l'aide d'un test statistique de type bandit manchot. Elle envoie davantage de messages aux variantes les plus performantes et moins à celles qui le sont moins.

Elle commence par une répartition uniforme pour entraîner et optimiser le modèle, puis deux fois par jour, elle ajuste la répartition en faveur des variantes performantes et au détriment des moins performantes, jusqu'à ce qu'elle ait rassemblé suffisamment de preuves pour être confiante (95 %+) d'avoir choisi la répartition optimale.

## Rapports {#reporting}

![Rapport d'amélioration]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Une fois le test terminé pour l'envoi unique, et après un court délai pour l'envoi récurrent, nous disposons de données fiables à rapporter. Nous affichons toute amélioration que la sélection de variante BrazeAI<sup>TM</sup> a pu obtenir dans le tableau de bord.

{% tabs %}
{% tab Envoi unique %}
Après l'envoi de la cohorte d'entraînement, Braze attend la durée définie dans le paramètre de durée et examine les données. En fonction de la répartition des variantes concurrentes, nous calculons une moyenne de ce à quoi les performances ressembleraient sans optimisation, puis nous calculons l'amélioration en fonction de la variante gagnante.

Par exemple (en supposant une répartition uniforme) :
- Variante 1 : 3,5 %
- Variante 2 : 3 %
- Variante 3 : 2,5 %
- Variante 4 : 2 %

Le taux d'ouverture sans optimisation est de 2,75 % (.035*.25 + .03*.25 + 0.025*.25 + 0.02*.25). La sélection de variante choisit la variante 1, soit 3,5 %, ce qui donne une amélioration de 27,3 %.
{% endtab %}

{% tab Récurrent %}
Braze analyse régulièrement les résultats lors des ajustements et affiche l'amélioration basée sur la moyenne de l'amélioration de chaque période.

Nous calculons l'amélioration de chaque période en fonction de l'ampleur de l'ajustement, de manière similaire à l'envoi unique.

Par exemple :
- Variante 1 : 3,5 %, 25 % de la cohorte
- Variante 2 : 3 %, 25 % de la cohorte
- Variante 3 : 2,5 %, 25 % de la cohorte
- Variante 4 : 2 %, 25 % de la cohorte

Le taux d'ouverture sans optimisation est de 2,75 % (.035*.25 + .03*.25 + 0.025*.25 + 0.02*.25). La sélection de variante pondère davantage les variantes les plus performantes.

Supposons qu'elle effectue la répartition suivante :
- Variante 1 : 65 %
- Variante 2 : 15 %
- Variante 3 : 10 %
- Variante 4 : 5 %

Cela équivaut à un taux d'ouverture choisi de 3,075 % (.035*.65 + .03*.15 + 0.025*.1 + 0.02*.05), soit une amélioration de 11,8 %. Nous effectuons ce calcul à chaque période, puis nous en faisons la moyenne sur l'ensemble de la période d'optimisation.
{% endtab %}
{% endtabs %}

## Questions fréquentes {#faq}

### Pourquoi la rééligibilité en moins de 24 heures n'est-elle pas disponible lorsqu'elle est combinée avec la sélection de variante pour les campagnes ou Canvas récurrents ? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-variant-selection-for-recurring-campaigns-or-canvases}

Nous n'autorisons pas les campagnes avec sélection de variante à avoir une rééligibilité dans une fenêtre trop courte, car nos tests montrent que cela affecte l'intégrité de la variante de contrôle et peut conduire à des répartitions indésirables.

### Pourquoi mes variantes affichent-elles des envois égaux pendant les premières étapes de ma campagne récurrente ? {#why-are-my-variants-showing-equal-sends-during-the-early-stages-of-my-recurring-campaign}

La sélection de variante ne détermine les allocations finales des variantes qu'après une période d'entraînement, pendant laquelle les envois sont répartis uniformément entre les variantes. Elle s'ajuste au fil du temps en détectant les tendances de performance. Si vous ne souhaitez pas envoyer de manière uniforme pendant les premières étapes de votre campagne, utilisez des variantes fixes pour un test A/B traditionnel.

### La sélection de variante récurrente cesse-t-elle d'optimiser sans choisir de gagnant clair ? {#does-recurring-variant-selection-stop-optimizing-without-picking-a-clear-winner}

Oui, elle cesse d'optimiser lorsqu'elle a une confiance de 95 % que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport à son taux actuel.

### Pourquoi ne puis-je pas activer la sélection de variante dans mon Canvas ou ma campagne ? {#why-cant-i-enable-variant-selection-in-my-canvas-or-campaign}

Pour l'envoi unique, vous ne pouvez pas activer la sélection de variante si votre Canvas ou votre campagne ne comporte qu'une seule variante.

Pour les envois récurrents, vous ne pouvez pas activer la sélection de variante si :
- Vous n'avez pas ajouté d'événements de conversion à votre campagne ou Canvas.
- Vous avez activé la rééligibilité avec une fenêtre inférieure à 24 heures.
- Votre Canvas ou votre campagne ne comporte qu'une seule variante.