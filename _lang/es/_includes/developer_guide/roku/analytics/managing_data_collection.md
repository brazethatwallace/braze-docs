{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Borrar datos almacenados previamente {#wiping-previously-stored-data}

El SDK or kit de desarrollo de software de Roku no incluye un método `wipeData`. Para producir un estado limpio funcionalmente equivalente a `wipeData()` en otros SDK or kit de desarrollo de software de Braze, borra las cuatro secciones del registro de Braze y luego reinicializa el SDK or kit de desarrollo de software.

El SDK or kit de desarrollo de software de Roku de Braze persiste datos en las siguientes secciones del registro:

| Sección | Contenido |
|---------|----------|
| `braze.section.device_id` | El UUID del dispositivo utilizado para identificar este dispositivo en Braze. |
| `braze.section.user_id` | El ID de usuario externo, si se ha establecido uno. |
| `braze.section.session` | El UUID de la sesión activa, la hora de inicio y la hora de finalización. |
| `braze.section.config` | Configuración del SDK or kit de desarrollo de software en caché y datos de conmutadores de características. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Borrar datos almacenados previamente" }

### Paso 1: Borrar las secciones del registro {#step-1-clear-the-registry-sections}

Usa [`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md) para eliminar cada sección de Braze y luego llama a `Flush()` para persistir los cambios:

```brightscript
sub WipeBrazeData()
    registry = CreateObject("roRegistry")
    registry.Delete("braze.section.device_id")
    registry.Delete("braze.section.user_id")
    registry.Delete("braze.section.session")
    registry.Delete("braze.section.config")
    registry.Flush()
end sub
```

### Paso 2: Reinicializar el SDK or kit de desarrollo de software de Braze {#step-2-re-initialize-the-braze-sdk}

Cuando [inicializas el SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) de nuevo, el SDK or kit de desarrollo de software gestiona correctamente los datos faltantes del registro:

- La sección del ID de dispositivo está vacía, por lo que el SDK or kit de desarrollo de software genera un nuevo UUID y trata el dispositivo como anónimo.
- La sección del ID de usuario está vacía, por lo que el SDK or kit de desarrollo de software se establece de forma predeterminada como un usuario anónimo (una cadena vacía `""`).
- La sección de sesión está vacía, por lo que el SDK or kit de desarrollo de software inicia una nueva sesión.
- La sección de configuración está vacía, por lo que el SDK or kit de desarrollo de software vuelve a obtener la configuración del servidor.

{% alert note %}
El SDK or kit de desarrollo de software de Roku no genera ninguna solicitud de eliminación del lado del servidor cuando borras el registro. Si también necesitas eliminar al usuario de Braze, envía una solicitud a [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) usando el `external_id` o `braze_id` del usuario.
{% endalert %}

## Cierre de sesión y cancelación del registro de push {#logout-and-unregister-push}

Esta característica aún no es compatible con el SDK or kit de desarrollo de software de Roku.