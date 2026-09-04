---
nav_title: Validity
article_title: Validity
alias: /partners/validity/
description: "Cet article de référence décrit le partenariat entre Braze et Validity, une plateforme de livrabilité des e-mails qui synchronise les listes de test Everest avec Braze et automatise les tests de placement en boîte de réception pour les Campaigns et les Canvas."
page_type: partner
search_tag: Partner
---

# Validity

> [Validity Everest](https://www.validity.com/everest/) est une plateforme de livrabilité des e-mails qui vous aide à mesurer le placement en boîte de réception et à protéger votre réputation d'expéditeur. L'intégration entre Braze et Validity synchronise votre liste de test Everest avec Braze, envoie automatiquement des tests aux Campaigns et Canvas éligibles, et récupère les indicateurs d'engagement dans Validity Inbox afin que vous puissiez comparer le placement basé sur les tests avec l'engagement réel de vos utilisateurs abonnés.

_Cette intégration est maintenue par Validity._

## À propos de l'intégration {#about-the-integration}

Validity crée et maintient des utilisateurs de liste de test e-mail dans Braze afin que les adresses de test restent actives et non supprimées. Lorsqu'une Campaign ou un Canvas est prêt à être testé, Validity envoie une copie à cette liste de test et affiche les indicateurs d'engagement — livrés, rebonds, ouvertures, clics et désabonnements — dans Validity Inbox aux côtés des données de placement en boîte de réception.

## Cas d'usage {#use-cases}

### Auto-seeding

Avec la fonctionnalité d'auto-seeding de Validity, Validity détecte lorsqu'une Campaign ou un Canvas Braze atteint un volume d'envoi éligible et envoie une copie du contenu de cette Campaign à votre liste de test Validity. Les envois de test ciblent les utilisateurs dont l'attribut personnalisé `validity_seed` est défini sur `true`.

## Prérequis {#prerequisites}

Avant de commencer, vous avez besoin des éléments suivants :

| Condition | Description |
| ----------- | ----------- |
| Un compte Validity | Un compte Validity est nécessaire pour bénéficier de ce partenariat. |
| Une clé API REST Braze | Une clé API REST Braze avec les permissions suivantes : `users.track`, `users.delete`, `email.bounce.remove`, `email.spam.remove`, `campaigns.list`, `campaigns.details`, `campaigns.data_series`, `canvas.list`, `canvas.details`, `canvas.data_series`, `content_blocks.list`, `content_blocks.info` et `messages.send`. <br><br> Créez cette clé dans le tableau de bord de Braze depuis **Paramètres** > **API et identifiants**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. Par exemple, `rest.iad-01.braze.com`. |
| Un identifiant d'application Braze | L'identifiant d'application Braze auquel les envois de test doivent être attribués. Vous le trouverez sous **Paramètres** > **API et identifiants** > **Identifiants d'application**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégrer Validity {#integrating-validity}

### Étape 1 : Partager les identifiants Braze avec Validity {#step-1-share-braze-credentials-with-validity}

Validity a besoin de trois identifiants depuis **Paramètres** > **API et identifiants** dans votre tableau de bord de Braze :

- Votre clé API REST (avec les permissions listées dans [Prérequis](#prerequisites))
- Votre endpoint REST
- Votre identifiant d'application

Partagez ces identifiants avec votre conseiller Validity, qui finalisera la configuration de l'intégration pour vous. Validity valide les identifiants avec un appel de test en direct vers Braze avant d'activer l'intégration. Si vous ne savez pas qui est votre contact Validity, envoyez un e-mail à [support@validity.com](mailto:support@validity.com).

Une fois l'intégration activée, Validity synchronise votre liste de test Everest avec Braze selon un cycle récurrent (toutes les 10 minutes). Validity crée, met à jour et supprime les utilisateurs de test dans Braze pour les maintenir alignés avec votre liste de test actuelle dans Everest.

### Étape 2 : Créer éventuellement un segment Braze pour les utilisateurs de test Validity {#step-2-optionally-create-a-braze-segment-for-validity-seed-users}

La création d'un segment est facultative. L'auto-seeding envoie des e-mails de test en utilisant un objet [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience) filtré sur l'attribut personnalisé `validity_seed` chaque fois qu'un envoi éligible est détecté. Vous n'avez pas besoin de créer un segment ni de l'associer à vos Campaigns.

Si vous souhaitez visualiser cette audience dans Braze à titre de référence, créez un segment sous **Audience** > **Segments** avec le filtre `validity_seed` est `true`.

Validity crée les utilisateurs via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) en utilisant le schéma suivant :

```bash
curl -X POST "https://YOUR_API_ENDPOINT/users/track" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BRAZE_API_KEY" \
  -d '{
    "attributes": [
      {
        "email": "example1@example.com",
        "validity_seed": true
      },
      {
        "email": "example2@example.com",
        "validity_seed": true
      }
    ],
    "events": [
      {
        "email": "example1@example.com",
        "name": "validity_seed_event",
        "time": "2026-07-02T18:00:00.000Z"
      }
    ]
  }'
```

Ces utilisateurs incluent toujours l'attribut personnalisé `validity_seed` avec la valeur booléenne `true`. Validity envoie également un événement personnalisé `validity_seed_event` pour chaque utilisateur de test afin qu'ils soient enregistrés comme utilisateurs actifs dans votre compte Braze.

## Considérations {#considerations}

### Fonctionnement des envois de test {#how-seed-sends-work}

Validity récupère le corps de la Campaign, l'objet et l'adresse d'expéditeur via les endpoints de détails des Campaigns et Canvas, puis envoie une copie de ce contenu à la liste de test via l'endpoint Braze [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Votre tableau de bord de Braze continue d'afficher uniquement la Campaign d'origine.

### Seuil d'auto-seeding {#auto-seeding-threshold}

Validity détecte lorsqu'une Campaign ou un Canvas dépasse votre seuil de volume d'envoi configuré (10 000 envois par défaut) et envoie le test à ce moment-là. Vous n'avez pas besoin d'ajouter l'audience de test à vos Campaigns ou Canvas.

Un test envoie votre Campaign e-mail aux adresses de la liste de test, collecte les données de placement et vous aide à identifier les problèmes avant ou en parallèle des envois à votre audience. Les indicateurs de placement en boîte de réception montrent si votre Campaign arrive dans la boîte de réception, le dossier spam, ou est manquante. Utilisez ces indicateurs pour confirmer le placement en boîte de réception et détecter les problèmes de livrabilité.

Les tests peuvent également vous aider à diagnostiquer pourquoi des e-mails arrivent dans le dossier spam ou sont manquants. L'examen des données d'en-tête, de l'authentification (SPF, DKIM et DMARC), de la validation des liens et du rendu du design peut indiquer les mesures à prendre pour améliorer votre taux de placement en boîte de réception.

### Santé de la liste de test {#seed-list-health}

Validity surveille les utilisateurs de la liste de test et peut les mettre à jour ou les supprimer s'ils commencent à perdre en efficacité — par exemple, si les fournisseurs de services d'e-mail marketing (fournisseur de services d'e-mailing) commencent à signaler les membres de l'audience de la liste de test comme spam. Ces permissions permettent à Validity de surveiller la santé de la liste de test et de la mettre à jour en conséquence.

### Gestion du contenu dynamique {#how-dynamic-content-is-handled}

Les e-mails Braze utilisent souvent la personnalisation Liquid liée au profil d'un destinataire réel. Comme les adresses de test ne disposent pas de ces données de profil, Validity fait passer chaque e-mail par un processus de nettoyage avant de l'envoyer en test. Ce processus résout les Content Blocks, évalue la logique Liquid de base et remplace tout ce qu'il ne peut pas résoudre (comme un prénom) par une marque substitutive visible `[REDACTED]`. Les sections entièrement construites à partir d'API Connected Content en direct s'affichent vides dans le test.

Vous pouvez activer ou désactiver le processus de nettoyage. Lorsqu'il est désactivé, Braze résout la personnalisation Liquid pour les envois de test de la même manière que pour un destinataire réel.

### Inbox Aggregate

L'activation de l'auto-seeding active également Inbox Aggregate. Cette fonctionnalité récupère les indicateurs d'engagement — envoyés, livrés, rebonds, ouvertures, clics et désabonnements — de vos envois Braze réels (séparément des envois de test) et les affiche dans Validity Inbox aux côtés de vos données de placement en boîte de réception. Les deux fonctionnalités fonctionnent selon des planifications indépendantes et n'ont pas besoin d'être gérées séparément.