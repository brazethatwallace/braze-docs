## Desactivación del seguimiento de datos {#disabling-data-tracking}

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab implementación estándar %}
Para desactivar la actividad de seguimiento de datos en el SDK Web, utiliza el método [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Esto sincronizará cualquier dato registrado antes de que se llamara a `disableSDK()`, y hará que todas las llamadas posteriores al SDK Web de Braze para esta página y las cargas de páginas futuras se ignoren.
{% endtab %}

{% tab Google Tag Administrador %}
Utiliza el tipo de etiqueta **Disable Tracking** o **Resume Tracking** para desactivar o reactivar el seguimiento web, respectivamente. Estas dos opciones llaman a [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) y [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Prácticas recomendadas {#best-practices}

Para ofrecer a los usuarios la opción de dejar de ser rastreados, te recomendamos crear una página sencilla con dos enlaces o botones: uno que llame a `disableSDK()` al hacer clic, y otro que llame a `enableSDK()` para permitir a los usuarios volver a aceptar el seguimiento. También puedes utilizar estos controles para iniciar o detener el seguimiento a través de otros subprocesadores de datos.

{% alert note %}
No es necesario inicializar el SDK de Braze para llamar a `disableSDK()`, lo que te permite desactivar el seguimiento para usuarios completamente anónimos. Por el contrario, `enableSDK()` no inicializa el SDK de Braze, por lo que también debes llamar a `initialize()` después para habilitar el seguimiento.
{% endalert %}

## Reanudación del seguimiento de datos {#resuming-data-tracking}

Para reanudar la recopilación de datos, puedes utilizar el método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

## Cerrar sesión y cancelar el registro de push {#logout-and-unregister-push}

El SDK de Braze proporciona métodos para dejar de segmentar un dispositivo cuando un usuario cancela su registro de notificaciones push o cierra sesión. Estos métodos eliminan los datos de registro push del usuario actual en el servidor de Braze y en el SDK, de modo que Braze ya no envía futuras Campaigns de notificaciones push a ese usuario.

### Cerrar sesión {#logout}

Cuando un usuario cierra sesión en una aplicación, llama al método `logout` del SDK para eliminar el registro push del dispositivo del usuario actual y realizar automáticamente acciones de limpieza en el SDK. El método `logout` realiza lo siguiente:

- Cancela el registro del token de notificaciones push del dispositivo del usuario actual en el servidor de Braze.
- Si la llamada de cancelación de registro tiene éxito, el SDK borra los datos del SDK almacenados localmente y desactiva el SDK.
- En caso de error, invoca el `errorCallback` para permitir que el integrador tome medidas.

El siguiente ejemplo muestra el manejo de `logout` basado en devoluciones de llamada. Úsalo cuando necesites manejo inmediato de éxito y errores, y reemplaza el registro con el flujo de tu aplicación.

```javascript
import { logout } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully logged out');
};

const errorCallback = () => {
  console.log('Failed to log out');
};

logout(successCallback, errorCallback);
```

#### Reactivar el seguimiento y push después de `logout` {#re-enable-tracking-and-push-after-logout}

Después de un `logout` exitoso, llama a [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk), y luego vuelve a registrarte para notificaciones con tu sistema operativo (SO) o proveedor de push siguiendo la [configuración de notificaciones push web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

#### Evitar llamadas de cancelación de registro inmediatas {#avoid-immediate-unregister-calls}

Evita llamar a `logout` o `unregisterPush` directamente después de registrarte para notificaciones push con el SO o el proveedor de push. Debido al procesamiento asíncrono del servidor, esto puede, en raras ocasiones, volver a añadir el token de notificaciones push al usuario de Braze.

### Cancelar el registro de push {#unregister-push}

Para dejar de enviar push a un dispositivo sin limpieza automatizada adicional, usa el método `unregisterPush`. Esto elimina el token de notificaciones push del dispositivo del usuario actual en el servidor de Braze y borra el token almacenado localmente.

El siguiente ejemplo muestra el manejo de `unregisterPush` basado en devoluciones de llamada. Úsalo cuando necesites manejo inmediato de éxito y errores, y reemplaza el registro con el flujo de tu aplicación.

```javascript
import { unregisterPush } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully unregistered from push');
};

const errorCallback = () => {
  console.log('Failed to unregister from push');
};

unregisterPush(successCallback, errorCallback);
```

#### Volver a registrar push después de `unregisterPush` {#re-register-push-after-unregisterpush}

Después de llamar a `unregisterPush`, vuelve a registrarte para notificaciones con tu SO o proveedor de push siguiendo la [configuración de notificaciones push web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) antes de enviar notificaciones push de Braze de nuevo.

{% alert note %}
En navegadores compatibles, cuando existe una suscripción push activa, `unregisterPush` también cancela el registro del prestador de servicios gestionado por Braze después de cancelar la suscripción de la API Push del navegador. Si estableces `manageServiceWorkerExternally` en `true`, el SDK no cancela el registro del prestador de servicios por ti.
{% endalert %}

#### Evitar llamadas de cancelación de registro inmediatas

Evita llamar a `logout` o `unregisterPush` directamente después de registrarte para notificaciones push con el SO o el proveedor de push. Debido al procesamiento asíncrono del servidor, esto puede, en raras ocasiones, volver a añadir el token de notificaciones push al usuario de Braze.