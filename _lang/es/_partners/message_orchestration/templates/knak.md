---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Este artículo de referencia describe la asociación entre Braze y Knak, una plataforma de creación de campañas que permite crear correos electrónicos totalmente receptivos en cuestión de minutos u horas en lugar de días o semanas, y exportarlos como plantillas de Braze listas para usar."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) es la primera plataforma de creación de campañas diseñada para que los equipos de marketing empresarial la utilicen internamente. Su plataforma de arrastrar y soltar permite a cualquier persona crear correos electrónicos y páginas de inicio atractivos y alineados con la marca en cuestión de minutos, sin necesidad de código ni de ayuda externa.

_Esta integración está mantenida por Knak._

## Sobre la integración {#about-the-integration}

La integración de Braze y Knak te permite crear correos electrónicos totalmente receptivos en cuestión de minutos u horas, en lugar de días o semanas, y exportarlos como plantillas de Braze listas para usar. Knak está pensado para especialistas en marketing que desean mejorar la creación de correos electrónicos para campañas gestionadas en Braze, sin necesidad de agencias externas ni de codificación manual.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Knak | Se necesita una cuenta Knak para aprovechar esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos completos de **Plantillas**. <br><br>Se puede crear en el dashboard de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Knak está pensado para especialistas en marketing que desean mejorar la creación de sus correos electrónicos, sin necesidad de codificación ni ayuda externa. Es ideal para quienes:
- Actualmente utilizan plantillas sencillas para los correos electrónicos y quieren mejorar sus resultados
- Dependen de agencias o desarrolladores externos para crear correos electrónicos para Braze
- Quieren recuperar el control creativo sobre la creación de activos y llegar al mercado mucho más rápido

## Integración {#integration}

### Paso 1: Configura tu integración {#step-1-configure-your-integration}

En Knak, ve a **Integrations > Platforms > + Add New Integration**.

![Botón para añadir integración]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

A continuación, selecciona la plataforma **Braze** y proporciona la clave de API de Braze y el punto de conexión REST. Haz clic en **Create New Integration** para completar tu integración.

![Crear una nueva integración]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### Paso 2: Sincroniza tus plantillas de Knak {#step-2-sync-your-knak-templates}

En Knak, localiza un correo electrónico que quieras sincronizar con Braze y selecciona **Publish** y luego **Sync**.

![Integración de Knak 1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

A continuación, verifica el nombre del correo electrónico y haz clic en **Sync**.

![Integración de Knak 2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## Uso de la integración {#using-the-integration}

Puedes encontrar los correos electrónicos de Knak que has cargado en Braze en **Engagement > Plantillas y medios**. Serán atractivos, alineados con la marca y totalmente receptivos. ¡El único límite es tu propia creatividad!