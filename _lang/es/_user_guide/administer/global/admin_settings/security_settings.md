---
nav_title: Configuración de seguridad
article_title: Configuración de seguridad
page_order: 2
toc_headers: h2
page_type: reference
description: "Este artículo de referencia cubre la configuración genérica de seguridad entre empresas, incluidas las reglas de autenticación, las listas de IP permitidas, la PII y la autenticación de dos factores (2FA)."

---

# Configuración de seguridad {#security-settings}

> Como administrador, la seguridad es una prioridad en tu lista de preocupaciones. La página **Configuración de seguridad** puede ayudarte a gestionar la configuración de seguridad genérica para toda la empresa, incluidas las reglas de autenticación, la lista de IP permitidas y la autenticación de dos factores.

Para acceder a esta página, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad**.

## Reglas de autenticación {#authentication-rules}

### Longitud de la contraseña {#password-length}

Utiliza este campo para cambiar la longitud mínima requerida de la contraseña. El mínimo predeterminado es de ocho caracteres.

### Complejidad de la contraseña {#password-complexity}

Selecciona **Aplicar contraseñas complejas** para requerir que las contraseñas incluyan al menos uno de cada uno de los siguientes elementos:
- Letra mayúscula
- Letra minúscula
- Número
- Carácter especial (cualquier carácter que no sea una letra ni un número, como `!`, `@`, `#` o `(`)

### Reutilización de contraseñas {#password-re-usability}

Determina el número mínimo de contraseñas nuevas que deben establecerse antes de que un usuario pueda reutilizar una contraseña. El valor predeterminado es tres.

### Reglas de expiración de contraseñas {#password-expiration-rules}

Utiliza este campo para establecer cuándo quieres que los usuarios de tu cuenta de Braze restablezcan su contraseña.

### Reglas de duración de la sesión {#session-duration-rules}

Utiliza este campo para definir cuánto tiempo Braze mantendrá tu sesión activa. Cuando Braze considere que tu sesión está inactiva (sin actividad durante el número de minutos definido), cerrará la sesión del usuario. El número máximo de minutos que puedes introducir es 10 080 (equivalente a una semana) si la autenticación de dos factores está habilitada para tu empresa; de lo contrario, la duración máxima de la sesión es de 1440 minutos (equivalente a 24 horas).

### Autenticación de inicio de sesión único (SSO) {#single-sign-on-sso-authentication}

Puedes restringir a tus usuarios para que inicien sesión utilizando una contraseña o SSO.

Para [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on), los clientes deben configurar sus ajustes de SAML antes de aplicar esta opción. Si los clientes utilizan Google SSO, solo necesitan aplicar la página de configuración de seguridad sin ningún esfuerzo adicional.

## Lista de IP permitidas del panel {#dashboard-ip-allowlisting}

Usa el campo que se muestra para añadir a la lista de permitidas las direcciones IP y subredes específicas desde las que los usuarios pueden iniciar sesión en tu cuenta (por ejemplo, desde una red corporativa o VPN). Especifica las direcciones IP y subredes como rangos CIDR en una lista separada por comas. Si no se especifica, los usuarios pueden iniciar sesión desde cualquier dirección IP.

## Autenticación de dos factores (2FA) {#two-factor-authentication-2fa}

La autenticación de dos factores es obligatoria para todos los usuarios de la empresa. Añade un segundo nivel de verificación de identidad a un inicio de sesión de cuenta, haciéndolo más seguro que solo un nombre de usuario y una contraseña. Si tu panel no puede admitir la autenticación de dos factores, ponte en contacto con tu administrador de éxito de cliente.

Cuando la autenticación de dos factores está activada:

- Además de introducir una contraseña, los usuarios necesitan introducir un código de verificación al iniciar sesión en su cuenta de Braze. El código puede enviarse a través de una aplicación de autenticación, correo electrónico o SMS.
- La casilla **Recordar esta cuenta durante 30 días** pasa a estar disponible para los usuarios.

Braze bloquea a los usuarios que no configuren su autenticación de dos factores en su cuenta de Braze. Los usuarios de cuentas de Braze también pueden configurar la autenticación de dos factores por su cuenta en **Configuración de la cuenta**, aunque no sea obligatorio por parte del administrador.

¡Asegúrate de guardar los cambios antes de salir de la página!

### Recordar esta cuenta durante 30 días {#remember-me}

Esta característica está disponible cuando la autenticación de dos factores está activada.

Cuando seleccionas **Recordar esta cuenta durante 30 días**, se almacena una cookie en tu dispositivo, y solo necesitarás iniciar sesión con autenticación de dos factores una vez en el transcurso de 30 días.

![Casilla Recordar esta cuenta durante 30 días]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Los clientes con varias cuentas en una empresa del panel pueden experimentar problemas al usar esta característica, ya que la cookie está vinculada a un dispositivo específico. Si los usuarios utilizan el mismo dispositivo para iniciar sesión en varias cuentas, la cookie se reemplazará para las cuentas previamente autorizadas en ese dispositivo. Braze espera que solo un dispositivo esté asociado a una cuenta, no un dispositivo para varias cuentas.

### Restablecer la autenticación de usuario {#resetting-user-authentication}

Si tienes problemas para iniciar sesión con la autenticación de dos factores, ponte en contacto con los administradores de tu empresa para restablecer tu autenticación de dos factores. Los administradores pueden realizar los siguientes pasos:

1. Ve a **Configuración** > **Configuración de la empresa** > **Gestión de usuarios** > **Usuarios de la empresa**.
2. Selecciona el usuario de la lista proporcionada.
3. Selecciona **Restablecer** en **Autenticación de dos factores**.

Un restablecimiento puede resolver problemas comunes de autenticación, como dificultades con aplicaciones de autenticación, verificación por correo electrónico que no se envía, fallos de inicio de sesión debido a interrupciones de SMS o errores del usuario, y más.

### Requisitos para 2FA a nivel de empresa {#requirements-for-2fa-at-the-company-level}

Primero, verifica si 2FA está habilitado para tu panel yendo a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** > **Autenticación de dos factores**. Si el interruptor está en gris, 2FA no se ha activado para tu empresa y no es obligatorio para todos los usuarios de la empresa.

#### Opciones del usuario cuando 2FA no es obligatorio {#user-options-when-2fa-isnt-mandatory}

Si 2FA no se aplica a nivel de empresa, los usuarios individuales pueden configurar 2FA por su cuenta en su página de configuración de la cuenta. En este caso, los usuarios no serán bloqueados de sus cuentas si no lo configuran. Puedes identificar qué usuarios han optado por habilitar 2FA consultando la lista de **Usuarios de la empresa**.

#### Requisitos cuando 2FA es obligatorio {#requirements-when-2fa-is-mandatory}

Si 2FA se aplica a nivel de empresa, los usuarios que no lo configuren en sus propias cuentas al iniciar sesión serán bloqueados del panel. Los usuarios deben completar la configuración de 2FA para mantener el acceso.

{% alert important %}
2FA es obligatorio para todos los usuarios de la empresa solo si el inicio de sesión único (SSO) no está habilitado. Si se utiliza SSO, no es necesario aplicar 2FA a nivel de empresa.
{% endalert %}

## Configurar 2FA manualmente {#manually-set-up-2fa}

Para activar manualmente la autenticación de dos factores (2FA) en tu cuenta de Braze, sigue estos pasos:

1. En Braze, selecciona el icono de tu perfil en el encabezado global y luego selecciona **Administrar tu cuenta**. Desplázate hasta la sección **Autenticación de dos factores** y selecciona **Iniciar configuración**.
2. Introduce tu contraseña en el modal de inicio de sesión y selecciona **Verificar contraseña**.
3. En el modal **Configuración de autenticación de dos factores**, introduce tu número de teléfono y selecciona **Habilitar**.
4. Copia el código de siete dígitos generado desde tu correo electrónico o mensaje SMS, luego regresa a Braze y pégalo en el modal **Configuración de autenticación de dos factores**. Selecciona **Verificar**.
5. (Opcional) Para evitar introducir 2FA durante los próximos 30 días, habilita la opción **Recordar esta cuenta durante 30 días**.

## Acceso elevado {#elevated-access}

El acceso elevado añade una capa adicional de seguridad para las acciones sensibles en tu panel de Braze. Cuando está activo, los usuarios deben volver a verificar su cuenta antes de exportar un Segment o ver una clave de API. Para usar el acceso elevado, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y actívalo.

Si un usuario no puede volver a verificarse, será redirigido al lugar donde se quedó y no podrá continuar con la acción sensible. Después de verificarse correctamente, no necesitará hacerlo de nuevo durante la siguiente hora, a menos que cierre sesión primero.

## Descargar un informe de eventos de seguridad {#security-event-report}

El informe de eventos de seguridad es un informe CSV de eventos de seguridad como invitaciones a cuentas, eliminaciones de cuentas, intentos de inicio de sesión fallidos y exitosos, y otras actividades. Puedes usarlo para realizar auditorías internas.

Para descargar este informe, haz lo siguiente:

1. Ve a **Configuración** > **Configuración de empresa** > **Configuración de administrador** > **Configuración de seguridad**.
2. Ve a la sección **Descarga de evento de seguridad**.
3. Selecciona **Download report**.

Esta descarga manual de informe solo contiene los 10 000 eventos de seguridad más recientes de tu cuenta. Si tu CSV exportado contiene exactamente 10 001 filas (incluida la fila de encabezado), alcanzaste el límite de 10 000 eventos del informe y es posible que no se incluyan eventos más antiguos.

Para exportar eventos de seguridad a Amazon S3 sin este límite de filas, consulta [Exportación de eventos de seguridad con Amazon S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3).

### Definiciones de columnas del CSV {#csv-column-definitions}

El informe CSV de eventos de seguridad contiene las siguientes columnas:

| Columna | Descripción |
|--------|-------------|
| CreatedAt | Marca de tiempo en la que se registró el evento, en UTC. |
| EmailAtTimeOfEvent | Dirección de correo electrónico del usuario del panel que desencadenó el evento, tal como se registró cuando ocurrió el evento. |
| CurrentEmail | Dirección de correo electrónico actual del usuario del panel que desencadenó el evento. Si el usuario ya no existe, se usa su ID de desarrollador en su lugar. |
| EventName | Tipo de evento de seguridad. Consulta el desplegable **Eventos de seguridad reportados** después de esta tabla. |
| OtherAccount | Dirección de correo electrónico de otro usuario del panel afectado por el evento, cuando corresponda (por ejemplo, cuando se añade o elimina una cuenta). |
| JsonProperties | Propiedades específicas del evento en formato JSON. Los campos incluidos varían según el tipo de evento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definiciones de columnas del CSV" }

Las [exportaciones a S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3) incluyen estas columnas más `Version`, la versión del esquema para el formato de exportación (actualmente `1`).

{% details Eventos de seguridad reportados %}
### Inicio de sesión y cuenta {#login-and-account}
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Added Additional Developer
- Added Account
- Developer Suspended
- Developer Unsuspended
- Developer Updated
- Removed Developer
- Removed Account
- User Subscription Status Updated
- User Updated
- Developer Account Updated

### Acceso elevado
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access
- Enabled Elevated Access Enforcement
- Disabled Elevated Access Enforcement

Campaign
- Added Campaign
- Edited Campaign

Canvas
- Added Canvas
- Edited Canvas

### Segment
- Added Segment
- Edited Segment
- Exported data to CSV
- Exported Segment via API
- Segment Users Deleted
- Cleared Cohort

### Clave de API REST {#rest-api-key}
- Added REST API key
- Removed REST API key

### Credencial de autenticación básica {#basic-authentication-credential}
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### Permiso {#permission}
- Cleared Developer 2FA
- Updated Account Permission
- Added Team
- Edited Team
- Archived Team
- Unarchived Team
- Created App Group Permission Set
- Edited App Group Permission Set
- Removed App Group Permission Set
- Created Custom Role
- Updated Custom Role
- Deleted Custom Role

### Configuración de empresa {#company-settings}
- Added App Group
- Added App
- Company Settings Changed
- Updated Company Security Settings
- Updated Security Event Cloud Export
- Added Landing Pages Custom Domain
- Removed Landing Pages Custom Domain
- Custom Domain Created
- Custom Domain Deleted
- Enabled Global Control Group
- Disabled Global Control Group
- Updated Global Control Exclusions
- Updated Subscription Group SMS Allow List

### Plantilla de correo electrónico {#email-template}
- Added Email Template
- Updated Email Template

### Credencial push {#push-credential}
- Updated Push Credential
- Removed Push Credential

### Depurador de SDK {#sdk-debugger}
- Started SDK Debugger Session
- Exported SDK Debugger Log

### Usuarios {#users}
- Users Deleted
- Users Viewed
- User Import Started
- User Subscription Group Status Updated
- User Deleted
- Single User Deletion Cancelled
- Bulk User Deletion Cancelled

### Catálogos {#catalogs}
- Catalog Created
- Catalog Deleted

### Braze Agents
- Created Agent
- Edited Agent

### BrazeAI Operator
- Requested BrazeAI Operator Response
- BrazeAI Operator Responded
{% enddetails %}

## Ver información de identificación personal (PII) {#view-pii}

El permiso **View PII** solo es accesible para unos pocos usuarios seleccionados de la empresa. De forma predeterminada, todos los administradores tienen su permiso **View PII** activado en los permisos de usuario. Esto significa que pueden ver todos los atributos estándar y personalizados que tu empresa ha definido como PII en todo el panel. Cuando este permiso está desactivado para los usuarios, esos usuarios no podrán ver ninguno de esos atributos.

{% alert note %}
Necesitas el permiso **View PII** para usar el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/building_queries), ya que permite el acceso directo a algunos datos de clientes.
{% endalert %}

Para las capacidades existentes de permisos de equipo, consulta [Configurar permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

### Definir PII {#defining-pii}

{% alert important %}
Seleccionar y definir ciertos campos como campos PII solo afecta lo que los usuarios pueden ver en el panel de Braze y no afecta cómo se manejan los datos del usuario final en dichos campos PII.<br><br>Consulta con tu equipo legal para alinear la configuración de tu panel con cualquier regulación y política de privacidad aplicable a tu empresa, incluidas las relacionadas con la [retención de datos]({{site.baseurl}}/data_retention).
{% endalert %}

Puedes seleccionar los campos que tu empresa designa como PII en el panel. Para hacerlo, ve a **Configuración** > **Configuración de empresa** > **Configuración de administrador** > **Configuración de seguridad**.

Los siguientes atributos pueden designarse como PII y ocultarse de los usuarios de la empresa que no tengan permisos de **View PII**.

#### Atributos potenciales de PII {#potential-pii-attributes}

| Atributos estándar | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown}<ul> <li>Dirección de correo electrónico </li> <li> Número de teléfono </li> <li> Nombre </li> <li> Apellido </li> <li> Género </li> <li> Fecha de nacimiento </li> <li> ID de dispositivo </li> <li> LINE ID </li> <li> Ubicación más reciente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos los atributos personalizados<ul><li>Los atributos personalizados individuales pueden marcarse como PII si no necesitas ocultar todos los atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos potenciales de PII" }

### Áreas restringidas {#limited-areas}

Lo siguiente asume que todos los campos están configurados como PII, y los usuarios mencionados son usuarios de la empresa que usan la plataforma Braze. Además, los atributos "anteriores" se refieren a los de la tabla [Atributos potenciales de PII](#potential-pii-attributes). Quitar los permisos de PII de un usuario puede afectar la usabilidad más allá de estas áreas listadas.

| Navegación del panel | Resultado | Notas |
| -------------------- | ------ | ----- |
| Búsqueda de usuarios | El usuario que inicia sesión no puede buscar por dirección de correo electrónico, número de teléfono, nombre o apellido: {::nomarkdown} <ul> <li> No se le mostrarán los atributos estándar y personalizados anteriores al ver un perfil de usuario. </li> <li> No puede editar los atributos estándar anteriores de un perfil de usuario desde el panel de Braze. </li> <li> No puede actualizar el estado de suscripción en un perfil de usuario. </li></ul> {:/} | El acceso a esta sección aún requiere acceso para ver un perfil de usuario. |
| Importación de usuarios | El usuario no puede descargar archivos desde la página **Importación de usuarios**. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campaigns </li> <li> Canvas </li> </ul> {:/} | En el menú desplegable **User Data**: {::nomarkdown} <ul> <li> El usuario no tendrá la opción <b>CSV Export Email Address</b>. </li> <li> El usuario no recibirá los atributos estándar y personalizados anteriores en el archivo CSV al seleccionar <b>CSV Export User Data</b>. </li> </ul> {:/} | |
| Grupo de prueba interno | El usuario no tendrá acceso a los atributos estándar anteriores de cualquier usuario añadido al grupo de prueba interno. | |
| Registro de actividad de mensajes | El usuario no tendrá acceso a los atributos estándar anteriores de cualquier usuario identificado en el registro de actividad de mensajes. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Áreas restringidas" }

{% alert note %}
Al previsualizar un mensaje, el permiso **View PII** no se aplica, por lo que los usuarios pueden ver los [atributos estándar anteriores](#potential-pii-attributes) si fueron referenciados en el mensaje a través de Liquid.
{% endalert %}

## Preferencias de eliminación de datos {#data-deletion-preferences}

Puedes usar esta configuración para establecer preferencias sobre si Braze debe eliminar ciertos campos durante el proceso de eliminación de usuarios para eventos. Estas preferencias solo afectan a los datos de los usuarios que Braze ha eliminado.

Cuando se elimina un usuario, Braze elimina toda la PII de los datos de eventos, pero conserva los datos anonimizados con fines de análisis. Algunos campos definidos por el usuario pueden contener PII si envías información de usuarios finales a Braze. Si estos campos contienen PII, puedes optar por eliminar los datos cuando Braze anonimiza los datos de eventos de los usuarios eliminados; si los campos no contienen PII, puedes conservarlos para análisis.

Eres responsable de determinar las preferencias correctas para tu espacio de trabajo. La mejor manera de determinar la configuración adecuada es revisarla con los equipos internos que envían datos de eventos a Braze y con los equipos que utilizan extras de mensaje en Braze para confirmar si los campos pueden contener PII.

### Campos relevantes {#relevant-fields}

| Nombre o tipo de evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | properties |  |
| Evento de compra | properties |  |
| Envío de mensaje | message_extras | Varios tipos de eventos contienen un campo `message_extras`. La preferencia se aplica a todos los tipos de eventos de envío de mensaje que admiten `message_extras`, incluidos los tipos de eventos que se añadan en el futuro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos relevantes" }

{% alert warning %}
**¡La eliminación es permanente!** Si optas por eliminar cualquier campo de Snowflake para los usuarios eliminados, la configuración se aplica a todos los datos históricos en tus espacios de trabajo y a cualquier evento de usuarios eliminados en el futuro. Después de que Braze haya ejecutado el proceso para aplicar la configuración a los datos históricos de eventos de usuarios eliminados, **no puedes restaurar** los datos.
{% endalert %}

### Configurar preferencias {#configure-preferences}

Establece las preferencias predeterminadas marcando las casillas de los campos que Braze debe eliminar si se elimina un usuario. Selecciona cualquiera de los campos que contengan PII. Esta preferencia se aplica a todos los espacios de trabajo actuales y futuros, a menos que los espacios de trabajo se añadan explícitamente a un grupo de preferencias.

Para personalizar las preferencias por espacio de trabajo, puedes añadir grupos de preferencias con configuraciones diferentes a las predeterminadas. Aplicamos la configuración predeterminada a cualquier espacio de trabajo que no se haya añadido a un grupo de preferencias adicional, incluidos los espacios de trabajo creados en el futuro.

![Sección de preferencias de eliminación de datos con el interruptor activado para personalizar las preferencias de eliminación de datos por espacio de trabajo.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Solución de problemas {#troubleshooting}

### Problemas de bucle en la configuración de la autenticación de dos factores (2FA) {#two-factor-authentication-2fa-setup-loop-issues}

Si te encuentras atrapado en un bucle después de introducir correctamente tu número de teléfono para 2FA y se te redirige de vuelta a la página de inicio de sesión, es probable que se deba a un fallo en la verificación en el primer intento. Para resolver este problema, sigue estos pasos:

1. Desactiva cualquier bloqueador de anuncios.
2. Habilita las cookies en la configuración de tu navegador.
3. Reinicia tu PC o portátil.
4. Intenta configurar 2FA de nuevo.

Si el problema persiste después de estos pasos, ponte en contacto con [Soporte]({{site.baseurl}}/braze_support) para obtener ayuda.

### No se puede habilitar la autenticación de dos factores (2FA) {#cant-enable-two-factor-authentication-2fa}

Si 2FA está habilitada pero no ocurre nada cuando seleccionas el botón **Habilitar**, puede deberse a que tu navegador está bloqueando la redirección necesaria para enviar el código de verificación a través de SMS. Estos son los pasos para solucionar este problema:

1. Suspende temporalmente cualquier bloqueador de anuncios que tengas habilitado en tu navegador.
2. Confirma que has habilitado las cookies de terceros en la configuración de tu navegador.
3. Intenta configurar 2FA.

### El código de verificación no se envía {#verification-code-doesnt-send}

Si tienes problemas al introducir tu número de teléfono en la página de Authy y no recibes un SMS, sigue estos pasos:

1. Instala la aplicación Authy en tu teléfono e inicia sesión en el autenticador Authy.
2. Introduce tu número de teléfono y comprueba la aplicación Authy en busca de cambios o notificaciones por SMS.
3. Si sigues sin recibir el SMS, intenta usar una conexión de red diferente, como tu red doméstica o una red Wi-Fi no corporativa. Las redes corporativas pueden tener políticas de seguridad que interfieren con la entrega de SMS.

Si los problemas persisten, elimina el perfil antiguo en la aplicación Authy y escanea el código QR de nuevo para configurar 2FA. Asegúrate de haber desactivado cualquier bloqueador de anuncios, habilitado las cookies de terceros o utilizado un navegador diferente antes de intentar la configuración de nuevo.

## Próximos pasos {#next-steps}

Para obtener más información sobre autenticación y acceso, consulta:

- [SAML e inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) para configurar SSO con tu proveedor de identidad.
- [Permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para controlar qué acciones pueden realizar los usuarios en el panel.