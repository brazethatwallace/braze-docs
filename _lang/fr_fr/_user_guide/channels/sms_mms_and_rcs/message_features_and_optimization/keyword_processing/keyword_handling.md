---
nav_title: Gestion personnalisée des mots-clés
article_title: Gestion personnalisée des mots-clés
page_order: 2
description: "Cet article de référence explique comment Braze gère l'envoi de messages bidirectionnel par SMS, MMS et RCS ainsi que les réponses automatiques. Il comprend des explications sur le fonctionnement du déclenchement par mots-clés, les catégories de mots-clés personnalisées et la prise en charge multilingue."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Gestion personnalisée des mots-clés {#custom-keyword-handling}

> Cet article de référence explique comment Braze gère l'envoi de messages bidirectionnel par SMS, MMS et RCS ainsi que les réponses automatiques. Il comprend des explications sur le fonctionnement du déclenchement par mots-clés, les catégories de mots-clés personnalisées et la prise en charge multilingue.

## Envoi de messages bidirectionnel (réponses par mots-clés personnalisés) {#two-way-messaging-custom-keyword-responses}

L'envoi de messages bidirectionnel vous permet d'envoyer des messages et de traiter les réponses à ces messages. Il nécessite que les utilisateurs finaux envoient un mot-clé à Braze, auquel l'utilisateur recevra une réponse automatique. Appliqué correctement, l'envoi de messages bidirectionnel peut être une solution simple, immédiate et dynamique pour le marketing client, permettant de gagner du temps et des ressources.

## Gestion des mots-clés et des réponses automatiques {#managing-keywords-and-auto-responses}

Les SMS, MMS et RCS avec Braze vous offrent la possibilité de créer des déclencheurs de mots-clés, des réponses personnalisées, de définir des ensembles de mots-clés pour plusieurs langues et d'établir des catégories de mots-clés personnalisées.

{% alert note %}
Braze utilise l'ensemble complet de vos mots-clés de désabonnement ([mots-clés par défaut]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/) et [mots-clés personnalisés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/)) pour la gestion exacte des désabonnements et le [désabonnement approximatif]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/).
{% endalert %}

{% tabs %}
{% tab Ajouter des déclencheurs de mots-clés %}

### Ajouter des déclencheurs de mots-clés {#add-keyword-triggers}

En plus des mots-clés d'abonnement et de désabonnement par défaut, vous pouvez également définir vos propres mots-clés pour déclencher des réponses d'abonnement, de désabonnement et d'aide.

Pour définir vos propres mots-clés, procédez comme suit :

1. Dans le tableau de bord de Braze, accédez à **Audience** > **Gestion des groupes d'abonnement** et sélectionnez un groupe d'abonnement **SMS/MMS/RCS**.
2. Sous **Global Keywords**, sélectionnez l'icône de crayon à côté de la catégorie de mots-clés à laquelle vous souhaitez ajouter un mot-clé. ![Mots-clés d'abonnement avec l'icône de crayon affichée.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Dans l'onglet qui s'ouvre, ajoutez un mot-clé que vous souhaitez utiliser pour déclencher cette catégorie de mots-clés. Notez que les mots-clés ne sont pas sensibles à la casse et que les mots-clés universels comme `START`, `YES` et `UNSTOP` ne peuvent pas être modifiés. ![Modification des mots-clés pour la catégorie « Opt-In ». Les mots-clés ajoutés sont « START », « UNSTOP » et « YES ». Le champ du message de réponse indique « You have been unsubscribed to messages from this number. Reply HELP for help. Reply STOP to unsubscribe. Message and data rates may apply. »]({% image_buster /assets/img/sms/keyword_edit2.png %})

Les règles suivantes s'appliquent aux mots-clés et aux réponses de mots-clés :

| Mots-clés | Réponses de mots-clés |
| -------- | ----------------- |
| - Caractères encodés en UTF-8 valides<br>- Maximum de 20 mots-clés par catégorie au total<br>- Longueur maximale de 34 caractères<br>- Longueur minimale de 1 caractère<br>- Ne peuvent pas contenir d'espaces<br>- Doivent être insensibles à la casse et uniques dans le groupe d'abonnement | - Ne peuvent pas être vides<br>- Longueur maximale de 300 caractères<br>- Caractères UTF-8 valides |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ajouter des déclencheurs de mots-clés" }

{% alert tip %}
Vous souhaitez voir comment ces mots-clés peuvent être utilisés dans vos campagnes et Canvas pour recibler et déclencher des messages ? Consultez [Reciblage des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) pour plus d'informations.
{% endalert %}
{% endtab %}

{% tab Gérer les réponses %}

### Gérer les réponses {#manage-responses}

Vous pouvez gérer vos propres réponses envoyées aux utilisateurs après qu'ils ont envoyé un mot-clé correspondant à une catégorie de mots-clés spécifique.

1. Dans le tableau de bord de Braze, accédez à **Audience** > **Gestion des groupes d'abonnement** et sélectionnez un groupe d'abonnement **SMS/MMS/RCS**. <br><br>
2. Sous **Global Keywords**, sélectionnez une catégorie de mots-clés pour modifier une réponse en sélectionnant l'icône de crayon. ![Mots-clés d'abonnement avec l'icône de crayon affichée.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Dans l'onglet qui s'ouvre, modifiez votre réponse. Gardez à l'esprit nos [six règles pour assurer la conformité]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/#the-six-rules-to-get-compliance-right) lors de la création de votre réponse, et lisez les règles suivantes qui s'appliquent aux mots-clés et aux réponses de mots-clés.<br><br>
4. Pour raccourcir automatiquement les URL statiques dans votre réponse, activez le bouton **Link Shortening**. Le compteur de caractères se mettra à jour pour afficher la longueur attendue de l'URL raccourcie. ![Un GIF montrant la mise à jour du compteur de caractères lorsque le bouton « Link Shortening » est activé.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

#### Considérations {#considerations}

| Mots-clés | Réponses de mots-clés |
| -------- | ----------------- |
| - Caractères encodés en UTF-8 valides<br>- Maximum de 20 mots-clés par catégorie au total<br>- Longueur maximale de 34 caractères<br>- Longueur minimale de 1 caractère<br>- Ne peuvent pas contenir d'espaces<br>- Doivent être insensibles à la casse et uniques dans le groupe d'abonnement | - Ne peuvent pas être vides<br>- Longueur maximale de 300 caractères<br>- Caractères UTF-8 valides |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considérations" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Si un Canvas basé sur une action est déclenché par un message SMS, MMS ou RCS entrant, vous pouvez référencer les propriétés SMS, MMS ou RCS dans la première [étape de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) du Canvas.
{% endalert %}

## Prise en charge multilingue {#multi-language-support}

Lors de l'envoi vers certains pays, un expéditeur peut être tenu de prendre en charge les mots-clés entrants et les réponses sortantes dans une langue locale. Pour cela, Braze vous permet de créer un paramètre de mots-clés spécifique à une langue. Une fois créés, les paramètres de mots-clés spécifiques à une langue s'appliqueront à tous les numéros d'envoi du groupe d'abonnement.
![Menu déroulant affichant les langues à ajouter comme paramètre de mots-clés.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Création de mots-clés spécifiques à une langue {#creating-language-specific-keywords}

Sélectionnez **Add a Language** et choisissez votre langue cible ou recherchez une langue dans le menu déroulant.

{% alert important %}
Les langues autres que l'anglais ne sont pas fournies avec des mots-clés et des réponses prédéfinis. Les expéditeurs devront donc travailler avec leurs équipes marketing et juridiques pour ajouter les mots-clés requis à cet ensemble. Sinon, Braze ne traitera pas les messages entrants localisés pour ces langues.
{% endalert %}

Si vous devez supprimer une langue, sélectionnez le bouton **Delete Language** en bas à droite.

![Page des mots-clés globaux avec l'onglet « Italian » sélectionné. Des onglets supplémentaires existent pour chaque langue ajoutée.]({% image_buster /assets/img/sms/multi-language2.png %})

## Catégories de mots-clés personnalisées {#custom-keyword-categories}

En plus des trois catégories de mots-clés par défaut (abonnement, désabonnement et aide), vous pouvez également créer jusqu'à 25 catégories de mots-clés personnalisées. Cela vous permet d'identifier des mots-clés arbitraires et de configurer des réponses spécifiques à votre activité. Un exemple de catégorie pourrait être « PROMO » ou « REMISE », qui pourrait déclencher une réponse sur les promotions en cours ce mois-ci.

Ces mots-clés personnalisés fonctionnent en permanence, ce qui signifie que tout utilisateur abonné à votre service de messagerie peut envoyer des mots-clés et recevoir une réponse à tout moment. En plus de ce comportement, vous avez également la possibilité de définir des mots-clés spécifiques qui ne peuvent être envoyés qu'à [certains moments](#lifecycle-specific-keywords) du cycle de vie de votre utilisateur.

![Mots-clés pour une catégorie « Promo ». Si un utilisateur envoie « YO », il reçoit le message avec un code promotionnel.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Création d'une catégorie personnalisée {#creating-a-custom-category}

Pour créer une catégorie de mots-clés personnalisée, procédez comme suit :

1. Modifiez le groupe d'abonnement approprié.
2. Sélectionnez **Add custom keyword**. ![Champs pour ajouter de nouveaux mots-clés.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Indiquez un nom de catégorie de mots-clés et définissez les mots-clés qu'un utilisateur peut envoyer pour recevoir le message de réponse.

Une fois cette catégorie de mots-clés créée, elle sera disponible pour [filtrer et déclencher]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) dans vos campagnes et Canvas.

Les mots-clés créés dans les catégories de mots-clés personnalisées respectent toutes les règles et validations applicables à la création de nouveaux mots-clés.

### Mots-clés spécifiques au cycle de vie {#lifecycle-specific-keywords}

Si vous avez un cas d'utilisation où vous souhaitez limiter le moment où un client peut envoyer un mot-clé spécifique au cours de son cycle de vie (par exemple, lors de son onboarding initial) pour recevoir une réponse, vous pouvez utiliser le déclencheur **Sent inbound SMS to subscription group within keyword category OTHER** dans votre campagne ou Canvas et définir les mots-clés que vos utilisateurs peuvent envoyer à un moment donné.

Ce déclencheur prend en charge le filtrage sur le message entrant spécifique en utilisant des comparaisons « est » ou « n'est pas » du message, ainsi que des règles d'expression régulière « correspond » ou « ne correspond pas » pour valider la saisie de l'utilisateur.

#### Canvas

![Étape Canvas basée sur une action avec le déclencheur « Send inbound SMS to subscription group "Messaging Service" within keyword category "Other" » où le corps du message correspond à l'expression régulière « caret symbol skip ».]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campaign

![Campaign basée sur une action avec le déclencheur « Send inbound SMS to subscription group "Marketing Message Service A" within keyword category "Other" » où le corps du message est « Keyword1 » ou est « Keyword2 » ou n'est pas « Keyword A ».]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Gestion des mots-clés inconnus {#dealing-with-unknown-keywords}

Nous recommandons vivement de configurer une réponse automatique lorsque des utilisateurs abonnés envoient un texte qui ne correspond à aucun de vos mots-clés définis (géré sous la catégorie de mots-clés **OTHER**).

Pour envoyer une réponse par défaut, par exemple « Désolé ! Nous n'avons pas reconnu ce mot-clé. », procédez comme suit :

1. Créez une [campagne SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/).
2. Pour **Audience cible**, choisissez **Tous les utilisateurs** (le déclencheur limite toujours qui reçoit le message).
3. Pour **Planification**, choisissez **Livraison par événement**.
4. Définissez le déclencheur sur **Send inbound SMS** au groupe d'abonnement approprié **within keyword category OTHER**.
5. Dans l'étape **Messaging**, saisissez le corps de la réponse que vous souhaitez que les utilisateurs reçoivent.

Pour savoir comment Braze gère les messages entrants provenant de numéros de téléphone **inconnus** (avant qu'un profil n'existe), consultez [Gestion des numéros de téléphone inconnus]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/unknown_phone_numbers/).

{% alert tip %}
Vous souhaitez voir comment ces mots-clés et catégories de mots-clés peuvent être utilisés dans vos campagnes et Canvas pour recibler et déclencher des messages ? Consultez [Reciblage des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) pour plus d'informations.
{% endalert %}