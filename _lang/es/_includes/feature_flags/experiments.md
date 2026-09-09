# Experimentos de conmutadores de características {#feature-flag-experiments}

> Los experimentos con conmutadores de características te permiten hacer pruebas A/B de los cambios en tus aplicaciones para optimizar las tasas de conversión. Los especialistas en marketing pueden utilizar los conmutadores de características para determinar si una nueva característica influye positiva o negativamente en las tasas de conversión, o qué conjunto de propiedades del conmutador de características es el más óptimo.

## Requisitos previos {#prerequisites}

Antes de poder rastrear datos de usuario en el experimento, tu aplicación necesita registrar cuándo un usuario interactúa con un conmutador de características. Esto se denomina impresión de conmutador de características. Asegúrate de registrar una impresión de conmutador de características cada vez que un usuario vea o podría haber visto la característica que estás probando, incluso si se encuentra en el grupo de control.

Para obtener más información sobre el registro de impresiones de conmutadores de características, consulta [Crear conmutadores de características]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions).

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

## Creación de un experimento con conmutador de características {#creating-a-feature-flag-experiment}

### Paso 1: Crear un experimento {#step-1-create-an-experiment}

1. Ve a **Mensajería** > **Campaigns** y selecciona **+ Crear Campaign**.
2. Selecciona **Experimento con conmutador de características**.
3. Dale a tu campaign un nombre claro y significativo.

### Paso 2: Añadir variantes del experimento {#step-2-add-experiment-variants}

A continuación, crea variaciones. Para cada variante, elige el conmutador de características que deseas activar o desactivar, y luego revisa sus propiedades asignadas.

Para probar el impacto de tu característica, usa variantes para dividir el tráfico en dos o más grupos. Nombra un grupo "Mi grupo de control" y desactiva sus conmutadores de características.

Los experimentos con conmutadores de características admiten hasta nueve grupos en total: un grupo de control más hasta ocho variantes.

### Paso 3: Sobrescribir propiedades (opcional) {#step-3-overwrite-properties-optional}

Puedes elegir sobrescribir las propiedades predeterminadas que configuraste inicialmente para los usuarios que reciben una variante de campaña específica.

Para editar, añadir o eliminar propiedades predeterminadas adicionales, edita el conmutador de características desde **Mensajería** > **Conmutadores de características**. Cuando una variante está desactivada, el SDK devolverá un objeto de propiedades vacío para el conmutador de características dado.

![La sección "Variantes del experimento" con la clave de variable "link" sobrescrita con "/sales".]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Paso 4: Elegir los usuarios a los que dirigirse {#step-4-choose-users-to-target}

Usa uno de tus Segments o filtros para elegir tus [usuarios objetivo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users). Por ejemplo, puedes usar el filtro **Variante de conmutador de características recibida** para reorientar a usuarios que ya han recibido una prueba A/B.

![La página "Objetivo" en un experimento con conmutador de características con "Variante de conmutador de características recibida" resaltado en la barra de búsqueda del grupo de filtros.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
La pertenencia al Segment se calcula cuando se actualizan los conmutadores de características para un usuario determinado. Los cambios estarán disponibles después de que tu aplicación actualice los conmutadores de características, o cuando se inicie una nueva sesión.
{% endalert %}

### Paso 5: Distribuir variantes {#step-5-distribute-variants}

Elige la distribución porcentual para tu experimento. Como buena práctica, no deberías cambiar la distribución después de que tu experimento haya sido lanzado.

### Paso 6: Asignar conversiones {#step-6-assign-conversions}

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una campaign. Especifica una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

### Paso 7: Revisar y lanzar {#step-7-review-and-launch}

Cuando hayas terminado de construir la última parte de tu experimento, revisa sus detalles y selecciona **Lanzar experimento**.

## Revisión de los resultados {#reviewing-the-results}

Una vez que tu experimento con el conmutador de características haya finalizado, puedes revisar los datos de impresiones de tu experimento. Ve a **Messaging** > **Campaigns** y selecciona la campaña con tu experimento de conmutador de características.

### Análisis de Campaign {#campaign-analytics}

**Campaign Analytics** ofrece un resumen de alto nivel del rendimiento de tu experimento, como:

- El número total de impresiones
- El número de impresiones únicas
- La tasa de conversión primaria
- Los ingresos totales generados por el mensaje
- La audiencia estimada

También puedes ver la configuración del experimento en cuanto a entrega, audiencia y conversión.

### Rendimiento de los experimentos de conmutadores de características {#feature-flag-experiment-performance}

**Feature Flags Experiments Performance** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas específicas que veas variarán en función del canal de mensajería elegido y de si estás ejecutando una prueba multivariante. Para ver los valores del conmutador de características asociados con cada variante, selecciona **vista previa**.