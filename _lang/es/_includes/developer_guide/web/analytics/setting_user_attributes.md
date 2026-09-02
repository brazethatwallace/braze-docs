{% multi_lang_include developer_guide/prerequisites/web.md %}

## Atributos predeterminados del usuario {#default-user-attributes}

### Métodos predefinidos {#predefined-methods}

Braze proporciona métodos predefinidos para configurar los siguientes atributos de usuario dentro de la [clase `User`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html):

- Nombre
- Apellido
- Idioma
- País
- Fecha de nacimiento
- Correo electrónico
- Género
- Ciudad natal
- Número de teléfono

### Configuración de atributos predeterminados {#setting-default-attributes}

{% tabs %}
{% tab usando métodos %}
Para establecer un atributo predeterminado para un usuario, llama al método `getUser()` en tu instancia de Braze para obtener una referencia al usuario actual de tu aplicación. Luego puedes llamar a los métodos para establecer un atributo de usuario.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Con Google Tag Manager, los atributos estándar del usuario (como el nombre de un usuario) deben registrarse de la misma manera que los atributos personalizados del usuario. Asegúrate de que los valores que estás pasando para los atributos estándar coincidan con el formato esperado especificado en la documentación de la [clase User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por ejemplo, el atributo de género puede aceptar cualquiera de los siguientes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Por lo tanto, para establecer el género de un usuario como femenino, crea una etiqueta HTML personalizada con el siguiente contenido:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Desactivar atributos predeterminados {#unsetting-default-attributes}

Puedes eliminar o desactivar un atributo de usuario a través del código de tu aplicación, una solicitud a la REST API o un paso de Canvas [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Para atributos de tipo array y booleano, usa `null`. Para otros tipos de datos, usa una cadena vacía (`""`).

Para desactivar un atributo predeterminado del usuario con el SDK Web, pasa `null` al método correspondiente. Por ejemplo:

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Atributos personalizados del usuario {#custom-user-attributes}

### Establecer atributos personalizados {#setting-custom-attributes}

{% tabs %}
{% tab usando métodos %}
Además de los métodos de atributos predeterminados del usuario, también puedes establecer [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attribute-data-types) para tus usuarios. Para las especificaciones completas de los métodos, consulta [nuestro JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
Para establecer un atributo personalizado con un valor `string`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
Para establecer un atributo personalizado con un valor `integer`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

{% endsubtab %}
{% subtab Date %}
Para establecer un atributo personalizado con un valor `date`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```

{% endsubtab %}
{% subtab Array %}

La cantidad predeterminada y máxima de elementos en un array es 500. Puedes actualizar la cantidad máxima de arrays en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Los arrays que excedan la cantidad máxima de elementos se truncan para contener la cantidad máxima de elementos.


Para establecer un atributo personalizado con un valor `array`:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Las fechas pasadas a Braze con este método deben ser objetos JavaScript Date.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Las claves y los valores de atributos personalizados solo pueden tener un máximo de 255 caracteres. Para obtener más información sobre los valores válidos de atributos personalizados, consulta la [documentación de referencia](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
Los atributos personalizados del usuario no están disponibles debido a una limitación en el lenguaje de scripting de Google Tag Manager. Para registrar atributos personalizados, crea una etiqueta HTML personalizada con el siguiente contenido:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
La plantilla GTM no admite propiedades anidadas en eventos ni compras. Puedes usar el HTML anterior para registrar cualquier evento o compra que requiera propiedades anidadas.
{% endalert %}
{% endtab %}
{% endtabs %}

### Desactivar atributos personalizados {#unsetting-custom-attributes}

Para desactivar un atributo personalizado, pasa `null` al método correspondiente.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Anidar atributos personalizados {#nesting-custom-attributes}

También puedes anidar propiedades dentro de atributos personalizados. En el siguiente ejemplo, se establece un objeto `favorite_book` con propiedades anidadas como atributo personalizado en el perfil de usuario. Para más detalles, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Usar la REST API {#using-the-rest-api}

También puedes utilizar nuestra REST API para establecer o desactivar atributos del usuario. Para obtener más información, consulta [Endpoints de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Configuración de suscripciones del usuario {#setting-user-subscriptions}

Para configurar una suscripción para tus usuarios (ya sea de correo electrónico o push), llama a las funciones `setEmailNotificationSubscriptionType()` o `setPushNotificationSubscriptionType()`, respectivamente. Ambas funciones toman el tipo `enum` `braze.User.NotificationSubscriptionTypes` como argumento. Este tipo tiene tres estados diferentes:

| Estado de suscripción | Definición |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Dado de baja o con exclusión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de suscripciones del usuario" }

Cuando un usuario se registra para push, el navegador le obliga a elegir entre permitir o bloquear las notificaciones; si elige permitir push, se establece como `OPTED_IN` de forma predeterminada.

Visita [Gestión de suscripciones de usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions) para obtener más información sobre la implementación de suscripciones y adhesiones voluntarias explícitas.

### Cancelar la suscripción de correo electrónico de un usuario {#unsubscribing-a-user-from-email}

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Cancelar la suscripción push de un usuario {#unsubscribing-a-user-from-push}

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
