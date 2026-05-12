# Le serveur MCP Braze {#the-braze-mcp-server}

> Découvrez le serveur MCP Braze, une connexion sécurisée qui permet aux outils d'intelligence artificielle tels que Claude et Cursor d'accéder aux données Braze non personnelles afin de répondre à des questions, d'analyser des tendances et de fournir des informations.

{% multi_lang_include mcp_server/beta_alert.md %}

## Qu'est-ce que le protocole de contexte de modèle (MCP) ? {#what-is-model-context-protocol-mcp}

​​Le protocole MCP (Model Context Protocol) est une norme qui permet aux agents d'intelligence artificielle de se connecter à une autre plateforme et d'utiliser ses données. Il se compose de deux parties principales :

- **Client MCP :** L'application sur laquelle l'agent d'intelligence artificielle est exécuté, telle que Cursor ou Claude.
- **Serveur MCP :** Un service fourni par une autre plateforme, telle que Braze, qui détermine les outils que l'intelligence artificielle peut utiliser et les données auxquelles elle peut accéder.

## À propos du serveur MCP Braze {#about-the-braze-mcp-server}

Après avoir [configuré le serveur MCP Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, vous pouvez connecter des outils d'intelligence artificielle tels que des agents, des assistants et des chatbots directement à Braze, leur permettant ainsi de lire des données agrégées telles que les analyses Canvas et Campaign, les attributs personnalisés, les Segments, et bien plus encore. Le serveur MCP Braze est particulièrement adapté pour :

- Créer des outils basés sur l'intelligence artificielle nécessitant le contexte Braze.
- Les ingénieurs CRM élaborant des workflows en plusieurs étapes pour les agents.
- Les marketeurs techniques explorant les requêtes en langage naturel.

Le serveur MCP Braze prend en charge 39 endpoints qui ne renvoient pas les données des profils utilisateurs Braze. Vous pouvez choisir les endpoints à attribuer à votre clé API Braze afin de contrôler ce à quoi un agent peut accéder ou modifier.

{% alert warning %}
N'attribuez que les autorisations de clé API que vous souhaitez accorder à votre agent. Si vous ne souhaitez pas que votre agent effectue des modifications dans Braze, veillez à ne pas activer les autorisations d'écriture. Les agents peuvent tenter d'écrire des données via toute autorisation que vous leur accordez.
{% endalert %}

## Exemple d'utilisation {#usage-example}

Vous pouvez interagir avec Braze en utilisant le langage naturel grâce à des outils tels que Claude ou Cursor. Pour d'autres exemples et bonnes pratiques, consultez [Utilisation du serveur MCP Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![« Quelles sont les fonctions Braze à ma disposition ? » : question posée et réponse fournie dans Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Quelles sont les fonctions Braze disponibles ? » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Foire aux questions (FAQ) {#faq}

### Quels clients MCP sont pris en charge ? {#which-mcp-clients-are-supported}

Seuls [Claude](https://claude.ai/) et [Cursor](https://cursor.com/) sont officiellement pris en charge. Il est nécessaire de disposer d'un compte auprès de l'un de ces clients pour pouvoir utiliser le serveur MCP Braze.

### À quelles données Braze mon client MCP a-t-il accès ? {#what-braze-data-can-my-mcp-client-access}

Les clients MCP peuvent accéder aux endpoints qui ne renvoient pas d'informations personnelles identifiables. Vous contrôlez les endpoints auxquels un agent peut accéder grâce aux autorisations que vous attribuez à votre clé API.

### Mon client MCP peut-il modifier les données Braze ? {#can-my-mcp-client-change-braze-data}

Le serveur n'expose que l'endpoint d'écriture `/media_library/create`, qui vous permet de télécharger des ressources multimédia dans votre bibliothèque multimédia. Si vous ne souhaitez pas que votre agent effectue ces modifications dans Braze, laissez l'autorisation `media_library.create` décochée lors de la création de votre clé API.

### Puis-je utiliser un serveur MCP tiers pour Braze ? {#can-i-use-a-third-party-mcp-server-for-braze}

Il est déconseillé d'utiliser un serveur MCP tiers pour les données Braze. Veuillez utiliser uniquement le serveur officiel MCP Braze hébergé sur [PyPi](https://pypi.org/project/braze-mcp-server/).

### Pourquoi le serveur MCP Braze n'offre-t-il pas d'accès aux informations personnelles identifiables ? {#why-doesnt-the-braze-mcp-server-offer-pii-access}

Afin de protéger les données des utilisateurs tout en favorisant des cas d'utilisation pertinents, le serveur est limité aux endpoints qui ne renvoient généralement pas d'informations personnelles identifiables. Cela permet de réduire les risques pour votre espace de travail et les personnes qui y sont associées.

### Puis-je réutiliser mes clés API ? {#can-i-reuse-my-api-keys}

Non. Vous devrez créer une nouvelle clé API pour votre client MCP. Veillez à n'accorder à vos outils d'intelligence artificielle que l'accès aux informations que vous jugez approprié et évitez les autorisations étendues.

### Le serveur MCP Braze est-il hébergé localement ou à distance ? {#is-the-braze-mcp-server-hosted-locally-or-remotely}

Le serveur MCP Braze est hébergé localement.

### Pourquoi Cursor ne répertorie-t-il que des fonctions ? {#why-is-cursor-only-listing-functions}

Vérifiez si vous êtes en mode demande ou en mode agent. Pour utiliser le serveur MCP, il est nécessaire d'être en mode agent.

### Que dois-je faire lorsque l'agent renvoie une réponse qui semble incorrecte ? {#what-do-i-do-when-the-agent-returns-an-answer-that-looks-incorrect}

Lorsque vous utilisez des outils tels que Cursor, il peut être utile d'essayer de modifier le modèle utilisé. Par exemple, si vous l'avez réglé sur « auto », essayez de le régler sur un modèle spécifique et testez-le afin de déterminer quel modèle fonctionne le mieux pour votre cas d'utilisation. Vous pouvez également essayer de démarrer une nouvelle conversation et de réessayer l'invite.

Si les problèmes persistent, vous pouvez nous contacter par e-mail à l'adresse [mcp-product@braze.com](mailto:mcp-product@braze.com) pour nous en informer. Si possible, veuillez inclure une vidéo et développer les fonctions d'appel afin que nous puissions examiner les appels que l'agent a tenté de passer.

{% multi_lang_include mcp_server/legal_disclaimer.md %}