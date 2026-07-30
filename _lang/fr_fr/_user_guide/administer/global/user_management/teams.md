---
nav_title: Teams
article_title: Teams
page_order: 2
page_type: reference
alias: /teams/
description: "Cet article de référence traite de l'utilisation des Teams Braze dans le tableau de bord. Vous y apprendrez à créer des Teams, à attribuer des rôles, ainsi que des étiquettes et des filtres."

---

# Teams {#teams}

> En tant qu'administrateur Braze, vous pouvez regrouper les utilisateurs de votre entreprise au sein de Teams avec différents rôles et autorisations. Cela permet à plusieurs groupes d'utilisateurs, sans lien entre eux, de collaborer au sein d'un même espace de travail tout en séparant les types de contenu pouvant être modifiés.

Les Teams peuvent être constituées en fonction de la localisation des clients, de la langue et d'attributs personnalisés, de sorte que les membres et les non-membres d'une équipe aient un accès différent aux fonctionnalités d'envoi de messages et aux données clients. Des filtres et des étiquettes d'équipe peuvent être attribués à différents outils d'engagement. Il n'y a aucune limite au nombre d'équipes que vous pouvez créer dans votre espace de travail.

L'option Teams n'est pas disponible sur tous les contrats Braze. Pour accéder à cette fonctionnalité, contactez votre gestionnaire de compte Braze ou [contactez-nous](mailto:success@braze.com) pour une consultation.

## En quoi les Teams diffèrent-elles des ensembles d'autorisations et des rôles ? {#how-do-teams-differ-from-permission-sets-and-roles}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Créer des Teams {#creating-teams}

Allez dans **Paramètres** > **Équipes internes** et sélectionnez <i class="fas fa-plus"></i> **Ajouter une équipe**.

![Fenêtre permettant d'ajouter une nouvelle équipe.]({% image_buster /assets/img_archive/adding_a_team.png %})

Saisissez le **nom de l'équipe**. Si vous le souhaitez, utilisez le champ **Définir l'équipe (facultatif)** pour sélectionner un attribut personnalisé, un emplacement ou une langue afin de préciser davantage les données utilisateur auxquelles l'équipe a accès. Par exemple, un cas d'usage possible consiste à effectuer des [tests avec les Teams](#test-with-teams) en créant une équipe de développement qui n'a accès qu'aux utilisateurs test, identifiés par un attribut personnalisé. Un autre cas d'usage consiste à restreindre la communication avec les utilisateurs en fonction du produit.

Si une équipe est définie par un attribut personnalisé, une langue ou un pays, vous pouvez alors utiliser l'équipe pour filtrer les utilisateurs finaux pour des fonctionnalités telles que les Campaigns, les Canvas, les Content Cards, les Segments, et plus encore. Pour en savoir plus, consultez [Attribuer des étiquettes d'équipe](#tags-and-filters).

## Assigner des utilisateurs à des Teams {#assign-users-to-teams}

Les administrateurs Braze et les utilisateurs à accès limité disposant de l'autorisation au niveau de l'entreprise « Can Manage Company Settings » peuvent attribuer des autorisations au niveau de l'équipe à un utilisateur de l'entreprise disposant d'un accès limité. Lorsqu'ils sont assignés à une équipe, les utilisateurs de l'entreprise sont limités à la lecture ou à l'écriture des données disponibles pour leurs Teams spécifiques, telles que la langue de l'utilisateur, l'emplacement ou l'attribut personnalisé, tels que définis lors de la création de l'équipe.

### Limiter les autorisations d'un utilisateur de l'entreprise sans supprimer l'utilisateur {#limit-company-user-permissions-without-deleting-a-user}

Pour empêcher un utilisateur de l'entreprise de se connecter tout en préservant son compte, [suspendez l'utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#suspending-company-users). La suspension place le compte dans un état inactif où l'utilisateur ne peut pas se connecter.

Si l'utilisateur doit pouvoir continuer à se connecter avec des capacités limitées, accédez à **Paramètres** > **Utilisateurs de l'entreprise**, sélectionnez l'utilisateur et modifiez ses autorisations. Supprimez les autorisations au niveau de l'espace de travail pour les Campaigns, les Canvas, les Segments et les données utilisateur, et ne conservez qu'un accès minimal, par exemple « View Media Library Assets ». Pour en savoir plus, consultez [Modifier les autorisations d'un utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).

Les autorisations d'équipe fonctionnent en complément des autorisations de l'espace de travail. Si vous assignez l'utilisateur à une équipe, n'accordez que les autorisations minimales au niveau de l'équipe dont il a besoin, et n'accordez pas d'autorisations pour les Campaigns, les Canvas, les Segments ou les profils utilisateur. L'utilisateur reste dans l'espace de travail et peut se connecter, mais il ne peut pas effectuer la plupart des actions de communication ou d'audience.

Pour assigner un utilisateur à une équipe, accédez à **Paramètres** > **Utilisateurs de l'entreprise** et sélectionnez l'utilisateur que vous souhaitez ajouter à votre équipe.

Effectuez ensuite les étapes suivantes :

1. Dans la section **Autorisations au niveau de l'espace de travail**, ajoutez l'utilisateur à l'espace de travail approprié s'il n'y est pas déjà inclus.

![Autorisations au niveau de l'espace de travail avec l'ensemble d'autorisations Banner Template.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Sélectionnez **+ Add team-level permissions**, puis sélectionnez l'équipe (**Team**) à laquelle vous souhaitez ajouter cet utilisateur.
3. Attribuez des autorisations spécifiques depuis la section des autorisations **Team**.

![Autorisations de modèle de page de destination au niveau de l'équipe.]({% image_buster /assets/img/teams.png %})

### Autorisations disponibles au niveau de l'équipe {#available-team-level-permissions}

Voici toutes les autorisations disponibles que vous pouvez attribuer au niveau de l'équipe. Les autorisations non répertoriées ici ne sont accordées qu'au niveau de l'espace de travail, et ces autorisations apparaîtront sous la forme « -- » dans la colonne des autorisations **Teams**.

- View Campaigns
- Edit Campaigns
- Archive Campaigns
- Launch Campaigns
- Approve Campaigns
- View Canvases
- Edit Canvases
- Archive Canvases
- Launch Canvases
- Approve Canvases
- View Content Blocks
- Edit Content Blocks
- Archive Content Blocks
- Launch Content Blocks
- View Segments
- Edit Segments
- Archive Segments
- View IAM Templates
- Edit IAM Templates
- Archive IAM Templates
- View Email Templates
- Edit Email Templates
- Archive Email Templates
- View Webhook Templates
- Edit Webhook Templates
- Archive Webhook Templates
- View Email Link Templates
- Edit Email Link Templates
- View Media Library Assets
- Edit Media Library Assets
- Delete Media Library Assets
- Export User Data
- View User Profiles (PII Redacted)
- View PII
- Edit Dashboard Users
- Edit Canvas Templates
- View Canvas Templates
- Archive Canvas Templates
- View Dashboard Reports
- Edit Dashboard Reports
- Delete Dashboard Reports

Pour consulter les descriptions de ce que chaque autorisation utilisateur inclut et comment les utiliser, consultez notre section [Autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Attribuer des étiquettes d'équipe {#tags-and-filters}

Vous pouvez attribuer une équipe aux Canvas, Campaigns, Content Cards, Segments, modèles d'e-mail, modèles de webhook, Content Blocks et ressources de la bibliothèque multimédia à l'aide du filtre **Ajouter une équipe**.

Pour les Canvas, les filtres d'équipe ne valident les utilisateurs qu'à l'entrée du Canvas. Une fois qu'un utilisateur entre dans un Canvas, il continue de recevoir les messages de toutes les étapes du Canvas, même si ses attributs changent et qu'il ne correspond plus aux critères du filtre d'équipe. Les filtres d'équipe ne fonctionnent pas comme des validations de réception qui réévaluent les utilisateurs à chaque étape de message.

![Ajout d'une étiquette d'équipe à une campagne.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- En fonction des définitions appliquées lors de la création de l'équipe, lorsqu'un filtre d'équipe est attribué, l'audience de cet outil d'engagement est restreinte aux profils utilisateur correspondant à la définition.
- En fonction des autorisations attribuées, les membres de l'équipe ne peuvent accéder qu'aux outils d'engagement du tableau de bord auxquels leur filtre d'équipe est appliqué. S'ils disposent d'autorisations limitées ou inexistantes au niveau de l'espace de travail, ils doivent ajouter un filtre d'équipe à certains objets avant de pouvoir les enregistrer ou les lancer. Les membres de l'équipe peuvent également filtrer les Canvas, Campaigns, Content Cards et Segments par équipe pour identifier le contenu qui les concerne.
- Les utilisateurs disposant uniquement d'autorisations au niveau de l'équipe ne voient pas les filtres **Créé par** ou **Dernière modification par** sur les pages de Segments, Campaigns ou Canvas. Braze masque ces filtres afin que les utilisateurs limités à une équipe ne puissent pas parcourir l'ensemble des utilisateurs Braze depuis ces menus déroulants.

### Cas d'usage {#use-cases}

Considérez les deux scénarios suivants pour une marketeure utilisant Braze nommée Michelle. Michelle est membre d'une équipe appelée « Development ». Elle a accès à toutes les autorisations au niveau de l'équipe pour l'équipe Development.

{% tabs %}
{% tab Scénario 1 - Autorisations d'équipe uniquement %}

Dans ce scénario, Michelle est une utilisatrice limitée qui ne dispose d'aucune autorisation au niveau de l'espace de travail. Ses autorisations ressemblent à ceci :

![Autorisations personnalisées sans autorisation au niveau de l'espace de travail et 16 autorisations basées sur l'équipe.]({% image_buster /assets/img_archive/scenario1.png %})

En fonction des autorisations attribuées à Michelle, chaque fois qu'elle crée une campagne, elle ne peut attribuer que l'équipe « Development » à cette campagne. Elle ne peut pas lancer la campagne tant que l'équipe n'est pas attribuée, et elle ne peut pas voir ni accéder aux autres étiquettes d'équipe.

![Menu déroulant des étiquettes d'équipe de la campagne qui n'affiche que l'étiquette d'équipe « Development ».]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scénario 2 - Autorisations d'équipe et d'espace de travail %}

Dans ce scénario, Michelle est toujours membre de l'équipe Development, mais elle dispose également d'une autorisation supplémentaire au niveau de l'espace de travail.

![Autorisations personnalisées avec une autorisation au niveau de l'espace de travail et 15 autorisations basées sur l'équipe.]({% image_buster /assets/img_archive/scenario2.png %})

Comme Michelle dispose de l'autorisation au niveau de l'espace de travail « Accéder aux Campaigns, Canvas, cartes, Content Blocks, indicateurs de fonctionnalité, Segments, bibliothèque multimédia et centres de préférences », elle peut voir et attribuer d'autres filtres d'équipe à la campagne qu'elle crée.

![Menu déroulant des étiquettes d'équipe de la campagne avec plusieurs étiquettes d'équipe.]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Comme dans le premier scénario, Michelle doit ajouter l'étiquette d'équipe Development à la campagne avant de pouvoir la lancer.

{% endtab %}
{% endtabs %}

## Tester avec Teams {#test-with-teams}

Un cas d'usage possible pour Teams est de créer un système d'approbation basé sur Teams pour tester et lancer du contenu dans un environnement de production.

Pour ce faire, créez une équipe « Développement » qui n'a accès qu'aux utilisateurs test. Vous pouvez limiter une équipe à l'accès aux seuls utilisateurs test si vos utilisateurs test sont identifiables par un attribut personnalisé. Ensuite, ajoutez l'attribut personnalisé comme définition lors de la création ou de la modification de l'équipe (voir la section précédente [Créer des Teams](#creating-Teams)). Vos approbateurs doivent avoir accès à tous les utilisateurs.

Le processus général serait le suivant :

1. L'équipe de développement crée une Campaign et ajoute le tag d'équipe « Développement ».
2. L'équipe de développement lance la Campaign auprès des utilisateurs test.
3. L'équipe d'approbation valide la conception locale de la Campaign, la promeut et la lance. Pour la lancer, l'équipe d'approbation remplace le tag d'équipe « Développement » par « [All Teams] » et relance la Campaign.

Pour les modifications apportées aux Campaigns actives :

1. L'équipe de développement clone la Campaign en cours, ajoute le tag d'équipe « Développement » et enregistre.
2. L'équipe de développement effectue les modifications et les partage avec l'équipe d'approbation.
3. L'équipe d'approbation supprime le tag d'équipe « Développement », met en pause la Campaign précédente et lance la nouvelle Campaign.

## Archiver une équipe existante {#archive-an-existing-team}

Vous pouvez archiver des équipes depuis la page **Internal Teams**.

Sélectionnez une ou plusieurs équipes à archiver. Si l'équipe n'est associée à aucun objet dans Braze, elle est archivée immédiatement. Si l'équipe est associée à un objet, une option vous est proposée pour retirer l'équipe après le processus d'archivage ou la remplacer.

![Archivage d'une équipe associée à un objet dans Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Les administrateurs Braze peuvent désarchiver une équipe en sélectionnant l'équipe archivée, puis en sélectionnant **Unarchive**.