# Configurer le serveur Braze MCP {#setting-up-the-braze-mcp-server}

> Découvrez comment configurer le serveur Braze MCP afin de pouvoir interagir avec vos données Braze en langage naturel à l'aide d'outils tels que Claude et Cursor. Pour obtenir des informations plus générales, consultez [Serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Prérequis | Description |
|--------------|-------------|
| Clé API Braze | Une clé API Braze avec les autorisations requises. Vous créerez une nouvelle clé lors de la [configuration de votre serveur Braze MCP](#create-api-key). |
| Client MCP | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) et [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) sont officiellement pris en charge. Vous devez disposer d'un compte auprès de l'un de ces clients pour utiliser le serveur Braze MCP. |
| Terminal | Une application de terminal vous permettant d'exécuter des commandes et d'installer des outils. Utilisez votre application de terminal préférée ou celle préinstallée sur votre ordinateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Configuration du serveur Braze MCP

### Étape 1 : Installer `uv` {#step-1-install-uv}

Commencez par installer `uv`&#8212;un [outil en ligne de commande développé par Astral](https://docs.astral.sh/uv/getting-started/installation/) pour la gestion des dépendances et des paquets Python.

{% tabs local %}
{% tab MacOS and Linux %}
Ouvrez votre application de terminal, collez la commande suivante, puis appuyez sur <kbd>Entrée</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Le résultat est similaire à ce qui suit :

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Ouvrez Windows PowerShell, collez la commande suivante, puis appuyez sur <kbd>Entrée</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Le résultat est similaire à ce qui suit :

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### Étape 2 : Créer une clé API {#create-api-key}

Le serveur Braze MCP comprend des endpoints en lecture seule et des endpoints en écriture. Ils ne renvoient pas de données issues des profils utilisateurs Braze. Les endpoints en écriture permettent aux agents de créer ou de mettre à jour du contenu dans votre espace de travail.

Pour créer votre clé API :

1. Rendez-vous dans **Paramètres** > **API et identifiants** > **Clés API**.
2. Créez une nouvelle clé.
3. Attribuez certaines ou toutes les autorisations suivantes à votre clé.

{% alert important %}
N'attribuez que les autorisations que vous souhaitez que votre agent utilise. Pour empêcher votre agent d'effectuer des modifications dans Braze, ne cochez aucune autorisation d'écriture lors de la création de votre clé API.
{% endalert %}

{% details Liste des autorisations prises en charge %}
#### Campaigns

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

#### Canvas

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas" }

#### Catalogues {#catalogs}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalogs" }

#### Ingestion de données cloud {#cloud-data-ingestion}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cloud Data Ingestion" }

#### Content Blocks

Les autorisations `content_blocks.create` et `content_blocks.update` sont des autorisations d'écriture. Ne les ajoutez que si vous souhaitez que votre agent puisse créer ou mettre à jour des Content Blocks dans votre espace de travail.

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | `content_blocks.info` |
| [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | `content_blocks.create` |
| [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | `content_blocks.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

#### Attributs personnalisés {#custom-attributes}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom Attributes" }

#### Événements {#events}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Events" }

#### Indicateurs clés de performance {#kpis}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KPIs" }

#### Bibliothèque multimédia {#media-library}

L'autorisation `media_library.create` est une autorisation d'écriture. Ne l'ajoutez que si vous souhaitez que votre agent puisse importer des ressources dans votre bibliothèque multimédia.

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | `media_library.create` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Media Library" }

#### Messages

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messages" }

#### Centre de préférences {#preference-center}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Preference Center" }

#### Achats {#purchases}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Purchases" }

#### Segments

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segments" }

#### Envois {#sends}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sends" }

#### Sessions

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sessions" }

#### Clés d'authentification SDK {#sdk-authentication-keys}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK Authentication Keys" }

#### Abonnement {#subscription}

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription" }

#### Modèles {#templates}

Les autorisations `templates.email.create` et `templates.email.update` sont des autorisations d'écriture. Ne les ajoutez que si vous souhaitez que votre agent puisse créer ou mettre à jour des modèles d'e-mail dans votre espace de travail.

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | `templates.email.info` |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | `templates.email.create` |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | `templates.email.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Templates" }
{% enddetails %}

{% alert warning %}
Ne réutilisez pas une clé API existante. Créez-en une spécifiquement pour votre client MCP. N'attribuez que les autorisations dont votre agent a besoin. Les agents peuvent tenter d'utiliser toute autorisation que vous leur accordez : ne cochez donc pas les autorisations d'écriture si vous ne souhaitez pas que votre agent effectue des modifications dans Braze.
{% endalert %}

### Étape 3 : Obtenir votre identifiant et votre endpoint {#step-3-get-your-identifier-and-endpoint}

Lorsque vous configurez votre client MCP, vous aurez besoin de l'identifiant de votre clé API et de l'endpoint REST de votre espace de travail. Pour obtenir ces informations, retournez à la page **Clés API** dans le tableau de bord&#8212;gardez cette page ouverte afin de pouvoir vous y référer lors de [l'étape suivante](#configure-client).

![La page « Clés API » dans Braze affichant une clé API nouvellement créée et l'endpoint REST de l'utilisateur.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Étape 4 : Configurer votre client MCP {#configure-client}

Configurez votre client MCP à l'aide du fichier de configuration fourni.

{% tabs %}
{% tab Claude %}
Configurez votre serveur MCP en utilisant le répertoire de connecteurs de [Claude Desktop](https://claude.ai/download).

1. Dans Claude Desktop, rendez-vous dans **Settings** > **Connectors** > **Browse Connectors** > **Desktop Extensions** > **Braze MCP Server** > **Install**.
2. Saisissez votre clé API et votre URL de base.
3. Enregistrez la configuration et redémarrez Claude Desktop.

{% endtab %}

{% tab Cursor %}
Dans [Cursor](https://cursor.com/), rendez-vous dans **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP**, puis ajoutez l'extrait de code suivant :

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

Remplacez `key-identifier` et `rest-endpoint` par les valeurs correspondantes figurant sur la page **Clés API** dans Braze. Votre configuration devrait être similaire à ce qui suit :

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Une fois terminé, enregistrez la configuration et redémarrez Cursor.
{% endtab %}
{% tab Gemini CLI %}
Gemini CLI lit les paramètres utilisateur à partir de `~/.gemini/settings.json`. Si ce fichier n'existe pas, vous pouvez le créer en exécutant la commande suivante dans votre terminal :

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

Ensuite, remplacez `yourname` par la chaîne de caractères exacte précédant `@BZXXXXXXXX` dans votre invite de commande. Puis remplacez `key-identifier` et `rest-endpoint` par les valeurs correspondantes figurant sur la page **Clés API** dans Braze.

Votre configuration devrait être similaire à ce qui suit :

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Une fois terminé, enregistrez la configuration et redémarrez Gemini CLI. Ensuite, dans Gemini, exécutez les commandes suivantes pour vérifier que le serveur Braze MCP est répertorié et que les outils et le schéma sont disponibles :

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Vous devriez voir le serveur `braze` répertorié avec les outils et le schéma disponibles.

{% endtab %}
{% endtabs %}

### Étape 5 : Envoyer un prompt de test {#step-5-send-a-test-prompt}

Après avoir configuré le serveur Braze MCP, essayez d'envoyer un prompt de test à votre client MCP. Pour d'autres exemples et bonnes pratiques, consultez [Utilisation du serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
**Exemple de prompt :** `What are my available Braze functions?`
**Exemple de réponse :** A utilisé `list_functions` et renvoyé les catégories de fonctions Braze MCP disponibles.
{% endtab %}

{% tab Cursor %}
**Exemple de prompt :** `What are my available Braze functions?`
**Exemple de réponse :** A interrogé `list_functions` et listé les fonctions telles que `get_canvas_list`.
{% endtab %}

{% tab Gemini CLI %}
**Exemple de prompt :** `What are my available Braze functions?`
**Exemple de réponse :** A interrogé `list_functions` dans Gemini CLI et renvoyé les catégories de fonctions Braze MCP disponibles ainsi que des exemples de fonctions.
{% endtab %}
{% endtabs %}

## Résolution des problèmes {#troubleshooting}

### Erreurs de terminal {#terminal-errors}

#### Commande `uvx` introuvable {#uvx-command-not-found}

Si vous recevez une erreur indiquant que la commande `uvx` est introuvable, réinstallez `uv` et redémarrez votre terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Erreur `spawn uvx ENOENT` {#spawn-uvx-enoent-error}

Si vous rencontrez des erreurs `spawn uvx ENOENT`, il peut être nécessaire de mettre à jour le chemin d'accès dans le fichier de configuration de votre client. Commencez par ouvrir votre terminal et exécutez la commande suivante :

```bash
which uvx
```

La commande devrait renvoyer un message similaire à ce qui suit :

```bash
/Users/alex-lee/.local/bin/uvx
```

Copiez le message dans votre presse-papiers et ouvrez [le fichier de configuration de votre client](#configure-client). Remplacez `"command": "uvx"` par le chemin que vous avez copié, puis redémarrez votre client. Par exemple :

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### L'installation du paquet échoue {#package-installation-fails}

Si l'installation de votre paquet échoue, essayez d'installer une version spécifique de Python à la place.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuration du client {#client-configuration}

#### « Cette extension n'est pas compatible avec votre appareil » {#this-extension-is-not-compatible-with-your-device}

Si vous voyez cette erreur lors de l'installation de l'extension du serveur Braze MCP, cela peut indiquer l'une des situations suivantes :

- **Votre appareil ne répond pas aux exigences** : certaines extensions de serveur MCP nécessitent des versions spécifiques du système d'exploitation ou du matériel.
- **Outils de développement manquants (macOS uniquement)** : sur macOS, l'installation de l'extension nécessite les outils de développement en ligne de commande pour exécuter les commandes Python. Si ces outils ne sont pas installés, l'installation échouera avec cette erreur.

Pour installer les outils de développement en ligne de commande sur macOS, exécutez la commande suivante dans votre terminal :

```bash
xcode-select --install
```

Une fois l'installation terminée, redémarrez votre client MCP et essayez à nouveau d'installer l'extension.

#### Le client MCP ne parvient pas à trouver le serveur Braze {#mcp-client-cant-find-the-braze-server}

1. Vérifiez que la syntaxe de configuration de votre client MCP est correcte.
2. Redémarrez votre client MCP après avoir modifié la configuration.
3. Vérifiez que `uvx` est présent dans le `PATH` de votre système.

#### Erreurs d'authentification {#authentication-errors}

1. Vérifiez que votre `BRAZE_API_KEY` est correcte et active.
2. Assurez-vous que votre `BRAZE_BASE_URL` correspond à votre instance Braze.
3. Vérifiez que votre clé API dispose des [autorisations appropriées](#create-api-key).

#### Délais d'attente de connexion ou erreurs réseau {#connection-timeouts-or-network-errors}

1. Vérifiez que votre `BRAZE_BASE_URL` est correcte pour votre instance.
2. Vérifiez votre connexion réseau et les paramètres de votre pare-feu.
3. Assurez-vous que vous utilisez le protocole HTTPS dans votre URL de base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}