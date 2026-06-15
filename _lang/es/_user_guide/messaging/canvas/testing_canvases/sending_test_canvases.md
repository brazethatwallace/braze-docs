---
nav_title: Enviar Canvas de prueba
article_title: Enviar Canvas de prueba
page_order: 1
description: "Este artículo de referencia explica cómo probar un Canvas antes de lanzarlo y las mejores prácticas."
page_type: reference
tool: Canvas
---

# Enviar Canvas de prueba

> Después de [crear tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/), hay varias comprobaciones que puedes realizar antes de lanzarlo, dependiendo de detalles como el tamaño de tu audiencia o el número de filtros de segmentación.

Siempre que sea posible, Braze recomienda probar un Canvas antes de lanzarlo. Esta prueba normalmente se realizará en tu entorno de Braze. Probar tu Canvas puede implicar duplicarlo, hacer que los usuarios de prueba recorran el recorrido del usuario y verificar si el comportamiento del usuario se alinea con lo que has definido en tu Canvas.

## Paso 1: Crea tu plan de pruebas

Crear un plan de pruebas es esencial antes de comenzar a probar tu Canvas. Un plan de pruebas puede ayudarte a identificar y hacer seguimiento de áreas específicas del recorrido de tu Canvas.

A medida que construyas tu plan de pruebas, considera las siguientes preguntas:
- ¿Se ha creado al menos un usuario para cada rama y ruta del Canvas?
- ¿Se están utilizando segmentos en tu Canvas?
	- Si se utilizan segmentos, puede haber requisitos previos para que un usuario entre en el Canvas antes de ser elegible para un recorrido de usuario.
- ¿Los mensajes en el Canvas de prueba tienen algún Liquid en los títulos de los mensajes que extraigan el ID de usuario o la dirección de correo electrónico para asegurar que sea fácil identificar tanto el mensaje como el usuario con fines de prueba?

## Paso 2: Identifica los usuarios de prueba

A continuación, identifica un conjunto de usuarios de prueba que recorrerán los pasos del Canvas sin enviar realmente mensajes a tus usuarios previstos. Los usuarios de prueba pueden ser direcciones de correo electrónico existentes que no se utilizan para servicios reales en tu dashboard de Braze, o nuevas direcciones de correo electrónico que se usan exclusivamente con fines de prueba.

## Paso 3: Configura tu Canvas

A continuación, es hora de probar tu Canvas. Para mantener organizados tu Canvas original y la información del Canvas de prueba, crea un duplicado de tu Canvas con fines de prueba.

Hay dos formas de probar tu Canvas.

- **Método 1:** En el Canvas duplicado, edita la sección **Audiencia de entrada** del constructor de Canvas para que solo los usuarios de prueba sean elegibles para el Canvas. También puedes introducir tu propia dirección de correo electrónico como usuario de prueba añadiendo el filtro de prueba **Dirección de correo electrónico**. En el ejemplo siguiente, hemos limitado el Canvas a dos usuarios de prueba que han utilizado la aplicación por primera vez hace menos de tres días.

![Un Canvas con una audiencia de entrada de "Usó estas aplicaciones por primera vez hace menos de 3 días" y las direcciones de correo electrónico de dos usuarios de prueba.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Método 2:** [Previsualiza las rutas de los usuarios]({{site.baseurl}}/preview_user_paths/) seleccionando el botón **Test Canvas** en el pie de página del constructor de Canvas.

## Paso 4: Lanza tu prueba

Lanza tu Canvas de prueba para permitir que los usuarios comiencen a entrar. Completa los comportamientos de usuario en tu aplicación que enviarían a los usuarios a través del recorrido correspondiente del Canvas.

Verifica que tus usuarios de prueba estén recibiendo los mensajes previstos de los pasos de tu Canvas. Ten en cuenta que tus usuarios de prueba pueden no recibir un mensaje por razones que incluyen, entre otras:

- No ser elegible para el Grupo de control global
- Limitaciones de limitación de frecuencia
- Pertenencia a segmentos no coincidente
- Mensajes abortados
- Tokens de notificaciones push asociados a diferentes usuarios

Continúa iterando las pruebas del Canvas para asegurarte de que tu Canvas funcione como se espera.

## Consejos generales

### Identifica los pasos de tu Canvas

En algunos casos, un usuario puede recibir potencialmente múltiples mensajes al recorrer un Canvas. Si el retraso entre pasos se ha reducido significativamente para las pruebas, puede que no siempre quede claro qué mensaje se está desencadenando durante la prueba. Asegurarte de que los mensajes de prueba incluyan el nombre del paso o el ID de usuario (usando Liquid) facilitará identificar y confirmar si el mensaje correcto se ha enviado a los usuarios correctos.

### Crea un grupo interno

En lugar de crear usuarios de prueba individuales, puedes crear un [grupo de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/), que es un grupo interno cuyo propósito es revisar el contenido de tu mensaje. Esto incluye un grupo de usuarios que recibirán mensajes de prueba de campañas y Canvas. Luego, puedes añadir este grupo de prueba en el campo **Añadir grupos de prueba de contenido** en **Destinatarios de prueba**.

### Reduce los retrasos de tiempo

Para ayudar a ejecutar las pruebas de manera más eficiente, sugerimos reducir los retrasos de tiempo a minutos o segundos con fines de prueba para que puedas ver los mensajes de manera oportuna. Por ejemplo, permite al menos 2-3 minutos entre pruebas para poder aislar acciones específicas en recorridos específicos del Canvas.

### Aprovecha los bloques de contenido

Si algún contenido se va a repetir en tu marco de pruebas (por ejemplo, Liquid complejo para filtrar usuarios en diferentes pasos del Canvas), intenta guardar este contenido repetido como un [bloque de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). Ahora podrás incluir el bloque de contenido en los pasos individuales del Canvas.

### Usa Postman y el punto de conexión de seguimiento de usuarios

Puedes ejecutar pruebas con Postman y la [colección Postman de Braze]({{site.baseurl}}/api/postman_collection/). Usa el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar y hacer seguimiento de eventos personalizados y compras para tus diversos usuarios de prueba.

Ten en cuenta que el envío de datos a la API de seguimiento de usuarios solo se puede hacer con un ID externo. Por lo tanto, puede que sea necesario añadir los usuarios de prueba como usuarios de prueba dentro de un grupo interno en el dashboard de Braze para que se puedan investigar más a fondo errores específicos.

#### Pruebas para múltiples ramas

Cuando estés probando un Canvas con múltiples ramas que se dirigen a usuarios basándose en diferentes atributos y eventos, sigue este plan de pruebas:

1. Para cada rama, identifica los atributos y eventos que el usuario debe tener para ser incluido en el recorrido del Canvas.
2. Constrúyelos en una carga útil JSON para publicarlos usando el punto de conexión `/users/track`.