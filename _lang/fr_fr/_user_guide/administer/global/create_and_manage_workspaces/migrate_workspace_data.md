---
nav_title: Migrer des données entre espaces de travail
article_title: Migrer des données entre espaces de travail et instances
page_order: 1
page_type: reference
description: "Découvrez comment les données d'un espace de travail sont isolées, ce que Braze peut copier ou importer entre les espaces de travail, et comment planifier des déplacements entre des environnements de staging, de production ou des tableaux de bord distincts."
---

# Migrer des données entre espaces de travail et instances {#migrate-data-between-workspaces-and-instances}

> Les espaces de travail maintiennent vos données Braze séparées. Cette page explique comment cet isolement affecte la migration, ce que vous pouvez déplacer avec les fonctionnalités du produit et les API, et ce que vous devez reconstruire ou gérer en dehors de Braze. La migration est généralement un effort transversal, pas uniquement une tâche d'administrateur de société. Les administrateurs sont souvent responsables de la configuration de l'espace de travail et des canaux ; les développeurs gèrent les modifications du SDK et de l'API ; les marketeurs reconstruisent les segments et copient le contenu des messages. Chaque étape nécessite les [autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) appropriées dans les espaces de travail source et de destination.

Tout ce que vous stockez dans Braze — profils utilisateur, segments, contenu des messages et historique d'engagement — réside dans un espace de travail. Un segment, une Campaign ou un Canvas ne peut pas lire ni cibler des données provenant d'un autre espace de travail. Les utilisateurs du tableau de bord utilisent souvent plusieurs espaces de travail sur le même tableau de bord d'entreprise pour le staging et la production, pour différentes marques ou pour des répartitions régionales. Cette configuration vous offre l'isolement, mais cela signifie également qu'il n'existe aucune action unique dans le tableau de bord permettant de déplacer toutes les données d'un espace de travail vers un autre espace de travail ou une autre instance Braze.

Pour le contexte de planification, consultez [Premiers pas : espaces de travail]({{site.baseurl}}/user_guide/get_started/workspaces/) et [Créer et gérer des espaces de travail]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/).

## Ce que Braze ne migre pas automatiquement entre les espaces de travail {#what-braze-does-not-automatically-migrate-between-workspaces}

Les éléments suivants ne sont pas migrés en masse lorsque vous pointez les SDK ou les API vers un nouvel espace de travail (ou un nouvel environnement de tableau de bord Braze avec ses propres espaces de travail) :

| Domaine | Comportement |
| --- | --- |
| **Profils utilisateur** | Les profils ne sont pas transférés en tant qu'unité packagée. Recréez ou importez les utilisateurs dans l'espace de travail de destination (voir [Données de profil utilisateur](#user-profile-data)). |
| **Segments et filtres** | Les définitions de segments restent dans l'espace de travail source. Reconstruisez les segments dans l'espace de travail de destination en utilisant la même logique lorsque c'est possible. |
| **Historique des messages** | L'historique de réception des Campaigns et Canvas sur un profil est lié à l'espace de travail source. Il n'apparaît pas sur un nouveau profil dans un autre espace de travail, sauf si vous le modélisez vous-même (par exemple, via des attributs personnalisés), comme indiqué dans la [FAQ d'onboarding Braze]({{site.baseurl}}/user_guide/onboarding_faq/). |
| **Configuration spécifique aux canaux** | Les domaines d'envoi, les abonnements SMS, les numéros WhatsApp et les paramètres similaires sont limités à l'espace de travail. Reconfigurez-les dans l'espace de travail de destination le cas échéant. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What Braze does not automatically migrate between workspaces" }

{% alert important %}
Si vous utilisez des espaces de travail distincts pour le staging et la production, n'oubliez pas que les connecteurs [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) ne sont pas partagés entre les espaces de travail. Planifiez quel espace de travail gère les exports de production. Pour plus de détails, consultez [Premiers pas : espaces de travail]({{site.baseurl}}/user_guide/get_started/workspaces/#currents-connectors).
{% endalert %}

## Ce que vous pouvez déplacer ou recréer {#what-you-can-move-or-recreate}

### Contenu des Campaigns et Canvas {#campaign-and-canvas-content}

Vous pouvez copier de nombreuses définitions de Campaigns et Canvas vers un autre espace de travail sous forme de brouillons. Les canaux pris en charge, les champs omis et les mises en garde concernant Liquid sont documentés dans [Copier des Campaigns et Canvas entre espaces de travail]({{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces/). Après la copie, mettez à jour les segments, les déclencheurs et toutes les références spécifiques à l'espace de travail avant de lancer.

### Données de profil utilisateur {#user-profile-data}

Approches courantes :

- **REST API :** Utilisez [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour créer ou mettre à jour des utilisateurs dans l'espace de travail de destination avec les identifiants et attributs nécessaires. C'est le même schéma décrit pour la [migration de données utilisateur historiques]({{site.baseurl}}/developer_guide/getting_started/integration_overview/#migrating-legacy-user-data) lors de l'importation de données historiques dans Braze.
- **Import CSV :** Pour les imports pilotés par les marketeurs, consultez [Importer des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/) et [Import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).
- **Ingestion de données cloud :** Pour synchroniser des attributs depuis un entrepôt de données vers l'espace de travail de destination, consultez [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/).
- **Exports depuis l'espace de travail source :** Utilisez [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) ou [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) pour extraire les données que vous êtes autorisé à déplacer, puis mappez-les dans `users/track` ou un CSV pour la destination. Respectez vos obligations en matière de rétention des données, de confidentialité et contractuelles lors de l'export et du rechargement des données.

{% alert note %}
La fusion de profils en double avec l'endpoint [Fusionner des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) ou les [utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/) dans le tableau de bord s'applique au sein d'un seul espace de travail, pas entre deux espaces de travail.
{% endalert %}

### Champs d'export utilisateur qui ne correspondent pas aux API de profil standard {#user-export-fields-that-dont-map-to-standard-profile-apis}

Lorsque vous reconstruisez des utilisateurs dans un espace de travail de destination à partir d'un [export utilisateur]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), certains champs d'export ne peuvent pas être réécrits dans les champs de profil standard de Braze via la REST API ou le CSV (de la manière dont le SDK et le serveur les remplissent). Vous pouvez souvent conserver les valeurs en tant qu'attributs personnalisés à la place. Soyez conscient des limites suivantes.

#### Informations sur l'appareil (`devices`) {#device-information-devices}

Les enregistrements d'appareils dans l'export sont remplis par le SDK. Vous ne pouvez pas migrer ces données dans les champs d'appareil standard de Braze via la REST API.

Si vous avez besoin de ces informations avant que l'utilisateur ne démarre une session dans une application ciblant l'espace de travail de destination, envoyez-les en tant qu'attributs personnalisés lors de l'import de l'utilisateur. Les filtres de segmentation standard et les références Liquid qui s'appuient sur les données d'appareil intégrées n'utilisent pas le payload d'appareil exporté tant que l'utilisateur n'ouvre pas une session sur une instance d'application connectée au nouvel espace de travail (lorsque le SDK actualise les champs d'appareil standard).

{% alert note %}
Ceci est distinct de la [migration des jetons de notification push](#push-tokens), qui utilise le champ `push_tokens` sur [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
{% endalert %}

#### Total des sessions et données de session par application (`apps` et `sessions` imbriqués) {#total-sessions-and-per-app-session-data-apps-and-nested-sessions}

Les totaux de sessions et les données de session imbriquées de l'objet `apps` dans un export ne peuvent pas être réimportés dans les mêmes champs intégrés. Pour conserver les compteurs historiques (par exemple, le total des sessions de l'espace de travail source), stockez-les dans des attributs personnalisés et segmentez sur ces champs dans l'espace de travail de destination.

Vous pouvez définir `date_of_first_session` et `date_of_last_session` via [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou l'import CSV. Pour les formats acceptés, consultez l'[objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) et l'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).

#### Compartiment aléatoire (`random_bucket`) {#random-bucket-random_bucket}

Chaque utilisateur se voit attribuer un [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/#random-bucket-number-update-events) dans son espace de travail. Cette valeur ne peut pas être réimportée ; l'utilisateur obtient un nouveau compartiment aléatoire dans l'espace de travail de destination.

Si vous vous appuyez sur l'ancien numéro pour des groupes de contrôle ou un échantillonnage (par exemple, exclure les utilisateurs dont le `random_bucket` est inférieur à un seuil), enregistrez la valeur exportée en tant qu'attribut personnalisé et construisez des segments ou des filtres sur cet attribut au lieu du champ de compartiment aléatoire intégré.

#### Champs d'attribution partenaire (`attributed_*`) {#partner-attribution-fields-attributed_}

Les champs d'attribution provenant des intégrations partenaires (les champs `attributed_*` dans un export) ne peuvent pas être définis sur les champs d'attribution standard de Braze via la REST API. Mappez-les vers des attributs personnalisés dans l'espace de travail de destination si vous devez les conserver pour la segmentation ou l'envoi de messages.

### Jetons de notification push {#push-tokens}

Lorsque les utilisateurs possèdent déjà des jetons de notification push provenant d'un fournisseur précédent ou d'une version antérieure de l'application, vous pouvez importer les jetons pour les applications mobiles via l'API, ou vous appuyer sur le SDK après l'intégration. Les jetons de notification push Web ont des limitations au niveau de l'API. Pour tous les détails et exemples, consultez [Migration des jetons de notification push]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens).

### WhatsApp

Les numéros de téléphone et les groupes d'abonnement peuvent être déplacés entre les espaces de travail avec un flux de transfert spécifique. Consultez [Transférer des numéros de téléphone WhatsApp et des groupes d'abonnement entre espaces de travail]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces/).

### Données d'engagement et d'analyse en dehors de Braze {#engagement-and-analytics-data-outside-braze}

Si vous avez besoin d'un historique des envois, ouvertures ou clics lors de la consolidation d'environnements, [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) et d'autres exports sont le moyen pris en charge pour transférer ces données dans votre entrepôt de données ou vos outils. Ces données ne sont pas réingérées dans Braze en tant qu'historique de messages natif par utilisateur sur un autre espace de travail.

## Avant de changer les clés SDK ou API {#before-you-change-sdk-or-api-keys}

Lorsque vous avez pointé votre application ou votre site vers un nouvel espace de travail :

- Les utilisateurs qui ouvrent l'application ou le site peuvent créer de nouveaux profils dans le nouvel espace de travail. Ils ne conservent pas automatiquement l'historique spécifique à l'espace de travail précédent.
- Si la même personne peut exister dans les deux espaces de travail, vous pouvez rencontrer des [scénarios de type doublon]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/#should-i-create-a-new-workspace-when-im-releasing-an-updated-app) (par exemple, une portée push qui se chevauche). Privilégiez un plan délibéré de données et de ciblage plutôt que de partager involontairement les clés de production et de staging.

{% alert tip %}
Pour les limites de suppression d'espaces de travail ou d'instances d'application, les déplacements de comptes spéciaux ou la planification de migrations à grande échelle, [contactez l'assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) avec vos liens de tableau de bord et un résumé des espaces de travail source et de destination.
{% endalert %}