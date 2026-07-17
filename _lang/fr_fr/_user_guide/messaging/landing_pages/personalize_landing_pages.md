---
nav_title: Personnaliser les pages de destination
article_title: Personnaliser les pages de destination
description: "Cet article explique comment personnaliser les pages de destination Braze avec l'éditeur par glisser-déposer."
page_order: 4
---

# Personnaliser les pages de destination {#personalize-landing-pages}

> Utilisez la personnalisation Liquid dans les pages de destination pour adapter dynamiquement le contenu avec les données du profil utilisateur. Par exemple, vous pouvez personnaliser les titres en fonction de différents attributs utilisateur sans avoir à gérer plusieurs pages de destination statiques.

{% alert important %}
La personnalisation Liquid pour les pages de destination n'est disponible que sur le niveau Pro des pages de destination. Actuellement, le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), le [multilingue]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings) et les [codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) ne sont pas pris en charge avec la personnalisation Liquid dans les pages de destination.
{% endalert %}

## Insérer du Liquid {#inserting-liquid}

Dans l'éditeur par glisser-déposer, vous pouvez insérer de la personnalisation Liquid à la fois dans l'éditeur et dans les paramètres de la page ou du bloc dans le panneau de droite. Pour des instructions sur l'utilisation de Liquid, consultez notre [documentation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dédiée.

![Éditeur de page de destination avec personnalisation Liquid ajoutée.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Prévisualisation et test {#previewing-and-testing}

Lors de la prévisualisation d'une page de destination dans l'éditeur, vous pouvez afficher la page en tant qu'utilisateur aléatoire, utilisateur existant ou utilisateur personnalisé.

Cependant, lors de la prévisualisation de la page de destination depuis le tableau de données ou la page **Détails de la page de destination**, vous ne pourrez la visualiser qu'en tant qu'utilisateur aléatoire.

## Considérations relatives à la personnalisation {#personalization-considerations}

Pour maintenir des performances optimales avec les pages de destination personnalisées, notez les limites de taille suivantes :

- **Enregistrement d'une page de destination :** si la taille dépasse 500&nbsp;Ko, vous pouvez recevoir un message d'avertissement indiquant que la page a dépassé nos limites de taille, ce qui peut empêcher sa publication.
- **Rendu avec personnalisation Liquid :** la taille totale ne doit pas dépasser 1&nbsp;Mo. Sinon, la page peut être automatiquement dépubliée par Braze.

### Éviter la dépublication des pages de destination {#avoid-unpublishing-landing-pages}

Si votre page dépasse ces limites de taille, vous recevrez un e-mail indiquant qu'elle pourrait être dépubliée si elle continue à dépasser la limite. Lorsque le seuil est atteint, la page sera automatiquement dépubliée et vous recevrez une notification.

Pour éviter que votre page ne dépasse les limites de taille ou ne connaisse des temps de chargement lents, assurez-vous d'utiliser une personnalisation Liquid qui :

- Ne boucle pas continuellement et ne référence pas de grands ensembles de données.
- Ne repose pas sur une logique mathématique ou conditionnelle étendue au sein du bloc Liquid.

De plus, évitez d'intégrer directement dans le code de votre page de destination des scripts volumineux, des feuilles de style et des ressources encodées en base64. Ces ressources en ligne comptent dans la limite de taille de la page et peuvent ralentir le rendu. Téléchargez plutôt les polices, images, feuilles de style et scripts dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Les ressources servies depuis la bibliothèque multimédia sont hébergées sur le CDN de Braze, elles ne sont donc pas traitées pour le rendu Liquid et ne comptent pas dans la limite de taille de la page.

### Utiliser Liquid pour les utilisateurs identifiés et anonymes {#use-liquid-for-identified-and-anonymous-users}

Liquid peut personnaliser l'expérience de la page de destination pour les visiteurs identifiés et anonymes.

- **Utilisateurs identifiés :** créez un lien vers la page de destination depuis un message Braze et incluez l'[étiquette Liquid de page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users#using-landing-page-liquid-tags). Cela associe l'utilisateur à son profil Braze et personnalise l'expérience de la page.
- **Visiteurs anonymes :** utilisez Liquid pour du contenu contextuel non basé sur le profil, comme un nombre aléatoire ou un message d'accueil selon l'heure de la journée.

### Préremplir les champs de formulaire {#pre-fill-form-fields}

Si un champ de formulaire de page de destination correspond à un attribut du profil utilisateur, vous pouvez préremplir ce champ pour les utilisateurs qui reviennent. Cela permet de réduire les frictions liées au formulaire et d'améliorer les taux de complétion pour les visiteurs connus.

Pour préremplir les champs de formulaire :

1. Sélectionnez votre champ de formulaire dans l'éditeur par glisser-déposer.
2. Dans le panneau de paramètres de droite, associez le champ à l'attribut de profil approprié.
3. Sélectionnez **Préremplir à partir du profil utilisateur**.

![Paramètres du champ de formulaire de la page de destination montrant l'option de préremplissage à partir des données du profil utilisateur.]({% image_buster /assets/img/landing_pages/pre-fill-checkbox.png %}){: style="max-width:70%;"}

Le préremplissage ne fonctionne que pour les [utilisateurs identifiés](#use-liquid-for-identified-and-anonymous-users). Pour les visiteurs anonymes, les champs de formulaire conservent leur état par défaut :

- **Champs de saisie :** affichent leur texte de marque substitutive.
- **Cases à cocher, boutons radio et contrôles similaires :** restent non sélectionnés jusqu'à ce que l'utilisateur interagisse avec eux.

{% alert warning %}
Si un utilisateur transfère un lien de page de destination (depuis un e-mail, un SMS ou un autre message) à une autre personne, le destinataire verra les données préremplies destinées à l'utilisateur d'origine. Il s'agit de la même considération de sécurité qui s'applique aux liens de désabonnement et aux liens du centre de préférences. Tenez compte de la sensibilité des données que vous préremplissez et du comportement de partage de votre audience lorsque vous utilisez cette fonctionnalité.
{% endalert %}

## Récupérer des données externes avec du code personnalisé {#fetching-external-data-with-custom-code}

Vous pouvez utiliser un bloc **Code personnalisé** pour récupérer des données depuis des endpoints externes et les afficher dans votre page de destination. Cette approche effectue la requête côté client (dans le navigateur de l'utilisateur), de sorte que la page se charge rapidement sans délais de rendu côté serveur.

{% alert warning %}
Lorsque vous récupérez des données externes, vous êtes responsable de la sécurité de votre déploiement. Les identifiants externes utilisés dans les appels API doivent être des UUID ou utiliser un schéma de nommage équivalent en termes de sécurité. Consultez les [bonnes pratiques de nommage des ID utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).
{% endalert %}

### Cas d'usage {#use-case}

Ce modèle est utile lorsque vous devez afficher des données spécifiques à l'utilisateur qui ne sont pas stockées dans Braze. Par exemple : inventaire en temps réel, recommandations personnalisées ou autres données que votre organisation gère dans des systèmes distincts.

### Exemple de déploiement {#example-implementation}

Cet exemple montre comment récupérer des données utilisateur depuis une API externe. Remplacez l'endpoint de l'API par votre propre endpoint sécurisé et utilisez un identifiant sécurisé.

{% raw %}
```html
<script>
window.onload = () => {
  // Use Liquid to template the user's external ID
  const userId = "{{${user_id}}}";

  const loadUserData = async () => {
    try {
      // Replace with your own secure API endpoint
      const response = await fetch(`https://your-api.example.com/user/${userId}`);

      if (!response.ok) {
        throw new Error('Failed to load data');
      }

      const data = await response.json();

      // Update the page with the fetched data
      document.querySelector("#user-data").textContent = JSON.stringify(data, null, 2);
      document.querySelector("#user-name").textContent = data.name || "User";
    } catch (error) {
      // Handle errors gracefully
      document.querySelector("#user-data").textContent = "Unable to load data at this time.";
    }
  };

  loadUserData();
};
</script>

<!-- Display area for fetched data -->
<p>Welcome, <span id="user-name">Loading...</span></p>
<pre id="user-data">Loading your information...</pre>
```
{% endraw %}

### Considérations {#considerations}

Lorsque vous récupérez des données externes dans les pages de destination :

- **États de chargement :** les utilisateurs verront un texte de remplacement jusqu'à ce que l'endpoint réponde. Envisagez d'ajouter un indicateur de chargement ou un écran squelette.
- **Gestion des erreurs :** si l'endpoint échoue ou met du temps à répondre, la page peut sembler défectueuse. Implémentez des messages d'erreur et des solutions de repli appropriés.
- **Performances :** la page se charge immédiatement, mais les données apparaissent après la fin de la requête externe. Gardez vos réponses API rapides pour une expérience utilisateur optimale.
- **Sécurité :** assurez-vous que votre endpoint API valide l'identifiant et ne renvoie que les données que l'utilisateur est autorisé à consulter. Implémentez une limitation de débit pour prévenir les abus. Pour des conseils sur le choix d'identifiants sécurisés, consultez les [bonnes pratiques de nommage des ID utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).

## Pages de secours {#fallback-pages}

Si vos utilisateurs tentent d'accéder à une page qui a été dépubliée, ils verront un message indiquant que la page ne peut pas être chargée actuellement. Les raisons pour lesquelles une page a été dépubliée incluent :

- Un Liquid complexe ou défectueux, pouvant entraîner des temps de rendu longs
- Des problèmes de réseau côté utilisateur
- Le dépassement des limites maximales de taille de la page de destination