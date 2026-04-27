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
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Casos de uso {#use-cases}

Esta integración admite las siguientes capacidades de Braze:

- **Sincronización de datos de usuario (`/users/track`):** Sincroniza atributos de miembros, eventos y compras con Braze para segmentación y personalización.
- **Desencadenamiento de Campaigns (`/campaigns/trigger/send`):** Desencadena mensajes únicos o transaccionales usando Campaigns de Braze.
- **Desencadenamiento de Canvas (`/canvas/trigger/send`):** Inicia recorridos de varios pasos y mensajería de ciclo de vida usando **Canvas** de Braze.
- **Segmentación y personalización:** Crea audiencias segmentadas y entrega comunicaciones personalizadas a partir de los datos sincronizados.

## Integración {#integration}

La integración de GRAVTY® y Braze está basada en API. Admite sincronización de datos en tiempo real y desencadenamiento de comunicaciones.

![Diagrama de flujo de GRAVTY® enviando datos y desencadenadores a las API de Braze, y luego mensajes a SMS, correo electrónico, push y WhatsApp.]({% image_buster /assets/img/lji/braze-gravty-integration.png %})

### Paso 1: Conectar Braze con GRAVTY® {#step-1-connect-braze-with-gravty}

1. Ve a **Subscriber Setup** en GRAVTY® para administrar las integraciones externas.
2. Selecciona **Add New Subscriber**.
3. Selecciona **Braze** como proveedor de integración.
4. Introduce lo siguiente:
   * **API URL** (tu punto de conexión REST de Braze)
   * **API Key** (tu clave de API REST de Braze)
5. Guarda la configuración y confirma que la conexión está activa.

![Formulario Add Subscriber de GRAVTY® con Braze seleccionado, campos de API URL y API key, y un interruptor de suscriptor activo.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### Paso 2: Configurar el mapeado de atributos de plantilla {#step-2-configure-template-attribute-mapping}

Después de guardar el suscriptor de Braze, GRAVTY® abre la página **Template Attribute Mapping**. Úsala para mapear campos a Braze.

1. Selecciona **Add New Field**.
2. Selecciona un **atributo de GRAVTY®** de la lista.
3. Introduce el **nombre del atributo de Braze** (atributo personalizado) donde el valor debe aparecer en Braze.

{% alert important %}
No necesitas mapear `external_id`. GRAVTY® lo genera internamente aplicando un hash al ID de miembro, y Braze recibe ese valor hasheado como `external_id` en el perfil de usuario.<br><br> Antes de habilitar la integración, confirma que esto coincide con la forma en que configuras `external_id` en Braze actualmente. Si Braze ya usa un `external_id` diferente para las mismas personas, trabaja con LJI para alinear los identificadores antes de sincronizar datos.
{% endalert %}

{: start="4"}
4. Repite los pasos 1–3 para agregar más mapeados.
5. Selecciona **Save**.

![Página Subscription Setup de GRAVTY® con configuración de plantilla, configuración de sincronización y una tabla que mapea entidad, atributo de GRAVTY® y campos de atributo de plantilla para Braze.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
La integración admite tipos de datos de atributos personalizados de Braze, incluidos números (enteros, flotantes), cadenas, arrays, booleanos, objetos, arrays de objetos y fechas.
{% endalert %}

### Paso 3: Probar la integración {#step-3-test-the-integration}

Desencadena un evento de prueba en GRAVTY® para confirmar la sincronización, los desencadenadores de comunicación y el flujo de extremo a extremo.

![Resumen del perfil de usuario en Braze mostrando perfil, atributos personalizados (nivel, fechas, país, ciudad) y eventos personalizados poblados desde el mapeado de GRAVTY®.]({% image_buster /assets/img/lji/braze-member-profile.png %})

## Soporte {#support}

Para soporte de integración o solución de problemas, ponte en contacto con LJI en [support@lji.io](mailto:support@lji.io).