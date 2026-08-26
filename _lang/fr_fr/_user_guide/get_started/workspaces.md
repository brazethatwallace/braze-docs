---
nav_title: Espaces de travail
article_title: "Pour commencer : Espaces de travail"
page_order: 3
page_type: reference
description: "Tout ce que vous faites dans la plateforme Braze se produit au sein d'un espace de travail. Cet article décrit leur fonctionnement et les éléments importants à prendre en compte lors de la planification de vos espaces de travail dans Braze."
---

# Pour commencer : Espaces de travail {#get-started-workspaces}

> Tout ce que vous faites dans la plateforme Braze se produit au sein d'un espace de travail. Les espaces de travail agissent comme des silos de données distincts et vous permettent de séparer différentes marques ou activités. Plusieurs versions de votre site web ou de votre application mobile peuvent envoyer des données au même espace de travail. Les différents sites et applications rassemblés au sein d'un espace de travail sont appelés des « instances d'applications ».

## Comprendre les espaces de travail {#understanding-workspaces}

Les espaces de travail remplissent deux fonctions clés :

- **Unifier les données utilisateur :** lorsque plusieurs instances d'application se trouvent dans un même espace de travail, vous pouvez collecter et cibler les données utilisateur de façon fluide entre les différentes versions de votre application, comme iOS, Android et le web. Cela garantit que vous disposez toujours d'informations à jour sur chaque utilisateur, quelle que soit la plateforme qu'il utilise.
- **Séparer des activités distinctes :** les espaces de travail permettent également de garder des marques ou des activités distinctes séparées. Par exemple, si vous avez plusieurs sous-marques avec des bases d'utilisateurs différentes, il est avantageux de créer des espaces de travail distincts pour chacune.

{% alert tip %}
Cette approche est particulièrement utile pour des entreprises comme les studios de jeux mobiles, qui peuvent gérer des espaces de travail individuels pour chacun de leurs jeux, ou les sites d'e-commerce qui souhaitent des espaces de travail distincts pour chaque région dans laquelle ils opèrent.
{% endalert %}

## Planification des espaces de travail {#planning-workspaces}

Vous devez créer des instances d'application distinctes pour chaque version de votre application sur chaque plateforme. Lorsque vous décidez quelles instances d'application inclure dans un espace de travail, pensez aux utilisateurs que vous souhaitez cibler et regroupez-les en conséquence.

L'idée de regrouper plusieurs instances d'application dans un même espace de travail peut être séduisante, car cela vous permet d'appliquer une limite de débit à l'ensemble de votre portefeuille d'applications. Cependant, en tant que bonne pratique, nous recommandons de ne regrouper que les différentes versions d'applications identiques (ou très similaires) au sein d'un même espace de travail.

### Espaces de travail partagés {#shared-workspaces}

Voici des exemples courants dans lesquels vous pourriez souhaiter avoir plusieurs instances d'application dans le même espace de travail :

- Lorsque vous avez plusieurs applications quasiment identiques sur différentes plateformes
- Lorsque vous avez différentes révisions majeures de l'application, mais souhaitez continuer à interagir avec les mêmes utilisateurs lorsqu'ils effectuent la mise à jour
- Lorsque vous avez différentes versions de l'application entre lesquelles un même utilisateur pourrait basculer (par exemple, de la version gratuite à la version premium)

#### Impact sur les filtres de segmentation {#impact-on-segmentation-filters}

Les données de toutes les applications que vous choisissez de regrouper dans un espace de travail seront agrégées. Cela aura un impact notable sur les filtres de segmentation suivants dans Braze (cette liste n'est pas exhaustive) :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Argent dépensé dans l'application
- Abonnement aux notifications push (cela devient une situation tout ou rien — si vos utilisateurs se désabonnent d'une application, ils sont désabonnés de toutes les applications de l'espace de travail.)
- Abonnement par e-mail (cela devient une situation tout ou rien et peut vous exposer à des problèmes de conformité.)

{% alert note %}
L'agrégation des données entre les instances d'application dans ces filtres est la raison pour laquelle nous déconseillons d'héberger des applications sensiblement différentes au sein du même espace de travail. Cela peut rendre le ciblage complexe !
{% endalert %}

### Espaces de travail séparés {#separate-workspaces}

D'autres fois, vous souhaiterez peut-être avoir plusieurs espaces de travail séparés. Voici des exemples courants :

- Des espaces de travail séparés pour les environnements de développement et de production de la même application
- Des sous-marques différentes, par exemple, une société de jeux mobiles qui propose plusieurs jeux
- Différentes localisations de la même application ou du même site web qui opèrent dans différents pays ou ciblent différentes langues

### Considérations importantes {#important-considerations}

N'oubliez pas que les espaces de travail fonctionnent comme des silos de données séparés. Toutes les données, qu'il s'agisse de données utilisateur ou de ressources marketing, sont stockées au sein d'un espace de travail. Ces données ne peuvent pas être facilement partagées en dehors de cet espace de travail.

Voici les éléments clés qui sont configurés au sein d'un espace de travail :

- [Instances d'application](#app-instances)
- [Teams](#teams)
- [Permissions des utilisateurs de l'entreprise](#company-user-permissions) (mais pas les utilisateurs eux-mêmes)
- [Connecteurs Currents](#currents-connectors)
- [Profils utilisateur](#user-profiles) et les données utilisateur associées
- [Segments, Campaigns et Canvas](#segments-campaigns-and-canvases)

#### Instances d'application {#app-instances}

Vous devez créer des instances d'application distinctes pour chaque version de votre application sur chaque plateforme. Par exemple, si vous avez des versions gratuite et Pro de votre application sur iOS et Android, créez quatre instances d'application dans votre espace de travail (application iOS gratuite, application Android gratuite, application iOS Pro et application Android Pro). Vous obtiendrez ainsi quatre clés API, une pour chaque instance d'application.

#### Teams {#teams}

Les [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) peuvent être configurées en fonction de la localisation de la base client, de la langue et d'attributs personnalisés, afin que les membres et les non-membres d'une équipe aient des accès différents aux fonctionnalités de communication et aux données client.

#### Permissions des utilisateurs de l'entreprise {#company-user-permissions}

Les espaces de travail ont des définitions d'accès et de permissions utilisateur indépendantes. Les [permissions utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) vous permettent de créer des contrôles granulaires concernant ce à quoi un utilisateur individuel du tableau de bord ou une équipe a accès au sein d'un espace de travail unique.

#### Connecteurs Currents {#currents-connectors}

L'outil [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) est un flux de données en temps réel de vos événements d'engagement, qui constitue l'export le plus robuste et le plus granulaire de la plateforme Braze. Les connecteurs Currents sont inclus dans certains packages Braze, et vous en avez peut-être reçu un initialement, en supposant un espace de travail unique.

Lorsque vous décidez entre la création d'espaces de travail séparés ou combinés, il est important de penser au nombre de connecteurs Currents dont vous disposez, car les connecteurs Currents ne sont pas partagés entre les espaces de travail.

Par exemple, si vous avez des espaces de travail séparés pour les environnements de développement et de production de la même application, activez votre connecteur Currents dans l'espace de travail de production. Pour activer Currents dans les deux espaces de travail, vous devrez acheter un connecteur Currents supplémentaire.

#### Profils utilisateur {#user-profiles}

Toutes les données persistantes associées à un utilisateur sont stockées dans son [profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Cependant, les profils utilisateur constituent également une excellente ressource pour la résolution des problèmes et les tests, car vous pouvez facilement accéder aux informations sur l'historique d'engagement d'un utilisateur, son appartenance à des Segments, son appareil et son système d'exploitation.

#### Segments, Campaigns et Canvas {#segments-campaigns-and-canvases}

Un Segment, une Campaign ou un Canvas ne peut pas référencer ni accéder aux données hébergées dans un autre espace de travail. À l'inverse, lorsque plusieurs applications sont dans le même espace de travail, toutes les applications ont leurs données agrégées. Cela aura un [impact sur les filtres dans Braze](#impact-on-segmentation-filters).

### Aperçu de chaque approche {#overview-of-each-approach}

Le tableau suivant décrit les avantages et les inconvénients de ces deux approches de la planification des espaces de travail :

- **Espaces de travail et profils utilisateur séparés :** un espace de travail contient une seule instance d'application et une personne possède un profil utilisateur pour cette instance d'application.
- **Espaces de travail et profils utilisateur partagés :** un espace de travail contient plusieurs instances d'application et une personne possède un profil utilisateur pour toutes ces instances d'application.

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

<table aria-label="Aperçu de chaque approche">
  <caption>Aperçu de chaque approche</caption>
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
        <td>Le moyen le plus sûr de garder les communications séparées. Les campagnes sont garanties de ne cibler que des profils utilisateur spécifiques.</td>
        <td>Impossible d'envoyer des messages promotionnels croisés même si vous savez qu'un utilisateur possède un autre profil utilisateur dans un espace de travail différent.</td>
        <td>Possibilité d'envoyer des messages promotionnels croisés si vous savez qu'un utilisateur possède plusieurs applications dans votre espace de travail.<br><br>Possibilité de référencer les données utilisateur provenant de différentes applications. Par exemple, Jean possède l'attribut X pertinent pour l'application 1 et l'attribut Y pertinent pour l'application 2, et les deux peuvent être référencés dans une même campagne.</td>
        <td>Plus de marge pour l'erreur humaine — vous pourriez accidentellement cibler des utilisateurs à travers plusieurs instances d'application.<br><br>Pour envoyer des messages in-app, vous devez disposer d'événements personnalisés spécifiques à l'application afin qu'une campagne ne s'affiche pas par accident dans une autre application. Par exemple, <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Événements et attributs personnalisés</th>
        <td>Les attributs et événements personnalisés sont garantis d'être spécifiques à une instance d'application.</td>
        <td>Impossible de suivre le comportement des utilisateurs entre les espaces de travail.<br><br><b>Astuce :</b> vous pouvez tirer parti de plusieurs connecteurs Currents pour y parvenir.</td>
        <td>Possibilité de suivre le comportement des utilisateurs à travers toutes les instances d'application de l'espace de travail.</td>
        <td>Les attributs et événements personnalisés s'appliqueraient à toutes les instances d'application, ce qui pourrait rendre difficile l'identification des données pertinentes pour chaque instance dans un profil utilisateur. Par exemple, « date_of_parking » est-il pertinent pour l'application 1 ou l'application 2 ? Pour y remédier, veillez à utiliser des conventions de nommage bien structurées.</td>
    </tr>
    <tr>
        <th scope="row">Limite de fréquence</th>
        <td>La limite de fréquence peut être définie séparément pour chaque instance d'application (en fonction de l'espace de travail).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>La limite de fréquence s'applique à toutes les campagnes, et non par application, ce qui rend plus difficile la prévention du sur-envoi de messages aux clients.</td>
    </tr>
    <tr>
        <th scope="row">Statut d'abonnement des profils utilisateur</th>
        <td>Le statut d'abonnement de chaque profil utilisateur est unique à chaque instance d'application.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Les statuts d'abonnement d'un profil utilisateur sont combinés entre les instances d'application.<br><br><b>Astuce :</b> vous pourriez utiliser des <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>attributs personnalisés</a> pour gérer les abonnements de vos utilisateurs à la place.</td>
    </tr>
    <tr>
        <th scope="row">Permissions des utilisateurs de l'entreprise</th>
        <td>N/A</td>
        <td>La mise à jour des <a href='/docs/user_guide/administer/global/user_management/permissions'>permissions utilisateur</a> pour un utilisateur du tableau de bord doit être effectuée séparément pour chaque espace de travail auquel l'utilisateur a besoin d'accéder.</td>
        <td>Les <a href='/docs/user_guide/administer/global/user_management/permissions'>permissions utilisateur</a> peuvent être définies une seule fois pour un utilisateur du tableau de bord, et il disposera des mêmes permissions pour toutes les instances d'application de l'espace de travail.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Duplication de contenu</th>
        <td>N/A</td>
        <td>Certains contenus, tels que les Segments et les campagnes de cartes de contenu, ne peuvent pas être copiés d'un espace de travail à l'autre.</td>
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
Pour comprendre comment les MAU diffèrent entre l'affichage de toutes les applications et celui d'une seule application, consultez [Utilisateurs actifs mensuels]({{site.baseurl}}/user_guide/analytics/dashboards/home#monthly-active-users).
{% endalert %}

## Bonnes pratiques {#best-practices}

### Configurer un espace de travail de test {#set-up-a-testing-workspace}

En tant que bonne pratique, chaque fois que vous prévoyez de configurer un espace de travail de production (un espace de travail qui enverra des messages à de vrais utilisateurs), vous devriez également configurer un espace de travail de test. Un espace de travail de test est un duplicata de votre espace de travail de production sans aucune donnée utilisateur réelle.

Cela est considéré comme une bonne pratique pour plusieurs raisons :

- **Isolation des modifications :** Cela vous permet de tester de nouvelles fonctionnalités, configurations ou mises à jour dans un environnement isolé sans affecter votre environnement de production en direct. Ainsi, si quelque chose ne se passe pas comme prévu pendant les tests, votre environnement de production reste intact.
- **Tests plus précis :** Cela permet des tests plus précis, car les données de l'environnement de test peuvent être contrôlées et manipulées sans se soucier des données réelles.
- **Débogage :** Il est plus facile de déboguer les problèmes dans un environnement de test, car vous pouvez librement manipuler l'environnement sans risquer d'impacter l'environnement de production.
- **Formation :** Les nouveaux membres de l'équipe peuvent se familiariser avec l'espace de travail dans un environnement sûr où les erreurs n'auront pas de conséquences réelles.

{% alert tip %}
L'ordre dans lequel vous configurez un espace de travail de test et un espace de travail de production peut dépendre de vos besoins et circonstances spécifiques. Cependant, il est généralement recommandé de configurer d'abord un espace de travail de test. Cela vous permet de tester les fonctionnalités, configurations et mises à jour avant qu'elles ne soient implémentées dans l'espace de travail de production. Une fois que vous êtes satisfait des tests et des résultats, vous pouvez alors mettre en place votre espace de travail de production.
{% endalert %}

### Ajouter des administrateurs {#add-administrators}

Vous devriez avoir plus d'un utilisateur Braze disposant de permissions d'administration pour un même espace de travail. Cela garantit qu'il y a suffisamment de personnes dans votre organisation pour gérer les permissions des autres utilisateurs.

## Prochaines étapes {#next-steps}

Après avoir déterminé le plan de votre espace de travail, il est temps de créer votre espace de travail et d'ajouter des instances d'application. Pour les étapes à suivre, consultez [Créer et gérer les espaces de travail]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).