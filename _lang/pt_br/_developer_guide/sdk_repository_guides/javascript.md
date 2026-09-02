---
nav_title: JavaScript SDK or kit de desenvolvimento de software
article_title: Guia do repositório do JavaScript SDK or kit de desenvolvimento de software
page_order: 4
description: "Referência do README do Braze JavaScript SDK or kit de desenvolvimento de software espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do JavaScript SDK or kit de desenvolvimento de software {#javascript-sdk-repository-guide}

## Sobre o Braze JavaScript SDK or kit de desenvolvimento de software {#about-the-braze-javascript-sdk}

O Braze JavaScript SDK or kit de desenvolvimento de software ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=javascript)

### Visão geral da arquitetura {#architecture-overview}

O Braze JavaScript SDK or kit de desenvolvimento de software é uma biblioteca **independente de plataforma** projetada para funcionar em qualquer ambiente JavaScript puro. Ele não contém APIs específicas de navegador ou Node.js, o que o torna adequado para uso em diversos runtimes JavaScript.

**Princípios de design principais:**
- **Injeção de dependência**: O SDK or kit de desenvolvimento de software requer implementações para armazenamento, rede e informações do dispositivo em vez de usar APIs específicas de plataforma
- **Async-First**: A maioria dos métodos da API or interface de programação do aplicativo (API) é assíncrona e retorna Promises; alguns métodos utilitários (por exemplo, `destroy`, `subscribeToInAppMessage`, `toggleLogging`, `setLogger`) são síncronos. Consulte as definições TypeScript para assinaturas exatas.
- **Sessão singleton**: A API or interface de programação do aplicativo (API) em nível de módulo (`initialize`/`destroy`) gerencia uma sessão ativa do SDK or kit de desenvolvimento de software por vez.
- **Gerenciamento interno de dependências**: Cria e gerencia dependências internas (UserManager, SessionManager, DataFlushController, etc.) a partir das implementações fornecidas

<!--
Effective marketing automation is an essential part of successfully scaling and managing your business. Braze empowers you to build better customer relationships through a seamless, multi-channel approach that addresses all aspects of the user life cycle. Braze helps you engage your users on an ongoing basis. We'll have you up and running in no time!

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction)
- [Initial Web SDK or kit de desenvolvimento de software Setup](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)
- [Braze Web SDK or kit de desenvolvimento de software Documentation](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html) -->

## Início rápido {#quickstart}

Instale o SDK or kit de desenvolvimento de software com npm:

``` bash
npm install @braze/javascript-sdk
```

Ou com yarn:

``` bash
yarn add @braze/javascript-sdk
```

Com a API or interface de programação do aplicativo (API) em nível de módulo:
``` typescript
import { initialize, openSession, changeUser } from '@braze/javascript-sdk';

await initialize({
  apiKey,
  baseUrl,
  options,
  sdkMetadata,
  deviceInfo,
  storageManager,
  networkManager,
});

await changeUser(userId);

await openSession();
```

## Pré-requisitos {#prerequisites}

Antes de integrar o Braze JavaScript SDK or kit de desenvolvimento de software, você precisará de:

- **Conta Braze**: Uma conta Braze com acesso à API or interface de programação do aplicativo (API)
- **Chave de API or interface de programação do aplicativo (API)**: A chave de API or interface de programação do aplicativo (API) do seu app no dashboard da Braze
- **Endpoint do SDK or kit de desenvolvimento de software**: A URL do endpoint do SDK or kit de desenvolvimento de software da Braze (por exemplo, `sdk.iad-01.braze.com`)

### Obtendo suas credenciais {#getting-your-credentials}

1. **Chave de API or interface de programação do aplicativo (API)**: Encontrada no dashboard da Braze em **Configurações** → **Chaves de API or interface de programação do aplicativo (API)**
2. **Endpoint do SDK or kit de desenvolvimento de software**: Localizado em **Configurações** → **Autenticação do SDK or kit de desenvolvimento de software** → **Endpoints**

## Integração {#integration}

### Chamando a API or interface de programação do aplicativo (API) {#calling-the-api}

Use a API or interface de programação do aplicativo (API) em nível de módulo: chame `initialize()` uma vez e depois chame as funções exportadas. Para trocar a configuração, chame `destroy()` primeiro e depois `initialize()` novamente.

``` typescript
import { initialize, logPurchase, changeUser } from '@braze/javascript-sdk';

await initialize({ apiKey, baseUrl, options, ... });
await changeUser('user-123');
await logPurchase('sku-1', 9.99, 'USD', 1);
```

### Conceitos principais {#core-concepts}

#### Implementações obrigatórias {#required-implementations}

O objeto de configuração do initialize requer `storageManager`. `networkManager` e `pushManager` são opcionais.

**1. StorageManager** — Interface de armazenamento assíncrono chave-valor
``` typescript
interface StorageManager {
  store(key: string, value: string, isId?: boolean): Promise<void>;
  remove(key: string, isId?: boolean): Promise<void>;
  retrieve(key: string, isId?: boolean): Promise<string | null>;
  clearData(storageKeys: string[]): Promise<void>;
}
```
- O parâmetro `isId` indica **armazenamento persistente de ID**: quando `true`, o SDK or kit de desenvolvimento de software está armazenando um identificador persistente (ID do dispositivo, ID do usuário) ou a flag de descadastramento. As implementações devem persistir esses dados entre reinicializações do app para que o SDK or kit de desenvolvimento de software possa reconhecer o mesmo dispositivo/usuário. Quando `false`, o valor é dado de sessão/cache (eventos, atributos, etc.) e pode ficar apenas em memória. Para ambientes web, considere usar cookies para chaves armazenadas com `isId: true` para garantir persistência entre sessões.
- Deve lidar com operações assíncronas para todas as operações de armazenamento

**2. NetworkManager** (opcional) — Interface de requisição HTTP POST
``` typescript
interface NetworkManager {
  postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: globalThis.Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>>;
}
```
- A implementação padrão usa a API or interface de programação do aplicativo (API) `fetch` (requer `fetch` e `URL` globais)
- Pode ser substituída se `fetch` não for a API or interface de programação do aplicativo (API) preferida
- Nota: O SDK or kit de desenvolvimento de software já possui lógica de retry e limite de frequência integrada

**3. PushManager** (opcional) — Interface de notificação por push
``` typescript
interface PushManager {
  isPushBlocked(): boolean | undefined;
  isPushPermissionGranted(): boolean | undefined;
  isPushSupported(): boolean | undefined;
  registerPush(
    successCallback?: (endpoint: string, publicKey: string, userAuth: string) => void,
    deniedCallback?: (temporaryDenial: boolean) => void,
  ): void;
  unregisterPush(successCallback?: () => void, errorCallback?: () => void): void;
}
```
- Necessário apenas se você estiver implementando notificações por push

#### Envio de dados (Data Flushing) {#data-flushing}

O SDK or kit de desenvolvimento de software envia automaticamente os dados em cache para os servidores da Braze a cada 10 segundos (configurável via `flushIntervalInSeconds`). Use `requestImmediateDataFlush()` para forçar a sincronização imediata.

### Padrões de integração {#integration-patterns}

Para assinaturas de métodos, tipos de parâmetros e retorno, e detalhes completos da API or interface de programação do aplicativo (API), consulte as definições TypeScript no pacote.

#### Integração básica {#basic-integration}

Exemplo funcional completo com tratamento de erros:

``` typescript
import {
  initialize,
  openSession,
  changeUser,
  logCustomEvent,
  type StorageManager,
  type DeviceInfo
} from '@braze/javascript-sdk';

// Implement required StorageManager interface (in-memory only; does not persist data).
// This example treats all keys equally and ignores the isId parameter
// See "Complete StorageManager implementation with IndexedDB" below for an
// example where we properly handle isId
class InMemoryStorageManager implements StorageManager {
  private storage = new Map<string, string>();

  async store(key: string, value: string, isId?: boolean): Promise<void> {
    this.storage.set(key, value);
  }

  async retrieve(key: string, isId?: boolean): Promise<string | null> {
    return this.storage.get(key) ?? null;
  }

  async remove(key: string, isId?: boolean): Promise<void> {
    this.storage.delete(key);
  }

  async clearData(storageKeys: string[]): Promise<void> {
    for (const key of storageKeys) {
      this.storage.delete(key);
    }
  }
}

const storageManager: StorageManager = new InMemoryStorageManager();

// Provide device information (use your platform's APIs for non-browser)
const deviceInfo: DeviceInfo = {
  os: 'my-runtime-os',
  language: 'en',
  timezone: 'UTC',
  browser: 'Chrome', // Optional
  browserVersion: '120', // Optional
  userAgent: "some-user-agent" // Optional
};

// Browser-only example (uncomment and adapt if you are running in a web browser)
// const deviceInfo: DeviceInfo = {
//   os: navigator.platform || 'Unknown',
//   language: navigator.language || 'en',
//   timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
//   browser: 'Chrome', // Optional
//   browserVersion: '120', // Optional
//   userAgent: navigator.userAgent // Optional
// };

// Initialize SDK
try {
  const initialized = await initialize({
    apiKey: 'YOUR-API-KEY-HERE',
    baseUrl: 'sdk.iad-01.braze.com', // Your Braze SDK endpoint
    options: {
      sdkVersion: '1.0.0',
      enableLogging: true, // Remove in production
      sessionTimeoutInSeconds: 1800, // 30 minutes
      flushIntervalInSeconds: 10
    },
    sdkMetadata: ['npm'], // Identify your platform
    deviceInfo,
    storageManager
  });

  if (!initialized) {
    console.error('Failed to initialize Braze SDK');
    return;
  }

  // Identify user (wait for promise to resolve)
  await changeUser('user-123');

  // Open session (must be after changeUser)
  const isNewSession = await openSession();
  console.log('Session opened:', isNewSession ? 'new' : 'resumed');

  // Log events
  await logCustomEvent('app_opened', {
    source: 'homepage',
    timestamp: new Date().toISOString()
  });

} catch (error) {
  console.error('Braze SDK error:', error);
}
```

#### Implementação de armazenamento personalizado {#custom-storage-implementation}

Implementação completa do StorageManager com IndexedDB para IDs persistentes:

``` typescript
import type { StorageManager } from '@braze/javascript-sdk';

class IndexedDBStorageManager implements StorageManager {
  private dbName = 'braze-storage';
  private storeName = 'braze-ids';
  private memoryCache = new Map<string, string>();
  private db: IDBDatabase | null = null;
  private dbInitPromise: Promise<void> | null = null;

  private async initDB(): Promise<void> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, 1);
      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve();
      };
      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;
        if (!db.objectStoreNames.contains(this.storeName)) {
          db.createObjectStore(this.storeName);
        }
      };
    });
  }

  private async ensureDB(): Promise<void> {
    if (this.dbInitPromise !== null) {
      return this.dbInitPromise;
    }
    this.dbInitPromise = this.initDB();
    return this.dbInitPromise;
  }

  async store(key: string, value: string, isId?: boolean): Promise<void> {
    await this.ensureDB();
    this.memoryCache.set(key, value);

    if (isId && this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readwrite');
        const store = transaction.objectStore(this.storeName);
        await new Promise<void>((resolve, reject) => {
          const request = store.put(value, key);
          request.onsuccess = () => resolve();
          request.onerror = () => reject(request.error);
        });
      } catch (error) {
        console.error('Failed to store ID in IndexedDB:', error);
      }
    }
  }

  async retrieve(key: string, isId?: boolean): Promise<string | null> {
    await this.ensureDB();
    if (this.memoryCache.has(key)) {
      return this.memoryCache.get(key) || null;
    }

    if (isId && this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readonly');
        const store = transaction.objectStore(this.storeName);
        return new Promise<string | null>((resolve, reject) => {
          const request = store.get(key);
          request.onsuccess = () => {
            const value = request.result;
            if (value) {
              this.memoryCache.set(key, value);
            }
            resolve(value || null);
          };
          request.onerror = () => reject(request.error);
        });
      } catch (error) {
        console.error('Failed to retrieve ID from IndexedDB:', error);
        return null;
      }
    }

    return null;
  }

  async remove(key: string, isId?: boolean): Promise<void> {
    await this.ensureDB();
    this.memoryCache.delete(key);

    if (isId && this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readwrite');
        const store = transaction.objectStore(this.storeName);
        await new Promise<void>((resolve, reject) => {
          const request = store.delete(key);
          request.onsuccess = () => resolve();
          request.onerror = () => reject(request.error);
        });
      } catch (error) {
        console.error('Failed to remove ID from IndexedDB:', error);
      }
    }
  }

  async clearData(storageKeys: string[]): Promise<void> {
    await this.ensureDB();
    for (const key of storageKeys) {
      this.memoryCache.delete(key);
    }

    if (this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readwrite');
        const store = transaction.objectStore(this.storeName);
        await Promise.all(
          storageKeys.map(
            (key) =>
              new Promise<void>((resolve, reject) => {
                const request = store.delete(key);
                request.onsuccess = () => resolve();
                request.onerror = () => reject(request.error);
              })
          )
        );
      } catch (error) {
        console.error('Failed to clear data from IndexedDB:', error);
      }
    }
  }
}

const storageManager = new IndexedDBStorageManager();
```

#### Implementação de rede personalizada {#custom-network-implementation}

NetworkManager que registra cada requisição de saída (o SDK or kit de desenvolvimento de software já lida com erros e retries):

``` typescript
import type { NetworkManager } from '@braze/javascript-sdk';

function logRequest(url: string, data: Partial<Record<string, unknown>>): void {
  // Send to your analytics, monitoring, or logging backend
  console.log('Braze SDK request', { url, data });
}

class LoggingNetworkManager implements NetworkManager {
  async postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>> {
    logRequest(url, data);

    const requestHeaders = new Headers(headers);
    requestHeaders.set('Content-Type', 'application/json');

    const response = await fetch(url, {
      method: 'POST',
      headers: requestHeaders,
      body: JSON.stringify(data),
    });

    const result = await response.json();
    return result as Partial<Record<string, unknown>>;
  }
}

const networkManager = new LoggingNetworkManager();
```

#### Tratamento de erros {#error-handling}

Padrões completos de tratamento de erros:

``` typescript
import {
  getUserId,
  logCustomEvent,
  initialize,
} from '@braze/javascript-sdk';

// Pattern 1: Check for undefined (SDK not initialized)
async function getDevice() {
  const deviceId = await getDeviceId();
  if (deviceId === undefined) {
    console.warn('SDK not initialized');
    return null;
  }
  return deviceId;
}

// Pattern 2: Try-catch for methods that may throw
async function logEventSafely() {
  try {
    const success = await logCustomEvent('button_clicked', { button: 'submit' });
    if (success === undefined) {
      console.warn('SDK not initialized, event not logged');
    } else if (success) {
      console.log('Event logged successfully');
    } else {
      console.warn('Event failed to enqueue');
    }
  } catch (error) {
    console.error('Error logging event:', error);
    // Handle error (e.g., retry, queue for later)
  }
}

// Pattern 3: Handle null vs undefined distinction
async function checkUser() {
  const userId = await getUserId();

  if (userId === undefined) {
    // SDK not initialized
    console.warn('SDK not initialized');
  } else if (userId === null) {
    // Current user is anonymous
    console.log('Current user is anonymous');
  } else {
    // User is identified
    console.log(`User ID is ${userId}`);
  }
}

// Pattern 4: Handle initialization errors
async function initializeSafely() {
  try {
    const initialized = await initialize({
      apiKey: 'YOUR-API-KEY',
      baseUrl: 'sdk.iad-01.braze.com',
      options: { sdkVersion: '1.0.0' },
      sdkMetadata: ['npm'],
      deviceInfo: { os: 'iOS', language: 'en', timezone: 'UTC' },
      storageManager: myStorageManager
    });

    if (!initialized) {
      console.error('Failed to initialize SDK');
      // Check if already initialized, disabled, or validation failed
      return false;
    }

    return true;
  } catch (error) {
    console.error('Initialization error:', error);
    return false;
  }
}
```

#### Gerenciamento de inscrições {#subscription-management}

``` typescript
import {
  ControlMessage,
  logInAppMessageImpression,
  removeSubscription,
  subscribeToInAppMessage,
} from '@braze/javascript-sdk';

const displayMessage = (inAppMessage) => {
  // Add custom code to display in-app messages
}

// Subscribe to in-app messages
const subscriptionId = subscribeToInAppMessage((inAppMessage) => {
  if (inAppMessage instanceof ControlMessage) {
    return; // Skip control messages
  }

  displayMessage(inAppMessage);

  logInAppMessageImpression(inAppMessage);
});

// Later, remove subscription if it was successfully created
if (subscriptionId) {
  removeSubscription(subscriptionId);
}
```

**Trocando a configuração:** Apenas uma sessão ativa existe por vez. Para trocar configurações, chame `destroy()` e depois `initialize()`:

``` typescript
import { destroy, initialize } from '@braze/javascript-sdk';

destroy();
await initialize({ /* new config */ });
```

### Casos de uso comuns {#common-use-cases}

#### Identificação de usuário e rastreamento de atributos {#user-identification-and-attribute-tracking}

``` typescript
import {
  changeUser,
  setCustomUserAttribute,
  setUserEmail,
  setUserFirstName,
  setUserLastName,
} from '@braze/javascript-sdk';

// Identify user
await changeUser('user-123');

// Set standard attributes
await setUserEmail('user@example.com');
await setUserFirstName('John');
await setUserLastName('Doe');

// Set custom attributes
await setCustomUserAttribute('subscription_tier', 'premium');
await setCustomUserAttribute('last_login', new Date());
await setCustomUserAttribute('tags', ['vip', 'early-adopter']);
```

#### Registro de eventos e análise de dados {#event-logging-and-analytics}

``` typescript
import {
  logCustomEvent,
  logPurchase,
  requestImmediateDataFlush,
} from '@braze/javascript-sdk';

await logCustomEvent('product_viewed', {
  product_id: '123',
  category: 'electronics',
  price: 99.99
});

await logPurchase('product-123', 99.99, 'USD', 1, {
  category: 'electronics'
});

// Flushing these events to the server will happen periodically,
// however you can manually trigger a flush if necessary
requestImmediateDataFlush((success) => {
  console.log('Data flushed:', success);
});
```

#### Tratamento de mensagens no app {#in-app-message-handling}

``` typescript
import {
  ControlMessage,
  logInAppMessageImpression,
  subscribeToInAppMessage,
} from '@braze/javascript-sdk';

const displayInAppMessage = async (inAppMessage) => {
  // Add custom code to display in-app messages
}

subscribeToInAppMessage(async (inAppMessage) => {
  if (inAppMessage instanceof ControlMessage) {
    return;
  }

  await displayInAppMessage(inAppMessage);

  await logInAppMessageImpression(inAppMessage);
});
```

### Tratamento de erros e casos extremos {#error-handling-edge-cases}

#### Condições de erro comuns {#common-error-conditions}

**SDK or kit de desenvolvimento de software não inicializado:**
- A maioria dos métodos retorna `undefined` (não lança exceção) quando o SDK or kit de desenvolvimento de software não está inicializado
- `initialize()` retorna `false` se já estiver inicializado ou se a validação falhar
- `changeUser()` é um no-op e a promise é resolvida se o SDK or kit de desenvolvimento de software não estiver inicializado
- Sempre verifique se os valores de retorno são `undefined` antes de usá-los

**Falhas de validação:**
- Chave de API or interface de programação do aplicativo (API) ou URL base inválida: `initialize()` retorna `false`, registra erro
- Nomes de eventos/chaves inválidos: Devem ter no máximo 255 caracteres, não podem começar com `$`, apenas alfanuméricos + pontuação
- Valores de atributos inválidos: Strings com no máximo 255 caracteres, sem quebras de linha/tabulações/aspas duplas, não podem começar com `$`
- Códigos de moeda inválidos: Códigos não suportados resultam em aviso, nenhuma ação é tomada
- Quantidade de compra inválida: Deve ser de 1 a 100, caso contrário é ignorada

**Erros de rede:**
- O `postRequest()` do NetworkManager deve tratar erros e rejeitar promises adequadamente
- O controlador de envio de dados faz retry automaticamente em requisições com falha
- Use o retorno de chamada de `requestImmediateDataFlush()` para detectar falhas de envio

**Erros de armazenamento:**
- Os métodos do StorageManager devem tratar erros de forma adequada
- Se o armazenamento falhar, o SDK or kit de desenvolvimento de software pode não funcionar corretamente
- A flag `isId` determina a persistência: IDs persistem entre sessões, objetos têm escopo de sessão

**Casos extremos de identificação de usuário:**
- Não é possível reverter para usuário anônimo após a identificação
- A troca de usuário encerra a sessão atual e inicia uma nova sessão
- O histórico do usuário anônimo é preservado ao identificar pela primeira vez
- O histórico é mesclado se o usuário existir em outro dispositivo

**Gerenciamento de sessão:**
- As sessões expiram após 30 minutos de inatividade (configurável)
- `openSession()` retorna `true` para nova sessão, `false` se retomada
- Deve chamar `openSession()` após `changeUser()` ou `setIdentifierToken()`

**Gerenciamento de inscrições:**
- Os retornos de chamada de inscrição são chamados de forma síncrona quando os eventos ocorrem
- Remova inscrições para evitar vazamentos de memória
- `removeAllSubscriptions()` limpa todas as inscrições de uma vez

**Envio de dados:**
- Envio automático a cada 10 segundos (configurável, mínimo: 3 segundos)
- O envio pode falhar silenciosamente — use o retorno de chamada de `requestImmediateDataFlush()`
- Os dados são enfileirados se a rede estiver indisponível e enviados quando a rede for restaurada

### Notas importantes de implementação {#important-implementation-notes}

1. **A maioria dos métodos é assíncrona**: Métodos assíncronos do SDK or kit de desenvolvimento de software retornam uma Promise (use `await` ou `.then()`). Alguns métodos de configuração e utilitários (por exemplo, `destroy`, `toggleLogging`, `setLogger`) são síncronos; consulte as definições TypeScript ou a tabela de referência rápida para detalhes.

2. **Métodos podem retornar `undefined`**: Se o SDK or kit de desenvolvimento de software não estiver inicializado, a maioria dos métodos retorna `undefined` em vez de lançar exceção. Verifique se o valor é `undefined` antes de usar os valores de retorno.

3. **Métodos podem retornar `null`**: Alguns métodos retornam `null` para indicar "não encontrado" (por exemplo, `getUserId()` retorna `null` se o usuário for anônimo). Isso é diferente de `undefined` (SDK or kit de desenvolvimento de software não inicializado).

4. **Chaves de armazenamento usam a flag `isId`**: O parâmetro `isId` nos métodos do StorageManager distingue entre:
   - Armazenamento de ID: Identificadores persistentes (ID do dispositivo, ID do usuário) que devem persistir entre sessões
   - Armazenamento de objetos: Dados com escopo de sessão que podem ser limpos

5. **Tags de metadados do SDK or kit de desenvolvimento de software**: O array `sdkMetadata` identifica a plataforma/wrapper que está usando o SDK or kit de desenvolvimento de software (por exemplo, `['npm']` ou `[BrazeSdkMetadata.NPM]`). Tags válidas são definidas pelo enum `BrazeSdkMetadata` (como `npm`, `cdn`, `manu`, `shp`, `gg`, `kep`), e o SDK or kit de desenvolvimento de software adiciona automaticamente `'wjs'` para indicar JavaScript SDK or kit de desenvolvimento de software.

6. **NetworkManager padrão**: Se `networkManager` não for fornecido, o SDK or kit de desenvolvimento de software usa uma implementação padrão que requer as APIs globais `fetch` e `URL`. Forneça uma implementação personalizada se essas APIs não estiverem disponíveis.

7. **PushManager é opcional**: Implemente o `PushManager` apenas se você precisar de funcionalidade de notificação por push. Caso contrário, pode ser omitido.

8. **Destroy e limpeza**: Chame `destroy()` quando precisar encerrar o SDK or kit de desenvolvimento de software. Apenas uma sessão ativa pode existir por vez; você deve chamar `destroy()` antes de chamar `initialize()` novamente. Isso interrompe timers, envia dados pendentes e libera recursos.

9. **Envio de dados**: Os dados são enviados automaticamente a cada 10 segundos (configurável). Use `requestImmediateDataFlush()` para sincronização imediata.

10. **Gerenciamento de sessão**: Sempre chame `openSession()` após `changeUser()` ou `setIdentifierToken()` para evitar a criação de usuários anônimos duplicados.

11. **Segurança de tipos**: O SDK or kit de desenvolvimento de software é escrito em TypeScript com definições de tipos completas. Use TypeScript para a melhor experiência e verificação de tipos.

12. **Regras de validação**: Nomes de eventos, chaves de atributos e chaves de propriedades têm validação rigorosa (máximo de 255 caracteres, não podem começar com `$`, apenas alfanuméricos + pontuação). Valores inválidos podem ser ignorados ou causar erros.

## Depuração / Solução de problemas {#debugging-troubleshooting}

Passe a opção `enableLogging: true` nas opções de inicialização. Isso é útil para desenvolvimento, mas certifique-se de remover essa opção ou [fornecer um logger alternativo](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html#setlogger) antes de publicar sua página em produção.

## Fale com a gente {#contact}

Se você tiver dúvidas, entre em contato com [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-javascript-sdk](https://github.com/braze-inc/braze-javascript-sdk).