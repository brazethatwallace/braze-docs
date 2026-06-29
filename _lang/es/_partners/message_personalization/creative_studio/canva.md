---
nav_title: Canva
article_title: Canva
description: "Este artículo de referencia describe la asociación entre Braze y Canva para enviar activos de medios a la Biblioteca de medios de Braze y publicar diseños de correo electrónico de Canva como plantillas de correo electrónico de Braze."
alias: /partners/canva/
page_type: partner
search_tag: Partner

---

# Canva

> [Canva](https://www.canva.com/) es una plataforma y herramienta de diseño gráfico que te permite crear contenido visual para publicaciones en redes sociales, presentaciones, videos y más. La aplicación de Braze en Canva también permite exportar diseños de **correo electrónico** como plantillas de correo electrónico de Braze, además de enviar diseños estáticos a tu Biblioteca de medios.

## Acerca de la integración {#about-the-integration}

La integración de Braze y Canva admite dos rutas de exportación:

| Tipo de exportación | Qué hace |
| --- | --- |
| **Imagen o diseño a la Biblioteca de medios** | Envía tu diseño como un activo a la Biblioteca de medios de Braze. |
| **Diseño de correo electrónico a Braze** | Publica un documento de **correo electrónico** de Canva como una plantilla de correo electrónico de Braze, incluyendo los metadatos de la línea del asunto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acerca de la integración" }

## Integrar Braze con Canva {#integrate-braze-with-canva}

### Paso 1: Instalar la aplicación de Braze en Canva {#step-1-install-the-braze-app-in-canva}

Puedes encontrar la aplicación de Braze en el [Canva Apps Marketplace](https://www.canva.com/your-apps/AAG1cO7kIyc).

Después de instalar la aplicación, estará disponible dentro de un diseño, en el menú **Apps**.

![Aplicación de Braze en el menú Apps de Canva.]({% image_buster /assets/img/canva_integration/braze-canva-app.png %}){: style="max-width:50%;"}

### Paso 2: Autorizar tu cuenta de Braze {#step-2-authorize-your-braze-account}

La primera vez que uses la aplicación de Braze, ya sea que la abras desde el menú **Apps** (exportación a la Biblioteca de medios) o desde el menú **Share** (exportación de correo electrónico), selecciona **Connect** para iniciar la autorización. Esto permite que Canva liste los espacios de trabajo de Braze a los que puedes acceder y cree activos en la Biblioteca de medios en tu nombre.

Para las exportaciones de **correo electrónico**, Canva puede pedirte que inicies sesión de nuevo y apruebes acceso adicional, incluyendo el permiso para **crear plantillas de correo electrónico**. Acepta esos permisos para terminar de publicar diseños de correo electrónico en Braze.

![Botón Connect y flujo de autorización para vincular Canva con Braze.]({% image_buster /assets/img/canva_integration/canva-connect-panel.jpg %})

## Exportar imágenes a la Biblioteca de medios {#export-images-to-the-media-library}

Usa este flujo para diseños estándar de Canva cuando quieras un archivo en la Biblioteca de medios de Braze.

Los siguientes videos muestran cómo enviar diseños desde Canva a tu Biblioteca de medios de Braze.

Video: Abre la aplicación de Braze en Canva e inicia una exportación a la Biblioteca de medios.

{% multi_lang_include video.html id="uf5krks2cx" source="wistia" %}

Video: Elige un espacio de trabajo de Braze y completa la exportación a la Biblioteca de medios.
{% multi_lang_include video.html id="3d09tafx7c" source="wistia" %}

1. Desde el menú **Apps** en tu diseño, abre la aplicación de Braze. Si aún no estás conectado, selecciona **Connect** y completa los pasos en [Autorizar tu cuenta de Braze](#step-2-authorize-your-braze-account).
2. Elige tu espacio de trabajo de destino, opcionalmente ingresa un nombre de archivo y selecciona **Start Export**.

![Pantalla de exportación de Canva con el espacio de trabajo de destino y el botón Start Export.]({% image_buster /assets/img/canva_integration/canva-upload-screen.jpg %})

{: start="3"}
3. Cuando tu exportación se complete, tu nuevo activo estará disponible en la **Biblioteca de medios**, con una fuente de "Canva".

![Activo de Canva exportado en la Biblioteca de medios de Braze.]({% image_buster /assets/img/canva_integration/media-library-source.jpg %})

## Exportar diseños de correo electrónico como plantillas de Braze {#export-email-designs-as-braze-templates}

Usa este flujo cuando tu archivo de Canva sea un tipo de diseño de **correo electrónico**. Publica HTML en Braze como una plantilla (metadatos similares al flujo de imágenes, pero comienzas desde **Share** en lugar de **Apps**).

1. En Canva, crea o abre un diseño de **correo electrónico**. Construye tu mensaje desde cero o usa una plantilla de correo electrónico de Canva.
2. Haz clic en **Share** en la esquina superior derecha del editor y selecciona **Braze**. Si Braze no aparece en la lista, abre **See more** y desplázate hasta **More options** para encontrar Braze.

![Más formas de publicar en Canva con Braze en More options.]({% image_buster /assets/img/canva_integration/canva-share-more-options-braze.png %})

{: start="3"}
3. Si se te solicita conectar o iniciar sesión de nuevo, selecciona **Connect** en el panel de Braze (o completa el flujo de inicio de sesión en el navegador) para que Canva pueda crear plantillas en tu espacio de trabajo.

![Barra lateral de Braze en Canva solicitando Connect para la exportación de correo electrónico.]({% image_buster /assets/img/canva_integration/canva-email-connect-sidebar.png %})

{: start="4"}
4. En el panel de Braze, selecciona qué página de **correo electrónico** publicar (si el diseño tiene varias páginas), elige tu **espacio de trabajo de Braze**, ingresa un **Template name** y una **Subject line**, y luego selecciona **Publish now**. Canva muestra el progreso mientras tu diseño se publica.

![Panel de Braze en Canva con espacio de trabajo, nombre de plantilla, línea del asunto y Publish now.]({% image_buster /assets/img/canva_integration/canva-email-publish-fields.png %})

{: start="5"}
5. Cuando la publicación termine, aparecerá un mensaje de éxito. Selecciona **Check it out** para abrir la plantilla de correo electrónico en Braze.

![Mensaje de éxito después de publicar un diseño de correo electrónico de Canva en Braze, con Check it out.]({% image_buster /assets/img/canva_integration/canva-email-publish-success.png %})

{: start="6"}
6. En Braze, completa cualquier configuración de correo electrónico requerida, como la dirección del **remitente**, el preencabezado y un enlace para cancelar suscripción, antes de usar la plantilla en una campaña o Canvas.

![Plantilla de correo electrónico en Braze abierta desde Canva, con información de envío y vista previa.]({% image_buster /assets/img/canva_integration/braze-email-template-from-canva.png %})