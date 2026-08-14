---
nav_title: "Abonnements"
article_title: "Abonnements"
page_order: 5
description: "Cet article de référence couvre les différents états d'abonnement des utilisateurs, comment créer et gérer des groupes d'abonnement, et comment segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - email

---

# Abonnements e-mail {#email-subscriptions}

> Découvrez les états d'abonnement des utilisateurs, comment créer et gérer des groupes d'abonnement, et comment segmenter les utilisateurs en fonction de leurs abonnements.

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

Les groupes d'abonnement sont des filtres de segment qui peuvent affiner davantage votre audience à partir des [états d'abonnement globaux](#subscription-states). Ces groupes vous permettent de proposer des options d'abonnement plus granulaires aux utilisateurs finaux.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

Par exemple, supposons que vous envoyez plusieurs catégories de Campaigns par e-mail (promotionnelles, newsletters ou mises à jour de produits). Dans ce cas, vous pouvez utiliser des groupes d'abonnement pour permettre à vos clients de choisir les catégories d'e-mails auxquelles ils souhaitent s'abonner ou se désabonner en masse depuis une seule page, en utilisant un [centre de préférences e-mail](#email-preference-center). Vous pouvez également utiliser des groupes d'abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d'abonnement pour des e-mails quotidiens, hebdomadaires ou mensuels.

Utilisez les [endpoints des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) pour gérer de manière programmatique les groupes d'abonnement que vous avez enregistrés dans le tableau de bord de Braze sur la page **Groupe d'abonnement**.

### Créer un groupe d'abonnement {#creating-a-subscription-group}

1. Accédez à **Audience** > **Gestion des groupes d'abonnement**.
2. Sélectionnez **Créer un groupe d'abonnement e-mail**.
3. Donnez un nom et une description à votre groupe d'abonnement.
4. Sélectionnez **Enregistrer**.

Tous les groupes d'abonnement sont automatiquement ajoutés à votre centre de préférences.

![Champs pour créer un groupe d'abonnement.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmenter avec un groupe d'abonnement {#segmenting-with-a-subscription-group}

Lors de la création de vos Segments, définissez le nom du groupe d'abonnement comme filtre pour cibler les utilisateurs qui se sont abonnés à votre groupe. Cela est utile pour les newsletters mensuelles, les coupons, les niveaux d'adhésion, et plus encore.

![Exemple de ciblage des utilisateurs dans le segment « Utilisateurs inactifs » avec le filtre pour les utilisateurs du groupe d'abonnement « E-mails hebdomadaires ».]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archiver des groupes d'abonnement {#archiving-subscription-groups}

Les groupes d'abonnement archivés ne peuvent pas être modifiés et n'apparaissent plus dans les filtres de segment ni dans votre centre de préférences. Si vous tentez d'archiver un groupe utilisé comme filtre de segment dans un e-mail, une Campaign ou un Canvas, vous recevez un message d'erreur qui vous empêche d'archiver le groupe tant que vous n'avez pas supprimé toutes les utilisations de celui-ci.

Pour archiver votre groupe depuis la page **Groupes d'abonnement**, procédez comme suit :

1. Trouvez votre groupe dans la liste des groupes d'abonnement.
2. Sélectionnez **Archiver** dans le menu déroulant <i class="fa-solid fa-ellipsis-vertical" aria-label="Plus d'options"></i>&nbsp;.

Braze ne traite pas les changements d'état pour les utilisateurs dans les groupes archivés. Par exemple, si vous archivez le groupe d'abonnement 1 alors qu'Alex y est abonné, Alex reste « abonné » même s'il clique sur un lien de désabonnement. Cela n'a pas d'importance car le groupe d'abonnement 1 est archivé et vous ne pouvez pas envoyer de messages en l'utilisant.

#### Consulter la taille des groupes d'abonnement {#viewing-subscription-group-sizes}

Vous pouvez consulter le graphique **Série temporelle du groupe d'abonnement** sur la page **Groupes d'abonnement** pour visualiser la taille du groupe d'abonnement en fonction du nombre d'utilisateurs sur une période donnée. Ces tailles de groupes d'abonnement sont également cohérentes avec d'autres zones de Braze, comme le calcul de la taille des Segments.

![Un exemple de graphique « Série temporelle du groupe d'abonnement » daté du 2 au 11 décembre. Le graphique montre une augmentation d'environ 10 millions du nombre d'utilisateurs entre le 6 et le 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Pourquoi les comptages de groupes d'abonnement peuvent différer des comptages de Segments {#why-subscription-group-counts-can-differ-from-segment-counts}

Les tailles des groupes d'abonnement correspondent aux Segments qui utilisent uniquement le filtre **Groupe d'abonnement**. Elles peuvent diverger d'un Segment qui utilise **Statut d'abonnement e-mail**, lequel reflète l'[état d'abonnement global aux e-mails](#subscription-states), et non l'appartenance à un groupe spécifique, ou qui combine plusieurs filtres. Par exemple, un utilisateur peut être globalement abonné aux e-mails mais désabonné d'un groupe d'abonnement spécifique.

Pour comparer l'état d'abonnement global d'un utilisateur avec ses appartenances aux groupes d'abonnement, accédez à son profil et sélectionnez l'onglet **Engagement**. Pour filtrer par état global, consultez [Segmenter par abonnements des utilisateurs](#segmenting-by-user-subscriptions).

#### Consulter les groupes d'abonnement dans l'analyse de Campaign {#viewing-subscription-groups-in-campaign-analytics}

Vous pouvez voir le nombre d'utilisateurs qui ont modifié leur état d'abonnement (abonnés ou désabonnés) à partir d'une Campaign par e-mail spécifique sur la page d'analyse de cette Campaign.

1. Depuis la page **Analyse de Campaign** de votre Campaign, faites défiler jusqu'à la section **Performance des messages e-mail**.
2. Sélectionnez la flèche sous **Groupes d'abonnement** pour voir le nombre agrégé de changements d'état, tels que soumis par vos clients.

![La page « Performance des messages e-mail » affichant le nombre agrégé de changements d'état soumis par les clients.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Vérifier le groupe d'abonnement e-mail d'un utilisateur {#checking-a-users-email-subscription-group}

- **Profil utilisateur :** Les profils utilisateur individuels sont accessibles via le tableau de bord de Braze depuis la page [Rechercher des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles). Vous pouvez y rechercher des profils utilisateur par adresse e-mail, numéro de téléphone ou identifiant utilisateur externe. Vous pouvez également consulter les groupes d'abonnement e-mail d'un utilisateur dans l'onglet **Engagement**.
- **REST API de Braze :** Utilisez l'[endpoint Lister les groupes d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou l'[endpoint Lister le statut du groupe d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) pour consulter les groupes d'abonnement du profil d'un utilisateur individuel.

## Centre de préférences e-mail {#email-preference-center}

Le centre de préférences e-mail vous permet de gérer quels utilisateurs reçoivent les newsletters des groupes d'abonnement. Vous le trouverez dans le tableau de bord sous **Subscription Groups**. Chaque groupe d'abonnement que vous créez est ajouté à la liste du centre de préférences.

Pour en savoir plus sur l'ajout ou la personnalisation d'un centre de préférences, consultez [Centre de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

## Modification des abonnements e-mail {#changing-email-subscriptions}

Dans la plupart des cas, les utilisateurs gèrent leur abonnement e-mail via des liens inclus dans les e-mails qu'ils reçoivent. Insérez un pied de page conforme à la législation avec un lien de désabonnement en bas de chaque e-mail. Lorsque les utilisateurs sélectionnent l'URL de désabonnement, Braze les désabonne et affiche une page de destination confirmant le changement. Incluez cette étiquette Liquid : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

{% alert note %}
Vous pouvez utiliser l'étiquette Liquid {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} uniquement dans les Campaigns et les Canvas par e-mail. Vous ne pouvez pas utiliser cette étiquette dans d'autres canaux de communication.
{% endalert %}

Lorsqu'un utilisateur sélectionne « Se désabonner de tous les types d'e-mails ci-dessus » dans le centre de préférences, Braze définit son état d'abonnement e-mail global sur `unsubscribed` et le désabonne de tous les groupes.

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