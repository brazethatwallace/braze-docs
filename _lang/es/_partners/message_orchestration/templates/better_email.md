---
nav_title: Better Email
article_title: Better Email
alias: /partners/better_email/
description: "Este artículo de referencia describe la asociación entre Braze y Better Email, una plataforma colaborativa de creación de correo electrónico construida en torno a un sistema de diseño de correo electrónico que te permite exportar plantillas listas para producción a Braze."
page_type: partner
search_tag: Partner
---

# Better Email

> [Better Email](https://www.betteremail.dev) es una plataforma colaborativa de creación de correo electrónico construida en torno a un sistema de diseño de correo electrónico. Los equipos pueden diseñar, administrar y exportar correos electrónicos listos para producción desde un sistema compartido de bloques y estilos, garantizando la consistencia de marca a escala sin depender de desarrolladores o agencias.

_Esta integración es mantenida por Better Email._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Better Email te permite crear y administrar plantillas de correo electrónico en el editor colaborativo de Better Email y exportarlas directamente a Braze como plantillas de correo electrónico listas para usar.

Reexportar un correo electrónico actualiza la plantilla existente de Braze en lugar de crear un duplicado, de modo que tu biblioteca de plantillas se mantiene limpia.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Better Email | Una cuenta de Better Email con acceso de administrador para crear integraciones |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos completos de **Templates**.<br><br>Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Usa el host REST, no la URL del dashboard; por ejemplo, `rest.fra-01.braze.eu`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

Better Email está diseñado para equipos de marketing que desean administrar correos electrónicos a través de un sistema de diseño y exportarlos a Braze sin trabajo manual de HTML. Es ideal para quienes:

- Mantienen una gran biblioteca de plantillas de correo electrónico y necesitan consistencia en todas ellas
- Quieren aplicar directrices de marca a través de un sistema de diseño de correo electrónico compartido
- Colaboran entre equipos (diseñadores, especialistas en marketing y desarrolladores) en la producción de correos electrónicos
- Usan Braze para la ejecución de campañas y quieren eliminar el cuello de botella en la transferencia entre diseño y despliegue

## Integrar Better Email con Braze {#integrate-better-email-with-braze}

### Paso 1: Encuentra tus valores de Braze {#step-1-find-your-braze-values}

En tu dashboard de Braze, recopila lo siguiente:

- **Instance URL**: usa el host REST, no la URL del dashboard (por ejemplo, `rest.fra-01.braze.eu`).
- **API key**: una clave de API REST con permisos completos de **Templates**, creada en **Settings** > **API Keys**.

### Paso 2: Configura la integración en Better Email {#step-2-set-up-the-integration-in-better-email}

1. Ve a **Integrations**.
2. Crea una nueva integración.
3. Introduce un nombre para la integración (por ejemplo, `Braze`).
4. Selecciona **Braze** como tipo.
5. Opcionalmente, restringe la integración a usuarios o grupos específicos en **Access**.
6. Selecciona **Save**.
7. Introduce la **Instance URL** y la **API Key**.
8. Habilita la integración.
9. Selecciona **Save** de nuevo.

### Paso 3: Exporta a Braze {#step-3-export-to-braze}

Cuando la integración esté activa, abre cualquier correo electrónico en Better Email y selecciona **Export** > **Braze**.

Better Email crea o actualiza la plantilla de correo electrónico correspondiente en Braze. Después de la primera exportación, Better Email almacena el ID de la plantilla de Braze; reexportar el mismo correo electrónico actualiza esa plantilla en lugar de crear un duplicado.

### Opcional: Sincronizar campos de destinatario desde Braze {#optional-sync-recipient-fields-from-braze}

Better Email puede sincronizar atributos personalizados de Braze para usarlos como etiquetas de combinación y campos de segmentación.

1. Abre la integración de Braze en Better Email.
2. Habilita **Sync recipient fields**.
3. Selecciona **Save**.
4. Ve a **Recipient Fields**.
5. Ejecuta **Sync from** el nombre de tu integración.

Better Email lee los atributos personalizados disponibles de Braze y los asigna a campos de destinatario.

## Solución de problemas {#troubleshooting}

Si una exportación o sincronización falla, verifica lo siguiente:

- La **Instance URL** es la URL REST, no la URL del dashboard
- La clave de API sigue activa y tiene los permisos de **Templates** necesarios
- La integración está habilitada en Better Email
- Los usuarios o grupos correctos tienen acceso a la integración

Para soporte adicional, contacta a [support@better.email](mailto:support@better.email).

## Usa la integración {#use-the-integration}

Puedes encontrar tus plantillas exportadas de Better Email en Braze en **Plantillas y medios** > **Plantillas de correo electrónico**. Úsalas en cualquier Campaign o Canvas de Braze.