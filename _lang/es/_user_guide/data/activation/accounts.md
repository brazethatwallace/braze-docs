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
- Personalizar mensajes con contexto de cuenta compartido (como el nombre de la empresa o la industria)
- Modelar relaciones entre cuentas y conectar un perfil de usuario a varias cuentas

Este enfoque reemplaza la duplicación de los mismos atributos de cuenta en muchos perfiles de usuario.

## Requisitos previos {#prerequisites}

Antes de comenzar:

- Tu espacio de trabajo debe estar habilitado para el acceso anticipado de Accounts. Ponte en contacto con tu equipo de cuenta de Braze.
- Ya debes tener usuarios en Braze.
- Una vez habilitado Accounts, aparecerá en **Configuración de datos** > **Accounts**. Si es la primera vez que usas Accounts, sigue las instrucciones de inicialización en pantalla.

## Modelo de datos de cuenta {#account-data-model}

Cada cuenta requiere un ID externo (`id`) y un nombre (`name`).

Los campos de cuenta en esta sección definen el esquema del objeto Cuenta. Estos campos se aplican a cada registro de cuenta individual que almacenas en Braze.

Braze incluye objetos de cuenta con campos estándar de forma predeterminada. Puedes añadir y eliminar campos personalizados según tu caso de uso.

| Nombre del campo | Tipo de campo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `id` | cadena | Sí | El ID de tu sistema para la cuenta (por ejemplo, ID de CRM). Debe ser único en tu espacio de trabajo. |
| `name` | cadena | Sí | Nombre de la cuenta. |
| `type` | cadena | No | Tipo de cuenta, como cliente, partner o revendedor. |
| `annual_revenue` | número | No | Ingresos anuales de la cuenta. |
| `industry` | cadena | No | Industria de la cuenta. |
| `number_of_employees` | número | No | Número de empleados/as. |
| `address` | cadena | No | Dirección postal. |
| `city` | cadena | No | Ciudad. |
| `state` | cadena | No | Estado o provincia. |
| `postal_code` | cadena | No | Código postal. |
| `country` | cadena | No | País. |
| `notes` | cadena | No | Notas adicionales. |
| `website` | cadena | No | URL del sitio web. |
| `main_phone` | cadena | No | Número de teléfono principal. |
| `created_date` | hora | No | Marca de tiempo de creación de la cuenta. |
| `sic_code` | cadena | No | Código de Clasificación Industrial Estándar. |
| Campos personalizados | personalizado | No | Campos que tú defines y gestionas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campos del modelo de datos de cuenta" }

## Opciones de integración de datos {#data-integration-options}

Puedes gestionar los registros de cuenta a través de:

- Endpoints de REST API para registros de cuenta
- Edición en el navegador en **Data Settings** > **Accounts** para registros individuales

## Primeros pasos {#get-started}

### Paso 1: Habilitar Accounts {#step-1-enable-accounts}

Accounts se habilita a nivel de empresa. Durante el acceso anticipado, tu equipo de cuenta de Braze se encarga de la habilitación única.

Cuando Accounts esté habilitado, ve a **Configuración de datos** > **Accounts** y completa el flujo de inicialización único si se te solicita.

### Paso 2: Añadir registros de cuenta {#step-2-add-account-records}

Añade o actualiza registros de cuenta a través de la REST API o mediante la edición en el navegador.

### Paso 3: Crear un filtro calculado para criterios de cuenta {#step-3-create-a-calculated-filter-for-account-criteria}

Antes de segmentar según los datos de cuenta, crea un filtro calculado que defina tus criterios de cuenta:

1. Ve a **Audiencia** > **Filtros calculados**.
2. Selecciona **Crear filtro** y, a continuación, selecciona **Filtros de objetos de datos**.
3. Define tus criterios de cuenta.

Para más detalles, consulta [Filtros calculados]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#create-a-calculated-filter).

### Paso 4: Usar el filtro calculado en el generador de Segments {#step-4-use-the-calculated-filter-in-segment-builder}

En el generador de Segments, selecciona el filtro calculado que creaste y añade cualquier filtro de atributo de usuario adicional que respalde la segmentación de tu Campaign o Canvas.

## Crea segmentos basados en cuentas {#build-account-based-segments}

Cuando tus registros de cuenta y tu filtro calculado estén listos:

1. Ve al [constructor de Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Añade tu filtro calculado preconfigurado para los criterios de cuenta.
3. Añade cualquier filtro de atributo de usuario adicional.
4. Guarda tu Segment.

Por ejemplo:

- **Filtro calculado:** la cuenta `industry` es exactamente `healthcare`
- **Filtro de atributo de usuario:** `days_since_last_login` es menor que `30`

## Personalizar con Liquid {#personalize-with-liquid}

Usa la etiqueta de Liquid `{% raw %}{% data_object account %}{% endraw %}` para cargar los datos de cuenta del usuario en el array `data_objects`.

{% alert note %}
Cuando uses **Vista previa y prueba**, utiliza un Segment que incluya datos de cuenta para que la personalización se resuelva correctamente.
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

## Aspectos básicos de la API {#api-basics}

Puedes utilizar la REST API para gestionar registros de cuentas durante el acceso anticipado.

Para obtener detalles sobre los endpoints, consulta [Endpoints de objetos personalizados]({{site.baseurl}}/api/endpoints/custom_objects).

Para información sobre autenticación y aspectos básicos de los endpoints REST, consulta [Resumen de la API de Braze]({{site.baseurl}}/api/basics).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo agregar campos personalizados a las cuentas? {#can-i-add-custom-fields-to-accounts}

Sí. Puedes definir y gestionar campos de cuenta personalizados en tu espacio de trabajo. Para conocer los requisitos de los campos, consulta [Modelo de datos de cuenta](#account-data-model).

### ¿Accounts es un complemento de pago? {#is-accounts-a-paid-add-on}

No. Accounts no es un complemento de pago y está disponible en todos los planes. Durante el acceso anticipado, tu equipo de cuenta de Braze debe habilitarlo para tu espacio de trabajo.