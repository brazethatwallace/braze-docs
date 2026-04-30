---
nav_title: Personnaliser les pages d'accueil
article_title: Personnaliser les pages d'accueil
description: "Cet article explique comment personnaliser les pages d'accueil Braze avec l'éditeur par glisser-déposer."
page_order: 4
---

# Personnaliser les pages d'accueil {#personalize-landing-pages}

> Utilisez la personnalisation Liquid dans les pages d'accueil pour adapter dynamiquement le contenu avec les données du profil utilisateur. Par exemple, vous pouvez personnaliser les titres en fonction de différents attributs utilisateur sans avoir à gérer plusieurs pages d'accueil statiques.

{% alert important %}
La personnalisation Liquid pour les pages d'accueil n'est disponible que sur le niveau Pro des pages d'accueil. Actuellement, le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), le [multilingue]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/) et les [codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/) ne sont pas pris en charge avec la personnalisation Liquid dans les pages d'accueil.
{% endalert %}

## Insérer du Liquid {#inserting-liquid}

Dans l'éditeur par glisser-déposer, vous pouvez insérer de la personnalisation Liquid à la fois dans l'éditeur et dans les paramètres de la page ou du bloc dans le panneau de droite. Pour des instructions sur l'implémentation de Liquid, consultez notre [documentation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#using-liquid) dédiée.

![Éditeur de page d'accueil avec personnalisation Liquid ajoutée.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Prévisualisation et test {#previewing-and-testing}

Lors de la prévisualisation d'une page d'accueil dans l'éditeur, vous pouvez afficher la page en tant qu'utilisateur aléatoire, utilisateur existant ou utilisateur personnalisé.

Cependant, lors de la prévisualisation de la page d'accueil depuis le tableau de données ou la page **Détails de la page d'accueil**, vous ne pourrez la visualiser qu'en tant qu'utilisateur aléatoire.

## Considérations relatives à la personnalisation {#personalization-considerations}

Pour maintenir des performances optimales avec les pages d'accueil personnalisées, notez les limites de taille suivantes :

- **Enregistrement d'une page d'accueil :** si la taille dépasse 500&nbsp;Ko, vous pouvez recevoir un message d'avertissement indiquant que la page a dépassé nos limites de taille, ce qui peut empêcher sa publication.
- **Rendu avec personnalisation Liquid :** la taille totale ne doit pas dépasser 1&nbsp;Mo. Sinon, la page peut être automatiquement dépubliée par Braze.

### Éviter la dépublication des pages d'accueil {#avoid-unpublishing-landing-pages}

Si votre page dépasse ces limites de taille, vous recevrez un e-mail indiquant qu'elle pourrait être dépubliée si elle continue à dépasser la limite. Lorsque le seuil est atteint, la page sera automatiquement dépubliée et vous recevrez une notification.

Pour éviter que votre page ne dépasse les limites de taille ou ne connaisse des temps de chargement lents, assurez-vous d'utiliser une personnalisation Liquid qui :

- Ne boucle pas continuellement et ne référence pas de grands ensembles de données.
- Ne repose pas sur une logique mathématique ou conditionnelle étendue au sein du bloc Liquid.

De plus, évitez d'intégrer directement dans le code de votre page d'accueil des scripts volumineux, des feuilles de style et des ressources encodées en base64. Ces ressources en ligne comptent dans la limite de taille de la page et peuvent ralentir le rendu. Téléchargez plutôt les polices, images, feuilles de style et scripts dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Les ressources servies depuis la bibliothèque multimédia sont hébergées sur le réseau de diffusion de contenu de Braze, elles ne sont donc pas traitées pour le rendu Liquid et ne comptent pas dans la limite de taille de la page.

### Utiliser Liquid pour les utilisateurs identifiés et anonymes {#use-liquid-for-identified-and-anonymous-users}

Liquid peut personnaliser l'expérience de la page d'accueil pour les visiteurs identifiés et anonymes.

- **Utilisateurs identifiés :** créez un lien vers la page d'accueil depuis un message Braze et incluez l'[étiquette Liquid de page d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/#using-landing-page-liquid-tags). Cela associe l'utilisateur à son profil Braze et personnalise l'expérience de la page.
- **Visiteurs anonymes :** utilisez Liquid pour du contenu contextuel non basé sur le profil, comme un nombre aléatoire ou un message d'accueil selon l'heure de la journée.

## Pages de secours {#fallback-pages}

Si vos utilisateurs tentent d'accéder à une page qui a été dépubliée, ils verront un message indiquant que la page ne peut pas être chargée actuellement. Les raisons pour lesquelles une page a été dépubliée incluent :

- Un Liquid complexe ou défectueux, pouvant entraîner des temps de rendu longs
- Des problèmes de réseau côté utilisateur
- Le dépassement des limites maximales de taille de la page d'accueil