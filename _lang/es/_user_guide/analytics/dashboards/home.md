---
nav_title: Inicio
article_title: Dashboard de inicio (anteriormente Resumen)
page_order: 1
page_type: reference
description: "Este artículo de referencia describe tu dashboard de inicio y proporciona definiciones de las estadísticas disponibles en esta página."
tool:
  - Reports

---

# Dashboard de inicio {#home-dashboard}

> La página **Inicio** del dashboard proporciona métricas clave para que puedas hacer seguimiento y comprender el rendimiento de tu aplicación o sitio web, y te ofrece una visión general de alto nivel de tu base de usuarios.

La página **Inicio** tiene dos secciones principales:
- [Retoma donde lo dejaste](#pick-up-where-you-left-off)
- [Resumen de rendimiento](#performance-overview)


## Retoma donde lo dejaste {#pick-up-where-you-left-off}

Puedes retomar donde lo dejaste en el dashboard de Braze con acceso directo a los archivos que editaste o creaste recientemente. Esta sección aparece en la parte superior de la página **Inicio** del dashboard de Braze.

Puedes volver a visitar campañas, Canvas y segmentos editados o creados recientemente. Cada tarjeta está acompañada de etiquetas que indican el tipo de contenido (Campaign, Canvas, Segment) y el estado (activo, borrador, archivado, detenido).

{% alert note %}
La sección **Retoma donde lo dejaste** aparece después de que hayas editado o creado una Campaign, un Canvas o un Segment.
{% endalert %}

![Un borrador de Canvas, un segmento activo y un borrador de Campaign en la sección "Retoma donde lo dejaste".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Resumen de rendimiento {#performance-overview}

De forma predeterminada, la sección **Resumen de rendimiento** muestra los datos de los últimos 30 días para todas las aplicaciones y sitios. Todas tus métricas se calculan en función del rango de fechas seleccionado.

Los porcentajes se calculan comparando el rango de fechas actual con el rango de fechas anterior, con la excepción de *MAU* (MAU), que utiliza el último día del período anterior en lugar de un rango.

Por ejemplo, si estableces tu rango de fechas en **Últimos 7 días** y tus *Usuarios activos diarios* muestran un aumento porcentual del 1,8 %, eso significa que tuviste un 1,8 % más de usuarios activos diarios esta semana en comparación con la semana pasada.

![Un mosaico de métrica para usuarios activos diarios que muestra un promedio de 22,2 mil con una señal de aumento del 7,1 % y una línea de tendencia.]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Mostrar desglose {#show-breakdown}

Selecciona **Show Breakdown** para cada fila de las estadísticas del resumen de rendimiento para ver el valor de cada estadística por día dentro del rango de fechas especificado.

### Rendimiento a lo largo del tiempo {#performance-over-time}

El gráfico **Rendimiento a lo largo del tiempo** muestra el valor de cada estadística durante el rango de fechas especificado para las aplicaciones seleccionadas.

![El gráfico de rendimiento a lo largo del tiempo mostrando estadísticas de nuevos usuarios durante 30 días.]({% image_buster /assets/img/dashboards/performance_over_time.png %})

Puedes graficar estadísticas para:
- Banners
- Content Cards
- Usuarios activos diarios
  - (Opcional) Desglose por segmento
- Correo electrónico
- Mensajes dentro de la aplicación
- Fórmulas de indicador clave de rendimiento
  - Selecciona **Manage indicador clave de rendimiento Formulas** para crear una fórmula o editar una fórmula existente.
- LINE
- MAU (MAU)
- Nuevos usuarios
- Push
  - (Opcional) Desglose por segmento
- Sesiones
  - (Opcional) Desglose por segmento o versión de la aplicación
- Sesiones por hora
- Sesiones por MAU
- SMS
- Adherencia
- Desinstalaciones
  - (Opcional) Desglose por segmento
- Usuarios
- Webhooks
- WhatsApp

## Estadísticas disponibles {#available-statistics}

A continuación se presentan las definiciones de las estadísticas disponibles, cómo se calculan y por qué deberían ser importantes para ti.

### Usuarios {#users}

*Usuarios* es el número total de usuarios creados en ese espacio de trabajo. Esto incluye a todos los usuarios registrados que han utilizado tu aplicación o sitio web en cualquier momento, y aquellos que podrían no estar asociados con una aplicación o sitio web específico. Este número es el porcentaje de cuántos de tus usuarios históricos están representados como *MAU* (MAU), lo cual es útil para ver la retención de usuarios durante un largo período de tiempo.

Una proporción baja de MAU respecto a usuarios puede indicar que necesitas diversificar tus canales de mensajería o aumentar tus esfuerzos para contactar a los usuarios inactivos. Consulta nuestra guía rápida sobre [captar usuarios inactivos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users) para más información. En general, la proporción de MAU respecto a usuarios históricos inevitablemente disminuirá con el tiempo debido a la cancelación de usuarios, pero las herramientas de Braze pueden ayudarte a minimizar este efecto manteniendo a los usuarios comprometidos durante más tiempo.

### Sesiones históricas {#lifetime-sessions}

*Sesiones históricas* es el recuento total de sesiones que Braze ha registrado desde la integración. Una sesión es cada vez que un usuario utiliza la aplicación o visita tu sitio web. Para una definición más precisa de cómo se definen las sesiones por plataforma, consulta los artículos correspondientes para desarrolladores sobre seguimiento de sesiones en
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android) o [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).

### MAU {#monthly-active-users}

*MAU* (MAU) es el número de usuarios que han registrado una sesión en tu aplicación o sitio en los últimos 30 días. Los MAU se calculan cada noche con una ventana móvil de 30 días. Los MAU te proporcionan una buena comprensión de la salud de una aplicación o sitio durante un período prolongado, ya que suavizan las inconsistencias entre días con intensidad de uso variable.

El porcentaje junto al recuento de MAU muestra el cambio en MAU para este período en comparación con el período anterior.

$$\text{Cambio en MAU} = \frac{\text{MAU del último día del rango} - \text{MAU del día anterior a la fecha de inicio}}{\text{MAU del día anterior a la fecha de inicio}}$$

#### Reglas de cálculo de MAU {#mau-calculation-rules}

Los cálculos de MAU siguen reglas específicas para garantizar una facturación precisa y consistente:

- **Momento del cálculo**: se calcula una vez al día a las 12:05 UTC como una instantánea de 30 días; los recuentos nunca cambian retroactivamente.
- **Perfiles anónimos**: se cuentan **solo** cuando se registra al menos una sesión.
- **Perfiles identificados**: se cuentan solo cuando `date_of_last_session` está dentro de la ventana móvil de 30 días.
- **Perfiles huérfanos**: los duplicados fusionados con otro usuario **no** se cuentan.
- **Cargas por CSV e importaciones por REST API**: los usuarios cargados por CSV o la REST API cuentan para el MAU cuando proporcionas `date_of_last_session` dentro de la ventana móvil de 30 días, o cuando posteriormente registran una sesión. Proporcionar solo `date_of_first_session` no afecta al MAU.
- **Eliminaciones por API**: eliminar un usuario a través de la API no actualiza el MAU de inmediato; el recuento se corrige automáticamente en el siguiente ciclo mensual.

{% alert note %}
Los usuarios anónimos también cuentan para tu MAU. Para dispositivos móviles, los usuarios anónimos dependen del dispositivo. Para usuarios web, los usuarios anónimos dependen de la caché del navegador. <br><br> Los recuentos de MAU en Braze pueden diferir de herramientas como Amplitude cuando cada producto utiliza una definición diferente de usuario activo. Compara la configuración en Amplitude (y tus [reglas de cálculo de MAU](#mau-calculation-rules)) antes de investigar una discrepancia como un problema del pipeline de datos.
{% endalert %}

#### Ejemplo de cálculo de MAU {#mau-calculation-example}

El siguiente ejemplo demuestra cómo funcionan los cálculos de MAU a través de diferentes acciones de usuario:

| Paso | Acción | Cambio inmediato en MAU | Total resultante |
|------|--------|----------------------|-----------------|
| 1 | Crear **Usuario anónimo 1** y registrar una sesión | +1 | 1 |
| 2 | Identificar **Usuario anónimo 1** (el perfil se convierte en identificado) | 0 | 1 |
| 3 | Crear **Usuario anónimo 2** y registrar una sesión | +1 | 2 |
| 4 | Identificar **Usuario anónimo 2** como la **misma persona** que el Usuario 1 (el Usuario 2 se convierte en huérfano) | –1 | 1 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Ejemplo de cálculo de MAU" }

Las instantáneas de MAU se calculan una vez al día y nunca cambian retroactivamente. En este ejemplo, el recuento de MAU del día posterior al paso 3 permanece permanentemente en 2, aunque el Usuario 2 posteriormente se convierta en huérfano. Sin embargo, el recuento de MAU de los días siguientes refleja solo al usuario no huérfano. Dentro de cualquier ventana de 30 días, este flujo consume en última instancia 1 MAU, ya que solo queda un usuario distinto y no huérfano.

##### Consideraciones sobre el recuento de MAU {#mau-count-considerations}

Los recuentos de MAU en Braze dependen de dónde los consultes. El MAU total se calcula a nivel de usuario, independientemente de las aplicaciones y plataformas, por lo que cada usuario se cuenta solo una vez. Sin embargo, cuando consultas los recuentos de MAU por aplicación, la suma de MAU de todas las aplicaciones puede superar tu MAU total; un usuario que utiliza varias aplicaciones en tu espacio de trabajo se cuenta en la métrica de MAU individual de cada aplicación.

### Usuarios activos diarios {#daily-active-users}

*Usuarios activos diarios* (usuario activo diario) muestra el número de usuarios únicos que registran al menos una sesión en tu aplicación o sitio en un día determinado. usuario activo diario puede ser una estadística útil para examinar la variabilidad diaria del uso de tu aplicación o sitio y adaptar tus campañas de mensajería para que sean lo más efectivas posible. Por ejemplo, el uso de tu aplicación puede experimentar un aumento notable los fines de semana, lo que te indicaría que podrías llegar a más usuarios con mensajes dentro de la aplicación en esos días en lugar de entre semana.

### Nuevos usuarios {#new-users}

*Nuevos usuarios* te indica cuántos usuarios que nunca habían registrado una sesión anteriormente comenzaron a usar tu aplicación o sitio. Este número es el total de nuevos usuarios durante el período de tiempo dado. Esta estadística puede ser muy valiosa para hacer seguimiento de la efectividad de tus esfuerzos publicitarios.

{% alert note %}
Cuando integras Braze inicialmente, todos los usuarios aparecerán como nuevos usuarios porque Braze nunca había registrado una sesión para ellos antes. <br><br> A diferencia de MAU, el recuento de *Nuevos usuarios* puede disminuir retroactivamente cuando Braze fusiona un perfil anónimo con un perfil identificado y convierte en huérfano el perfil anónimo. Braze elimina el perfil huérfano de los totales de uso de la aplicación, lo que puede reducir *Nuevos usuarios* para fechas que ya habías consultado. Para conocer el comportamiento de vinculación de perfiles, consulta [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).
{% endalert %}

{% alert important %}
Los usuarios asociados con más de una aplicación se cuentan por separado para cada aplicación. Esto significa que un solo usuario puede contribuir al recuento de *Nuevos usuarios* varias veces si inicia sesiones en diferentes aplicaciones dentro de tu espacio de trabajo.
{% endalert %}

### Adherencia {#stickiness}

El valor de *Adherencia* es una proporción entre los usuario activo diario y los MAU de un período determinado. En esencia, la adherencia mide el porcentaje de tus MAU que regresan diariamente.

Por ejemplo, si el rango de fechas se establece en 30 días, una proporción del 50 % indica que, en promedio, un usuario activo utiliza la aplicación o el sitio web 15 de los 30 días, o que aproximadamente la mitad de tus usuarios activos regresan diariamente. La adherencia es una métrica importante para el éxito porque la mayoría de los usuarios no dejan de usar una aplicación porque la odien activamente, sino porque no se ha convertido en parte de su rutina diaria. Por lo tanto, puedes usar la adherencia como un indicador de qué tan bien estás involucrando a tus usuarios.

El porcentaje junto a la proporción de adherencia muestra el cambio en la adherencia para este período en comparación con el período anterior.

$$\text{Cambio en adherencia} = \frac{\text{Adherencia del último período} - \text{Adherencia de este período}}{\text{Adherencia del último período}}$$

Los marcos temporales para "último período" y "este período" están determinados por el rango de fechas que selecciones.

{% alert important %}
El valor de MAU se calcula cada noche y no se actualizará hasta el día siguiente.
{% endalert %}

### Sesiones diarias {#daily-sessions}

*Sesiones diarias* es el número de sesiones registradas en un día determinado. Comparar este valor con tu recuento de usuario activo diario puede informarte de cuántas veces tus usuarios abren la aplicación o visitan tu sitio web en los días en que registran al menos una sesión.

{% alert note %}
El *Recuento de sesiones diarias* para una fecha determinada puede cambiar cuando consultas el dashboard de inicio en días diferentes. Si un usuario inicia una sesión sin conexión, es posible que la sesión no llegue a Braze hasta que vuelva a abrir la aplicación. Cuando esa sesión se envía, Braze la atribuye a la fecha en que comenzó la sesión, lo que puede aumentar el recuento de esa fecha retroactivamente.
{% endalert %}

### Sesiones diarias por MAU {#daily-sessions-per-mau}

*Sesiones diarias por MAU* es la proporción de *Sesiones diarias* respecto a MAU en un día determinado. Esta estadística te indica cuántas sesiones por día puedes esperar que se registren por MAU. Cuando se agrega y promedia, esto puede darte una idea de la frecuencia relativa con la que tus usuarios utilizan tu aplicación o sitio. Es decir, si tus *Sesiones diarias por MAU* fueran en promedio 0,5, podrías esperar que cada MAU registre una sesión aproximadamente cada 2 días.