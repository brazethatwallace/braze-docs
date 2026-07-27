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

> Cette page explique comment utiliser le générateur de rapports pour créer et consulter des rapports détaillés à partir des données Braze, et comment ajouter des rapports à des tableaux de bord.

La vidéo suivante offre un aperçu de la création et de la personnalisation de rapports dans le générateur de rapports.

{% multi_lang_include video.html id="oi66kwwldv" source="wistia" %}

## Utiliser un modèle de rapport {#using-a-report-template}

1. Accédez à **Analytics** > **Report Builder (New)**.
2. Sélectionnez la flèche **Plus d'options** à côté du bouton **Create New Report**, puis sélectionnez **Use a report template**.<br><br>![Menu déroulant du bouton « Create New Report » avec les options pour créer un rapport personnalisé ou utiliser un modèle.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Sélectionnez l'un des modèles de rapport dans la bibliothèque de modèles Braze.
    - Utilisez les menus déroulants **Row items** et **Tags** pour trouver les rapports pertinents pour vos cas d'usage.<br><br>![Fenêtre « Braze report templates » avec la liste des modèles Braze à sélectionner.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Suivez l'étape 3 et les suivantes dans [Créer un rapport](#creating-a-report) pour personnaliser davantage le rapport en fonction de votre cas d'usage.

## Créer un rapport {#creating-a-report}

1. Accédez à **Analytics** > **Report Builder (New)**.
2. Sélectionnez **Create New Report**.
3. Dans le menu déroulant **Rows**, sélectionnez ce sur quoi vous souhaitez créer un rapport :
    - Campaigns
    - Canvas
    - Campaigns et Canvas
    - Canaux
    - Tags

    Notez que votre sélection dans **Rows** aura un impact sur [les indicateurs que vous pouvez consulter](#metrics-availability). Par exemple, vous pouvez afficher les indicateurs multivariantes uniquement si vous créez un rapport sur les **Canvas**, ou les **Campaigns** avec un détail par **Variant**. Vous ne pouvez pas afficher ces indicateurs lorsque vous créez un rapport sur **Campaigns and Canvases**, même si ces Campaigns et Canvas comportent des tests multivariantes.

![La section « Rows and columns » avec des champs pour sélectionner les lignes et les regroupements de votre rapport.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (Facultatif) Sélectionnez **Add drilldown** pour décomposer vos données en vues plus granulaires :
    - Canaux
    - Date
        - Utilisez cette option pour diviser vos données en plages temporelles plus petites. Par exemple, si vous souhaitez savoir comment vos Campaigns ont performé par jour, sélectionnez la configuration suivante :
            - **Rows** : Campaigns
            - **Grouping :** Date
            - **Interval :** Days
    - Variantes
    - Campaigns et Canvas

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
    - **Ajouter manuellement :** Choisissez chaque Campaign ou Canvas à inclure dans le rapport en utilisant les filtres pour les dates de **Last Sent** et les tags ou canaux, ou en recherchant le nom de la Campaign ou du Canvas.<br><br>![La section « Manually add campaigns and canvases » avec une liste de Campaigns à sélectionner.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Ajouter automatiquement :** Définissez des règles pour déterminer quelles Campaigns ou quels Canvas inclure dans le rapport. Vous n'êtes tenu de sélectionner qu'un seul champ sur cette page.
        - Notez qu'à mesure que des Campaigns ou des Canvas supplémentaires remplissent les conditions que vous avez définies sur cet écran, ils sont automatiquement ajoutés aux exécutions futures de votre rapport.
        - Les bannières ne sont pas une option dans le menu déroulant **Channel**, vous ne pouvez donc pas utiliser les règles de canal pour ajouter automatiquement des Campaigns ou des Canvas de type bannière. Vous pouvez toutefois inclure les KPI des bannières dans les indicateurs de votre rapport.<br><br>![La section « Automatically add campaigns and canvases » avec des champs pour définir les règles déterminant quelles Campaigns et quels Canvas doivent être ajoutés au rapport.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. Exécutez le rapport en sélectionnant **Save & Run**.

{% alert note %}
L'exécution du rapport peut prendre quelques minutes, en fonction de la plage de dates et du nombre de Campaigns ou de Canvas que vous avez sélectionnés lors de la configuration.
{% endalert %}

## Disponibilité des indicateurs {#metrics-availability}

Votre sélection pour **Lignes** affecte les indicateurs que vous pouvez sélectionner.

{% alert tip %}
Si vous souhaitez créer un rapport sur les variantes ou les étapes d'un Canvas, sélectionnez **Canvas** pour les lignes et laissez le champ vide ou sélectionnez **Date** comme ventilation. Cela crée un menu déroulant **Vue Canvas** pour afficher les indicateurs du Canvas uniquement, ou regrouper les indicateurs par variante, étape ou message.<br><br> Lorsque vous regroupez par étape, le tableau de prévisualisation lors de la configuration de votre rapport affiche un maximum de 50 lignes. Exécutez le rapport ou exportez-le au format CSV pour afficher toutes les lignes.

![Le menu déroulant « Vue Canvas » ouvert.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Indicateur | Description |
| --- | --- |
| Indicateurs de conversion | Disponible pour Campaigns, Canvas, Campaigns et Canvas. |
| Entrées | Disponible pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. |
| Date du dernier envoi | Disponible pour Campaigns, Canvas, Campaigns et Canvas. S'affiche uniquement pour les campagnes planifiées — ne se remplit pas pour les campagnes déclenchées par une action ou par l'API. |
| Envois | Disponible pour chaque canal pertinent. |
| Messages envoyés | Disponible pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. |
| Ligne d'objet | Disponible pour les Campaigns d'e-mail avec la ventilation **Variante**, les Canvas et les Canvas avec la ventilation **Variante**. |
| Chiffre d'affaires total | Disponible pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. Non disponible avec la ventilation **Canaux**. |
| Impressions uniques | Disponible pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. |
| Destinataires uniques | Disponible pour Campaigns, Canvas, Campaigns et Canvas, étiquettes. Non disponible avec la ventilation **Canaux**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilité des indicateurs" }

### Variantes de message supprimées {#deleted-message-variants}

Les statistiques des variantes de message supprimées ne s'affichent pas lorsque vous ventilez votre rapport par campagnes ou Canvas. Cependant, les totaux au niveau du canal incluent toutes les statistiques, que la variante ait été supprimée ou non. Par exemple, les _Envois_ pour l'e-mail incluent tous les envois d'e-mails, mais si vous ventilez ces statistiques par campagne, les chiffres peuvent être inférieurs car les envois des variantes de message supprimées sont filtrés.

Dans le même rapport, les _Destinataires uniques_ peuvent être supérieurs aux _Impressions uniques_ lorsqu'une variante de message a été supprimée après l'envoi. Les _Destinataires uniques_ au niveau de la campagne peuvent toujours inclure les utilisateurs qui ont reçu la variante supprimée, tandis que les _Impressions uniques_ omettent les statistiques des variantes supprimées dans les agrégations au niveau du message.

## Consulter un rapport {#viewing-a-report}

Après avoir exécuté votre rapport, vous pouvez consulter vos résultats sous forme de tableau sur la page du rapport.

![Un tableau des données du rapport pour les indicateurs de chaque campagne.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Créer un graphique de rapport {#creating-a-report-chart}

En bas de la page, vous pouvez créer un graphique de vos données en sélectionnant un **Type de graphique** et en configurant les indicateurs du graphique. Par défaut, vous verrez le premier indicateur.

![Un graphique des données du rapport avec des options pour configurer l'axe x, l'axe y, le type de graphique, et plus encore.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Pour créer un graphique linéaire, sélectionnez **Date** comme option de ventilation lors de la configuration du rapport. Cela affichera les tendances au fil du temps.
{% endalert %}

#### Télécharger un graphique de rapport {#downloading-a-report-chart}

Pour télécharger une image du graphique de rapport, sélectionnez l'icône en pointillés puis choisissez une option de téléchargement.

![Un menu avec des options de téléchargement pour différents formats de fichiers.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Partager un rapport {#sharing-a-report}

Vous pouvez partager un lien vers le tableau de bord du rapport en sélectionnant **Partager** et l'une de ces options :
- **Partager un lien :** Copiez et partagez le lien.
- **Envoyer ou planifier un e-mail :** Envoyez un e-mail immédiatement ou à un moment défini, contenant un lien de téléchargement qui expire au bout d'une heure. Vous pouvez sélectionner des destinataires parmi les utilisateurs de l'entreprise répertoriés dans le menu déroulant **Email Recipients** ou saisir toute autre adresse e-mail.

{% alert note %}
Le menu déroulant **Email Recipients** répertorie uniquement les utilisateurs Braze de l'entreprise et enregistre leurs adresses e-mail pour les planifications de rapports. Les adresses e-mail externes doivent être saisies manuellement chaque fois que vous créez une nouvelle planification de rapport. Si vous envoyez fréquemment des rapports à des destinataires externes, comme un contact partenaire, envisagez de les ajouter en tant qu'utilisateur de l'entreprise avec les autorisations appropriées afin que leur adresse apparaisse dans le menu déroulant.
{% endalert %}

![Fenêtre « Planifier un e-mail » avec des champs pour choisir le format du rapport, les destinataires et l'heure d'envoi.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Télécharger le CSV :** Téléchargez un CSV du rapport.

## Ajout d'un rapport à un tableau de bord {#adding-a-report-to-a-dashboard}

1. Sélectionnez l'icône en pointillés en haut du tableau du rapport.
2. Sélectionnez **Ajouter au tableau de bord**.
3. Choisissez si vous souhaitez créer un nouveau tableau de bord ou l'ajouter à un tableau de bord existant.<br><br>![Fenêtre avec les options pour choisir d'ajouter le rapport à un nouveau tableau de bord ou à un tableau de bord existant.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Suivez les étapes décrites dans le [Générateur de tableaux de bord]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder) pour en savoir plus sur la création d'un tableau de bord.

## Résolution des problèmes {#troubleshooting}

### Le rapport n'affiche aucun envoi pour une campagne ou un Canvas {#report-shows-no-sends-for-a-campaign-or-canvas}

Une campagne ou un Canvas apparaît dans le rapport lorsque sa date de **Dernier envoi** se situe dans la fenêtre **Dernier envoi** que vous avez configurée. Les **envois** et les autres indicateurs ne sont renseignés que pour l'activité comprise dans la plage de dates **Afficher les données pour**. Si le message n'a pas été envoyé pendant la période **Afficher les données pour**, la ligne peut tout de même afficher la campagne ou le Canvas avec zéro envoi.

Par exemple, supposons que **Dernier envoi** soit défini du 1er janvier 2025 au 14 avril 2025, de sorte qu'une campagne est incluse, mais que **Afficher les données pour** couvre la période du 1er décembre 2024 au 14 janvier 2025. Si cette campagne n'a eu aucun envoi en décembre ou en janvier, elle apparaît tout de même dans le tableau sans indicateur d'envoi.

### Le lien de téléchargement a expiré {#download-link-has-expired}

Les liens de téléchargement de rapports expirent au bout d'une heure. Si votre lien a expiré, générez un nouveau rapport et téléchargez-le dans l'heure. Il n'est pas possible de prolonger le délai d'expiration.

Si vous avez un [compartiment Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3) connecté dans **Intégrations partenaires**, vous pouvez éventuellement récupérer les données de rapports plus anciens en parcourant directement votre compartiment S3.