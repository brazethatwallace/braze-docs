# Le serveur MCP Braze {#the-braze-mcp-server}

> Découvrez le serveur MCP Braze, une connexion sécurisée qui permet aux outils d'intelligence artificielle tels que Claude et Cursor d'accéder aux données Braze non personnelles afin de répondre à des questions, d'analyser des tendances et de fournir des informations.

{% multi_lang_include mcp_server/beta_alert.md %}

## Qu'est-ce que le protocole de contexte de modèle (MCP) ? {#what-is-model-context-protocol-mcp}

​​Le protocole MCP (Model Context Protocol) est une norme qui permet aux agents d'intelligence artificielle de se connecter à une autre plateforme et d'utiliser ses données. Il se compose de deux parties principales :

- **Client MCP :** L'application sur laquelle l'agent d'intelligence artificielle est exécuté, telle que Cursor ou Claude.
- **Serveur MCP :** Un service fourni par une autre plateforme, telle que Braze, qui détermine les outils que l'intelligence artificielle peut utiliser et les données auxquelles elle peut accéder.

## À propos du serveur MCP Braze {#about-the-braze-mcp-server}

Après avoir [configuré le serveur MCP Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, vous pouvez connecter des outils d'intelligence artificielle tels que des agents, des assistants et des chatbots directement à Braze, leur permettant ainsi de lire des données agrégées telles que les analyses Canvas et Campaign, les attributs personnalisés, les segments, et bien plus encore. Le serveur MCP Braze est particulièrement adapté pour :

- Créer des outils basés sur l'intelligence artificielle nécessitant le contexte Braze.
- Les ingénieurs CRM élaborant des workflows en plusieurs étapes pour les agents.
- Les marketeurs techniques explorant les requêtes en langage naturel.

Le serveur MCP Braze comprend des endpoints en lecture seule et en écriture. Ils ne renvoient pas les données des profils utilisateurs Braze. Vous choisissez les endpoints à attribuer à votre clé API Braze, et ce choix détermine ce qu'un agent peut lire, créer ou mettre à jour. Pour consulter la liste complète des endpoints disponibles et les autorisations requises, voir [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
N'attribuez que les autorisations de clé API que vous souhaitez accorder à votre agent. Si vous ne souhaitez pas que votre agent effectue des modifications dans Braze, veillez à ne pas activer les autorisations d'écriture lors de la création de votre clé API. Les agents peuvent tenter d'écrire des données via toute autorisation d'écriture que vous leur accordez.
{% endalert %}

## Exemple d'utilisation {#usage-example}

Vous pouvez interagir avec Braze en utilisant le langage naturel grâce à des outils tels que Claude ou Cursor. Pour d'autres exemples et bonnes pratiques, consultez [Utilisation du serveur MCP Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Used `list_functions` and returned available Braze MCP function groups.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Queried `list_functions` and listed sample functions such as `get_canvas_list`.
{% endtab %}
{% endtabs %}

## Foire aux questions (FAQ) {#faq}

### Quels clients MCP sont pris en charge ? {#which-mcp-clients-are-supported}

Seuls [Claude](https://claude.ai/) et [Cursor](https://cursor.com/) sont officiellement pris en charge. Il est nécessaire de disposer d'un compte auprès de l'un de ces clients pour pouvoir utiliser le serveur MCP Braze.

### À quelles données Braze mon client MCP a-t-il accès ? {#what-braze-data-can-my-mcp-client-access}

Les clients MCP peuvent accéder aux endpoints qui ne renvoient pas d'informations personnelles identifiables. Vous contrôlez les endpoints auxquels un agent peut accéder grâce aux autorisations que vous attribuez à votre clé API.

### Mon client MCP peut-il modifier les données Braze ? {#can-my-mcp-client-change-braze-data}

Oui. Le serveur expose un ensemble ciblé d'endpoints en écriture qui permettent aux agents de créer ou de mettre à jour du contenu dans votre espace de travail, comme des ressources de la bibliothèque multimédia, des modèles d'e-mail et des Content Blocks. Chaque endpoint en écriture nécessite sa propre autorisation de clé API. Si vous ne souhaitez pas que votre agent effectue une modification donnée dans Braze, laissez cette autorisation décochée lors de la création de votre clé API. Pour consulter la liste complète des fonctions d'écriture et les autorisations requises, voir [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

### Puis-je utiliser un serveur MCP tiers pour Braze ? {#can-i-use-a-third-party-mcp-server-for-braze}

Il est déconseillé d'utiliser un serveur MCP tiers pour les données Braze. Veuillez utiliser uniquement le serveur officiel MCP Braze hébergé sur [PyPi](https://pypi.org/project/braze-mcp-server/).

### Pourquoi le serveur MCP Braze n'offre-t-il pas d'accès aux informations personnelles identifiables ? {#why-doesnt-the-braze-mcp-server-offer-pii-access}

Afin de protéger les données des utilisateurs tout en favorisant des cas d'utilisation pertinents, le serveur est limité aux endpoints qui ne renvoient généralement pas d'informations personnelles identifiables. Cela permet de réduire les risques pour votre espace de travail et les personnes qui y sont associées.

### Puis-je réutiliser mes clés API ? {#can-i-reuse-my-api-keys}

Non. Vous devrez créer une nouvelle clé API pour votre client MCP. Veillez à n'accorder à vos outils d'intelligence artificielle que l'accès aux données que vous jugez approprié et évitez les autorisations étendues.

### Le serveur MCP Braze est-il hébergé localement ou à distance ? {#is-the-braze-mcp-server-hosted-locally-or-remotely}

Le serveur MCP Braze est hébergé localement.

### Pourquoi Cursor ne répertorie-t-il que des fonctions ? {#why-is-cursor-only-listing-functions}

Vérifiez si vous êtes en mode demande ou en mode agent. Pour utiliser le serveur MCP, il est nécessaire d'être en mode agent.

### Que faire lorsque l'agent renvoie une réponse qui semble incorrecte ? {#what-do-i-do-when-the-agent-returns-an-answer-that-looks-incorrect}

Lorsque vous utilisez des outils tels que Cursor, il peut être utile de changer le modèle utilisé. Par exemple, si vous l'avez réglé sur « auto », essayez de sélectionner un modèle spécifique et testez différentes options afin de déterminer lequel fonctionne le mieux pour votre cas d'utilisation. Vous pouvez également démarrer une nouvelle conversation et réessayer votre requête.

Si les problèmes persistent, vous pouvez nous contacter par e-mail à l'adresse [mcp-product@braze.com](mailto:mcp-product@braze.com) pour nous en informer. Si possible, joignez une vidéo et développez les fonctions d'appel afin que nous puissions examiner les appels que l'agent a tenté d'effectuer.

{% multi_lang_include mcp_server/legal_disclaimer.md %}