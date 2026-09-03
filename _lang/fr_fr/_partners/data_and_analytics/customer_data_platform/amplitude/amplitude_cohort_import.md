---
nav_title: Amplitude
article_title: Importation de cohortes d'Amplitude
description: "Cet article de référence décrit la fonctionnalité d'importation de la cohorte d'Amplitude, une plateforme d'analyse de produits et d'aide à la décision."
page_type: partner
search_tag: Partner
---

# Importation de cohortes Amplitude {#amplitude-cohort-import}

> Cet article explique comment importer des cohortes d'utilisateurs d'[Amplitude](https://amplitude.com/) vers Braze. Pour plus d'informations sur l'intégration d'Amplitude et de ses autres fonctionnalités, consultez l'[article principal sur Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences).

## Intégration d'importation de données {#data-import-integration}

Toute intégration que vous configurez sera comptabilisée dans le volume de points de donnée de votre compte.

### Étape 1 : Obtenir la clé d'importation des données Braze {#step-1-get-the-braze-data-import-key}

Dans Braze, naviguez vers **Partner Integrations** > **Technology Partners** et sélectionnez **Amplitude**. Vous y trouverez l'endpoint REST et pourrez générer votre clé d'importation des données Braze.

Une fois générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'Amplitude.<br><br>![Page de partenaire technologique Braze Amplitude affichant la clé d'importation des données et l'endpoint.]({% image_buster /assets/img/amplitude3.png %})

### Étape 2 : Configurer l'intégration Braze dans Amplitude {#step-2-set-up-the-braze-integration-in-amplitude}

Dans Amplitude, naviguez vers **Sources & Destinations** > **[nom du projet]** > **Destinations** > **Braze**. Dans l'invite qui apparaît, fournissez la clé d'importation des données Braze et l'endpoint REST, puis cliquez sur **Save**.

![Paramètres de destination Amplitude pour la synchronisation de cohortes Braze avec les identifiants saisis.]({% image_buster /assets/img/amplitude.png %})

### Étape 3 : Exporter une cohorte Amplitude vers Braze {#step-3-export-an-amplitude-cohort-to-braze}

Tout d'abord, pour exporter des utilisateurs d'Amplitude vers Braze, créez une [cohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) des utilisateurs que vous souhaitez exporter. Ensuite, pour capturer les utilisateurs identifiés et anonymes, configurez deux synchronisations pour cette cohorte avec les propriétés de mappage d'identifiant suivantes :
- User ID (ID externe)
- Device ID

Vous pouvez configurer plusieurs connexions Braze dans votre compte Amplitude. Cela vous permet de configurer une connexion pour synchroniser les User ID des utilisateurs connus et une autre pour synchroniser les Device ID des utilisateurs anonymes.

Une fois la cohorte créée, cliquez sur **Sync to...** pour exporter ces utilisateurs vers Braze.

{% alert important %}
Seuls les utilisateurs existant déjà dans Braze seront ajoutés ou retirés d'une cohorte. L'importation de cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

#### Définir la cadence de synchronisation {#defining-sync-cadence}

Les synchronisations de cohortes peuvent être configurées en synchronisation unique, planifiées quotidiennement ou toutes les heures, ou même en temps réel avec une mise à jour toutes les minutes.

Toute intégration que vous configurez enregistrera des points de donnée. Si vous avez des questions sur les subtilités des points de donnée Braze, votre gestionnaire de compte Braze pourra y répondre.

### Étape 4 : Segmenter les utilisateurs dans Braze {#step-4-segment-users-in-braze}

Dans Braze, pour créer un segment de ces utilisateurs, naviguez vers **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Amplitude Cohorts** comme filtre. Ensuite, utilisez l'option « includes » et choisissez la cohorte que vous avez créée dans Amplitude.

![Dans le générateur de segments Braze, le filtre « amplitude_cohorts » est défini sur « includes_value » et « Amplitude cohort test ».]({% image_buster /assets/img/amplitude2.png %})

Après l'enregistrement, vous pouvez référencer ce segment lors de la création d'un Canvas ou d'une Campaign à l'étape de ciblage des utilisateurs.

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être mis en correspondance soit par leur `external_id`, soit par leur `alias`. Les utilisateurs anonymes peuvent être mis en correspondance par leur `device_id`. Les utilisateurs identifiés qui ont été initialement créés en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent être identifiés par leur `external_id` ou leur `alias`.

## FAQ

### Puis-je récupérer une liste des cohortes Amplitude ? {#can-i-pull-a-list-of-amplitude-cohorts}

Braze ne fournit pas d'API pour exporter un catalogue de toutes les définitions de cohortes Amplitude. Vous pouvez consulter et utiliser les cohortes aux emplacements suivants :

1. **Dans Amplitude :** Consultez et gérez les cohortes dans le tableau de bord Amplitude avant de les synchroniser avec Braze.
2. **Dans Braze :** Une fois qu'une cohorte est synchronisée, ciblez les utilisateurs avec le filtre de Segment **Amplitude Cohorts**. Le filtre répertorie les cohortes synchronisées par le nom envoyé par Amplitude.

Pour les erreurs de synchronisation de cohortes, vérifiez d'abord l'alignement des identifiants utilisateur et les clés API dans Amplitude. Consultez [« We do not have enough data yet for this filter » lors de la synchronisation d'une cohorte]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort).