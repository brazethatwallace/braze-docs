---
nav_title: NiftyImages
article_title: NiftyImages
description: "Aprende a conectar NiftyImages con Braze para crear elementos visuales dinámicos y personalizados, sincronizar propiedades de contacto y publicar activos como Content Blocks reutilizables."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com) ayuda a los clientes de Braze a crear contenido visual personalizado y en tiempo real para correo electrónico, móvil y mensajería dentro de la aplicación. Al conectar datos en vivo de clientes, productos y negocios con imágenes y contenido dinámicos, las marcas pueden ofrecer experiencias oportunas y relevantes, como temporizadores de cuenta atrás, recomendaciones personalizadas, mensajería localizada, actualizaciones de inventario y ofertas promocionales que impulsan la interacción y las conversiones.

_Esta integración está mantenida por NiftyImages._

## Acerca de la integración {#about-the-integration}

La integración de NiftyImages para Braze te ayuda a crear elementos visuales dinámicos y personalizados utilizando datos de contacto de Braze. Los equipos pueden crear activos como imágenes personalizadas, temporizadores de cuenta atrás, mapas, calendarios, elementos visuales de fidelización y más, y luego publicarlos como [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) reutilizables de Braze para usarlos en Campaigns y Canvas. Esto ahorra tiempo, reduce errores y simplifica la gestión de contenido personalizado.

## Casos de uso {#use-cases}

Puedes usar NiftyImages para:

- **Personalizar imágenes:** Crea imágenes que incluyan el nombre de cada cliente, estado de fidelización, saldo de recompensas, ubicación, preferencia de producto, nivel de membresía, detalles de cuenta u otras propiedades de contacto de Braze.
- **Añadir temporizadores de cuenta atrás:** Añade temporizadores de cuenta atrás en tiempo real para ventas, lanzamientos de productos, eventos, ofertas por tiempo limitado, citas, plazos de incorporación y fechas de vencimiento personalizadas.
- **Mostrar mapas dinámicos:** Muestra la tienda más cercana, ubicación de evento, área de servicio, concesionario, club, sucursal o punto de recogida basándote en los datos de ubicación del cliente o en las propiedades de contacto de Braze.
- **Mostrar calendarios:** Muestra fechas personalizadas, eventos, citas, periodos de renovación, momentos de campaña o hitos del cliente directamente dentro de los elementos visuales de la campaña.
- **Ejecutar encuestas en directo:** Añade encuestas interactivas a las campañas y muestra resultados actualizados en tiempo real después de que los clientes voten.
- **Crear rasca y gana:** Crea experiencias gamificadas de rasca y gana que revelen una recompensa, descuento, oferta, imagen o mensaje personalizado.
- **Visualizar datos de fidelización:** Convierte los datos de clientes en barras de progreso, resúmenes de cuenta, elementos visuales de fidelización, tablas y gráficos personalizados para cada destinatario.
- **Aplicar contenido basado en reglas:** Muestra diferentes elementos visuales según la hora, ubicación, dispositivo, datos del cliente, segmento de audiencia o lógica de campaña.
- **Reutilizar contenido dinámico:** Publica activos de NiftyImages completados en Content Blocks de Braze para que los equipos puedan reutilizarlos en correos electrónicos de marketing, plantillas, campañas y activos de marca compartidos.

## Requisitos previos {#prerequisites}

Antes de empezar, confirma que tienes lo siguiente:

| Requisitos | Descripción |
| ---------- | ----------- |
| Cuenta de NiftyImages | Se requiere una [cuenta de NiftyImages](https://niftyimages.com/Signup) para crear y gestionar imágenes personalizadas, temporizadores, mapas, calendarios, rasca y gana, gráficos y otros elementos visuales dinámicos. |
| Cuenta de Braze | Se requiere una cuenta de Braze para usar NiftyImages dentro de Campaigns de Braze, Canvas, plantillas de correo electrónico y canales de mensajería. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `custom_attributes.get` y `content_blocks.create`.<br><br>Se puede crear en el dashboard de Braze desde **Configuración** > **API e identificadores**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/api/basics#endpoints). Tu punto de conexión depende de la URL de Braze para tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Conecta tu cuenta de Braze en NiftyImages para sincronizar propiedades de contacto y publicar activos en Content Blocks de Braze.

### Paso 1: Abre las integraciones en NiftyImages {#step-1-open-integrations-in-niftyimages}

1. En NiftyImages, ve a **Settings** > **Integrations**.
2. Selecciona **Braze**.
3. Selecciona **Connect Braze**.

### Paso 2: Crea tu clave de API REST de Braze {#step-2-create-your-braze-rest-api-key}

1. En Braze, ve a **Configuración** > **API e identificadores**.
2. Crea o selecciona una clave de API REST para la integración de NiftyImages.
3. En **Custom Attributes**, selecciona `custom_attributes.get`.
4. En **Content Blocks**, selecciona `content_blocks.create`.
5. Guarda la clave de API, luego copia la clave de API REST y tu [punto de conexión REST]({{site.baseurl}}/api/basics#endpoints).

### Paso 3: Conecta tu cuenta de Braze en NiftyImages {#step-3-connect-your-braze-account-in-niftyimages}

1. Vuelve a la pantalla de integración de Braze en NiftyImages.
2. Pega la clave de API REST de Braze.
3. Introduce tu punto de conexión REST de Braze.
4. Confirma la conexión.
5. Verifica que tu cuenta de Braze aparezca en **Connected Braze accounts** con un estado **Active** o **Connected**.

Puedes conectar varias cuentas de Braze si es necesario, lo cual es útil para agencias, equipos multimarca u organizaciones que gestionan varias instancias de Braze.

## Personalizar activos en NiftyImages {#customize-assets-in-niftyimages}

Después de conectar Braze, usa la sincronización de variables de contacto y la publicación de Content Blocks para gestionar elementos visuales personalizados.

### Usar la sincronización de variables de contacto {#use-contact-variable-sync}

La sincronización de variables de contacto te permite usar propiedades de contacto de Braze existentes directamente dentro de NiftyImages sin necesidad de escribir o recrear etiquetas merge manualmente.

1. Crea o edita una imagen personalizada u otro activo de NiftyImages.
2. Abre el SELECTOR de etiquetas merge o personalización.
3. Selecciona **Pick from connected integrations** y luego elige las propiedades de Braze que quieras usar.
4. Añade esos valores a capas de texto, imagen, temporizador, mapa, gráfico, calendario o contenido dinámico.
5. Guarda la imagen.

Las imágenes guardadas que usan variables de Braze incluyen automáticamente esos valores de personalización en la URL de la imagen de NiftyImages.

### Publicar en Content Blocks de Braze {#publish-to-braze-content-blocks}

1. Finaliza tu activo de NiftyImages.
2. Selecciona **Send to Braze**.

## Usar NiftyImages en Braze {#use-niftyimages-in-braze}

Usa los Content Blocks publicados en plantillas de correo electrónico, Campaigns y Canvas de Braze.

### Añadir un activo de NiftyImages a un correo electrónico de Braze {#add-a-niftyimages-asset-to-a-braze-email}

1. Abre una plantilla de correo electrónico, una Campaign o un mensaje de correo electrónico de Canvas en Braze.
2. En el editor de mensajes, abre el menú de personalización y selecciona **Content Blocks** como tipo de personalización.
3. Selecciona el Content Block de NiftyImages que publicaste desde NiftyImages.

### Reutilizar activos de NiftyImages en Braze {#reuse-niftyimages-assets-across-braze}

1. Usa el Content Block publicado en correos electrónicos de marketing, plantillas de correo electrónico, campañas, activos de marca compartidos y flujos automatizados.
2. Cuando un activo de NiftyImages usa variables dinámicas, Braze pasa los valores de contacto según el mensaje y el canal.
3. Actualiza el activo de origen en NiftyImages cuando necesites cambios creativos.

### Desconectar una cuenta de Braze {#disconnect-a-braze-account}

1. Vuelve a **Settings** > **Integrations** en NiftyImages.
2. Abre la página de conexión de Braze.
3. Selecciona el icono de quitar o desconectar de la cuenta que quieras eliminar.
4. Confirma la desconexión.

## Consideraciones {#considerations}

- **Permisos de la REST API:** La clave de API REST de Braze debe incluir `custom_attributes.get` para la sincronización de propiedades de contacto y `content_blocks.create` para publicar activos en Content Blocks de Braze.
- **Disponibilidad de propiedades de contacto:** Solo las propiedades de contacto disponibles para la cuenta de Braze conectada pueden sincronizarse en NiftyImages.
- **Valores alternativos:** Usa valores alternativos al crear elementos visuales personalizados para que cada cliente vea una imagen pulida incluso cuando falta una propiedad de contacto.
- **Content Blocks reutilizables:** Publicar en Content Blocks de Braze ayuda a los equipos a evitar copiar y pegar HTML manualmente, reducir errores de etiquetas merge y reutilizar activos en campañas y plantillas.
- **Varias cuentas de Braze:** NiftyImages admite varias cuentas de Braze conectadas, lo cual es útil para agencias, equipos multimarca y equipos que gestionan varias instancias de Braze.
- **Pruebas:** Prueba el mensaje final de Braze con perfiles de clientes de muestra antes de lanzar una Campaign o un Canvas.

## Solución de problemas {#troubleshooting}

Consulta la siguiente tabla si experimentas problemas con la integración de NiftyImages.

| Problema | Resolución |
| -------- | ---------- |
| La cuenta de Braze no se conecta | Confirma que la clave de API REST sea válida, que el punto de conexión REST sea correcto y que la clave incluya los permisos necesarios. |
| Las propiedades de contacto de Braze no aparecen en NiftyImages | Confirma que la clave de API incluya `custom_attributes.get`. Luego actualiza la conexión de Braze dentro de NiftyImages. |
| El activo no se publica en Content Blocks de Braze | Confirma que la clave de API incluya `content_blocks.create` y que la cuenta de Braze conectada permita la creación de Content Blocks. |
| La personalización no se muestra correctamente | Verifica que la propiedad de contacto de Braze seleccionada contenga un valor para el usuario de prueba. Añade valores alternativos en NiftyImages donde sea necesario. |
| La imagen no se renderiza en Braze | Confirma que el activo de NiftyImages esté guardado, activo y publicado correctamente. Envía un mensaje de prueba de Braze para verificar la imagen en el canal previsto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }