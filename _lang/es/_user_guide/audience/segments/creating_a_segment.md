---
nav_title: Crear un segmento
article_title: Crear un segmento
page_order: 1
page_type: tutorial
description: "Este artículo práctico te guiará sobre cómo configurar y crear un segmento con Braze."
tool: Segments
search_rank: 3
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Crear un segmento {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordercreate-a-segment}

> La segmentación te permite dirigirte a los usuarios en función de sus características y acciones demográficas, de comportamiento o técnicas. El uso creativo e inteligente de la segmentación y la automatización de mensajería te permite mover fácilmente a tus usuarios desde el primer contacto hasta convertirlos en clientes a largo plazo. Los segmentos se actualizan en tiempo real a medida que cambian los datos, y puedes crear tantos segmentos como necesites para tus propósitos de segmentación y mensajería.

## Paso 1: Navega a la sección de segmentos {#step-1-navigate-to-the-segments-section}

Ve a **Audiencia** > **Segments**.

## Paso 2: Nombra tu segmento {#step-2-name-your-segment}

Selecciona **Crear segmento** para empezar a construir tu segmento. Nombra tu segmento describiendo el tipo de usuario que pretendes filtrar. Esto te ayudará a identificar el segmento cuando quieras dirigirte a él para tus Campaigns o Canvas. Los títulos de segmento vagos pueden resultar confusos.

Opcionalmente, puedes hacer lo siguiente:
- Añadir una descripción al segmento para proporcionar más detalles sobre la intención de esta audiencia y dejar notas para que otros miembros del equipo puedan consultarlas.
- Añadir un [equipo]({{site.baseurl}}/user_guide/administer/global/user_management/teams) a tu segmento.
- Añadir [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) a tu segmento para una mayor organización.

![Modal de crear segmento donde el segmento se llama "Lapsed Users" con la descripción del segmento "This is our main Lapsed User segment to target non-actives within the past fourteen days." con dos botones: Cancelar y Crear segmento.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Paso 3: Elige tu aplicación o plataforma {#step-3-choose-your-app-or-platform}

Elige a qué aplicaciones o plataformas te gustaría dirigirte seleccionando **Usuarios de todas las aplicaciones** (predeterminado) o **Usuarios de aplicaciones específicas**. **Usuarios de aplicaciones específicas** se dirige a usuarios con al menos una sesión en las aplicaciones especificadas.

Por ejemplo, si quisieras enviar un mensaje dentro de la aplicación solo a dispositivos iOS, selecciona tu aplicación iOS. Esto asegurará que los usuarios que puedan usar tanto un dispositivo iOS como Android solo reciban el mensaje en su dispositivo iOS. En la lista de aplicaciones específicas, la opción **Usuarios sin aplicaciones** te permite incluir usuarios sin sesiones ni datos de aplicación (normalmente creados mediante importación de usuarios o REST API).

![Panel de detalles del segmento con la opción "Usuarios de todas las aplicaciones" seleccionada en la sección Aplicaciones utilizadas.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Paso 4: Añade filtros a tu segmento {#step-4-add-filters-to-your-segment}

Añade al menos un filtro a tu segmento. Puedes combinar tantos filtros como quieras para hacer tu segmentación más específica.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### Grupos de filtros {#filter-groups}

Los filtros se organizan en grupos de filtros. Cada filtro debe formar parte de un grupo de filtros que tenga un mínimo de un filtro. Un segmento puede tener múltiples grupos de filtros. Para añadir uno, selecciona **Añadir grupo de filtros**. Edita el nombre del grupo de filtros seleccionando el icono que aparece cuando pasas el cursor junto a él.

![Grupo de filtros con un icono de edición junto a su nombre.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Selecciona los iconos junto a cada filtro para contraer el editor de filtros o duplicar filtros individuales. Después de duplicar un filtro, puedes ajustar sus valores dentro de cada desplegable.

### Lógica de segmentación usando AND y OR {#segmentation-logic-using-and-and-or}

Dentro de un grupo de filtros, los filtros pueden unirse mediante "AND" u "OR". Entre grupos de filtros, los grupos pueden unirse mediante "AND" u "OR". Al usar grupos de filtros, puedes crear lógica de segmentación como:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

Seleccionar "OR" para tus filtros significa que tu segmento contendrá usuarios que cumplan cualquier combinación de uno, algunos o todos esos filtros. Seleccionar "AND" significa que los usuarios que no pasen ese filtro no serán incluidos en tu segmento.

{% alert tip %}
Al seleccionar "OR" para filtros que incluyen un filtro negativo (como "no es" en un grupo de suscripción), recuerda que los usuarios solo necesitan cumplir uno de los filtros "OR" para ser incluidos en el segmento. Para aplicar el filtro negativo independientemente de los otros filtros, usa un [grupo de exclusión](#exclusion).
{% endalert %}

{% details Cuándo evitar el operador OR %}

Puede haber situaciones de segmentación de usuarios en las que se debe evitar el uso del operador `OR`. El operador `OR` crea una declaración que se evalúa como verdadera si un usuario cumple los criterios de uno o más de los filtros en una declaración. Por ejemplo, si quieres crear un segmento de usuarios que pertenecen a "Foodies" pero no pertenecen a "Non-foodies" ni a "Candy-lovers", entonces usar el operador `OR` funcionaría aquí.

![Grupo de filtros para usuarios en el segmento "foodies" y que no están en los segmentos "non-foodies" o "candy-lovers".]({% image_buster /assets/img_archive/or_operator_segment.png %})

Sin embargo, si tu objetivo es segmentar usuarios que pertenecen al segmento "Foodies" y no están en ninguno de los segmentos "Non-foodies" y "Candy-lovers", entonces usa el operador `AND`. De esta manera, los usuarios que reciban la Campaign o Canvas están en el segmento previsto ("foodies") y no en los otros segmentos ("Non-foodies" y "Candy-lovers") al mismo tiempo.

Los siguientes criterios de segmentación negativa no deben usarse con el operador `OR` cuando dos o más filtros hacen referencia al mismo atributo:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Si `not included`, `is not`, `does not equal` o `does not match regex` se usan con el operador `OR` dos o más veces en una declaración, se segmentarán usuarios con todos los valores del atributo relevante.

{% enddetails %}

### Operadores de filtro {#filter-operators}

Dependiendo del filtro específico que selecciones, tendrás diferentes operadores para identificar los valores del filtro. Para profundizar en los operadores disponibles para diferentes tipos de atributos personalizados, consulta [Almacenamiento de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#setting-custom-attributes). Ten en cuenta que al usar el operador "is any of", el número máximo de elementos que puedes incluir en ese campo es 256.

{% alert note %}
Braze no genera perfiles para los usuarios hasta que hayan usado la aplicación por primera vez, por lo que no puedes dirigirte a usuarios que aún no han abierto tu aplicación.
{% endalert %}

![Grupos de filtros del segmentador con el operador AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Los segmentos que ya usan el filtro **Pertenencia a segmento** no pueden incluirse ni anidarse adicionalmente en otros segmentos. Esto evita un ciclo en el que el Segment A incluye al Segment B, que luego intenta incluir al Segment A de nuevo. Si eso ocurriera, el segmento seguiría referenciándose a sí mismo, haciendo imposible calcular quién realmente pertenece a él.

Además, anidar segmentos de esta manera añade complejidad y puede ralentizar las cosas. En su lugar, recrea el segmento que intentas incluir usando los mismos filtros.
{% endalert %}

### Grupos de exclusión (opcional) {#exclusion}

Al construir un segmento, puedes aplicar uno o varios grupos de exclusión. Los grupos de exclusión contienen criterios que identifican a los usuarios que se excluirán de tu segmento, y siempre estarán conectados a tus grupos de filtros con un operador "AND NOT".

Los grupos de exclusión anulan los criterios del segmento. Si un usuario cumple los criterios de tu grupo de exclusión, no formará parte de tu segmento, incluso si cumple los criterios dentro de tus grupos de filtros.

Crea un grupo de exclusión añadiendo filtros como lo harías para los grupos de filtros. La estadística de *Usuarios alcanzables estimados* en un grupo de exclusión muestra el número estimado de usuarios que permanecen en tu segmento después de aplicar los criterios de exclusión.

Los usuarios excluidos no se contarán como parte de la estadística de *Total de usuarios alcanzables* de tu segmento.

![Un grupo de exclusión con dos filtros.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### Ver estadísticas de embudo {#viewing-funnel-statistics}

Selecciona **Ver estadísticas de embudo** para mostrar las estadísticas de ese grupo de filtros y ver cómo cada filtro añadido impacta en las estadísticas de tu segmento. Verás un recuento estimado y un porcentaje de usuarios que son segmentados por todos los filtros hasta ese punto. Una vez que se muestren las estadísticas para un grupo de filtros, se actualizarán automáticamente cada vez que cambies los filtros. Estas estadísticas son estimadas y pueden tardar un momento en generarse.

Ten en cuenta que si usas AND entre tus filtros, las estadísticas de embudo disminuirán; si usas OR entre tus filtros, las estadísticas de embudo aumentarán.

![Dos filtros con estadísticas de embudo del segmento.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Al añadir filtros que documenten el flujo de tus usuarios, puedes ver los puntos donde los usuarios abandonan. Por ejemplo, si eres una aplicación de redes sociales y quieres ver dónde podrías estar perdiendo usuarios durante tu proceso de incorporación, puedes añadir filtros de datos personalizados para registrarse, añadir amigos y enviar el primer mensaje. Si descubres que el 85% de los usuarios se registran y añaden amigos, pero solo el 45% envió el primer mensaje, entonces sabrás que debes enfocarte en fomentar más envíos de mensajes durante tus campañas de incorporación y marketing.

### Probar segmentos {#testing-segments}

Después de añadir aplicaciones y filtros a tu segmento, puedes probar si tu segmento está configurado como se esperaba buscando un usuario para confirmar si coincide con los criterios del segmento. Para hacerlo, busca el `external_id` o `braze_id` de un usuario en la sección **Búsqueda de usuario**.

{% alert note %}
**Búsqueda de usuario** solo acepta `external_id` y `braze_id`. No acepta direcciones de correo electrónico, números de teléfono ni otros identificadores. Para encontrar un perfil por correo electrónico, teléfono u otros campos, usa [**Buscar usuarios**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles) en su lugar.
{% endalert %}

![Sección de búsqueda de usuario con un campo de búsqueda.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

La búsqueda de usuario está disponible cuando:
- Creas un segmento
- Configuras una audiencia de Campaign o Canvas
- Configuras un paso de Rutas de audiencia

Cuando un usuario coincide con los criterios del segmento, filtro y aplicación, una alerta lo indicará.

![Una búsqueda de usuario de "testuser" muestra una alerta que dice: "testuser coincide con todos los segmentos, filtros y aplicaciones."]({% image_buster /assets/img_archive/user_lookup_match.png %})

Cuando un usuario no coincide con parte o la totalidad de los criterios del segmento, filtro o aplicación, los criterios faltantes se enumeran para fines de solución de problemas.

![Una búsqueda de usuario con una alerta que dice: "test1 no coincide con los siguientes criterios de segmentación:" y muestra los criterios faltantes.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### Segmentos de un solo usuario {#single-user-segments}

Puedes crear segmentos de un solo usuario (o segmentos de un puñado de usuarios) usando atributos únicos que identifican a los usuarios, como un nombre de usuario o un ID de usuario.

Sin embargo, las estadísticas de segmentación o la vista previa pueden no mostrar a este usuario individual porque las estadísticas de segmento se calculan basándose en una muestra aleatoria con un intervalo de confianza del 95% de que el resultado está dentro de +/- 1%. Cuanto mayor sea tu base de usuarios, más probable es que el tamaño de tu segmento sea una estimación aproximada. Para asegurarte de que tu segmento contiene al usuario único al que te diriges, selecciona **Calcular estadísticas exactas**. Esto calculará el número exacto de usuarios en tu segmento con una precisión superior al 99,999%.

Braze tiene filtros de prueba para dirigirse a usuarios específicos por ID de usuario o dirección de correo electrónico.

## Paso 5: Guarda tu segmento {#step-5-save-your-segment}

Selecciona **Guardar**. ¡Ahora estás listo para empezar a enviar mensajes a tus usuarios!

## Medir el tamaño del segmento {#measuring-segment-size}

Para aprender sobre cómo monitorizar la pertenencia y el tamaño de tu segmento, consulta [Medir el tamaño del segmento]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Archivar segmentos {#archiving-segments}

Si ya no necesitas o deseas retirar un segmento específico, puedes archivarlo yendo a la página **Segments** y seleccionando **Archivar** en el menú de la fila de ese segmento.

{% alert warning %}
Cuando archivas un segmento, cualquier Campaign o Canvas que lo use (incluso si el segmento solo se usa en un único componente de Canvas) también se archivará. Esto también incluye segmentos anidados donde tanto los segmentos como cualquier Campaign o Canvas que los use también se archivarán.
<br><br>
Recibirás una advertencia que enumera qué Campaigns y Canvas están a punto de ser archivados al archivar el segmento asociado.
{% endalert %}

Puedes desarchivar el segmento navegando hasta él dentro de la página **Segments** y seleccionando **Desarchivar**.

## Comportamiento de segmentación cuando los usuarios tienen múltiples dispositivos {#targeting-behavior-when-users-have-multiple-devices}

Los usuarios tienen más de un dispositivo si inician sesión en la misma cuenta en múltiples dispositivos. Puedes verificar múltiples dispositivos en la sección **Dispositivos recientes** de un [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

Al segmentar con filtros dependientes del dispositivo (modelo de dispositivo, sistema operativo del dispositivo y versión de la aplicación), tu segmento contendrá a todos los usuarios que coincidan con tus criterios de filtro. Estos usuarios recibirán un mensaje en todos sus dispositivos, incluidos los que pueden no cumplir tus criterios de filtro. Por ejemplo, supongamos que el Usuario A tiene dos dispositivos: el Dispositivo 1 tiene OS 13.0 y el Dispositivo 2 tiene OS 10.0. Si un segmento se dirige a usuarios con OS 10.0, este usuario formará parte de ese segmento y recibirá mensajes en ambos dispositivos.

### Notificaciones push {#push-notifications}

Puedes especificar que solo se envíe una notificación push a cada usuario. Al [redactar tu mensaje]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#step-4-compose-your-push-message), selecciona **Enviar solo al último dispositivo usado del usuario** en **Configuración adicional**.

!["Configuración adicional" con una casilla de verificación para enviar solo al último dispositivo usado del usuario.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Consideraciones {#considerations}

- **Los mensajes enviados pueden superar el tamaño de la audiencia.** Cuando algunos usuarios tienen más de un dispositivo, cada dispositivo puede recibir un mensaje. Esto causa un número mayor de envíos de mensajes que de usuarios en tu segmento.
- **La pertenencia de un usuario al segmento puede no verse como esperarías.**
    - Un usuario puede ser segmentado en su dispositivo actual basándose en atributos asociados con un dispositivo diferente. Si no esperabas que un usuario recibiera un mensaje, verifica su perfil de usuario para múltiples dispositivos.
    - Un usuario puede haber estado en tu segmento objetivo en el momento del envío, pero debido a comportamientos asociados con cualquiera de sus dispositivos, puede que ya no forme parte de ese segmento después. Esto puede resultar en que un usuario reciba una Campaign o Canvas aunque actualmente no cumpla los criterios del filtro. <br><br>Por ejemplo, un usuario podría recibir un mensaje dirigido a usuarios con la versión de aplicación más reciente de OS 10.0 aunque actualmente tenga OS 13.0. En este caso, el usuario tenía OS 10.0 cuando se envió el mensaje y luego actualizó a OS 13.0 después.<br><br> De manera similar, si un usuario usa posteriormente un dispositivo con una versión de aplicación diferente, su perfil de usuario se actualizará con una nueva versión de aplicación más reciente. Esto podría hacer parecer que el usuario no debería haber calificado para el mensaje, aunque calificó cuando se envió.