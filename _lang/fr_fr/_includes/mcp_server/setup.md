# Configurer le serveur Braze MCP {#setting-up-the-braze-mcp-server}

> Découvrez comment vous connecter au serveur Braze MCP distant, vous authentifier avec OAuth et commencer à utiliser les outils Braze depuis votre client MCP. Pour plus d'informations, consultez [Serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables {#prerequisites}

Avant de commencer, assurez-vous de disposer des éléments suivants :

| Prérequis | Description |
|--------------|-------------|
| Inscription à l'accès anticipé | Votre gestionnaire de compte peut inscrire votre entreprise au programme d'accès anticipé. |
| Client MCP pris en charge | Tout client prenant en charge les serveurs MCP distants avec OAuth peut fonctionner. Braze a vérifié Claude, ChatGPT, Cursor, OpenAI Codex et Claude Code. |
| Compte sur le tableau de bord de Braze | Vous vous connectez avec vos identifiants Braze habituels, y compris SSO ou SAML si votre entreprise les utilise. Il n'y a pas d'identifiant MCP distinct. |
| Sélection de l'endpoint du serveur | Choisissez `https://mcp.braze.com/mcp` (US) ou `https://mcp.braze.eu/mcp` (EU). Les deux endpoints peuvent atteindre n'importe quel cluster Braze. |
| Pas de liste d'autorisation IP | Les clients qui utilisent la [liste d'autorisation IP](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) ne peuvent pas participer à l'accès anticipé pour le moment. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

{% alert note %}
L'accès de votre agent reflète vos autorisations sur le tableau de bord. Si votre accès au tableau de bord est limité à une équipe plutôt qu'à un espace de travail complet, certains outils peuvent ne pas fonctionner pendant l'accès anticipé.
{% endalert %}

## Gérer l'accès (pour les administrateurs) {#managing-access-for-admins}

### Accorder l'accès {#grant-access}

Les administrateurs contrôlent l'accès au serveur MCP via l'autorisation **Use MCP Server**. Par défaut, les utilisateurs ne disposent pas de cette autorisation et elle doit être explicitement accordée.

Si un administrateur ne voit pas cette autorisation, contactez votre gestionnaire de compte Braze pour demander l'inscription à l'accès anticipé.

### Révoquer l'accès {#revoke-access}

Pour révoquer l'accès, retirez l'autorisation **Use MCP Server** de l'utilisateur. La suppression des autorisations du tableau de bord d'un utilisateur supprime également ces capacités de tout agent connecté lors de la prochaine requête.

### Auditer l'utilisation {#audit-usage}

Lorsqu'un utilisateur se connecte avec succès via OAuth, un événement est enregistré dans le [rapport d'événements de sécurité](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report).

## Connecter votre client {#connect-your-client}

### Étape 1 : Confirmer les autorisations et l'accès à l'espace de travail {#step-1-confirm-permissions-and-workspace-access}

1. Vous ou l'administrateur de votre entreprise devez confirmer que vous disposez de l'autorisation **Use MCP Server**.
2. Si vous avez besoin d'accéder à plusieurs espaces de travail, assurez-vous que l'autorisation est activée pour tous les espaces de travail concernés.

### Étape 2 : Ajouter Braze en tant que connecteur MCP distant {#step-2-add-braze-as-a-remote-mcp-connector}

Dans votre client MCP, ajoutez un nouveau serveur distant ou connecteur personnalisé et saisissez votre URL Braze MCP. Par exemple, dans Claude, vous pouvez aller dans **Settings** > **Connectors** > **Add custom connector** et coller l'URL.

Aucun identifiant client, secret client ou clé API n'est requis. Votre client s'enregistre automatiquement auprès de Braze.

Options d'endpoint Braze MCP :

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

{% alert tip %}
Les clients EU doivent utiliser l'endpoint EU. Les clients non-EU peuvent utiliser l'un ou l'autre endpoint.
{% endalert %}

Guides de configuration des clients :

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)

### Étape 3 : Se connecter à Braze via OAuth {#step-3-sign-in-to-braze-through-oauth}

La première fois que votre agent appelle un outil Braze, votre client ouvre une fenêtre de navigateur et vous redirige vers Braze pour vous connecter.

1. Connectez-vous à Braze comme vous le feriez normalement, y compris via SSO si nécessaire.
2. Si votre identifiant peut accéder à plusieurs entreprises sur le même cluster, sélectionnez l'entreprise que vous souhaitez utiliser.
3. Sur l'écran de consentement, examinez l'accès demandé par l'application.
4. Cochez la case d'acceptation pour accepter la politique de confidentialité de Braze, puis sélectionnez **Continue** pour revenir à votre client MCP.

![L'écran de consentement Braze montrant que Claude Desktop demande l'accès aux informations du compte Braze et un accès étendu aux données Braze, avec une case d'acceptation de la politique de confidentialité et les boutons Cancel et Continue.]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: style="max-width:65%;"}

Votre session utilise des jetons d'accès à durée de vie courte qui se renouvellent automatiquement. Vous devrez peut-être vous reconnecter occasionnellement.

### Étape 4 : Indiquer à votre agent quel espace de travail utiliser {#step-4-tell-your-agent-which-workspace-to-use}

Si votre compte peut accéder à plusieurs espaces de travail, précisez l'espace de travail dans votre prompt. Par exemple :

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

Si vous ne précisez pas d'espace de travail, votre agent peut vous demander de clarifier.

### Étape 5 : Envoyer un prompt de test {#step-5-send-a-test-prompt}

Après la configuration, envoyez un prompt de validation rapide tel que :

- `List the Braze tools available in this workspace.`
- `Show my recent Canvases from the Production workspace.`

Pour d'autres exemples, consultez [Utilisation du serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

## Exemple : se connecter avec Claude {#example-connect-with-claude}

La connexion d'un client ne prend que quelques étapes. La procédure suivante utilise Claude, mais le flux est similaire pour les autres clients pris en charge.

1. Dans Claude, allez dans **Settings** > **Connectors** > **Add custom connector**.
2. Saisissez un nom, par exemple `Braze`, puis collez votre URL Braze MCP : `https://mcp.braze.com/mcp` pour les US ou `https://mcp.braze.eu/mcp` pour l'EU. Vous n'avez pas besoin d'identifiant client, de secret client ou de clé API.
3. Sélectionnez **Add** pour enregistrer le connecteur. Claude s'enregistre automatiquement auprès de Braze.
4. Sélectionnez **Connect** pour démarrer l'authentification. Claude ouvre une fenêtre de navigateur et vous redirige vers Braze pour vous connecter.
5. Connectez-vous à Braze avec vos identifiants habituels, y compris SSO si votre entreprise l'utilise. Si votre identifiant peut accéder à plusieurs entreprises sur le même cluster, sélectionnez l'entreprise que vous souhaitez utiliser.
6. Sur l'écran de consentement, examinez l'accès demandé, cochez la case d'acceptation, puis sélectionnez **Continue**. Claude revient à votre conversation et votre agent peut désormais utiliser les outils Braze.

Pour confirmer la connexion, envoyez un prompt de test tel que `Show my recent Canvases from the Production workspace`.

## Migration depuis le serveur bêta local {#migrating-from-the-local-beta-server}

Vous pouvez exécuter le serveur bêta local et le serveur hébergé à distance en parallèle pendant la migration. Vous devrez peut-être indiquer explicitement à votre agent lequel utiliser.

Le serveur hébergé à distance inclut de nouveaux outils qui n'existent pas dans le serveur bêta local. Si vous avez créé des compétences pour le serveur local, vous devrez peut-être mettre à jour ces compétences pour référencer les nouveaux noms et comportements des outils.

Une fois que vous avez confirmé que vos workflows et compétences fonctionnent sur le serveur distant, désactivez le serveur hébergé localement.

## Résolution des problèmes {#troubleshooting}

### L'authentification échoue dans un client pris en charge {#authentication-fails-in-a-supported-client}

1. Confirmez que votre entreprise est inscrite à l'accès anticipé.
2. Confirmez que votre utilisateur dispose de l'autorisation **Use MCP Server**.
3. Réessayez la connexion et l'autorisation.

### L'authentification est bloquée dans un client non vérifié {#authentication-is-blocked-in-an-unverified-client}

Pendant l'accès anticipé, Braze maintient une liste d'autorisation des domaines de clients pris en charge pour des raisons de sécurité. Si vous vous connectez depuis un client qui ne figure pas sur la liste d'autorisation, l'authentification peut être bloquée. Si vous pensez que votre client devrait être pris en charge, contactez [mcp-product@braze.com](mailto:mcp-product@braze.com).

Les clients qui s'exécutent localement sur votre machine sans schéma personnalisé, tels que Claude Code et OpenAI Codex, devraient également fonctionner.

### L'agent ne peut pas accéder aux outils attendus {#agent-cannot-access-expected-tools}

1. Confirmez que votre utilisateur du tableau de bord dispose des autorisations requises. Votre agent ne peut utiliser que les outils correspondant à votre propre accès au tableau de bord.
2. Confirmez que vous avez sélectionné l'espace de travail attendu dans votre prompt.
3. Demandez à votre agent d'appeler `get_workspaces` et vérifiez les identifiants d'espaces de travail disponibles.

### L'agent utilise le mauvais espace de travail {#agent-uses-the-wrong-workspace}

Si votre compte peut accéder à plusieurs espaces de travail, nommez l'espace de travail dans votre prompt en utilisant le nom exact affiché dans le tableau de bord de Braze. Si vous ne précisez pas d'espace de travail, votre agent peut vous demander de clarifier ou en utiliser un inattendu.

{% alert important %}
Avant que votre agent ne commence à travailler, confirmez toujours quel espace de travail il utilise. Dans certains cas, un agent peut sélectionner un espace de travail différent de celui que vous aviez prévu.
{% endalert %}

### Changer d'entreprise {#switching-to-a-different-company}

Votre entreprise est définie lors de votre première autorisation. Pour travailler dans une autre entreprise sur le même cluster, déconnectez le connecteur Braze dans votre client, autorisez à nouveau et sélectionnez l'autre entreprise lors de la connexion.

{% multi_lang_include mcp_server/legal_disclaimer.md %}