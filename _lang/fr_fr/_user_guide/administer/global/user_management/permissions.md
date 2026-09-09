---
nav_title: Autorisations
article_title: "Autorisations Braze"
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Cet article de référence explique le fonctionnement des autorisations utilisateur dans Braze. Vous y apprendrez comment modifier et définir les autorisations utilisateur, en choisissant qui peut y accéder."
tool: Dashboard
---

# Autorisations Braze {#braze-permissions}

> Découvrez comment créer des ensembles d'autorisations, créer des rôles, modifier les autorisations utilisateur et exporter les autorisations utilisateur, afin de vous assurer que vos utilisateurs n'accèdent qu'aux espaces de travail et aux fonctionnalités dont ils ont le plus besoin.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Créer un ensemble d'autorisations {#create-a-permission-set}

Utilisez les ensembles d'autorisations pour regrouper les autorisations liées à des domaines ou des actions spécifiques. Vous pouvez appliquer des ensembles d'autorisations aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un ensemble d'autorisations, allez dans **Paramètres** > **Gestion des utilisateurs** > **Ensembles d'autorisations**, puis sélectionnez **Créer un ensemble d'autorisations**. Pour une description de chaque autorisation, consultez [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab exemples d'ensembles d'autorisations %}
| Nom | Autorisations |
|-----------|----------------|
| Développeurs | « View API Keys », « Edit API Keys », « View Internal Groups », « Edit Internal Groups », « View Message Activity Log », « View Event User Log », « View API identifiers », « View API Usage Dashboard », « View API Limits », « View API Usage Alerts », « Edit API Usage Alerts », « View SDK Debugger », « Edit SDK Debugger ». |
| Marketeurs | « View Campaigns », « Edit Campaigns », « Archive Campaigns », « View Canvases », « Edit Canvases », « Archive Canvases », « View Frequency Capping Rules », « Edit Frequency Capping Rules », « View Message Prioritization », « Edit Message Prioritization », « View Content Blocks », « View Feature Flags », « Edit Feature Flags », « Archive Feature Flags », « View Segments », « Edit Segments », « Edit Global Control Group », « View IAM Templates », « Edit IAM Templates », « Archive IAM Templates », « View Email Templates », « Edit Email Templates », « Archive Email Templates », « View Webhook Templates », « Edit Webhook Templates », « Archive Webhook Templates », « View Email Link Templates », « Edit Email Link Templates », « View Media Library Assets », « View Locations », « Edit Locations », « Archive Locations », « View Promotion Codes », « Edit Promotion Codes », « Export Promotion Codes », « View Preference Centers », « Edit Preference Centers », « Edit Dashboard Reports », « View Banner Templates », « View Localization Settings », « Use Operator », « View Decisioning Studio Agents ». |
| Gestion des utilisateurs | « Edit Dashboard Users », « View Teams », « Edit Teams », « Archive Teams ». |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple d'ensemble d'autorisations" }
{% endtab %}
{% endtabs %}

## Création d'un rôle {#creating-a-role}

Les rôles permettent d'apporter plus de structure en regroupant vos autorisations personnalisées individuelles avec les contrôles d'accès aux espaces de travail. Cela est particulièrement utile si vous avez de nombreuses marques ou des espaces de travail régionaux dans un même tableau de bord. Grâce aux rôles, vous pouvez ajouter des utilisateurs du tableau de bord aux espaces de travail appropriés et leur accorder directement les autorisations associées. Pour créer un rôle, accédez à **Paramètres** > **Gestion des utilisateurs** > **Rôles**, puis sélectionnez **Créer un rôle**. Pour une description de chaque autorisation, consultez [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab exemples de rôles %}
| Nom du rôle    | Espace de travail | Autorisations
----------- | ----------- | ---------
| Marketeur - Marques de mode | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Marketeur - Marques de soins de la peau | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers".|
| Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemples de rôles" }
{% endtab %}
{% endtabs %}

## En quoi les ensembles d'autorisations et les rôles diffèrent-ils des Teams ? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Considérations pour l'ajout d'autorisations utilisateur aux Teams {#considerations-for-adding-user-permissions-to-teams}

Vous pouvez rencontrer des difficultés lorsque vous essayez d'enregistrer des autorisations dans le tableau de bord de Braze, notamment lors de l'ajout ou de la suppression d'utilisateurs d'un espace de travail, ou lors de leur ajout à une Team. Le bouton **Save/Update Users** peut être grisé si les autorisations de l'utilisateur sont identiques à celles qu'il possède déjà au niveau de l'espace de travail. Cette restriction existe car il n'y a aucun avantage à avoir une Team si tous les utilisateurs possèdent les mêmes autorisations que l'ensemble de l'espace de travail.

Pour ajouter un utilisateur à une Team tout en conservant les mêmes autorisations, n'attribuez aucune autorisation au niveau de l'espace de travail. Attribuez plutôt les autorisations exclusivement au niveau de l'équipe.

## Utilisateurs à accès limité {#limited-users}

Les utilisateurs à accès limité disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze, tout en ayant des restrictions par rapport aux administrateurs de l'entreprise et aux administrateurs d'espace de travail.

| Portée | Description |
| --- | --- |
| Autorisations | Les utilisateurs à accès limité peuvent modifier les autorisations d'autres utilisateurs à accès limité s'ils disposent de l'autorisation « Modifier les utilisateurs du tableau de bord ». Ils peuvent également créer de nouveaux utilisateurs à accès limité et modifier leurs ensembles d'autorisations. En revanche, ils ne peuvent pas créer ni gérer de comptes d'administrateur de l'entreprise. |
| Limitations des rôles | Si un utilisateur à accès limité possède toutes les autorisations sauf « Administrateur d'espace de travail », il a tout de même accès à toutes les autres autorisations généralement accordées à un administrateur d'espace de travail. |
| Visibilité des autorisations | Si un utilisateur à accès limité dispose de l'autorisation « Modifier les utilisateurs du tableau de bord » pour un espace de travail (comme Dev) mais pas pour un autre (comme Prod), il ne verra pas les autorisations de l'espace de travail Prod dans sa page de détail des utilisateurs du tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autorisations pour les utilisateurs à accès limité" }

### Comparer les utilisateurs à accès limité {#compare-limited-users}

| Type d'utilisateur à accès limité | Description |
| --- | --- |
| Administrateur d'espace de travail | Les administrateurs d'espace de travail disposent d'autorisations spécifiques à la gestion des espaces de travail, mais n'ont pas la même autorité que les administrateurs de l'entreprise. Les utilisateurs à accès limité peuvent hériter d'autorisations similaires à celles des administrateurs d'espace de travail si les autorisations nécessaires leur sont attribuées. |
| Administrateur (administrateur de l'entreprise) | Les administrateurs de l'entreprise disposent d'autorisations plus étendues, notamment la possibilité de supprimer des utilisateurs du tableau de bord. Cependant, ils ne peuvent pas supprimer leur propre compte et doivent contacter un autre administrateur de l'entreprise pour cette action. |
| Accès en lecture seule | Pour accéder à certaines parties du tableau de bord, comme la page Campaigns, les utilisateurs doivent disposer des autorisations de consultation correspondantes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparaison des utilisateurs à accès limité" }

### Erreur d'accès limité {#limited-access-error}

Les utilisateurs peuvent rencontrer des messages tels que « Vous avez besoin de l'autorisation "Voir les pages de destination" pour accéder à cette page ». Dans ce cas, l'utilisateur et l'administrateur du compte doivent vérifier que les autorisations requises sont bien accordées. Si c'est le cas, essayez de résoudre le problème en désactivant puis en réactivant les autorisations de l'utilisateur.

{% alert note %}
Il n'est pas possible de fusionner ou d'importer les autorisations d'un utilisateur du tableau de bord vers un autre.
{% endalert %}

## Nuances des autorisations utilisateur {#nuances-of-user-permissions}

Gardez à l'esprit les comportements suivants lorsque vous attribuez l'accès au tableau de bord :

- **Administrateur d'espace de travail versus Administrateur d'entreprise :** Les administrateurs d'espace de travail gèrent les autorisations au sein des espaces de travail qui leur sont attribués. Les administrateurs d'entreprise disposent d'une autorité à l'échelle de l'entreprise, y compris la suppression d'autres utilisateurs du tableau de bord.
- **Utilisateurs limités :** Les utilisateurs limités disposant de l'autorisation « Modifier les utilisateurs du tableau de bord » peuvent gérer d'autres utilisateurs limités, mais ne peuvent pas créer ni gérer des comptes d'administrateur d'entreprise.
- **Portée de la gestion des utilisateurs du tableau de bord :** Sur la page de détail de l'utilisateur, les autorisations n'apparaissent que pour les espaces de travail auxquels l'éditeur peut accéder. Un utilisateur limité qui peut modifier des utilisateurs dans un espace de travail peut ne pas voir les cases à cocher d'autorisations d'un autre espace de travail.
- **Bouton Attribuer des autorisations :** Lorsque vous modifiez un utilisateur et que celui-ci dispose déjà d'autorisations au niveau de l'espace de travail ou d'ensembles d'autorisations pour chaque espace de travail que vous pouvez gérer, le bouton **Attribuer des autorisations** disparaît. Cela se produit parce qu'il ne reste plus d'espaces de travail supplémentaires à attribuer au niveau de l'espace de travail.
- **Exporter les données utilisateur :** L'exportation des données utilisateur nécessite un accès au niveau de l'espace de travail en plus de l'autorisation d'exportation.
- **Autorisations composites :** Certaines zones nécessitent plusieurs autorisations. Par exemple, la configuration des [partenaires technologiques]({{site.baseurl}}/partners) requiert généralement à la fois l'accès au partenaire et une autorisation de lecture de base pour les fonctionnalités de l'espace de travail associé.
- **Importer et mettre à jour les données utilisateur :** Cette autorisation inclut la possibilité de modifier les profils utilisateur de l'application via les flux d'importation, et pas seulement les enregistrements des utilisateurs du tableau de bord.

## Modifier les autorisations d'un utilisateur {#edit-a-users-permissions}

Pour modifier les autorisations actuelles d'un utilisateur (administrateur, entreprise ou espace de travail), accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, puis sélectionnez son nom.

![La page « Utilisateurs de l'entreprise » dans Braze affichant un tableau des utilisateurs du tableau de bord.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrateur %}

### Administrateur {#admin}

Les administrateurs ont accès à toutes les fonctionnalités et peuvent modifier n'importe quel paramètre de l'entreprise. Ils peuvent :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow)
- Ajouter, modifier, supprimer, suspendre ou réactiver d'autres [utilisateurs Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users)
- Exporter les utilisateurs Braze au format CSV

Pour accorder ou retirer les privilèges d'administrateur, sélectionnez **This user is an admin**, puis sélectionnez **Update user**.

{% alert warning %}
Si vous retirez les privilèges d'administrateur d'un utilisateur, celui-ci ne pourra plus accéder à Braze tant que vous ne lui aurez pas attribué au moins une [autorisation au niveau de l'entreprise ou de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Entreprise %}

### Entreprise {#company}

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case à côté de l'autorisation correspondante. Lorsque vous avez terminé, sélectionnez **Update user**.

| Nom de l'autorisation | Description |
|----------|-----------|
| Gérer les paramètres de l'entreprise | Permet aux utilisateurs de modifier les paramètres d'autorisation et la vérification de l'expéditeur. |
| Créer et supprimer des espaces de travail | Permet aux utilisateurs de créer et de supprimer des espaces de travail. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autorisations au niveau de l'entreprise" }

{% endtab %}
{% tab Espace de travail %}

### Espace de travail {#workspace}

Vous pouvez attribuer à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer ses autorisations au niveau de l'espace de travail, sélectionnez **Select workspaces and permissions**, puis choisissez ses autorisations manuellement ou attribuez un [ensemble d'autorisations ou un rôle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set) que vous avez créé précédemment. Si vous devez accorder à un utilisateur des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% subtabs %}
{% subtab Sélection manuelle %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans le menu déroulant. Puis, sous **Permissions**, sélectionnez une ou plusieurs autorisations. Ces autorisations ne seront attribuées que pour les espaces de travail que vous avez sélectionnés. Vous pouvez également sélectionner **Assign workspace admin access** si vous souhaitez accorder à l'utilisateur l'ensemble des autorisations pour cet espace de travail.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail sélectionnées manuellement dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Attribuer un ensemble d'autorisations %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans le menu déroulant. Puis, sous **Permission Sets**, choisissez un ensemble d'autorisations. Ces autorisations ne seront attribuées que pour les espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail attribuées via un ensemble d'autorisations dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Attribuer un rôle %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans le menu déroulant. Puis, sous **Role**, choisissez un rôle. Ces autorisations ne seront attribuées que pour les espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail attribuées via un rôle dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporter les autorisations des utilisateurs {#exporting-user-permissions}

Pour télécharger une liste de vos utilisateurs et de leurs autorisations, accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, puis sélectionnez **Exporter les utilisateurs**. Un fichier CSV sera envoyé à votre adresse e-mail sous peu.

## Liste des autorisations {#list-of-permissions}

### Communication {#messaging}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Campaigns | Afficher les Campaigns | Afficher les Campaigns |
| Campaigns | Lancer des Campaigns | Démarrer, arrêter, mettre en pause ou reprendre des Campaigns existantes |
| Campaigns | Archiver des Campaigns | Déplacer des Campaigns vers les archives |
| Campaigns | Modifier des Campaigns | Créer et mettre à jour des Campaigns |
| Campaigns | Approuver et refuser des Campaigns | Approuver ou refuser des Campaigns. Le [workflow d'approbation pour les Campaigns]({{site.baseurl}}/user_guide/messaging/governance/approvals) doit être activé pour que cette autorisation s'applique. |
| Canvas | Afficher les Canvas | Afficher les Canvas |
| Canvas | Archiver des Canvas | Déplacer des Canvas vers les archives |
| Canvas | Modifier des Canvas | Créer et mettre à jour des Canvas |
| Canvas | Lancer des Canvas | Démarrer, arrêter, mettre en pause ou reprendre des Canvas existants |
| Canvas | Approuver et refuser des Canvas | Approuver ou refuser des Canvas. Le [workflow d'approbation pour les Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals) doit être activé pour que cette autorisation s'applique. |
| Feature flags | Afficher les feature flags | Afficher les feature flags |
| Feature flags | Archiver des feature flags | Déplacer des feature flags vers les archives |
| Feature flags | Modifier des feature flags | Créer et mettre à jour des feature flags |
| Limites de fréquence | Afficher les règles de limite de fréquence | Afficher les règles de limite de fréquence |
| Limites de fréquence | Modifier les règles de limite de fréquence | Créer et mettre à jour les règles de limite de fréquence |
| Pages de destination | Afficher les pages de destination | Afficher les pages de destination |
| Pages de destination | Publier des pages de destination | Rendre active une page de destination en brouillon |
| Pages de destination | Modifier les brouillons de pages de destination | Créer et enregistrer des brouillons de pages de destination |
| Paramètres d'archivage des messages | Afficher les paramètres d'archivage des messages | Afficher les paramètres d'archivage des messages sans effectuer de modifications |
| Paramètres d'archivage des messages | Modifier les paramètres d'archivage des messages | Créer et mettre à jour les paramètres d'archivage des messages |
| Priorisation des messages | Afficher la priorisation des messages | Afficher les paramètres de priorisation des messages sans effectuer de modifications |
| Priorisation des messages | Modifier la priorisation des messages | Créer et mettre à jour les paramètres de priorisation des messages |
| WhatsApp Flows | Afficher les WhatsApp Flows | Afficher tous les WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations de communication" }

### Audience {#audience}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Groupe de contrôle global | Afficher le groupe de contrôle global | Afficher la page de configuration du groupe de contrôle global |
| Groupe de contrôle global | Modifier le groupe de contrôle global | Créer et enregistrer des modifications au groupe de contrôle global. Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » doivent également disposer des autorisations « Modifier des Campaigns » et « Modifier des Canvas ». Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » se voient également accorder l'autorisation « Afficher le groupe de contrôle global ». |
| Emplacements | Archiver des emplacements | Déplacer des emplacements vers les archives |
| Emplacements | Afficher les emplacements | Afficher les emplacements |
| Emplacements | Modifier des emplacements | Créer et modifier des emplacements |
| Segments | Afficher les Segments | Afficher les Segments. Les utilisateurs doivent disposer de l'autorisation « Afficher les Segments » pour avoir l'autorisation « Modifier des Segments » ou « Archiver des Segments » |
| Segments | Archiver des Segments | Archiver et désarchiver des Segments. Les utilisateurs disposant de l'autorisation « Archiver des Segments » doivent également disposer de l'autorisation « Afficher les Segments » |
| Segments | Modifier des Segments | Créer et mettre à jour des Segments. Les utilisateurs disposant de l'autorisation « Modifier des Segments » doivent également disposer de l'autorisation « Afficher les Segments » |
| Données utilisateur | Afficher l'importation d'utilisateurs | Afficher les importations d'utilisateurs par CSV sans effectuer de modifications |
| Données utilisateur | Importer des utilisateurs | Charger des utilisateurs dans le tableau de bord |
| Données utilisateur | Modifier les données utilisateur | Créer et mettre à jour les données utilisateur |
| Données utilisateur | Exporter les données utilisateur | Télécharger des utilisateurs depuis le tableau de bord |
| Utilisateurs en double | Afficher les enregistrements de fusion d'utilisateurs | Afficher une liste des enregistrements de fusion d'utilisateurs |
| Utilisateurs | Afficher les profils utilisateur (données d'identification masquées) | Afficher les profils utilisateur de manière conforme aux données d'identification. Les utilisateurs disposant de cette autorisation ne peuvent pas enregistrer ou lancer de Campaigns qui font référence à des attributs personnalisés marqués comme données d'identification, sauf s'ils disposent également de l'autorisation « Afficher les attributs personnalisés marqués comme données d'identification ».<br><br>L'autorisation « Afficher les profils utilisateur (données d'identification masquées) » doit être activée avant utilisation. Contactez votre gestionnaire de la satisfaction client pour l'activer dans votre espace de travail. |
| Utilisateurs | Afficher les propriétés d'événement utilisateur | Afficher les propriétés d'événement dans l'onglet **Historique des événements** des profils utilisateur |
| Utilisateurs en double | Fusionner des utilisateurs en double | Combiner des utilisateurs en double en un seul utilisateur. Les doublons sont supprimés après la fusion |
| Suppression d'utilisateurs | Afficher les enregistrements de suppression d'utilisateurs | Afficher une liste des enregistrements de suppression d'utilisateurs |
| Suppression d'utilisateurs | Supprimer des utilisateurs | Supprimer définitivement des utilisateurs du tableau de bord individuellement ou en masse |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations d'audience" }

### Modèle {#template}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Modèles de bannière | Afficher les modèles de bannière | Afficher les modèles de bannière |
| Modèles de bannière | Archiver des modèles de bannière | Déplacer des modèles de bannière vers les archives |
| Modèles de bannière | Modifier des modèles de bannière | Créer et mettre à jour des modèles de bannière |
| Modèles Canvas | Afficher les modèles Canvas | Afficher les modèles Canvas |
| Modèles Canvas | Archiver des modèles Canvas | Déplacer des modèles Canvas vers les archives |
| Modèles Canvas | Créer et modifier des modèles Canvas | Créer et mettre à jour des modèles Canvas |
| Content Blocks | Afficher les Content Blocks | Afficher les Content Blocks |
| Content Blocks | Lancer des Content Blocks | Publier des Content Blocks en brouillon, et modifier, archiver et désarchiver des Content Blocks lancés |
| Content Blocks | Archiver des Content Blocks | Déplacer des Content Blocks vers les archives |
| Content Blocks | Modifier des Content Blocks | Créer des Content Blocks et modifier des Content Blocks en brouillon |
| Modèles de liens e-mail | Afficher les modèles de liens e-mail | Afficher les modèles de liens sans effectuer de modifications |
| Modèles de liens e-mail | Modifier des modèles de liens e-mail | Créer et mettre à jour des modèles de liens |
| Modèles d'e-mail | Afficher les modèles d'e-mail | Afficher les modèles d'e-mail |
| Modèles d'e-mail | Archiver des modèles d'e-mail | Déplacer des modèles d'e-mail vers les archives |
| Modèles d'e-mail | Modifier des modèles d'e-mail | Créer et mettre à jour des modèles d'e-mail |
| Modèles de messages in-app | Afficher les modèles de messages in-app | Afficher les modèles de messages in-app sans effectuer de modifications |
| Modèles de messages in-app | Archiver des modèles de messages in-app | Déplacer des modèles de messages in-app vers les archives |
| Modèles de messages in-app | Modifier des modèles de messages in-app | Créer et mettre à jour des modèles de messages in-app |
| Modèles de pages de destination | Afficher les modèles de pages de destination | Afficher les modèles de pages de destination |
| Modèles de pages de destination | Archiver des modèles de pages de destination | Déplacer des modèles de pages de destination vers les archives |
| Modèles de pages de destination | Modifier des modèles de pages de destination | Créer et mettre à jour des modèles de pages de destination |
| Modèles de webhook | Afficher les modèles de webhook | Afficher les modèles de webhook sans effectuer de modifications |
| Modèles de webhook | Archiver des modèles de webhook | Déplacer des modèles de webhook vers les archives |
| Modèles de webhook | Modifier des modèles de webhook | Créer et mettre à jour des modèles de webhook |
| Modèles de messages WhatsApp | Afficher les modèles de messages WhatsApp | Permet aux utilisateurs d'afficher les [modèles de messages WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) |
| Modèles de messages WhatsApp | Modifier des modèles de messages WhatsApp | Permet aux utilisateurs de créer des modèles de messages WhatsApp dans le générateur de modèles. Cette fonctionnalité est actuellement en accès anticipé. |
| Modèles de messages WhatsApp depuis Meta | Afficher les modèles de messages WhatsApp depuis Meta | Afficher tous les modèles WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations de modèles" }

### Intégrations partenaires {#partner-integrations}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Intégrations Currents | Afficher les intégrations Currents | Afficher les intégrations Currents |
| Intégrations Currents | Modifier des intégrations Currents | Créer, mettre à jour et supprimer des intégrations Currents |
| Partenaires technologiques | Modifier des partenaires technologiques | Créer et mettre à jour des partenaires technologiques |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations d'intégrations partenaires" }

### Paramètres de données {#data-settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Catalogues | Afficher les catalogues | Afficher les catalogues et les sélections |
| Catalogues | Supprimer des catalogues | Supprimer définitivement des catalogues |
| Catalogues | Exporter des catalogues | Télécharger des catalogues depuis le tableau de bord |
| Catalogues | Modifier des catalogues | Créer et mettre à jour des catalogues et des sélections |
| Ingestion de données cloud | Modifier l'ingestion de données cloud | Créer, mettre à jour et supprimer des sources et des synchronisations |
| Attributs personnalisés | Afficher les attributs personnalisés | Afficher les attributs personnalisés et le rapport d'utilisation |
| Attributs personnalisés | Exporter les attributs personnalisés | Télécharger les attributs personnalisés depuis le tableau de bord |
| Attributs personnalisés | Supprimer des attributs personnalisés | Supprimer définitivement des attributs personnalisés |
| Attributs personnalisés | Bloquer des attributs personnalisés | Ajouter des attributs personnalisés à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Attributs personnalisés | Modifier des attributs personnalisés | Créer et mettre à jour des attributs personnalisés |
| Segmentation par propriétés d'événements personnalisés | Modifier la segmentation par propriétés d'événements personnalisés | Activer et désactiver la segmentation par propriétés d'événements personnalisés |
| Événements personnalisés | Afficher les événements personnalisés | Afficher les événements personnalisés et le rapport d'utilisation, et ajouter des événements personnalisés à l'e-mail de rapport d'analyse quotidien |
| Événements personnalisés | Exporter les événements personnalisés | Télécharger les événements personnalisés depuis le tableau de bord |
| Données d'identification | Afficher les données d'identification | Afficher les données d'identification |
| Événements personnalisés | Supprimer des événements personnalisés | Supprimer définitivement des événements personnalisés |
| Événements personnalisés | Bloquer des événements personnalisés | Ajouter des événements personnalisés à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Événements personnalisés | Modifier des événements personnalisés | Créer et mettre à jour des événements personnalisés |
| Produits | Afficher les produits | Afficher les produits |
| Produits | Bloquer des produits | Ajouter des produits à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Produits | Modifier des produits | Créer et mettre à jour des produits |
| Segmentation par propriétés d'achat | Modifier la segmentation par propriétés d'achat | Activer et désactiver la segmentation par propriétés d'événements d'achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations des paramètres de données" }

### Paramètres {#settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Identifiants API | Afficher les identifiants API | Afficher les identifiants API et autres identifiants |
| Clés API | Afficher les clés API | Afficher les clés API |
| Clés API | Modifier des clés API | Créer et mettre à jour des clés API |
| Limites API | Afficher les limites API | Afficher les limites de débit API |
| Alertes d'utilisation API | Afficher les alertes d'utilisation API | Afficher les alertes d'utilisation API |
| Alertes d'utilisation API | Modifier les alertes d'utilisation API | Créer et mettre à jour les alertes d'utilisation API |
| Données d'utilisation API | Afficher le tableau de bord d'utilisation API | Afficher le tableau de bord d'utilisation API |
| Paramètres de l'application | Modifier les paramètres de l'application | Créer, modifier et mettre à jour des applications dans les paramètres de l'application |
| Paramètres de l'application | Afficher les paramètres de l'application | Afficher la page des paramètres de l'application |
| Paramètres de synchronisation d'audience | Afficher les paramètres de synchronisation d'audience | Afficher tous les paramètres de leurs partenaires de synchronisation d'audience connectés |
| Utilisateurs du tableau de bord | Modifier les utilisateurs du tableau de bord | Afficher, créer et modifier les utilisateurs de l'entreprise |
| Paramètres d'e-mail | Afficher les paramètres d'e-mail | Afficher les préférences d'e-mail |
| Paramètres d'e-mail | Modifier les paramètres d'e-mail | Activer et mettre à jour les préférences d'e-mail |
| Journal des événements utilisateurs | Afficher le journal des événements utilisateurs | Afficher les journaux des événements utilisateurs |
| Groupes internes | Afficher les groupes d'utilisateurs internes | Afficher les groupes internes |
| Groupes internes | Supprimer des groupes d'utilisateurs internes | Supprimer des groupes internes |
| Groupes internes | Modifier des groupes d'utilisateurs internes | Créer et mettre à jour des groupes internes |
| Journal d'activité des messages | Afficher le journal d'activité des messages | Afficher les journaux d'activité des messages |
| Paramètres multilingues | Afficher les paramètres de localisation | Afficher la page des paramètres des langues multilingues |
| Paramètres multilingues | Supprimer des paramètres de localisation | Supprimer une langue multilingue |
| Paramètres multilingues | Modifier les paramètres de localisation | Créer des langues multilingues |
| Centres de préférences | Afficher les centres de préférences | Afficher les centres de préférences |
| Centres de préférences | Modifier des centres de préférences | Créer et mettre à jour des centres de préférences |
| Centres de préférences | Lancer des centres de préférences | Rendre un centre de préférences en brouillon actif ou mettre à jour un centre existant |
| Paramètres push | Afficher les paramètres push | Afficher les paramètres push |
| Paramètres push | Modifier les paramètres push | Créer et mettre à jour les paramètres push |
| Débogueur SDK | Afficher le débogueur SDK | Afficher le débogueur SDK ou les sessions de débogage |
| Débogueur SDK | Modifier le débogueur SDK | Créer et télécharger des sessions du débogueur SDK |
| Étiquettes | Afficher les étiquettes | Afficher les étiquettes |
| Étiquettes | Supprimer des étiquettes | Supprimer définitivement des étiquettes |
| Étiquettes | Modifier des étiquettes | Créer et mettre à jour des étiquettes |
| Teams | Afficher les Teams | Afficher les Teams |
| Teams | Archiver des Teams | Déplacer des Teams vers les archives |
| Teams | Modifier des Teams | Créer et mettre à jour des Teams |
| Paramètres WhatsApp | Afficher les paramètres WhatsApp | Afficher tous les paramètres du canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations des paramètres" }

### Decisioning Studio

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Agents Decisioning Studio | Afficher les agents Decisioning Studio | Afficher la configuration des agents Decisioning Studio sans effectuer de modifications |
| Audience Decisioning Studio | Afficher l'audience Decisioning Studio | Voir les détails de l'audience dans les résumés de configuration des agents Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations de Decisioning Studio" }

### Autre {#other}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Utilisation de l'application | Afficher les données d'utilisation | Afficher les données d'utilisation |
| Facturation | Afficher les détails de facturation | Afficher les détails de facturation |
| Agents IA personnalisés | Afficher les agents IA de la console | Permet aux utilisateurs d'afficher les agents IA personnalisés |
| Agents IA personnalisés | Archiver des agents IA de la console | Permet aux utilisateurs d'archiver des agents IA personnalisés |
| Agents IA personnalisés | Modifier des agents IA de la console | Permet aux utilisateurs de créer et mettre à jour des agents IA personnalisés |
| Attributs personnalisés marqués comme données d'identification | Afficher les attributs personnalisés marqués comme données d'identification | Afficher les attributs personnalisés marqués comme données d'identification |
| Rapports du tableau de bord | Afficher les rapports du tableau de bord | Afficher les rapports sans effectuer de modifications |
| Rapports du tableau de bord | Supprimer des rapports du tableau de bord | Supprimer définitivement des rapports |
| Rapports du tableau de bord | Modifier des rapports du tableau de bord | Créer et mettre à jour des rapports |
| Paramètres de domaine | Modifier les paramètres de domaine | Ajouter des domaines délégués et des domaines personnalisés sous Domaines vérifiés |
| Chiffrement au niveau des champs | Modifier le chiffrement au niveau des champs d'identification | Activer et mettre à jour les paramètres de chiffrement au niveau des champs |
| Ressources de la bibliothèque multimédia | Afficher les ressources de la bibliothèque multimédia | Afficher les ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Supprimer des ressources de la bibliothèque multimédia | Supprimer des ressources de la bibliothèque multimédia de l'interface. Les ressources supprimées restent hébergées par Braze pour éviter de casser les messages qui y font référence. Pour supprimer définitivement une ressource, contactez le support Braze. |
| Ressources de la bibliothèque multimédia | Modifier des ressources de la bibliothèque multimédia | Créer et mettre à jour des ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Remplacer des ressources de la bibliothèque multimédia | Remplacer le fichier d'une ressource existante de la bibliothèque multimédia tout en conservant son URL et son ID de ressource stables |
| Limites de débit des messages | Afficher les limites de débit des messages | Afficher les limites de débit des messages au niveau de l'espace de travail |
| Limites de débit des messages | Modifier les limites de débit des messages | Configurer et modifier les limites de débit des messages au niveau de l'espace de travail |
| Operator | Utiliser BrazeAI<sup>TM</sup> Operator | Accéder à Braze Operator et l'utiliser pour répondre à des questions, guider la configuration, résoudre des problèmes et générer des idées |
| Emplacements de bannière | Afficher les emplacements de bannière | Afficher les emplacements de bannière |
| Emplacements de bannière | Archiver des emplacements de bannière | Déplacer des emplacements de bannière vers les archives |
| Emplacements de bannière | Modifier des emplacements de bannière | Créer et mettre à jour des emplacements de bannière |
| Codes de promotion | Afficher les codes de promotion | Afficher les codes de promotion |
| Codes de promotion | Exporter les codes de promotion | Télécharger une liste de codes de promotion depuis le tableau de bord |
| Codes de promotion | Modifier des codes de promotion | Créer et mettre à jour des codes de promotion |
| Groupes d'abonnement | Modifier des abonnements | Créer et mettre à jour des groupes d'abonnement |
| Transformations | Modifier des transformations de données | Créer et mettre à jour des transformations de données |
| Transformations | Afficher les transformations de données | Afficher les transformations de données |
| Tickets de support | Créer un ticket de support | Créer et mettre à jour des tickets de support |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autres autorisations" }