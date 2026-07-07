---
nav_title: Le tableau de bord
article_title: Le tableau de bord de Braze
page_order: 1
page_type: reference
description: "Le tableau de bord de Braze est votre espace de travail central pour créer, gérer et analyser l'engagement client. Il rassemble les outils d'envoi de messages, les informations sur l'audience, la segmentation et les données de performance en temps réel en un seul endroit."

---

# Le tableau de bord de Braze {#the-braze-dashboard}

> Le tableau de bord de Braze est votre espace de travail central pour créer, gérer et analyser l'engagement client. Accédez-y à l'adresse [dashboard.braze.com](https://dashboard.braze.com/) ou [dashboard.braze.eu](https://dashboard.braze.eu/).

Utilisez le tableau de bord de Braze pour planifier des campagnes, lancer et gérer des messages, explorer les informations sur l'audience, ajuster la segmentation et consulter les indicateurs de performance et d'engagement en temps réel depuis une interface unique.

## Aperçu du tableau de bord {#dashboard-overview}

Lorsque vous vous connectez, le tableau de bord offre une vue centralisée de vos outils d'engagement et de vos données :

- **Page d'accueil :** affiche votre [contenu récemment modifié](#pick-up-where-you-left-off) et les indicateurs de performance clés en un coup d'œil
- **Navigation latérale :** organise les outils par fonction (envoi de messages, audience, analyse, paramètres)
- **En-tête global :** fournit un accès rapide à la recherche, à l'assistance, aux paramètres de langue, aux notifications et à votre compte

Votre expérience du tableau de bord est organisée par [espaces de travail]({{site.baseurl}}/user_guide/get_started/workspaces), qui vous aident à gérer le contenu pour différentes marques, régions ou équipes. Vous pouvez [basculer entre les espaces de travail](#workspace-switcher) à tout moment depuis la navigation latérale.

## Accéder à votre tableau de bord {#access-your-dashboard}

Pour commencer, [connectez-vous à votre compte Braze]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Votre accès aux pages du tableau de bord et votre autorisation d'effectuer certaines actions sont basés sur vos [autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) attribuées. Si vous avez besoin d'aide avec vos autorisations, contactez vos administrateurs Braze.

## Naviguer dans Braze {#navigate-braze}

La navigation de Braze est conçue pour vous aider à accéder efficacement aux fonctionnalités et au contenu sur tous les appareils. Il existe deux niveaux de navigation dans le tableau de bord de Braze : l'en-tête global et la navigation latérale.

L'en-tête global est presque toujours visible en haut de l'écran. Il fournit un accès rapide aux outils et paramètres essentiels, notamment :

- [Recherche](#search-your-dashboard)
- Liens vers l'assistance et la communauté
- [Langue du tableau de bord]({{site.baseurl}}/user_guide/administer/personal/language_settings)
- Notifications
- Paramètres du compte
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)

### Utiliser la navigation latérale {#use-the-side-navigation}

Le menu vertical à gauche organise les outils de Braze par fonction et garde vos éléments les plus utilisés à portée de main. Sélectionnez un élément du menu principal pour afficher ses options dans une disposition verticale empilée.

![Sélecteur d'espace de travail dans le tableau de bord de Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Sélecteur d'espace de travail {#workspace-switcher}

Situé en haut de la navigation latérale, le sélecteur d'espace de travail vous permet de passer d'un espace de travail à un autre dans votre instance Braze. L'espace de travail actif est mis en surbrillance.

Les [espaces de travail]({{site.baseurl}}/user_guide/get_started/workspaces) aident à organiser le contenu par marque, région, ligne de produits ou équipe. Chaque espace de travail comprend ses propres données, Campaigns et paramètres. Votre accès peut varier d'un espace de travail à l'autre. Par exemple, vous pourriez avoir un accès en modification dans un espace de travail et un accès en lecture seule dans un autre.

Pour changer d'espace de travail, sélectionnez le menu déroulant de l'espace de travail en haut de la navigation latérale et choisissez l'espace de travail auquel vous souhaitez accéder. Vous pouvez également [ajouter des espaces de travail favoris](#favorite-workspaces) pour un accès plus rapide à ceux que vous utilisez le plus souvent.

#### Réduire la navigation latérale {#minimize-the-side-navigation}

Pour réduire l'encombrement visuel, notamment lors de tâches comme la conception d'un Canvas, vous pouvez réduire le panneau de navigation latérale. Appuyez sur **Réduire le menu** pour le replier. Même lorsqu'il est réduit, survolez n'importe quelle icône pour afficher des infobulles avec les noms des éléments de menu. Cela vous aide à passer rapidement d'un outil à l'autre tout en gardant votre espace de travail épuré.

![Icônes de réduction et d'agrandissement du menu]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navigation responsive {#responsive-navigation}

La navigation s'adapte de façon fluide aux différentes tailles d'écran. Sur les écrans plus petits, la navigation latérale se replie automatiquement. Appuyez sur <i class="fa-solid fa-bars" aria-label="Ouvrir le menu de navigation"></i> pour ouvrir le menu si nécessaire.

![Sur les écrans plus petits, la navigation latérale se replie automatiquement. Appuyer sur l'icône de menu ouvre les options de navigation.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Rechercher dans votre tableau de bord {#search-your-dashboard}

La barre de recherche globale, située dans l'en-tête, est le moyen le plus rapide de trouver du contenu dans votre tableau de bord de Braze. Sélectionnez-la pour ouvrir l'interface de recherche et accéder directement à ce dont vous avez besoin.

![Recherche globale ouverte sans terme de recherche saisi, affichant les pages récemment ouvertes.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Votre contenu récemment ouvert apparaît sous la barre de recherche. Cela inclut toute Campaign, tout Canvas, modèle ou page avec lesquels vous avez récemment interagi, ce qui facilite le retour à votre travail.

### Que pouvez-vous rechercher ? {#what-can-you-search-for}

Vous pouvez rechercher les éléments et actions suivants :

- Noms de Campaigns
- Noms de Canvas
- Content Blocks
- Noms de Segments
- Noms de modèles d'e-mail
- Pages dans Braze (y compris les synonymes)

{% alert tip %}
Pour rechercher un texte exact, mettez votre terme de recherche entre guillemets (""). Par exemple, la recherche de ["all users"] renverra tous les éléments contenant la phrase exacte « all users » dans leur nom.
{% endalert %}

### Étiquettes de type de contenu et de statut {#content-type-and-status-tags}

Chaque résultat est accompagné d'une étiquette indiquant son type de contenu — comme Campaign, Canvas ou Segment — et son statut (actif, archivé, arrêté).

### Filtrer le contenu actif et en brouillon {#filter-for-active-and-draft-content}

Par défaut, la recherche inclut les éléments actifs, en brouillon et archivés. Utilisez le bouton **Show active and draft only** pour affiner vos résultats.

![Le bouton « Show active and draft only ».]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Raccourcis clavier {#keyboard-shortcuts}

Vous pouvez parcourir les résultats de recherche à l'aide de votre clavier.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Action                              | Raccourci clavier                                                             |
| ----------------------------------- | ----------------------------------------------------------------------------- |
| Ouvrir le menu de recherche         | {::nomarkdown} <ul> <li> Mac : <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows : <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/}  |
| Se déplacer entre les résultats     | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Sélectionner un résultat            | <kbd>Enter</kbd>    |
| Fermer le menu de recherche         | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Raccourcis clavier" }

## Fonctionnalités de productivité {#productivity-features}

Le tableau de bord de Braze comprend plusieurs fonctionnalités pour vous aider à travailler plus efficacement et à accéder rapidement aux outils et au contenu que vous utilisez le plus.

### BrazeAI Operator

BrazeAI Operator™ est un assistant alimenté par l'intelligence artificielle intégré au tableau de bord. Utilisez-le pour obtenir des réponses, suivre des étapes de configuration, résoudre des problèmes et trouver des idées. Ouvrez-le depuis **BrazeAI Operator™** dans l'en-tête global à côté de votre profil. Pour en savoir plus, consultez [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator).

### Reprendre là où vous en étiez {#pick-up-where-you-left-off}

Sur la page **Accueil**, le tableau de bord affiche vos Campaigns, Canvas et Segments récemment modifiés ou créés. Cela facilite le retour à un travail en cours sans avoir à effectuer de recherche. Chaque élément inclut des étiquettes indiquant le type de contenu et le statut (comme brouillon, actif ou arrêté).

![Un brouillon de Canvas, un Segment actif et un brouillon de Campaign dans la section « Reprendre là où vous en étiez ».]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

Pour en savoir plus, consultez [Tableau de bord d'accueil]({{site.baseurl}}/user_guide/analytics/dashboards/home#pick-up-where-you-left-off).

### Espaces de travail favoris {#favorite-workspaces}

Si vous travaillez avec plusieurs espaces de travail, vous pouvez marquer ceux que vous utilisez le plus fréquemment comme favoris. Les espaces de travail favoris apparaissent en haut du sélecteur d'espace de travail pour un accès plus rapide.

Pour ajouter des espaces de travail favoris :

1. [Accédez aux paramètres de votre profil](#access-your-profile-settings).
2. Dans la section **Profil du compte**, localisez le champ **Espaces de travail favoris**.
3. Sélectionnez les espaces de travail que vous souhaitez ajouter aux favoris.

### Accéder aux paramètres de votre profil {#access-your-profile-settings}

Pour gérer les paramètres de votre compte, vos préférences de notification et vos informations personnelles :

1. Sélectionnez l'icône de votre profil dans l'en-tête global.
2. Sélectionnez **Gérer votre compte** pour accéder à votre page de profil.

Depuis votre page de profil, vous pouvez mettre à jour vos paramètres d'e-mail, configurer l'authentification à deux facteurs, consulter vos clés API et gérer d'autres détails de votre compte.

## Accessibilité dans le tableau de bord {#accessibility-in-the-dashboard}

Le tableau de bord de Braze utilise des couleurs de marque conformes aux normes WCAG AA en matière de contraste des couleurs. Cela favorise une expérience inclusive pour tous les utilisateurs et s'aligne sur les meilleures pratiques en matière d'accessibilité.

## Partager vos commentaires {#sharing-feedback}

Vous souhaitez nous dire ce que vous en pensez ? Vous pouvez partager vos commentaires sur la navigation, l'accessibilité, l'ergonomie, le design visuel et bien plus encore. Ouvrez le menu **Assistance** dans l'en-tête global et sélectionnez **Share feedback**. Nous examinons tous les commentaires pour améliorer votre expérience avec Braze.

## Ressources associées {#related-resources}

### Tâches administratives {#administrative-tasks}

- [Créer et gérer des espaces de travail]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)
- [Gérer les utilisateurs Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)
- [Autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)
- [Équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams)

### Tâches clés et prochaines étapes {#key-tasks-and-next-steps}

- **Créer des campagnes** : [Créer une Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- **Créer des parcours** : [Créer un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- **Définir des audiences** : [Créer un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)
- **Consulter les performances** : [Aperçu de l'analyse]({{site.baseurl}}/user_guide/analytics/dashboards/home)
- **Configurer les paramètres** : [Paramètres des applications]({{site.baseurl}}/user_guide/administer/global/workspace_settings)