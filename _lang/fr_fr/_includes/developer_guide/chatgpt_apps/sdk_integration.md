# Intégration de l'application ChatGPT {#chatgpt-app-integration}

## Configuration {#setup}

### Étape 1 : Obtenir le fichier d'intégration Braze {#step-1-get-the-braze-integration-file}

Copiez le fichier `braze.js` depuis notre [dépôt d'intégration des applications ChatGPT](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) dans votre projet. Ce fichier contient toutes les configurations et fonctions d'aide nécessaires au SDK Braze.

### Étape 2 : Installer les dépendances {#step-2-install-dependencies}

Installez notre SDK Web pour bénéficier des fonctionnalités les plus récentes de Braze :

**Pour l'intégration côté client :**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Implementation

There are two ways to integrate Braze with your ChatGPT app depending on your use case:

### Client-side integration (custom widgets)

{% alert tip %}
**Recommended Approach:** This method enables rich messaging experiences and real-time user interaction tracking within your ChatGPT app widgets.
{% endalert %}

For displaying Braze messaging and tracking user interactions within your custom ChatGPT app widgets, use the Web SDK integration. A full messaging example can be found in our sample repository [here](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox).

#### Configure widget metadata

Add the following metadata to your MCP server file to allow Braze domains, ensuring to update the CDN domain based on [your region]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/):

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

Remplacez `YOUR-SDK-ENDPOINT` par votre endpoint SDK Braze réel.

#### Configurer le hook useBraze {#set-up-the-usebraze-hook}

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

#### Afficher les Content Cards Braze {#display-braze-content-cards}

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

#### Suivre les événements du widget {#track-widget-events}

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

### Intégration côté serveur (serveur MCP) {#server-side-integration-mcp-server}

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
Si vous avez également besoin d'une intégration côté serveur pour les fonctionnalités d'envoi de messages sur votre serveur MCP, contactez <span style="white-space:nowrap;">`mcp-product@braze.com`</span>. Pour suivre les événements et les achats depuis votre serveur MCP, utilisez notre [REST API]({{site.baseurl}}/api/home/).

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