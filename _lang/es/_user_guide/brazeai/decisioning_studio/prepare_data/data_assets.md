---
nav_title: Activos de datos críticos
article_title: Activos de datos críticos para Decisioning Studio
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre los activos de datos obligatorios y opcionales para BrazeAI Decisioning Studio, incluidos los datos de retroalimentación necesarios para cerrar el bucle de toma de decisiones con IA."
---

# Activos de datos críticos {#critical-data-assets}

> Decisioning Studio requiere ciertos activos de datos para funcionar y se beneficia de datos opcionales adicionales. Este artículo describe qué es cada activo, por qué es importante y qué campos son obligatorios.

## Cerrar el bucle de toma de decisiones con IA {#close-the-ai-decisioning-loop}

Los tres activos de eventos obligatorios (activaciones, interacciones y conversiones) forman juntos el bucle de retroalimentación que permite a Decisioning Studio aprender y mejorar con el tiempo.

- **Las activaciones** indican al modelo qué decidió hacer
- **Las interacciones** indican al modelo cómo respondieron los clientes al mensaje
- **Las conversiones** indican al modelo si se logró el resultado de negocio final

Cada uno de estos debe estar estructurado como un flujo de eventos incremental (no una instantánea). Consulta [Instantáneas frente a flujos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) para más detalles.

{% alert note %}
Si Decisioning Studio está integrado de forma nativa con tu plataforma de interacción con los clientes (como Braze o Salesforce Marketing Cloud), los datos de activación e interacción pueden recopilarse automáticamente sin configuración adicional. Consulta la documentación de configuración para confirmarlo.
{% endalert %}

## Activos obligatorios {#required-assets}

### Perfil de cliente {#customer-profile}

Los datos del perfil de cliente describen quiénes son tus clientes. Decisioning Studio utiliza estos datos para comprender el estado actual de cada cliente y generar recomendaciones relevantes.

Los atributos de perfil más comunes incluyen:

- Años como cliente
- Geografía (cuando lo permitan tu sector y los requisitos de privacidad)
- Canal de adquisición (por ejemplo, web, teléfono, tienda física)
- Puntuación de satisfacción o sentimiento
- Puntuaciones derivadas de modelos (por ejemplo, propensión al abandono, estimación del valor de duración del ciclo de vida)
- Nivel de fidelización o pertenencia a un programa

### Datos de activación e interacción {#activation-and-engagement-data}

Los datos de activación registran lo que Decisioning Studio realmente envió: qué recomendación se entregó a qué cliente a través de qué canal. Los datos de interacción registran lo que hizo el cliente en respuesta: si abrió, hizo clic o interactuó de alguna otra forma con el mensaje.

Para integraciones nativas con Braze, los datos de activación e interacción pueden estar disponibles automáticamente a través de Braze Currents. Para otras configuraciones, estos datos deben proporcionarse de forma explícita.

Estos datos son críticos porque cierran el bucle entre una recomendación y su resultado. Sin ellos, el modelo no puede aprender qué decisiones están funcionando.

### Datos de conversiones {#conversions-data}

Los datos de conversiones describen lo que le sucedió al cliente después de que se hizo una recomendación y se envió un mensaje. Esta es la señal principal que el modelo utiliza para evaluar si una recomendación fue exitosa.

| Requisito | Razón |
|-------------|--------|
| Cada registro contiene el identificador de cliente, consistente con todos los demás activos | Decisioning Studio debe poder vincular las conversiones con las recomendaciones que las precedieron. |
| Cada registro tiene una marca de tiempo del momento en que ocurrió el evento de conversión | La precisión temporal es esencial para la atribución. El modelo necesita saber a qué recomendación se puede atribuir una conversión. |
| Si se utiliza una métrica de éxito no binaria (por ejemplo, ingresos en lugar de convertido o no convertido), el valor de la métrica debe incluirse con cada registro de conversión | Decisioning Studio utiliza el valor de la métrica para generar experiencias de entrenamiento. Sin el valor, el modelo solo puede aprender que ocurrió una conversión, no cuán valiosa fue. |
| Si las conversiones pueden atribuirse directamente a una comunicación específica (por ejemplo, canje de cupón), incluye los campos necesarios para vincular la conversión con el registro de activación | La atribución directa proporciona al modelo la señal de aprendizaje más clara. Si la atribución directa no es posible, Decisioning Studio utiliza la atribución basada en proximidad como alternativa. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datos de conversiones" }

## Activos opcionales {#optional-assets}

Más datos generalmente conducen a un mejor rendimiento del modelo, pero deben equilibrarse con el esfuerzo de implementación requerido. Los siguientes activos opcionales suelen ser útiles:

### Comportamiento del cliente {#customer-behavior}

- Historial de inicio de sesión en la cuenta
- Tipo de dispositivo y sistema operativo
- Interacciones con el servicio de atención al cliente (por ejemplo, número de llamadas de soporte, temas tratados)
- Uso del producto (por ejemplo, horas de uso al día, características utilizadas, categorías de contenido consultadas)

### Otras transacciones {#other-transactions}

- Productos comprados por fecha, incluidos los atributos del producto
- Importes de las transacciones
- Canales de transacción (por ejemplo, tienda física frente a en línea)
- Métodos de pago

### Otras interacciones de marketing {#other-marketing-engagement}

- Comunicaciones salientes enviadas fuera de las recomendaciones de Decisioning Studio (por ejemplo, correos electrónicos, SMS)
- Interacción con correos electrónicos no desencadenada por Decisioning Studio (por ejemplo, aperturas, clics)
- Respuestas a cuestionarios (por ejemplo, puntuaciones NPS, cuestionarios de interacción)
- Actividad en la web y en la aplicación móvil (por ejemplo, páginas visitadas, productos consultados)