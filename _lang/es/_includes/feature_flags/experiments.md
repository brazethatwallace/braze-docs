# Experimentos de conmutadores de características {#feature-flag-experiments}

> Los experimentos con conmutadores de características te permiten hacer pruebas A/B de los cambios en tus aplicaciones para optimizar las tasas de conversión. Los especialistas en marketing pueden utilizar los conmutadores de características para determinar si una nueva característica influye positiva o negativamente en las tasas de conversión, o qué conjunto de propiedades del conmutador de características es el más óptimo.

## Requisitos previos {#prerequisites}

Antes de que puedas hacer un seguimiento de los datos de usuario en el experimento, tu aplicación necesita registrar cuándo un usuario interactúa con un conmutador de características. Esto se denomina impresión de conmutador de características. Asegúrate de registrar una impresión del conmutador de características siempre que un usuario vea o pudiera haber visto la característica que estás probando, aunque esté en el grupo de control.

Para saber más sobre el registro de impresiones de conmutadores de características, consulta [Crear conmutadores de características]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions).

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Crear un experimento de conmutador de características {#creating-a-feature-flag-experiment}

### Paso 1: Crea un experimento {#step-1-create-an-experiment}

1. Ve a **Mensajería** > **Campaigns** y selecciona **+ Create Campaign**.
2. Selecciona **Feature Flag Experiment**.
3. Dale a tu campaña un nombre claro y significativo.

### Paso 2: Añadir variantes del experimento {#step-2-add-experiment-variants}

A continuación, crea variaciones. Para cada variante, elige el conmutador de características que quieras activar o desactivar y, a continuación, revisa sus propiedades asignadas.

Para probar el impacto de tu característica, utiliza variantes para dividir el tráfico en dos o más grupos. Nombra un grupo "Mi grupo de control" y desactiva sus conmutadores de características.

Los experimentos de conmutadores de características admiten hasta nueve grupos en total: un grupo de control más hasta ocho variantes.

### Paso 3: Sobrescribir propiedades (opcional) {#step-3-overwrite-properties-optional}

Puedes elegir sobrescribir las propiedades predeterminadas que configuraste inicialmente para los usuarios que reciben una variante de campaña específica.

Para editar, añadir o eliminar propiedades predeterminadas adicionales, edita el propio conmutador de características desde **Mensajería** > **Conmutadores de características**. Cuando una variante está desactivada, el SDK devolverá un objeto de propiedades vacío para el conmutador de características dado.

![La sección "Variantes del experimento" con la clave variable "link" sobrescrita con "/sales".]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Paso 4: Elige los usuarios a los que dirigirte {#step-4-choose-users-to-target}

Utiliza uno de tus Segments o filtros para elegir a tus [usuarios objetivo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users). Por ejemplo, puedes utilizar el filtro **Received Feature Flag Variant** para reorientar a los usuarios que ya han recibido una prueba A/B.

![La página "Objetivo" en un experimento de conmutador de características con "Received Feature Flag Variant" resaltado en la barra de búsqueda del grupo de filtros.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
La pertenencia a un Segment se calcula cuando se actualizan los conmutadores de características para un usuario determinado. Los cambios están disponibles cuando tu aplicación actualiza los conmutadores de características, o cuando se inicia una nueva sesión.
{% endalert %}

### Paso 5: Distribuir variantes {#step-5-distribute-variants}

Elige la distribución porcentual para tu experimento. Como práctica recomendada, no debes cambiar la distribución una vez iniciado tu experimento.

### Paso 6: Asignar conversiones {#step-6-assign-conversions}

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events), después de recibir una campaña. Especifica una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

### Paso 7: Revisión y lanzamiento {#step-7-review-and-launch}

Cuando hayas terminado de construir lo último de tu experimento, revisa sus detalles y, a continuación, selecciona **Launch Experiment**.

## Revisión de los resultados {#reviewing-the-results}

Una vez finalizado tu experimento de conmutador de características, puedes revisar los datos de impresión de tu experimento. Ve a **Mensajería** > **Campaigns** y selecciona la campaña con tu experimento de conmutador de características.

### Análisis de la campaña {#campaign-analytics}

**Campaign Analytics** ofrece un resumen de alto nivel del rendimiento de tu experimento, como por ejemplo:

- El número total de impresiones
- El número de impresiones únicas
- La tasa de conversión primaria
- Los ingresos totales generados por el mensaje
- La audiencia estimada

También puedes ver la configuración del experimento para la entrega, la audiencia y la conversión.

### Rendimiento del experimento de conmutador de características {#feature-flag-experiment-performance}

**Feature Flags Experiments Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas específicas que veas variarán en función del canal de mensajería elegido y de si estás realizando una prueba multivariante. Para ver los valores de los conmutadores de características asociados a cada variante, selecciona **Vista previa**.