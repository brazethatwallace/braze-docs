---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "Cet article de référence présente le partenariat entre Braze et Kickbox, une plateforme de vérification d'e-mails utilisée pour valider des listes d'e-mails ou intégrer la vérification dans votre application."
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/) est une plateforme de vérification des e-mails tout-en-un, dotée des fonctionnalités, des intégrations et de la sécurité dont vous avez besoin pour que vos données e-mail restent propres et livrables. L'intégration de Kickbox améliore la livrabilité de vos Campaigns Braze en utilisant la vérification des e-mails de Kickbox pour identifier les adresses e-mail non distribuables et de faible qualité avant l'envoi.

Kickbox vous permet de valider la qualité des adresses e-mail de vos utilisateurs au moment où un profil utilisateur est mis à jour dans Braze. Pour ce faire, un Canvas dédié ou un flux de travail de Campaign est déclenché par le remplissage du champ `email` d'un profil.

Le Canvas ou la Campaign enverra un webhook à Kickbox, partageant l'adresse e-mail de l'utilisateur. Kickbox validera l'adresse e-mail et utilisera l'endpoint de la REST API de Braze pour mettre à jour le profil utilisateur avec un attribut personnalisé détaillant sa qualité.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --------------------------------------|-------------------------------------------------------------------------------|
| Compte Kickbox | Un compte Kickbox actif est nécessaire pour utiliser cette intégration. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`. <br><br>Celle-ci peut être créée dans le tableau de bord de Braze en allant dans **Paramètres** > **API et identifiants** > **Clés API**. |
| Demander l'accès à l'intégration | Demandez à l'équipe d'assistance de Kickbox de vous accorder l'accès à l'intégration de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour intégrer Kickbox, suivez les étapes décrites dans la section [Intégration à Braze](https://docs.kickbox.com/docs/integrating-with-braze#/).

## Cas d'utilisation {#use-cases}

### Vérification en bloc {#bulk-verification}

Vous pouvez également choisir de vérifier l'ensemble de votre liste tous les quelques mois ou tous les trimestres, afin de vous protéger des e-mails qui deviennent obsolètes ou des listes qui se dégradent au fil du temps et font lentement chuter votre livrabilité.

Pour ce faire, vous devez modifier les paramètres **Entry Settings** du flux de travail, comme indiqué par Kickbox. Au lieu de sélectionner **Action-Based Delivery**, sélectionnez **Scheduled**. Choisissez ensuite une heure planifiée pour que votre liste soit vérifiée en une seule fois.

### Créer des segments vérifiés {#create-verified-segments}

Les attributs personnalisés de Kickbox ont un schéma cohérent, correspondant aux exemples suivants.

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@kickbox.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "kickbox.com"
    },
    {
      "email": "example2@gamil.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@gmail.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "gamil.com"
    }
  ]
}
```
{% endraw %}

Cela signifie que vous pouvez créer des segments d'audience regroupant les utilisateurs dont les adresses e-mail ont été vérifiées, afin que vos Campaigns et Canvas bénéficient d'un taux de réussite de distribution plus élevé, protégeant ainsi votre réputation auprès des ESP.

Pour ce faire, suivez les étapes suivantes :

1. Dans Braze, allez dans **Audience** > **Segments** > **Créer un segment**.
2. Dans la section **Filter Group**, ajoutez le filtre **Custom Attribute** et sélectionnez « result » dans le menu déroulant.

En fonction de votre cas d'utilisation, il peut être approprié de créer un segment dans lequel l'attribut personnalisé Kickbox « result » existe sur un profil utilisateur, ou dans lequel sa valeur est égale à « deliverable ». Ce filtre peut être utilisé seul pour créer un segment, ou peut être intégré à tous les futurs segments afin de valider tous les utilisateurs qui s'y trouvent.