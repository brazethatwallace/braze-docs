---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Este artículo de referencia describe la asociación entre Braze y ViralSweep, un servicio de software que permite a las marcas crear, ejecutar y gestionar promociones de marketing digital como sorteos, concursos, premios instantáneos, listas de espera, promociones por referidos y más."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) es un servicio de software que permite a las marcas crear, ejecutar y gestionar promociones de marketing digital como sorteos, concursos, premios instantáneos, listas de espera, promociones por referidos y más.

_Esta integración está mantenida por ViralSweep._

## Sobre la integración {#about-the-integration}

La integración de Braze y ViralSweep te permite realizar sorteos y concursos en la plataforma ViralSweep (haciendo crecer tus listas de correo electrónico y SMS) y luego enviar la información de participación en sorteos o concursos a Braze para utilizarla en Campaigns o Canvas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de ViralSweep | Se requiere una cuenta de ViralSweep que utilice el plan de empresa para aprovechar esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con todos los permisos de datos de usuario y correo electrónico. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la URL de Braze para [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con Braze dentro de ViralSweep {#step-1-connect-to-braze-within-viralsweep}

En ViralSweep, ve a **Integrations > Email & SMS > Add Service** y selecciona **Braze**.

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### Paso 2: Añadir credenciales de Braze {#step-2-add-braze-credentials}

En la ventana de configuración de integraciones, proporciona tu clave de API REST de Braze y tu punto de conexión REST. Asegúrate de que el punto de conexión que proporcionas no incluye `https://`, por ejemplo, `dashboard-03.braze.com`.

![Página de integración del servicio ViralSweep que solicita al usuario la clave de API de Braze y la URL del dashboard de Braze.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Haz clic en **Connect**.

### Paso 3: Añadir credenciales de Braze {#step-3-add-braze-credentials}
¡Estás conectado! La promoción está ahora conectada a Braze, y todas las entradas recogidas por ViralSweep se enviarán a Braze automáticamente.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué campos pasa ViralSweep a Braze? {#what-fields-does-viralsweep-pass-to-braze}
- Nombre
- Apellido
- Dirección de correo electrónico
- Dirección
- Dirección 2
- Ciudad
- Estado
- Código postal
- País
- Fecha de nacimiento
- Teléfono
- ID de la promoción
- Enlace de referidos
- Nombre de la campaña de seguimiento

### ¿Actualiza ViralSweep a los suscriptores? {#does-viralsweep-update-subscribers}
Sí. Si realizas una promoción y ViralSweep pasa a alguien a Braze, y luego realizas otra promoción en el futuro y la misma persona participa, la información de esa persona se actualizará automáticamente en Braze (si se proporciona nueva información). Principalmente, la URL de referidos se actualizará con la URL más reciente de cada promoción en la que participen, y el campo de ID de promoción contendrá el ID de todas las promociones en las que hayan participado.

## Solución de problemas {#troubleshooting}

Si te has conectado a Braze y no se están añadiendo datos a tu cuenta, puede deberse a que:

- **El correo electrónico ya existe en Braze**<br>
Es posible que la dirección de correo electrónico introducida en la promoción ya figure en tu cuenta de Braze, por lo que no se añadirá de nuevo; solo se actualizará si se proporciona nueva información para ese contacto.<br><br>
- **El correo electrónico ya se introdujo en ViralSweep**<br>
La dirección de correo electrónico introducida en la promoción ya fue introducida anteriormente, por lo que no se pasa de nuevo a Braze. Esto puede ocurrir si configuras tu integración con Braze después de haber participado en la promoción.