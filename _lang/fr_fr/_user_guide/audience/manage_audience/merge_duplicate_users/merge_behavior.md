---
nav_title: Comportement de fusion
article_title: Comportement de fusion des utilisateurs
page_order: 1
page_type: reference
description: "Découvrez comment Braze gère la fusion des utilisateurs pour les utilisateurs marqués pour suppression, les utilisateurs test et les utilisateurs du Groupe de contrôle global."
---

# Comportement de fusion des utilisateurs {#user-merge-behavior}

> Découvrez comment Braze gère la fusion des utilisateurs, y compris les trois types d'utilisateurs pour lesquels le comportement par défaut ne s'applique pas : les utilisateurs marqués pour suppression, les utilisateurs test et les utilisateurs du Groupe de contrôle global.

Ce comportement s'applique à toutes les fusions, que vous utilisiez la [fusion individuelle]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#individual-merging), la [fusion en masse]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#bulk-merging) ou l'[endpoint de l'API Merge users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

## Comportement général de fusion {#general-merge-behavior}

Lorsque vous fusionnez deux profils utilisateur, Braze remplit les champs vides du profil à conserver avec les valeurs du profil à fusionner. Si un champ possède une valeur sur les deux profils, Braze conserve la valeur du profil à conserver.

Par exemple, si une valeur n'existe que sur l'un ou l'autre des profils, Braze la conserve :

| Champ | Profil à fusionner | Profil à conserver | Profil résultant |
|---|---|---|---|
| `first_name` | Alex | (vide) | Alex |
| `last_name` | (vide) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Si les deux profils ont une valeur pour le même champ, Braze conserve la valeur du profil à conserver :

| Champ | Profil à fusionner | Profil à conserver | Profil résultant |
|---|---|---|---|
| `first_name` | Alex | Al | Al |
| `last_name` | (vide) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Ce comportement fonctionne bien pour les attributs par défaut et les attributs personnalisés. Cependant, Braze gère les types d'utilisateurs suivants différemment.

## Résumé des comportements {#behavior-summary}

| Type d'utilisateur | Comportement | Raison |
|---|---|---|
| Utilisateurs marqués pour suppression | Pas de fusion | Les profils marqués pour suppression sont supprimés sous 7 jours, leurs données n'ont donc pas besoin d'être conservées. |
| Utilisateurs test | Fusion, avec conservation du statut d'utilisateur test | Le maintien du statut d'utilisateur test vous aide à conserver une population de test exploitable après une fusion. |
| Utilisateurs du Groupe de contrôle global | Pas de fusion | La fusion modifierait les numéros de compartiment aléatoire, ce qui affecterait les expériences et les rapports. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Utilisateurs marqués pour suppression {#users-marked-for-deletion}

Lorsque vous utilisez l'[outil de suppression en masse des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/) pour supprimer un segment, Braze marque ces profils utilisateur pour suppression dans les 7 jours suivants. Braze ne fusionne pas les profils marqués pour suppression, qu'il s'agisse du profil à conserver ou du profil à fusionner.

Si vous devez fusionner un profil marqué pour suppression, commencez par [annuler la suppression du segment]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/#cancel) ou retirez l'utilisateur de la suppression afin que le profil ne soit plus marqué.

## Utilisateurs test {#test-users}

Braze permet la fusion des profils d'utilisateurs test et conserve le statut d'utilisateur test sur le profil résultant. Cela diffère du [comportement général de fusion](#general-merge-behavior), qui conserverait autrement la valeur du profil à conserver.

Le tableau suivant montre le statut d'utilisateur test résultant pour chaque combinaison :

| Profil à fusionner | Profil à conserver | Profil résultant |
|---|---|---|
| Pas un utilisateur test | Pas un utilisateur test | Pas un utilisateur test |
| Utilisateur test | Utilisateur test | Utilisateur test |
| Utilisateur test | Pas un utilisateur test | Utilisateur test |
| Pas un utilisateur test | Utilisateur test | Utilisateur test |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour en savoir plus sur les utilisateurs test, consultez [Groupes internes]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/).

## Utilisateurs du Groupe de contrôle global {#global-control-group-users}

Braze ne fusionne pas les profils utilisateur appartenant à un [Groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group/), qu'il s'agisse du profil à conserver ou du profil à fusionner.

L'appartenance au Groupe de contrôle global est déterminée par le [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) d'un utilisateur. La fusion modifierait les utilisateurs appartenant au groupe, ce qui affecterait vos expériences et vos rapports.

## Articles connexes {#related-articles}

- [Fusionner les utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/)
- [POST : Fusionner des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [Supprimer des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)
- [Groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group/)
- [Numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)
- [Groupes internes]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/)