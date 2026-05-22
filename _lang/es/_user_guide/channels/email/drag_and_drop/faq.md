---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes del editor de arrastrar y soltar
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Este artículo cubre varias preguntas frecuentes relacionadas con el editor de arrastrar y soltar."
tool:
  - Campaigns
  - Canvas

---

# Preguntas frecuentes {#frequently-asked-questions}

> Esta página ofrece respuestas a algunas preguntas frecuentes relacionadas con el editor de arrastrar y soltar para correo electrónico.

### ¿Puedo previsualizar cómo se ve mi correo electrónico en modo oscuro? {#can-i-preview-how-my-email-appears-in-dark-mode}

Sí. Ve a la sección **Preview and Test** del editor de arrastrar y soltar y activa **Dark mode**. También recomendamos previsualizar y probar tus correos electrónicos en diferentes plataformas de usuario y usar imágenes transparentes para las imágenes de fondo de las filas cuando sea posible.

### ¿Cómo debo diseñar correos electrónicos para modo oscuro y modo claro? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

Los correos electrónicos no necesitan enviarse en diseños separados de modo claro y oscuro, ya que los clientes y dispositivos de correo electrónico pueden aplicar su propio tema oscuro. Sin embargo, esto puede invertir colores u ocultar fondos si no se establecen colores explícitos en el contenedor exterior y las secciones principales. Para evitar esto, recomendamos establecer colores de fondo sólidos para que tu mensaje se lea claramente tanto en modo oscuro como en modo claro.

### ¿Cómo puedo cambiar el relleno del correo electrónico en móvil sin actualizar el relleno en la vista web? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

No puedes editar el relleno para las vistas de móvil y web de forma independiente, por lo que cualquier edición se refleja en ambas vistas. Sin embargo, puedes agregar lógica CSS en el editor HTML que establezca el relleno según diferentes tamaños de pantalla. Esto no es compatible con el editor de arrastrar y soltar, así que puedes exportar el archivo HTML y usar el editor HTML en su lugar.

### ¿Cómo puedo optimizar una fila de botones para que permanezcan horizontales en escritorio y móvil? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Al crear un correo electrónico con el editor de arrastrar y soltar, si creas una fila horizontal de botones de llamada a la acción, es posible que los botones cambien a una orientación vertical en móvil.

Para mantener el mismo formato en diferentes tamaños de dispositivo, recomendamos crear una fila separada con botones de llamada a la acción que tengan un relleno optimizado para móvil y estén configurados para ocultar la fila en un dispositivo de escritorio. Tener dos filas separadas significa que puedes establecer el relleno deseado para la mejor representación del texto en dispositivos de escritorio y móviles.

### ¿Puedo ajustar la altura de la fila en el editor de arrastrar y soltar? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

La altura de la fila se ajusta automáticamente al contenido. Como alternativa, recomendamos que:
1. Agregues un bloque divisor.
2. Hagas clic en el interruptor para activar su transparencia.
3. Ajustes la altura.

### ¿Es posible crear capas en el editor? ¿Puedo agregar una imagen de fondo, superponer una imagen y agregar una capa de texto encima? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

El editor de arrastrar y soltar actualmente admite dos capas. Puedes establecer una imagen de fondo de fila y personalizar los colores de fondo.

### ¿Puedo guardar mi correo electrónico de arrastrar y soltar como plantilla después de crearlo dentro de mi campaña o Canvas? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

No, debes recrear el correo electrónico en **Plantillas de correo electrónico** para guardarlo.

### ¿Puedo agregar archivos adjuntos de correo electrónico en el editor de arrastrar y soltar? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Sí. Puedes agregar archivos adjuntos a tu mensaje de correo electrónico yendo a **Sending Settings** > **Advanced**.