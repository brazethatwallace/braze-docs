---
nav_title: Solución de problemas de vinculación en profundidad
article_title: Solución de problemas de vinculación en profundidad
description: "Diagnostica problemas de vinculación en profundidad en iOS mediante un índice de síntomas, una ruta de investigación estándar y comprobaciones específicas de la plataforma."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Solución de problemas de vinculación en profundidad {#troubleshoot-deep-linking}

> Usa esta página para diagnosticar problemas comunes de vinculación en profundidad en iOS. Para obtener ayuda sobre cómo elegir el tipo de enlace adecuado, consulta la [guía de vinculación en profundidad de iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Para más detalles de implementación, consulta [Vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift).

## Empieza aquí: Identifica tu síntoma {#start-here-match-your-symptom}

Busca el comportamiento que estás observando en la tabla y luego sigue los pasos de esa sección. Si no estás seguro de qué sección aplica, utiliza la [ruta de investigación estándar](#standard-investigation-path).

| Síntoma | Ir a |
| --- | --- |
| El enlace de esquema personalizado abre la aplicación pero muestra la pantalla incorrecta | [El vínculo profundo de esquema personalizado no abre la vista correcta](#custom-scheme-deep-link-does-not-open-the-correct-view) |
| El enlace universal abre Safari en lugar de la aplicación | [El enlace universal se abre en Safari en lugar de la aplicación](#universal-link-opens-in-safari-instead-of-the-app) |
| El enlace del correo electrónico no abre la aplicación | [El vínculo profundo desde el correo electrónico no abre la aplicación](#deep-link-from-email-does-not-open-the-app) |
| Todos los enlaces del correo electrónico abren la aplicación | [Todos los enlaces del correo electrónico abren la aplicación](#every-email-link-opens-the-app) |
| Funciona desde push pero no desde mensaje dentro de la aplicación (o viceversa) | [El vínculo profundo funciona desde push pero no desde mensaje dentro de la aplicación](#deep-link-works-from-push-but-not-from-in-app-message) |
| "Open Web URL Inside App" muestra un WebView en blanco | ["Open Web URL Inside App" muestra una página en blanco o rota](#open-web-url-inside-app-shows-a-blank-or-broken-page) |
| El enlace de Branch no abre la aplicación o no enruta correctamente | [Solución de problemas de Branch con Braze](#branch) |
| El vínculo profundo falla sin causa clara | [Consejos generales de depuración](#general-debugging-tips) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de vinculación en profundidad" }

## Ruta de investigación estándar {#standard-investigation-path}

Utiliza este flujo de trabajo para cada incidente de vinculación en profundidad. Comienza en el paso 1.

1. Prueba el enlace fuera de Braze. Para esquemas personalizados, ejecuta `xcrun simctl openurl booted "<URL>"` en Terminal (por ejemplo, `xcrun simctl openurl booted "myapp://products/123"`). Para enlaces universales, pega la URL en la aplicación Notas en un dispositivo físico y tócala.
2. [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) y reproduce el problema. Busca entradas `Opening '<URL>':` con `channel`, `useWebView` e `isUniversalLink`.
3. Para enlaces universales, valida tu archivo AASA y el permiso de Associated Domains.
4. Para enlaces de correo electrónico, confirma que el dominio de seguimiento de clics aloja un archivo AASA válido.
5. Si implementas `BrazeDelegate.braze(_:shouldOpenURL:)`, verifica que gestione los enlaces de manera consistente en todos los canales.
6. Si el problema persiste, contacta con [soporte de Braze]({{site.baseurl}}/braze_support) con los registros detallados y la URL del enlace.

## El vínculo profundo con esquema personalizado no abre la vista correcta {#custom-scheme-deep-link-does-not-open-the-correct-view}

**Síntoma:** Un vínculo profundo con esquema personalizado (por ejemplo, `myapp://products/123`) abre tu aplicación pero no navega a la pantalla prevista.

1. **Verifica que el esquema esté registrado.** En Xcode, comprueba que tu esquema aparezca en `CFBundleURLTypes` dentro de `Info.plist`.
2. **Comprueba tu controlador.** Establece un punto de interrupción en `application(_:open:options:)` para confirmar que se está llamando e inspecciona el parámetro `url`.
3. **Prueba el vínculo de forma independiente.** Ejecuta el siguiente comando desde Terminal para probar el vínculo profundo fuera de Braze:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Si el vínculo no funciona aquí, el problema está en la gestión de URL de tu aplicación, no en Braze.
4. **Comprueba el formato de la URL.** Verifica que la URL en tu Campaign coincida con lo que tu controlador espera. Los errores comunes incluyen componentes de ruta faltantes o uso incorrecto de mayúsculas y minúsculas.

## El enlace universal se abre en Safari en lugar de en la aplicación {#universal-link-opens-in-safari-instead-of-the-app}

**Síntoma:** Un enlace universal (por ejemplo, `https://myapp.com/products/123`) se abre en Safari en lugar de en tu aplicación.

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

## Los vínculos profundos del correo electrónico no abren la aplicación {#deep-link-from-email-does-not-open-the-app}

**Síntoma:** Un enlace en un correo electrónico no abre tu aplicación a través del enlace universal.

Los enlaces de correo electrónico pasan por el sistema de seguimiento de clics de tu ESP, que envuelve los enlaces en un dominio de seguimiento (por ejemplo, `https://click.yourdomain.com/...`). Para que los enlaces universales funcionen desde el correo electrónico, debes configurar el archivo AASA en tu dominio de seguimiento de clics, no solo en tu dominio principal.

### Verificar el AASA del dominio de seguimiento de clics {#verify-click-tracking-domain-aasa}

1. Identifica tu dominio de seguimiento de clics en la configuración de tu ESP (SendGrid, SparkPost o Amazon SES).
2. Aloja el archivo AASA en `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Confirma que el archivo AASA en el dominio de seguimiento de clics incluye el mismo `appID` y patrones de ruta válidos.

Para instrucciones de configuración específicas de cada ESP, consulta [Enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

### Comprobar la cadena de redirecciones {#check-the-redirect-chain}

Algunos ESP realizan una redirección desde la URL de seguimiento de clics a tu URL final. Los enlaces universales solo funcionan si iOS reconoce el dominio *inicial* (el dominio de seguimiento de clics) como asociado con tu aplicación. Si la redirección omite la verificación del AASA, el enlace se abre en Safari.

Para probar:

1. Envíate un correo electrónico de prueba.
2. Mantén presionado el enlace e inspecciona la URL: esta es la URL de seguimiento de clics.
3. Verifica que este dominio tenga un archivo AASA válido.

## Todos los enlaces de correo electrónico abren la aplicación {#every-email-link-opens-the-app}

**Síntoma:** Todos los enlaces de un correo electrónico abren tu aplicación, incluidos los enlaces que esperas que se abran en un navegador.

Tu archivo AASA en el dominio de seguimiento de clics usa `paths` que coinciden con todas las URL de ese dominio (por ejemplo, `*` o `/*`). iOS entonces trata cada enlace de correo electrónico con seguimiento de clics como un enlace universal.

Limita `paths` a las URL que deben abrir la aplicación. Para SendGrid, haz coincidir `/uni/` y añade `universal="true"` solo en esos enlaces.

Para la configuración específica de ESP, incluidos los valores de `pathPrefix` de Android, consulta [Enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#universal-links-app-links-and-click-tracking).

## El vínculo profundo funciona desde push pero no desde un mensaje dentro de la aplicación (o viceversa) {#deep-link-works-from-push-but-not-from-in-app-message}

**Síntoma:** El mismo vínculo profundo funciona desde un canal de Braze pero no desde otro.

### Verifica el BrazeDelegate {#check-the-brazedelegate}

Si implementas `BrazeDelegate.braze(_:shouldOpenURL:)`, verifica que gestione los vínculos de forma coherente en todos los canales. El parámetro `context` incluye el canal de origen. Busca lógica condicional que pueda filtrar accidentalmente vínculos de canales específicos.

### Habilita el registro detallado {#enable-verbose-logging}

[Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) y reproduce el problema. Busca la entrada de registro `Opening`:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Compara la salida del registro del canal que funciona con la del canal que no funciona. Las diferencias en `useWebView` o `isUniversalLink` indican cómo el SDK está interpretando el vínculo de forma diferente.

### Verifica los delegados de visualización personalizados {#check-for-custom-display-delegates}

Si usas un delegado de visualización personalizado para mensajes dentro de la aplicación o un controlador de clics de Content Cards, verifica que pase correctamente los eventos de vínculo al SDK de Braze para su gestión.

## "Abrir URL web dentro de la aplicación" muestra una página en blanco o dañada {#open-web-url-inside-app-shows-a-blank-or-broken-page}

**Síntoma:** Al seleccionar **Open Web URL Inside App** aparece una WebView en blanco o dañada.

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
- Dominios personalizados (si están configurados en el panel de Branch)

### Habilita el registro de ambos SDK {#enable-both-sdks-logging}

Para diagnosticar dónde se rompe el enlace en la cadena:

1. Habilita el [registro detallado de Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Busca entradas `Opening '<URL>':` para verificar que el SDK recibió el enlace.
2. Habilita el [modo de prueba de Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Comprueba el panel de Branch para ver los eventos de clics en los enlaces.
3. Si Braze registra el enlace, pero Branch no detecta un clic, es probable que el problema esté en la lógica de enrutamiento del `BrazeDelegate`.

### Comprueba la configuración del panel de Branch {#check-branch-dashboard-configuration}

En el panel de Branch, verifica:

- El **Bundle ID** y el **Team ID** de tu aplicación coinciden con tu proyecto Xcode.
- Tus **Associated Domains** incluyen el dominio de enlace de Branch.
- Tu archivo AASA de Branch es válido (Branch lo aloja automáticamente en dominios `app.link`).

### Prueba los enlaces de Branch de forma independiente {#test-branch-links-independently}

Prueba el enlace de Branch fuera de Braze para aislar el problema:

1. Abre el enlace de Branch en Safari en tu dispositivo. Si no se abre la aplicación, el problema está en tu configuración de Branch o AASA, no en Braze.
2. Pega el enlace de Branch en la aplicación Notas y pulsa sobre él. Los enlaces universales funcionan de forma más fiable desde Notas que desde la barra de direcciones de Safari.

## Consejos generales de depuración {#general-debugging-tips}

### Usa el registro detallado {#use-verbose-logging}

[Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) para ver exactamente cómo el SDK procesa los enlaces. Entradas clave a buscar:

| Entrada de registro | Qué significa |
|---|---|
| `Opening '<URL>': - channel: notification` | El SDK está procesando un enlace de una notificación push |
| `Opening '<URL>': - channel: inAppMessage` | El SDK está procesando un enlace de un mensaje dentro de la aplicación |
| `Opening '<URL>': - channel: contentCard` | El SDK está procesando un enlace de una tarjeta de contenido |
| `useWebView: true` | El SDK abre la URL en el WebView dentro de la aplicación |
| `isUniversalLink: true` | El SDK identificó la URL como un enlace universal |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Usa el registro detallado" }

Para más detalles sobre cómo leer estos registros, consulta [Lectura de registros detallados]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

### Prueba los enlaces de forma aislada {#test-links-in-isolation}

Antes de probar a través de Braze, verifica que tu vínculo profundo o enlace universal funcione por sí solo:

- **Esquema personalizado**: Ejecuta `xcrun simctl openurl booted "myapp://path"` en la Terminal.
- **Enlace universal**: Pega la URL en la aplicación Notas en un dispositivo físico y tócala. No pruebes desde la barra de direcciones de Safari, ya que iOS trata las URL escritas de forma diferente a los enlaces que se tocan.
- **Enlace de Branch**: Abre el enlace de Branch desde la aplicación Notas en un dispositivo.

### Prueba en un dispositivo físico {#test-on-a-physical-device}

Los enlaces universales tienen soporte limitado en el simulador de iOS. Siempre prueba en un dispositivo físico para obtener resultados precisos. Si necesitas probar en un simulador, añade el archivo `.entitlements` a la fase de compilación **Copy Bundle Resources**.