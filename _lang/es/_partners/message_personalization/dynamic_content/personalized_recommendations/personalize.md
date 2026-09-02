---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "Este artículo de referencia describe la asociación entre Braze y Personalize.AI, una plataforma empresarial software como servicio (SaaS) basada en IA que impulsa el crecimiento de los ingresos a partir de recomendaciones personalizadas."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) se asocia con Braze para generar ingresos adicionales entregando mensajes personalizados y ofertas enviadas a través de Braze.

La integración de Braze y Personalize.AI te permite exportar datos de Personalize.AI a la plataforma Braze para la personalización y segmentación de mensajes.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Instancia de Personalize.AI | Se necesita una instancia de Personalize.AI para aprovechar esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con todos los permisos. <br><br>Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | La URL de tu punto de conexión REST or transferencia de estado representacional. Tu punto de conexión dependerá de la [URL de Braze para tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

* Desplegar pruebas, incluida la estratificación flexible, para obtener resultados a partir de las opiniones de los clientes
* Proporcionar recomendaciones personalizadas para artículos y ofertas, incluyendo el tratamiento, el momento y el contenido
* Identificar objetivos prioritarios y dirigirte a tu audiencia óptima a través de Braze
* Identificar oportunidades para reactivar la interacción de los usuarios inactivos
* Utilizar los datos de geolocalización para encontrar la audiencia adecuada para las ubicaciones de nueva apertura
* Utilizar el modelado de similitud para basarte en los limitados datos disponibles de los usuarios más nuevos, emparejándolos con las recomendaciones más relevantes
* Identificar las formas adecuadas de interactuar con los clientes a lo largo de su ciclo de vida
* Evaluar proactivamente la probabilidad de abandono de los clientes y asignar una puntuación de riesgo para encontrar indicadores tempranos de abandono
* Dirigirte a los clientes con intervenciones personalizadas para evitar que se vuelvan inactivos

## Integración {#integration}

### Configura una conexión con Braze en Personalize.AI {#configure-a-connection-with-braze-in-personalizeai}

1. En Personalize.AI, ve a la pestaña **Integrations**, situada en **Operationalization**, en tu instancia de Personalize.AI.
2. Haz clic en **Braze**.
3. Configura tu integración con Braze.
    * **Connection Name:** Ponle nombre a tu conexión. Así es como se hará referencia a tu integración en Personalize.AI.
    * **Sync Frequency:** La frecuencia de sincronización controla con qué frecuencia Personalize.AI exporta datos a Braze. Selecciona **Daily**, **Weekly** o **Monthly**.
    * **API Key:** Añade tu clave de API de Braze.
    * **API URL:** Añade la URL de tu punto de conexión REST or transferencia de estado representacional de Braze.
4. Haz clic en **EXPORT** para exportar los datos a Braze.

Una vez exportados tus datos, Personalize.AI seguirá pasando datos a Braze en los intervalos determinados por la frecuencia de sincronización que estableciste durante la integración.

## Uso de esta integración {#using-this-integration}

Personalize.AI exporta a Braze los identificadores utilizados para la segmentación personalizada. Estos atributos personalizados indican el momento, el contenido, el tratamiento y las ofertas para cada cliente. Dependiendo de la integración, los campos pueden pasarse como un evento o extraerse a través de las [API de Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/public_apis/) en lugar de almacenarse en el perfil del cliente. Personalize.AI admite el uso de `external_id` como identificador.

Los atributos de datos importados en Braze se nombran de forma intuitiva para su uso en Canvas, siguiendo una terminología coherente. Por ejemplo, el atributo `C402_Target_Variant` en Personalize.AI se exportaría a Braze como `"P.AI_Model_Treatment"`. Los atributos exportados desde Personalize.AI están diseñados para no interferir con ningún atributo existente ni con tu seguimiento. Estos atributos se validan continuamente para confirmar que puedes hacer referencia a ellos con confianza.

Por ejemplo, aquí tienes un conjunto de atributos de cliente relacionados con un ejemplo de Canvas centrado en el abandono.

| Atributo de Personalize.AI | Valor |
| ----------- | ------------- |
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Treatment |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salad" |
| `C4_Subject_Line` | "We miss you" |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Uso de esta integración" }