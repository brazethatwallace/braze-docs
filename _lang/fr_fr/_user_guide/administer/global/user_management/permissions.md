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

Utilisez les ensembles d'autorisations pour regrouper les autorisations liées à des domaines ou des actions spécifiques. Vous pouvez appliquer des ensembles d'autorisations aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un ensemble d'autorisations, accédez à **Paramètres** > **Gestion des utilisateurs** > **Ensembles d'autorisations**, puis sélectionnez **Créer un ensemble d'autorisations**. Pour une description de chaque autorisation, consultez [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab exemples d'ensembles d'autorisations %}
| Nom | Autorisations |
|-----------|----------------|
| Développeurs | "View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger". |
| Marketeurs | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents". |
| Gestion des utilisateurs | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple d'ensemble d'autorisations" }
{% endtab %}
{% endtabs %}

## Créer un rôle {#creating-a-role}

Les rôles permettent une meilleure structuration en regroupant vos autorisations personnalisées individuelles avec les contrôles d'accès aux espaces de travail. Cela est particulièrement utile si vous avez de nombreuses marques ou des espaces de travail régionaux dans un même tableau de bord. Grâce aux rôles, vous pouvez ajouter des utilisateurs du tableau de bord aux espaces de travail appropriés et leur accorder directement les autorisations associées. Pour créer un rôle, accédez à **Paramètres** > **Gestion des utilisateurs** > **Rôles**, puis sélectionnez **Créer un rôle**. Pour une description de chaque autorisation, consultez [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab exemples de rôles %}
| Nom du rôle    | Espace de travail | Autorisations
----------- | ----------- | ---------
| Marketeur - Marques de mode | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Marketeur - Marques de soins | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |"View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers".|
| Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemples de rôles" }
{% endtab %}
{% endtabs %}

## En quoi les ensembles d'autorisations et les rôles diffèrent-ils des équipes ? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Considérations relatives à l'ajout d'autorisations utilisateur aux équipes {#considerations-for-adding-user-permissions-to-teams}

Vous pouvez rencontrer des difficultés lorsque vous essayez d'enregistrer des autorisations dans le tableau de bord de Braze, notamment lors de l'ajout ou de la suppression d'utilisateurs d'un espace de travail, ou de leur ajout à une équipe. Le bouton **Save/Update Users** peut être grisé si les autorisations de l'utilisateur sont identiques à celles qu'il possède déjà au niveau de l'espace de travail. Cette restriction existe car il n'y a aucun avantage à avoir une équipe si tous les utilisateurs disposent des mêmes autorisations que l'ensemble de l'espace de travail.

Pour ajouter un utilisateur à une équipe tout en conservant les mêmes autorisations, n'attribuez aucune autorisation au niveau de l'espace de travail. Attribuez plutôt les autorisations exclusivement au niveau de l'équipe.

## Utilisateurs limités {#limited-users}

Les utilisateurs limités disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze, tout en ayant des restrictions par rapport aux administrateurs de l'entreprise et aux administrateurs d'espaces de travail.

| Portée | Description |
| --- | --- |
| Autorisations | Les utilisateurs limités peuvent modifier les autorisations d'autres utilisateurs limités s'ils disposent de l'autorisation « Edit Dashboard Users ». Ils peuvent également créer de nouveaux utilisateurs limités et modifier leurs ensembles d'autorisations. En revanche, ils ne peuvent pas créer ni gérer de comptes d'administrateur de l'entreprise. |
| Limitations de rôle | Si un utilisateur limité dispose de toutes les autorisations sauf « Workspace Admin », il conserve l'accès à toutes les autres autorisations habituellement accordées à un administrateur d'espace de travail. |
| Visibilité des autorisations | Si un utilisateur limité dispose de l'autorisation « Edit Dashboard Users » pour un espace de travail (par exemple Dev) mais pas pour un autre (par exemple Prod), il ne verra pas les autorisations de l'espace de travail Prod dans sa page de détails des utilisateurs du tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autorisations pour les utilisateurs limités" }

### Comparer les utilisateurs limités {#compare-limited-users}

| Type d'utilisateur limité | Description |
| --- | --- |
| Administrateur d'espace de travail | Les administrateurs d'espace de travail disposent d'autorisations spécifiques à la gestion des espaces de travail, mais n'ont pas la même autorité que les administrateurs de l'entreprise. Les utilisateurs limités peuvent hériter d'autorisations similaires à celles des administrateurs d'espace de travail s'ils disposent des autorisations nécessaires cochées. |
| Administrateur (administrateur de l'entreprise) | Les administrateurs de l'entreprise disposent d'autorisations plus étendues, y compris la possibilité de supprimer des utilisateurs du tableau de bord. Cependant, ils ne peuvent pas supprimer leur propre compte et doivent contacter un autre administrateur de l'entreprise pour cette action. |
| Accès en lecture seule | Pour accéder à certaines parties du tableau de bord, comme la page Campaigns, les utilisateurs doivent se voir attribuer des autorisations de consultation. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparaison des utilisateurs limités" }

### Erreur d'accès limité {#limited-access-error}

Les utilisateurs peuvent rencontrer des messages tels que « You need "View Landing Pages" permissions to access this page ». Dans ce cas, l'utilisateur et l'administrateur du compte doivent vérifier que les autorisations requises ont bien été accordées. Si c'est le cas, essayez de résoudre le problème en désactivant puis en réactivant les autorisations de l'utilisateur.

{% alert note %}
Il n'est pas possible de fusionner ou d'importer les autorisations d'un utilisateur du tableau de bord vers un autre.
{% endalert %}

## Nuances des autorisations utilisateur {#nuances-of-user-permissions}

Gardez les comportements suivants à l'esprit lorsque vous attribuez l'accès au tableau de bord :

- **Administrateur d'espace de travail versus Administrateur de l'entreprise :** Les administrateurs d'espace de travail gèrent les autorisations au sein des espaces de travail qui leur sont attribués. Les administrateurs de l'entreprise disposent d'une autorité à l'échelle de l'entreprise, y compris la suppression d'autres utilisateurs du tableau de bord.
- **Utilisateurs limités :** Les utilisateurs limités disposant de l'autorisation « Modifier les utilisateurs du tableau de bord » peuvent gérer d'autres utilisateurs limités, mais ne peuvent pas créer ni gérer des comptes d'administrateur de l'entreprise.
- **Portée de la gestion des utilisateurs du tableau de bord :** Sur la page de détail de l'utilisateur, les autorisations n'apparaissent que pour les espaces de travail auxquels l'éditeur peut accéder. Un utilisateur limité pouvant modifier des utilisateurs dans un espace de travail peut ne pas voir les cases à cocher des autorisations d'un autre espace de travail.
- **Bouton Attribuer des autorisations :** Lorsque vous modifiez un utilisateur et que celui-ci dispose déjà d'autorisations au niveau de l'espace de travail ou d'ensembles d'autorisations pour chaque espace de travail que vous pouvez gérer, le bouton **Assign permissions** disparaît. Cela se produit car il n'y a plus d'espaces de travail supplémentaires à attribuer au niveau de l'espace de travail.
- **Exporter les données utilisateur :** L'exportation des données utilisateur nécessite un accès au niveau de l'espace de travail en plus de l'autorisation d'exportation.
- **Autorisations composites :** Certains domaines nécessitent plusieurs autorisations. Par exemple, la configuration des [partenaires technologiques]({{site.baseurl}}/partners) nécessite généralement à la fois un accès partenaire et une autorisation de lecture de base pour les fonctionnalités de l'espace de travail associé.
- **Importer et mettre à jour les données utilisateur :** Cette autorisation inclut la possibilité de modifier les profils utilisateur de l'application via les flux d'importation, et pas uniquement les enregistrements des utilisateurs du tableau de bord.

## Modifier les autorisations d'un utilisateur {#edit-a-users-permissions}

Pour modifier les autorisations actuelles d'un utilisateur au niveau administrateur, entreprise ou espace de travail, accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, puis sélectionnez son nom.

![La page « Utilisateurs de l'entreprise » dans Braze affichant un tableau des utilisateurs du tableau de bord.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrateur %}

### Administrateur {#admin}

Les administrateurs ont accès à toutes les fonctionnalités et peuvent modifier tous les paramètres de l'entreprise. Ils peuvent :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow)
- Ajouter, modifier, supprimer, suspendre ou réactiver d'autres [utilisateurs Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users)
- Exporter les utilisateurs Braze sous forme de fichier CSV

Pour accorder ou retirer les privilèges d'administrateur, sélectionnez **This user is an admin**, puis sélectionnez **Update user**.

{% alert warning %}
Si vous retirez les privilèges d'administrateur d'un utilisateur, celui-ci ne pourra plus accéder à Braze tant que vous ne lui aurez pas attribué au moins une [autorisation au niveau de l'entreprise ou de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Entreprise %}

### Entreprise {#company}

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case correspondante. Lorsque vous avez terminé, sélectionnez **Update user**.

| Nom de l'autorisation | Description |
|----------|-----------|
| Gérer les paramètres de l'entreprise | Permet aux utilisateurs de modifier les paramètres d'autorisations et la vérification de l'expéditeur. |
| Créer et supprimer des espaces de travail | Permet aux utilisateurs de créer et de supprimer des espaces de travail. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autorisations au niveau de l'entreprise" }

{% endtab %}
{% tab Espace de travail %}

### Espace de travail {#workspace}

Vous pouvez attribuer à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer ses autorisations au niveau de l'espace de travail, sélectionnez **Select workspaces and permissions**, puis choisissez ses autorisations manuellement ou attribuez-lui un [ensemble d'autorisations ou un rôle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set) que vous avez précédemment créé. Si vous devez attribuer à un utilisateur des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

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

Pour télécharger une liste de vos utilisateurs et de leurs autorisations, accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, puis sélectionnez **Exporter les utilisateurs**. Un fichier CSV sera envoyé sous peu à votre adresse e-mail.

## Liste des autorisations {#list-of-permissions}

### Communication {#messaging}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Campaigns | Voir les Campaigns | Consulter les Campaigns |
| Campaigns | Lancer les Campaigns | Démarrer, arrêter, mettre en pause ou reprendre les Campaigns existantes |
| Campaigns | Archiver les Campaigns | Déplacer les Campaigns dans les archives |
| Campaigns | Modifier les Campaigns | Créer et mettre à jour les Campaigns |
| Campaigns | Approuver et refuser les Campaigns | Approuver ou refuser les Campaigns. Le [flux de travail d'approbation des Campaigns]({{site.baseurl}}/user_guide/messaging/governance/approvals) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement en accès anticipé. Contactez votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Canvas | Voir les Canvas | Consulter les Canvas |
| Canvas | Archiver les Canvas | Déplacer les Canvas dans les archives |
| Canvas | Modifier les Canvas | Créer et mettre à jour les Canvas |
| Canvas | Lancer les Canvas | Démarrer, arrêter, mettre en pause ou reprendre les Canvas existants |
| Canvas | Approuver et refuser les Canvas | Approuver ou refuser les Canvas. Le [flux de travail d'approbation des Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement en accès anticipé. Contactez votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Feature flags | Voir les feature flags | Consulter les feature flags |
| Feature flags | Archiver les feature flags | Déplacer les feature flags dans les archives |
| Feature flags | Modifier les feature flags | Créer et mettre à jour les feature flags |
| Limites de fréquence | Voir les règles de limite de fréquence | Consulter les règles de limite de fréquence |
| Limites de fréquence | Modifier les règles de limite de fréquence | Créer et mettre à jour les règles de limite de fréquence |
| Pages de destination | Voir les pages de destination | Consulter les pages de destination |
| Pages de destination | Publier les pages de destination | Activer un brouillon de page de destination |
| Pages de destination | Modifier les brouillons de pages de destination | Créer et enregistrer des brouillons de pages de destination |
| Paramètres d'archivage des messages | Voir les paramètres d'archivage des messages | Consulter les paramètres d'archivage des messages sans apporter de modifications |
| Paramètres d'archivage des messages | Modifier les paramètres d'archivage des messages | Créer et mettre à jour les paramètres d'archivage des messages |
| Priorisation des messages | Voir la priorisation des messages | Consulter les paramètres de priorisation des messages sans apporter de modifications |
| Priorisation des messages | Modifier la priorisation des messages | Créer et mettre à jour les paramètres de priorisation des messages |
| WhatsApp Flows | Voir les WhatsApp Flows | Consulter tous les WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations de communication" }

### Audience {#audience}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Groupe de contrôle global | Voir le groupe de contrôle global | Consulter la page de configuration du groupe de contrôle global |
| Groupe de contrôle global | Modifier le groupe de contrôle global | Créer et enregistrer des modifications du groupe de contrôle global. Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » doivent également disposer des autorisations « Modifier les Campaigns » et « Modifier les Canvas ». Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » bénéficient également de l'autorisation « Voir le groupe de contrôle global ». |
| Emplacements | Archiver les emplacements | Déplacer les emplacements dans les archives |
| Emplacements | Voir les emplacements | Consulter les emplacements |
| Emplacements | Modifier les emplacements | Créer et modifier les emplacements |
| Segments | Voir les Segments | Consulter les Segments. Les utilisateurs doivent disposer de l'autorisation « Voir les Segments » pour avoir l'autorisation « Modifier les Segments » ou « Archiver les Segments » |
| Segments | Archiver les Segments | Archiver et désarchiver les Segments. Les utilisateurs disposant de l'autorisation « Archiver les Segments » doivent également disposer de l'autorisation « Voir les Segments » |
| Segments | Modifier les Segments | Créer et mettre à jour les Segments. Les utilisateurs disposant de l'autorisation « Modifier les Segments » doivent également disposer de l'autorisation « Voir les Segments » |
| Données utilisateur | Voir l'importation d'utilisateurs | Consulter les importations CSV d'utilisateurs sans apporter de modifications |
| Données utilisateur | Importer des utilisateurs | Téléverser des utilisateurs vers le tableau de bord |
| Données utilisateur | Modifier les données utilisateur | Créer et mettre à jour les données utilisateur |
| Données utilisateur | Exporter les données utilisateur | Télécharger les utilisateurs depuis le tableau de bord |
| Utilisateurs en double | Voir les enregistrements de fusion d'utilisateurs | Consulter la liste des enregistrements de fusion d'utilisateurs |
| Utilisateurs | Voir les profils utilisateur (données d'identification masquées) | Consulter les profils utilisateur de manière conforme aux données d'identification. Les utilisateurs disposant de cette autorisation ne peuvent pas enregistrer ou lancer des Campaigns faisant référence à des attributs personnalisés marqués comme données d'identification, sauf s'ils disposent également de l'autorisation « Voir les attributs personnalisés marqués comme données d'identification ».<br><br>L'autorisation « Voir les profils utilisateur (données d'identification masquées) » doit être activée avant utilisation. Contactez votre gestionnaire du succès des clients pour l'activer dans votre espace de travail. |
| Utilisateurs | Voir les propriétés d'événement utilisateur | Consulter les propriétés d'événement dans l'onglet **Historique des événements** sur les profils utilisateur |
| Utilisateurs en double | Fusionner les utilisateurs en double | Combiner les utilisateurs en double en un seul utilisateur. Les doublons sont supprimés après la fusion |
| Suppression d'utilisateurs | Voir les enregistrements de suppression d'utilisateurs | Consulter la liste des enregistrements de suppression d'utilisateurs |
| Suppression d'utilisateurs | Supprimer des utilisateurs | Supprimer définitivement des utilisateurs du tableau de bord, individuellement ou en masse |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations d'audience" }

### Modèle {#template}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Modèles de bannière | Voir les modèles de bannière | Consulter les modèles de bannière |
| Modèles de bannière | Archiver les modèles de bannière | Déplacer les modèles de bannière dans les archives |
| Modèles de bannière | Modifier les modèles de bannière | Créer et mettre à jour les modèles de bannière |
| Modèles Canvas | Voir les modèles Canvas | Consulter les modèles Canvas |
| Modèles Canvas | Archiver les modèles Canvas | Déplacer les modèles Canvas dans les archives |
| Modèles Canvas | Créer et modifier les modèles Canvas | Créer et mettre à jour les modèles Canvas |
| Content Blocks | Voir les Content Blocks | Consulter les Content Blocks |
| Content Blocks | Lancer les Content Blocks | Publier les brouillons de Content Blocks, et modifier, archiver et désarchiver les Content Blocks publiés |
| Content Blocks | Archiver les Content Blocks | Déplacer les Content Blocks dans les archives |
| Content Blocks | Modifier les Content Blocks | Créer des Content Blocks et modifier les brouillons de Content Blocks |
| Modèles de liens e-mail | Voir les modèles de liens e-mail | Consulter les modèles de liens sans apporter de modifications |
| Modèles de liens e-mail | Modifier les modèles de liens e-mail | Créer et mettre à jour les modèles de liens |
| Modèles d'e-mail | Voir les modèles d'e-mail | Consulter les modèles d'e-mail |
| Modèles d'e-mail | Archiver les modèles d'e-mail | Déplacer les modèles d'e-mail dans les archives |
| Modèles d'e-mail | Modifier les modèles d'e-mail | Créer et mettre à jour les modèles d'e-mail |
| Modèles de messages in-app | Voir les modèles de messages in-app | Consulter les modèles de messages in-app sans apporter de modifications |
| Modèles de messages in-app | Archiver les modèles de messages in-app | Déplacer les modèles de messages in-app dans les archives |
| Modèles de messages in-app | Modifier les modèles de messages in-app | Créer et mettre à jour les modèles de messages in-app |
| Modèles de pages de destination | Voir les modèles de pages de destination | Consulter les modèles de pages de destination |
| Modèles de pages de destination | Archiver les modèles de pages de destination | Déplacer les modèles de pages de destination dans les archives |
| Modèles de pages de destination | Modifier les modèles de pages de destination | Créer et mettre à jour les modèles de pages de destination |
| Modèles de webhooks | Voir les modèles de webhooks | Consulter les modèles de webhooks sans apporter de modifications |
| Modèles de webhooks | Archiver les modèles de webhooks | Déplacer les modèles de webhooks dans les archives |
| Modèles de webhooks | Modifier les modèles de webhooks | Créer et mettre à jour les modèles de webhooks |
| Modèles de messages WhatsApp | Voir les modèles de messages WhatsApp | Permet aux utilisateurs de consulter les [modèles de messages WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) |
| Modèles de messages WhatsApp | Modifier les modèles de messages WhatsApp | Permet aux utilisateurs de créer des modèles de messages WhatsApp dans le générateur de modèles. Cette fonctionnalité est actuellement en accès anticipé. |
| Modèles de messages WhatsApp de Meta | Voir les modèles de messages WhatsApp de Meta | Consulter tous les modèles WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations de modèles" }

### Intégrations partenaires {#partner-integrations}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Intégrations Currents | Voir les intégrations Currents | Consulter les intégrations Currents |
| Intégrations Currents | Modifier les intégrations Currents | Créer, mettre à jour et supprimer les intégrations Currents |
| Partenaires technologiques | Modifier les partenaires technologiques | Créer et mettre à jour les partenaires technologiques |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations des intégrations partenaires" }

### Paramètres des données {#data-settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Catalogues | Voir les catalogues | Consulter les catalogues et les sélections |
| Catalogues | Supprimer les catalogues | Supprimer définitivement les catalogues |
| Catalogues | Exporter les catalogues | Télécharger les catalogues depuis le tableau de bord |
| Catalogues | Modifier les catalogues | Créer et mettre à jour les catalogues et les sélections |
| Ingestion de données cloud | Modifier l'ingestion de données cloud | Créer, mettre à jour et supprimer les sources et les synchronisations |
| Attributs personnalisés | Voir les attributs personnalisés | Consulter les attributs personnalisés et le rapport d'utilisation |
| Attributs personnalisés | Exporter les attributs personnalisés | Télécharger les attributs personnalisés depuis le tableau de bord |
| Attributs personnalisés | Supprimer les attributs personnalisés | Supprimer définitivement les attributs personnalisés |
| Attributs personnalisés | Bloquer les attributs personnalisés | Ajouter des attributs personnalisés à une liste de blocage qui restreint leur utilisation dans le tableau de bord |
| Attributs personnalisés | Modifier les attributs personnalisés | Créer et mettre à jour les attributs personnalisés |
| Segmentation par propriétés d'événement personnalisé | Modifier la segmentation par propriétés d'événement personnalisé | Activer et désactiver la segmentation par propriétés d'événement personnalisé |
| Événements personnalisés | Voir les événements personnalisés | Consulter les événements personnalisés et le rapport d'utilisation, et ajouter des événements personnalisés à l'e-mail de rapport d'analyse quotidien |
| Événements personnalisés | Exporter les événements personnalisés | Télécharger les événements personnalisés depuis le tableau de bord |
| Données d'identification | Voir les données d'identification | Consulter les données d'identification |
| Événements personnalisés | Supprimer les événements personnalisés | Supprimer définitivement les événements personnalisés |
| Événements personnalisés | Bloquer les événements personnalisés | Ajouter des événements personnalisés à une liste de blocage qui restreint leur utilisation dans le tableau de bord |
| Événements personnalisés | Modifier les événements personnalisés | Créer et mettre à jour les événements personnalisés |
| Produits | Voir les produits | Consulter les produits |
| Produits | Bloquer les produits | Ajouter des produits à une liste de blocage qui restreint leur utilisation dans le tableau de bord |
| Produits | Modifier les produits | Créer et mettre à jour les produits |
| Segmentation par propriétés d'achat | Modifier la segmentation par propriétés d'achat | Activer et désactiver la segmentation par propriétés d'événement d'achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations des paramètres des données" }

### Paramètres {#settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Identifiants API | Voir les identifiants API | Consulter les identifiants API et autres identifiants |
| Clés API | Voir les clés API | Consulter les clés API |
| Clés API | Modifier les clés API | Créer et mettre à jour les clés API |
| Limites API | Voir les limites API | Consulter les limites de débit de l'API |
| Alertes d'utilisation API | Voir les alertes d'utilisation API | Consulter les alertes d'utilisation API |
| Alertes d'utilisation API | Modifier les alertes d'utilisation API | Créer et mettre à jour les alertes d'utilisation API |
| Données d'utilisation API | Voir le tableau de bord d'utilisation API | Consulter le tableau de bord d'utilisation API |
| Paramètres de l'application | Modifier les paramètres de l'application | Créer, modifier et mettre à jour les applications dans les paramètres de l'application |
| Paramètres de l'application | Voir les paramètres de l'application | Consulter la page des paramètres de l'application |
| Paramètres Audience Sync | Voir les paramètres Audience Sync | Consulter tous les paramètres de leurs partenaires Audience Sync connectés |
| Utilisateurs du tableau de bord | Modifier les utilisateurs du tableau de bord | Consulter, créer et modifier les utilisateurs de l'entreprise |
| Paramètres e-mail | Voir les paramètres e-mail | Consulter les préférences e-mail |
| Paramètres e-mail | Modifier les paramètres e-mail | Activer et mettre à jour les préférences e-mail |
| Journal des événements utilisateurs | Voir le journal des événements utilisateurs | Consulter les journaux d'événements utilisateurs |
| Groupes internes | Voir les groupes internes | Consulter les groupes internes |
| Groupes internes | Supprimer les groupes internes | Supprimer les groupes internes |
| Groupes internes | Modifier les groupes internes | Créer et mettre à jour les groupes internes |
| Journal d'activité des messages | Voir le journal d'activité des messages | Consulter les journaux d'activité des messages |
| Paramètres multilingues | Voir les paramètres de localisation | Consulter la page des paramètres de localisation multilingue |
| Paramètres multilingues | Supprimer les paramètres de localisation | Supprimer des paramètres régionaux multilingues |
| Paramètres multilingues | Modifier les paramètres de localisation | Créer des paramètres régionaux multilingues |
| Centres de préférences | Voir les centres de préférences | Consulter les centres de préférences |
| Centres de préférences | Modifier les centres de préférences | Créer et mettre à jour les centres de préférences |
| Centres de préférences | Lancer les centres de préférences | Activer un brouillon de centre de préférences ou mettre à jour un centre existant |
| Paramètres push | Voir les paramètres push | Consulter les paramètres des notifications push |
| Paramètres push | Modifier les paramètres push | Créer et mettre à jour les paramètres des notifications push |
| Débogueur SDK | Voir le débogueur SDK | Consulter le débogueur SDK ou les sessions de débogage |
| Débogueur SDK | Modifier le débogueur SDK | Créer et télécharger les sessions du débogueur SDK |
| Étiquettes | Voir les étiquettes | Consulter les étiquettes |
| Étiquettes | Supprimer les étiquettes | Supprimer définitivement les étiquettes |
| Étiquettes | Modifier les étiquettes | Créer et mettre à jour les étiquettes |
| Teams | Voir les Teams | Consulter les Teams |
| Teams | Archiver les Teams | Déplacer les Teams dans les archives |
| Teams | Modifier les Teams | Créer et mettre à jour les Teams |
| Paramètres WhatsApp | Voir les paramètres WhatsApp | Consulter tous les paramètres du canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations des paramètres" }

### Decisioning Studio

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Agents Decisioning Studio | Voir les agents Decisioning Studio | Consulter la configuration des agents Decisioning Studio sans apporter de modifications |
| Audience Decisioning Studio | Voir l'audience Decisioning Studio | Consulter les détails de l'audience dans les résumés de configuration des agents Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations de Decisioning Studio" }

### Autres {#other}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Utilisation de l'application | Voir les données d'utilisation | Consulter les données d'utilisation |
| Facturation | Voir les détails de facturation | Consulter les détails de facturation |
| Agents personnalisés | Voir les agents IA de la console d'agents | Permet aux utilisateurs de consulter les agents IA personnalisés |
| Agents personnalisés | Archiver les agents IA de la console d'agents | Permet aux utilisateurs d'archiver les agents IA personnalisés |
| Agents personnalisés | Modifier les agents IA de la console d'agents | Permet aux utilisateurs de créer et de mettre à jour les agents IA personnalisés |
| Attributs personnalisés marqués comme données d'identification | Voir les attributs personnalisés marqués comme données d'identification | Consulter les attributs personnalisés marqués comme données d'identification |
| Rapports du tableau de bord | Voir les rapports du tableau de bord | Consulter les rapports sans apporter de modifications |
| Rapports du tableau de bord | Supprimer les rapports du tableau de bord | Supprimer définitivement les rapports |
| Rapports du tableau de bord | Modifier les rapports du tableau de bord | Créer et mettre à jour les rapports |
| Paramètres de domaine | Modifier les paramètres de domaine | Ajouter des domaines délégués et des domaines personnalisés sous Domaines vérifiés |
| Chiffrement au niveau des champs | Modifier le chiffrement au niveau des champs d'identification | Activer et mettre à jour les paramètres de chiffrement au niveau des champs |
| Ressources de la bibliothèque multimédia | Voir les ressources de la bibliothèque multimédia | Consulter les ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Supprimer les ressources de la bibliothèque multimédia | Supprimer des ressources de la bibliothèque multimédia de l'interface. Les ressources supprimées restent hébergées par Braze pour éviter de casser les messages qui y font référence. Pour supprimer définitivement une ressource, contactez le support Braze. |
| Ressources de la bibliothèque multimédia | Modifier les ressources de la bibliothèque multimédia | Créer et mettre à jour les ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Remplacer les ressources de la bibliothèque multimédia | Remplacer le fichier d'une ressource existante de la bibliothèque multimédia tout en conservant son URL et son identifiant de ressource stables |
| Limites de débit des messages | Voir les limites de débit des messages | Consulter les limites de débit des messages au niveau de l'espace de travail |
| Limites de débit des messages | Modifier les limites de débit des messages | Configurer et modifier les limites de débit des messages au niveau de l'espace de travail |
| Operator | Utiliser BrazeAI<sup>TM</sup> Operator | Accéder et utiliser Braze Operator pour répondre à des questions, guider la configuration, résoudre des problèmes et proposer des idées |
| Placements | Voir les placements | Consulter les placements de bannière |
| Placements | Archiver les placements | Déplacer les placements de bannière dans les archives |
| Placements | Modifier les placements | Créer et mettre à jour les placements de bannière |
| Codes de promotion | Voir les codes de promotion | Consulter les codes de promotion |
| Codes de promotion | Exporter les codes de promotion | Télécharger une liste de codes de promotion depuis le tableau de bord |
| Codes de promotion | Modifier les codes de promotion | Créer et mettre à jour les codes de promotion |
| Groupes d'abonnement | Modifier les abonnements | Créer et mettre à jour les groupes d'abonnement |
| Transformations | Modifier les transformations de données | Créer et mettre à jour les transformations de données |
| Transformations | Voir les transformations de données | Consulter les transformations de données |
| Tickets de support | Créer un ticket de support | Créer et mettre à jour les tickets de support |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autres autorisations" }