{% if include.location == "dnd" %}

1. Ve a **Content** > **Content Block**. Selecciona <i class="fas fa-plus"></i> **Create Content Block** y selecciona **Drag-and-drop Content Block**.
2. Arrastra y suelta los [bloques de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) para construir un bloque de contenido de arrastrar y soltar.
3. Arrastra y suelta un bloque de formato de la pestaña **Rows** en el editor para crear el diseño de tu bloque de contenido. <br><br> ![Compositor de bloques de contenido de arrastrar y soltar.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Añade bloques de contenido de arrastrar y soltar según necesites para construir tus campañas de correo electrónico.
5. Después de crear tu bloque de contenido, selecciona **Done**.
6. Dale un nombre a tu bloque de contenido. Este nombre se rellenará automáticamente como parte de la **Content Block Liquid Tag**.
7. (Opcional) Añade una descripción.
8. Selecciona la pestaña **Preview** para ver cómo aparecerá tu bloque de contenido. Opcionalmente, selecciona **Copy preview link** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que sea necesario regenerarlo.<br><br> ![Pestaña de vista previa del compositor de bloques de contenido de arrastrar y soltar.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Selecciona **Launch Content Block**.

{% elsif include.location == "html" %}

1. Ve a **Content** > **Content Block**. Selecciona <i class="fas fa-plus"></i> **Create Content Block** y selecciona **HTML code editor**.
2. Introduce tu HTML en la pestaña **HTML** o construye tu bloque de contenido en la pestaña **Classic**. <br><br> ![Compositor del editor de código HTML.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. Después de crear tu bloque de contenido, selecciona **Done**.
4. Introduce un nombre para tu bloque de contenido. Este nombre se rellenará automáticamente como parte de la **Content Block Liquid Tag**.
5. (Opcional) Añade una descripción.
6. Selecciona la pestaña **Preview** para ver cómo aparecerá tu bloque de contenido. Opcionalmente, selecciona **Copy preview link** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que sea necesario regenerarlo.<br><br> ![Pestaña de vista previa del compositor del editor de código HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. Selecciona **Launch Content Block**.

{% endif %}