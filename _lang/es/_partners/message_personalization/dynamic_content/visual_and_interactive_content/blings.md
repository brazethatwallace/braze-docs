---
nav_title: Blings
article_title: Blings
description: "Este artículo de referencia describe la integración entre Braze y Blings."
alias: /partners/blings/
page_type: partner
search_tag: Partner
---

# Blings

> [Blings](https://www.blings.io/) es una plataforma de video personalizado de nueva generación que te permite entregar experiencias de video en tiempo real, interactivas y basadas en datos a través de canales a escala.

_Esta integración está mantenida por Blings._

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|-----------------|-----------------------------------------------------------------------------|
| Cuenta de Blings | Se necesita una cuenta de Blings para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

### Paso 1: Obtén tu fragmento de código HTML de Blings {#step-1-obtain-your-blings-html-snippet}

{% tabs %}
{% tab Blings business and free plans %}

#### Planes Blings business y gratuito {#blings-business-and-free-plans}

Localiza y copia tu fragmento de código HTML directamente en la aplicación de Blings.

1. Ve a la pestaña **Connect** del proyecto MP5 seleccionado.
2. Añade etiquetas de Braze Liquid a las variables correspondientes en la página **Connect** de Blings. Las etiquetas rellenarán dinámicamente los valores en el fragmento de código HTML.

![Fragmento de código HTML de Blings.]({% image_buster /assets/img/blings/blings_connect_audience.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Blings Enterprise plan %}

#### Plan Blings Enterprise {#blings-enterprise-plan}

Solicita el fragmento de código HTML a tu representante de Blings.

{% endtab %}
{% endtabs %}

### Paso 2: Crea una Campaign en Braze {#step-2-create-a-braze-campaign}

En Braze, crea una nueva Campaign de correo electrónico o de mensaje dentro de la aplicación e inserta el fragmento de código HTML de Blings.

![Campaign de Blings en Braze.]({% image_buster /assets/img/blings/blings_braze_campaign.png %})

### Paso 3: Prueba y lanzamiento {#step-3-test-and-launch}

Realiza una vista previa de la Campaign en Braze para confirmar que los campos personalizados se rellenan correctamente. Después, despliega tu Campaign MP5 a escala.

![Vista previa de Blings en Braze.]({% image_buster /assets/img/blings/blings_braze_preview.png %}){: style="max-width:70%;"}

## Obtener soporte {#getting-support}

Para cualquier pregunta o para solicitar tu fragmento de código, ponte en contacto con Blings en [support@blings.io](mailto:support@blings.io) o consulta el [centro de ayuda de Blings](https://blings.gitbook.io/blings-knowledge-base/documentation).