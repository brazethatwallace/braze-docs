---
nav_title: Utilisateurs de l'entreprise
article_title: Gérer les utilisateurs de l'entreprise
page_order: 0
page_type: reference
description: "Cette page explique comment gérer les utilisateurs de votre entreprise, notamment ajouter et supprimer des utilisateurs, définir les autorisations, créer des équipes et gérer les paramètres de l'entreprise."
---

# Gérer les utilisateurs de l'entreprise {#manage-company-users}

> Découvrez comment gérer les utilisateurs dans le compte de votre entreprise, notamment comment ajouter, suspendre et supprimer des utilisateurs.

## Ajouter des utilisateurs de l'entreprise {#adding-company-users}

Vous devez disposer des autorisations d'administrateur pour ajouter des utilisateurs à votre compte Braze.

Pour ajouter un nouvel utilisateur :

1. Accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**.
2. Sélectionnez **+ Ajouter un nouvel utilisateur**.
3. Saisissez les informations demandées, notamment l'adresse e-mail, le département et le [rôle utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#creating-a-role).
4. Pour les utilisateurs qui ne sont pas administrateurs, sélectionnez les [autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#editing-a-users-permissions) au niveau de l'entreprise et au niveau de l'espace de travail que vous souhaitez accorder à cet utilisateur.

![Autorisations au niveau de l'espace de travail avec une section pour les champs d'autorisations personnalisées.]({% image_buster /assets/img/add_new_user_3.png %})

### Exigences relatives aux adresses e-mail {#email-address-requirements}

Chaque adresse e-mail utilisée dans une [instance]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/) doit être unique. Cela signifie que si vous essayez d'ajouter une adresse e-mail déjà associée à un utilisateur qui a eu ou a encore accès à un espace de travail de l'entreprise dans cette instance, un message d'erreur s'affichera.

Si votre équipe utilise Gmail et que vous rencontrez des difficultés pour ajouter une adresse e-mail, vous pouvez créer un alias en ajoutant un signe plus (+) suivi de « 1 » ou « test » à l'adresse e-mail. Par exemple, `contractor@braze.com` peut avoir un alias `contractor+1@braze.com`. Les e-mails envoyés à `contractor+1@braze.com` seront toujours livrés à `contractor@braze.com`, mais l'alias sera reconnu comme une adresse e-mail unique.

Pour utiliser un seul compte sur plusieurs entreprises sans alias, consultez [Utiliser les développeurs multi-entreprises]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account/#use-multi-company-developers). Si vous utilisez l'authentification unique, consultez [Considérations relatives à l'authentification unique (SSO)]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account/#considerations-for-single-sign-on-sso) avant de vous inscrire avec plusieurs adresses e-mail.

### Puis-je modifier l'adresse e-mail de mon compte Braze ? {#can-i-change-my-braze-accounts-email-address}

Pour des raisons de sécurité, les utilisateurs ne peuvent pas modifier l'adresse e-mail associée à leur compte Braze. Si un utilisateur souhaite mettre à jour son adresse e-mail, un administrateur doit [créer un nouveau compte](#adding-company-users) avec l'adresse e-mail souhaitée.

## Attribuer l'accès et les responsabilités des utilisateurs {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions.md content="Differences" %}

## Suspendre des utilisateurs de l'entreprise {#suspending-company-users}

La suspension d'un utilisateur met son compte dans un état inactif : l'utilisateur ne peut plus se connecter, mais les données associées à son compte sont conservées. Seuls les administrateurs peuvent suspendre ou réactiver des utilisateurs de l'entreprise. Notez que les utilisateurs suspendus peuvent toujours recevoir des notifications de Braze.

Pour suspendre un utilisateur, accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, recherchez son nom d'utilisateur et sélectionnez <i class="fa-solid fa-user-lock"></i> **Suspendre**.

![Option pour suspendre un utilisateur.]({% image_buster /assets/img_archive/suspend_user.png %})

Les administrateurs peuvent également suspendre un utilisateur en sélectionnant son nom dans la liste, puis en sélectionnant **Suspendre l'utilisateur** dans le pied de page.

![Suspendre un utilisateur lors de la modification des détails de l'utilisateur.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Supprimer des utilisateurs de l'entreprise {#deleting-company-users}

Pour supprimer un utilisateur, accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, recherchez le nom de l'utilisateur et sélectionnez <i class="fa fa-trash-can"></i> **Supprimer l'utilisateur**.

Seuls les administrateurs peuvent supprimer des utilisateurs de l'entreprise, et les utilisateurs ne peuvent pas supprimer leur propre compte. Un administrateur ne peut pas supprimer son propre compte du tableau de bord ; un autre administrateur doit le faire à sa place.

![Supprimer un utilisateur.]({% image_buster /assets/img_archive/delete_user_new.png %})

Après la suppression d'un utilisateur, Braze ne conserve aucune des données de compte suivantes :

- Les attributs de l'utilisateur
- L'adresse e-mail
- Le numéro de téléphone
- L'ID utilisateur externe
- Le genre
- Le pays
- La langue
- Toute autre donnée similaire

Braze conservera les données de compte suivantes :

- Les attributs personnalisés ou les données de test associés à leur compte
- Les Campaigns ou Canvas qu'ils ont créés (mais le nom de l'utilisateur n'y apparaîtra plus, par exemple dans la colonne **Dernière modification**)

### Impact de la suppression d'un utilisateur du tableau de bord {#impact-of-deleting-a-dashboard-user}

Lorsqu'un utilisateur du tableau de bord est supprimé, il n'y a pas d'impact significatif sur les ressources qu'il a créées dans le tableau de bord, telles que les campagnes, les segments et les Canvas. Cependant, le champ **Créé par** de ces ressources affichera une valeur « null » au lieu de l'adresse e-mail de l'utilisateur supprimé.

Si un nouvel utilisateur du tableau de bord est ensuite créé avec la même adresse e-mail que l'utilisateur supprimé, Braze ne réassociera pas les ressources créées par l'utilisateur supprimé au nouvel utilisateur. Le nouvel utilisateur du tableau de bord repartira de zéro et ne sera pas crédité comme créateur des ressources existantes dans le tableau de bord.

## Résolution des problèmes {#troubleshooting}

### « Impossible d'effectuer l'action » lors de l'ajout d'un utilisateur {#unable-to-perform-action-when-adding-a-user}

Si l'ajout d'un utilisateur du tableau de bord échoue avec une erreur « Unable to perform action » (ou similaire) :

- Supprimez les espaces en début ou en fin de chaîne ainsi que les caractères masqués de l'adresse e-mail.
- Vérifiez que l'adresse est dans un format d'e-mail valide pour votre organisation. Certains caractères spéciaux sont rejetés.
- La même adresse e-mail ne peut pas être utilisée pour deux utilisateurs du tableau de bord dans le même [cluster]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account/). Si l'adresse est déjà enregistrée dans un autre espace de travail de ce cluster, utilisez une adresse distincte ou un alias tel que `user+1@company.com`.

### « L'adresse e-mail est déjà utilisée » lors de l'ajout d'un utilisateur {#email-is-already-taken-when-trying-to-add-a-user}

Si vous essayez d'ajouter un nouvel utilisateur et recevez une erreur indiquant que l'adresse e-mail est déjà utilisée, mais que vous ne le trouvez pas dans votre liste d'utilisateurs, cet utilisateur existe probablement dans une autre instance du même cluster du tableau de bord de Braze.

Pour créer ce nouvel utilisateur, vous pouvez effectuer l'une des actions suivantes :

1. Supprimer l'utilisateur de l'autre instance avant de le créer dans la nouvelle, ou
2. Créer l'utilisateur avec une adresse e-mail différente (comme `testing+01@braze.com`) ou un autre alias d'e-mail.

Si vous ne recevez pas le message d'activation dans votre boîte de réception lorsque vous utilisez `testing+01@braze.com`, vérifiez auprès de votre équipe informatique que vous pouvez recevoir des messages provenant de ce type d'adresse e-mail. Certains administrateurs filtrent les messages envoyés à des adresses e-mail contenant un `+`.

## Étapes suivantes {#next-steps}

Après avoir ajouté des utilisateurs, gérez leur accès :

- [Autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) pour configurer ce que chaque utilisateur peut faire dans le tableau de bord.
- [Équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) pour organiser les utilisateurs en groupes avec un accès partagé à des objets spécifiques du tableau de bord.