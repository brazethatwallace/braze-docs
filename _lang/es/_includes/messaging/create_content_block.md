{% if include.location == "dnd" %}

1. Ve a **Contenido** > **Content Block**. Selecciona <i class="fas fa-plus"></i> **Crear Content Block** y selecciona **Content Block de arrastrar y soltar**.
2. Arrastra y suelta los [bloques de editor]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks) para construir un Content Block de arrastrar y soltar.
3. Arrastra y suelta un bloque de formato de la pestaña **Filas** en el editor para crear el diseño de tu Content Block. <br><br> ![Creador de Content Blocks de arrastrar y soltar.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Añade Content Blocks de arrastrar y soltar según necesites para construir tus campañas de correo electrónico.
5. Después de crear tu Content Block, selecciona **Listo**.
6. Dale un nombre a tu Content Block. Este nombre se rellenará automáticamente como parte de la **etiqueta de Liquid del Content Block**.
7. (Opcional) Añade una descripción.
8. Selecciona la pestaña **Vista previa** para ver cómo aparecerá tu Content Block. Opcionalmente, selecciona **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que sea necesario regenerarlo.<br><br> ![Pestaña de vista previa del creador de Content Blocks de arrastrar y soltar.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Selecciona **Lanzar Content Block**.

{% elsif include.location == "html" %}

1. Ve a **Contenido** > **Content Block**. Selecciona <i class="fas fa-plus"></i> **Crear Content Block** y selecciona **Editor de código HTML**.
2. Introduce tu HTML en la pestaña **HTML** o construye tu Content Block en la pestaña **Clásico**. <br><br> ![Creador del editor de código HTML.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. Después de crear tu Content Block, selecciona **Listo**.
4. Introduce un nombre para tu Content Block. Este nombre se rellenará automáticamente como parte de la **etiqueta de Liquid del Content Block**.
5. (Opcional) Añade una descripción.
6. Selecciona la pestaña **Vista previa** para ver cómo aparecerá tu Content Block. Opcionalmente, selecciona **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que sea necesario regenerarlo.<br><br> ![Pestaña de vista previa del creador del editor de código HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. Selecciona **Lanzar Content Block**.

{% endif %}