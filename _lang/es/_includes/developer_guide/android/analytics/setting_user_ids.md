# Establecer ID de usuario {#setting-user-ids}

> Este artículo de referencia muestra cómo configurar ID de usuario en tu aplicación Android o FireOS, las convenciones sugeridas para nombrar ID de usuario y algunas buenas prácticas.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convención de nomenclatura de ID de usuario sugerida {#suggested-user-id-naming-convention}

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Asignar un ID de usuario {#assigning-a-user-id}

Debes realizar la siguiente llamada en cuanto se identifique al usuario (generalmente después de iniciar sesión) para establecer el ID de usuario:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**No llames a `changeUser()` cuando un usuario cierra la sesión. `changeUser()` solo se debe llamar cuando el usuario inicia sesión en la aplicación.** Si configuras `changeUser()` con un valor predeterminado estático, se asociará TODA la actividad del usuario con ese "usuario" predeterminado hasta que vuelva a iniciar sesión.
{% endalert %}

Además, te recomendamos **que no** cambies el ID de usuario cuando un usuario cierra la sesión, ya que esto hace que no puedas dirigirte al usuario que había iniciado sesión anteriormente con campañas de reactivación de la interacción. Si prevés varios usuarios en el mismo dispositivo, pero solo quieres dirigirte a uno de ellos cuando tu aplicación esté en estado desconectado, te recomendamos que hagas un seguimiento por separado del ID de usuario al que quieres dirigirte mientras está desconectado y que vuelvas a cambiar a ese ID de usuario como parte del proceso de cierre de sesión de tu aplicación.

Consulta la documentación de [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) para más información.

### Suscribirse a eventos de cambio de usuario {#subscribing-to-user-change-events}

Usa [`subscribeToChangeUserEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-change-user-events.html) para ejecutar lógica cuando tu aplicación cambia de usuario con `changeUser()`. Este método está disponible en el SDK de Android 40.0.0 y versiones posteriores.

La devolución de llamada del suscriptor se ejecuta cuando se cambia de usuario mediante `changeUser()` y recibe un `BrazeUserChangeEvent`. `BrazeUserChangeEvent` se dispara cuando el usuario actual ha cambiado o cuando el SDK acaba de inicializarse. El SDK puede disparar múltiples eventos para el mismo usuario, incluso cuando no se produce ninguna transición.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToChangeUserEvents(new IEventSubscriber<BrazeUserChangeEvent>() {
  @Override
  public void trigger(BrazeUserChangeEvent event) {
    // Add your app logic for user changes, such as refreshing user-scoped state.
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToChangeUserEvents { event ->
  // Add your app logic for user changes, such as refreshing user-scoped state.
}
```

{% endtab %}
{% endtabs %}

## Prácticas recomendadas y notas sobre la integración del ID de usuario {#user-id-integration-best-practices-and-notes}

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Alias de usuarios {#aliasing-users}

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}