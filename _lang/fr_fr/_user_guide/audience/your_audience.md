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

Un [profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) constitue une source unique de vérité pour tout ce que Braze sait sur cette personne, notamment :

- Les identifiants (tels que les ID utilisateur ou les ID externes)
- Les appareils et canaux de communication
- Les données comportementales et événements
- Les attributs et préférences
- L'historique d'engagement des messages

Un seul profil utilisateur peut être associé à plusieurs appareils et canaux, ce qui vous permet de comprendre et de contacter une personne de manière globale sur l'ensemble des plateformes.

## Utilisateurs anonymes et utilisateurs identifiés {#anonymous-users-and-identified-users}

Les utilisateurs dans Braze se trouvent généralement dans l'un des deux états suivants.

### Utilisateurs anonymes {#anonymous-users}

Un [utilisateur anonyme]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/) est une personne qui a interagi avec votre application ou votre site web mais qui n'a pas encore reçu d'identifiant de votre système (tel qu'un `external_id`).

- Les utilisateurs anonymes sont automatiquement créés lorsque le SDK Braze s'initialise
- Vous pouvez tout de même suivre les événements, les attributs et l'engagement des messages
- Ces utilisateurs peuvent recevoir des messages, en fonction du canal et du statut d'abonnement

### Utilisateurs identifiés {#identified-users}

Un [utilisateur identifié]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#identified-user-profiles) est un utilisateur qui a été associé à un `external_id` que vous fournissez (par exemple, un ID client ou un ID de compte).

L'identification d'un utilisateur vous permet de :

- Fusionner l'activité entre les appareils et les sessions
- Envoyer des messages de manière cohérente sur l'ensemble des canaux
- Segmenter et personnaliser en utilisant les données utilisateur à long terme
- Gérer les profils via les API et les intégrations

Lorsqu'un utilisateur anonyme est identifié ultérieurement, Braze fusionne les données éligibles dans le profil identifié selon [ce comportement de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior). Par exemple, les jetons de notification push et l'historique de messagerie sont transférés, et de nombreux champs du profil anonyme ne sont fusionnés que lorsqu'ils ne sont pas déjà définis sur le profil identifié ; en cas de conflit de valeurs, le profil identifié est conservé.

## Envoyer des messages aux utilisateurs via les canaux {#message-users-through-channels}

Un [canal]({{site.baseurl}}/user_guide/channels/) est un moyen spécifique par lequel Braze peut délivrer un message à un utilisateur. Les canaux courants incluent :

- [Push (web ou mobile)]({{site.baseurl}}/user_guide/channels/push/)
- [E-mail]({{site.baseurl}}/user_guide/channels/email/)
- [SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/)
- [Messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)
- [Bannières]({{site.baseurl}}/user_guide/channels/banners/)
- [LINE]({{site.baseurl}}/user_guide/channels/line/)
- [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/)

Un seul profil utilisateur peut avoir plusieurs canaux associés, comme une adresse e-mail et un appareil mobile. Braze utilise ce modèle pour coordonner l'envoi de messages cross-canal tout en maintenant une vue unifiée de l'utilisateur.

Chaque canal possède ses propres règles de distribution, exigences d'abonnement et métadonnées, mais tous sont associés au même profil utilisateur.

## Comment les utilisateurs entrent dans Braze {#ways-users-enter-braze}

Les utilisateurs sont créés dans Braze chaque fois qu'une personne interagit avec votre marque via une intégration ou un canal pris en charge. La manière dont ils sont ajoutés dépend de votre implémentation de Braze.

{% tabs %}
{% tab Applications mobiles %}
- Lorsqu'un utilisateur ouvre votre application pour la première fois, le SDK Braze crée un profil utilisateur.
- Les appareils et les jetons de notification push sont automatiquement enregistrés.
- Les événements et les attributs peuvent être enregistrés immédiatement.
{% endtab %}

{% tab Web %}
- Les utilisateurs sont créés lorsque le SDK Web s'initialise.
- Les abonnements aux notifications push web enregistrent un navigateur comme canal de communication.
{% endtab %}

{% tab E-mail et SMS %}
- Les utilisateurs peuvent être créés lorsque vous importez des données, appelez des API ou collectez des abonnements.
- Les adresses e-mail et les numéros de téléphone sont stockés comme identifiants de canal.
- Le statut d'abonnement est suivi par canal et par région.
{% endtab %}

{% tab API et intégrations %}
- Vous pouvez créer ou mettre à jour des utilisateurs directement via les [REST API]({{site.baseurl}}/api/endpoints/user_data/) ou en [importantun CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).
- Les outils externes (tels que les CDP, CRM ou entrepôts de données) peuvent synchroniser automatiquement les utilisateurs dans Braze.
{% endtab %}
{% endtabs %}

## Sources de données d'audience {#audience-data-sources}

Les données utilisateur dans Braze proviennent généralement d'une combinaison de sources.

{% tabs %}
{% tab Collecte automatique %}
Les SDK Braze collectent automatiquement des données contextuelles telles que :

- Le type d'appareil et le système d'exploitation
- La langue et le fuseau horaire
- La version de l'application et l'activité de session
{% endtab %}

{% tab Comportement utilisateur %}
Lorsque les utilisateurs interagissent avec votre application ou vos messages, Braze enregistre :

- Les [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) (par exemple, les achats ou l'utilisation de fonctionnalités)
- Les ouvertures de messages, les clics et les conversions
- L'activité de session et les tendances d'engagement
{% endtab %}

{% tab Vos systèmes %}
Vous pouvez envoyer des données depuis vos propres outils vers Braze en utilisant :

- Les [REST API]({{site.baseurl}}/api/endpoints/user_data/)
- Les [imports CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)
- Les synchronisations de données planifiées

Cela inclut souvent des identifiants, des données de compte ou du contexte historique.
{% endtab %}
{% endtabs %}

### Données fournies par l'utilisateur {#user-provided-input}

Les utilisateurs peuvent fournir des données directement via :

- Les [centres de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/)
- Les formulaires ou enquêtes (SDK ou intégrations)
- Les expériences in-app

### Intégrations {#integrations}

Braze s'intègre avec des plateformes comme [Segment]({{site.baseurl}}/partners/segment/), des entrepôts de données et des partenaires technologiques d'analyse via des intégrations, permettant aux données utilisateur de circuler automatiquement vers les profils utilisateur.

## Gérer les données utilisateur {#manage-user-data}

Vous pouvez ajouter, mettre à jour ou supprimer des données utilisateur de plusieurs manières :

- **Outils du tableau de bord** pour les modifications manuelles ou les imports CSV
- **API** pour les mises à jour en temps réel ou programmatiques
- **SDK** pour capturer le comportement directement dans votre application ou votre site
- **Intégrations** pour la synchronisation continue

Les données peuvent être supprimées en :

- Effaçant les valeurs d'attributs
- Supprimant les étiquettes
- Mettant à jour les statuts d'abonnement
- Réinitialisant les utilisateurs à la déconnexion (pour les cas d'utilisation anonymes)

## Fonctionnalités liées aux données d'audience {#audience-data-features}

Une fois les données utilisateur dans Braze, elles alimentent pratiquement toutes les capacités d'engagement. Plus vos données utilisateur sont complètes et précises, plus vous pouvez utiliser efficacement les fonctionnalités suivantes.

| Fonctionnalité | Description |
| ---- | ---- |
| [Segmentation]({{site.baseurl}}/user_guide/audience/segments/) | Créez des audiences basées sur : {::nomarkdown}<ul><li>Les attributs et champs personnalisés</li> <li>Les événements et comportements</li> <li>L'engagement des messages</li> <li>Les propriétés des appareils et des canaux</li></ul>{:/} <br>Les segments peuvent être réutilisés dans les Campaigns et les Canvas. |
| [Personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/) | Utilisez les données utilisateur pour adapter le contenu, par exemple : {::nomarkdown}<ul><li>Les noms et préférences dans le texte des messages</li> <li>Les recommandations dynamiques</li> <li>Le contenu spécifique à l'emplacement ou à la langue</li></ul>{:/} |
| Automatisation et orchestration  | Déclenchez des messages et des parcours basés sur : {::nomarkdown}<ul><li>Les actions des utilisateurs</li> <li>Les changements d'attributs</li> <li>Les conditions temporelles</li></ul>{:/} |
| Coordination cross-canal | Atteignez les utilisateurs sur le canal le plus approprié tout en respectant : {::nomarkdown}<ul><li>Le statut d'abonnement</li> <li>Les limites de fréquence</li> <li>Les préférences de canal</li></ul>{:/} |
| [Analyse et informations]({{site.baseurl}}/user_guide/analytics/) | Comprenez comment différentes audiences se comportent en analysant : {::nomarkdown}<ul><li>Les taux d'engagement</li> <li>Les parcours de conversion</li> <li>La performance des segments au fil du temps</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnalités liées aux données d'audience" }