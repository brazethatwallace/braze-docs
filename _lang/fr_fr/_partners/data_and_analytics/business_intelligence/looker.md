---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Cet article de référence décrit le partenariat entre Braze et Looker, une plateforme d'aide à la décision et d'analyse de big data."
page_type: partner
search_tag: Partner

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlooker-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderlooker}

> [Looker](https://looker.com/), une plateforme d'aide à la décision et d'analyse de big data, vous permet d'explorer, d'analyser et de partager des analyses commerciales en temps réel de façon fluide.

L'intégration de Braze et Looker permet aux utilisateurs de l'entreprise de tirer parti du signalement des utilisateurs via les [blocs Looker](#looker-blocks) et les [actions Looker](#looker-actions) de première partie via la REST API. Ces utilisateurs signalés peuvent être ajoutés à des Segments pour [cibler](#segment-users) de futures Campaigns ou Canvas Braze. Pour utiliser Looker avec Braze, nous vous recommandons d'envoyer vos données Braze vers un [entrepôt de données à l'aide de Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners), puis d'utiliser les blocs Looker de Braze pour modéliser et visualiser rapidement vos données Braze dans Looker.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Looker | Un [compte Looker](https://looker.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

### Considérations {#considerations}

- Ce processus ne fonctionne qu'avec les données qui n'ont pas été pivotées.
- L'API traite un maximum de 100 000 lignes à la fois.
- Le nombre final de drapeaux d'un utilisateur peut être inférieur en raison de doublons ou de non-utilisateurs.

## Intégration {#integration}

### Blocs Looker {#looker-blocks}

Nos blocs Looker aident les clients de Braze à accéder rapidement à une vue des données granulaires que nous proposons via [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents). Nos blocs fournissent des visualisations et une modélisation prédéfinies pour les données Currents afin que les clients de Braze puissent facilement mettre en œuvre des modèles analytiques tels que la rétention, évaluer la livrabilité des messages, examiner plus en détail le comportement des utilisateurs, et bien plus encore.

Pour mettre en œuvre les blocs Looker, suivez les instructions fournies dans les fichiers README du code GitHub.
- [README du bloc d'analyse de l'engagement des messages](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [README du bloc d'analyse du comportement des utilisateurs](https://github.com/llooker/braze_retention_block/blob/master/README.md)

Les deux intégrations supposent que votre [intégration Braze initiale]({{site.baseurl}}/user_guide/get_started/sdk_overview), ainsi que votre intégration Braze avec un [entrepôt de données compatible Looker](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), sont correctement configurées pour capturer et envoyer les données nécessaires.


{% alert important %}
Braze a construit ses blocs Looker en utilisant [Snowflake](https://www.snowflake.com/) comme entrepôt de données. Bien que nous souhaitions que nos blocs fonctionnent avec autant d'entrepôts de données que possible, certaines fonctions SQL peuvent différer en termes de disponibilité, de syntaxe ou de comportement selon les dialectes.
{% endalert %}

{% alert warning %}
Soyez conscient des différentes conventions de dénomination ! Les noms personnalisés peuvent provoquer des incohérences dans les données, sauf si vous modifiez tous les noms correspondants. Si vous avez personnalisé un nom de vue/table ou de modèle, renommez-le dans LookML avec le nom que vous avez sélectionné.
{% endalert %}

### Blocs disponibles {#available-blocks}

| Bloc | Description |
|---|---|
| Bloc d'analyse de l'engagement des messages | Ce bloc comprend des données relatives aux événements de notification push, d'e-mail, de messages in-app, de webhook, de conversion, d'entrée dans Canvas et d'inscription au groupe de contrôle de Campaign. <br><br>En savoir plus sur ce [bloc Looker](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), ou consultez le [code GitHub](https://github.com/llooker/braze_message_engagement_block). |
| Bloc d'analyse du comportement des utilisateurs | Ce bloc comprend des données relatives aux événements personnalisés, aux achats, aux sessions, aux événements de localisation et aux désinstallations.<br><br>En savoir plus sur ce [bloc Looker](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), ou consultez le [code GitHub](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Blocs disponibles" }

### Actions Looker {#looker-actions}

Les actions Looker vous permettent de signaler des utilisateurs dans Braze via l'endpoint de la REST API à partir d'un Looker Look. Les actions nécessitent qu'une dimension soit balisée avec `braze_id`. L'action ajoutera la valeur signalée à l'attribut personnalisé `looker_export` de l'utilisateur.

{% alert important %}
Seuls les utilisateurs existants seront signalés. Vous ne pouvez pas utiliser les Looks pivotés lorsque vous signalez des données dans Braze.
{% endalert %}

#### Étape 1 : Configurer une action Braze Looker {#step-1-set-up-a-braze-looker-action}

Configurez une action Braze Looker avec votre clé API REST de Braze et votre endpoint REST.

![La page de configuration Looker Braze. Vous trouverez ici des champs pour la clé API Braze et l'endpoint de la REST API Braze.]({% image_buster /assets/img/braze-looker-action.png %})

#### Étape 2 : Configurer Looker Develop {#step-2-set-up-looker-develop}

Dans Looker Develop, sélectionnez les vues appropriées. Ajoutez `braze_id` à la balise des dimensions et validez les modifications.
Cette balise `braze_id` est utilisée pour déterminer quel champ est la clé unique.

```lookml
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Assurez-vous de valider les modifications. L'action Looker ne fonctionnera qu'avec les paramètres de production.**

#### Étape 3 : Définir les attributs utilisateur dans les balises {#step-3-set-user-attributes-in-tags}

Optionnellement, n'importe quel attribut peut être défini à l'aide d'une balise `braze[]` avec le nom de l'attribut entre crochets. Par exemple, si vous souhaitez qu'un attribut personnalisé `user_segment` soit envoyé, la balise serait `braze[user_segment]`.

Notez les limites suivantes :
- Les attributs ne seront envoyés que s'ils **sont inclus en tant que champ dans le Look**.
- Les types pris en charge sont `Strings`, `Boolean`, `Numbers` et `Dates`.
- Les noms d'attributs sont sensibles à la casse.
- Les attributs standard peuvent également être définis à condition qu'ils correspondent exactement aux noms du [profil utilisateur standard]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields).
- La balise complète doit être mise en forme entre guillemets. Par exemple, `tags: ["braze[first_name]"]`. D'autres balises peuvent également être attribuées mais seront ignorées.
- Des informations supplémentaires sont disponibles sur [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Étape 4 : Envoyer l'action Looker {#step-4-send-the-looker-action}

1. Dans un Look dont une dimension `braze_id` est sélectionnée, cliquez sur l'icône d'engrenage (<i class="fas fa-cog"></i>) dans la barre d'outils, puis sélectionnez **Send...**.
2. Sélectionnez l'action Braze personnalisée.
3. Sous **Unique Key**, indiquez la clé de mappage utilisateur principale pour le compte Braze (`external_id` ou `braze_id`).
4. Donnez un nom à l'exportation. Si aucun nom n'est fourni, `LOOKER_EXPORT` sera utilisé.
5. Sous **Advanced Options**, sélectionnez **Results in Table** ou **All Results**, puis **Send**.<br><br>![Boîte de dialogue d'envoi Looker avec l'action Braze et les options avancées sélectionnées.]({% image_buster /assets/img/send-looker-action.png %})<br><br>Si l'exportation a été correctement envoyée, `LOOKER_EXPORT` devrait apparaître dans le profil de l'utilisateur sous la forme d'un attribut personnalisé avec la valeur que vous avez saisie dans l'action.<br><br>![Profil utilisateur Braze affichant la valeur de l'attribut personnalisé LOOKER_EXPORT.]({% image_buster /assets/img/custom-attributes-looker.png %})

##### Exemple d'appel API sortant {#example-outgoing-api}

Voici un exemple d'appel API sortant, qui sera envoyé à l'[endpoint `/users/track/`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

###### En-tête {#header}
```
Authorization: Bearer [API_KEY]
```

###### Corps {#body}
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Segmenter les utilisateurs dans Braze {#segment-users}

Dans Braze, pour créer un Segment avec ces utilisateurs signalés, naviguez vers **Segments** sous **Engagement**, nommez votre Segment et sélectionnez **Looker_Export** comme filtre. Ensuite, utilisez l'option « inclut la valeur » et fournissez le drapeau d'attribut personnalisé que vous avez attribué dans Looker.

![Dans le générateur de Segments Braze, le filtre « looker_export » est réglé sur « includes_value » et « Looker ».]({% image_buster /assets/img/braze_segments.png %})

Une fois enregistré, vous pouvez faire référence à ce Segment lors de la création d'un Canvas ou d'une Campaign à l'étape du ciblage des utilisateurs.

## Résolution des problèmes {#troubleshooting}

Si vous rencontrez des problèmes avec l'action Looker, ajoutez un utilisateur test aux [groupes internes]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups) et vérifiez les points suivants :

* La clé API possède les autorisations `users.track`.
* L'endpoint REST correct est saisi, par exemple `https://rest.iad-01.braze.com`.
* Une balise `braze_id` est définie dans la vue de dimension.
* Votre requête inclut la dimension ou l'attribut Id sous forme de colonne.
* Les résultats de Looker ne sont pas pivotés.
* La clé unique est correctement sélectionnée. Habituellement, il s'agit de `external_id`.
* Le `braze_id` dans la dimension est différent du `braze_id` dans l'API. Le `braze_id` dans la dimension est utilisé pour indiquer qu'il s'agit du champ `id` pour l'API Braze. Dans la plupart des cas, lors de l'envoi, `external_id` est la clé primaire.
* L'utilisateur `external_id` existe sur la plateforme Braze.
* Le champ `looker_export` est défini comme `Automatically Detect` sous `Braze Platform > Settings > Manage Settings > Custom Attributes`.
* Les modifications sont validées en production. L'action Looker fonctionne avec les paramètres de production.