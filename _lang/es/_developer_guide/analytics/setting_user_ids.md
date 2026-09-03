---
nav_title: Establecer ID de usuario
article_title: Establecer ID de usuario
page_order: 1.1
description: "Aprende a configurar los ID de usuario a través del SDK de Braze."
---

# Establecer ID de usuario {#set-user-ids}

> Aprende a configurar los ID de usuario a través del SDK de Braze. Son identificadores únicos que te permiten realizar el seguimiento de los usuarios en distintos dispositivos y plataformas, importar sus datos a través de la [API de datos de usuario]({{site.baseurl}}/api/endpoints/user_data) y enviar mensajes dirigidos a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging). Si no asignas un ID único a un usuario, Braze le asignará un ID anónimo; sin embargo, no podrás utilizar estas características hasta que lo hagas.

{% alert note %}
Para los SDK envolventes que no aparecen en la lista, utiliza el método nativo de Android o Swift correspondiente.
{% endalert %}

## Acerca de los usuarios anónimos {#about-anonymous-users}

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

### Prevenir el seguimiento de usuarios anónimos {#preventing-anonymous-user-tracking}

Si tu caso de uso requiere que no se recopilen datos antes de que un usuario sea identificado, puedes retrasar la inicialización del SDK de Braze hasta que el usuario inicie sesión y haya un `external_id` disponible. Establece una bandera en tu código que cambie a `true` cuando el usuario inicie sesión, y solo inicializa el SDK cuando esa bandera esté establecida.

{% alert warning %}
Solo retrasa la inicialización la **primera vez** que un usuario descargue tu aplicación (antes de que se establezca un `external_id`). Si impides que el SDK se inicialice cada vez que un usuario cierra sesión o inicia una nueva sesión, esto interferirá con la precarga de activos de mensajes dentro de la aplicación y tarjetas de contenido, lo que puede provocar errores de capacidad de entrega en esas Campaigns.
{% endalert %}

## Establecer un ID de usuario {#setting-a-user-id}

Para establecer un ID de usuario, llama al método `changeUser()` después de que el usuario inicie sesión por primera vez. Los ID deben ser únicos y seguir nuestras [buenas prácticas de nomenclatura](#naming-best-practices).

Si estás aplicando un hash a un identificador único, asegúrate de normalizar la entrada de tu función de hash. Por ejemplo, cuando apliques un hash a una dirección de correo electrónico, elimina los espacios en blanco iniciales o finales y ten en cuenta la localización.

{% tabs local %}
{% tab WEB %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Si prefieres utilizar Google Tag Administrador, puedes usar el tipo de etiqueta **Change User** para llamar al [método `changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Úsalo cada vez que un usuario inicie sesión o se identifique de alguna otra forma con su identificador único `external_id`.

Asegúrate de introducir el ID único del usuario actual en el campo **External User ID**, que generalmente se rellena mediante una variable de capa de datos enviada por tu sitio web.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción de Braze. Los ajustes incluidos son "tag type" y "external user ID".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}

{% alert note %}
`changeUser` pone en cola el cambio de usuario y retorna inmediatamente en el hilo que realiza la llamada. Cualquier setter de atributos llamado en `braze.user` después se serializa automáticamente detrás de las operaciones iniciadas por `changeUser`. La lectura de `braze.user.id` bloquea el hilo que realiza la llamada hasta que el cambio de usuario se complete por completo. Para contextos del hilo principal o sensibles a la latencia, utiliza en su lugar las alternativas no bloqueantes.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.user.getId { userId in
  print("User ID:", userId ?? "anonymous")
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let userId = await AppDelegate.braze?.user.getId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze.user getIdWithCompletion:^(NSString * _Nullable userId) {
  NSLog(@"User ID: %@", userId ?: @"anonymous");
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab React Native %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

### Cómo funciona `changeUser()` {#how-changeuser-works}

Cuando llamas a `changeUser()`, se aplican los siguientes comportamientos:

- Llamar a `changeUser()` con el **mismo** ID de usuario que ya está configurado no tiene efecto en el conteo de sesiones.
- Llamar a `changeUser()` con un ID de usuario **diferente** finaliza automáticamente la sesión actual e inicia una nueva.
- Cuando un usuario anónimo llama a `changeUser()` con un ID de usuario **nuevo** (uno que aún no existe en Braze), los datos del perfil anónimo se fusionan con el nuevo perfil identificado.
- Cuando un usuario anónimo llama a `changeUser()` con un ID de usuario **existente**, los datos del perfil anónimo no se fusionan con el perfil identificado.

{% alert note %}
Llamar a `changeUser()` desencadena un vaciado de datos como parte del cierre de la sesión del usuario actual. El SDK vacía automáticamente cualquier dato pendiente del usuario anterior antes de cambiar al nuevo usuario, por lo que no necesitas solicitar manualmente un vaciado de datos antes de llamar a `changeUser()`.
{% endalert %}

{% alert warning %}
No asignes un único ID de usuario compartido (por ejemplo, un ID externo estático predeterminado) ni llames a `changeUser()` cuando un usuario cierre la sesión. Hacerlo te impide volver a interactuar con usuarios que hayan iniciado sesión anteriormente en dispositivos compartidos y hace que todos los datos se registren bajo un único ID de usuario, lo que puede provocar que otras características no se comporten como se espera. En su lugar, haz un seguimiento de todos los ID de usuario por separado y asegúrate de que el proceso de cierre de sesión de tu aplicación permita volver a cambiar a un usuario que haya iniciado sesión anteriormente. Cuando se inicia una nueva sesión, Braze actualiza automáticamente los datos del perfil recién activo.
{% endalert %}

## Alias de usuario {#user-aliases}

### Cómo funcionan {#how-they-work}

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Establecer un alias de usuario {#setting-a-user-alias}

Un alias de usuario consta de dos partes: un nombre y una etiqueta. El nombre se refiere al identificador en sí, mientras que la etiqueta se refiere al tipo de identificador al que pertenece. Por ejemplo, si tienes un usuario en una plataforma de asistencia al cliente de terceros con el ID externo `987654`, puedes asignarle un alias en Braze con el nombre `987654` y la etiqueta `support_id`, para poder realizar su seguimiento entre plataformas.

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab React Native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## Prácticas recomendadas de nomenclatura de ID {#naming-best-practices}

Te recomendamos que crees ID de usuario utilizando el estándar [UUID (Universally Unique Identifier)](https://en.wikipedia.org/wiki/Universally_unique_identifier), es decir, cadenas de 128 bits aleatorias y bien distribuidas.

Como alternativa, puedes realizar un hash de un identificador único existente (como un nombre o una dirección de correo electrónico) para generar tus ID de usuario. Si lo haces, asegúrate de implementar la [autenticación del SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication) para evitar la suplantación de identidad de los usuarios.

{% alert warning %}
No utilices un valor fácil de adivinar ni un número incremental para tu ID de usuario. Esto puede exponer a tu organización a ataques maliciosos o a la filtración de datos.

Para mayor seguridad, utiliza la [autenticación del SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication).
{% endalert %}

Aunque es fundamental que nombres correctamente tus ID de usuario desde el principio, siempre puedes renombrarlos en el futuro utilizando el endpoint [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration).

| Tipos de ID no recomendados | Ejemplo no recomendado |
| ------------ | ----------- |
| ID de perfil visible del usuario o nombre de usuario | JonDoe829525552 |
| Dirección de correo electrónico | Anna@email.com |
| ID de usuario con autoincremento | 123 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prácticas recomendadas de nomenclatura de ID" }

{% alert warning %}
Evita compartir detalles sobre cómo creas los ID de usuario, ya que esto podría exponer a tu organización a ataques maliciosos o a la filtración de datos.
{% endalert %}