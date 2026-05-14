---
nav_title: VWO
article_title: Intégrer VWO à Braze
description: "Découvrez comment intégrer VWO à Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) est une plateforme d'expérimentation puissante qui aide les marques à améliorer les indicateurs clés de l'entreprise en permettant aux équipes d'exécuter des programmes d'optimisation des conversions étayés par les données comportementales des clients. Avec VWO, vous pouvez unifier les données clients, obtenir des informations comportementales, créer des hypothèses, effectuer des tests A/B sur plusieurs plateformes (serveur, web et mobile), déployer des fonctionnalités, personnaliser les expériences et optimiser l'ensemble du parcours client.

En intégrant VWO à Braze, vous pouvez exploiter les données d'expérience de VWO pour créer des segments ciblés et proposer des campagnes personnalisées.

## Conditions préalables {#prerequisites}

| Condition | Description |
|-----------------|-------------|
| Compte VWO | Un compte VWO avec accès aux données d'expérimentation. |
| Compte Braze | Un compte Braze actif avec l'intégration du [SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) sur votre page web. Vous devez également activer la segmentation des propriétés d'événement. Pour en faire la demande, reportez-vous à la rubrique [Considérations](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de VWO avec Braze {#integrating-vwo-with-braze}

### Étape 1 : Activer l'intégration de Braze dans VWO {#step-1-enable-the-braze-integration-in-vwo}

1. Connectez-vous à votre compte VWO.
2. Dans le tableau de bord de VWO, allez dans **Configurations > Integrations**. Ici, vous pouvez activer les intégrations au niveau de l'espace de travail, ce qui applique par défaut l'intégration à toutes les futures campagnes de test.

   ![Configuration de l'intégration VWO]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Sélectionnez l'intégration de Braze pour l'activer.
5. En option, vous pouvez activer l'intégration de Braze pour toutes les campagnes existantes. Pour ce faire, sélectionnez une campagne, puis allez dans **Configuration > Integrations**, et activez Braze.

   ![Activer l'intégration de Braze]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Une fois que vous avez activé l'intégration, VWO commencera à envoyer des données d'expérience à Braze au niveau de la campagne.

### Étape 2 : Créer un segment dans Braze avec les propriétés d'événement de VWO {#step-2-create-a-segment-in-braze-with-vwo-event-properties}

1. Dans le tableau de bord de Braze, sélectionnez **Segments** > **+ Create Segment**.
3. Dans la fenêtre **Create Segment**, saisissez un nom pour le segment, puis sélectionnez **Create Segment**.
4. Dans votre segment nouvellement créé, sélectionnez **Filters** > **Add Filter**, puis choisissez **Custom Event** comme type de filtre.
6. Dans le menu déroulant du filtre, recherchez **VWO**.
7. Sélectionnez la propriété VWO concernée et indiquez la valeur requise.
8. Si nécessaire, configurez le nombre de visites et la période de temps. Lorsque vous avez terminé, sélectionnez **Save**.

   ![Création de segments dans Braze]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Pour afficher le nombre d'utilisateurs correspondant à vos critères de segmentation, sélectionnez **Calculate Exact Statistics**.

   ![Statistiques du segment Braze]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Flux de données {#data-flow}

VWO envoie les données d'expérience de la campagne à Braze sous la forme d'un événement personnalisé au format suivant :

- **Nom de l'événement :** VWO
- **Propriétés d'événement :** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Ces propriétés d'événements personnalisés peuvent également être utilisées à des fins de segmentation et de ciblage.
{% endalert %}

## Considérations {#considerations}

### Demander la segmentation des propriétés d'événement {#request-event-property-segmentation}

Avant de pouvoir utiliser la segmentation des propriétés d'événement, vous devez l'activer dans Braze. Utilisez le modèle suivant pour contacter votre gestionnaire de la satisfaction client Braze ou l'équipe d'assistance pour obtenir l'accès.

   <table aria-label="Demander la segmentation des propriétés d'événement">
     <caption>Demander la segmentation des propriétés d'événement</caption>
   <thead>
      <tr>
         <th>Champ</th>
         <th>Détails</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Objet</strong></td>
         <td>Demande d'activation de la segmentation des propriétés d'événement pour l'intégration de VWO</td>
      </tr>
      <tr>
         <td><strong>Corps</strong></td>
         <td>
         Bonjour l'équipe Braze,<br><br>
         Nous aimerions activer la segmentation des propriétés d'événement pour les événements envoyés depuis notre intégration VWO&lt;&gt;Braze. Voici les détails :<br><br>
         - <strong>Nom de l'événement :</strong> VWO<br>
         - <strong>Propriétés d'événement :</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Veuillez confirmer une fois que les propriétés ont été activées dans notre compte.<br><br>
         Merci.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Demander la segmentation des propriétés d'événement" }

### Points de données Braze {#braze-data-points}

L'événement personnalisé envoyé par VWO à Braze&#8212;y compris toutes les propriétés d'événement activées pour la segmentation&#8212;enregistrera des points de données dans votre instance Braze.

### Remarques

Actuellement, cette intégration ne prend pas en charge la synchronisation en temps réel des données de test. Il peut s'écouler jusqu'à 15 minutes avant que les données de test n'apparaissent dans Braze.

## Résolution des problèmes {#troubleshooting}

Si vous ne voyez pas les données VWO dans Braze :

1. Faites un clic droit sur la page où se déroule votre campagne de test et sélectionnez **Inspect Element**.
2. Sous l'onglet **Network**, recherchez **Braze** pour filtrer les appels réseau vers Braze.
3. Les appels réseau se remplissent au fur et à mesure du chargement de la page. Vous pouvez recharger la page pour voir les appels réseau.
4. Sélectionnez un appel réseau pour en savoir plus.
5. Allez dans la section **Request Payload** de l'onglet **Payload**, où vous trouverez events: contenant name: **ce**, indiquant un événement personnalisé (Custom Event).
6. Développez 0: et data: pour voir n: "VWO" (nom de l'événement personnalisé) et p: {vwo_campaign_name: "<nom de votre campagne VWO>", vwo_variation_name: "<nom de la variante>"}. Cela indique que les valeurs sont bien transmises par VWO à Braze.

 ![Résolution des problèmes Braze]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Pour obtenir une assistance supplémentaire, contactez votre gestionnaire de la satisfaction client VWO.