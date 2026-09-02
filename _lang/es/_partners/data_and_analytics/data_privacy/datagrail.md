---
nav_title: DataGrail
article_title: DataGrail
description: "Este artículo de referencia describe la asociación entre Braze y DataGrail, una plataforma de gestión de la privacidad, que permite detectar los datos de los consumidores recopilados y almacenados en Braze para procesar rápidamente las DSR."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), una plataforma de gestión de la privacidad, ayuda a fomentar la confianza de los consumidores y a eliminar los negocios de riesgo. Con la detección continua del sistema y el cumplimiento automatizado de las solicitudes de los interesados (DSR), DataGrail potencia los programas de privacidad, apoyando el cumplimiento de las leyes y normativas de privacidad en evolución, como el RGPD, la CCPA y la CPRA.

_Esta integración está mantenida por DataGrail._

## Sobre la integración {#about-the-integration}

La integración de Braze y DataGrail permite detectar los datos de los consumidores recopilados y almacenados en Braze para procesar rápidamente las DSR (solicitudes de acceso, eliminación y no venta). Braze se sumará a un plano preciso de dónde residen los datos de los consumidores en tu organización con el mapeado de datos automatizado; ya no se necesitan cuestionarios ni hojas de cálculo para mantener un marco de privacidad o producir un registro de actividades de procesamiento (RoPA).

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Cuenta DataGrail | Se necesita una cuenta DataGrail para aprovechar esta asociación.<br>Ponte en contacto con tu administrador o envía un correo electrónico a support@datagrail.io si tienes algún problema o pregunta sobre la integración. |
| Clave de API de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `events.list`, `users.export.ids`, `users.delete` y `users.track`.<br><br>Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**. |
| Instancia de Braze | Tu instancia de Braze se puede obtener a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Inicia sesión en el portal de DataGrail y selecciona **Connect** en la página de integración de Braze. A continuación, introduce tu instancia y tu clave de API de Braze y selecciona **Connect Braze**.

Si hay cuentas de Braze adicionales que integrar:
1. Selecciona **Edit Connection** en la página de integración de Braze.
2. En el desplegable, selecciona **+Add New Connection**.
3. En **Connection Name**, introduce un nuevo nombre para identificar esta cuenta independiente (por ejemplo, Cuenta de formación Braze).
4. Introduce una instancia de Braze y una clave de API independientes para esta nueva cuenta.
5. Selecciona **Connect**.

Envía un correo electrónico a DataGrail a support@datagrail.io si tienes algún problema o pregunta sobre tu integración.