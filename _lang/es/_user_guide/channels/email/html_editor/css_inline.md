---
nav_title: Inserción de CSS
article_title: CSS Inlining
page_order: 5.1
description: "Este artículo de referencia explica cómo habilitar la inserción de CSS y algunas buenas prácticas."
channel:
  - email

---

# Inserción de CSS

> CSS inlining es una forma de preprocesamiento de correo electrónico que traslada los estilos de una hoja de estilos CSS al cuerpo de un correo electrónico HTML. El término "inlining" se refiere al hecho de que los estilos se aplican "en línea" a elementos HTML individuales.

Para algunos clientes de correo electrónico, la inserción de CSS puede mejorar la presentación de los mensajes y confirmar que tienen el aspecto esperado. Si ya tienes la mayor parte del CSS alineado o estás seguro de que tu HTML y CSS son compatibles con los requisitos de la mayoría de los clientes de correo, puede que no sea necesario activar esta característica. Puede hacer que los estilos incrustados dinámicamente entren en conflicto con tus estilos en línea existentes y puede alterar la vista previa esperada y la representación del correo electrónico.

## Utilizar la inserción de CSS

Puedes controlar si la inserción de CSS está activada o desactivada para cualquier mensaje de correo electrónico utilizando la opción **Habilitar CSS incrustado** en la pestaña **Información de envío** del editor HTML.

![Casilla para administrar la inserción de CSS en el compositor HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado de inserción predeterminado

Puedes establecer un estado predeterminado de activación o desactivación de forma global desde **Configuración** > **Preferencias de correo electrónico**. Busca la configuración de **CSS Inlining**. Esta configuración determina el valor predeterminado deseado con el que comienzan todos los nuevos mensajes de correo electrónico. Ten en cuenta que cambiar esta configuración no afectará a ninguno de tus mensajes de correo electrónico existentes. También puedes anular este valor predeterminado en cualquier momento mientras redactas mensajes de correo electrónico.

![Opción de CSS en línea en nuevos correos electrónicos por defecto ubicada en la configuración del correo electrónico.]({% image_buster /assets/img_archive/css-inline1.png %})