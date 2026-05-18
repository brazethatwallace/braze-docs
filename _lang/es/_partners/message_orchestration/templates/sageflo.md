---
nav_title: Sageflo
article_title: Sageflo Radiate
description: "Este artículo de referencia describe la asociación entre Braze y Sageflo, una herramienta de marketing distribuido que permite a los equipos enviar fácilmente sus propios correos electrónicos utilizando plantillas aprobadas por marketing, imágenes y segmentos de audiencia a través de integraciones de API con Braze."
alias: /partners/sageflo/
page_type: partner
search_tag: Partner

---

# Sageflo Radiate

> [Sageflo Radiate](https://sageflo.com/radiate) es una herramienta de marketing distribuido que permite a los equipos locales enviar fácilmente sus propios correos electrónicos utilizando plantillas aprobadas por marketing, imágenes y segmentos de audiencia a través de integraciones de API con Braze.

_Esta integración está mantenida por Sageflo._

## Sobre la integración {#about-the-integration}

Proporciona a los equipos locales las herramientas que necesitan para hacer un marketing más inteligente aprovechando las sofisticadas capacidades de Braze, que incluyen la segmentación de la audiencia, la gobernanza de la frecuencia y el contenido dinámico, todo ello incluyendo mecanismos de protección para tu marca.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Sageflo Radiate | Se necesita una cuenta Sageflo Radiate para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con todos los permisos de `templates` y `campaigns`. <br><br> Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión de API coincide con la URL del dashboard de tu instancia de Braze. <br><br> Por ejemplo, si la URL de tu dashboard es `https://dashboard-03.braze.com`, tu punto de conexión será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Radiate es ideal para franquicias y empresas de comercio minorista que desean ampliar sus esfuerzos de marketing permitiendo a los equipos distribuidos enviar correos electrónicos a sus audiencias locales a través de Braze.

* Permite que los equipos distribuidos envíen fácilmente correos electrónicos y SMS de marketing
* Crea conexiones con los clientes centradas en la comunidad
* Mantén la coherencia de la marca con mecanismos de protección integrados
* Quita la carga de tu equipo nacional de marketing

## Integración {#integration}

Tu equipo de cuentas de Sageflo se encargará de configurar tu integración. Se te pedirá que proporciones tus credenciales de API de Braze y Sageflo trabajará con tu equipo de marketing para configurar segmentos de audiencia para ubicaciones y sucursales específicas.

Una vez conectado, Sageflo:

* Configurará el entorno Radiate y la conexión con Braze
* Configurará segmentos de audiencia basados en la ubicación en Braze
* Definirá la configuración de Campaign, ubicación y grupo de usuarios
* Mapeará plantillas de Braze para usarlas con Campaigns de Radiate
* Programará y realizará la formación de los usuarios