---
nav_title: Bynder
article_title: Bynder
description: "Este artículo de referencia describe la asociación entre Braze y Bynder, una plataforma de gestión de activos digitales (DAM) que te permite buscar e insertar URL de activos aprobados en Campaigns y Canvas de Braze a través de la extensión Universal Compact View de Chrome."
alias: /partners/bynder/
page_type: partner
search_tag: Partner
---

# Bynder

> [Bynder](https://www.bynder.com) es una plataforma de gestión de activos digitales (DAM) que ayuda a los clientes a crear, gestionar, encontrar y distribuir activos digitales aprobados (imágenes, videos y otros creativos) desde una única fuente de verdad. Cuando se integra con Braze, la extensión Universal Compact View (UCV) de Google Chrome de Bynder permite a los especialistas en marketing buscar y seleccionar activos de Bynder sin salir del panel de Braze. Inserta enlaces a esos activos directamente en Campaigns y Canvas.

_Esta integración es mantenida por Bynder._

## Acerca de esta integración {#about-this-integration}

Conectar Bynder a Braze a través de la extensión UCV de Chrome da a los especialistas en marketing acceso a su biblioteca de activos de Bynder dentro del editor de contenido de Braze. Abre la Universal Compact View como una superposición en cualquier pestaña del navegador, incluido el panel de Braze. Busca o filtra el creativo adecuado y luego pega la URL del activo en tu Campaign.

Esto mantiene las Campaigns de Braze alineadas con la única fuente de verdad de Bynder: los permisos correctos, la versión de archivo más actual y los derechos de uso correctos.

## Ejemplos {#use-cases}

- Los especialistas en marketing que crean un correo electrónico, un mensaje dentro de la aplicación o un Content Block en Braze pueden insertar imágenes principales, banners o enlaces de video promocional obtenidos directamente de Bynder para que las campañas utilicen la última versión aprobada de un activo.
- Los administradores de campañas pueden usar la barra de búsqueda y filtro de la Universal Compact View para localizar creativos aprobados regionales o localizados para un segmento de audiencia específico antes de añadirlo a un paso en Canvas.
- Los equipos creativos pueden aplicar la transformación dinámica de activos de Bynder para redimensionar o reformatear un activo para un canal específico antes de copiar el enlace en Braze. Por ejemplo, usa un recorte compacto para una notificación push o un banner de tamaño completo para correo electrónico.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Una cuenta de Bynder | Una cuenta de Bynder con acceso a los activos DAM que deseas referenciar en Braze. |
| Extensión Universal Compact View (UCV) de Bynder para Chrome | Instalada desde la Chrome Web Store y conectada a tu portal de Bynder. Disponible solo para Google Chrome. |
| Activos y derivados públicos | Cualquier activo, y el derivado específico al que planeas enlazar, debe estar marcado como público en Bynder para que su URL se resuelva correctamente para los destinatarios del mensaje. |
| Una cuenta de Braze | Acceso al canal de mensajería (correo electrónico, Content Block, mensaje dentro de la aplicación, Canvas, etc.) donde se utiliza el activo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Instalar y conectar la extensión UCV de Bynder para Chrome {#step-1-install-and-connect-the-bynder-ucv-chrome-extension}

1. Ve a la [extensión UCV de Bynder](https://chromewebstore.google.com/detail/bynders-universal-compact/ilghhphnbdblpbdhmbdfiaidganphema) en la Chrome Web Store.
2. Haz clic en **Añadir a Chrome**, revisa los permisos solicitados y luego haz clic en **Añadir extensión**.
3. Desde la barra de herramientas de Chrome, selecciona el icono de Bynder UCV (fíjalo a la barra de herramientas primero si aún no es visible).
4. Introduce el dominio de tu portal de Bynder (sin `https://`) y luego haz clic en **Connect**.
5. En la ventana que se abre, inicia sesión en tu portal de Bynder con tus credenciales habituales.

### Paso 2: Buscar y seleccionar un activo de Bynder {#step-2-search-for-and-select-a-bynder-asset}

1. Con la extensión conectada, abre la Universal Compact View desde cualquier pestaña del navegador, incluido tu panel de Braze.
2. Usa el filtro inteligente y la barra de búsqueda para localizar la imagen, video, documento o activo de audio que necesitas.
3. Selecciona el activo y luego selecciona el derivado (o el archivo original, si es público) que deseas usar.
4. Haz clic en **Add Asset** para copiar la URL del activo seleccionado a tu portapapeles.

### Paso 3: Añadir la URL del activo a tu Campaign de Braze {#step-3-add-the-asset-url-to-your-braze-campaign}

1. En Braze, abre el correo electrónico, Content Block, mensaje dentro de la aplicación o paso en Canvas donde deseas añadir el activo.
2. Pega la URL del activo de Bynder copiada en el campo correspondiente. Por ejemplo, usa una etiqueta `<img src="">` o el campo de URL de imagen de un Content Block.

   Ejemplo de URL de imagen:

   ```html
   <img src="https://your-portal.bynder.com/m/abcdef123456/original/campaign-banner.jpg" alt="Summer Campaign">
   ```

{: start="3"}
3. Guarda y previsualiza tu mensaje para confirmar que el activo se muestra como se espera.

## Consejos {#tips}

### Aplicar transformaciones dinámicas de activos antes de copiar la URL {#apply-dynamic-asset-transformations-before-copying-the-url}

Dentro de la Universal Compact View, usa las opciones de transformación disponibles para redimensionar, recortar o reformatear un activo para el canal al que te diriges. Esto evita subir versiones recortadas por separado a Bynder.

### Generar URL de derivados específicas por canal {#generate-channel-specific-derivative-urls}

Cada transformación o derivado produce su propia URL distinta. Genera una versión dimensionada para correo electrónico, otra para push y otra para mensajes dentro de la aplicación, y luego pega cada una en el canal de Braze o paso en Canvas correspondiente.

### Reutilizar una URL de activo en varios canales {#reuse-one-asset-url-across-channels}

Dado que un enlace pegado apunta a un activo y derivado específico en Bynder, el mismo formato de URL puede reutilizarse en correo electrónico, Content Blocks, mensajes dentro de la aplicación y pasos en Canvas. Esto mantiene la coherencia creativa en todos los lugares donde se usa en una campaña.

### Actualizar el activo de origen sin editar tus campañas {#update-the-source-asset-without-editing-your-campaigns}

Si el archivo subyacente en Bynder se reemplaza manteniendo la misma configuración de activo público y derivado, cualquier mensaje en vivo de Braze que haga referencia a esa URL refleja automáticamente la actualización. No necesitas editar la campaña en sí.

## Consideraciones {#considerations}

- La extensión UCV de Bynder para Chrome solo está disponible para Google Chrome. En otros navegadores, copia las URL de activos directamente desde el portal completo de Bynder.
- Solo los activos (y los derivados específicos a los que se enlaza) que están marcados como públicos en Bynder se resuelven cuando se pegan en Braze. Los activos privados devuelven un error de acceso a los destinatarios.
- Si las ventanas emergentes no están permitidas o el portal ya está abierto en otra pestaña, la ventana de inicio de sesión puede no abrirse correctamente. Antes de conectar, confirma que las ventanas emergentes están permitidas y cierra cualquier otra pestaña donde el portal esté abierto.
- El acceso dentro de la extensión sigue los permisos existentes del usuario de la empresa en el DAM de Bynder, por lo que solo ve y puede seleccionar los activos a los que ya está autorizado a acceder.

## Solución de problemas {#troubleshooting}

| Problema | Resolución |
| --- | --- |
| El icono de la extensión no es visible | Fija la extensión UCV de Bynder a la barra de herramientas de Chrome desde el menú de extensiones. |
| **Connect** no abre una ventana de inicio de sesión | Confirma que las ventanas emergentes de Chrome están permitidas para el dominio de tu portal de Bynder y cierra cualquier otra pestaña donde el portal ya esté abierto. |
| La URL del activo no se muestra en Braze | Confirma que el activo y el derivado específico utilizado están marcados como públicos en el portal de Bynder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

Para más información, consulta la [documentación de Universal Compact View](https://support.bynder.com/hc/en-us/sections/16936397091858-Universal-Compact-View-UCV) de Bynder o contacta con el soporte de Bynder.