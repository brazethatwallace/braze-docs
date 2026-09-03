---
nav_title: Outgrow
article_title: Outgrow
alias: /partners/outgrow/
description: "Este artículo proporciona una guía completa sobre la configuración de una integración nativa entre Outgrow y Braze para mejorar la sincronización de datos de usuario y las campañas personalizadas."
page_type: partner
search_tag: Partner
---

# Outgrow

> [Outgrow](https://outgrow.co/) es una plataforma de contenido interactivo que te permite crear cuestionarios, calculadoras, encuestas y otros tipos de contenido atractivo para recopilar datos de usuario e información. La integración de Braze y Outgrow te permite transferir automáticamente los datos de usuario de Outgrow a Braze, habilitando campañas altamente personalizadas y dirigidas.

Cuando utilizas la integración de Braze y Outgrow para contenido interactivo, las ventajas que obtienes incluyen:

- **Personalización mejorada**: Recopila datos de cuestionarios, encuestas y calculadoras de Outgrow que puedan mapearse a atributos personalizados en Braze. Estos datos permiten una segmentación precisa y campañas personalizadas.
- **Sincronización de datos en tiempo real**: Recibe datos de Outgrow en Braze en tiempo real, lo que te permite actuar de inmediato sobre la información de los usuarios. Esto permite un seguimiento puntual o mensajes personalizados basados en las interacciones más recientes de los usuarios.
- **Gestión de datos optimizada**: Automatiza la transferencia de datos entre Outgrow y Braze, eliminando las exportaciones e importaciones manuales de datos, reduciendo las discrepancias de datos y ahorrando tiempo.
- **Mejora de la experiencia del usuario**: Aprovecha la información de los usuarios para crear experiencias más relevantes, que conduzcan a una mayor satisfacción, retención y LTV.
- **Segmentación y orientación flexibles**: Perfecciona la segmentación en Braze utilizando los datos de Outgrow, lo que te permite dirigirte a los usuarios en función de interacciones específicas (como las puntuaciones de los cuestionarios o las respuestas a las encuestas) para crear campañas que resuenen entre tus usuarios.

## Requisitos previos {#prerequisites}

Antes de configurar la integración de Outgrow y Braze, confirma que tienes lo siguiente:

| Requisito | Descripción |
|-------------|-------------|
| **Cuenta de Outgrow** | Una cuenta de Outgrow registrada para configurar y administrar el contenido interactivo y la configuración de transferencia de datos |
| **Cuenta de Braze** | Una cuenta de Braze con acceso a las credenciales de la REST API |
| **Clave de API** | Una clave de API de Braze con el permiso `users.track` para habilitar la transferencia de datos de usuario |
| **Atributos personalizados en Braze** | Atributos personalizados configurados en Braze para captar las respuestas de Outgrow (como puntuaciones de cuestionarios, segmentos y otros) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Sigue estos pasos para configurar la integración de Braze y Outgrow:

### Paso 1: Generar la clave de API de Braze {#step-1-generate-braze-api-key}

1. En tu cuenta de Braze, ve a **Consola para desarrolladores** > **Configuración de API**.
2. Selecciona **Crear nueva clave de API**.
3. Pon un nombre a tu clave de API, activa el permiso `users.track` y guarda la clave de API.

### Paso 2: Configurar la integración de Braze en Outgrow {#step-2-configure-the-braze-integration-in-outgrow}

1. Inicia sesión en tu cuenta de Outgrow.
2. En el panel, ve a **Integrations**.
3. En la lista de integraciones disponibles, selecciona **Braze**.
4. Introduce tu **Braze API Key** y la **REST API Endpoint URL**:
   - **API Key**: Introduce la clave de API que se generó en Braze
   - **REST Endpoint URL**: Introduce el endpoint de tu instancia de Braze (por ejemplo, `https://rest.iad-01.braze.com`)
5. Selecciona **Save** para activar la integración.

### Paso 3: Mapear datos de Outgrow a atributos de Braze {#step-3-map-outgrow-data-to-braze-attributes}

En Outgrow, puedes mapear respuestas de contenido interactivo (como resultados de cuestionarios, segmentos personalizados o puntuaciones de participación) a atributos personalizados de Braze.

1. En la **Integration Settings** de Outgrow para Braze, define qué respuestas de Outgrow mapear a atributos de Braze.
2. Asegúrate de que cada respuesta seleccionada se alinea con un atributo personalizado en Braze. Por ejemplo:
   - La puntuación del cuestionario se mapea a `outgrow_quiz_score`.
   - El segmento personalizado se mapea a `outgrow_custom_segment`.
3. Guarda tu configuración de mapeado.

### Paso 4: Probar la integración {#step-4-test-the-integration}

Tras configurar la integración, realiza una prueba para confirmar que los datos se transfieren correctamente de Outgrow a Braze.

1. Publica una experiencia de Outgrow (como un cuestionario o una calculadora) y complétala como usuario de prueba.
2. En tu cuenta de Braze, ve a la sección **Perfil de usuario** y comprueba si hay atributos actualizados (como `outgrow_quiz_score` o `outgrow_custom_segment`).
3. Verifica que los datos se rellenan correctamente con los atributos personalizados adecuados.

## Uso de los datos de Outgrow en Braze para segmentación y orientación {#using-outgrow-data-in-braze-for-segmentation-and-targeting}

### Crear segmentos en Braze con datos de Outgrow {#creating-segments-in-braze-with-outgrow-data}

Con la integración, puedes crear segmentos en Braze basados en atributos personalizados rellenados a partir de las respuestas de Outgrow.

1. En Braze, ve a **Participación** > **Segments** y selecciona **Crear nuevo segmento**.
2. Nombra tu segmento y establece filtros basados en los datos de Outgrow. Por ejemplo:
   - Filtra por `outgrow_quiz_score` para dirigirte a los usuarios que hayan superado un determinado umbral.
   - Filtra por `outgrow_custom_segment` para dirigirte a los usuarios que pertenecen a un segmento determinado definido por Outgrow.
3. Guarda tu segmento para utilizarlo en Campaigns y Canvas.

### Lanzar campañas con segmentos definidos por Outgrow {#launching-campaigns-with-outgrow-defined-segments}

Puedes utilizar los segmentos personalizados creados a partir de los datos de Outgrow para personalizar tus campañas en Braze y dirigirte a los usuarios en función de sus respuestas al contenido interactivo. Para hacerlo y crear una experiencia de usuario más personalizada, sigue estos pasos:

1. En Braze, ve a **Participación** > **Campaigns**.
2. Selecciona **Create Campaign** y elige el tipo de campaña (correo electrónico, push, mensaje dentro de la aplicación u otros).
3. En el paso de segmentación de la audiencia, selecciona el segmento creado a partir de los atributos de Outgrow (como usuarios con puntuaciones específicas en el cuestionario o segmentos concretos).
4. Personaliza el contenido y la configuración de tu campaña, y luego lánzala.

## Solución de problemas comunes {#troubleshooting-common-issues}

| Problema | Solución |
|-------|----------|
| **Los datos no se transfieren a Braze** | Verifica que la clave de API y la URL del endpoint son correctas en tu configuración de integración de Outgrow. Asegúrate de que la clave de API tiene el permiso `users.track` activado. |
| **Mapeado incorrecto de los datos** | Asegúrate de que cada respuesta de Outgrow mapeada corresponde a un atributo personalizado de Braze válido y que los nombres de los atributos coinciden exactamente. |
| **El segmento no se filtra correctamente** | Asegúrate de que los atributos personalizados en Braze están correctamente configurados y reciben datos. Vuelve a comprobar la lógica de filtrado de tu segmento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas comunes" }

## Consideraciones adicionales {#additional-considerations}

- **Privacidad de datos**: Cumple con la normativa sobre privacidad de datos (como el RGPD y la CCPA) al transferir datos de usuario entre plataformas.
- **Límites de velocidad**: Los datos de Outgrow se envían a Braze en tiempo real, pero pueden aplicarse límites de velocidad de la API de Braze para grandes volúmenes de datos. Planifica en consecuencia para experiencias de alto tráfico.
- **Configuración de atributos personalizados**: Verifica que los atributos personalizados de Braze utilizados en esta integración están correctamente configurados para capturar los datos enviados desde Outgrow.

Para obtener ayuda adicional, consulta la [documentación de Outgrow](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) o ponte en contacto con el soporte de Outgrow.