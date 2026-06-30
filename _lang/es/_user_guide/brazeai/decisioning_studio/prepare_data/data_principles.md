---
nav_title: Principios generales
article_title: Principios generales de datos para Decisioning Studio
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre los principios generales de datos que se aplican a todos los activos de datos utilizados por BrazeAI Decisioning Studio."
---

# Principios generales {#general-principles}

> Los datos bien estructurados son la base de un agente eficaz de Decisioning Studio. Antes de profundizar en los requisitos específicos de cada activo, es útil comprender los cuatro principios fundamentales que se aplican a todos los datos que envías a Decisioning Studio. Las violaciones de cualquiera de estos principios se encuentran entre las causas más comunes de un rendimiento degradado del modelo.

## Un identificador de cliente consistente en todos los activos {#one-consistent-customer-identifier-across-all-assets}

Cada activo de datos (perfiles de clientes, activaciones, interacciones, conversiones) debe hacer referencia al mismo identificador de cliente. Debe haber exactamente un identificador principal que identifique de forma única y consistente a cada cliente en todos los activos.

| Requisito | Implicación si se incumple |
|-----------|---------------------------|
| Un identificador de cliente único debe estar presente en cada activo | Si diferentes activos utilizan diferentes sistemas de ID (por ejemplo, un ID de almacén de datos para características pero un ID de plataforma para activaciones), el motor de Decisioning Studio no puede unirlos de forma fiable. Esto rompe el ciclo de retroalimentación y degrada tanto el entrenamiento del modelo como la precisión de los informes. Si el mapeado entre los dos sistemas de ID resulta ser de muchos a muchos en lugar de uno a muchos, los fallos de integridad de datos resultantes pueden ser graves. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Un identificador de cliente consistente en todos los activos" }

Consulta [Usar el ID externo de Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id) para obtener orientación sobre qué identificador utilizar.

## Los datos de eventos deben pasarse como un flujo incremental, no como una instantánea {#event-data-must-be-passed-as-an-incremental-stream-not-as-a-snapshot}

Los eventos, como conversiones, interacciones y activaciones, representan cosas discretas que ocurrieron en un momento específico en el tiempo. Deben entregarse a Decisioning Studio como un flujo incremental (solo de adición) de registros individuales, no como una instantánea agregada.

| Requisito | Implicación si se incumple |
|-----------|---------------------------|
| Los datos de eventos deben estructurarse como registros individuales con marca de tiempo y entregarse de forma incremental | Cuando los datos de eventos se agregan en una instantánea (por ejemplo, almacenando un atributo de "hora del último envío" en lugar de registros de envío individuales), se pierde la temporización precisa de cada evento. Esto hace imposible atribuir con precisión los resultados a decisiones específicas, rompiendo el ciclo de retroalimentación que el modelo necesita para aprender. Sin marcas de tiempo precisas de los eventos, no puedes saber exactamente cuándo ocurrió una conversión o qué recomendación la desencadenó. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Los datos de eventos deben pasarse como un flujo incremental, no como una instantánea" }

Consulta [Instantáneas frente a flujos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) para una explicación completa de la distinción y ejemplos de patrones correctos e incorrectos.

## Los datos de instantáneas deben actualizarse en un calendario regular basado en el tiempo {#snapshot-data-must-be-updated-on-a-regular-time-driven-schedule}

Los datos de instantáneas (como perfiles de clientes y características) representan el estado actual de un cliente en un momento dado. Las actualizaciones de los datos de instantáneas deben regirse por un calendario regular (por ejemplo, diario), no por desencadenadores de eventos.

| Requisito | Implicación si se incumple |
|-----------|---------------------------|
| Las instantáneas deben actualizarse para todos los clientes en un calendario regular, independientemente de si un cliente tuvo un evento ese día | Si las actualizaciones de instantáneas solo se desencadenan cuando ocurre un evento, las características que dependen del paso del tiempo (como "días desde la última compra" o "días desde la inscripción") se volverán obsoletas para los clientes que no hayan tenido un evento reciente. El modelo estará entrenándose con valores de características desactualizados, lo que reduce su capacidad para hacer recomendaciones precisas y oportunas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Los datos de instantáneas deben actualizarse en un calendario regular basado en el tiempo" }

## Todos los activos deben cumplir requisitos mínimos de calidad e integridad de datos {#all-assets-must-meet-minimum-data-quality-and-integrity-requirements}

Más allá de la estructura, los datos en sí deben ser internamente consistentes y lo suficientemente completos para ser útiles.

| Requisito | Implicación si se incumple |
|-----------|---------------------------|
| Cada activo debe contener los campos necesarios para establecer una clave primaria y, cuando corresponda, claves de unión con otros activos. Los registros duplicados deben eliminarse o deduplicarse antes de la ingesta. | Los registros duplicados o que no se pueden emparejar añaden ruido al entrenamiento del modelo y pueden causar una atribución incorrecta. Las claves faltantes impiden que el motor vincule eventos a lo largo del recorrido del cliente, desde la recomendación hasta la conversión. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Todos los activos deben cumplir requisitos mínimos de calidad e integridad de datos" }

Para los datos de flujos de eventos específicamente, cada registro debe incluir como mínimo:

**Campos obligatorios:**
- Identificador de cliente
- Marca de tiempo de cuándo ocurrió el evento (no de cuándo se creó el registro en tu sistema; son diferentes; consulta [Instantáneas frente a flujos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) para entender por qué esto importa)
- Marca de tiempo de cuándo se creó el registro en tu sistema (utilizada para segmentar de forma fiable las exportaciones incrementales)
- Tipo de evento
- Campos suficientes para filtrar hasta los eventos específicos que te interesan

**Campos recomendados:**
- Metadatos adicionales del evento que permitan un emparejamiento fiable entre tipos de eventos (por ejemplo, vincular un evento de conversión con la activación específica que lo precedió)