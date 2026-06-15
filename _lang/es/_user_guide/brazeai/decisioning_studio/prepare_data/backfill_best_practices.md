---
nav_title: Mejores prácticas de backfill
article_title: Mejores prácticas de backfill
page_order: 7
page_type: reference
description: "Aprende a realizar correctamente el backfill de datos históricos para BrazeAI Decisioning Studio, incluyendo requisitos, errores comunes y cómo evitar problemas de calidad de datos que afectan el rendimiento del modelo de IA."
---

# Mejores prácticas de backfill {#backfill-best-practices}

> Por diversas razones, puede ser necesario realizar un backfill de datos, ya sea por errores en los datos, nueva información (como nuevas características), o la conciliación de datos entre dos sistemas. Cuando se realiza un backfill, sigue los principios de este artículo para mantener la calidad de los datos y el rendimiento del modelo.

## Cuándo se necesita un backfill {#when-backfilling-is-needed}

El backfill es el proceso de poblar retroactivamente un conjunto de datos con datos históricos. Los escenarios comunes incluyen:

| Escenario | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Nuevas características** | Has identificado una nueva métrica que es importante para tu modelo y tienes los registros históricos sin procesar para calcularla. | Agregas "tasa de click-through" como una característica y necesitas tres meses de historial para que el modelo tenga suficientes datos de los cuales aprender. |
| **Recuperación de datos** | Tu pipeline de datos falló en días específicos, creando vacíos en los datos entregados a Decisioning Studio. | Una interrupción del pipeline el martes dejó un vacío. Después de implementar la corrección, realizas el backfill de esos registros faltantes desde el sistema de origen. |
| **Cambios de lógica** | Has actualizado la fórmula para el cálculo de una característica o cambiado la definición de un evento. | Redefiniste "usuario activo" y necesitas reexportar los datos históricos para que el modelo se entrene con la definición actualizada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cuándo se necesita un backfill" }

## Requisitos {#requirements}

Para que Decisioning Studio funcione correctamente, todos los datos entrantes deben soportar backfill para períodos históricos. La ventana de retrospectiva específica requerida (medida en meses) depende de los requisitos de entrenamiento del modelo de IA. Consulta con tu equipo de AI Decisioning Services para confirmar el valor correcto para tu caso de uso.

Al realizar un backfill histórico, los siguientes estándares son obligatorios:

- **Consistencia del proceso:** Las instantáneas históricas de características deben generarse utilizando un proceso que sea completamente consistente con la creación de instantáneas en vivo. Si tu pipeline en vivo aplica transformaciones, agregaciones o filtros, esos mismos pasos deben aplicarse a los datos del backfill.
- **Consistencia del esquema:** El esquema de los datos del backfill debe coincidir exactamente con el pipeline diario normal, incluyendo los mismos campos, tipos de datos y convenciones de nomenclatura de columnas.

## Errores comunes {#common-pitfalls}

### Fuga de datos (sesgo de anticipación) {#data-leakage-look-ahead-bias}

La fuga de datos es el error de backfill más crítico. Ocurre cuando el proceso de backfill incorpora inadvertidamente información que no habría estado disponible en el momento en que se generó el registro histórico.

#### Por qué es importante {#why-it-matters}

Si el modelo se entrena con datos que "conocen el futuro", parecerá tener un buen rendimiento durante el entrenamiento, pero producirá resultados deficientes en producción, porque las decisiones en tiempo real no tienen acceso a datos futuros.

Por ejemplo, considera calcular una característica histórica de "valor de duración del ciclo de vida" utilizando el gasto total de un cliente hasta la fecha (es decir, hasta hoy), y luego usar ese valor para predecir un comportamiento que ocurrió hace meses. En el momento de ese evento histórico, el valor de duración del ciclo de vida completo aún no se conocía.

Esto se puede evitar reconstruyendo siempre las características históricas utilizando únicamente la información que habría estado disponible en la marca de tiempo histórica, no la información que se acumuló después.

### Deriva de esquema y lógica {#schema-and-logic-drift}

Las estructuras de datos y las definiciones de negocio evolucionan con el tiempo. Las inconsistencias entre los datos históricos y los datos en vivo pueden degradar silenciosamente la calidad del modelo.

- **Deriva de esquema:** Si un campo (por ejemplo, `zip_code`) se agregó recientemente a tu base de datos, los registros del backfill anteriores a ese cambio contendrán valores nulos para ese campo. Asegúrate de que tu pipeline maneje los campos faltantes de manera adecuada y de que el modelo no dependa excesivamente de campos con cobertura histórica escasa.
- **Deriva de lógica:** Si la definición de una métrica cambió en un momento específico (por ejemplo, "usuario activo" se redefinió en 2024), aplicar la nueva definición de manera uniforme a datos más antiguos (por ejemplo, registros de 2022) puede crear picos o caídas artificiales que en realidad no ocurrieron. Cuando sea posible, aplica la definición que estaba vigente en el momento de cada registro histórico, o documenta claramente el punto de quiebre para que el modelo pueda tenerlo en cuenta.

### Registros duplicados por trabajos de backfill fallidos {#duplicate-records-from-failed-backfill-jobs}

Los trabajos de backfill que fallan a mitad de ejecución y se reinician pueden producir registros duplicados si el proceso no está diseñado para prevenirlo. Los registros duplicados inflan artificialmente las métricas e introducen ruido en el entrenamiento del modelo.

**La solución:** Diseña todos los scripts de backfill para que sean idempotentes: ejecutar el mismo trabajo dos veces debe producir el mismo resultado que ejecutarlo una vez. Usa uno de los siguientes patrones:

- **Upsert (actualizar o insertar):** Con clave en un ID de transacción único o marca de tiempo, de modo que reinsertar un registro existente lo actualice en lugar de crear un duplicado.
- **Eliminar y luego insertar:** Elimina los registros existentes para el rango de tiempo objetivo antes de insertar, de modo que el conjunto de datos siempre se reemplace de forma limpia.