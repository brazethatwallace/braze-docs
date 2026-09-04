---
nav_title: Personalizar páginas de inicio
article_title: Personalizar páginas de inicio
description: "Este artículo explica cómo personalizar las páginas de inicio de Braze con el editor de arrastrar y soltar."
page_order: 4
---

# Personalizar páginas de inicio {#personalize-landing-pages}

> Usa la personalización con Liquid en las páginas de inicio para adaptar dinámicamente el contenido con datos del perfil de usuario. Por ejemplo, puedes personalizar los títulos en función de diferentes atributos de usuario sin gestionar múltiples páginas de inicio estáticas.

{% alert important %}
La personalización con Liquid para páginas de inicio solo está disponible en el nivel Pro de páginas de inicio. Actualmente, [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [multiidioma]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings) y [códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) no son compatibles con la personalización con Liquid en páginas de inicio.
{% endalert %}

## Insertar Liquid {#inserting-liquid}

En el editor de arrastrar y soltar, puedes insertar personalización con Liquid tanto en el editor como en la configuración de la página o del bloque en el panel de la derecha. Para obtener instrucciones sobre cómo implementar Liquid, consulta nuestra [documentación de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dedicada.

![Editor de landing page con personalización de Liquid añadida.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Vista previa y pruebas {#previewing-and-testing}

Al previsualizar una página de destino en el editor, puedes ver la página como un usuario aleatorio, un usuario existente o un usuario personalizado.

Sin embargo, al previsualizar la página de destino desde la tabla de datos o la página de **detalles de la página de destino**, solo podrás verla como un usuario aleatorio.

## Consideraciones de personalización {#personalization-considerations}

Para mantener un rendimiento óptimo con las páginas de destino personalizadas, ten en cuenta los siguientes límites de tamaño:

- **Guardar una página de destino:** Si el tamaño supera los 500&nbsp;KB, es posible que recibas un mensaje de advertencia indicando que la página ha superado nuestros límites de tamaño, lo que puede impedir su publicación.
- **Renderizado con personalización de Liquid:** El tamaño total no debe superar 1&nbsp;MB. De lo contrario, Braze puede despublicar la página automáticamente.

### Evitar la despublicación de páginas de destino {#avoid-unpublishing-landing-pages}

Si tu página supera estos límites de tamaño, recibirás un correo electrónico indicando que puede ser despublicada si continúa superando el límite. Cuando se alcance el umbral, la página se despublicará automáticamente y recibirás una notificación.

Para evitar que tu página supere los límites de tamaño o experimente tiempos de carga lentos, asegúrate de usar personalización de Liquid que:

- No recorra continuamente ni haga referencia a conjuntos de datos grandes.
- No dependa de lógica matemática o condicional extensa dentro del bloque de Liquid.

Además, evita incrustar scripts grandes, hojas de estilo y activos codificados en base64 directamente en el código de tu página de destino. Estos activos en línea cuentan para el límite de tamaño de la página y pueden ralentizar el renderizado. En su lugar, sube fuentes, imágenes, hojas de estilo y scripts a la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Los activos servidos desde la biblioteca de medios están alojados en el CDN de Braze, por lo que no se procesan para el renderizado de Liquid y no cuentan para el límite de tamaño de la página.

### Usar Liquid para usuarios identificados y anónimos {#use-liquid-for-identified-and-anonymous-users}

Liquid puede personalizar la experiencia de la página de destino tanto para visitantes identificados como anónimos.

- **Usuarios identificados:** Enlaza a la página de destino desde un mensaje de Braze e incluye la [etiqueta de Liquid de página de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users#using-landing-page-liquid-tags). Esto asocia al usuario con su perfil de Braze y personaliza la experiencia de la página.
- **Visitantes anónimos:** Usa Liquid para contenido contextual no basado en el perfil, como un número aleatorio o un saludo según la hora del día.

### Rellenar previamente los campos del formulario {#pre-fill-form-fields}

Si un campo de formulario de la página de destino está mapeado a un atributo del perfil de usuario, puedes rellenar previamente ese campo para los usuarios que regresan. Esto ayuda a reducir la fricción del formulario y mejora las tasas de finalización para los visitantes conocidos.

Para usar el rellenado previo de campos del formulario:

1. Selecciona tu campo de formulario en el editor de arrastrar y soltar.
2. En el panel de configuración de la derecha, mapea el campo al atributo de perfil correspondiente.
3. Selecciona **Rellenar previamente desde el perfil de usuario**.

![Configuración de campo de formulario de página de destino mostrando la opción de rellenar previamente desde los datos del perfil de usuario.]({% image_buster /assets/img/landing_pages/pre-fill-checkbox.png %}){: style="max-width:70%;"}

El rellenado previo solo funciona para [usuarios identificados](#use-liquid-for-identified-and-anonymous-users). Para los visitantes anónimos, los campos del formulario mantienen su estado predeterminado:

- **Campos de entrada:** Muestran su texto de marcador de posición.
- **Casillas de verificación, botones de radio y controles similares:** Permanecen sin seleccionar hasta que el usuario interactúe con ellos.

{% alert warning %}
Si un usuario reenvía un enlace de página de destino (desde un correo electrónico, SMS u otro mensaje) a otra persona, el destinatario verá los datos rellenados previamente destinados al usuario original. Esta es la misma consideración de seguridad que se aplica a los enlaces de cancelación de suscripción y a los enlaces del centro de preferencias. Ten en cuenta la sensibilidad de los datos que estás rellenando previamente y el comportamiento de compartición de tu audiencia al usar esta característica.
{% endalert %}

## Obtener datos externos con código personalizado {#fetching-external-data-with-custom-code}

Puedes usar un bloque de **código personalizado** para obtener datos de endpoints externos y mostrarlos en tu página de destino. Este enfoque realiza la solicitud en el lado del cliente (en el navegador del usuario), por lo que la página se carga rápidamente sin retrasos de renderizado del lado del servidor.

{% alert tip %}
Para otros usos avanzados del bloque de **código personalizado**, consulta [Puente JavaScript para páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) y [Crear bloques de formulario personalizados]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks).
{% endalert %}

{% alert warning %}
Al obtener datos externos, eres responsable de la seguridad de tu implementación. Los identificadores externos utilizados en las llamadas a la API deben ser UUID o usar un esquema de nomenclatura equivalentemente seguro; consulta [Mejores prácticas de nomenclatura de ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).
{% endalert %}

### Caso de uso {#use-case}

Este patrón es útil cuando necesitas mostrar datos específicos del usuario que no están almacenados en Braze. Los ejemplos incluyen inventario en tiempo real, recomendaciones personalizadas u otros datos que tu organización gestiona en sistemas separados.

### Ejemplo de implementación {#example-implementation}

Este ejemplo muestra cómo obtener datos de usuario de una API externa. Reemplaza el endpoint de la API con tu propio endpoint seguro y usa un identificador seguro.

{% raw %}
```html
<script>
window.onload = () => {
  // Use Liquid to template the user's external ID
  const userId = "{{${user_id}}}";

  const loadUserData = async () => {
    try {
      // Replace with your own secure API endpoint
      const response = await fetch(`https://your-api.example.com/user/${userId}`);

      if (!response.ok) {
        throw new Error('Failed to load data');
      }

      const data = await response.json();

      // Update the page with the fetched data
      document.querySelector("#user-data").textContent = JSON.stringify(data, null, 2);
      document.querySelector("#user-name").textContent = data.name || "User";
    } catch (error) {
      // Handle errors gracefully
      document.querySelector("#user-data").textContent = "Unable to load data at this time.";
    }
  };

  loadUserData();
};
</script>

<!-- Display area for fetched data -->
<p>Welcome, <span id="user-name">Loading...</span></p>
<pre id="user-data">Loading your information...</pre>
```
{% endraw %}

### Consideraciones {#considerations}

Al obtener datos externos en páginas de destino:

- **Estados de carga:** Los usuarios verán texto de marcador de posición hasta que el endpoint responda. Considera añadir un indicador de carga o una pantalla esqueleto.
- **Manejo de errores:** Si el endpoint falla o tarda en responder, la página puede parecer rota. Implementa mensajes de error y alternativas apropiados.
- **Rendimiento:** La página se carga inmediatamente, pero los datos aparecen después de que se completa la solicitud externa. Mantén las respuestas de tu API rápidas para la mejor experiencia de usuario.
- **Seguridad:** Asegúrate de que tu endpoint de API valide el identificador y solo devuelva datos que el usuario esté autorizado a ver. Implementa límites de velocidad para prevenir abusos. Para orientación sobre cómo elegir identificadores seguros, consulta [Mejores prácticas de nomenclatura de ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).

{% alert warning %}
Para páginas de destino personalizadas con Liquid, Braze procesa los delimitadores {% raw %}`{{`{% endraw %} y {% raw %}`{%`{% endraw %} en cualquier lugar donde aparezcan en el HTML de la página de destino, incluyendo dentro de cadenas de JavaScript, comentarios y expresiones regulares. Esto se aplica a toda la página, pero los bloques de **código personalizado** son el lugar más probable donde estas secuencias se incluyan accidentalmente.

Si estas secuencias aparecen sin etiquetas de cierre coincidentes (por ejemplo, {% raw %}`/* version {{ 2.0 */`{% endraw %}), Braze las trata como etiquetas de Liquid abiertas. Otras etiquetas de Liquid válidas en la página pueden no renderizarse, o el renderizado de Liquid puede fallar en otra parte del mismo bloque. En casos graves, un Liquid roto puede impedir que la página se publique o causar que se despublique (consulta [Páginas alternativas](#fallback-pages)).

Para evitar esto, escapa o elimina {% raw %}`{{`{% endraw %} y {% raw %}`{%`{% endraw %} de contextos que no sean Liquid, divide las secuencias en JavaScript (por ejemplo, {% raw %}`'{' + '{'`{% endraw %}). Liquid se ejecuta en el lado del servidor antes de que el script se ejecute. También puedes envolver secciones más grandes que no sean Liquid en etiquetas {% raw %}`&#123;% raw %&#125;...&#123;% endraw %&#125;`{% endraw %}.
{% endalert %}

## Páginas alternativas {#fallback-pages}

Si tus usuarios intentan acceder a una página que ha sido despublicada, verán un mensaje indicando que la página no puede cargarse en ese momento. Las razones por las que una página ha sido despublicada incluyen:

- Liquid complejo o con errores, que puede causar tiempos de renderizado prolongados
- Problemas de red del usuario
- Exceder los límites máximos de tamaño de la página de destino