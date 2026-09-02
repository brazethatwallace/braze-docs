## Sobre o SDK or kit de desenvolvimento de software Braze Vega {#about-the-braze-vega-sdk}

O SDK or kit de desenvolvimento de software Braze Vega permite coletar análise de dados e exibir mensagens no app ricas para seus usuários. A maioria dos métodos no SDK or kit de desenvolvimento de software Braze Vega é assíncrona e retorna promises que devem ser aguardadas ou resolvidas.

## Integrando o SDK or kit de desenvolvimento de software Braze Vega {#integrating-the-braze-vega-sdk}

### Etapa 1: Instale a biblioteca da Braze {#step-1-install-the-braze-library}

Instale o SDK or kit de desenvolvimento de software Braze Vega usando o gerenciador de pacotes de sua preferência.

{% tabs local %}
{% tab npm %}
Se o seu projeto usa NPM, você pode adicionar o SDK or kit de desenvolvimento de software Braze Vega como uma dependência.

```bash
npm install @braze/vega-sdk --save
```

Após a instalação, você pode importar os métodos necessários:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
Se o seu projeto usa Yarn, você pode adicionar o SDK or kit de desenvolvimento de software Braze Vega como uma dependência.

```bash
yarn add @braze/vega-sdk
```

Após a instalação, você pode importar os métodos necessários:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Etapa 2: Inicialize o SDK or kit de desenvolvimento de software {#step-2-initialize-the-sdk}

Depois que o SDK or kit de desenvolvimento de software Braze Vega for adicionado ao seu projeto, inicialize a biblioteca com a chave de API or interface de programação do aplicativo (API) e a [URL do endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) encontradas em **Configurações** > **Configurações do app** no dashboard da Braze.

{% alert important %}
Você deve aguardar ou resolver a promise de `changeUser` antes de chamar outros métodos da Braze, caso contrário os eventos e atributos podem ser definidos para o usuário incorreto.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");

      // Start a session
      await openSession();

      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };

    initBraze();
  }, []);

  return (
    // Your app components
  );
};
```

{% alert important %}
Usuários anônimos podem ser contabilizados no seu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users). Por isso, você pode querer carregar ou inicializar o SDK or kit de desenvolvimento de software de forma condicional para excluir esses usuários da sua contagem de MAU.
{% endalert %}

## Configurações opcionais {#optional-configurations}

### Registro de logs {#logging}

Você pode ativar o registro de logs do SDK or kit de desenvolvimento de software para ajudar na depuração e solução de problemas. Existem várias formas de ativar o registro de logs.

#### Ativar o registro de logs durante a inicialização {#enable-logging-during-initialization}

Passe `enableLogging: true` para `initialize()` para registrar mensagens de depuração no console:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Os logs básicos são visíveis para todos os usuários, então considere desativar o registro de logs antes de enviar seu código para produção.
{% endalert %}

#### Ativar o registro de logs após a inicialização {#enable-logging-after-initialization}

Use `toggleLogging()` para ativar ou desativar o registro de logs do SDK or kit de desenvolvimento de software após a inicialização:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Registro de logs personalizado {#custom-logging}

Use `setLogger()` para fornecer uma função de logger personalizada e ter mais controle sobre como os logs do SDK or kit de desenvolvimento de software são tratados:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Opções de configuração {#configuration-options}

Você pode passar opções de configuração adicionais para `initialize()` para personalizar o comportamento do SDK or kit de desenvolvimento de software:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 1800 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Fazendo upgrade do SDK or kit de desenvolvimento de software {#upgrading-the-sdk}

Quando você referencia o SDK or kit de desenvolvimento de software Braze Vega a partir do NPM ou Yarn, pode fazer upgrade para a versão mais recente atualizando a dependência do seu pacote:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Testando sua integração {#testing-your-integration}

Para verificar se a integração do SDK or kit de desenvolvimento de software está funcionando corretamente:

1. Inicialize o SDK or kit de desenvolvimento de software com `enableLogging: true` para ver mensagens de depuração no console
2. Certifique-se de usar `await changeUser()` antes de chamar outros métodos do SDK or kit de desenvolvimento de software
3. Chame `await openSession()` para iniciar uma sessão
4. Verifique o dashboard da Braze em **Visão geral** para confirmar que os dados da sessão estão sendo registrados
5. Teste o registro de um evento personalizado e verifique se ele aparece no seu dashboard