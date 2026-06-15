---
nav_title: Équipes
article_title: Équipes
page_order: 2
page_type: reference
alias: /teams/
description: "Cet article de référence traite de l'utilisation des Teams Braze dans le tableau de bord. Vous y apprendrez à créer des Teams, à attribuer des rôles, ainsi que des étiquettes et des filtres."

---

# Équipes {#teams}

> En tant qu'administrateur Braze, vous pouvez regrouper les utilisateurs de votre entreprise au sein de Teams avec différents rôles et autorisations. Cela permet à plusieurs groupes d'utilisateurs, sans lien entre eux, de collaborer au sein d'un même espace de travail tout en séparant les types de contenu pouvant être modifiés.

Les Teams peuvent être constituées en fonction de la localisation des clients, de la langue et d'attributs personnalisés, de sorte que les membres et les non-membres d'une équipe aient un accès différent aux fonctionnalités d'envoi de messages et aux données clients. Des filtres et des étiquettes d'équipe peuvent être attribués à différents outils d'engagement. Il n'y a aucune limite au nombre d'équipes que vous pouvez créer dans votre espace de travail.

L'option Teams n'est pas disponible sur tous les contrats Braze. Pour accéder à cette fonctionnalité, contactez votre gestionnaire de compte Braze ou [contactez-nous](mailto:success@braze.com) pour une consultation.

## En quoi les Teams diffèrent-elles des jeux d'autorisations et des rôles ? {#how-do-teams-differ-from-permission-sets-and-roles}

{% multi_lang_include permissions.md content="Differences" %}

## Créer des Teams {#creating-teams}

Allez dans **Paramètres** > **Équipes internes** et sélectionnez <i class="fas fa-plus"></i> **Ajouter une équipe**.

![Fenêtre permettant d'ajouter une nouvelle équipe.]({% image_buster /assets/img_archive/adding_a_team.png %})

Saisissez le **nom de l'équipe**. Si vous le souhaitez, utilisez le champ **Définir l'équipe (facultatif)** pour sélectionner un attribut personnalisé, un emplacement ou une langue afin de préciser davantage les données utilisateur auxquelles l'équipe a accès. Par exemple, un cas d'utilisation possible consiste à effectuer des [tests avec les Teams](#test-with-teams) en créant une équipe de développement qui n'a accès qu'aux utilisateurs test, identifiés par un attribut personnalisé. Un autre cas d'utilisation consiste à restreindre la communication avec les utilisateurs en fonction du produit.

Si une équipe est définie par un attribut personnalisé, une langue ou un pays, vous pouvez alors utiliser l'équipe pour filtrer les utilisateurs finaux pour des fonctionnalités telles que les Campaigns, les Canvas, les Content Cards, les Segments, et plus encore. Pour en savoir plus, consultez [Attribuer des étiquettes d'équipe](#tags-and-filters).

## Affecter des utilisateurs à des Teams {#assign-users-to-teams}

Les administrateurs Braze et les utilisateurs limités disposant de l'autorisation au niveau de l'entreprise « Peut gérer les paramètres de l'entreprise » peuvent attribuer des autorisations au niveau de l'équipe à un utilisateur de l'entreprise ayant un accès limité. Lorsqu'un utilisateur est affecté à une équipe, il est limité à la lecture ou à l'écriture des données disponibles pour ses équipes spécifiques, telles que la langue de l'utilisateur, l'emplacement ou l'attribut personnalisé, tels que définis lors de la création de l'équipe.

### Limiter les autorisations d'un utilisateur sans supprimer son compte {#limit-company-user-permissions-without-deleting-a-user}

Pour empêcher un utilisateur de se connecter tout en conservant son compte, [suspendez l'utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#suspending-company-users). La suspension place le compte dans un état inactif où l'utilisateur ne peut pas se connecter.

Si l'utilisateur doit pouvoir continuer à se connecter avec des capacités limitées, accédez à **Paramètres** > **Utilisateurs de l'entreprise**, sélectionnez l'utilisateur et modifiez ses autorisations. Supprimez les autorisations au niveau de l'espace de travail pour les Campaigns, les Canvas, les Segments et les données utilisateur, et ne laissez qu'un accès minimal, par exemple « Voir les ressources de la bibliothèque multimédia ». Pour plus d'informations, consultez [Modifier les autorisations d'un utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#edit-a-users-permissions).

Les autorisations d'équipe s'ajoutent aux autorisations de l'espace de travail. Si vous affectez l'utilisateur à une équipe, n'accordez que les autorisations minimales au niveau de l'équipe dont il a besoin, et n'accordez pas d'autorisations pour les Campaigns, les Canvas, les Segments ou les profils utilisateur. L'utilisateur reste dans l'espace de travail et peut se connecter, mais il ne peut pas effectuer la plupart des actions d'envoi de messages ou de ciblage d'audience.

Pour affecter un utilisateur à une équipe, accédez à **Paramètres** > **Utilisateurs de l'entreprise** et sélectionnez l'utilisateur que vous souhaitez ajouter à votre équipe.

Effectuez ensuite les étapes suivantes :

1. Dans la section **Autorisations au niveau de l'espace de travail**, ajoutez l'utilisateur à l'espace de travail approprié s'il n'y est pas déjà inclus.

![Autorisations au niveau de l'espace de travail avec le jeu d'autorisations Modèle de bannière.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Sélectionnez **+ Ajouter des autorisations au niveau de l'équipe**, puis sélectionnez l'**équipe** à laquelle vous souhaitez ajouter cet utilisateur.
3. Attribuez des autorisations spécifiques depuis la section des autorisations de l'**équipe**.

![Autorisations de modèle de page d'accueil au niveau de l'équipe.]({% image_buster /assets/img/teams.png %})

### Autorisations disponibles au niveau de l'équipe {#available-team-level-permissions}

Voici toutes les autorisations disponibles que vous pouvez attribuer au niveau de l'équipe. Toute autorisation non répertoriée ici n'est accordée qu'au niveau de l'espace de travail, et ces autorisations apparaîtront sous la forme « -- » dans la colonne des autorisations **Teams**.

- Voir les Campaigns
- Modifier les Campaigns
- Archiver les Campaigns
- Lancer les Campaigns
- Approuver les Campaigns
- Voir les Canvas
- Modifier les Canvas
- Archiver les Canvas
- Lancer les Canvas
- Approuver les Canvas
- Voir les Content Blocks
- Modifier les Content Blocks
- Archiver les Content Blocks
- Lancer les Content Blocks
- Voir les Segments
- Modifier les Segments
- Archiver les Segments
- Voir les modèles de messages in-app
- Modifier les modèles de messages in-app
- Archiver les modèles de messages in-app
- Voir les modèles d'e-mail
- Modifier les modèles d'e-mail
- Archiver les modèles d'e-mail
- Voir les modèles de webhook
- Modifier les modèles de webhook
- Archiver les modèles de webhook
- Voir les modèles de liens d'e-mail
- Modifier les modèles de liens d'e-mail
- Voir les ressources de la bibliothèque multimédia
- Modifier les ressources de la bibliothèque multimédia
- Supprimer les ressources de la bibliothèque multimédia
- Exporter les données utilisateur
- Voir les profils utilisateur (PII masquées)
- Voir les PII
- Modifier les utilisateurs du tableau de bord
- Modifier les modèles de Canvas
- Voir les modèles de Canvas
- Archiver les modèles de Canvas
- Voir les rapports du tableau de bord
- Modifier les rapports du tableau de bord
- Supprimer les rapports du tableau de bord

Pour consulter les descriptions de ce que chaque autorisation utilisateur inclut et comment les utiliser, consultez notre section [Autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

## Attribuer des étiquettes d'équipe {#tags-and-filters}

Vous pouvez attribuer une équipe aux Canvas, Campaigns, Content Cards, Segments, modèles d'e-mail, modèles de webhook, Content Blocks et ressources de la bibliothèque multimédia à l'aide du filtre **Ajouter une équipe**.

![Ajout d'une étiquette d'équipe à une campagne.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- En fonction des *définitions* appliquées lors de la création de l'équipe, lorsqu'un filtre d'équipe est attribué, l'audience de cet outil d'engagement est restreinte aux profils utilisateur correspondant à la définition.
- En fonction des *autorisations* attribuées, les membres de l'équipe ne pourront accéder qu'aux outils d'engagement du tableau de bord auxquels leur filtre d'équipe est appliqué. S'ils disposent d'autorisations limitées ou inexistantes au niveau de l'espace de travail, ils doivent ajouter un filtre d'équipe à certains objets avant de pouvoir les enregistrer ou les lancer. Les membres de l'équipe peuvent également filtrer les Canvas, Campaigns, Content Cards et Segments par équipe pour identifier le contenu qui les concerne.

### Cas d'utilisation {#use-cases}

Considérez les deux scénarios suivants pour une marketeur utilisant Braze nommée Michelle. Michelle est membre d'une équipe appelée « Development ». Elle a accès à toutes les autorisations au niveau de l'équipe pour l'équipe Development.

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

## Tester avec les Teams {#test-with-teams}

Un cas d'utilisation possible des Teams consiste à créer un système d'approbation basé sur les équipes pour tester et lancer du contenu dans un environnement de production.

Pour ce faire, créez une équipe « Development » qui n'a accès qu'aux utilisateurs test. Vous pouvez limiter une équipe aux seuls utilisateurs test si vos utilisateurs test sont identifiables par un attribut personnalisé. Ajoutez ensuite l'attribut personnalisé comme définition lors de la création ou de la modification de l'équipe (voir la section précédente [Créer des Teams](#creating-Teams)). Vos approbateurs doivent avoir accès à tous les utilisateurs.

Le processus général serait le suivant :

1. L'équipe Development crée une campagne et ajoute l'étiquette d'équipe « Development ».
2. L'équipe Development lance la campagne auprès des utilisateurs test.
3. L'équipe d'approbation valide la conception locale de la campagne, la promeut et la lance. Pour lancer, l'équipe d'approbation change l'étiquette d'équipe de « Development » à « [All Teams] » et relance la campagne.

Pour les modifications apportées aux campagnes actives :

1. L'équipe Development clone la campagne en cours, ajoute l'étiquette d'équipe « Development » et enregistre.
2. L'équipe Development effectue les modifications et les partage avec l'équipe d'approbation.
3. L'équipe d'approbation supprime l'étiquette d'équipe « Development », met en pause la campagne précédente et lance la nouvelle campagne.

## Archiver une équipe existante {#archive-an-existing-team}

Vous pouvez archiver des équipes depuis la page **Équipes internes**.

Sélectionnez une ou plusieurs équipes à archiver. Si l'équipe n'est associée à aucun objet dans Braze, elle sera archivée immédiatement. Si l'équipe est associée à un objet, vous aurez la possibilité de supprimer l'équipe après le processus d'archivage ou de la remplacer.

![Archivage d'une équipe associée à un objet dans Braze.]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Les administrateurs Braze peuvent désarchiver une équipe en sélectionnant l'équipe archivée puis en sélectionnant **Désarchiver**.