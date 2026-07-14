# Bannières {#banners}

> Avec les bannières, vous pouvez créer des messages personnalisés pour vos utilisateurs, tout en élargissant la portée de vos autres canaux, tels que les e-mails ou les notifications push. Vous pouvez intégrer des bannières directement dans votre application ou votre site web, ce qui vous permet d'interagir avec les utilisateurs à travers une expérience naturelle.

## Conditions préalables {#prerequisites}

La disponibilité des bannières dépend de votre forfait Braze. Contactez votre gestionnaire de compte ou votre gestionnaire du succès des clients pour commencer.

Avant de démarrer, assurez-vous d'avoir [créé des emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements) dans votre application ou votre site web.

![Exemple de bannière affichée sur un appareil.]({% image_buster /assets/img/banners/sample_banner.png %})

## Pourquoi utiliser des bannières ? {#why-use-banners}

Les bannières permettent aux équipes marketing et produit de personnaliser dynamiquement le contenu des applications ou des sites web, en tenant compte en temps réel de l'éligibilité et du comportement des utilisateurs. Elles affichent de manière persistante des messages en ligne, offrant des expériences non intrusives et contextuellement pertinentes qui peuvent être actualisées au début d'une session ou en cours de session lorsque votre application ou votre site web en fait explicitement la demande.

Une fois les bannières intégrées à une application ou à un site web, les marketeurs peuvent concevoir et lancer des bannières à l'aide d'un éditeur simple par glisser-déposer ou d'un éditeur HTML complet, ce qui élimine le besoin d'une assistance continue de la part des développeurs, réduit la complexité et améliore l'efficacité.

| Cas d'usage | Explication |
| --- | --- |
| Annonces | Mettez en avant les annonces telles que les événements à venir ou les changements de politique dans votre expérience sur l'application. |
| Personnalisation des offres | Présentez des promotions et des incitations personnalisées en fonction de l'historique de navigation, du contenu du panier, du niveau d'abonnement et du statut de fidélité de chaque utilisateur. |
| Ciblage de l'engagement des nouveaux utilisateurs | Accompagnez les nouveaux utilisateurs tout au long du processus d'onboarding et de la configuration de leur compte. |
| Soldes et promotions | Mettez en avant le contenu phare, les produits tendance et les campagnes de marque en cours de manière persistante et directement sur votre page d'accueil, sans perturber l'expérience utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pourquoi utiliser des bannières ?" }

## Fonctionnalités {#features}

Les fonctionnalités des bannières comprennent :

- **Création de contenu simplifiée :** Créez et prévisualisez votre bannière à l'aide d'un éditeur visuel par glisser-déposer prenant en charge les images, le texte, les boutons, les formulaires de saisie d'adresse e-mail, le code personnalisé, et plus encore. Les équipes qui préfèrent gérer leur propre balisage peuvent utiliser l'éditeur HTML pour un contrôle total sur le HTML et les styles de la bannière, ou demander à [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages) de générer du HTML à partir d'une description.
- **Emplacements flexibles :** Définissez plusieurs emplacements au sein de votre application ou site web où les bannières peuvent apparaître, ce qui permet un ciblage précis en fonction de contextes ou d'expériences utilisateur spécifiques.
- **Personnalisation dynamique :** Les bannières recalculent la personnalisation (logique Liquid) et la segmentation à chaque actualisation de la bannière. Si un utilisateur met à jour son profil ou qu'un attribut personnalisé change, la prochaine actualisation de la bannière reflétera ces modifications.
- **Priorisation native :** Définissez la priorité d'affichage lorsque plusieurs bannières ciblent le même emplacement, afin de garantir que le bon message parvienne aux utilisateurs au bon moment.
- **Bloc éditeur de code personnalisé :** Utilisez le bloc éditeur de code personnalisé pour ajouter du HTML personnalisé afin de bénéficier d'une personnalisation avancée ou d'une intégration fluide avec vos styles web existants.

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

## Limitations

Chaque espace de travail peut prendre en charge jusqu'à 200 campagnes de bannières actives. Si cette limite est atteinte, vous devrez [archiver ou désactiver]({{site.baseurl}}/user_guide/messaging/governance/statuses#changing-the-status) une campagne existante avant d'en créer une nouvelle.

De plus, les messages de bannière ne prennent pas en charge les fonctionnalités suivantes :

- Campaigns déclenchées par API et par événement
- Contenu connecté
- Codes promotionnels
- `catalog_items` utilisant [l'étiquette `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)

## Étapes suivantes {#next-steps}

- [Créer des emplacements de bannières dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements)
- [Créer une campagne de bannières dans Braze]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)
- [Tutoriel : Afficher une bannière par ID de placement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)

{% alert tip %}
Vous souhaitez contribuer à définir les priorités pour la suite ? Contactez [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}