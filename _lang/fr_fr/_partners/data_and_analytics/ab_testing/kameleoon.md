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

## Prérequis {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Condition | Description |
| --- | --- |
| Compte Kameleoon | Un compte Kameleoon est nécessaire pour tirer parti de ce partenariat. |
| Compte Braze | Un compte Braze actif avec le [SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) intégré sur votre page web. Vous devrez également activer la segmentation par propriétés d'événement. Pour en faire la demande, consultez la section [Considérations](#considerations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Cas d'usage {#use-cases}

Kameleoon envoie des événements personnalisés à Braze pour identifier les utilisateurs participant à des expériences et des campagnes de personnalisation, permettant un ciblage plus précis et une communication personnalisée.

## Intégration de Kameleoon {#integrating-kameleoon}

Cette intégration fonctionne en tant que traqueur JavaScript via le fichier engine.js de Kameleoon. Elle peut être activée depuis la plateforme Kameleoon.

### Étape 1 : Accéder à la page des intégrations Kameleoon {#step-1-go-to-the-kameleoon-integrations-page}

Dans votre application Kameleoon, sélectionnez **Admin** puis **Integrations** dans la barre latérale.

![Le panneau Admin dans la plateforme Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Étape 2 : Installer l'outil Braze {#step-2-install-the-braze-tool}

Par défaut, l'outil Braze n'est pas installé. Recherchez l'icône Braze, puis sélectionnez **Install the tool**. ![Un carré gris avec une flèche pointant vers le bas.]({% image_buster /assets/img/kameleoon/img_2.png %})

Sélectionnez les projets pour lesquels vous souhaitez activer l'outil Braze, afin que les données Kameleoon soient correctement transmises à Braze.

![L'icône de l'outil Braze dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Après avoir configuré l'outil, sélectionnez **Validate**, ce qui ferme le panneau de configuration. Un bouton bascule **ON** apparaît à côté de l'icône de l'outil Braze, indiquant le nombre de projets sur lesquels l'outil est configuré.

![L'outil Braze activé dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

### Étape 3 : Associer Braze aux Campaigns Kameleoon {#step-3-associate-braze-with-kameleoon-campaigns}

#### Dans l'éditeur graphique/code {#in-the-graphiccode-editor}

Pour compléter votre expérience, sélectionnez l'étape **Integrations** pour configurer Braze en tant qu'outil de suivi, puis sélectionnez **Braze**.

![Le tableau de bord des intégrations dans Kameleoon affichant toutes les intégrations disponibles, y compris l'intégration active Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze est mentionné dans le récapitulatif avant la mise en ligne. Kameleoon transmet automatiquement les données à Braze, et vous pouvez les utiliser pour l'analyse et la segmentation directement dans Braze.

##### Création de personnalisation {#personalization-creation}

Sur la page **Personalization Creation**, vous pouvez sélectionner Braze parmi les outils de reporting pour personnaliser vos rapports.

![Section des outils de reporting affichant des intégrations telles que Heap, Mixpanel, Clarity, avec Braze sélectionné.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Création de feature flag {#feature-flag-creation}

Configurez l'intégration dans l'environnement de feature flag dans la section **Integrations**. Activez-la pour les environnements où vous souhaitez qu'elle soit active.

![La page Feature Flag dans Kameleoon avec les intégrations disponibles. Il y a deux interrupteurs pour chaque partenaire, « Delivery rules » et « Feature experiments ».]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Page des résultats {#results-page}

Une fois que Braze est défini comme outil de reporting pour une expérience, vous pouvez le sélectionner (ou le désélectionner) sur la page des résultats de Kameleoon dans le menu **Experiment configuration**.

{% alert note %}
Cette intégration nécessite une [implémentation hybride](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) et n'est compatible qu'avec les SDK web.
{% endalert %}

![Le panneau latéral de la page des résultats dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Les outils de reporting associés à l'expérience apparaissent. Sélectionnez **Edit** pour modifier cette sélection.

### Étape 4 : Analyser et exploiter vos données Kameleoon dans Braze {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

Une fois l'intégration configurée, Kameleoon envoie des événements personnalisés appelés `kameleoon_exposure` avec des propriétés telles que **Experiment name**, **Experiment ID**, **Variation name**, **Variation ID** à Braze.

![Le journal des événements utilisateurs personnalisés dans Braze, montrant un exemple de payload de l'événement reçu par Braze depuis Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

Vous pouvez ensuite consulter ces données dans les événements personnalisés, créer des rapports d'événements personnalisés pour identifier l'exposition aux Campaigns Kameleoon, et activer la segmentation basée sur les propriétés d'événement. Vous pouvez utiliser les événements personnalisés lors de la création de Campaigns ou de Canvas ultérieurs ou liés via les [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-groups), les [déclencheurs basés sur des actions]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) ou la création de [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

De plus, ces événements sont accessibles via les [objets d'événements personnalisés Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) pour permettre des rapports et des analyses complets.

## Considérations {#considerations}

### Demande de segmentation par propriétés d'événement {#request-event-property-segmentation}

Avant de pouvoir utiliser la segmentation par propriétés d'événement, vous devrez la faire activer dans Braze. Utilisez le modèle suivant pour contacter votre CSM Braze ou l'équipe d'assistance afin d'obtenir l'accès.

   <table aria-label="Demande de segmentation par propriétés d'événement">
     <caption>Demande de segmentation par propriétés d'événement</caption>
   <thead>
      <tr>
         <th>Champ</th>
         <th>Détails</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Objet</strong></td>
         <td>Request to Enable Event Property Segmentation for Kameleoon Integration</td>
      </tr>
      <tr>
         <td><strong>Corps</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our Kameleoon&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> Kameleoon<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Demande de segmentation par propriétés d'événement" }

### Points de donnée Braze {#braze-data-points}

L'événement personnalisé envoyé de Kameleoon à Braze&#8212;y compris les propriétés d'événement activées pour la segmentation&#8212;consommera des points de donnée dans votre instance Braze.