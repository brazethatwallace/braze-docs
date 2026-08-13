## Solución de problemas {#troubleshooting}

### Tocar una notificación push no abre la aplicación {#tapping-push-notification-doesnt-open-the-app}

En Android, si tocar una notificación push lleva automáticamente tu aplicación al primer plano y abre su vínculo profundo depende del indicador nativo `com_braze_handle_push_deep_links_automatically`, que por defecto es `false`.

Con el valor predeterminado de `false`:

- El SDK nativo sigue enviando una difusión `BRAZE_PUSH_CLICKED` y tu listener Dart `push_opened` sigue activándose como se espera.
- El SDK nativo no llama a `startActivity()`, por lo que tu aplicación no se lleva al primer plano y el vínculo profundo no se sigue automáticamente.

Si estos dos comportamientos coinciden con lo que estás viendo, es probable que la configuración del indicador sea la causa.
Para confirmarlo, revisa los registros de tu dispositivo en busca de una entrada `BrazePushReceiver` que gestione `com.braze.action.BRAZE_PUSH_CLICKED`, seguida de un evento `push_opened` en tus registros de Flutter, sin un lanzamiento de aplicación correspondiente.

Para solucionarlo, establece `com_braze_handle_push_deep_links_automatically` en `true` en tu `braze.xml`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Para más información, consulta [Añadir vínculos profundos (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android) en la guía de notificaciones push de Flutter.

### Otros problemas de entrega push y registro {#other-push-delivery-and-registration-issues}

Dado que el SDK de Braze para Flutter en Android está construido sobre el SDK nativo de Braze para Android, la mayoría de los demás problemas de entrega push, registro y logging (como discrepancias en el ID del remitente, ausencia de Google Play Services o que `BrazeFirebaseMessagingService` no esté registrado) también se aplican a las aplicaciones Flutter. Para más información, consulta la [guía de solución de problemas nativa de Android]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android).