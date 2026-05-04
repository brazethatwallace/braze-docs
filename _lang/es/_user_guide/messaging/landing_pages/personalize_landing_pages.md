---
nav_title: Personalizar páginas de inicio
article_title: Personalizar páginas de inicio
description: "Este artículo explica cómo personalizar las páginas de inicio de Braze con el editor de arrastrar y soltar."
page_order: 4
---

# Personalizar páginas de inicio {#personalize-landing-pages}

> Usa la personalización con Liquid en las páginas de inicio para adaptar dinámicamente el contenido con datos del perfil de usuario. Por ejemplo, puedes personalizar los títulos en función de diferentes atributos de usuario sin gestionar múltiples páginas de inicio estáticas.

{% alert important %}
La personalización con Liquid para páginas de inicio solo está disponible en el nivel Pro de páginas de inicio. Actualmente, [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), [multiidioma]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/) y [códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/) no son compatibles con la personalización con Liquid en páginas de inicio.
{% endalert %}

## Insertar Liquid {#inserting-liquid}

En el editor de arrastrar y soltar, puedes insertar personalización con Liquid tanto en el editor como en la configuración de la página o del bloque en el panel de la derecha. Para obtener instrucciones sobre cómo implementar Liquid, consulta nuestra [documentación dedicada de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#using-liquid).

![Editor de páginas de inicio con personalización de Liquid añadida.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Vista previa y pruebas {#previewing-and-testing}

Al previsualizar una página de inicio en el editor, puedes ver la página como un usuario aleatorio, un usuario existente o un usuario personalizado.

Sin embargo, al previsualizar la página de inicio desde la tabla de datos o la página de **detalles de la página de inicio**, solo podrás verla como un usuario aleatorio.

## Consideraciones sobre la personalización {#personalization-considerations}

Para mantener un rendimiento óptimo con las páginas de inicio personalizadas, ten en cuenta los siguientes límites de tamaño:

- **Guardar una página de inicio:** Si el tamaño supera los 500&nbsp;KB, es posible que recibas un mensaje de advertencia indicando que la página ha superado nuestros límites de tamaño, lo que puede impedir su publicación.
- **Renderizado con personalización de Liquid:** El tamaño total no debe superar 1&nbsp;MB. De lo contrario, Braze puede despublicar la página automáticamente.

### Evitar la despublicación de páginas de inicio {#avoid-unpublishing-landing-pages}

Si tu página supera estos límites de tamaño, recibirás un correo electrónico indicando que puede ser despublicada si continúa superando el límite. Cuando se alcance el umbral, la página se despublicará automáticamente y recibirás una notificación.

Para evitar que tu página supere los límites de tamaño o experimente tiempos de carga lentos, asegúrate de usar personalización con Liquid que:

- No recorra continuamente ni haga referencia a grandes conjuntos de datos.
- No dependa de lógica matemática o condicional extensa dentro del bloque de Liquid.

Además, evita incrustar scripts grandes, hojas de estilo y activos codificados en base64 directamente en el código de tu página de inicio. Estos activos en línea cuentan para el límite de tamaño de la página y pueden ralentizar el renderizado. En su lugar, sube fuentes, imágenes, hojas de estilo y scripts a la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Los activos servidos desde la biblioteca de medios están alojados en el CDN de Braze, por lo que no se procesan para el renderizado de Liquid y no cuentan para el límite de tamaño de la página.

### Usar Liquid para usuarios identificados y anónimos {#use-liquid-for-identified-and-anonymous-users}

Liquid puede personalizar la experiencia de la página de inicio tanto para visitantes identificados como anónimos.

- **Usuarios identificados:** Enlaza a la página de inicio desde un mensaje de Braze e incluye la [etiqueta de Liquid de la página de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/#using-landing-page-liquid-tags). Esto asocia al usuario con su perfil de Braze y personaliza la experiencia de la página.
- **Visitantes anónimos:** Usa Liquid para contenido contextual no basado en el perfil, como un número aleatorio o un saludo según la hora del día.

## Páginas alternativas {#fallback-pages}

Si tus usuarios intentan acceder a una página que ha sido despublicada, verán un mensaje indicando que la página no puede cargarse actualmente. Las razones por las que una página ha sido despublicada incluyen:

- Liquid complejo o con errores, lo que puede causar tiempos de renderizado prolongados
- Problemas de red del usuario
- Superación de los límites máximos de tamaño de la página de inicio