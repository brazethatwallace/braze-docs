---
nav_title: Kubit
article_title: Importation de la cohorte Kubit
description: "Cet article de référence présente la fonctionnalité d'importation de cohortes de Kubit, une plateforme d'analyse/analytique en libre-service sans code qui fournit des informations instantanées sur les produits, vous permettant d'importer des cohortes d'utilisateurs Kubit et de les cibler dans l'envoi de messages Braze."
page_type: partner
search_tag: Partner
---

# Importation de la cohorte Kubit {#kubit-cohort-import}

> Cet article décrit comment importer des cohortes d'utilisateurs de [Kubit](https://kubit.ai/) vers Braze. Pour plus d'informations sur l'intégration de Kubit et de ses autres fonctionnalités, consultez l'[article principal sur Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit).

## Intégration de l'importation de données {#data-import-integration}

### Étape 1 : Obtenir la clé d'importation des données de Braze {#step-1-get-the-braze-data-import-key}

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Kubit**. Ici, vous trouverez l'endpoint REST et générerez votre clé d'importation des données Braze.

Une fois générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Kubit.

![La page partenaire technologique de Kubit dans Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Étape 2 : Configurer Braze dans Kubit {#step-2-configure-braze-in-kubit}

Fournissez la clé d'importation des données de Braze et l'endpoint REST de Braze à votre contact d'assistance Kubit. L'équipe Kubit configurera l'intégration de leur côté et vous informera lorsque l'intégration sera active.

### Étape 3 : Importer des cohortes dans Braze {#step-3-import-cohorts-to-braze}

#### Créer une cohorte dans Kubit {#create-a-cohort-in-kubit}
[Créez une cohorte](https://www.kubit.ai/doc/fundamentals#cohort) dans Kubit et définissez les critères de vos utilisateurs ciblés.<br><br>![Générateur de cohortes Kubit avec les critères d'utilisateurs cibles configurés.]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Importer des utilisateurs vers Braze {#import-users-to-braze}
Une fois que vous avez enregistré votre cohorte, vous pouvez l'importer dans Braze pour l'utiliser dans les segments Braze. Ces segments peuvent ensuite être utilisés pour créer des campagnes ciblées par e-mail ou notification push, ainsi que des Canvas.

Pour ce faire, accédez à votre cohorte existante et, sous **Cohort Control**, sélectionnez **Import to Braze**.

![Menu Cohort Control de Kubit avec l'option Import to Braze sélectionnée.]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Sélectionnez ensuite la cadence d'importation souhaitée. Les importations ponctuelles vous permettent d'effectuer une importation unique. Les importations planifiées vous permettent d'effectuer des importations quotidiennes, hebdomadaires ou mensuelles à un moment précis. Notez que chaque cohorte ne peut avoir qu'une seule planification d'importation active.

![Paramètres de planification d'importation Kubit avec les options de cadence pour les importations Braze.]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation de cohortes ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

#### Vérifier le statut de l'importation {#verify-import-status}
Une fois l'importation terminée, un e-mail de notification sera envoyé aux destinataires spécifiés dans la planification de l'importation. Vous pouvez également vérifier le statut d'importation d'une cohorte sous **Schedule** dans Kubit. L'historique de la planification affiche l'heure d'exécution de chaque importation, le résultat et le nombre total d'utilisateurs de la cohorte qui ont été importés vers Braze.<br><br>![Historique de planification Kubit affichant les heures d'exécution des importations, les résultats et le nombre d'utilisateurs importés.]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Vous pouvez déclencher manuellement une importation en cliquant sur l'icône **Import to Braze** pour cette planification d'importation.

### Étape 4 : Créer des segments Braze avec des cohortes Kubit {#step-4-create-braze-segments-with-kubit-cohorts}
Après avoir importé des cohortes dans Braze, vous pouvez les utiliser comme filtres pour créer des segments Braze et les inclure dans des campagnes ou des Canvas Braze. Consultez notre documentation sur les segments pour en savoir plus sur la [création de segments Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#step-4-add-filters-to-your-segment).

![Dans le générateur de segments de Braze, l'attribut utilisateur « Cohortes Kubit » est défini sur « includes_value » et affiche une liste des cohortes disponibles.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Correspondance entre les utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être associés par leur `external_id` ou leur `alias`. Les utilisateurs anonymes peuvent être mis en correspondance par leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent être identifiés par leur `external_id` ou leur `alias`.