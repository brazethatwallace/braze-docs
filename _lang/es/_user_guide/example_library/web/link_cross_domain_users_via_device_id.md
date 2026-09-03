---
nav_title: Vincular usuarios del SDK Web entre dominios
article_title: Vincular usuarios del SDK Web entre dominios mediante el ID de dispositivo
page_order: 1
page_type: reference
description: "Pasa el ID de dispositivo del SDK Web de Braze desde el sitio de marketing de Kitchenerie a un dominio de tienda independiente para que la actividad anónima comparta un único perfil de usuario."
---

# Vincular usuarios del SDK Web entre dominios mediante el ID de dispositivo {#link-cross-domain-web-sdk-users-through-device-id}

> Pasa el ID de dispositivo del SDK Web de Braze a través de la URL de destino cuando dos dominios no pueden compartir cookies, de modo que las sesiones anónimas en ambos sitios se asignen al mismo perfil de usuario de Braze.

## Acerca de este ejemplo {#about-this-example}

Kitchenerie, un comercio minorista ficticio de artículos de cocina, aloja un sitio de marketing (`kitchenerie.com`) y una tienda (`kitchenerie.shop`). Cada dominio tiene su propia integración del SDK Web de Braze. Las cookies del navegador no se comparten entre dominios, por lo que Braze asigna ID de dispositivo independientes —y perfiles anónimos separados— cuando el mismo usuario pasa del sitio de marketing a la tienda.

Este patrón:

1. Lee el ID de dispositivo en el dominio de origen con `getDeviceId` después de la inicialización del SDK
2. Lo añade a los enlaces salientes como parámetro de consulta (por ejemplo, `brazeDeviceId`)
3. En el dominio de destino, lee ese parámetro y lo pasa a `braze.initialize` a través de la opción `deviceId`

La transferencia es más importante para los usuarios anónimos. Después de que el usuario inicia sesión en la tienda, `changeUser` con un `external_id` se convierte en el identificador duradero entre dispositivos. Consulta [Establecer ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).

Ambos dominios deben usar la misma clave de API del espacio de trabajo de Braze y el mismo punto final de SDK para que los eventos se registren en un solo perfil.

## Consideraciones {#considerations}

- El ID de dispositivo es por navegador. Este patrón no vincula la actividad entre diferentes navegadores, dispositivos o perfiles. Usa `external_id` a través de `changeUser` para la identidad autenticada entre dispositivos.
- Recupera el ID de dispositivo solo después de que el SDK Web se haya inicializado en el dominio de origen. Llamar a `getDeviceId` antes de `initialize` no devuelve un valor.
- El SDK Web lee `deviceId` una sola vez en `initialize`. No existe un `setDeviceId` posterior a la inicialización que cambie el ID de dispositivo activo. Lee el parámetro de la URL en el dominio de destino antes de llamar a `initialize`.
- Las visitas directas, los marcadores o los referidos de terceros a la tienda sin `brazeDeviceId` deben recurrir a la asignación predeterminada de ID de dispositivo, lo cual es esperado cuando no hay un ID del dominio de origen que heredar.
- Los parámetros de consulta aparecen en el historial del navegador y en los registros del servidor.
- Los parámetros de consulta pueden filtrarse a través de las cabeceras de referencia. El ID de dispositivo no es PII por sí solo, pero elimina el parámetro después de consumirlo si tu equipo de privacidad lo requiere (consulta el paso 2).
- Prueba de extremo a extremo. Confirma que los eventos del dominio 2 usan el ID de dispositivo esperado con la inspección de red.
- Adapta los nombres de host, los selectores de enlaces y el manejo de errores a tu sitio. Prueba en tu entorno de desarrollo antes de pasar a producción.

## Configuración {#setup}

### Paso 1: Añadir el ID de dispositivo a los enlaces entre dominios en el dominio de origen {#step-1-append-the-device-id-to-cross-domain-links-on-the-source-domain}

En `kitchenerie.com` (dominio 1), inicializa el SDK Web como de costumbre y luego añade el ID de dispositivo actual a los enlaces que apuntan a `kitchenerie.shop` (dominio 2).

Elige un nombre de parámetro de consulta que no colisione con tu sitio (este ejemplo usa `brazeDeviceId`). La misma idea se aplica a enlaces renderizados en el servidor, navegación del lado del cliente o valores `src` de iframe que controles.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});
braze.openSession();

const destinationHost = "kitchenerie.shop";

braze.getDeviceId(function (deviceId) {
  if (!deviceId) {
    return;
  }

  const links = document.querySelectorAll('a[href*="' + destinationHost + '"]');

  links.forEach(function (link) {
    try {
      const url = new URL(link.href);
      url.searchParams.set("brazeDeviceId", deviceId);
      link.href = url.toString();
    } catch (e) {
      // Skip malformed hrefs (for example, javascript:, mailto:, or unparsable relative paths).
    }
  });
});
```

Si tu versión del SDK expone `getDeviceId` de forma síncrona (sin devolución de llamada), llámalo después de la inicialización:

```javascript
const deviceId = braze.getDeviceId();
```

Consulta [Guía del repositorio del SDK Web — Obtener ID de dispositivo]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#get-device-id) y [Opciones de inicialización — `deviceId`]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#initialization-options).

### Paso 2: Leer el ID de dispositivo e inicializar el SDK Web en el dominio de destino {#step-2-read-the-device-id-and-initialize-the-web-sdk-on-the-destination-domain}

En `kitchenerie.shop` (dominio 2), lee `brazeDeviceId` de la cadena de consulta antes de `initialize` y pásalo en las opciones de inicialización cuando esté presente.

```javascript
import * as braze from "@braze/web-sdk";

const urlParams = new URLSearchParams(window.location.search);
const passedDeviceId = urlParams.get("brazeDeviceId");

const initOptions = {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
};

if (passedDeviceId) {
  initOptions.deviceId = passedDeviceId;
}

braze.initialize("YOUR-API-KEY-HERE", initOptions);
braze.openSession();

// Optional: remove the parameter from the visible URL after consumption.
if (passedDeviceId) {
  const cleanUrl = new URL(window.location.href);
  cleanUrl.searchParams.delete("brazeDeviceId");
  window.history.replaceState({}, document.title, cleanUrl.toString());
}
```

Cuando el usuario inicie sesión, llama a `changeUser` con su `external_id` para que la actividad futura se vincule al perfil identificado.

### Paso 3: Verificar la transferencia {#step-3-verify-the-handoff}

1. Abre el dominio 1 en un navegador en el que no hayas iniciado sesión.
2. Sigue un enlace entre dominios al dominio 2.
3. En la pestaña de red del navegador, confirma que el dominio 2 envía eventos con el mismo ID de dispositivo que usó el dominio 1.
4. Repite con una visita directa al dominio 2 (sin parámetro de consulta) y confirma que se asigna un nuevo ID de dispositivo.

## Artículos relacionados {#related-articles}

- [Guía del repositorio del SDK Web]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)
- [Integración multidominio para el SDK Web de Braze]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)
- [Establecer ID de usuario a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)
- [Usuarios anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)
- [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Almacenamiento del SDK Web]({{site.baseurl}}/developer_guide/storage)