---
date_published: "2026-09-08"
nav_title: GrowSurf
article_title: GrowSurf
description: "Cet article de référence décrit le partenariat entre Braze et GrowSurf, une plateforme de programmes de recommandation et d'affiliation qui synchronise les données des participants vers Braze pour la segmentation et la personnalisation Liquid."
alias: /partners/growsurf/
page_type: partner
search_tag: Partner
---

# GrowSurf

> [GrowSurf](https://www.growsurf.com/) envoie les données des participants de programmes de recommandation et d'affiliation vers les profils utilisateur Braze. L'intégration ajoute les liens de recommandation, les détails des participants, les nombres de recommandations, d'invitations, d'impressions et la progression des jalons en tant qu'attributs personnalisés que vous pouvez utiliser pour la segmentation Braze et la personnalisation Liquid.

_Cette intégration est maintenue par GrowSurf._

## À propos de l'intégration {#about-the-integration}

GrowSurf est un logiciel de programmes de recommandation et d'affiliation. L'intégration unidirectionnelle maintient les données de recommandation des participants GrowSurf disponibles dans Braze afin que vous puissiez segmenter les participants, personnaliser les messages avec les liens de recommandation et la progression, et envoyer des communications de programme pertinentes depuis Braze.

## Cas d'usage {#use-cases}

- Ajouter le lien de recommandation de chaque participant aux messages Braze.
- Créer des segments à partir du statut de recommandation, du nombre de recommandations et de la progression des jalons.
- Personnaliser les Campaigns et les Canvas avec les attributs des participants et des parrains.

## Prérequis {#prerequisites}

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis | Description |
| --- | --- |
| Un compte GrowSurf | Un abonnement payant GrowSurf est requis pour cette intégration. |
| Une clé API REST Braze | Une clé API REST Braze avec les permissions `users.track`. Créez cette clé dans le tableau de bord de Braze depuis **Paramètres** > **API et identifiants** > **Clés API**. Pour plus d'informations, consultez [Créer des clés API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Un endpoint REST Braze | L'URL de votre endpoint REST Braze (par exemple, `https://rest.iad-01.braze.com`). Pour plus d'informations, consultez [Endpoints de la REST API]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

Suivez ces étapes pour connecter un programme GrowSurf à Braze. Pour des instructions détaillées, consultez la [documentation de l'intégration GrowSurf avec Braze](https://docs.growsurf.com/integrations/braze).

### Étape 1 : Créer une clé API REST Braze {#step-1-create-a-braze-rest-api-key}

1. Dans Braze, accédez à **Paramètres** > **API et identifiants** > **Clés API**.
2. Créez une clé API REST avec les permissions `users.track`.
3. Copiez la clé API et notez l'endpoint REST pour le même espace de travail Braze.

### Étape 2 : Connecter Braze dans GrowSurf {#step-2-connect-braze-in-growsurf}

1. Dans GrowSurf, accédez à **Program Editor** > **4. Options** > **Integrations** > **Braze**.
2. Sélectionnez l'endpoint REST Braze correspondant.
3. Saisissez la clé API REST et sélectionnez **Submit**.

### Étape 3 : Vérifier la première synchronisation d'un participant {#step-3-verify-the-first-participant-sync}

1. Ajoutez ou mettez à jour un participant de test dans GrowSurf.
2. Dans Braze, accédez à **Audience** > **Recherche d'utilisateurs** et recherchez par e-mail pour ouvrir le profil utilisateur correspondant.
3. Confirmez que les attributs personnalisés `grsf_` apparaissent sur le profil.

## Attributs GrowSurf dans Braze {#growsurf-attributes-in-braze}

GrowSurf met 15 attributs de recommandation à disposition dans Braze. La première synchronisation envoie l'ensemble complet. Par la suite, GrowSurf envoie des mises à jour lorsque les données d'un participant changent. Si une valeur est supprimée dans GrowSurf, l'attribut Braze correspondant est également effacé. Les valeurs de comptage sont envoyées sous forme de nombres.

### Attributs de type chaîne de caractères {#string-attributes}

| Attribut personnalisé | Description |
| --- | --- |
| `grsf_share_url` | L'URL de partage de recommandation du participant. |
| `grsf_participant_id` | L'identifiant GrowSurf du participant. |
| `grsf_referral_status` | Le statut de recommandation du participant. |
| `grsf_participant_first_name` | Le prénom du participant. |
| `grsf_participant_last_name` | Le nom de famille du participant. |
| `grsf_referrer_first_name` | Le prénom du parrain. |
| `grsf_referrer_last_name` | Le nom de famille du parrain. |
| `grsf_referrer_email` | L'adresse e-mail du parrain. |
| `grsf_next_milestone` | Le prochain jalon vers lequel le participant progresse. |
| `grsf_next_monthly_milestone` | Le prochain jalon mensuel vers lequel le participant progresse. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs de type chaîne de caractères" }

### Attributs de type nombre {#number-attributes}

| Attribut personnalisé | Description |
| --- | --- |
| `grsf_total_referral_count` | Le nombre total de recommandations du participant. |
| `grsf_monthly_referral_count` | Le nombre de recommandations du participant pour le mois en cours. |
| `grsf_prev_monthly_referral_count` | Le nombre de recommandations du participant pour le mois précédent. |
| `grsf_total_invite_count` | Le nombre total d'invitations du participant. |
| `grsf_total_impression_count` | Le nombre total d'impressions du lien de recommandation du participant. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs de type nombre" }

## Utiliser GrowSurf avec Braze {#use-growsurf-with-braze}

Utilisez les attributs de recommandation GrowSurf pour la segmentation Braze et la personnalisation Liquid. GrowSurf met à jour ces attributs lorsqu'un participant est ajouté ou lorsque ses données de recommandation changent. Vous pouvez également synchroniser les participants qui étaient déjà dans votre programme.

### Étape 1 : Créer des segments {#step-1-build-segments}

1. Dans Braze, créez un segment avec les attributs personnalisés `grsf_` pertinents.
2. Ciblez ou excluez des participants en fonction du statut de recommandation, du nombre de recommandations ou de la progression des jalons.

### Étape 2 : Personnaliser les messages {#step-2-personalize-messages}

1. Ajoutez l'attribut personnalisé `grsf_share_url` à un message Braze avec Liquid : {% raw %}`{{custom_attribute.${grsf_share_url}}}`{% endraw %}.

{: start="2"}
2. Utilisez les autres attributs `grsf_` pour personnaliser le statut de recommandation, les compteurs et la progression des jalons.

## Considérations {#considerations}

- GrowSurf envoie uniquement des attributs personnalisés. Il n'envoie pas d'événements personnalisés, d'achats ni de changements d'abonnement.
- GrowSurf identifie les profils Braze par l'e-mail du participant. Si aucun profil correspondant n'existe, Braze crée un profil avec l'e-mail uniquement.
- Si le même e-mail appartient à des participants dans plusieurs programmes GrowSurf connectés, les données du programme synchronisé le plus récemment apparaissent sur ce profil Braze.
- Connectez Braze avant d'importer des participants. Pour synchroniser les participants existants, utilisez l'option de synchronisation des participants existants de GrowSurf.

## Résolution des problèmes {#troubleshooting}

- Confirmez que la clé API REST Braze dispose des permissions `users.track` et que l'endpoint REST sélectionné appartient au même espace de travail Braze.
- Si un participant ne parvient pas à se synchroniser, vérifiez que le participant possède une adresse e-mail valide.
- Consultez les journaux d'activité du participant dans GrowSurf pour le résultat de la synchronisation.
- GrowSurf réessaie automatiquement en cas d'erreurs temporaires de Braze. Si GrowSurf ne peut pas confirmer une mise à jour, il envoie tous les attributs de recommandation lors de la prochaine synchronisation de ce profil Braze. Si la clé API ou l'endpoint REST est invalide, corrigez les paramètres et reconnectez l'intégration.

Pour plus de détails sur la résolution des problèmes, consultez la [documentation de l'intégration GrowSurf avec Braze](https://docs.growsurf.com/integrations/braze#troubleshooting).