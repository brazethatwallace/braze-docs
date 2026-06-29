{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Borrar datos almacenados previamente {#wiping-previously-stored-data}

El SDK de Roku no incluye un método `wipeData`. Para producir un estado limpio funcionalmente equivalente a `wipeData()` en otros SDK de Braze, borra las cuatro secciones del registro de Braze y luego reinicializa el SDK.

El SDK de Roku de Braze persiste los datos en las siguientes secciones del registro:

| Sección | Contenido |
|---------|----------|
| `braze.section.device_id` | El UUID del dispositivo utilizado para identificar este dispositivo en Braze. |
| `braze.section.user_id` | El ID de usuario externo, si se ha establecido uno. |
| `braze.section.session` | El UUID de la sesión activa, la hora de inicio y la hora de finalización. |
| `braze.section.config` | Configuración del SDK en caché y datos de conmutadores de características. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wiping previously-stored data" }

### Paso 1: Borrar las secciones del registro {#step-1-clear-the-registry-sections}

Utiliza [`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md) para eliminar cada sección de Braze y luego llama a `Flush()` para persistir los cambios:

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

### Paso 2: Reinicializar el SDK de Braze {#step-2-re-initialize-the-braze-sdk}

Cuando [inicializas el SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) de nuevo, el SDK gestiona correctamente los datos faltantes del registro:

- La sección del ID de dispositivo está vacía, por lo que el SDK genera un nuevo UUID y trata el dispositivo como anónimo.
- La sección del ID de usuario está vacía, por lo que el SDK se establece de forma predeterminada como un usuario anónimo (una cadena vacía `""`).
- La sección de sesión está vacía, por lo que el SDK inicia una nueva sesión.
- La sección de configuración está vacía, por lo que el SDK vuelve a obtener la configuración del servidor.

{% alert note %}
El SDK de Roku no genera ninguna solicitud de eliminación del lado del servidor cuando borras el registro. Si también necesitas eliminar al usuario de Braze, envía una solicitud a [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) utilizando el `external_id` o `braze_id` del usuario.
{% endalert %}