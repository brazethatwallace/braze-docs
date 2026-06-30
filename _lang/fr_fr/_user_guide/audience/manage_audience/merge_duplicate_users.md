---
nav_title: Fusionner les utilisateurs en double
article_title: Fusionner les utilisateurs en double
description: "Découvrez comment trouver et fusionner les utilisateurs en double dans votre tableau de bord de Braze."
page_order: 4
---

# Fusionner les utilisateurs en double {#merge-duplicate-users}

> Découvrez comment trouver et fusionner les utilisateurs en double afin de maximiser l'efficacité de vos Campaigns et Canvas.

## REST API : identifier et fusionner les utilisateurs {#rest-api-identify-and-merge-users}

Les outils de cette page fusionnent les profils en double dans le tableau de bord. Vous pouvez également combiner ou réorienter des profils via les [endpoints User Data]({{site.baseurl}}/api/endpoints/user_data) de Braze :

- [POST : Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) (`/users/identify`) : combine un profil uniquement alias, uniquement e-mail ou uniquement numéro de téléphone avec un profil possédant un `external_id`.
- [POST : Fusionner les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) (`/users/merge`) : fusionne un profil utilisateur dans un autre, y compris lorsque les deux profils possèdent déjà un `external_id`. Consultez les [Conditions préalables]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#prerequisites) et le [Comportement de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) avant d'appeler cet endpoint.

Lorsqu'un profil anonyme est associé à un profil identifié existant (par exemple via un appel SDK `changeUser()` ou `/users/identify`), Braze rend orphelin le profil anonyme et ne copie que certains champs sur le profil identifié. Pour en savoir plus, consultez [Que se passe-t-il lorsque vous identifiez des utilisateurs anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).

Les fusions d'utilisateurs sont difficiles à annuler. Si vous prévoyez une fusion complexe impliquant plusieurs valeurs `external_id` ou des migrations de profils à grande échelle, contactez votre gestionnaire de la satisfaction client Braze pour obtenir des conseils avant de vous appuyer sur `/users/merge`.

Braze traite différemment trois types d'utilisateurs lors de la fusion : les utilisateurs marqués pour suppression, les utilisateurs test et les utilisateurs du Groupe de contrôle global. Pour plus de détails, consultez [Comportement de fusion des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior).

## Fusion individuelle {#individual-merging}

Si une recherche d'utilisateurs renvoie des profils en double, vous pouvez fusionner chaque profil individuellement depuis le profil de l'utilisateur dans le tableau de bord de Braze.

### Étape 1 : Rechercher un profil en double {#step-1-search-for-a-duplicate-profile}

Dans Braze, sélectionnez **Audience** > **User Search**.

![La tuile « User Search » mise en évidence dans le menu de navigation.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Saisissez un identifiant unique, tel qu'une adresse e-mail ou un numéro de téléphone, pour le profil en double, puis sélectionnez **Search**.

![La page « User Search » dans le tableau de bord de Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Étape 2 : Fusionner les doublons {#step-2-merge-duplicates}

Pour lancer le processus de fusion, sélectionnez **Merge duplicates**.

![L'un des profils utilisateur en double.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Choisissez le profil utilisateur à conserver et celui à fusionner, puis sélectionnez **Merge profiles**. Répétez ce processus jusqu'à ce que tous les profils en double aient été fusionnés.


{% alert warning %}
Les profils utilisateur en double ne peuvent pas être récupérés après la fusion.
{% endalert %}

## Fusion en masse {#bulk-merging}

Lorsque vous fusionnez des utilisateurs en double en masse, Braze recherche les profils ayant des identifiants correspondants (tels qu'une adresse e-mail) et conserve un seul profil. Braze donne d'abord la priorité aux profils possédant un `external_id`, puis applique vos paramètres de **résolution des égalités** : **Resolve ties using** et **Prioritization**. S'il n'existe aucun profil avec un `external_id`, Braze utilise **Resolve ties using** et **Prioritization** sur les profils sans `external_id`. Braze ne fusionne les utilisateurs que lorsque ces paramètres identifient un profil à conserver. Par exemple, si **Resolve ties using** est défini sur **Updated date** et que les deux profils ont le même horodatage de dernière mise à jour, Braze ne peut pas résoudre l'égalité, et ces utilisateurs ne sont donc pas fusionnés.

### Étape 1 : Accéder à Gérer l'audience {#step-1-go-to-manage-audience}

Dans le tableau de bord de Braze, sélectionnez **Audience** > **Manage Audience**.

![La tuile « Manage Audience » mise en évidence dans le menu de navigation.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Étape 2 : Prévisualiser les résultats (facultatif) {#step-2-preview-the-results-optional}

Pour prévisualiser vos résultats avant de fusionner vos doublons, sélectionnez **Generate list of duplicates**.

![La page « Manage Audience » avec « Generate list of duplicates » mis en évidence.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze génère votre prévisualisation et l'envoie à votre adresse e-mail sous forme de fichier CSV.


Dans l'exemple suivant, Braze utilise l'ID externe de l'utilisateur pour signaler les profils en double et identifier celui à conserver. Si ces profils sont fusionnés en masse, Braze utilisera le profil possédant un ID externe comme nouveau profil principal de l'utilisateur.

{% tabs local %}
{% tab example csv file %}
| Adresse e-mail   | ID externe  | Numéro de téléphone | ID Braze              | Identifiant pour la règle | Profil à conserver | Profil à fusionner |
| ---------------- | ----------- | ------------------- | --------------------- | ------------------------- | ------------------ | ------------------ |
| alex@company.com | A8i3mkd99   | (555) 123-4567      | 65fcaa547f470494d1370 | email                     | TRUE               | FALSE              |
| alex@company.com |             | (555) 987-6543      | 65fcaa547f47d004d1348 | email                     | FALSE              | TRUE               |
| alex@company.com |             | (555) 321-0987      | 65fcaa547f47d0049135c | email                     | FALSE              | TRUE               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Prévisualiser les résultats (facultatif)" }
{% endtab %}
{% endtabs %}

#### Comportement de fusion {#merge-behavior}

Braze remplira les champs vides du profil conservé avec les valeurs du profil fusionné. Pour consulter la liste des champs qui seront remplis, reportez-vous à [Comportement de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

### Étape 3 : Fusionner vos doublons {#step-3-merge-your-duplicates}

Si les résultats de votre prévisualisation vous conviennent, sélectionnez **Merge all duplicates**.

{% alert warning %}
Les profils utilisateur en double ne peuvent pas être récupérés après la fusion.
{% endalert %}


## Fusion basée sur des règles {#rules-based-merging}

Vous pouvez utiliser des règles pour contrôler la manière dont les profils en double sont résolus lors d'une fusion, afin de conserver le profil utilisateur le plus pertinent. Lorsque des règles sont définies, Braze conserve les profils correspondant à vos critères.

### Étape 1 : Définir vos règles {#step-1-define-your-rules}

1. Accédez à **Audience** > **Manage Audience** > **Edit rules**.
2. Dans la section **Profile to keep** du panneau **Edit rules**, sélectionnez l'**Identifier** des profils qui seront conservés lors de la fusion des doublons. Il peut s'agir de l'adresse e-mail ou du numéro de téléphone.
3. Dans la section **Resolving ties**, sélectionnez les critères permettant de résoudre les égalités entre les profils ayant des critères correspondants dans **Profile to keep**. Vous pouvez sélectionner les options suivantes :<br>
- **Resolve ties using** : Created date, Updated date, Last session
- **Prioritization** : Newest, Oldest

![Le panneau « Edit rules » avec des sections pour sélectionner les options de « Profile to keep » et « Resolving ties ».]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Par exemple, vous pourriez conserver le profil qui possède un numéro de téléphone. Si plusieurs utilisateurs ont le même numéro de téléphone, vous pourriez résoudre les égalités en utilisant le champ **Updated date** et donner la priorité à l'utilisateur le plus récemment mis à jour.

### Étape 2 : Prévisualiser les résultats (facultatif)

Après avoir enregistré vos règles, vous pouvez prévisualiser leur fonctionnement en sélectionnant **Generate a list of duplicates**. Braze génère votre prévisualisation et l'envoie à votre adresse e-mail sous forme de fichier CSV indiquant quels utilisateurs seraient conservés et fusionnés si vos règles étaient appliquées.

### Étape 3 : Fusionner les doublons {#step-3-merge-duplicates}

Si les résultats de votre prévisualisation vous conviennent, retournez à la page **Manage Audience** et sélectionnez **Merge all duplicates**.

{% alert warning %}
Les profils utilisateur en double ne peuvent pas être récupérés après la fusion.
{% endalert %}

## Fusion planifiée {#scheduled-merging}

Similaire à la fusion basée sur des règles, la fusion planifiée vous permet d'automatiser la fusion des profils utilisateur sur une base quotidienne à l'aide de règles préconfigurées.

![La page « Manage Audience » avec le bouton « schedule ».]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Une fois la fonctionnalité activée, Braze attribue automatiquement un créneau horaire pour effectuer le processus de fusion quotidiennement, aux alentours de minuit dans le fuseau horaire de la société de l'utilisateur. Vous pouvez désactiver la fusion planifiée à tout moment. Braze notifie les administrateurs de votre espace de travail 24 heures avant la fusion planifiée, fournissant un rappel et le temps de vérifier la configuration.

{% alert warning %}
Les profils utilisateur en double ne peuvent pas être récupérés après la fusion.
{% endalert %}

## Pourquoi plusieurs profils utilisateur sont-ils associés à la même adresse e-mail ? {#why-are-multiple-user-profiles-associated-with-the-same-email-address}

Braze conserve plusieurs profils utilisateur partageant la même adresse e-mail lorsque les profils sont créés via différents identifiants, importations ou sessions anonymes avant identification. Il s'agit d'un comportement attendu lorsque les utilisateurs ne partagent pas un même `external_id`.

Avant de fusionner les doublons, utilisez l'[endpoint d'exportation de profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) pour confirmer quels profils existent pour une adresse e-mail et quels champs chaque profil contient. Vous pouvez également effectuer une recherche par e-mail dans **Audience** > **User Search** pour examiner les doublons dans le tableau de bord.

## Articles connexes {#related-articles}

- [Comportement de fusion des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior)
- [POST : Fusionner les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)
- [Supprimer des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)