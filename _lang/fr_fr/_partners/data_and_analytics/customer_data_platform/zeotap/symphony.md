---
nav_title: Zeotap Symphony
description: "Cet article de référence décrit le partenariat entre Braze et Zeotap, une plateforme de données clients de nouvelle génération qui fournit des solutions d'identité, des informations exploitables et des outils d'enrichissement des données."
page_type: partner
search_tag: Partner
page_order: 2
---

# Zeotap Symphony

L'intégration de Braze et Zeotap Symphony vous permet de créer des orchestrations en temps réel et d'exécuter des campagnes d'e-mails et de notifications push.

- Envoyez les prénoms et les noms de famille via Zeotap, ce qui permet aux utilisateurs d'envoyer des e-mails personnalisés via Braze.
- Envoyez des événements personnalisés ou un événement d'achat en temps réel via Zeotap, ce qui permet aux utilisateurs de créer des déclencheurs de campagne dans Braze pour cibler leurs clients.

{% alert note %}
Pour créer des campagnes de marketing par e-mail, intégrez les e-mails bruts à Zeotap en les mappant à `Email Raw` dans le catalogue Zeotap.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Nom du client | Il s'agit du nom de votre client pour votre compte Braze. Vous pouvez le trouver en accédant à la console Braze. |
| Clé API REST de Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Instance | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Cette section fournit des informations sur les deux méthodes d'intégration avec Braze :

### Méthode 1 {#method-1}
Dans cette méthode, vous devez effectuer les tâches suivantes :
1. Intégrez le SDK Braze sur votre site web ou application.
2. Intégrez Braze avec Zeotap via Symphony.

- `User traits` doit être mappé aux champs Braze respectifs sous l'onglet **Data To Send**. Si vous mappez les attributs `Event` et `Purchase`, cela entraîne la duplication d'événements dans Braze.
- Mappez `External ID` à l'`User ID` configuré lors de la mise en place du SDK Braze.

Lorsque l'intégration est correctement configurée, vous pouvez créer des campagnes d'e-mail et de notifications push basées sur des attributs personnalisés envoyés à Braze via Symphony.

### Méthode 2 {#method-2}
Dans cette méthode, vous pouvez intégrer Braze avec Zeotap via Symphony.

- Cette méthode ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze, telles que les messages in-app, les Content Cards ou les notifications push.
- Zeotap recommande de mapper le `hashed email` disponible dans le catalogue Zeotap à l'`External ID`.

Lorsque l'intégration est correctement configurée, vous ne pouvez créer que des campagnes d'e-mail basées sur des attributs personnalisés envoyés à Braze via Symphony.

## Flux de données vers Braze et identifiants pris en charge {#data-flow-to-braze-and-supported-identifiers}

Les données circulent de Zeotap vers Braze via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Les points suivants résument le flux de données :

1. Zeotap envoie des attributs de profil utilisateur, des attributs personnalisés, des événements personnalisés et des champs d'achat.
2. Vous mappez tous les champs pertinents du catalogue Zeotap aux champs Braze sous l'onglet **Data To Send**.
3. Les données sont ensuite téléchargées vers Braze.

Vous pouvez trouver des détails sur les différents attributs dans la section [Data To Send](#data-to-send-tab).

## Configuration de la destination {#destination-setup}

Après avoir appliqué des filtres ou ajouté une condition pour vos utilisateurs dans Symphony, vous pouvez les activer dans Braze sous **Send to Destinations**. Une nouvelle fenêtre s'ouvre, dans laquelle vous pouvez configurer votre destination. Vous pouvez utiliser une destination existante de la liste des **Available Destinations** ou en créer une nouvelle.

### Ajouter une nouvelle destination {#add-new-destination}
Effectuez les étapes suivantes pour ajouter une nouvelle destination :
1. Sélectionnez **Add New Destination**.
2. Recherchez **Braze**.
3. Ajoutez le **Client Name**, l'**API Key** et l'**Instance**, puis enregistrez la destination.

La destination est créée et mise à disposition sous **Available Destinations**.

### Ajouter des entrées au niveau du flux de travail {#add-workflow-level-inputs}
Après avoir créé une destination, vous devez ensuite ajouter des entrées au niveau du flux de travail, comme décrit dans cette section.
1. Choisissez la destination dans la liste des destinations disponibles en utilisant la fonctionnalité de recherche.
2. Les champs **Client Name**, **API Key** et **Instance** sont automatiquement remplis en fonction de la valeur que vous avez saisie lors de la création de la destination.
3. Saisissez le **Audience Name** que vous souhaitez créer pour ce nœud de flux de travail. Celui-ci est envoyé en tant qu'**attribut personnalisé** à Braze.
4. Complétez le mappage du catalogue vers la destination sous l'onglet **Data To Send**. Vous trouverez des détails sur la façon d'effectuer le mappage dans cette section.

### Onglet Data To Send {#data-to-send-tab}
L'onglet **Data To Send** vous permet de mapper les champs du catalogue Zeotap aux champs Braze qui peuvent être envoyés à Braze. Le mappage peut être effectué de l'une des manières suivantes :
- **Mappage statique** — Certains champs sont automatiquement mappés par Zeotap aux champs Braze pertinents, comme l'e-mail, le téléphone, le prénom, le nom de famille, etc.<br>
- **Sélection déroulante** — Mappez les champs pertinents ingérés dans Zeotap aux champs Braze fournis dans le menu déroulant.<br>![Diverses caractéristiques d'utilisateur définies dans Zeotap, telles que la langue, la ville, la date d'anniversaire, et plus encore.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Entrée de données personnalisées** — Ajoutez des données personnalisées mappées au champ Zeotap pertinent et envoyez-les à Braze.<br>![Sélection de « loyalty_points » comme caractéristique d'utilisateur dans Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Attributs pris en charge {#supported-attributes}
Vous trouverez dans cette section les détails de tous les champs Braze.

| Champ Braze | Type de mappage | Description |
| --- | --- | --- |
| External ID | Sélection déroulante | Il s'agit de l'`User ID` persistant défini par Braze pour suivre les utilisateurs sur différents appareils et plateformes. Nous vous recommandons de mapper `User ID` à `External ID` ; sinon, Zeotap peut envoyer l'e-mail en tant qu'alias d'utilisateur.<br><br>Zeotap recommande de mapper le `hashed email` disponible dans le catalogue Zeotap à l'`External ID`. |
| E-mail | Mappage statique | Ceci est mappé à `Email Raw` dans le catalogue Zeotap. |
| Téléphone | Mappage statique | Ceci est mappé à `Mobile Raw` dans le catalogue Zeotap.<br><br>• Braze accepte les numéros de téléphone au format `E.164`. Zeotap ne réalise aucune transformation. Par conséquent, vous devez ingérer les numéros de téléphone dans le format prescrit. Pour plus d'informations, consultez la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers). |
| Prénom | Mappage statique | Ceci est mappé à `First Name` dans le catalogue Zeotap. |
| Nom de famille | Mappage statique | Ceci est mappé à `Last Name` dans le catalogue Zeotap. |
| Genre | Mappage statique | Ceci est mappé à `Gender` dans le catalogue Zeotap. |
| Nom de l'événement personnalisé | Mappage statique | Ceci est mappé à `Event Name` dans le catalogue Zeotap.<br><br>Le nom de l'événement personnalisé et l'horodatage de l'événement personnalisé doivent tous deux être mappés pour capturer des événements personnalisés dans Braze. L'événement personnalisé ne peut pas être traité si l'un des deux n'est pas mappé. Pour plus d'informations, consultez la section sur l'[objet d'événement]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| Horodatage de l'événement personnalisé | Mappage statique | Ceci est mappé à `Event Timestamp` dans le catalogue Zeotap.<br><br>Le nom de l'événement personnalisé et l'horodatage de l'événement personnalisé doivent tous deux être mappés pour capturer des événements personnalisés dans Braze. L'événement personnalisé ne peut pas être traité si l'un des deux n'est pas mappé. Pour plus d'informations, consultez la section sur l'[objet d'événement]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| Abonnement aux e-mails | Sélection déroulante | Intégrez un champ `Email Marketing Preference` et établissez une correspondance avec ce dernier.<br><br>Zeotap envoie les trois valeurs suivantes :<br>• `opted_in` — Indique que l'utilisateur s'est explicitement inscrit pour la préférence de marketing par e-mail<br>• `unsubscribed` — Indique que l'utilisateur a explicitement refusé les e-mails<br>• `subscribed` — Indique que l'utilisateur n'a ni opté pour ni opté contre |
| Abonnement aux notifications push | Sélection déroulante | Intégrez un champ `Push Marketing Preference` et établissez une correspondance avec ce dernier.<br><br>Zeotap envoie les trois valeurs suivantes :<br>• `opted_in` — Indique que l'utilisateur s'est explicitement inscrit à la préférence de marketing push<br>• `unsubscribed` — Indique que l'utilisateur a explicitement refusé les messages push<br>• `subscribed` — Indique que l'utilisateur n'a ni opté pour ni opté contre |
| Activation du suivi d'ouverture des e-mails | Sélection déroulante | Mappez le champ `Marketing Preference` pertinent.<br><br>Lorsqu'il est défini sur vrai, un pixel de suivi d'ouverture est ajouté à tous les futurs e-mails envoyés à cet utilisateur. |
| Activation du suivi des clics dans les e-mails | Sélection déroulante | Mappez le champ `Marketing Preference` pertinent.<br><br>Lorsqu'il est défini sur vrai, le suivi des clics est activé pour tous les liens dans tous les futurs e-mails envoyés à cet utilisateur. |
| ID du produit | Sélection déroulante | • Identifiant pour une action d'achat `(Product Name/Product Category)`. Pour plus de détails, consultez l'[objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object).<br>• Intégrez l'attribut pertinent au catalogue Zeotap et établissez une correspondance avec ce dernier.<br><br>`Product ID`, `Currency` et `Price` doivent être mappés obligatoirement pour capturer les événements d'achat dans Braze. L'événement d'achat ne peut pas aboutir si l'un des trois est manquant. Pour plus d'informations, consultez l'[objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-object). |
| Devise | Sélection déroulante | • Attribut de devise pour l'action d'achat.<br>• Le format pris en charge est `ISO 4217 Alphabetic Currency Code`.<br>• Intégrez correctement les données de devise formatées dans le catalogue Zeotap et établissez une correspondance avec ces dernières.<br><br>`Product ID`, `Currency` et `Price` doivent être mappés obligatoirement pour capturer les événements d'achat dans Braze. L'événement d'achat ne peut pas aboutir si l'un des trois est manquant. |
| Prix | Sélection déroulante | • Attribut de prix pour l'action d'achat.<br>• Intégrez l'attribut pertinent au catalogue Zeotap et établissez une correspondance avec ce dernier.<br><br>`Product ID`, `Currency` et `Price` doivent être mappés obligatoirement pour capturer les événements d'achat dans Braze. L'événement d'achat ne peut pas aboutir si l'un des trois est manquant. |
| Quantité | Sélection déroulante | • Attribut de quantité pour l'action d'achat.<br>• Intégrez l'attribut pertinent au catalogue Zeotap et établissez une correspondance avec ce dernier. |
| Pays | Sélection déroulante | Établissez une correspondance avec le champ de catalogue `Country` que vous intégrez. |
| Ville | Sélection déroulante | Établissez une correspondance avec le champ de catalogue `City` que vous intégrez. |
| Langue | Sélection déroulante | • Le format accepté est la norme `ISO-639-1` (par exemple, en).<br>• Intégrez la langue correctement formatée et établissez une correspondance avec cette dernière. |
| Date de naissance | Sélection déroulante | Établissez une correspondance avec le champ `Date of Birth` que vous intégrez. |
| Attribut personnalisé | Entrée de données personnalisées | Mappez tout attribut utilisateur à une entrée de données personnalisées, qui est ensuite envoyée à Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Attributs pris en charge" }

## Affichage des données sur la console Braze {#viewing-data-on-braze-console}

Après avoir mappé les attributs pertinents à envoyer et publié le flux de travail, les événements commencent à circuler vers Braze en fonction des critères définis. Vous pouvez effectuer une recherche par ID d'e-mail ou ID externe sur la console Braze.

![Vue du profil utilisateur Braze affichant les attributs et événements entrants de Zeotap.]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Les différents attributs apparaissent dans différentes sections du tableau de bord utilisateur dans Braze.
- L'onglet **Profile** contient les attributs de l'utilisateur.
- L'onglet **Custom Attributes** contient les attributs personnalisés définis par l'utilisateur.
- L'onglet **Custom Events** contient les événements personnalisés définis par l'utilisateur.
- L'onglet **Purchases** contient les achats effectués par l'utilisateur sur une période donnée.

## Création de campagnes {#campaign-creation}

Les utilisateurs peuvent créer des campagnes dans Braze et activer les utilisateurs en temps réel ou selon l'heure planifiée. Les campagnes peuvent être déclenchées en fonction des actions effectuées par l'utilisateur (événement personnalisé, achat) ou de ses attributs.