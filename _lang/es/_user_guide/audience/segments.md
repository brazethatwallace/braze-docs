---
nav_title: Segments
article_title: Segments
page_order: 3
layout: dev_guide
guide_top_header: "Segments"
guide_top_text: "La segmentación de audiencia es clave para el marketing estratégico: puede evitar que te excedas en la segmentación, molestes o pierdas una conexión potencial con un cliente. Consulta los siguientes artículos para aprender a segmentar y filtrar tu audiencia para tu (y su) mayor beneficio."
descriptions: "La segmentación de audiencia es clave para el marketing estratégico: puede evitar que te excedas en la segmentación, molestes o pierdas una conexión potencial con un cliente. Consulta esta página de inicio para aprender a segmentar y filtrar tu audiencia para tu (y su) mayor beneficio."
search_rank: 4
tool: Segments
page_type: landing
description: "Esta página de inicio cubre artículos sobre segmentación dentro de las campañas del panel. Aquí puedes encontrar información sobre cómo configurar un segmento, filtros, embudos, información, extensiones y más."

guide_featured_title: "Artículos de la sección"
guide_featured_list:
  - name: Crear un segmento
    link: /docs/user_guide/audience/segments/creating_a_segment
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Administrar segmentos
    link: /docs/user_guide/audience/segments/managing_segments
    image: /assets/img/braze_icons/edit-05.svg
  - name: Filtros de segmentación
    link: /docs/user_guide/audience/segments/segmentation_filters
    image: /assets/img/braze_icons/flag-02.svg
  - name: Datos del segmento
    link: /docs/user_guide/audience/segments/segment_data
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Extensiones de segmento
    link: /docs/user_guide/audience/segments/segment_extension
    image: /assets/img/braze_icons/users-01.svg
  - name: Información del segmento
    link: /docs/user_guide/audience/segments/segment_insights
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "Más artículos"
guide_menu_list:
  - name: Segmentación por ubicación
    link: /docs/user_guide/audience/segments/location_targeting
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Expresiones regulares
    link: /docs/user_guide/audience/segments/regex
    image: /assets/img/braze_icons/search-sm.svg
  - name: Medir el tamaño del segmento
    link: /docs/user_guide/audience/segments/measuring_segment_size
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: "Ejemplo: segmentar con atributos personalizados anidados"
    link: /docs/user_guide/audience/segments/segment_with_nested_custom_attributes
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Solución de problemas
    link: /docs/user_guide/audience/segments/troubleshooting
    image: /assets/img/braze_icons/annotation-question.svg

---

## Acerca de los segmentos de Braze {#about-braze-segments}

En Braze, los segmentos son grupos dinámicos de usuarios que cumplen criterios específicos que tú defines, como atributos de usuario, comportamiento de usuario y eventos personalizados. Puedes ser granular con los criterios anidando segmentos dentro de otros segmentos y aplicando características adicionales, reduciendo el alcance de tu audiencia para que puedas enviar contenido altamente personalizado y atractivo a los usuarios correctos.

Puedes crear tantos segmentos como quieras para dirigirte a los usuarios. Explora diferentes combinaciones de características de segmentos y filtros de segmentación para descubrir formas creativas de utilizar tus datos de usuario, y desbloquea nuevas formas de enviar mensajes relevantes a los usuarios y aumentar la participación.

Consulta los siguientes ejemplos para una pequeña vista previa de cómo los segmentos de Braze pueden ayudarte a dirigirte a tus usuarios.

### Ejemplos {#use-cases}

- **Mensajes de bienvenida:** Segmenta a los nuevos usuarios para que puedas enviar correos electrónicos de incorporación o mensajes dentro de la aplicación que les presenten tu aplicación.
- **Recompensas de fidelización:** Segmenta a los usuarios según su frecuencia de compra, aniversario de membresía u otros hitos, y envía ofertas exclusivas o recompensas a tus usuarios más fieles.
- **Desencadenantes de comportamiento:** Segmenta a los usuarios según sus acciones, como abandonar un carrito en el proceso de pago, para desencadenar mensajes dentro de la aplicación o notificaciones push.
- **Recomendaciones de productos:** Segmenta a los usuarios que compraron productos específicos y envíales recomendaciones de productos complementarios o de nivel superior.
- **Pruebas A/B:** Segmenta a los usuarios para realizar pruebas A/B con diferentes mensajes, líneas del asunto o contenido para determinar qué resuena mejor con usuarios de edades, géneros y otros atributos específicos.

#### Ejemplos de extensiones de segmento {#segment-extension-use-cases}

Puedes refinar aún más tus segmentos utilizando [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para dirigirte a los usuarios según el comportamiento de eventos personalizados o compras almacenado durante toda la vida de su perfil de usuario.

- **Compras históricas:** Segmenta a los usuarios según si compraron un color específico de un producto específico al menos dos veces en los últimos dos años.
- **Eventos e interacciones con mensajes:** Segmenta a los usuarios según si realizaron una compra en los últimos treinta días y también interactuaron con un mensaje específico dentro de la aplicación.
- **Consultar datos:**
  - **Consultar Snowflake:** Segmenta a los usuarios con datos combinados de Braze y fuentes externas, como un CRM or administración de las relaciones con el cliente o un almacén de datos, utilizando [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) para consultar Snowflake.
  - **Sincronizar desde el almacén de datos:** Segmenta a los usuarios con datos sincronizados directamente desde tu almacén de datos o sistema de almacenamiento de archivos a Braze utilizando [extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).