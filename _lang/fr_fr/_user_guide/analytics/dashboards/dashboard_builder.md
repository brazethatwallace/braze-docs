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
2. Sélectionnez **Créer un tableau de bord**.
3. Sélectionnez la source de données qui alimentera vos rapports :
- **Rapports** créés dans le Générateur de rapports
- **Requêtes personnalisées** créées dans le Générateur de requêtes<br><br>![Fenêtre de sélection de la source de données pour votre tableau de bord.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Suivez ensuite les étapes correspondant à votre source de données :

{% tabs %}
{% tab Rapports %}

{: start="4"}
4. Sélectionnez **+ Ajouter une tuile**, puis choisissez l'un des rapports que vous avez créés dans le [Générateur de rapports (Nouveau)]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

{% alert important %}
Une fois qu'un rapport du Générateur de rapports est ajouté à une tuile du Générateur de tableaux de bord, la tuile n'est pas connectée au rapport d'origine. Si vous modifiez le rapport d'origine dans le Générateur de rapports, vous devez supprimer la tuile existante du tableau de bord et en créer une nouvelle en utilisant le rapport mis à jour comme source de données.
{% endalert %}

{: start="5"}
5. Sélectionnez l'icône de crayon pour modifier l'affichage du titre et du type de graphique dans la tuile.
    - Vous pouvez basculer entre différents types de graphiques sous la visualisation par défaut. Les options actuelles incluent les graphiques à barres (horizontaux ou verticaux) et les graphiques linéaires (disponibles uniquement si vous avez sélectionné **Date** comme option de ventilation dans la configuration du Générateur de rapports).<br><br>![Boutons de basculement pour les différents types de graphiques.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Utilisez le menu déroulant des indicateurs pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, la première colonne du rapport sera l'indicateur affiché.
6. Sélectionnez **Enregistrer** une fois que vous avez modifié la visualisation à votre convenance.
7. Ajoutez un nom, une description et une étiquette pour retrouver plus facilement votre tableau de bord par la suite.
{% endtab %}
{% tab Requêtes personnalisées %}
{: start="4"}
4. Sélectionnez **+ Ajouter une tuile**, puis choisissez une requête que vous avez exécutée dans le Générateur de requêtes.
5. Pour modifier l'affichage des résultats de la requête dans la tuile, sélectionnez l'icône de crayon pour changer le titre et le type de graphique.
    - Vous pouvez basculer entre différents types de graphiques sous la visualisation par défaut. Les options actuelles incluent les tableaux, les graphiques à barres (horizontaux ou verticaux) et les graphiques linéaires.<br><br>![Boutons de basculement pour les différents types de graphiques.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Si vous choisissez l'une des options de graphique, utilisez le menu déroulant **Axe X** pour sélectionner une seule colonne de vos résultats de requête à utiliser comme axe X.
        - Utilisez le menu déroulant **Axe Y** pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, toutes les colonnes de vos résultats de requête seront affichées ; désélectionnez celles que vous ne souhaitez pas visualiser.<br><br>![Boutons de basculement pour les différents types de graphiques.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Facultatif) Vous pouvez utiliser le menu déroulant **Regroupement** pour regrouper les résultats de votre requête. Par exemple, si vous avez un ID de campagne comme colonne de résultat et que vous souhaitez additionner toutes les lignes ayant cette valeur, utilisez le menu déroulant **Regroupement**.
        - (Facultatif) Pour modifier les données affichées, sélectionnez la requête associée au visuel et effectuez vos modifications dans le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
6. Sélectionnez **Enregistrer** une fois que vous avez modifié la visualisation à votre convenance.
7. Ajoutez un nom, une description et une étiquette pour retrouver plus facilement votre tableau de bord par la suite.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Répétez les étapes 4 à 7 pour votre méthode respective jusqu'à obtenir le tableau de bord souhaité.
9. Sélectionnez **Afficher le tableau de bord** > sélectionnez **Exécuter le tableau de bord**.

La génération des rapports de votre tableau de bord peut prendre quelques minutes.

{% alert note %}
Vous pouvez ajouter jusqu'à 10 tuiles à un tableau de bord.
{% endalert %}

## Gérer les tuiles du tableau de bord {#managing-dashboard-tiles}

### Supprimer des tuiles {#delete-tiles}

Supprimez une tuile du tableau de bord en sélectionnant **Supprimer la tuile** en bas de la tuile. **Cette action est irréversible.**

### Dupliquer des tuiles {#duplicate-tiles}

Créez une copie de votre tuile en sélectionnant **Dupliquer la tuile** en bas de la tuile.

### Ajuster la taille et la position des tuiles {#adjust-tile-size-and-position}

Ajustez la taille de la tuile en faisant glisser le coin inférieur droit de la tuile, et ajustez la position de la tuile sur le tableau de bord en faisant glisser la poignée située dans le coin supérieur droit de la tuile.

## Exécuter un tableau de bord {#running-a-dashboard}

1. Accédez à **Analytics** > **Générateur de tableaux de bord**. La page d'accueil répertorie tous les tableaux de bord existants dans votre espace de travail, avec les tableaux de bord créés par Braze en haut de la liste. Ceux-ci sont identifiés par la mention « (Braze) » dans le titre.
2. Sélectionnez le tableau de bord qui vous intéresse.
3. Sélectionnez **Exécuter le tableau de bord** pour charger le tableau de bord correspondant.

### Tableaux de bord disponibles {#available-dashboards}

Braze fournit des tableaux de bord préconfigurés pour les cas d'utilisation courants, comme l'analyse du chiffre d'affaires par attribution au dernier point de contact. Notez que la possibilité de modifier un tableau de bord n'est pas encore disponible. Contactez votre gestionnaire de la satisfaction client si vous souhaitez voir certains tableaux de bord à l'avenir.

#### Chiffre d'affaires - Attribution au dernier point de contact {#revenue-last-touch-attribution}

Le tableau de bord **Revenue - Last Touch Attribution** fournit une vue d'ensemble du chiffre d'affaires par campagne, Canvas et canal. Toutes les données de chiffre d'affaires sont attribuées au dernier message avec lequel l'utilisateur a interagi pendant la fenêtre d'attribution.

Les points de contact incluent le *clic sur un e-mail* (clic sur un lien), le *clic sur une carte de contenu*, le *clic sur un message in-app* (hors boutons de fermeture), les *ouvertures de notification push*, le *clic sur un lien court SMS*, la *lecture WhatsApp* et l'*envoi de webhook*.

| Indicateur | Définition |
| --- | --- |
| Chiffre d'affaires total au dernier point de contact | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact dans la plage de dates et la fenêtre d'attribution sélectionnées. |
| Total des conversions d'achat | Nombre de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact qualifiant. |
| Nombre moyen de jours avant conversion | Durée moyenne entre tous les événements d'achat des campagnes et Canvas ayant un événement de dernier point de contact qualifiant. |
| Chiffre d'affaires par destinataire | Somme du chiffre d'affaires des événements de chiffre d'affaires qualifiés divisée par le nombre d'utilisateurs uniques ayant reçu un message dans la plage de dates. |
| Acheteurs uniques | Nombre d'utilisateurs uniques ayant un événement de chiffre d'affaires qualifié. |
| Chiffre d'affaires par pays | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact, regroupés par pays. |
| Chiffre d'affaires par campagne | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact qualifiant, regroupés par campagne. |
| Chiffre d'affaires par variante de campagne | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact qualifiant, regroupés par variante de campagne. |
| Chiffre d'affaires par Canvas | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact qualifiant, regroupés par Canvas. |
| Chiffre d'affaires par variante du Canvas | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact qualifiant, regroupés par variante du Canvas. |
| Achats par produit | Nombre de tous les achats regroupés par produit. |
| Chiffre d'affaires par canal | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact qualifiant, regroupés par canal. |
| Série temporelle du chiffre d'affaires | Somme de tous les événements de chiffre d'affaires des campagnes et Canvas ayant un événement de dernier point de contact qualifiant, regroupés par jour en UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chiffre d'affaires - Attribution au dernier point de contact" }

#### Appareils et opérateurs {#devices-and-carriers}

| Indicateur | Définition |
| --- | --- |
| Opérateurs des appareils | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par opérateur de l'appareil. |
| Modèle d'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par modèle d'appareil. |
| Système d'exploitation de l'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par système d'exploitation de l'appareil. |
| Taille d'écran de l'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée ayant ouvert une notification push, regroupés par résolution d'écran (taille) de l'appareil. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Appareils et opérateurs" }

#### Statistiques des segments - E-mail {#segment-insights-email}

| Indicateur | Définition |
|---|---|
| Indicateurs e-mail hebdomadaires (taux) | Taux d'engagement e-mail (taux de réception, de rebond, d'ouverture, de clic et de désabonnement) regroupés par segment et affichés sous forme de série temporelle hebdomadaire. |
| Indicateurs e-mail hebdomadaires (nombres) | Nombres d'engagement e-mail (envois, réceptions, rebonds, ouvertures, clics, désabonnements) regroupés par segment et affichés sous forme de série temporelle hebdomadaire. |
| Indicateurs d'achat hebdomadaires (taux) | Taux de conversion d'achat (chiffre d'affaires par destinataire) à partir des ouvertures et clics d'e-mails, regroupés par segment et affichés sous forme de série temporelle hebdomadaire. |
| Indicateurs d'achat hebdomadaires (nombres) | Nombres d'achats et totaux de chiffre d'affaires à partir des ouvertures et clics d'e-mails, regroupés par segment et affichés sous forme de série temporelle hebdomadaire. |
| Engagement e-mail par segment | Tableau récapitulatif montrant les indicateurs d'engagement e-mail totaux (envois, réceptions, rebonds, ouvertures, clics, désabonnements et leurs taux) agrégés par segment. |
| Achats et chiffre d'affaires par segment | Tableau récapitulatif montrant les indicateurs d'achat totaux (achats, chiffre d'affaires et chiffre d'affaires par destinataire) à partir des ouvertures et clics d'e-mails, agrégés par segment. |
| Top 10 des campagnes pour les indicateurs d'engagement | Liste classée des campagnes ayant les indicateurs d'engagement e-mail les plus élevés (indicateur configurable pour le classement). |
| 10 dernières campagnes pour les indicateurs d'engagement | Liste classée des campagnes ayant les indicateurs d'engagement e-mail les plus faibles (indicateur configurable pour le classement). |
| Top 10 des Canvas pour les indicateurs d'engagement | Liste classée des Canvas ayant les indicateurs d'engagement e-mail les plus élevés (indicateur configurable pour le classement). |
| 10 derniers Canvas pour les indicateurs d'engagement | Liste classée des Canvas ayant les indicateurs d'engagement e-mail les plus faibles (indicateur configurable pour le classement). |
| Top 10 des campagnes pour les indicateurs d'achat | Liste classée des campagnes ayant les indicateurs de conversion d'achat les plus élevés à partir de l'engagement e-mail (indicateur configurable pour le classement). |
| 10 dernières campagnes pour les indicateurs d'achat | Liste classée des campagnes ayant les indicateurs de conversion d'achat les plus faibles à partir de l'engagement e-mail (indicateur configurable pour le classement). |
| Top 10 des Canvas pour les indicateurs d'achat | Liste classée des Canvas ayant les indicateurs de conversion d'achat les plus élevés à partir de l'engagement e-mail (indicateur configurable pour le classement). |
| 10 derniers Canvas pour les indicateurs d'achat | Liste classée des Canvas ayant les indicateurs de conversion d'achat les plus faibles à partir de l'engagement e-mail (indicateur configurable pour le classement). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statistiques des segments - E-mail" }

#### Analyse des sessions {#session-analytics}

| Indicateur | Définition |
|---|---|
| Nombre de sessions par jour (série temporelle) | Nombre de sessions uniques regroupées par jour dans la plage de dates sélectionnée, affichées sous forme de série temporelle. |
| Nombre moyen de sessions par utilisateur | Nombre moyen de sessions par utilisateur calculé comme le total des sessions divisé par le nombre d'utilisateurs uniques dans la plage de dates sélectionnée. |
| Campagnes converties en sessions | Nombre de sessions uniques survenues en même temps que des conversions de campagne, regroupées par ID de campagne et classées par nombre de sessions. |
| Canvas convertis en sessions | Nombre de sessions uniques survenues en même temps que des conversions de Canvas, regroupées par ID de Canvas et classées par nombre de sessions. |
| Nombre total de sessions par utilisateur | Liste des 1 000 premiers utilisateurs par nombre total de sessions dans la plage de dates sélectionnée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analyse des sessions" }

## Partagez vos commentaires {#share-your-feedback-with-us}

Sélectionnez le bouton **Envoyer des commentaires** ou contactez votre gestionnaire de la satisfaction client pour nous faire part de vos retours.