---
nav_title: Heap
article_title: "Analyse Heap"
description: "Cet article de référence explique comment utiliser Braze Currents pour analyser automatiquement les événements d'engagement avec Heap, une plateforme d'informations numériques, qui vous permet d'importer des données Heap dans Braze, de créer des cohortes d'utilisateurs et d'exporter des données Braze vers Heap pour créer des segments."
page_type: partner
alias: /partners/heap/
search_tag: Partner

---

# Analyse Heap {#heap-analytics}

> Cet article explique comment envoyer automatiquement des événements d'engagement de Braze à Heap pour analyse. Pour plus d'informations sur l'intégration de Heap et ses autres fonctionnalités, telles que la [synchronisation des cohortes Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap#data-import-integration) avec Braze, consultez l'[article principal de Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import).

## Intégration de l'exportation de données {#data-export-integration}

Utilisez Braze Currents pour envoyer automatiquement les événements d'engagement (par exemple, e-mail envoyé, notification push envoyée) de Braze à Heap pour analyse.

### Étape 1 : Obtenir les identifiants Heap {#step-1-get-heap-credentials}

Vous aurez besoin d'une URL d'endpoint webhook pour configurer cette intégration. Vous pouvez l'obtenir auprès de votre gestionnaire de compte Heap.

### Étape 2 : Configurer Braze Currents {#step-2-configure-braze-currents}

Dans Braze, accédez à **Intégrations partenaires** > **Exportation de données**, cliquez sur **Créer un nouveau Current**, puis sélectionnez **Heap Export**.

Donnez un nom à votre export, puis passez à la page **Détails du Current**. Sur cette page, saisissez l'endpoint et le jeton porteur facultatif (s'il est fourni).

Après avoir configuré les identifiants de votre intégration, cochez tous les événements d'engagement de messages, de comportement des clients et d'utilisateurs que vous souhaitez exporter vers Heap, puis cliquez sur **Lancer le Current**.

![Page de configuration du Current Braze Heap avec les champs d'endpoint, de jeton et de sélection des événements.]({% image_buster /assets/img/heap/heap4.png %}){: style="max-width:90%;"}