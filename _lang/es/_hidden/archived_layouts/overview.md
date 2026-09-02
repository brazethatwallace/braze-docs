---
nav_title: Resumen
page_order: 0
noindex: true
---

# Ejemplo de diseño: Resumen

> El diseño de resumen es útil para crear una opción de navegación específica en la parte superior de una página que permita a los usuarios hacer clic en un botón para ir a una parte concreta de la página o a otra completamente distinta.

Ejemplos clásicos del diseño del SELECTOR son la página de [registros de cambios del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/changelogs) o la [página de detalles creativos de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types).

## Componentes obligatorios

1. Notación de apertura y cierre YAML. Es decir, --- antes del contenido y --- después.
2. Comillas alrededor de cierto contenido de parámetros. (Parámetros de encabezado, parámetros de texto, contenido con guiones u otros caracteres especiales).
3. Notación de etiquetas de glosario (son etiquetas de filtro).

## Parámetros obligatorios

| Parámetro | Tipo de contenido | Detalles |
|---|---|---|
| `page_order`| numérico | Ordena la página dentro de la sección. Este orden se reflejará en la navegación del lado izquierdo. |
| `nav-title`| alfanumérico | Título que aparecerá en la navegación del lado izquierdo. |
|`layout`| alfanumérico, sin espacios | Selecciona un diseño de la [sección de diseños](https://github.com/Appboy/braze-docs/tree/develop/_layouts) de la documentación. |
| `guide_top_header`| alfanumérico | Título de tu página.|
| `guide_top_text`| alfanumérico | Describe tu página; este texto aparecerá directamente encima de los botones y su título. Se requieren comillas alrededor del contenido. |
| `guide_featured_title`| alfanumérico | Título de tus tarjetas. Aparecerá directamente encima de los botones.
| `guide_featured_list`| más YAML, alfanumérico | Consulta [Formato de listado de guía](#guide-listing-format) a continuación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros obligatorios" }

### Formato de listado de guía {#guide-listing-format}

| Parámetro | Tipo de contenido | Detalles |
|---|---|---|
|`name`| alfanumérico | Nombre de la casilla. |
| `link`| URL o ruta | Enlace al destino de la casilla. Debe contener la URL completa o (si es un enlace interno) `/docs...` |
|`image`| ruta | Enlace a la ubicación de la imagen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Formato de listado de guía" }

Ejemplo de formato:

```yaml
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

```yaml
---
nav_title: Detalles creativos
page_order: 4
layout: featured
guide_top_header: "Detalles creativos"
guide_top_text: "¡Sé creativo con nuestros mensajes dentro de la aplicación! Pero antes deberías conocer algunas directrices. Al fin y al cabo, ¡tienes que conocer las reglas para poder romperlas! Consulta las especificaciones creativas de cada tipo de mensaje o los detalles creativos globales a continuación."

guide_featured_title: "Especificaciones creativas por tipo de mensaje"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Deslizamiento hacia arriba
  link: /docs/user_guide/channels/in_app_messages/message_types/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Pantalla completa
  link: /docs/user_guide/channels/in_app_messages/message_types/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Detalles creativos {#general}

Los mensajes dentro de la aplicación de Braze tienen especificaciones creativas tanto globales como individuales. Para obtener más información sobre nuestros tipos de mensajes dentro de la aplicación más personalizables, visita nuestra página [Personalizar]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% alert important %}
  Estos detalles solo se aplican a nuestra generación más reciente de mensajes dentro de la aplicación (Generación 3). Si no estás utilizando nuestra generación más reciente de mensajes dentro de la aplicación, consulta nuestra documentación sobre [generaciones anteriores de mensajes dentro de la aplicación]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/).
{% endalert %}