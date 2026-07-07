---
nav_title: Recurly
article_title: Recurly
description: "Recurly est la principale plateforme de gestion des abonnements et de facturation pour les marques de vente directe aux consommateurs qui cherchent à développer leurs abonnements et leur chiffre d'affaires récurrent."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) est une plateforme de gestion des abonnements et de facturation. La plateforme intégrée Recurly simplifie l'automatisation du cycle de vie des abonnements à grande échelle en permettant aux équipes de gérer et d'optimiser l'expérience des abonnés&#8212;depuis le test de nouveaux plans, offres et promotions jusqu'à la gestion des méthodes de paiement, des intégrations et des informations.

_Cette intégration est maintenue par Recurly._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Recurly et Braze simplifie le processus de partage des données d'abonnement avec Braze, ce qui permet une communication ciblée avec les clients.

- Exploitez les événements du cycle de vie des abonnements Recurly (par exemple, les renouvellements, les pauses ou les annulations d'abonnement) dans Braze pour déclencher des campagnes et des communications personnalisées.
- Exploitez les données d'abonnement Recurly (par exemple, les plans d'abonnement, les modules complémentaires ou le statut) pour créer et gérer les utilisateurs de l'entreprise, les Segments et les Canvas dans Braze afin d'exécuter des campagnes et des communications spécifiques aux cohortes.
- Envoyez les données Recurly directement à Braze afin de prendre en charge davantage de cas d'utilisation d'envoi de messages et de réduire les frais généraux de développement.

Vous trouverez plus de détails sur l'utilisation de Recurly avec Braze dans la [documentation de Recurly](https://docs.recurly.com/docs/braze-integration).

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Recurly | Un plan d'abonnement Elite [Recurly](https://recurly.com/) avec l'indicateur de fonctionnalité Braze activé est nécessaire pour tirer parti de ce partenariat. L'activation des factures de crédit dans votre plateforme Recurly est également nécessaire. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. Recurly n'utilisant que l'endpoint `users.track`, nous vous recommandons de provisionner une clé spécifique à Recurly avec cette seule autorisation. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Avant de commencer, assurez-vous d'avoir des comptes actifs à la fois sur Braze et sur Recurly.

### Connecter Recurly à Braze {#connect-recurly-to-braze}

1. Dans Recurly, allez dans **Integrations** > **Braze**. Lors de la première navigation vers la page de configuration de l'intégration Braze dans Recurly, l'interface vous invitera à connecter les deux systèmes.

2. Fournissez les informations d'identification suivantes :

- **Instance URL :** L'endpoint REST de Braze de l'instance auprès de laquelle vous êtes provisionné.
- **API Key (Identifier) :** La clé API REST de Braze que Recurly doit utiliser lors de l'envoi de requêtes à Braze.

N'oubliez pas de copier l'URL de votre instance Braze. Par exemple, votre URL pourrait ressembler à ceci :

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3. Après avoir saisi vos informations d'identification, cliquez sur **Connect**.

## Utiliser cette intégration {#using-this-integration}

### Identifiants pris en charge {#supported-identifiers}

Recurly utilise le paramètre `account_code` d'un compte comme `external_id` dans Braze. Pour cette raison, le paramètre `account_code` de vos comptes Recurly doit correspondre au paramètre `external_id` de votre utilisateur Braze.

### Événements personnalisés {#custom-events}

Pour un engagement client efficace, vous devez [configurer des événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) dans Braze afin de recevoir les événements déclenchés par Recurly. Veillez à inclure chaque événement de Recurly pour une intégration complète des données. Ces événements peuvent également être suivis dans le cadre de l'[analytique de Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics). Une fois configurés, ces événements personnalisés peuvent être utilisés pour segmenter les utilisateurs ou personnaliser les messages.

| Événement personnalisé Braze | Événement Recurly |
| ----------- | ----------- |
| Recurly New Subscription              | Déclenché lors de la création d'un abonnement                            |
| Recurly Renewed Subscription          | Déclenché lors du renouvellement d'un abonnement                                |
| Recurly Updated Subscription          | Déclenché lorsque les attributs d'un abonnement changent (changement de plan, de prix ou de quantité) |
| Recurly Canceled Subscription         | Déclenché lors de l'annulation d'un abonnement                           |
| Recurly Reactivated Subscription      | Déclenché lorsqu'un abonnement annulé est réactivé               |
| Recurly Paused Subscription           | Déclenché lorsqu'un abonnement est mis en pause                   |
| Recurly Resumed Subscription          | Déclenché lorsqu'un abonnement interrompu reprend                              |
| Recurly Subscription Expired          | Déclenché à l'expiration d'un abonnement                               |
| Recurly Invoice Created               | Déclenché lors de la création d'une facture                                |
| Recurly Successful Payment            | Déclenché lorsqu'une facture a été recouvrée avec succès                 |
| Recurly Refund Issued                 | Déclenché lors de l'émission d'un remboursement                                   |
| Recurly Failed Recurring Payment      | Déclenché en cas d'échec de la facturation d'un renouvellement d'abonnement          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements personnalisés" }

### Mise en lots et limite de débit {#batching-and-rate-limiting}

Comme Recurly utilise l'endpoint `/users/track` de Braze, l'intégration est soumise aux limites de débit standard de Braze, à savoir 50 000 requêtes par minute.

Recurly regroupe certains événements du cycle de vie des abonnements en appels API uniques vers Braze afin de réduire le nombre de requêtes.

- Recurly regroupe et envoie plusieurs abonnements créés en même temps en une seule requête.
- Recurly regroupe plusieurs renouvellements simultanés d'un compte en une seule requête.
- Recurly envoie les événements du cycle de vie des abonnements du même modèle en une seule requête. Par exemple, une facture nouvellement créée avec un paiement donne lieu à une requête API contenant les événements personnalisés `Recurly Invoice Created` et `Recurly Successful Payment`.

Les lots sont envoyés à Braze par groupes de 75 événements maximum à la fois. Par exemple, si 100 abonnements sont créés en même temps, Recurly effectuera deux requêtes API à Braze. Pour plus d'informations, reportez-vous à la section [relative à la mise en lots des requêtes de suivi des utilisateurs]({{site.baseurl}}/api/api_limits/#batch-user-track).