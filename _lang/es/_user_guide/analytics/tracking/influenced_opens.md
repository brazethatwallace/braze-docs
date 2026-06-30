---
nav_title: Influenced Opens
article_title: Influenced Opens
page_order: 2
page_type: reference
description: "Este artículo de referencia explica las Influenced Opens y cómo puedes realizar un seguimiento de las mismas para proporcionar un mayor nivel de detalle en tus campañas push."
channel: push

---

# Influenced Opens {#influenced-opens}

> Cuando un usuario selecciona una notificación push y es dirigido a tu aplicación, Braze lo registra como un Direct Opens. Cuando los usuarios no seleccionan la notificación pero aún así pueden verse influidos por la notificación push, Braze lo registra como un Influenced Opens. Esto proporciona un mayor nivel de detalle sobre el efecto de tus campañas push.

## Cómo funciona {#how-it-works}

En esencia, las Influenced Opens miden el número de usuarios que abren la aplicación tras recibir una notificación sin seleccionarla. Como no hay una acción directa que vincule la notificación con la apertura de la aplicación, se registra una Influenced Opens si el usuario abre la aplicación menos de treinta minutos después de recibir la notificación push o en menos de la mitad del tiempo medio transcurrido desde la última sesión de ese usuario.

Por ejemplo, supongamos que envías una notificación push a los usuarios de tu aplicación. Si un usuario que normalmente abre la aplicación 30 veces al día abre tu aplicación seis horas después de recibir el push, el push recibe poco o ningún crédito por influir en la apertura. Sin embargo, si un usuario que normalmente utiliza la aplicación una vez al mes la abre seis horas después de recibir el push, la apertura tiene muchas más posibilidades de contabilizarse como una Influenced Opens.

Esto difiere de establecer las aperturas de aplicaciones como un evento de conversión para una campaña push. Para las conversiones, todas las aperturas dentro de la ventana de conversión se atribuirán a la campaña. Las Influenced Opens configuran una ventana de tiempo y un crédito de atribución basados en el comportamiento de un usuario individual.

## Ver las Influenced Opens de una campaña {#viewing-a-campaigns-influenced-opens}

Las Influenced Opens se suman a las Direct Opens de una campaña para obtener un número de aperturas totales. Esto se muestra en la página **Campaign Analytics** de una campaña push. Las aperturas totales y las Direct Opens se muestran en las secciones de rendimiento de los mensajes y **Historical Performance**. Las Influenced Opens son la diferencia entre las dos medidas.

![Estadísticas de Influenced Opens en la página de detalles de una campaña]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Para más información sobre el seguimiento de aperturas, consulta la sección de seguimiento de conversiones de nuestras [mejores prácticas para push]({{site.baseurl}}/user_guide/channels/push/best_practices).