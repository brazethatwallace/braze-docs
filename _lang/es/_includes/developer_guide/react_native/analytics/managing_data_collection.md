{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Desactivar el seguimiento de datos {#disabling-data-tracking}

Para desactivar la recopilación de datos, utiliza el método `disableSDK`. Después de llamar a este método, el SDK de Braze deja de enviar datos a los servidores de Braze.

```javascript
Braze.disableSDK();
```

## Reanudar el seguimiento de datos {#resuming-data-tracking}

Para reanudar la recopilación de datos después de deshabilitarla, utiliza el método `enableSDK`.

```javascript
Braze.enableSDK();
```

## Borrar datos {#wiping-data}

Para eliminar todos los datos del SDK de Braze almacenados localmente en el dispositivo, utiliza el método `wipeData`. Después de llamar a este método, el SDK se deshabilita y debe volver a habilitarse con `enableSDK`.

```javascript
Braze.wipeData();
```

## Vaciado de datos {#flushing-data}

Para solicitar un vaciado inmediato de cualquier dato pendiente a los servidores de Braze, utiliza `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Configurar el seguimiento de anuncios habilitado {#setting-ad-tracking-enabled}

Para informar a Braze si el seguimiento de anuncios está habilitado para este dispositivo, utiliza el método `setAdTrackingEnabled`. El SDK no recopila estos datos automáticamente.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

El segundo parámetro es el ID de publicidad de Google y solo se utiliza en Android.

## Actualizar la lista de permitidos de la propiedad de seguimiento (solo iOS) {#updating-the-tracking-property-allow-list-ios-only}

Para actualizar la lista de tipos de datos declarados para seguimiento, utiliza `updateTrackingPropertyAllowList`. Esto no tiene efecto en Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

Para más información, consulta [Manifiesto de privacidad]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

## Cierre de sesión y cancelación del registro push {#logout-and-unregister-push}

Esta característica aún no es compatible con el SDK de React Native.