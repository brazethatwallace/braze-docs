---
nav_title: Cuentas
article_title: Objetos de cuenta
page_order: 7
page_type: reference
description: "Usa objetos de cuenta para segmentar usuarios, personalizar mensajes con datos de cuenta y gestionar registros de cuenta."
---

# Objetos de cuenta {#account-objects}

> Usa objetos de cuenta para segmentar y personalizar la mensajería con datos de cuenta.

{% alert important %}
Cuentas se encuentra en acceso anticipado. Estas instrucciones pueden cambiar a medida que la característica evolucione.
{% endalert %}

Con los objetos de cuenta, puedes:

- Crear segmentos con criterios de cuenta
- Personalizar mensajes con atributos de cuenta a través de Liquid
- Gestionar registros de cuenta en un solo lugar

Los objetos de cuenta son modelos de datos a nivel de espacio de trabajo conectados a perfiles de usuario. Un registro de cuenta es una cuenta específica y sus datos de campo asociados.
Usa objetos de cuenta cuando el contexto de la cuenta, como los atributos de la empresa, te ayude a segmentar y personalizar la mensajería.
También puedes modelar jerarquías de cuentas (como cuentas principales y secundarias) y vincular un perfil de usuario a múltiples cuentas.

## ¿Por qué usar objetos de cuenta? {#why-use-account-objects}

Algunos casos de uso requieren contexto a nivel de cuenta, incluso cuando tus Campaigns y Canvas se envían a usuarios individuales.

Los objetos de cuenta te permiten almacenar datos de cuenta una vez y reutilizarlos para segmentación y personalización en Braze.

Esto te permite:

- Segmentar por atributos de cuenta
- Personalizar mensajes con contexto de cuenta compartido (como nombre de empresa o industria)
- Modelar relaciones entre cuentas y conectar un perfil de usuario a múltiples cuentas

Este enfoque reemplaza la duplicación de los mismos atributos de cuenta en muchos perfiles de usuario.

## Requisitos previos {#prerequisites}

Antes de comenzar:

- Tu espacio de trabajo debe estar habilitado para el acceso anticipado de Cuentas. Contacta a tu equipo de cuenta de Braze.
- Ya debes tener usuarios en Braze.
- Después de que Cuentas esté habilitado, aparece en **Configuración de datos** > **Cuentas**. Si es la primera vez que usas Cuentas, sigue las instrucciones de inicialización en pantalla.

## Modelo de datos de cuenta {#account-data-model}

Cada cuenta requiere un ID externo (`id`) y un nombre (`name`).

Los campos de cuenta en esta sección definen el esquema del objeto de cuenta. Esos campos se aplican a cada registro de cuenta individual que almacenas en Braze.

Braze incluye objetos de cuenta con campos estándar de forma predeterminada. Puedes agregar y eliminar campos personalizados según tu caso de uso.

| Nombre del campo | Tipo de campo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `id` | cadena | Sí | El ID de tu sistema para la cuenta (por ejemplo, ID de CRM). Debe ser único en tu espacio de trabajo. |
| `name` | cadena | Sí | Nombre de la cuenta. |
| `type` | cadena | No | Tipo de cuenta, como cliente, partner o revendedor. |
| `annual_revenue` | número | No | Ingresos anuales de la cuenta. |
| `industry` | cadena | No | Industria de la cuenta. |
| `number_of_employees` | número | No | Cantidad de empleados/as. |
| `address` | cadena | No | Dirección. |
| `city` | cadena | No | Ciudad. |
| `state` | cadena | No | Estado o provincia. |
| `postal_code` | cadena | No | Código postal. |
| `country` | cadena | No | País. |
| `notes` | cadena | No | Notas adicionales. |
| `website` | cadena | No | URL del sitio web. |
| `main_phone` | cadena | No | Número de teléfono principal. |
| `created_date` | hora | No | Marca de tiempo de creación de la cuenta. |
| `sic_code` | cadena | No | Código de clasificación industrial estándar. |
| Campos personalizados | personalizado | No | Campos que defines y gestionas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campos del modelo de datos de cuenta" }

## Opciones de integración de datos {#data-integration-options}

Puedes gestionar registros de cuenta a través de:

- Endpoints de REST API para registros de cuenta
- Edición en el navegador en **Configuración de datos** > **Cuentas** para registros individuales

## Primeros pasos {#get-started}

### Paso 1: Habilitar Cuentas {#step-1-enable-accounts}

Cuentas se habilita a nivel de empresa. Durante el acceso anticipado, tu equipo de cuenta de Braze se encarga de la habilitación única.

Cuando Cuentas esté habilitado, ve a **Configuración de datos** > **Cuentas** y completa el flujo de inicialización única si se te solicita.

### Paso 2: Agregar registros de cuenta {#step-2-add-account-records}

Agrega o actualiza registros de cuenta a través de la REST API o la edición en el navegador.

### Paso 3: Crear un filtro calculado para criterios de cuenta {#step-3-create-a-calculated-filter-for-account-criteria}

Antes de segmentar con datos de cuenta, crea un filtro calculado que defina tus criterios de cuenta. Para más detalles, consulta [Cómo funcionan los filtros calculados]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#how-it-works).

### Paso 4: Usar el filtro calculado en el generador de segmentos {#step-4-use-the-calculated-filter-in-segment-builder}

En el generador de segmentos, selecciona el filtro calculado que creaste y luego agrega cualquier filtro de atributo de usuario adicional que respalde la segmentación de tu Campaign o Canvas.

## Crear segmentos basados en cuentas {#build-account-based-segments}

Después de que tus registros de cuenta y filtro calculado estén listos:

1. Ve al [generador de segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Agrega tu filtro calculado preconfigurado para criterios de cuenta.
3. Agrega cualquier filtro de atributo de usuario adicional.
4. Guarda tu segmento.

Por ejemplo:

- **Filtro calculado:** la `industry` de la cuenta es exactamente `healthcare`
- **Filtro de atributo de usuario:** `days_since_last_login` es menor que `30`

## Personalizar con Liquid {#personalize-with-liquid}

Usa la etiqueta de Liquid `{% raw %}{% data_object account %}{% endraw %}` para cargar datos de cuenta del usuario en el array `data_objects`.

{% alert note %}
Al usar **Vista previa y prueba**, usa un segmento que incluya datos de cuenta para que la personalización pueda resolverse correctamente.
{% endalert %}

{% raw %}
```liquid
{% data_object account %}
Hi {{${first_name}}},
We'd love to invite you and your peers at {{ data_objects[0].name }}.
```
{% endraw %}

Para iterar sobre todas las cuentas coincidentes:

{% raw %}
```liquid
{% data_object account %}
{% for acct in data_objects %}
- {{ acct.name }}
{% endfor %}
```
{% endraw %}

## Conceptos básicos de la API {#api-basics}

Puedes usar la REST API para gestionar registros de cuenta durante el acceso anticipado.

{% alert note %}
Los detalles de los endpoints para Cuentas se proporcionan durante la incorporación del acceso anticipado. Si necesitas acceso o detalles de incorporación, contacta a tu equipo de cuenta de Braze.
{% endalert %}

Para autenticación y conceptos básicos de endpoints REST, consulta [Resumen de la API de Braze]({{site.baseurl}}/api/basics).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo agregar campos personalizados a las cuentas? {#can-i-add-custom-fields-to-accounts}

Sí. Puedes definir y gestionar campos de cuenta personalizados en tu espacio de trabajo. Para los requisitos de los campos, consulta [Modelo de datos de cuenta](#account-data-model).

### ¿Cuentas es un complemento de pago? {#is-accounts-a-paid-add-on}

No. Cuentas no es un complemento de pago y está disponible en todos los planes. Durante el acceso anticipado, tu equipo de cuenta de Braze debe habilitarlo para tu espacio de trabajo.