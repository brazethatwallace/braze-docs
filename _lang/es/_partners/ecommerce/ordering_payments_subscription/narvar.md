---
nav_title: Narvar
article_title: Narvar
description: "Aprende a integrar Narvar con Braze."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar es una plataforma post-compra que mejora la fidelización de los clientes mediante el seguimiento de los pedidos, las actualizaciones de las entregas y la gestión de las devoluciones. La integración de Braze y Narvar permite a las marcas aprovechar los eventos de notificación de Narvar para desencadenar mensajes directamente desde Braze, manteniendo a los clientes informados con actualizaciones puntuales.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Cuenta Narvar | Se requiere una cuenta Narvar para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permiso de `messages.send`. Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende de la URL de tu instancia de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Características compatibles {#supported-features}

| Tipo | Características compatibles |
|-------|----------|
| Notificaciones | - Anticipación de la entrega<br>- Retraso del operador<br>- Entrega estándar |
| Canales | Notificaciones push |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Características compatibles" }

{% alert note %}
Si te interesan otros tipos o canales de notificación, ponte en contacto con tu CSM de Braze y Narvar.
{% endalert %}

## Detalles de la integración {#integration-details}

Para cada evento de notificación, Narvar inicia una solicitud al punto de conexión [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging/) de Braze para entregar un mensaje push a cada consumidor con adhesión voluntaria.

Narvar es responsable de configurar las cargas útiles de notificación push para cada mensaje. Actualmente, Narvar no tiene una interfaz de diseño integrada para notificaciones push, por lo que su equipo colaborará con el tuyo para determinar y definir los requisitos de la carga útil. Estas cargas útiles pueden personalizarse en la misma medida que las que se envían a través de tu propio sistema, incluida la compatibilidad con marcadores de posición de contenido variable, como datos de pedidos y detalles de consumidores.

## Introducción a la integración Braze-Narvar {#getting-started-with-the-braze-narvar-integration}

1. **Ponte en contacto con tu CSM de Narvar** para expresar tu interés en la integración.
2. **Designa entornos de Braze** para staging y producción.
3. **Genera la clave de API** en Braze para uso de Narvar.
4. **Genera claves de Campaign** en Braze según sea necesario.
5. **Proporciona las claves de API y de Campaign** a Narvar a través de un enlace seguro de un solo uso.
6. **Comparte los detalles de la carga útil de la notificación push** para finalizar la configuración.