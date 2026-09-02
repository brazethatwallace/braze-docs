---
nav_title: Kameleoon
article_title: Kameleoon
description: "Découvrez comment intégrer Kameleoon à Braze"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) est une solution d'optimisation offrant des fonctionnalités d'expérimentation, de personnalisation par l'intelligence artificielle et de gestion des fonctionnalités au sein d'une plateforme unifiée.

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Exigence | Description |
| --- | --- |
| Compte Kameleoon | Un compte Kameleoon est nécessaire pour bénéficier de ce partenariat. |
| Compte Braze | Un compte Braze actif avec le [SDK Web Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) intégré sur votre page web. Vous devrez également activer la segmentation des propriétés d'événement. Pour en faire la demande, consultez la section [Considérations](#considerations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Kameleoon envoie des événements personnalisés à Braze pour identifier les utilisateurs participant à des campagnes d'expérimentation et de personnalisation, ce qui permet un ciblage plus précis et un envoi de messages personnalisés.

## Intégration de Kameleoon {#integrating-kameleoon}

Cette intégration fonctionne comme un tracker JavaScript via le fichier engine.js de Kameleoon. Elle peut être activée rapidement depuis la plateforme Kameleoon.

### Étape 1 : Accéder à la page Intégrations de Kameleoon {#step-1-go-to-the-kameleoon-integrations-page}

Dans votre application Kameleoon, sélectionnez **Admin** puis **Integrations** dans la barre latérale.

![Le panneau d'administration de la plateforme Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Étape 2 : Installer l'outil Braze {#step-2-install-the-braze-tool}

Par défaut, l'outil Braze n'est pas installé. Recherchez l'icône Braze, puis sélectionnez **Install the tool**. ![Un carré gris avec une flèche pointant vers le bas.]({% image_buster /assets/img/kameleoon/img_2.png %})

Sélectionnez les projets pour lesquels vous souhaitez activer l'outil Braze, afin que les données de Kameleoon soient correctement transmises à Braze.

![L'icône de l'outil Braze dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Après avoir configuré l'outil, sélectionnez **Validate**, ce qui fermera le panneau de configuration. Vous verrez alors un basculeur **ON** à côté de l'icône de l'outil Braze, indiquant le nombre de projets sur lesquels l'outil est configuré.

![L'outil Braze activé sur « On » dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}
Cette fonctionnalité est en version bêta. Rejoignez le [programme bêta de Kameleoon](https://help.kameleoon.com/account-and-team-management/join-beta-program/) pour commencer à utiliser cette intégration.
{% endalert %}

### Étape 3 : Associer Braze aux campagnes Kameleoon {#step-3-associate-braze-with-kameleoon-campaigns}

#### Dans l'éditeur graphique/de code {#in-the-graphiccode-editor}

Pour finaliser votre expérience, sélectionnez l'étape **Integrations** pour configurer Braze comme outil de suivi, puis sélectionnez **Braze**.

![Le tableau de bord des intégrations dans Kameleoon montrant toutes les intégrations disponibles, y compris l'intégration active Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze sera mentionné dans le résumé avant la mise en production. Kameleoon transmettra automatiquement les données à Braze, et vous pourrez les utiliser pour l'analyse et la segmentation directement dans Braze.

##### Création de personnalisation {#personalization-creation}

Sur la page **Personalization Creation**, vous pouvez sélectionner Braze parmi les outils de reporting pour personnaliser vos rapports.

![La section Outils de reporting montre des intégrations telles que Heap, Mixpanel, Clarity, avec Braze sélectionné.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Création d'un indicateur de fonctionnalité {#feature-flag-creation}

Configurez l'intégration dans l'environnement de l'indicateur de fonctionnalité dans la section **Integrations**. Activez-la pour les environnements dans lesquels vous souhaitez qu'elle soit active.

![La page de l'indicateur de fonctionnalité dans Kameleoon avec les intégrations disponibles. Il existe deux commutateurs pour chaque partenaire, « Delivery rules » et « Feature experiments ».]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Page des résultats {#results-page}

Une fois que Braze est défini comme outil de reporting pour une expérience, vous pouvez le sélectionner (ou le désélectionner) sur la page des résultats de Kameleoon dans le menu **Experiment configuration**.

{% alert note %}
Cette intégration nécessite une [mise en œuvre hybride](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) et n'est compatible qu'avec les SDK web.
{% endalert %}

![Le panneau latéral de la page des résultats dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Les outils de reporting associés à l'expérience s'affichent. Sélectionnez **Edit** pour modifier cette sélection.

### Étape 4 : Analyser et exploiter vos données Kameleoon dans Braze {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

Une fois l'intégration mise en place, Kameleoon enverra à Braze des événements personnalisés appelés `kameleoon_exposure` avec des propriétés telles que le **nom de l'expérience**, l'**ID de l'expérience**, le **nom de la variation** et l'**ID de la variation**.

![Le journal des événements utilisateurs personnalisés dans Braze, montrant un exemple de payload de l'événement reçu par Braze depuis Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

Vous pouvez ensuite consulter ces données dans les événements personnalisés, créer des rapports d'événements personnalisés pour identifier l'exposition aux campagnes Kameleoon et activer la segmentation en fonction des propriétés d'événement. Vous pouvez utiliser des événements personnalisés lors de la création de Campaigns et de Canvas ultérieurs ou liés par le biais de [Parcours d'actions]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), de [déclencheurs basés sur des actions]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) ou de la création de [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).

En outre, ces événements seront accessibles via les [objets d'événements personnalisés de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/), ce qui permettra d'établir des rapports et des analyses complets.

## Considérations {#considerations}

### Demander la segmentation des propriétés d'événement {#request-event-property-segmentation}

Avant de pouvoir utiliser la segmentation des propriétés d'événement, vous devez l'activer dans Braze. Utilisez le modèle suivant pour contacter votre CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients Braze ou l'équipe d'assistance afin d'obtenir l'accès.

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
         <td>Demande d'activation de la segmentation des propriétés d'événement pour l'intégration Kameleoon</td>
      </tr>
      <tr>
         <td><strong>Corps</strong></td>
         <td>
         Bonjour l'équipe Braze,<br><br>
         Nous souhaitons activer la segmentation des propriétés d'événement pour les événements envoyés depuis notre intégration Kameleoon&lt;&gt;Braze. Voici les détails :<br><br>
         - <strong>Nom de l'événement :</strong> Kameleoon<br>
         - <strong>Propriétés d'événement :</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Veuillez confirmer une fois que les propriétés ont été activées dans notre compte.<br><br>
         Merci.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Demander la segmentation des propriétés d'événement" }

### Points de données Braze {#braze-data-points}

L'événement personnalisé envoyé par Kameleoon à Braze&#8212;y compris toutes les propriétés d'événement activées pour la segmentation&#8212;enregistrera des points de données dans votre instance Braze.