# Le serveur MCP Braze {#the-braze-mcp-server}

> Découvrez le serveur MCP Braze, une connexion distante sécurisée qui permet aux outils d'intelligence artificielle tels que Claude et Cursor d'accéder aux données Braze non personnelles afin de répondre à des questions, d'analyser des tendances, de fournir des informations et de créer du contenu.

{% alert important %}
Le serveur MCP distant est en accès anticipé. Contactez votre gestionnaire de compte pour demander l'accès.
{% endalert %}

## Qu'est-ce que le Model Context Protocol (MCP) ? {#what-is-model-context-protocol-mcp}

​​Le Model Context Protocol, ou MCP, est un standard qui permet aux agents IA de se connecter à une autre plateforme et d'interagir avec ses données. Il se compose de deux éléments principaux :

- **Client MCP :** L'application dans laquelle l'agent IA s'exécute, comme Cursor ou Claude.
- **Serveur MCP :** Un service fourni par une autre plateforme, comme Braze, qui définit les outils que l'IA peut utiliser et les données auxquelles elle peut accéder.

## À propos du serveur MCP Braze {#about-the-braze-mcp-server}

Après avoir [configuré le serveur MCP Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, vous pouvez connecter des outils d'IA tels que des agents, des assistants et des chatbots directement à Braze, leur permettant de lire des données agrégées comme les analyses de Canvas et de Campaign, les attributs personnalisés, les Segments, et bien plus encore. Le serveur MCP Braze est idéal pour :

- Créer des outils alimentés par l'IA qui nécessitent un contexte Braze.
- Les ingénieurs CRM qui conçoivent des workflows d'agents à plusieurs étapes.
- Les marketeurs techniques qui expérimentent des requêtes en langage naturel.

Le serveur MCP Braze comprend des outils de lecture et d'écriture. Ces outils ne renvoient pas de données issues des profils utilisateur Braze. Vos agents héritent des permissions de votre utilisateur du tableau de bord de Braze. Pour consulter la liste complète des outils disponibles, voir [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Les outils exposant des données d'identification au niveau utilisateur ne sont pas disponibles.
{% endalert %}

Utilisez le serveur MCP pour poser des questions sur les performances des Campaigns et des Canvas, explorer vos Segments et attributs personnalisés, générer des rapports et créer du contenu tel que des modèles d'e-mail, des Content Blocks et des ressources de la bibliothèque multimédia grâce au langage naturel.

## Le serveur MCP bêta est-il obsolète ? {#is-the-beta-mcp-server-deprecated}

Oui. Le serveur MCP hébergé localement, publié en août 2025, est obsolète et ne recevra pas de mises à jour supplémentaires. Vous pouvez continuer à l'utiliser, mais Braze recommande de migrer vers la version hébergée à distance.

### En quoi le serveur distant est-il différent ? {#how-is-the-remote-server-different}

Le précédent serveur MCP de Braze s'exécutait localement sur votre machine. Vous deviez installer un package, gérer un fichier de configuration et créer une clé API Braze avec les permissions appropriées. Le serveur MCP distant supprime cette configuration locale.

Connectez-vous depuis un client MCP compatible en moins d'une minute. L'authentification utilise OAuth. L'accès est lié à votre compte utilisateur du tableau de bord de Braze, et non à une clé API partagée. Ainsi, ce qu'un agent peut voir et faire reflète vos permissions dans le tableau de bord. Si un utilisateur du tableau de bord perd son accès dans Braze, le client perd également son accès.

Les principales différences sont :

- **Configuration :** Collez une URL Braze au lieu d'installer un package et de modifier des fichiers de configuration.
- **Authentification :** Connectez-vous avec votre compte Braze au lieu de créer une clé API.
- **Permissions :** L'accès est basé sur votre compte utilisateur du tableau de bord au lieu des permissions de la clé API.
- **Ciblage de l'espace de travail :** Le contexte de l'espace de travail est transmis à chaque requête au lieu d'être fixé dans la configuration locale.

## Foire aux questions (FAQ) {#faq}

### Quels clients MCP sont pris en charge ? {#which-mcp-clients-are-supported}

Tout client MCP prenant en charge les serveurs MCP distants avec OAuth peut fonctionner. Braze a vérifié :

- Claude via des connecteurs personnalisés
- ChatGPT via des connecteurs personnalisés
- Cursor
- OpenAI Codex
- Claude Code
- Visual Studio Code

### À quelles données Braze mon client MCP a-t-il accès ? {#what-braze-data-can-my-mcp-client-access}

Les clients MCP peuvent accéder aux outils qui ne renvoient pas de données d'identification au niveau utilisateur.

### Mon client MCP peut-il modifier les données Braze ? {#can-my-mcp-client-change-braze-data}

Oui, si votre utilisateur du tableau de bord dispose de ces autorisations.

### Ai-je encore besoin d'une clé API Braze ? {#do-i-still-need-a-braze-api-key}

Pas pour le MCP. Les clés API fonctionnent toujours pour la REST API et ne sont pas en cours de dépréciation.

### Quelles régions sont prises en charge ? {#which-regions-are-supported}

Les deux clusters Braze sont pris en charge. Deux endpoints sont disponibles aujourd'hui :

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

L'un ou l'autre endpoint peut atteindre n'importe quel cluster Braze.

### Puis-je utiliser le serveur MCP distant Braze avec des outils autres que ceux de la liste vérifiée ? {#can-i-use-the-braze-remote-mcp-server-with-tools-other-than-the-verified-list}

Vous pouvez essayer, mais l'authentification peut être bloquée. Braze maintient actuellement une liste autorisée de domaines pris en charge pour des raisons de sécurité. Si votre outil ne figure pas sur la liste et que vous rencontrez des problèmes d'authentification, contactez [mcp-product@braze.com](mailto:mcp-product@braze.com).

### Le serveur distant prend-il en charge plusieurs espaces de travail ? {#does-the-remote-server-support-multiple-workspaces}

Oui. Spécifiez l'espace de travail par conversation ou par requête. Une seule connexion couvre tous les espaces de travail auxquels vous êtes autorisé à accéder.

### Mon agent peut-il accéder aux données d'identification au niveau utilisateur ? {#can-my-agent-access-user-level-pii}

Non. À ce jour, les outils exposant des données d'identification ne sont pas disponibles.

### Que se passe-t-il lorsque mes autorisations changent ? {#what-happens-when-my-permissions-change}

L'accès de l'agent évolue avec l'utilisateur du tableau de bord. Les modifications d'autorisations s'appliquent à la requête suivante. Les utilisateurs du tableau de bord désactivés perdent l'accès au MCP.

### Pourquoi ne vois-je pas le connecteur Braze dans le répertoire de mon client ? {#why-do-i-not-see-the-braze-connector-in-my-clients-directory}

Les inscriptions dans les répertoires sont déployées après le début de l'accès anticipé. Vous pouvez toujours vous connecter manuellement en utilisant l'URL MCP Braze.

### Mon entreprise utilise une liste d'adresses IP autorisées. Pouvons-nous utiliser le serveur MCP distant ? {#my-company-uses-ip-allowlisting-can-we-use-the-remote-mcp-server}

Pas pour le moment. Les clients qui utilisent la [liste d'adresses IP autorisées](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) ne peuvent pas participer au programme d'accès anticipé.

{% multi_lang_include mcp_server/legal_disclaimer.md %}