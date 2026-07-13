---
nav_title: Instantáneas frente a transmisiones de eventos
article_title: Instantáneas frente a transmisiones de eventos
page_order: 4
page_type: reference
description: "Este artículo de referencia explica la diferencia entre los datos de instantánea y los datos de transmisión de eventos, y cómo cada uno debe estructurarse y entregarse a BrazeAI Decisioning Studio."
---

# Instantáneas frente a transmisiones de eventos {#snapshots-versus-event-streams}

> Los datos se clasifican en una de dos categorías fundamentales: instantáneas (estado) y transmisiones de eventos (lo que sucedió). Comprender esta distinción y aplicarla correctamente es una de las cosas más importantes que puedes hacer para asegurar que tu agente de Decisioning Studio aprenda de manera efectiva.

## Datos de instantánea (estado) {#snapshot-data-state}

Una instantánea representa el estado de un cliente en un momento específico. Responde a la pregunta: "¿Cómo se ve este cliente ahora mismo?"

Una instantánea es estática y agregada. Refleja el resultado acumulado de todos los cambios hasta ese momento. Es ideal para perfiles de clientes, características calculadas (por ejemplo, "días desde la última compra", "nivel de fidelización", "puntuación de cancelación").

### Campos obligatorios {#required-fields}

| Campo | Propósito |
|-------|-----------|
| Identificador del cliente | A quién describe este registro |
| Fecha de la instantánea | Cuándo se tomó esta instantánea |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos obligatorios" }

### Cómo deben actualizarse las instantáneas {#how-snapshots-should-be-updated}

- **Desencadenante:** Basado en tiempo, no en eventos. Las instantáneas deben generarse en un horario fijo (por ejemplo, diariamente), independientemente de si un cliente tuvo alguna actividad ese día.
- **Alcance:** Cada actualización debe incluir a todos los clientes relevantes, incluidos aquellos que no tuvieron ningún evento.
- **Método:** Agrega nuevos registros de instantánea al conjunto de datos en lugar de sobrescribir los valores anteriores. Esto preserva el estado histórico para el entrenamiento del modelo.

### Consultar datos de instantánea para entrega diaria {#query-snapshot-data-for-daily-delivery}

Decisioning Studio ejecuta su pipeline de recomendación una vez al día. Al entregar datos de instantánea, exporta la instantánea del día anterior en cada ejecución del pipeline:

```sql
SELECT *
FROM snapshot_data
WHERE snapshot_date = {t-1} -- on pipeline run date t, export the snapshot from t-1
```

## Datos de transmisión de eventos (flujo) {#event-stream-data-flow}

Una transmisión de eventos registra acciones discretas a medida que ocurren. Responde a la pregunta: "¿Qué hizo este cliente y cuándo?" Una transmisión de eventos es ideal para datos sin procesar, inmutables, incrementales y cronológicos. Cada registro representa algo que sucedió en un momento específico. Por ejemplo, usa esta transmisión de datos para registros de activación, registros de participación (aperturas, clics), eventos de conversión o canjes de cupones.

### Campos obligatorios

| Campo | Propósito |
|-------|-----------|
| Identificador del cliente | A quién se refiere este evento |
| Tipo de evento | Qué sucedió (por ejemplo, activación, conversión, clic) |
| Marca de tiempo del evento | Cuándo ocurrió realmente el evento |
| Marca de tiempo de creación | Cuándo se creó este registro en tu sistema (consulta la nota en la siguiente sección) |
| Propiedades del evento | Metadatos adicionales sobre el evento; cuanto más enriquecidos sean, mejor podrá Decisioning Studio vincular eventos a lo largo del recorrido del cliente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos obligatorios" }

{% alert important %}
La marca de tiempo del evento y la marca de tiempo de creación son campos diferentes y ambos son obligatorios. La marca de tiempo del evento registra cuándo ocurrió realmente la acción. La marca de tiempo de creación registra cuándo se escribió la entrada de datos en tu sistema, lo cual puede ser posterior debido a retrasos en el procesamiento. No confundas ambas.
{% endalert %}

### Cómo deben actualizarse las transmisiones de eventos {#how-event-streams-should-be-updated}

- **Desencadenante:** Basado en eventos. Se agregan nuevos registros cuando ocurren nuevos eventos.
- **Alcance:** Solo los clientes que tuvieron un evento obtienen nuevos registros.
- **Método:** Los registros existentes son inmutables. Las actualizaciones siempre son inserciones de nuevos registros.

### Consultar datos de eventos para entrega diaria {#query-event-data-for-daily-delivery}

Usa `create_timestamp`, no `event_timestamp`, para segmentar las exportaciones diarias. Los eventos a veces se escriben en tu sistema después de que ocurren (llegadas tardías). Si segmentas por `event_timestamp`, esos registros de llegada tardía se perderán permanentemente.

```sql
-- Correct: use create_timestamp to ensure late-arriving events are captured
SELECT *
FROM events_data
WHERE DATE(create_timestamp) = {t-1} -- on run date t, export all records created yesterday
```

```sql
-- Incorrect: slicing on event_timestamp will permanently lose late-arriving events
SELECT *
FROM events_data
WHERE DATE(event_timestamp) = {t-1}
```

Por ejemplo: si un evento ocurrió el 1 de enero pero no se escribió en tu sistema hasta el 2 de enero, segmentar por `event_timestamp` el 2 de enero lo perdería por completo. Segmentar por `create_timestamp` lo captura correctamente.

## Para integraciones nativas de Braze {#for-native-braze-integrations}

Braze proporciona dos mecanismos integrados que se corresponden directamente con estos dos tipos de datos.

### Atributos personalizados: datos de instantánea {#custom-attributes-snapshot-data}

Los atributos personalizados almacenan el estado a nivel de usuario en un momento dado. Son el vehículo correcto para perfiles de clientes y características calculadas (por ejemplo, `churn_score`, `total_purchases_last_30d`). **No** son adecuados para datos de eventos sin procesar, porque sobrescriben en lugar de acumular.

### Braze Currents: datos de transmisión de eventos {#braze-currents-event-stream-data}

Braze Currents proporciona datos de flujo de eventos sin procesar e inmutables. La tabla `USER_BEHAVIOR_CUSTOM_EVENTS` captura cada instancia de un evento personalizado a medida que ocurre, lo que la convierte en la fuente correcta para eventos de activación, participación y conversión.

{% alert tip %}
Trata los atributos personalizados como la fuente del estado del cliente y Braze Currents como la fuente de los eventos de comportamiento del cliente. No uses atributos personalizados para pasar datos de eventos sin procesar a Decisioning Studio.
{% endalert %}

## Problemas comunes {#common-issues}

### Pasar datos de eventos como una instantánea {#pass-event-data-as-a-snapshot}

Agregar datos de eventos en campos de instantánea antes de enviarlos a Decisioning Studio causa varios problemas:

- **Pérdida de granularidad:** Una vez que los datos se agregan a un resumen diario a nivel de cliente, los registros de eventos individuales desaparecen. Decisioning Studio no puede reconstruirlos.
- **Marcas de tiempo imprecisas:** Un campo como "last_email_sent" te indica la ocurrencia más reciente, pero pierde el historial completo de eventos y hace imposible una atribución precisa.
- **Actualizaciones fantasma:** Incluso en días en los que no ocurrieron eventos, el registro de instantánea se actualiza, creando entradas duplicadas que son difíciles de deduplicar.

Si usas Braze, utiliza las exportaciones de Currents (no los atributos personalizados) para entregar datos de eventos sin procesar a Decisioning Studio.

### Actualizar datos de instantánea con un desencadenante de evento {#update-snapshot-data-on-an-event-trigger}

Algunas implementaciones actualizan los datos de instantánea solo cuando ocurre un evento, por ejemplo, recalculando una característica solo cuando un cliente realiza una compra. Esto provoca que las características que dependen del paso del tiempo se vuelvan obsoletas para los clientes que no han tenido un evento reciente.

Por ejemplo, una característica como `days_since_last_purchase` tiene un valor correcto diferente cada día. Si solo se recalcula cuando ocurre una compra, quedará congelada en un valor incorrecto para todos los clientes que no han comprado recientemente. Actualiza siempre los datos de instantánea con un horario basado en tiempo que cubra a todos los clientes, todos los días.