En el panel de Braze, ve a **Configuración de datos** > **Transformación de datos**.

Selecciona **Crear transformación** para darle un nombre a tu transformación y, a continuación, elige tu experiencia de edición.

![Detalles de transformación con la opción de elegir "Utilizar una plantilla" o "Empezar de cero" para tu experiencia de edición.]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

Selecciona **Utilizar una plantilla** para examinar una biblioteca de plantillas, incluidos los ejemplos de transformación de datos. O bien, selecciona **Empezar de cero** para cargar una plantilla de código predeterminada.

Si empiezas de cero, elige un destino para tu transformación. Todavía puedes insertar una plantilla de código de la biblioteca de plantillas.

{% details Más sobre destinos %}
* **POST: Track users:** Transforma los webhooks de una plataforma de origen en actualizaciones del perfil de usuario, como atributos, eventos o compras.
* **PUT: Update multiple catalog items:** Transforma los webhooks de una plataforma de origen en actualizaciones de elementos del catálogo.
* **DELETE: Delete multiple catalog items:** Transforma los webhooks de una plataforma de origen en eliminaciones de elementos del catálogo.
* **PATCH: Edit multiple catalog items:** Transforma los webhooks de una plataforma de origen en ediciones de elementos del catálogo.
* **POST: Send messages immediately via API Only:** Transforma los webhooks de una plataforma de origen para enviar mensajes inmediatos a usuarios designados.
{% enddetails %}

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="additional templates or destinations" %}
{% endalert %}

Después de crear tu transformación, verás la vista detallada de la transformación. Aquí puedes ver el webhook más reciente recibido para esta transformación en **Webhook details** y un espacio para escribir tu código de transformación en **Transformation code**.

{% if include.location == "typeform" %}

![Un ejemplo de detalles de webhook y código de transformación.]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

Copia tu **URL del webhook** para utilizarla en el siguiente paso.