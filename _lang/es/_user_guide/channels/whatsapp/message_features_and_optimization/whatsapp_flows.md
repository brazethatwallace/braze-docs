---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 3
description: "Este artículo de referencia cubre los pasos necesarios para crear y configurar un mensaje de WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows es una mejora del canal de WhatsApp existente que te permite crear experiencias de mensajería interactivas y dinámicas. Esta página proporciona instrucciones paso a paso para usar WhatsApp Flows.

## Configurar WhatsApp Flows {#setting-up-whatsapp-flows}

1. Inicia sesión en tu cuenta de Meta.
2. Crea Flows desde una de las dos ubicaciones principales:
    - **Account tools:** Ve a la pestaña **Flows** para ver el ID del Flow y crear uno nuevo.
    - **Manage templates:** Este es el método recomendado para crear Flows. Aquí puedes generar plantillas y seleccionar una opción de Flow durante el proceso de creación de la plantilla.

![Administrador de WhatsApp con una página para crear una plantilla de Flows.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}
3. Selecciona un Flow existente o crea uno. Si creas un Flow, elige entre dos opciones:
  - **Custom Form:** Para requisitos específicos
  - **Pre-designed Elements:** Para una configuración más rápida

## Configurar mensajes y respuestas de WhatsApp Flow {#configuring-whatsapp-flow-messages-and-responses}

{% tabs local %}
{% tab Mensaje de plantilla %}

1. En un Canvas de Braze, crea un paso de mensaje de WhatsApp que use la plantilla de mensaje que contiene el Flow correspondiente.
2. Continúa creando tu plantilla. Si es necesario, añade medios, contenido variable o ambos a tu mensaje. Tu selección de Flow se elige cuando se crea la plantilla, por lo que no se requiere información adicional para la experiencia del Flow.

![Creador de mensajes de WhatsApp usando una plantilla de WhatsApp Flow.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Mensaje de respuesta %}

1. En un Canvas de Braze, crea un paso de mensaje de WhatsApp que use un mensaje de respuesta y un mensaje de Flow.

![Un paso de mensaje para un tipo de mensaje de respuesta de WhatsApp y un diseño de mensaje de Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Selecciona el Flow correspondiente y luego continúa creando tu mensaje.

![Un creador de mensajes de respuesta de Flow con un menú desplegable expandido para seleccionar un Flow.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Vista previa del Flow {#preview-flow}

Antes de lanzar un Canvas con un Flow, puedes seleccionar **Preview Flow** para previsualizar el Flow directamente en Braze y confirmar que se comporta como se espera. También puedes interactuar con el Flow en la vista previa para experimentar cómo un usuario navegaría por el Flow, y luego hacer ajustes en tiempo real. Si un Flow contiene varias páginas, puedes interactuar con cada una.

![Ventana de vista previa que muestra un formulario para que un usuario complete su registro.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Guardar la respuesta completa del Flow {#full-flow}

Al incorporar un mensaje de WhatsApp Flow en un Canvas o una Campaign de Braze, es posible que quieras capturar y utilizar información específica que los usuarios envían a través del Flow. Braze necesita recibir información adicional sobre la estructura de la respuesta del usuario, específicamente la forma esperada de la respuesta JSON, para generar el esquema de atributo personalizado anidado (NCA) requerido.

### Paso 1: Generar el atributo personalizado del Flow {#step-1-generate-the-flow-custom-attribute}

{% tabs local %}
{% tab Método recomendado %}

La forma más sencilla de proporcionar a Braze la información sobre la estructura de la respuesta es guardar la respuesta del Flow como un atributo personalizado y completar un envío de prueba.

#### Usar un Flow que no se ha utilizado en Braze {#using-a-flow-that-hasnt-been-used-in-braze}

Si estás usando un Flow que no se ha utilizado previamente en Braze, al ver la sección **Flow Custom Attribute** en **Compose Messages**, es posible que no veas ninguna información. Esto significa que el esquema aún no se ha generado.

![Sección de Meta Flow con una opción para ver el atributo personalizado del Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Para resolver esto, haz lo siguiente:

1. Completa la configuración de tu paso de mensaje de WhatsApp.
2. Confirma que marcaste **Save Flow responses as a custom attribute**.
3. Envíate un mensaje de prueba y completa el Flow como usuario.

Ahora, Braze tiene la forma del JSON de respuesta del Flow y puede generar el atributo personalizado.

{% endtab %}
{% tab Métodos alternativos %}

Usa el editor JSON avanzado para guardar atributos de la respuesta del Flow en atributos personalizados, o usa un Canvas de varios pasos para guardar la respuesta en un atributo personalizado anidado.

{% subtabs %}
{% subtab Editor JSON avanzado %}

En el editor JSON avanzado, introduce {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, donde "flow_1" es el atributo personalizado en el que deseas guardar el Flow.

![Paso de Actualización de usuario con un editor JSON avanzado.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab Editor de interfaz %}

1. Confirma que ya has creado un atributo personalizado con el tipo de datos de objeto ("flow_1" en este ejemplo) dentro de la configuración de datos de tu espacio de trabajo.
2. En el editor de interfaz, usa el Liquid {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} para rellenar el atributo personalizado y guardar toda la respuesta del Flow del usuario en él. Necesitas rellenar el valor de la clave como {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} antes de seleccionar el atributo personalizado que creaste.

![Paso de Actualización de usuario que usa el editor de interfaz.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Después de que Braze reciba una respuesta del Flow, guardaremos el atributo personalizado anidado con el nombre prescrito en el perfil de usuario. Ese atributo personalizado se puede utilizar al crear Canvas.

![Una ventana que muestra el contenido de un atributo personalizado "flow_1".]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 2: Ver la respuesta guardada del Flow {#step-2-view-the-saved-flow-response}

Cuando el Flow se completa, Braze crea automáticamente un atributo personalizado del Flow con un nombre basado en el ID del Flow. Luego puedes ir al perfil de usuario para ver la respuesta guardada del Flow como un objeto anidado en la sección **Custom Attributes**.

Después de que se genera el esquema, la sección **Custom Attribute** del Flow mostrará la estructura esperada, incluyendo los tipos de datos anticipados para cada respuesta (por ejemplo, "String" o "String Array").

![Ventana de detalles de atributos personalizados del Flow con menú desplegable de esquema.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Consideraciones {#considerations}

- **Atributos existentes:** Si ya se ha generado un atributo personalizado para un Flow en particular, el Flow se cargará con la información del atributo disponible. En estos casos, no necesitas enviar un mensaje de prueba para generar el esquema, ya que Braze ya reconoce los mensajes de respuesta esperados.
- **Cambios en el Flow:** Si realizas cambios en el Flow después de que se genera el esquema, debes enviar un mensaje de prueba adicional para que Braze pueda entender que la forma de la respuesta del Flow ha cambiado y ajustar la estructura del atributo en consecuencia. Esta acción está limitada a una vez cada 24 horas.
- **Consistencia:** El atributo personalizado del Flow generado es consistente y será el mismo atributo para este Flow específico, independientemente del Canvas en el que se use.
- **Opción manual:** No es obligatorio seleccionar la casilla **Save Flow responses as a custom attribute**. Puedes generar manualmente el atributo personalizado [guardando campos específicos de las respuestas del Flow en un atributo personalizado específico](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), lo que evita duplicar pasos del usuario.

## Guardar campos específicos de las respuestas del Flow en un atributo personalizado específico {#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute}

### Paso 1: Crear una ruta de acción {#step-1-create-an-action-path}

Crea un paso de Canvas de [ruta de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) o una Campaign basada en acciones. Selecciona un desencadenador **Send a WhatsApp inbound message** y la condición **Responded to Flow**, y luego selecciona el Flow relevante o **Any Flow**.

![Un desencadenador para usuarios que enviaron un mensaje entrante de WhatsApp y respondieron a cualquier Flow.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Paso 2: Extraer campos de las respuestas del Flow {#step-2-extract-fields-from-flow-responses}

Puedes usar atributos personalizados anidados o la etiqueta de Liquid `json_parse` para extraer campos específicos de las respuestas del Flow.

{% tabs %}
{% tab Atributos personalizados anidados %}

Para guardar partes específicas de la respuesta del Flow del usuario, completa todos los pasos en [Guardar la respuesta completa del Flow](#full-flow), **incluyendo el lanzamiento del Canvas**. El Canvas debe lanzarse para crear el atributo personalizado anidado que vas a referenciar. Después de lanzar el Canvas y completar un Flow, sigue estos pasos:

1. Crea un paso posterior de Actualización de usuario que use el editor de interfaz.
2. Selecciona **Add Personalization**, luego selecciona **Nested Custom Attribute** y el atributo de nivel superior correspondiente donde se almacena el Flow.

![Paso de Actualización de usuario con una personalización de atributos personalizados anidados.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3. Selecciona el atributo clave que deseas guardar e inserta el Liquid en el campo **Key Value**.

![Ventana para "flow_1" con atributos para seleccionar.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. Elige el atributo donde deseas almacenarlo.
5. Envía un mensaje de prueba para probar el Flow.

{% endtab %}
{% tab Función de análisis %}

Usa la etiqueta de Liquid `json_parse` para extraer respuestas específicas del Flow. Por ejemplo, puedes extraer el token del Flow y las opciones seleccionadas para personalizar un mensaje de seguimiento.

En el editor de interfaz, selecciona lo siguiente:

- **Attribute Name:** TU_ATRIBUTO_PERSONALIZADO (en este ejemplo: "First_name")
- **Action:** Update
- **Key Value:** {% raw %} `{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}`{% endraw %}

![Creador de mensajes de WhatsApp con un componente "Add Personalization" para insertar una personalización de propiedades de WhatsApp con el atributo personalizado `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Cuando estés listo, envía un mensaje de prueba para probar el Flow. ¡Luego, lanza el Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Un nuevo mensaje de WhatsApp "borra" la capacidad del Canvas de usar (y reutilizar) la respuesta de Liquid del Flow, así que asegúrate de que los mensajes de seguimiento estén después de todos los pasos de Actualización de usuario, webhooks u otros pasos que usen la respuesta de Liquid del Flow.
{% endalert %}

## Añadir una etiqueta de personalización de Flow {#adding-a-flow-personalization-tag}

Para usar la respuesta del Flow a través de Liquid con [etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), completa los siguientes pasos:

1. Al redactar tu mensaje de WhatsApp, selecciona <i class="fas fa-plus-circle" aria-label="Añadir personalización"></i> **Add Personalization** para abrir la ventana **Add Personalization**.
2. Selecciona **WhatsApp Properties** para el tipo de personalización e **inbound_flow_response** para el atributo personalizado. Esto se puede usar para guardar información en perfiles de usuario, incluirla en mensajes o reenviarla a otros servicios, como webhooks.

![Creador de mensajes de WhatsApp con un componente "Add Personalization" para insertar una personalización de propiedades de WhatsApp con el atributo personalizado inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Si tienes preguntas o necesitas más ayuda, ponte en contacto con [Soporte]({{site.baseurl}}/braze_support).