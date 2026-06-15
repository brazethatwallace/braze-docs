---
nav_title: Fuentes de conocimiento
article_title: Fuentes de conocimiento
permalink: "/knowledge_sources/"
description: "Este artículo de referencia explica cómo crear y gestionar fuentes de conocimiento para tus agentes de BrazeAI."
page_type: reference
---

# Fuentes de conocimiento {#knowledge-sources}

> Las fuentes de conocimiento ayudan a tus agentes de IA a interpretar los datos del catálogo y recuperar la información adecuada para cumplir tus objetivos.

{% alert important %}
Las fuentes de conocimiento para la Consola de Agente se encuentran actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en este acceso anticipado.
{% endalert %}

## Cómo funciona {#how-it-works}

Las fuentes de conocimiento son un tipo de contexto de agente. Un agente de IA puede hacer referencia a una fuente de conocimiento para recuperar datos del catálogo con mayor precisión que si se hace referencia al catálogo directamente en las instrucciones del agente.

Supongamos que estás creando un agente para recomendar restaurantes en Nueva York basándose en la cocina favorita de un usuario, que es un atributo personalizado. Este agente hace referencia a la fuente de conocimiento del catálogo "nyc_restaurants". Cuando creas esa fuente de conocimiento, incluyes solo los campos que el agente necesita, como el nombre del restaurante, la ubicación y el tipo de cocina, y excluyes otras columnas del catálogo que no son relevantes para las recomendaciones.

Las instrucciones del agente describen claramente su función y sus restricciones:

{% raw %}
```
You are a restaurant recommendation agent. Use your knowledge to help find restaurants for the user. Only include filters in your knowledge source query. Don't ask any followup questions. The user's favorite cuisine is {{custom_attribute.${favorite_cuisine}}}
```
{% endraw %}

Si la cocina favorita de un usuario es la pizza, el agente puede devolver la siguiente respuesta basándose en la fuente de conocimiento:

```
Here are some pizza recommendations for you:
- Dale's Pizza (Greenwich Village, Manhattan): Dale's Pizza invites you to savor the taste of authentic New York. Nestled in the heart of Manhattan, this iconic pizzeria offers a warm and inviting atmosphere perfect for any occasion.
- Pizza Palace (Carroll Gardens, Brooklyn): Pizza Palace is a highly-rated culinary gem renowned for its exquisite pizza. This inviting spot offers a warm and modern dining experience.
```

## Crear una fuente de conocimiento {#create-a-knowledge-source}

Para crear una fuente de conocimiento:

1. Ve a **Consola de Agente** > **Fuentes de conocimiento**.
2. Selecciona **Añadir fuente de conocimiento**. En el menú desplegable, selecciona **Catálogo**.
3. Selecciona el catálogo en el menú desplegable.
4. Revisa los campos del catálogo y desmarca los que no apliquen al caso de uso de tu agente. Recomendamos excluir los campos del catálogo que no sean útiles para la recuperación o la generación; limita la fuente de conocimiento solo a los campos que tu agente necesita.
5. (opcional) Añade una descripción para describir lo que contiene la fuente de conocimiento.
6. Selecciona **Añadir fuente de conocimiento**.

Incluir todos los campos del catálogo puede añadir contexto innecesario y reducir la calidad de los resultados. Desmarcar los campos que no son relevantes para tu caso de uso ayuda al agente a centrarse en los datos que importan.

![Una fuente de conocimiento "nyc_restaurants" que hace referencia al catálogo "nyc_restaurants".]({% image_buster /assets/unlisted_docs/img/knowledge_sources/knowledge_source_example.png %}){: style="max-width:80%;"}

También puedes crear una fuente de conocimiento mientras construyes un agente yendo a la sección **Instrucciones** de tu agente. Luego, selecciona **Añadir conocimiento** > **Crear fuente de conocimiento**.

## Usar una fuente de conocimiento en tu agente de IA {#use-a-knowledge-source-in-your-ai-agent}

Puedes gestionar las fuentes de conocimiento desde la sección **Fuentes de conocimiento**. Aquí puedes ver detalles como qué fuentes de conocimiento están activas y cuándo se sincronizaron por última vez. Ten en cuenta que el nombre de la fuente de conocimiento coincide con el nombre del catálogo utilizado como fuente.

Para usar una fuente de conocimiento en tu agente de IA:

1. Ve a la sección **Instrucciones** de tu agente.
2. Luego, selecciona **+ Contexto de agente** > **Añadir conocimiento**.
3. En el menú desplegable, selecciona la fuente de conocimiento.

Ahora, tu agente puede hacer referencia a la fuente de conocimiento y recuperar los datos relevantes del catálogo.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo funcionan las fuentes de conocimiento? {#how-do-knowledge-sources-work}

Convertir un catálogo en una fuente de conocimiento ayuda a los agentes de Braze a comprender el verdadero significado detrás de las palabras y frases del catálogo, de modo que los agentes puedan encontrar datos significativos de forma más eficaz para generar mejores resultados.

### ¿Cuándo debo crear una fuente de conocimiento? {#when-should-i-create-a-knowledge-source}

Crea una fuente de conocimiento cuando quieras configurar un agente personalizado (agente de Canvas o agente de Catálogo) que pueda usar un catálogo como contexto. Usar fuentes de conocimiento es una mejor forma de adjuntar un catálogo como contexto en comparación con el método existente.

### Si a un agente se le ha proporcionado una fuente de conocimiento como contexto, ¿también necesito asignar el catálogo original como contexto? {#if-an-agent-has-been-given-a-knowledge-source-as-context-do-i-also-need-to-assign-the-original-catalog-as-context}

No. La fuente de conocimiento reemplaza al catálogo como contexto del agente; no necesitas adjuntar ambos. Cuando crees la fuente de conocimiento, incluye solo los campos del catálogo que tu agente necesita.

### ¿Cómo debo evaluar la eficacia de una fuente de conocimiento? {#how-should-i-evaluate-the-efficacy-of-knowledge-source}

Duplica cualquier agente existente que utilices y que haga referencia a un catálogo normal, y cámbialo para que haga referencia a la fuente de conocimiento equivalente. Ejecuta algunas invocaciones de prueba en la Consola de Agente para verificar la precisión y luego considera reemplazar el agente existente donde esté desplegado, o realizar pruebas A/B del agente antiguo frente al nuevo (usando la ruta de experimentos) para comprender el impacto en el rendimiento.