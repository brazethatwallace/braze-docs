# Conmutadores de características {#feature-flags}

> Los conmutadores de características te permiten habilitar o deshabilitar a distancia la funcionalidad para una selección específica o aleatoria de usuarios. Y lo que es más importante, te permiten activar y desactivar una característica en producción sin necesidad de desplegar código adicional ni actualizar la tienda de aplicaciones. Esto te permite desplegar nuevas características con seguridad y confianza.

{% alert tip %}
Cuando estés listo para crear tus propios conmutadores de características, consulta [Crear conmutadores de características]({{site.baseurl}}/developer_guide/feature_flags/create).
{% endalert %}

## Requisitos previos {#prerequisites}

Estas son las versiones mínimas del SDK or kit de desarrollo de software necesarias para empezar a usar los conmutadores de características:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Ejemplos {#use-cases}

### Despliegues graduales {#gradual-rollouts}

Usa los conmutadores de características para habilitar progresivamente características a una muestra de la población. Por ejemplo, puedes lanzar de forma suave una nueva característica primero a tus usuarios VIP. Esta estrategia ayuda a mitigar los riesgos asociados con desplegar nuevas características a todos de una vez y ayuda a detectar errores temprano.

![Imagen en movimiento del control deslizante de tráfico de despliegue yendo de 0% a 100%.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Por ejemplo, digamos que hemos decidido añadir un nuevo enlace de "Soporte por chat en vivo" a nuestra aplicación para un servicio al cliente más rápido. Podríamos lanzar esta característica a todos los clientes de una vez. Sin embargo, un lanzamiento amplio conlleva riesgos, como:

* Nuestro equipo de soporte todavía está en formación, y los clientes pueden abrir tickets de soporte después de que se lance. Esto no nos da ningún margen en caso de que el equipo de soporte necesite más tiempo.
* No estamos seguros del volumen real de nuevos casos de soporte que recibiremos, por lo que podríamos no tener el personal adecuado.
* Si nuestro equipo de soporte se ve abrumado, no tenemos una estrategia para desactivar rápidamente esta característica de nuevo.
* Podría haber errores introducidos en el widget de chat, y no queremos que los clientes tengan una experiencia negativa.

Con los conmutadores de características de Braze, podemos desplegar gradualmente la característica y mitigar todos estos riesgos:

* Activaremos la característica de "Soporte por chat en vivo" cuando el equipo de soporte diga que está listo.
* Habilitaremos esta nueva característica solo para el 10 % de los usuarios para determinar si tenemos el personal adecuado.
* Si hay algún error, podemos desactivar rápidamente la característica en lugar de apresurarnos a desplegar una nueva versión.

Para desplegar gradualmente esta característica, podemos [crear un conmutador de características]({{site.baseurl}}/developer_guide/feature_flags/create) llamado "Live Chat Widget."

![Detalles del conmutador de características de un ejemplo llamado Live Chat Widget. El ID es enable_live_chat. La descripción de este conmutador de características indica que el widget de chat en vivo se mostrará en la página de soporte.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

En el código de nuestra aplicación, solo mostraremos el botón **Start Live Chat** cuando el conmutador de características de Braze esté habilitado:

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

{% alert note %}
Leer `braze.featureFlags.featureFlags` o `braze.featureFlags.featureFlag(id:)` bloquea el hilo que lo llama hasta que el SDK or kit de desarrollo de software haya completado sus operaciones posteriores a la inicialización. Para contextos del hilo principal o sensibles a la latencia, usa [`getAllFeatureFlags(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/getallfeatureflags(_:)) en su lugar.

```swift
// Non-blocking — completion handler always delivers on the main thread.
braze.featureFlags.getAllFeatureFlags { flags in
  let liveChatEnabled = flags.first(where: { $0.id == "enable_live_chat" })?.enabled ?? false
  liveChatView.isHidden = !liveChatEnabled
}
```

En Objective-C:

```objc
[braze.featureFlags getAllFeatureFlagsWithCompletion:^(NSArray<BRZFeatureFlag *> *flags) {
  // Use `flags` here.
}];
```
{% endalert %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### Controlar variables de la aplicación de forma remota {#remotely-control-app-variables}

Usa los conmutadores de características para modificar la funcionalidad de tu aplicación en producción. Esto puede ser particularmente importante para las aplicaciones móviles, donde las aprobaciones de la tienda de aplicaciones impiden desplegar cambios rápidamente a todos los usuarios.

Por ejemplo, digamos que nuestro equipo de marketing quiere listar nuestras ventas y promociones actuales en la navegación de nuestra aplicación. Normalmente, nuestros ingenieros requieren una semana de anticipación para cualquier cambio y tres días para la revisión de la tienda de aplicaciones. Pero con el Día de Acción de Gracias, el Black Friday, el Cyber Monday, Hanukkah, Navidad y Año Nuevo, todo dentro de dos meses, no podremos cumplir con estos plazos ajustados.

Con los conmutadores de características, podemos dejar que Braze controle el contenido del enlace de navegación de nuestra aplicación, permitiendo que nuestro director de marketing haga cambios en minutos en lugar de días.

Para configurar remotamente esta característica, crearemos un nuevo conmutador de características llamado `navigation_promo_link` y definiremos las siguientes propiedades iniciales:

![Conmutador de características con propiedades de enlace y texto que dirigen a una página genérica de ventas.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

En nuestra aplicación, usaremos métodos getter de Braze para obtener las propiedades de este conmutador de características y construir los enlaces de navegación basándonos en esos valores:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

Ahora, el día antes de Acción de Gracias, solo tenemos que cambiar esos valores de propiedades en el panel de Braze.

![Conmutador de características con propiedades de enlace y texto que dirigen a una página de ventas de Acción de Gracias.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Como resultado, la próxima vez que alguien cargue la aplicación, verá las nuevas ofertas de Acción de Gracias.

### Coordinación de mensajes {#message-coordination}

Usa los conmutadores de características para sincronizar el despliegue de una característica y la mensajería, y reforzar la colaboración entre los equipos de producto y marketing. Al coordinar los lanzamientos de características y la mensajería a través de conmutadores de características, ambos equipos pueden alinear sus estrategias y crear experiencias de usuario consistentes.

Por ejemplo, digamos que estamos lanzando un nuevo programa de recompensas de fidelización para nuestros usuarios. Puede ser difícil para los equipos de marketing y producto coordinar perfectamente el momento de los mensajes promocionales con el despliegue de una característica. Sin embargo, con los conmutadores de características en Canvas, nuestro equipo de producto puede aplicar lógica sofisticada para habilitar una característica para una audiencia específica, mientras que nuestro equipo de marketing controla la mensajería relacionada para esos mismos usuarios.

Para coordinar de manera efectiva el despliegue de la característica y la mensajería, crearemos un nuevo conmutador de características llamado `show_loyalty_program`. Para nuestra primera fase de lanzamiento, dejaremos que Canvas controle cuándo y para quién se habilita el conmutador de características. Por ahora, dejaremos el porcentaje de despliegue en 0 % y no seleccionaremos ningún Segment objetivo.

![Un conmutador de características con el nombre Loyalty Rewards Program. El ID es show_loyalty_program, y la descripción indica que muestra el nuevo programa de recompensas de fidelización en la pantalla de inicio y la página de perfil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Luego, en Canvas, crearemos un [paso de conmutador de características]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) que habilite el conmutador de características `show_loyalty_program` para nuestro Segment "Clientes de alto valor":

![Un ejemplo de Canvas con un paso de división de audiencia donde el Segment de clientes de alto valor activa el conmutador de características show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Ahora, los usuarios en este Segment comenzarán a ver el nuevo programa de fidelización, y después de que se habilite, se enviará automáticamente un correo electrónico y un cuestionario para ayudar a nuestros equipos a recopilar comentarios.

### Experimentación de características {#feature-experimentation}

Usa los conmutadores de características para experimentar y confirmar tus hipótesis sobre tu nueva característica. Al dividir el tráfico en dos o más grupos, puedes comparar el impacto de un conmutador de características entre grupos y determinar el mejor curso de acción basándote en los resultados.

Para los experimentos de conmutadores de características, puedes tener hasta nueve grupos en total: un grupo de control más hasta ocho variantes.

Una [prueba A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) es una herramienta poderosa que compara las respuestas de los usuarios a múltiples versiones de una variable.

En este ejemplo, nuestro equipo ha creado un nuevo flujo de pago para nuestra aplicación de comercio electrónico. Aunque estamos seguros de que mejora la experiencia del usuario, queremos ejecutar una prueba A/B para medir su impacto en los ingresos de nuestra aplicación.

Para empezar, crearemos un nuevo conmutador de características llamado `enable_checkout_v2`. No añadiremos una audiencia ni un porcentaje de despliegue. En su lugar, usaremos un experimento de conmutador de características para dividir el tráfico, habilitar la característica y medir el resultado.

En nuestra aplicación, comprobaremos si el conmutador de características está habilitado o no, e intercambiaremos el flujo de pago según la respuesta:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Configuraremos nuestra prueba A/B en un [experimento de conmutador de características]({{site.baseurl}}/developer_guide/feature_flags/experiments).

Ahora, el 50 % de los usuarios verá la experiencia antigua, mientras que el otro 50 % verá la experiencia nueva. Luego podemos analizar las dos variantes para determinar qué flujo de pago resultó en una tasa de conversión más alta. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![Un experimento de conmutador de características que divide el tráfico en dos grupos del 50 por ciento.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Una vez que determinemos nuestra variante ganadora, podemos detener esta Campaign y aumentar el porcentaje de despliegue del conmutador de características al 100 % para todos los usuarios, mientras nuestro equipo de ingeniería lo codifica de forma fija en nuestra próxima versión de la aplicación.

### Segmentación {#segmentation}

Usa el filtro de **conmutador de características** para crear un Segment o dirigir mensajería a usuarios basándote en si tienen un conmutador de características habilitado. Por ejemplo, digamos que tienes un conmutador de características que controla contenido premium en tu aplicación. Podrías crear un Segment que filtre por usuarios que no tienen el conmutador de características habilitado, y luego enviar a ese Segment un mensaje instándolos a actualizar su cuenta para ver el contenido premium.

1. Abre tu Segment o audiencia del mensaje.
2. Añade el filtro de **conmutador de características**.
3. Selecciona el conmutador de características.
4. Configura el comparador a **es** para incluir a los usuarios que tienen el conmutador de características habilitado, o **no es** para incluir a los usuarios que no lo tienen.
![Constructor de Segments de Braze usando un filtro de valor habilitado de conmutador de características.]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Para más información sobre cómo filtrar en Segments, consulta [Crear un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

{% alert note %}
Para evitar Segments recursivos, no es posible crear un Segment que haga referencia a otros conmutadores de características.
{% endalert %}

## Limitaciones del plan {#plan-limitations}

Estas son las limitaciones de los conmutadores de características para los planes gratuitos y de pago.

| Característica                                                                                                   | Versión gratuita     | Versión de pago      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Conmutadores de características activos](#active-feature-flags)                                                                     | 10 por espacio de trabajo | 110 por espacio de trabajo |
| [Experimentos de Campaign activos]({{site.baseurl}}/developer_guide/feature_flags/experiments)          | 1 por espacio de trabajo  | 100 por espacio de trabajo |
| [Pasos de conmutador de características en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) | Ilimitados        | Ilimitados         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitaciones del plan" }

Un conmutador de características se considera activo y contará para tu límite si se aplica alguna de las siguientes condiciones:

- El despliegue es superior al 0%
- Se usa en un Canvas activo
- Se usa en un experimento activo

Incluso si el mismo conmutador de características coincide con varios criterios, como si se usa en un Canvas y el despliegue es del 50%, solo contará como 1 conmutador de características activo para tu límite.

{% alert note %}
Para comprar la versión de pago de los conmutadores de características, ponte en contacto con tu director de cuentas de Braze o solicita una actualización en el panel de Braze.
{% endalert %}