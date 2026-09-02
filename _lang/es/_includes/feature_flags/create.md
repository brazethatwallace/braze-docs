# Crear conmutadores de características {#create-feature-flags}

> Los conmutadores de características te permiten habilitar o deshabilitar a distancia la funcionalidad para una selección de usuarios. Crea un nuevo conmutador de características dentro del panel de Braze. Proporciona un nombre y un `ID`, una audiencia objetivo y un porcentaje de usuarios para los que habilitar esta característica. Luego, utilizando ese mismo `ID` en el código de tu aplicación o sitio web, puedes ejecutar condicionalmente determinadas partes de tu lógica empresarial. Para saber más sobre los conmutadores de características y cómo puedes utilizarlos en Braze, consulta [Acerca de los conmutadores de características]({{site.baseurl}}/developer_guide/feature_flags).

## Requisitos previos {#prerequisites}

### Versión del SDK {#sdk-version}

Para usar los conmutadores de características, asegúrate de que tus SDK estén actualizados con al menos estas versiones mínimas:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Permisos de Braze {#braze-permissions}

Para gestionar los conmutadores de características en el panel, necesitarás ser administrador o tener los siguientes [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions):

| Permiso                                                                    | Lo que puedes hacer                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Manage Feature Flags**                                                      | Ver, crear y editar conmutadores de características.     |
| **Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library** | Ver la lista de conmutadores de características disponibles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos de Braze" }

## Crear un conmutador de características {#creating-a-feature-flag}

### Paso 1: Crear un nuevo conmutador de características {#step-1-create-a-new-feature-flag}

Ve a **Mensajería** > **Conmutadores de características** y selecciona **Crear conmutador de características**.

![Una tabla de datos que muestra un conmutador de características existente y cómo crear uno nuevo.]({% image_buster /assets/img/feature_flags/create_ff.png %}){: style="max-width:75%"}

### Paso 2: Completar los detalles {#step-2-fill-out-the-details}

En **Detalles del conmutador de características**, introduce un nombre, ID y descripción para tu conmutador de características.

![Un formulario que muestra que puedes añadir un nombre, ID, descripción y propiedades a un conmutador de características.]({% image_buster /assets/img/feature_flags/create_ff_properties.png %}){: style="max-width:75%"}


| Campo        | Descripción                                                                |
|--------------|----------------------------------------------------------------------------|
| Nombre       | Un título legible para tus especialistas en marketing y administradores.   |
| ID           | El ID único que usarás en tu código para comprobar si esta característica está [habilitada para un usuario](#enabled). Este ID no se puede cambiar después, así que revisa las [prácticas recomendadas de nomenclatura de ID](#naming-conventions) antes de continuar. |
| Descripción  | Una descripción opcional que aporta contexto sobre tu conmutador de características. |
| Propiedades  | Propiedades opcionales que configuran remotamente tu conmutador de características. Se pueden sobrescribir en pasos en Canvas o en experimentos de conmutadores de características. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Completar los detalles" }

### Paso 2a: Crear propiedades personalizadas {#step-2a-create-custom-properties}

En **Propiedades**, opcionalmente puedes crear propiedades personalizadas a las que tu aplicación puede acceder a través del SDK de Braze cuando tu característica está habilitada. Puedes asignar un valor de cadena, booleano, imagen, marca de tiempo, JSON o número a cada variable, así como establecer un valor predeterminado.

{% tabs local %}
{% tab ejemplo %}
En el siguiente ejemplo, el conmutador de características muestra un banner de agotamiento de existencias para una tienda de comercio electrónico usando las propiedades personalizadas listadas:

|Nombre de la propiedad|Tipo|Valor|
|--|--|--|
| `banner_height`|`number`|`75`|
| `banner_color`|`string`|`blue`|
| `banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
| `homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
| `account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
| `footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2a: Crear propiedades personalizadas" }

{% alert tip %}
No hay límite en la cantidad de propiedades que puedes añadir. Sin embargo, las propiedades de un conmutador de características están limitadas a un total de 10.000 caracteres.
{% endalert %}
{% endtab %}
{% endtabs %}

### Paso 4: Elegir los segmentos objetivo {#step-4-choose-segments-to-target}

Antes de desplegar un conmutador de características, necesitas elegir un [segmento]({{site.baseurl}}/user_guide/audience/segments) de usuarios al que dirigirte. Selecciona **Añadir regla** en tu conmutador recién creado y luego usa los menús desplegables de grupo de filtros y segmento para filtrar usuarios de tu audiencia objetivo. Añade múltiples filtros para refinar aún más tu audiencia.

![Un cuadro de texto etiquetado como Tráfico de despliegue con la capacidad de añadir segmentos y filtros.]({% image_buster /assets/img/feature_flags/segmentation_ff.png %}){: style="max-width:75%;"}

### Paso 5: Configurar el tráfico de despliegue {#rollout}

De forma predeterminada, los conmutadores de características siempre están inactivos, lo que te permite separar la fecha de lanzamiento de tu característica de la activación total de usuarios. Para comenzar tu despliegue, usa la sección **Tráfico de despliegue** para introducir un porcentaje en el cuadro de texto. Esto elegirá el porcentaje de usuarios aleatorios en tu segmento seleccionado que recibirán esta nueva característica.

{% alert important %}
No configures tu tráfico de despliegue a más de 0% hasta que estés listo para que tu nueva característica entre en funcionamiento. Cuando definas inicialmente tu conmutador de características en el panel, deja esta configuración en 0%.
{% endalert %}

{% alert important %}
Para desplegar un conmutador con una sola regla o para una audiencia única, añade tu primera regla con los criterios de segmentación y porcentajes de despliegue seleccionados. Por último, confirma que la regla **Todos los demás** esté desactivada y guarda tu conmutador.
{% endalert %}

## Implementaciones de conmutadores de características con varias reglas {#multi-rule-feature-flag-rollouts}

Usa las implementaciones de conmutadores de características con varias reglas para definir una secuencia de reglas de evaluación de usuarios, lo que permite una segmentación precisa y lanzamientos de características controlados. Este método es ideal para desplegar la misma característica a audiencias diversas.

### Orden de evaluación {#evaluation-order}

Las reglas de los conmutadores de características se evalúan de arriba a abajo, en el orden en que aparecen en la lista. Un usuario cumple la primera regla que satisface. Si un usuario no cumple ninguna regla, su elegibilidad se determina por la regla predeterminada "Todos los demás".

### Cualificación de usuarios {#user-qualification}

- Si un usuario cumple los criterios de la primera regla, es inmediatamente elegible para recibir el conmutador de características.
- Si un usuario no califica para la primera regla, se evalúa con la segunda regla, y así sucesivamente.

La evaluación secuencial continúa hasta que un usuario califica para una regla o llega a la regla "Todos los demás" en la parte inferior de la lista.

### Regla "Todos los demás" {#everyone-else-rule}

La regla "Todos los demás" actúa como predeterminada. Si un usuario no califica para ninguna de las reglas anteriores, su elegibilidad para el conmutador de características se determinará por la configuración del interruptor de la regla "Todos los demás". Por ejemplo, si la regla "Todos los demás" está desactivada, en el estado predeterminado, un usuario que no cumpla los criterios de ninguna otra regla no recibirá el conmutador de características al iniciar su sesión.

### Reordenar reglas {#re-ordering-rules}

De forma predeterminada, las reglas se ordenan en la secuencia en que se crean, pero puedes reordenarlas arrastrándolas y soltándolas en el panel.

![Una imagen que muestra que un usuario puede añadir una regla a un conmutador de características.]({% image_buster /assets/img/feature_flags/add_rule.png %}){: style="max-width:80%;"}

![Una imagen que muestra un resumen de un conmutador de características con varias reglas añadidas y una regla de todos los demás.]({% image_buster /assets/img/feature_flags/mr_rules_overview.png %}){: style="max-width:80%;"}

### Ejemplos de conmutadores de características con varias reglas {#multi-rule-feature-flag-use-cases}

#### Lanzar gradualmente una página de pago {#gradually-release-a-checkout-page}

Supongamos que trabajas para una marca de comercio electrónico y tienes una nueva página de pago que deseas implementar en diferentes regiones geográficas para garantizar la estabilidad. Usando conmutadores de características con varias reglas, puedes configurar lo siguiente:

- **Regla 1:** Tu Segment de EE. UU. se establece al 100 %.
- **Regla 2:** Tu Segment se establece al 50 % de tus usuarios brasileños, de modo que no todos reciben el flujo al mismo tiempo.
- **Regla 3 (Todos los demás):** Para todos los demás usuarios, activa tu regla "Todos los demás" y configúrala al 15 %, de modo que una parte de todos los usuarios pueda pagar con el nuevo flujo.

#### Alcanzar primero a los testers internos {#reach-internal-testers-first}

Supongamos que eres un gestor de producto que quiere asegurarse de que tus testers internos siempre reciban el conmutador de características cuando lanzas un nuevo producto. Puedes añadir tu Segment de testers internos a tu primera regla y configurarla al 100 %, para que tus testers internos sean elegibles durante cada lanzamiento de características.

## Utilizar el campo «habilitado» para tus conmutadores de características {#enabled}

Una vez definido tu conmutador de características, configura tu aplicación o sitio web para comprobar si está habilitado para un usuario concreto. Cuando esté habilitado, establecerás alguna acción o harás referencia a las propiedades variables del conmutador de características en función de tu caso de uso. El SDK de Braze proporciona métodos getter para obtener el estado de tu conmutador de características y sus propiedades en tu aplicación.

Los conmutadores de características se actualizan automáticamente al inicio de la sesión, para que puedas mostrar la versión más actualizada de tu característica en el momento del lanzamiento. El SDK almacena en caché estos valores para poder utilizarlos sin conexión.

{% alert note %}
Asegúrate de registrar [las impresiones del conmutador de características](#impressions).
{% endalert %}

Supongamos que vas a lanzar un nuevo tipo de perfil de usuario para tu aplicación. Puedes configurar el `ID` como `expanded_user_profile`. A continuación, harías que tu aplicación comprobara si debe mostrar este nuevo perfil de usuario a un usuario concreto. Por ejemplo:

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Cordova %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### Registro de la impresión de un conmutador de características {#impressions}

Realiza un seguimiento de la impresión de un conmutador de características siempre que un usuario haya tenido la oportunidad de interactuar con tu nueva característica, o cuando __podría__ haber interactuado si la característica está desactivada (en el caso de un grupo de control en una prueba A/B). Las impresiones del conmutador de características solo se registran una vez por sesión.

Normalmente, puedes poner esta línea de código directamente debajo de donde haces referencia a tu conmutador de características en tu aplicación:

{% tabs %}
{% tab Web %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Flutter %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### Acceder a las propiedades {#accessing-properties}

Para acceder a las propiedades de un conmutador de características, utiliza uno de los métodos siguientes, según el tipo que hayas definido en el panel.

Si no existe ninguna propiedad del tipo correspondiente para la clave que proporcionaste, estos métodos devolverán `null`.

{% tabs %}
{% tab Web %}

```javascript
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the string property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty: Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty: String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty: [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Unity %}

```csharp
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");
```

{% endtab %}
{% tab Cordova %}

```javascript
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Flutter %}

```dart
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Roku %}

```brightscript
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% endtabs %}

### Obtener una lista de todos los conmutadores de características {#get-list-of-flags}

{% tabs %}
{% tab Web %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Swift %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Unity %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab Cordova %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Flutter %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab Roku %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### Actualizar los conmutadores de características {#refreshing}

Puedes actualizar los conmutadores de características del usuario actual en mitad de la sesión para obtener los últimos valores de Braze.

{% alert tip %}
La actualización se produce automáticamente al iniciar la sesión. Solo es necesario actualizar antes de acciones importantes del usuario, como antes de cargar una página de pago, o si sabes que se hará referencia a un conmutador de características.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.refreshFeatureFlags();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab Flutter %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### Escuchar los cambios {#updates}

Puedes configurar el SDK de Braze para que escuche y actualice tu aplicación cuando el SDK actualice cualquier conmutador de características.

Esto es útil si quieres actualizar tu aplicación cuando un usuario ya no es elegible para una característica. Por ejemplo, establecer algún estado en tu aplicación en función de si una característica está habilitada o no, o de uno de sus valores de propiedad.

{% tabs %}
{% tab Web %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab Swift %}

```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab Unity %}

Para escuchar los cambios, ajusta los valores de **Game Object Name** y **Callback Method Name** en **Braze Configuration** > **Feature Flags** a los valores correspondientes de tu aplicación.

{% endtab %}
{% tab Cordova %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab Flutter %}

En el código Dart de tu aplicación, utiliza el siguiente código de ejemplo:

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

{% subtabs %}
{% subtab Flutter SDK 18.0.0+ %}

Los datos de los conmutadores de características se reenvían automáticamente desde las capas nativas de Android e iOS. No se requiere configuración adicional.

{% endsubtab %}
{% subtab Flutter SDK 17.1.0 and earlier %}

Si estás usando Flutter SDK 17.1.0 o anterior, el reenvío de datos de conmutadores de características desde la capa nativa de iOS requiere configuración manual. Es probable que tu aplicación contenga una devolución de llamada `featureFlags.subscribeToUpdates` que llame a `BrazePlugin.processFeatureFlags(featureFlags)`. Para migrar a Flutter SDK 18.0.0, elimina la llamada a `BrazePlugin.processFeatureFlags(_:)` — el reenvío de datos ahora se gestiona automáticamente.

Para ver un ejemplo, consulta [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) en la aplicación de ejemplo del SDK de Braze para Flutter.

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React Hook %}
```typescript
import { useEffect, useState } from "react";
import {
  FeatureFlag,
  getFeatureFlag,
  removeSubscription,
  subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    };
  }, [id]);

  return featureFlag;
};
```
{% endtab %}
{% endtabs %}

## Comprobar la elegibilidad del usuario {#checking-user-eligibility}

Para comprobar a qué conmutadores de características es elegible un usuario en Braze, ve a **Audiencia** > **Buscar usuarios**, luego busca y selecciona un usuario.

En la pestaña **Elegibilidad de conmutadores de características**, puedes filtrar la lista de conmutadores de características elegibles por plataforma, aplicación o dispositivo. También puedes previsualizar la carga útil que se devolverá al usuario seleccionando <i class="fa-solid fa-eye" aria-label="Vista previa"></i> junto a un conmutador de características.

![Una imagen que muestra la tabla de conmutadores de características para los que un usuario es elegible.]({% image_buster /assets/img/feature_flags/eligibility.png %}){: style="max-width:85%;"}

## Ver el registro de cambios {#viewing-the-changelog}

Para ver el registro de cambios de un conmutador de características, abre un conmutador de características y selecciona **Registro de cambios**.

![Página "Editar" de un conmutador de características, con el botón "Registro de cambios" resaltado.]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

Aquí puedes revisar cuándo se realizó un cambio, quién lo hizo, a qué categoría pertenece y más.

![El registro de cambios del conmutador de características seleccionado.]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## Segmentación con conmutadores de características {#segmentation}

Braze hace un seguimiento automático de los usuarios que tienen habilitado un conmutador de características. Puedes crear un segmento o dirigir mensajería utilizando el [filtro **Feature Flag**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#feature-flags). Para más información sobre cómo filtrar por segmentos, consulta [Crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

![La sección «Filtros» con «Feature Flag» escrito en la barra de búsqueda del filtro.]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
Para evitar segmentos recursivos, no es posible crear un segmento que haga referencia a otros conmutadores de características.
{% endalert %}

## Prácticas recomendadas {#best-practices}

### No combines los despliegues con Canvas o experimentos {#dont-combine-rollouts-with-canvases-or-experiments}

Para evitar que los usuarios se habiliten y deshabiliten desde diferentes puntos de entrada, debes establecer el control deslizante de despliegues en un valor mayor que cero O habilitar el conmutador de características en un Canvas o experimento. Como práctica recomendada, si planeas utilizar un conmutador de características en un Canvas o experimento, mantén el porcentaje de despliegue en cero.

### Convenciones de nomenclatura {#naming-conventions}

Para mantener tu código claro y coherente, considera usar el siguiente formato cuando asignes un nombre al ID de tu conmutador de características:

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

Sustituye lo siguiente:

| Marcador de posición | Descripción |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | El comportamiento de la característica. En tu código, asegúrate de que el comportamiento esté deshabilitado de forma predeterminada y evita usar frases como `disabled` en el nombre del conmutador de características. |
| `PRODUCT`   | El producto al que pertenece la característica. |
| `FEATURE`    | El nombre de la característica. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Convenciones de nomenclatura" }

Este es un ejemplo de conmutador de características donde `show` es el comportamiento, `animation_profile` es el producto y `driver` es la característica:

```plaintext
show_animation_profile_driver
```

### Planifica con anticipación {#planning-ahead}

Ve siempre a lo seguro. Al considerar nuevas características que puedan necesitar un interruptor de apagado, es mejor lanzar código nuevo con un conmutador de características y no necesitarlo, que darte cuenta de que se requiere una nueva actualización de la aplicación.

### Sé descriptivo {#be-descriptive}

Añade una descripción a tu conmutador de características. Aunque este es un campo opcional en Braze, puede ayudar a responder preguntas que otros puedan tener al explorar los conmutadores de características disponibles.

- Datos de contacto de quién es responsable de la habilitación y el comportamiento de este conmutador
- Cuándo se debe deshabilitar este conmutador
- Enlaces a documentación o notas sobre la nueva característica que controla este conmutador
- Cualquier dependencia o nota sobre cómo usar la característica

### Limpia los conmutadores de características antiguos {#clean-up-old-feature-flags}

Todos somos culpables de dejar características activas al 100 % de despliegue más tiempo del necesario.

Para ayudar a mantener tu código (y el panel de Braze) limpio, elimina los conmutadores de características permanentes de tu código base una vez que todos los usuarios se hayan actualizado y ya no necesites la opción de deshabilitar la característica. Esto ayuda a reducir la complejidad de tu entorno de desarrollo, y además mantiene ordenada tu lista de conmutadores de características.