# Bannières {#banners}

> Avec les bannières, vous pouvez créer des messages personnalisés pour vos utilisateurs, tout en élargissant la portée de vos autres canaux, tels que les e-mails ou les notifications push. Vous pouvez intégrer des bannières directement dans votre application ou votre site web, ce qui vous permet d'interagir avec les utilisateurs à travers une expérience naturelle.

## Prérequis {#prerequisites}

La disponibilité des Banners dépend de votre offre Braze. Contactez votre gestionnaire de compte ou votre gestionnaire du succès des clients pour commencer.

Avant de commencer, assurez-vous d'avoir créé des [emplacements de Banner]({{site.baseurl}}/developer_guide/banners/placements) dans votre application ou votre site web.

![Exemple de Banner affiché sur un appareil.]({% image_buster /assets/img/banners/sample_banner.png %})

## Pourquoi utiliser les Banners ? {#why-use-banners}

Les Banners permettent aux équipes marketing et produit de personnaliser dynamiquement le contenu d'une application ou d'un site web, en reflétant l'éligibilité et le comportement des utilisateurs en temps réel. Ils affichent des messages de manière persistante et intégrée, offrant des expériences non intrusives et contextuellement pertinentes qui peuvent être actualisées au début d'une session ou en cours de session lorsque votre application ou site web le demande explicitement.

Une fois les Banners intégrés dans une application ou un site web, les marketeurs peuvent concevoir et lancer des Banners à l'aide d'un éditeur par glisser-déposer ou d'un éditeur HTML complet, éliminant ainsi le besoin d'une assistance continue des développeurs, réduisant la complexité et améliorant l'efficacité.

| Cas d'usage | Explication |
| --- | --- |
| Annonces | Gardez les annonces telles que les événements à venir ou les changements de politique au premier plan de votre expérience sur l'application. |
| Personnalisation des offres | Affichez des promotions et des incitations personnalisées en fonction de l'historique de navigation, du contenu du panier, du niveau d'abonnement et du statut de fidélité de chaque utilisateur. |
| Ciblage de l'engagement des nouveaux utilisateurs | Guidez les nouveaux utilisateurs à travers les flux d'onboarding et la configuration de leur compte. |
| Ventes et promotions | Mettez en avant le contenu vedette, les produits tendance et les Campaigns de marque en cours de manière persistante et directement sur votre page d'accueil, sans perturber l'expérience utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pourquoi utiliser les Banners ?" }

## Fonctionnalités {#features}

Les fonctionnalités des Banners incluent :

- **Création de contenu simplifiée :** Créez et prévisualisez votre Banner à l'aide d'un éditeur visuel par glisser-déposer prenant en charge les images, le texte, les boutons, les formulaires de capture d'e-mail, le code personnalisé, et bien plus encore. Les équipes qui préfèrent gérer leur propre balisage peuvent utiliser l'éditeur HTML à la place pour un contrôle total sur le HTML et les styles du Banner, ou demander à [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages) de générer du HTML à partir d'une description.
- **Placements flexibles :** Définissez plusieurs emplacements au sein de votre application ou de votre site web où les Banners peuvent apparaître, permettant un ciblage précis vers des contextes ou des expériences utilisateur spécifiques.
- **Personnalisation dynamique :** Les Banners recalculent la personnalisation (logique Liquid) et la segmentation à chaque actualisation du banner. Si un utilisateur met à jour son profil ou si un attribut personnalisé change, la prochaine actualisation du Banner reflétera ces modifications.
- **Priorisation native :** Définissez la priorité d'affichage lorsque plusieurs Banners ciblent le même placement, garantissant que le bon message atteigne les utilisateurs au bon moment.
- **Bloc éditeur de code personnalisé :** Utilisez le bloc éditeur de code personnalisé pour ajouter du HTML personnalisé afin de permettre une personnalisation avancée ou une intégration harmonieuse avec vos styles web existants.

## À propos des bannières {#about-banners}

### ID de placement {#placement-id}

Les emplacements de bannières sont des localisations spécifiques dans votre application ou votre site web [que vous créez à l'aide du SDK Braze]({{site.baseurl}}/developer_guide/banners/placements) et qui désignent les endroits où les bannières peuvent apparaître.

Les localisations courantes incluent le haut de votre page d'accueil, les pages détaillées des produits et les processus de paiement. Une fois les emplacements créés, les bannières peuvent être [affectées dans votre campagne de bannières]({{site.baseurl}}/user_guide/channels/banners/create_a_banner).

Il n'y a pas de limite fixe au nombre d'emplacements que vous pouvez créer par espace de travail, et vous pouvez créer autant d'ID de placement que votre expérience l'exige. Chaque emplacement doit être unique au sein d'un espace de travail. Un seul ID de placement peut être référencé par jusqu'à 25 messages actifs simultanément.

{% alert important %}
Évitez de modifier les ID de placement après le lancement d'une campagne de bannières.
{% endalert %}

### Priorité des bannières {#priority}

Lorsque plusieurs messages de bannière font référence au même ID de placement, les bannières sont affichées par ordre de priorité : élevée, moyenne ou faible. Par défaut, les bannières sont définies sur moyenne, mais vous pouvez [définir manuellement la priorité]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#set-banner-priority-optional) lorsque vous créez ou modifiez votre campagne de bannières.

Si plusieurs bannières sont définies avec la même priorité, la bannière la plus récente à laquelle l'utilisateur est éligible s'affiche en premier.

### Demandes de placement {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Distribution des messages {#message-delivery}

Les messages de bannière sont diffusés sur votre application ou votre site web sous forme de contenu HTML, généralement affiché dans un iframe. Cela garantit un rendu cohérent de vos bannières sur tous les appareils et vous aide à séparer leurs styles et leurs scripts du reste de votre code.

Les iframes permettent des mises à jour dynamiques et personnalisées du contenu sans nécessiter de modifications de votre base de code. Chaque iframe récupère et affiche le HTML pour chaque session utilisateur à l'aide de la logique de ciblage et de personnalisation de la campagne.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### Dimensions et taille {#dimensions-and-sizing}

Voici ce que vous devez savoir sur les dimensions et la taille des bannières :

- Bien que le compositeur vous permette de prévisualiser les bannières dans différentes dimensions, cette information n'est pas enregistrée ni envoyée au SDK.
- Le HTML occupe toute la largeur du conteneur dans lequel il est affiché.
- Nous vous recommandons de créer un élément de dimension fixe et de tester ces dimensions dans le compositeur.

### Contenu connecté {#connected-content}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Vous pouvez utiliser le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) pour extraire des données en temps réel à partir d'API externes dans votre bannière. Étant donné que les bannières s'affichent en ligne lors d'une actualisation de session, le contenu connecté présente des limitations spécifiques dans ce canal :

- **Requêtes GET uniquement :** les bannières n'exécutent que les requêtes de contenu connecté de type `GET`. Les requêtes `POST` ne sont pas prises en charge.
- **Budget de rendu partagé :** tous les emplacements renvoyés dans une seule requête d'actualisation (jusqu'à 10) partagent un budget de rendu d'environ deux secondes. Chaque appel de contenu connecté est décompté de ce budget partagé, de sorte qu'un emplacement avec des appels lents ou nombreux peut consommer le temps dont les autres emplacements ont besoin.
- **Pas de nouvelles tentatives :** si un appel de contenu connecté échoue, expire ou si le budget de rendu est dépassé, le résultat du contenu connecté pour cet emplacement est traité comme nul. Contrairement aux autres canaux, les bannières ne relancent pas la requête et ne retardent pas la distribution.

## Limitations

Chaque espace de travail peut prendre en charge jusqu'à 200 Campaigns de bannières actives. Si cette limite est atteinte, vous devrez [archiver ou désactiver]({{site.baseurl}}/user_guide/messaging/governance/statuses#changing-the-status) une Campaign existante avant d'en créer une nouvelle.

De plus, les messages de bannière ne prennent pas en charge les fonctionnalités suivantes :

- Campaigns déclenchées par API et par événement
- [Contenu connecté](#connected-content) (en accès anticipé)
- Codes promotionnels
- `catalog_items` utilisant [l'étiquette `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)

## Étapes suivantes {#next-steps}

- [Créer des emplacements de bannières dans votre application ou site web]({{site.baseurl}}/developer_guide/banners/placements)
- [Créer une campagne de bannières dans Braze]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)
- [Tutoriel : Afficher une bannière par ID d'emplacement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)

{% alert tip %}
Vous souhaitez contribuer à définir les prochaines priorités ? Contactez [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}