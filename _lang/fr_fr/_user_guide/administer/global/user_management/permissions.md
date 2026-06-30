---
nav_title: Autorisations
article_title: Autorisations des utilisateurs de l'entreprise
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Cet article de référence explique le fonctionnement des autorisations utilisateur dans Braze. Vous y apprendrez comment modifier et définir les autorisations utilisateur, en choisissant qui peut accéder à vos applications dans le tableau de bord."
tool: Dashboard

---

# Autorisations Braze {#braze-permissions}

> Découvrez comment créer des ensembles d'autorisations, créer des rôles, modifier les autorisations utilisateur et exporter les autorisations utilisateur, afin de vous assurer que vos utilisateurs n'accèdent qu'aux espaces de travail et aux fonctionnalités dont ils ont le plus besoin.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Créer un ensemble d'autorisations {#create-a-permission-set}

Utilisez les ensembles d'autorisations pour regrouper les autorisations liées à des domaines ou des actions spécifiques. Vous pouvez appliquer des ensembles d'autorisations aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un ensemble d'autorisations, accédez à **Paramètres** > **Gestion des utilisateurs** > **Ensembles d'autorisations**, puis sélectionnez **Créer un ensemble d'autorisations**. Pour une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Exemples d'ensembles d'autorisations %}
| Nom | Autorisations |
|-----------|----------------|
| Développeurs | "View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger". |
| Marketeurs | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents". |
| Gestion des utilisateurs | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple d'ensemble d'autorisations" }
{% endtab %}
{% endtabs %}

## Créer un rôle {#creating-a-role}

Les rôles permettent de structurer davantage en regroupant vos autorisations personnalisées individuelles avec des contrôles d'accès aux espaces de travail. C'est particulièrement utile si vous avez plusieurs marques ou espaces de travail régionaux dans un même tableau de bord. Avec les rôles, vous pouvez ajouter des utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. Pour créer un rôle, accédez à **Paramètres** > **Gestion des utilisateurs** > **Rôles**, puis sélectionnez **Créer un rôle**. Pour une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Exemples de rôles %}
| Nom du rôle | Espace de travail | Autorisations |
| ----------- | ----------- | --------- |
| Marketeur - Marques de mode | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Marketeur - Marques de soins | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemples de rôles" }
{% endtab %}
{% endtabs %}

## Quelle est la différence entre les ensembles d'autorisations, les rôles et les équipes ? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Considérations pour l'ajout d'autorisations utilisateur aux équipes {#considerations-for-adding-user-permissions-to-teams}

Vous pouvez rencontrer des difficultés lorsque vous essayez d'enregistrer des autorisations dans le tableau de bord de Braze, notamment lors de l'ajout ou de la suppression d'utilisateurs d'un espace de travail, ou lors de leur ajout à une équipe. Le bouton **Enregistrer/Mettre à jour les utilisateurs** peut être grisé si les autorisations de l'utilisateur sont identiques à celles qu'il possède déjà au niveau de l'espace de travail. Cette restriction existe car il n'y a aucun avantage à avoir une équipe si tous les utilisateurs possèdent les mêmes autorisations que l'ensemble de l'espace de travail.

Pour ajouter un utilisateur à une équipe tout en conservant les mêmes autorisations, n'attribuez aucune autorisation au niveau de l'espace de travail. Attribuez plutôt les autorisations exclusivement au niveau de l'équipe.

## Utilisateurs limités {#limited-users}

Les utilisateurs limités disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze tout en ayant des restrictions par rapport aux administrateurs de l'entreprise et aux administrateurs d'espace de travail.

| Portée | Description |
| --- | --- |
| Autorisations | Les utilisateurs limités peuvent modifier les autorisations d'autres utilisateurs limités s'ils disposent de l'autorisation « Edit Dashboard Users ». Ils peuvent également créer de nouveaux utilisateurs limités et modifier leurs ensembles d'autorisations. Cependant, ils ne peuvent pas créer ni gérer des comptes d'administrateur d'entreprise. |
| Limitations des rôles | Si un utilisateur limité dispose de toutes les autorisations sauf « Workspace Admin », il aura tout de même accès à toutes les autres autorisations généralement accordées à un administrateur d'espace de travail. |
| Visibilité des autorisations | Si un utilisateur limité dispose de l'autorisation « Edit Dashboard Users » pour un espace de travail (tel que Dev) mais pas pour un autre (tel que Prod), il ne verra pas les autorisations de l'espace de travail Prod dans la page de détails des utilisateurs du tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autorisations pour les utilisateurs limités" }

### Comparer les utilisateurs limités {#compare-limited-users}

| Type d'utilisateur limité | Description |
| --- | --- |
| Administrateur d'espace de travail | Les administrateurs d'espace de travail disposent d'autorisations spécifiques à la gestion des espaces de travail, mais n'ont pas la même autorité que les administrateurs d'entreprise. Les utilisateurs limités peuvent hériter d'autorisations similaires à celles des administrateurs d'espace de travail s'ils disposent des autorisations nécessaires cochées. |
| Administrateur (administrateur d'entreprise) | Les administrateurs d'entreprise disposent d'autorisations plus larges, notamment la possibilité de supprimer des utilisateurs du tableau de bord. Cependant, ils ne peuvent pas supprimer leur propre compte et doivent contacter un autre administrateur d'entreprise pour cette action. |
| Accès en lecture seule | Pour accéder à certaines parties du tableau de bord, comme la page Campaigns, les utilisateurs doivent disposer des autorisations de consultation qui leur sont attribuées. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparaison des utilisateurs limités" }

### Erreur d'accès limité {#limited-access-error}

Les utilisateurs peuvent rencontrer des messages tels que « You need "View Landing Pages" permissions to access this page ». Dans ce cas, l'utilisateur et l'administrateur du compte doivent vérifier que les autorisations requises sont accordées. Si c'est le cas, essayez de résoudre le problème en désactivant puis en réactivant les autorisations de l'utilisateur.

{% alert note %}
Il n'est pas possible de fusionner ou d'importer les autorisations utilisateur d'un utilisateur du tableau de bord vers un autre.
{% endalert %}

## Nuances des autorisations utilisateur {#nuances-of-user-permissions}

Gardez les comportements suivants à l'esprit lorsque vous attribuez l'accès au tableau de bord :

- **Administrateur d'espace de travail et administrateur d'entreprise :** les administrateurs d'espace de travail gèrent les autorisations au sein des espaces de travail qui leur sont attribués. Les administrateurs d'entreprise disposent d'une autorité à l'échelle de l'entreprise, y compris la suppression d'autres utilisateurs du tableau de bord.
- **Utilisateurs limités :** les utilisateurs limités disposant de l'autorisation « Edit Dashboard Users » peuvent gérer d'autres utilisateurs limités, mais ne peuvent pas créer ni gérer des comptes d'administrateur d'entreprise.
- **Portée de la gestion des utilisateurs du tableau de bord :** sur la page de détails de l'utilisateur, les autorisations n'apparaissent que pour les espaces de travail auxquels l'éditeur peut accéder. Un utilisateur limité qui peut modifier les utilisateurs dans un espace de travail peut ne pas voir les cases à cocher des autorisations d'un autre espace de travail.
- **Exporter les données utilisateur :** l'exportation des données utilisateur nécessite un accès au niveau de l'espace de travail en plus de l'autorisation d'exportation.
- **Autorisations composites :** certaines zones nécessitent plusieurs autorisations. Par exemple, la configuration des [partenaires technologiques]({{site.baseurl}}/partners) nécessite généralement à la fois l'accès au partenaire et une autorisation de lecture de base pour les fonctionnalités de l'espace de travail concerné.
- **Importer et mettre à jour les données utilisateur :** cette autorisation inclut la possibilité de modifier les profils utilisateur de l'application via les flux d'importation, et pas seulement les enregistrements des utilisateurs du tableau de bord.

## Modifier les autorisations d'un utilisateur {#edit-a-users-permissions}

Pour modifier les autorisations actuelles d'un utilisateur (administrateur, entreprise ou espace de travail), accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, puis sélectionnez son nom.

![La page « Utilisateurs de l'entreprise » dans Braze affichant un tableau des utilisateurs du tableau de bord.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrateur %}

### Administrateur {#admin}

Les administrateurs ont accès à toutes les fonctionnalités et la possibilité de modifier tous les paramètres de l'entreprise. Ils peuvent :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow)
- Ajouter, modifier, supprimer, suspendre ou réactiver d'autres [utilisateurs Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users)
- Exporter les utilisateurs Braze au format CSV

Pour accorder ou retirer les privilèges d'administrateur, sélectionnez **This user is an admin**, puis sélectionnez **Update user**.

{% alert warning %}
Si vous retirez les privilèges d'administrateur d'un utilisateur, il ne pourra plus accéder à Braze tant que vous ne lui aurez pas attribué au moins une [autorisation au niveau de l'entreprise ou de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Entreprise %}

### Entreprise {#company}

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case à côté de cette autorisation. Lorsque vous avez terminé, sélectionnez **Update user**.

| Nom de l'autorisation | Description |
|----------|-----------|
| Manage company settings | Permet aux utilisateurs de modifier les paramètres d'autorisations et la vérification de l'expéditeur. |
| Create and delete workspaces | Permet aux utilisateurs de créer et de supprimer des espaces de travail. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autorisations au niveau de l'entreprise" }

{% endtab %}
{% tab Espace de travail %}

### Espace de travail {#workspace}

Vous pouvez attribuer à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer ses autorisations au niveau de l'espace de travail, sélectionnez **Select workspaces and permissions**, puis choisissez ses autorisations manuellement ou attribuez un [ensemble d'autorisations ou un rôle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que vous avez créé précédemment. Si vous devez attribuer à un utilisateur des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Sélection manuelle %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans le menu déroulant. Ensuite, sous **Permissions**, sélectionnez une ou plusieurs autorisations. Elles seront attribuées à l'utilisateur uniquement pour les espaces de travail que vous avez sélectionnés. Vous pouvez également sélectionner **Assign workspace admin access** si vous souhaitez lui accorder toutes les autorisations pour cet espace de travail.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail sélectionnées manuellement dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Attribuer un ensemble d'autorisations %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans le menu déroulant. Ensuite, sous **Permission Sets**, choisissez un ensemble d'autorisations. Elles seront attribuées à l'utilisateur uniquement pour les espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail attribuées via un ensemble d'autorisations dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Attribuer un rôle %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans le menu déroulant. Ensuite, sous **Role**, choisissez un rôle. Les autorisations correspondantes seront attribuées à l'utilisateur uniquement pour les espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail attribuées via un rôle dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporter les autorisations utilisateur {#exporting-user-permissions}

Pour télécharger une liste de vos utilisateurs et de leurs autorisations, accédez à **Paramètres** > **Gestion des utilisateurs** > **Utilisateurs de l'entreprise**, puis sélectionnez **Export Users**. Un fichier CSV sera envoyé à votre adresse e-mail sous peu.

## Liste des autorisations {#list-of-permissions}

### Envoi de messages {#messaging}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Campaigns | View Campaigns | Consulter les Campaigns |
| Campaigns | Launch Campaigns | Démarrer, arrêter, mettre en pause ou reprendre des Campaigns existantes |
| Campaigns | Archive Campaigns | Déplacer des Campaigns vers les archives |
| Campaigns | Edit Campaigns | Créer et mettre à jour des Campaigns |
| Campaigns | Approve and Deny Campaigns | Approuver ou refuser des Campaigns. Le [flux de travail d'approbation pour les Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement en accès anticipé. Contactez votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Canvas | View Canvases | Consulter les Canvas |
| Canvas | Archive Canvases | Déplacer des Canvas vers les archives |
| Canvas | Edit Canvases | Créer et mettre à jour des Canvas |
| Canvas | Launch Canvases | Démarrer, arrêter, mettre en pause ou reprendre des Canvas existants |
| Canvas | Approve and Deny Canvases | Approuver ou refuser des Canvas. Le [flux de travail d'approbation pour les Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement en accès anticipé. Contactez votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Indicateurs de fonctionnalité | View Feature Flags | Consulter les indicateurs de fonctionnalité |
| Indicateurs de fonctionnalité | Archive Feature Flags | Déplacer des indicateurs de fonctionnalité vers les archives |
| Indicateurs de fonctionnalité | Edit Feature Flags | Créer et mettre à jour des indicateurs de fonctionnalité |
| Limites de fréquence | View Frequency Capping Rules | Consulter les règles de limite de fréquence |
| Limites de fréquence | Edit Frequency Capping Rules | Créer et mettre à jour les règles de limite de fréquence |
| Pages d'accueil | View Landing Pages | Consulter les pages d'accueil |
| Pages d'accueil | Publish Landing Pages | Rendre active une page d'accueil en brouillon |
| Pages d'accueil | Edit Landing Page Drafts | Créer et enregistrer des brouillons de pages d'accueil |
| Paramètres d'archivage des messages | View Message Archiving Settings | Consulter les paramètres d'archivage des messages sans apporter de modifications |
| Paramètres d'archivage des messages | Edit Message Archiving Settings | Créer et mettre à jour les paramètres d'archivage des messages |
| Priorisation des messages | View Message Prioritization | Consulter les paramètres de priorisation des messages sans apporter de modifications |
| Priorisation des messages | Edit Message Prioritization | Créer et mettre à jour les paramètres de priorisation des messages |
| WhatsApp Flows | View WhatsApp Flows | Consulter tous les WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations d'envoi de messages" }

### Audience {#audience}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Groupe de contrôle global | View Global Control Group | Consulter la page de configuration du groupe de contrôle global |
| Groupe de contrôle global | Edit Global Control Group | Créer et enregistrer des modifications du groupe de contrôle global. Les utilisateurs disposant de l'autorisation « Edit Global Control Group » doivent également disposer des autorisations « Edit Campaigns » et « Edit Canvases ». Les utilisateurs disposant de l'autorisation « Edit Global Control Group » se voient également accorder l'autorisation « View Global Control Group ». |
| Emplacements | Archive Locations | Déplacer des emplacements vers les archives |
| Emplacements | View Locations | Consulter les emplacements |
| Emplacements | Edit Locations | Créer et modifier des emplacements |
| Segments | View Segments | Consulter les Segments. Les utilisateurs doivent disposer de l'autorisation « View Segments » pour avoir l'autorisation « Edit Segments » ou « Archive Segments » |
| Segments | Archive Segments | Archiver et désarchiver des Segments. Les utilisateurs disposant de l'autorisation « Archive Segments » doivent également disposer de l'autorisation « View Segments » |
| Segments | Edit Segments | Créer et mettre à jour des Segments. Les utilisateurs disposant de l'autorisation « Edit Segments » doivent également disposer de l'autorisation « View Segments » |
| Données utilisateur | View Import Users | Consulter les importations CSV d'utilisateurs sans apporter de modifications |
| Données utilisateur | Import Users | Importer des utilisateurs dans le tableau de bord |
| Données utilisateur | Edit User Data | Créer et mettre à jour les données utilisateur |
| Données utilisateur | Export User Data | Télécharger des utilisateurs depuis le tableau de bord |
| Utilisateurs en double | View User Merge Records | Consulter une liste des enregistrements de fusion d'utilisateurs |
| Utilisateurs | View User Profiles (PII Redacted) | Consulter les profils utilisateur de manière conforme aux données personnelles |
| Utilisateurs en double | Merge Duplicate Users | Combiner des utilisateurs en double en un seul utilisateur. Les doublons sont supprimés après la fusion |
| Suppression d'utilisateurs | View User Deletion Records | Consulter une liste des enregistrements de suppression d'utilisateurs |
| Suppression d'utilisateurs | Delete Users | Supprimer définitivement des utilisateurs du tableau de bord individuellement ou en masse |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations d'audience" }

### Modèle {#template}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Modèles de bannière | View Banner Templates | Consulter les modèles de bannière |
| Modèles de bannière | Archive Banner Templates | Déplacer des modèles de bannière vers les archives |
| Modèles de bannière | Edit Banner Templates | Créer et mettre à jour des modèles de bannière |
| Modèles de Canvas | View Canvas Templates | Consulter les modèles de Canvas |
| Modèles de Canvas | Archive Canvas Templates | Déplacer des modèles de Canvas vers les archives |
| Modèles de Canvas | Create and Edit Canvas Templates | Créer et mettre à jour des modèles de Canvas |
| Content Blocks | View Content Blocks | Consulter les Content Blocks |
| Content Blocks | Launch Content Blocks | Publier des brouillons de Content Blocks, et modifier, archiver et désarchiver des Content Blocks publiés |
| Content Blocks | Archive Content Blocks | Déplacer des Content Blocks vers les archives |
| Content Blocks | Edit Content Blocks | Créer des Content Blocks et modifier des brouillons de Content Blocks |
| Modèles de liens d'e-mail | View Email Link Templates | Consulter les modèles de liens sans apporter de modifications |
| Modèles de liens d'e-mail | Edit Email Link Templates | Créer et mettre à jour des modèles de liens |
| Modèles d'e-mail | View Email Templates | Consulter les modèles d'e-mail |
| Modèles d'e-mail | Archive Email Templates | Déplacer des modèles d'e-mail vers les archives |
| Modèles d'e-mail | Edit Email Templates | Créer et mettre à jour des modèles d'e-mail |
| Modèles de messages in-app | View IAM Templates | Consulter les modèles de messages in-app sans apporter de modifications |
| Modèles de messages in-app | Archive IAM Templates | Déplacer des modèles de messages in-app vers les archives |
| Modèles de messages in-app | Edit IAM Templates | Créer et mettre à jour des modèles de messages in-app |
| Modèles de page d'accueil | View Landing Page Templates | Consulter les modèles de page d'accueil |
| Modèles de page d'accueil | Archive Landing Page Template | Déplacer des modèles de page d'accueil vers les archives |
| Modèles de page d'accueil | Edit Landing Page Templates | Créer et mettre à jour des modèles de page d'accueil |
| Modèles de webhook | View Webhook Templates | Consulter les modèles de webhook sans apporter de modifications |
| Modèles de webhook | Archive Webhook Templates | Déplacer des modèles de webhook vers les archives |
| Modèles de webhook | Edit Webhook Templates | Créer et mettre à jour des modèles de webhook |
| Modèles de messages WhatsApp | View WhatsApp Message Templates | Permet aux utilisateurs de consulter les [modèles de messages WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) |
| Modèles de messages WhatsApp | Edit WhatsApp Message Templates | Permet aux utilisateurs de créer des modèles de messages WhatsApp dans le générateur de modèles. Cette fonctionnalité est actuellement en accès anticipé. |
| Modèles de messages WhatsApp depuis Meta | View WhatsApp Message Templates From Meta | Consulter tous les modèles WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations de modèles" }

### Intégrations partenaires {#partner-integrations}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Intégrations Currents | View Currents Integration | Consulter les intégrations Currents |
| Intégrations Currents | Edit Currents Integrations | Créer, mettre à jour et supprimer des intégrations Currents |
| Partenaires technologiques | Edit Technology Partners | Créer et mettre à jour des partenaires technologiques |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations d'intégrations partenaires" }

### Paramètres des données {#data-settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Catalogues | View Catalogs | Consulter les catalogues et les sélections |
| Catalogues | Delete Catalogs | Supprimer définitivement des catalogues |
| Catalogues | Export Catalogs | Télécharger des catalogues depuis le tableau de bord |
| Catalogues | Edit Catalogs | Créer et mettre à jour des catalogues et des sélections |
| Ingestion de données cloud | Edit Cloud Data Ingestion | Créer, mettre à jour et supprimer des sources et des synchronisations |
| Attributs personnalisés | View Custom Attributes | Consulter les attributs personnalisés et le rapport d'utilisation |
| Attributs personnalisés | Export Custom Attributes | Télécharger des attributs personnalisés depuis le tableau de bord |
| Attributs personnalisés | Delete Custom Attributes | Supprimer définitivement des attributs personnalisés |
| Attributs personnalisés | Blocklist Custom Attributes | Ajouter des attributs personnalisés à une liste de blocage qui restreint leur utilisation dans le tableau de bord |
| Attributs personnalisés | Edit Custom Attributes | Créer et mettre à jour des attributs personnalisés |
| Segmentation par propriétés d'événement personnalisé | Edit Custom Event Property Segmentation | Activer et désactiver la segmentation pour les propriétés d'événement personnalisé |
| Événements personnalisés | View Custom Events | Consulter les événements personnalisés et le rapport d'utilisation, et ajouter des événements personnalisés à l'e-mail de rapport d'analyse quotidien |
| Événements personnalisés | Export Custom Events | Télécharger des événements personnalisés depuis le tableau de bord |
| PII | View PII | Consulter les données personnelles |
| Événements personnalisés | Delete Custom Events | Supprimer définitivement des événements personnalisés |
| Événements personnalisés | Blocklist Custom Events | Ajouter des événements personnalisés à une liste de blocage qui restreint leur utilisation dans le tableau de bord |
| Événements personnalisés | Edit Custom Events | Créer et mettre à jour des événements personnalisés |
| Produits | View Products | Consulter les produits |
| Produits | Blocklist Products | Ajouter des produits à une liste de blocage qui restreint leur utilisation dans le tableau de bord |
| Produits | Edit Products | Créer et mettre à jour des produits |
| Segmentation par propriétés d'achat | Edit Purchase Property Segmentation | Activer et désactiver la segmentation pour les propriétés d'événement d'achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations des paramètres de données" }

### Paramètres {#settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Identifiants API | View API identifiers | Consulter les identifiants API et autres identifiants |
| Clés API | View API Keys | Consulter les clés API |
| Clés API | Edit API Keys | Créer et mettre à jour des clés API |
| Limites API | View API Limits | Consulter les limites de débit API |
| Alertes d'utilisation API | View API Usage Alerts | Consulter les alertes d'utilisation API |
| Alertes d'utilisation API | Edit API Usage Alerts | Créer et mettre à jour les alertes d'utilisation API |
| Données d'utilisation API | View API Usage Dashboard | Consulter le tableau de bord d'utilisation API |
| Paramètres des applications | Edit App Settings | Créer, modifier et mettre à jour des applications dans les paramètres des applications |
| Paramètres des applications | View App Settings | Consulter la page des paramètres des applications |
| Paramètres Audience Sync | View Audience Sync Settings | Consulter tous les paramètres de leurs partenaires Audience Sync connectés |
| Utilisateurs du tableau de bord | Edit Dashboard Users | Consulter, créer et modifier les utilisateurs de l'entreprise |
| Paramètres des e-mails | View Email Settings | Consulter les préférences des e-mails |
| Paramètres des e-mails | Edit Email Settings | Activer et mettre à jour les préférences des e-mails |
| Journal des événements utilisateur | View Event User Log | Consulter les journaux des événements utilisateur |
| Groupes internes | View Internal User Groups | Consulter les groupes internes |
| Groupes internes | Delete Internal User Groups | Supprimer des groupes internes |
| Groupes internes | Edit Internal User Groups | Créer et mettre à jour des groupes internes |
| Journal d'activité des messages | View Message Activity Log | Consulter les journaux d'activité des messages |
| Paramètres multilingues | View Localization Settings | Consulter la page des paramètres de localisation multilingue |
| Paramètres multilingues | Delete Localization Settings | Supprimer une localisation multilingue |
| Paramètres multilingues | Edit Localization Settings | Créer des localisations multilingues |
| Centres de préférences | View Preference Centers | Consulter les centres de préférences |
| Centres de préférences | Edit Preference Centers | Créer et mettre à jour des centres de préférences |
| Centres de préférences | Launch Preference Centers | Rendre actif un brouillon de centre de préférences ou mettre à jour un centre existant |
| Paramètres de notifications push | View Push Settings | Consulter les paramètres de notifications push |
| Paramètres de notifications push | Edit Push Settings | Créer et mettre à jour les paramètres de notifications push |
| Outil de débogage du SDK | View SDK Debugger | Consulter l'outil de débogage du SDK ou les sessions de débogage |
| Outil de débogage du SDK | Edit SDK Debugger | Créer et télécharger des sessions de l'outil de débogage du SDK |
| Étiquettes | View Tags | Consulter les étiquettes |
| Étiquettes | Delete Tags | Supprimer définitivement des étiquettes |
| Étiquettes | Edit Tags | Créer et mettre à jour des étiquettes |
| Équipes | View Teams | Consulter les équipes |
| Équipes | Archive Teams | Déplacer des équipes vers les archives |
| Équipes | Edit Teams | Créer et mettre à jour des équipes |
| Paramètres WhatsApp | View WhatsApp Settings | Consulter tous les paramètres du canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations des paramètres" }

### Decisioning Studio

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Agents Decisioning Studio | View Decisioning Studio Agent | Consulter la configuration des agents Decisioning Studio sans apporter de modifications |
| Audience Decisioning Studio | View Decisioning Studio Audience | Consulter les détails de l'audience dans les résumés de configuration des agents Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisations Decisioning Studio" }

### Autres {#other}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Utilisation de l'application | View Usage Data | Consulter les données d'utilisation |
| Facturation | View Billing Details | Consulter les détails de facturation |
| Agents personnalisés | View Agent Console AI Agents | Permet aux utilisateurs de consulter les agents IA personnalisés |
| Agents personnalisés | Archive Agent Console AI Agents | Permet aux utilisateurs d'archiver les agents IA personnalisés |
| Agents personnalisés | Edit Agent Console AI Agents | Permet aux utilisateurs de créer et de mettre à jour les agents IA personnalisés |
| Attributs personnalisés marqués comme PII | View Custom Attributes Marked as PII | Consulter les attributs personnalisés marqués comme données personnelles |
| Rapports du tableau de bord | View Dashboard Reports | Consulter les rapports sans apporter de modifications |
| Rapports du tableau de bord | Delete Dashboard Reports | Supprimer définitivement des rapports |
| Rapports du tableau de bord | Edit Dashboard Reports | Créer et mettre à jour des rapports |
| Paramètres de domaine | Edit Domain Settings | Ajouter des domaines délégués et des domaines personnalisés sous les domaines vérifiés |
| Chiffrement au niveau des champs | Edit Identifier Field-Level Encryption | Activer et mettre à jour les paramètres de chiffrement au niveau des champs |
| Ressources de la bibliothèque multimédia | View Media Library Assets | Consulter les ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Delete Media Library Assets | Supprimer définitivement des ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Edit Media Library Assets | Créer et mettre à jour des ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Replace Media Library Assets | Remplacer le fichier d'une ressource existante de la bibliothèque multimédia tout en conservant son URL et son ID de ressource |
| Limites de débit des messages | View Messaging Rate Limits | Consulter les limites de débit des messages au niveau de l'espace de travail |
| Limites de débit des messages | Edit Messaging Rate Limits | Configurer et modifier les limites de débit des messages au niveau de l'espace de travail |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Accéder à BrazeAI Operator et l'utiliser pour répondre à des questions, guider la configuration, résoudre des problèmes et trouver des idées |
| Placements | View Placements | Consulter les placements de bannière |
| Placements | Archive Placements | Déplacer des placements de bannière vers les archives |
| Placements | Edit Placements | Consulter les placements de bannière sans apporter de modifications |
| Codes de promotion | View Promotion Codes | Consulter les codes de promotion |
| Codes de promotion | Export Promotion Codes | Télécharger une liste de codes de promotion depuis le tableau de bord |
| Codes de promotion | Edit Promotion Codes | Créer et mettre à jour des codes de promotion |
| Groupes d'abonnement | Edit Subscriptions | Créer et mettre à jour des groupes d'abonnement |
| Transformations | Edit Data Transformation | Créer et mettre à jour des transformations de données |
| Transformations | View Data Transformation | Consulter les transformations de données |
| Tickets d'assistance | Create Support Ticket | Créer et mettre à jour des tickets d'assistance |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autres autorisations" }