# Utilisation du serveur Braze MCP {#using-the-braze-mcp-server}

> Découvrez comment interagir avec vos données Braze à l'aide d'outils de langage naturel tels que Claude et Cursor. Pour plus d'informations générales, consultez [Serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, vous devez [configurer le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Bonnes pratiques {#best-practices}

Lorsque vous utilisez le serveur Braze MCP via des outils de langage naturel tels que Claude et Cursor, gardez ces conseils à l'esprit pour obtenir les meilleurs résultats :

- Les LLM peuvent commettre des erreurs : vérifiez toujours leurs réponses.
- Pour l'analyse des données, précisez clairement la période souhaitée. Les plages plus courtes donnent souvent des résultats plus précis.
- Utilisez la [terminologie Braze](https://www.braze.com/resources/articles/glossary) exacte afin que votre LLM appelle la bonne fonction.
- Si les résultats semblent incomplets, demandez à votre LLM de poursuivre ou d'approfondir.
- Essayez des requêtes créatives ! Selon votre client MCP, vous pourrez peut-être exporter un fichier CSV ou d'autres fichiers utiles.

## Exemples d'utilisation {#usage-examples}

Après avoir [configuré le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, vous pouvez interagir avec Braze en langage naturel grâce à des outils tels que Claude ou Cursor. Voici quelques exemples pour vous aider à démarrer :

### Quelles sont les fonctions Braze à ma disposition ? {#what-are-my-available-braze-functions}

{% tabs %}
{% tab Claude %}
**Example prompt:** `What are my available Braze functions?`

**Example response:** Called `list_functions` and returned categories like Campaign, Canvas, Templates, and Content Blocks with sample functions such as `get_canvas_list` and `create_email_template`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`

**Example response:** Queried `list_functions`, confirmed available function groups, and listed examples including `get_canvas_details` and `update_content_block`.
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `list_functions`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obtenir des détails sur un ID Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Used `get_canvas_details` and returned sample metadata (status, channel, created/updated time) for `YOUR-TEST-CANVAS-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Returned Canvas and message details with dummy values like `YOUR-TEST-MESSAGE-ID-123` and `YOUR-TEST-SUBJECT-LINE`.
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `get_canvas_details`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Afficher mes Canvas récents {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Called `get_canvas_list` and returned recent items such as `YOUR-TEST-CANVAS-ALPHA` with IDs like `YOUR-TEST-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Listed recently edited Canvases with sample values for name, last edited time, ID, and tags.
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `get_canvas_list`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Créer un modèle d'e-mail {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Create an email template named "YOUR-TEST-TEMPLATE-NAME".`

**Example response:** Created a template via `create_email_template` and returned `YOUR-TEST-TEMPLATE-ID-123`.
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `create_email_template`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Mettre à jour un bloc de contenu {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123".`

**Example response:** Updated the block with `update_content_block` and confirmed `YOUR-TEST-CONTENT-BLOCK-ID-123` moved to a new version.
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `update_content_block`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}