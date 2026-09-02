# Integração do app ChatGPT {#chatgpt-app-integration}

## Configuração {#setup}

### Etapa 1: Obtenha o arquivo de integração da Braze {#step-1-get-the-braze-integration-file}

Copie o arquivo `braze.js` do nosso [repositório de integração de apps ChatGPT](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) para o seu projeto. Este arquivo contém toda a configuração necessária do SDK or kit de desenvolvimento de software da Braze e funções auxiliares.

### Etapa 2: Instale as dependências {#step-2-install-dependencies}

Instale nosso Web SDK or kit de desenvolvimento de software para o conjunto mais atualizado de recursos da Braze:

**Para integração do lado do cliente:**
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

Substitua `YOUR-SDK-ENDPOINT` pelo seu endpoint real do SDK or kit de desenvolvimento de software da Braze.

#### Configure o hook useBraze {#set-up-the-usebraze-hook}

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

#### Exiba Content Cards da Braze {#display-braze-content-cards}

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

#### Rastreie eventos do widget {#track-widget-events}

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

### Integração do lado do servidor (servidor MCP) {#server-side-integration-mcp-server}

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
Se você também precisar de uma integração do lado do servidor para funcionalidade de envio de mensagens no seu servidor MCP, entre em contato com <span style="white-space:nowrap;">`mcp-product@braze.com`</span>. Para rastreamento de eventos e compras do seu servidor MCP, use nossa [REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/home/).

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
Use the [SDK or kit de desenvolvimento de software debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging/) to verify your integration and troubleshoot any issues.
{% endalert %} -->