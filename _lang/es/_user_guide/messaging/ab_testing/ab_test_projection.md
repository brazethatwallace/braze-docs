---
nav_title: Proyección de pruebas A/B
article_title: Proyección de pruebas A/B
page_order: 20
hidden: true
page_type: reference
description: "Este artículo explica cómo funciona la proyección de pruebas A/B, cómo ejecutar una proyección y cómo utiliza Braze tus datos."
---

# Proyección de pruebas A/B {#ab-test-projection}

> La proyección de pruebas A/B utiliza redes neuronales para predecir qué líneas del asunto tienen mejor rendimiento. Nuestro modelo extrae las características lingüísticas de las pruebas A/B ganadoras realizadas en Braze y utiliza esos patrones lingüísticos estadísticos para enseñar a nuestra IA cuáles son las mejores líneas del asunto.

{% alert important %}
Esta característica se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas o de éxito del cliente de Braze si te interesa participar en el acceso anticipado.
{% endalert %}

## Ejecutar una proyección {#running-a-projection}

En la composición de la campaña, inserta tus variantes de mensaje y sus líneas del asunto en el editor. Cuando estés listo, ve al paso **Target Audience** del flujo de creación de campañas. En el panel **A/B Testing**, selecciona **Run Projection**.

<img width="518" alt="imagen" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Se abrirá un modal con las líneas del asunto de cualquier variante de mensaje que ya hayas creado. Opcionalmente, puedes insertar líneas del asunto adicionales (hasta un máximo de diez) introduciéndolas manualmente en el campo y ejecutando la proyección. Selecciona **Run Projection**.

<img width="722" alt="imagen" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

La línea del asunto que nuestra IA predice como la mejor se resaltará con una etiqueta de **Projected Winner**.

{% alert note %}
Para las [campañas push rápidas]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/quick_push_messages/), las pruebas A/B son compatibles cuando seleccionas múltiples plataformas.
{% endalert %}

### ¿Qué tan precisas son las proyecciones? {#how-accurate-are-the-projections}

En las pruebas, encontramos que las proyecciones tienen una precisión de aproximadamente el 70 % al elegir entre pares de mensajes en pruebas A/B reales. Ten esto en cuenta al interpretar los mensajes que el modelo proyecta como ganadores.

### ¿Cómo utilizamos tus datos? {#how-do-we-use-your-data}

Esta característica aprende de pruebas A/B anteriores realizadas en Braze. El texto real de tus mensajes o de los mensajes de cualquier cliente de Braze nunca se proporciona al modelo. Primero extraemos los patrones lingüísticos de alto nivel que predicen los mensajes ganadores en las pruebas A/B. Luego, proporcionamos esos patrones a nuestra IA para enseñarle a discernir qué características lingüísticas constituyen líneas del asunto superiores.