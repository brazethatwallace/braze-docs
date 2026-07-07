---
nav_title: GRAVTY®
article_title: Plataforma de fidelización GRAVTY®
description: "Este artículo describe la asociación entre Braze y GRAVTY®, una plataforma de fidelización de nivel empresarial que permite a las marcas diseñar, administrar y escalar programas de fidelización basados en datos para mejorar la interacción con los clientes y la retención."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# Plataforma de fidelización GRAVTY® {#gravty-loyalty-platform}

> [GRAVTY®](https://www.lji.io/) es una plataforma de fidelización de nivel empresarial de Loyalty Juggernaut Inc. (LJI) que permite a las marcas de comercio minorista, viajes, restaurantes (incluidos los de servicio rápido) y servicios financieros diseñar, administrar y escalar programas de nueva generación, impulsando un crecimiento medible en interacción, retención y valor de duración del ciclo de vida del cliente a través de experiencias personalizadas y basadas en datos.

Construida sobre una arquitectura flexible y API-first, GRAVTY® admite acumulación y canje en tiempo real, gestión de ecosistemas de socios e integración entre canales. Los equipos pueden lanzar más rápido, iterar en los programas y ofrecer experiencias de fidelización a escala.

_Esta integración es mantenida por LJI._

## Acerca de la integración {#about-the-integration}

La integración de Braze y GRAVTY® conecta los datos de fidelización y los desencadenadores de mensajería en ambas plataformas. GRAVTY® envía datos de usuario a Braze como atributos, eventos y compras. Braze almacena esos datos y entrega mensajes a través de canales como SMS, correo electrónico y notificaciones push. Puedes usar los datos sincronizados para segmentación, personalización y desencadenadores.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

| Requisito | Descripción |
| :--- | :--- |
| Cuenta de GRAVTY® | Una cuenta de GRAVTY® con permiso para configurar integraciones y administrar suscripciones de eventos. |
| Cuenta de Braze | Una cuenta activa de Braze con acceso a la API habilitado. |
| Clave de API REST de Braze | Una clave de API REST con permisos `campaigns.trigger.send`, `canvas.trigger.send` y `users.track`.<br><br> Crea esta clave en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión de la API de Braze | Tu punto de conexión REST de Braze (por ejemplo, `https://rest.fra-01.braze.eu`). Para más información, consulta [Instancias y puntos de conexión de Braze]({{site.baseurl}}/api/basics/#endpoints). |
| IDs de Campaign o Canvas | IDs de los flujos de trabajo de **Campaigns** o **Canvas** que desencadenas desde GRAVTY®. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

Esta integración admite las siguientes capacidades de Braze:

- **Sincronización de datos de usuario (`/users/track`):** Sincroniza atributos de miembros, eventos y compras con Braze para segmentación y personalización.
- **Desencadenamiento de Campaigns (`/campaigns/trigger/send`):** Desencadena mensajes únicos o transaccionales usando Campaigns de Braze.
- **Desencadenamiento de Canvas (`/canvas/trigger/send`):** Inicia recorridos de varios pasos y mensajería de ciclo de vida usando **Canvas** de Braze.
- **Segmentación y personalización:** Crea audiencias segmentadas y entrega comunicaciones personalizadas a partir de los datos sincronizados.

## Integración {#integration}

La integración de GRAVTY® y Braze está basada en API, lo que permite la sincronización de datos en tiempo real y el desencadenamiento de comunicaciones entre GRAVTY® y Braze.

### Paso 1: Conectar Braze con GRAVTY® {#step-1-connect-braze-with-gravty}

1. Ve a **Subscriber Setup** en GRAVTY® para administrar las integraciones externas.
2. Selecciona **Add New Subscriber**.
3. Selecciona **Braze** como proveedor de integración.
4. Introduce lo siguiente:
   * **API URL** (tu punto de conexión REST de Braze)
   * **API Key** (tu clave de API REST de Braze)
5. Guarda la configuración y confirma que la conexión está activa.

![Formulario Add Subscriber de GRAVTY® con Braze seleccionado, campos de API URL y API key, y un interruptor de suscriptor activo.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### Paso 2: Configurar el desencadenador de eventos {#step-2-configure-event-trigger}

Crea un evento en GRAVTY® que se ejecute cuando la actividad de un miembro cumpla las condiciones que definas (por ejemplo, una transacción, puntos acumulados, un cambio de nivel o la inscripción en un programa).

1. Navega a la sección **Events** en GRAVTY®.
2. Haz clic en **Create Event**.
3. Define las condiciones del evento (por ejemplo, transacción creada, puntos acumulados o ascenso de nivel).
4. Configura las reglas que determinan cuándo debe desencadenarse el evento.
5. Adjunta el suscriptor de Braze al evento para habilitar los desencadenadores de comunicación.
6. Guarda la configuración del evento.

El siguiente es un ejemplo de un evento configurado para desencadenarse cuando un miembro se inscribe en el programa:

![Configuración de evento en GRAVTY® para la inscripción de un miembro en el programa, con Braze adjunto como suscriptor.]({% image_buster /assets/img/lji/event-configuration.png %})

### Paso 3: Configurar el mapeado de atributos de plantilla {#step-3-configure-template-attribute-mapping}

Después de configurar el evento, completa la configuración del suscriptor para habilitar la sincronización de datos y los desencadenadores de comunicación:

1. Selecciona el **suscriptor de Braze** creado en el paso 1 desde el menú desplegable de suscriptores.
2. Elige el **canal** apropiado (**Campaign** o **Canvas**) según tu caso de uso. Para escenarios de solo sincronización de datos, el canal puede dejarse sin seleccionar.
3. Introduce el **Campaign ID** o **Canvas ID** correspondiente en el campo **Template Name**, según corresponda.
4. Configura el tipo de comunicación para admitir sincronización y/o mensajería basada en desencadenadores.

Para configurar el mapeado de campos en GRAVTY®:

1. Haz clic en **Add New Field**.
2. Selecciona el **atributo de GRAVTY®** del menú desplegable.
3. Introduce el **nombre del atributo de Braze** correspondiente donde deben mapearse los datos.

{% alert important %}
No necesitas mapear `external_id`. GRAVTY® lo genera internamente aplicando un hash al ID de miembro (el identificador único de miembro en GRAVTY®), y Braze recibe ese valor hasheado como `external_id` en el perfil de usuario.<br><br> Antes de habilitar la integración, confirma que esto coincide con la forma en que configuras `external_id` en Braze actualmente. Si Braze ya usa un `external_id` diferente para las mismas personas, trabaja con LJI para alinear los identificadores antes de sincronizar datos.
{% endalert %}

{: start="4"}
4. Repite los pasos **1–3** para agregar mapeados adicionales según sea necesario.
5. Haz clic en **Save** para aplicar la configuración.

![Configuración de mapeado de atributos para la sincronización de miembros con Braze.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
La integración admite todos los tipos de datos de atributos personalizados de Braze, incluidos números (enteros, flotantes), cadenas, arrays, booleanos, objetos, arrays de objetos y fechas.
{% endalert %}

### Paso 4: Probar la integración {#step-4-test-the-integration}

Desencadena un evento de prueba en GRAVTY® para verificar que la sincronización, los desencadenadores de comunicación y la integración general funcionan como se espera.

* Los datos del miembro se sincronizan con Braze y se reflejan en el perfil del miembro.

![Los campos de datos se completan según el mapeado de campos configurado.]({% image_buster /assets/img/lji/braze-member-profile.png %})

* La comunicación se desencadena según la Campaign o el Canvas configurados.

![Ejemplo de un correo electrónico desencadenado desde Braze.]({% image_buster /assets/img/lji/braze-email-example.png %})

## Soporte {#support}

Para soporte de integración o solución de problemas, ponte en contacto con LJI en [support@lji.io](mailto:support@lji.io).