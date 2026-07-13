---
nav_title: Importation de cohortes Hightouch
article_title: Importation de cohortes Hightouch
description: "Cet article de référence décrit la fonctionnalité d'importation de la cohorte de Hightouch, une plateforme permettant de synchroniser les données de vos clients depuis votre entrepôt avec les outils commerciaux."
page_type: partner
search_tag: Partner

---
# Importation de cohortes Hightouch {#hightouch-cohort-import}

> Cet article explique comment importer des cohortes d'utilisateurs depuis [Hightouch](https://hightouch.io) vers Braze afin de pouvoir envoyer des campagnes ciblées en fonction de données qui n'existent peut-être que dans votre entrepôt. Pour plus d'informations sur l'intégration de Hightouch et ses autres fonctionnalités, consultez l'[article principal sur Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch).

## Intégration de l'importation de données {#data-import-integration}

### Étape 1 : Obtenir la clé d'importation des données Braze {#step-1-get-the-braze-data-import-key}
Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Hightouch**.

Vous y trouverez votre endpoint REST et pourrez générer votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez en créer une nouvelle ou invalider une clé existante.<br><br>![Page de partenaire technologique Braze Hightouch affichant l'endpoint REST et les contrôles de la clé d'importation des données.]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"}

### Étape 2 : Ajouter les cohortes Braze en tant que destination dans Hightouch {#step-2-add-braze-cohorts-as-a-destination-in-hightouch}
Accédez à la page **Destination** de votre espace de travail Hightouch, recherchez **Braze Cohorts** et cliquez sur **Continue**. Saisissez ensuite votre endpoint REST et votre clé d'importation des données, puis cliquez sur **Continue**.<br><br>![Configuration de la destination Hightouch pour Braze Cohorts avec les champs d'identification.]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Étape 3 : Synchroniser un modèle (ou une audience) dans Braze Cohorts {#step-3-sync-a-model-or-audience-into-braze-cohorts}
Dans Hightouch, à l'aide du [modèle](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) ou de l'[audience](https://hightouch.io/docs/audiences/usage/) que vous avez créé, créez une nouvelle synchronisation. Sélectionnez ensuite la destination Braze Cohorts que vous avez créée à l'étape précédente. Enfin, dans la configuration de la destination Braze Cohorts, sélectionnez l'identifiant de correspondance souhaité et indiquez si vous souhaitez que Hightouch crée une nouvelle cohorte Braze ou mette à jour une cohorte existante.<br><br>![Configuration de la synchronisation Hightouch Braze Cohorts avec l'identifiant de correspondance et les options de cohorte.]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés à une cohorte ou en être retirés. L'importation de cohortes ne crée pas de nouveaux utilisateurs dans Braze.
{% endalert %}

### Étape 4 : Créer un segment Braze à partir de l'audience personnalisée Hightouch {#step-4-create-a-braze-segment-from-the-hightouch-custom-audience}
Dans Braze, accédez à **Segments**, créez un nouveau segment et sélectionnez **Hightouch Cohorts** comme filtre. Vous pouvez alors choisir la cohorte Hightouch que vous souhaitez inclure. Une fois votre segment de cohorte Hightouch créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une Campaign ou d'un Canvas.<br><br>![Générateur de segments Braze utilisant le filtre Hightouch Cohorts.]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Utilisation de cette intégration {#using-this-integration}
Pour utiliser votre segment Hightouch, créez une Campaign ou un Canvas Braze et sélectionnez le segment comme audience cible.<br><br>![Étape de ciblage d'audience Braze avec un segment basé sur Hightouch sélectionné.]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être associés par leur `external_id` ou leur `alias`. Les utilisateurs anonymes peuvent être associés par leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent l'être par leur `external_id` ou leur `alias`.