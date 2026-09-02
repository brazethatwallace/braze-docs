---
nav_title: Capacidad de entrega en dispositivos Android chinos
article_title: Capacidad de entrega push en dispositivos Android chinos
page_order: 10

page_type: reference
description: "Este artículo cubre los matices de la capacidad de entrega push que debes tener en cuenta al dirigirte a usuarios en dispositivos Android fabricados por OEM chinos."
channel: push

---

# Capacidad de entrega push en dispositivos Android chinos {#push-deliverability-for-chinese-android-devices}

> Algunos dispositivos Android fabricados por fabricantes de equipos originales (OEM) chinos, como Xiaomi, OPPO y Vivo, optimizan la duración de la batería mediante una gestión agresiva del ciclo de vida de las aplicaciones. Esta optimización puede tener la consecuencia no deseada de cerrar el procesamiento en segundo plano de las aplicaciones, lo que puede reducir la capacidad de entrega de tus notificaciones push.<br><br>Para asegurarte de que el rendimiento de mensajería de tu aplicación funcione como se espera en estos dispositivos, tus equipos de marketing e ingeniería deben colaborar y seguir los pasos descritos en este artículo.

## Pasos para desarrolladores {#steps-for-developers}
Estos OEM realizan sus optimizaciones cerrando agresivamente las aplicaciones en segundo plano y bloqueándolas para que no se inicien automáticamente y ejecuten tareas en segundo plano. Como desarrollador, necesitarás configurar tu aplicación para que solicite al usuario que alivie estas restricciones siempre que sea posible.

Esto se puede lograr haciendo que tu aplicación se inicie automáticamente en el dispositivo del usuario final, lo que le otorga a tu aplicación permiso para ejecutarse en segundo plano y escuchar mensajes de Braze. Desafortunadamente, dado que este es un problema específico del OEM y no un problema de Android, no existen API documentadas para mostrar el aviso de permiso de inicio automático para cada OEM.

Para resolver esto, integra una biblioteca como [AutoStarter](https://github.com/judemanutd/AutoStarter) en tu aplicación. AutoStarter es compatible con múltiples fabricantes, lo que te ofrece una forma sencilla de invocar el administrador de permisos de inicio en una amplia variedad de dispositivos. Después de integrar AutoStarter, llama a `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para abrir el administrador de permisos de inicio en el dispositivo del usuario final. Acompaña esta acción con un aviso que anime al usuario final a habilitar el "inicio automático" para tu aplicación. Tu equipo de marketing redactará este mensaje; ¡consulta la siguiente sección!

## Pasos para especialistas en marketing {#steps-for-marketers}
Después de que tus usuarios acepten recibir notificaciones push, hay pasos adicionales que pueden seguir por su parte para mejorar la entrega de mensajes en estos dispositivos. Te recomendamos que complementes tu [mensaje de preparación push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) con un mensaje dentro de la aplicación dirigido a usuarios en dispositivos OEM chinos con estos pasos adicionales:

- Habilitar el "inicio automático" para la aplicación
- Desactivar la optimización de batería para la aplicación

Para amplificar aún más tu mensaje, añade otros canales para recuperar información de notificaciones push no abiertas a través de canales fuera de la aplicación como servicio de mensajes cortos, WhatsApp y LINE, y canales dentro de la aplicación como mensajes dentro de la aplicación y Content Cards. Tus usuarios podrán ver cualquier cosa que se hayan perdido la próxima vez que abran la aplicación.