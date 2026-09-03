---
nav_title: Extensions de segments CDI
article_title: Extensions de segments CDI
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "Cet article explique comment les extensions de segments CDI s'appuient sur l'ingestion de données cloud pour interroger votre entrepôt de données et définir des audiences dans Braze."

---

# Extensions de segments CDI {#cdi-segment-extensions}

> Avec l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) (CDI) de Braze, vous pouvez établir une connexion directe entre votre entrepôt de données ou votre système de stockage de fichiers et Braze pour synchroniser les données utilisateur ou de catalogue pertinentes de manière récurrente.

{% alert warning %}
Les extensions de segments CDI interrogent directement votre entrepôt de données, ce qui signifie que vous supporterez tous les coûts associés à l'exécution de ces requêtes dans votre entrepôt de données. Les extensions de segments CDI ne consomment pas de [crédits de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits), ne sont pas comptabilisées dans votre limite d'extensions de segments et ne génèrent pas de points de donnée.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser les données de votre entrepôt de données à des fins de segmentation dans votre espace de travail Braze, vous devez créer une [source connectée]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources), puis créer un segment CDI dans vos [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Les extensions de segments CDI vous permettent d'écrire du SQL qui interroge directement votre propre entrepôt de données en utilisant les données rendues disponibles via vos connexions CDI, et de créer un groupe d'utilisateurs pouvant être ciblés dans Braze.

## Créer un segment CDI {#creating-a-cdi-segment}

### Étape 1 : Configurer votre source {#step-1-set-up-your-source}

Avant de créer votre première extension de segment CDI, configurez une nouvelle source connectée avec votre entrepôt de données en suivant les étapes décrites dans [Sources connectées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

### Étape 2 : Créer un segment {#step-2-create-a-segment}

Commencez par créer une nouvelle [extension de segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension), puis sélectionnez **Full refresh**.

![Exemple de placement d'une fenêtre modale de content card.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Pour votre source de données, choisissez **CDI Data Tables**.

![Capture d'écran relative à l'étape 2 : créer un segment.]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Dans le cadre de votre configuration CDI, vous pouvez sélectionner différentes connexions à utiliser dans les extensions de segments CDI. Chaque connexion dispose d'un ensemble spécifique de tables de données. Votre équipe de développement peut configurer vos connexions et tables de données lors de la configuration CDI.

Pour afficher les tables de données disponibles, y compris leur schéma et les descriptions disponibles, sélectionnez **Reference**. Lorsque vous êtes prêt, sélectionnez une connexion.

![Pour afficher les tables de données disponibles, y compris leur schéma et les descriptions disponibles, sélectionnez Reference. Lorsque vous êtes prêt, sélectionnez une connexion.]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

Ensuite, écrivez le SQL pour votre segment en utilisant [la syntaxe SQL de Braze]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql).

Gardez à l'esprit que toutes les extensions de segments CDI doivent utiliser `external_user_id` comme colonne sélectionnée, et votre `external_user_id` doit correspondre à celui défini dans Braze pour les utilisateurs.

{% alert important %}
`external_user_id` doit être une valeur de type **chaîne de caractères**. Si votre identifiant source est stocké sous forme de nombre (par exemple, `client_id` en tant qu'entier), [convertissez-le en chaîne de caractères dans votre SQL](https://www.w3schools.com/sql/func_sqlserver_cast.asp) afin qu'il corresponde au type `external_id` dans Braze.
{% endalert %}

Si les résultats de votre requête incluent des utilisateurs qui n'existent pas dans Braze, ces utilisateurs sont ignorés. Braze ne crée pas de nouveaux utilisateurs à partir des résultats de votre extension de segment CDI.

{% alert tip %}
Pour découvrir comment prévisualiser vos extensions de segments, les gérer et exécuter des actualisations automatiques des membres, consultez [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).
{% endalert %}

Enfin, vous pouvez [utiliser cette extension de segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment) au sein d'un segment Braze pour envoyer une Campaign ou un Canvas à cette audience.

## Considérations {#considerations}

- Une extension de segment ne peut référencer les données que d'une seule connexion, pas de plusieurs.
- Une extension de segment peut utiliser l'une des sources de données suivantes : les tables de données CDI ou les données Braze Snowflake (Currents). Vous ne pouvez pas mélanger les sources de données au sein d'une même extension de segment, mais vous pouvez créer plusieurs extensions de segments à référencer ensemble au sein d'un segment.

## Résolution des problèmes {#troubleshooting}

- Votre requête peut expirer lorsqu'elle atteint la durée d'exécution maximale, qui est configurée pour chaque synchronisation de connexion sur la page **Cloud Data Ingestion**. La durée d'exécution maximale autorisée est de 60 minutes.
- Assurez-vous que votre SQL est écrit en utilisant la syntaxe appropriée pour votre entrepôt de données.