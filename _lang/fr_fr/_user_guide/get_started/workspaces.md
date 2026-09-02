---
nav_title: Espaces de travail
article_title: "Pour commencer : Espaces de travail"
page_order: 3
page_type: reference
description: "Tout ce que vous faites dans la plateforme Braze se produit au sein d'un espace de travail. Cet article décrit leur fonctionnement et les éléments importants à prendre en compte."
---

# Pour commencer : Espaces de travail {#get-started-workspaces}

> Tout ce que vous faites dans la plateforme Braze se produit au sein d'un espace de travail. Les espaces de travail agissent comme des silos de données distincts et vous permettent de séparer différentes marques ou activités. Plusieurs versions de votre site web ou de votre application mobile peuvent envoyer des données au même espace de travail. Les différents sites et applications rassemblés au sein d'un espace de travail sont appelés des « instances d'applications ».

## Comprendre les espaces de travail {#understanding-workspaces}

Les espaces de travail remplissent deux fonctions clés :

- **Unifier les données utilisateur :** lorsque plusieurs instances d'une application se trouvent dans un même espace de travail, vous pouvez collecter et cibler les données utilisateur de façon fluide à travers les différentes versions de votre application, comme iOS, Android et le web. Cela garantit que vous disposez toujours d'informations à jour sur chaque utilisateur, quelle que soit la plateforme qu'il utilise.
- **Séparer les activités distinctes :** les espaces de travail permettent également de garder des marques ou des activités distinctes séparées. Par exemple, si vous avez plusieurs sous-marques avec des bases d'utilisateurs différentes, il est avantageux de créer des espaces de travail distincts pour chacune.

{% alert tip %}
Cette approche est particulièrement utile pour des entreprises telles que les studios de jeux mobiles, qui peuvent gérer des espaces de travail individuels pour chacun de leurs jeux, ou les sites d'e-commerce qui souhaitent des espaces de travail séparés pour chaque région dans laquelle ils opèrent.
{% endalert %}

## Planification des espaces de travail {#planning-workspaces}

Vous devez créer des instances d'application distinctes pour chaque version de votre application sur chaque plateforme. Lorsque vous décidez quelles instances d'application inclure dans un espace de travail, réfléchissez aux utilisateurs que vous souhaitez cibler et regroupez-les en conséquence.

L'idée de regrouper plusieurs instances d'application dans un même espace de travail peut être tentante, car cela vous permet d'appliquer une limitation du débit à l'ensemble de votre portefeuille d'applications. Cependant, nous recommandons comme bonne pratique de ne regrouper que les différentes versions d'une même application (ou d'applications très similaires) dans un seul espace de travail.

### Espaces de travail partagés {#shared-workspaces}

Voici des exemples courants où vous pourriez souhaiter avoir plusieurs instances d'application dans le même espace de travail :

- Lorsque vous avez plusieurs applications presque identiques sur différentes plateformes
- Lorsque vous avez différentes révisions majeures de l'application, mais souhaitez continuer à engager les mêmes utilisateurs lors de leur mise à jour
- Lorsque vous avez différentes versions de l'application dans lesquelles le même utilisateur peut entrer ou sortir (par exemple, de la version gratuite à la version premium)

#### Impact sur les filtres de segmentation {#impact-on-segmentation-filters}

Quelle que soit la combinaison d'applications que vous choisissez de regrouper dans un espace de travail, leurs données seront agrégées. Cela aura un impact notable sur les filtres de segmentation suivants dans Braze (cette liste n'est pas exhaustive) :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Argent dépensé dans l'application
- Abonnement push (cela devient une situation de tout ou rien : si vos utilisateurs se désabonnent d'une application, ils sont désabonnés de toutes les applications de l'espace de travail.)
- Abonnement e-mail (cela devient une situation de tout ou rien et peut vous exposer à des problèmes de conformité.)

{% alert note %}
L'agrégation des données entre les instances d'application dans ces filtres est la raison pour laquelle nous déconseillons d'héberger des applications sensiblement différentes dans le même espace de travail. Cela peut rendre le ciblage compliqué !
{% endalert %}

### Espaces de travail séparés {#separate-workspaces}

Dans d'autres cas, vous pouvez souhaiter disposer de plusieurs espaces de travail séparés. Voici des exemples courants :

- Des espaces de travail séparés pour les environnements de développement et de production de la même application
- Des sous-marques différentes, par exemple une entreprise de jeux mobiles qui propose plusieurs jeux
- Des localisations différentes de la même application ou du même site web opérant dans différents pays ou ciblant différentes langues

### Considérations importantes {#important-considerations}

N'oubliez pas que les espaces de travail fonctionnent comme des silos de données séparés. Toutes les données, qu'il s'agisse de données utilisateur ou de ressources marketing, sont stockées au sein d'un espace de travail. Ces données ne peuvent pas être facilement partagées en dehors de cet espace de travail.

Les éléments suivants sont tous des éléments clés configurés au sein d'un espace de travail :

- [Instances d'application](#app-instances)
- [Teams](#teams)
- [Autorisations des utilisateurs de l'entreprise](#company-user-permissions) (mais pas les utilisateurs eux-mêmes)
- [Connecteurs Currents](#currents-connectors)
- [Profils utilisateur](#user-profiles) et les données utilisateur associées
- [Segments, Campaigns et Canvas](#segments-campaigns-and-canvases)

#### Instances d'application {#app-instances}

Vous devez créer des instances d'application distinctes pour chaque version de votre application sur chaque plateforme. Par exemple, si vous avez des versions Gratuite et Pro de votre application sur iOS et Android, créez quatre instances d'application dans votre espace de travail (application iOS gratuite, application Android gratuite, application iOS pro et application Android pro). Cela vous donnera quatre clés API à utiliser, une pour chaque instance d'application.

#### Teams {#teams}

Les [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) peuvent être configurées en fonction de la localisation de la base de clients, de la langue et d'attributs personnalisés afin que les membres et non-membres d'une équipe aient des accès différents aux fonctionnalités d'envoi de messages et aux données clients.

#### Autorisations des utilisateurs de l'entreprise {#company-user-permissions}

Les espaces de travail disposent de définitions indépendantes d'accès et d'autorisations utilisateur. Les [autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) vous permettent de créer des contrôles granulaires concernant ce à quoi un utilisateur individuel du tableau de bord ou une équipe a accès au sein d'un seul espace de travail.

#### Connecteurs Currents {#currents-connectors}

L'outil [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) est un flux de données en temps réel de vos événements d'engagement, constituant l'exportation la plus robuste et la plus granulaire de la plateforme Braze. Les connecteurs Currents sont inclus avec certains forfaits Braze, et vous en avez peut-être initialement reçu un, en supposant un seul espace de travail.

Lorsque vous décidez de créer des espaces de travail séparés ou combinés, il est important de prendre en compte le nombre de connecteurs Currents dont vous disposez, car les connecteurs Currents ne sont pas partagés entre les espaces de travail.

Par exemple, si vous avez des espaces de travail séparés pour les environnements de développement et de production de la même application, activez votre connecteur Currents dans l'espace de travail de production. Pour activer Currents dans les deux espaces de travail, vous devrez acheter un connecteur Currents supplémentaire.

#### Profils utilisateur {#user-profiles}

Toutes les données persistantes associées à un utilisateur sont stockées dans son [profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Cependant, les profils utilisateur sont également une excellente ressource pour la résolution des problèmes et les tests, car vous pouvez facilement accéder aux informations sur l'historique d'engagement d'un utilisateur, son appartenance à un segment, son appareil et son système d'exploitation.

#### Segments, Campaigns et Canvas {#segments-campaigns-and-canvases}

Un Segment, une Campaign ou un Canvas ne peut pas référencer ou accéder aux données hébergées dans un autre espace de travail. À l'inverse, lorsque plusieurs applications sont dans le même espace de travail, toutes les applications verront leurs données agrégées. Cela aura un [impact sur les filtres dans Braze](#impact-on-segmentation-filters).

### Vue d'ensemble de chaque approche {#overview-of-each-approach}

Le tableau suivant décrit les avantages et inconvénients de ces deux approches de planification des espaces de travail :

- **Espaces de travail et profils utilisateur séparés :** un espace de travail contient une instance d'application et une personne dispose d'un profil utilisateur pour cette instance d'application.
- **Espaces de travail et profils utilisateur partagés :** un espace de travail contient plusieurs instances d'application et une personne dispose d'un profil utilisateur pour l'ensemble de ces instances d'application.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
</style>

<table aria-label="Vue d'ensemble de chaque approche">
  <caption>Vue d'ensemble de chaque approche</caption>
    <thead>
    <tr>
        <th></th>
        <th colspan="2" scope="colgroup">Espaces de travail séparés</th>
        <th colspan="2" scope="colgroup">Espaces de travail partagés</th>
    </tr>
    <tr>
        <th></th>
        <th scope="col">Avantages</th>
        <th scope="col">Inconvénients</th>
        <th scope="col">Avantages</th>
        <th scope="col">Inconvénients</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th scope="row">Ciblage</th>
        <td>Moyen le plus sûr de garder les communications séparées. Les Campaigns sont garanties de ne cibler que des profils utilisateur spécifiques.</td>
        <td>Impossible d'envoyer des messages promotionnels croisés même si vous savez qu'un utilisateur possède un autre profil utilisateur dans un espace de travail différent.</td>
        <td>Possibilité d'envoyer des messages promotionnels croisés si vous savez qu'un utilisateur dispose de plusieurs applications dans votre espace de travail.<br><br>Possibilité de référencer les données utilisateur de l'ensemble des applications. Par exemple, Jean possède l'attribut X pertinent pour l'application 1 et l'attribut Y pertinent pour l'application 2, et les deux peuvent être référencés dans une seule Campaign.</td>
        <td>Plus de risques d'erreur humaine : vous pourriez accidentellement cibler des utilisateurs sur plusieurs instances d'application.<br><br>Pour envoyer des messages in-app, vous devez disposer d'événements personnalisés spécifiques à chaque application afin qu'une Campaign ne s'affiche pas dans une autre application par accident. Par exemple, <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Événements et attributs personnalisés</th>
        <td>Les attributs et événements personnalisés sont garantis d'être spécifiques à une instance d'application.</td>
        <td>Impossible de suivre le comportement des utilisateurs entre les espaces de travail.<br><br><b>Astuce :</b> vous pouvez tirer parti de plusieurs connecteurs Currents pour y parvenir.</td>
        <td>Possibilité de suivre le comportement des utilisateurs sur toutes les instances d'application de l'espace de travail.</td>
        <td>Les attributs et événements personnalisés s'appliqueraient à toutes les instances d'application, ce qui pourrait rendre difficile l'identification des données pertinentes pour chaque instance dans un profil utilisateur. Par exemple, « date_of_parking » est-il pertinent pour l'application 1 ou l'application 2 ? Pour y remédier, assurez-vous d'utiliser des conventions de nommage bien structurées.</td>
    </tr>
    <tr>
        <th scope="row">Limite de fréquence</th>
        <td>La limite de fréquence peut être définie séparément pour chaque instance d'application (basée sur l'espace de travail).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>La limite de fréquence s'applique à toutes les Campaigns, et non par application, ce qui rend plus difficile la prévention de la sur-sollicitation des clients.</td>
    </tr>
    <tr>
        <th scope="row">Statut d'abonnement des profils utilisateur</th>
        <td>Le statut d'abonnement de chaque profil utilisateur est unique à chaque instance d'application.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Les statuts d'abonnement d'un profil utilisateur sont combinés entre les instances d'application.<br><br><b>Astuce :</b> vous pourriez utiliser des <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>attributs personnalisés</a> pour gérer les abonnements de vos utilisateurs à la place.</td>
    </tr>
    <tr>
        <th scope="row">Autorisations des utilisateurs de l'entreprise</th>
        <td>N/A</td>
        <td>La mise à jour des <a href='/docs/user_guide/administer/global/user_management/permissions'>autorisations utilisateur</a> pour un utilisateur du tableau de bord doit être effectuée séparément pour chaque espace de travail auquel l'utilisateur a besoin d'accéder.</td>
        <td>Les <a href='/docs/user_guide/administer/global/user_management/permissions'>autorisations utilisateur</a> peuvent être définies une seule fois pour un utilisateur du tableau de bord, et il disposera des mêmes autorisations pour toutes les instances d'application de l'espace de travail.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Duplication de contenu</th>
        <td>N/A</td>
        <td>Certains contenus, tels que les Segments et les campagnes de cartes de contenu, ne peuvent pas être copiés entre les espaces de travail.</td>
        <td>Possibilité de <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces'>copier des Campaigns, des Canvas et des pages de destination entre les espaces de travail</a>. Les contenus pris en charge incluent les Campaigns et les Canvas pour les canaux éligibles, ainsi que les pages de destination, les modèles d'e-mail, les feature flags et les Content Blocks.<br><br>Possibilité de dupliquer des Segments, des Campaigns, des Canvas et des pages de destination pour réutiliser du contenu d'une instance d'application à une autre.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Analyse</th>
        <td>Les statistiques globales seront exactes sur la page d'accueil.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Les statistiques globales seront agrégées pour toutes les instances d'application de l'espace de travail sur la page d'accueil.</td>
    </tr>
    </tbody>
</table>

{% alert note %}
Pour savoir en quoi les MAU diffèrent selon que vous consultez toutes les applications ou une seule application, consultez [Utilisateurs actifs mensuels]({{site.baseurl}}/user_guide/analytics/dashboards/home#monthly-active-users).
{% endalert %}

## Bonnes pratiques {#best-practices}

### Configurer un espace de travail de test {#set-up-a-testing-workspace}

En tant que bonne pratique, chaque fois que vous prévoyez de configurer un espace de travail de production (un espace de travail qui enverra des messages à de vrais utilisateurs), vous devriez également configurer un espace de travail de test. Un espace de travail de test est un duplicata de votre espace de travail de production sans aucune donnée utilisateur réelle.

Ceci est considéré comme une bonne pratique pour plusieurs raisons :

- **Isolation des modifications :** cela vous permet de tester de nouvelles fonctionnalités, configurations ou mises à jour dans un environnement isolé sans affecter votre environnement de production en direct or en ligne/en production/instantané. Ainsi, si quelque chose se passe mal pendant les tests, votre environnement de production reste inchangé.
- **Tests précis :** cela permet des tests plus précis puisque les données de l'environnement de test peuvent être contrôlées et manipulées sans se soucier des données réelles.
- **Débogage :** il est plus facile de déboguer les problèmes dans un environnement de test, car vous pouvez librement manipuler l'environnement sans craindre d'impacter l'environnement de production.
- **Formation :** les nouveaux membres de l'équipe peuvent se familiariser avec l'espace de travail dans un environnement sûr où les erreurs n'auront pas de conséquences réelles.

{% alert tip %}
L'ordre dans lequel vous configurez un espace de travail de test et un espace de travail de production peut dépendre de vos besoins et circonstances spécifiques. Cependant, il est généralement judicieux de configurer d'abord un espace de travail de test. Cela vous permet de tester les fonctionnalités, configurations et mises à jour avant qu'elles ne soient implémentées dans l'espace de travail de production. Une fois que vous êtes satisfait des tests et des résultats, vous pouvez alors mettre en place votre espace de travail de production.
{% endalert %}

### Ajouter des administrateurs {#add-administrators}

Vous devriez avoir plus d'un utilisateur Braze disposant de permissions d'administrateur pour un même espace de travail. Cela garantit qu'il y a suffisamment de personnes dans votre organisation pour gérer les permissions des autres utilisateurs.

## Étapes suivantes {#next-steps}

Après avoir déterminé le plan de votre espace de travail, il est temps de créer votre espace de travail et d'ajouter des instances d'application. Pour connaître les étapes, consultez [Créer et gérer des espaces de travail]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).