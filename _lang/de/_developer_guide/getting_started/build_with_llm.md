---
nav_title: Mit einem LLM entwickeln
article_title: Mit einem LLM entwickeln
page_order: 4
description: "Erfahren Sie, wie Sie KI-Codierungsassistenten mit der Braze-Dokumentation einsetzen können, um Ihren SDK-Integrations-Workflow zu beschleunigen."
platform:
  - Web
  - React Native
---

# Mit einem LLM entwickeln {#building-with-an-llm}

> Nutzen Sie KI-Codierungsassistenten, um Ihren Braze-Integrations-Workflow zu beschleunigen. Verbinden Sie Ihre IDE über Context7 mit dem Braze Docs MCP-Server und erhalten Sie präzise, aktuelle SDK-Anleitungen direkt in Ihrer Entwicklungsumgebung.

KI-Codierungsassistenten können Ihnen beim Schreiben von Integrationscode, bei der Fehlerbehebung und beim Erkunden der Features des Braze SDK behilflich sein&#8212;jedoch nur, wenn sie über den richtigen Kontext verfügen. Der Braze Docs MCP-Server ermöglicht Ihrem KI-Assistenten direkten Zugriff auf die Braze-Dokumentation, sodass er präzise Code-Snippets generieren und technische Fragen auf Grundlage der neuesten SDK-Referenzen beantworten kann.

## Verbindung mit dem Braze Docs MCP herstellen {#connecting-to-the-braze-docs-mcp}

[Context7](https://context7.com/braze-inc/braze-docs) fungiert als Schnittstelle zwischen Ihrem KI-Assistenten und der Braze-Dokumentationsbibliothek. Durch Hinzufügen von Context7 zur MCP-Konfiguration Ihrer IDE kann Ihr KI-Assistent die gesamte Braze-Dokumentation abfragen und bei Bedarf relevante SDK-Referenzen, Code-Beispiele und Integrationsanleitungen abrufen.

### Einrichtung von Context7 {#setting-up-context7}

Um Ihren KI-Assistenten über Context7 mit dem Braze Docs MCP zu verbinden, fügen Sie die folgende Konfiguration zur `mcp.json`-Datei Ihrer IDE hinzu.

{% tabs %}
{% tab Cursor %}
Gehen Sie in [Cursor](https://cursor.com/) zu **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP** und fügen Sie anschließend das folgende Snippet hinzu:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Speichern Sie die Konfiguration und starten Sie Cursor neu. Ihr KI-Assistent kann nun über Context7 auf die Braze-Dokumentation zugreifen, wenn Sie `use context7` in Ihre Prompts einfügen.
{% endtab %}

{% tab Claude %}
Öffnen Sie in Claude Desktop **Settings** > **Developer** > **Edit Config** und fügen Sie Folgendes zu Ihrer `claude_desktop_config.json`-Datei hinzu:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Speichern Sie die Konfiguration und starten Sie Claude Desktop neu.
{% endtab %}

{% tab VS Code %}
Fügen Sie Folgendes zu Ihrer VS Code `settings.json`- oder `.vscode/mcp.json`-Datei hinzu:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Speichern Sie die Konfiguration und starten Sie VS Code neu.
{% endtab %}
{% endtabs %}

{% alert note %}
Context7 unterscheidet sich vom [Braze MCP-Server]({{site.baseurl}}/developer_guide/mcp_server). Context7 gewährt Ihrem KI-Assistenten Zugriff auf die **Braze-Dokumentation**, während der Braze MCP-Server schreibgeschützten Zugriff auf **Ihre Braze-Workspace-Daten** (wie Campaigns, Segmente und Analytics) ermöglicht. Sie können beide zusammen verwenden, um eine umfassendere KI-gestützte Entwicklungserfahrung zu erzielen.
{% endalert %}

## Prompts für die Braze-SDK-Entwicklung schreiben {#writing-prompts-for-braze-sdk-development}

Nachdem Sie Context7 eingerichtet haben, fügen Sie `use context7` in Ihre Prompts ein, um Ihrem KI-Assistenten mitzuteilen, dass er die Braze-Dokumentation als Kontext heranziehen soll. Die folgenden Beispiele veranschaulichen, wie Sie effektive Prompts für gängige SDK-Aufgaben erstellen können.

### React Native SDK {#react-native-sdk}

Diese Prompts veranschaulichen gängige Integrationsaufgaben für das [Braze React Native SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native).

#### Initialisierung des SDK {#initializing-the-sdk}

```text
Using the Braze React Native SDK, show me how to initialize the SDK
in my App.tsx with an API key and custom endpoint. Include the
configuration for automatic session tracking. Use context7.
```

#### Protokollierung angepasster Events mit Eigenschaften {#logging-custom-events-with-properties}

```text
I need to track user activity in my React Native app using the Braze
React Native SDK. Show me how to log a custom event called
"ProductViewed" with properties for product_id, category, and price.
Use context7.
```

#### Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

```text
Using the Braze React Native SDK, walk me through requesting push
notification permissions on both iOS and Android 13+. Include the
code for registering the push token with Braze. Use context7.
```

#### Umgang mit In-App-Nachrichten {#handling-in-app-messages}

```text
Show me how to subscribe to in-app messages using the Braze React
Native SDK, including how to log impressions and button clicks
programmatically. Use context7.
```

### Web SDK {#web-sdk}

Diese Prompts veranschaulichen gängige Integrationsaufgaben für das [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web).

#### Initialisierung des SDK

```text
Using the Braze Web SDK, show me how to initialize the SDK with
braze.initialize(), including the API key, base URL, and options
for enabling logging and automatic in-app message display.
Use context7.
```

#### Tracking von angepassten Events und Käufen {#tracking-custom-events-and-purchases}

```text
Using the Braze Web SDK, create a JavaScript module that logs a
custom event called "VideoPlayed" with properties for video_id,
duration_seconds, and completion_percentage. Also show how to log
a purchase with product ID, price, currency code, and quantity.
Use context7.
```

#### Registrierung für Web-Push {#registering-for-web-push}

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to
register a user for web push notifications after they click a
"Subscribe to updates" button. Include the service worker setup.
Use context7.
```

#### Verwaltung von Nutzerattributen {#managing-user-attributes}

```text
Using the Braze Web SDK, show me how to set standard user attributes
(first name, email, country) and custom user attributes (favorite_genre,
subscription_tier) for the current user. Use context7.
```

## Klartext-Dokumentation {#plain-text-documentation}

Sie können auf die Dokumentation des Braze Developer Guide als reine Textdateien zugreifen, die für KI-Tools und LLMs optimiert sind. Diese Dateien enthalten die Braze-Dokumentation in einem Format, das KI-Assistenten ohne den Aufwand des HTML-Renderings analysieren und verstehen können.

| Datei | Beschreibung |
|------|-------------|
| [llms.txt]({{site.baseurl}}/developer_guide/llms.txt) | Ein Verzeichnis der Braze-Dokumentationsseiten für Entwickler:innen mit Titeln und Beschreibungen. Nutzen Sie dies als Ausgangspunkt, um die verfügbare Dokumentation zu entdecken. |
| [llms-full.txt]({{site.baseurl}}/developer_guide/llms-full.txt) | Die vollständige Braze-Dokumentation für Entwickler:innen in einer einzigen Textdatei, formatiert für die Verwendung mit LLMs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klartext-Dokumentation" }

Diese Dateien entsprechen dem [llms.txt-Standard](https://llmstxt.org/), einer sich entwickelnden Konvention, um Dokumentationen für KI-Tools zugänglich zu machen. Sie können diese Dateien direkt in Ihren Prompts referenzieren oder ihren Inhalt zur Kontextualisierung in ein LLM einfügen.