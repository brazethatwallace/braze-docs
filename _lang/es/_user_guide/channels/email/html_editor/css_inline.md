---
nav_title: Inserción de CSS
article_title: Inserción de CSS
page_order: 5.1
description: "Este artículo de referencia explica cómo habilitar la inserción de CSS y algunas buenas prácticas."
channel:
  - email

---

# Inserción de CSS {#css-inlining}

> La inserción de CSS (CSS inlining) es una forma de preprocesamiento de correo electrónico que traslada los estilos de una hoja de estilos CSS al cuerpo de un correo electrónico HTML. El término "inlining" se refiere al hecho de que los estilos se aplican "en línea" a elementos HTML individuales.

Para algunos clientes de correo electrónico, la inserción de CSS puede mejorar la presentación de los mensajes y confirmar que tienen el aspecto esperado. Si ya tienes la mayor parte del CSS insertado en línea o estás seguro de que tu HTML y CSS son compatibles con los requisitos de la mayoría de los clientes de correo, puede que no sea necesario activar esta característica. Puede hacer que los estilos incrustados dinámicamente entren en conflicto con tus estilos en línea existentes y puede alterar la vista previa esperada y la representación del correo electrónico.

## Utilizar la inserción de CSS {#using-css-inlining}

Puedes controlar si la inserción de CSS está activada o desactivada para cualquier mensaje de correo electrónico utilizando la opción **Habilitar CSS en línea** en la pestaña **Información de envío** del editor HTML.

![Casilla para administrar la inserción de CSS en el compositor HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado de inserción predeterminado {#default-inlining-state}

Puedes establecer un estado predeterminado de activación o desactivación de forma global desde **Configuración** > **Preferencias de correo electrónico**. Busca la configuración de **CSS Inlining**. Esta configuración determina el valor predeterminado deseado con el que comienzan todos los nuevos mensajes de correo electrónico. Ten en cuenta que cambiar esta configuración no afectará a ninguno de tus mensajes de correo electrónico existentes. También puedes anular este valor predeterminado en cualquier momento mientras redactas mensajes de correo electrónico.

![Opción de CSS en línea en nuevos correos electrónicos por defecto ubicada en la configuración del correo electrónico.]({% image_buster /assets/img_archive/css-inline1.png %})

## Contenido conectado e inserción de CSS {#connected-content-and-css-inlining}

La inserción de CSS se ejecuta **antes** de que se evalúe el [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). El HTML devuelto por el Contenido conectado **no** pasa por el mismo paso de inserción. Coloca los estilos que necesites del Contenido conectado directamente en la respuesta (atributos `style` en línea o reglas incrustadas), o desactiva la inserción para el mensaje si eso se ajusta mejor a tu plantilla.

## Content Blocks en plantillas HTML personalizadas {#content-blocks-in-custom-html-templates}

Cuando incorporas un [bloque de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) con Liquid dentro de una plantilla de correo electrónico o Campaign con **HTML personalizado**, las reglas CSS de la plantilla principal pueden anular los estilos definidos dentro del bloque de contenido. Comprueba si hay selectores en conflicto o reglas globales en el envoltorio de la plantilla.

## Limitaciones de CSS en Gmail {#gmail-css-limitations}

Gmail tiene limitaciones específicas de CSS que pueden hacer que los correos electrónicos se muestren en vista de escritorio en lugar de vista móvil en la aplicación de Gmail. Esto puede ocurrir por las siguientes razones:

- **Demasiado CSS:** si tu correo electrónico contiene CSS excesivo, Gmail puede eliminar todo el bloque de estilos.
- **CSS incompatible:** cualquier CSS que sea incompatible con Gmail (incluido CSS válido que Gmail no admite) puede provocar que se elimine el bloque de estilos.
- **Cuentas que no son de Gmail en la aplicación de Gmail:** el CSS en el `<head>` no es compatible.

### Consultas de medios en Gmail {#media-queries-in-gmail}

Las consultas de medios CSS generalmente funcionan en las aplicaciones de Gmail, pero existen limitaciones. Si tienes problemas con consultas de medios que no funcionan correctamente en Gmail:

- Revisa la [referencia de CSS compatible con Gmail](https://developers.google.com/gmail/design/reference/supported_css) para asegurarte de que tu CSS es compatible.
- Consulta las [directrices de diseño CSS de Gmail](https://developers.google.com/gmail/design/css) para conocer las buenas prácticas.
- Considera patrones de diseño receptivo principalmente móvil que no dependan únicamente de las consultas de medios para la representación en dispositivos móviles.