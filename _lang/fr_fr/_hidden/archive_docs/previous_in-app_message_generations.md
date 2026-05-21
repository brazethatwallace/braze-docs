---
nav_title: Générations précédentes
article_title: Générations précédentes de messages in-app
page_order: 20
page_type: reference
description: "Cet article passe en revue les informations précédentes concernant les messages in-app dans Braze."
channel: in-app messages
noindex: true
hidden : true
---

# Générations précédentes de messages in-app {#previous-in-app-message-generations}

{% alert important %}
Cette page passe en revue les informations précédentes concernant nos messages in-app. Pour consulter les informations les plus à jour sur notre génération actuelle de messages in-app, reportez-vous à notre documentation actuelle sur les [messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/).
{% endalert %}

## Universel {#universal}

Cette section passe en revue les informations précédentes concernant nos messages in-app. Pour consulter les informations les plus à jour sur notre génération actuelle de messages in-app, reportez-vous à notre [documentation d'aperçu des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/).

{% details Plein écran %}
Il s'agit des messages les plus engageants, mais aussi les plus intrusifs, car ils occupent la totalité de l'écran de l'utilisateur. Ils sont parfaits pour afficher de grandes images riches et peuvent s'avérer utiles pour transmettre des informations très importantes, telles que de nouvelles fonctionnalités clés et des promotions arrivant à expiration. Étant donné qu'ils perturbent davantage l'expérience utilisateur, utilisez-les avec parcimonie pour le contenu hautement prioritaire.

![Message plein écran]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Fonctionnalités personnalisables**

- En-tête et texte du corps
- Une grande image
- Jusqu'à deux boutons d'appel à l'action avec un comportement au clic et des liens profonds distincts
- Des couleurs différentes pour l'en-tête et le texte du corps, les boutons et l'arrière-plan
- Paires clé-valeur

{% enddetails %}
{% details  Fenêtre modale %}
Ces messages ne sont pas aussi intrusifs que ceux en plein écran, car ils permettent toujours aux utilisateurs de voir une partie de l'interface de votre application. Comme ils contiennent toujours des boutons et des images, les messages modaux peuvent constituer une meilleure option que les contextuels si vous souhaitez une campagne visuelle plus interactive. Ils sont parfaits pour le contenu de priorité moyenne, comme les mises à jour d'applications et les offres et événements non urgents.

![Message modal]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Fonctionnalités personnalisables**

- En-tête et texte du corps
- Une icône d'image ou de badge personnalisable
- Jusqu'à deux boutons d'appel à l'action avec un comportement au clic et des liens profonds distincts
- Des couleurs différentes pour l'en-tête et le texte du corps, les boutons et l'arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Contextuel traditionnel %}
Il s'agit du type de message le moins intrusif, bien qu'il puisse attirer plus ou moins l'attention selon les couleurs et les icônes de badge utilisées. Ce format de message peut être idéal pour l'onboarding de nouveaux utilisateurs et pour les orienter vers des fonctionnalités spécifiques de l'application, car il ne suspend pas l'expérience sur l'application et permet une exploration continue.

![Message contextuel]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Fonctionnalités personnalisables**

- Texte du corps
- Une icône d'image ou de badge personnalisable
- Couleurs différentes pour l'arrière-plan, le texte et l'icône du contextuel
- Comportement de fermeture du message
- Position du contextuel (haut ou bas de l'écran de l'application)
- Paires clé-valeur

{% enddetails %}

<br>

## Web

Cette section passe en revue les informations précédentes concernant des messages in-app plus personnalisés. Pour consulter les informations les plus à jour sur notre génération actuelle de messages in-app, reportez-vous à notre [documentation de personnalisation]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/).

{% details Message de capture d'e-mail %}
Les messages de capture d'e-mail vous permettent d'inviter facilement les utilisateurs de votre site à soumettre leur adresse e-mail, après quoi celle-ci sera disponible dans le système Braze pour l'ensemble de vos campagnes de communication.

![Message de capture d'e-mail]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Pour activer les messages in-app de capture d'e-mail via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent exécuter du JavaScript, d'où la nécessité qu'un responsable du site les active.

**Fonctionnalités personnalisables**

- Texte de l'en-tête, du corps et du bouton d'envoi
- Une image facultative
- Un lien facultatif vers les conditions d'utilisation
- Des couleurs différentes pour l'en-tête et le texte du corps, les boutons et l'arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Message HTML personnalisé %}

Bien que les messages in-app par défaut de Braze puissent être personnalisés de diverses manières, vous pouvez obtenir un contrôle encore plus grand sur l'apparence de vos campagnes en utilisant des messages conçus et créés à l'aide de HTML, CSS et JavaScript. Grâce à une composition simple, vous pouvez débloquer des fonctionnalités et une image de marque personnalisées pour répondre à tous vos besoins. Les messages in-app HTML offrent un contrôle accru de l'apparence d'un message, et tout ce qui est pris en charge par HTML5 l'est également par Braze.

**Pont JavaScript (appboyBridge)**

Les messages in-app HTML prennent en charge une interface de pont JavaScript vers le SDK Web de Braze, ce qui vous permet de déclencher des actions Braze personnalisées lorsque les utilisateurs cliquent sur des éléments avec des liens ou interagissent avec votre contenu. Les méthodes JavaScript suivantes sont prises en charge dans les messages in-app HTML de Braze :

{% multi_lang_include archive/appboyBridge.md platform="web" %}

De plus, à des fins de suivi analytique, tous les éléments `<a>` ou `<button>` dans votre HTML enregistrent automatiquement une action de « clic » sur la Campaign associée au message in-app. Pour enregistrer un « clic de bouton » au lieu d'un « clic de corps », fournissez soit une valeur de chaîne de requête abButtonId dans le href de votre lien (par exemple, `<a href="http://mysite.com?abButtonId=0">click me</a>`), soit un identifiant sur l'élément HTML (par exemple, `<a id="0" href="http://mysite.com">click me</a>`). Notez que les seuls identifiants de bouton actuellement acceptés sont « 0 » et « 1 ». Un lien avec un identifiant de bouton 0 sera représenté comme « Button 1 » sur le tableau de bord, tandis qu'un lien avec un identifiant de bouton 1 sera représenté comme « Button 2 ».

>  Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent exécuter du JavaScript, d'où la nécessité qu'un responsable du site les active.

{% enddetails %}

{% details Modèles de messages in-app HTML %}

Nous avons conçu un ensemble de modèles de messages in-app HTML5 pour vous aider à démarrer. Consultez notre [dépôt GitHub](https://github.com/braze-inc/in-app-message-templates) qui contient des instructions détaillées sur la façon d'utiliser et de personnaliser ces modèles selon vos besoins.

**Fonctionnalités personnalisables**

- Polices
- Styles
- Images et vidéos
- Comportements au clic
- Composants interactifs

{% enddetails %}

<br>

## Spécifications {#specifications}

Cette section passe en revue les informations précédentes concernant nos spécifications créatives de messages in-app. Pour consulter les informations les plus à jour sur notre génération actuelle de messages in-app, reportez-vous à notre [documentation des spécifications créatives]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/).

### Limites de caractères et d'images {#character-and-image-limits}

Pour tous les types de messages in-app répertoriés dans le tableau suivant, les directives supplémentaires suivantes s'appliquent :

- **Taille d'image recommandée :** 500&nbsp;Ko
- **Taille maximale de l'image :** 5&nbsp;Mo
- **Types de fichiers pris en charge :** PNG, JPEG, GIF

| Type                               | Rapport hauteur/largeur | Nombre max. de caractères |
| :--------------------------------- | :----------: | :-----------------: |
| Portrait plein écran (image uniquement)  |    10:16     |         240         |
| Portrait plein écran (avec texte)   |     5:4      |         240         |
| Paysage plein écran (avec texte)  |     16:5     |         240         |
| Paysage plein écran (image uniquement) |    16:10     |         240         |
| Contextuel                            |     1:1      |         140         |
| Modal (image uniquement)                 |     1:1      |         140         |
| Modal (avec texte)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Character and image limits" }

### Conserver des tailles de fichiers réduites pour les messages in-app {#keeping-in-app-message-file-sizes-small}

Braze vous recommande de conserver vos images et vos archives ZIP de ressources HTML aussi petites que possible, et ce pour plusieurs raisons :

- Des payloads HTML et d'images plus légers se téléchargent plus rapidement et s'affichent de manière plus fiable pour vos clients.
- Des payloads HTML et d'images plus légers permettent également de réduire les coûts de données de vos clients. Les messages in-app de Braze sont téléchargés en arrière-plan au début de la session afin de pouvoir être déclenchés en temps réel selon les critères que vous sélectionnez. Par conséquent, si vous avez 10 messages in-app HTML de 1&nbsp;Mo chacun, vos clients devront tous supporter 10&nbsp;Mo de frais de données, même s'ils n'ont jamais déclenché tous ces messages. La somme peut rapidement augmenter avec le temps, même si les messages in-app sont mis en cache et ne sont pas retéléchargés d'une session à l'autre.

Les stratégies suivantes sont utiles pour conserver des tailles de fichiers réduites :

- Référencez les polices intégrées dans votre application ou votre site web pour personnaliser vos messages in-app HTML, plutôt que d'inclure les fichiers de polices dans votre dossier ZIP de ressources HTML.
- Assurez-vous qu'aucun CSS ou JavaScript superflu ou dupliqué ne figure dans vos archives ZIP de ressources HTML.
- Utilisez [ImageOptim](https://imageoptim.com/) sur toutes les images pour les compresser à leur taille minimale possible sans réduction de qualité.

### Spécifications de l'iPhone 5 {#iphone-5-specs}

![Spécifications de l'iPhone 5]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %})

### Spécifications de l'iPhone 6 {#iphone-6-specs}

![Spécifications de l'iPhone 6]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %})