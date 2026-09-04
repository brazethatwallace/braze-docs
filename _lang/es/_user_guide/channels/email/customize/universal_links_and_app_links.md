---
nav_title: "Enlaces universales y App Links"
article_title: "Enlaces universales y App Links"
page_order: 6.4
page_type: reference
description: "Este artículo describe cómo configurar los enlaces universales de Apple y los Android App Links."
channel: email
---

# Enlaces universales y App Links {#universal-links-and-app-links}

> Este artículo describe cómo configurar los enlaces universales de Apple y los Android App Links.

{% alert tip %}
Para una comparación de tipos de enlaces en todos los canales de mensajería y orientación sobre cuándo necesitas un archivo AASA, consulta la [guía de vinculación en profundidad de iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide).
{% endalert %}

Los enlaces universales de Apple y los Android App Links son mecanismos diseñados para proporcionar una transición fluida entre el contenido web y las aplicaciones móviles. Mientras que los enlaces universales son específicos de iOS, los Android App Links cumplen el mismo propósito para las aplicaciones Android.

## Cómo funcionan los enlaces universales y los App Links {#how-universal-links-and-app-links-work}

Los enlaces universales (iOS) y los App Links (Android) son enlaces web estándar (`http://mydomain.com`) que apuntan tanto a una página web como a un contenido dentro de una aplicación.

Cuando se abre un enlace universal o un App Link, el sistema operativo comprueba si alguna aplicación instalada está registrada para ese dominio. Si se encuentra una aplicación, se abre de inmediato sin cargar la página web. Si no se encuentra ninguna aplicación, la URL web se carga en el navegador web predeterminado del usuario, que también podría estar configurado para redirigir a la App Store o a Google Play Store, respectivamente.

En términos sencillos, los enlaces universales permiten que un sitio web asocie sus páginas web con pantallas específicas de la aplicación, de modo que cuando un usuario hace clic en un enlace a una página web que corresponde a una pantalla de la aplicación, la aplicación puede abrirse directamente (si la aplicación está instalada actualmente).

{% alert important %}
Firebase Dynamic Links está obsoleto. Braze no tiene una integración directa con Firebase, y la vinculación en profundidad se gestiona fuera de la plataforma de Braze. Migra a soluciones nativas de cada plataforma (enlaces universales de Apple y Android App Links, como se describe en este artículo) o a proveedores de servicios alternativos de vinculación en profundidad. Para obtener orientación sobre la migración, consulta [las preguntas frecuentes de migración de Firebase](https://firebase.google.com/support/dynamic-links-faq).
{% endalert %}

Esta tabla describe las diferencias clave entre los enlaces universales y los vínculos profundos tradicionales:

|                        | Enlaces universales y App Links                                  | Vínculos profundos                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilidad de plataforma | iOS (versión 9 y posteriores) y Android (versión 6.0 y posteriores)  | Se utilizan en varios sistemas operativos móviles    |
| Propósito                | Vinculan fácilmente contenido web y de aplicación en dispositivos iOS y Android | Vincular a contenido específico de la aplicación |
| Función               | Dirige a páginas web o contenido de la aplicación según el contexto           | Abre pantallas específicas de la aplicación   |
| Instalación de la aplicación       | Abre la aplicación si está instalada, de lo contrario abre contenido web | Requiere que la aplicación esté instalada |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo funcionan los enlaces universales y los App Links" }

## Ejemplos {#use-cases}

Los enlaces universales y los App Links se utilizan con más frecuencia en las campañas de correo electrónico, ya que los correos electrónicos pueden abrirse y hacerse clic desde dispositivos de escritorio y móviles.

Algunos canales no funcionan bien con estos enlaces. Por ejemplo, las notificaciones push, los mensajes dentro de la aplicación y las Content Cards deben usar vínculos profundos basados en esquema (`mydomain://`).

{% alert note %}
Los Android App Links requieren un `IBrazeDeeplinkHandler` personalizado con lógica para gestionar los enlaces de sus dominios de forma independiente de otras URL web. Puede ser más fácil usar vínculos profundos en su lugar y mantener las prácticas de enlace uniformes para los canales distintos al correo electrónico.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar enlaces universales y App Links:

- Tu sitio web debe ser accesible a través de HTTPS
- Tu aplicación debe estar disponible en la App Store (iOS) o Google Play Store (Android)

## Configuración de enlaces universales y App Links {#setting-up-universal-links-and-app-links}

Para que las aplicaciones admitan enlaces universales o App Links, tanto iOS como Android requieren que se aloje un archivo de permisos especial en el dominio del enlace. Este archivo contiene definiciones de qué aplicaciones pueden abrir enlaces desde ese dominio y, para iOS, qué rutas pueden abrir esas aplicaciones:

- **iOS:** Archivo Apple App Site Association (AASA)
- **Android:** Archivo Digital Asset Links

Además de este archivo de permisos, existen definiciones codificadas de qué dominios de enlace la aplicación puede abrir, que se configuran dentro de la aplicación:

- **iOS:** Se establecen como "Associated Domains" en Xcode
- **Android:** Se definen en el archivo `AndroidManifest.xml` de la aplicación

Esta asociación bidireccional dominio-aplicación es necesaria para que un enlace universal o App Link funcione y evita que cualquier aplicación secuestre enlaces de un dominio en particular o que cualquier dominio abra una aplicación en particular.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Estos pasos están adaptados de la documentación para desarrolladores de Apple. Para más información, consulta [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Paso 1: Configura los permisos de tu aplicación {#step-1-configure-your-app-entitlements}

{% alert note %}
[En Xcode 13 y versiones posteriores](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), Xcode puede gestionar el aprovisionamiento de permisos de forma automática. Probablemente puedes pasar directamente al [paso&nbsp;1c](#step-1c) y volver a estas instrucciones si tienes problemas.
{% endalert %}

#### Paso 1a: Registra tu aplicación {#step-1a}

1. Ve a developer.apple.com e inicia sesión.
2. Haz clic en **Certificates, Identifiers & Profiles**.
3. Haz clic en **Identifiers**.
4. Si aún no tienes un identificador de aplicación registrado, haz clic en + para crear uno.
   a. Introduce un **Name**. Puede ser lo que quieras.
   b. Introduce el **Bundle ID**. Puedes encontrar tu bundle ID en la pestaña **General** de tu proyecto de Xcode para el destino de compilación adecuado.

#### Paso 1b: Activa Associated Domains en tu identificador de aplicación {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. En tu identificador de aplicación existente o recién creado, localiza la sección **App Services**.
2. Selecciona **Associated Domains**.
3. Haz clic en **Save**.

![Sección App Services]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Paso 1c: Activa Associated Domains en tu proyecto de Xcode {#step-1c}

Antes de continuar, asegúrate de que tu proyecto de Xcode tenga seleccionado el mismo equipo que donde acabas de registrar tu identificador de aplicación.

1. En Xcode, ve a la pestaña **Capabilities** de tu archivo de proyecto.
2. Activa **Associated Domains**.

##### Consejo de solución de problemas {#troubleshooting-tip}

Si ves el error "An App ID with Identifier 'your-app-id' is not available. Please enter a different string", haz lo siguiente:

1. Comprueba que tienes seleccionado el equipo correcto.
2. Comprueba que el Bundle ID ([paso 1a](#step-1a)) de tu proyecto de Xcode coincide con el utilizado para registrar el identificador de aplicación.

#### Paso 1d: Añade el permiso de dominio {#step-1d-add-the-domain-entitlement}

En la sección de dominios, añade la etiqueta de dominio correspondiente. Debes añadir el prefijo `applinks:`. En este caso, puedes ver que hemos añadido `applinks:yourdomain.com`.

![Sección Associated Domains]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Paso 1e: Confirma que el archivo de permisos está incluido en la compilación {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

En el explorador del proyecto, asegúrate de que tu nuevo archivo de permisos esté seleccionado en **Target Membership**.

Xcode debería gestionarlo automáticamente.

### Paso 2: Configura tu sitio web para alojar el archivo AASA {#step-2-configure-your-website-to-host-the-aasa-file}

Para asociar el dominio de tu sitio web con tu aplicación nativa en iOS, necesitas alojar el archivo Apple App Site Association (AASA) en tu sitio web. Este archivo funciona como una forma segura de verificar la propiedad del dominio en iOS. Antes de iOS 9, los desarrolladores podían registrar cualquier esquema URI para abrir sus aplicaciones, sin ninguna verificación. Sin embargo, con AASA, este proceso se ha vuelto mucho más seguro y fiable.

El archivo AASA contiene un objeto JSON con una lista de aplicaciones y las rutas URL del dominio que deben incluirse o excluirse como enlaces universales. Aquí tienes un ejemplo de archivo AASA:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: Se construye combinando el **Team ID** de tu aplicación (ve a `https://developer.apple.com/account/#/membership/` para obtener el team ID) y el **Bundle Identifier**. En este ejemplo, "JHGFJHHYX" es el team ID, y "com.Facebook.ios" es el bundle ID.
- `paths`: Matriz de cadenas que especifican qué rutas se incluyen o excluyen de la asociación. Puedes usar `NOT` antes de la ruta para desactivar rutas. En este ejemplo, todos los enlaces de esta ruta irán a la web en lugar de abrir la aplicación. Puedes usar `*` como comodín para habilitar todas las rutas de un directorio y `?` para coincidir con un solo carácter (como /archives/201?/ para coincidir con todos los números de 2010 a 2019).

{% alert note %}
Estas cadenas distinguen entre mayúsculas y minúsculas, y las cadenas de consulta y los identificadores de fragmento se ignoran.
{% endalert %}

### Paso 3: Aloja el archivo AASA en tu dominio {#step-3-host-the-aasa-file-on-your-domain}

Cuando tu archivo AASA esté listo, puedes alojarlo en tu dominio en `https://<<yourdomain>>/apple-app-site-association` o en `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Sube el archivo `apple-app-site-association` a tu servidor web HTTPS. Puedes colocar el archivo en la raíz de tu servidor o en el subdirectorio `.well-known`. No añadas `.json` al nombre del archivo.

{% alert important %}
iOS solo intentará obtener el archivo AASA a través de una conexión segura (HTTPS).
{% endalert %}

Al alojar el archivo AASA, asegúrate de que el archivo siga estas directrices:

- Se sirve a través de HTTPS.
- Usa el tipo MIME `application/json`.
- No supera los 128 KB (requisito a partir de iOS 9.3.1)

### Paso 4: Prepara tu aplicación para gestionar enlaces universales {#step-4-prepare-your-app-to-handle-universal-links}

Cuando un usuario toca un enlace universal en un dispositivo iOS, el dispositivo inicia la aplicación y le envía un objeto [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). La aplicación puede entonces consultar el objeto NSUserActivity para determinar cómo fue iniciada.

Para admitir enlaces universales en tu aplicación, sigue estos pasos:

1. Añade un permiso que especifique los dominios que tu aplicación admite.
2. Actualiza el delegado de tu aplicación para responder adecuadamente cuando reciba el objeto NSUserActivity.

En Xcode, abre la sección **Associated Domains** en la pestaña **Capabilities** y añade una entrada para cada dominio que tu aplicación admita, con el prefijo `applinks:`. Por ejemplo, `applinks:www.mywebsite.com`.

{% alert note %}
Apple recomienda limitar esta lista a no más de 20 a 30 dominios.
{% endalert %}

### Paso 5: Prueba tu enlace universal {#step-5-test-your-universal-link}

Añade el enlace universal a un correo electrónico y envíalo a un dispositivo de prueba. Pegar un enlace universal directamente en el campo de URL de Safari no hará que la aplicación se abra automáticamente. Si haces esto, tendrás que deslizar manualmente el sitio web hacia abajo para que aparezca un aviso en la parte superior preguntándote si deseas abrir la aplicación correspondiente.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Estos pasos están adaptados de la documentación para desarrolladores de Android. Para más información, consulta [Add Android App Links](https://developer.android.com/training/app-links#add-app-links) y [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Los Android App Links requieren un `IBrazeDeeplinkHandler` personalizado con lógica para gestionar los enlaces de sus dominios por separado de otras URL web. Puede resultar más sencillo usar vínculos profundos y mantener prácticas de vinculación uniformes para canales distintos del correo electrónico.
{% endalert %}

### Paso 1: Crea vínculos profundos {#step-1-create-deep-links}

Primero, necesitas crear vínculos profundos para tu aplicación Android. Esto se puede hacer añadiendo [filtros de intención](https://developer.android.com/guide/components/intents-filters) en tu archivo `AndroidManifest.xml`. El filtro de intención debe incluir la acción `VIEW` y la categoría `BROWSABLE`, junto con la URL de tu sitio web en el elemento de datos.

### Paso 2: Asocia tu aplicación con tu sitio web {#step-2-associate-your-app-with-your-website}

Necesitas asociar tu aplicación con tu sitio web. Esto se puede hacer creando un archivo Digital Asset Links. Este archivo debe estar en formato JSON e incluir detalles sobre las aplicaciones Android que pueden abrir enlaces a tu sitio web. Debe colocarse en el directorio `.well-known` de tu sitio web.

### Paso 3: Actualiza el archivo de manifiesto de tu aplicación {#step-3-update-your-app-manifest-file}

En tu archivo `AndroidManifest.xml`, añade un elemento meta-data dentro del elemento application. El elemento meta-data debe tener un atributo `android:name` de "asset_statements" y un atributo `android:resource` que apunte a un archivo de recursos con una matriz de cadenas que incluya la URL de tu sitio web.

### Paso 4: Prepara tu aplicación para gestionar vínculos profundos {#step-4-prepare-your-app-to-handle-deep-links}

En tu aplicación Android, necesitas gestionar los vínculos profundos entrantes. Puedes hacerlo obteniendo la intención que inició tu actividad y extrayendo los datos de ella.

### Paso 5: Prueba tus vínculos profundos {#step-5-testing-your-deep-links}

Finalmente, puedes probar tus vínculos profundos. Envíate un enlace a través de una aplicación de mensajería o correo electrónico y haz clic en él. Si todo está configurado correctamente, debería abrir tu aplicación.

{% endtab %}
{% endtabs %}

## Enlaces universales, App Links y seguimiento de clics {#universal-links-app-links-and-click-tracking}

{% alert note %}
Los enlaces con seguimiento de clics normalmente se configuran como parte de tu incorporación para correo electrónico. Si esto no se completó durante la incorporación del cliente, contacta a tu director de cuentas para obtener ayuda.
{% endalert %}

Nuestros partners de envío de correo electrónico utilizan dominios de seguimiento de clics para envolver todos los enlaces e incluir parámetros de URL para el seguimiento de clics en los correos electrónicos de Braze.

Por ejemplo, un enlace como `https://www.example.com` se convierte en algo como `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Para permitir que los enlaces de correo electrónico con seguimiento de clics funcionen como enlaces universales o App Links, necesitarás realizar alguna configuración adicional. Asegúrate de añadir el dominio de seguimiento de clics (`links.email.example.com`) como un dominio que la aplicación tiene permitido abrir. Además, el dominio de seguimiento de clics debe servir los archivos AASA (iOS) o Digital Asset Links (Android). Esto ayudará a garantizar que los enlaces de correo electrónico con seguimiento de clics funcionen fácilmente.

Si no quieres que cada enlace con seguimiento de clics sea un enlace universal o App Link, puedes especificar qué enlaces deben ser enlaces universales según el partner de envío de correo electrónico. Consulta las siguientes pestañas para más detalles.

{% tabs %}
{% tab SendGrid %}

Para tratar un enlace con seguimiento de clics de SendGrid como un enlace universal:

1. Configura tus valores de pathPrefix en AASA o AndroidManifest para tratar solo los enlaces con `/uni/` en la ruta de la URL como enlaces universales.
2. Añade el atributo `universal="true"` a la etiqueta ancla (`<a>`) de tu enlace. Esto cambia la ruta de URL del enlace envuelto para incluir `/uni/`.

{% alert note %}
Para correos electrónicos páginas móviles aceleradas, este atributo debe ser data-universal="true".
{% endalert %}

Por ejemplo:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. Asegúrate de que tu aplicación esté configurada para manejar los enlaces envueltos correctamente. Consulta el artículo de SendGrid sobre [Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) y sigue los pasos para tu sistema operativo. Este artículo contiene código de ejemplo para [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) y [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Con esta configuración, los enlaces con `/uni/` en la ruta de URL funcionarán como enlaces universales, mientras que todos los demás enlaces funcionarán como enlaces web.

{% endtab %}
{% tab SparkPost %}

Para tratar un enlace con seguimiento de clics de SparkPost como un enlace universal, añade el siguiente atributo en la sección de atributos del editor de arrastrar y soltar para correo electrónico, o edita manualmente el HTML del enlace para incluir el siguiente atributo en la etiqueta ancla de tu enlace: `data-msys-sublink="custom_path"`.

Esta ruta personalizada te permite tratar selectivamente las URLs con ese valor como un enlace universal.

Por ejemplo:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Luego, asegúrate de que tu aplicación esté configurada para manejar la ruta personalizada correctamente. Consulta el artículo de SparkPost sobre [Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Este artículo contiene código de ejemplo para [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) y [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

{% endtab %}
{% tab Amazon SES %}

Utiliza rutas personalizadas para añadir segmentos de ruta a las URLs de seguimiento de clics de correo electrónico. Esto crea patrones de URL predecibles que los sistemas operativos móviles pueden reconocer para enlaces universales y App Links.

Cuando los usuarios tocan enlaces de correo electrónico en dispositivos móviles, las rutas personalizadas te ayudan a controlar si los enlaces se abren en tu aplicación móvil principal, una aplicación especializada o el navegador móvil (por ejemplo, páginas de productos, programas de fidelización, enlaces para cancelar suscripción o páginas legales).

Para tratar un enlace con seguimiento de clics de Amazon SES como un enlace universal o App Link:

1. Añade atributos `ses:custom-path` a tus etiquetas ancla en el HTML del correo electrónico, o añade el atributo en la sección **Atributos** del editor de arrastrar y soltar para correo electrónico. La ruta personalizada se inserta en la URL de seguimiento de clics envuelta.

Por ejemplo:

```html
<!-- Opens main shopping app -->
<a href="https://yourstore.com/product" ses:custom-path="shop">Shop Now</a>
<!-- Opens loyalty app -->
<a href="https://yourstore.com/rewards" ses:custom-path="rewards">My Rewards</a>
<!-- Opens specialized app -->
<a href="https://yourstore.com/limited" ses:custom-path="limited">Limited Edition</a>
<!-- Stays in browser -->
<a href="https://yourstore.com/unsubscribe" ses:no-track>Unsubscribe</a>
```

Asegúrate de que tus rutas personalizadas cumplan estos requisitos:

- **Formato:** Solo caracteres alfanuméricos, puntos, guiones bajos y guiones
- **Longitud:** 1–32 caracteres
- **Distinción entre mayúsculas y minúsculas:** Las rutas distinguen entre mayúsculas y minúsculas para cumplir con los requisitos del sistema operativo móvil

{:start="2"}
2. Confirma que tus URLs de seguimiento envueltas incluyan el segmento de ruta personalizada. Sin el atributo, los enlaces rastreados usan `track.yourstore.com/CL0/{encodedUrl}/...`. Con el atributo, siguen este formato: `track.yourstore.com/CL1/{customPath}/{encodedUrl}/...`

Por ejemplo:

- `track.yourstore.com/CL1/shop/...`
- `track.yourstore.com/CL1/rewards/...`

{:start="3"}
3. Configura tus archivos de asociación de sitio en tu dominio de seguimiento de clics para que las rutas coincidan con `/CL1/{customPath}/`.

**iOS (Apple App Site Association):**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/CL1/shop/*", "/CL1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/CL1/limited/*"]
    }]
  }
}
```

**Android (Digital Asset Links):**

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourcompany.mainapp",
    "sha256_cert_fingerprints": ["..."]
  }
}]
```

Android hace coincidir las rutas en tu aplicación en lugar de en `assetlinks.json`. Establece `android:pathPrefix="/CL1/{customPath}/"` en el filtro de intención en tu `AndroidManifest.xml` para cada ruta personalizada que tu aplicación maneje.

Asegúrate de que tu aplicación esté configurada para manejar estos enlaces envueltos. Añade tu dominio de seguimiento de clics a los dominios asociados de tu aplicación (iOS) o filtros de intención (Android), y aloja el archivo AASA o Digital Asset Links en ese dominio como se describió anteriormente en este artículo.

{% endtab %}
{% endtabs %}

### Desactivar el seguimiento de clics enlace por enlace {#turning-off-click-tracking-on-a-link-to-link-basis}

Puedes desactivar el seguimiento de clics para enlaces específicos añadiendo código HTML a tu mensaje de correo electrónico para el editor HTML o a un bloque HTML para el editor de arrastrar y soltar.

#### SendGrid

Si tu proveedor de servicios de correo electrónico es SendGrid, utiliza el código HTML `clicktracking=off` de esta manera:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

Si tu proveedor de servicios de correo electrónico es SparkPost, utiliza el código HTML `data-msys-clicktrack="0"` de esta manera:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Si tu proveedor de servicios de correo electrónico es Amazon SES, utiliza el código HTML `ses:no-track` de esta manera:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Editor de arrastrar y soltar {#drag-and-drop-editor}

Al utilizar el editor de correo electrónico de arrastrar y soltar, introduce tu código HTML como un atributo personalizado si tu enlace está adjunto a texto, un botón o una imagen.

##### Atributo personalizado para un enlace de texto {#custom-attribute-for-a-text-link}

#### SendGrid

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `clicktracking`
- **Valor:** `off`

#### SparkPost

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `data-msys-clicktrack`
- **Valor:** `0`

![Un atributo personalizado para un enlace de texto.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Atributo personalizado para un botón o imagen {#custom-attribute-for-a-button-or-image}

#### SendGrid

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `clicktracking`
- **Valor:** `off`
- **Tipo:** Link

#### SparkPost

Selecciona lo siguiente para el atributo personalizado:

- **Nombre:** `data-msys-clicktrack`
- **Valor:** `0`
- **Tipo:** Link

![Un atributo personalizado para un botón.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Solución de problemas de enlaces universales con seguimiento de clics {#troubleshooting-universal-links-with-click-tracking}

Si tus enlaces universales no funcionan como se espera en tus correos electrónicos, como cuando navegan al destinatario desde su aplicación de correo electrónico al navegador web antes de finalmente redirigir a la aplicación, consulta estos consejos para solucionar problemas de tu configuración de enlaces universales.

#### Outlook muestra `[?it=` o texto de URL sin formato en lugar de un botón {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

Outlook puede mostrar texto de llamada a la acción como `[?it=` o imprimir parte del `href` cuando un enlace no utiliza un esquema de URL válido **`http://` o `https://`**. Los esquemas personalizados, los esquemas faltantes o las URLs mal formadas no se tratan como hipervínculos, por lo que el cliente muestra el texto del atributo en su lugar. Confirma que cada botón, enlace de imagen y URL rastreada use un destino `https://` (o `http://`) completo. Esto aplica tanto a enlaces universales como a enlaces web estándar.

#### Verifica la ubicación del archivo de enlaces {#verify-link-file-location}

Asegúrate de que el archivo AASA (iOS) o el archivo Digital Asset Links (Android) esté ubicado en el lugar correcto:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

Es importante asegurarte de que estos archivos siempre sean accesibles públicamente. Si no puedes acceder a ellos, es posible que hayas omitido un paso en la configuración de enlaces universales para correo electrónico.

#### Verifica las definiciones de dominio {#verify-domain-definitions}

Asegúrate de que tengas las definiciones correctas para los dominios que tu aplicación tiene permitido abrir.

- **iOS:** Revisa los dominios asociados configurados en Xcode para tu aplicación ([Paso 1c: Activar los dominios asociados en tu proyecto de Xcode]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links?tab=ios#step-1c)). Comprueba que el dominio de seguimiento de clics esté incluido en esa lista.
- **Android:** Abre la página de información de la aplicación (mantén presionado el icono de la aplicación y haz clic en ⓘ). Dentro del menú de información de la aplicación, localiza **Abrir de forma predeterminada** y toca esa opción. Esto debería mostrar una pantalla con todos los enlaces verificados que la aplicación tiene permitido abrir. Comprueba que el dominio de seguimiento de clics esté incluido en esa lista.

#### Cada enlace de correo electrónico abre la aplicación {#every-email-link-opens-the-app}

Si cada enlace en un correo electrónico abre tu aplicación, incluidos los enlaces que esperas que se abran en un navegador, los valores de `paths` del AASA (iOS) o `pathPrefix` de Android en tu dominio de seguimiento de clics coinciden con todo el dominio (por ejemplo `*` o `/*`).

Limita esos patrones a las URLs que deben abrir la aplicación. Para SendGrid, haz coincidir `/uni/` y añade `universal="true"` solo en esos enlaces. Consulta [Enlaces universales, App Links y seguimiento de clics](#universal-links-app-links-and-click-tracking).

#### El dominio de seguimiento no puede servir archivos .well-known {#tracking-domain-cant-serve-well-known-files}

En algunos casos, tu dominio de seguimiento de clics puede no ser capaz de alojar los archivos `.well-known` requeridos debido a limitaciones del ESP o restricciones de infraestructura. Si no puedes alojar el archivo AASA o Digital Asset Links en tu dominio de seguimiento, considera las siguientes opciones:

- **Desactivar selectivamente el seguimiento de clics en URLs de vínculos profundos:** Puedes desactivar el seguimiento de clics para enlaces universales específicos para que vayan directamente a tu dominio principal (donde puedes alojar el archivo AASA o Digital Asset Links). Ten en cuenta que este método puede causar pérdida de análisis de clics para esos enlaces específicos. Consulta [Desactivar el seguimiento de clics enlace por enlace](#turning-off-click-tracking-on-a-link-to-link-basis) para obtener instrucciones.
- **Colocar un CDN delante del subdominio de seguimiento:** Si necesitas cobertura completa de seguimiento de clics y vinculación en profundidad, puedes colocar un CDN (como Cloudflare o CloudFront) delante de tu subdominio de seguimiento. Configura el CDN para servir los archivos `.well-known` localmente y redirigir todo el tráfico restante a tu ESP. Este enfoque es más complejo, pero te da control total sobre el seguimiento de clics y los enlaces universales.

#### Los enlaces funcionan en un espacio de trabajo pero no en otro {#links-working-in-one-workspace-but-not-another}

Si los enlaces universales o App Links funcionan correctamente en tu espacio de trabajo de producción pero fallan en tu espacio de trabajo de desarrollo o pruebas, verifica que el dominio de la dirección de correo electrónico de envío coincida con el dominio de seguimiento configurado en la configuración de correo electrónico de cada espacio de trabajo. Una configuración inconsistente entre espacios de trabajo puede causar que los enlaces se comporten de manera diferente incluso cuando se utilizan las mismas plantillas de correo electrónico y archivos AASA o Digital Asset Links.

Para comprobar tu configuración de correo electrónico:

1. Ve a **Configuración** > **Preferencias de correo electrónico** en el panel de Braze.
2. Revisa la **Configuración de correo electrónico saliente** en **Configuración de envío**.
3. Confirma que tu dominio de envío y dominio de seguimiento estén correctamente alineados para el espacio de trabajo donde los enlaces no funcionan.

Si tu dominio de envío difiere entre espacios de trabajo, asegúrate de que cada espacio de trabajo tenga los registros de DNS apropiados configurados y que tus archivos AASA (iOS) o Digital Asset Links (Android) sean accesibles desde cada dominio de seguimiento.