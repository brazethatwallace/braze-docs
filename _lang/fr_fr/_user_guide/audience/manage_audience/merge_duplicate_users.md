---
nav_title: Fusionner les utilisateurs en double
article_title: Fusionner les utilisateurs en double
description: "Découvrez comment trouver et fusionner les utilisateurs en double dans votre tableau de bord de Braze."
page_order: 4
---

# Fusionner les utilisateurs en double {#merge-duplicate-users}

> Découvrez comment trouver et fusionner les utilisateurs en double afin de maximiser l'efficacité de vos Campaigns et Canvas.

{% alert tip %}
Pour fusionner les utilisateurs en double à l'aide de la REST API de Braze, consultez [POST : Fusionner les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## Fusion individuelle {#individual-merging}

Si une recherche d'utilisateurs renvoie des profils en double, vous pouvez fusionner chaque profil individuellement depuis le profil de l'utilisateur dans le tableau de bord de Braze.

### Étape 1 : Rechercher un profil en double {#step-1-search-for-a-duplicate-profile}

Dans Braze, sélectionnez **Audience** > **Recherche d'utilisateurs**.

![La tuile « Recherche d'utilisateurs » mise en évidence dans le menu de navigation.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Saisissez un identifiant unique, tel qu'une adresse e-mail ou un numéro de téléphone, pour le profil en double, puis sélectionnez **Rechercher**.

![La page « Recherche d'utilisateurs » dans le tableau de bord de Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Étape 2 : Fusionner les doublons {#step-2-merge-duplicates}

Pour lancer le processus de fusion, sélectionnez **Merge duplicates**.

![L'un des profils utilisateur en double.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Choisissez le profil utilisateur à conserver et celui à fusionner, puis sélectionnez **Merge profiles**. Répétez ce processus jusqu'à ce que tous les profils en double aient été fusionnés.

![La page de fusion individuelle pour un profil en double.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
Les profils utilisateur en double ne peuvent pas être récupérés après la fusion.
{% endalert %}

## Fusion en masse {#bulk-merging}

Lorsque vous fusionnez des utilisateurs en double en masse, Braze recherche les profils ayant des identifiants correspondants (tels qu'une adresse e-mail) et fusionne toutes leurs données dans le profil le plus récemment mis à jour possédant un `external_id`. S'il n'existe aucun profil avec un `external_id`, le profil le plus récemment mis à jour sans `external_id` sera utilisé à la place.

### Étape 1 : Accéder à Gérer l'audience {#step-1-go-to-manage-audience}

Dans le tableau de bord de Braze, sélectionnez **Audience** > **Manage Audience**.

![La tuile « Manage Audience » mise en évidence dans le menu de navigation.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Étape 2 : Prévisualiser les résultats (facultatif) {#step-2-preview-the-results-optional}

Pour prévisualiser vos résultats avant de fusionner vos doublons, sélectionnez **Generate list of duplicates**.

![La page « Manage Audience » avec « Generate list of duplicates » mis en évidence.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze génère votre prévisualisation et l'envoie à votre adresse e-mail sous forme de fichier CSV.

![Un e-mail de Braze contenant un lien vers le fichier CSV généré.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

Dans l'exemple suivant, Braze utilise l'ID externe de l'utilisateur pour signaler les profils en double et identifier celui à conserver. Si ces profils sont fusionnés en masse, Braze utilisera le profil possédant un ID externe comme nouveau profil principal de l'utilisateur.

{% tabs local %}
{% tab example csv file %}
| Adresse e-mail   | ID externe  | Numéro de téléphone | ID Braze              | Identifiant pour la règle | Profil à conserver | Profil à fusionner |
| ---------------- | ----------- | ------------------- | --------------------- | ------------------------- | ------------------ | ------------------ |
| alex@company.com | A8i3mkd99   | (555) 123-4567      | 65fcaa547f470494d1370 | email                     | TRUE               | FALSE              |
| alex@company.com |             | (555) 987-6543      | 65fcaa547f47d004d1348 | email                     | FALSE              | TRUE               |
| alex@company.com |             | (555) 321-0987      | 65fcaa547f47d0049135c | email                     | FALSE              | TRUE               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### Comportement de la fusion {#merge-behavior}

Braze remplira les champs vides du profil conservé avec les valeurs du profil fusionné. Pour consulter la liste des champs qui seront remplis, reportez-vous à [Comportement de la fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Étape 3 : Fusionner vos doublons {#step-3-merge-your-duplicates}

Si les résultats de votre prévisualisation vous conviennent, sélectionnez **Merge all duplicates**.

{% alert warning %}
Les profils utilisateur en double ne peuvent pas être récupérés après la fusion.
{% endalert %}

![La page « Manage Audience » avec « Merge all duplicates » mis en évidence.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

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