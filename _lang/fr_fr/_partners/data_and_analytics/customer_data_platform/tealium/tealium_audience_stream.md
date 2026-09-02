---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Cet article de référence présente le partenariat entre Braze et Tealium, un centre de données universel qui vous permet de connecter des données mobiles, web et alternatives à d'autres sources tierces."
page_type: partner
search_tag: Partner
---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) est un moteur omnicanal de segmentation client et d'action en temps réel. AudienceStream exploite les données qui affluent dans EventStream et crée des profils de visiteurs représentant les attributs les plus importants de l'engagement de vos clients avec votre marque.

L'intégration entre Braze et Tealium s'appuie sur les profils de visiteurs d'AudienceStream. Les comportements partagés segmentent ces profils pour créer des ensembles de visiteurs présentant des traits communs, appelés audiences. Ces audiences peuvent contribuer à alimenter votre pile technologique marketing en temps réel via des connecteurs.

{% alert important %}
Tealium AudienceStreams et EventStreams offrent à la fois des actions de connecteur par lots et non par lots. Le connecteur non par lots doit être utilisé lorsque les requêtes en temps réel sont importantes pour le cas d'usage et qu'il n'y a pas de préoccupation quant au respect des spécifications de limitation du débit de l'API Braze. Contactez l'[assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) de Braze ou votre gestionnaire du succès des clients si vous avez des questions.
{% endalert %}

## Prérequis {#prerequisites}

| Nom | Description |
| ---- | ----------- |
| Compte Tealium | Un [compte Tealium](https://my.tealiumiq.com/) avec un accès côté serveur est requis. Nous recommandons également d'utiliser les intégrations côté client pour tirer parti de ce partenariat. |
| Clé API REST | Une clé API REST Braze avec les permissions `users.track`, `users.delete` et `subscription.status.set`.<br><br>Celle-ci peut être créée dans **Tableau de bord de Braze > Console de développement > Clé API REST > Créer une nouvelle clé API** |
| [Endpoint REST Braze]({{site.baseurl}}/api/basics#endpoints) | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL Braze de votre instance]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Configurer les attributs et les badges {#step-1-set-up-attributes-and-badges}

#### Comprendre les attributs {#understanding-attributes}

La première étape de l'utilisation d'AudienceStream consiste à créer des attributs. Les attributs vous permettent de définir les caractéristiques importantes représentant les habitudes, les préférences, les actions et l'engagement d'un visiteur avec votre marque.

**Attributs de visite** : Les attributs de visite se rapportent à la visite (ou session) en cours de l'utilisateur. Les données stockées dans ces attributs persistent pendant toute la durée de la visite. Voici quelques exemples d'attributs de visite :
- Durée de visite (Number)
- Navigateur actuel (String)
- Appareil actuel (String)
- Nombre de pages vues (Number)

**Attributs de visiteur** : Les attributs de visiteur se rapportent à l'utilisateur actuel. Les données stockées dans ces attributs persistent pendant toute la durée de vie de l'utilisateur. Voici quelques exemples d'attributs de visiteur :
- Valeur des commandes sur la durée de vie (Number)
- Prénom (String)
- Date de naissance (Date)
- Marques achetées (Tally)

Consultez la documentation [Tealium](https://docs.tealium.com/server-side/attributes/about/) pour obtenir la liste complète des types de données disponibles.

##### Enrichissement des attributs {#attribute-enrichment}

Une fois que vous avez identifié les attributs souhaités, vous pouvez les configurer avec des [enrichissements](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) — des règles métier qui déterminent quand et comment mettre à jour les valeurs des attributs. Chaque type de données propose sa propre sélection d'enrichissements pour manipuler la valeur de l'attribut. Cela est associé au paramètre « WHEN ». Les options suivantes sont disponibles pour chaque attribut de visite et de visiteur :

- New Visitor : se produit la première fois qu'un visiteur accède à votre site.
- New Visit : se produit lors d'une nouvelle visite d'un visiteur.
- Any Event : se produit sur n'importe quel événement.
- Visit Ended : se produit lorsqu'une visite se termine.

Vous pouvez également créer une condition personnalisée, appelée règle, qui déterminera quand l'enrichissement se produira.

#### Badges

Les badges sont des attributs de visiteur spéciaux qui représentent des modèles de comportement précieux. Les badges sont attribués ou retirés aux visiteurs en fonction de la logique de leurs enrichissements. Cette logique combine généralement plusieurs conditions pour capturer des Segments de visiteurs ou définir un seuil pour quand une valeur particulière est atteinte.

#### Exemple d'attribut et de badge {#attribute-and-badge-example}

{% tabs local %}
{% tab Attribut %}

Créez un attribut de visiteur « Lifetime Order Value » qui calcule le montant cumulé dépensé (`order_total`) par le client pour toutes les commandes terminées (événement d'achat). Pour configurer la valeur des commandes sur la durée de vie dans votre compte Tealium, suivez les instructions suivantes :

1. Accédez à **AudienceStream > Visitor/Visit Attributes** et cliquez sur **Add Attribute**.
2. Sélectionnez la portée **Visitor** et cliquez sur **Continue**.
3. Sélectionnez le type de données **Number** et cliquez sur **Continue**.
4. Saisissez le nom de l'attribut, « Lifetime Order Value ».
5. Cliquez sur **Add Enrichment** et sélectionnez **Increment or Decrement Number**.
6. Sélectionnez l'attribut contenant la valeur à incrémenter (`order_total`).
7. Laissez le paramètre « WHEN » défini sur « Any Event », puis cliquez sur **Create a New Rule**.
8. Créez une règle qui identifie quand un événement d'achat s'est produit.
9. Cliquez sur **Save**, puis sur **Finish**.

Désormais, tous les clients auront un attribut de valeur des commandes sur la durée de vie qui leur est associé.

{% endtab %}
{% tab Badge %}

Vous pouvez créer des badges qui vous aident à classer et cibler vos utilisateurs en fonction de certains attributs qu'ils partagent. Dans l'exemple suivant, nous créons un badge VIP pour les utilisateurs dont la « Lifetime Order Value » dépasse 500 $.

1. Accédez à **AudienceStream > Visitor/Visit Attributes** et cliquez sur **Add Attribute**.
2. Sélectionnez la portée **Visitor** et cliquez sur **Continue**.
3. Sélectionnez le type de données **Badge** et cliquez sur **Continue**.
4. Saisissez le nom du badge, « VIP ».
5. Cliquez sur **Add Enrichment** et sélectionnez **Assign Badge**.
6. Laissez le paramètre « WHEN » défini sur « Any Event ».
7. Créez une règle pour l'attribution du badge en sélectionnant **Create Rule**. Attribuez un titre à cette règle et, en utilisant l'attribut créé précédemment, définissez la règle sur « ...has attribute "Lifetime Order Value greater than 500" ».
8. Cliquez sur **Save**, puis sur **Finish**.

{% endtab %}
{% endtabs %}

### Étape 2 : Créer une audience {#step-2-create-an-audience}

Depuis la page d'accueil Tealium, sélectionnez **Audiences** sous **AudienceStream** dans la navigation latérale. Ici, vous pouvez créer une audience d'utilisateurs partageant des attributs communs. L'entrée ou la sortie d'un utilisateur de cette audience sera le déclencheur de l'action du connecteur, configurée à l'étape suivante, qui transmettra ces informations au profil utilisateur dans Braze.

Tout d'abord, nommez votre audience, puis réfléchissez aux attributs qui s'appliqueraient au type d'audience que vous essayez de créer. Par exemple, pour créer une audience d'utilisateurs VIP, vous pourriez créer une audience de visiteurs possédant le **badge VIP**.

Assurez-vous d'**enregistrer / publier** votre audience lorsque vous avez terminé.

### Étape 3 : Créer un connecteur d'événement {#step-3-create-an-event-connector}

Un connecteur est une intégration entre Tealium et un autre fournisseur utilisée pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API prises en charge par leur partenaire.

1. Depuis la barre latérale de Tealium sous **Server-Side**, accédez à **AudienceStream > Audience Connectors**.
2. Sélectionnez le bouton bleu **+ Add Connector** pour parcourir la marketplace de connecteurs. Dans la nouvelle boîte de dialogue qui apparaît, utilisez la recherche rapide pour trouver le connecteur **Braze**.
3. Pour ajouter ce connecteur, cliquez sur la tuile du connecteur **Braze**. Lorsque vous cliquez dessus, vous pouvez voir le résumé de la connexion et la liste des informations requises, des actions prises en charge et des instructions de configuration. La configuration comprend trois étapes : source, configuration et action.

#### Source

Dans la boîte de dialogue **Source** qui apparaît, sélectionnez l'audience que vous avez créée à l'étape précédente et un déclencheur approprié à votre situation. Vous pouvez également activer la limitation de fréquence pour contrôler la fréquence à laquelle cette action se déclenche.

![Configuration de la source du connecteur Tealium AudienceStream avec sélection de l'audience et du déclencheur.]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuration

Ensuite, une boîte de dialogue **Configuration** apparaît. Sélectionnez **Add Connector** en bas de la page. Nommez votre connecteur et fournissez ici votre endpoint d'API Braze et votre clé REST API Braze.

![Boîte de dialogue de configuration du connecteur Tealium avec les champs endpoint Braze et clé REST API.]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si vous avez déjà créé un connecteur auparavant, vous pouvez éventuellement en utiliser un existant dans la liste des connecteurs disponibles et le modifier selon vos besoins avec l'icône de crayon ou le supprimer avec l'icône de corbeille.

Après avoir créé ou sélectionné un connecteur à associer à cette audience, cliquez sur Done pour continuer.

#### Action

Ensuite, nommez l'action de votre connecteur et sélectionnez un type d'action qui enverra les données selon le mappage que vous configurez. Ici, vous allez mapper les attributs Braze aux noms d'attributs Tealium. Selon le type d'action que vous choisissez, une sélection variable de champs sera requise par Tealium. Voici des exemples et des explications de ces champs.

{% alert important %}
Tous les champs proposés ne sont pas obligatoires.

![Panneau de mappage d'action Tealium montrant les champs optionnels pouvant être réduits.]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Suivre l'utilisateur - Par lots et sans lots %}

Cette action vous permet de suivre les attributs d'utilisateur, d'événement et d'achat en une seule action. Bien que l'action Track User soit la même pour AudienceStream et EventStream, Tealium recommande de configurer les mappages d'attributs utilisateur avec les actions AudienceStream et les mappages d'événements et d'achats avec les actions EventStream.

| Paramètres | Description |
| ---------- | ----------- |
| User ID | Utilisez ce champ pour mapper le champ d'ID utilisateur Tealium à son équivalent Braze. Mappez un ou plusieurs attributs d'ID utilisateur. Lorsque plusieurs ID sont spécifiés, la première valeur non vide est sélectionnée selon l'ordre de priorité suivant : External ID, Braze ID, Alias Name et Alias Label.<br><br>- External ID et Braze ID ne doivent pas être spécifiés si vous importez des jetons de notification push.<br>- Si vous spécifiez un alias d'utilisateur, le nom d'alias et le libellé d'alias doivent être définis. <br><br>Pour plus d'informations, consultez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze. |
| User attributes | Utilisez les noms de champs existants du profil utilisateur Braze pour mettre à jour les valeurs du profil utilisateur dans le tableau de bord de Braze ou ajoutez vos propres données d'[attribut utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object) personnalisé aux profils utilisateur.<br><br>- Par défaut, de nouveaux utilisateurs sont créés si aucun n'existe.<br>- En définissant **Update Existing Only** sur `true`, seuls les utilisateurs existants sont mis à jour et aucun nouvel utilisateur n'est créé.<br>- Si un attribut Tealium est vide, il est converti en null et supprimé du profil utilisateur Braze. Les enrichissements doivent être utilisés si les valeurs null ne doivent pas être envoyées à Braze pour supprimer un attribut utilisateur. |
| Modify user attributes | Utilisez ce champ pour incrémenter ou décrémenter certains attributs utilisateur<br><br>- Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>- Les attributs de type tableau peuvent être modifiés en ajoutant ou en supprimant des valeurs des tableaux existants. |
| Event | Un événement représente une occurrence unique d'un événement personnalisé par un utilisateur particulier à un horodatage donné. Utilisez ce champ pour suivre et mapper les attributs d'événement comme ceux de l'[objet événement]({{site.baseurl}}/api/objects_filters/event_object) Braze. <br><br>- L'attribut d'événement `Name` est obligatoire pour chaque événement mappé.<br>- L'attribut d'événement `Time` est automatiquement défini sur l'heure actuelle sauf s'il est explicitement mappé. <br>- Par défaut, de nouveaux événements seront créés si aucun n'existe. En définissant `Update Existing Only` sur `true`, seuls les événements existants seront mis à jour et aucun nouvel événement ne sera créé.<br>-  Mappez les attributs de type tableau pour ajouter plusieurs événements. Les attributs de type tableau doivent être de longueur égale.<br>- Les attributs à valeur unique peuvent être utilisés et appliqués à chaque événement. |
| Event template | Fournissez des modèles d'événement à référencer dans les données du corps. Les modèles peuvent être utilisés pour transformer les données avant de les envoyer à Braze. Consultez le [guide des modèles](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium pour en savoir plus. |
| Event template variable | Fournissez des variables de modèle d'événement comme entrée de données. Consultez le [guide des variables de modèle](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium pour en savoir plus. |
| Purchase | Utilisez ce champ pour suivre et mapper les attributs d'achat utilisateur comme ceux de l'[objet achat]({{site.baseurl}}/api/objects_filters/purchase_object) Braze.<br><br>- Les attributs d'achat `Product ID`, `Currency` et `Price` sont obligatoires pour chaque achat mappé.<br>- L'attribut d'achat `Time` est automatiquement défini sur l'heure actuelle sauf s'il est explicitement mappé.<br>- Par défaut, de nouveaux achats seront créés si aucun n'existe. En définissant `Update Existing Only` sur `true`, seuls les achats existants seront mis à jour et aucun nouvel achat ne sera créé.<br>- Mappez les attributs de type tableau pour ajouter plusieurs articles d'achat. Les attributs de type tableau doivent être de longueur égale.<br>- Les attributs à valeur unique peuvent être utilisés et s'appliqueront à chaque article.|
| Purchase template | Les modèles peuvent être utilisés pour transformer les données avant leur envoi à Braze.<br>- Définissez un modèle d'achat si vous avez besoin de la prise en charge d'objets imbriqués.<br>- Lorsqu'un modèle d'achat est défini, la configuration établie dans la section achats de votre action sera ignorée.<br>- Consultez le [guide des modèles](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium pour en savoir plus.|
| Purchase template variable | Fournissez des variables de modèle de produit comme entrée de données. Consultez le [guide des variables de modèle](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium pour en savoir plus. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Action" }

![Exemple d'action Track User Tealium avec des attributs utilisateur et des champs d'événement mappés.]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Supprimer l'utilisateur - Sans lots %}

Cette action vous permet de supprimer des utilisateurs du tableau de bord de Braze.

| Paramètres | Description |
| ---------- | ----------- |
| User ID | Utilisez ce champ pour mapper le champ d'ID utilisateur Tealium à son équivalent Braze.<br><br>- Mappez un ou plusieurs attributs d'ID utilisateur. Lorsque plusieurs ID sont spécifiés, la première valeur non vide est sélectionnée selon l'ordre de priorité suivant : External ID, Braze ID, Alias Name et Alias Label.<br>- Lorsque vous spécifiez un alias d'utilisateur, Alias Name et Alias Label doivent être définis tous les deux.<br><br>Pour plus d'informations, consultez l'[endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Action" }

![Action de suppression d'utilisateur Tealium avec les mappages d'ID utilisateur Braze configurés.]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Mettre à jour le statut du groupe d'abonnement de l'utilisateur - Sans lots %}
Cette action vous permet d'ajouter ou de supprimer des utilisateurs des groupes d'abonnement SMS ou e-mail de Braze.

| Paramètres | Description |
| ---------- | ----------- |
| Group type | Utilisez ce champ pour indiquer s'il s'agit d'un groupe d'abonnement SMS ou e-mail. |
| Update type | Mappez cette action à un événement de désabonnement ou d'abonnement |
| Attributes | - Subscription group ID (obligatoire) : L'ID du groupe d'abonnement lié au type de groupe mappé dans le champ précédent.<br>- External ID : L'ID externe de l'utilisateur.<br><br>Spécifique au groupe e-mail :<br>- Email : L'adresse e-mail de l'utilisateur.<br>**Si l'ID externe n'est pas défini, l'e-mail sera obligatoire.**<br><br>Spécifique au groupe SMS :<br>- Phone : Le numéro de téléphone au format E.164. Par exemple, +14155552671.<br>**Si l'ID externe n'est pas défini, le numéro de téléphone sera obligatoire.** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Action" }

![Action de mise à jour du statut du groupe d'abonnement Tealium avec les mappages de type de groupe et de type de mise à jour.]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Sélectionnez **Finish**.

#### Résumé {#summary}

Consultez le résumé du connecteur que vous avez créé. Si vous souhaitez modifier les options choisies, sélectionnez **Back** pour les modifier ou **Finish** pour terminer.

Votre connecteur est maintenant affiché dans la liste des connecteurs sur votre page d'accueil Tealium.

Assurez-vous d'enregistrer ou de publier votre connecteur lorsque vous avez terminé. Les actions que vous avez configurées se déclencheront désormais lorsque les conditions de déclenchement seront remplies.

### Étape 4 : Tester votre connecteur Tealium {#step-4-test-your-tealium-connector}

Une fois que votre connecteur est opérationnel, vous devez le tester pour vous assurer qu'il fonctionne correctement. Le moyen le plus simple de le tester est d'utiliser l'outil **Trace** de Tealium. Pour commencer à utiliser Trace, assurez-vous d'avoir ajouté l'extension de navigateur Tealium Tools.

1. Pour démarrer un nouveau traçage, sélectionnez **Trace** dans la barre latérale sous les options **Server-Side**. Cliquez sur **Start** et capturez l'ID de traçage.
2. Ouvrez l'extension de navigateur et saisissez l'ID de traçage dans AudienceStream Trace.
3. Examinez le journal en temps réel.
4. Vérifiez l'action que vous souhaitez valider en cliquant sur l'entrée **Actions Triggered** pour la développer.
5. Recherchez l'action que vous souhaitez valider et consultez le statut du journal.

Consultez la [documentation Trace](https://docs.tealium.com/server-side/connectors/trace/about/) de Tealium pour des instructions plus détaillées sur la mise en œuvre de l'outil Trace de Tealium.

## Démonstration de l'intégration {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Démonstration de l'intégration Tealium AudienceStream" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Dépassements potentiels de points de données {#potential-data-point-overages}

Il existe trois principales façons de dépasser accidentellement vos quotas de points de données lors de l'intégration de Braze via Tealium :

### Envoi de données en double - n'envoyez que les deltas d'attributs Braze {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
Tealium n'envoie pas les deltas d'attributs utilisateur à Braze. Par exemple, si vous avez une action EventStream qui suit le prénom, l'e-mail et le numéro de téléphone portable d'un utilisateur, Tealium enverra les trois attributs à Braze chaque fois que l'action est déclenchée. Tealium ne cherchera pas à identifier ce qui a changé ou été mis à jour pour n'envoyer que cette information.<br><br>
**Solution** : <br>Vous pouvez vérifier dans votre backend si un attribut a changé ou non, et le cas échéant, appeler les méthodes appropriées de Tealium pour mettre à jour le profil utilisateur. **C'est ce que font généralement les utilisateurs qui intègrent Braze directement.** <br>**OU**<br> Si vous ne stockez pas votre propre version du profil utilisateur dans votre backend et ne pouvez pas déterminer si les attributs changent ou non, vous pouvez utiliser AudienceStream et [créer des enrichissements](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) pour n'envoyer les attributs utilisateur que lorsque les valeurs ont changé.

#### Envoi de données non pertinentes ou écrasement inutile de données {#sending-irrelevant-data-or-needlessly-overwriting-data}
Si vous avez plusieurs EventStreams ciblant le même flux d'événements, **toutes les actions activées pour ce connecteur** se déclencheront automatiquement à chaque fois qu'une seule action est déclenchée, **ce qui pourrait également entraîner l'écrasement de données dans Braze.**<br><br>
**Solution** : <br>Configurez une spécification d'événement ou un flux distinct pour suivre chaque action. <br>**OU**<br> Désactivez les actions (ou connecteurs) que vous ne souhaitez pas déclencher en utilisant les bascules dans le tableau de bord de Tealium.

#### Initialisation de Braze trop précoce {#initializing-braze-too-early}
Si vous effectuez l'intégration avec Tealium en utilisant la balise SDK Web de Braze, vous pourriez constater une augmentation considérable de vos MAU. **Si Braze est initialisé au chargement de la page, Braze créera un profil anonyme chaque fois qu'un utilisateur web accède au site pour la première fois.** Cela inclut le trafic de robots, ce qui peut gonfler votre nombre d'utilisateurs actifs. Certains peuvent souhaiter ne suivre le comportement des utilisateurs que lorsqu'ils ont effectué une action spécifique, comme « Connecté » ou « Vidéo regardée », pour réduire leur nombre de MAU. <br><br>
**Solution** : <br>Configurez des [règles de chargement](https://docs.tealium.com/iq-tag-management/load-rules/about/) pour déterminer exactement quand et où une balise se charge sur votre site. Pour des conseils plus complets sur le filtrage du trafic de robots et l'initialisation conditionnelle du SDK, consultez [Filtrage du trafic de robots]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).