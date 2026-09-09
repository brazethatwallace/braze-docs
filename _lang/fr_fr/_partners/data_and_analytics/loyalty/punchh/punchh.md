---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Cet article de référence décrit le partenariat entre Braze et Punchh, une plateforme de fidélisation et d'engagement, qui vous permet de synchroniser les données entre les deux plateformes. Les données publiées dans Braze seront disponibles pour la segmentation et pourront être synchronisées avec Punchh via la configuration de modèles de webhooks dans Braze."
page_type: partner
search_tag: Partner
---

# Punchh

> [Punchh](https://punchh.com/) est une plateforme de fidélisation et d'engagement de pointe qui permet aux marques de proposer des programmes de fidélité omnicanaux à la fois en magasin et en ligne.

_Cette intégration est maintenue par Punchh._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Punchh vous permet de synchroniser les données relatives aux cadeaux et à la fidélité entre les deux plateformes. Les données publiées dans Braze seront disponibles pour la segmentation et pourront resynchroniser les données utilisateur dans Punchh via les webhooks Braze.

## Quels sont les avantages ? {#what-are-the-benefits}

- Ingérer les données de fidélité de Punchh vers Braze en temps réel.
- Exploiter et superposer les données d'audience puissantes de Braze pour offrir des expériences cross-canal significatives et dynamiques (application, mobile, web, e-mail et SMS)
  - Les clients ont-ils ouvert les e-mails ? Les clients ont-ils ouvert l'application à proximité d'un magasin ?
- Standardiser l'apparence des e-mails transactionnels envoyés via Braze.
- Créer des parcours permettant le test A/B et l'optimisation au fil du temps.

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte Punchh | Vous devez disposer d'un compte Punchh actif pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec les permissions `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Que faut-il savoir d'autre ? {#what-else-should-i-know}

### Avant l'intégration {#before-integrating}

- Lors de l'utilisation de l'intégration Braze, deux campagnes seront nécessaires, une dans Punchh et la seconde dans Braze. Par exemple, si vous envoyez une campagne avec une offre associée, la campagne de distribution de cadeaux sera configurée dans Punchh, et la notification pourra être envoyée depuis Braze.
- Les invités doivent déjà exister dans Punchh et Braze. Punchh filtrera tout client qui n'est pas déjà un invité du programme de fidélité.

### Points importants à noter {#important-things-to-note}

- Punchh a ajouté la possibilité de désactiver l'envoi des attributs utilisateur par défaut à Braze, afin que le client n'encoure pas de dépassements de points de données. Ceci est configuré lors de la mise en place de l'adaptateur.
- Si vous utilisez des Segments personnalisés dans des campagnes récurrentes, le nom de la campagne doit être utilisé à la place de l'identifiant de la campagne, car les identifiants changent à chaque exécution de la campagne.
- Les canaux de communication disponibles dans chaque campagne de distribution de cadeaux Punchh incluent les messages enrichis, les notifications push, les SMS et les e-mails.
- Une fois que les utilisateurs ont été envoyés vers un Segment personnalisé Punchh depuis Braze, ils ne peuvent pas être retirés. Seuls de nouveaux invités peuvent être ajoutés à un Segment personnalisé existant. Si des invités doivent être retirés d'un Segment personnalisé Punchh existant, une nouvelle campagne webhook devra être créée dans Braze pour envoyer les utilisateurs vers un nouveau Segment personnalisé Punchh.

## Intégration {#integration}

Punchh propose plusieurs endpoints accessibles aux clients de Braze pour faciliter l'ajout d'ID externes à la plateforme Punchh à l'aide des endpoints API Punchh suivants. Une fois les ID externes ajoutés, créez un adaptateur dans Punchh, fournissez vos identifiants Braze et sélectionnez les événements que vous souhaitez synchroniser. Vous pouvez ensuite utiliser l'ID de Segment Punchh pour créer un webhook Punchh afin de déclencher la synchronisation des clients dans un parcours Canvas.

Notez que le `user_id` Punchh et l'`external_id` Braze doivent être disponibles sur l'une ou l'autre plateforme pour que l'intégration se synchronise correctement.
- Les événements envoyés de Punchh à Braze incluront l'`external_id` Braze comme identifiant. Si Punchh est configuré pour utiliser l'`external_source_id`, cette valeur sera définie comme l'`external_id` Braze. Sinon, l'intégration définira par défaut le `user_id` Punchh comme l'`external_id` Braze.
- Pour envoyer des webhooks de Braze à Punchh, le `user_id` Punchh doit être disponible sur le profil utilisateur Braze. Si le `user_id` Punchh n'est pas utilisé comme l'`external_id` Braze, il doit être défini comme attribut personnalisé « punchh_user_id ».

### Étape 1 : Configurer les endpoints d'ingestion d'ID externes (facultatif) {#step-1-set-up-external-id-ingestion-endpoints-optional}

Les ID externes de Braze peuvent être ajoutés à l'aide des endpoints suivants pour les utilisateurs Punchh nouveaux et existants.

{% alert important %}
Les valeurs des champs `external_source` et `external_source_id` doivent être uniques dans Punchh et ne pas être associées à des profils existants.
{% endalert %}

1. Nouveaux utilisateurs Punchh<br>
Créez de nouveaux utilisateurs dans Punchh avec un endpoint d'inscription Punchh en utilisant les champs `external_source` et `external_source_id`. Punchh permet d'envoyer des identifiants externes avec un profil utilisateur via l'un des endpoints d'inscription suivants :
- [API d'inscription mobile](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [API d'inscription authentification unique](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Utilisateurs Punchh existants <br>
Mettez à jour l'`external_source_id` pour les utilisateurs Punchh existants. Punchh permet d'ajouter des identifiants externes à un profil via un endpoint de mise à jour de l'API utilisateur :
- [Mise à jour utilisateur mobile](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Mise à jour utilisateur authentification unique](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Mise à jour utilisateur tableau de bord](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab Exemple d'API d'inscription utilisateur %}
Cet exemple vous permet d'envoyer des identifiants externes avec un profil utilisateur au moment de l'inscription. Pour ce faire, envoyez `external_source` comme « customer_id » et `external_source_id` comme « 111111111111111111 » en tant que type de donnée string.

```bash
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab Exemple d'API de mise à jour utilisateur %}
Cet exemple vous permet de mettre à jour des identifiants externes avec un profil utilisateur. Pour ce faire, envoyez `external_source` comme « customer_id » et `external_source_id` comme « 111111111111111111 » en tant que type de donnée string.

```bash
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Configuration de la plateforme :** pour activer les identifiants externes dans Punchh, depuis le tableau de bord Punchh, accédez à **Cockpit** > **Dashboard** > **External User Identifier**.
{% endalert %}

### Étape 2 : Configuration de l'adaptateur Braze dans Punchh {#step-2-braze-adapter-setup-in-punchh}

#### Événements disponibles à synchroniser {#available-events-to-sync}

1. **Guest :** déclenché lors de toute inscription, mise à jour du profil invité, désactivation ou suppression
2. **Loyalty Check-in :** déclenché pour les transactions de fidélité ou les gains par scan de code-barres depuis le reçu
3. **Gift Check-in :** déclenché pour les points offerts dans le cadre d'une campagne
4. **Redemption :** déclenché en cas d'échange de récompense, à l'exclusion des coupons Punchh, car ceux-ci sont envoyés séparément en tant qu'événements de coupon, y compris l'émission et l'échange
5. **Rewards :** déclenché par les récompenses offertes via des campagnes, une activité, la conversion de points en récompenses ou l'attribution par un administrateur
6. **Transaction Notifications :** déclenché lors d'une activité transactionnelle pour un utilisateur au sein du système Punchh (par exemple, l'expiration de points)
7. **Marketing Notifications :** déclenché en fonction de différentes configurations de campagnes dans Punchh pour un Segment d'utilisateurs associé

{% alert note %}
Consultez la documentation Punchh pour découvrir à quoi peuvent ressembler les exemples de payloads pour ces événements disponibles.
{% endalert %}

Travaillez avec votre responsable de déploiement Punchh pour configurer cet adaptateur.

Pour configurer l'intégration Braze et Punchh, procédez comme suit :

1. Dans le tableau de bord Punchh, accédez à **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** et activez **Enable Webhook Management**.<br><br>
2. Ensuite, activez les adaptateurs en accédant à **Settings** > **Webhooks gestionnaire** > **Configurations** > **Show Adapters Tab** et activez **Show Adapters Tab**.<br><br>
3. Accédez à **Webhooks Manager** sous l'onglet **Settings**, sélectionnez l'onglet **Adapters**, puis cliquez sur **Create Adapter**. <br><br>![Onglet Adapters du gestionnaire de webhooks Punchh avec l'option Create Adapter sélectionnée.]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Renseignez le nom de l'adaptateur, la description et l'e-mail de l'administrateur. Sélectionnez **Braze** comme adaptateur et fournissez votre endpoint REST API Braze et votre clé API Braze.<br><br>
5. Ensuite, sélectionnez les événements disponibles que vous souhaitez activer. Une liste de ces événements est disponible dans [Événements disponibles à synchroniser](#available-events-to-sync).<br><br>![Paramètres de l'adaptateur Punchh affichant les événements sélectionnables pour la synchronisation avec Braze.]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Cliquez sur **Submit** pour activer le webhook.

## Créer un webhook Punchh dans Braze {#create-punchh-webhook-in-braze}

Braze peut ajouter des utilisateurs à un Segment Punchh via des webhooks en utilisant les segments personnalisés Punchh.

1. Créez un segment personnalisé dans Punchh et notez le `custom_segment_id` présent dans l'URL du tableau de bord des segments Punchh, comme illustré dans l'exemple suivant. Les générateurs de segments classique et bêta peuvent tous deux être utilisés. Cependant, la version bêta est recommandée, car la version classique sera à terme abandonnée.<br><br>Dans la plateforme Punchh, accédez à **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![Tableau de bord des segments personnalisés Punchh montrant l'identifiant du segment personnalisé dans l'URL.]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Créez une campagne webhook dans Braze en utilisant l'endpoint Punchh pour ajouter un utilisateur à un segment personnalisé comme URL du webhook. Ici, vous pouvez fournir le `custom_segment_id` extrait de l'URL et le `user_id` en tant que paires clé-valeur.<br><br>![Composeur de webhook Braze avec l'endpoint Punchh et les champs de payload sous forme de paires clé-valeur.]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Ce webhook peut être configuré en tant que Campaign unique ou en tant qu'étape au sein d'un Canvas. Alternativement, si le webhook ajoutant des utilisateurs à ce Segment Punchh spécifique sera utilisé dans plusieurs Campaigns ou Canvas, il peut être configuré en tant que [modèle]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates).<br><br>
La clé `user_id` dans le webhook correspond à l'identifiant utilisateur Punchh. Cet identifiant devra être ajouté à tous les webhooks créés dans Braze pour ajouter des utilisateurs à un segment personnalisé Punchh. L'attribut personnalisé `punch_user_id` peut être renseigné dynamiquement comme valeur de la clé `user_id` à l'aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables). Vous pouvez insérer la variable d'attribut personnalisé `punchh_user_id` en utilisant l'icône bleue « plus » dans la barre d'outils du champ de texte modélisé.<br><br>![Champ de payload du webhook Braze avec la variable Liquid de l'identifiant utilisateur Punchh insérée.]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![Sélecteur de personnalisation Braze affichant l'attribut personnalisé punchh_user_id.]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Une fois le webhook enregistré, il peut être utilisé pour synchroniser les utilisateurs. Par exemple, 136 invités seraient ajoutés au segment personnalisé Punchh lorsque cette campagne webhook Braze est lancée.<br><br>![Exemple de synchronisation d'utilisateurs à l'aide du webhook enregistré grâce à l'intégration de Braze et Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Pour plus d'informations sur l'utilisation des webhooks dans Braze, consultez [Créer un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).

## Campaigns de cas d'usage {#use-case-campaigns}

### Configuration de Campaign et de Canvas {#campaign-and-canvas-configuration}

#### Déclenchement {#triggering}

Les cas d'usage pour la messagerie Braze déclenchée par des événements Punchh envoyés à Braze, tels que des événements de récompense ou des événements invité, peuvent être créés en tant que [campaigns basées sur des actions]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) ou Canvas déclenchés par l'événement Punchh pertinent.

L'ajout d'un déclencheur fera apparaître la liste des événements créés dans Braze. Choisissez l'événement qui doit déclencher l'envoi de votre Campaign ou Canvas à l'utilisateur qui a enregistré l'événement.

![Configuration du déclencheur Braze montrant un événement Punchh sélectionné pour une campagne basée sur une action.]({% image_buster /assets/img/punchh/update5.png %})

Des filtres de propriétés peuvent être ajoutés pour affiner davantage l'événement déclencheur. Par exemple, le message ne doit être déclenché que lorsqu'un client déclenche l'événement « checkins_gift » dont la propriété d'événement approved est `true`. Il s'agit d'une fonctionnalité facultative qui peut ne pas s'appliquer à tous les cas d'usage.

#### Segmentation

Dans de nombreux cas, les Campaigns et Canvas Braze déclenchés par des événements Punchh peuvent être définis pour une audience « Tous les utilisateurs », car la segmentation des utilisateurs déclenchant ces événements est déterminée au sein de Punchh. Cependant, les clients souhaitant affiner davantage l'audience des utilisateurs qui recevront la messagerie Braze déclenchée par l'événement peuvent le faire en ajoutant des filtres et des Segments supplémentaires dans la section **Target Audiences** du compositeur de Campaign ou dans l'**Entry Audience** du compositeur de Canvas.

### Cas d'usage {#use-cases}

{% tabs local %}
{% tab Inscription %}
#### Campagne d'inscription {#sign-up-campaign}

Lorsque vous utilisez la configuration Braze pour une campagne d'inscription avec une offre associée, une campagne de cadeau à l'inscription doit être configurée dans Punchh et un message d'accueil dans Braze.

Punchh recommande d'ajouter un délai d'exécution à la campagne d'inscription, afin que Braze puisse d'abord déclencher le message d'accueil basé sur l'événement invité. Si vous souhaitez envoyer un message de suivi informant l'utilisateur qu'il a reçu un cadeau, vous pouvez le déclencher à partir de l'événement de récompense.

Dans le cas d'une campagne d'inscription, tous les inscrits peuvent être utilisés pour le Segment ; par conséquent, un Segment Braze personnalisé ne sera pas nécessaire.

Configurations Punchh requises :
- Campaign : Inscription
- Segment : Tous les inscrits
- Récompense : Choix du client
Événements requis :
- Événement de récompense
- Événement invité
Considérations :
- Délai d'exécution, il est recommandé que l'invité ajoute un délai de 5 à 10 minutes

![Un Segment d'utilisateurs est configuré dans Punchh, et les invités s'inscrivent à un programme de fidélité. Ensuite, l'événement invité, s'il est déclenché, et la campagne de messagerie Braze est déclenchée. Puis, la campagne de cadeau à l'inscription Punchh est déclenchée après 10 minutes, déclenchant l'événement de récompense et le message de suivi facultatif.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Accueil Braze %}
#### Campagne d'accueil Braze {#braze-welcome-campaign}

Lorsqu'un nouvel utilisateur s'inscrit, Punchh envoie à Braze un événement invité qui crée l'utilisateur et envoie un attribut personnalisé `signup_channel`, que vous pouvez utiliser pour déclencher la campagne d'accueil Braze.

Pour configurer la campagne d'accueil Braze, suivez ces étapes :

1. Dans Braze, créez une campagne basée sur une action.
2. Pour le déclencheur, sélectionnez **Change Custom Attribute Value** avec l'attribut personnalisé `signup_channel` défini sur **Any new value**.
3. Continuez à créer votre Campaign, puis envoyez-la quand elle est prête !

{% endtab %}
{% tab Offre groupée %}
#### Campagne d'offre groupée {#mass-offer-campaign}

Lorsque vous utilisez une campagne d'offre groupée pour les cadeaux, une campagne d'offre groupée doit être configurée dans Punchh et une campagne de messagerie dans Braze.

Si vous souhaitez utiliser un Segment Braze pour votre Campaign ou envoyer une communication depuis Braze avant d'offrir des cadeaux aux invités sur la plateforme Punchh, un [Segment Punchh personnalisé]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) sera nécessaire pour la campagne de cadeaux Punchh.

Créer le Segment d'utilisateurs pour recevoir cette offre dans Braze n'est recommandé que si vous utilisez des attributs non disponibles dans Punchh. Sinon, la segmentation Punchh peut être utilisée, et la campagne de messagerie Braze sera créée en tant que Campaign basée sur une action déclenchée par les utilisateurs recevant leur récompense (l'événement de récompense déclenché par Punchh).

Configurations Punchh requises :
- Campaign : Offre groupée
- Segment : Liste personnalisée ou choix du client
- Récompense : Choix du client

**Utilisation de Punchh pour la segmentation et les cadeaux, et de Braze pour la messagerie :**<br>
Par exemple, une récompense de 2 $ de réduction est envoyée à un Segment configurable dans Punchh avec la messagerie envoyée via Braze.<br>
![Un Segment d'utilisateurs peut être configuré dans Punchh, et les utilisateurs reçoivent un cadeau via une campagne d'offre groupée Punchh. Ensuite, un événement de récompense est déclenché, puis la campagne de messagerie Braze est déclenchée.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Utilisation de la segmentation et de la messagerie Braze, et de Punchh pour les cadeaux :**<br>
Par exemple, une récompense de 2 $ de réduction et la messagerie envoyées à un Segment avec des attributs non disponibles dans Punchh.<br>
![Un Segment d'utilisateurs peut être configuré dans Braze, puis un message peut être envoyé depuis un Segment Braze. Ensuite, les utilisateurs sont envoyés au Segment Punchh personnalisé via un webhook Braze avec l'identifiant de Segment et l'identifiant utilisateur. Après cela, l'utilisateur reçoit un cadeau via une campagne d'offre groupée Punchh avec un Segment personnalisé. Puis l'événement de récompense est déclenché.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Utilisation de la segmentation Braze et de Punchh pour les cadeaux ou la messagerie, ou les deux :**<br>
Par exemple, une récompense de 2 $ de réduction est envoyée à un Segment avec des attributs non disponibles dans Punchh, mais aucune messagerie n'est requise, ou la messagerie peut être envoyée via Punchh (notez que tous les invités doivent être présents dans Punchh).<br>
![Un Segment d'utilisateurs peut être configuré dans Braze, et les utilisateurs sont envoyés au Segment Punchh personnalisé via un webhook Braze avec l'identifiant de Segment et l'identifiant utilisateur. Après cela, l'utilisateur reçoit un cadeau via une campagne d'offre groupée Punchh avec un Segment personnalisé. Puis l'événement de récompense est déclenché.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Offre groupée récurrente %}
#### Campagne d'offre groupée récurrente {#recurring-mass-offer-campaign}

Lorsque vous utilisez une campagne d'offre groupée récurrente pour les cadeaux, une campagne d'offre groupée doit être configurée dans Punchh et une campagne de messagerie dans Braze. Un Segment Punchh personnalisé sera nécessaire si le client souhaite utiliser la segmentation Braze (recommandé uniquement si vous utilisez des attributs non disponibles dans Punchh). Sinon, la segmentation Punchh peut être utilisée, et la campagne de messagerie Braze sera déclenchée à partir de l'événement de récompense.

Configurations Punchh requises :
- Campaign : Offre groupée récurrente
- Segment : Liste personnalisée ou choix du client
- Récompense : Choix du client
Considérations :
- Les identifiants de Campaign et les noms de Campaign sont envoyés à Braze en tant que propriété d'événement sur l'événement. Si vous souhaitez utiliser un identifiant de campagne Punchh dans Braze pour filtrer davantage l'audience recevant la Campaign, vous devez utiliser le nom de la Campaign car les identifiants de Campaign changent quotidiennement.

{% endtab %}
{% tab Offre post-visite avec notification %}
#### Campagne d'offre post-visite avec notification {#post-check-in-offer-campaign-with-notification}

Lorsque vous utilisez une campagne d'offre post-visite, Braze enverra la notification concernant le cadeau, et lorsque l'invité effectue une visite, il recevra ensuite le cadeau de la campagne Punchh post-visite. Par conséquent, une campagne d'offre post-visite doit être configurée dans Punchh et une campagne de messagerie dans Braze (si vous souhaitez notifier les clients de la campagne).

Configurations Punchh requises :
- Campaign : Offre post-visite
- Segment : Liste personnalisée
- Récompense : Choix du client

Par exemple, un e-mail notifiant les invités de visiter ce week-end pour des points doublés vers un Segment avec des attributs non disponibles dans Punchh. Punchh offrira des points à ce Segment après une visite éligible et une messagerie facultative depuis Braze.

![Un Segment d'utilisateurs est configuré dans Braze, et les messages sont envoyés depuis la campagne Braze post-visite. Ensuite, les utilisateurs éligibles sont envoyés au Segment Punchh personnalisé via un webhook Braze avec l'identifiant de Segment et l'identifiant utilisateur. Enfin, l'utilisateur éligible dans le Segment personnalisé effectue une visite et reçoit le cadeau et le message facultatif via la campagne post-visite.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Offre post-visite sans notification %}
#### Campagne d'offre post-visite sans notification {#post-check-in-offer-campaign-without-notification}

Lorsque vous utilisez une campagne d'offre post-visite qui ne notifie pas d'abord les clients, la campagne offrira le cadeau (messagerie facultative) et déclenchera toute notification dans Braze. Par conséquent, une campagne d'offre post-visite doit être configurée dans Punchh ; cependant, une liste personnalisée n'est pas requise. Vous pouvez plutôt choisir le Segment souhaité dans Punchh.

Configurations Punchh requises :
- Campaign : Offre post-visite
- Segment : Choix du client
- Récompense : Choix du client

Par exemple, une campagne Braze de surprise et plaisir est envoyée à un Segment disponible dans Punchh, remerciant les invités pour leur visite et les récompensant avec 2 $ de réduction lors de leur prochaine visite.

![Un Segment d'utilisateurs éligibles peut être configuré dans Punchh, et un utilisateur éligible effectue une visite et reçoit un cadeau via une campagne Punchh post-visite. Ensuite, un événement de récompense est déclenché et le message de rappel notifiant les invités de la récompense est envoyé depuis Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Anniversaire %}
#### Campagne d'anniversaire {#anniversary-campaign}

Lorsque vous utilisez une campagne d'anniversaire, un utilisateur recevra d'abord un cadeau pour son anniversaire de la campagne Punchh. Ce cadeau (événement de récompense) déclenchera la campagne de messagerie dans Braze qui notifie l'utilisateur du cadeau. Par conséquent, une liste personnalisée n'est pas requise. Vous pouvez plutôt choisir le Segment et le paramètre d'anniversaire dans Punchh.

Configurations Punchh requises :
- Campaign : Campagne d'anniversaire
- Segment : Choix du client
- Récompense : Choix du client
Considérations :
- Mois d'inscription pour le cadeau
- Durée de validité (combien de temps la récompense d'anniversaire est-elle valide ?)
- Campaigns récurrentes, planification requise

![Un Segment facultatif peut être créé dans Punchh, et un utilisateur éligible reçoit une récompense via une campagne d'anniversaire Punchh. Ensuite, un événement de récompense est déclenché et le message de rappel notifiant les invités de la récompense est envoyé depuis Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Rappel %}
#### Campagne de rappel {#recall-campaign}

Lorsque vous ciblez des utilisateurs en fonction de leur inactivité, une campagne de rappel peut être utilisée. Le client peut créer le Segment et la Campaign dans Punchh, mais utiliser Braze pour la messagerie.

Si vous souhaitez utiliser une segmentation créée dans Braze, un [Segment Punchh personnalisé]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) basé sur l'inactivité peut être associé à une campagne d'offre groupée récurrente.

Configurations Punchh requises :
- Campaign : Campagne de rappel
- Segment : Choix du client
- Récompense : Choix du client
Considérations :
- La Campaign s'exécute selon une planification

![Un Segment facultatif peut être créé dans Punchh, et un utilisateur éligible reçoit une récompense via une campagne de rappel Punchh. Ensuite, un événement de récompense est déclenché, et le message de rappel notifiant les invités de la récompense est envoyé depuis Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}