---
nav_title: Profils utilisateur
article_title: Profils utilisateur
page_order: 2
page_type: reference
tool:
  - Dashboard
description: "Cet article de référence décrit comment accéder au profil d'un utilisateur dans le tableau de bord, les cas d'usage des profils et ce que chaque profil contient."

---

# Profils utilisateur {#user-profiles}

> Les profils utilisateur sont un excellent moyen de trouver des informations sur des utilisateurs spécifiques. Toutes les données persistantes associées à un utilisateur sont stockées dans son profil utilisateur.

## Accéder aux profils {#access-profiles}

Pour accéder au profil d'un utilisateur, rendez-vous sur la page **Search Users** et recherchez un utilisateur à l'aide de l'un des critères suivants :

- ID utilisateur externe
- ID Braze
- E-mail
- Numéro de téléphone
- Jeton push
- Alias d'utilisateur au format « [user_alias]:[alias_name] », par exemple « amplitude_id:user_123 »

Si une correspondance est trouvée, vous pouvez consulter les informations que vous avez enregistrées pour cet utilisateur avec le SDK Braze. Si votre recherche renvoie plusieurs profils utilisateurs, vous pouvez fusionner chaque profil individuellement ou effectuer une fusion en masse. Pour un guide complet, consultez [Fusionner les utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

{% alert note %}
**Search Users** n'est pas la même chose que **User Lookup** dans le compositeur de Segment ou de Campaign. **User Lookup** vérifie si un utilisateur spécifique correspond à votre audience et n'accepte que `external_id` ou `braze_id`. **Search Users** sur cette page prend en charge l'e-mail, le téléphone, le jeton push et l'alias d'utilisateur. Pour plus d'informations, consultez [Tester les segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).
{% endalert %}

{% alert important %}
Lorsqu'un numéro de téléphone est utilisé dans la recherche, il est converti au format [`E.164`](https://en.wikipedia.org/wiki/e.164). Les utilisateurs dont le numéro de téléphone ne peut pas être converti au format `E.164` (par exemple, parce que le numéro comporte un indicatif de pays ou de zone invalide) ne peuvent pas être recherchés par numéro de téléphone.
{% endalert %}

![Résultats de recherche avec une bannière indiquant « Plusieurs utilisateurs correspondent à vos critères de recherche » et deux boutons intitulés Précédent et Suivant.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Cas d'usage {#use-cases}

Les profils utilisateurs constituent une ressource précieuse pour la résolution des problèmes et les tests, car vous pouvez facilement accéder aux informations relatives à l'historique d'engagement d'un utilisateur, à son appartenance à un Segment, à son appareil et à son système d'exploitation.

Par exemple, si un utilisateur signale un problème et que vous ne savez pas quel appareil ni quel système d'exploitation il utilise, vous pouvez consulter l'[onglet Aperçu](#overview-tab) pour trouver ces informations (à condition de disposer de son e-mail ou de son ID utilisateur). Vous pouvez également consulter la langue d'un utilisateur, ce qui peut s'avérer utile si vous résolvez un problème lié à une [campagne multilingue]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) qui ne s'est pas comportée comme prévu.

Vous pouvez utiliser l'[onglet Engagement](#engagement-tab) pour vérifier si un utilisateur donné a reçu une Campaign. De plus, si cet utilisateur a effectivement reçu la Campaign, vous pouvez voir quand il l'a reçue. Vous pouvez également vérifier si un utilisateur fait partie d'un certain Segment et s'il est abonné aux notifications push, aux e-mails, ou aux deux. Ces informations sont utiles à des fins de résolution des problèmes. Par exemple, vous devriez vérifier ces informations si un utilisateur ne reçoit pas une Campaign que vous vous attendiez à ce qu'il reçoive, ou s'il reçoit une Campaign que vous ne vous attendiez pas à ce qu'il reçoive.

## Éléments du profil utilisateur {#elements-of-user-profile}

Le profil d'un utilisateur comporte cinq sections principales.

- **Aperçu :** Informations de base sur l'utilisateur, données de session, attributs personnalisés, événements personnalisés, achats et dernier appareil sur lequel l'utilisateur s'est connecté.
- **Engagement :** Informations sur les paramètres de contact de l'utilisateur, les Campaigns reçues, les Segments, les statistiques de communication, l'attribution d'installation et le numéro de compartiment aléatoire.
- **Historique des événements :** Événements personnalisés et achats des 30 derniers jours, avec les propriétés d'événement complètes affichées en JSON.
- **Historique de communication :** Événements récents liés à la communication pour cet utilisateur au cours des 30 derniers jours.
- **Éligibilité aux feature flags :** Vérifiez les feature flags auxquels un utilisateur est actuellement éligible à travers les déploiements, les étapes Canvas et les expériences.

{% tabs %}
{% tab Onglet Aperçu %}

### Onglet Aperçu {#overview-tab}

L'onglet **Aperçu** contient les informations de base sur un utilisateur et ses interactions avec votre application ou site web.

| Catégorie de l'aperçu | Contenu |
| --- | --- |
| Profil | Genre, tranche d'âge, localisation, langue, paramètres régionaux, fuseau horaire et date de naissance. |
| Aperçu des sessions | Nombre de sessions, dates de la première et de la dernière session, et sur quelles applications. |
| Attributs personnalisés | Attributs personnalisés associés à cet utilisateur et leurs valeurs, y compris les attributs personnalisés imbriqués. |
| Appareils récents | Nombre d'appareils sur lesquels l'utilisateur s'est connecté, détails de chaque appareil et identifiants publicitaires associés (le cas échéant). |
| Événements personnalisés | Événements personnalisés effectués par cet utilisateur, nombre d'occurrences et date de la dernière exécution de chaque événement. |
| Achats | Chiffre d'affaires total attribué à cet utilisateur, dernier achat, nombre total d'achats et liste de chaque achat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Onglet Aperçu" }

Pour en savoir plus sur ces données, consultez [Collecte de données du SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

{% endtab %}
<a id="engagement-tab"></a>
{% tab Onglet Engagement %}

### Onglet Engagement {#engagement-tab}

L'onglet **Engagement** contient des informations sur les interactions d'un utilisateur avec les messages que vous lui avez envoyés via Braze.

| Catégorie d'engagement | Contenu |
| --- | --- |
| Paramètres de contact | Statut d'abonnement pour l'e-mail, le SMS et les notifications push, ainsi que les groupes d'abonnement auxquels cet utilisateur est associé pour ces trois canaux. Cette section inclut également les informations du journal des modifications pour les jetons push. Consultez les articles sur l'[e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions), le [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) et les [notifications push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) pour en savoir plus sur la configuration des abonnements et des opt-ins. |
| Campaigns reçues | **Campaigns reçues** reflète les horaires d'envoi et de consultation spécifiques à chaque canal. La plupart des canaux enregistrent un envoi lorsque Braze transmet le message au fournisseur de distribution, même si le message n'est finalement pas distribué. Les **Content Cards** fonctionnent différemment : les Campaigns n'apparaissent ici qu'après que l'utilisateur a consulté la carte dans l'application. Pour un détail par canal, consultez [Quand les Campaigns apparaissent dans Campaigns reçues](#when-campaigns-appear-in-campaigns-received). <br><br>Lorsqu'un message est reçu, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal que le profil ayant enregistré l'interaction (par exemple, la même adresse e-mail pour l'e-mail, ou le même numéro de téléphone pour le SMS ou WhatsApp). Les utilisateurs partageant un identifiant avec quelqu'un qui a reçu, ouvert ou cliqué le message peuvent correspondre à ce filtre même s'ils ne faisaient pas partie de la Campaign à l'origine ou n'ont pas reçu directement le message.<br><br>Ces listes utilisent les [données d'interaction de communication]({{site.baseurl}}/api/data_retention/messaging_interaction_data) (y compris les règles d'expiration) pour déterminer ce qui apparaît pour le reciblage et l'historique.<br><br> Sélectionnez une Campaign dans la liste pour la consulter. |
| Segments | Segments auxquels cet utilisateur appartient. Sélectionnez un Segment dans la liste pour le consulter. |
| Statistiques de communication | Date du dernier message reçu par cet utilisateur pour chaque canal. |
| Attribution d'installation | Informations sur la manière et le moment où un utilisateur a installé votre application. En savoir plus sur la [compréhension des installations utilisateur]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution). |
| Divers | Le [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) de l'utilisateur. |
| Messages Canvas reçus | Messages Canvas reçus par cet utilisateur et leur date. Les horaires d'envoi suivent les mêmes règles par canal que **Campaigns reçues** ; consultez [Quand les Campaigns apparaissent dans Campaigns reçues](#when-campaigns-appear-in-campaigns-received).<br><br> Lorsqu'un message est reçu, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal que le profil ayant enregistré l'interaction (par exemple, la même adresse e-mail pour l'e-mail, ou le même numéro de téléphone pour le SMS ou WhatsApp). Les utilisateurs partageant un identifiant avec quelqu'un qui a reçu, ouvert ou cliqué le message peuvent correspondre à ce filtre même s'ils ne faisaient pas partie de la Campaign à l'origine ou n'ont pas reçu directement le message.<br><br> Sélectionnez un message dans la liste pour le consulter. |
| Prédictions | Scores de [prédiction d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) et de [prédiction d'événements]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) pour cet utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Onglet Engagement" }

{% endtab %}
<a id="event-history-tab"></a>
{% tab Onglet Historique des événements %}

### Onglet Historique des événements {#event-history-tab}

{% alert note %}
Pour consulter l'onglet **Historique des événements**, vous devez disposer des [permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) **Search Users**, **View User Event Properties** et **View PII**, car les propriétés d'événement peuvent contenir des données personnelles.
{% endalert %}

L'onglet **Historique des événements** affiche les événements personnalisés et les achats enregistrés par un utilisateur. Utilisez-le pour vérifier que les données d'événement arrivent correctement et résoudre les problèmes au niveau utilisateur directement dans le tableau de bord, sans export de données ni outil externe.

| Catégorie de l'historique des événements | Contenu |
| --- | --- |
| Liste des événements | Événements personnalisés et achats des 30 derniers jours (jusqu'aux 100 plus récents), classés du plus récent au plus ancien. |
| Type d'événement | Indique si la ligne est un **événement personnalisé** ou un **achat**. |
| Horodatage | Date et heure d'enregistrement de l'événement. |
| Nom de l'événement | Nom de l'événement personnalisé ou de l'achat. |
| Propriétés d'événement | Propriétés d'événement complètes, affichées en JSON. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Onglet Historique des événements" }

{% endtab %}
{% endtabs %}

### Quand les Campaigns apparaissent dans Campaigns reçues {#when-campaigns-appear-in-campaigns-received}

De manière générale, Braze affiche une Campaign dans **Campaigns reçues** après avoir tenté d'envoyer le message. La distribution effective sur l'appareil ou dans la boîte de réception de l'utilisateur n'est pas requise pour qu'un envoi soit enregistré. **Messages Canvas reçus** suit les mêmes règles spécifiques à chaque canal pour chaque type de message Canvas.

{% alert tip %}
Lorsque les horodatages sont affichés en format relatif (par exemple « il y a 6 jours »), survolez-les pour voir la date et l'heure exactes.
{% endalert %}

- **E-mail :** Braze enregistre un envoi lorsque le message est transmis à votre fournisseur de services d'e-mailing (ESP). Après cette transmission, le message n'est pas annulé en raison de la logique Liquid, de la limitation du débit ou du marquage de l'utilisateur comme injoignable. Les événements suivants sont généralement une distribution ou un rebond.
- **Notification push :** Braze enregistre un envoi lorsque le message est transmis au fournisseur push (par exemple, Apple Push Notification service (APNs) ou Firebase Cloud Messaging (FCM)). Le fournisseur tente généralement de distribuer immédiatement ; si l'appareil est indisponible (par exemple, hors ligne), le fournisseur peut réessayer jusqu'à l'expiration du message.
- **Messages in-app :** Braze enregistre un envoi lorsque la Campaign est lancée.
- **Content Cards :** Le moment où Braze enregistre un événement _Sent_ dépend du type de distribution et de votre paramètre **Card Creation**. Une Campaign de Content Cards n'apparaît dans **Campaigns reçues** sur le profil utilisateur qu'après que l'utilisateur a consulté la carte dans l'application. Pour le détail complet, consultez [Quand les envois sont enregistrés]({{site.baseurl}}/user_guide/channels/content_cards/reporting#when-sends-are-logged) et [Campaigns reçues et filtres de reciblage]({{site.baseurl}}/user_guide/channels/content_cards/reporting#campaigns-received-and-retargeting-filters) dans l'article sur le reporting des Content Cards.
- **SMS, WhatsApp et webhooks :** Braze enregistre un envoi lorsque le message entre dans le chemin de distribution de ce canal (par exemple, le fournisseur SMS ou WhatsApp, ou votre endpoint webhook).

{% alert note %}
Ces descriptions couvrent le moment où un envoi est enregistré pour **Campaigns reçues**. Elles sont distinctes des [annulations de messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) qui peuvent arrêter un message avant qu'il n'atteigne un fournisseur.
{% endalert %}

![L'onglet Engagement d'un profil utilisateur affichant les paramètres de contact et les statistiques de communication.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Onglet Historique de communication {#messaging-history-tab}

L'onglet **Historique de communication** du profil utilisateur affiche les événements récents liés à la communication (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements incluent les messages envoyés à l'utilisateur, reçus, avec lesquels il a interagi, et plus encore.

Les données de cet onglet ne sont pas mises à jour après la fusion d'un utilisateur. De plus, les événements associés aux messages envoyés via l'API (par exemple, l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#creating-new-users-with-api-sends)) n'apparaissent pas dans cet onglet si aucun identifiant de Campaign n'est spécifié dans ces envois.

{% alert important %}
Les événements RCS ne sont actuellement pas pris en charge dans l'onglet **Historique de communication**.
{% endalert %}

![L'onglet Historique de communication montrant les Campaigns et Canvas qu'un utilisateur a reçus.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Consulter et comprendre les événements {#viewing-and-understanding-events}

Pour chaque événement du tableau **Historique de communication**, vous pouvez voir le canal de communication, le type d'événement, l'horodatage de l'événement, la Campaign ou le message Canvas associé, ainsi que les données de l'appareil de l'utilisateur. Pour filtrer des événements spécifiques, cliquez sur **Filtres** et sélectionnez les événements dans la liste.

##### Événements d'engagement liés aux messages {#message-engagement-events}

Les événements d'engagement suivants sont disponibles pour l'e-mail, le SMS, les notifications push, les messages in-app, les Content Cards et les webhooks. Pour en savoir plus sur le suivi de chaque événement, consultez le [Glossaire des événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

| Canal | Événements d'engagement disponibles |
| --- | --- |
| E-mail | Rebond<br>Clic<br>Événements de report<br>Distribution<br>Signalement comme spam<br>Ouverture (voir [note sur l'événement d'ouverture d'e-mail](#note-on-email-open-event))<br>Envoi<br>Échec provisoire d'envoi<br>Désabonnement |
| SMS | Envoi par l'opérateur<br>Distribution<br>Échec de distribution<br>Réception entrante<br>Rejet<br>Envoi |
| Notification push | Rebond<br>Ouverture influencée<br>iOS Foreground<br>Ouverture<br>Envoi |
| Message in-app | Clic<br>Impression |
| Content Cards | Clic<br>Rejet<br>Impression<br>Envoi |
| Webhooks | Envoi |
| WhatsApp | Annulation<br>Distribution<br>Échec<br>Limite de fréquence atteinte<br>Réception entrante<br>Lecture<br>Envoi |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements d'engagement liés aux messages" }

##### Événements d'annulation de message {#message-abort-events}

Les événements d'annulation de message se produisent lorsqu'un message envoyé à un utilisateur est annulé en raison d'une logique conditionnelle dans [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) ou le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content), ou en raison de délais d'expiration du rendu Liquid.

Les événements d'annulation sont disponibles pour les canaux suivants :

- E-mail
- SMS
- Notification push
- Webhooks

Les événements d'annulation ne sont actuellement pas disponibles pour les messages in-app et les Content Cards.

##### Événements de limite de fréquence {#frequency-cap-events}

Un événement de limite de fréquence se produit lorsqu'un utilisateur est éligible pour recevoir un message, mais ne le reçoit pas en raison des paramètres de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Vous pouvez personnaliser les paramètres de limite de fréquence depuis **Paramètres** > **Règles de limite de fréquence**.

##### Destinations vides {#blank-destinations}

Certains envois de messages peuvent apparaître dans l'historique de communication avec des destinations vides (signalées par « — »). Cela s'explique par le fait que certains canaux, comme les Content Cards et les webhooks, ne collectent pas de données d'appareil lors de l'envoi du message.

Les envois de Content Cards sont enregistrés lorsque la carte est disponible pour consultation. Comme les Content Cards peuvent être consultées sur plusieurs appareils, les données d'appareil ne sont pas enregistrées lors de l'envoi. Ces informations sont plutôt enregistrées lors de l'impression (lorsque la carte est effectivement consultée). Les webhooks sont envoyés à un endpoint système (et non à un appareil), les données d'appareil ne sont donc pas applicables.

#### Note sur l'événement d'ouverture d'e-mail {#note-on-email-open-event}

Le suivi des ouvertures d'e-mail est sujet aux erreurs dans tout outil, y compris Braze. Avec les diverses fonctionnalités de protection de la vie privée proposées par les différents clients de messagerie, qui bloquent le chargement automatique des images ou les chargent de manière proactive sur le serveur, les événements d'ouverture d'e-mail sont susceptibles de générer des faux positifs comme des faux négatifs.

Bien que les statistiques d'ouverture d'e-mail puissent être utiles de manière agrégée, par exemple pour comparer l'efficacité de différentes lignes d'objet, vous ne devez pas considérer qu'un événement d'ouverture individuel pour un utilisateur donné est significatif.

#### Pourquoi certains champs sont-ils vides dans l'onglet Historique de communication ? {#why-are-certain-fields-blank-in-the-message-history-tab}

Certains champs peuvent être absents dans l'onglet **Historique de communication** d'un utilisateur dans les scénarios suivants :

- Lorsqu'un événement ne contient pas de données pour **Message envoyé**, cela indique que la Campaign ne comporte aucune variante de message.
- Lorsqu'un événement ne contient pas de données pour **Campaign/Canvas** et **Message envoyé**, cela indique que ce message a été envoyé depuis une Campaign API (et non des Campaigns déclenchées par API) qui n'a pas spécifié les paramètres `campaign_id` et `message_variation_id`. Ces champs sont facultatifs et peuvent être omis du corps de la requête. Lorsque ces champs sont spécifiés, les informations sont renseignées dans les journaux de l'historique de communication.
   - Si un message particulier est totalement absent de l'historique de communication mais apparaît dans le journal **Campaigns reçues**, il est probable que l'utilisateur a reçu la Campaign avant d'être identifié comme l'utilisateur actuel. Si un profil existant est orphelin, le journal **Campaigns reçues** est transféré, mais l'historique de communication ne l'est pas.
- Lorsque les données sont manquantes pour **Campaign/Canvas**, un test manuel a peut-être été envoyé. Les tests manuels sont enregistrés dans l'onglet **Historique de communication**, mais la Campaign ou le Canvas envoyé ne sera pas enregistré.
- Lorsqu'un utilisateur fait partie d'un groupe initiateur ou d'une autre audience de test interne, l'**Historique de communication** peut afficher des métadonnées de Campaign ou de Canvas limitées par rapport aux envois en production.

## Articles connexes {#related-articles}

- [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [POST : Exporter un profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [POST : Supprimer des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)