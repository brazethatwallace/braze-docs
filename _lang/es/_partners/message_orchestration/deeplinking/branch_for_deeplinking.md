---
nav_title: Branch para la vinculación en profundidad
article_title: Branch para la vinculación en profundidad
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Este artículo de referencia describe la asociación entre Braze y Branch y cómo utilizarla para apoyar tus prácticas de vinculación en profundidad."
search_tag: Partner

---

# Branch para la vinculación en profundidad {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/) es una plataforma de enlace móvil utilizada para adquirir, interactuar y medir a través de dispositivos, canales y plataformas, proporcionando una visión holística de los puntos de intervención del usuario.

_Esta integración está mantenida por Branch._

## Sobre la integración {#about-the-integration}

La integración de Braze y Branch te permite ofrecer mejores experiencias a tus clientes, ya que te permite [atribuir]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) correctamente el inicio de su viaje de usuario y conectarlos a través de vínculos profundos a su ubicación prevista.

{% alert tip %}
Para obtener ayuda a la hora de elegir el enfoque de vinculación en profundidad adecuado para tu caso de uso, consulta la [guía de vinculación en profundidad de iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/).
{% endalert %}

## Integración {#integration}

Sigue [la guía de integración de SDK de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview) para poner en marcha tu integración de Branch. Consulta a continuación otros casos de uso.

### Compatibilidad con enlaces universales de iOS {#support-ios-universal-links}

Para admitir el envío de enlaces universales de iOS como vínculos profundos desde Braze:

#### Paso 1: Configurar los enlaces universales de Branch {#step-1-set-up-branch-universal-links}

Sigue la documentación de Branch para configurar [los enlaces universales](https://help.branch.io/developers-hub/docs/ios-universal-links). Como parte de esta configuración, Branch aloja el archivo AASA en tu dominio de enlace de Branch (por ejemplo, `yourapp.app.link`) de forma automática.

#### Paso 2: Configurar los dominios asociados {#step-2-configure-associated-domains}

En Xcode, ve al objetivo de tu aplicación > **Signing & Capabilities** y añade tu dominio de enlace de Branch en **Associated Domains**:

```
applinks:yourapp.app.link
applinks:yourapp-alternate.app.link
```

Si utilizas un dominio personalizado de Branch, añádelo también.

#### Paso 3: Reenviar enlaces universales en Braze {#step-3-forward-universal-links-in-braze}

Establece `forwardUniversalLinks` en `true` en la configuración de tu SDK de Braze para que el SDK reenvíe los enlaces universales al `AppDelegate` de tu aplicación:

{% tabs %}
{% tab swift %}
```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
let braze = Braze(configuration: configuration)
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
configuration.forwardUniversalLinks = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endtab %}
{% endtabs %}

#### Paso 4: Enrutar los enlaces de Branch con BrazeDelegate {#step-4-route-branch-links-with-brazedelegate}

Implementa [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate) para interceptar los enlaces de Branch antes de que Braze los gestione. Esto garantiza que Branch pueda procesar el enlace y realizar su propio enrutamiento:

{% tabs %}
{% tab swift %}
```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host,
     host.contains("app.link") || host.contains("yourdomain.com") {
    // Let Branch handle this link
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle all other links
  return true
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  NSString *host = context.url.host;
  if (host && ([host containsString:@"app.link"] || [host containsString:@"yourdomain.com"])) {
    [[Branch getInstance] handleDeepLink:context.url];
    return NO;
  }
  return YES;
}
```
{% endtab %}
{% endtabs %}

Sustituye `yourdomain.com` por tu dominio personalizado de Branch, si corresponde.

### Vinculación en profundidad en el correo electrónico {#deep-linking-in-email}

Consulta la documentación sobre [enlaces universales y enlaces de aplicación]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/)
o consulta [la documentación de Branch](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) para configurar la vinculación en profundidad desde los correos electrónicos enviados a través de Braze.

La vinculación a números de teléfono (añadir `tel` a `href`) no es compatible con la aplicación de Gmail para iOS a menos que el usuario conceda permisos de llamada a la aplicación.

Dependiendo de tu ESP, puede ser necesaria una personalización adicional para admitir enlaces universales con seguimiento de clics. Esta información se describe en nuestro artículo específico. También puedes consultar las siguientes referencias para obtener más información:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

## Solución de problemas {#troubleshooting}

Si los enlaces de Branch no funcionan como se espera desde las campañas de Braze, sigue estos pasos.

### Verificar que el enlace funciona fuera de Braze {#verify-the-link-works-outside-of-braze}

Abre el enlace de Branch desde la aplicación Notas en un dispositivo iOS físico. Si no abre tu aplicación:

- El problema está en tu configuración de Branch o AASA, no en Braze.
- Valida tu AASA de Branch en `https://yourapp.app.link/.well-known/apple-app-site-association`.
- Comprueba que tu Bundle ID y Team ID coinciden en el dashboard de Branch.

### Habilitar el registro dual {#enable-dual-logging}

1. **Braze**: [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) y busca entradas `Opening '<URL>':`. Esto confirma que el SDK recibió el enlace.
2. **Branch**: Habilita el [modo de prueba de Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) y comprueba en el dashboard de Branch los eventos de clic en enlaces.
3. **Compara**: Si Braze registra el enlace pero Branch no detecta un clic, es probable que la lógica de enrutamiento de `BrazeDelegate` no esté interceptando el enlace correctamente. Comprueba que la coincidencia de dominio en `shouldOpenURL` incluya tu dominio de Branch.

### Problemas comunes {#common-issues}

| Síntoma | Causa probable | Solución |
|---|---|---|
| El enlace de Branch se abre en Safari | AASA no válido o ausente en el dominio de Branch | Verifica los dominios asociados y el archivo AASA |
| El enlace de Branch se abre pero lleva a la pantalla incorrecta | Datos del enlace de Branch mal configurados | Comprueba las reglas de enrutamiento en el dashboard de Branch |
| El enlace funciona desde push pero no desde correo electrónico | Falta AASA en el dominio de seguimiento de clics | Aloja el AASA en el dominio de seguimiento de clics de tu ESP; consulta [Configuración de correo electrónico](#deep-linking-in-email) |
| `shouldOpenURL` nunca se activa para los enlaces de Branch | `forwardUniversalLinks` no está habilitado | Establece `configuration.forwardUniversalLinks = true` |
| El enlace de Branch funciona desde Notas pero no desde Braze | `BrazeDelegate` devuelve `true` para las URL de Branch | Verifica la comprobación de dominio en `shouldOpenURL` para que coincida con tu dominio de Branch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Problemas comunes" }

Para más escenarios de solución de problemas de vinculación en profundidad, consulta [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/).