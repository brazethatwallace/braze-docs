---
nav_title: FAQ
article_title: FAQ sur le partage des données Snowflake
page_order: 50
page_type: FAQ
description: "Cet article répond aux questions fréquemment posées sur le partage des données Snowflake."

---

# Questions fréquemment posées {#frequently-asked-questions}

## Est-il possible de masquer les données d'identification via le partage de données Snowflake ? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
Non, cette fonctionnalité n'est pas prise en charge pour le moment.

## Ai-je besoin du partage de données pour la même région ou entre régions ? {#do-i-need-data-share-for-the-same-region-or-cross-region}
Utilisez le partage de données pour la même région dans les scénarios suivants :
- Votre compte Snowflake est dans US-EAST-1 (AWS) et la région de votre tableau de bord de Braze est aux États-Unis.
- Votre région Snowflake est dans EU-CENTRAL-1 (AWS) et la région de votre tableau de bord de Braze est dans l'UE.
- Votre région Snowflake est dans AP-Northeast-1 (AWS) et la région de votre tableau de bord de Braze est au Japon.
- Votre région Snowflake est dans AP-Southeast-2 (AWS) et la région de votre tableau de bord de Braze est en Australie.
- Votre région Snowflake est dans AP-Southeast-3 (AWS) et la région de votre tableau de bord de Braze est en Indonésie.

Sinon, utilisez le partage de données entre régions.

## Que dois-je faire avec mon partage de données lorsque je passe à un nouveau compte Snowflake ? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
Vous pouvez supprimer l'ancien partage de données associé à votre ancien compte Snowflake, puis créer un nouveau partage pour le nouveau compte. Toutes les données historiques seront disponibles dans le nouveau partage.

## Que se passe-t-il si je bascule mon partage de données vers un nouvel espace de travail Braze ? {#what-happens-if-i-switch-my-data-share-to-a-new-braze-workspace}

Si vous reconfigurez une intégration de partage de données existante pour utiliser un espace de travail Braze différent, vous pouvez voir cette erreur dans Snowflake lors de l'interrogation des tables :

> Shared database is no longer available for use. It will need to be re-created if and when the publisher makes it available again.

Pour résoudre ce problème, vous devez supprimer et recréer le partage dans Snowflake :

1. Supprimez la base de données qui a été créée avec le partage précédent.
2. Créez à nouveau la base de données en suivant les [instructions d'intégration]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake#step-2-create-the-database-in-snowflake).
3. Réattribuez les privilèges d'accès nécessaires à la nouvelle base de données.
4. Recréez les vues (le cas échéant) qui faisaient référence à l'ancienne base de données.

{% alert note %}
Dans la nouvelle interface Snowflake, vous pouvez trouver le partage Braze sous **Data Products** > **Private Sharing** > **Shared with you**.
{% endalert %}

## Pourquoi ne vois-je pas de données dans mon partage de données ? {#why-dont-i-see-data-in-my-data-share}
Il est possible que vous ayez utilisé le mauvais identifiant de compte Snowflake lors de la création de votre partage de données. L'identifiant de compte sur le tableau de bord de partage de données doit correspondre à la sortie de `CURRENT_ACCOUNT()` depuis votre compte Snowflake.

Si votre partage est inter-régions, les données peuvent ne pas être immédiatement disponibles. En fonction de votre volume de données, la synchronisation vers votre région peut prendre quelques heures.

## Pourquoi est-ce que je reçois une erreur de conformité HIPAA lors de la création d'un partage de données ? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

Le compte spécifié n'est pas conforme à la norme HIPAA ou utilise une [édition Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inférieure à Business Critical. Votre compte Snowflake doit être mis à niveau vers l'édition Business Critical pour être conforme à la norme HIPAA en matière de partage de données. Contactez le support Snowflake pour obtenir de l'aide concernant la mise à niveau de votre compte.

## Pourquoi ne puis-je pas recréer un partage de données après en avoir supprimé un ? {#why-cant-i-recreate-a-data-share-after-deleting-one}

Il est possible que le système soit encore en train de traiter la suppression de votre précédent partage de données. Attendez quelques minutes que le processus de déprovisionnement se termine, puis essayez de créer le nouveau partage de données.

## Combien de fois dois-je exécuter `CREATE DATABASE` lorsque plusieurs espaces de travail partagent des données vers le même compte Snowflake ? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

Vous n'avez besoin d'exécuter `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` qu'une seule fois. Lorsque plusieurs partages de données provenant de différents espaces de travail Braze sont partagés vers le même compte Snowflake, ils sont automatiquement combinés dans le même partage. Après avoir créé la base de données initiale, les données des espaces de travail supplémentaires sont automatiquement ajoutées à la base de données existante sans nécessiter de demandes de partage ou d'étapes de création de base de données supplémentaires.

Par exemple, si vous créez un partage de données vers le compte Snowflake 123 depuis l'espace de travail A, vous acceptez la demande de partage et créez une base de données. Lorsque vous créez ultérieurement un partage de données vers le même compte Snowflake 123 depuis l'espace de travail B, aucune nouvelle demande de partage n'est envoyée : les données sont immédiatement ajoutées au partage existant et deviennent disponibles dans la base de données précédemment créée.

## Si j'ai plusieurs espaces de travail, une seule base de données contient-elle les données de tous ces espaces ? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

Oui. Lorsque vous partagez des données provenant de plusieurs espaces de travail Braze vers le même compte Snowflake, toutes les données sont combinées dans un seul partage et disponibles dans la même base de données. Vous pouvez filtrer les données par `app_group_id` pour distinguer les espaces de travail.

En tant que bonne pratique, filtrez toujours par `app_group_id` dans vos requêtes pour les pérenniser. Cela garantit que vos tableaux de bord et rapports restent précis si vous ajoutez des espaces de travail supplémentaires à l'avenir. Sans ce filtre, vos indicateurs pourraient inclure de manière inattendue des données provenant d'espaces de travail nouvellement ajoutés.

## Quelle est l'approche recommandée pour gérer les données de plusieurs espaces de travail dans Snowflake ? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

Envoyez toutes les données Braze dans la même base de données et filtrez par `app_group_id` pour distinguer les espaces de travail. Cette approche simplifie la gestion des données et garantit des rapports cohérents au sein de votre organisation.

## Combien de connecteurs Snowflake Data Share me faut-il pour plusieurs espaces de travail ? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

Le nombre de connecteurs dont vous avez besoin dépend de votre configuration et de vos droits spécifiques. Contactez votre équipe de compte Braze pour en savoir plus sur les droits adaptés à votre cas d'usage.

## Quelles options existent pour isoler les données de différents espaces de travail au sein du même compte Snowflake ? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

Vous pouvez isoler les données de manière logique à l'aide de la colonne `app_group_id`, qui identifie l'espace de travail auquel chaque ligne de données appartient. Les approches les plus courantes sont les suivantes :

- **Vues (recommandé) :** Créez une vue pour chaque espace de travail filtrée par `app_group_id`. Cela évite de dupliquer les données tout en offrant à chaque équipe ou cas d'usage une vue claire et délimitée des données de son espace de travail.
- **Copies de tables locales :** Copiez les données dans des tables distinctes filtrées par `app_group_id`. Cela duplique les données, c'est pourquoi l'approche par vues est généralement préférée.
- **Politiques d'accès aux lignes et rôles :** Utilisez les politiques d'accès aux lignes natives de Snowflake combinées à des rôles pour restreindre les lignes que chaque rôle peut interroger. Cela conserve les données dans une seule table tout en appliquant le contrôle d'accès au moment de la requête.

Vous configurez ces options au sein de votre compte Snowflake.

## Puis-je utiliser un compte Snowflake différent pour isoler les données de différents espaces de travail ? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

Oui. Si l'espace de travail A partage vers le compte X et l'espace de travail B partage vers le compte Y, chaque compte reçoit un partage indépendant avec des données séparées. Cependant, la plupart des organisations utilisent un seul compte Snowflake pour l'ensemble de leurs données métier. Cette approche peut donc ajouter une charge opérationnelle supplémentaire. Évaluez ce compromis avant de la préférer aux approches d'isolation logique décrites dans la section précédente.

## L'isolation des données par espace de travail est-elle un cas d'usage pris en charge pour le partage de données Snowflake ? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

Oui, grâce aux approches d'isolation logique décrites dans les sections précédentes. Braze ne crée pas de partages distincts pour chaque espace de travail, vous gérez donc l'isolation au niveau de Snowflake à l'aide de vues, de politiques d'accès aux lignes ou de comptes séparés.