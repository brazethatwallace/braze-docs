---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "Este artículo de referencia describe la integración entre Braze y Copy Pastd, un creador de correo electrónico de arrastrar y soltar que envía Content Blocks y plantillas con Liquid directamente a tu espacio de trabajo de Braze."
page_type: partner
search_tag: Partner
---

# Copy Pastd

> [Copy Pastd](https://copypastd.com/) Building Blocks es un creador de correo electrónico de arrastrar y soltar que envía Content Blocks con Liquid y plantillas completas directamente a tu espacio de trabajo de Braze. Diseña una vez, sincroniza con Braze y reutiliza los mismos componentes en Campaigns, Canvas y flujos desencadenados sin tener que reconstruir el HTML cada vez.

_Esta integración es mantenida por Copy Pastd._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Copy Pastd te permite crear correos electrónicos en Building Blocks, un creador de correo electrónico alojado que produce resultados nativos de Braze con Liquid limpio, referencias a Content Blocks y plantillas que se insertan en cualquier Campaign o Canvas sin necesidad de traducción.

Puedes ensamblar un correo electrónico a partir de bloques reutilizables, enviarlo a Braze con un solo clic y confiar en que los mismos estilos de marca, componentes y contenido dinámico se renderizan de forma consistente en cada envío. El resultado son menos plantillas codificadas a mano, menos tiempo dedicado a crear y enviar correos electrónicos, y una biblioteca centralizada que se actualiza en todas partes cuando cambia.

## Requisitos previos {#prerequisites}

Los siguientes elementos son necesarios para utilizar esta integración:

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Copy Pastd | Obligatoria para usar Building Blocks. Regístrate en [copypastd.com](https://copypastd.com). Cada cliente obtiene un espacio de trabajo, una biblioteca de hojas de estilo, cinco puestos de creador y una biblioteca de bloques. |
| Clave de API REST de Braze para plantillas de correo electrónico | Una clave de API con los permisos `templates.email.create`, `templates.email.update` y `templates.email.list`.<br><br>Crea la clave en el dashboard de Braze desde **Settings** > **API Keys**. |
| Clave de API REST de Braze para Content Blocks | Una clave de API con los permisos `content_blocks.create`, `content_blocks.update`, `content_blocks.info` y `content_blocks.list`.<br><br>Crea la clave en el dashboard de Braze desde **Settings** > **API Keys**. |
| Clave de API REST de Braze para Catálogos (opcional) | Una clave de API con acceso de lectura a `catalogs.get`, `catalogs.get_item` y `catalogs.get_selections`. Solo es obligatoria si planeas vincular bloques a Catálogos de Braze. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión depende de la URL de Braze de tu instancia. Building Blocks selecciona el punto de conexión automáticamente en función del clúster que elijas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

* **Creación consistente con la marca a escala.** Aplica una hoja de estilo de Building Blocks a cada plantilla, y los colores, fuentes, estilos de botón y escala de relleno se renderizan de forma idéntica en cientos de correos electrónicos. Cuando la marca cambie, actualiza la hoja de estilo una vez y resincroniza para implementar la actualización en todos tus correos electrónicos a la vez.
* **Plantillas de producto vinculadas a Contenido conectado y Catálogos.** Vincula los campos de los bloques de correo electrónico directamente a tus puntos de conexión de [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) y [Catálogos de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/) desde dentro del creador. Reutiliza la misma plantilla para lanzamientos de nuevos productos, colecciones de temporada o actualizaciones de contenido sin tocar Liquid.
* **Producción de correo electrónico de autoservicio para especialistas en marketing no técnicos.** Compón un correo electrónico completo a partir de bloques aprobados, incluyendo personalización y lógica de Liquid, y envíalo a Braze para revisión sin necesidad de soporte de desarrolladores para escribir HTML o Liquid ni realizar control de calidad en ninguno de los dos.
* **Encabezados y pies de página centralizados, actualizados con un clic.** Crea un encabezado o pie de página una vez en el creador de Building Blocks y envíalo a Braze. Cada plantilla que lo referencia se mantiene sincronizada, de modo que un cambio de logotipo, una modificación de texto legal o un nuevo enlace social solo requiere una actualización dentro de Building Blocks para aplicarse en todos los correos electrónicos que ya están en Braze.
* **Contenido centralizado en todos los correos electrónicos.** Crea un hero, pie de página o tarjeta promocional una vez como bloque inteligente de Building Blocks. Actualízalo, sincroniza, y cada correo electrónico en Braze que lo referencia recoge el cambio en el siguiente envío. Los flujos de bienvenida, los boletines semanales y los recorridos desencadenados se mantienen actualizados sin editar cada Campaign.
* **Plantillas bloqueadas para que los colaboradores se autogestionen.** Crea plantillas, bloquea campos seleccionados y luego invita a otros equipos a crear sus propios correos electrónicos desde una interfaz de colaborador sin otorgarles acceso a herramientas orientadas al usuario.

## Integración {#integration}

### Paso 1: Conectar Building Blocks a Braze {#step-1-connect-building-blocks-to-braze}

{% alert note %}
Conectar Building Blocks a Braze es una configuración única. Una vez que tus credenciales se validen, Building Blocks las guarda para todas las sincronizaciones y envíos de plantillas futuros.
{% endalert %}

1. Inicia sesión en Building Blocks en [blocks.copypastd.com](https://blocks.copypastd.com), o selecciona **Login** en [copypastd.com](https://copypastd.com).
2. Desde el dashboard, selecciona **Set up your Braze connection**. (Esta píldora aparece para los administradores en el primer inicio de sesión y hasta que se complete. También puedes acceder a la página desde **Team Settings** > **Connect** > **Braze API Keys**.)
3. Selecciona tu clúster de Braze en el menú desplegable. El punto de conexión REST correspondiente se completa automáticamente.
4. Pega tu clave de API de plantillas, tu clave de API de Content Blocks y (opcionalmente) tu clave de API de Catálogos en los campos correspondientes.
5. Selecciona **Validate and save**. Building Blocks llama a Braze para confirmar que las claves funcionan y que los alcances de permisos son correctos. Si falta algo, un error en línea te muestra qué alcance es incorrecto.

### Paso 2: Sincronizar tu biblioteca con Braze {#step-2-sync-your-library-to-braze}

1. Una vez que las claves se validen, selecciona **Sync now** en el modal de configuración. (También puedes resincronizar en cualquier momento desde **Settings** > **Connect** > **Braze** > **Sync library**.) <br> Building Blocks envía tu hoja de estilo y bloques a tu espacio de trabajo de Braze como Content Blocks de Braze. Aparecen en Braze con nombres con el prefijo `CP_` (por ejemplo, `CP_Hero_1`) o `cp_` para hojas de estilo (por ejemplo, `cp_default_style`).
2. Una vez que la sincronización finalice, puedes enviar plantillas individuales desde el creador usando **Push to Braze**.

## Personalizar Building Blocks {#customize-building-blocks}

### Paso 1: Configurar tu hoja de estilo {#step-1-set-up-your-stylesheet}

1. En Building Blocks, navega a **Settings** > **Build** > **Stylesheets**.
2. Edita la hoja de estilo predeterminada o crea una nueva. Configura tu paleta de colores (24 colores con nombre), fuentes (compatible con Google Fonts), estilos de botón, estilos de enlace, radio y escala de relleno.
3. Selecciona **Save**. Building Blocks regenera el Liquid para cada bloque que usa esta hoja de estilo.
4. Selecciona **Sync now** para enviar los estilos actualizados a tu espacio de trabajo de Braze.

### Paso 2: Habilitar puntos de conexión de Contenido conectado (opcional) {#step-2-enable-connected-content-endpoints-optional}

1. En Building Blocks, navega a **Settings** > **Connect** > **Connected Content endpoints**.
2. Agrega la URL del punto de conexión, asígnale un nombre y guárdalo. Building Blocks admite un formato de respuesta de Google Sheets además del formato JSON estándar.
3. En el creador, vincula cualquier campo de texto, imagen o enlace a una variable de Contenido conectado desde el panel **Personalize**. El Liquid correcto {% raw %}`{% connected_content %}`{% endraw %} se genera en la exportación.

### Paso 3: Vincular a Catálogos de Braze (opcional) {#step-3-bind-to-braze-catalogs-optional}

1. En Building Blocks, navega a **Settings** > **Connect** > **Catalogs**. Building Blocks lee tu lista de catálogos usando la clave de API de Catálogos.
2. Abre un bloque compatible (por ejemplo, una cuadrícula de productos).
3. Selecciona un catálogo y una selección, luego mapea los campos del bloque a los atributos de los elementos del catálogo.
4. Envía la plantilla. Building Blocks emite el Liquid correcto {% raw %}`{% catalog_items %}`{% endraw %} y {% raw %}`{% catalog_selection_items %}`{% endraw %} para que Braze lo resuelva en el momento del envío.

### Paso 4: Agregar tus atributos personalizados de Braze (opcional) {#step-4-add-your-braze-custom-attributes-optional}

Building Blocks viene con los atributos de usuario predeterminados de Braze (`first_name`, `email`, `country`, etc.). Para vincular bloques a tus propios atributos personalizados, impórtalos a Building Blocks una vez y permanecerán disponibles en cada menú desplegable de **Personalize**.

1. En Building Blocks, navega a **Team Settings** > **Connect** > **Custom Attributes**.
2. Importa tus atributos personalizados usando uno de los siguientes métodos:
* **Importación masiva (recomendado).** En Braze, navega a **Data Settings** > **Custom Attributes** y selecciona **Export** (esquina superior derecha). Carga el CSV en Building Blocks.
* **Agregar atributos de uno en uno.** Escribe el nombre del atributo (por ejemplo, `loyalty_tier`) y selecciona **Add**. Este método es útil si solo estás agregando algunos atributos o si deseas agregar un nuevo atributo entre exportaciones de Braze.

Después de guardar, tus atributos personalizados aparecen en el menú desplegable **Personalize** del creador junto con los predeterminados. Al insertar uno, se renderiza el Liquid correcto {% raw %}`{{custom_attribute.${name}}}`{% endraw %} en la exportación, de modo que Braze resuelve el valor por destinatario en el momento del envío.

## Usar la integración {#use-the-integration}

### Paso 1: Enviar una plantilla a Braze {#step-1-push-a-template-to-braze}

1. Abre cualquier correo electrónico en el creador de Building Blocks.
2. Selecciona **Push to Braze** (esquina superior derecha).
3. Selecciona el espacio de trabajo y confirma. Building Blocks crea una plantilla de correo electrónico en Braze con el Liquid renderizado.

La plantilla aparece en Braze en **Templates & Media** > **Email Templates**, con el nombre del correo electrónico y la fecha seleccionada en la configuración del correo electrónico.

### Paso 2: Usar la plantilla en una Campaign o Canvas {#step-2-use-the-template-in-a-campaign-or-canvas}

1. En Braze, crea una nueva Campaign de correo electrónico o un paso en Canvas.
2. Selecciona **Templates** y elige la plantilla que Building Blocks envió.

La plantilla lleva cada referencia de Building Blocks (hoja de estilo, Content Blocks) como Liquid activo {% raw %}`{{content_blocks.${...}}}`{% endraw %}, de modo que las actualizaciones en Building Blocks se propagan sin necesidad de reimportar la plantilla.

### Paso 3: Actualizar contenido de forma centralizada {#step-3-update-content-centrally}

1. En Building Blocks, edita el bloque o la hoja de estilo correspondiente.
2. Selecciona **Sync** para enviar el Content Block actualizado de vuelta a Braze.

Cada correo electrónico en Braze que lo referencia (permanentes, desencadenados, flujos de bienvenida) recoge la nueva versión en el siguiente envío. No necesitas editar cada Campaign.

### Paso 4: Crear pools de contenido {#step-4-build-content-pools}

Los pools de contenido son tablas de filas de contenido que los correos electrónicos referencian en lugar de contener texto estático. Actualiza el pool en Building Blocks, y cada correo electrónico en Braze que lo usa sirve el nuevo contenido en el siguiente envío. Usa pools de contenido en cualquier lugar donde la misma pieza de contenido necesite mantenerse actualizada en muchos correos electrónicos, como boletines semanales, flujos de bienvenida, secuencias de recuperación, campañas de temporada o recorridos post-compra.

1. En Building Blocks, selecciona **Content** en la navegación principal.
2. Selecciona **New Pool**. Proporciona un nombre que describa lo que contiene (por ejemplo, Ofertas semanales, Catálogo de productos, Artículos de noticias).
3. Elige el tipo de bloque que alimenta el pool (por ejemplo, Hero, Grid, Card). Esto establece qué campos están disponibles en cada fila.
4. Agrega filas. Cada fila es una pieza de contenido. Completa los campos (titular, imagen, texto del CTA, enlace del CTA, etc.).
5. Establece el orden de prioridad arrastrando las filas hacia arriba o hacia abajo. Alterna cada fila entre activa o inactiva, y establece fechas de inicio y fin opcionales. En el momento del envío, gana la fila activa de mayor prioridad cuyas fechas sean válidas.
6. Haz clic en **Save**. Los bloques inteligentes ahora pueden referenciar este pool.

### Paso 5: Usar bloques inteligentes para renderizar contenido del pool en tus correos electrónicos {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

Un bloque inteligente es un bloque en el lienzo del creador que referencia uno o más pools de contenido en lugar de contener contenido estático. En el momento del envío, Braze renderiza la fila del pool que tiene la mayor prioridad, está activa y tiene fechas válidas. El Liquid exportado hace el trabajo. No se necesita configuración adicional en Braze.

1. En Building Blocks, arrastra un bloque inteligente al lienzo (cualquier tipo de bloque que tenga un pool correspondiente).
2. En el panel de propiedades, abre el editor de cascada.
3. Agrega uno o más pools de contenido en orden de prioridad. Esta es la cascada: el primer pool con una fila activa y con fechas válidas se renderiza. Si no tiene nada en vivo, el bloque inteligente pasa al siguiente pool, y luego al siguiente. Un patrón común es Venta flash > Ofertas semanales > Favoritos permanentes, de modo que siempre hay algo disponible.
4. Envía la plantilla a Braze. El Liquid exportado lleva la cascada completa, de modo que Braze evalúa la prioridad del pool y las fechas en cada envío.

A partir de ahora, actualizas el pool, no el correo electrónico. Los flujos desencadenados, los boletines permanentes y las campañas de temporada se mantienen actualizados siempre que el pool esté actualizado.

Encuentra tus plantillas de Building Blocks cargadas en Braze en **Templates & Media** > **Email Templates**. Las hojas de estilo y bloques sincronizados aparecen en **Templates & Media** > **Content Blocks**.

## Consideraciones {#considerations}

- **Una instancia de Braze por espacio de equipo de Building Blocks.** Cada equipo de Building Blocks se conecta a una sola instancia de Braze. Los clientes que ejecutan múltiples espacios de trabajo (marcas, regiones o entornos separados) pueden agregarlos al mismo equipo, lo que permite compartir bloques.
- **Los permisos de las claves de API tienen alcances separados.** Las claves de plantillas y las claves de Content Blocks se mantienen separadas. La validación falla rápidamente si a una clave le falta un alcance requerido, de modo que sabes exactamente qué permiso agregar en Braze.
- **Los nombres de Content Blocks tienen espacio de nombres.** Building Blocks envía Content Blocks con los prefijos `CP_` (bloques) y `cp_` (hojas de estilo) para evitar colisiones con Content Blocks creados directamente en Braze.
- **Las ediciones de hojas de estilo actualizan todos los correos electrónicos.** Las hojas de estilo se renderizan como un único Content Block de Braze referenciado por cada plantilla. Un cambio en Building Blocks actualiza cada correo electrónico en Braze que lo usa, incluidos los que ya están planificados. Prueba los cambios de hoja de estilo en una plantilla borrador antes de sincronizar.
- **La vinculación de catálogos es de solo lectura.** Building Blocks lee los catálogos para poblar la interfaz de vinculación. No escribe en los Catálogos de Braze. Toda la gestión de catálogos sigue ocurriendo en el dashboard de Braze.
- **Límites de velocidad y reintentos.** Todas las solicitudes salientes respetan los límites de velocidad de Braze, con retirada exponencial, jitter y manejo de Retry-After. Se envía un encabezado `User-Agent: partner-CopyPastd` en cada llamada para la atribución del socio.
- **No se transmiten datos de usuario.** Building Blocks es una herramienta de creación de contenido. No envía atributos de usuario, eventos, compras ni datos de segmentos a Braze, y no consume puntos de datos de Braze.

## Solución de problemas {#troubleshooting}

- **La validación de la clave de API falla.** Verifica que cada clave tenga los permisos exactos listados en los requisitos previos. Los alcances de plantillas y Content Blocks se verifican por separado. Si regeneras una clave en Braze, pega el nuevo valor en Building Blocks y vuelve a validar.
- **Discrepancia en el punto de conexión REST.** Las claves de plantillas y Content Blocks deben provenir del mismo espacio de trabajo de Braze, y el punto de conexión REST debe coincidir con el clúster. El menú desplegable de Building Blocks lo configura por ti, así que verifica la selección del clúster si la validación falla.
- **Push to Braze devuelve un error.** Abre **Settings** > **Build** > **Activity log** para ver el último intento de sincronización y la respuesta que Braze devolvió. La mayoría de los fallos están relacionados con permisos (alcance faltante) o cuotas (límite de velocidad, reintentado automáticamente).
- **El Content Block no se actualiza en Braze.** Activa una resincronización manual desde **Settings** > **Connect** > **Braze** > **Sync library**. Building Blocks realiza una comparación e intercambio, por lo que los bloques sin cambios se omiten.
- **La plantilla referencia un Content Block que aún no existe en Braze.** Envía primero las dependencias (hoja de estilo, bloques inteligentes) usando **Sync library**, luego envía la plantilla.
- **Para todo lo demás.** Ponte en contacto con Copy Pastd en [help@copypastd.com](mailto:help@copypastd.com). Incluye el nombre de tu equipo y la hora de la acción fallida para que Copy Pastd pueda consultar el registro de actividad correspondiente.