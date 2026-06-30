---
nav_title: Analyse
article_title: Analyse des tests A/B
page_order: 10
page_type: reference
description: "Cet article explique comment consulter et interpréter les résultats d'une campagne multivariée ou d'un test A/B."
---

# Analyse des tests multivariés et A/B {#multivariate-and-ab-test-analytics}

> Cet article explique comment consulter les résultats d'un test multivarié ou A/B. Si vous n'avez pas encore configuré votre test, consultez [Créer des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) pour connaître les étapes à suivre.

Une fois votre campagne lancée, vous pouvez vérifier les performances de chaque variante en sélectionnant votre campagne dans la section **Campaigns** du tableau de bord.

## Analyse par option d'optimisation {#analytics-by-optimization-option}

Votre vue analytique varie selon que vous avez sélectionné ou non une [optimisation]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) lors de votre configuration initiale.

### Aucune optimisation {#no-optimization}

Si vous avez sélectionné **Aucune optimisation** lors de la configuration de votre campagne, votre vue analytique reste inchangée. La page **Analyse de campagne** affiche les performances de vos variantes par rapport à votre groupe de contrôle, si vous en avez inclus un.

![Section Performance de l'analyse de campagne pour une campagne e-mail avec plusieurs variantes. Le tableau répertorie divers indicateurs de performance pour chaque variante, tels que les destinataires, les rebonds, les clics et les conversions.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Pour plus de détails, consultez l'article [Analyse de campagne]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) correspondant à votre canal de communication.

### Sélection de variante BrazeAI<sup>TM</sup> (push uniquement) {#brazeai-variant-selection-push-only}

Si vous utilisez la sélection de variante BrazeAI<sup>TM</sup>, selon qu'il s'agit d'un envoi unique ou d'une campagne récurrente, une fois la fenêtre d'expérimentation (ou la première période pour les campagnes récurrentes) écoulée, vous verrez le gain éventuel sur la page d'accueil de la campagne. Vous trouverez également des détails supplémentaires similaires à ceux de la variante gagnante ci-dessous si vous lancez une campagne à envoi unique.

Pour plus de détails sur la façon dont nous rapportons le gain de la sélection de variante BrazeAI<sup>TM</sup>, consultez [Sélection de variante]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

![Analyse de campagne montrant le gain de la sélection de variante BrazeAI<sup>TM</sup>, y compris les indicateurs de comparaison après la fenêtre d'expérimentation.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

### Variante gagnante {#winning-variant}

Si vous avez sélectionné **Variante gagnante** comme optimisation lors de la configuration de votre campagne, vous avez accès à un onglet supplémentaire dans l'analyse de votre campagne appelé **Résultat du test A/B**. Une fois la variante gagnante envoyée aux utilisateurs restants de votre test, cet onglet affiche les résultats de cet envoi.

Le **Résultat du test A/B** est divisé en deux onglets : **Test initial** et **Variante gagnante**.

{% tabs local %}
{% tab Test initial %}

L'onglet **Test initial** affiche les indicateurs de chaque variante du test A/B initial envoyé à une partie de votre segment cible. Vous pouvez voir un résumé des performances de toutes les variantes et déterminer s'il y a eu une gagnante pendant le test.

Si une variante a surpassé toutes les autres avec un niveau de [confiance]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence) supérieur à 95 %, Braze lui attribue le label « Gagnante ».

Si aucune variante ne surpasse toutes les autres avec un niveau de confiance de 95 % et que vous avez choisi d'envoyer quand même la variante la plus performante, celle-ci sera tout de même envoyée et indiquée avec le label « Gagnante ».

![Résultats d'un test initial envoyé pour déterminer la variante gagnante, où aucune variante n'a obtenu de performances suffisamment supérieures aux autres pour atteindre le seuil de confiance de 95 % de significativité statistique.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Comment la variante gagnante est sélectionnée {#how-the-winning-variant-is-selected}

Braze compare toutes les variantes entre elles à l'aide du [test du khi-deux de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Ce test mesure si une variante surpasse statistiquement toutes les autres à un niveau de significativité de p < 0,05, soit ce que nous appelons une significativité de 95 %. Si c'est le cas, la variante gagnante est indiquée avec le label « Gagnante ».

Il s'agit d'un test distinct du score de confiance, qui décrit uniquement la performance d'une variante par rapport au groupe de contrôle avec une valeur numérique comprise entre 0 et 100 %.

Une variante peut obtenir de meilleurs résultats que le groupe de contrôle, mais le test du khi-deux vérifie si une variante est meilleure que toutes les autres. Des [tests de suivi](#recommended-follow-ups) peuvent fournir plus de détails.

{% endtab %}
{% tab Variante gagnante %}

L'onglet **Variante gagnante** affiche les résultats du second envoi, où chaque utilisateur restant a reçu la variante la plus performante du test initial. Votre **% d'audience** correspond au pourcentage du segment cible que vous avez réservé pour le groupe de la variante gagnante.

![Résultats de la variante gagnante envoyée au groupe de la variante gagnante.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Si vous souhaitez voir les performances de la variante gagnante tout au long de la campagne, y compris les envois du test A/B, consultez la page **Analyse de campagne**.

### Variante personnalisée {#personalized-variant}

Si vous avez sélectionné **Variante personnalisée** comme optimisation lors de la configuration de votre campagne, le **Résultat du test A/B** est divisé en deux onglets : **Test initial** et **Variante personnalisée**.

{% tabs local %}
{% tab Test initial %}

L'onglet **Test initial** affiche les indicateurs de chaque variante du test A/B initial envoyé à une partie de votre segment cible.

![Résultats d'un test initial envoyé pour déterminer la variante la plus performante pour chaque utilisateur. Un tableau affiche les performances de chaque variante selon divers indicateurs pour le canal cible.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Par défaut, le test recherche des associations entre les événements personnalisés de chaque utilisateur et ses préférences de variante de message. Cette analyse détecte si les événements personnalisés augmentent ou diminuent la probabilité de répondre à une variante de message particulière. Ces relations sont ensuite utilisées pour déterminer quel utilisateur reçoit quelle variante de message lors de l'envoi final.

Les relations entre les événements personnalisés et les préférences de message sont affichées dans le tableau de l'onglet **Envoi initial**.

![Tableaux de données d'événements personnalisés pour la variante 1 et la variante 2, montrant les scores d'impact des événements personnalisés qui indiquent comment chaque événement influence la préférence de variante.]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Si le test ne parvient pas à trouver de relation significative entre les événements personnalisés et les préférences de parcours, il se rabat sur une méthode d'analyse basée sur les sessions, et aucun tableau de données d'événements personnalisés n'est affiché.

{% details Méthode d'analyse de secours %}

**Méthode d'analyse basée sur les sessions**<br>
Si la méthode de secours est utilisée pour déterminer les variantes personnalisées, l'onglet **Test initial** affiche une répartition des variantes préférées des utilisateurs basée sur une combinaison de certaines caractéristiques.

Ces caractéristiques sont :

- **Récence :** date de leur dernière session
- **Fréquence :** fréquence de leurs sessions
- **Ancienneté :** depuis combien de temps ils sont utilisateurs

Par exemple, le test peut révéler que la plupart des utilisateurs préfèrent la variante A, mais que les utilisateurs ayant eu une session il y a environ 3 à 12 jours, avec un intervalle de 1 à 12 jours entre les sessions, et créés au cours des 67 à 577 derniers jours, tendent à préférer la variante B. Par conséquent, les utilisateurs de cette sous-population ont reçu la variante B lors du second envoi, tandis que les autres ont reçu la variante A.

![Le tableau des caractéristiques utilisateur, qui montre quels utilisateurs sont susceptibles de préférer la variante A et la variante B en fonction des trois compartiments dans lesquels ils se trouvent pour la récence, la fréquence et l'ancienneté.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Comment les variantes personnalisées sont sélectionnées**<br>
Avec cette méthode, le message recommandé pour un utilisateur individuel est la somme des effets de sa récence, sa fréquence et son ancienneté spécifiques. La récence, la fréquence et l'ancienneté sont réparties en compartiments, comme illustré dans le tableau **Caractéristiques utilisateur**. La plage temporelle de chaque compartiment est déterminée par les données des utilisateurs de chaque campagne et varie d'une campagne à l'autre.

Chaque compartiment peut avoir une contribution ou une « impulsion » différente vers chaque variante de message. La force de l'impulsion pour chaque compartiment est déterminée à partir des réponses des utilisateurs lors de l'envoi initial en utilisant la [régression logistique](https://en.wikipedia.org/wiki/Logistic_regression). Ce tableau ne fait que résumer les résultats en indiquant avec quelle variante les utilisateurs de chaque compartiment ont eu tendance à interagir. La variante personnalisée réelle d'un utilisateur individuel dépend de la somme des effets des trois compartiments dans lesquels il se trouve, un pour chaque caractéristique.

{% enddetails %}

{% endtab %}
{% tab Variante personnalisée %}

L'onglet **Variante personnalisée** affiche les résultats du second envoi, où chaque utilisateur restant a reçu la variante avec laquelle il était le plus susceptible d'interagir.

Les trois cartes de cette page affichent votre gain projeté, les résultats globaux et les résultats projetés si vous aviez envoyé uniquement la variante gagnante. Même en l'absence de gain, ce qui peut parfois arriver, le résultat est identique à l'envoi de la seule variante gagnante (un test A/B traditionnel).

- **Gain projeté :** l'amélioration de l'indicateur d'optimisation sélectionné pour cet envoi grâce à l'utilisation de variantes personnalisées au lieu d'un test A/B standard (si les utilisateurs restants n'avaient reçu que la variante gagnante).
- **Résultats globaux :** les résultats du second envoi basés sur l'indicateur d'optimisation choisi (*Ouvertures uniques*, *Clics uniques* ou *Événement de conversion principal*).
- **Résultats projetés :** les résultats projetés du second envoi basés sur l'indicateur d'optimisation choisi si vous aviez envoyé uniquement la variante gagnante.

![Onglet Variante personnalisée pour une campagne optimisée pour les ouvertures uniques. Les cartes affichent le gain projeté, les ouvertures uniques globales (avec variante personnalisée) et les ouvertures uniques projetées (avec variante gagnante).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

Le tableau de cette page affiche les indicateurs de chaque variante de l'envoi de la variante personnalisée. Votre **% d'audience** correspond au pourcentage du segment cible que vous avez réservé pour le groupe de la variante personnalisée.

![Tableau des résultats de l'envoi de la variante personnalisée montrant les indicateurs de performance pour la variante A, la variante B et toutes les variantes, y compris le pourcentage d'audience, les envois, les distributions, les ouvertures, les clics et les conversions.]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Comprendre la confiance {#understanding-confidence}

La confiance est la mesure statistique de notre certitude qu'une différence observée dans les données, comme les taux de conversion, est réelle et non simplement due au hasard.

{% alert note %}
Vous ne voyez pas la confiance dans vos résultats ? La confiance n'apparaît que si vous avez un groupe de contrôle.
{% endalert %}

Un aspect important de vos résultats est le niveau de confiance. Par exemple, que se passe-t-il si le groupe de contrôle avait un taux de conversion de 20 % et la variante A un taux de conversion de 25 % ? Cela semble indiquer que l'envoi de la variante A est plus efficace que l'absence de message. Un niveau de confiance de 95 % signifie que la différence entre les deux taux de conversion est probablement due à une différence réelle dans les réponses des utilisateurs, et qu'il n'y a que 5 % de probabilité que cette différence soit due au hasard.

Braze compare le taux de conversion de chaque variante à celui du groupe de contrôle à l'aide d'une procédure statistique appelée [test Z](https://en.wikipedia.org/wiki/Z-test). Un résultat avec un niveau de confiance de 95 % ou plus, comme dans l'exemple précédent, indique que la différence est statistiquement significative. Cela s'applique partout où vous voyez un indicateur de confiance dans le tableau de bord de Braze décrivant la différence entre deux messages ou populations d'utilisateurs.

En général, un niveau de confiance d'au moins 95 % est nécessaire pour démontrer que vos résultats reflètent les préférences réelles des utilisateurs et ne sont pas dus au hasard. Dans les tests scientifiques rigoureux, un niveau de confiance de 95 % (ou, autrement dit, une valeur « p » inférieure à 0,05) est le seuil couramment utilisé pour déterminer la significativité statistique. Si vous n'atteignez pas systématiquement un niveau de confiance de 95 %, essayez d'augmenter la taille de votre échantillon ou de réduire le nombre de variantes.

La confiance reflète la probabilité qu'une différence observée entre les taux de conversion de la variante et du groupe de contrôle soit réelle plutôt que due au hasard. Elle dépend de la taille de l'échantillon et de l'ampleur de la différence entre les taux de conversion. Que les taux de conversion globaux soient élevés ou faibles importe généralement moins que la différence observée et la taille de l'échantillon pour déterminer la force de la mesure de confiance. Il est possible qu'une variante ait un taux de conversion très différent d'une autre sans pour autant atteindre un niveau de confiance de 95 % ou plus. Il est également possible que deux ensembles de variantes aient des taux de conversion ou de gain similaires, mais des niveaux de confiance différents.

À mesure que de nouvelles données arrivent, la confiance peut diminuer si les taux de conversion de la variante et du groupe de contrôle se rapprochent — la différence que vous mesurez se réduit, ce qui peut l'emporter sur l'effet d'un échantillon plus grand.

### Résultats statistiquement non significatifs {#statistically-insignificant-results}

Un test qui n'atteint pas un niveau de confiance de 95 % peut tout de même fournir des informations précieuses. Voici quelques enseignements que vous pouvez tirer d'un test aux résultats statistiquement non significatifs :

- Il est possible que toutes vos variantes aient eu à peu près le même effet. Le savoir vous fait gagner le temps que vous auriez consacré à effectuer ces changements. Parfois, vous constaterez que les techniques marketing conventionnelles, comme répéter votre appel à l'action, ne fonctionnent pas nécessairement pour votre audience.
- Bien que vos résultats puissent être dus au hasard, ils peuvent orienter l'hypothèse de votre prochain test. Si plusieurs variantes semblent avoir des résultats à peu près similaires, relancez certaines d'entre elles avec de nouvelles variantes pour voir si vous pouvez trouver une alternative plus efficace. Si une variante obtient de meilleurs résultats, mais pas de manière significative, vous pouvez effectuer un autre test dans lequel la différence de cette variante est plus marquée.
- Continuez à tester ! Un test aux résultats non significatifs devrait susciter certaines questions. Y avait-il vraiment aucune différence entre vos variantes ? Auriez-vous dû structurer votre test différemment ? Vous pouvez répondre à ces questions en effectuant des tests de suivi.
- Bien que les tests soient utiles pour découvrir quel type de message génère le plus de réponses de votre audience, il est également important de comprendre quelles modifications n'ont qu'un effet négligeable. Cela vous permet soit de continuer à tester pour trouver une alternative plus efficace, soit de gagner le temps qui aurait été consacré à choisir entre deux messages alternatifs.

Que votre test ait un gagnant clair ou non, il peut être utile d'effectuer un [test de suivi](#recommended-follow-ups) pour confirmer vos résultats ou appliquer vos conclusions à un scénario légèrement différent.

## Écarts entre le groupe de contrôle et la variante {#discrepancies-between-the-control-group-and-variant}

Pour les campagnes de messages in-app avec des répartitions A/B ou multivariées, les pourcentages que vous configurez sont des objectifs d'affectation. Les impressions rapportées correspondent rarement exactement à ces pourcentages, car seuls les utilisateurs qui effectuent l'action de déclenchement enregistrent des impressions, et les utilisateurs du groupe de contrôle qui déclenchent l'action enregistrent une impression même s'ils ne voient jamais de message.

Par exemple, supposons qu'une campagne ait une audience cible de 200 utilisateurs au lancement, avec 100 utilisateurs dans le groupe de contrôle et 100 utilisateurs dans la variante.

Les 100 utilisateurs de la variante reçoivent le payload du message in-app, et 50 d'entre eux effectuent l'action de déclenchement et voient le message in-app. Les 100 utilisateurs du groupe de contrôle ne sont suivis que s'ils effectuent l'action de déclenchement de la campagne, et 75 d'entre eux effectuent l'action de déclenchement et enregistrent une impression sans voir le message in-app.

Malgré la répartition initiale 50/50, les impressions uniques enregistrées ne sont pas équilibrées. Le groupe de la variante a 50 impressions, tandis que le groupe de contrôle en a 75.

### Délais des messages in-app {#in-app-message-delays}

Pour les campagnes de messages in-app déclenchés qui incluent des affichages différés, les impressions du groupe de contrôle seront enregistrées au moment où l'utilisateur final aurait initialement reçu le message in-app. Par exemple, si une campagne est configurée pour retarder l'affichage d'une heure, les impressions du groupe de contrôle ne seront pas enregistrées avant que le délai d'une heure ne soit écoulé. Cela permet un suivi précis des impressions en lien avec le moment prévu de la distribution du message.

## Tests de suivi recommandés {#recommended-follow-ups}

Un test multivarié ou A/B peut (et devrait !) inspirer des idées pour de futurs tests, ainsi que vous guider vers des changements dans votre stratégie de communication. Voici quelques actions de suivi possibles :

### Modifier votre stratégie de communication en fonction des résultats du test {#change-your-messaging-strategy-based-on-test-results}

Les résultats de votre test multivarié peuvent vous amener à modifier la façon dont vous formulez ou formatez vos messages.

### Mieux comprendre vos utilisateurs {#change-the-way-you-understand-your-users}

Chaque test éclaire les comportements de vos utilisateurs, la façon dont ils réagissent aux différents canaux de communication, ainsi que les différences (et similitudes) entre vos segments.

### Améliorer la structure de vos futurs tests {#improve-the-way-you-structure-future-tests}

Votre échantillon était-il trop petit ? Les différences entre vos variantes étaient-elles trop subtiles ? Chaque test est une occasion d'apprendre à améliorer les tests futurs. Si votre confiance est faible, votre échantillon est trop petit et devrait être augmenté pour les prochains tests. Si vous ne constatez aucune différence nette entre les performances de vos variantes, il est possible que les différences étaient trop subtiles pour avoir un effet perceptible sur les réponses des utilisateurs.

### Effectuer un test de suivi avec un échantillon plus grand {#run-a-follow-up-test-with-a-larger-sample-size}

Des échantillons plus grands augmentent les chances de détecter de petites différences entre les variantes.

### Effectuer un test de suivi sur un canal de communication différent {#run-a-follow-up-test-using-a-different-messaging-channel}

Si vous constatez qu'une stratégie particulière est très efficace sur un canal, vous pouvez tester cette stratégie sur d'autres canaux. Si un type de message est efficace sur un canal mais pas sur un autre, vous pouvez en conclure que certains canaux sont plus propices à certains types de messages. Ou peut-être y a-t-il une différence entre les utilisateurs qui sont plus susceptibles d'activer les notifications push et ceux qui sont plus susceptibles de prêter attention aux messages in-app. En fin de compte, ce type de test vous aide à comprendre comment votre audience interagit avec vos différents canaux de communication.

### Effectuer un test de suivi sur un segment d'utilisateurs différent {#run-a-follow-up-test-on-a-different-segment-of-users}

Pour ce faire, créez un autre test avec le même canal de communication et les mêmes variantes, mais choisissez un segment d'utilisateurs différent. Par exemple, si un type de message s'est avéré extrêmement efficace pour les utilisateurs engagés, il peut être utile d'étudier son effet sur les utilisateurs inactifs. Il est possible que les utilisateurs inactifs réagissent de manière similaire, ou qu'ils préfèrent une autre variante. Ce test vous aidera à en apprendre davantage sur vos différents segments et sur la façon dont ils réagissent aux différents types de messages. Pourquoi faire des suppositions sur vos segments quand vous pouvez baser votre stratégie sur des données ?

### Effectuer un test de suivi basé sur les enseignements d'un test précédent {#run-a-follow-up-test-based-on-insights-from-a-previous-test}

Utilisez les informations recueillies lors de tests passés pour guider vos futurs tests. Un test précédent suggère-t-il qu'une technique de communication est plus efficace ? N'êtes-vous pas certain de l'aspect spécifique d'une variante qui l'a rendue meilleure ? Effectuer des tests de suivi basés sur ces questions vous aidera à générer des conclusions pertinentes sur vos utilisateurs.

### Comparer l'impact à long terme de différentes variantes {#compare-the-long-term-impact-of-different-variants}

Si vous effectuez des tests A/B sur des messages de réengagement, n'oubliez pas de comparer l'impact à long terme des différentes variantes à l'aide des [rapports de rétention]({{site.baseurl}}/user_guide/analytics/reports/retention_reports). Vous pouvez utiliser les rapports de rétention pour analyser comment chaque variante a influencé un comportement utilisateur de votre choix au bout de quelques jours, semaines ou un mois après la réception du message, et vérifier s'il y a un gain.