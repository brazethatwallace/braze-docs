---
nav_title: Amplitude
article_title: Importation de cohortes d'Amplitude
description: "Cet article de référence décrit la fonctionnalité d'importation de la cohorte d'Amplitude, une plateforme d'analyse de produits et d'aide à la décision."
page_type: partner
search_tag: Partner
---

# Importation de cohortes Amplitude {#amplitude-cohort-import}

> Cet article explique comment importer des cohortes d'utilisateurs d'[Amplitude](https://amplitude.com/) vers Braze. Pour plus d'informations sur l'intégration d'Amplitude et de ses autres fonctionnalités, consultez l'[article principal sur Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Intégration de l'importation de données {#data-import-integration}

Toute intégration que vous configurez sera prise en compte dans le volume de points de données de votre compte.

### Étape 1 : Obtenir la clé d'importation des données de Braze {#step-1-get-the-braze-data-import-key}

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Amplitude**. Vous y trouverez l'endpoint REST et pourrez générer votre clé d'importation des données Braze.

Une fois générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'Amplitude.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Étape 2 : Configurer l'intégration de Braze dans Amplitude {#step-2-set-up-the-braze-integration-in-amplitude}

Dans Amplitude, accédez à **Sources & Destinations** > **[nom du projet]** > **Destinations** > **Braze**. Dans l'invite qui s'affiche, indiquez la clé d'importation des données Braze et l'endpoint REST, puis cliquez sur **Save**.

![]({% image_buster /assets/img/amplitude.png %})

### Étape 3 : Exporter une cohorte Amplitude vers Braze {#step-3-export-an-amplitude-cohort-to-braze}

Tout d'abord, pour exporter des utilisateurs d'Amplitude vers Braze, créez une [cohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) d'utilisateurs que vous souhaitez exporter. Ensuite, pour capturer les utilisateurs identifiés et anonymes, configurez deux synchronisations pour cette cohorte avec les propriétés de mappage d'identifiants suivantes :
- ID utilisateur (ID externe)
- ID de l'appareil

Vous pouvez configurer plusieurs connexions Braze dans votre compte Amplitude. Cela vous permet de configurer une connexion pour synchroniser les ID utilisateur des utilisateurs connus et une autre pour synchroniser les ID d'appareil des utilisateurs anonymes.

Une fois que vous avez créé une cohorte, cliquez sur **Sync to...** pour exporter ces utilisateurs vers Braze.

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation de cohortes ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

#### Définition de la cadence de synchronisation {#defining-sync-cadence}

Les synchronisations de cohortes peuvent être configurées comme synchronisation unique, planifiées quotidiennement ou toutes les heures, ou même en temps réel avec des mises à jour toutes les minutes.

Toute intégration que vous mettez en place enregistrera des points de données. Si vous avez des questions sur les subtilités des points de données de Braze, votre gestionnaire de compte Braze peut y répondre.

### Étape 4 : Segmenter les utilisateurs dans Braze {#step-4-segment-users-in-braze}

Dans Braze, pour créer un segment de ces utilisateurs, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Amplitude Cohorts** comme filtre. Ensuite, utilisez l'option « includes » et choisissez la cohorte que vous avez créée dans Amplitude.

![Dans le générateur de segments Braze, le filtre « amplitude_cohorts » est réglé sur « includes_value » et « Amplitude cohort test ».]({% image_buster /assets/img/amplitude2.png %})

Après l'enregistrement, vous pouvez référencer ce segment lors de la création d'un Canvas ou d'une Campaign à l'étape de ciblage des utilisateurs.

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être associés par leur `external_id` ou leur `alias`. Les utilisateurs anonymes peuvent être associés par leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent être identifiés par leur `external_id` ou leur `alias`.