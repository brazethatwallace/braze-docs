---
nav_title: "Abonnements"
article_title: "Abonnements"
page_order: 5
description: "Cet article de référence couvre les différents états d'abonnement des utilisateurs, comment gérer les abonnements e-mail, et comment segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - email

---

# Abonnements e-mail {#email-subscriptions}

> Découvrez les états d'abonnement globaux aux e-mails, les pieds de page et les pages de désabonnement, les centres de préférences et le ciblage des Campaigns. Pour les groupes d'abonnement sur tous les canaux, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

Ce document est fourni à titre informatif uniquement. Il n'est pas destiné à fournir, et ne peut être considéré comme fournissant, des conseils juridiques de quelque nature que ce soit. L'envoi d'e-mails marketing et transactionnels peut être soumis à des exigences légales spécifiques. Pour vous assurer que vous agissez en conformité avec toutes les lois, règles et réglementations applicables à votre entreprise, vous devez consulter votre conseiller juridique et/ou votre équipe de conformité réglementaire.

## États d'abonnement {#subscription-states}

Braze utilise des états d'abonnement globaux pour contrôler quels utilisateurs reçoivent des e-mails. Pour les définitions de `opted-in`, `subscribed` et `unsubscribed`, les différences entre l'état global et les groupes d'abonnement, et le fonctionnement de l'état d'abonnement sur les autres canaux, consultez [Statut d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#email).

### Adresses e-mail désabonnées {#unsubscribed-email-addresses}

Braze désabonne automatiquement tout utilisateur qui se désabonne manuellement via un [pied de page personnalisé]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer). Si l'utilisateur met à jour son adresse e-mail et que l'option **Resubscribe users when they update their email** est activée dans **Sending Configuration**, l'envoi normal reprend.

Si un utilisateur signale un ou plusieurs de vos e-mails comme spam, Braze n'envoie que des e-mails transactionnels à cet utilisateur. Les e-mails transactionnels correspondent à l'option **Send to all users including unsubscribed users** dans **Target Audience**.

{% alert tip %}
Consultez nos bonnes pratiques d'[IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) pour des conseils sur la manière de réengager efficacement vos utilisateurs.
{% endalert %}

### Rebonds et e-mails invalides {#bounces-and-invalid-emails}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

Lorsqu'une adresse e-mail subit un échec d'envoi définitif, Braze ne modifie pas automatiquement l'état d'abonnement de l'utilisateur en « désabonné ». Si une adresse subit un échec d'envoi définitif (invalide ou inexistante), Braze la marque comme invalide et ne tente plus d'envoi. Si l'utilisateur change son adresse e-mail, Braze reprend l'envoi. Braze retente les échecs provisoires d'envoi pendant 72 heures.

### Mise à jour des états d'abonnement e-mail {#updating-email-subscription-states}

Il existe quatre façons de mettre à jour l'état d'abonnement e-mail d'un utilisateur :

#### Intégration SDK {#sdk-integration}

Utilisez le SDK Braze pour mettre à jour l'état d'abonnement d'un utilisateur.

#### REST API

Utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour mettre à jour l'[attribut `email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) d'un utilisateur. Par exemple, pour définir l'état d'abonnement e-mail d'un utilisateur comme désabonné lorsqu'il utilise un lien de désabonnement personnalisé, incluez `email_subscribe: "unsubscribed"` dans les attributs utilisateur de votre requête.

#### Profil utilisateur {#user-profile}

1. Trouvez l'utilisateur via **Search Users**.
2. Sous **Engagement**, sélectionnez **Unsubscribed**, **Subscribed** ou **Opted In** pour modifier l'état d'abonnement de l'utilisateur.

Le profil utilisateur affiche également un horodatage indiquant la dernière modification de l'abonnement de l'utilisateur. Un horodatage est enregistré lorsque l'état est **Opted-in** ou **Unsubscribed**, mais pas lorsque l'état est **Subscribed** — par exemple, un profil nouvellement créé qui n'a jamais explicitement confirmé ou refusé l'abonnement n'a pas d'horodatage d'abonnement.

#### Centre de préférences {#preference-center}

Incluez le code Liquid du [centre de préférences](#email-preference-center) en bas de vos e-mails pour permettre aux utilisateurs de s'abonner ou de se désabonner. Braze gère les mises à jour de l'état d'abonnement depuis le centre de préférences.

### Vérification de l'état d'abonnement e-mail {#checking-email-subscription-state}

![Profil utilisateur de John Doe avec son état d'abonnement e-mail défini sur Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez vérifier l'état d'abonnement e-mail d'un utilisateur de la manière suivante :

1. **Export via la REST API :** Utilisez les endpoints [Exporter les utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) ou [Exporter les utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) pour exporter les profils utilisateur individuels au format JSON.
2. **Profil utilisateur :** Trouvez le profil de l'utilisateur sur la page [Rechercher des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles), puis sélectionnez l'onglet **Engagement** pour consulter et mettre à jour manuellement l'état d'abonnement d'un utilisateur.

Lorsqu'un utilisateur met à jour son adresse e-mail, son état d'abonnement est défini sur « abonné ». Si l'adresse e-mail mise à jour existe déjà ailleurs dans un espace de travail Braze, l'utilisateur hérite de l'état d'abonnement de cet utilisateur existant, sauf si l'option **Resubscribe users when they update their email setting** est activée dans **Sending Configuration**.

Pour résoudre les problèmes liés aux changements d'état d'abonnement, consultez **Email Subscription-State Changes** dans les journaux du profil utilisateur pour l'historique et la source. Les sources suivantes peuvent déclencher un changement d'état d'abonnement e-mail :

| Source | Description |
| ------ | ----------- |
| SDK | Mise à jour d'attribut utilisateur envoyée via un SDK Braze |
| REST API | Mise à jour d'attribut utilisateur envoyée via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) |
| Tableau de bord | État d'abonnement modifié manuellement sur la page du profil utilisateur |
| Import CSV | État d'abonnement défini lors d'un import CSV d'utilisateurs |
| Centre de préférences | L'utilisateur a mis à jour ses préférences depuis un centre de préférences hébergé par Braze |
| Page d'abonnement | L'utilisateur a sélectionné un lien de désabonnement dans un e-mail et a accédé à la page d'abonnement Braze |
| List-Unsubscribe | L'utilisateur s'est désabonné via l'en-tête list-unsubscribe natif du client de messagerie |
| Étape de mise à jour utilisateur Canvas | État d'abonnement mis à jour par une [étape de mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update) dans un Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sources de mise à jour de l'état d'abonnement e-mail" }

Lorsque l'état d'abonnement e-mail global d'un utilisateur change, Braze propage cet état aux autres profils partageant la même adresse e-mail, jusqu'à 100 profils par changement. Braze ne garantit pas la propagation lorsque plus de 100 profils partagent la même adresse e-mail. Si des utilisateurs partageant une adresse e-mail affichent des états d'abonnement différents, contactez l'assistance Braze.

## Groupes d'abonnement {#subscription-groups}

Les groupes d'abonnement par e-mail permettent aux utilisateurs de s'abonner ou de se désabonner de catégories d'e-mails spécifiques (telles que les newsletters ou les promotions) sans modifier leur état d'abonnement global aux e-mails. Les groupes que vous créez peuvent être ajoutés à votre [centre de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

Pour plus d'informations sur la création de groupes, la segmentation, l'archivage et le comportement spécifique à chaque canal, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups).

## Centre de préférences e-mail {#email-preference-center}

Le centre de préférences e-mail vous permet de gérer quels utilisateurs reçoivent les newsletters des groupes d'abonnement. Vous le trouverez dans le tableau de bord sous **Subscription Groups**. Chaque groupe d'abonnement que vous créez est ajouté à la liste du centre de préférences.

Pour en savoir plus sur la manière d'ajouter ou de personnaliser un centre de préférences, consultez [Centre de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

## Modification des abonnements e-mail {#changing-email-subscriptions}

Dans la plupart des cas, les utilisateurs gèrent leur abonnement e-mail via des liens inclus dans les e-mails qu'ils reçoivent. Insérez un pied de page conforme à la législation avec un lien de désabonnement en bas de chaque e-mail. Lorsque les utilisateurs sélectionnent l'URL de désabonnement, Braze les désabonne et affiche une page de destination confirmant le changement. Incluez cette étiquette Liquid : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

{% alert note %}
Vous pouvez utiliser l'étiquette Liquid {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} uniquement dans les Campaigns et les Canvas par e-mail. Vous ne pouvez pas utiliser cette étiquette dans d'autres canaux de communication.
{% endalert %}

Lorsqu'un utilisateur sélectionne « Se désabonner de tous les types d'e-mails répertoriés » dans le centre de préférences, Braze définit son état d'abonnement e-mail global sur `unsubscribed` et le désabonne de tous les groupes.

Les désabonnements côté destinataire — liens de désabonnement, list-unsubscribe, soumissions du centre de préférences et désabonnements signalés par le fournisseur de services de messagerie — apparaissent dans la table Snowflake `USERS_MESSAGES_EMAIL_UNSUBSCRIBE`. Les désabonnements effectués via la REST API ne sont pas inclus dans cette table ; ils émettent à la place des événements [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) ou [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events). Pour le schéma de la table, consultez [USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED).

### Création de pieds de page personnalisés {#custom-footer}

Si vous ne souhaitez pas utiliser le pied de page par défaut, créez un pied de page e-mail personnalisé à l'échelle de l'espace de travail et intégrez-le dans chaque e-mail en utilisant {% raw %}`{{${email_footer}}}`{% endraw %}.

Cela vous évite de créer un nouveau pied de page pour chaque modèle d'e-mail ou Campaign par e-mail. Pour les étapes détaillées, consultez [Pied de page e-mail personnalisé]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer).

#### Gestion des états d'abonnement pour les adresses IP chinoises {#managing-subscription-states-for-chinese-ip-addresses}

Si vous prévoyez des adresses IP chinoises, ne vous fiez pas uniquement à un lien de désabonnement pour maintenir les listes de désabonnés (`unsubscribed`). Proposez des chemins de désabonnement alternatifs tels qu'un ticket d'assistance ou une adresse e-mail de conseiller client.

### Création d'une page de désabonnement personnalisée {#creating-a-custom-unsubscribe-page}

Lorsque les utilisateurs sélectionnent une URL de désabonnement dans un e-mail, ils accèdent à une page par défaut qui confirme le changement d'abonnement.

Pour utiliser une page de destination personnalisée à la place :

1. Accédez à **Email Preferences** > **Subscription Pages and Footers**.
2. Ajoutez le HTML de votre page personnalisée.

Incluez un lien de réabonnement (par exemple {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) pour que les utilisateurs puissent annuler un désabonnement accidentel. Comme pour {% raw %}`${set_user_to_unsubscribed_url}`{% endraw %}, vous pouvez utiliser cette étiquette uniquement dans les Campaigns et les Canvas par e-mail.

Vous pouvez également rediriger les utilisateurs vers votre site et mettre à jour le statut avec la REST API de Braze (par exemple un lien avec {% raw %}`?user_id={{${user_id}}}`{% endraw %} puis appeler [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)).

{% alert note %}
Si vous utilisez le pied de page du tableau de bord au lieu d'un simple bloc de contenu HTML, le modèle doit toujours contenir {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} pour pouvoir être enregistré. Pour utiliser temporairement une URL de désabonnement différente, vous pouvez commenter l'étiquette par défaut. Par exemple : {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![Page de désabonnement personnalisée avec un aperçu « Désolé de vous voir partir ! ».]({% image_buster /assets/img/custom_unsubscribe.png %})

### Création d'une page d'abonnement personnalisée {#creating-a-custom-opt-in-page}

Utilisez une page d'abonnement personnalisée pour permettre aux utilisateurs de prendre connaissance et de contrôler leurs préférences de notification avant l'abonnement. Cette communication supplémentaire peut aider vos Campaigns par e-mail à éviter les dossiers de spam.

1. Accédez à **Settings** > **Email Preferences**.
2. Sélectionnez **Subscription Pages and Footers**.
3. Personnalisez le style dans la section **Custom opt-in page** pour voir comment cela indique à vos utilisateurs qu'ils ont été abonnés.

Les utilisateurs accèdent à cette page via l'étiquette {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. Comme pour les autres étiquettes Liquid d'abonnement e-mail, vous pouvez utiliser cette étiquette uniquement dans les Campaigns et les Canvas par e-mail.

{% alert tip %}
Utilisez un processus de double abonnement pour améliorer votre portée. Braze envoie un e-mail de confirmation supplémentaire dans lequel l'utilisateur confirme ses préférences de notification via un lien. Après confirmation, l'abonnement de l'utilisateur est confirmé.
{% endalert %}

![E-mail d'abonnement personnalisé avec le message « Heureux de voir que vous souhaitez toujours avoir de nos nouvelles ».]({% image_buster /assets/img/custom_optin.png %})

## Abonnements et ciblage des Campaigns {#subscriptions-and-campaign-targeting}

Par défaut, Braze cible les Campaigns avec des notifications push ou des e-mails vers les utilisateurs qui sont abonnés ou dont l'abonnement est confirmé. Modifiez cela dans **Target Audience** en sélectionnant le menu déroulant à côté de **Send to these users:**.

Braze prend en charge trois états de ciblage :

- Les utilisateurs qui sont abonnés ou dont l'abonnement est confirmé (par défaut).
- Uniquement les utilisateurs dont l'abonnement est confirmé.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer à toutes les [lois anti-spam]({{site.baseurl}}/help/best_practices/spam_regulations#spam-regulations) applicables lors de l'utilisation de ces paramètres de ciblage.
{% endalert %}

## Segmentation par abonnements des utilisateurs {#segmenting-by-user-subscriptions}

Utilisez les filtres « Email Subscription Status » et « Push Subscription Status » pour segmenter les utilisateurs par état d'abonnement.

Utilisez cette approche pour cibler les utilisateurs qui ne se sont ni abonnés ni désabonnés et les encourager à confirmer explicitement leur abonnement. Créez un segment avec le filtre « Email/Push Subscription Status is Subscribed » et envoyez des Campaigns aux utilisateurs qui sont abonnés mais dont l'abonnement n'est pas confirmé.

![État d'abonnement e-mail utilisé comme filtre de segment.]({% image_buster /assets/img_archive/not_optin.png %})