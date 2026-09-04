---
page_order: 1.1
nav_title: Guía de vinculación en profundidad para iOS
article_title: Guía de vinculación en profundidad para iOS
description: "Descubre qué tipo de vínculo profundo debes utilizar para tu aplicación iOS, cuándo necesitas un archivo AASA y qué métodos de delegado de aplicación debes implementar."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Guía de vinculación en profundidad para iOS {#ios-deep-linking-guide}

> Esta guía te ayuda a elegir la estrategia de vinculación en profundidad adecuada para tu aplicación iOS, en función del canal de mensajería que utilices y de si utilizas un proveedor de vínculos externo como Branch.

Para obtener más información sobre la implementación, consulta [Vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Para solucionar problemas, consulta [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Elegir un tipo de enlace {#choosing-a-link-type}

Hay tres formas de gestionar los enlaces de los mensajes de Braze en tu aplicación iOS. Cada una funciona de manera diferente y es adecuada para distintos canales y ejemplos.

| Tipo de enlace | Ejemplo | Ideal para | ¿Se abre sin la aplicación instalada? |
|---|---|---|---|
| **Esquema personalizado** | `myapp://products/123` | Push, mensajes dentro de la aplicación, Content Cards | No — el enlace falla |
| **Enlace universal** | `https://myapp.com/products/123` | Correo electrónico, SMS, canales con seguimiento de clics | Sí — recurre a la web |
| **Abrir URL web dentro de la aplicación** | Cualquier URL `https://` | Mostrar contenido web en un WebView modal | N/A — se muestra en WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Elegir un tipo de enlace" }

### Vínculos profundos con esquema personalizado {#custom-scheme-deep-links}

Los vínculos profundos con esquema personalizado (por ejemplo, `myapp://products/123`) abren tu aplicación directamente en una pantalla específica. Son la opción más sencilla para canales en los que los enlaces no son modificados por un tercero.

**Usa vínculos profundos con esquema personalizado cuando:**
- Envíes notificaciones push, mensajes dentro de la aplicación o Content Cards
- No necesites que el enlace funcione si la aplicación no está instalada
- No necesites seguimiento de clics (encapsulamiento de enlaces del ESP de correo electrónico)

**No uses vínculos profundos con esquema personalizado cuando:**
- Envíes correos electrónicos — los ESP encapsulan los enlaces para el seguimiento de clics, lo que rompe los esquemas personalizados
- Necesites que el enlace recurra a una página web si la aplicación no está instalada

### Enlaces universales {#universal-links}

Los enlaces universales (por ejemplo, `https://myapp.com/products/123`) son URL HTTPS estándar que iOS puede dirigir a tu aplicación en lugar de abrirlas en un navegador. Requieren configuración del lado del servidor (un archivo AASA) y configuración del lado de la aplicación (habilitación de Associated Domains).

**Usa enlaces universales cuando:**
- Envíes correos electrónicos. Tu ESP encapsula los enlaces para el seguimiento de clics, por lo que los enlaces deben ser HTTPS.
- Envíes SMS u otros canales en los que los enlaces se encapsulan o acortan.
- Necesites que el enlace recurra a una página web cuando la aplicación no esté instalada.
- Estés usando un proveedor de vinculación de terceros como Branch o AppsFlyer.

**No uses enlaces universales cuando:**
- Solo necesites vínculos profundos desde push, mensajes dentro de la aplicación o Content Cards. Los esquemas personalizados son más sencillos.

### "Abrir URL web dentro de la aplicación" {#open-web-url-inside-app}

Esta opción abre una página web dentro de un WebView modal en tu aplicación. Es gestionada completamente por el SDK de Braze usando `Braze.WebViewController` — no necesitas escribir ningún código de manejo de URL.

**Usa "Abrir URL web dentro de la aplicación" cuando:**
- Quieras mostrar una página web (como una promoción o un artículo) sin salir de tu aplicación.
- La URL sea una página web HTTPS estándar, no un vínculo profundo a una pantalla específica de la aplicación.

**No uses "Abrir URL web dentro de la aplicación" cuando:**
- Necesites navegar a una vista específica en tu aplicación. En su lugar, usa un esquema personalizado o un enlace universal.
- La página web requiera autenticación o tenga encabezados de Content Security Policy que bloqueen la incrustación.

## Lo que necesitas para cada tipo de enlace {#what-you-need-for-each-link-type}

### Vínculos profundos de esquema personalizado

| Requisito | Detalles |
|---|---|
| Archivo AASA | No es necesario |
| `Info.plist` | Registra tu esquema en `CFBundleURLTypes` y añádelo a `LSApplicationQueriesSchemes` |
| Método del delegado de la aplicación | Implementa `application(_:open:options:)` para analizar la URL y navegar |
| Configuración del SDK de Braze | Ninguna: el SDK abre las URL de esquema personalizado de forma predeterminada |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vínculos profundos de esquema personalizado" }

### Enlaces universales

| Requisito | Detalles |
|---|---|
| Archivo AASA | Obligatorio: alójalo en `https://yourdomain.com/.well-known/apple-app-site-association` |
| Dominios asociados | Añade `applinks:yourdomain.com` en Xcode en **Signing & Capabilities** |
| Método del delegado de la aplicación | Implementa `application(_:continue:restorationHandler:)` para gestionar `NSUserActivity` |
| Configuración del SDK de Braze | Establece `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (opcional) | Implementa `braze(_:shouldOpenURL:)` para enrutamiento personalizado (por ejemplo, Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enlaces universales" }

{% alert important %}
Si envías correos electrónicos a través de Braze, tu ESP (SendGrid, SparkPost o Amazon SES) envuelve los enlaces en un dominio de seguimiento de clics. Debes alojar el archivo AASA en tu dominio de seguimiento de clics también, no solo en tu dominio principal. Para la configuración completa, consulta [Enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links). Si todos los enlaces de correo electrónico abren la aplicación, consulta [Todos los enlaces de correo electrónico abren la aplicación]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting#every-email-link-opens-the-app).
{% endalert %}

### "Abrir URL web dentro de la aplicación"

| Requisito | Detalles |
|---|---|
| Archivo AASA | No es necesario |
| Método del delegado de la aplicación | No es necesario: el SDK lo gestiona automáticamente |
| Configuración del SDK de Braze | Ninguna: selecciona **Open Web URL Inside App** en el creador de la campaña |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abrir URL web dentro de la aplicación" }

## Cuándo necesitas un archivo AASA {#when-aasa}

Solo se requiere un archivo Apple App Site Association (AASA) cuando utilizas **enlaces universales**. Le indica a iOS qué URL puede gestionar tu aplicación.

Necesitas un archivo AASA cuando:

- Envías vínculos profundos en Campaigns de correo electrónico (porque los ESP envuelven los vínculos en URL de seguimiento de clics HTTPS).
- Envías vínculos profundos en Campaigns de SMS (porque los vínculos pueden acortarse a direcciones URL HTTPS).
- Utilizas Branch, AppsFlyer u otro proveedor de vínculos (porque utilizan sus propios dominios HTTPS).
- Utilizas enlaces universales desde notificaciones push, mensajes dentro de la aplicación o Content Cards (menos habitual, pero posible con `forwardUniversalLinks = true`).

No necesitas un archivo AASA cuando:

- Solo utilizas vínculos profundos con esquema personalizado (por ejemplo, `myapp://`) desde notificaciones push, mensajes dentro de la aplicación o Content Cards.
- Utilizas la opción **Abrir URL web dentro de la aplicación**.

Para obtener instrucciones sobre la configuración de AASA, consulta [Enlaces universales y enlaces de aplicaciones]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Cuándo necesitas código de aplicación para gestionar enlaces {#when-app-code}

El método delegado que implementes dependerá del tipo de enlace que estés utilizando:

| Método delegado | Gestiona | Cuándo implementar |
|---|---|---|
| `application(_:open:options:)` | Vínculos profundos con esquema personalizado (`myapp://`) | Utilizas vínculos profundos con esquema personalizado desde cualquier canal |
| `application(_:continue:restorationHandler:)` | Enlaces universales (`https://`) | Utilizas enlaces universales desde correo electrónico, SMS o con `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Todas las URL abiertas por el SDK | Necesitas una lógica de enrutamiento personalizada (por ejemplo, Branch, gestión condicional, análisis) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cuándo necesitas código de aplicación para gestionar enlaces" }

{% alert tip %}
Si utilizas un proveedor de vínculos externo como Branch, implementa `BrazeDelegate.braze(_:shouldOpenURL:)` para interceptar las URL y reenviarlas al SDK del proveedor. Consulta [Branch para la vinculación en profundidad]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) para ver un ejemplo completo.
{% endalert %}

## Usar Branch con Braze {#branch}

Si utilizas [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) como proveedor de vínculos, tu configuración requiere algunos pasos adicionales más allá de la configuración estándar de enlaces universales:

1. **SDK de Branch**: Integra el SDK de Branch siguiendo [la documentación de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Dominios asociados**: Añade tu dominio de Branch (por ejemplo, `applinks:yourapp.app.link`) en Xcode, en **Signing & Capabilities**.
3. **BrazeDelegate**: Implementa `braze(_:shouldOpenURL:)` para redirigir los enlaces de Branch al SDK de Branch en lugar de dejar que Braze los gestione directamente.
4. **Reenviar enlaces universales**: Establece `configuration.forwardUniversalLinks = true` en tu configuración del SDK de Braze.

Para obtener detalles sobre la implementación y orientación sobre la depuración, consulta [Branch para la vinculación en profundidad]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking).