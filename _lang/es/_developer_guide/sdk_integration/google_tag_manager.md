---
nav_title: Google tag Administrador
article_title: Google Tag Administrador with the Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Learn how to initialize the Braze SDK using methods like runtime initialization, delayed initialization, or Google Tag Administrador."

---
## Acerca de Google Tag Administrador para Web {#google-tag-manager}

Google Tag Administrador (GTM) te permite añadir, eliminar y editar etiquetas de forma remota en tu sitio web sin necesidad de liberar código de producción ni recursos de ingeniería. Braze ofrece las siguientes plantillas para el SDK Web:

| Tipo de etiqueta | Caso de uso |
|--------|--------|
| Etiqueta de inicialización | Esta etiqueta te permite [integrar el SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sin necesidad de modificar el código de tu sitio. |
| Etiqueta de acción | Esta etiqueta te permite [crear Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [establecer atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) y [administrar la recopilación de datos]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acerca de Google Tag Administrador para Web" }

## Secuenciación de etiquetas para las etiquetas de acción de Braze {#tag-sequencing-for-braze-action-tags}

La etiqueta de inicialización de Braze debe activarse antes que cualquier etiqueta que llame a métodos del SDK de Braze (como `braze.getUser()`, `braze.logCustomEvent()` o `braze.logPurchase()`). Si estos métodos se activan antes de que el SDK esté inicializado, puedes encontrar errores como `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`.

Para configurar la secuenciación de etiquetas en Google Tag Administrador:

1. Abre la etiqueta que llama a métodos del SDK de Braze (como una etiqueta HTML personalizada o una etiqueta de acción de Braze).
2. Ve a **Advanced Settings** > **Tag Sequencing**.
3. Selecciona **A tag that fires before [this tag] is fired**.
4. Elige tu etiqueta **Braze Initialization**.

Esto garantiza que el SDK esté completamente cargado antes de que cualquier otra etiqueta intente llamar a métodos de Braze.

Para más detalles, consulta [Verificar la secuenciación de etiquetas para eventos personalizados]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Solución de problemas

### Sesiones del SDK Web atribuidas al usuario incorrecto

Si GTM activa las etiquetas de inicialización o de eventos de Braze antes de que tu aplicación identifique al usuario que ha iniciado sesión, las sesiones y eventos pueden asociarse al perfil incorrecto. Inicializa el SDK Web, llama a `changeUser()` con el `external_id` del usuario que ha iniciado sesión, y luego llama a `openSession()` antes de cualquier etiqueta que registre eventos o establezca atributos. Utiliza la secuenciación de etiquetas de GTM o los desencadenantes de consentimiento para que las etiquetas de Braze solo se ejecuten después de que tu flujo de autenticación se complete.

### Registro en consola del SDK Web con Shopify o instalaciones mediante etiqueta de script

La integración de la aplicación de Shopify carga el SDK Web con el registro en consola desactivado. Configura el registro en tu etiqueta de inicialización de GTM o en las opciones de `initialize()`. El panel de Braze no incluye un control de registro para estos cargadores.

Si los registros de Braze aparecen en la consola del navegador, elimina `enableLogging: true` de la etiqueta de inicialización de GTM o del HTML personalizado antes de publicar en producción. Después de la inicialización, utiliza `toggleLogging()` o el parámetro de URL `?brazeLogging=true`. Para ver todas las opciones del SDK Web, consulta [Registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

Si Braze no se inicializa o los eventos no aparecen como se espera, confirma que tu contenedor de GTM está publicado, que los desencadenantes y el orden de activación de las etiquetas están alineados con tu [ciclo de vida y estrategia de inicialización]({{site.baseurl}}/developer_guide/sdk_integration) del SDK, y que los dispositivos de prueba no están bloqueando los endpoints de Braze.

Para fallos de inicialización, verifica que la etiqueta de Braze o el proveedor de etiquetas personalizado reciba el `actionType` y los parámetros esperados (consulta las pestañas de Android, Swift y Web en esta página). Para el registro detallado mientras validas eventos activados por GTM, habilita el registro de depuración del SDK de tu plataforma como se describe en las guías de integración de plataforma enlazadas desde esas pestañas.