---
nav_title: Conectar orígenes de datos
article_title: Conectar orígenes de datos
page_order: 1
description: "Descubre cómo BrazeAI Decisioning Studio Go se conecta a los datos de clientes a través de tu plataforma de interacción con los clientes."
---

# Conectar orígenes de datos {#connect-data-sources}

> BrazeAI Decisioning Studio™ Go se conecta a los datos de tus clientes a través de tu plataforma de interacción con los clientes (CEP). Este artículo explica qué datos se utilizan y cómo funciona la conexión.

## Cómo Go accede a los datos de clientes {#how-go-accesses-customer-data}

A diferencia de Decisioning Studio Pro, que admite integraciones directas de datos con diversos orígenes, Decisioning Studio Go accede a los datos de clientes a través de tu CEP. Esto significa:

- **Los datos de audiencia** se extraen directamente de los segmentos o listas definidos en tu CEP (Braze o Salesforce Marketing Cloud) y solo pueden incluir determinados atributos predefinidos (no datos 1P).
- **Los datos de interacción** (aperturas, clics, envíos) se recopilan mediante consultas automatizadas o integraciones nativas con tu CEP.
- **No** es necesario **configurar ningún canal de datos adicional** más allá de lo que configures en tu CEP.

## Patrones de integración compatibles {#supported-integration-patterns}

Decisioning Studio Go admite los siguientes CEP para el acceso a datos:

| CEP | Fuente de audiencia | Datos de interacción |
|-----|-----------------|-----------------|
| **Braze** | Segments | Exportación de Braze Currents |
| **Salesforce Marketing Cloud** | Extensiones de datos | Automatización de consultas SQL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Requisitos de datos según el CEP {#data-requirements-by-cep}

{% tabs %}
{% tab Braze %}

### Requisitos de datos de Braze {#braze-data-requirements}

Para las integraciones de Braze, Decisioning Studio Go requiere:

1. **Braze Currents:** debes tener Braze Currents habilitado y configurado para exportar datos de interacción a Decisioning Studio Go. Esto permite al agente aprender de las respuestas de los clientes.

2. **Acceso a Segments:** la clave de API que crees debe tener permisos para acceder a los segmentos que definen tu audiencia objetivo.

3. **Datos del perfil de usuario:** cualquier atributo del perfil de usuario o atributo personalizado que desees que el agente tenga en cuenta debe ser accesible a través de la API de Braze.

{% alert important %}
Asegúrate de que tu exportación de Braze Currents incluya datos de todas las Campaigns con las que quieras comparar (incluidas las Campaigns BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### Requisitos de datos de SFMC {#sfmc-data-requirements}

Para las integraciones de Salesforce Marketing Cloud, Decisioning Studio Go requiere:

1. **Extensiones de datos:** tu audiencia debe estar definida en una extensión de datos a la que Decisioning Studio Go pueda acceder. Utiliza la SubscriberKey como identificador principal del usuario.
2. **Acceso al seguimiento de eventos:** siempre que el paquete de aplicaciones instalado admita la configuración automatizada de extremo a extremo, no se requiere ninguna configuración adicional.

Las extensiones de datos y las consultas SQL se configuran como parte de la [configuración de la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/).

{% endtab %}
{% endtabs %}

## Buenas prácticas {#best-practices}

- **Mantén los datos actualizados:** asegúrate de que tus segmentos de audiencia y datos de clientes se actualicen con regularidad (como mínimo, a diario) para que el agente trabaje con información actualizada.
- **Incluye los atributos relevantes:** piensa en qué características de los clientes podrían influir en los mensajes que mejor les funcionan: los datos demográficos, el historial de interacción, el comportamiento de compra y la etapa del ciclo de vida son señales muy valiosas.

## Próximos pasos {#next-steps}

Ahora que ya sabes cómo se conecta Go a los datos, continúa con la configuración de la integración CEP:

- [Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)