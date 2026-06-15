---
nav_title: Mensajes de derecha a izquierda
article_title: Crear mensajes de derecha a izquierda
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "Esta página cubre las mejores prácticas para crear mensajes en Braze que se leen de derecha a izquierda."
---

# Crear mensajes de derecha a izquierda {#create-right-to-left-messages}

> La apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios (como Apple, Android y Google) los renderizan. Esta página cubre las mejores prácticas para crear mensajes de derecha a izquierda para que tus mensajes se muestren con la mayor precisión posible.

## Apariencia del mensaje {#message-appearance}

Al crear un mensaje de derecha a izquierda, ten en cuenta lo siguiente:

- **Apariencia en el panel de Braze:** Cuando un mensaje aparece en el dispositivo de un usuario, su apariencia está determinada en gran medida por el sistema operativo y la configuración de idioma de su dispositivo&#8212;lo que significa que lo que ves en el dashboard no siempre es 100% preciso.
- **Apariencia en el dispositivo:** Apple y Android tienen un control significativo sobre cómo se renderizan los mensajes, mientras que los proveedores de servicios de correo electrónico (ESP) tienen cierto control. La personalización de correo electrónico HTML en Braze puede ser más flexible; sin embargo, el mismo mensaje puede renderizarse de manera diferente en distintos dispositivos según la configuración del usuario.

Además, verifica la puntuación y los emojis para determinar si tu mensaje se está renderizando de forma estándar o de derecha a izquierda.

| Renderizado occidental estándar | Renderizado de derecha a izquierda |
|------------------|------------------------|
| Muestra el signo de exclamación y el emoji al **final** de las oraciones. | Muestra el signo de exclamación y el emoji al **inicio** de la oración. |
| ![Un ejemplo de un mensaje estándar de derecha a izquierda.]({% image_buster /assets/img/right-to-left/standard.png %}) | ![Un ejemplo de un mensaje de izquierda a derecha.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Apariencia del mensaje" }

## Crear un mensaje de derecha a izquierda {#creating-a-right-to-left-message}

Para crear tu mensaje de derecha a izquierda en Braze:

1. Redacta tu mensaje estándar en el editor de Braze.
2. Copia el texto del mensaje desde Braze y luego usa una herramienta de localización para convertirlo en un mensaje de derecha a izquierda.
3. Pega tu mensaje convertido de nuevo en Braze.
4. Verifica el formato y la alineación del texto. Si estás creando un correo electrónico de arrastrar y soltar o HTML, puedes hacerlo dentro del compositor. De lo contrario, necesitarás usar un procesador de texto independiente.<br><br>![Menú del editor de correo electrónico de arrastrar y soltar con botón para alternar la alineación del texto entre derecha a izquierda e izquierda a derecha.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Consideraciones {#considerations}

### Notificaciones push largas {#long-push-notifications}

El método de copiar y pegar para mensajes push puede ser difícil de usar con notificaciones push más largas porque el contenido más extenso puede renderizarse en múltiples líneas en un dispositivo móvil. Si copias el texto de tu mensaje desde fuera de Braze (como un documento de Word) y lo pegas directamente en Braze, la alineación de las oraciones y la ubicación de las palabras pueden cambiar. Para evitar este escenario, copia y pega por partes y añade un salto de línea. Por ejemplo, copia y pega las primeras cinco palabras, añade un salto de línea, copia las siguientes cinco palabras, añade un salto de línea, y así sucesivamente.

Las funciones de vista previa y prueba están diseñadas para mensajes de izquierda a derecha, por lo que los mensajes de derecha a izquierda no se renderizarán correctamente en la sección **Preview & Test**, pero sí se renderizarán correctamente en los dispositivos de los usuarios si su configuración está preparada para ello. Te sugerimos enviarte mensajes a ti mismo en un entorno en vivo para confirmar que se renderizan correctamente según la configuración del dispositivo.

### Alineación del título y el cuerpo {#title-and-body-alignment}

En las notificaciones push, la alineación del título generalmente sigue la configuración de idioma del dispositivo, mientras que la alineación del cuerpo puede seguir el primer carácter direccional fuerte en cada línea (trata cada línea después de un salto de línea por separado). Esto significa que una sola notificación push puede mezclar la alineación entre líneas; por ejemplo, una línea de cuerpo de derecha a izquierda seguida de una línea de izquierda a derecha. Cuando necesites un diseño predecible, mantén la consistencia direccional y usa saltos de línea entre segmentos de idiomas mixtos.

### Texto bidireccional {#bi-directional-text}

Muchos usuarios que escriben en idiomas de derecha a izquierda en realidad usan texto bidireccional: una combinación de idiomas de izquierda a derecha y de derecha a izquierda. Por ejemplo, un especialista en marketing puede enviar un mensaje en hebreo con un nombre de empresa en inglés. Braze no puede manejar el formato del texto bidireccional. Dos formas de evitar problemas de formato son evitar completamente el texto bidireccional o separar el texto de izquierda a derecha del texto de derecha a izquierda usando saltos de línea.

{% alert tip %}
El formato adecuado para texto bidireccional es especialmente importante al crear mensajes que incluyen códigos promocionales; los códigos promocionales suelen estar en formato de izquierda a derecha porque los mismos códigos pueden usarse en diferentes mercados. Dos formas de acomodar los códigos promocionales son usar una imagen para el código promocional o añadir el código promocional al final del mensaje después de un salto de línea.
{% endalert %}

### Caracteres especiales, números y emojis {#special-characters-numbers-and-emojis}

Los caracteres especiales (como puntuación, símbolos matemáticos y monedas), números, viñetas y emojis pueden "saltar de posición" al crear mensajes de derecha a izquierda en Braze. Para solucionar esto, escribe tu texto con el formato adecuado en un procesador de texto externo y luego pega el texto en Braze. También puede ayudar evitar colocar emojis al inicio de tu texto y en su lugar separarlos (junto con caracteres especiales y números) del texto con saltos de línea para evitar problemas de alineación.

### Mensajes en árabe {#arabic-messages}

Al redactar mensajes en árabe, usa tamaños de fuente significativamente más grandes para lograr la misma legibilidad que conseguirías con otros idiomas. Te sugerimos usar un tamaño de fuente aproximadamente un 20% más grande que tu tamaño habitual para idiomas que usan el alfabeto latino o romano. Esto se debe a que las fuentes árabes se diseñan pequeñas para acomodar el espacio vertical que ocupan los diacríticos (marcas de acento).