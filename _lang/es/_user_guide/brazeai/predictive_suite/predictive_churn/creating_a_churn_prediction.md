---
nav_title: Crear una predicción de abandono
article_title: Crear una predicción de abandono
description: "Este artículo explica cómo crear una predicción de abandono en el panel de Braze."
page_order: 1.1

---

# Crear una predicción de abandono {#create-a-churn-prediction}

> Aprende a crear una predicción de abandono en el panel de Braze.

## Paso 1: Crear una nueva predicción {#step-1-create-a-new-prediction}

En Braze, ve a **Analytics** > **Predictive Churn**.

Una predicción es una instancia de un modelo de aprendizaje automático entrenado y todos los parámetros y datos que utiliza. En esta página, verás una lista de las predicciones activas actuales junto con información básica sobre ellas. Aquí puedes renombrar, archivar y crear nuevas predicciones. Las predicciones archivadas están inactivas y no actualizan las puntuaciones de los usuarios.

Para crear una nueva predicción, elige **Create Prediction** y selecciona una nueva **Churn Prediction**.

{% alert note %}
Hay un límite de cinco predicciones de cancelación activas simultáneamente. Antes de adquirir Predictive Churn, el límite es una predicción de cancelación activa en vista previa. Una predicción de cancelación en vista previa no actualizará regularmente las puntuaciones ni te permitirá dirigirte a usuarios en función de los resultados de la predicción. Ponte en contacto con tu director de cuentas para obtener más información.
{% endalert %}

En la página **Basics**, asigna a tu nueva predicción un nombre único. También puedes proporcionar una descripción opcional para tomar cualquier nota sobre esta predicción en particular.

Selecciona **Forward** para pasar al siguiente paso. Si lo deseas, puedes seleccionar **Generar ahora** para utilizar todas las configuraciones predeterminadas y pasar al último paso de la creación. Tendrás la oportunidad de revisar la configuración antes de iniciar el proceso de compilación. Puedes volver a cualquier paso más tarde seleccionándolo en el indicador de progreso.

## Paso 2: Definir el abandono {#step-2-define-churn}

En el panel **Definición de cancelación**, utiliza los filtros proporcionados para especificar cómo defines el abandono de usuarios para tu empresa. En otras palabras, ¿qué tiene que hacer un usuario en qué plazo de tiempo para que lo consideres abandonado?

Recuerda que no tienes que explicar qué comportamientos pueden preceder al abandono, solo qué hace que un usuario sea un usuario perdido. Piensa en esto en términos de algo que un usuario hace una vez (`do`) o deja de hacer (`do not`) y que constituye un abandono. Por ejemplo, puedes considerar abandonados a los usuarios que no han abierto tu aplicación en 7 días. Podrías considerar la desinstalación, o eventos personalizados como darse de baja, desactivar una cuenta u otros que provoquen que un usuario se dé de baja.

#### Ventana de abandono {#churn-window}

La ventana de abandono es el periodo en el que la actividad de un usuario cumple los criterios para el abandono. Puedes configurarla para un máximo de 60 días, dependiendo de los datos disponibles. Esta ventana se utiliza para extraer datos históricos con los que entrenar tu predicción. Una vez creada la predicción, verás si había datos suficientes para obtener resultados precisos.

Una vez que se genera la predicción y los usuarios reciben las puntuaciones, la _puntuación de riesgo de abandono_ muestra la probabilidad de que un usuario abandone dentro del plazo que hayas establecido en la ventana de abandono.

He aquí un ejemplo de definición simple basada en las sesiones caducadas en los últimos 7 días.

![Definición de abandono: un usuario se considera abandonado si no inicia una sesión en 7 días.]({% image_buster /assets/img/churn/churn1.png %})

Para este caso, seleccionamos `do not` y `start a session`. Puedes combinar otros filtros con `AND` y `OR` según te convenga para crear la definición que necesites. ¿Te interesan algunas posibles definiciones de abandono a tener en cuenta? Puedes encontrar algo de inspiración en la siguiente sección sobre [definiciones de muestra de abandono](#sample-definitions).

{% alert note %}
Para `do`, asumimos que los usuarios activos no realizaron la acción que especificas para esta fila antes del abandono. Realizar la acción provoca su abandono. <br><br>Para `do not`, consideramos que los usuarios activos son aquellos que realizaron esa acción en los días anteriores y luego dejaron de hacerlo. <br><br>**Ejemplo:** Si el abandono se define como «no ha iniciado una sesión en los últimos 60 días», consideramos usuarios activos a aquellos que sí han iniciado una sesión en los últimos 60 días. Como resultado, cualquier persona que no haya iniciado una sesión en los últimos 60 días no se considera un usuario activo. Esto significa que una audiencia de abandono creada a partir de esta definición de abandono solo incluiría a los usuarios que hayan iniciado una sesión en los últimos 60 días. Esto puede hacer que la audiencia de predicción de cancelación resultante parezca significativamente más pequeña que la población original: es posible que la mayoría de los usuarios de un espacio de trabajo ya cumplan la definición de usuarios perdidos y, por lo tanto, no estén activos en la predicción de cancelación.
{% endalert %}

Debajo de la definición, verás estimaciones de cuántos usuarios (en el pasado que abandonaron y que no abandonaron según tu definición) están disponibles. También verás los valores mínimos requeridos. Braze debe tener este número mínimo de usuarios disponibles en los datos históricos para que la predicción tenga suficientes datos de los que aprender.

## Paso 3: Filtra tu audiencia de predicción {#step-3-filter-your-prediction-audience}

Tu audiencia de predicción es el grupo de usuarios para los que deseas predecir el riesgo de abandono. La audiencia de predicción define el grupo de usuarios que el modelo de aprendizaje automático analiza para aprender del pasado. De forma predeterminada, está configurado en **Todos los usuarios**, lo que significa que esta predicción creará puntuaciones de riesgo de abandono para todos tus usuarios activos (consulta la nota anterior para saber quién se considera activo para un modelo de abandono).

Dependiendo de tu caso de uso, es posible que desees utilizar filtros para especificar los usuarios que deseas evaluar para el modelo. Para ello, selecciona **Define mi propia audiencia de predicción** y elige tus filtros de audiencia. Por ejemplo, si tienes una aplicación de transporte compartido con conductores y pasajeros en tu base de usuarios, y estás creando un modelo de abandono para los pasajeros, te interesará filtrar tu audiencia de predicción para incluir solo a los pasajeros. Ten en cuenta que muchos casos de uso no requieren que selecciones una audiencia de predicción específica. Por ejemplo, si tu caso de uso consiste en dirigirte a los usuarios de la región de la UE con mayor probabilidad de abandono, puedes ejecutar tu modelo en todos los usuarios y, a continuación, simplemente incluir un filtro para la región de la UE en el segmento de la Campaign.

Braze te mostrará el tamaño estimado de tu audiencia de predicción. Si especificas la audiencia deseada y no cumples con los requisitos mínimos para ejecutar el modelo, intenta especificar un filtro más amplio o utiliza la opción **Todos los usuarios**. Ten en cuenta que el tamaño del grupo «todos los usuarios» no es estático y varía de un modelo a otro, ya que tiene en cuenta tu definición de abandono. Por ejemplo, supongamos que la definición de abandono es **no** iniciar una sesión en 30 días; en este caso, Braze aplica el modelo a los usuarios que **han** iniciado una sesión en los últimos 30 días (y predice la probabilidad de que **no** inicien una sesión en los próximos 30 días), por lo que esos son los usuarios que se reflejan en la métrica «todos los usuarios».

{% alert note %}
La audiencia de la predicción no puede superar los 100 millones de usuarios.
{% endalert %}

Cuando el periodo de predicción es de 14 días o menos, el periodo de tiempo para los filtros que comienzan con «Last...», como «Last Used App» y «Last placed an order» **no puede superar el periodo de abandono especificado** en la definición de abandono. Por ejemplo, si tu definición de abandono tiene una ventana de 14 días, la ventana de tiempo para los filtros «Last...» no puede superar los 14 días.

La ventana de abandono se evalúa analizando el número de días transcurridos desde la última vez que se ejecutó el modelo, por lo que si la ventana de abandono es de 15 días y el modelo se ejecutó por última vez el 1 de diciembre, el modelo analiza el periodo comprendido entre el 16 y el 30 de noviembre para comprender la actividad de los usuarios con respecto a la elegibilidad de la audiencia y el entrenamiento.

#### Modo de filtro completo {#full-filter-mode}

Para crear una nueva predicción de forma inmediata, solo se admite un subconjunto de filtros de segmentación de Braze. El modo de filtro completo te permite utilizar todos los filtros de Braze, pero requerirá una ventana de abandono para crear la predicción. Por ejemplo, si la ventana de abandono se establece en 15 días, se tardará 15 días en recopilar los datos de usuario y construir la predicción cuando se utilicen filtros solo admitidos en el modo de filtro completo. Además, algunas estimaciones sobre el tamaño de la audiencia no estarán disponibles en el modo de filtro completo.

Para ver una lista de definiciones de audiencia de predicción, consulta nuestras definiciones de muestra en la siguiente sección sobre [definiciones de muestra de abandono](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Al igual que en la página anterior, el panel inferior te mostrará el número estimado de usuarios históricos resultantes de tu definición de abandono y de audiencia de predicción. Estas estimaciones deben cumplir los requisitos mínimos indicados para crear una predicción.

## Paso 4: Elige la frecuencia de actualización de la predicción de cancelación {#step-4-choose-the-update-frequency-for-churn-prediction}

El modelo de aprendizaje automático generará puntuaciones de probabilidad de eventos para los usuarios, y esas puntuaciones se actualizarán en función del calendario que selecciones aquí. Podrás dirigirte a los usuarios en función de su puntuación de probabilidad de evento.

Selecciona la **frecuencia máxima de actualizaciones** que te resulte útil. Por ejemplo, si vas a enviar una promoción semanal para evitar el abandono de usuarios, establece la frecuencia de actualización en **Weekly** el día y la hora que elijas.

![Programa de actualización de predicciones establecido en diario a las 17:00 h.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
La vista previa y la predicción de demostración nunca actualizarán el riesgo de abandono de los usuarios. Además, las actualizaciones diarias de las predicciones requieren una compra adicional más allá de las actualizaciones semanales o mensuales con Predictive Churn. Para adquirir esta funcionalidad, ponte en contacto con tu director de cuentas.
{% endalert %}

## Paso 5: Construir la predicción {#step-5-build-prediction}

Comprueba que los datos que has proporcionado son correctos y elige **Build Prediction**. También puedes guardar tus cambios en forma de borrador seleccionando **Guardar como borrador** para volver a esta página y construir el modelo más tarde. Después de seleccionar **Build Prediction**, se iniciará el proceso que genera el modelo. Esto puede tardar entre 30 minutos y unas horas, dependiendo del volumen de datos. Para esta predicción, verás una página en la que se explica que el entrenamiento está en curso durante todo el proceso de creación del modelo. El modelo de Braze tiene en cuenta eventos personalizados, eventos de compra, eventos de comercio electrónico, eventos de interacción con Campaign y datos de sesión.

Una vez hecho esto, la página cambiará automáticamente a la vista de análisis y también recibirás un correo electrónico informándote de que la predicción y los resultados están listos. En caso de error, la página volverá al modo de edición con una explicación de lo que ha ido mal.

La predicción se reconstruirá («reentrenará») de nuevo cada **dos semanas automáticamente** para mantenerla actualizada con los datos disponibles más recientes. Ten en cuenta que se trata de un proceso distinto al de la obtención de las _puntuaciones de riesgo de abandono_ de los usuarios, que es el resultado de la predicción. Esto último viene determinado por la frecuencia de actualización que elegiste en el paso 4.

## Definiciones de muestra de abandono y audiencia de predicción {#sample-definitions}

**Ejemplos de definiciones de abandono**<br>
- «En un plazo de 7 días, realiza el evento personalizado 'Cancelación de suscripción'»<br>
- «En un plazo de 30 días, realiza el evento personalizado 'Prueba caducada'»<br>
- «En el plazo de 1 día, desinstala».<br>
- «En un plazo de 14 días, no realiza una compra».<br>

Para las definiciones de abandono que hemos esbozado, puede haber algunas definiciones de audiencia de predicción correspondientes:<br>
- **Comenzó la suscripción hace más de 2 semanas O comenzó la suscripción hace menos de dos semanas**<br>En este caso, es posible que quieras crear 2 predicciones y luego enviar mensajes a los nuevos suscriptores de forma diferente a los suscriptores a largo plazo. También podrías definirlo como «Primera compra realizada hace más de 30 días».<br>
- **Desinstaladores**<br>Podrías centrarte en clientes que hayan comprado algo en el pasado reciente o que hayan utilizado la aplicación muy recientemente.<br>
- **Los que corren el riesgo de no comprar como definición de abandono**<br>Es posible que quieras centrarte en los clientes que han estado navegando o buscando, o interactuando con tu aplicación más recientemente. Tal vez una intervención adecuada con descuentos evite que este grupo más comprometido abandone.

## Predicciones archivadas {#archived-predictions}

Las predicciones archivadas dejarán de actualizar las puntuaciones de los usuarios. Cualquier predicción archivada que se desarchive seguirá actualizando las puntuaciones de los usuarios en su horario predeterminado. Las predicciones archivadas nunca se borran y permanecen en la lista.