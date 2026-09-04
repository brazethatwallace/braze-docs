---
nav_title: Cifrado a nivel de campo del identificador
article_title: Cifrado a nivel de campo del identificador
page_order: 2
alias: "/field_level_encryption/"
description: "Este artículo de referencia explica cómo cifrar direcciones de correo electrónico para minimizar la información de identificación personal (PII) compartida en Braze."
page_type: reference
---

# Cifrado a nivel de campo del identificador {#identifier-field-level-encryption}

> Cifra direcciones de correo electrónico para minimizar la información de identificación personal (PII) compartida en Braze.

{% multi_lang_include data_activation/field_level_encryption_pii_description.md %}

{% alert important %}
El cifrado a nivel de campo del identificador está disponible como característica adicional. Para empezar a utilizar el cifrado a nivel de campo del identificador, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

## Cómo funciona {#how-it-works}

Las direcciones de correo electrónico deben ser hasheadas y encriptadas antes de añadirse a Braze. Cuando se envía un mensaje, se realizará una llamada a AWS KMS para obtener la dirección de correo electrónico desencriptada. A continuación, la dirección de correo electrónico hasheada se insertará en los metadatos para que los eventos de entrega y participación se vinculen al usuario original. Así es como Braze puede rastrear los análisis de correo electrónico. Braze eliminará cualquier dirección de correo electrónico en texto plano que se incluya y no almacenará la dirección de correo electrónico en texto plano del usuario.

## Requisitos previos {#prerequisites}

Para utilizar el cifrado a nivel de campo de identificador, debes tener acceso a AWS KMS para [cifrar](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) y [generar un hash](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) de las direcciones de correo electrónico **antes** de enviarlas a Braze.

Sigue estos pasos para configurar tu método de autenticación con clave secreta de AWS.

1. Para obtener tu ID de clave de acceso y tu clave de acceso secreta, [crea un usuario de IAM y un grupo de administradores](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) en AWS con una política de permisos para AWS Key Management Service. El usuario de IAM debe tener los permisos [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) y [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Para más detalles, consulta [Permisos de AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Selecciona **Show User Security Credentials** para revelar tu ID de clave de acceso y tu clave de acceso secreta. Anota estas credenciales en algún lugar o selecciona el botón **Download Credentials**, ya que necesitarás introducirlas al conectar tus claves de AWS KMS.
3. Debes configurar KMS en las siguientes regiones de AWS:
    - **Clústeres de Braze en EE. UU.:** `us-east-1`
    - **Clústeres de Braze en la UE:** `eu-central-1`
    - **Clúster de Braze en AU:** `ap-southeast-2`
    - **Clúster de Braze en ID:** `ap-southeast-3`
    - **Clúster de Braze en JP:** `ap-northeast-1`
4. En AWS Key Management Service, crea dos claves y asegúrate de que el usuario de IAM se añada en los permisos de uso de claves:
    - **[Cifrar/descifrar](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Selecciona el tipo de clave **Symmetric** y el uso de clave **Encrypt and Decrypt**.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Selecciona el tipo de clave **Symmetric** y el uso de clave **Generate and Verify MAC**. La especificación de la clave debe ser **HMAC_256**. Después de crear la clave, anota el ID de clave HMAC en algún lugar, ya que necesitarás introducirlo en Braze.

![Configuración de los ajustes de clave con las opciones symmetric, generate and verify MAC y HMAC_256 seleccionadas.]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Paso 1: Conecta tus claves de AWS KMS {#step-1-connect-your-aws-kms-keys}

En el panel de Braze, ve a **Configuración de datos** > **Cifrado a nivel de campo**. Para tu configuración de AWS KMS, introduce lo siguiente:

- ID de clave de acceso
- Clave de acceso secreta
- Identificador de clave HMAC (ID de clave o ARN de clave; no se puede actualizar después de guardar)

## Paso 2: Selecciona tus campos cifrados {#step-2-select-your-encrypted-fields}

A continuación, selecciona **Email address** para cifrar el campo.

Cuando el cifrado está activado para un campo, no se puede revertir a un campo descifrado. Esto significa que el cifrado es una configuración permanente. Al configurar el cifrado para la dirección de correo electrónico, confirma que no haya usuarios con direcciones de correo electrónico en el espacio de trabajo. Esto garantiza que no se almacenen direcciones de correo electrónico en texto plano en Braze al activar la característica para el espacio de trabajo.

![Configuración de cifrado a nivel de campo.]({% image_buster /assets/img/field_level_encryption.png %})

## Paso 3: Importar y actualizar usuarios {#step-3-import-and-update-users}

Cuando la encriptación a nivel de campo de identificador está activada, debes aplicar hash y encriptar la dirección de correo electrónico antes de añadirla a Braze. Asegúrate de convertir la dirección de correo electrónico a minúsculas antes de aplicar el hash. Consulta el [objeto de atributos de usuario](#user-attributes-object) para más detalles.

Al actualizar la dirección de correo electrónico en Braze, debes usar el valor de correo electrónico con hash en cualquier lugar donde se incluya `email`. Esto incluye:

- Endpoints REST:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Añadir o actualizar usuarios mediante CSV

{% alert note %}
Al crear un nuevo usuario con una dirección de correo electrónico, debes añadir `email_encrypted` con el valor de correo electrónico encriptado del usuario. De lo contrario, el usuario no se creará. De manera similar, si estás añadiendo una dirección de correo electrónico a un usuario existente que no tiene correo electrónico, debes añadir `email_encrypted`. De lo contrario, el usuario no se actualizará.
{% endalert %}

## Consideraciones {#considerations}

Estas características no son compatibles con la encriptación a nivel de campo de identificadores:

- Identificación y captura de direcciones de correo electrónico a través del SDK
- Formularios de captura de correo electrónico en mensajes dentro de la aplicación
- Informes sobre el dominio del destinatario, incluidos los gráficos de proveedores de buzón de Email Insights
- Filtro de dirección de correo electrónico por expresión regular
- Audience sync
- Integración con Shopify

### Objeto de atributos de usuario {#user-attributes-object}

Cuando uses la encriptación a nivel de campo de identificadores con el endpoint `/users/track`, ten en cuenta estos detalles de campo para el [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- El campo `email` debe ser el valor hash del correo electrónico.
- El campo `email_encrypted` debe ser el valor encriptado del correo electrónico.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuál es la diferencia entre cifrar y aplicar hash? {#what-is-the-difference-between-encrypting-and-hashing}

El cifrado es una función bidireccional en la que es posible cifrar y descifrar datos. Si el mismo valor en texto plano se cifra varias veces, el algoritmo de cifrado de AWS (AES-256-GCM) producirá valores cifrados diferentes. El hash es una función unidireccional en la que el texto plano se transforma de una manera que no se puede descifrar. El hash produce el mismo valor cada vez. Esto nos permite mantener los estados de suscripción en varios usuarios que comparten la misma dirección de correo electrónico.

### ¿Qué dirección de correo electrónico debo usar en mi envío de prueba? {#what-email-address-should-i-use-in-my-test-send}

Las direcciones de correo electrónico en texto plano son compatibles con los envíos de prueba. Para ver cómo luce un correo electrónico para un usuario específico, haz lo siguiente:

1. Selecciona **Vista previa del mensaje como un usuario**.
2. En **Envío de prueba**, selecciona **Anular los atributos de los destinatarios con los atributos del usuario de vista previa actual**.

### ¿Puedo usar un ARN para la clave HMAC? {#can-i-use-an-arn-for-the-hmac-key}

Sí. En **Configuración de datos** > **Cifrado a nivel de campo**, el identificador de la clave HMAC acepta un ID de clave o un ARN de clave.

### ¿Cómo elimino o restablezco una clave HMAC? {#how-do-i-remove-or-reset-an-hmac-key}

No puedes eliminar ni restablecer una clave HMAC en el panel después de guardarla. Para solicitar el restablecimiento de una clave HMAC o la eliminación de la configuración de cifrado a nivel de campo del identificador, contacta a tu director de cuentas de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support).

{%raw%}
### ¿Qué sucede si agrego esta dirección de correo electrónico con Liquid `{{${email_address}}}` en Braze? {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Braze mostrará la dirección de correo electrónico en texto plano al enviar el correo electrónico. En las vistas previas, mostraremos la versión cifrada del correo electrónico. Recomendamos usar el ID externo del usuario si estás haciendo referencia a un usuario en una URL personalizada de cancelación de suscripción con un clic.

`{{${email_address}}}` no es compatible actualmente con el centro de preferencias ni con las páginas de cancelación de suscripción.
{%endraw%}

### ¿Qué dirección de correo electrónico debo esperar ver en Currents? {#what-email-address-should-i-expect-to-see-in-currents}

La dirección de correo electrónico con hash se incluye en los eventos de entrega y participación de correo electrónico.

### ¿Qué dirección de correo electrónico debo esperar ver en el archivo de mensajes? {#what-email-address-should-i-expect-to-see-in-message-archiving}

La dirección de correo electrónico en texto plano se incluye en el archivo de mensajería. Estos se envían directamente al proveedor de almacenamiento en el cloud del cliente y puede haber otros datos personales incluidos en los cuerpos del correo electrónico.

### ¿Puedo usar la cancelación de suscripción de lista por correo para la gestión de suscripciones con el cifrado a nivel de campo del identificador? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

No. Usar la cancelación de suscripción de lista por correo enviaría la dirección de correo electrónico descifrada en texto plano a Braze. Con el cifrado a nivel de campo del identificador activado, admitimos el método basado en URL HTTP:, incluido un clic. También recomendamos incluir un enlace de cancelación de suscripción con un clic en el cuerpo de tu correo electrónico.

### ¿El cifrado a nivel de campo del identificador admite otros identificadores como el teléfono? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

No. Actualmente, el cifrado a nivel de campo del identificador solo es compatible con direcciones de correo electrónico.