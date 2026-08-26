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
Nous vous recommandons vivement de suivre notre cours gratuit [Parcours d'apprentissage pour les praticiens](https://learning.braze.com/page/practitioner) en complément de ces articles. Aucun identifiant ou compte spécial n'est nécessaire. Si vous êtes développeur et que vous recherchez une présentation technique de Braze, consultez également la rubrique <a href="/docs/developer_guide/getting_started/platform_overview">Démarrage pour les développeurs</a>.
{% endalert %}

Dans les sections Démarrage, nous nous concentrons sur les déploiements courants de Braze. Cependant, Braze est extrêmement flexible et peut être personnalisé pour apporter de la valeur à votre organisation de multiples façons. Par souci de clarté et de concision, nous avons fourni un aperçu descriptif de la configuration par défaut plutôt que des instructions rigides. Nous savons que chaque organisation a des besoins distincts, et Braze est conçu pour offrir une large gamme d'options de personnalisation adaptables à vos exigences spécifiques.

Explorons ensemble la puissance de Braze.

## Comment fonctionne Braze {#how-braze-works}

Braze est une plateforme d'engagement client qui aide les marques de toutes tailles à créer des campagnes personnalisées et ciblées sur différents canaux. Braze vous offre la possibilité d'écouter vos clients, de comprendre ce que leur comportement signale, puis d'agir en envoyant le bon message, par le bon canal, au bon moment.

{% alert tip %}
N'oubliez pas d'[ajouter vos collègues à Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) afin qu'ils puissent explorer la plateforme avec vous.
{% endalert %}

## Utilisateurs et Segments {#users-and-segments}

Les utilisateurs sont vos clients, c'est-à-dire les personnes qui reçoivent les messages que vous envoyez via Braze. Toutes les données que vous collectez sur un utilisateur et que vous ingérez dans Braze sont stockées dans son profil utilisateur, telles que ses données démographiques, ses informations personnelles, ses préférences et ses comportements. Ces informations alimentent votre communication et vous permettent d'adapter vos messages au bon utilisateur.

![Capture d'écran relative aux utilisateurs et aux Segments.]({% image_buster /assets/img/getting_started/user_profile.png %})

Les Segments divisent votre base de clients en groupes plus petits que vous pouvez ensuite cibler avec des messages spécifiques. Vous pouvez utiliser différentes variables pour créer des Segments, allant de caractéristiques telles que le genre, la localisation et l'âge à des comportements comme les schémas d'interaction avec les Campaigns précédentes ou la position de l'utilisateur dans le parcours client.

Les Segments sont dynamiques : les utilisateurs peuvent entrer et sortir des Segments en temps réel en fonction de leur comportement et de leur relation avec votre marque. Cela garantit que vos clients reçoivent les messages les plus pertinents à tout moment. Vous pouvez créer autant de Segments que nécessaire pour vos besoins de ciblage et de communication.

![Les Segments sont dynamiques : les utilisateurs peuvent entrer et sortir des Segments en temps réel en fonction de leur comportement et de leur relation avec votre marque. Cela garantit que vos clients reçoivent les messages les plus pertinents à tout moment. Vous pouvez créer autant de Segments que nécessaire pour vos besoins de ciblage et de communication.]({% image_buster /assets/img/getting_started/segment.png %})

Pour en savoir plus, consultez : [Pour commencer : Utilisateurs et Segments]({{site.baseurl}}/user_guide/get_started/users_and_segments).

## Campaigns et Canvas {#campaigns-and-canvases}

Les Campaigns et les Canvas sont les moyens par lesquels vous envoyez des messages à vos utilisateurs.

Les Campaigns sont idéales pour envoyer des messages uniques à un Segment d'audience spécifique sur différents canaux. Vous pouvez tirer parti de n'importe lequel de nos canaux de communication pris en charge dans votre Campaign (e-mail, notification push, In-App Messages, SMS, et plus encore).

Les Canvas sont des workflows avancés qui vous permettent d'automatiser et d'orchestrer des parcours clients personnalisés sur plusieurs canaux. Au sein d'un Canvas, vous pouvez configurer une logique de branchement, des délais, des points de décision et des événements de conversion pour guider les clients à travers une série d'interactions. Les Canvas contribuent à garantir une communication cohérente et fluide sur les différents points de contact, augmentant ainsi les chances d'engagement et de conversion des clients.

Pour en savoir plus, consultez : [Pour commencer : Campaigns et Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).

## Espaces de travail {#workspaces}

Les espaces de travail regroupent vos données — utilisateurs, Segments, Campaigns et Canvas — en un seul endroit. Les informations ne sont pas partagées entre les espaces de travail, gardez donc cela à l'esprit lorsque vous ajoutez des sites web et des applications à vos espaces de travail. Nous recommandons, comme bonne pratique, de ne regrouper sous un même espace de travail que les différentes versions d'une même application ou d'applications très similaires.

Exemples d'utilisation des espaces de travail :

- Différentes gammes de produits ou applications
- Différentes audiences (comme les livreurs par rapport aux clients)
- Entreprises distinctes
- Environnement de test

Pour en savoir plus, consultez : [Pour commencer : Espaces de travail]({{site.baseurl}}/user_guide/get_started/workspaces).

## Intégrer Braze {#integrating-braze}

Braze est conçu pour être opérationnel rapidement et facilement. Notre délai moyen de retour sur investissement est de six semaines pour l'ensemble de notre base de clients composée de centaines de marques.

![Capture d'écran liée à l'intégration de Braze.]({% image_buster /assets/img/getting_started/timetovalue.png %})

Voici le cadre de référence Braze pour estimer la durée de votre intégration, basé sur quatre composantes sur lesquelles vous pouvez travailler en parallèle. La fourchette typique est de 30 à 180 jours, la plupart des comptes finalisant leur intégration en 45 à 60 jours.

- **Niveau de complexité de la migration des Campaigns :** le temps nécessaire pour migrer des Campaigns dépend de leur nombre, de leur degré de personnalisation et de vos ressources. Si vous avez moins de dix Campaigns à migrer, cela prendra moins de 60 jours. Mais si vous en avez plus de 100, ce sera plus complexe. La situation est différente si une seule personne migre 100 Campaigns ou si dix personnes s'en chargent.

{% alert tip %}
Besoin d'aide pour votre migration ? Nos [partenaires Braze certifiés](https://www.braze.com/partners/solutions-partners) peuvent vous accompagner !
{% endalert %}

- **Volume d'e-mails :** pour envoyer des e-mails, vous devrez chauffer vos adresses IP. L'[IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) est le processus de construction de la réputation de l'expéditeur avec vos adresses IP nouvellement attribuées. Si vous envoyez moins de 2 à 3 millions d'e-mails par jour, votre IP warming devrait prendre 30 jours ou moins. Gardez à l'esprit vos pics d'envoi. Si vous envoyez habituellement 2 millions d'e-mails par jour mais prévoyez d'en envoyer 7 millions lors d'une période saisonnière, c'est ce volume « de pointe » que vous devriez atteindre lors du warming. Les expéditeurs à fort volume peuvent utiliser plusieurs adresses IP pour accélérer le processus de warming.
- **Complexité organisationnelle :** notre processus d'onboarding peut s'adapter aux besoins de votre entreprise. Que vous soyez une unité commerciale unique, que vous disposiez d'un centre d'excellence, de plusieurs unités indépendantes ou que vous fassiez appel à des agences pour renforcer vos équipes, Braze a l'expérience de tous ces scénarios.
- **Sophistication de l'infrastructure de données :** si vous implémentez uniquement le SDK Braze ou si vous disposez déjà d'une plateforme de données client (CDP), il est possible de tout mettre en place en seulement 30 jours. L'utilisation d'une CDP moderne peut accélérer le processus. En revanche, si vous avez de nombreux systèmes backend, outils ou bases de données à connecter avec Braze, cela peut prendre plus de temps et nécessiter davantage de ressources dédiées pour finaliser la configuration.

Pour en savoir plus, consultez : [Pour commencer : aperçu de l'intégration]({{site.baseurl}}/user_guide/get_started/integrations).