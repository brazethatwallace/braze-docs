{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

{% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Création d'un ensemble d'autorisations {#creating-a-permission-set}

Utilisez les ensembles d'autorisations pour regrouper les autorisations liées à des domaines ou actions spécifiques. Vous pouvez appliquer ces ensembles aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un ensemble d'autorisations, accédez à **Paramètres** > **Paramètres des autorisations**, puis sélectionnez **Créer un ensemble d'autorisations**. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab Exemples d'ensembles d'autorisations %}
| Nom | Autorisations |
|-----------|----------------|
| Développeurs | "Afficher les clés API", "Modifier les clés API", "Afficher les groupes internes", "Modifier les groupes internes", "Afficher le journal d'activité des messages", "Afficher le journal des événements utilisateurs", "Afficher les identifiants API", "Afficher le tableau de bord d'utilisation de l'API", "Afficher les limites de l'API", "Afficher les alertes d'utilisation de l'API", "Modifier les alertes d'utilisation de l'API", "Afficher le débogueur SDK", "Modifier le débogueur SDK". |
| Marketeurs | "Afficher les campagnes", "Modifier les campagnes", "Archiver les campagnes", "Afficher les Canvas", "Modifier les Canvas", "Archiver les Canvas", "Afficher les règles de limite de fréquence", "Modifier les règles de limite de fréquence", "Afficher la priorisation des messages", "Modifier la priorisation des messages", "Afficher les Content Blocks", "Afficher les indicateurs de fonctionnalité", "Modifier les indicateurs de fonctionnalité", "Archiver les indicateurs de fonctionnalité", "Afficher les segments", "Modifier les segments", "Modifier le groupe de contrôle global", "Afficher les modèles IAM", "Modifier les modèles IAM", "Archiver les modèles IAM", "Afficher les modèles d'e-mail", "Modifier les modèles d'e-mail", "Archiver les modèles d'e-mail", "Afficher les modèles de webhook", "Modifier les modèles de webhook", "Archiver les modèles de webhook", "Afficher les modèles de liens d'e-mail", "Modifier les modèles de liens d'e-mail", "Afficher les ressources de la bibliothèque multimédia", "Afficher les emplacements", "Modifier les emplacements", "Archiver les emplacements", "Afficher les codes de promotion", "Modifier les codes de promotion", "Exporter les codes de promotion", "Afficher les centres de préférences", "Modifier les centres de préférences", "Modifier les rapports du tableau de bord", "Afficher les modèles de bannières", "Afficher les paramètres de localisation", "Utiliser l'opérateur", "Afficher les agents Decisioning Studio". |
| Gestion des utilisateurs | "Modifier les utilisateurs du tableau de bord", "Afficher les équipes", "Modifier les équipes", "Archiver les équipes". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Création d'un ensemble d'autorisations" }
{% endtab %}
{% endtabs %}

## Création d'un rôle {#creating-a-role}

Les rôles offrent une meilleure structuration en regroupant vos autorisations personnalisées avec les contrôles d'accès aux espaces de travail. C'est particulièrement utile lorsque vous gérez plusieurs marques ou espaces de travail régionaux dans un même tableau de bord. Grâce aux rôles, vous pouvez ajouter les utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab Exemples de rôles %}
| Nom du rôle    | Espace de travail | Autorisations
----------- | ----------- | ---------
| Marketeur - Marques de mode | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "Afficher les campagnes", "Modifier les campagnes", "Archiver les campagnes", "Afficher les Canvas", "Modifier les Canvas", "Archiver les Canvas", "Afficher les Content Blocks", "Modifier les Content Blocks", "Archiver les Content Blocks", "Lancer les Content Blocks", "Afficher les indicateurs de fonctionnalité", "Modifier les indicateurs de fonctionnalité", "Archiver les indicateurs de fonctionnalité", "Afficher les segments", "Modifier les segments", "Afficher les modèles de bannières", "Modifier les modèles de bannières", "Afficher les modèles d'e-mail", "Modifier les modèles d'e-mail", "Afficher les ressources de la bibliothèque multimédia", "Modifier les ressources de la bibliothèque multimédia", "Supprimer les ressources de la bibliothèque multimédia", "Afficher les emplacements", "Modifier les emplacements", "Archiver les emplacements", "Afficher les codes de promotion", "Modifier les codes de promotion", "Exporter les codes de promotion", "Afficher les centres de préférences", "Modifier les centres de préférences". |
| Marketeur - Marques de soins de la peau | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Afficher les campagnes", "Modifier les campagnes", "Archiver les campagnes", "Afficher les Canvas", "Modifier les Canvas", "Archiver les Canvas", "Afficher les Content Blocks", "Modifier les Content Blocks", "Archiver les Content Blocks", "Lancer les Content Blocks", "Afficher les indicateurs de fonctionnalité", "Modifier les indicateurs de fonctionnalité", "Archiver les indicateurs de fonctionnalité", "Afficher les segments", "Modifier les segments", "Afficher les modèles de bannières", "Modifier les modèles de bannières", "Afficher les modèles d'e-mail", "Modifier les modèles d'e-mail", "Afficher les ressources de la bibliothèque multimédia", "Modifier les ressources de la bibliothèque multimédia", "Supprimer les ressources de la bibliothèque multimédia", "Afficher les emplacements", "Modifier les emplacements", "Archiver les emplacements", "Afficher les codes de promotion", "Modifier les codes de promotion", "Exporter les codes de promotion", "Afficher les centres de préférences", "Modifier les centres de préférences". |
| Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Modifier les utilisateurs du tableau de bord", "Afficher les équipes", "Modifier les équipes", "Archiver les équipes" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Création d'un rôle" }
{% endtab %}
{% endtabs %}

## Quelle est la différence entre les ensembles d'autorisations, les rôles et les Teams ? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions.md content="Differences" %}

### Points à considérer lors de l'ajout d'autorisations utilisateur aux Teams {#considerations-for-adding-user-permissions-to-teams}

Vous pourriez rencontrer des difficultés en essayant d'enregistrer les autorisations dans le tableau de bord de Braze, notamment lorsque vous ajoutez ou supprimez des utilisateurs d'un espace de travail, ou lorsque vous les ajoutez à une équipe. Le bouton **Enregistrer/Mettre à jour les utilisateurs** peut apparaître grisé si les autorisations de l'utilisateur sont identiques à celles dont il dispose déjà au niveau de l'espace de travail. Cette restriction existe car il n'y a aucun intérêt à utiliser des Teams si tous les utilisateurs possèdent les mêmes autorisations que l'ensemble de l'espace de travail.

Pour ajouter un utilisateur à une Team tout en conservant les mêmes autorisations, n'attribuez aucune autorisation au niveau de l'espace de travail. Attribuez-les exclusivement au niveau de l'équipe.

## Utilisateurs limités {#limited-users}

Les utilisateurs limités disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze, tout en étant soumis à des restrictions par rapport aux administrateurs d'entreprise et aux administrateurs d'espace de travail.

| Portée | Description |
| --- | --- |
| Autorisations | Les utilisateurs limités peuvent modifier les autorisations d'autres utilisateurs limités s'ils disposent de l'autorisation « Modifier les utilisateurs du tableau de bord ». Ils peuvent également créer de nouveaux utilisateurs limités et modifier leurs ensembles d'autorisations. En revanche, ils ne peuvent pas créer ni gérer de comptes administrateur d'entreprise. |
| Limitations de rôle | Si un utilisateur limité dispose de toutes les autorisations sauf « Administrateur de l'espace de travail », il conserve l'accès à toutes les autres autorisations généralement accordées à un administrateur d'espace de travail. |
| Visibilité des autorisations | Si un utilisateur limité dispose de l'autorisation « Modifier les utilisateurs du tableau de bord » pour un espace de travail (par exemple Dev) mais pas pour un autre (par exemple Prod), il ne verra pas les autorisations de l'espace de travail Prod dans la page de détails des utilisateurs de son tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Utilisateurs limités" }

### Comparaison des types d'utilisateurs limités {#comparing-limited-users}

| Type d'utilisateur limité | Description |
| --- | --- |
| Administrateur de l'espace de travail | Les administrateurs d'espace de travail disposent d'autorisations spécifiques à la gestion des espaces de travail, mais n'ont pas les mêmes prérogatives que les administrateurs d'entreprise. Les utilisateurs limités peuvent hériter d'autorisations similaires à celles des administrateurs d'espace de travail s'ils disposent des autorisations nécessaires. |
| Administrateur (administrateur d'entreprise) | Les administrateurs d'entreprise disposent d'autorisations plus étendues, notamment la possibilité de supprimer des utilisateurs du tableau de bord. Cependant, ils ne peuvent pas supprimer leur propre compte et doivent contacter un autre administrateur d'entreprise pour cette action. |
| Accès en lecture seule | Pour accéder à certaines parties du tableau de bord, comme la page Campaigns, les utilisateurs doivent disposer des autorisations de consultation correspondantes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparaison des types d'utilisateurs limités" }

### Erreur d'accès restreint {#limited-access-error}

Les utilisateurs peuvent rencontrer des messages tels que « Vous devez disposer de l'autorisation "Afficher les pages d'accueil" pour accéder à cette page ». Dans ce cas, l'utilisateur et l'administrateur du compte doivent vérifier que les autorisations requises sont bien accordées. Si c'est le cas, essayez de résoudre le problème en désactivant puis en réactivant les autorisations de l'utilisateur.

{% alert note %}
Il n'est pas possible de fusionner ou d'importer les autorisations d'un utilisateur du tableau de bord vers un autre.
{% endalert %}

## Modifier les autorisations d'un utilisateur {#editing-a-users-permissions}

Pour modifier les autorisations actuelles d'un utilisateur (administrateur, entreprise ou espace de travail), accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez son nom.

![La page « Utilisateurs de l'entreprise » dans Braze affichant un tableau des utilisateurs du tableau de bord.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrateur %}

### Administrateur {#admin}

Les administrateurs ont accès à toutes les fonctionnalités et peuvent modifier tous les paramètres de l'entreprise. Ils peuvent :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/messaging/governance/approvals/#turning-on-the-approval-workflow)
- Ajouter, modifier, supprimer, suspendre ou réactiver d'autres [utilisateurs de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#adding-company-users)
- Exporter les utilisateurs de Braze au format CSV

Pour accorder ou retirer les privilèges d'administrateur, sélectionnez **This user is an admin**, puis sélectionnez **Update user**.


{% alert warning %}
Si vous retirez les privilèges d'administrateur à un utilisateur, celui-ci ne pourra plus accéder à Braze tant que vous ne lui aurez pas attribué au moins une [autorisation au niveau de l'entreprise ou de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Entreprise %}

### Entreprise {#company}

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case correspondante. Lorsque vous avez terminé, sélectionnez **Update user**.

| Nom de l'autorisation | Description |
|----------|-----------|
| Gérer les paramètres de l'entreprise | Permet aux utilisateurs de modifier les paramètres d'autorisation et la vérification de l'expéditeur. |
| Créer et supprimer des espaces de travail | Permet aux utilisateurs de créer et de supprimer des espaces de travail. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entreprise" }

{% endtab %}
{% tab Espace de travail %}

### Espace de travail {#workspace}

Vous pouvez attribuer à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer les autorisations au niveau de l'espace de travail, sélectionnez **Select workspaces and permissions**, puis choisissez les autorisations manuellement ou attribuez un [ensemble d'autorisations ou un rôle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que vous avez précédemment créé. Si vous devez attribuer des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Sélection manuelle %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Permissions**, sélectionnez une ou plusieurs autorisations. Elles ne seront attribuées que pour les espaces de travail sélectionnés. Vous pouvez également sélectionner **Assign workspace admin access** si vous souhaitez accorder toutes les autorisations pour cet espace de travail.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail sélectionnées manuellement dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Attribuer un ensemble d'autorisations %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Permission Sets**, choisissez un ensemble d'autorisations. Ces autorisations ne seront attribuées que pour les espaces de travail sélectionnés.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail attribuées via un ensemble d'autorisations dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Attribuer un rôle %}

Sous **Workspaces**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Role**, sélectionnez un rôle. Ces autorisations ne seront attribuées que pour les espaces de travail sélectionnés.

Lorsque vous avez terminé, sélectionnez **Update user**.

![Autorisations au niveau de l'espace de travail attribuées via un rôle dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporter les autorisations des utilisateurs {#exporting-user-permissions}

Pour télécharger la liste de vos utilisateurs et de leurs autorisations, accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez **Export Users**. Un fichier CSV sera envoyé à votre adresse e-mail sous peu.

![La page « Utilisateurs de l'entreprise » dans Braze avec l'option « Export Users » mise en évidence.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

Il n'est pas possible d'exporter en masse une matrice complète des autorisations de chaque utilisateur du tableau de bord depuis Braze. Si vous avez besoin de plus de détails que ce que fournit **Export Users**, envisagez les options suivantes :

- Utilisez le [provisionnement automatisé des utilisateurs]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/) (SCIM) pour gérer les comptes des utilisateurs du tableau de bord. Par exemple, vous pouvez [rechercher un utilisateur du tableau de bord par e-mail]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user/) ou obtenir les détails d'un utilisateur par identifiant de ressource, comme décrit dans [Consulter les informations d'un compte utilisateur]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/).
- [Contactez l'assistance Braze]({{site.baseurl}}/braze_support/). Dans certains cas, l'assistance peut fournir une liste de comptes, mais pas une matrice complète des autorisations.
- Filtrez le [rapport d'événements de sécurité]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report) de votre entreprise, qui enregistre des événements tels que **Added Account** et **Updated Permissions**, pour auditer les modifications d'autorisations en dehors du tableau de bord.

## Liste des autorisations {#list-of-permissions}

### Envoi de messages {#messaging}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Campaigns | Afficher les campagnes | Afficher les campagnes |
| Campaigns | Lancer les campagnes | Lancer, arrêter, suspendre ou reprendre des campagnes existantes |
| Campaigns | Archiver les campagnes | Déplacer les campagnes vers les archives |
| Campaigns | Modifier les campagnes | Créer et mettre à jour des campagnes |
| Campaigns | Approuver et refuser les campagnes | Approuver ou refuser les campagnes. Le [flux de travail d'approbation des campagnes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement disponible en accès anticipé. Contactez votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Canvas | Afficher les Canvas | Afficher les Canvas |
| Canvas | Archiver les Canvas | Déplacer les Canvas vers les archives |
| Canvas | Modifier les Canvas | Créer et mettre à jour des Canvas |
| Canvas | Lancer les Canvas | Lancer, arrêter, suspendre ou reprendre des Canvas existants |
| Canvas | Approuver et refuser les Canvas | Approuver ou refuser les Canvas. Le [flux de travail d'approbation des Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement disponible en accès anticipé. Contactez votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Indicateurs de fonctionnalité | Afficher les indicateurs de fonctionnalité | Afficher les indicateurs de fonctionnalité |
| Indicateurs de fonctionnalité | Archiver les indicateurs de fonctionnalité | Déplacer les indicateurs de fonctionnalité vers les archives |
| Indicateurs de fonctionnalité | Modifier les indicateurs de fonctionnalité | Créer et mettre à jour des indicateurs de fonctionnalité |
| Limites de fréquence | Afficher les règles de limite de fréquence | Afficher les règles de limite de fréquence |
| Limites de fréquence | Modifier les règles de limite de fréquence | Créer et mettre à jour les règles de limite de fréquence |
| Pages d'accueil | Afficher les pages d'accueil | Afficher les pages d'accueil |
| Pages d'accueil | Publier les pages d'accueil | Rendre active une page d'accueil en brouillon |
| Pages d'accueil | Modifier les brouillons de pages d'accueil | Créer et enregistrer des brouillons de pages d'accueil |
| Paramètres d'archivage des messages | Afficher les paramètres d'archivage des messages | Consulter les paramètres d'archivage des messages sans apporter de modifications |
| Paramètres d'archivage des messages | Modifier les paramètres d'archivage des messages | Créer et mettre à jour les paramètres d'archivage des messages |
| Priorisation des messages | Afficher la priorisation des messages | Consulter les paramètres de priorisation des messages sans apporter de modifications |
| Priorisation des messages | Modifier la priorisation des messages | Créer et mettre à jour les paramètres de priorisation des messages |
| WhatsApp Flows | Afficher les WhatsApp Flows | Afficher tous les WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Envoi de messages" }

### Audience

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Groupe de contrôle global | Afficher le groupe de contrôle global | Consulter la page de configuration du groupe de contrôle global |
| Groupe de contrôle global | Modifier le groupe de contrôle global | Créer et enregistrer les modifications apportées au groupe de contrôle global. Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » doivent également disposer des autorisations « Modifier les campagnes » et « Modifier les Canvas ». Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » se voient également accorder l'autorisation « Afficher le groupe de contrôle global ». |
| Emplacements | Archiver les emplacements | Déplacer les emplacements vers les archives |
| Emplacements | Afficher les emplacements | Afficher les emplacements |
| Emplacements | Modifier les emplacements | Créer et modifier des emplacements |
| Segments | Afficher les segments | Afficher les segments. Les utilisateurs doivent disposer de l'autorisation « Afficher les segments » pour pouvoir bénéficier des autorisations « Modifier les segments » ou « Archiver les segments ». |
| Segments | Archiver les segments | Archiver et désarchiver des segments. Les utilisateurs disposant de l'autorisation « Archiver les segments » doivent également se voir accorder l'autorisation « Afficher les segments ». |
| Segments | Modifier les segments | Créer et mettre à jour des segments. Les utilisateurs disposant de l'autorisation « Modifier les segments » doivent également se voir accorder l'autorisation « Afficher les segments ». |
| Données utilisateur | Afficher les importations d'utilisateurs | Afficher les importations d'utilisateurs CSV sans apporter de modifications |
| Données utilisateur | Importer des utilisateurs | Importer des utilisateurs dans le tableau de bord |
| Données utilisateur | Modifier les données utilisateur | Créer et mettre à jour les données utilisateur |
| Données utilisateur | Exporter les données utilisateur | Télécharger les utilisateurs depuis le tableau de bord |
| Enregistrements de fusion d'utilisateurs | Afficher les enregistrements de fusion d'utilisateurs | Consulter la liste des enregistrements de fusion d'utilisateurs |
| Utilisateurs | Voir les profils utilisateur (PII expurgées) | Consulter les profils utilisateur de manière conforme aux PII |
| Utilisateurs en double | Fusionner les utilisateurs en double | Combiner les utilisateurs en double en un seul utilisateur. Les doublons sont supprimés après la fusion. |
| Utilisateurs | Supprimer les utilisateurs | Supprimer définitivement les utilisateurs du tableau de bord individuellement ou en masse |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience" }

### Modèles {#template}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Modèles de bannières | Afficher les modèles de bannières | Consulter les modèles de bannières |
| Modèles de bannières | Archiver les modèles de bannières | Déplacer les modèles de bannières vers les archives |
| Modèles de bannières | Modifier les modèles de bannières | Créer et mettre à jour des modèles de bannières |
| Modèles Canvas | Afficher les modèles Canvas | Consulter les modèles Canvas |
| Modèles Canvas | Archiver les modèles Canvas | Déplacer les modèles Canvas vers les archives |
| Modèles Canvas | Créer et modifier les modèles Canvas | Créer et mettre à jour des modèles Canvas |
| Content Blocks | Afficher les Content Blocks | Afficher les Content Blocks |
| Content Blocks | Lancer les Content Blocks | Publier les brouillons de Content Blocks, et modifier, archiver et désarchiver les Content Blocks publiés |
| Content Blocks | Archiver les Content Blocks | Déplacer les Content Blocks vers les archives |
| Content Blocks | Modifier les Content Blocks | Créer des Content Blocks et modifier les brouillons de Content Blocks |
| Modèles de liens d'e-mail | Afficher les modèles de liens d'e-mail | Consulter les modèles de liens sans apporter de modifications |
| Modèles de liens d'e-mail | Modifier les modèles de liens d'e-mail | Créer et mettre à jour des modèles de liens |
| Modèles d'e-mail | Afficher les modèles d'e-mail | Consulter les modèles d'e-mail |
| Modèles d'e-mail | Archiver les modèles d'e-mail | Déplacer les modèles d'e-mail vers les archives |
| Modèles d'e-mail | Modifier les modèles d'e-mail | Créer et mettre à jour des modèles d'e-mail |
| Modèles IAM | Afficher les modèles IAM | Consulter les modèles de messages in-app sans apporter de modifications |
| Modèles IAM | Archiver les modèles IAM | Déplacer les modèles IAM vers les archives |
| Modèles IAM | Modifier les modèles IAM | Créer et mettre à jour des modèles de messages in-app |
| Modèles de pages d'accueil | Afficher les modèles de pages d'accueil | Consulter les modèles de pages d'accueil |
| Modèles de pages d'accueil | Archiver les modèles de pages d'accueil | Déplacer les modèles de pages d'accueil vers les archives |
| Modèles de pages d'accueil | Modifier les modèles de pages d'accueil | Créer et mettre à jour des modèles de pages d'accueil |
| Modèles de webhook | Afficher les modèles de webhook | Consulter les modèles de webhook sans apporter de modifications |
| Modèles de webhook | Archiver les modèles de webhook | Déplacer les modèles de webhook vers les archives |
| Modèles de webhook | Modifier les modèles de webhook | Créer et mettre à jour des modèles de webhook |
| Modèles de messages WhatsApp | Afficher les modèles de messages WhatsApp | Permet aux utilisateurs de visualiser les [modèles de messages WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message) |
| Modèles de messages WhatsApp | Modifier les modèles de messages WhatsApp | Permet aux utilisateurs de créer des modèles de messages WhatsApp dans le générateur de modèles. Cette fonctionnalité est actuellement disponible en accès anticipé. |
| Modèles de messages WhatsApp depuis Meta | Afficher les modèles de messages WhatsApp depuis Meta | Afficher tous les modèles WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modèles" }

### Intégrations partenaires {#partner-integrations}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Intégrations Currents | Afficher les intégrations Currents | Consulter les intégrations Currents |
| Intégrations Currents | Modifier les intégrations Currents | Créer, mettre à jour et supprimer des intégrations Currents |
| Partenaires technologiques | Modifier les partenaires technologiques | Créer et mettre à jour les partenaires technologiques |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Intégrations partenaires" }

### Paramètres des données {#data-settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Catalogues | Afficher les catalogues | Consulter les catalogues et les sélections |
| Catalogues | Supprimer les catalogues | Supprimer définitivement les catalogues |
| Catalogues | Exporter les catalogues | Télécharger les catalogues depuis le tableau de bord |
| Catalogues | Modifier les catalogues | Créer et mettre à jour des catalogues et des sélections |
| Ingestion de données cloud | Modifier l'ingestion de données cloud | Créer, mettre à jour et supprimer des sources et des synchronisations |
| Attributs personnalisés | Afficher les attributs personnalisés | Consulter les attributs personnalisés et le rapport d'utilisation |
| Attributs personnalisés | Exporter les attributs personnalisés | Télécharger les attributs personnalisés depuis le tableau de bord |
| Attributs personnalisés | Supprimer les attributs personnalisés | Supprimer définitivement les attributs personnalisés |
| Attributs personnalisés | Ajouter les attributs personnalisés à la liste de blocage | Ajouter des attributs personnalisés à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Attributs personnalisés | Modifier les attributs personnalisés | Créer et mettre à jour des attributs personnalisés |
| Segmentation des propriétés d'événements personnalisés | Modifier la segmentation des propriétés d'événements personnalisés | Activer et désactiver la segmentation pour les propriétés d'événements personnalisés |
| Événements personnalisés | Afficher les événements personnalisés | Consulter les événements personnalisés et le rapport d'utilisation, et ajouter des événements personnalisés au rapport analytique quotidien envoyé par e-mail |
| Événements personnalisés | Exporter les événements personnalisés | Télécharger les événements personnalisés depuis le tableau de bord |
| PII | Afficher les PII | Afficher les PII |
| Événements personnalisés | Supprimer les événements personnalisés | Supprimer définitivement les événements personnalisés |
| Événements personnalisés | Ajouter les événements personnalisés à la liste de blocage | Ajouter des événements personnalisés à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Événements personnalisés | Modifier les événements personnalisés | Créer et mettre à jour des événements personnalisés |
| Produits | Afficher les produits | Consulter les produits |
| Produits | Ajouter les produits à la liste de blocage | Ajouter des produits à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Produits | Modifier les produits | Créer et mettre à jour des produits |
| Segmentation des propriétés d'achat | Modifier la segmentation des propriétés d'achat | Activer et désactiver la segmentation pour les propriétés d'événements d'achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres des données" }

### Paramètres {#settings}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Identifiants API | Afficher les identifiants API | Afficher les identifiants API et autres identifiants |
| Clés API | Afficher les clés API | Afficher les clés API |
| Clés API | Modifier les clés API | Créer et mettre à jour des clés API |
| Limites de l'API | Afficher les limites de l'API | Consulter les limites de débit de l'API |
| Alertes d'utilisation de l'API | Afficher les alertes d'utilisation de l'API | Consulter les alertes d'utilisation de l'API |
| Alertes d'utilisation de l'API | Modifier les alertes d'utilisation de l'API | Créer et mettre à jour des alertes d'utilisation de l'API |
| Données d'utilisation de l'API | Afficher le tableau de bord d'utilisation de l'API | Consulter le tableau de bord d'utilisation de l'API |
| Paramètres de l'application | Modifier les paramètres de l'application | Créer, modifier et mettre à jour des applications dans les paramètres de l'application |
| Paramètres de l'application | Afficher les paramètres de l'application | Consulter la page Paramètres de l'application |
| Paramètres Audience Sync | Afficher les paramètres Audience Sync | Consulter tous les paramètres des partenaires Audience Sync connectés |
| Utilisateurs du tableau de bord | Modifier les utilisateurs du tableau de bord | Afficher, créer et modifier les utilisateurs de l'entreprise |
| Paramètres d'e-mail | Afficher les paramètres d'e-mail | Consulter les préférences d'e-mail |
| Paramètres d'e-mail | Modifier les paramètres d'e-mail | Activer et mettre à jour les préférences d'e-mail |
| Journal des événements utilisateurs | Afficher le journal des événements utilisateurs | Consulter les journaux des événements utilisateurs |
| Groupes internes | Afficher les groupes internes | Afficher les groupes internes |
| Groupes internes | Supprimer les groupes internes | Supprimer des groupes internes |
| Groupes internes | Modifier les groupes internes | Créer et mettre à jour des groupes internes |
| Journal d'activité des messages | Afficher le journal d'activité des messages | Consulter les journaux d'activité des messages |
| Paramètres multilingues | Afficher les paramètres de localisation | Afficher la page des paramètres multilingues |
| Paramètres multilingues | Supprimer les paramètres de localisation | Supprimer des paramètres régionaux multilingues |
| Paramètres multilingues | Modifier les paramètres de localisation | Créer des paramètres régionaux multilingues |
| Centres de préférences | Afficher les centres de préférences | Consulter les centres de préférences |
| Centres de préférences | Modifier les centres de préférences | Créer et mettre à jour les centres de préférences |
| Centres de préférences | Lancer les centres de préférences | Activer un brouillon de centre de préférences ou mettre à jour un centre existant |
| Paramètres push | Afficher les paramètres push | Afficher les paramètres de notifications push |
| Paramètres push | Modifier les paramètres push | Créer et mettre à jour les paramètres de notifications push |
| Débogueur SDK | Afficher le débogueur SDK | Consulter le débogueur SDK ou les sessions de débogage |
| Débogueur SDK | Modifier le débogueur SDK | Créer et télécharger des sessions du débogueur SDK |
| Étiquettes | Afficher les étiquettes | Afficher les étiquettes |
| Étiquettes | Supprimer les étiquettes | Supprimer définitivement les étiquettes |
| Étiquettes | Modifier les étiquettes | Créer et mettre à jour des étiquettes |
| Équipes | Afficher les équipes | Afficher les équipes |
| Équipes | Archiver les équipes | Déplacer les équipes vers les archives |
| Équipes | Modifier les équipes | Créer et mettre à jour des équipes |
| Paramètres WhatsApp | Afficher les paramètres WhatsApp | Consulter tous les paramètres du canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres" }

### Decisioning Studio

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Agents Decisioning Studio | Afficher les agents Decisioning Studio | Consulter la configuration des agents Decisioning Studio sans apporter de modifications |
| Audience Decisioning Studio | Afficher l'audience Decisioning Studio | Consulter les détails de l'audience dans les résumés de configuration des agents Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning Studio" }

### Autres {#other}

| Domaine produit | Autorisation | Définition |
| --- | --- | --- |
| Utilisation de l'application | Afficher les données d'utilisation | Consulter les données d'utilisation |
| Facturation | Afficher les détails de facturation | Consulter les détails de facturation |
| Agents personnalisés | Afficher les agents IA de la Console des agents | Permet aux utilisateurs de visualiser les agents IA personnalisés |
| Agents personnalisés | Archiver les agents IA de la Console des agents | Permet aux utilisateurs d'archiver des agents IA personnalisés |
| Agents personnalisés | Modifier les agents IA de la Console des agents | Permet aux utilisateurs de créer et de mettre à jour des agents IA personnalisés |
| Attributs personnalisés marqués comme PII | Afficher les attributs personnalisés marqués comme PII | Afficher les attributs personnalisés marqués comme PII |
| Rapports du tableau de bord | Afficher les rapports du tableau de bord | Consulter les rapports sans apporter de modifications |
| Rapports du tableau de bord | Supprimer les rapports du tableau de bord | Supprimer définitivement les rapports |
| Rapports du tableau de bord | Modifier les rapports du tableau de bord | Créer et mettre à jour des rapports |
| Paramètres de domaine | Modifier les paramètres de domaine | Ajouter des domaines délégués et des domaines personnalisés sous Domaines vérifiés |
| Chiffrement au niveau du champ | Modifier le chiffrement au niveau du champ de l'identifiant | Activer et mettre à jour les paramètres de chiffrement au niveau du champ |
| Ressources de la bibliothèque multimédia | Afficher les ressources de la bibliothèque multimédia | Consulter les ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Supprimer les ressources de la bibliothèque multimédia | Supprimer définitivement les ressources de la bibliothèque multimédia |
| Ressources de la bibliothèque multimédia | Modifier les ressources de la bibliothèque multimédia | Créer et mettre à jour les ressources de la bibliothèque multimédia |
| Limites de débit des messages | Afficher les limites de débit des messages | Consulter les limites de débit des messages au niveau de l'espace de travail |
| Limites de débit des messages | Modifier les limites de débit des messages | Configurer et modifier les limites de débit des messages au niveau de l'espace de travail |
| Operator | Utiliser BrazeAI Operator<sup>TM</sup> | Accéder à BrazeAI Operator et l'utiliser pour répondre à des questions, guider la configuration, résoudre des problèmes et trouver des idées |
| Placements | Afficher les placements | Afficher les emplacements de bannières |
| Placements | Archiver les placements | Déplacer les emplacements de bannières vers les archives |
| Placements | Modifier les placements | Consulter les emplacements de bannières sans apporter de modifications |
| Codes de promotion | Afficher les codes de promotion | Consulter les codes de promotion |
| Codes de promotion | Exporter les codes de promotion | Télécharger la liste des codes de promotion depuis le tableau de bord |
| Codes de promotion | Modifier les codes de promotion | Créer et mettre à jour des codes de promotion |
| Groupes d'abonnement | Modifier les abonnements | Créer et mettre à jour des groupes d'abonnement |
| Transformations | Modifier les transformations de données | Créer et mettre à jour des transformations de données |
| Transformations | Afficher les transformations de données | Afficher les transformations de données |
| Enregistrements de suppression d'utilisateurs | Afficher les enregistrements de suppression d'utilisateurs | Consulter les enregistrements de suppression d'utilisateurs |
| Tickets d'assistance | Créer un ticket d'assistance | Créer et mettre à jour des tickets d'assistance |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autres" }