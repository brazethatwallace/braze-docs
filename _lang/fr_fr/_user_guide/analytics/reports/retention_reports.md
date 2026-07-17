---
nav_title: Rapports de rétention
article_title: Rapports de rétention pour les campagnes et les Canvas
page_order: 9
tool: Reports
page_type: reference
description: "Cette page explique comment mesurer la rétention des utilisateurs ayant effectué un événement de rétention sélectionné dans une campagne ou un Canvas spécifique."
---

# Rapports de rétention {#retention-reports}

> La rétention des utilisateurs est l'un des indicateurs les plus importants pour tout marketeur. Garder les utilisateurs engagés et les inciter à revenir est un signe de bonne santé pour l'entreprise. Braze vous permet de mesurer la rétention des utilisateurs directement depuis la page **Analytics** de votre campagne ou Canvas.

{% alert important %}
Les rapports de rétention ne sont pas disponibles pour les campagnes déclenchées par API.
{% endalert %}

## Exécuter un rapport de rétention {#running-a-retention-report}

### Étape 1 : Sélectionner une plage de dates {#step-1-select-a-date-range}

![Date du rapport]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Commencez par accéder à n'importe quelle campagne ou Canvas dans votre tableau de bord de Braze, puis sélectionnez une plage de dates pour votre rapport. Le choix d'une plage de dates appropriée est essentiel en raison de son impact sur les rapports de rétention.

Ce rapport inclura tous les utilisateurs qui sont initialement entrés dans la campagne ou le Canvas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport.

Pour sélectionner une plage de dates, accédez à la page **Analytics** de la campagne ou du Canvas et sélectionnez différentes plages ou définissez une plage personnalisée pour votre rapport.

### Étape 2 : Sélectionner un événement de rétention {#step-2-select-a-retention-event}

{% tabs %}
{% tab Campaign %}

Ensuite, accédez à la section **Campaign Retention**. La rétention de Campaign vous montre le taux auquel tout utilisateur ayant reçu cette campagne spécifique a effectué un événement de rétention (que vous avez spécifié dans le rapport de rétention) au cours des 30 jours suivant la réception de la campagne.

{% endtab %}
{% tab Canvas %}

Ensuite, sélectionnez **Analyze Variants**. À partir de là, vous pouvez analyser vos variantes, consulter votre rapport d'entonnoir et afficher votre rapport de rétention. La rétention de Canvas vous montre le taux auquel tout utilisateur ayant reçu ce Canvas spécifique a effectué un événement de rétention (que vous avez spécifié dans le rapport de rétention) au cours des 30 jours suivant la réception du Canvas.

{% endtab %}
{% endtabs %}

![Sélectionner un événement de rétention]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Étape 3 : Générer le rapport {#step-3-generate-the-report}

Après avoir sélectionné un événement de rétention, sélectionnez **Run Report** pour lancer la requête.

![Exécuter le rapport]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Cette requête peut prendre quelques minutes, selon le volume de données à récupérer pour générer les résultats. Si cela prend trop de temps, vous verrez une notification vous demandant de réessayer de charger le rapport. Vous devrez peut-être attendre jusqu'à cinq minutes avant que le rapport ne se charge.

Une fois le rapport généré, il ne peut pas être relancé avec le même événement de rétention pendant 24 heures. Vous verrez toujours un horodatage indiquant la dernière génération du rapport, ainsi qu'une option pour le régénérer si plus d'un jour s'est écoulé. Vous pouvez toutefois modifier l'événement de rétention et relancer le rapport pour examiner l'impact de la campagne sur différents KPI.

Le rapport n'affichera que les jours où la campagne ou le Canvas envoyait des messages. Pour certaines campagnes et certains Canvas, cela peut signifier que le rapport n'affiche qu'un seul jour si l'envoi n'a eu lieu qu'une seule fois. S'il s'agit d'un envoi récurrent ou déclenché, vous pourrez voir plusieurs jours dans le tableau.

{% tabs %}
{% tab Campaign %}

![Rapport complet]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Rapport complet]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explication du rapport {#report-explanation}

Le rapport de rétention propose à la fois une formule de rétention glissante et une formule de rétention par plage. Pour afficher votre rapport de campagne ou Canvas avec l'un de ces types de rétention, sélectionnez **Rolling Retention** ou **Range Retention** pour votre **Type of Retention**.

### Rétention glissante {#rolling-retention}

La rétention glissante mesure combien d'utilisateurs reviennent et effectuent l'événement de rétention le jour indiqué ou après, parmi les jours listés en haut du rapport. Ainsi, si un utilisateur a démarré une session entre le jour trois et le jour sept, il sera comptabilisé comme retenu dans les colonnes « 3 jours », « 1 jour » et « 0 jour ». Tout utilisateur comptabilisé comme retenu après la barre des 30 jours suivant l'envoi de la campagne ou du Canvas sera comptabilisé dans la colonne « 30 jours » de cette ligne.

Un utilisateur qui effectue l'événement plusieurs fois au cours d'une fenêtre de 30 jours ou plus sera comptabilisé dans plusieurs périodes. Par exemple, un utilisateur qui effectue une session après un jour sera incrémenté dans les colonnes >0 et >1. S'il effectue ensuite l'événement après trois jours, il sera à nouveau incrémenté dans les colonnes précédentes (>0 et >1), ce qui peut entraîner un taux de rétention supérieur à 100 %.

#### Comment lire les rapports de rétention glissante {#how-to-read-rolling-retention-reports}

La façon de lire le graphique du rapport de rétention pour une colonne jour trois serait : Y % ou Y nombre d'utilisateurs (selon les unités choisies) ont effectué l'événement trois jours ou plus après avoir reçu la campagne le jour Z.

![Rapport glissant]({% image_buster /assets/img/campaign_retention3.png %})

Autre exemple, en se référant au tableau de l'image précédente, le 25 mars, un total de 38 utilisateurs ont effectué l'événement de rétention. La rétention au jour zéro était de 68,42 %, ce qui signifie que 68,42 % des utilisateurs ont effectué l'événement de rétention zéro jour ou plus (le jour zéro ou après) après avoir reçu la campagne. La rétention au jour sept était de 57,89 %, ce qui signifie que 57,89 % des utilisateurs ont effectué l'événement sept jours ou plus (le jour sept ou après) après avoir reçu la campagne.

Cette information peut être utile si vous souhaitez connaître le pourcentage d'utilisateurs qui ont et n'ont pas utilisé votre produit 30 jours ou plus après la première utilisation. Un pourcentage ou une valeur numérique dans la colonne jour 30 vous indique le pourcentage d'utilisateurs qui sont revenus le jour 30 ou après.

### Rétention par plage {#range-retention}

La rétention par plage mesure combien d'utilisateurs reviennent dans la plage de jours indiquée en haut du rapport. Ainsi, si un utilisateur a démarré une session entre les jours trois et sept, puis à nouveau le jour 13, il sera comptabilisé comme retenu dans les plages « Jour 3-7 » et « Jour 7-14 ».

#### Comment lire les rapports de rétention par plage {#how-to-read-range-retention-reports}

Les rapports par plage sont parmi les rapports les plus intuitifs à lire. Ils indiquent clairement, parmi tous les utilisateurs d'une cohorte, quel pourcentage de ces utilisateurs a effectué l'événement de rétention dans une plage de dates donnée. Par exemple, dans l'image suivante, en se référant à la cohorte Tous les utilisateurs, sur la plage de dates « Jour 0 (0-24h) », 35,71 % de la cohorte a effectué l'événement de rétention. Si un utilisateur effectue plusieurs événements de rétention dans plusieurs plages de dates, il sera comptabilisé comme retenu pour chaque plage.

![Rapport de rétention]({% image_buster /assets/img/range_retention.png %})

### Composants du rapport de rétention {#retention-report-components}

- **Colonne Utilisateurs** : La valeur affichée correspond au nombre d'utilisateurs uniques ayant effectué l'action de départ dans la période sélectionnée ; le nombre d'utilisateurs pour le jour en cours sera exclu car il est en cours de calcul.
- **Lignes Cohorte Z** : Affiche les jours pendant lesquels la campagne ou le Canvas envoyait des messages.
- **Colonnes Jour X** : Jours allant de 0 à 30 jours à différents intervalles.
- **Ligne Tous les utilisateurs** : Également appelée ligne de synthèse du rapport, elle résume les données de rétention pour l'ensemble de la période. Notez que si un utilisateur a reçu la campagne ou le Canvas dans plusieurs cohortes, ses résultats seront comptabilisés deux fois ici.
- **Pourcentages/Nombres** : Affiche le pourcentage ou le nombre d'utilisateurs ayant effectué l'événement X jours ou plus après avoir reçu la campagne ou le Canvas le jour Z. Ces pourcentages sont des moyennes pondérées. Les valeurs incomplètes seront signalées par un astérisque.
- **Plage de dates** : Définie sur la page **Details** de la campagne ou du Canvas, la plage de dates inclut tous les utilisateurs ayant reçu la campagne ou le Canvas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport.
- **Unités** : Vous pouvez ajuster les unités entre le pourcentage d'utilisateurs et le nombre d'utilisateurs depuis les contrôles du graphique ; certaines unités peuvent s'avérer plus pertinentes pour évaluer l'impact d'une campagne ou d'un Canvas.
- **Carte de couleurs** : Dans votre rapport de rétention, les pourcentages ou nombres d'utilisateurs plus élevés se voient attribuer des nuances de bleu plus foncées. Les pourcentages ou nombres d'utilisateurs plus faibles se voient attribuer des nuances de bleu plus claires. Cela permet de faciliter la visualisation de ces données.
- **Graphique du rapport de rétention** : Ce graphique résume les résultats pour toutes les cohortes sur la plage de dates sélectionnée.

### Performance par variante {#performance-by-variant}

L'affichage de votre rapport de rétention par variante vous permet de comparer la rétention glissante pour chaque variante ou variation de message sur la période sélectionnée, ainsi que le groupe de contrôle. Ce rapport peut être consulté en basculant **Show Performance For** sur **By Variant**.

Quelques cas d'usage pour l'affichage de la performance par variante :

- Certaines variantes ou expériences semblent avoir des résultats peu concluants ou sans signification statistique ? Examinez-les à nouveau pour voir si l'une ou l'autre a eu un impact à plus long terme.
- Découvrez à quoi ressemble la rétention si vous n'aviez pas envoyé de message en analysant les données de rétention du groupe de contrôle.

{% tabs %}
{% tab Campaign %}

![Affichage par variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Affichage par variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Composants du rapport de rétention par variante {#retention-report-by-variant-components}

- **Plage de dates** : Définie sur la page **Details** de la campagne ou du Canvas, la plage de dates inclut tous les utilisateurs ayant reçu la campagne ou le Canvas pendant cette fenêtre, et parmi ces utilisateurs, les données de ceux qui ont effectué leur événement de rétention pendant la plage de dates apparaîtront dans le rapport. Chaque jour, le taux de rétention, la variation en pourcentage par rapport au groupe de contrôle et la confiance sont mesurés.
- **Taux de rétention** : Affiche le taux de rétention par variante. Le taux de rétention est égal au nombre d'utilisateurs ayant effectué l'événement de rétention divisé par le nombre total d'utilisateurs ayant reçu la campagne ou le Canvas.
- **Variation en pourcentage par rapport au contrôle** : Quantifie la variation en pourcentage de chaque variante par rapport au groupe de contrôle.
- **Confiance** : {% multi_lang_include analytics/metrics.md metric='Confidence' %} Braze compare le taux de conversion de chaque variante avec celui du groupe de contrôle à l'aide d'une procédure statistique appelée test Z pour calculer un pourcentage de [confiance]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence).
- **Unités** : Vous pouvez ajuster les unités entre le pourcentage d'utilisateurs et le nombre d'utilisateurs depuis les contrôles du graphique ; certaines unités peuvent s'avérer plus pertinentes pour évaluer l'impact d'une campagne ou d'un Canvas.
- **Graphique des variantes** : Ce graphique résume les résultats par variante sur la plage de dates sélectionnée.

## Points à examiner dans vos rapports de rétention {#things-to-look-for-in-your-retention-reports}

Les rapports de rétention sont simples à générer, mais difficiles à interpréter et à exploiter. Les sujets et questions suivants peuvent vous aider à tirer le meilleur parti de vos rapports de rétention.

- Examinez les tendances par jour de la semaine pour les campagnes récurrentes (par exemple, les cohortes du lundi obtiennent-elles de meilleurs résultats que celles du samedi ?).
- À quel moment l'impact commence-t-il à diminuer ? Cela pourrait indiquer qu'une nouvelle campagne ou un nouveau Canvas ciblant les utilisateurs à ce moment précis est nécessaire pour donner un nouvel élan à la rétention.
- Observez-vous une fatigue liée à l'envoi de messages ?
- Une optimisation spécifique que vous avez apportée à une campagne ou un Canvas il y a X jours a-t-elle eu un impact positif ?