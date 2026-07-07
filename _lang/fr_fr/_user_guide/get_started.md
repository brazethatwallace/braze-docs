---
nav_title: Commencer
article_title: "Pour commencer : Aperçu de Braze"
page_order: 1
page_type: reference
description: "Familiarisez-vous avec les concepts fondamentaux à connaître pour travailler avec Braze."

---

# Pour commencer : Aperçu de Braze {#get-started-braze-overview}

> Bienvenue dans Braze ! Cette collection d'articles vous aidera à prendre en main notre plateforme et vous présentera les termes clés, les fonctionnalités et les caractéristiques de Braze. Cette page présente les concepts fondamentaux que vous devrez connaître pour travailler avec Braze.

{% alert tip %}
Nous vous recommandons vivement de suivre notre cours gratuit [Parcours d'apprentissage pour les praticiens](https://learning.braze.com/page/practitioner) en complément de ces articles. Aucun identifiant ou compte spécial n'est nécessaire. Si vous êtes développeur et que vous recherchez une présentation technique de Braze, consultez également la rubrique [Démarrage pour les développeurs]({{site.baseurl}}/developer_guide/getting_started/platform_overview).
{% endalert %}

Dans les sections Démarrage, nous nous concentrons sur les déploiements courants de Braze. Cependant, Braze est extrêmement flexible et peut être personnalisé pour apporter de la valeur à votre organisation de multiples façons. Par souci de clarté et de concision, nous avons fourni un aperçu descriptif de la configuration par défaut plutôt que des instructions rigides. Nous savons que chaque organisation a des besoins distincts, et Braze est conçu pour offrir une large gamme d'options de personnalisation adaptables à vos exigences spécifiques.

Explorons ensemble la puissance de Braze.

## Comment fonctionne Braze {#how-braze-works}

Braze est une plateforme d'engagement client qui aide les marques de toutes tailles à créer des campagnes personnalisées et ciblées sur différents canaux. Braze vous donne la possibilité d'écouter vos clients, de comprendre ce que leur comportement signifie, puis d'agir en envoyant le bon message, par le bon canal, au bon moment.

{% alert tip %}
N'oubliez pas d'[ajouter vos collègues à Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) pour qu'ils puissent explorer la plateforme avec vous.
{% endalert %}

## Utilisateurs et segments {#users-and-segments}

Les utilisateurs sont vos clients, c'est-à-dire les personnes qui reçoivent les messages que vous envoyez via Braze. Toutes les données que vous collectez sur un utilisateur et que vous ingérez dans Braze sont stockées dans son profil utilisateur : données démographiques, informations personnelles, préférences et comportements. Ces informations alimentent votre envoi de messages et vous permettent d'adapter vos messages au bon utilisateur.

![Capture d'écran liée aux utilisateurs et aux segments.]({% image_buster /assets/img/getting_started/user_profile.png %})

Les segments divisent votre base de clients en groupes plus petits que vous pouvez ensuite cibler avec des messages spécifiques. Vous pouvez utiliser différentes variables pour créer des segments, allant de caractéristiques telles que le genre, la localisation et l'âge à des comportements tels que les schémas d'interaction avec les campagnes précédentes ou la position dans le parcours client.

Les segments sont dynamiques : les utilisateurs peuvent entrer et sortir des segments en temps réel en fonction de leur comportement et de leur relation avec votre marque. Vos clients reçoivent ainsi les messages les plus pertinents à tout moment. Vous pouvez créer autant de segments que nécessaire pour vos objectifs de ciblage et d'envoi de messages.

![Les segments sont dynamiques : les utilisateurs peuvent entrer et sortir des segments en temps réel en fonction de leur comportement et de leur relation avec votre marque. Vos clients reçoivent ainsi les messages les plus pertinents à tout moment. Vous pouvez créer autant de segments que nécessaire pour vos objectifs de ciblage et d'envoi de messages.]({% image_buster /assets/img/getting_started/segment.png %})

Pour en savoir plus, consultez : [Pour commencer : Utilisateurs et segments]({{site.baseurl}}/user_guide/get_started/users_and_segments).

## Campaigns et Canvas {#campaigns-and-canvases}

Les Campaigns et les Canvas vous permettent d'envoyer des messages à vos utilisateurs.

Les Campaigns sont idéales pour les messages uniques envoyés à un segment d'audience spécifique sur différents canaux. Vous pouvez exploiter tous les canaux de communication pris en charge dans votre Campaign (e-mail, notification push, messages in-app, SMS, et plus encore).

Les Canvas sont des workflows avancés qui vous permettent d'automatiser et d'orchestrer des parcours clients personnalisés sur plusieurs canaux. Dans un Canvas, vous pouvez mettre en place une logique de branchement, des délais, des points de décision et des événements de conversion pour guider les clients à travers une série d'interactions. Les Canvas assurent une communication cohérente et fluide sur différents points de contact, augmentant ainsi les chances d'engagement et de conversion des clients.

Pour en savoir plus, consultez : [Pour commencer : Campaigns et Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).

## Espaces de travail {#workspaces}

Les espaces de travail regroupent vos données — utilisateurs, segments, Campaigns et Canvas — en un seul emplacement. Les informations ne sont pas partagées entre les espaces de travail, gardez donc cela à l'esprit lorsque vous ajoutez des sites web et des applications à vos espaces de travail. Nous vous conseillons de ne regrouper que les différentes versions d'une même application ou d'applications très similaires au sein d'un même espace de travail.

Voici quelques exemples d'utilisation des espaces de travail :

- Différentes lignes de produits ou applications
- Différentes audiences (par exemple, les livreurs et les clients)
- Entreprises distinctes
- Environnement de test

Pour en savoir plus, consultez : [Pour commencer : Espaces de travail]({{site.baseurl}}/user_guide/get_started/workspaces).

## Intégrer Braze {#integrating-braze}

Braze est conçu pour être opérationnel rapidement et facilement. Notre délai moyen de rentabilisation est de six semaines pour notre clientèle composée de centaines de marques.

![Capture d'écran liée à l'intégration de Braze.]({% image_buster /assets/img/getting_started/timetovalue.png %})

Voici le cadre proposé par Braze pour estimer la durée de votre intégration, basé sur quatre composants sur lesquels vous pouvez travailler en parallèle. La fourchette habituelle est de 30 à 180 jours, la plupart des comptes achevant leur intégration dans un délai de 45 à 60 jours.

- **Niveau de complexité de la migration des campagnes :** Le temps nécessaire à la migration des campagnes dépend de leur nombre, de leur degré de personnalisation et de vos ressources. Si vous avez moins de dix campagnes à migrer, cela prendra moins de 60 jours. En revanche, si vous avez plus de 100 campagnes, ce sera plus complexe. Une seule personne qui migre 100 campagnes, ce n'est pas la même chose que 10 personnes qui en migrent 100.

{% alert tip %}
Besoin d'aide pour votre migration ? Nos [partenaires certifiés Braze](https://www.braze.com/partners/solutions-partners) peuvent vous aider !
{% endalert %}

- **Volume d'e-mails :** Pour envoyer des e-mails, vous devez réchauffer vos adresses IP. L'[IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) est le processus qui consiste à établir la réputation de l'expéditeur avec vos nouvelles adresses IP. Si vous envoyez moins de 2 à 3 millions d'e-mails par jour, le réchauffement devrait prendre 30 jours ou moins. Gardez à l'esprit vos pics d'envoi. Si vous envoyez normalement 2 millions d'e-mails par jour mais que vous prévoyez d'en envoyer 7 millions pendant une période saisonnière, c'est ce « pic » d'envoi que vous devez viser lors du réchauffement. Les expéditeurs à fort volume peuvent utiliser plusieurs adresses IP pour accélérer le processus.
- **Complexité organisationnelle :** Notre processus d'onboarding peut s'adapter aux besoins de votre entreprise. Que vous soyez une seule unité commerciale, que vous disposiez d'un centre d'excellence, de plusieurs unités indépendantes, ou que vous fassiez appel à des agences pour renforcer vos équipes, Braze a l'expérience de tous ces scénarios.
- **Sophistication de l'infrastructure de données :** Si vous ne déployez que le SDK Braze ou si vous disposez déjà d'une plateforme de données client (CDP), il est possible de tout configurer en seulement 30 jours. L'utilisation d'une CDP moderne peut accélérer le processus. En revanche, si vous avez de nombreux systèmes back-end, outils ou bases de données à connecter à Braze, cela peut prendre plus de temps et nécessiter davantage de ressources dédiées pour finaliser la configuration.

Pour en savoir plus, consultez : [Pour commencer : Aperçu de l'intégration]({{site.baseurl}}/user_guide/get_started/integrations).