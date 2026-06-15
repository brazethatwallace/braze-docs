---
nav_title: Tableau de bord des benchmarks sectoriels
article_title: Tableau de bord des benchmarks sectoriels
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "Cet article fournit un aperçu du tableau de bord des benchmarks sectoriels."
hidden: true
noidex: true
---

# Tableau de bord des benchmarks sectoriels {#industry-benchmarks-dashboard}

> Le tableau de bord **Industry Benchmarks** compare les performances d'engagement de votre espace de travail à des benchmarks agrégés et respectueux de la vie privée, issus d'entreprises comparables dans chaque secteur d'activité.

Utilisez le tableau de bord **Industry Benchmarks** pour comparer vos performances e-mail, push, Content Cards et SMS à celles de vos pairs du secteur, et pour identifier les canaux et régions où des opportunités d'optimisation existent.

Pour afficher le tableau de bord **Industry Benchmarks**, accédez à **Analytics** > **Dashboard Builder**, puis sélectionnez **Industry Benchmarks**. Si le tableau de bord ne contient aucune donnée, sélectionnez **Run Dashboard** pour générer les résultats les plus récents. Utilisez les filtres en haut du tableau de bord pour affiner les résultats par secteur d'activité ou par période.

{% alert note %}
Le tableau de bord **Industry Benchmarks** est actuellement en accès anticipé. Contactez votre gestionnaire de la satisfaction client si vous souhaitez participer à l'accès anticipé.
{% endalert %}

## À propos du tableau de bord {#about-the-dashboard}

Le tableau de bord est organisé en quatre sections par canal : **Email**, **Notification push**, **Content Card** et **SMS** :

| Section | Description |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cartes d'indicateurs clés de performance | Affichent le taux de votre espace de travail pour chaque indicateur clé, ainsi que l'écart par rapport au taux du secteur. Une flèche verte vers le haut indique que votre espace de travail est au-dessus du taux du secteur ; une flèche rouge vers le bas indique qu'il est en dessous. |
| Graphique de tendance mensuelle | Trace le taux de votre espace de travail par rapport au taux du secteur au fil du temps, afin d'identifier la saisonnalité et les tendances à plus long terme. |
| Répartition régionale | Décompose le taux de votre espace de travail par rapport au taux du secteur selon les régions, afin de repérer les écarts de performance régionale par rapport au secteur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Section" }

Dans chaque graphique, la série de couleur plus claire représente le benchmark sectoriel et la série plus foncée (préfixée par **Workspace**) représente vos propres performances.

## Indicateurs disponibles {#available-metrics}

Chaque indicateur par canal est disponible sous deux types :

| Type d'indicateur | Description | Exemple |
|----------|---------------------------------------|------------------------------------------------------|
| _Total_ | Comptabilise chaque événement d'engagement. | Si un utilisateur clique trois fois, cela est compté comme trois clics. |
| _Distinct_ | Comptabilise les utilisateurs uniques. | Si un utilisateur clique trois fois, cela est compté comme un seul clic. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metric type" }

Les indicateurs sont regroupés selon les combinaisons suivantes de secteur, région, sous-secteur et date :

- Secteur + Date
- Secteur + Région + Date
- Secteur + Sous-secteur + Région + Date

Sélectionnez un onglet pour afficher les indicateurs de chaque canal.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab E-mail %}

<table aria-label="Indicateurs e-mail"><thead><tr><th>Indicateur</th><th>Description</th><th>Formule</th></tr></thead><tbody>
<tr><td class="no-split"><i>Taux d'ouverture unique</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Ce taux exclut les ouvertures automatiques.</td><td class="no-split"><i>Ouvertures uniques</i> / <i>Envois uniques</i></td></tr>
<tr><td class="no-split"><i>Taux de clics unique</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Clics uniques</i> / <i>Envois uniques</i></td></tr>
<tr><td class="no-split"><i>Taux de clics par ouverture unique</i></td><td class="no-split">Le pourcentage d'utilisateurs qui ont cliqué sur un e-mail après l'avoir ouvert.</td><td class="no-split"><i>Clics uniques</i> / <i>Ouvertures uniques</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Email metrics" }

![Indicateurs de benchmarks sectoriels pour l'e-mail affichés sous forme de graphiques linéaires et de graphiques à barres.]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab Push %}

Les indicateurs push sont disponibles pour iOS, Android, Web et pour l'ensemble des plateformes combinées.

<table aria-label="Indicateurs push"><thead><tr><th>Indicateur</th><th>Description</th><th>Formule</th></tr></thead><tbody>
<tr><td class="no-split"><i>Taux d'ouverture directe</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Ouvertures directes</i> / <i>Envois uniques</i></td></tr>
<tr><td class="no-split"><i>Taux d'ouverture influencée</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Ouvertures influencées</i> / <i>Envois uniques</i></td></tr>
<tr><td class="no-split"><i>Taux d'ouverture total</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Ouvertures directes</i> + <i>Ouvertures influencées</i>) / <i>Envois uniques</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push metrics" }

![Indicateurs de benchmarks sectoriels pour le push affichés sous forme de graphiques linéaires et de graphiques à barres.]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab SMS %}

<table aria-label="Indicateurs SMS"><thead><tr><th>Indicateur</th><th>Description</th><th>Formule</th></tr></thead><tbody>
<tr><td class="no-split"><i>Taux de distribution</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Distributions</i> / <i>Envois uniques</i></td></tr>
<tr><td class="no-split"><i>Taux de clics sur lien court</i></td><td class="no-split">Le pourcentage d'utilisateurs qui ont cliqué sur un lien court après avoir reçu un SMS.</td><td class="no-split"><i>Clics sur lien court</i> / <i>Envois uniques</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS metrics" }

![Indicateurs de benchmarks sectoriels pour le SMS affichés sous forme de graphiques linéaires et de graphiques à barres.]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Indicateurs Content Cards"><thead><tr><th>Indicateur</th><th>Description</th><th>Formule</th></tr></thead><tbody>
<tr><td class="no-split"><i>Taux de clics</i></td><td class="no-split">Le pourcentage d'utilisateurs qui ont reçu une Content Card et cliqué sur un lien.</td><td class="no-split"><i>Clics uniques</i> / <i>Impressions uniques</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Cards metrics" }

![Indicateurs de benchmarks sectoriels pour les Content Cards affichés sous forme de graphiques linéaires et de graphiques à barres.]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## Méthodologie {#methodology}

Les benchmarks Braze sont calculés selon un processus en trois étapes conçu pour produire des chiffres stables et représentatifs.

### Étape 1 : Échantillonnage dynamique {#step-1-dynamic-sampling}

Plutôt que d'analyser chaque point de donnée, Braze sélectionne un échantillon représentatif. La méthode d'échantillonnage sur-échantillonne les groupes d'utilisateurs plus petits pour garantir une représentation adéquate et ajuste en fonction de la taille de l'entreprise afin qu'un petit nombre de très grandes entreprises ne fausse pas les résultats pour l'ensemble d'un secteur.

### Étape 2 : Suppression des valeurs aberrantes {#step-2-outlier-removal}

Braze identifie et supprime les valeurs statistiquement aberrantes. Cela réduit considérablement la volatilité des données avec un impact minimal sur les taux de performance moyens, ce qui signifie que les anomalies sont éliminées sans modifier les tendances sous-jacentes.

### Étape 3 : Pondération post-stratification {#step-3-post-stratification-weighting}

L'échantillon est pondéré pour refléter la population réelle. Des poids sont appliqués aux sous-groupes pour corriger les déséquilibres résiduels de l'échantillonnage, ce qui produit des benchmarks finaux représentatifs et non biaisés.

## Gouvernance des données {#data-governance}

- **Cycle d'actualisation :** les données sont actualisées mensuellement le 5 de chaque mois et sont à jour jusqu'au dernier mois complet.
- **Confidentialité :** tous les benchmarks sont agrégés et anonymisés pour protéger les informations des utilisateurs.