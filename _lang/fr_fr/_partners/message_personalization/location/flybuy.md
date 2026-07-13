---
nav_title: Flybuy
article_title: Flybuy
alias: /partners/flybuy/
description: "Cet article de référence décrit le partenariat entre Braze et Flybuy, une plateforme de services de localisation, pour ajouter de l'intelligence de localisation à vos opérations et à vos capacités marketing."
page_type: partner
search_tag: Partner

---

# Flybuy

> [Flybuy](https://www.flybuy.com/) de Radius Networks est la principale plateforme de localisation omnicanal exploitant une technologie alimentée par l'intelligence artificielle pour optimiser la rapidité de service pour le retrait, la livraison, le drive et la restauration sur place. Grâce à sa Marketing Suite intégrée, Flybuy permet également aux marques de diffuser des messages hyper-ciblés et contextuels, contribuant à stimuler l'engagement, augmenter le panier moyen et soutenir des initiatives de fidélisation plus larges.

_Cette intégration est maintenue par Flybuy._

## À propos de l'intégration {#about-the-integration}

Flybuy transmet des événements riches d'intelligence utilisateur dans Braze, permettant aux marques d'envoyer des messages hyper-pertinents et contextualisés par la localisation avec le plus haut niveau de personnalisation. Lorsqu'un utilisateur génère un événement dans Flybuy, des événements personnalisés accompagnés d'attributs utilisateur enrichis sont transmis à Braze. Ces événements et attributs peuvent être utilisés pour alimenter des opérations omnicanal et déclencher des messages basés sur la proximité.

## Conditions préalables {#prerequisites}

Les éléments suivants sont requis avant d'activer l'intégration :

| Condition | Description |
|---|---|
| Compte Flybuy | Un compte Flybuy avec au moins un projet. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour activer l'intégration, suivez les étapes suivantes :

1. Dans le portail marchand Flybuy, accédez à **Project Info** et cliquez sur **Events Engine**.
2. Cliquez sur **Add a Destination**, puis sélectionnez **Braze**.
3. Ajoutez votre clé API Braze et votre endpoint, puis sélectionnez les événements que vous souhaitez activer.
4. Cliquez sur **Finish Setup**.

{% alert important %}
Flybuy associe `loyalty_id` à l'`external_id` de Braze pour les utilisateurs connectés.
{% endalert %}

## Cas d'utilisation {#use-cases}

- [Retrait](https://www.flybuy.com/flybuypickup)
- [Livraison](https://www.flybuy.com/flybuydelivery)
- [Drive](https://www.flybuy.com/flybuydrivethru)
- [Service à table](https://www.flybuy.com/flybuytableservice)
- [Enregistrement mobile et commande en hôtellerie](https://www.flybuy.com/industries/hospitality)
- [Marketing Suite](https://www.flybuy.com/flybuy-marketing-suite)

## Exemples de déclencheurs basés sur les événements et les attributs {#event-and-attribute-based-trigger-examples}

Les événements personnalisés et les attributs personnalisés peuvent être utilisés pour alimenter une variété d'expériences personnalisées.

### Créer un segment d'audience de clients ayant eu une mauvaise expérience de retrait {#build-an-audience-segment-of-customers-who-had-a-bad-pickup-experience}

Par exemple, ciblez tout client ayant évalué son expérience de retrait à moins de 5 étoiles.

![Segment pour une mauvaise expérience de retrait]({% image_buster /assets/img/flybuy/flybuy1.png %})

### Déclencher une alerte lorsqu'un client entre dans une zone de retrait virtuelle {#trigger-an-alert-when-a-customer-enters-a-virtual-pickup-area}

Envoyez un SMS personnalisé ciblant les clients sans compte de fidélité pour les inciter à télécharger l'application et créer un compte de fidélité.

![Déclencher une alerte lorsqu'un client entre dans une zone de retrait virtuelle]({% image_buster /assets/img/flybuy/flybuy2.png %})

![Message d'alerte déclenché lorsqu'un client entre dans une zone de retrait virtuelle]({% image_buster /assets/img/flybuy/flybuy2a.png %})

### Créer un segment d'audience de clients ayant eu un temps d'attente prolongé {#build-an-audience-segment-of-customers-who-had-a-long-wait-time}

Par exemple, ciblez tout client ayant eu un temps d'attente de plus de deux minutes en quittant les locaux virtuels d'un magasin.

![Créer un segment d'audience de clients ayant eu un temps d'attente prolongé]({% image_buster /assets/img/flybuy/flybuy3.png %})

### Déclencher une alerte de correction de trajet lorsqu'un client se dirige vers le mauvais emplacement {#trigger-a-course-correction-alert-when-a-customer-is-headed-to-the-wrong-location}

Envoyez une notification push aux clients lorsqu'ils se dirigent vers un emplacement différent de celui où ils ont passé leur commande, ou lorsqu'ils y sont arrivés.

### Proposer des offres spéciales basées sur des jalons de trajet {#deliver-special-offers-based-on-trip-milestones}

Par exemple, envoyez une offre spéciale lorsqu'un client VIP arrive à ses emplacements favoris.

### Créer un segment d'audience de clients dont des articles manquaient dans leur commande {#build-an-audience-segment-of-customers-who-were-missing-items-in-their-order}

Par exemple, ciblez tout client ayant signalé que des articles manquaient dans sa commande numérique.

Pour plus de détails sur les API et les SDK, consultez la [documentation développeur Flybuy](https://www.radiusnetworks.com/developers/flybuy/#/).