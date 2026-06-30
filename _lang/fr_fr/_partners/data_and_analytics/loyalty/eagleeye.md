---
nav_title: Eagle Eye
article_title: Eagle Eye
description: Découvrez comment intégrer Eagle Eye à Braze.
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> [Eagle Eye](https://eagleeye.com/) est une société leader dans le domaine des technologies SaaS et de l'intelligence artificielle permettant aux marques de retail, de voyage et d'hôtellerie de gagner la fidélité de leurs clients finaux en alimentant leurs activités de marketing consommateur en temps réel, omnicanales et personnalisées, à grande échelle.

_Cette intégration est maintenue par Eagle Eye._

## Aperçu {#overview}

Eagle Eye Connect est une intégration bidirectionnelle entre Braze et AIR qui permet aux marques d'activer les données de fidélisation et de promotion directement dans Braze. Les clients peuvent attribuer des récompenses dans AIR aux consommateurs qui entrent dans une audience dans AIR. Les marketeurs peuvent ainsi personnaliser l'engagement client à l'aide de données en temps réel telles que les soldes de points, les promotions et les activités de récompense.

## Cas d'utilisation {#use-cases}

- Déclenchez des Campaigns Braze en fonction d'événements de fidélisation tels que des seuils de points ou des récompenses obtenues.
- Enrichissez les profils utilisateurs de Braze avec des données de fidélisation en temps réel pour permettre un ciblage plus personnalisé.
- Suivez et rendez compte de l'efficacité des Campaigns liées à l'échange de récompenses.
- Attribuez des récompenses dans AIR lorsque les utilisateurs participent à des Campaigns dans Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
|--------------------------|-------------|
| Compte AIR Eagle Eye | Vous devez disposer d'un compte AIR Eagle Eye actif pour bénéficier de ce partenariat. Pour commencer, contactez l'équipe des partenariats d'Eagle Eye à [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com). |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br>Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres > Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Sortant et entrant {#outbound-vs-inbound}

Les tableaux suivants présentent les deux types d'intégrations pris en charge entre Braze et Eagle Eye AIR. Eagle Eye Connect est le logiciel intermédiaire qui permet l'échange de données entre AIR et des systèmes partenaires comme Braze. Pour en savoir plus, consultez la [documentation Braze d'Eagle Eye](https://developer.eagleeye.com/docs/braze).

{% tabs local %}
{% tab sortant %}
<table aria-label="Sortant et entrant">
  <caption>Sortant et entrant</caption>
  <thead>
    <tr>
      <th>Direction</th>
      <th>Initiée par</th>
      <th>Flux de données</th>
      <th>Objectif</th>
      <th>Exemple</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>Vers l'API Braze</td>
      <td>
        Envoyez les données de fidélisation dans les profils utilisateurs de Braze sous forme d'attributs personnalisés via des événements personnalisés. Au sein de Braze, les données ingérées peuvent être utilisées pour :
        <ul>
          <li>segmenter les utilisateurs, déclencher des Campaigns</li>
          <li>personnaliser les messages</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Envoi de points de fidélité ou de statut de palier dans Braze (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>Mise à jour du profil d'un utilisateur lorsqu'il reçoit ou échange un coupon.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Sortant et entrant" }
{% endtab %}

{% tab entrant %}
<table aria-label="Sortant et entrant">
  <caption>Sortant et entrant</caption>
  <thead>
    <tr>
      <th>Direction</th>
      <th>Initiée par</th>
      <th>Flux de données</th>
      <th>Objectif</th>
      <th>Exemple</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Vers l'API Eagle Eye via webhook</td>
      <td>
        Lorsqu'un consommateur entre dans une audience dans Braze, quelle que soit la source, Braze peut déclencher un webhook vers EE Connect, ce qui permet à EE d'émettre une récompense (coupon ou points).<br><br>
        Une fois l'action terminée dans AIR, Braze reçoit un événement sortant d'AIR.
      </td>
      <td>
        <ul>
          <li>Des récompenses (coupons ou points) sont attribuées à un consommateur qui adhère au programme de fidélisation.</li>
          <li>Des récompenses sont attribuées à un consommateur ayant subi une livraison tardive.</li>
          <li>Récompenses d'anniversaire</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Sortant et entrant" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour en savoir plus sur les données personnalisées que vous pouvez envoyer à Braze en tant qu'attributs ou événements personnalisés, consultez la [documentation Braze d'Eagle Eye](https://developer.eagleeye.com/docs/braze#data-model).
{% endalert %}

## Aperçu de l'intégration {#integration-overview}

Actuellement, les connecteurs entrants et sortants ne peuvent être mis en place que via l'API avec l'aide directe de l'équipe Eagle Eye. Toutefois, une option en libre-service dans le tableau de bord AIR est en cours de développement !

En travaillant avec votre équipe Eagle Eye, vous accomplirez les étapes suivantes :

### Étape 1 : Fournir les détails de configuration {#step-1-provide-configuration-details}

Tout d'abord, vous fournirez les informations suivantes à votre équipe Eagle Eye :

| Vous fournissez | Description |
|------------------------|-------------|
| Identifiants de l'API Braze | Partagez votre endpoint REST Braze, votre identifiant d'application et votre clé API en toute sécurité avec votre contact Eagle Eye. |
| Correspondance des identifiants | Déterminez et partagez l'identifiant principal de l'utilisateur pour les mises à jour de profil, commun à AIR et Braze, tel que l'ID externe ou l'e-mail. |
| Clé d'authentification | Déterminez et partagez une clé d'authentification secrète pour chaque connecteur entrant et sortant. |
| Code devise | Partagez le code devise à 3 caractères pour l'affichage des montants d'achat monétaires (par ex., USD). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1 : Fournir les détails de configuration" }

### Étape 2 : Configurer Eagle Eye Connect {#step-2-configure-eagle-eye-connect}

Votre équipe Eagle Eye configurera Eagle Eye Connect en utilisant les détails que vous avez fournis, ainsi que les identifiants uniques de l'API AIR et les événements sortants pour les connecteurs.

### Étape 3 : Configurer les actions comportementales sociales dans AIR {#step-3-configure-social-behavioral-actions-in-air}

Ensuite, vous mettrez en place une ou plusieurs actions comportementales sociales dans AIR avec des références d'action uniques pour attribuer des points ou des coupons.

### Étape 4 : Configurer Braze {#step-4-configure-braze}

Dans Braze, vous accomplirez les tâches suivantes :

- Mettre en place des Campaigns dans Braze pour distribuer des récompenses dans AIR
- Configurer les communications aux consommateurs lorsque des événements AIR sont reçus

### Étape 5 : Tester votre intégration {#step-5-test-your-integration}

Effectuez des appels API dans AIR et observez le flux de données d'événements dans votre espace de travail Braze. Validez les données reçues d'AIR et confirmez que les attributs sont mis à jour comme prévu.

Ajoutez également des utilisateurs aux audiences et confirmez que les récompenses sont émises dans AIR.

### Étape 6 : Lancer en production {#step-6-launch-to-production}

Une fois les tests réussis, l'intégration peut être mise en production pour envoyer des données en continu à Braze. Les mêmes étapes de configuration sont requises pour les environnements de production dans AIR et Braze.

Contactez votre gestionnaire de la satisfaction client Eagle Eye pour qu'une ressource vous soit attribuée afin de mettre en place EE Connect.

## Assistance {#support}

Pour l'assistance à l'intégration ou la résolution des problèmes, veuillez contacter l'équipe d'assistance Eagle Eye à l'adresse [support@eagleeye.com](mailto:support@eagleeye.com).