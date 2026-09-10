---
nav_title: Capacidad de entrega en dispositivos Android chinos
article_title: Capacidad de entrega push en dispositivos Android chinos
page_order: 10

page_type: reference
description: "Este artículo cubre los matices de la capacidad de entrega push que debes tener en cuenta al dirigirte a usuarios en dispositivos Android fabricados por OEM chinos."
channel: push

---

# Capacidad de entrega push en dispositivos Android chinos {#push-deliverability-for-chinese-android-devices}

> Algunos dispositivos Android fabricados por fabricantes de equipos originales (OEM) chinos, como Xiaomi, OPPO, Vivo y Huawei, optimizan la duración de la batería mediante una gestión agresiva del ciclo de vida de las aplicaciones. Esta optimización puede tener la consecuencia no deseada de cerrar el procesamiento en segundo plano de las aplicaciones, lo que puede reducir la capacidad de entrega de tus notificaciones push.<br><br>Para asegurarte de que el rendimiento de mensajería de tu aplicación funcione como se espera en estos dispositivos, tus equipos de marketing e ingeniería deben colaborar y seguir los pasos descritos en este artículo.

## Pasos para desarrolladores {#steps-for-developers}
Estos OEM realizan sus optimizaciones mediante la terminación agresiva de aplicaciones en segundo plano y bloqueándolas para que no se inicien automáticamente y ejecuten tareas en segundo plano. Como desarrollador, necesitarás configurar tu aplicación para que solicite al usuario que reduzca estas restricciones siempre que sea posible.

Esto se puede lograr haciendo que tu aplicación se inicie automáticamente en el dispositivo de tu usuario final, lo que le da a tu aplicación permiso para ejecutarse en segundo plano y escuchar mensajes de Braze. Lamentablemente, dado que este es un problema específico del OEM y no un problema de Android, no existen API documentadas para mostrar el aviso de permiso de inicio automático para cada OEM.

Para resolver esto, integra una biblioteca como [AutoStarter](https://github.com/judemanutd/AutoStarter) en tu aplicación. AutoStarter es compatible con múltiples fabricantes, lo que te ofrece una forma sencilla de invocar el administrador de permisos de inicio en una amplia variedad de dispositivos. Después de haber integrado AutoStarter, llama a `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para mostrar el administrador de permisos de inicio en el dispositivo de tu usuario final. Acompaña esta acción con un mensaje que anime al usuario final a habilitar el "inicio automático" para tu aplicación. Tu equipo de marketing redactará este mensaje. ¡Consulta la siguiente sección!

## Pasos para especialistas en marketing {#steps-for-marketers}
Después de que tus usuarios acepten recibir notificaciones push, hay pasos adicionales que pueden seguir por su cuenta para mejorar la entrega de mensajes en estos dispositivos. Te recomendamos que, tras tu [mensaje push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), envíes un mensaje dentro de la aplicación dirigido a los usuarios con dispositivos OEM chinos con estos pasos adicionales:

- Habilitar el "inicio automático" para la aplicación
- Desactivar la optimización de batería para la aplicación

### Identificar usuarios en dispositivos OEM chinos {#identifying-users-on-chinese-oem-devices}

Para dirigir tu mensaje dentro de la aplicación a usuarios en dispositivos OEM chinos específicos, utiliza los [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) **Device Model** o **Device OS**:

- **Device Model:** Usa este filtro para dirigirte a los usuarios según el modelo de su teléfono móvil. Por ejemplo, para identificar dispositivos Huawei, utiliza un patrón regex que contenga `huawei` para coincidir con los nombres de modelo. Para instrucciones de configuración paso a paso, consulta [Crear una regex de Device Model para dispositivos Huawei](#build-a-device-model-regex-for-huawei-devices).
- **Device OS:** Usa este filtro para dirigirte a los usuarios según su sistema operativo. Algunos OEM chinos, como Huawei, pueden especificar explícitamente su versión personalizada de Android en el campo de sistema operativo del dispositivo. Para los pasos de verificación, consulta [Verificar los valores de Device OS antes de segmentar](#verify-device-os-values-before-you-target).

#### Crear una regex de Device Model para dispositivos Huawei {#build-a-device-model-regex-for-huawei-devices}

1. Ve a **Audience** > **Segments** y luego crea o edita un Segment.
2. Añade el filtro **Device Model**.
3. Establece el operador en **matches regex**.
4. Introduce `huawei` para coincidir con los nombres de modelo Huawei.
5. (Opcional) Si también quieres incluir dispositivos de la marca Honor, usa `(huawei|honor)`.

Para más información sobre el comportamiento de las expresiones regulares en Braze y la prueba de patrones, consulta [Expresiones regulares]({{site.baseurl}}/user_guide/audience/segments/regex).

#### Verificar los valores de Device OS antes de segmentar {#verify-device-os-values-before-you-target}

Algunas variantes de OEM pueden reportar nombres de sistema operativo personalizados en los metadatos del dispositivo. Dado que este valor puede variar según el modelo de dispositivo y la distribución de Android, verifica lo que tus usuarios envían en Braze antes de crear el Segment:

1. Ve a **Search Users** y abre un perfil de un usuario objetivo conocido.
2. En la pestaña **Overview**, revisa **Recent devices** y comprueba el valor del sistema operativo mostrado para ese dispositivo.
3. Copia la cadena exacta del sistema operativo en tu filtro de Segment:
   - Usa **Device OS** cuando necesites una coincidencia exacta o basada en regex de la cadena del sistema operativo.
   - Usa **Device OS Version Number** cuando necesites rangos de versión numéricos.
4. En el creador de Segments, usa **User Lookup** para confirmar que los usuarios de prueba coinciden como se esperaba.

Para más detalles sobre dónde encontrar los metadatos del dispositivo en los perfiles, consulta [Perfiles de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Para más detalles sobre cómo probar la lógica de segmentación, consulta [Crear un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).