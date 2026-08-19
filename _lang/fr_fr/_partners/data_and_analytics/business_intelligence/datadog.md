---
nav_title: Datadog
article_title: Datadog
description: "Cet article de référence décrit le partenariat entre Braze et Datadog, un service d'observabilité pour les applications à l'échelle du cloud, fournissant une surveillance des serveurs, des bases de données, des outils et des services via une plateforme d'analyse de données basée sur le SaaS."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) est un service d'observabilité pour les applications à l'échelle du cloud, fournissant une surveillance des serveurs, des bases de données, des outils et des services via une plateforme d'analyse de données basée sur le SaaS.

L'intégration de Braze et Datadog permet aux clients de collecter les données de Braze dans Datadog et de créer des alertes sur les données envoyées. Par exemple, vous pouvez configurer un moniteur et une alerte si votre campagne de newsletter hebdomadaire envoie un volume anormalement bas de messages, ou si une étape du Canvas qui n'envoie habituellement que quelques messages par jour commence à en envoyer des milliers.

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte Datadog | Un compte Datadog est nécessaire pour bénéficier de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Générer une clé Datadog {#step-1-generate-datadog-key}

Dans Datadog, vous devrez créer une [clé API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Pour ajouter une clé API, accédez à **Organization Settings** > **API Keys** > **New Key**.

### Étape 2 : Ajouter la clé à Braze {#step-2-add-key-to-braze}

Dans le tableau de bord de Braze, accédez à **Partner Integrations** > **Technology Partners**, puis recherchez **Datadog**. Sur la page partenaire Datadog, renseignez la clé API Datadog. Cela créera une connexion permettant à Braze d'envoyer des données à Datadog.

## Événements Braze {#braze-events}

Une fois la connexion intégrée, Braze envoie les événements suivants à Datadog :

- `braze.messaging.sent` - Le nombre d'envois

Chacun de ces événements possède des métadonnées sous forme de tags Datadog qui vous fournissent des informations telles que :

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (si disponible)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (si disponible)

Ces événements et tags peuvent être surveillés sur la page **Metrics Explorer** de Datadog. Ces indicateurs sont enregistrés en tant que [distributions](https://docs.datadoghq.com/metrics/distributions/) dans DataDog. Étant donné la nature des indicateurs et l'imprécision des agrégations et des cumuls de DataDog, Braze ne retente pas les erreurs réseau intermittentes ou les autres erreurs de l'API DataDog qui peuvent survenir lors de la transmission. Cela signifie que ces comptages d'indicateurs peuvent différer légèrement des comptages affichés dans le tableau de bord de Braze et/ou via Currents.

![Metrics Explorer de Datadog affichant les indicateurs et tags des événements Braze.]({% image_buster /assets/img/datadog.png %})

## Résolution des problèmes {#troubleshooting}

### Pourquoi les indicateurs `braze.messaging.sent` sont-ils absents dans Datadog ? {#why-are-brazemessagingsent-metrics-missing-in-datadog}

Si vous avez connecté Braze à Datadog mais que vous ne voyez pas `braze.messaging.sent` dans le Metrics Explorer, vérifiez que le **site Datadog** sélectionné dans Braze correspond à l'URL du site de votre organisation Datadog. Les sites disponibles sont :

- `datadoghq.com` (par défaut)
- `us3.datadoghq.com`
- `us5.datadoghq.com`
- `datadoghq.eu`
- `ddog-gov.com`
- `ap1.datadoghq.com`

Une incohérence de site peut empêcher les indicateurs d'apparaître dans l'espace de travail où vous effectuez vos recherches. Dans le tableau de bord de Braze, accédez à **Partner Integrations** > **Technology Partners** > **Datadog** et vérifiez que le site correspond au sous-domaine de l'URL de votre compte Datadog.

Le champ **Site Datadog** est verrouillé après la connexion. Pour le modifier, déconnectez l'intégration puis reconnectez-vous avec le site correct.

Après avoir corrigé le site, attendez qu'une nouvelle activité d'envoi se produise avant que les indicateurs n'apparaissent. Les données historiques ne sont pas rétro-alimentées.