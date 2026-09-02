---
nav_title: Usar el ID externo de Braze
article_title: Usar el ID externo de Braze
page_order: 5
page_type: reference
description: "Este artículo de referencia explica por qué Decisioning Studio utiliza el ID externo de Braze como unidad de identidad del cliente y qué sucede si se usa una estructura de identificador diferente."
---

# Usar el ID externo de Braze {#use-braze-external-id}

> Decisioning Studio requiere un identificador de cliente único y estable que sea consistente en todos los activos de datos. La recomendación es usar el ID externo de Braze como ese identificador. Este artículo explica por qué y qué riesgos surgen cuando se utilizan otras estructuras de identificador en su lugar.

## ¿Por qué usar el ID externo de Braze? {#why-use-braze-external-id}

Decisioning Studio opera exclusivamente usando el ID externo de Braze como su unidad de identidad del cliente. Todos los activos de datos (perfiles de usuario, características, activaciones, interacciones, conversiones) deben hacer referencia al ID externo de Braze como el identificador principal del cliente.

Más allá de cumplir un requisito técnico, requerir el ID externo de Braze es una decisión de diseño deliberada que protege la fiabilidad del entrenamiento y las recomendaciones del modelo.

### Desafíos de otros identificadores {#challenges-of-other-identifiers}

Muchas organizaciones mantienen dos sistemas de identificador de cliente diferentes:

- **Un ID de almacén de datos o sistema de registro** (a veces llamado "ID canónico" o "ID físico"): la fuente de verdad para métricas como el LTV or valor de duración del ciclo de vida or valor de duración del ciclo de vida, devoluciones y fidelización. Reside en tu almacén de datos o ERP.
- **Un ID de plataforma:** el identificador utilizado por herramientas como Braze, normalmente vinculado a una dirección de correo electrónico, token de dispositivo o un canal de activación similar.

La tentación es usar el ID del almacén de datos para construir características de cliente (ya que ahí es donde residen los datos) y el ID de Braze para la activación (ya que es lo que usa Braze). Pero esto requiere una capa de traducción entre los dos sistemas, y esa capa de traducción introduce fragilidad.

#### Deriva de identidad {#identity-drift}

Incluso si el mapeado entre tu ID de almacén de datos y tu ID de Braze es actualmente de uno a muchos (un cliente físico se mapea a múltiples perfiles de Braze), ese mapeado puede desestabilizarse con el tiempo y convertirse en muchos a muchos. Si un único ID de almacén de datos se reasigna a diferentes clientes con el tiempo, o si el mismo perfil de Braze se asocia con múltiples ID de almacén de datos, el resultado es **deriva de identidad**.

La deriva de identidad causa:

- **Fallos en el entrenamiento del modelo:** si el cliente al que el modelo creía estar recomendando es en realidad una persona diferente, la señal de entrenamiento se corrompe.
- **Inexactitudes en los informes:** las métricas pierden sentido cuando el mapeado de identidad subyacente es inestable.
- **Errores de atribución:** las conversiones se asocian con las recomendaciones incorrectas.

### Cómo el ID externo de Braze aborda estos riesgos {#how-braze-external-id-addresses-these-risks}

#### Listo para la activación por diseño {#activation-ready-by-design}

Las recomendaciones generadas a partir de un ID externo de Braze pueden inyectarse directamente en los mensajes a través de Liquid o contenido conectado sin ningún paso de traducción de ID. Eliminar la capa de traducción elimina una fuente significativa de complejidad operativa y fallos.

#### Aislado de cambios en sistemas anteriores {#isolated-from-upstream-changes}

Al operar con el ID externo de Braze, Decisioning Studio está aislado de los cambios en tus sistemas anteriores. Si tu ID interno de almacén de datos cambia debido a una migración de sistema, una corrección de calidad de datos o una actualización de ERP, el ID externo de Braze, y todo lo asociado a él, permanece estable.

#### Separación limpia de canales {#clean-channel-separation}

En Braze, un perfil de usuario corresponde a un canal de comunicación alcanzable. Si un cliente registra dos direcciones de correo electrónico, tiene dos perfiles de Braze distintos con dos ID externos de Braze distintos. Decisioning Studio los trata como dos entidades separadas, lo que significa que las recomendaciones y el historial de eventos de un correo electrónico no se contaminan con la actividad asociada al otro.

Esto previene lo que podría llamarse "contaminación de contexto". La herramienta de recomendaciones no mezclaría, por ejemplo, el comportamiento de compra relacionado con el trabajo en las recomendaciones enviadas a una cuenta de correo electrónico personal.

## Consideraciones de múltiples entidades {#multi-entity-considerations}

### Negocios multitienda o jerárquicos {#multi-store-or-hierarchical-businesses}

Para negocios que operan múltiples tiendas o submarcas (por ejemplo, un franquiciador con muchos franquiciados), el concepto de "cliente" puede ser ambiguo. Un cliente que compra en múltiples ubicaciones puede tener registros separados en cada ubicación, pero debería tratarse como una sola persona para fines de recomendación.

Si tu negocio tiene esta estructura, consulta con tu equipo de Decisioning Studio cómo modelar la jerarquía de clientes antes de finalizar tu estrategia de identificador.

### Fragmentación de identidad B2C {#b2c-identity-fragmentation}

Una sola persona física puede acumular múltiples perfiles de Braze con el tiempo, por ejemplo, al registrarse con diferentes direcciones de correo electrónico o al iniciar sesión en diferentes dispositivos antes de la fusión de cuentas. Decisioning Studio trata cada ID externo de Braze como un cliente distinto.

Esto es por diseño: cada perfil representa un canal de activación distinto. Sin embargo, esto significa que la calidad de tus recomendaciones depende de la calidad de tu resolución de identidad en Braze. Si tu implementación de Braze no fusiona de manera fiable los perfiles duplicados, algunos clientes pueden recibir una personalización de menor calidad porque su historial está fragmentado en múltiples perfiles.