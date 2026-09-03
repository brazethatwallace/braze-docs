---
nav_title: Privacidad y seguridad de datos
article_title: Privacidad y seguridad de datos para BrazeAI Operator
page_order: 5
page_type: reference
description: "Este artículo de referencia cubre cómo BrazeAI Operator gestiona los datos, incluyendo el cumplimiento de HIPAA, la retención de datos, la minimización de PII y la gobernanza."
---

# Privacidad y seguridad de datos para BrazeAI Operator {#data-privacy-and-security-for-brazeai-operator}

> BrazeAI Operator<sup>TM</sup> se integra con OpenAI para proporcionar asistencia impulsada por IA. Este artículo cubre cómo Operator gestiona los datos, qué información se comparte con OpenAI y cómo minimizar la exposición de PII y controlar el acceso.

## Cómo Operator accede a los datos {#how-operator-accesses-data}

El acceso de Operator a los datos de clientes es estrictamente basado en eventos y limitado al ámbito de la invocación, no persistente. Cada mensaje de usuario o evento de navegación mientras Operator está abierto desencadena una solicitud HTTP discreta a OpenAI. No existe una conexión permanente ni un flujo de datos persistente.

OpenAI no tiene acceso directo a los almacenes de datos de Braze ni a la tabla de usuarios completa. El LLM recibe únicamente la carga útil específica asociada a la solicitud activa.

### Qué datos se incluyen en cada solicitud {#what-data-is-included-in-each-request}

Cada carga útil de solicitud enviada a OpenAI puede incluir lo siguiente:

- **Metadatos del sistema:** indicaciones del sistema creadas por Braze y esquemas de herramientas (definiciones de herramientas que el LLM puede invocar).
- **Mensaje del usuario del panel:** la entrada escrita por el usuario del panel.
- **Resultados de herramientas:** resultados de búsqueda que contienen nombres, ID y datos relacionados.
- **Contenido de la página extraído:** contenido de la página activa del panel, truncado a aproximadamente 4000 caracteres.
- **Cadenas de contexto de la página:** cadenas contextuales de la página activa del panel.

## Subprocesadores de datos {#data-sub-processors}

### Proveedores de modelos como subprocesadores o proveedores externos {#model-providers-as-sub-processors-or-third-party-providers}

Cuando utilizas una integración con un proveedor de LLM proporcionado por Braze a través de los servicios de Braze ("LLM proporcionado por Braze"), los proveedores de dicho LLM proporcionado por Braze actúan como subprocesadores de Braze, sujetos a los términos del Anexo de Procesamiento de Datos (DPA) entre tú y Braze. BrazeAI Operator<sup>TM</sup> se integra con OpenAI.

### Cómo se utilizan los datos con OpenAI {#how-data-is-used-with-openai}

Para generar resultados de IA a través de las características de BrazeAI que aprovechan OpenAI ("Resultados"), Braze enviará cierta información ("Entrada") a OpenAI. La Entrada consiste en tus indicaciones, el contenido mostrado en el panel y los datos del espacio de trabajo relevantes para tus consultas. Según los [compromisos de la plataforma API de OpenAI](https://openai.com/enterprise-privacy/), los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar ni mejorar los modelos de OpenAI. Entre tú y Braze, los Resultados son tu propiedad intelectual. Braze no reclamará ningún derecho de propiedad de copyright sobre dichos Resultados. Braze no ofrece ninguna garantía de ningún tipo con respecto a cualquier contenido generado por IA, incluidos los Resultados.

## Cumplimiento de HIPAA y retención de datos {#hipaa-compliance-and-data-retention}

### Cumplimiento de HIPAA {#hipaa-compliance}

Si utilizas el clúster US-02 de Braze, Operator está cubierto por el Acuerdo de Asociado Comercial (BAA) de Braze, y la Información de Salud Personal (PHI) puede enviarse a la característica de acuerdo con los requisitos de HIPAA. No envíes PHI sujeta a HIPAA cuando utilices Operator en otros clústeres de Braze.

### Redacción de PII {#pii-redaction}

No existe una capa automatizada de redacción de PII en el flujo de solicitudes de Operator. Los datos se envían completamente sin procesar y no se anonimizan antes de la transmisión a OpenAI. El acceso está limitado a la página activa del panel o a la entrada del usuario del panel, pero no se aplica ningún filtrado de contenido antes de la transmisión.

### Retención de datos de OpenAI {#openai-data-retention}

El tiempo que OpenAI retiene los datos enviados a través de Operator depende de tu clúster:

| Clúster | Retención |
| --- | --- |
| US-02 (clientes HIPAA) | Retención de datos cero (ZDR). Los datos no son almacenados por OpenAI después del procesamiento. |
| Todos los demás clústeres | 30 días para monitoreo de abuso. Este es un período de retención estándar de la industria impuesto por OpenAI. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Retención de datos de OpenAI por clúster" }

### Entrenamiento de modelos {#model-training}

Los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar ni mejorar los modelos de OpenAI. Esto se rige por acuerdos contractuales entre Braze y OpenAI y los compromisos de la plataforma API de OpenAI. OpenAI actúa como subprocesador de Braze, y todos los datos personales están sujetos al DPA entre Braze y sus clientes.

### Enrutamiento de datos en la UE {#eu-data-routing}

El enrutamiento de datos en la UE no está implementado actualmente para Operator, y no hay planes actuales para implementarlo.

## Minimizar la exposición de PII {#minimize-pii-exposure}

Hay varios pasos que puedes seguir para limitar la exposición de PII al usar Operator:

- **Desactiva la configuración Ver PII** para cualquier usuario que utilice Operator. Si un usuario no puede ver PII, Operator tampoco puede acceder a ella.
- **No abras Operator en una página de perfil de usuario.** El contenido de la página se extrae y se incluye en cada solicitud enviada a OpenAI.
- **Al hacer pruebas, usa un perfil de usuario personalizado** en lugar de seleccionar uno existente. Este es el comportamiento predeterminado de Operator.
- **No escribas ni pegues PII** directamente en la indicación de Operator. Operator no bloquea la PII incluida en las indicaciones de los usuarios. Si un usuario escribe PII manualmente en una solicitud, ese contenido se envía al modelo de lenguaje subyacente.
- **Desactiva la aprobación automática de acciones** para mantener el control sobre lo que Operator puede acceder y ejecutar.
- **No le pidas a Operator que muestre valores de vista previa para atributos** al crear un segmento o escribir Liquid.

## Gobernanza y control de acceso {#governance-and-access-control}

### Restringir el acceso a Operator {#restrict-access-to-operator}

El acceso a Operator se gestiona a nivel de espacio de trabajo a través de [permisos granulares de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Los administradores pueden otorgar o revocar el permiso "Use BrazeAI Operator" para usuarios individuales, asegurando que solo el personal autorizado pueda interactuar con la herramienta. Sin estos permisos específicos, la interfaz de Operator se suprime completamente y los endpoints del backend permanecen protegidos.

### Modelo de intervención humana {#human-in-the-loop-model}

De forma predeterminada, Operator requiere aprobación explícita antes de confirmar cualquier cambio. Las modificaciones propuestas se presentan como [tarjetas de acción]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) para su revisión. Si un usuario rechaza una propuesta, no se realizan cambios. Si un usuario acepta una propuesta, el panel se actualiza, pero los cambios quedan pendientes y deben guardarse o lanzarse manualmente para que sean persistentes.

Los usuarios pueden habilitar **Auto-approve actions** en el panel de chat de Operator, lo que hace que las acciones sugeridas se ejecuten inmediatamente sin revisión manual. Incluso con la aprobación automática habilitada, algunas acciones siempre requieren aprobación explícita por seguridad, incluyendo la generación de imágenes y la modificación de configuraciones a nivel de espacio de trabajo.

### Herencia de permisos de usuario {#user-permission-inheritance}

Operator hereda completamente el perfil de permisos del usuario que ha iniciado sesión. Tiene restringido ver datos o ejecutar acciones, como modificaciones de campañas, que el usuario no está autorizado a realizar de forma independiente.

### Permiso Ver PII {#view-pii-permission}

Operator no requiere el permiso "Ver PII" para funcionar, y esto es intencional. Operator no tiene acceso directo a tu almacén de datos y no consulta tu base de datos de forma independiente. En su lugar, realiza solicitudes a los mismos endpoints del backend que el resto del panel, utilizando las credenciales de sesión del usuario autenticado. Esto significa que Operator está completamente limitado por los [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) existentes del usuario y no puede acceder a nada que el usuario no pueda ver ya.

La PII solo puede llegar a Operator de dos maneras:

- El usuario escribe PII directamente en una indicación.
- El usuario ya está viendo PII en el panel cuando utiliza Operator.

Si un usuario no tiene el permiso "Ver PII", Operator no puede mostrarle PII. Ten en cuenta que Operator no filtra el contenido escrito directamente en las indicaciones: la PII ingresada manualmente se envía al modelo de lenguaje subyacente. Para reducir este riesgo, consulta [Minimizar la exposición de PII](#minimize-pii-exposure).

### Auditar el uso del equipo {#audit-team-usage}

Descarga el [Informe de eventos de seguridad]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) de Braze para monitorear el uso del equipo. El evento "Requested BrazeAI Operator Response" proporciona un registro de auditoría completo, que te permite revisar las entradas exactas proporcionadas a Operator.