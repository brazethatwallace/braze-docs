---
nav_title: Votre audience
article_title: Votre audience Braze
page_order: 0
page_type: reference
description: "Découvrez comment Braze définit et gère vos utilisateurs, identifie les utilisateurs et exploite les données utilisateur pour alimenter la segmentation, la personnalisation et l'envoi de messages cross-canal."

---

# Votre audience Braze {#your-braze-audience}

> Découvrez comment Braze définit et gère vos utilisateurs, identifie les utilisateurs et exploite les données utilisateur pour alimenter la segmentation, la personnalisation et l'envoi de messages cross-canal.

Dans Braze, un utilisateur (et son profil utilisateur) représente une personne individuelle à laquelle vous pouvez envoyer des messages et que vous pouvez analyser.

## Profils utilisateur {#user-profiles}

Un [profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) constitue la source unique de vérité pour tout ce que Braze sait sur une personne, notamment :

- Les identifiants (tels que les ID utilisateur ou les ID externes)
- Les appareils et canaux de communication
- Les données comportementales et événements
- Les attributs et préférences
- L'historique d'engagement aux messages

Un seul profil utilisateur peut être associé à plusieurs appareils et canaux, ce qui vous permet de comprendre et de communiquer avec une personne de manière globale sur l'ensemble des plateformes.

## Utilisateurs anonymes et utilisateurs identifiés {#anonymous-users-and-identified-users}

Les utilisateurs dans Braze se répartissent généralement en deux catégories.

### Utilisateurs anonymes {#anonymous-users}

Un [utilisateur anonyme]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) est une personne qui a interagi avec votre application ou votre site web, mais à laquelle aucun identifiant de votre système n'a encore été attribué (comme un `external_id`).

- Les utilisateurs anonymes sont automatiquement créés lors de l'initialisation du SDK Braze
- Vous pouvez tout de même suivre les événements, les attributs et l'engagement lié aux messages
- Ces utilisateurs peuvent recevoir des messages, en fonction du canal et du statut d'abonnement

#### Utilisateurs anonymes et consentement {#anonymous-users-and-consent}

Si vous devez encapsuler le SDK Braze dans un wrapper de consentement pour respecter vos politiques de consentement, vous pouvez collecter des données anonymes avant que les utilisateurs n'accordent leur consentement. Lors de l'initialisation du SDK, un profil utilisateur anonyme est créé, ce qui vous permet de suivre le comportement tout en respectant les exigences de consentement.

**Envoyer des messages aux utilisateurs anonymes :**
Les utilisateurs anonymes peuvent déclencher et recevoir des messages tant que le SDK Braze reste initialisé. Cela inclut :

- Les [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)
- Les [notifications push]({{site.baseurl}}/user_guide/channels/push) (si les jetons push sont enregistrés)
- Les [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)

Cependant, si vous désactivez ou empêchez l'initialisation du SDK lorsqu'un utilisateur ne donne pas son consentement ou le retire, les canaux déclenchés par le SDK ne fonctionnent pas pour cet utilisateur.

**Cibler les utilisateurs en fonction du statut de consentement :**
Pour envoyer des messages aux utilisateurs en fonction de leur statut de consentement, définissez un attribut utilisateur personnalisé (par exemple `has_marketing_consent`) sur leur profil. Vous pouvez ensuite créer des Segments basés sur cet attribut et maintenir cette valeur synchronisée si les utilisateurs modifient leurs préférences de consentement en dehors de Braze. Pour en savoir plus sur le ciblage des utilisateurs anonymes, consultez [Cas d'usages]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#use-cases).

### Utilisateurs identifiés {#identified-users}

Un [utilisateur identifié]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles) est un utilisateur qui a été associé à un `external_id` que vous fournissez (par exemple, un identifiant client ou un identifiant de compte).

Identifier un utilisateur vous permet de :

- Fusionner l'activité entre les appareils et les sessions
- Envoyer des messages de manière cohérente sur l'ensemble des canaux
- Segmenter et personnaliser en utilisant les données utilisateur à long terme
- Gérer les profils via les API et les intégrations

Lorsqu'un utilisateur anonyme est identifié par la suite, Braze fusionne les données éligibles dans le profil identifié conformément à [ce comportement de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior). Par exemple, les jetons push et l'historique des messages sont conservés, et de nombreux champs du profil anonyme ne sont fusionnés que lorsqu'ils ne sont pas déjà définis sur le profil identifié ; en cas de conflit de valeurs, le profil identifié est conservé.

## Envoyer des messages aux utilisateurs via les canaux de communication {#message-users-through-channels}

Un [canal de communication]({{site.baseurl}}/user_guide/channels) est un moyen spécifique par lequel Braze peut transmettre un message à un utilisateur. Les canaux courants incluent :

- [Notification push (Web ou mobile)]({{site.baseurl}}/user_guide/channels/push)
- [E-mail]({{site.baseurl}}/user_guide/channels/email)
- [SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [Messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [Bannières]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks)

Un même profil utilisateur peut être associé à plusieurs canaux, comme une adresse e-mail et un appareil mobile. Braze utilise ce modèle pour coordonner l'envoi de messages sur l'ensemble des canaux tout en conservant une vue unifiée de l'utilisateur.

Chaque canal possède ses propres règles de distribution, ses exigences d'abonnement et ses métadonnées, mais tous sont associés au même profil utilisateur.

## Comment les utilisateurs entrent dans Braze {#ways-users-enter-braze}

Les utilisateurs sont créés dans Braze chaque fois qu'une personne interagit avec votre marque via une intégration ou un canal pris en charge. La manière dont ils sont ajoutés dépend de la façon dont vous avez implémenté Braze.

{% tabs %}
{% tab Applications mobiles %}
- Lorsqu'un utilisateur ouvre votre application pour la première fois, le SDK Braze crée un profil utilisateur.
- Les appareils et les jetons de notification push sont automatiquement enregistrés.
- Les événements et les attributs peuvent être enregistrés immédiatement.
{% endtab %}

{% tab Web %}
- Les utilisateurs sont créés lorsque le SDK Web s'initialise.
- Les abonnements aux notifications push Web enregistrent un navigateur en tant que canal de communication.
{% endtab %}

{% tab E-mail et SMS %}
- Les utilisateurs peuvent être créés lorsque vous chargez des données, appelez des API ou collectez des abonnements.
- Les adresses e-mail et les numéros de téléphone sont stockés en tant qu'identifiants de canal.
- Le statut d'abonnement est suivi par canal et par région.
{% endtab %}

{% tab API et intégrations %}
- Vous pouvez créer ou mettre à jour des utilisateurs directement via les [REST API]({{site.baseurl}}/api/endpoints/user_data) ou en [important un fichier CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).
- Des outils externes (tels que des CDP, des CRM ou des entrepôts de données) peuvent synchroniser automatiquement les utilisateurs dans Braze.
{% endtab %}
{% endtabs %}

## Sources de données d'audience {#audience-data-sources}

Les données utilisateur dans Braze proviennent généralement d'une combinaison de sources.

{% tabs %}
{% tab Collecte automatique %}
Les SDK Braze collectent automatiquement des données contextuelles telles que :

- Type d'appareil et système d'exploitation
- Langue et fuseau horaire
- Version de l'application et activité de session
{% endtab %}

{% tab Comportement utilisateur %}
Lorsque les utilisateurs interagissent avec votre application ou vos messages, Braze enregistre :

- Les [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) (par exemple, les achats ou l'utilisation de fonctionnalités)
- Les ouvertures de messages, les clics et les conversions
- L'activité de session et les tendances d'engagement
{% endtab %}

{% tab Vos systèmes %}
Vous pouvez envoyer des données depuis vos propres outils vers Braze en utilisant :

- Les [REST API]({{site.baseurl}}/api/endpoints/user_data)
- Les [imports CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- Les synchronisations de données planifiées

Cela inclut souvent des identifiants, des données de compte ou du contexte historique.
{% endtab %}
{% endtabs %}

### Données fournies par l'utilisateur {#user-provided-input}

Les utilisateurs peuvent fournir des données directement via :

- Les [centres de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- Les formulaires ou sondages (SDK ou intégrations)
- Les expériences in-app

### Intégrations {#integrations}

Braze s'intègre avec des plateformes telles que [Segment]({{site.baseurl}}/partners/segment), des entrepôts de données et des partenaires technologiques d'analyse grâce à des intégrations, permettant aux données utilisateur d'alimenter automatiquement les profils utilisateur.

## Gérer les données utilisateur {#manage-user-data}

Vous pouvez ajouter, mettre à jour ou supprimer des données utilisateur de plusieurs façons :

- **Outils du tableau de bord** pour les modifications manuelles ou les imports CSV
- **API** pour les mises à jour en temps réel ou programmatiques
- **SDK** pour capturer le comportement directement dans votre application ou votre site
- **Intégrations** pour une synchronisation continue

Les données peuvent être supprimées en :

- Effaçant les valeurs d'attributs
- Supprimant des tags
- Mettant à jour les états d'abonnement
- Réinitialisant les utilisateurs à la déconnexion (pour les cas d'usage d'utilisateurs anonymes)

## Fonctionnalités des données d'audience {#audience-data-features}

Une fois les données utilisateur intégrées dans Braze, elles alimentent quasiment toutes les capacités d'engagement. Plus vos données utilisateur sont complètes et précises, plus vous pouvez exploiter efficacement les fonctionnalités suivantes.

| Fonctionnalité | Description |
| ---- | ---- |
| [Segmentation]({{site.baseurl}}/user_guide/audience/segments) | Créez des audiences basées sur : {::nomarkdown}<ul><li>Les attributs et les champs personnalisés</li> <li>Les événements et les comportements</li> <li>L'engagement vis-à-vis des messages</li> <li>Les propriétés d'appareil et de canal</li></ul>{:/} <br>Les Segments peuvent être réutilisés dans les Campaigns et les Canvas. |
| [Personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | Utilisez les données utilisateur pour adapter le contenu, par exemple : {::nomarkdown}<ul><li>Noms et préférences dans le texte des messages</li> <li>Recommandations dynamiques</li> <li>Contenu spécifique à l'emplacement ou à la langue</li></ul>{:/} |
| Automatisation et orchestration  | Déclenchez des messages et des parcours en fonction de : {::nomarkdown}<ul><li>Actions de l'utilisateur</li> <li>Changements d'attributs</li> <li>Conditions basées sur le temps</li></ul>{:/} |
| Coordination cross-canal | Contactez les utilisateurs sur le canal le plus approprié tout en respectant : {::nomarkdown}<ul><li>Le statut d'abonnement</li> <li>Les limites de fréquence</li> <li>Les préférences de canal</li></ul>{:/} |
| [Analyse et informations]({{site.baseurl}}/user_guide/analytics) | Comprenez le comportement de différentes audiences en analysant : {::nomarkdown}<ul><li>Les taux d'engagement</li> <li>Les parcours de conversion</li> <li>Les performances des Segments au fil du temps</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnalités des données d'audience" }