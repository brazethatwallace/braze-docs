---
nav_title: Usuarios de la empresa
article_title: Administrar usuarios de la empresa
page_order: 0
page_type: reference
description: "Esta página cubre la administración de los usuarios de tu empresa, como añadir y eliminar usuarios, configurar permisos de usuario, crear equipos y administrar la configuración de la empresa."
---

# Administrar usuarios de la empresa {#manage-company-users}

> Aprende a administrar usuarios en la cuenta de tu empresa, incluyendo añadir, suspender y eliminar usuarios.

## Añadir usuarios de la empresa {#adding-company-users}

Debes tener permisos de administrador para añadir usuarios a tu cuenta de Braze.

Para añadir un nuevo usuario:

1. Ve a **Configuración** > **Administrar usuarios** > **Usuarios de la empresa**.
2. Selecciona **+ Añadir nuevo usuario**.
3. Introduce su información según se solicite, incluyendo su correo electrónico, departamento y [rol de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role).
4. Para los usuarios que no son administradores, selecciona los [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#editing-a-users-permissions) a nivel de empresa y a nivel de espacio de trabajo que deseas que tenga este usuario.

![Permisos a nivel de espacio de trabajo con una sección para campos de permisos personalizados.]({% image_buster /assets/img/add_new_user_3.png %})

### Requisitos de dirección de correo electrónico {#email-address-requirements}

Cada dirección de correo electrónico utilizada en una [instancia]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) debe ser única. Esto significa que si intentas añadir una dirección de correo electrónico que ya está asociada a un usuario que tuvo o aún tiene acceso a un espacio de trabajo de la empresa en esa instancia, verás un mensaje de error.

Si tu equipo utiliza Gmail y tienes problemas para añadir una dirección de correo electrónico, puedes crear un alias añadiendo un signo más (+) como "+1" o "+test" a la dirección de correo electrónico. Por ejemplo, `contractor@braze.com` puede tener un alias de `contractor+1@braze.com`. Los correos electrónicos enviados a `contractor+1@braze.com` seguirán entregándose a `contractor@braze.com`, pero el alias será reconocido como una dirección de correo electrónico única.

Para usar una cuenta en varias empresas sin alias, consulta [Usar desarrolladores multiempresa]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#use-multi-company-developers). Si usas SSO, revisa [Consideraciones para el inicio de sesión único (SSO)]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#considerations-for-single-sign-on-sso) antes de registrarte con varias direcciones de correo electrónico.

### ¿Puedo cambiar la dirección de correo electrónico de mi cuenta de Braze? {#can-i-change-my-braze-accounts-email-address}

Por razones de seguridad, los usuarios no pueden cambiar la dirección de correo electrónico asociada a su cuenta de Braze. Si un usuario desea actualizar su dirección de correo electrónico, un administrador debe [crear una nueva cuenta](#adding-company-users) con la dirección de correo electrónico preferida.

## Asignar acceso y responsabilidades de usuario {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Suspender usuarios de la empresa {#suspending-company-users}

Suspender a un usuario pone su cuenta en un estado inactivo, donde el usuario ya no puede iniciar sesión, pero los datos asociados a su cuenta se conservan. Solo los administradores pueden suspender o reactivar usuarios de la empresa. Ten en cuenta que los usuarios suspendidos aún pueden recibir notificaciones de Braze.

Para suspender a un usuario, ve a **Configuración** > **Administrar usuarios** > **Usuarios de la empresa**, busca su nombre de usuario y selecciona <i class="fa-solid fa-user-lock"></i> **Suspender**.

![Opción para suspender a un usuario.]({% image_buster /assets/img_archive/suspend_user.png %})

Los administradores también pueden suspender a un usuario seleccionando su nombre de la lista y seleccionando **Suspender usuario** en el pie de página.

![Suspender a un usuario al editar los detalles del usuario.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Eliminar usuarios de la empresa {#deleting-company-users}

Para eliminar a un usuario, ve a **Configuración** > **Administrar usuarios** > **Usuarios de la empresa**, busca el nombre del usuario y selecciona <i class="fa fa-trash-can"></i> **Eliminar usuario**.

Solo los administradores pueden eliminar usuarios de la empresa, y los usuarios de la empresa no pueden eliminar sus propias cuentas. Un administrador no puede eliminar su propia cuenta del dashboard; otro administrador debe hacerlo por él.

![Eliminar a un usuario.]({% image_buster /assets/img_archive/delete_user_new.png %})

Después de eliminar a un usuario, Braze no conserva ninguno de los siguientes datos de la cuenta:

- Cualquier atributo que el usuario tenía
- Dirección de correo electrónico
- Número de teléfono
- ID de usuario externo
- Género
- País
- Idioma
- Otros datos similares

Braze conservará los siguientes datos de la cuenta:

- Atributos personalizados o datos de prueba asociados a su cuenta
- Campaigns o Canvas que crearon (pero el nombre del usuario no aparecerá en ellos, como por ejemplo en la columna **Fecha últ. modific.**)

### Impacto de eliminar un usuario del dashboard {#impact-of-deleting-a-dashboard-user}

Cuando se elimina un usuario del dashboard, no hay un impacto significativo en los activos que creó dentro del dashboard, como Campaigns, Segments y Canvas. Sin embargo, el campo **Creada por** de estos activos mostrará un valor "null" en lugar de la dirección de correo electrónico del usuario eliminado.

Si posteriormente se crea un nuevo usuario del dashboard con la misma dirección de correo electrónico que el usuario eliminado, Braze no volverá a asociar los activos creados por el usuario eliminado con el nuevo usuario. El nuevo usuario del dashboard comenzará desde cero y no se le acreditará como creador de ningún activo existente en el dashboard.

## Solución de problemas {#troubleshooting}

### "No se puede realizar la acción" al añadir un usuario {#unable-to-perform-action-when-adding-a-user}

Si al añadir un usuario del dashboard se produce un error de "No se puede realizar la acción" (o similar):

- Elimina los espacios iniciales o finales y los caracteres ocultos de la dirección de correo electrónico.
- Confirma que la dirección tiene un formato de correo electrónico válido para tu organización. Algunos caracteres especiales son rechazados.
- El mismo correo electrónico no puede utilizarse para dos usuarios del dashboard en el mismo [clúster]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Si la dirección ya está registrada en otro espacio de trabajo en ese clúster, utiliza una dirección diferente o un alias como `user+1@company.com`.

### "El correo electrónico ya está en uso" al intentar añadir un usuario {#email-is-already-taken-when-trying-to-add-a-user}

Si intentas añadir un nuevo usuario y recibes un error que indica que el correo electrónico ya está en uso, pero no puedes encontrarlo en tu lista de usuarios, ese usuario probablemente existe en una instancia diferente del mismo clúster del dashboard de Braze.

Para crear este nuevo usuario, puedes hacer cualquiera de las siguientes opciones:

1. Eliminar al usuario de la otra instancia antes de poder crearlo en la nueva, o
2. Crear al usuario con una cadena de correo electrónico diferente (como `testing+01@braze.com`) u otro alias de correo electrónico.

Si no recibes el mensaje de activación en tu buzón de entrada al usar `testing+01@braze.com`, confirma con tu equipo de TI que puedes recibir mensajes de ese tipo de dirección de correo electrónico. Algunos administradores filtran los mensajes enviados a direcciones de correo electrónico con un `+`.

## Próximos pasos {#next-steps}

Después de añadir usuarios, administra su acceso:

- [Permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para configurar lo que cada usuario puede hacer en el dashboard.
- [Equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) para organizar usuarios en grupos con acceso compartido a objetos específicos del dashboard.