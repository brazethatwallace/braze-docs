# Integration der ChatGPT-App {#chatgpt-app-integration}

## Einrichtung {#setup}

### 1. Schritt: Die Braze-Integrationsdatei herunterladen {#step-1-get-the-braze-integration-file}

Kopieren Sie die `braze.js`-Datei aus unserem [ChatGPT-Apps-Integrations-Repository](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) in Ihr Projekt. Diese Datei enthält alle erforderlichen Konfigurations- und Hilfsfunktionen für das Braze SDK.

### 2. Schritt: Abhängigkeiten installieren {#step-2-install-dependencies}

Installieren Sie unser Web SDK, um die aktuellsten Features von Braze zu nutzen:

**Für die clientseitige Integration:**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Implementierung

Es gibt zwei Möglichkeiten für die Integration von Braze in Ihre ChatGPT-App je nach Ihrem Anwendungsfall:

### Clientseitige Integration (angepasste Widgets)

{% alert tip %}
**Empfohlener Ansatz:** Diese Methode ermöglicht umfangreiche Messaging-Erlebnisse und Realtime-Tracking von Benutzerinteraktionen innerhalb Ihrer ChatGPT-App-Widgets.
{% endalert %}

Um Braze-Nachrichten anzuzeigen und Benutzerinteraktionen innerhalb Ihrer angepassten ChatGPT-App-Widgets zu verfolgen, verwenden Sie bitte die Web-SDK-Integration. Ein vollständiges Beispiel für das Messaging finden Sie in unserem Beispiel-Repository [hier](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox).

#### Widget-Metadaten konfigurieren

Fügen Sie die folgenden Metadaten zu Ihrer MCP-Serverdatei hinzu, um Braze-Domains zulässig zu machen. Achten Sie dabei darauf, die CDN-Domain entsprechend [Ihrer Region]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) zu aktualisieren:

```javascript
"openai/widgetCSP": {
  connect_domains: ["https://YOUR-SDK-ENDPOINT"],
  resource_domains: [
    "https://appboy-images.com",
    "https://braze-images.com",
    "https://cdn.braze.eu",
    "https://use.fontawesome.com"
  ],
}
```

Ersetzen Sie `YOUR-SDK-ENDPOINT` durch Ihren tatsächlichen Braze-SDK-Endpunkt.

#### Den useBraze-Hook einrichten {#set-up-the-usebraze-hook}

```javascript
import { useBraze } from "./utils/braze";

function YourWidget() {
  const braze = useBraze({
    apiKey: "your-braze-api-key",
    baseUrl: "your-braze-endpoint.braze.com",
  });

  useEffect(() => {
    if (!braze.isInitialized) {
      return;
    }

    // Set user identity
    braze.changeUser("user-id-123");

    // Log widget interactions
    braze.logCustomEvent("viewed_pizzaz_list");
  }, [braze.isInitialized]);

  return (
    // Your widget JSX
  );
}
```

#### Braze Content Cards anzeigen {#display-braze-content-cards}

```javascript
const [cards, setCards] = useState([]);

useEffect(() => {
  // Get cached content cards
  setCards(braze.getCachedContentCards()?.cards ?? []);

  // Subscribe to content card updates
  braze.subscribeToContentCardsUpdates((contentCards) => {
    setCards(contentCards.cards);
  });

  // Open session
  braze.openSession();

  return () => {
    braze.removeAllSubscriptions();
  }
}, []);
```

#### Widget-Events verfolgen {#track-widget-events}

```javascript
// Track user interactions within your widget
const handleButtonClick = () => {
  braze.logCustomEvent("widget_button_clicked", {
    button_type: "save_list",
    widget_name: "pizza_list"
  });
};

const handleItemInteraction = (itemId) => {
  braze.logCustomEvent("item_interacted", {
    item_id: itemId,
    interaction_type: "view_details"
  });
};
```

### Serverseitige Integration (MCP-Server) {#server-side-integration-mcp-server}

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
Sollten Sie auch eine serverseitige Integration für Messaging-Funktionen auf Ihrem MCP-Server benötigen, wenden Sie sich an <span style="white-space:nowrap;">`mcp-product@braze.com`</span>. Für das Tracking von Events und Käufen von Ihrem MCP-Server verwenden Sie unsere [REST API]({{site.baseurl}}/api/home/).

<!-- #### Import the Braze functions

```javascript
// Import the desired methods from wherever you saved the file
import { BrazeSessionInfo, logCustomEvent, logPurchase } from "./braze/braze.js";
```

#### Set up session information

```javascript
// Create session info for Braze
const brazeSessionInfo: BrazeSessionInfo = {
  userId: userId,
  sessionId: sessionId || "default-session"
};
```

#### Track user interactions

```javascript
// Log custom events for user interactions
await logCustomEvent(brazeSessionInfo, "chatgpt_app_interaction", {
  app_id: "your_chatgpt_app_id",
  tool_name: request.params.name,
  user_authenticated: userId !== "anonymous",
  timestamp: new Date().toISOString()
});
```

#### Track purchases and transactions

```javascript
// Calculate order details for purchases
const totalPrice = examplePriceMethod(args.size, args.quantity);
const orderId = `ORDER-${Date.now()}`;

// Define the purchase properties you'd like to use
const purchaseProperties = {
  orderId,
  customerName: args.customerName,
  size: args.size,
  quantity: args.quantity,
  deliveryAddress: args.deliveryAddress,
  specialInstructions: args.specialInstructions,
  estimatedTime,
  totalPrice
};

// Log the purchase to Braze
await logPurchase(
  brazeSessionInfo,
  "pizza",
  totalPrice,
  "USD",
  args.quantity,
  purchaseProperties
);
```

{% alert tip %}
Use the [SDK debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging/) to verify your integration and troubleshoot any issues.
{% endalert %} -->