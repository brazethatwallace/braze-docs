---
nav_title: ActionIQ
article_title: ActionIQ
description: "Cet article de référence couvre l'intégration de Braze et d'ActionIQ. ActionIQ est une plateforme de données client d'entreprise pour les marketeurs, les analystes et les technologues. Cette intégration permet aux marques de synchroniser et de mapper leurs données ActionIQ directement sur Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ](https://www.actioniq.com/) est une plateforme de données client pour les marques d'entreprise qui offre aux marketeurs des moyens simples et sécurisés d'activer les données n'importe où dans l'expérience client. Grâce à l'architecture composable unique d'ActionIQ, les données peuvent rester en toute sécurité là où elles se trouvent, et les équipes marketing n'utilisent que les outils dont elles ont besoin.

_Cette intégration est maintenue par ActionIQ._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et d'ActionIQ permet aux marques de synchroniser et de mapper leurs données ActionIQ directement sur Braze, favorisant ainsi la distribution d'expériences client extraordinaires basées sur l'ensemble de leurs données client. Les intégrations disponibles permettent aux utilisateurs de :

- Mettre à jour les profils utilisateurs dans Braze avec les informations d'appartenance à l'audience et tous les attributs directement depuis ActionIQ
- Transmettre les événements suivis par ActionIQ à Braze en temps réel pour déclencher des campagnes personnalisées et ciblées
- Diffuser des campagnes déclenchées par l'API dans Braze directement à partir des points de contact d'un parcours ActionIQ

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte ActionIQ | Un compte ActionIQ est nécessaire pour profiter de cette intégration. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations requises pour l'intégration concernée. Consultez la section Conditions de l'intégration correspondante pour plus de détails. <br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégrations {#integrations}

### Appartenance à l'audience {#audience-membership}

Cette intégration permet de synchroniser l'appartenance à l'audience ActionIQ avec Braze en créant des attributs personnalisés qui indiquent si un profil Braze fait partie d'un segment. Chaque audience ActionIQ correspond à un attribut personnalisé booléen unique.

La convention de dénomination standard pour l'attribut personnalisé créé est la suivante : `AIQ_<Audience ID>_<Split ID>`.

Pour créer un segment de ces utilisateurs, procédez comme suit :
1. Dans Braze, accédez à **Segments**.
2. Créez un nouveau segment.
3. Sélectionnez **Custom Attributes** comme filtre.
4. Choisissez ensuite l'attribut personnalisé ActionIQ.
5. Une fois le segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

De plus, cette intégration mettra à jour tout attribut personnalisé ou standard dans un profil utilisateur Braze avec les valeurs d'attribut ActionIQ correspondantes.

#### Conditions {#requirements}

Une clé API REST Braze avec les autorisations `users.track` et `user.export.ids` est nécessaire. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**.

Dans ActionIQ, établissez une connexion avec Braze en fournissant votre clé API REST et l'endpoint REST Braze.

Pour faire correspondre les consommateurs sur la plateforme Braze, les identifiants suivants doivent être inclus dans votre paramètre d'activation :
- `braze_id`
- `external_id`

### Événements {#events}

Vous pouvez configurer la plateforme ActionIQ pour recevoir des informations sur les événements via son service d'ingestion de flux. Cette option d'intégration transmet ces événements à Braze pour que les marketeurs puissent les utiliser à des fins d'orchestration ou pour déclencher des campagnes marketing. L'intégration des événements peut envoyer des attributs ActionIQ supplémentaires dans le cadre des propriétés du payload de l'événement.

#### Conditions

Une clé API REST Braze avec les autorisations `users.track` et `user.export.ids` est nécessaire. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**.

L'intégration des événements envoie les informations suivantes à Braze :
- Nom de l'événement
- Identifiant du consommateur (`braze_id` ou `external_id`)
- Horodatage
- Propriétés d'événement, qui sont complétées par tout attribut supplémentaire dans le paramètre d'exportation

### Campagnes déclenchées {#triggered-campaigns}

Cette intégration déclenchera une campagne dans Braze pour tous les utilisateurs d'un segment ActionIQ. Après avoir configuré le contenu de votre campagne, les tests multivariés et les règles de rééligibilité, vous pouvez la déclencher à partir de n'importe quel point de contact du parcours ActionIQ en ajoutant l'ID de la campagne Braze à vos paramètres d'exportation.

En option, vous pouvez inclure d'autres attributs ActionIQ dans votre exportation afin d'alimenter le contenu de votre campagne. Ceux-ci sont envoyés avec l'objet `trigger_properties`.

#### Conditions

Une clé API REST Braze avec les autorisations `campaigns.trigger.send` et `campaigns.list` est nécessaire. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**.

Les valeurs suivantes doivent être envoyées dans votre exportation ActionIQ vers Braze :
- Identifiant du consommateur (`braze_id` ou `external_id`)
- ID de campagne