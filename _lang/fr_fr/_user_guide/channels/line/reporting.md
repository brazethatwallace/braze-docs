---
nav_title: Rapports
article_title: Rapports LINE
page_order: 21
description: "Cet article de référence présente les indicateurs LINE utilisés dans Braze, ainsi que la manière de les consulter dans vos campagnes LINE."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# Rapports LINE {#line-reporting}

> Après le lancement de votre campagne ou Canvas, vous pouvez consulter les indicateurs clés sur la page de détails de la campagne ou dans l'analyse du Canvas. Cet article explique où trouver ces indicateurs et ce qu'ils représentent.

{% alert tip %}
Vous cherchez les définitions des termes et indicateurs de votre rapport ? Consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).
{% endalert %}

## Analyse de la campagne {#campaign-analytics}

Dans l'onglet **Campaign Analytics**, vous pouvez consulter vos rapports sous forme de panneaux. Vous pourriez en voir plus ou moins que ceux répertoriés dans les sections ci-dessous, mais chacun a son utilité.

{% alert note %}
Les statistiques relatives aux ouvertures et aux clics pour LINE ne sont calculées que si plus de 20 utilisateurs effectuent l'événement un jour donné.
{% endalert %}

### Détails de la campagne {#campaign-details}

Le panneau **Campaign Details** présente un aperçu général des performances de vos messages LINE.

Consultez ce panneau pour voir les indicateurs globaux tels que le nombre de messages envoyés au nombre de destinataires, le taux de conversion principal et le chiffre d'affaires total généré par ce message. Vous pouvez également vérifier les paramètres de réception, d'audience et de conversion depuis cette page.

#### Groupes de contrôle {#control-groups}

Pour mesurer l'impact d'un message LINE individuel, vous pouvez ajouter un [groupe de contrôle]({{site.baseurl}}/user_guide/messaging/ab_testing) à un test A/B. Le panneau de niveau supérieur **Campaign Details** n'inclut pas les indicateurs de la variante du groupe de contrôle.

### Performances LINE {#line-performance}

Le panneau **LINE Performance** décrit les performances de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous effectuez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Prévisualisation** pour afficher votre message pour chaque variante ou canal.

![Le panneau « LINE Performance » affichant les indicateurs pour deux variantes.]({% image_buster /assets/img/line/line_performance.png %})

Si vous souhaitez simplifier votre vue, sélectionnez **+ Add/Remove Columns** et décochez les indicateurs souhaités. Par défaut, tous les indicateurs sont affichés.

#### Indicateurs LINE {#line-metrics}

Voici quelques indicateurs LINE clés que vous pouvez retrouver dans vos analyses. Pour consulter les définitions de tous les indicateurs LINE utilisés dans Braze, reportez-vous au [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

| Terme | Définition |
| --- | --- |
| Envois | Le nombre total d'envois communiqués avec succès entre Braze et LINE. Cela ne signifie pas que le message a été reçu par l'utilisateur. |
| Ouvertures uniques | Le nombre total de messages LINE envoyés qui ont été ouverts par les utilisateurs après qu'un seuil minimum de 20 messages par jour a été atteint. |
| Ouvertures totales | Le nombre total de fois où les messages LINE envoyés ont été ouverts par les utilisateurs après qu'un seuil minimum de 20 messages par jour a été atteint. |
| Clics uniques | Le nombre total de messages LINE envoyés qui ont été cliqués par les utilisateurs après qu'un seuil minimum de 20 messages par jour a été atteint. |
| Clics totaux | Le nombre total de fois où les messages LINE envoyés ont été cliqués par les utilisateurs après qu'un seuil minimum de 20 messages par jour a été atteint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs LINE" }

### Performances historiques {#historical-performance}

Le panneau **Historical Performance** vous permet de visualiser les indicateurs du panneau **Message Performance** sous forme de graphique au fil du temps. Utilisez les filtres en haut du panneau pour modifier les statistiques et les canaux affichés dans le graphique. La plage temporelle de ce graphique correspond toujours à la plage temporelle spécifiée en haut de la page.

Pour obtenir une ventilation jour par jour, sélectionnez le menu hamburger <i class="fas fa-bars"></i> et sélectionnez **Download CSV** pour recevoir un export CSV du rapport.

### Détails des événements de conversion {#conversion-event-details}

Le panneau **Conversion Event Details** vous montre les performances de vos événements de conversion pour votre campagne. Pour en savoir plus, consultez [Événements de conversion]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation).

### Corrélation de conversion {#conversion-correlation}

Le panneau **Conversion Correlation** vous donne un aperçu des attributs et comportements utilisateurs qui favorisent ou nuisent aux résultats que vous avez définis pour vos campagnes. Pour en savoir plus, consultez [Corrélation de conversion]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation).