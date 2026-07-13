---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Este artículo de referencia describe la asociación entre Braze y Sheetlabs, un servicio que te permite personalizar tus campañas de marketing con datos procedentes de hojas de cálculo."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/) es una plataforma que te permite convertir hojas de cálculo en API potentes y bien documentadas. Puedes importar datos de Google Sheets o Excel, convertirlos en una API y luego utilizar esa API en otras aplicaciones, como Braze.
_Esta integración está mantenida por Sheetlabs._

## Sobre la integración {#about-the-integration}

La integración de Sheetlabs y Braze te permite utilizar [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) para incluir las API de Sheetlabs en tus campañas de marketing de Braze. Se suele utilizar para establecer un puente entre una hoja de cálculo de Google (que el equipo de marketing actualiza directamente) y las plantillas de Braze. Esto te permite conseguir más con las plantillas de Braze, como traducciones o conjuntos más amplios de atributos personalizados.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Sheetlabs | Para beneficiarte de esta asociación es necesario disponer de una [cuenta de Sheetlabs](https://sheetlabs.com/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

La integración de Braze y Sheetlabs te permite lograr los siguientes casos de uso:

1. **Separar el acceso del especialista en marketing del acceso a las campañas de Braze**: Algunos equipos desean evitar dar a todo el personal acceso para configurar directamente las plantillas y el contenido de Braze. En su lugar, quieren que el personal actualice el contenido de marketing en una hoja de cálculo. Sheetlabs sirve de puente entre las hojas de cálculo y Braze y puede actualizarse en tiempo real.
2. **Traducciones**: Las plantillas de Braze no admiten traducciones de forma nativa. Si deseas admitir varios idiomas, debes crear varias plantillas. Al utilizar Sheetlabs junto con Braze, puedes tener una única plantilla de Braze traducida a varios idiomas.
3. **Ampliación de los atributos personalizados**: Braze proporciona un cierto número de atributos personalizados que pueden configurarse. Al utilizar Sheetlabs junto con Braze, puedes añadir atributos personalizados adicionales más allá de esta asignación inicial.

Consulta [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) para obtener más información sobre estos casos de uso.

## Integración {#integration}

### Paso 1: Importa tu hoja de cálculo a Sheetlabs {#step-1-import-your-spreadsheet-into-sheetlabs}

En Sheetlabs, carga una hoja de cálculo de Excel o vincula tu cuenta de Google e importa una hoja de Google.

- Para importar una hoja de cálculo de Excel, haz clic en **Data Tables** en la barra de menús y, a continuación, en **Import from CSV/Excel**.
- Para importar desde Google Sheets, haz clic en **Data Tables** en la barra de menús y, a continuación, en **Import from Google**. A continuación, tendrás que proporcionar tus credenciales de inicio de sesión de Google e importar la hoja.

También puedes optar por mantener tu hoja de Google sincronizada, lo que significa que Sheetlabs obtendrá automáticamente los datos más recientes de tu hoja de Google cuando cambien.

Asegúrate de incluir el ID de usuario de Braze en tu hoja de cálculo o cualquier otro dato que puedas utilizar como búsqueda más adelante.

### Paso 2: Crea una API en Sheetlabs {#step-2-create-an-api-in-sheetlabs}

A continuación, en Sheetlabs, ve a **APIs > Create API** y dale un nombre a tu API. Es probable que desees permitir consultas a través de un campo de búsqueda de tu hoja de cálculo, como el ID de usuario de Braze.

En este punto, deberías poder acceder a tu API con un enlace como:<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Paso 3: Utiliza la API en Contenido conectado de Braze {#step-3-use-the-api-in-braze-connected-content}

Ahora que tu API es accesible, puedes utilizarla en tus llamadas a Contenido conectado. Aquí tienes un ejemplo de cómo podría verse una plantilla de traducciones:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Para más ejemplos y consejos sobre la integración con Sheetlabs, consulta la [documentación de Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}