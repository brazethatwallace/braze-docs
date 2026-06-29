---
nav_title: JavaScript SDK
article_title: Guía del repositorio del JavaScript SDK
page_order: 4
description: "Referencia del README del JavaScript SDK de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Acerca del JavaScript SDK de Braze {#about-the-braze-javascript-sdk}

El JavaScript SDK de Braze te ayuda a integrar las funcionalidades de mensajería, análisis e interacción con usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=javascript)

### Resumen de la arquitectura {#architecture-overview}

El JavaScript SDK de Braze es una biblioteca **independiente de la plataforma** diseñada para funcionar en cualquier entorno JavaScript puro. No contiene APIs específicas del navegador ni de Node.js, lo que la hace adecuada para su uso en diversos entornos de ejecución de JavaScript.

**Principios de diseño clave:**
- **Inyección de dependencias**: el SDK requiere implementaciones para almacenamiento, red e información del dispositivo en lugar de usar APIs específicas de la plataforma
- **Asíncrono primero**: la mayoría de los métodos de la API son asíncronos y devuelven Promises; algunos métodos de utilidad (por ejemplo, `destroy`, `subscribeToInAppMessage`, `toggleLogging`, `setLogger`) son síncronos. Consulta las definiciones de TypeScript para las firmas exactas.
- **Sesión singleton**: la API a nivel de módulo (`initialize`/`destroy`) gestiona una sesión activa del SDK a la vez.
- **Gestión interna de dependencias**: crea y gestiona dependencias internas (UserManager, SessionManager, DataFlushController, etc.) a partir de las implementaciones proporcionadas

<!--
Effective marketing automation is an essential part of successfully scaling and managing your business. Braze empowers you to build better customer relationships through a seamless, multi-channel approach that addresses all aspects of the user life cycle. Braze helps you engage your users on an ongoing basis. We'll have you up and running in no time!

- [Braze User Guide]({{site.baseurl}}/user_guide/introduction/)
- [Initial Web SDK Setup]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)
- [Braze Web SDK Documentation](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html) -->

## Inicio rápido {#quickstart}

Instala el SDK con npm:

``` bash
npm install @braze/javascript-sdk
```

O con yarn:

``` bash
yarn add @braze/javascript-sdk
```

Con la API a nivel de módulo:
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

## Requisitos previos {#prerequisites}

Antes de integrar el JavaScript SDK de Braze, necesitarás:

- **Cuenta de Braze**: una cuenta de Braze con acceso a la API
- **Clave de API**: la clave de API de tu aplicación desde el panel de Braze
- **Punto de conexión del SDK**: la URL de tu punto de conexión del SDK de Braze (por ejemplo, `sdk.iad-01.braze.com`)

### Obtener tus credenciales {#getting-your-credentials}

1. **Clave de API**: se encuentra en tu panel de Braze en **Configuración** > **Claves de API**
2. **Punto de conexión del SDK**: se encuentra en **Configuración** > **Autenticación SDK** > **Puntos finales**

## Integración {#integration}

### Llamar a la API {#calling-the-api}

Usa la API a nivel de módulo: llama a `initialize()` una vez y luego llama a las funciones exportadas. Para cambiar la configuración, llama primero a `destroy()` y luego a `initialize()` de nuevo.

``` typescript
import { initialize, logPurchase, changeUser } from '@braze/javascript-sdk';

await initialize({ apiKey, baseUrl, options, ... });
await changeUser('user-123');
await logPurchase('sku-1', 9.99, 'USD', 1);
```

### Conceptos principales {#core-concepts}

#### Implementaciones requeridas {#required-implementations}

El objeto de configuración de inicialización requiere `storageManager`. `networkManager` y `pushManager` son opcionales.

**1. StorageManager** - Interfaz de almacenamiento asíncrono clave-valor
``` typescript
interface StorageManager {
  store(key: string, value: string, isId?: boolean): Promise<void>;
  remove(key: string, isId?: boolean): Promise<void>;
  retrieve(key: string, isId?: boolean): Promise<string | null>;
  clearData(storageKeys: string[]): Promise<void>;
}
```
- El parámetro `isId` indica **almacenamiento persistente de ID**: cuando es `true`, el SDK está almacenando un identificador persistente (ID de dispositivo, ID de usuario) o la marca de exclusión. Las implementaciones deben persistir estos datos entre reinicios de la aplicación para que el SDK pueda reconocer el mismo dispositivo/usuario. Cuando es `false`, el valor son datos de sesión/caché (eventos, atributos, etc.) y pueden estar solo en memoria. Para entornos web, considera usar cookies para las claves almacenadas con `isId: true` para garantizar la persistencia entre sesiones.
- Debe manejar operaciones asíncronas para todas las operaciones de almacenamiento

**2. NetworkManager** (opcional) - Interfaz de solicitudes HTTP POST
``` typescript
interface NetworkManager {
  postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: globalThis.Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>>;
}
```
- La implementación predeterminada usa la API `fetch` (requiere `fetch` y `URL` globales)
- Se puede sobrescribir si `fetch` no es la API preferida
- Nota: el SDK ya tiene lógica de reintentos y límite de velocidad incorporada

**3. PushManager** (opcional) - Interfaz de notificaciones push
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
- Solo es necesario si implementas notificaciones push

#### Vaciado de datos {#data-flushing}

El SDK vacía automáticamente los datos en caché a los servidores de Braze cada 10 segundos (configurable mediante `flushIntervalInSeconds`). Usa `requestImmediateDataFlush()` para forzar la sincronización inmediata.

### Patrones de integración {#integration-patterns}

Para las firmas de los métodos, tipos de parámetros y retorno, y detalles completos de la API, consulta las definiciones de TypeScript en el paquete.

#### Integración básica {#basic-integration}

Ejemplo funcional completo con manejo de errores:

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

#### Implementación de almacenamiento personalizado {#custom-storage-implementation}

Implementación completa de StorageManager con IndexedDB para IDs persistentes:

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

#### Implementación de red personalizada {#custom-network-implementation}

NetworkManager que registra cada solicitud saliente (el SDK ya maneja errores y reintentos):

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

#### Manejo de errores {#error-handling}

Patrones completos de manejo de errores:

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

#### Gestión de suscripciones {#subscription-management}

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

**Cambiar la configuración:** solo existe una sesión activa a la vez. Para cambiar configuraciones, llama a `destroy()` y luego a `initialize()`:

``` typescript
import { destroy, initialize } from '@braze/javascript-sdk';

destroy();
await initialize({ /* new config */ });
```

### Casos de uso comunes {#common-use-cases}

#### Identificación de usuarios y seguimiento de atributos {#user-identification-and-attribute-tracking}

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

#### Registro de eventos y análisis {#event-logging-and-analytics}

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

#### Manejo de mensajes dentro de la aplicación {#in-app-message-handling}

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

### Manejo de errores y casos límite {#error-handling-edge-cases}

#### Condiciones de error comunes {#common-error-conditions}

**SDK no inicializado:**
- La mayoría de los métodos devuelven `undefined` (no lanzan una excepción) cuando el SDK no está inicializado
- `initialize()` devuelve `false` si ya está inicializado o la validación falla
- `changeUser()` no realiza ninguna acción y la promesa se resuelve si el SDK no está inicializado
- Siempre verifica los valores de retorno `undefined` antes de usarlos

**Fallos de validación:**
- Clave de API o URL base no válida: `initialize()` devuelve `false`, registra el error
- Nombres de eventos/claves no válidos: deben tener un máximo de 255 caracteres, no pueden comenzar con `$`, solo alfanuméricos + puntuación
- Valores de atributos no válidos: cadenas de máximo 255 caracteres, sin saltos de línea/tabulaciones/comillas dobles, no pueden comenzar con `$`
- Códigos de moneda no válidos: los códigos no compatibles generan una advertencia, no se realiza ninguna acción
- Cantidad de compra no válida: debe ser de 1 a 100, de lo contrario se ignora

**Errores de red:**
- `postRequest()` de NetworkManager debe manejar errores y rechazar promesas adecuadamente
- El controlador de vaciado de datos reintenta automáticamente las solicitudes fallidas
- Usa la devolución de llamada de `requestImmediateDataFlush()` para detectar fallos de vaciado

**Errores de almacenamiento:**
- Los métodos de StorageManager deben manejar errores de forma elegante
- Si el almacenamiento falla, el SDK puede no funcionar correctamente
- La marca `isId` determina la persistencia: los IDs persisten entre sesiones, los objetos tienen alcance de sesión

**Casos límite de identificación de usuarios:**
- No se puede revertir a un usuario anónimo después de la identificación
- El cambio de usuario finaliza la sesión actual e inicia una nueva sesión
- El historial del usuario anónimo se conserva al identificar por primera vez
- El historial se fusiona si el usuario existe en otro dispositivo

**Gestión de sesiones:**
- Las sesiones expiran después de 30 minutos de inactividad (configurable)
- `openSession()` devuelve `true` para una sesión nueva, `false` si se reanudó
- Debes llamar a `openSession()` después de `changeUser()` o `setIdentifierToken()`

**Gestión de suscripciones:**
- Las devoluciones de llamada de suscripción se ejecutan de forma síncrona cuando ocurren los eventos
- Elimina las suscripciones para evitar fugas de memoria
- `removeAllSubscriptions()` elimina todas las suscripciones a la vez

**Vaciado de datos:**
- Vaciado automático cada 10 segundos (configurable, mínimo: 3 segundos)
- El vaciado puede fallar silenciosamente; usa la devolución de llamada de `requestImmediateDataFlush()`
- Los datos se ponen en cola si la red no está disponible y se vacían cuando se restaura la red

### Notas importantes de implementación {#important-implementation-notes}

1. **La mayoría de los métodos son asíncronos**: los métodos asíncronos del SDK devuelven una Promise (usa `await` o `.then()`). Algunos métodos de configuración y utilidad (por ejemplo, `destroy`, `toggleLogging`, `setLogger`) son síncronos; consulta las definiciones de TypeScript o la tabla de referencia rápida para más detalles.

2. **Los métodos pueden devolver `undefined`**: si el SDK no está inicializado, la mayoría de los métodos devuelven `undefined` en lugar de lanzar una excepción. Verifica si el valor es `undefined` antes de usar los valores de retorno.

3. **Los métodos pueden devolver `null`**: algunos métodos devuelven `null` para indicar "no encontrado" (por ejemplo, `getUserId()` devuelve `null` si el usuario es anónimo). Esto es diferente de `undefined` (SDK no inicializado).

4. **Las claves de almacenamiento usan la marca `isId`**: el parámetro `isId` en los métodos de StorageManager distingue entre:
   - Almacenamiento de ID: identificadores persistentes (ID de dispositivo, ID de usuario) que deben persistir entre sesiones
   - Almacenamiento de objetos: datos con alcance de sesión que se pueden borrar

5. **Etiquetas de metadatos del SDK**: el array `sdkMetadata` identifica la plataforma/envoltorio que usa el SDK (por ejemplo, `['npm']` o `[BrazeSdkMetadata.NPM]`). Las etiquetas válidas están definidas por la enumeración `BrazeSdkMetadata` (como `npm`, `cdn`, `manu`, `shp`, `gg`, `kep`), y el SDK agrega automáticamente `'wjs'` para indicar JavaScript SDK.

6. **NetworkManager predeterminado**: si no se proporciona `networkManager`, el SDK usa una implementación predeterminada que requiere las APIs globales `fetch` y `URL`. Proporciona una implementación personalizada si estas no están disponibles.

7. **PushManager es opcional**: solo implementa `PushManager` si necesitas funcionalidad de notificaciones push. De lo contrario, se puede omitir.

8. **Destruir y limpiar**: llama a `destroy()` cuando necesites desmontar el SDK. Solo puede existir una sesión activa a la vez; debes llamar a `destroy()` antes de llamar a `initialize()` de nuevo. Hacerlo detiene los temporizadores, vacía los datos y libera los recursos.

9. **Vaciado de datos**: los datos se vacían automáticamente cada 10 segundos (configurable). Usa `requestImmediateDataFlush()` para la sincronización inmediata.

10. **Gestión de sesiones**: siempre llama a `openSession()` después de `changeUser()` o `setIdentifierToken()` para evitar crear usuarios anónimos duplicados.

11. **Seguridad de tipos**: el SDK está escrito en TypeScript con definiciones de tipos completas. Usa TypeScript para la mejor experiencia y verificación de tipos.

12. **Reglas de validación**: los nombres de eventos, claves de atributos y claves de propiedades tienen validación estricta (máximo 255 caracteres, no pueden comenzar con `$`, solo alfanuméricos + puntuación). Los valores no válidos pueden ser ignorados o causar errores.

## Depuración / solución de problemas {#debugging-troubleshooting}

Pasa la opción `enableLogging: true` a las opciones de inicialización. Esto es valioso para el desarrollo, pero asegúrate de eliminar esta opción o [proporcionar un registrador alternativo](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html#setlogger) antes de publicar tu página en producción.

## Contacto {#contact}

Si tienes preguntas, ponte en contacto con [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-javascript-sdk](https://github.com/braze-inc/braze-javascript-sdk).