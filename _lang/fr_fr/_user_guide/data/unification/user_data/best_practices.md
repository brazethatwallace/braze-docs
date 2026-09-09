---
nav_title: Bonnes pratiques de collecte
article_title: Bonnes pratiques de collecte
page_order: 4
page_type: reference
description: "Cet article aide à clarifier les différentes méthodes et bonnes pratiques pour la collecte de données sur les utilisateurs nouveaux et existants."

---

# Bonnes pratiques de collecte {#collection-best-practices}

> Savoir quand et comment collecter les données des utilisateurs connus et inconnus peut s'avérer difficile lorsque vous envisagez le cycle de vie du profil utilisateur de vos clients. Cet article aide à clarifier les différentes méthodes et bonnes pratiques pour la collecte de données d'utilisateurs nouveaux et existants en vous guidant à travers un cas d'usage.

L'exemple suivant est un cas d'usage de collecte d'e-mails, mais la logique s'applique à de nombreux scénarios de collecte de données différents. Dans cet exemple, nous supposons que vous avez déjà intégré un formulaire d'inscription ou une autre façon de recueillir des informations sur l'utilisateur.

Lorsqu'un utilisateur vous fournit des informations à enregistrer, nous vous recommandons de vérifier si les données existent déjà dans votre base de données et, le cas échéant, de créer un profil d'alias utilisateur ou de mettre à jour le profil utilisateur existant.

Si un utilisateur inconnu consulte votre site puis, à une date ultérieure, crée un compte ou s'identifie par le biais d'une inscription par e-mail, la fusion des profils doit être gérée avec précaution. En fonction de la méthode utilisée pour la fusion, les informations relatives aux utilisateurs avec alias uniquement ou les données anonymes peuvent être écrasées.

## Capture de données utilisateur via un formulaire web {#capturing-user-data-through-a-web-form}

### Étape 1 : Vérifier si l'utilisateur existe {#step-1-check-if-the-user-exists}

Lorsqu'un utilisateur saisit des informations via un formulaire web, vérifiez si un utilisateur possédant cette adresse e-mail existe déjà dans votre base de données. Vous pouvez procéder de l'une des manières suivantes :

- **Vérifier la base de données interne (recommandé) :** Si vous disposez d'un enregistrement externe ou d'une base de données contenant les informations utilisateur fournies en dehors de Braze, consultez-la au moment de la soumission de l'e-mail ou de la création du compte pour confirmer que les informations n'ont pas déjà été capturées.
- **[Endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) :** Utilisez `email` comme identifiant, et un nouveau profil utilisateur sera créé si l'adresse e-mail n'existe pas encore.
- **[Endpoint `/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) :** Si vous collectez les adresses e-mail via un formulaire personnalisé, puis définissez l'appartenance au groupe d'abonnement via la REST API, appelez d'abord cet endpoint. Si aucun profil correspondant n'existe, créez ou abonnez l'utilisateur avec l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Sinon, mettez à jour le profil existant au lieu de créer un doublon.

### Étape 2 : Enregistrer ou mettre à jour l'utilisateur {#step-2-log-or-update-user}

- **Si un utilisateur existe :**
  - Ne créez pas de nouveau profil.
  - Enregistrez un attribut personnalisé (par exemple, `newsletter_subscribed: true`) sur le profil de l'utilisateur pour indiquer qu'il a soumis son adresse e-mail via une inscription à une newsletter. Si plusieurs profils utilisateur Braze possèdent la même adresse e-mail, tous les profils seront exportés.<br><br>
- **Si un utilisateur n'existe pas :**
  - Créez un profil alias uniquement via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Cet endpoint accepte un [objet `user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object) et crée un profil alias uniquement lorsque `update_existing_only` est défini sur `false`. Définissez l'adresse e-mail de l'utilisateur comme alias d'utilisateur pour pouvoir le référencer ultérieurement (car l'utilisateur ne disposera pas d'un `external_id`).

![Diagramme illustrant le processus de mise à jour d'un profil utilisateur alias uniquement. Un utilisateur soumet son adresse e-mail et un attribut personnalisé, son code postal, sur une page de destination marketing. Une flèche allant de la collecte sur la page de destination vers un profil utilisateur alias uniquement montre une requête API Braze vers l'endpoint Track user, dont le corps contient le nom d'alias, le libellé d'alias, l'adresse e-mail et le code postal de l'utilisateur. Le profil porte la mention « Utilisateur alias uniquement créé dans Braze » avec les attributs du corps de la requête pour montrer les données reflétées sur le profil nouvellement créé.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Capturer les e-mails des utilisateurs via un formulaire de capture d'e-mail {#capturing-user-emails-through-an-email-capture-form}

Utilisez un formulaire de capture d'e-mail pour inviter les utilisateurs à soumettre leur adresse e-mail, qui sera ajoutée à leur profil utilisateur. Pour plus d'informations sur la configuration de ce formulaire, consultez [Formulaire de capture d'e-mail]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form).

Si vous utilisez un formulaire personnalisé et définissez l'appartenance à un groupe d'abonnement via la REST API, vérifiez si un profil existe déjà avant de créer un utilisateur. Consultez [Étape 1 : Vérifier si l'utilisateur existe](#step-1-check-if-user-exists).

## Identification des utilisateurs uniquement identifiés par alias {#identifying-alias-only-users}

Lors de l'identification des utilisateurs à la création d'un compte, les utilisateurs uniquement identifiés par alias peuvent être identifiés et se voir attribuer un ID externe via l'[endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) en fusionnant l'utilisateur uniquement identifié par alias avec le profil connu.

Pour vérifier si un utilisateur est uniquement identifié par alias, [vérifiez si l'utilisateur existe](#step-1-check-if-user-exists) dans votre base de données.
- Si un enregistrement externe existe, vous pouvez appeler l'endpoint `/users/identify/`.
- Si l'[endpoint `/users/export/id`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) renvoie un `external_id`, vous pouvez appeler l'endpoint `/users/identify/`.
- Si l'endpoint ne renvoie rien, l'appel à `/users/identify/` ne doit pas être effectué.

## Capturer les données utilisateur lorsque des informations d'utilisateur alias uniquement sont déjà présentes {#capturing-user-data-when-alias-only-user-information-is-already-present}

Lorsqu'un utilisateur crée un compte ou s'identifie via une inscription par e-mail, vous pouvez fusionner les profils. Pour obtenir la liste des champs pouvant être fusionnés, consultez [Comportement de la mise à jour de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

### Fusionner les profils utilisateur en double {#merging-duplicate-user-profiles}

Au fur et à mesure que vos données utilisateur augmentent, vous pouvez fusionner les profils utilisateur en double depuis le tableau de bord de Braze. Ces profils en double doivent être trouvés à l'aide de la même requête de recherche. Pour plus d'informations sur la manière de dupliquer les profils utilisateur, consultez [Fusionner les utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

Vous pouvez également utiliser l'[endpoint Fusionner les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) pour fusionner un profil utilisateur avec un autre.

{% alert note %}
Une fois les profils utilisateur fusionnés, cette action ne peut pas être annulée.
{% endalert %}

## Ressources supplémentaires {#additional-resources}
- Consultez notre article sur le [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) de Braze pour obtenir plus de contexte.<br>
- Consultez notre documentation sur la configuration des ID utilisateur et l'appel de la méthode `changeUser()` pour [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift#naming-best-practices) et [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).