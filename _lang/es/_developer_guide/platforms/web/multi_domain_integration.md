---
nav_title: Integración multidominio
article_title: Integración multidominio para el SDK or kit de desarrollo de software Web de Braze
platform: Web
page_order: 23
page_type: reference
description: "Aprende a implementar el SDK or kit de desarrollo de software Web de Braze en varios dominios, incluyendo la estrategia de claves de API, la configuración push y el comportamiento de sesiones."
---

# Integración multidominio {#multi-domain-integration}

> Aprende a integrar el SDK or kit de desarrollo de software Web de Braze en varios dominios web.

Cuando tu implementación abarca varios dominios, los límites de origen del navegador afectan la forma en que el SDK or kit de desarrollo de software Web de Braze almacena y lee el estado del usuario.

## Elige una estrategia de aplicación y clave de API {#choose-an-app-and-api-key-strategy}

Puedes usar una sola clave de API del SDK or kit de desarrollo de software Web en varios dominios, pero en la mayoría de los casos, usar claves de API separadas asignadas a aplicaciones distintas en el mismo espacio de trabajo te da un mejor control.

| Estrategia | Recomendada cuando | Compensaciones |
|---|---|---|
| **Aplicaciones separadas (recomendado)** | Quieres segmentación, informes y control de campañas independientes por dominio | Requiere gestionar dos integraciones de aplicación |
| **Aplicación única** | Tratas ambos dominios como una sola propiedad operativamente | Los desencadenadores de sesión y los informes a nivel de dominio son más difíciles de separar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Opciones de estrategia de aplicación y clave de API" }

Con aplicaciones separadas en un espacio de trabajo, puedes usar filtros de aplicación para una segmentación más limpia y una segmentación de mensajes por dominio.

## Configura notificaciones push en un dominio {#configure-push-notifications-on-one-domain}

Para dominios raíz separados, el registro de notificaciones push web está aislado por dominio.

- Elige un dominio como tu dominio de notificaciones push.
- No registres push en ambos dominios raíz para el mismo recorrido de usuario, ya que esto puede crear comportamientos conflictivos de solicitud y suscripción.

## Identifica usuarios de forma consistente entre dominios {#identify-users-consistently-across-domains}

De forma predeterminada, cada dominio raíz almacena su propio estado del SDK or kit de desarrollo de software. Para asociar la actividad al mismo perfil de usuario de Braze entre dominios:

- Llama a [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) con el mismo `external_id` en cada dominio después de iniciar sesión.
- Mantén ambas aplicaciones en el mismo espacio de trabajo si estás usando claves de API separadas.

Para orientación general sobre ID de usuario, consulta [Establecer ID de usuario a través del SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## Planifica el comportamiento de eventos y desencadenadores por dominio {#plan-event-and-trigger-behavior-by-domain}

La forma en que modelas eventos y desencadenadores depende de tu estrategia de aplicación:

- **Aplicación única en varios dominios:** Registra eventos personalizados específicos del dominio para poder distinguir el comportamiento por sitio en la segmentación y los desencadenadores.
- **Aplicaciones separadas:** Prefiere los filtros de aplicación para la segmentación y los análisis específicos del dominio.

## Comprende el comportamiento de sesiones entre dominios {#understand-session-behavior-across-domains}

De forma predeterminada, el tiempo de espera de sesión del SDK or kit de desarrollo de software Web es de 30 minutos de inactividad. Para dominios raíz separados que usan una sola aplicación/clave de API:

- Cada dominio inicia y finaliza sesiones de forma independiente.
- Un usuario que se mueve entre ambos dominios puede crear sesiones superpuestas.
- Los desencadenadores de inicio de sesión pueden activarse en ambos dominios.

Para detalles sobre el ciclo de vida base de las sesiones, consulta [Rastrear sesiones a través del SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).