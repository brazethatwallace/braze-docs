---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "La integración de Braze y Movable Ink Da Vinci permite a las marcas entregar mensajes altamente personalizados aprovechando el motor de toma de decisiones sobre contenidos basado en IA de Da Vinci. Da Vinci selecciona el contenido más relevante para cada usuario y despliega fácilmente los mensajes a través de Braze."
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> La integración de Braze y Movable Ink [Da Vinci](https://movableink.com/da-vinci) permite a las marcas entregar mensajes altamente personalizados aprovechando el motor de toma de decisiones sobre contenidos basado en IA de Da Vinci. Da Vinci selecciona el contenido más relevante para cada usuario y despliega fácilmente los mensajes a través de Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|------------|-------------|
| Movable Ink Da Vinci | Se necesita una cuenta de Movable Ink Da Vinci para beneficiarse de esta asociación. |
| Braze Currents - Eventos de interacción con mensajes | Se necesita una exportación personalizada de Braze Currents para enviar datos de eventos de interacción con mensajes a Movable Ink. |
| Clave de API REST de Braze | Se necesita una clave de API REST de Braze con los permisos `messages.send`, `sends.id.create` y `campaigns.details`. Se puede crear en el panel de Braze desde **Settings** > **API Keys**. <br><br>Tu equipo de cuentas de Movable Ink te proporcionará directamente más instrucciones de configuración. Consulta la sección [Integración](#integration).|
| Instancia de la aplicación Da Vinci en Braze | Crea una instancia de la aplicación Da Vinci dedicada en Braze. Se puede crear una nueva aplicación en el panel de Braze yendo a **Settings** > **App Settings** > **+ Add App**. Nombra la aplicación "**Movable Ink - Da Vinci**" y selecciona cualquier plataforma (es necesario seleccionar una plataforma, pero el tipo no afecta a la funcionalidad). Más información sobre [cómo añadir una nueva aplicación]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para empezar con la integración, ponte en contacto con tu equipo de cuentas de Movable Ink para obtener ayuda. Movable Ink te proporcionará las instrucciones de acceso y configuración correspondientes. Tendrás que proporcionar a Movable Ink un conjunto de credenciales de la API de Braze para permitir que Da Vinci envíe despliegues de correo electrónico a través de la API de mensajería de Braze.

Una vez conectado, Movable Ink:

- Trabajará con el cliente y Braze para configurar la cuenta Da Vinci de la marca de modo que se implemente correctamente con Braze.
- Capturará configuraciones específicas de la marca para alinearlas con tus casos de uso de mensajería.
- Realizará pruebas exhaustivas y controles de calidad para validar que los correos electrónicos se entregan según lo previsto y cumplen todas las normas de rendimiento y funcionamiento.