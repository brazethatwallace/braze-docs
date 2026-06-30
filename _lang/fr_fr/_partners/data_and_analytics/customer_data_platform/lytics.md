---
nav_title: Lytics
article_title: Lytics
description: "Cet article de référence traite de l'intégration de Braze et Lytics. Lytics est une plateforme de données clients d'entreprise pour les marketeurs, les analystes et les technologues. Cette intégration permet aux marques de synchroniser et de mapper leurs données Lytics directement sur Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/) est la plateforme de données client (CDP) de choix pour la prochaine génération d'entreprises centrées sur le client. Les solutions Lytics Decision Engine, Conductor et Cloud Connect offrent aux marketeurs et aux équipes chargées des données des possibilités de résolution d'identité, d'orchestration et d'optimisation des campagnes en temps réel et dans le respect de la confidentialité.

_Cette intégration est maintenue par Lytics._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Lytics offre une vue unifiée de vos clients pour permettre une personnalisation puissante et mener des campagnes optimisées à l'aide de l'orchestration et des décisions de la prochaine meilleure action.

L'intégration permet aux marques de :

- Exporter des audiences vers Braze directement à partir de Lytics
- Envoyer les événements des Campaigns ou Canvas Braze à Lytics en temps réel pour des campagnes personnalisées et pour créer des profils utilisateurs riches

## Cas d'utilisation {#use-cases}

Connectez Braze à Lytics pour [importer](#importing-data-from-braze-to-lytics) des e-mails, des SMS et l'activité des notifications push afin d'enrichir les profils utilisateurs Lytics. En utilisant conjointement Braze et Lytics, vous pouvez également [exporter](#integration) les audiences cross-canal et basées sur le comportement de Lytics pour créer des parcours clients Braze hautement personnalisés à l'aide de données first-party.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Lytics | Un compte Lytics est nécessaire pour profiter de cette intégration. |
| Numéro de compte Lytics | Un numéro de compte Lytics est nécessaire pour configurer l'URL de l'endpoint webhook. |
| Jeton API Lytics | Un jeton REST API Lytics avec des autorisations de gestionnaire de données. <br><br> Celui-ci peut être créé dans le tableau de bord Lytics à partir de la **console Paramètres du compte** > **Access Tokens** > **Create New Token**. |
| Clé REST API de Braze | Une clé REST API Braze avec l'autorisation `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Instance de Braze | Votre [instance Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). En cas de doute, contactez votre gestionnaire d'onboarding Braze pour obtenir ces informations. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Cette section décrit comment exporter des données Lytics dans Braze.

### Étape 1 : Créer une autorisation {#step-1-create-an-authorization}

Dans Lytics, accédez au tableau de bord **Authorization** au sein de la console **Data** dans la barre de navigation. Sélectionnez **Create New Authorization**, puis recherchez et sélectionnez **Braze**.

Dans l'invite **Configure Authorization** qui s'affiche, fournissez un libellé et une description, puis saisissez votre clé REST API et votre instance Braze. Sélectionnez **Complete** lorsque vous avez terminé.

![Invite de configuration de l'autorisation Lytics pour Braze avec des champs pour le libellé, la description, la clé REST API et l'instance Braze.]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### Étape 2 : Créer une nouvelle tâche {#step-2-create-a-new-job}

Dans Lytics, accédez au tableau de bord **Jobs** dans la console **Data** de la barre de navigation. Sélectionnez **Create New Job**, recherchez et sélectionnez **Braze**. Dans l'invite **Select Job Type** qui s'affiche, sélectionnez **Export Audience**.

![Invite de sélection du type de tâche Lytics pour une nouvelle tâche Braze avec Export Audience sélectionné.]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

Ensuite, choisissez une autorisation dans les options **Select Authorization**.

![Étape de sélection de l'autorisation Lytics montrant l'autorisation Braze à utiliser pour la tâche d'exportation.]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### Étape 3 : Configurer la tâche {#step-3-configure-the-job}

Dans l'invite **Configure Job**, indiquez un libellé et une description facultative. Ensuite, dans le champ **Braze External User ID Field**, sélectionnez le champ de Lytics qui contient l'ID utilisateur externe de Braze (`braze_id`). L'étape suivante est la plus importante : dans la même boîte de dialogue, sélectionnez les audiences à exporter vers Braze à l'aide du sélecteur d'audiences.

Enfin, choisissez l'option souhaitée pour la case à cocher **Existing Users**. En laissant cette case cochée, les utilisateurs qui existent déjà dans l'audience Lytics sélectionnée seront ajoutés. Si la case n'est pas cochée, les utilisateurs ne seront exportés vers Braze que lorsqu'ils entreront ou sortiront de l'audience après le début du flux de travail.

{% alert note %}
En cochant cette case, tous les utilisateurs existants dans l'audience sélectionnée seront envoyés vers Braze. Si votre tarification Braze inclut des points de données, surveillez l'utilisation des points de données en conséquence.
{% endalert %}

Sélectionnez **Complete** lorsque vous avez terminé pour lancer l'exportation et enregistrer.

![Résumé de la tâche d'exportation Lytics montrant le contrôle Complete et les options pour enregistrer ou exécuter l'exportation d'audience Braze.]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

Une fois la tâche d'exportation configurée, Lytics enverra les audiences sélectionnées à Braze via l'intégration native. Vous trouverez ci-dessous un exemple d'audience montrant la structure JSON de l'audience envoyée à Braze.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Un nouvel utilisateur sera créé dans Braze pour tout `external_id` inclus dans l'exportation d'audience qui n'existe pas encore dans Braze.

## Importation de données de Braze vers Lytics {#importing-data-from-braze-to-lytics}

Vous pouvez importer des données d'audience de Braze vers Lytics à l'aide des méthodes suivantes :

- [Utilisation de webhooks](#using-webhooks)
- [À partir d'un fichier CSV](#from-a-csv-file)

### Utilisation de webhooks {#using-webhooks}

#### Étape 1 : Créer un jeton API Lytics {#step-1-create-a-lytics-api-token}

Accédez au menu du compte Lytics dans le coin inférieur gauche en sélectionnant votre nom de compte, puis sélectionnez **Access Tokens** dans le menu déroulant. Ensuite, sélectionnez **Create API Token**.

![Écran Access Tokens de Lytics avec Create API Token sélectionné depuis le menu du compte.]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

Saisissez un nom, une description facultative et une période d'expiration du jeton. Ensuite, activez le périmètre **Data Manager** pour les autorisations API et sélectionnez **Generate Token**. Copiez le jeton et conservez-le en lieu sûr.

![Autorisations du jeton API Lytics avec le périmètre Data Manager activé avant la génération du jeton.]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### Étape 2 : Configurer l'URL du webhook Lytics {#step-2-configure-the-lytics-webhook-url}

L'URL du webhook Lytics est utilisée par Braze pour envoyer un message à l'API Lytics depuis Braze. Ce message peut être utilisé pour personnaliser vos campagnes dans Lytics ou pour enrichir votre profil client Lytics. Les deux paramètres suivants doivent être ajoutés à l'URL du webhook Lytics :

- Numéro de compte Lytics
- Jeton API Lytics

Configurez l'URL de votre webhook comme suit :

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Remplacez `<ACCOUNT-NUMBER>` par votre numéro de compte et `<LYTICS-API-TOKEN>` par votre jeton API Lytics.

#### Étape 3 : Créer un webhook dans Braze {#step-3-create-a-webhook-on-braze}

Dans Braze, créez une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook). Ajoutez l'URL du webhook Lytics dans le champ **Webhook URL**.

Après avoir défini le type de requête (méthode HTTP `POST`) et configuré le reste des détails du webhook, votre webhook est prêt à être testé et déployé. Voici un exemple de payload de la requête POST après avoir configuré le webhook dans Braze :

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "Alex",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@example.com",
  "braze_id": "xxxxxx"
}
```

### À partir d'un fichier CSV {#from-a-csv-file}

Cette section décrit comment importer les données des utilisateurs Braze d'un segment dans Lytics.

#### Étape 1 : Créer une autorisation

Dans Lytics, accédez au tableau de bord **Authorization** au sein de la console **Data** dans la barre de navigation. Sélectionnez **Create New Authorization**, puis recherchez et sélectionnez **Custom Integrations**.

Sélectionnez le type d'autorisation SFTP qui vous convient le mieux en fonction de vos besoins en termes de sécurité et d'activité. Les types d'autorisation suivants sont pris en charge pour l'importation de fichiers dans Lytics via SFTP :

- Client SFTP Server Authorization
- Client SFTP Server Authorization with PGP Private Key
- Lytics Managed SFTP Server Authorization

Les autorisations SFTP à clé publique sont destinées uniquement à l'exportation SFTP.

![Options de méthode d'autorisation SFTP Lytics pour l'importation Custom Integrations, incluant les choix de serveur client et géré par Lytics.]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

Dans l'invite **Configure Authorization** qui s'affiche, fournissez un libellé et une description, puis complétez le reste des exigences de configuration. Sélectionnez **Complete** lorsque vous avez terminé.

#### Étape 2 : Exporter vos données de segment au format CSV {#step-2-export-your-segment-data-to-csv}

Dans Braze, accédez à **Audience** > **Segments**. Localisez le segment que vous souhaitez exporter, puis sélectionnez <i class="fas fa-gear" aria-label="Paramètres"></i> puis **CSV Export User Data**. Vous pouvez exporter jusqu'à 500 000 utilisateurs dans un segment. Pour plus d'informations, reportez-vous à la section [Exportation des données de segment au format CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

#### Étape 3 : Configurer une tâche d'importation CSV {#step-3-configure-a-csv-import-job}

Dans Lytics, accédez au tableau de bord **Jobs** dans la console **Data** de la barre de navigation. Sélectionnez **Create New Job**, puis recherchez et sélectionnez **Custom Integrations**.

Sélectionnez ensuite le type de tâche. Pour importer des fichiers CSV de Braze dans Lytics, sélectionnez **Import CSV** comme type de tâche.

![Configuration de tâche Custom Integrations Lytics avec Import CSV sélectionné comme type de tâche.]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

Enfin, saisissez un libellé et une description facultative pour la tâche, puis configurez tout autre détail nécessaire. Sélectionnez **Complete** pour lancer et enregistrer la tâche.