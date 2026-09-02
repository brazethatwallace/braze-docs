{% multi_lang_include developer_guide/prerequisites/web.md %} Cependant, aucune configuration supplémentaire n'est nécessaire.

## Types de messages {#message-types}

Tous les messages in-app héritent de leur prototype de [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html), qui définit le comportement et les caractéristiques de base de tous les messages in-app. Les sous-classes prototypiques sont [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) et [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

Chaque type de message in-app est personnalisable en termes de contenu, d'images, d'icônes, d'actions au clic, d'analyse, d'affichage et de réception.

{% tabs %}
{% tab Contextuel %}

Les messages in-app [`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) sont ainsi nommés car, traditionnellement sur les plateformes mobiles, ils « glissent vers le haut » ou « glissent vers le bas » depuis le haut ou le bas de l'écran. Dans le SDK Web de Braze, ces messages sont affichés plutôt sous forme de notification de type Growl ou Toast, pour s'aligner sur le paradigme dominant du web. Ils couvrent une petite partie de l'écran et offrent une capacité de communication efficace et non intrusive.

![Un message in-app contextuel glissant depuis le bas de l'écran d'un téléphone affichant « Les humains sont complexes. L'engagement personnalisé ne devrait pas l'être. » En arrière-plan, le même message in-app est affiché dans le coin inférieur d'une page web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fenêtre modale %}

Les messages in-app [`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) apparaissent au centre de l'écran et sont encadrés par un panneau translucide. Utiles pour les communications plus importantes, ils peuvent être équipés de jusqu'à deux boutons avec actions au clic et suivi analytique.

![Un message in-app de type fenêtre modale au centre de l'écran d'un téléphone affichant « Les humains sont complexes. L'engagement personnalisé ne devrait pas l'être. » En arrière-plan, le même message in-app est affiché au centre d'une page web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Plein écran %}

Les messages in-app [`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) sont utiles pour maximiser le contenu et l'impact de votre communication utilisateur. Sur les fenêtres de navigateur étroites (par exemple, le web mobile), les messages in-app `full` occupent l'intégralité de la fenêtre du navigateur. Sur les fenêtres de navigateur plus larges, les messages in-app `full` s'affichent de manière similaire aux messages in-app `modal`. La moitié supérieure d'un message in-app `full` contient une image, et la moitié inférieure permet d'afficher jusqu'à huit lignes de texte ainsi que jusqu'à deux boutons avec actions au clic et suivi analytique.

![Un message in-app plein écran affiché sur l'intégralité de l'écran d'un téléphone avec le texte « Les humains sont complexes. L'engagement personnalisé ne devrait pas l'être. » En arrière-plan, le même message in-app est affiché en grand au centre d'une page web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personnalisé %}

Les messages in-app [`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) sont utiles pour créer du contenu utilisateur entièrement personnalisé. Le HTML défini par l'utilisateur est affiché dans un iFrame et peut contenir du contenu riche, tel que des images, des polices, des vidéos et des éléments interactifs, permettant un contrôle total sur l'apparence et la fonctionnalité du message. Ils prennent en charge une interface JavaScript `brazeBridge` pour appeler des méthodes du SDK Web de Braze depuis votre HTML. Consultez nos [bonnes pratiques]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices) pour plus de détails.

{% alert important %}
Pour activer les messages in-app HTML via le SDK Web, vous **devez** fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Ceci est une mesure de sécurité. Les messages in-app HTML peuvent exécuter du JavaScript, c'est pourquoi un responsable du site doit les activer.
{% endalert %}

L'exemple suivant montre un message in-app HTML paginé :

![Un message in-app HTML avec un carrousel de contenu et des boutons interactifs.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}