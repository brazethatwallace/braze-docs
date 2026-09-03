---
nav_title: Groupes d'abonnement
article_title: Groupes d'abonnement
page_order: 4
description: "Découvrez comment les groupes d'abonnement fonctionnent sur les différents canaux de Braze, comment les créer et les gérer, ainsi que le comportement spécifique à chaque canal pour l'e-mail, WhatsApp, les SMS, MMS, RCS et LINE."
---

# Groupes d'abonnement {#subscription-groups}

> Découvrez comment les groupes d'abonnement fonctionnent sur les différents canaux de Braze, comment les créer et les gérer dans le tableau de bord, et où s'appliquent les règles spécifiques à chaque canal.

Les groupes d'abonnement contrôlent quels utilisateurs peuvent recevoir des messages d'un ensemble spécifique de ressources d'envoi au sein d'un canal.

Pour l'e-mail, les groupes d'abonnement sont des filtres de catégories optionnels qui s'ajoutent à l'état d'abonnement global. Pour les SMS, WhatsApp et LINE, les groupes d'abonnement sont des filtres d'audience requis pour chaque envoi. Ils vous permettent d'offrir des choix granulaires d'abonnement et de désabonnement — comme les newsletters par rapport aux promotions, ou les SMS transactionnels par rapport aux SMS marketing — sans modifier l'état d'abonnement global d'un utilisateur lorsqu'il en existe un.

Utilisez les [endpoints des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) pour gérer de manière programmatique les groupes d'abonnement enregistrés dans votre espace de travail Braze.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## État d'abonnement global et groupes d'abonnement {#global-subscription-state-versus-subscription-groups}

Certains canaux disposent à la fois d'un état d'abonnement global et de groupes d'abonnement :

| Canal | État d'abonnement global | Groupes d'abonnement |
| --- | --- | --- |
| E-mail | Abonné volontaire (opted-in), abonné (subscribed) ou désabonné pour tous les e-mails | Catégories optionnelles (par exemple, newsletters ou promotions) au sein de l'e-mail |
| SMS, MMS et RCS | Pas d'état SMS global ; l'abonnement est par groupe | Requis pour chaque envoi ; chaque groupe contient des numéros de téléphone d'envoi ou des expéditeurs RCS |
| WhatsApp | Pas d'état WhatsApp global ; l'abonnement est par groupe | Créés lors de l'intégration de WhatsApp ; chaque groupe correspond à un numéro de téléphone d'envoi |
| LINE | Pas d'état LINE global ; l'abonnement est par groupe | Créés par intégration de canal LINE ; le suivi ou le désabonnement dans l'application LINE détermine l'état |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="État d'abonnement global et groupes d'abonnement" }

Un utilisateur peut être globalement abonné aux e-mails tout en étant désabonné d'un groupe d'abonnement e-mail spécifique. Pour les SMS, un utilisateur peut être abonné à un groupe transactionnel et désabonné d'un groupe promotionnel en même temps.

## Créer un groupe d'abonnement {#create-a-subscription-group}

La manière d'obtenir un groupe d'abonnement dépend du canal. Les groupes e-mail sont créés dans le tableau de bord ; les groupes SMS, MMS et RCS sont provisionnés lors de l'onboarding ; les groupes WhatsApp et LINE sont créés lors de l'intégration du canal. Pour les détails de provisionnement spécifiques à chaque canal, consultez [Comportement spécifique au canal](#channel-specific-behavior).

### E-mail {#email}

1. Accédez à **Audience** > **Gestion des groupes d'abonnement**.
2. Sélectionnez **Créer un groupe d'abonnement e-mail**.
3. Saisissez un nom et une description. Chaque groupe d'abonnement de votre espace de travail doit avoir un nom unique. Si vous saisissez un nom qui existe déjà, le tableau de bord affiche une erreur et n'enregistre pas le groupe.
4. Sélectionnez **Enregistrer**.

![Champs pour créer un groupe d'abonnement.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

## Segmenter avec les groupes d'abonnement {#segment-with-subscription-groups}

Lorsque vous construisez un segment, ajoutez un filtre de groupe d'abonnement pour cibler les utilisateurs qui ont opté pour ce groupe. Cela est utile pour les newsletters mensuelles, les programmes de coupons, les niveaux d'adhésion et d'autres envois basés sur des catégories.

![Exemple de ciblage des utilisateurs du segment « Utilisateurs inactifs » avec le filtre pour les utilisateurs du groupe d'abonnement « E-mails hebdomadaires ».]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

## Archiver les groupes d'abonnement {#archive-subscription-groups}

Les groupes d'abonnement archivés ne peuvent pas être modifiés et n'apparaissent plus dans les filtres de segment ni dans les centres de préférences. Si vous archivez un groupe utilisé comme filtre de segment dans une Campaign, un Canvas ou un segment actif, vous recevez une erreur jusqu'à ce que vous supprimiez ces références.

Pour archiver un groupe depuis **Gestion des groupes d'abonnement**, trouvez le groupe et sélectionnez **Archiver** dans le menu <i class="fa-solid fa-ellipsis-vertical" aria-label="Plus d'options"></i>.

Braze bloque l'envoi de messages aux groupes archivés, vous ne pouvez donc pas utiliser un groupe d'abonnement archivé dans des envois nouveaux ou actifs.

Certains canaux ont des règles d'archivage supplémentaires. Consultez [Groupes d'abonnement LINE](#line-subscription-groups) pour le comportement lié aux espaces de travail et à la réintégration.

## Vérifier les groupes d'abonnement d'un utilisateur {#check-a-users-subscription-groups}

- **Profil utilisateur :** ouvrez un profil depuis [Rechercher des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles). Dans l'onglet **Engagement**, consultez les groupes d'abonnement et les statuts pour l'e-mail, les SMS, WhatsApp et les canaux associés.
- **REST API :** utilisez les endpoints [Lister les groupes d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou [Lister le statut des groupes d'abonnement d'un utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status).

### Mettre à jour le statut d'un groupe d'abonnement {#update-subscription-group-status}

Vous pouvez mettre à jour l'appartenance d'un utilisateur à un groupe d'abonnement via la REST API, le SDK, l'importation d'utilisateurs, le profil utilisateur, le centre de préférences e-mail, l'étape de mise à jour utilisateur dans un Canvas, et d'autres flux spécifiques au canal. Les méthodes exactes dépendent du canal : consultez chaque [section de canal](#channel-specific-behavior) et [Groupes d'abonnement SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#set-a-users-state) pour des conseils de timing spécifiques aux SMS.

## Centres de préférences {#preference-centers}

Les groupes d'abonnement e-mail peuvent apparaître dans un [centre de préférences e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) afin que les utilisateurs puissent gérer leurs abonnements e-mail par catégorie en un seul endroit. Les groupes d'abonnement e-mail actifs peuvent être ajoutés lorsque vous créez un centre de préférences ; les centres de préférences hérités listent automatiquement tous les groupes e-mail actifs.

Pour les SMS et WhatsApp, gérez l'état d'abonnement via la REST API, les flux d'abonnement, les mots-clés (SMS), le profil utilisateur et d'autres méthodes spécifiques au canal dans chaque [section de canal](#channel-specific-behavior).

## Comportement spécifique au canal {#channel-specific-behavior}

### Groupes d'abonnement e-mail {#email-subscription-groups}

Les groupes d'abonnement e-mail s'ajoutent aux [états d'abonnement globaux aux e-mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) (abonné volontaire, abonné et désabonné). Les utilisateurs à l'état global `unsubscribed` ne reçoivent pas d'e-mails, quelle que soit leur appartenance à un groupe d'abonnement.

Détails spécifiques aux e-mails :

- **Centre de préférences :** chaque groupe d'abonnement e-mail que vous créez peut être ajouté à un centre de préférences.
- **Analytique de Campaign :** sur la page **Performances des messages e-mail** d'une Campaign, ouvrez **Groupes d'abonnement** pour voir les totaux d'abonnements et de désabonnements pour cet envoi.

#### Visualiser la taille des groupes d'abonnement {#viewing-subscription-group-sizes}

Dans **Gestion des groupes d'abonnement**, les graphiques chronologiques indiquent :

- **Taille du groupe d'abonnement :** utilisateurs abonnés à ce groupe à une date donnée
- **Taille des désabonnés du groupe d'abonnement :** utilisateurs désabonnés de ce groupe à une date donnée

Ces totaux reflètent l'appartenance à ce groupe, et non l'état d'abonnement global aux e-mails. Ils peuvent différer d'un segment qui utilise **Statut d'abonnement e-mail est Désabonné**, qui reflète l'[état d'abonnement global aux e-mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states).

La taille du groupe d'abonnement du jour n'est pas calculée par défaut. Si votre plage de dates inclut aujourd'hui, sélectionnez **Calculer les statistiques du jour** pour ajouter la valeur du jour à la série temporelle. Pour les très grands espaces de travail, Braze peut afficher des totaux estimés plutôt qu'exacts.

Pour les pieds de page, les pages de désabonnement et la gestion globale des abonnements e-mail, consultez [Abonnements e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions).

### Groupes d'abonnement WhatsApp {#whatsapp-subscription-groups}

Les groupes d'abonnement WhatsApp sont créés lorsque vous [intégrez WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) à votre espace de travail via le portail des partenaires technologiques.

| État | Définition |
| --- | --- |
| Abonné | L'utilisateur a explicitement confirmé vouloir recevoir des messages WhatsApp de votre entreprise. Les utilisateurs peuvent être abonnés via l'API d'abonnement de Braze ou votre flux d'abonnement. |
| Désabonné | L'utilisateur n'a pas opté ou a été retiré du groupe. Les utilisateurs désabonnés ne reçoivent pas de messages WhatsApp provenant des numéros de téléphone de ce groupe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement WhatsApp" }

WhatsApp exige un abonnement explicite. Les mots-clés d'abonnement ne sont pas pris en charge sur ce canal : vous gérez le consentement et l'état d'abonnement vous-même. Pour les flux d'abonnement et de désabonnement, consultez [Abonnements et désabonnements WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

Pour les étapes d'archivage, les mises à jour Canvas et les exemples REST API, consultez [Groupes d'abonnement WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

### Groupes d'abonnement SMS, MMS et RCS {#sms-mms-and-rcs-subscription-groups}

Les groupes d'abonnement SMS, MMS et RCS constituent la base de l'envoi de messages sur ces canaux. Chaque groupe est un ensemble d'[entités d'envoi]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup), telles que des codes courts, des codes longs, des identifiants d'expéditeur alphanumériques ou des expéditeurs vérifiés RCS, pour un objectif de communication spécifique (par exemple, transactionnel versus promotionnel).

| État | Définition |
| --- | --- |
| Abonné | L'utilisateur est abonné pour recevoir des messages de ce groupe d'abonnement, via l'API d'abonnement, des mots-clés d'abonnement ou d'autres flux pris en charge. Avec le [double abonnement]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) activé, les utilisateurs doivent confirmer avant que le statut ne passe à abonné. |
| Désabonné | L'utilisateur s'est désabonné via un mot-clé ou une mise à jour API. Les utilisateurs désabonnés ne reçoivent pas de SMS, MMS ou RCS provenant des expéditeurs de ce groupe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement SMS et RCS" }

Lorsque vous lancez un message SMS ou RCS, vous sélectionnez un groupe d'abonnement dans le compositeur. Braze ajoute un filtre d'audience afin que seuls les utilisateurs abonnés soient ciblés. Braze n'envoie pas de SMS ou RCS aux utilisateurs qui ne sont pas abonnés au groupe sélectionné. Pour recevoir un message SMS de test, le destinataire doit appartenir au groupe d'abonnement que vous sélectionnez pour le test. Pour plus de détails, consultez la [FAQ SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

Les groupes d'abonnement SMS sont provisionnés lors de l'onboarding. Pour les étiquettes MMS, la configuration des expéditeurs RCS, les autorisations géographiques, la migration RCS et la gestion avancée du désabonnement, consultez [Groupes d'abonnement SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

### Groupes d'abonnement LINE {#line-subscription-groups}

Chaque groupe d'abonnement LINE est connecté à une intégration de canal LINE.

| État | Définition |
| --- | --- |
| Abonné | L'utilisateur a suivi le canal LINE dans l'application LINE. Après l'intégration, Braze abonne les utilisateurs lorsqu'ils suivent le canal. |
| Désabonné | L'utilisateur n'a pas suivi le canal ou a cessé de le suivre. Les utilisateurs désabonnés ne reçoivent pas de messages LINE de ce groupe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement LINE" }

LINE est la source de référence pour le statut d'abonnement. Braze traite les événements de suivi et de désabonnement pour mettre à jour les profils.

Les groupes d'abonnement LINE ne peuvent pas être déplacés entre les espaces de travail. Si vous archivez un groupe et réintégrez le canal dans un autre espace de travail, Braze crée un nouveau groupe d'abonnement dans l'espace de travail cible.

Pour le comportement d'archivage, la réconciliation des utilisateurs et les étapes d'intégration, consultez [Groupes d'abonnement LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups) et [Configuration LINE]({{site.baseurl}}/user_guide/channels/line/line_setup).