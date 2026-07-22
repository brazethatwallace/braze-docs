---
nav_title: Integrar el SDK
article_title: Integra el SDK de Braze
description: "Aprende a integrar el SDK de Braze."
page_order: 2.0
---

# ![Logotipo de Braze]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integra el SDK de Braze {#braze-logo-image_buster-assetsbraze_primary_icon_blacksvg-stylefloatrightwidth120pxborder0-classnoimgborderintegrate-the-braze-sdk}

> Aprende a integrar el SDK de Braze. Cada SDK está alojado en su propio repositorio público de GitHub, que incluye aplicaciones de muestra totalmente compilables que puedes utilizar para probar las características de Braze o implementar junto con tus propias aplicaciones. Para obtener más información, consulta [Referencias, repositorios y aplicaciones de ejemplo]({{site.baseurl}}/developer_guide/references). Para obtener información más general sobre el SDK, consulta [Introducción: Resumen de la integración]({{site.baseurl}}/developer_guide/getting_started/integration_overview).

Para ver el contenido del README del SDK reflejado en la documentación, consulta [Guías de repositorios]({{site.baseurl}}/developer_guide/sdk_repository_guides).

{% alert tip %}
Después de integrar el SDK, puedes habilitar la [autenticación del SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication) para añadir una capa adicional de seguridad evitando las solicitudes no autorizadas al SDK. La autenticación del SDK está disponible para Web, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) y Expo.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
## Integración del SDK de Roku {#integrating-the-roku-sdk}

### Paso 1: Añadir archivos {#step-1-add-files}

Los archivos del SDK de Braze se encuentran en el directorio `sdk_files` del [repositorio del SDK de Braze para Roku](https://github.com/braze-inc/braze-roku-sdk).

1. Añade `BrazeSDK.brs` a tu aplicación en el directorio `source`.
2. Añade `BrazeTask.brs` y `BrazeTask.xml` a tu aplicación en el directorio `components`.

### Paso 2: Añadir referencias {#step-2-add-references}

Añade una referencia a `BrazeSDK.brs` en tu escena principal utilizando el siguiente elemento `script`:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Paso 3: Configurar {#step-3-configure}

Dentro de `main.brs`, establece la configuración de Braze en el nodo global:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Puedes encontrar tu [punto final de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) y tu clave de API en el panel de Braze.

### Paso 4: Inicializar Braze {#step-4-initialize-braze}

Inicializa la instancia de Braze:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configuraciones opcionales {#optional-configurations}

### Registro {#logging}

Para depurar tu integración de Braze, puedes ver la consola de depuración de Roku para los registros de Braze. Consulta [Depuración de código](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) de Roku Developers para obtener más información.

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
Mientras realizas el control de calidad de tu integración de SDK, utiliza el [Depurador de SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sin necesidad de activar el registro detallado en tu aplicación.
{% endalert %}