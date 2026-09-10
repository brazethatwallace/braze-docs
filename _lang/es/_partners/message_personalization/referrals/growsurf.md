---
date_published: "2026-09-08"
nav_title: GrowSurf
article_title: GrowSurf
description: "Este artículo de referencia describe la integración entre Braze y GrowSurf, una plataforma de programas de referidos y afiliados que sincroniza los datos de los participantes con Braze para segmentación y personalización con Liquid."
alias: /partners/growsurf/
page_type: partner
search_tag: Partner
---

# GrowSurf

> [GrowSurf](https://www.growsurf.com/) envía datos de participantes de programas de referidos y afiliados a los perfiles de usuario de Braze. La integración añade enlaces de referidos, detalles de participantes, recuentos de referidos, recuentos de invitaciones, recuentos de impresiones y progreso de hitos como atributos personalizados que puedes usar para segmentación en Braze y personalización con Liquid.

_Esta integración está mantenida por GrowSurf._

## Acerca de la integración {#about-the-integration}

GrowSurf es un software de programas de referidos y afiliados. La integración unidireccional mantiene los datos de referidos de los participantes de GrowSurf disponibles en Braze para que puedas segmentar participantes, personalizar mensajes con enlaces de referidos y progreso, y enviar comunicaciones oportunas del programa desde Braze.

## Ejemplos {#use-cases}

- Añadir el enlace de referidos de cada participante a los mensajes de Braze.
- Crear segmentos a partir del estado de referidos, recuentos de referidos y progreso de hitos.
- Personalizar Campaigns y Canvas con atributos de participantes y referidores.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

| Requisito previo | Descripción |
| --- | --- |
| Una cuenta de GrowSurf | Se requiere un plan de pago de GrowSurf para esta integración. |
| Una clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. Crea esta clave en el panel de Braze desde **Configuración** > **API e identificadores** > **Claves de API**. Para más información, consulta [Crear claves de API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Un endpoint REST de Braze | La URL de tu endpoint REST de Braze (por ejemplo, `https://rest.iad-01.braze.com`). Para más información, consulta [Endpoints de la REST API]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Sigue estos pasos para conectar un programa de GrowSurf a Braze. Para instrucciones paso a paso, consulta la [documentación de integración de GrowSurf con Braze](https://docs.growsurf.com/integrations/braze).

### Paso 1: Crear una clave de API REST de Braze {#step-1-create-a-braze-rest-api-key}

1. En Braze, ve a **Configuración** > **API e identificadores** > **Claves de API**.
2. Crea una clave de API REST con permisos de `users.track`.
3. Copia la clave de API y anota el endpoint REST del mismo espacio de trabajo de Braze.

### Paso 2: Conectar Braze en GrowSurf {#step-2-connect-braze-in-growsurf}

1. En GrowSurf, ve a **Program Editor** > **4. Options** > **Integrations** > **Braze**.
2. Selecciona el endpoint REST de Braze correspondiente.
3. Introduce la clave de API REST y selecciona **Submit**.

### Paso 3: Verificar la primera sincronización de participantes {#step-3-verify-the-first-participant-sync}

1. Añade o actualiza un participante de prueba en GrowSurf.
2. En Braze, ve a **Audiencia** > **Búsqueda de usuarios** y busca por correo electrónico para abrir el perfil de usuario correspondiente.
3. Confirma que los atributos personalizados `grsf_` aparecen en el perfil.

## Atributos de GrowSurf en Braze {#growsurf-attributes-in-braze}

GrowSurf pone a disposición 15 atributos de referidos en Braze. La primera sincronización envía el conjunto completo. Después, GrowSurf envía actualizaciones cuando los datos de los participantes cambian. Si un valor se elimina en GrowSurf, el atributo correspondiente en Braze también se borra. Los valores de recuento se envían como números.

### Atributos de cadena {#string-attributes}

| Atributo personalizado | Descripción |
| --- | --- |
| `grsf_share_url` | La URL de referidos compartida del participante. |
| `grsf_participant_id` | El ID del participante en GrowSurf. |
| `grsf_referral_status` | El estado de referidos del participante. |
| `grsf_participant_first_name` | El nombre del participante. |
| `grsf_participant_last_name` | El apellido del participante. |
| `grsf_referrer_first_name` | El nombre del referidor. |
| `grsf_referrer_last_name` | El apellido del referidor. |
| `grsf_referrer_email` | La dirección de correo electrónico del referidor. |
| `grsf_next_milestone` | El siguiente hito hacia el que avanza el participante. |
| `grsf_next_monthly_milestone` | El siguiente hito mensual hacia el que avanza el participante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos de cadena" }

### Atributos numéricos {#number-attributes}

| Atributo personalizado | Descripción |
| --- | --- |
| `grsf_total_referral_count` | El recuento total de referidos del participante. |
| `grsf_monthly_referral_count` | El recuento de referidos del participante en el mes actual. |
| `grsf_prev_monthly_referral_count` | El recuento de referidos del participante en el mes anterior. |
| `grsf_total_invite_count` | El recuento total de invitaciones del participante. |
| `grsf_total_impression_count` | El recuento total de impresiones del enlace de referidos del participante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos numéricos" }

## Usar GrowSurf con Braze {#use-growsurf-with-braze}

Usa los atributos de referidos de GrowSurf para segmentación en Braze y personalización con Liquid. GrowSurf actualiza estos atributos cuando se añade un participante o cuando cambian sus datos de referidos. También puedes sincronizar participantes que ya estaban en tu programa.

### Paso 1: Crear segmentos {#step-1-build-segments}

1. En Braze, crea un segmento con los atributos personalizados `grsf_` pertinentes.
2. Incluye o excluye participantes por estado de referidos, recuentos de referidos o progreso de hitos.

### Paso 2: Personalizar mensajes {#step-2-personalize-messages}

1. Añade el atributo personalizado `grsf_share_url` a un mensaje de Braze con Liquid: {% raw %}`{{custom_attribute.${grsf_share_url}}}`{% endraw %}.

{: start="2"}
2. Usa otros atributos `grsf_` para personalizar el estado de referidos, los recuentos y el progreso de hitos.

## Consideraciones {#considerations}

- GrowSurf envía solo atributos personalizados. No envía eventos personalizados, compras ni cambios de suscripción.
- GrowSurf identifica los perfiles de Braze por el correo electrónico del participante. Si no existe un perfil coincidente, Braze crea un perfil solo con correo electrónico.
- Si el mismo correo electrónico pertenece a participantes en más de un programa de GrowSurf conectado, los datos del programa sincronizado más recientemente aparecen en ese perfil de Braze.
- Conecta Braze antes de importar participantes. Para sincronizar participantes existentes, usa la opción de sincronización de participantes existentes de GrowSurf.

## Solución de problemas {#troubleshooting}

- Confirma que la clave de API REST de Braze tiene permisos de `users.track` y que el endpoint REST seleccionado pertenece al mismo espacio de trabajo de Braze.
- Si un participante no se sincroniza, verifica que el participante tenga una dirección de correo electrónico válida.
- Consulta los registros de actividad del participante en GrowSurf para ver el resultado de la sincronización.
- GrowSurf reintenta automáticamente los errores temporales de Braze. Si GrowSurf no puede confirmar una actualización, envía todos los atributos de referidos la próxima vez que se sincronice ese perfil de Braze. Si la clave de API o el endpoint REST no son válidos, corrige la configuración y vuelve a conectar la integración.

Para más detalles de solución de problemas, consulta la [documentación de integración de GrowSurf con Braze](https://docs.growsurf.com/integrations/braze#troubleshooting).