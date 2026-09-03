---
nav_title: Créer et gérer des espaces de travail
article_title: Créer et gérer des espaces de travail
page_order: 0
layout: dev_guide
guide_top_header: "Créer et gérer des espaces de travail"
guide_top_text: "Cet article explique comment créer, configurer et gérer vos espaces de travail."
page_type: reference
description: "Cet article explique comment créer, configurer et gérer vos espaces de travail."

guide_featured_title: "Articles de la section"
guide_featured_list:
- name: Migrer des données entre espaces de travail
  link: /docs/user_guide/administer/global/create_and_manage_workspaces/migrate_workspace_data
  image: /assets/img/braze_icons/switch-horizontal-01.svg
---

<br>

# Créer et gérer des espaces de travail {#create-and-manage-workspaces}

> Cet article explique comment créer, configurer et gérer vos espaces de travail.

## Qu'est-ce qu'un espace de travail ? {#what-is-a-workspace}

Tout ce que vous faites dans Braze se déroule au sein d'un espace de travail. Les espaces de travail sont un environnement partagé qui vous permet de suivre et de gérer l'engagement pour des applications mobiles ou des sites web associés. Les espaces de travail regroupent des applications identiques ou très similaires : par exemple, les versions Android et iOS de votre application mobile.

## Créer un espace de travail {#creating-a-workspace}

### Étape 1 : Avoir un plan {#step-1-have-a-plan}

Avant de commencer, assurez-vous d'avoir travaillé avec votre équipe et votre responsable d'onboarding Braze pour déterminer la meilleure configuration d'espace de travail pour votre cas d'usage. Pour en savoir plus sur la planification de vos espaces de travail dans Braze, consultez notre guide [Premiers pas : Espaces de travail]({{site.baseurl}}/user_guide/get_started/workspaces).

{% alert warning %}
**Bonne pratique : utilisez des projets Firebase dédiés par espace de travail**<br>
Bien que Braze permette de télécharger le même fichier JSON de compte de service Firebase dans plusieurs espaces de travail, tous les espaces de travail utilisant le même ID de projet Google partagent la limite de débit par défaut de Firebase Cloud Messaging de 600 000 messages par minute. Les expéditeurs à fort volume peuvent rencontrer des erreurs « Quota Exceeded » lors de lancements simultanés de Campaigns dans plusieurs espaces de travail.<br><br>Pour une livrabilité et une gestion des quotas isolées, utilisez des projets Firebase distincts et dédiés pour chaque espace de travail Braze.
{% endalert %}

### Étape 2 : Ajouter votre espace de travail {#step-2-add-your-workspace}

Vous pouvez créer de nouveaux espaces de travail ou basculer entre des espaces de travail existants depuis le menu déroulant des espaces de travail dans l'en-tête global.

1. Sélectionnez le menu déroulant des espaces de travail, puis sélectionnez <i class="fa-solid fa-square-plus" style="color: #0b8294;" aria-hidden="true"></i> **Créer un espace de travail**.

![Le menu déroulant des espaces de travail avec le bouton « Créer un espace de travail ».]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2. Donnez un nom à votre espace de travail.

{% alert tip %}
Vous pouvez adopter une convention de nommage afin que les autres membres de votre entreprise puissent facilement trouver votre espace de travail. Par exemple : « Upon Voyage US – Production » et « Upon Voyage US – Staging ».
{% endalert %}

{:start="3"}
3. Sélectionnez **Créer**. La création de votre espace de travail par Braze peut prendre quelques secondes.

![Fenêtre modale « Créer un espace de travail » avec le nom « Upon Voyage US - Staging ».]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Vous serez redirigé vers la page **Paramètres des applications** pour commencer à ajouter vos instances d'application. Vous pouvez accéder à cette page à tout moment depuis **Paramètres** > **Paramètres des applications**.

![Page « Paramètres des applications » pour l'espace de travail Upon Voyage US - Staging avec un bouton pour ajouter une application.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Étape 3 : Ajouter vos instances d'application {#step-3-add-your-app-instances}

Les différents sites et applications regroupés au sein d'un espace de travail sont appelés « instances d'application ».

1. Depuis la page **Paramètres des applications**, sélectionnez **+ Ajouter une application**.
2. Donnez un nom à votre instance d'application et sélectionnez la ou les plateformes sur lesquelles elle se trouve. Si vous sélectionnez plusieurs plateformes, Braze créera une instance d'application pour chaque plateforme.

![Fenêtre modale « Ajouter une nouvelle application à Upon Voyage US - Staging » avec des options pour sélectionner les détails de l'application.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3. Sélectionnez **Ajouter une application** pour confirmer.

#### Clés API de l'application {#app-api-keys}

Après avoir ajouté votre instance d'application, vous aurez accès à sa clé API. La clé API est utilisée pour effectuer des requêtes entre votre instance d'application et l'API Braze. La clé API est également importante pour intégrer le SDK Braze à votre application ou site web.

![Page de paramètres de l'application Upon Voyage iOS avec des champs pour la clé API et l'endpoint SDK.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Vous devez créer des instances d'application distinctes pour chaque version de votre application sur chaque plateforme. Par exemple, si vous avez des versions Free et Pro de votre application sur iOS et Android, créez quatre instances d'application dans votre espace de travail (application Free iOS, application Free Android, application Pro iOS et application Pro Android). Cela vous donnera quatre clés API à utiliser, une pour chaque instance d'application.
{% endalert %}

#### Version du SDK en production {#live-sdk-version}

La version du SDK en production affichée sur la page Paramètres des applications pour une application spécifique correspond à la version d'application la plus élevée représentant au moins 5 % de l'ensemble de vos sessions quotidiennes et ayant enregistré au moins 500 sessions au cours de la journée précédente.

Ce champ apparaît après avoir intégré le SDK Braze à votre application ou site web. Si une version plus récente du SDK Braze est disponible pour votre plateforme, cela sera indiqué ici avec l'étiquette « Newer Version Available ».

![Section « Version du SDK en production » avec une valeur de champ « 5.4.0 » et une icône indiquant qu'une nouvelle version est disponible.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Étape 4 : Répéter si nécessaire {#step-4-repeat-as-needed}

Répétez les étapes 2 et 3 pour configurer autant d'espaces de travail que votre plan le nécessite. Nous recommandons de créer un espace de travail de test pour les tests d'intégration et de Campaign.

{% alert tip %}
**Ajouter un espace de travail de test**<br>Vous pouvez effectuer des tests d'application en isolant complètement certains utilisateurs de votre instance de production. Créez un nouvel espace de travail et, lorsque vous publiez votre application, assurez-vous de modifier la clé API utilisée par Braze pour qu'elle corresponde à celle de votre espace de travail de production plutôt qu'à celle de votre espace de travail de test.
{% endalert %}

## Gérer les espaces de travail {#managing-workspaces}

### Ajouter des favoris {#adding-favorites}

Vous pouvez ajouter des espaces de travail favoris pour accéder encore plus rapidement aux espaces de travail que vous utilisez le plus.

![Menu déroulant des espaces de travail avec l'onglet « Espaces de travail favoris ».]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

Pour ajouter des espaces de travail favoris :

1. Sélectionnez le menu déroulant de votre profil, puis sélectionnez **Gérer votre compte**.
2. Dans la section **Profil du compte**, localisez le champ **Espaces de travail favoris**.
3. Sélectionnez vos espaces de travail dans la liste.
4. Sélectionnez **Enregistrer les modifications**.

Il n'y a pas de limite au nombre d'espaces de travail que vous pouvez mettre en favoris, mais nous recommandons de garder cette liste courte pour plus de commodité.

### Renommer des espaces de travail {#renaming-workspaces}

Pour renommer votre espace de travail :

1. Allez dans **Paramètres** > **Paramètres des applications**.
2. Survolez le nom de votre espace de travail et sélectionnez <i class="fa-solid fa-pencil" style="color: #0b8294;" aria-hidden="true"></i> **Modifier**.
3. Donnez un nouveau nom à votre espace de travail, puis sélectionnez <i class="fa-solid fa-square-check" style="color: #0b8294;" aria-hidden="true"></i> **Enregistrer**.

![L'icône de crayon apparaissant à côté du nom de l'espace de travail.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Supprimer des espaces de travail et des instances d'application {#deleting-workspaces-and-app-instances}

Pour supprimer votre espace de travail ou instance d'application :

1. Allez dans **Paramètres** > **Paramètres des applications**.
2. Sélectionnez **Supprimer l'espace de travail** pour supprimer l'espace de travail concerné, ou sélectionnez l'icône de corbeille à côté de l'instance d'application concernée.

Vous ne pouvez pas supprimer des instances d'application ou des espaces de travail qui sont actuellement utilisés pour cibler des utilisateurs ou qui comptent plus de 1 000 utilisateurs. Si vous essayez de le faire, vous recevrez un message d'erreur. Pour procéder à la suppression, [créez un cas d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) en incluant un lien vers le tableau de bord et le nom de l'instance d'application ou de l'espace de travail à supprimer.

{% alert warning %}
Soyez prudent lorsque vous supprimez des espaces de travail ! Une fois un espace de travail supprimé, il ne peut pas être restauré.
{% endalert %}

![La page Paramètres des applications avec un bouton pour supprimer un espace de travail et une icône de corbeille pour supprimer une application.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Questions fréquemment posées {#frequently-asked-questions}

### Dois-je créer un nouvel espace de travail lorsque je publie une mise à jour de mon application ? {#should-i-create-a-new-workspace-when-im-releasing-an-updated-app}

Cela dépend de si vous mettez à jour votre application ou si vous en créez une entièrement nouvelle.

#### Mettre à jour votre application {#updating-your-app}

Si vous mettez à jour votre application, vous devez séparer l'ancienne et la nouvelle version en créant une nouvelle instance d'application au sein du même espace de travail. De cette façon, vous pouvez cibler efficacement les utilisateurs de la nouvelle version lorsque vous sélectionnez cette application lors de la segmentation. Si vous souhaitez envoyer des messages aux utilisateurs de l'ancienne version, vous pouvez utiliser des filtres pour [cibler la version précédente de l'application]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

Si vous créez un nouvel espace de travail, vos utilisateurs existeront à deux endroits : l'ancien espace de travail et le nouveau. Ils pourraient également avoir le même jeton de notification push. Cela peut amener des utilisateurs à recevoir un message marketing destiné uniquement aux utilisateurs de l'ancien espace de travail, même s'ils ont déjà effectué la mise à jour.

#### Publier une nouvelle application {#releasing-a-new-app}

Si vous publiez une application entièrement nouvelle sur la boutique d'applications, vous devez créer un nouvel espace de travail. En créant un nouvel espace de travail, toutes les données historiques et les profils utilisateurs de l'ancienne version de l'application n'existeront pas dans ce nouvel espace de travail. Ainsi, lorsque les utilisateurs existants passeront à la nouvelle version de l'application, ils auront un nouveau profil créé sans aucune des données comportementales de l'ancienne application.

### J'ai plusieurs instances d'application dans un seul espace de travail — comment puis-je m'assurer de ne cibler qu'une seule application avec mon message ? {#singular-app}

Pour vous assurer que votre message ne cible qu'une application spécifique, ajoutez un segment qui ne cible que les utilisateurs des instances d'application souhaitées. C'est particulièrement important si un utilisateur peut avoir deux jetons de notification push pour différentes instances d'application dans le même espace de travail. Dans ce scénario, les utilisateurs pourraient recevoir une notification pour une application différente de celle sur laquelle ils se trouvent. Ce n'est pas une expérience idéale !

Par défaut, un segment cible toutes les applications et tous les sites web de l'espace de travail. Pour configurer un segment qui ne cible qu'une seule application ou un seul site web :

1. Créez un segment avec un nom significatif. Chez Braze, nous utilisons le format « All Users ({Name} {Platform}) ». Par exemple, « All Users (Upon Voyage iOS) ».
2. Pour **Applications et sites web ciblés**, sélectionnez **Utilisateurs d'applications spécifiques**.
3. Dans le menu déroulant **Applications spécifiques**, sélectionnez votre application ou site.

![Segment ciblant les utilisateurs d'applications spécifiques.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

Vous pouvez ensuite ajouter ce segment à votre message et affiner davantage votre audience avec des segments et des filtres supplémentaires si nécessaire.

#### Campaigns {#campaigns}

Pour les Campaigns, ajoutez votre segment à l'étape **Audience cible** du composeur.

#### Canvas {#canvas}

Dans Canvas, ajoutez votre segment à vos étapes de message, dans la section **Validations de réception/distribution**. Les validations de réception/distribution vérifient que votre audience répond à vos critères de réception/distribution au moment de l'envoi du message. N'oubliez pas de spécifier les validations de réception/distribution pour chaque étape de message afin de vous assurer que le message sera envoyé à la bonne application. Il n'est pas nécessaire de segmenter au niveau de l'entrée.

{% details Développer pour les étapes dans le workflow Canvas d'origine %}

Dans le workflow Canvas d'origine, ajoutez votre segment au niveau du composant Canvas dans la section **Audience**. Il n'est pas nécessaire de segmenter au niveau de l'entrée.

{% enddetails %}

## Étapes suivantes {#next-steps}

Après avoir créé votre espace de travail, configurez-le :

- [Paramètres de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/workspace_settings) pour configurer les clés API, les préférences des e-mails, les paramètres de notifications push, et plus encore.
- [Gérer les utilisateurs de l'entreprise]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) pour ajouter des utilisateurs et attribuer des autorisations pour cet espace de travail.