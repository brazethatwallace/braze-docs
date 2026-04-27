---
nav_title: FAQ
article_title: FAQ sur le partage des données Snowflake
page_order: 50
page_type: FAQ
description: "Cet article répond aux questions fréquemment posées sur le partage des données Snowflake."

---

# Questions fréquemment posées {#frequently-asked-questions}

### Est-il possible d'obscurcir les données personnelles identifiables via le partage de données Snowflake ? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
Non, pour l'instant, ce n'est pas possible.

### Ai-je besoin d'un partage de données pour la même région ou pour plusieurs régions ? {#do-i-need-data-share-for-the-same-region-or-cross-region}
Utilisez le partage de données pour la même région dans les scénarios suivants :
- Votre compte Snowflake se trouve dans la région US-EAST-1 (AWS) et la région de votre tableau de bord Braze se trouve aux États-Unis.
- Votre région Snowflake se trouve dans EU-CENTRAL-1 (AWS) et la région de votre tableau de bord Braze se trouve dans l'UE.
- Votre région Snowflake se trouve dans AP-Northeast-1 (AWS) et la région de votre tableau de bord Braze se trouve au Japon.
- Votre région Snowflake se trouve dans AP-Southeast-2 (AWS) et la région de votre tableau de bord Braze se trouve en Australie.
- Votre région Snowflake se trouve dans AP-Southeast-3 (AWS) et la région de votre tableau de bord Braze se trouve en Indonésie.

Dans le cas contraire, utilisez le partage de données inter-régions.

### Que dois-je faire de mon partage de données lorsque je passe à un nouveau compte Snowflake ? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
Vous pouvez supprimer l'ancien partage de données associé à votre ancien compte Snowflake, puis créer un nouveau partage pour le nouveau compte. Toutes les données historiques seront disponibles dans le nouveau partage.

### Pourquoi ne vois-je pas de données dans mon partage de données ? {#why-dont-i-see-data-in-my-data-share}
Vous avez peut-être utilisé le mauvais ID de compte Snowflake lors de la création de votre partage de données. L'ID du compte sur le tableau de bord de partage des données doit correspondre à la sortie de `CURRENT_ACCOUNT()` de votre compte Snowflake.

Si votre partage s'étend sur plusieurs régions, il est possible que les données ne soient pas immédiatement disponibles. Selon votre volume de données, la synchronisation des données avec votre région peut prendre quelques heures.

### Pourquoi est-ce que je reçois une erreur de conformité HIPAA lors de la création d'un partage de données ? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

Le compte spécifié n'est pas conforme à la norme HIPAA ou se trouve sur des [éditions Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inférieures à Business Critical. Votre compte Snowflake doit être mis à niveau vers l'édition Business Critical afin d'être conforme à la norme HIPAA pour le partage de données. Contactez l'assistance Snowflake pour obtenir de l'aide sur la mise à niveau de votre compte.

### Pourquoi ne puis-je pas recréer un partage de données après en avoir supprimé un ? {#why-cant-i-recreate-a-data-share-after-deleting-one}

Il se peut que le système soit encore en train de traiter la suppression de votre précédent partage de données. Attendez quelques minutes que le processus de déprovisionnement se termine, puis essayez à nouveau de créer le nouveau partage de données.

### Combien de fois dois-je exécuter `CREATE DATABASE` lorsque plusieurs espaces de travail partagent des données avec le même compte Snowflake ? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

Vous ne devez exécuter `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` qu'une seule fois. Lorsque plusieurs partages de données provenant de différents espaces de travail Braze sont envoyés vers le même compte Snowflake, ils sont automatiquement combinés en un seul partage. Une fois la base de données initiale créée, les données des espaces de travail supplémentaires sont automatiquement ajoutées à la base de données existante, sans nécessiter de demandes de partage supplémentaires ni d'étapes de création de base de données.

Par exemple, si vous créez un partage de données vers le compte Snowflake 123 à partir de l'espace de travail A, vous acceptez la demande de partage et créez une base de données. Lorsque vous créez ultérieurement un partage de données vers le même compte Snowflake 123 à partir de l'espace de travail B, aucune nouvelle demande de partage n'est envoyée : les données sont immédiatement ajoutées au partage existant et deviennent disponibles dans la base de données précédemment créée.

### Si j'ai plusieurs espaces de travail, une seule base de données contient-elle les données de tous ces espaces ? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

Oui. Lorsque vous partagez des données provenant de plusieurs espaces de travail Braze vers le même compte Snowflake, toutes les données sont combinées en un seul partage et disponibles dans la même base de données. Vous pouvez filtrer les données par `app_group_id` pour distinguer les espaces de travail.

En guise de bonne pratique, filtrez toujours par `app_group_id` dans vos requêtes afin de les pérenniser. Ainsi, vos tableaux de bord et rapports restent exacts si vous ajoutez des espaces de travail supplémentaires à l'avenir. Sans ce filtre, vos indicateurs peuvent inclure de manière inattendue des données provenant d'espaces de travail nouvellement ajoutés.

### Quelle est l'approche recommandée pour gérer les données provenant de plusieurs espaces de travail dans Snowflake ? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

Envoyez toutes les données de Braze dans la même base de données et filtrez par `app_group_id` pour distinguer les espaces de travail. Cette approche simplifie la gestion des données et garantit des rapports cohérents dans l'ensemble de votre organisation.

### De combien de connecteurs Snowflake Data Share ai-je besoin pour plusieurs espaces de travail ? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

Le nombre de connecteurs dont vous avez besoin dépend de votre configuration spécifique et de vos droits. Contactez votre équipe de compte Braze pour en savoir plus sur les droits adaptés à votre cas d'utilisation.

### Quelles options existent pour isoler les données de différents espaces de travail au sein du même compte Snowflake ? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

Vous pouvez isoler logiquement les données à l'aide de la colonne `app_group_id`, qui identifie l'espace de travail auquel chaque ligne de données appartient. Les approches les plus courantes sont les suivantes :

- **Vues (recommandé) :** créez une vue pour chaque espace de travail filtrée par `app_group_id`. Cela évite de dupliquer les données tout en offrant à chaque équipe ou cas d'utilisation une vue propre et délimitée de ses données d'espace de travail.
- **Copies de tables locales :** copiez les données dans des tables séparées filtrées par `app_group_id`. Cette méthode duplique les données, c'est pourquoi l'approche par vues est généralement préférée.
- **Politiques d'accès aux lignes et rôles :** utilisez les politiques d'accès aux lignes natives de Snowflake combinées à des rôles pour restreindre les lignes que chaque rôle peut interroger. Cela conserve les données dans une seule table tout en appliquant le contrôle d'accès au moment de la requête.

Vous configurez ces options au sein de votre compte Snowflake.

### Puis-je utiliser un compte Snowflake différent pour isoler les données de différents espaces de travail ? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

Oui. Si l'espace de travail A partage vers le compte X et l'espace de travail B partage vers le compte Y, chaque compte reçoit un partage indépendant avec des données séparées. Cependant, la plupart des organisations utilisent un seul compte Snowflake pour toutes leurs données métier. Cette approche peut donc ajouter une charge opérationnelle supplémentaire. Évaluez ce compromis avant de la choisir plutôt que les approches d'isolation logique décrites dans la section précédente.

### L'isolation des données par espace de travail est-elle un cas d'utilisation pris en charge pour le partage de données Snowflake ? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

Oui, grâce aux approches d'isolation logique décrites dans les sections précédentes. Braze ne crée pas de partages séparés pour chaque espace de travail ; vous gérez donc l'isolation au niveau de Snowflake à l'aide de vues, de politiques d'accès aux lignes ou de comptes séparés.