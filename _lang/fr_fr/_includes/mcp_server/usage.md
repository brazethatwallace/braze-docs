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
**Exemple de requête**

`What are my available Braze functions?`

**Exemple de réponse**

J'ai interrogé le serveur Braze MCP avec `list_functions` et trouvé 38 fonctions API disponibles.

Voici quelques exemples par catégorie :

- **Analyse et gestion des Campaigns**
  - `get_campaign_dataseries`
  - `get_campaign_details`
  - `get_campaign_list`
- **Analyse et gestion des Canvas**
  - `get_canvas_data_series`
  - `get_canvas_data_summary`
  - `get_canvas_list`
  - `get_canvas_details`
- **Modèles**
  - `create_email_template`
- **Content Blocks**
  - `create_content_block`
  - `get_content_blocks`
  - `get_content_block_info`
  - `update_content_block`
{% endtab %}

{% tab Cursor %}
**Exemple de requête**

`What are my available Braze functions?`

**Exemple de réponse**

Je vais vérifier vos fonctions disponibles à l'aide du serveur Braze MCP.

- Appel de `list_functions`

D'après le résultat, vous disposez de 38 fonctions API Braze organisées en catégories telles que :

- Analyse et gestion des Campaigns
- Analyse et gestion des Canvas
- Modèles
- Content Blocks

Exemples de fonctions :

- `get_campaign_list`
- `get_canvas_list`
- `get_canvas_details`
- `create_email_template`
- `update_content_block`
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `list_functions`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obtenir des détails sur un ID Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Exemple de requête**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Exemple de réponse**

J'ai récupéré les détails de `YOUR-TEST-CANVAS-ID-123` à l'aide de `get_canvas_details`.

- **Nom du Canvas :** `YOUR-TEST-CANVAS-NAME`
- **ID :** `YOUR-TEST-CANVAS-ID-123`
- **État :** Brouillon (non activé)
- **Créé le :** 15 janv. 2026, 10 h 30 UTC
- **Dernière mise à jour :** 16 janv. 2026, 14 h 45 UTC
- **Type de planification :** Basé sur le temps
- **Canal principal :** E-mail

Détails du message e-mail :

- **Objet :** `YOUR-TEST-SUBJECT-LINE`
- **Expéditeur :** `YOUR-TEST-SENDER@example.com`
- **ID du message :** `YOUR-TEST-MESSAGE-ID-123`
{% endtab %}

{% tab Cursor %}
**Exemple de requête**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Exemple de réponse**

J'ai récupéré ce Canvas à l'aide de `get_canvas_details` :

- **ID du Canvas :** `YOUR-TEST-CANVAS-ID-123`
- **Nom du Canvas :** `YOUR-TEST-CANVAS-NAME`
- **État :** Brouillon
- **Canal :** E-mail
- **ID du message :** `YOUR-TEST-MESSAGE-ID-123`

Résumé du contenu de l'e-mail :

1. Section d'en-tête avec image de marque
2. Section de titre principal
3. Section héros avec bouton CTA
4. Section de fonctionnalités avec contenu complémentaire
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `get_canvas_details`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Afficher mes Canvas récents {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Exemple de requête**

`Show me my recent Canvases`

**Exemple de réponse**

J'ai vérifié vos outils disponibles avec `list_functions`, puis utilisé `get_canvas_list` pour récupérer vos Canvas les plus récemment modifiés.

Canvas les plus récents :

1. **YOUR-TEST-CANVAS-ALPHA**
   - ID : `YOUR-TEST-ID-123`
   - Dernière modification : 16 janv. 2026, 14 h 45 UTC
2. **YOUR-TEST-CANVAS-BETA**
   - ID : `YOUR-TEST-ID-456`
   - Dernière modification : 15 janv. 2026, 11 h 10 UTC
3. **YOUR-TEST-CANVAS-GAMMA**
   - ID : `YOUR-TEST-ID-789`
   - Dernière modification : 14 janv. 2026, 20 h 25 UTC
{% endtab %}

{% tab Cursor %}
**Exemple de requête**

`Show me my recent Canvases`

**Exemple de réponse**

Je vais récupérer votre liste de Canvas récents depuis le serveur Braze MCP.

- Appel de `list_functions`
- Appel de `get_canvas_list`

Canvas récents (triés par date de dernière modification) :

- **Nom du Canvas :** `YOUR-TEST-CANVAS-ALPHA`
  - **Dernière modification :** 16 janv. 2026, 14 h 45 UTC
  - **ID du Canvas :** `YOUR-TEST-ID-123`
  - **Étiquettes :** `lifecycle`, `email`
- **Nom du Canvas :** `YOUR-TEST-CANVAS-BETA`
  - **Dernière modification :** 15 janv. 2026, 11 h 10 UTC
  - **ID du Canvas :** `YOUR-TEST-ID-456`
  - **Étiquettes :** `promo`
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `get_canvas_list`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Créer un modèle d'e-mail {#create-an-email-template}

{% tabs %}
{% tab Claude %}
**Exemple de requête**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Exemple de réponse**

J'ai créé votre modèle avec `create_email_template`.

- **Nom du modèle :** `YOUR-TEST-TEMPLATE-NAME`
- **ID du modèle :** `YOUR-TEST-TEMPLATE-ID-123`
- **Ligne d'objet :** `YOUR-TEST-SUBJECT-LINE`
- **Accroche :** `YOUR-TEST-PREHEADER`
- **Créé le :** 16 janv. 2026, 15 h 10 UTC

Vous pouvez désormais référencer `YOUR-TEST-TEMPLATE-ID-123` lors de la création ou de la mise à jour de Campaigns et de Canvas.
{% endtab %}

{% tab Cursor %}
**Exemple de requête**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Exemple de réponse**

J'ai utilisé `create_email_template` et créé un nouveau modèle avec succès.

- **ID du modèle :** `YOUR-TEST-TEMPLATE-ID-123`
- **Nom du modèle :** `YOUR-TEST-TEMPLATE-NAME`
- **Objet :** `YOUR-TEST-SUBJECT-LINE`
- **Description :** `Onboarding lifecycle template`

Si vous le souhaitez, je peux également générer un corps HTML de départ et une version texte brut de secours pour ce modèle.
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `create_email_template`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Mettre à jour un bloc de contenu {#update-a-content-block}

{% tabs %}
{% tab Claude %}
**Exemple de requête**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Exemple de réponse**

J'ai mis à jour votre bloc de contenu à l'aide de `update_content_block`.

- **ID du bloc de contenu :** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Nom :** `YOUR-TEST-CONTENT-BLOCK-NAME`
- **État :** Mis à jour
- **Mis à jour le :** 16 janv. 2026, 15 h 25 UTC

Aperçu :

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}

{% tab Cursor %}
**Exemple de requête**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Exemple de réponse**

J'ai exécuté `update_content_block` et confirmé que la mise à jour a été effectuée.

- **ID du bloc de contenu :** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Version précédente :** `v1`
- **Version actuelle :** `v2`
- **Dernière mise à jour :** 16 janv. 2026, 15 h 25 UTC

Aperçu du contenu mis à jour :

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}
{% endtabs %}

Pour en savoir plus sur la fonction `update_content_block`, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}