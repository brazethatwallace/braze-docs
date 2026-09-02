---
nav_title: Analyser
article_title: Operator Analyze
page_order: 100
description: "Posez des questions en langage naturel sur l'engagement de vos canaux, le chiffre d'affaires attribué et votre positionnement par rapport aux benchmarks du secteur. Vous obtenez des graphiques, des comparaisons et des informations exploitables en quelques secondes."
page_type: reference
hidden: true
---

# Operator Analyze {#operator-analyze}

> Operator Analyze répond à des questions de performance en langage naturel dans BrazeAI Operator<sup>TM</sup>. Les réponses incluent des graphiques, des comparaisons et de courtes informations exploitables. Vous n'avez pas besoin de créer un tableau de bord ni de générer un rapport complet au préalable.

{% alert important %}
Operator Analyze est actuellement en version bêta. Les fonctionnalités et les analyses prises en charge évoluent. Pour demander l'accès pour votre compte, contactez votre CSM.
{% endalert %}

## Pourquoi utiliser Operator Analyze ? {#why-use-operator-analyze}

La plupart des questions de performance nécessitent encore de changer d'outil, de créer des vues ou d'attendre qu'une autre personne s'en charge. Par exemple : « Comment s'est passée la semaine dernière ? », « Sommes-nous en phase avec le benchmark ? » ou « Quelle Campaign génère les meilleurs résultats ? »

Operator Analyze couvre les indicateurs d'engagement, le *chiffre d'affaires attribué* et les benchmarks du secteur. Ce sont les mêmes données que vous intégreriez autrement dans un rapport ou un tableau de bord. Posez votre question dans vos propres mots depuis le panneau Operator. Vous obtenez un graphique, une comparaison classée ou un tableau, accompagné d'une à cinq informations exploitables.

## Accéder à Operator Analyze {#access-operator-analyze}

Operator Analyze s'exécute dans le panneau de conversation Operator.

1. Sélectionnez **BrazeAI Operator<sup>TM</sup>** à côté de votre profil utilisateur depuis n'importe quelle page du tableau de bord de Braze.
2. Posez une question sur l'engagement d'un canal ou les comparaisons de benchmarks (voir [Exemples de questions](#example-questions)).
3. Operator renvoie la réponse et, le cas échéant, un graphique ou un tableau ainsi qu'une courte liste d'informations exploitables.

Pour en savoir plus sur le panneau de conversation Operator, consultez [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator).

## Exemples de questions {#example-questions}

Décrivez ce que vous souhaitez savoir. Aucune formulation fixe n'est requise. Sélectionnez un onglet pour voir des exemples de requêtes.

{% tabs %}
{% tab Comparaisons de benchmarks %}

* « Comment notre *taux d'ouverture* e-mail se compare-t-il aux benchmarks du secteur sur les 30 derniers jours ? »
* « Sommes-nous au-dessus ou en dessous du benchmark pour le *taux de clics* SMS ce trimestre ? »
* « Où sommes-nous en sous-performance par rapport au secteur sur l'ensemble de nos canaux ? »

{% endtab %}
{% tab Aperçus par canal %}

* « Quels canaux sont les plus performants pour nous depuis le début de l'exercice FY26 ? »
* « Détaillez l'engagement par canal sur les 90 derniers jours. »
* « Quel *chiffre d'affaires attribué* chaque canal marketing a-t-il généré le trimestre dernier ? »

{% endtab %}
{% tab Analyses détaillées de Campaigns et Canvas %}

* « Quelles sont nos 10 meilleures Campaigns e-mail par *taux de clics* ce trimestre fiscal ? »
* « Quels Canvas ont généré le plus de *clics* le mois dernier ? »
* « Quelles Campaigns ont généré le plus de *chiffre d'affaires attribué* au T1 de l'exercice FY26 ? »
* « Montrez nos Campaigns push les moins performantes sur les 30 derniers jours. »

{% endtab %}
{% tab Analyse de tendances %}

* « Quelle est la tendance mensuelle de l'engagement push pour l'exercice FY26 ? »
* « Comment le *taux de clics* e-mail a-t-il évolué d'un trimestre à l'autre au cours de la dernière année ? »
* « Comment notre *chiffre d'affaires attribué* a-t-il évolué au cours des 12 derniers mois ? »
* « Montrez-moi la tendance hebdomadaire d'engagement pour les In-App Messages sur les 90 derniers jours. »

{% endtab %}
{% tab Chiffre d'affaires et conversions %}

Posez des questions sur le *chiffre d'affaires attribué* et les *conversions* agrégés au niveau de la Campaign, du Canvas, du canal ou du programme.

* « Comparez le *chiffre d'affaires attribué* et les *conversions* du trimestre le plus récent par rapport au trimestre précédent. »
* « Quelles Campaigns ont généré le plus de *chiffre d'affaires attribué* au cours des 90 derniers jours ? »
* « Détaillez le *chiffre d'affaires attribué* par canal depuis le début de l'exercice FY26. »

{% endtab %}
{% tab Revues complètes %}

* « Donnez-moi une revue complète de notre programme d'engagement avec des recommandations. »
* « Où se trouvent nos plus grandes opportunités et nos principaux risques sur l'ensemble des canaux en ce moment ? »

{% endtab %}
{% endtabs %}

## Visualisations {#visualizations}

Operator ajoute un graphique lorsque les données le permettent. Les **graphiques en courbes** conviennent aux séries temporelles, les **graphiques en barres** aux comparaisons par catégorie, et les **tableaux** couvrent les autres cas. Les tableaux affichent les pourcentages à deux décimales et utilisent des virgules pour les grands nombres.

Lorsqu'une réponse inclut plusieurs indicateurs, Operator privilégie les taux d'engagement (*taux d'ouverture*, *taux de clics*, *taux d'ouverture push*) par rapport aux comptages bruts.

## Canaux et indicateurs pris en charge {#supported-channels-and-metrics}

Le *chiffre d'affaires attribué* et les *conversions* utilisent la même agrégation par Campaign, Canvas, canal et programme présentée dans [Exemples de questions](#example-questions) sous l'onglet **Chiffre d'affaires et conversions**.

| Canal | Indicateurs | Benchmarks du secteur |
| --- | --- | --- |
| E-mail | *Envois*, *Livraisons*, *Ouvertures uniques*, *Clics uniques*, *Désabonnements* | Oui |
| Push (iOS, Android, Web) | *Envois*, *Livraisons*, *Ouvertures* | Oui |
| SMS | *Envois*, *Livraisons*, *Clics sur les liens* | Oui |
| In-App Messages | *Impressions*, *Clics* | Oui |
| Content Cards | *Envois*, *Impressions*, *Clics* | Oui |
| WhatsApp | *Envois*, *Livraisons*, *Lectures*, *Clics* | Pas encore |
| RCS | *Envois*, *Livraisons*, *Lectures*, *Clics* (y compris les sous-types URL texte, bouton, action, action de réponse et bouton de réponse) | Pas encore |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canaux pris en charge, indicateurs et disponibilité des benchmarks" }

{% alert tip %}
Operator utilise des comptages uniques pour les taux (par exemple, *ouvertures uniques* divisées par les *livraisons* pour le *taux d'ouverture e-mail*). Si un chiffre diffère d'un tableau de bord, comparez la fenêtre d'attribution, la période et la définition. Operator indique ces trois éléments dans chaque réponse.
{% endalert %}

## Périodes et fenêtres d'attribution {#time-periods-and-attribution-windows}

### Exercice fiscal et année civile {#fiscal-year-vs-calendar-year}

Operator Analyze utilise par défaut l'**exercice fiscal Braze**, qui s'étend du 1er février au 31 janvier.

| Trimestre fiscal | Mois |
| --- | --- |
| FQ1 | Fév – Avr |
| FQ2 | Mai – Juil |
| FQ3 | Août – Oct |
| FQ4 | Nov – Jan |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Trimestres fiscaux Braze et mois correspondants" }

Pour les questions relatives à l'année civile, incluez « CY », « année civile » ou « année standard ». Les formulations ambiguës comme « l'année dernière » amènent Operator à vous demander de préciser le calendrier concerné.

Vous pouvez également utiliser des plages au format ISO telles que `Q4 2025` ou `2025-03-01 to 2025-05-31`.

### Fenêtres d'attribution {#attribution-windows}

Operator Analyze utilise par défaut une fenêtre de **7 jours**. Précisez une fenêtre dans votre question pour la modifier :

* **1 jour** pour des vérifications rapides de l'engagement
* **3 jours** pour des Campaigns à cycle court
* **7 jours** pour des aperçus généraux et des lectures de Campaigns (par défaut)
* **30 jours** pour des vues stratégiques ou à long terme
* **Toutes les fenêtres** pour une comparaison côte à côte 1J / 3J / 7J / 30J

Si les résultats diffèrent de plus de 50 % d'une fenêtre à l'autre, Operator affiche les quatre côte à côte.

## Fraîcheur des données {#data-freshness}

Les données sont actualisées quotidiennement. L'activité du jour en cours apparaît après la prochaine actualisation. Chaque réponse indique la date la plus récente du jeu de données. Si cette date semble obsolète, contactez votre CSM.

## Ce qui est hors périmètre {#whats-out-of-scope}

* **Analyses de performance au niveau produit.** Le *chiffre d'affaires attribué* et l'engagement sont agrégés au niveau de la Campaign, du Canvas, du canal ou du programme. Ils ne sont pas ventilés par produit ou par unité de gestion des stocks. Les questions au niveau produit ou unité de gestion des stocks ne sont pas prises en charge. Contactez votre CSM pour ces analyses.
* **Benchmarks du secteur pour WhatsApp et RCS.** Les indicateurs d'engagement pour ces deux canaux sont pris en charge. Les benchmarks ne sont pas encore disponibles.

Les questions hors périmètre reçoivent une réponse directe, une alternative suggérée lorsque c'est possible, ou une orientation vers votre CSM.

## Conseils pour de meilleurs résultats {#tips-for-better-results}

* **Période :** Préférez des plages explicites (« FY26 Q2 », « les 90 derniers jours ») aux formulations vagues comme « le trimestre dernier » lorsque vous avez besoin de précision.
* **Indicateurs :** Nommez le taux qui vous intéresse (*taux d'ouverture*, *taux de clics*, *taux de clic par ouverture*). Operator indique la formule utilisée.
* **Questions de suivi :** Approfondissez un résultat, modifiez la fenêtre ou changez de canal. Operator conserve le contexte tout au long du fil de conversation.
* **Terminologie des canaux :** WhatsApp et RCS utilisent le *taux de lecture* (et non le *taux d'ouverture*). Le SMS utilise le *taux de clics sur les liens*.
* **Requêtes combinées :** Benchmark et tendance dans une même requête sont pris en charge.

## Confidentialité et sécurité des données {#data-privacy-and-security}

Operator Analyze suit le même modèle de confidentialité et de sécurité que BrazeAI Operator<sup>TM</sup>. Pour en savoir plus, consultez [Confidentialité et sécurité des données]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Étapes suivantes {#next-steps}

* [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)
* [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)