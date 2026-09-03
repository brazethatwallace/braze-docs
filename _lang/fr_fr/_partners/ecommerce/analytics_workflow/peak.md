---
nav_title: Peak
article_title: Peak
description: "Cet article de référence décrit le partenariat entre Braze et Peak, une plateforme d'intelligence décisionnelle, qui vous permet de prendre la probabilité d'attrition prédite et les attributs basés sur les comportements et interactions des clients, et de les importer dans Braze pour les utiliser dans la segmentation et le ciblage des clients."
alias: /partners/peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://peak.ai/), une plateforme d'intelligence décisionnelle, est un système de bout en bout où l'intelligence décisionnelle est l'application commerciale de l'IA pour améliorer la prise de décision, augmenter le chiffre d'affaires et les bénéfices.

_Cette intégration est maintenue par Peak._

## À propos de l'intégration {#about-the-integration}

Le partenariat entre Braze et Peak vous permet d'importer dans Braze les prévisions d'attrition et les attributs basés sur les comportements et interactions des clients afin de les utiliser dans la segmentation et le ciblage des clients.

## Conditions préalables {#prerequisites}

Pour commencer, un tenant Peak doit héberger l'intégration entre Peak et Braze. Celui-ci est traditionnellement créé lors de l'onboarding des clients Peak. De plus, une solution d'intelligence décisionnelle est initialement requise, car elle génère les résultats pilotés par l'IA qui seront ensuite intégrés dans Braze.

| Exigence | Description |
| ----------- | ----------- |
| Tenant Peak | Une instance de la plateforme Peak, connue sous le nom de tenant, est requise pour héberger et orchestrer l'intégration. |
| Solution d'intelligence décisionnelle | L'intégration entre Peak et Braze est basée sur des résultats pilotés par l'IA et nécessite donc une solution Peak ou une solution client déployée au sein de votre tenant. |
| Clé REST API de Braze | Une clé REST API de Braze avec les autorisations `users.track`. <br><br>Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

L'intelligence client de la solution Peak utilise un modèle pour prédire une gamme d'attributs prospectifs basés sur les comportements et les interactions des clients. Ces attributs sont stockés dans Peak et peuvent être utilisés pour générer une segmentation prédictive, y compris la probabilité d'attrition d'un client. La mise à jour de ces attributs prédictifs repose sur une cadence configurable (quotidienne ou hebdomadaire).

### Étape 1 : Exécuter le modèle et extraire les clients {#step-1-run-model-and-extract-customers}

L'intégration est déclenchée par l'exécution du modèle d'IA et le recalcul des attributs prédictifs des clients. Ces résultats d'IA sont stockés dans Peak, y compris lorsqu'un attribut est mis à jour avec un nouveau statut ou une nouvelle valeur.

En fonction du moment où les attributs ont été mis à jour, une sélection est effectuée pour collecter tous les clients dont les attributs prédictifs ont été mis à jour depuis la dernière synchronisation entre Peak et Braze.

### Étape 2 : Mettre à jour Braze {#step-2-update-braze}

Une fois les clients mis à jour et les attributs associés récupérés, Peak les envoie à Braze via l'endpoint [`/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), en utilisant l'en-tête [bulk]({{site.baseurl}}/api/endpoints/user_data/post_user_track#need-to-update-users-in-bulk).

À la réception des codes de statut de réussite de l'API, Peak enregistre la synchronisation réussie entre Peak et Braze.

### Étape 3 : Utiliser cette intégration {#step-3-using-this-integration}

Une fois la synchronisation entre Peak et Braze réussie, les utilisateurs mis à jour incluent désormais les nouveaux attributs. Utilisez ces attributs dans les Campaigns et les Canvas pour cibler les utilisateurs et personnaliser les messages.