---
nav_title: Solución de problemas de vinculación en profundidad
article_title: Solución de problemas de vinculación en profundidad
description: "Problemas comunes de vinculación en profundidad en iOS y cómo diagnosticarlos, incluidos los vínculos de esquema personalizado, los vínculos universales, los vínculos de correo electrónico y proveedores externos como Branch."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Solución de problemas de vinculación en profundidad {#deep-linking-troubleshooting}

> Esta página cubre problemas comunes de vinculación en profundidad en iOS y cómo diagnosticarlos. Para obtener ayuda sobre cómo elegir el tipo de enlace adecuado, consulta la [guía de vinculación en profundidad de iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Para más detalles de implementación, consulta [Vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift).

## El vínculo profundo de esquema personalizado no abre la vista correcta {#custom-scheme-deep-link-doesnt-open-the-correct-view}

Si un vínculo profundo de esquema personalizado (por ejemplo, `myapp://products/123`) abre tu aplicación pero no navega a la pantalla deseada:

1. **Verifica que el esquema esté registrado.** En Xcode, comprueba que tu esquema aparece en la lista bajo `CFBundleURLTypes` en `Info.plist`.
2. **Comprueba tu controlador.** Establece un punto de interrupción en `application(_:open:options:)` para confirmar que se está llamando e inspecciona el parámetro `url`.
3. **Prueba el enlace de forma independiente.** Ejecuta el siguiente comando desde Terminal para probar el vínculo profundo fuera de Braze:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Si el enlace no funciona aquí, el problema está en el manejo de URL de tu aplicación, no en Braze.
4. **Comprueba el formato de la URL.** Verifica que la URL en tu campaña coincida con lo que espera tu controlador. Los errores comunes incluyen componentes de ruta faltantes o uso incorrecto de mayúsculas y minúsculas.

## El enlace universal se abre en Safari en lugar de en la aplicación {#universal-link-opens-in-safari-instead-of-the-app}

Si un enlace universal (por ejemplo, `https://myapp.com/products/123`) se abre en Safari en lugar de en tu aplicación:

### Verifica el derecho de dominios asociados {#verify-the-associated-domains-entitlement}

En Xcode, ve al objetivo de tu aplicación > **Signing & Capabilities** y comprueba que `applinks:yourdomain.com` aparece en la lista bajo **Associated Domains**.

### Valida el archivo AASA {#validate-the-aasa-file}

Tu archivo Apple App Site Association (AASA) debe estar alojado en una de estas ubicaciones:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Verifica lo siguiente:

- El archivo se sirve a través de HTTPS con un certificado válido.
- El `Content-Type` es `application/json`.
- El tamaño del archivo es inferior a 128 KB.
- El `appID` coincide con tu Team ID y Bundle ID (por ejemplo, `ABCDE12345.com.example.myapp`).
- La matriz `paths` o `components` incluye los patrones de URL que esperas.

Puedes validar tu AASA utilizando la [herramienta de validación de búsqueda de Apple](https://search.developer.apple.com/appsearch-validation-tool/) o ejecutando:

```bash
swcutil dl -d yourdomain.com
```

### Comprueba el `AppDelegate` {#check-the-appdelegate}

Verifica que `application(_:continue:restorationHandler:)` esté implementado en tu `AppDelegate` y gestione correctamente el `NSUserActivity`:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Verifica la configuración del SDK de Braze {#verify-braze-sdk-configuration}

Si utilizas enlaces universales desde notificaciones push, mensajes dentro de la aplicación o Content Cards entregados por Braze, confirma que `forwardUniversalLinks` está habilitado:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
El reenvío de enlaces universales requiere acceso a los derechos de la aplicación. Cuando se ejecuta en un simulador, estos derechos no están disponibles directamente. Para probar en un simulador, añade el archivo `.entitlements` a la fase de compilación **Copy Bundle Resources**.
{% endalert %}

### Comprueba el problema de la pulsación prolongada {#check-for-the-long-press-issue}

Si mantienes pulsado un enlace universal y seleccionas **Open**, iOS puede "romper" la asociación del enlace universal para ese dominio. Este es un comportamiento conocido de iOS. Para restablecerlo, mantén pulsado el enlace de nuevo y selecciona **Open in [App Name]**.

## El vínculo profundo del correo electrónico no abre la aplicación {#deep-link-from-email-doesnt-open-the-app}

Los enlaces de correo electrónico pasan por el sistema de seguimiento de clics de tu ESP, que envuelve los enlaces en un dominio de seguimiento (por ejemplo, `https://click.yourdomain.com/...`). Para que los enlaces universales funcionen desde el correo electrónico, debes configurar el archivo AASA en tu dominio de seguimiento de clics, no solo en tu dominio principal.

### Verifica el AASA del dominio de seguimiento de clics {#verify-click-tracking-domain-aasa}

1. Identifica tu dominio de seguimiento de clics en la configuración de tu ESP (SendGrid, SparkPost o Amazon SES).
2. Aloja el archivo AASA en `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Asegúrate de que el archivo AASA del dominio de seguimiento de clics incluya el mismo `appID` y patrones de ruta válidos.

Para obtener instrucciones de configuración específicas para cada ESP, consulta [Enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

### Comprueba la cadena de redireccionamiento {#check-the-redirect-chain}

Algunos ESP realizan un redireccionamiento desde la URL de seguimiento de clics a tu URL final. Los enlaces universales solo funcionan si iOS reconoce el dominio *inicial* (el dominio de seguimiento de clics) como asociado a tu aplicación. Si el redireccionamiento omite la comprobación AASA, el enlace se abre en Safari.

Para probar:

1. Envíate un correo electrónico de prueba.
2. Mantén pulsado el enlace e inspecciona la URL: esta es la URL de seguimiento de clics.
3. Verifica que este dominio tenga un archivo AASA válido.

## El vínculo profundo funciona desde push pero no desde mensajes dentro de la aplicación (o viceversa) {#deep-link-works-from-push-but-not-from-in-app-messages-or-vice-versa}

### Comprueba el BrazeDelegate {#check-the-brazedelegate}

Si implementas `BrazeDelegate.braze(_:shouldOpenURL:)`, verifica que gestiona los enlaces de forma coherente en todos los canales. El parámetro `context` incluye el canal de origen. Busca lógica condicional que pueda filtrar accidentalmente enlaces de canales específicos.

### Habilita el registro detallado {#enable-verbose-logging}

[Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) y reproduce el problema. Busca la entrada de registro `Opening`:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Compara la salida del registro del canal que funciona con la del canal que no funciona. Las diferencias en `useWebView` o `isUniversalLink` indican cómo el SDK interpreta el enlace de manera diferente.

### Comprueba si hay delegados de visualización personalizados {#check-for-custom-display-delegates}

Si utilizas un delegado de visualización de mensajes dentro de la aplicación personalizado o un controlador de clics de Content Cards, verifica que transmite correctamente los eventos de enlace al SDK de Braze para su gestión.

## "Abrir URL web dentro de la aplicación" muestra una página en blanco o dañada {#open-web-url-inside-app-shows-a-blank-or-broken-page}

Si al seleccionar **Open Web URL Inside App** aparece una WebView en blanco o dañada:

1. **Verifica que la URL utiliza HTTPS.** La WebView del SDK requiere URL compatibles con ATS. Los enlaces HTTP fallan silenciosamente.
2. **Comprueba los encabezados de Content Security Policy.** Si la página web de destino establece `X-Frame-Options: DENY` o una `Content-Security-Policy` restrictiva, bloquea la representación en una WebView.
3. **Comprueba si hay redireccionamientos a esquemas personalizados.** Si la página web redirige a un esquema personalizado (por ejemplo, `myapp://`), la WebView no puede gestionarlo.
4. **Prueba la URL en Safari.** Si la página no se carga en Safari en el dispositivo, tampoco se cargará en la WebView.

## Solución de problemas de Branch con Braze {#branch}

Si utilizas [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) como tu proveedor de enlaces:

### Verifica que el BrazeDelegate enrute a Branch {#verify-the-brazedelegate-routes-to-branch}

Tu `BrazeDelegate` debe interceptar los enlaces de Branch y pasarlos al SDK de Branch. Verifica lo siguiente:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Si `shouldOpenURL` devuelve `true` para enlaces de Branch, Braze los gestiona directamente en lugar de enrutarlos a Branch.

### Comprueba el dominio de enlace de Branch {#check-branch-link-domain}

Verifica que el dominio de Branch en tu `BrazeDelegate` coincida con tu dominio de enlace de Branch real. Branch utiliza varios formatos de dominio:

- `yourapp.app.link` (predeterminado)
- `yourapp-alternate.app.link` (alternativo)
- Dominios personalizados (si están configurados en el dashboard de Branch)

### Habilita el registro de ambos SDK {#enable-both-sdks-logging}

Para diagnosticar dónde se rompe el enlace en la cadena:

1. Habilita el [registro detallado de Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging): busca entradas `Opening '<URL>':` para verificar que el SDK recibió el enlace.
2. Habilita el [modo de prueba de Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking): comprueba el dashboard de Branch para ver los eventos de clics en los enlaces.
1. Habilita el [registro detallado de Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Busca entradas `Opening '<URL>':` para verificar que el SDK recibió el enlace.
2. Habilita el [modo de prueba de Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Comprueba el dashboard de Branch para ver los eventos de clics en los enlaces.
3. Si Braze registra el enlace, pero Branch no detecta un clic, es probable que el problema esté en la lógica de enrutamiento del `BrazeDelegate`.

### Comprueba la configuración del dashboard de Branch {#check-branch-dashboard-configuration}

En el dashboard de Branch, verifica:

- El **Bundle ID** y el **Team ID** de tu aplicación coinciden con tu proyecto Xcode.
- Tus **Associated Domains** incluyen el dominio de enlace de Branch.
- Tu archivo AASA de Branch es válido (Branch lo aloja automáticamente en dominios `app.link`).

### Prueba los enlaces de Branch de forma independiente {#test-branch-links-independently}

Prueba el enlace de Branch fuera de Braze para aislar el problema:

1. Abre el enlace de Branch en Safari en tu dispositivo. Si no se abre la aplicación, el problema está en tu configuración de Branch o AASA, no en Braze.
2. Pega el enlace de Branch en la aplicación Notas y pulsa sobre él. Los enlaces universales funcionan de forma más fiable desde Notas que desde la barra de direcciones de Safari.

## Consejos generales de depuración {#general-debugging-tips}

### Usa el registro detallado {#use-verbose-logging}

[Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) para ver exactamente cómo el SDK procesa los enlaces. Entradas clave que debes buscar:

| Entrada de registro | Qué significa |
|---|---|
| `Opening '<URL>': - channel: notification` | El SDK está procesando un enlace desde una notificación push |
| `Opening '<URL>': - channel: inAppMessage` | El SDK está procesando un enlace desde un mensaje dentro de la aplicación |
| `Opening '<URL>': - channel: contentCard` | El SDK está procesando un enlace desde una Content Card |
| `useWebView: true` | El SDK abre la URL en la WebView integrada en la aplicación |
| `isUniversalLink: true` | El SDK identificó la URL como un enlace universal |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Usa el registro detallado" }

Para más detalles sobre cómo leer estos registros, consulta [Lectura de registros detallados]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

### Prueba los enlaces de forma aislada {#test-links-in-isolation}

Antes de probar a través de Braze, verifica que tu vínculo profundo o enlace universal funciona por sí solo:

- **Esquema personalizado**: Ejecuta `xcrun simctl openurl booted "myapp://path"` en Terminal.
- **Enlace universal**: Pega la URL en la aplicación Notas en un dispositivo físico y pulsa sobre ella. No pruebes desde la barra de direcciones de Safari, ya que iOS trata las URL escritas de forma diferente a los enlaces pulsados.
- **Enlace de Branch**: Abre el enlace de Branch desde la aplicación Notas en un dispositivo.

### Prueba en un dispositivo físico {#test-on-a-physical-device}

Los enlaces universales tienen compatibilidad limitada en el simulador de iOS. Prueba siempre en un dispositivo físico para obtener resultados precisos. Si necesitas probar en un simulador, añade el archivo `.entitlements` a la fase de compilación **Copy Bundle Resources**.