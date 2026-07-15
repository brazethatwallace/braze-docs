---
nav_title: Exporter les données de campagne
article_title: Exporter les données de campagne
page_order: 2
page_type: reference
description: "Cet article de référence explique comment exporter les données de résultats de campagnes uniques, multicanales ou multivariées. L'article indique également comment exporter les données utilisateur des destinataires."
tool:
  - Campaigns
  - Reports

---

# Exporter les données de campagne {#export-campaign-data}

> Depuis la page **Campaigns** du tableau de bord, sélectionnez la campagne que vous souhaitez consulter et faites défiler vers le bas jusqu'aux graphiques de performances historiques, qui peuvent être exportés.<br><br>Cette page explique comment exporter les données de résultats de campagnes uniques, multicanales et multivariées, et comment exporter les données utilisateur des destinataires.

## Campagnes multicanales {#multichannel-campaigns}

Pour les campagnes multicanales, les données exportables dépendent des canaux de communication utilisés. Voici la liste complète des données pouvant être exportées à partir d'une campagne utilisant les notifications push iOS, les notifications push Android, l'e-mail et les messages in-app :

- Messages envoyés par date
    - Total des messages envoyés
    - Messages envoyés via les canaux de la campagne (peut inclure les notifications push, les e-mails et les messages in-app)
- Engagement par e-mail par date
    - Nombre d'e-mails livrés
    - Nombre d'e-mails envoyés
    - Nombre d'e-mails ouverts
    - Nombre de clics sur les e-mails
    - Nombre de rebonds d'e-mails
    - Nombre d'e-mails signalés comme courrier indésirable
- Engagement sur les messages in-app par date
    - Nombre de messages in-app envoyés
    - Impressions des messages in-app
    - Nombre de clics sur les messages in-app
- Engagement des notifications push iOS par date
    - Nombre de notifications push iOS envoyées
    - Nombre total d'ouvertures
    - Ouvertures directes
    - Rebonds
- Engagement des notifications push Android par date
    - Nombre de notifications push Android envoyées
    - Nombre total d'ouvertures
    - Ouvertures directes
    - Rebonds

## Campagnes multivariées {#multivariate-campaigns}

Pour les campagnes multivariées, qui n'utilisent qu'un seul canal de communication, vous pouvez exporter des données montrant les performances de chaque variante sur l'analytique du canal concerné au fil du temps. Ces données peuvent être affichées groupées par statistique ou par variante de message.

Les résultats de campagne de notifications push contiennent des graphiques pour les analyses suivantes :

- Messages envoyés par date pour chaque variante
- Conversions par date pour chaque variante
- Destinataires uniques par date pour chaque variante
- Ouvertures par date pour chaque variante
- Ouvertures directes par date pour chaque variante
- Rebonds par date pour chaque variante

Les résultats de campagne d'e-mail contiennent des graphiques pour les analyses suivantes :

- Nombre livrés par date pour chaque variante
- Nombre envoyés par date pour chaque variante
- Ouvertures par date pour chaque variante
- Clics par date pour chaque variante
- Rebonds par date pour chaque variante
- Signalements de courrier indésirable par date pour chaque variante

Les résultats de campagne de messages in-app contiennent des graphiques pour les analyses suivantes :

- Envoyés par date pour chaque variante
- Impressions par date pour chaque variante
- Clics par date pour chaque variante

## Destinataires de la campagne {#campaign-recipients}

Vous pouvez exporter les données utilisateur de tous les destinataires d'une campagne sous forme de fichier CSV. Pour ce faire, sélectionnez le bouton **User Data** dans la section **Campaign Details**.

{% alert note %}
Le bouton **User Data** n'apparaît pas ? Pour exporter les données utilisateur, vous avez besoin des [autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#limited-and-team-role-permissions) **Export User Data** pour cet espace de travail.
{% endalert %}

![Menu déroulant User Data sur la page Campaign Details]({% image_buster /assets/img/campaign_export_example.png %})

Le fichier CSV généré contient les données de profil utilisateur de chaque destinataire de la campagne. Braze génère le rapport en arrière-plan et l'envoie par e-mail à l'utilisateur actuellement connecté.

Si vous avez lié vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) à Braze, le fichier CSV sera également téléchargé dans votre compartiment S3. Sinon, le lien envoyé par e-mail expirera au bout de quelques heures.

Le fichier exporté comprend les mêmes champs de données utilisateur que ceux inclus lorsque vous [exportez les données utilisateur d'un segment]({{site.baseurl}}/user_guide/analytics/dashboards/home#exporting-app-usage-data). En plus de ces champs, si vous choisissez « Export All Recipient Data », le fichier exporté contiendra également les données suivantes pour chaque utilisateur :

- Nom de la variante de campagne reçue
- ID de l'API de la variante de campagne reçue
- Si l'utilisateur fait partie du groupe de contrôle

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la [résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}