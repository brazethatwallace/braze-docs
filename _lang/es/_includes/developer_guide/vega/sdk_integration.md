## Acerca del SDK de Braze Vega {#about-the-braze-vega-sdk}

El SDK de Braze Vega te permite recopilar análisis y mostrar mensajes enriquecidos dentro de la aplicación a tus usuarios. La mayoría de los métodos en el SDK de Braze Vega son asíncronos y devuelven promesas que deben ser esperadas o resueltas.

## Integración del SDK Braze Vega {#integrating-the-braze-vega-sdk}

### Paso 1: Instala la biblioteca de Braze {#step-1-install-the-braze-library}

Instala el SDK Braze Vega usando tu gestor de paquetes preferido.

{% tabs local %}
{% tab npm %}
Si tu proyecto usa NPM, puedes añadir el SDK Braze Vega como dependencia.

```bash
npm install @braze/vega-sdk --save
```

Después de la instalación, puedes importar los métodos que necesites:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
Si tu proyecto usa Yarn, puedes añadir el SDK Braze Vega como dependencia.

```bash
yarn add @braze/vega-sdk
```

Después de la instalación, puedes importar los métodos que necesites:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Paso 2: Inicializa el SDK {#step-2-initialize-the-sdk}

Después de añadir el SDK Braze Vega a tu proyecto, inicializa la biblioteca con la clave de API y la [URL del endpoint de SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) que se encuentran en **Configuración** > **Configuración de la aplicación** dentro de tu panel de Braze.

{% alert important %}
Debes esperar o resolver la promesa de `changeUser` antes de llamar a otros métodos de Braze, o los eventos y atributos podrían asignarse al usuario incorrecto.
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
Los usuarios anónimos pueden contabilizarse en tus [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users). Como resultado, puede que quieras cargar o inicializar el SDK de forma condicional para excluir a estos usuarios de tu conteo de MAU.
{% endalert %}

## Configuraciones opcionales {#optional-configurations}

### Registro {#logging}

Puedes habilitar el registro del SDK para ayudar con la depuración y la solución de problemas. Hay varias formas de habilitar el registro.

#### Habilitar el registro durante la inicialización {#enable-logging-during-initialization}

Pasa `enableLogging: true` a `initialize()` para registrar mensajes de depuración en la consola:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Los registros básicos son visibles para todos los usuarios, así que considera desactivar el registro antes de liberar tu código a producción.
{% endalert %}

#### Habilitar el registro después de la inicialización {#enable-logging-after-initialization}

Usa `toggleLogging()` para habilitar o desactivar el registro del SDK después de la inicialización:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Registro personalizado {#custom-logging}

Usa `setLogger()` para proporcionar una función de registro personalizada y tener más control sobre cómo se gestionan los registros del SDK:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Opciones de configuración {#configuration-options}

Puedes pasar opciones de configuración adicionales a `initialize()` para personalizar el comportamiento del SDK:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 1800 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Actualización del SDK {#upgrading-the-sdk}

Cuando haces referencia al SDK Braze Vega desde NPM o Yarn, puedes actualizar a la última versión modificando la dependencia de tu paquete:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Prueba de tu integración {#testing-your-integration}

Para verificar que la integración de tu SDK funciona correctamente:

1. Inicializa el SDK con `enableLogging: true` para ver los mensajes de depuración en la consola
2. Asegúrate de hacer `await changeUser()` antes de llamar a otros métodos del SDK
3. Llama a `await openSession()` para iniciar una sesión
4. Comprueba tu panel de Braze en **Resumen** para verificar que los datos de sesión se están registrando
5. Prueba registrar un evento personalizado y verifica que aparece en tu panel