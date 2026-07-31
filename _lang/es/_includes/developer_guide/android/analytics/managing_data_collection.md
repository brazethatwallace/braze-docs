## Cuestionario de privacidad de Google Play {#privacy-questionnaire}

A partir de abril de 2022, los desarrolladores de Android deberán cumplimentar el [formulario de seguridad de datos](https://support.google.com/googleplay/android-developer/answer/10787469) de Google Play para revelar las prácticas de privacidad y seguridad. Esta guía proporciona instrucciones sobre cómo rellenar este nuevo formulario con información sobre cómo gestiona Braze los datos de tu aplicación.

Como desarrollador de la aplicación, tú controlas qué datos envías a Braze. Los datos recibidos por Braze se procesan de acuerdo con tus instrucciones. Esto es lo que Google clasifica como [proveedor de servicios](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform).

{% alert important %}
Este artículo proporciona información sobre los datos que procesa el SDK de Braze en relación con el cuestionario de la sección de seguridad de Google. Este artículo no proporciona asesoramiento jurídico, por lo que te recomendamos que consultes con tu equipo jurídico antes de enviar cualquier información a Google.
{% endalert %}

### Preguntas {#questions}

| Preguntas | Respuestas para el SDK de Braze |
|---|---|
| ¿Recoge o comparte tu aplicación alguno de los tipos de datos de usuario requeridos? | Sí, el SDK para Android de Braze recopila datos según lo configure el desarrollador de la aplicación. |
| ¿Todos los datos de usuario recogidos por tu aplicación están encriptados en tránsito? | Sí. |
| ¿Proporcionas alguna forma de que los usuarios puedan solicitar que se eliminen sus datos? | Sí. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Preguntas" }

Para obtener más información sobre la gestión de las solicitudes de los usuarios sobre sus datos y su eliminación, consulta la [Información sobre la retención de datos de Braze]({{site.baseurl}}/api/data_retention).

### Recopilación de datos {#data-collection}

Los datos recopilados por Braze vienen determinados por tu integración específica y los datos de usuario que elijas recopilar. Para saber más sobre qué datos recopila Braze de manera predeterminada y cómo desactivar determinados atributos, consulta nuestras [opciones de recopilación de datos del SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

<table aria-label="Recopilación de datos" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Categoría</th>
            <th width="25%">Tipo de datos</th>
            <th width="50%">Uso de Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Ubicación</td>
            <td>Ubicación aproximada</td>
            <td rowspan="15">No se recopila de manera predeterminada.</td>
        </tr>
        <tr>
            <td>Ubicación precisa</td>
        </tr>
        <tr>
            <td rowspan="9">Información personal</td>
            <td>Nombre</td>
        </tr>
        <tr>
            <td>Dirección de correo electrónico</td>
        </tr>
        <tr>
            <td>ID de usuario</td>
        </tr>
        <tr>
            <td>Dirección</td>
        </tr>
        <tr>
            <td>Número de teléfono</td>
        </tr>
        <tr>
            <td>Raza y etnia</td>
        </tr>
        <tr>
            <td>Creencias políticas o religiosas</td>
        </tr>
        <tr>
            <td>Orientación sexual</td>
        </tr>
        <tr>
            <td>Otros datos</td>
        </tr>
        <tr>
            <td rowspan="4">Información financiera</td>
            <td>Información de pago del usuario</td>
        </tr>
        <tr>
            <td>Historial de compras</td>
        </tr>
        <tr>
            <td>Puntuación crediticia</td>
        </tr>
        <tr>
            <td>Otros datos financieros</td>
        </tr>
        <tr>
            <td rowspan="2">Salud y forma física</td>
            <td>Información de salud</td>
            <td rowspan="2">No se recopila de manera predeterminada.</td>
        </tr>
        <tr>
            <td>Información de acondicionamiento físico</td>
        </tr>
        <tr>
            <td rowspan="3">Mensajes</td>
            <td>Correos electrónicos</td>
            <td rowspan="2">No se recopila de manera predeterminada.</td>
        </tr>
        <tr>
            <td>SMS o MMS</td>
        </tr>
        <tr>
            <td>Otros mensajes dentro de la aplicación</td>
            <td>Si envías In-App Messages o notificaciones push a través de Braze, recopilamos información sobre cuándo los usuarios han abierto o leído estos mensajes.</td>
        </tr>
        <tr>
            <td rowspan="2">Fotos y videos</td>
            <td>Fotos</td>
            <td rowspan="8">No recopilado.</td>
        </tr>
        <tr>
            <td>Videos</td>
        </tr>
        <tr>
            <td rowspan="3">Archivos de audio</td>
            <td>Grabaciones de voz o sonido</td>
        </tr>
        <tr>
            <td>Archivos de música</td>
        </tr>
        <tr>
            <td>Otros archivos de audio</td>
        </tr>
        <tr>
            <td>Archivos y documentos</td>
            <td>Archivos y documentos</td>
        </tr>
        <tr>
            <td>Calendario</td>
            <td>Eventos del calendario</td>
        </tr>
        <tr>
            <td>Contactos</td>
            <td>Contactos</td>
        </tr>
        <tr>
            <td rowspan="5">Actividad de la aplicación</td>
            <td>Interacciones de la aplicación</td>
            <td>Braze recopila datos de actividad de la sesión de forma predeterminada. Todas las demás interacciones y actividades están determinadas por la integración personalizada de tu aplicación.</td>
        </tr>
        <tr>
            <td>Historial de búsqueda en la aplicación</td>
            <td>No recopilado.</td>
        </tr>
        <tr>
            <td>Aplicaciones instaladas</td>
            <td>No recopilado.</td>
        </tr>
        <tr>
            <td>Otros contenidos generados por usuarios</td>
            <td rowspan="2">No se recopila de manera predeterminada.</td>
        </tr>
        <tr>
            <td>Otras acciones</td>
        </tr>
        <tr>
            <td>Navegación web</td>
            <td>Historial de navegación web</td>
            <td>No recopilado.</td>
        </tr>
        <tr>
            <td rowspan="3">Información y rendimiento de la aplicación</td>
            <td>Registros de errores</td>
            <td>Braze recopila registros de errores que se producen en el SDK. Contienen el modelo de teléfono del usuario y el nivel de sistema operativo, junto con un ID de usuario específico de Braze.</td>
        </tr>
        <tr>
            <td>Diagnóstico</td>
            <td>No recopilado.</td>
        </tr>
        <tr>
            <td>Otros datos de rendimiento de la aplicación</td>
            <td>No recopilado.</td>
        </tr>
        <tr>
            <td>ID del dispositivo u otros ID</td>
            <td>ID del dispositivo u otros ID</td>
            <td>Braze genera un ID de dispositivo para diferenciar los dispositivos de los usuarios y comprueba si los mensajes se envían al dispositivo correcto previsto.</td>
        </tr>
    </tbody>
</table>

Para obtener más información sobre otros datos de dispositivo que Braze recopila y que pueden quedar fuera del ámbito de las directrices de seguridad de datos de Google Play, consulta nuestro [resumen de almacenamiento de Android]({{site.baseurl}}/developer_guide/storage/?tab=android) y nuestras [opciones de recopilación de datos del SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

## Desactivar el seguimiento de datos {#disabling-data-tracking}

Para desactivar la actividad de seguimiento de datos en el SDK de Android, utiliza el método [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Esto hará que se cancelen todas las conexiones de red, lo que significa que el SDK de Braze ya no enviará ningún dato a los servidores de Braze.

## Borrar datos almacenados previamente {#wiping-previously-stored-data}

Puedes utilizar el método [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) para borrar completamente todos los datos del lado del cliente almacenados en el dispositivo.

## Reanudación del seguimiento de datos {#resuming-data-tracking}

Para reanudar la recopilación de datos, puedes utilizar el método [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html). Ten en cuenta que esto no restaurará ningún dato previamente borrado.

## Cierre de sesión y cancelación del registro push {#logout-and-unregister-push}

El SDK de Braze proporciona métodos para dejar de segmentar un dispositivo cuando un usuario cancela su registro de notificaciones push o cierra sesión. Estos métodos eliminan los datos de registro push del usuario actual en el servidor de Braze y en el SDK, de modo que Braze ya no envía futuras Campaigns de notificaciones push a ese usuario.

### Cierre de sesión {#logout}

Cuando un usuario cierra sesión en una aplicación, llama al método `logout` del SDK para eliminar el registro push del dispositivo del usuario actual y realizar automáticamente acciones de limpieza en el SDK. El método `logout` realiza lo siguiente:

- Cancela el registro del token push del dispositivo del usuario actual en el servidor de Braze.
- Si la llamada de cancelación de registro tiene éxito, el SDK borra los datos del SDK almacenados localmente y desactiva el SDK.
- En caso de fallo, genera un error y un indicador `isRetriable` para permitir al integrador tomar medidas.

El siguiente ejemplo de devolución de llamada muestra el manejo de éxito y error de `logout`. Úsalo para flujos de cierre de sesión basados en devoluciones de llamada, y reemplaza el registro con tu lógica de reintento o reautenticación.

```kotlin
// Completion callback
Braze.getInstance(context).logout { result ->
  result
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

El siguiente ejemplo de corrutina muestra la API suspendida de `logout`. Úsalo en flujos basados en corrutinas y personaliza las ramas de éxito y fallo para tu aplicación.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).logout() }
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

#### Reactivar el seguimiento y push después de `logout` {#re-enable-tracking-and-push-after-logout}

Después de un `logout` exitoso, reactiva el SDK con [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html), y luego vuelve a registrarte para notificaciones con tu sistema operativo (SO) o proveedor de push siguiendo la [configuración push de Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

#### Evitar llamadas de cancelación de registro inmediatas {#avoid-immediate-unregister-calls}

Evita llamar a `logout` o `unregisterPush` directamente después de registrarte para notificaciones push con el SO o el proveedor de push. Debido al procesamiento asíncrono del servidor, esto puede, en raras ocasiones, volver a añadir el token push al usuario de Braze.

### Cancelar el registro push {#unregister-push}

Para dejar de enviar push a un dispositivo sin limpieza automatizada adicional, utiliza el método `unregisterPush`. Esto elimina el token push del dispositivo del usuario actual en el servidor de Braze y borra el token almacenado localmente.

El siguiente ejemplo de devolución de llamada muestra cómo manejar los resultados de `unregisterPush`. Úsalo cuando tu flujo esté basado en devoluciones de llamada, y reemplaza el registro con tu propia lógica de reintento.

```kotlin
// Completion callback
Braze.getInstance(context).unregisterPush { result ->
  result
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

El siguiente ejemplo de corrutina muestra la API suspendida de `unregisterPush`. Úsalo en flujos basados en corrutinas y personaliza las ramas de éxito y fallo para tu aplicación.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).unregisterPush() }
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

#### Volver a registrar push después de `unregisterPush` {#re-register-push-after-unregisterpush}

Después de llamar a `unregisterPush`, vuelve a registrarte para notificaciones con tu SO o proveedor de push siguiendo la [configuración push de Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) antes de enviar notificaciones push de Braze de nuevo.

#### Evitar llamadas de cancelación de registro inmediatas

Evita llamar a `logout` o `unregisterPush` directamente después de registrarte para notificaciones push con el SO o el proveedor de push. Debido al procesamiento asíncrono del servidor, esto puede, en raras ocasiones, volver a añadir el token push al usuario de Braze.