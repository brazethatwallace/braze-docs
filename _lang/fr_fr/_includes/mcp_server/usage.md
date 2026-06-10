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
![« Quelles sont les fonctions Braze à ma disposition ? » : question posée et réponse fournie dans Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Quelles sont les fonctions Braze à ma disposition ? » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `list_functions`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obtenir des détails sur un ID Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
![« Obtenir des détails sur un ID Canvas » : question posée et réponse fournie dans Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Obtenir des détails sur un ID Canvas » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `get_canvas_details`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Afficher mes Canvas récents {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
![« Afficher mes Canvas récents » : question posée et réponse fournie dans Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Afficher mes Canvas récents » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `get_canvas_list`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Créer un modèle d'e-mail {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
![« Créer un modèle d'e-mail » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/create_an_email_template.png %})
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `create_email_template`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Mettre à jour un bloc de contenu {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
![« Mettre à jour un bloc de contenu » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/update_a_content_block.png %})
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `update_content_block`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}