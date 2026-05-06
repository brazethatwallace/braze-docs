---
nav_title: Campañas desencadenadas por API y basadas en acciones
article_title: Probar campañas desencadenadas por API y basadas en acciones
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo probar campañas desencadenadas por API y basadas en acciones."

---

# Campañas desencadenadas por API y basadas en acciones

> Al configurar campañas, siempre es una buena práctica probar tus mensajes antes de lanzarlos. Este artículo de referencia cubre la creación de un segmento de usuarios de prueba que te permitirá inspeccionar solicitudes de API, cargas útiles y ver registros de capacidad de entrega.

## Paso 1: Crear un segmento de usuarios de prueba

La única forma de probar el desencadenamiento de una campaña con la API o un evento personalizado es poner la campaña en vivo. Como parte del lanzamiento de una nueva campaña, recomendamos encarecidamente añadir un segmento de usuarios de prueba a las campañas al probar la capacidad de entrega del desencadenamiento. Esto proporcionará una red de seguridad, asegurando que incluso si una campaña se envía accidentalmente, solo llegará a usuarios internos.

1. **Importar usuarios de prueba**<br>Los usuarios de prueba pueden importarse a Braze a través de un CSV o una solicitud por lotes única a través de [Postman]({{site.baseurl}}/api/postman_collection/). Al importar estos usuarios, recomendamos establecer un atributo personalizado en sus perfiles (como `internal_test_user: true`) que pueda usarse para crear un segmento de grupo de prueba. <br><br>
2. **Añadir usuarios de prueba como usuarios de prueba reconocidos por Braze**<br>[Marcar tus usuarios de prueba como usuarios de prueba reconocidos por Braze]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/) en el dashboard te da acceso a registros detallados para cada usuario, lo que te permite inspeccionar solicitudes de API, sus cargas útiles y ver registros de capacidad de entrega. Estos registros pueden ayudarte a determinar si hubo algún problema al entregar campañas a los usuarios finales. <br><br>
3. **Crear segmento**<br>Para crear un segmento de usuarios de prueba, crea un segmento de usuarios con el atributo personalizado `internal_test_user` establecido en `true`. Este segmento puede eliminarse cuando la campaña esté en vivo. 

## Paso 2: Probar envíos

A continuación, puedes hacer un envío de prueba desde el panel de Braze o usar Inbox Vision (solo correo electrónico) para ver cómo será el diseño mientras la campaña aún está en modo borrador. Luego puedes enviar la campaña a tu segmento de usuarios de prueba para verificar que se comporta como se espera. Independientemente de si la campaña es desencadenada por API o basada en acciones, usa Postman para enviar una solicitud única a la API de Braze, desencadenando la campaña. 

## Paso 3: Usar los registros de Braze para inspeccionar los resultados de entrada

Usa los registros de Braze para solucionar problemas de desencadenamiento, envío y eventos. 
- El [registro de eventos de usuario]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/) te mostrará la carga útil sin procesar de la solicitud de desencadenamiento por API, el evento personalizado que desencadena la campaña y cualquier propiedad de desencadenamiento o del evento asociada.
- El [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) registrará cualquier error y te ayudará a entender por qué un mensaje en particular puede no haberse entregado.

## Paso 4: Quitar el segmento de prueba y lanzar la campaña

Una vez que el mensaje se desencadena y se renderiza correctamente con todos los clics en enlaces registrados, puedes quitar el segmento y actualizar la campaña. Si prefieres iniciar la campaña desde cero para que las pocas impresiones de los usuarios de prueba no se incluyan, puedes duplicar la campaña y reiniciarla sin el segmento de usuarios de prueba.