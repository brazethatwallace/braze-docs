---
nav_title: CSS inlining
article_title: CSS inlining
page_order: 5.1
description: "Este artículo de referencia explica cómo habilitar CSS inlining y algunas prácticas recomendadas."
channel:
  - email

---

# CSS inlining

> CSS inlining es una forma de preprocesamiento de correo electrónico que mueve los estilos de una hoja de estilos CSS al cuerpo de un correo electrónico HTML. El término "inlining" se refiere al hecho de que los estilos se aplican "en línea" a elementos HTML individuales.

Para algunos clientes de correo electrónico, CSS inlining puede mejorar la forma en que se renderizan los correos electrónicos y ayudar a confirmar que tus correos se ven como esperas. Si ya tienes la mayor parte del CSS inlined o confías en que tu HTML y CSS son compatibles con los requisitos de la mayoría de los clientes de correo, puede que no sea necesario activar esta característica. Podría causar que los estilos incrustados dinámicamente entren en conflicto con tus estilos en línea existentes y podría alterar la vista previa y el renderizado esperados del correo electrónico.

## Uso de CSS inlining

Puedes controlar si CSS inlining está activado o desactivado para cualquier mensaje de correo electrónico usando el alternar **Enable inline CSS** en la pestaña **Sending Info** del editor HTML.

![Casilla de verificación para administrar CSS inlining en el compositor HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado de inlining predeterminado

Puedes establecer un estado predeterminado de activado o desactivado de forma global desde **Configuración** > **Preferencias de correo electrónico**. Busca la configuración de **CSS Inlining**. Esta configuración determina el valor predeterminado deseado con el que comienzan todos los nuevos mensajes de correo electrónico. Ten en cuenta que cambiar esta configuración no afectará a ninguno de tus mensajes de correo electrónico existentes. También puedes anular este valor predeterminado en cualquier momento mientras redactas mensajes de correo electrónico.

![Opción de CSS en línea en nuevos correos electrónicos por defecto ubicada en la configuración del correo electrónico.]({% image_buster /assets/img_archive/css-inline1.png %})