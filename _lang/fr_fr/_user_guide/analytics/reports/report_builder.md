---
nav_title: Générateur de rapports
article_title: Générateur de rapports
alias: /report_builder/
page_type: reference
description: "Cet article de référence décrit la fonctionnalité Générateur de rapports."
tool:
    - Reports
page_order: 3
---

# Générateur de rapports {#report-builder}

> Cette page explique comment utiliser le Générateur de rapports pour créer et consulter des rapports détaillés à partir des données Braze, et comment ajouter des rapports à des tableaux de bord.

La vidéo suivante offre un aperçu de la création et de la personnalisation de rapports dans le Générateur de rapports.

{% multi_lang_include video.html id="oi66kwwldv" source="wistia" %}

## Utiliser un modèle de rapport {#using-a-report-template}

1. Accédez à **Analytics** > **Report Builder (New)**.
2. Sélectionnez la flèche **More options** à côté du bouton **Create New Report**, puis sélectionnez **Use a report template**.<br><br>![Menu déroulant du bouton « Create New Report » avec les options de créer un rapport personnalisé ou d'utiliser un modèle.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Sélectionnez l'un des modèles de rapport dans la bibliothèque de modèles Braze.
    - Utilisez les menus déroulants **Row items** et **Tags** pour trouver les rapports pertinents pour vos cas d'utilisation.<br><br>![Fenêtre « Braze report templates » avec une liste de modèles Braze à sélectionner.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Suivez l'étape 3 et les suivantes dans [Créer un rapport](#creating-a-report) pour personnaliser davantage le rapport selon votre cas d'utilisation.

## Créer un rapport {#creating-a-report}

1. Accédez à **Analytics** > **Report Builder (New)**.
2. Sélectionnez **Create New Report**.
3. Dans le menu déroulant **Rows**, sélectionnez l'objet de votre rapport :
    - Campaigns
    - Canvases
    - Campaigns and Canvases
    - Channels
    - Tags

    Notez que votre sélection de **Rows** affectera [les indicateurs que vous pouvez consulter](#metrics-availability). Par exemple, vous pouvez afficher les indicateurs multivariés uniquement si vous créez un rapport sur les **Canvases**, ou les **Campaigns** avec un détail par **Variant**. Vous ne pouvez pas afficher ces indicateurs lorsque vous créez un rapport sur **Campaigns and Canvases**, même si ces Campaigns et Canvas comportent des tests multivariés.

![La section « Rows and columns » avec des champs pour sélectionner les lignes et les regroupements de votre rapport.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (Facultatif) Sélectionnez **Add drilldown** pour décomposer vos données en vues plus granulaires :
    - Channels
    - Date
        - Utilisez cette option pour diviser vos données en plages temporelles plus petites. Par exemple, si vous souhaitez savoir comment vos Campaigns ont performé par jour, sélectionnez la configuration suivante :
            - **Rows :** Campaigns
            - **Grouping :** Date
            - **Interval :** Days
    - Variants
    - Campaigns and Canvases

{% alert tip %}
Essayez différentes configurations d'options de détail pour explorer les [nombreuses façons de décomposer vos données](#metrics-availability).
{% endalert %}

{: start="5"}
5. Dans la section **Columns**, sélectionnez **Customize Metrics**.

![La section « Customize Metrics » avec des options pour sélectionner plusieurs indicateurs.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6. Parcourez les indicateurs par catégorie et cochez la case correspondante pour ajouter un indicateur à votre rapport.
    - Réorganisez les indicateurs et les colonnes en faisant glisser l'icône en pointillés vers le haut ou vers le bas.
7. Dans **Report content**, configurez la plage de dates pour laquelle vous souhaitez inclure des données dans votre rapport.
8. Ensuite, en fonction de vos sélections à l'étape 3, choisissez d'ajouter manuellement ou automatiquement des Campaigns, des Canvas, ou les deux à votre rapport.
    - **Ajouter manuellement :** Choisissez chaque Campaign ou Canvas à inclure dans le rapport en utilisant les filtres pour les dates de **Last Sent** et les étiquettes ou canaux, ou en recherchant le nom de la Campaign ou du Canvas.<br><br>![La section « Manually add campaigns and canvases » avec une liste de Campaigns à sélectionner.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Ajouter automatiquement :** Définissez des règles pour déterminer quelles Campaigns ou quels Canvas inclure dans le rapport. Vous n'êtes tenu de sélectionner qu'un seul champ sur cette page.
        - Notez qu'à mesure que des Campaigns ou des Canvas supplémentaires remplissent les conditions que vous avez définies sur cet écran, ils seront automatiquement ajoutés aux exécutions futures de votre rapport.<br><br>![La section « Automatically add campaigns and canvases » avec des champs pour définir les règles déterminant quelles Campaigns et quels Canvas doivent être ajoutés au rapport.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. Exécutez le rapport en sélectionnant **Save & Run**.

{% alert note %}
L'exécution du rapport peut prendre quelques minutes, en fonction de la plage de dates et du nombre de Campaigns ou de Canvas que vous avez sélectionnés lors de la configuration.
{% endalert %}

## Disponibilité des indicateurs {#metrics-availability}

Votre sélection pour **Rows** affecte les indicateurs que vous pouvez sélectionner.

{% alert tip %}
Si vous souhaitez créer un rapport sur les variantes ou les étapes de Canvas, sélectionnez **Canvases** pour les lignes et laissez le champ vide ou sélectionnez **Date** comme détail. Cela crée un menu déroulant **Canvas View** pour afficher les indicateurs du Canvas uniquement, ou regrouper les indicateurs par variante, étape ou message.

![Le menu déroulant « Canvas View » ouvert.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Indicateur | Description |
| --- | --- |
| Indicateurs de conversion | Disponibles pour Campaigns, Canvas, Campaigns et Canvas. |
| Entrées | Disponibles pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. |
| Date du dernier envoi | Disponible pour Campaigns, Canvas, Campaigns et Canvas. S'affiche uniquement pour les Campaigns planifiées — ne se remplit pas pour les Campaigns déclenchées par une action ou par l'API. |
| Envois | Disponibles pour chaque canal pertinent. |
| Messages envoyés | Disponibles pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. |
| Ligne d'objet | Disponible pour les Campaigns e-mail avec un détail par **Variant**, les Canvas et les Canvas avec un détail par **Variant**. |
| Chiffre d'affaires total | Disponible pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. Non disponible avec le détail par **Channels**. |
| Impressions uniques | Disponibles pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. |
| Destinataires uniques | Disponibles pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. Non disponible avec le détail par **Channels**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilité des indicateurs" }

### Variantes de message supprimées {#deleted-message-variants}

Les statistiques des variantes de message supprimées ne s'affichent pas lorsque vous décomposez votre rapport par Campaigns ou Canvas. Cependant, les totaux au niveau du canal incluent toutes les statistiques, que la variante ait été supprimée ou non. Par exemple, les *envois* pour l'e-mail incluent tous les envois d'e-mails, mais si vous décomposez ces statistiques par Campaign, les chiffres peuvent être inférieurs car les envois des variantes de message supprimées sont filtrés.

Dans le même rapport, les *destinataires uniques* peuvent être supérieurs aux *impressions uniques* lorsqu'une variante de message a été supprimée après l'envoi. Les *destinataires uniques* au niveau de la Campaign peuvent toujours inclure les utilisateurs qui ont reçu la variante supprimée, tandis que les *impressions uniques* omettent les statistiques des variantes supprimées dans les agrégations au niveau du message.

## Consulter un rapport {#viewing-a-report}

Après avoir exécuté votre rapport, vous pouvez consulter vos résultats sous forme de tableau sur la page du rapport.

![Un tableau des données du rapport pour les indicateurs de chaque Campaign.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Créer un graphique de rapport {#creating-a-report-chart}

En bas de la page, vous pouvez créer un graphique de vos données en sélectionnant un **Chart type** et en configurant les indicateurs du graphique. Par défaut, le premier indicateur est affiché.

![Un graphique des données du rapport avec des options pour configurer l'axe X, l'axe Y, le type de graphique, et plus encore.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Pour créer un graphique en courbes, sélectionnez **Date** comme option de détail lors de la configuration du rapport. Cela affichera les tendances au fil du temps.
{% endalert %}

#### Télécharger un graphique de rapport {#downloading-a-report-chart}

Pour télécharger une image du graphique de rapport, sélectionnez l'icône en pointillés puis choisissez une option de téléchargement.

![Un menu avec des options de téléchargement pour différents formats de fichier.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Partager un rapport {#sharing-a-report}

Vous pouvez partager un lien vers le rapport en sélectionnant **Share** et l'une de ces options :
- **Share a link :** Copiez et partagez le lien.

![Menu déroulant « Share a link » avec un lien vers le rapport.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Send or schedule an email :** Envoyez un e-mail immédiatement ou à une heure désignée contenant un lien de téléchargement qui expire après une heure. Vous pouvez sélectionner des destinataires parmi les utilisateurs de l'entreprise listés dans le menu déroulant **Email Recipients** ou saisir toute autre adresse e-mail.

![Fenêtre « Schedule an email » avec des champs pour choisir le format du rapport, les destinataires et l'heure d'envoi.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Download CSV :** Téléchargez un CSV du rapport.

## Ajouter un rapport à un tableau de bord {#adding-a-report-to-a-dashboard}

1. Sélectionnez l'icône en pointillés en haut du tableau du rapport.
2. Sélectionnez **Add to dashboard**.
3. Choisissez si vous souhaitez créer un nouveau tableau de bord ou l'ajouter à un tableau de bord existant.<br><br>![Fenêtre avec des options pour choisir si vous souhaitez ajouter le rapport à un nouveau tableau de bord ou à un tableau de bord existant.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Suivez les étapes dans [Générateur de tableaux de bord]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/) pour en savoir plus sur la création d'un tableau de bord.

## Résolution des problèmes {#troubleshooting}

### Le rapport n'affiche aucun envoi pour une Campaign ou un Canvas {#report-shows-no-sends-for-a-campaign-or-canvas}

Une Campaign ou un Canvas apparaît dans le rapport lorsque sa date de **Last sent** se situe dans la fenêtre de **Last sent** que vous avez configurée. Les **Sends** et les autres indicateurs ne se remplissent que pour l'activité comprise dans la plage de dates **Show data for**. Si le message n'a pas été envoyé pendant la période **Show data for**, la ligne peut tout de même lister la Campaign ou le Canvas avec zéro envoi.

Par exemple, supposons que **Last sent** est du 1er janvier 2025 au 14 avril 2025, de sorte qu'une Campaign est incluse, mais **Show data for** est du 1er décembre 2024 au 14 janvier 2025. Si cette Campaign n'a eu aucun envoi en décembre ou en janvier, elle apparaît tout de même dans le tableau sans indicateurs d'envoi.