---
nav_title: Données de segment
article_title: Données de segment
page_order: 4
page_type: reference
description: "Cette page explique la section Segments de votre tableau de bord de Braze et inclut un résumé des statistiques fournies."
alias: /viewing_and_understanding_segment_data/
tool:
  - Segments
  - Reports

---
# Données de segment {#segment-data}

> Cette page explique la section Segments de votre tableau de bord de Braze et inclut un résumé des statistiques fournies.

## Accéder aux données de vos segments et à l'appartenance {#accessing-data-about-your-segments-and-membership}

La page **Segments** de votre tableau de bord de Braze contient un résumé de tous vos segments et vous permet d'examiner les données détaillées de chacun d'entre eux. Sur cette page, recherchez et sélectionnez le nom d'un segment pour le modifier et consulter ses données. Pour savoir comment créer un segment, consultez [Créer un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#creating-a-segment).

![Page Segments]({% image_buster /assets/img_archive/segments.png %})

Après avoir sélectionné le nom d'un segment, vous pouvez consulter les statistiques et les filtres du segment, et le modifier en ajoutant ou en supprimant des filtres. N'oubliez pas d'enregistrer vos modifications !

Lorsque vous activez le [suivi analytique pour un segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking), vous pouvez consulter les sessions, les événements personnalisés et le chiffre d'affaires au fil du temps pour ce segment.

![Basculer le suivi analytique pour un segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Statistiques de segment {#segment-statistics}

Vous pouvez consulter les statistiques de segment suivantes, qui se mettent à jour en temps réel lorsque vous ajoutez ou supprimez des filtres :

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Statistiques de segment">
  <caption>Statistiques de segment</caption>
    <thead>
        <tr>
            <th>Statistique</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total des utilisateurs</td>
            <td class="no-split">Le nombre total d'utilisateurs de votre application.</td>
        </tr>
        <tr>
            <td class="no-split">Utilisateurs sélectionnés</td>
            <td class="no-split">Le nombre d'utilisateurs dans votre segment et le pourcentage qu'ils représentent par rapport à votre base totale d'utilisateurs.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (utilisateurs payants)</td>
            <td class="no-split">La valeur vie client par utilisateur (LTV) dans ce segment et la valeur vie client par utilisateur payant dans ce segment. La LTV est calculée en divisant votre chiffre d'affaires total par le nombre total d'utilisateurs.</td>
        </tr>
        <tr>
            <td class="no-split">Joignable par e-mail (abonnés)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} En raison des <a href="/docs/help/best_practices/spam_regulations#spam-regulationsspam regulations">réglementations anti-spam</a>, il est recommandé de demander à vos utilisateurs de s'abonner explicitement en mettant en place une politique de double abonnement où les utilisateurs doivent cliquer sur un lien dans un e-mail de confirmation initial. Pour encourager davantage d'utilisateurs à s'abonner, vous pouvez cibler un message vers <a href="/docs/user_guide/channels/email/subscriptions#segmenting-by-user-subscriptions">ceux qui ne se sont ni abonnés ni désabonnés</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Notifications push activées (abonnés)</td>
            <td class="no-split">Les notifications push activées correspondent au nombre d'utilisateurs disposant d'au moins un jeton de notification push. Certains utilisateurs peuvent avoir plusieurs jetons de notification push (par exemple, s'ils possèdent un iPhone et un iPad), de sorte que le nombre de notifications push que vous envoyez à ce segment peut être supérieur au nombre d'utilisateurs « push activés ». « Abonnés » correspond au nombre d'utilisateurs ayant explicitement accepté de recevoir des notifications push. Les utilisateurs doivent toujours s'abonner explicitement pour que vous puissiez leur envoyer des notifications push.</td>
        </tr>
    </tbody>
</table>

### Statistiques des segments {#segment-insights}

Vous pouvez voir les performances d'un segment par rapport à un autre sur un ensemble d'indicateurs clés de performance présélectionnés en visitant la page [Statistiques des segments]({{site.baseurl}}/user_guide/audience/segments/segment_insights) de votre tableau de bord.

### Utilisation dans les messages {#messaging-use}
La section **Messaging Use** indique quels segments, Campaigns actuellement activées et Canvas actuellement activés ciblent votre segment.

### Historique d'appartenance {#historical-membership}

La section **Historical Membership** montre comment la taille de votre segment a évolué au fil du temps. Utilisez le menu déroulant pour filtrer l'appartenance au segment par plage de dates.

Pour en savoir plus sur le suivi de l'appartenance et de la taille de votre segment, consultez [Mesurer la taille d'un segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

### Aperçu des utilisateurs {#user-preview}

Pour consulter des informations détaillées et spécifiques aux utilisateurs de vos segments, cliquez sur **User Data** et sélectionnez **User Preview**.

Sur cette page, vous pouvez consulter un certain nombre d'attributs spécifiques aux utilisateurs, tels que le genre, l'âge, le nombre de sessions, et s'ils se sont abonnés aux notifications push et aux e-mails.

Notez que dans les cas où votre segment est très petit par rapport à la taille de votre espace de travail, il est possible que l'aperçu des utilisateurs ne renvoie aucun utilisateur. Cela ne signifie pas nécessairement qu'il n'y a aucun utilisateur dans votre segment ; exécutez [Calculate Exact Stats]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#statistics-for-segment-size) pour déterminer la taille exacte de votre segment.

![Aperçu des utilisateurs]({% image_buster /assets/img_archive/user_preview.png %})

## Consulter les données de performance par segment {#viewing-performance-data-by-segment}

Utilisez les [modèles de rapports du Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/data_by_segments) pour ventiler les indicateurs de performance des Campaigns, Canvas, variantes et étapes par segments.

## Créer un rapport de ventilation par segment avec le Générateur de requêtes {#creating-a-segment-breakdown-report-using-query-builder}

Pour créer un rapport à partir d'un modèle du [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder), accédez au **Générateur de requêtes** et procédez comme suit :

1. Sélectionnez **Create SQL Query** > **Query Template**.
2. Filtrez les modèles pour ceux dont les indicateurs incluent « segment breakdowns ».
3. Sélectionnez le modèle que vous souhaitez utiliser.
4. Renseignez les variables de votre modèle SQL dans l'onglet [Variables](#variables).
5. (Facultatif) Modifiez directement le SQL dans le modèle.
6. Sélectionnez **Run Query**. Vos résultats s'afficheront dans un tableau.

## Variables {#variables}

Avant de générer votre rapport, accédez à l'onglet **Variables** pour fournir les informations nécessaires au modèle du Générateur de rapports, y compris les variables requises qui varieront en fonction du rapport.

Les variables incluent :

- **Campaign ou Canvas :** vous pouvez inclure une ou plusieurs campagnes ou Canvas (il n'y a pas de maximum pour le nombre de campagnes ou Canvas que vous pouvez spécifier). Si vous ne spécifiez aucune campagne ni aucun Canvas, le rapport inclura toutes les campagnes ou tous les Canvas de la période choisie.
- **Variante :** si vous utilisez un modèle offrant une ventilation au niveau des variantes, après avoir sélectionné une campagne ou un Canvas, vous pouvez sélectionner des variantes au sein de cette campagne ou de ce Canvas. Si vous sélectionnez plusieurs variantes, vos résultats seront regroupés par variante.
- **Étape :** si vous sélectionnez une variante de Canvas, vous pouvez sélectionner une étape du Canvas. Vous ne pouvez pas sélectionner une étape sans avoir d'abord sélectionné une variante de Canvas.
- **Plage de dates :** identifiez la période pour laquelle vous souhaitez extraire les données. Si aucune plage de dates n'est spécifiée, la période par défaut sera les 30 derniers jours.
- **Nom du produit :** si vous exécutez un rapport sur les données d'achat, vous pouvez identifier un produit spécifique pour lequel extraire les données.
- **Fenêtre de conversion :** toujours requise pour les rapports contenant des données de chiffre d'affaires et d'achat. Le nombre de jours après la réception ou le clic sur un e-mail pendant lesquels Braze doit attribuer les achats ou le chiffre d'affaires.
- **Segments :** identifiez les segments par lesquels ventiler les données. Si aucun n'est spécifié, le rapport sera exécuté pour tous les segments dont le suivi analytique est activé.
- **Étiquettes :** spécifiez des étiquettes dans **Variables** pour exécuter votre rapport pour toutes les campagnes ou Canvas ayant certaines étiquettes. Vous pouvez inclure plusieurs étiquettes. Si vous ajoutez à la fois des étiquettes et des campagnes ou Canvas spécifiques à un rapport, votre rapport inclura les données de vos étiquettes et des campagnes ou Canvas spécifiés.

## Disponibilité des données {#data-availability}

Les données sont disponibles pour les périodes où ces deux conditions sont remplies :

1. Le [suivi analytique des segments]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) est activé pour les segments dont vous souhaitez consulter les données.
2. La fonctionnalité de données de performance par segment est activée.

Vous ne pouvez pas accéder aux données des périodes antérieures à l'activation de cette fonctionnalité pour votre entreprise. Par exemple, si le suivi analytique est activé pour le Segment A le 1er octobre et que cette fonctionnalité est activée pour votre entreprise le 2 octobre, vous ne pourrez consulter les données du Segment A que pour les campagnes et Canvas ayant enregistré des indicateurs après le 2 octobre.

Si votre entreprise a activé cette fonctionnalité le 2 octobre et a activé le suivi analytique pour le Segment B le 3 octobre, vous ne pourrez consulter les données du Segment B que pour les campagnes et Canvas ayant enregistré des indicateurs après le 3 octobre.