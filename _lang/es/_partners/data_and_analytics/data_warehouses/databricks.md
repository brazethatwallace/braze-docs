---
nav_title: Databricks
article_title: Databricks
description: "Este artículo describe Databricks Delta Sharing con Braze (beta cerrada), que te permite acceder a los datos de interacción y Campaign de Braze en tu cuenta de Databricks."
page_type: partner
search_tag: Partner
permalink: /databricks/
hidden: true
---

# Databricks

> [Databricks](https://www.databricks.com/) es una plataforma de análisis abierta y unificada para crear, implementar, compartir y mantener soluciones empresariales de datos, análisis e IA a escala. La plataforma de inteligencia de datos de Databricks se integra con el almacenamiento en la nube y la seguridad de tu cuenta en la nube, y administra e implementa la infraestructura en la nube por ti.

{% alert important %}
Databricks Delta Sharing con Braze está en **beta cerrada**. La disponibilidad, las regiones compatibles y el comportamiento del producto pueden cambiar. Ponte en contacto con tu administrador del éxito del cliente de Braze para participar o confirmar si esta característica está habilitada para tu espacio de trabajo.
{% endalert %}

## Delta Sharing (de Braze a Databricks) {#delta-sharing-braze-to-databricks}

Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) te permite compartir datos de forma segura con unidades de negocio y filiales en distintas nubes o regiones sin copiar ni replicar los datos.

**Usa Delta Sharing cuando quieras:**
- Consultar datos de eventos y Campaign de Braze usando Databricks SQL
- Crear informes complejos y realizar modelos de atribución
- Combinar datos de Braze con otros datos en tu cuenta de Databricks
- Comparar tus datos de interacción entre canales, industrias y plataformas de dispositivos

Para obtener instrucciones de configuración, consulta [Databricks Delta Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/).

Para obtener más información sobre Delta Sharing en Databricks, consulta [¿Qué es Delta Sharing?](https://www.databricks.com/product/delta-sharing).

## Requisitos previos {#prerequisites}

Antes de poder usar esta característica, completa lo siguiente:

| Requisito | Descripción |
| ----------- | ----------- |
| Acceso a Braze | Para acceder a esta característica en Braze, ponte en contacto con tu administrador de cuenta o del éxito del cliente de Braze. |
| Cuenta de Databricks | Una cuenta de Databricks con permisos de `admin`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

Cuando estés listo para configurar el uso compartido y consultar los datos compartidos, continúa con [Databricks Delta Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/).