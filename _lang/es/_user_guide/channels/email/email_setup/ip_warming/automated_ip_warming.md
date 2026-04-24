---
nav_title: Calentamiento de IP automatizado
article_title: Calentamiento de IP automatizado
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre el calentamiento de IP automatizado y cómo monitorear tu calentamiento de IP."
channel: email
---

# Calentamiento de IP automatizado

> Usa el calentamiento de IP automatizado para aumentar gradualmente el volumen de correo electrónico desde una nueva dirección IP y construir la reputación del remitente con los proveedores de buzón de entrada.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Cómo funciona

Puedes usar el calentamiento de IP automatizado para aumentar gradualmente tu volumen de envío diario, permitiendo que los proveedores de buzón de entrada aprendan y confíen en tus patrones de envío. Cuando agregas un dominio a tu espacio de trabajo, puedes seleccionar el mosaico **Calentamiento de IP automatizado** en la sección **Retoma donde lo dejaste** de tu dashboard de inicio, y este mosaico permanece ahí durante 60 días.

Braze envía primero a tus suscriptores con mayor interacción, lo que permite que el volumen diario crezca a un ritmo que se ajusta a las mejores prácticas. Luego, Braze rastrea las señales de interacción y capacidad de entrega. Si Braze detecta algún problema, el sistema ajusta tu planificación automáticamente.

{% alert note %}
Solo puedes realizar un calentamiento de IP.
{% endalert %}

## Requisitos previos

Para realizar el calentamiento de IP automatizado, debes contar con lo siguiente:

- Subdominio verificado y direcciones IP activas
- Permisos para ver y lanzar un calentamiento de IP
    - "Ver datos de uso" para ver la sección de calentamiento de IP
    - "Ver plantillas de correo electrónico" para ver y seleccionar las plantillas de correo electrónico para el calentamiento de IP
    - "Administrar configuración del correo electrónico" para lanzar el calentamiento de IP
- "Acceso a campañas"
- "Aprobar y rechazar campañas" si el flujo de trabajo de aprobación para campañas está activado
    - Braze aprueba automáticamente las campañas creadas a partir del calentamiento de IP automatizado en tu nombre.

## Configurar un plan de calentamiento de IP automatizado

### Paso 1: Establecer una planificación

1. En la sección **Información de envío**, selecciona la **Dirección de remitente** para la que deseas calentar las direcciones IP.
2. Ingresa el volumen de envío diario actual y el volumen de envío objetivo.
3. Selecciona la fecha de inicio para el calentamiento de IP automatizado. Esta fecha debe ser al menos un día después de que se lance el plan.
4. Ingresa la hora de envío. Esto envía los mensajes en la zona horaria de la empresa.
5. Selecciona **Siguiente: Segmentos** para continuar la configuración.

![Ejemplo de detalles de planificación.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Paso 2: Seleccionar y clasificar segmentos

1. A continuación, selecciona los segmentos a los que deseas dirigirte. Durante el calentamiento de IP, Braze comienza enviando a tus usuarios con mayor interacción y aumenta gradualmente el volumen de envío con el tiempo, incorporando lentamente segmentos con menor interacción.
2. Luego, arrastra y suelta los segmentos para clasificarlos de mayor a menor interacción. Alta interacción incluye destinatarios que abren y hacen clic en tus correos electrónicos de manera consistente. Baja interacción incluye destinatarios que son inconsistentes en su interacción con tus correos electrónicos o que no han interactuado con tus correos electrónicos en mucho tiempo.
3. Selecciona **Siguiente: Mensajes** para continuar la configuración.

![Dos segmentos seleccionados como objetivo para el calentamiento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Paso 3: Seleccionar los mensajes a enviar

1. Selecciona **Seleccionar plantillas de correo electrónico**.
2. Elige las plantillas de correo electrónico para los mensajes a enviar. El contenido que envíes durante el calentamiento de IP debe fomentar las aperturas y los clics. Recomendamos elegir contenido que haya tenido buena recepción en el pasado. Por ejemplo, puedes usar ofertas promocionales para fomentar la interacción inmediata y las compras.
3. Selecciona **Seleccionar plantillas**. Braze calcula el número de plantillas requeridas antes de que puedas lanzar. Recomendamos proporcionar más plantillas que el mínimo requerido para permitir que el sistema se ajuste ante problemas de capacidad de entrega sin detenerse.
4. Después de agregar el número requerido de plantillas, selecciona **Siguiente: Resumen**.

{% alert important %}
Los cambios realizados en las campañas creadas desde la herramienta de calentamiento de IP (como cambiar la fecha planificada, el segmento o el volumen) no se reflejan en la página de **Resumen** del calentamiento de IP.
{% endalert %}

### Paso 4: Seleccionar eventos de conversión

Puedes definir hasta cuatro de los siguientes eventos de conversión para rastrear. Estos eventos de conversión no se pueden actualizar después de que se haya lanzado el plan de calentamiento de IP automatizado.

- Inicia sesión
- Realiza un pedido
- Realiza un evento personalizado
- Actualiza la aplicación
- Abre correo electrónico
- Hace clic en correo electrónico

A continuación, selecciona la fecha límite de conversión, que es el tiempo máximo que puede transcurrir entre que un usuario entra en una campaña y el evento de conversión.

![Configuración de conversión mostrando la selección de eventos de conversión y la fecha límite de conversión.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Paso 5: Revisar y lanzar

Revisa los detalles de tu plan de calentamiento de IP. Luego, selecciona **Lanzar**.

## Durante el calentamiento de IP activo

Las campañas de calentamiento de IP se crean con 1 a 2 días de anticipación, a menos que estés lanzando un calentamiento de IP para el día siguiente. Estas campañas se nombran automáticamente con el siguiente formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Cuando se alcanza el objetivo de envío diario, el sistema deja de enviar por ese día para proteger tu reputación.

El sistema monitorea tu salud basándose en los siguientes puntos de referencia de la industria:

- La tasa de entrega cae por debajo o es igual al 90 %
- La tasa de apertura es menor al 10 %
- Los rebotes son mayores al 5 %
- Las tasas de quejas por correo no deseado son mayores al 0,04 %

Si las estadísticas están por debajo de nuestros puntos de referencia, el sistema mantiene el volumen al día siguiente en lugar de aumentarlo para mitigar el riesgo a tu reputación del remitente.

## Detener un plan de calentamiento de IP

Braze te permite detener el calentamiento de IP y la creación de campañas futuras, pero si una campaña ya está activa o planificada para las próximas 24 a 48 horas, es posible que necesites detener la campaña específica manualmente. Detener un plan de calentamiento de IP también detiene todas las campañas asociadas.

Sin embargo, una vez detenido, el calentamiento de IP no se puede reanudar. En su lugar, debes configurar un nuevo plan para retomar donde lo dejaste:

- Descargando los datos existentes de tu plan detenido para conservarlos en tus registros, ya que una vez que inicies un nuevo calentamiento de IP, el rastreador anterior será eliminado
- Actualizando el **Volumen de envío diario actual** al volumen más reciente
- Agregando un filtro a un segmento si planeas usar el mismo segmento del último calentamiento de IP, excluyendo a los usuarios que ya recibieron campañas anteriores

## Cuando se completa un calentamiento de IP

El calentamiento de IP se marca como completado cuando el último día del calentamiento de IP termina a medianoche en la zona horaria de tu empresa. Por ejemplo, si la última campaña enviada en el plan de calentamiento de IP se envía a las 8 pm, entonces el plan se marca como completado después de cuatro horas.

El rastreador permanece en la página de inicio durante 90 días después de que finaliza el plan. Después de 90 días, el rastreador se elimina. La descarga de datos incluye estas métricas estándar de correo electrónico:

- _Enviados_
- _Entregados_
- _Rebotes_
- _Informes de correos no deseados_
- _Aperturas totales_
- _Aperturas únicas_
- _Clics_
- _Cancelaciones de suscripción_

Si un día incluye múltiples campañas utilizadas para cumplir con los requisitos de volumen, estas se agregan en la vista diaria.

![Rastreador de calentamiento de IP con volumen de envío para la semana del 16 de enero.]({% image_buster /assets/img/automated_ip_warming_example.png %})