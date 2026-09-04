---
nav_title: Générateur de tableaux de bord
article_title: Générateur de tableaux de bord
alias: "/dashboard_builder/"
description: "Cet article de référence explique comment utiliser le Générateur de tableaux de bord pour créer des tableaux de bord et des visualisations à partir de rapports créés dans le Générateur de requêtes."
page_type: reference
tool:
    - Reports
page_order: 6
---

# Générateur de tableaux de bord {#dashboard-builder}

> Utilisez le Générateur de tableaux de bord pour créer des tableaux de bord et des visualisations à partir de rapports créés dans le Générateur de rapports ou le Générateur de requêtes.

Le Générateur de tableaux de bord vous permet de composer et de visualiser des tableaux de bord analytiques personnalisés, que ce soit à partir de zéro ou à partir de tableaux de bord fournis par Braze. Vous pouvez utiliser une source de données sans code (Générateur de rapports) ou une source de données SQL (Générateur de requêtes) pour alimenter votre tableau de bord, ou partir de l'un des nombreux tableaux de bord fournis par Braze.

## Créer un tableau de bord personnalisé {#creating-a-custom-dashboard}

1. Accédez à **Analytics** > **Générateur de tableaux de bord**.
2. Sélectionnez **Create Dashboard**.
3. Sélectionnez la source de données qui alimentera vos rapports :
- **Reports** créés dans le générateur de rapports
- **Custom Queries** créées dans le générateur de requêtes<br><br>![Fenêtre de sélection de la source de données pour votre tableau de bord.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Suivez ensuite les étapes correspondant à votre source de données :

{% tabs %}
{% tab Reports %}

{: start="4"}
4. Sélectionnez **+ Add Tile**, puis choisissez l'un des rapports que vous avez créés dans le [générateur de rapports (nouveau)]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

{% alert important %}
Une fois qu'un rapport du générateur de rapports est ajouté à une tuile du générateur de tableaux de bord, la tuile n'est pas connectée au rapport d'origine. Si vous modifiez le rapport d'origine dans le générateur de rapports, vous devez supprimer la tuile existante du tableau de bord et en créer une nouvelle en utilisant le rapport mis à jour comme source de données.
{% endalert %}

{: start="5"}
5. Sélectionnez l'icône en forme de crayon pour modifier l'affichage du titre et du type de graphique dans la tuile.
    - Vous pouvez basculer entre différents types de graphiques dans les contrôles de type de graphique. Les options actuelles incluent les graphiques à barres (horizontales ou verticales) et les graphiques linéaires (disponibles uniquement si vous avez sélectionné **Date** comme option de ventilation dans la configuration du générateur de rapports).<br><br>![Boutons pour basculer entre les différents types de graphiques.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Utilisez le menu déroulant des indicateurs pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, la première colonne du rapport sera l'indicateur affiché par défaut.
6. Sélectionnez **Save** après avoir modifié la visualisation à votre convenance.
7. Ajoutez un nom, une description et une étiquette pour retrouver votre tableau de bord plus facilement par la suite.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. Sélectionnez **+ Add Tile**, puis choisissez une requête que vous avez exécutée dans le générateur de requêtes.
5. Pour modifier l'affichage des résultats de la requête dans la tuile, sélectionnez l'icône en forme de crayon pour changer le titre et le type de graphique.
    - Vous pouvez basculer entre différents types de graphiques dans les contrôles de type de graphique. Les options actuelles incluent les tableaux, les graphiques à barres (horizontales ou verticales) et les graphiques linéaires.<br><br>![Boutons pour basculer entre les différents types de graphiques.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Si vous choisissez l'une des options de graphique, utilisez le menu déroulant **X-axis** pour sélectionner une seule colonne de vos résultats de requête à utiliser comme axe des abscisses.
        - Utilisez le menu déroulant **Y-axis** pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, toutes les colonnes de vos résultats de requête s'afficheront ; désélectionnez celles que vous ne souhaitez pas visualiser.<br><br>![Boutons pour basculer entre les différents types de graphiques.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Facultatif) Vous pouvez utiliser le menu déroulant **Grouping** pour regrouper vos résultats de requête. Par exemple, si vous avez un identifiant de campagne comme colonne de résultat et que vous souhaitez additionner toutes les lignes ayant cette valeur, utilisez le menu déroulant **Grouping**.
        - (Facultatif) Pour modifier les données affichées, sélectionnez la requête associée au visuel et effectuez vos modifications dans le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
6. Sélectionnez **Save** après avoir modifié la visualisation à votre convenance.
7. Ajoutez un nom, une description et une étiquette pour retrouver votre tableau de bord plus facilement par la suite.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Répétez les étapes 4 à 7 pour la méthode correspondante jusqu'à obtenir le tableau de bord souhaité.
9. Sélectionnez **View Dashboard** > puis **Run Dashboard**.

La génération des rapports de votre tableau de bord peut prendre quelques minutes.

{% alert note %}
Vous pouvez ajouter jusqu'à 10 tuiles à un tableau de bord.
{% endalert %}

## Gestion des tuiles du tableau de bord {#managing-dashboard-tiles}

### Supprimer des tuiles {#delete-tiles}

Supprimez une tuile du tableau de bord en sélectionnant **Delete Tile** en bas de la tuile. **Cette action est irréversible.**

### Dupliquer des tuiles {#duplicate-tiles}

Créez une copie de votre tuile en sélectionnant **Duplicate Tile** en bas de la tuile.

### Ajuster la taille et la position des tuiles {#adjust-tile-size-and-position}

Ajustez la taille de la tuile en faisant glisser la poignée de redimensionnement, et ajustez la position de la tuile sur le tableau de bord en faisant glisser la poignée de la tuile.

## Exécuter un tableau de bord {#running-a-dashboard}

1. Rendez-vous dans **Analytics** > **Dashboard Builder**. La page d'accueil liste tous les tableaux de bord existants au sein de votre espace de travail, avec les tableaux de bord créés par Braze en haut. Ceux-ci sont identifiés par la mention « (Braze) » dans le titre.
2. Sélectionnez le tableau de bord qui vous intéresse.
3. Sélectionnez **Run Dashboard** pour charger le tableau de bord correspondant.

### Tableaux de bord disponibles {#available-dashboards}

Braze fournit des tableaux de bord préconfigurés pour les cas d'usage les plus fréquents. Utilisez le tableau suivant comme référence unique pour les tableaux de bord actuellement documentés et leur chemin d'accès.

| Tableau de bord | Chemin d'accès | Documentation |
| --- | --- | --- |
| Revenue - Last Touch Attribution | **Analytics** > **Dashboard Builder** | [Revenue - Last Touch Attribution](#revenue---last-touch-attribution) |
| Devices and carriers | **Analytics** > **Dashboard Builder** | [Devices and carriers](#devices-and-carriers) |
| Segment Insights - Email | **Analytics** > **Dashboard Builder** | [Segment Insights - Email](#segment-insights---email) |
| Session Analytics | **Analytics** > **Dashboard Builder** | [Session Analytics](#session-analytics) |
| eCommerce Revenue - Last Touch Attribution | **Analytics** > **Dashboard Builder** | [Tableau de bord des revenus eCommerce]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/ecommerce_revenue_dashboard) |
| Messaging Diagnostics | **Analytics** > **Dashboard Builder** | [Tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) |
| Industry Benchmarks | **Analytics** > **Dashboard Builder** | [Tableau de bord des benchmarks sectoriels]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/industry_benchmarks_dashboard) |
| Email performance | **Analytics** > **Email Performance** | [Tableaux de bord de performance par canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-performance-dashboard) |
| SMS performance | **Analytics** > **SMS Performance** | [Tableaux de bord de performance par canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#sms-performance-dashboard) |
| Push performance | **Analytics** > **Dashboard Builder** > **Push Channel Dashboard** | [Tableaux de bord de performance par canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#push-performance-dashboard) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tableaux de bord disponibles" }

{% alert note %}
La possibilité de modifier les tableaux de bord créés par Braze n'est pas encore disponible. Contactez votre gestionnaire du succès des clients si vous souhaitez demander des tableaux de bord supplémentaires.
{% endalert %}

#### Revenue - Last Touch Attribution {#revenue---last-touch-attribution}

Le tableau de bord **Revenue - Last Touch Attribution** fournit un aperçu du chiffre d'affaires à travers les campagnes, les Canvas et les canaux. Toutes les données de chiffre d'affaires sont attribuées au dernier message avec lequel l'utilisateur a interagi pendant la fenêtre d'attribution.

Les interactions incluent _Email Click_ (clic sur un lien), _Content Card Click_, _In-App Message Click_ (à l'exclusion des boutons de fermeture), _Push Opens_, _SMS Short Link Click_, _WhatsApp Read_ et _Webhook Send_.

| Indicateur | Définition |
| --- | --- |
| Chiffre d'affaires total (dernière interaction) | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction dans la plage de dates et la fenêtre d'attribution sélectionnées. |
| Total des conversions d'achat | Nombre total d'événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction qualifié. |
| Nombre moyen de jours avant conversion | Temps moyen entre tous les événements d'achat des campagnes et Canvas ayant un événement de dernière interaction qualifié. |
| Chiffre d'affaires par destinataire | Somme du chiffre d'affaires des événements qualifiés divisée par le nombre d'utilisateurs uniques ayant reçu un message dans la plage de dates. |
| Acheteurs uniques | Nombre d'utilisateurs uniques ayant un événement de chiffre d'affaires qualifié. |
| Chiffre d'affaires par pays | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction, regroupés par pays. |
| Chiffre d'affaires par campagne | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction qualifié, regroupés par campagne. |
| Chiffre d'affaires par variante de campagne | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction qualifié, regroupés par variante de campagne. |
| Chiffre d'affaires par Canvas | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction qualifié, regroupés par Canvas. |
| Chiffre d'affaires par variante du Canvas | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction qualifié, regroupés par variante du Canvas. |
| Achats par produit | Nombre total d'achats regroupés par produit. |
| Chiffre d'affaires par canal | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction qualifié, regroupés par canal. |
| Série temporelle du chiffre d'affaires | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernière interaction qualifié, regroupés par jour en UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue - Last Touch Attribution" }

#### Devices and carriers {#devices-and-carriers}

| Indicateur | Définition |
| --- | --- |
| Opérateurs d'appareils | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par opérateur d'appareil. |
| Modèle d'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par modèle d'appareil. |
| Système d'exploitation de l'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par système d'exploitation de l'appareil. |
| Taille d'écran de l'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par résolution d'écran (taille) de l'appareil. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Appareils et opérateurs" }

#### Segment Insights - Email {#segment-insights---email}

| Indicateur | Définition |
|---|---|
| Indicateurs e-mail hebdomadaires (taux) | Taux d'engagement e-mail (distribution, rebonds, ouvertures, clics, taux de désabonnement) regroupés par Segment et affichés sous forme de série temporelle hebdomadaire. |
| Indicateurs e-mail hebdomadaires (nombres) | Nombres d'engagement e-mail (envoyés, distribués, rebonds, ouvertures, clics, désabonnements) regroupés par Segment et affichés sous forme de série temporelle hebdomadaire. |
| Indicateurs d'achat hebdomadaires (taux) | Taux de conversion d'achat (chiffre d'affaires par destinataire) à partir des ouvertures et clics e-mail, regroupés par Segment et affichés sous forme de série temporelle hebdomadaire. |
| Indicateurs d'achat hebdomadaires (nombres) | Nombres d'achats et totaux de chiffre d'affaires à partir des ouvertures et clics e-mail, regroupés par Segment et affichés sous forme de série temporelle hebdomadaire. |
| Engagement e-mail par Segment | Tableau récapitulatif affichant les indicateurs d'engagement e-mail totaux (envoyés, distribués, rebonds, ouvertures, clics, désabonnements, et leurs taux) agrégés par Segment. |
| Achats et chiffre d'affaires par Segment | Tableau récapitulatif affichant les indicateurs d'achat totaux (achats, chiffre d'affaires et chiffre d'affaires par destinataire) à partir des ouvertures et clics e-mail, agrégés par Segment. |
| Top 10 des campagnes pour les indicateurs d'engagement | Liste classée des campagnes ayant les indicateurs d'engagement e-mail les plus élevés (indicateur configurable pour le classement). |
| 10 dernières campagnes pour les indicateurs d'engagement | Liste classée des campagnes ayant les indicateurs d'engagement e-mail les plus faibles (indicateur configurable pour le classement). |
| Top 10 des Canvas pour les indicateurs d'engagement | Liste classée des Canvas ayant les indicateurs d'engagement e-mail les plus élevés (indicateur configurable pour le classement). |
| 10 derniers Canvas pour les indicateurs d'engagement | Liste classée des Canvas ayant les indicateurs d'engagement e-mail les plus faibles (indicateur configurable pour le classement). |
| Top 10 des campagnes pour les indicateurs d'achat | Liste classée des campagnes ayant les indicateurs de conversion d'achat les plus élevés à partir de l'engagement e-mail (indicateur configurable pour le classement). |
| 10 dernières campagnes pour les indicateurs d'achat | Liste classée des campagnes ayant les indicateurs de conversion d'achat les plus faibles à partir de l'engagement e-mail (indicateur configurable pour le classement). |
| Top 10 des Canvas pour les indicateurs d'achat | Liste classée des Canvas ayant les indicateurs de conversion d'achat les plus élevés à partir de l'engagement e-mail (indicateur configurable pour le classement). |
| 10 derniers Canvas pour les indicateurs d'achat | Liste classée des Canvas ayant les indicateurs de conversion d'achat les plus faibles à partir de l'engagement e-mail (indicateur configurable pour le classement). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statistiques des segments - E-mail" }

#### Session Analytics {#session-analytics}

| Indicateur | Définition |
|---|---|
| Nombre de sessions par jour (série temporelle) | Nombre de sessions uniques regroupées par jour dans la plage de dates sélectionnée, affichées sous forme de série temporelle. |
| Nombre moyen de sessions par utilisateur | Nombre moyen de sessions par utilisateur calculé comme le total des sessions divisé par le nombre d'utilisateurs uniques dans la plage de dates sélectionnée. |
| Campagnes converties en sessions | Nombre de sessions uniques survenues en même temps que des conversions de campagne, regroupées par identifiant de campagne et classées par nombre de sessions. |
| Canvas convertis en sessions | Nombre de sessions uniques survenues en même temps que des conversions de Canvas, regroupées par identifiant de Canvas et classées par nombre de sessions. |
| Nombre total de sessions par utilisateur | Liste des 1 000 premiers utilisateurs classés par leur nombre total de sessions dans la plage de dates sélectionnée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analyse des sessions" }

## Partagez vos commentaires avec nous {#share-your-feedback-with-us}

{% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="Dashboard Builder" %}