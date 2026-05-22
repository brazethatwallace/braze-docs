---
nav_title: Bonnes pratiques
hidden: true
---

# Bonnes pratiques pour le cycle de vie des utilisateurs et les identifiants {#user-lifecycle-and-identifiers-best-practices}

## Collecte des données {#data-collection}

En savoir plus sur la manière dont Braze collecte les données :
- [Collecte de données par le SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/)
- [Bonnes pratiques en matière de collecte de données]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices/)
- [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)

## Identifiants Braze {#braze-identifiers}

- `braze_id` : un identifiant attribué par Braze, immuable et associé à un utilisateur particulier lors de sa création dans notre base de données.
- `external_id` : un identifiant attribué par le client, généralement un UUID. Nous recommandons aux clients d'attribuer l'`external_id` lorsque l'utilisateur peut être identifié de manière unique. Une fois qu'un utilisateur est identifié, il ne peut pas redevenir anonyme.
- `user_alias` : un identifiant alternatif unique que le client peut attribuer pour référencer l'utilisateur par un ID avant l'attribution d'un `external_id`. Les alias d'utilisateur peuvent ensuite être fusionnés avec d'autres alias ou un `external_id` lorsqu'un identifiant devient disponible via l'endpoint Braze [Identifier l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
    - Dans l'endpoint [Identifier l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), le champ `merge_behavior` peut être utilisé pour spécifier quelles données du profil d'alias utilisateur doivent être conservées dans le profil utilisateur connu.
    - Notez que pour que l'alias d'utilisateur soit un profil pouvant recevoir des envois, vous devez toujours inclure l'e-mail et/ou le téléphone comme attribut standard du profil.
- `device_id` : un identifiant spécifique à l'appareil, généré automatiquement. Un profil utilisateur peut être associé à plusieurs `device_ids`. Par exemple, un utilisateur qui s'est connecté à son compte sur son ordinateur professionnel, son ordinateur personnel, sa tablette et son application iOS aurait 4 `device_ids` associés à son profil.
- Adresse e-mail et numéro de téléphone :
    - Pris en charge en tant qu'identifiant dans l'endpoint de suivi des utilisateurs de Braze.
    - Lorsque l'adresse e-mail ou le numéro de téléphone est utilisé comme identifiant dans une requête, trois résultats sont possibles :
        1. Si un utilisateur avec cet e-mail/téléphone n'existe pas dans Braze, un profil utilisateur e-mail uniquement ou téléphone uniquement sera créé, et toutes les données de la requête seront ajoutées au profil.
        2. Si un profil avec cet e-mail/téléphone existe déjà dans Braze, il sera mis à jour pour inclure toutes les données envoyées dans la requête.
        3. Dans un cas d'utilisation avec plus d'un profil ayant cet e-mail/téléphone, le profil le plus récemment mis à jour sera prioritaire.
    - Notez que si un profil utilisateur e-mail uniquement ou téléphone uniquement existe et qu'un profil identifié avec le même e-mail/téléphone est ensuite créé (par exemple un autre profil avec la même adresse e-mail ET un ID externe), Braze créera un second profil. Les mises à jour ultérieures seront dirigées vers le profil portant l'ID externe.
        - Les deux profils peuvent être fusionnés à l'aide de l'endpoint Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)

## Gestion des utilisateurs anonymes {#handling-anonymous-users}

Dans le cas où vous devez créer ou mettre à jour un profil utilisateur dans Braze sans avoir accès à un `external_id`, un autre identifiant tel qu'une adresse e-mail ou un numéro de téléphone peut être transmis à l'endpoint Braze [Exporter l'utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour déterminer si un profil pour cet utilisateur existe dans Braze.

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Si un utilisateur existe dans Braze avec cet e-mail ou ce téléphone, son profil sera renvoyé. Sinon, un tableau « users » vide sera renvoyé. L'avantage d'utiliser l'endpoint d'exportation pour déterminer si un utilisateur avec cette adresse e-mail existe déjà est que cela vous permettra de savoir si des profils utilisateurs anonymes sont associés à cet utilisateur. Par exemple, un profil anonyme créé via le SDK (qui aura un `braze_id`) ou un profil d'alias d'utilisateur créé précédemment.

Si la requête ne renvoie pas de profil utilisateur, vous pouvez choisir de créer un alias d'utilisateur ou de créer un utilisateur e-mail uniquement :

### Alias d'utilisateur {#user-alias}

Utilisez l'endpoint de suivi des utilisateurs pour créer un alias d'utilisateur, en utilisant l'identifiant de votre choix comme nom d'alias. En incluant `_update_existing_only` avec la valeur `false` dans l'objet attribut, événement ou achat où le nouvel alias d'utilisateur est défini, vous pouvez créer le profil d'alias et ajouter simultanément des attributs, des événements et des achats à ce profil.

Pour que l'alias d'utilisateur soit un profil pouvant recevoir des envois, vous devez inclure l'adresse e-mail dans le champ `email`, comme indiqué ci-dessous.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Vous pouvez par la suite identifier et fusionner cet alias d'utilisateur avec un `external_id` lorsqu'un identifiant devient disponible via notre endpoint [Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).

### Création d'un utilisateur e-mail uniquement {#creating-an-email-only-user}

Utilisez l'adresse e-mail comme identifiant dans l'endpoint de suivi des utilisateurs.

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Cette fonctionnalité est en accès anticipé.
{% endalert %}

## Synchronisation des données avec les profils utilisateurs {#syncing-data-to-user-profiles}

[Suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- Il s'agit d'un endpoint accessible au public qui peut créer et mettre à jour des utilisateurs dans Braze, par exemple en enregistrant des attributs dans le profil utilisateur. Cet endpoint a une limite de débit de 50 000 requêtes par minute appliquée au niveau de l'espace de travail.
- Lorsque vous utilisez cet endpoint, incluez la clé `partner` comme indiqué dans notre documentation pour les partenaires.

[Ingestion de données cloud]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- Comme pour l'endpoint de suivi des utilisateurs, les données peuvent être synchronisées avec les profils utilisateurs par le biais de l'Ingestion de données cloud. Lorsque vous utilisez cet outil, les attributs, les événements et les achats sont enregistrés dans les profils en configurant et en connectant la table ou la vue de l'entrepôt de données que vous souhaitez synchroniser avec l'espace de travail Braze souhaité.

[Points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)
- Braze dispose d'un modèle de points de données dans lequel les points de données sont enregistrés par « écriture » dans le profil utilisateur, que la valeur ait changé ou non. C'est pourquoi nous recommandons de n'envoyer à Braze que les attributs qui ont été modifiés.

## Envoi d'audiences d'utilisateurs à Braze {#sending-audiences-of-users-to-braze}

[Documentation sur les partenaires de synchronisation d'importation de cohorte]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- Les audiences d'utilisateurs peuvent être synchronisées vers Braze en tant que cohorte à l'aide des endpoints de l'API d'importation de cohorte de Braze. Plutôt que de stocker ces audiences dans le profil utilisateur sous forme d'attributs, les clients peuvent créer et cibler cette cohorte à l'aide d'un filtre propre au partenaire dans notre outil de segmentation. Cela vous permet de trouver et de cibler plus efficacement un segment particulier d'utilisateurs.
- Les endpoints d'importation de cohorte ne sont pas publics et sont spécifiques à chaque partenaire. Pour cette raison, les synchronisations vers les endpoints de cohorte ne seront pas comptabilisées dans les limites de débit de l'espace de travail d'un client.

[Suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- Il s'agit d'un endpoint accessible au public qui peut être utilisé immédiatement pour créer des utilisateurs dans Braze en désignant un utilisateur dans une audience particulière par le biais d'un attribut utilisateur. La principale différence entre cet endpoint et l'endpoint d'importation de cohorte est que les audiences envoyées à l'aide de cet endpoint seront stockées dans le profil utilisateur, tandis que l'endpoint d'importation de cohorte apparaîtra comme un filtre dans notre outil de segmentation. Cet endpoint a une limite de débit de 50 000 requêtes par minute appliquée au niveau de l'espace de travail.
- Lorsque vous utilisez cet endpoint, assurez-vous d'inclure la clé `partner` comme indiqué dans notre [documentation pour les partenaires]({{site.baseurl}}/partners/isv_partners/api_partner/).

[Points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)<br>
- Braze dispose d'un modèle de points de données dans lequel les points de données sont enregistrés par « écriture » dans le profil utilisateur, que la valeur ait changé ou non.
- Les points de données sont générés à la fois par l'importation de cohorte et par les endpoints de suivi des utilisateurs.

## Diffusion en continu des analyses d'engagement vers le partenaire {#engagement-analytics-streaming-to-partner}

### Currents

Currents est un outil de diffusion en continu et en temps quasi réel des analyses d'engagement des messages dans Braze. Il transmet des données au niveau de l'utilisateur pour tous les envois, livraisons, ouvertures, clics, etc., pour les Campaigns et les Canvas envoyés depuis l'espace de travail du client. Quelques points à noter : Currents est tarifé par connecteur pour le client, de sorte que tous les nouveaux partenaires Currents doivent passer par un processus d'accès anticipé (EA). Nous demandons à nos partenaires d'avoir cinq clients dans le cadre de l'EA avant de créer l'interface utilisateur personnalisée et de rendre le connecteur disponible publiquement.
- [Documentation du partenaire]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector/)
- [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) — tous les clients qui achètent un connecteur Currents auront accès à ces événements.
- [Événements liés au comportement de l'utilisateur]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) — tous les clients qui achètent un connecteur Currents n'achètent pas nécessairement un connecteur « tous les événements » qui inclura ces événements.

### Partage de données Snowflake {#snowflake-data-share}

Les clients qui achètent un connecteur Snowflake Data Share auront automatiquement accès aux événements d'engagement des messages et de comportement des utilisateurs. Lorsque Snowflake Data Share est utilisé en tant qu'intégration de partenaire, Braze provisionne un partage sur l'instance Snowflake du partenaire au nom du client. Le partage de données inter-régions ayant un coût plus élevé pour nos clients, nous demandons aux partenaires souhaitant s'intégrer à Snowflake de prévoir un compte dans `US-EAST-1` et/ou `EU-CENTRAL-1`.
- [Documentation du partenaire]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector/)

## Créer et déclencher des Campaigns et des Canvas {#building-and-triggering-campaigns-and-canvases}

### Créer des ressources dans Braze {#creating-assets-in-braze}
Braze propose un certain nombre d'endpoints qui permettent aux clients et aux partenaires de créer ou mettre à jour des modèles d'e-mail et des Content Blocks dans l'espace de travail d'un client. Ces modèles et Content Blocks peuvent ensuite être utilisés dans les Campaigns et Canvas Braze du client.
- Modèles d'e-mail
    - [Endpoint de création de modèle]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [Endpoint de mise à jour de modèle]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)
    - [Endpoint de création de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [Endpoint de mise à jour de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### Campaigns et Canvas déclenchés par l'API {#api-triggered-campaigns-and-canvases}

Les clients peuvent configurer des Campaigns et des Canvas pour qu'ils soient déclenchés par l'API. Les requêtes API pour déclencher ces Campaigns peuvent être utilisées pour personnaliser et segmenter davantage la Campaign en transmettant des propriétés de déclenchement API et des paramètres d'audience ou de destinataire.
- [Déclencher des Campaigns via l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - Les Campaigns sont des messages individuels, tels que des e-mails distincts.
- [Déclencher des Canvas via l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - Canvas est une interface unifiée où les marketeurs peuvent créer des campagnes avec plusieurs messages et étapes pour former un parcours cohérent. Lorsque vous déclenchez un Canvas, vous faites entrer un utilisateur dans le flux Canvas, où il continuera à recevoir des messages jusqu'à ce qu'il ne corresponde plus aux critères du Canvas.
- [Propriétés de déclenchement API / propriétés d'entrée Canvas]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)
    - Données qui peuvent être intégrées de manière dynamique dans le message au moment de l'envoi.

### Campaigns API {#api-campaigns}
Lors de la création de Campaigns API (différentes des Campaigns déclenchées par l'API mentionnées ci-dessus), le tableau de bord de Braze est uniquement utilisé pour générer un `campaign_id`, qui permet au client de suivre les analyses pour le reporting de la Campaign. Le message de la Campaign lui-même est défini dans la requête API.
- [Envoyer immédiatement une Campaign API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [Planifier une Campaign API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### ID d'envoi {#send-ids}
Utilisez l'endpoint Braze pour générer un ID d'envoi qui peut être utilisé pour ventiler les analyses de la Campaign par envoi. Par exemple, si un `campaign_id` (Campaign API) est créé par emplacement, un ID d'envoi pourrait être généré par envoi pour suivre l'efficacité des différents messages pour un emplacement particulier.
- [ID d'envoi]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## Contenu connecté {#connected-content}

Le contenu connecté peut être utilisé dans n'importe quel type de canal pour envoyer une requête API à l'endpoint spécifié au moment de l'envoi et intégrer dans le message ce qui est renvoyé dans la réponse.

La polyvalence du contenu connecté en fait une fonctionnalité utilisée par nombre de nos clients pour insérer des contenus qui n'existent pas ou ne peuvent pas être hébergés dans Braze. Voici quelques-uns des cas d'utilisation les plus courants :
- Intégration de contenu de blog ou d'article dans les messages
- Recommandations de contenu
- Métadonnées de produit
- Localisation et traduction

Points importants à connaître :
- Braze ne facture pas les appels API et ceux-ci ne sont pas comptabilisés dans votre consommation de points de données.
- Les réponses du contenu connecté sont limitées à 1 Mo.
- Les appels de contenu connecté sont effectués lors de l'envoi du message, sauf pour les messages in-app, pour lesquels l'appel est effectué lors de la consultation du message.
- Les appels de contenu connecté ne suivent pas les redirections. Braze exige que le temps de réponse du serveur soit inférieur à 2 secondes pour des raisons de performances ; si le serveur met plus de 2 secondes à répondre, le contenu ne sera pas inséré.
- Les systèmes de Braze peuvent effectuer le même appel API de contenu connecté plus d'une fois par destinataire. Cela est dû au fait que Braze peut avoir besoin d'effectuer un appel API de contenu connecté pour générer le payload d'un message, et les payloads de message peuvent être générés plusieurs fois par destinataire pour des raisons de validation, de logique de nouvelle tentative ou d'autres besoins internes.

Consultez ces articles pour en savoir plus sur le contenu connecté :
- [Effectuer un appel de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)
- [Abandonner un contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/)
- [Nouvelles tentatives de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries/)