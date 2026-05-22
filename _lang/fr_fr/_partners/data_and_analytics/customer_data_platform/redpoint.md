---
nav_title: Redpoint
article_title: Redpoint
description: "L'intégration de Redpoint à Braze vous permet d'intégrer et d'enrichir les profils utilisateurs de Braze avec vos données first-party."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) est une plateforme technologique qui offre aux marketeurs une plateforme d'orchestration de campagne entièrement intégrée. Tirez parti des capacités de segmentation, de planification et d'automatisation de Redpoint pour contrôler comment et quand les données CDP sont importées dans Braze.

_Cette intégration est maintenue par Redpoint._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Redpoint vous permet de créer des segments Braze basés sur vos données CDP Redpoint. Redpoint propose deux modes pour transmettre des données à Braze :

1. Mode **Braze Onboarding and Upsert** : effectue un « upsert » d'un profil utilisateur de Redpoint dans Braze. Ce mode est destiné à l'onboarding ou à la mise à jour des enregistrements utilisateurs lorsque les données ont changé.
2. Mode **Braze Append** : met à jour un profil utilisateur si cet utilisateur existe déjà dans Braze.

Vous configurerez un modèle d'exportation et un canal sortant pour chaque mode.

{% alert note %}
Le terme « upsert » est une combinaison des mots « update » (mettre à jour) et « insert » (insérer). Il est utilisé lorsque vous souhaitez insérer un nouvel enregistrement dans une table de base de données s'il n'existe pas déjà, ou mettre à jour l'enregistrement s'il existe. Essentiellement, l'upsert vérifie si un enregistrement particulier est présent dans la base de données. Si l'enregistrement est présent, il est mis à jour, et s'il n'est pas présent, un nouvel enregistrement est inséré.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`. <br><br>Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Artefacts Redpoint Data Management | L'intégration Braze est prise en charge par un ensemble d'artefacts Redpoint Data Management. Contactez l'[assistance Redpoint](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) pour demander les artefacts correspondant à votre version de Redpoint Data Management. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Attributs personnalisés CDP Redpoint {#redpoint-cdp-custom-attributes}

Les attributs personnalisés Redpoint suivants peuvent être ajoutés à un profil utilisateur Braze.

| Champ               | Description                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | L'objet d'attribut de profil CDP Redpoint                                                                                  |
| `rpi_audience_outputs`| Tableau de balises de sortie d'audience où l'utilisateur est ciblé dans une exécution de canal de distribution sortante Redpoint vers Braze         |
| `rpi_offers`         | Tableau de balises d'offre où l'utilisateur est ciblé dans une exécution de canal de distribution sortante Redpoint vers Braze                   |
| `rpi_contact_ids`    | Tableau des identifiants de contact de l'historique des offres où l'utilisateur est ciblé dans une exécution de canal de distribution sortante Redpoint vers Braze     |
| `rpi_channel_exec_ids`| Tableau d'identifiants d'exécution de canal où l'utilisateur est ciblé dans une exécution de canal de distribution sortante Redpoint vers Braze       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Intégration {#integration}

### Étape 1 : Configurer les modèles {#step-1-set-up-templates}

#### Étape 1a : Créer le modèle Braze Onboarding and Upsert {#step-1a-create-the-braze-onboarding-and-upsert-template}

Dans Redpoint Interaction (RPI), créez un nouveau modèle d'exportation et nommez-le **Braze Onboarding and Upsert**. Ce modèle définit les correspondances principales entre le CDP Redpoint et le profil utilisateur Braze, ainsi que tous les attributs personnalisés supplémentaires que vous souhaitez ajouter à vos profils utilisateurs dans Braze.

Faites glisser les attributs CDP de Redpoint dans la colonne **Attribute**. Définissez chaque **Header Row Value** sur l'[attribut utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) Braze correspondant.

Le tableau suivant répertorie les attributs CDP Redpoint et leurs attributs Braze correspondants :

| Attribut Redpoint | Header Row Value |
|--------------------|------------------|
| PID                | `external_id`    |
| First Name          | `first_name`     |
| Last Name          | `last_name`      |
| Primary Email      | `email`          |
| Primary Country    | `country`        |
| DOB                | `dob`            |
| Gender             | `gender`         |
| Primary City       | `home_city`      |
| Primary Phone      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ajoutez l'attribut **Output Name** de la table **Offer History**. Enfin, ajoutez tous les attributs personnalisés Redpoint supplémentaires que vous souhaitez fusionner dans Braze. Par exemple, voici un modèle d'onboarding et d'upsert avec le diplôme, le revenu et l'état civil comme attributs supplémentaires.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Étape 1b : Créer le modèle Braze Append {#step-1b-create-the-braze-append-template}

Créez un deuxième modèle d'exportation pour les opérations d'ajout uniquement, nommé **Braze Append**.

Vous ne définirez que deux attributs pour ce modèle. Pour **PID**, définissez la **Header Row Value** sur `external_id`. Pour **Output Name**, définissez la **Header Row** sur `output_name`.

![Un exemple de modèle d'exportation avec les attributs `external_id` et output name.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Étape 1c : Définir le format de date {#step-1c-set-date-format}

Pour les deux modèles d'exportation, accédez à l'onglet **Options** et définissez le **Date Format** sur la valeur **Custom Format**. Définissez le format sur **yyyy-MM-dd**.

![L'onglet Options montrant le format de date défini sur yyyy-MM-dd.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Étape 2 : Créer des canaux sortants {#step-2-create-outbound-channels}

Dans RPI, créez deux nouveaux canaux. Définissez les deux canaux sur **Outbound Delivery**. Nommez un canal **Braze Onboarding and Upsert** et l'autre **Braze Append**.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Après l'onboarding initial de vos enregistrements CDP vers Braze, vérifiez que les workflows Redpoint Interaction suivants qui utilisent le canal Braze Onboarding and Upsert sont conçus pour sélectionner uniquement les enregistrements qui ont changé depuis la synchronisation initiale d'onboarding.
{% endalert %}

### Étape 3 : Configurer les canaux {#step-3-configure-the-channels}

#### Étape 3a : Définir le modèle et le format du chemin d'exportation {#step-3a-set-template-and-export-path-format}

Accédez à l'onglet **General** dans l'écran de **Configuration** des canaux. Définissez le modèle d'exportation pour chaque canal respectif.

Ensuite, définissez un **Export path format** sur les deux canaux qui pointe vers un emplacement de réseau partagé, un protocole de transfert de fichiers ou un fournisseur de contenu externe accessible à la fois à Redpoint Interaction et à Redpoint Data Management.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

Le format du répertoire d'exportation sur les deux canaux sera identique et devrait se terminer par `\\[Channel]\\[Offer]\\[Workflow ID]`.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Étape 3b : Configurer la post-exécution {#step-3b-configure-post-execution}

Accédez à l'onglet **Post Execution** dans l'écran de **Configuration** des canaux.

Cochez la case **Post-execution** pour appeler une URL de service après l'exécution du canal. Saisissez l'URL du service web Redpoint Data Management. Cette entrée sera identique sur vos canaux Onboarding et Append.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Étape 4 : Configurer les composants Braze dans Redpoint Data Management {#step-4-set-up-braze-components-in-redpoint-data-management}

L'archive contenant les artefacts Redpoint Data Management (RPDM) pour prendre en charge l'intégration Braze inclut un fichier README avec des instructions détaillées pour configurer les composants requis. Gardez à l'esprit les détails suivants lors de la configuration de votre intégration.

#### Étape 4a : Mettre à jour l'automatisation RPI vers Braze avec votre endpoint REST Braze et le répertoire de sortie de base RPI {#step-4a-update-the-rpi-to-braze-automation-with-your-braze-rest-endpoint-and-base-rpi-output-directory}

Après avoir importé les artefacts liés à Braze dans Redpoint Data Management, ouvrez l'automatisation nommée **AUTO_Process_RPI_to_Braze** et mettez à jour les deux variables d'automatisation suivantes avec les valeurs de votre environnement :

* **BRAZE_API_URL** : l'endpoint REST de Braze
* **BASE_OUTPUT_DIRECTORY** : le répertoire de sortie partagé entre Redpoint Interaction et Redpoint Data Management

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Étape 4b : Mettre à jour le projet RPI vers Braze Append {#step-4b-update-the-rpi-to-braze-append-project}

Le projet Redpoint Data Management nommé **PROJ_RPI_to_Braze_Append** contient le schéma du fichier d'exportation de distribution sortante et les mappages pour l'objet d'attribut personnalisé `rpi_cdp_attributes` dans Braze.

Mettez à jour le schéma de fichier d'entrée et l'outil d'injection de document nommé **RPI to Braze Document Injector** avec tous les attributs CDP personnalisés supplémentaires définis dans votre modèle de fichier d'exportation. Cet exemple montre le mappage supplémentaire du diplôme, des revenus et de l'état civil :

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Utilisation de l'intégration {#using-the-integration}

Le canal Braze de distribution sortante peut désormais être exploité dans les workflows Redpoint Interaction. Suivez les pratiques standard pour créer des règles de sélection et des audiences dans RPI, ainsi que pour créer les planifications de workflow et les déclencheurs associés.

Pour activer la synchronisation d'une sortie d'audience RPI vers Braze, créez une offre de distribution sortante et associez-la soit au canal **Braze Onboarding and Upsert**, soit au canal **Braze Append**. Ce choix dépend de votre intention : créer ou fusionner de nouveaux enregistrements dans Braze, ou uniquement ajouter des données de campagne si l'enregistrement existe déjà dans Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Une fois le workflow exécuté avec succès dans RPI, les données d'orchestration et de CDP provenant de RPI peuvent être utilisées pour créer des segments dans Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Vous pouvez consulter les propriétés associées à Redpoint sur le profil utilisateur.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}