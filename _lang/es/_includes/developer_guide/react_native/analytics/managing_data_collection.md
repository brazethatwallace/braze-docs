{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Desactivación del seguimiento de datos {#disabling-data-tracking}

Para desactivar la recopilación de datos, utiliza el método `disableSDK`. Después de llamar a este método, el SDK or kit de desarrollo de software de Braze deja de enviar datos a los servidores de Braze.

```javascript
Braze.disableSDK();
```

## Reanudar el seguimiento de datos {#resuming-data-tracking}

Para reanudar la recopilación de datos después de desactivarla, utiliza el método `enableSDK`.

```javascript
Braze.enableSDK();
```

## Borrar datos {#wiping-data}

Para eliminar todos los datos del SDK or kit de desarrollo de software de Braze almacenados localmente en el dispositivo, utiliza el método `wipeData`. Después de llamar a este método, el SDK or kit de desarrollo de software se desactiva y debe volver a habilitarse con `enableSDK`.

```javascript
Braze.wipeData();
```

## Vaciado de datos {#flushing-data}

Para solicitar un vaciado inmediato de cualquier dato pendiente a los servidores de Braze, utiliza `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Configurar el seguimiento de anuncios habilitado {#setting-ad-tracking-enabled}

Para informar a Braze si el seguimiento de anuncios está habilitado para este dispositivo, utiliza el método `setAdTrackingEnabled`. El SDK or kit de desarrollo de software no recopila estos datos automáticamente.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

El segundo parámetro es el ID de publicidad de Google y solo se utiliza en Android.

## Actualización de la lista de permitidos de la propiedad de seguimiento (solo iOS) {#updating-the-tracking-property-allow-list-ios-only}

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

Para más información, consulta [Manifiesto de privacidad]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest).

## Cerrar sesión y cancelar el registro de push {#logout-and-unregister-push}

Esta característica aún no es compatible con el SDK or kit de desarrollo de software de React Native.