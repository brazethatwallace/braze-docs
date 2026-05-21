---
nav_title: Transcend
article_title: Transcend
description: "Este artículo de referencia describe la asociación entre Braze y Transcend, una plataforma de infraestructura de privacidad de datos, que ayuda a los usuarios de Braze a automatizar el cumplimiento de las solicitudes de los interesados."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend es una empresa de infraestructura de privacidad de datos que simplifica a las empresas la tarea de dar a sus usuarios el control sobre sus datos, satisfaciendo automáticamente las solicitudes de los interesados dentro de las empresas en todos sus sistemas de datos y proveedores.

_Esta integración está mantenida por Transcend._

## Sobre la integración {#about-the-integration}

La asociación de Braze y Transcend ayuda a los usuarios a automatizar las solicitudes de privacidad mediante la orquestación de datos a través de docenas de sistemas de datos, ayudando a los equipos a cumplir con regulaciones como el RGPD y la CCPA. Transcend proporciona a los usuarios finales un panel de control, o centro de privacidad, alojado en `privacy.\<company\>.com`, donde los usuarios pueden gestionar sus preferencias de privacidad, exportar sus datos o eliminarlos.

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Cuenta de Transcend | Se requiere una cuenta de [Transcend](https://app.transcend.io/) con privilegios de administrador para beneficiarse de esta asociación. |
| Clave de API de Braze | Una clave de API REST de Braze con permisos `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` y `email.blacklist`.<br><br>Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Transcend te permite acceder de forma programática, borrar y excluir a los usuarios de la comunicación en la plataforma Braze de acuerdo con la normativa de privacidad de datos.

### Paso 1: Configurar la integración de Braze {#step-1-set-up-the-braze-integration}
Para empezar, inicia sesión en [Transcend](https://app.transcend.io/login).
1. Ve a **Data Map > Add Data Silo > Braze** y selecciona el botón **Connect**.<br><br>
2. Cuando se aprovisione tu cuenta, iniciarás sesión en una de las URL correspondientes: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Utiliza la siguiente [tabla]({{site.baseurl}}/api/basics/#endpoints) para averiguar qué subdominio debes incluir en función de la URL de tu dashboard.<br><br>
3. Cuando estés conectado, ve a la pestaña **Privacy Center** de Transcend. Aquí tendrás que asignar los datos de Braze a tus prácticas de datos. Para ello, crea una nueva categoría y una nueva recopilación de datos con la convención de nomenclatura adecuada (por ejemplo, "Listas de correo o perfil de usuario"). Cuando hayas terminado, selecciona **Publish**.<br><br>
4. Vuelve a tu Data Map y selecciona el silo de datos de Braze. Expande **Manage Datapoints** y selecciona en el desplegable la etiqueta de la colección (categoría) que creaste en el paso anterior. También puedes elegir qué acciones de datos (por ejemplo, acceso o borrado) están habilitadas para cada punto de datos. <br><br>
5. A continuación, mientras sigues en el silo de datos de Braze, expande **Manage Identifiers**. Marca las casillas correspondientes a los identificadores que deseas activar. Por ejemplo, si quieres que Transcend busque usuarios por dirección de correo electrónico, marca la casilla para activar el identificador de dirección de correo electrónico.

{% alert note %}
Si los identificadores no están habilitados correctamente, Transcend puede no procesar las solicitudes de determinados usuarios.
{% endalert %}

### Paso 2: Probar solicitudes {#step-2-test-requests}
Transcend recomienda probar las solicitudes a través de tu Data Map antes de empezar a procesar las solicitudes de los usuarios finales.
1. Ve al **Privacy Center** en Transcend y selecciona **View your Privacy Center**.<br><br>
2. En tu **Privacy Center**, selecciona **Take Control** y, a continuación, **Download my data**. Introduce tu correo electrónico o inicia sesión para autenticarte antes de enviar la solicitud.<br><br>
3. Revisa tu correo electrónico en busca de un mensaje de Transcend. Se te pedirá que hagas clic en un enlace de verificación para verificar la solicitud.<br><br>
4. A continuación, en el dashboard de **Admin**, ve a la pestaña **Incoming Requests** y selecciona tu solicitud. Ponte en contacto con Transcend en [support@transcend.io](mailto:support@transcend.io) si no ves la solicitud aquí.<br><br>
5. Una vez que hayas hecho clic en tu solicitud, ve a la pestaña **Data Silos** y selecciona **Braze**. Inspecciona y confirma los datos devueltos.<br><br>
6. Por último, ve a la pestaña **Report** y haz clic en **Approve and Send**. Deberías recibir el informe en la dirección de correo electrónico que proporcionaste con la solicitud.

## Eliminar la integración de Braze {#remove-the-braze-integration}
Para eliminar el silo de datos de Braze de tu Data Map de Transcend:
1. Ve a tu **Data Map** y haz clic en **Braze**. <br><br>
2. En la parte inferior de la pantalla, expande **Remove Braze** y haz clic en **Remove Silo**. Se te pedirá que confirmes que deseas eliminar el silo. Haz clic en **Ok**. <br><br>
3. Confirma que se ha eliminado el silo volviendo a tu Data Map.