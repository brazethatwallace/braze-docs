---
nav_title: mParticle de Rokt
article_title: mParticle de Rokt
alias: /partners/mparticle/
description: "Cet article de référence présente le partenariat entre Braze et mParticle, une plateforme de données client qui collecte et achemine les informations entre les sources de votre pile marketing."
page_type: partner
search_tag: Partner

---

# mParticle de Rokt {#mparticle-by-rokt}

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> La plateforme de données client de mParticle vous permet d'en faire plus avec vos données. Les marketeurs avertis utilisent mParticle pour orchestrer les données dans leur suite d'outils de croissance, et ainsi être performants dans les moments clés du parcours client.

L'intégration de Braze et mParticle vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes :
- Synchronisez les audiences mParticle avec Braze pour la segmentation des Campaign et Canvas Braze.
- Partagez les données entre les deux plateformes. Cela peut se faire grâce à l'intégration du kit mParticle et à l'intégration de serveur à serveur.
- [Envoyez les interactions des utilisateurs de Braze à mParticle par l'intermédiaire de Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents), afin de les rendre exploitables dans l'ensemble des outils de croissance.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est nécessaire pour profiter de ce partenariat. |
| Instance Braze | Votre instance Braze se trouve sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics#endpoints) (par exemple, `US-01` ou `US-02`). |
| Clé d'identification de l'application Braze | Votre clé d'identification de l'application. <br><br>Celle-ci se trouve dans **Gérer les paramètres** > **Clé API** dans le tableau de bord de Braze. |
| Clé API REST de l'espace de travail | (Serveur-à-serveur) Une clé API REST Braze<br><br>Celle-ci peut être créée dans **Console de développement** > **Paramètres API** > **Clé API** dans le tableau de bord de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Audiences

Utilisez le partenariat entre Braze et mParticle pour configurer votre intégration et importer les audiences mParticle directement dans Braze à des fins de reciblage, créant ainsi une boucle complète de données d'un système à l'autre.

Toute intégration que vous configurez enregistrera des points de donnée. Si vous avez des questions sur les subtilités des points de donnée Braze, votre gestionnaire de compte Braze pourra y répondre.

#### Transfert d'audiences {#forwarding-audiences}

mParticle propose trois façons de définir les attributs d'appartenance à une cohorte, contrôlées par le paramètre de configuration « [Envoyer les Segments en tant que](#send_settings) ». Consultez les sections suivantes pour le traitement de chaque option :

- [Attribut de chaîne unique](#string)
- [Attribut de tableau unique](#array)
- [Un attribut par segment](#per-segment)
- [Attribut de tableau unique et attribut de chaîne unique](#both-1)
- [Attribut de tableau unique et un attribut par segment](#both-2)
- [Attribut de chaîne unique et un attribut par segment](#both-3)
- [Attribut de tableau unique, attribut de chaîne unique et un attribut par segment](#multi)

##### Attribut de chaîne unique {#string}

mParticle créera un attribut personnalisé unique appelé `SegmentMembership`. La valeur de cet attribut est une chaîne d'ID d'audiences mParticle séparés par des virgules qui correspondent à l'utilisateur. Ces ID d'audiences se trouvent dans le tableau de bord mParticle sous **Audiences**.

Par exemple, si une audience mParticle « Ibiza dreamers » possède un ID d'audience « 11036 », vous pouvez segmenter ces utilisateurs avec le filtre `SegmentMembership` — `matches regex` — `11036`.

Bien qu'il s'agisse de l'option par défaut dans mParticle, la plupart des utilisateurs en entreprise préfèrent utiliser les [attributs de tableau unique](#array) pour l'expérience de filtrage lors de la création de Segments dans Braze.

{% alert important %}
Cette solution n'est pas recommandée si vous avez plus de quelques audiences, car les attributs personnalisés peuvent contenir jusqu'à 255 caractères. Vous ne pourrez donc pas stocker des dizaines ou des centaines d'audiences sur un profil utilisateur avec cette méthode. Si vous avez un grand nombre de cohortes par utilisateur, nous recommandons fortement la configuration « un attribut par segment ».
{% endalert %}

![Appartenance au segment mParticle]({% image_buster /assets/img_archive/mparticle1.png %})

##### Attribut de tableau unique {#array}

mParticle crée un attribut de tableau personnalisé unique dans Braze pour chaque utilisateur, appelé `SegmentMembershipArray`. La valeur de cet attribut est un tableau d'ID d'audiences mParticle qui correspondent à l'utilisateur.

Par exemple, si un utilisateur est membre de trois audiences mParticle avec les ID d'audiences « 13053 », « 13052 » et « 13051 », vous pouvez segmenter les utilisateurs correspondant à l'une de ces audiences avec le filtre `SegmentMembershipArray` — `includes value` — `13051`.

{% alert note %}
Les attributs de tableau Braze ont une longueur maximale par défaut de 500. Si l'un de vos utilisateurs est membre de plus de 500 audiences, Braze tronquera ses informations d'appartenance. Pour contourner ce problème, contactez votre gestionnaire de compte Braze pour augmenter votre seuil de longueur maximale de tableau.
{% endalert %}

##### Un attribut par segment {#per-segment}

mParticle créera un attribut personnalisé booléen pour chaque audience à laquelle un utilisateur appartient. Par exemple, si une audience mParticle s'appelle « Possible Parisians », vous pouvez segmenter ces utilisateurs avec le filtre `In Possible Parisians` - `equals` - `true`.

![Attribut personnalisé mParticle]({% image_buster /assets/img_archive/mparticle2.png %})

##### Attribut de tableau unique et attribut de chaîne unique {#both-1}

mParticle enverra les attributs tels que décrits par les options attribut de tableau unique et attribut de chaîne unique.

##### Attribut de tableau unique et un attribut par segment {#both-2}

mParticle enverra les attributs tels que décrits par les options attribut de tableau unique et un attribut par segment.

##### Attribut de chaîne unique et un attribut par segment {#both-3}

mParticle enverra les attributs tels que décrits par les options attribut de chaîne unique et un attribut par segment.

##### Attribut de tableau unique, attribut de chaîne unique et un attribut par segment {#multi}

mParticle enverra les attributs tels que décrits par les options attribut de tableau unique, attribut de chaîne unique et un attribut par segment.

#### Étape 1 : Créer une audience dans mParticle {#send_settings}

Pour créer une audience dans mParticle :

1. Accédez à **Audiences** > **Single Workspace** > **+ New Audience**.
2. Pour connecter Braze en tant que sortie pour votre audience, vous devez fournir les champs suivants :

| Nom du champ               | Description                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API                  | Dans le tableau de bord de Braze, accédez à **Paramètres** > **Clés API**. |
| Système d'exploitation de la clé API | Sélectionnez le système d'exploitation auquel votre clé API Braze correspond. Cette sélection limitera les types de jetons push transférés lors d'une mise à jour d'audience.                          |
| Envoyer les segments en tant que         | La méthode d'envoi des audiences vers Braze. Consultez la section [Transfert d'audiences](#forwarding-audiences) pour plus de détails.                                                          |
| Clé REST API de l'espace de travail   | Clé REST API de Braze avec toutes les permissions. Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**.                                                        |
| Type d'identité externe   | Le type d'identité utilisateur mParticle à transférer en tant qu'ID externe vers Braze. Nous recommandons de conserver la valeur par défaut, Customer ID.                                          |
| Type d'identité e-mail      | Le type d'identité utilisateur mParticle à transférer en tant qu'e-mail vers Braze.                                                                                                            |
| Instance Braze           | Spécifiez vers quel cluster vos données Braze seront transférées.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1 : Créer une audience dans mParticle" }

{:start="3"}
3. Enfin, **enregistrez** votre audience.

Vous devriez commencer à voir les audiences se synchroniser vers Braze en quelques minutes. L'appartenance à l'audience ne sera mise à jour que pour les utilisateurs disposant d'`external_ids` (c'est-à-dire pas les utilisateurs anonymes). Pour plus d'informations sur la création d'audiences Braze mParticle, consultez la documentation mParticle sur les [paramètres de configuration](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Étape 2 : Segmenter les utilisateurs dans Braze {#step-2-segment-users-in-braze}

Dans Braze, pour créer un segment de ces utilisateurs, accédez à **Segments** sous **Engagement** et nommez votre segment. Voici deux exemples de segments en fonction de l'option que vous avez sélectionnée pour **Envoyer les segments en tant que**. Pour plus de détails sur chaque option, consultez [Transfert d'audiences](#forwarding-audiences).

- **Attribut de tableau unique :** Sélectionnez `SegmentMembershipArray` comme filtre. Ensuite, utilisez l'option « includes value » et saisissez l'ID d'audience souhaité. ![Filtre de segment mParticle « SegmentMembershipArray » défini sur « includes value » avec l'ID d'audience.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Un attribut par segment :** Sélectionnez votre attribut personnalisé comme filtre. Ensuite, utilisez l'option « equals » et choisissez la logique appropriée. ![Filtre de segment mParticle « in possible parisians » défini sur « equals » et « true ».]({% image_buster /assets/img_archive/mparticle3.png %})

Une fois enregistré, vous pouvez référencer ce segment lors de la création d'un Canvas ou d'une Campaign à l'étape de ciblage des utilisateurs.

#### Désactivation et suppression de connexions {#deactivating-and-deleting-connections}

Étant donné que mParticle ne gère pas directement les Segments dans Braze, il ne supprimera pas les Segments lorsque la connexion d'audience mParticle correspondante est supprimée ou désactivée. Dans ce cas, mParticle ne mettra pas à jour les attributs utilisateur d'audience dans Braze pour retirer l'audience de chaque utilisateur.

Pour retirer l'audience d'un utilisateur Braze avant la suppression, ajustez les filtres d'audience pour forcer la taille de l'audience à 0 avant de supprimer une audience. Une fois le calcul de l'audience terminé et renvoyant 0 utilisateur, supprimez l'audience. L'appartenance à l'audience sera alors mise à jour dans Braze à `false` pour l'option d'attribut unique ou l'ID d'audience sera retiré du format tableau.

## Mappage des données {#data-mapping}

Les données peuvent être mappées à Braze en utilisant l'[intégration par kit embarqué](#embedded-kit-integration) si vous souhaitez connecter vos applications mobiles et web à Braze via mParticle. Vous pouvez également utiliser l'[intégration API serveur-à-serveur](#server-api-integration) pour transmettre des données côté serveur à Braze.

Quelle que soit l'approche choisie, vous devez configurer Braze comme sortie :

### Configurer les paramètres de sortie Braze {#configure-your-braze-output-settings}

Dans mParticle, accédez à **Setup > Outputs > Add Outputs** et sélectionnez **Braze** pour ouvrir la configuration du kit Braze. Cliquez sur **Save** une fois terminé.

| Nom du paramètre | Description |
| ------------ | ----------- |
| Clé d'identifiant d'application Braze | Votre clé d'identifiant d'application Braze se trouve dans le tableau de bord de Braze sous **Paramètres** > **Clés API**. Notez que les clés API diffèrent selon chaque plateforme (iOS, Android et Web). |
| Type d'identité externe | Le type d'identité utilisateur mParticle à transmettre comme ID externe à Braze. Nous recommandons de conserver la valeur par défaut, Customer ID. |
| Type d'identité e-mail | Le type d'identité utilisateur mParticle à transmettre comme e-mail à Braze. Nous recommandons de conserver la valeur par défaut, Email. |
| Instance Braze | Le cluster vers lequel vos données Braze seront transmises ; il doit correspondre au cluster sur lequel se trouve votre tableau de bord. |
| Activer la transmission du flux d'événements | (Serveur-à-serveur) Lorsque cette option est activée, tous les événements seront transmis en temps réel. Dans le cas contraire, tous les événements seront transmis en lot. Si vous choisissez d'activer la transmission du flux d'événements, assurez-vous que les données que vous envoyez à Braze respectent les [limites de débit]({{site.baseurl}}/api/api_limits). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurer les paramètres de sortie Braze" }

![Paramètres de sortie mParticle Braze avec les champs d'identifiant d'application, de mappage d'identité et d'instance.]({% image_buster /assets/img_archive/configure_settings.png %})

### Intégration par kit embarqué {#embedded-kit-integration}

Les SDK mParticle et Braze seront présents dans votre application via l'intégration par kit embarqué. Cependant, contrairement à une intégration directe de Braze, mParticle se charge d'appeler la majorité des méthodes du SDK Braze à votre place. Les méthodes mParticle que vous utilisez pour suivre les données utilisateur seront automatiquement mappées aux méthodes du SDK Braze.

Ces mappages du SDK mParticle pour [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) et [Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) sont open source et sont disponibles sur la [page GitHub de mParticle](https://github.com/mparticle-integrations).

L'intégration par kit embarqué du SDK vous permet de tirer parti de notre suite complète de fonctionnalités (notifications push, messages in-app et suivi analytique de tous les messages pertinents).

{% alert note %}
Pour les intégrations de Content Cards et de messages in-app personnalisés, appelez directement les méthodes du SDK Braze.
{% endalert %}

#### Étape 1 : Intégrer les SDK mParticle {#step-1-integrate-the-mparticle-sdks}

Intégrez les SDK mParticle appropriés dans votre application en fonction des besoins de votre plateforme :

* [mParticle pour Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle pour iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle pour Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Étape 2 : Compléter l'intégration du kit d'événements Braze de mParticle {#step-2-complete-mparticles-braze-event-kit-integration}

Bien que le SDK Braze n'ait pas besoin d'être directement inclus dans votre site web ou application pour cette intégration mParticle, le kit Appboy mParticle suivant doit être installé pour transmettre les données de votre application à Braze.

Le [guide d'intégration du kit d'événements Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle vous accompagnera dans les instructions d'alignement personnalisé entre mParticle et Braze en fonction de vos besoins de communication (notifications push, suivi de localisation, etc.).

#### Étape 3 : Paramètres de connexion pour votre sortie Braze {#step-3-connections-settings-for-your-braze-output}

Dans mParticle, accédez à **Connections** > **Connect** > **[Votre plateforme souhaitée]** > **Connect Output** pour ajouter Braze comme sortie. Puis sélectionnez **Save**.

![Configuration de la connexion du kit d'événements mParticle pour la sortie Braze.]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Tous les paramètres de connexion ne s'appliquent pas à toutes les plateformes et types d'intégration. Pour un détail des paramètres de connexion et des plateformes auxquelles ils s'appliquent, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Intégration API serveur-à-serveur {#server-api-integration}

Il s'agit d'un module complémentaire pour acheminer vos données backend vers Braze si vous utilisez les SDK côté serveur de mParticle (par exemple, Ruby, Python, etc.). Pour configurer cette intégration serveur-à-serveur avec Braze, suivez la [documentation de mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
L'intégration serveur-à-serveur ne prend pas en charge les fonctionnalités d'interface Braze, telles que les messages in-app, les Content Cards ou les notifications push. Il existe également des données capturées automatiquement, comme les champs au niveau de l'appareil, qui ne sont pas disponibles via cette méthode.

Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.

Pour que les données côté serveur soient transmises à Braze, elles doivent inclure un `external_id` ; les utilisateurs anonymes ne seront pas transmis.
{% endalert %}

#### Paramètres de connexion pour votre sortie Braze {#connections-settings-for-your-braze-output}

Dans mParticle, accédez à **Connections > Connect > [Votre plateforme souhaitée] > Connect Output** pour ajouter Braze comme sortie. Cliquez sur **Save** une fois terminé.

![Écran de connexions mParticle pour ajouter Braze comme sortie sur une plateforme.]({% image_buster /assets/img_archive/mParticle_connections.png %})

Tous les paramètres de connexion ne s'appliquent pas à toutes les plateformes et types d'intégration. Pour un détail des paramètres de connexion et des plateformes auxquelles ils s'appliquent, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Avant d'activer « Enriched User Attributes » ou « Enriched User Identities », nous vous recommandons de consulter la section [Dépassement de points de données](#potential-data-point-overages) pour vous assurer que vous êtes conscient de l'impact de ces paramètres sur l'utilisation des points de données.

### Détails du mappage des données {#data-mapping-details}

#### Types de données {#data-types}
Tous les types de données ne sont pas pris en charge entre les deux plateformes.
- Les [propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date. Elles ne prennent pas en charge les tableaux ni les objets imbriqués.
- Les [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) prennent en charge les objets de type chaîne de caractères, numérique, booléen, date et les tableaux, mais ne prennent pas en charge les objets ni les objets imbriqués.

{% alert note %}
Braze ne prend pas en charge les horodatages antérieurs à l'an 0 ou postérieurs à l'an 3000 dans les attributs personnalisés de type `Time`. Braze ingérera ces valeurs lorsqu'elles sont envoyées par mParticle, mais la valeur sera stockée sous forme de chaîne de caractères.
{% endalert %}

#### Mappage des données

| Type de données mParticle | Type de données Braze | Description |
| ------------------- | --------------- | ----------- |
| Attributs utilisateur (réservés) | Attribut standard | Par exemple, la clé d'attribut utilisateur réservée `$FirstName` de mParticle est mappée au champ d'attribut standard `first_name` de Braze. |
| Attributs utilisateur (autres) | Attribut personnalisé | Tout attribut utilisateur transmis à mParticle qui ne fait pas partie de ses clés d'attribut utilisateur réservées est enregistré dans Braze comme attribut personnalisé.<br><br>Les attributs utilisateur prennent en charge les types chaîne de caractères, numérique, booléen, date et tableaux, mais ne prennent pas en charge les objets ni les objets imbriqués. |
| Événement personnalisé | Événement personnalisé | Les événements personnalisés mParticle sont reconnus par Braze comme des événements personnalisés. Les attributs d'événement sont transmis en tant que propriétés d'événement personnalisé.<br><br>Les attributs d'événement transmis à Braze en tant que propriétés d'événement prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date, mais ne prennent pas en charge les tableaux ni les objets imbriqués. |
| Événement commercial d'achat | Événement d'achat | Les événements commerciaux d'achat seront mappés aux événements d'achat Braze. <br><br>Activez ou désactivez le paramètre de regroupement des données d'événement commercial pour enregistrer les achats au niveau de la commande ou au niveau du produit. Par exemple, si la valeur est `false`, un seul événement entrant comportant deux produits, promotions ou impressions uniques générerait au moins deux événements sortants Braze. Si la valeur est `true`, cela générerait un seul événement sortant avec un tableau imbriqué de produits, promotions ou impressions, respectivement.<br><br>Pour plus d'informations sur les champs commerciaux supplémentaires qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Lorsque le paramètre « bundle commerce event data » est défini sur `false`, les attributs de produit transmis à Braze en tant que propriétés d'événement d'achat prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date, mais ne prennent pas en charge les tableaux ni les objets imbriqués. |
| Tous les autres événements commerciaux | Événement personnalisé | Tous les autres événements commerciaux seront mappés à des événements personnalisés. <br><br>Activez ou désactivez le paramètre de regroupement des données d'événement commercial pour enregistrer les achats au niveau de la commande ou au niveau du produit. Par exemple, si la valeur est `false`, un seul événement entrant comportant deux produits, promotions ou impressions uniques générerait au moins deux événements sortants Braze. Si la valeur est `true`, cela générerait un seul événement sortant avec un tableau imbriqué de produits, promotions ou impressions, respectivement.<br><br>En plus de certaines valeurs commerciales par défaut, les attributs de produit seront enregistrés en tant que propriétés d'événement Braze. Pour plus d'informations sur les champs commerciaux supplémentaires qui seront enregistrés, consultez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events).<br><br>Lorsque le paramètre « bundle commerce event data » est défini sur `false`, les attributs de produit transmis à Braze en tant que propriétés d'événement prennent en charge les objets de type chaîne de caractères, numérique, booléen ou date, mais ne prennent pas en charge les tableaux ni les objets imbriqués. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mappage des données" }

#### Mappage d'identité utilisateur {#user-identity-mapping}
Pour chaque sortie mParticle, vous pouvez sélectionner le type d'identité externe à envoyer à Braze en tant qu'`external_id`. Bien que la valeur par défaut soit le customer ID, vous pouvez choisir de mapper un autre identifiant, tel que `MPID`, pour l'envoyer à Braze en tant qu'`external_id`. Sachez que le choix d'un identifiant autre que le customer ID peut influencer la manière dont les données sont envoyées dans Braze.

Par exemple, mapper le MPID à votre `external_id` Braze aura les effets suivants :
- En raison du moment où le MPID est attribué, tous les utilisateurs se verront assigner un `external_id` au démarrage de la session.
- La configuration de Currents peut nécessiter un mappage supplémentaire en raison des différences de types de données entre le MPID et l'`external_id`.

### Transmission des demandes d'effacement (demandes de personnes concernées) {#forwarding-erasure-requests-data-subject-requests}

Transmettez les demandes d'effacement à Braze en configurant une sortie de demande de personne concernée vers Braze. Pour transmettre les demandes d'effacement à Braze, suivez la [documentation de mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Dépassements potentiels de points de données {#potential-data-point-overages}

### Attributs utilisateur enrichis {#enriched-user-attributes}

#### Activation de l'enrichissement des attributs/identités utilisateur (serveur à serveur uniquement) {#enriched}

Dans les paramètres de connexion mParticle, Braze recommande de désactiver **Include Enriched User Attributes**. Si cette option est activée, mParticle transmettra tous les attributs utilisateur disponibles (tels que les attributs standard, les attributs personnalisés et les attributs calculés) du profil existant à Braze pour chaque événement enregistré. Cela entraîne une consommation élevée de points de données, car mParticle envoie à Braze les mêmes attributs inchangés à chaque appel.

Par exemple, si un utilisateur ajoute son prénom, son nom et son numéro de téléphone lors de sa première session, puis s'inscrit à une newsletter en ajoutant les mêmes informations ainsi qu'une adresse e-mail, ce qui déclenche un événement d'inscription à la newsletter :
- Si l'option est activée (par défaut), cinq points de données seront consommés. (événement d'inscription, adresse e-mail, prénom, nom et numéro de téléphone)
- Si l'option est désactivée, deux points de données seront consommés (événement d'inscription et adresse e-mail)

{% alert note %}
Désactiver ce paramètre ne vérifiera pas si les données ont changé. Cela empêchera cependant l'intégration d'envoyer tous les attributs utilisateur du profil de l'utilisateur qui n'ont pas été reçus dans le lot entrant d'origine ou qui n'ont pas été explicitement définis comme attribut pour l'événement. Il reste important de vérifier que seuls les deltas sont transmis à Braze.
{% endalert %}

#### Considérations liées à la désactivation des attributs utilisateur enrichis {#considerations-of-turning-off-enriched-user-attributes}

Il y a quelques points à prendre en compte lors de la désactivation de **Include Enriched User Attributes** :
1. L'intégration serveur à serveur utilise l'API d'événements mParticle pour envoyer des événements à Braze. Chaque requête est déclenchée par un événement. Lorsqu'un attribut utilisateur est modifié, par exemple la mise à jour d'une adresse e-mail, mais n'est pas associé à un événement spécifique (par exemple, un événement personnalisé de mise à jour du profil), la nouvelle valeur n'est transmise à une sortie comme Braze qu'en tant qu'« attribut enrichi » dans le payload du prochain événement déclenché par l'utilisateur. Lorsque **Include Enriched User Attributes** est désactivé, cette nouvelle valeur d'attribut non associée à un événement spécifique ne sera pas transmise à Braze.
  - Pour résoudre ce problème, nous recommandons de créer un événement distinct « user attribute updated » qui envoie uniquement le ou les attributs utilisateur spécifiques qui ont été mis à jour vers Braze. Notez qu'avec cette approche, vous consommerez tout de même un point de données supplémentaire pour l'événement « user attribute updated », mais la consommation de points de données sera bien inférieure à l'envoi de tous les attributs utilisateur à chaque appel avec la fonctionnalité activée.
2. Les attributs calculés sont transmis à Braze en tant qu'attributs utilisateur enrichis. Par conséquent, lorsque « Enriched User Attributes » est désactivé, ils ne seront plus transmis à Braze. Pour transmettre les attributs calculés à Braze lorsque « Enriched User Attributes » est désactivé, un [flux d'attributs calculés](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) pourrait aider sans pousser l'ensemble des attributs. Le flux déclenchera une mise à jour en aval vers Braze lorsqu'un attribut calculé change.

## Résolution des problèmes {#troubleshooting}

### Résolution des problèmes de notifications push iOS avec le kit d'événements Braze {#troubleshooting-ios-push-notifications-with-the-braze-event-kit}

Si les notifications push ne fonctionnent pas lorsque vous utilisez le kit d'événements Braze (intégration de kit intégré) sur iOS, vérifiez les points suivants :
1. **Transfert du jeton push :** Confirmez que mParticle transmet les jetons push à Braze. Dans votre tableau de bord mParticle, vérifiez que la connexion du kit Braze a le push activé et que les bonnes informations d'identification push Apple sont configurées dans le tableau de bord de Braze.
2. **Ordre d'initialisation du kit :** Le kit Braze doit être initialisé avant que votre application ne demande les autorisations push. Si les autorisations push sont demandées avant que le kit ne soit actif, le jeton push peut ne pas être transmis à Braze. Vérifiez que le SDK mParticle est démarré tôt dans le cycle de vie de votre application.
3. **Method swizzling :** Le kit Apple de mParticle utilise le method swizzling pour transmettre automatiquement les jetons push et gérer les événements de notification push. Si vous avez désactivé le swizzling ou si un autre SDK interfère, les jetons push peuvent ne pas parvenir à Braze. Vérifiez que le swizzling est activé dans votre configuration mParticle.
4. **Gestion manuelle des jetons :** Si vous gérez les jetons push manuellement (par exemple, en implémentant `application:didRegisterForRemoteNotificationsWithDeviceToken:`), assurez-vous de transmettre le jeton à mParticle en l'assignant à la propriété du jeton de notification push, par exemple : `MParticle.sharedInstance().pushNotificationToken = deviceToken`. Le kit le transmettra ensuite à Braze.
5. **Incohérence d'environnement :** Confirmez que l'environnement des identifiants APN (développement vs. production) correspond au build de votre application. Pour plus de détails, consultez la [résolution des problèmes de push iOS]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift).
6. **Timing d'initialisation du kit :** Si vous accédez à l'instance Braze depuis `didFinishLaunchingWithOptions`, le kit mParticle peut ne pas être prêt lorsqu'un push arrive. Initialisez la gestion du push dans [`userNotificationCenter(_:didReceive:withCompletionHandler:)`]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) (ou le délégué de réponse de notification équivalent) afin que le kit Braze soit actif lorsque l'utilisateur ouvre une notification.

### Envoi de données inutiles ou en double à Braze {#sending-unnecessary-or-duplicate-data-to-braze}
Braze comptabilise un point de donnée chaque fois qu'un attribut est transmis à Braze, même si la valeur est inchangée. Pour cette raison, Braze recommande de ne transmettre que les données nécessaires pour agir au sein de Braze et de s'assurer que seuls les deltas d'attributs sont transmis.

### Les événements n'apparaissent pas dans Braze {#events-are-not-appearing-in-braze}

Si des événements ou des attributs mParticle sont manquants dans Braze, le problème est souvent une mauvaise configuration de votre connexion mParticle ou du mappage des événements, et non une panne de Braze. Vérifiez les points suivants :

- **Sortie de connexion :** Confirmez que Braze est activé comme sortie pour la connexion concernée et que la bonne instance Braze, l'identifiant d'application et la clé REST API sont configurés.
- **Mappage d'identité :** Les synchronisations serveur-à-serveur et d'audience nécessitent un `external_id`. Les utilisateurs anonymes ne sont pas transmis.
- **Mappage des événements :** Vérifiez que les événements sont acheminés vers la sortie Braze et que les types de données non pris en charge (objets imbriqués, tableaux dans les propriétés d'événement) ne sont pas supprimés.

Si la configuration semble correcte mais que les données n'arrivent toujours pas, contactez le [support mParticle](https://support.mparticle.com/) pour examiner les journaux de distribution de leur côté.