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

Las direcciones de correo electrónico deben someterse a hash y cifrarse antes de añadirlas a Braze. Cuando se envía un mensaje, se realiza una llamada a AWS KMS para obtener la dirección de correo electrónico descifrada. A continuación, la dirección de correo electrónico con hash se inserta en los metadatos para que los eventos de entrega e interacción se vinculen al usuario original. Así es como Braze puede hacer un seguimiento del análisis del correo electrónico. Braze redactará cualquier dirección de correo electrónico en texto plano que se incluya y no almacenará la dirección de correo electrónico en texto plano del usuario.

## Requisitos previos {#prerequisites}

Para utilizar el cifrado a nivel de campo del identificador, debes tener acceso a AWS KMS para [cifrar](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) y [aplicar hash a](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) las direcciones de correo electrónico **antes de** enviarlas a Braze.

Sigue estos pasos para configurar tu método de autenticación con clave secreta de AWS.

1. Para recuperar tu ID de clave de acceso y tu clave de acceso secreta, [crea un usuario IAM y un grupo de administradores](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) en AWS con una política de permisos para AWS Key Management Service. El usuario IAM debe tener los permisos [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) y [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Para más detalles, consulta los [permisos de AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Selecciona **Show User Security Credentials** para revelar tu ID de clave de acceso y tu clave de acceso secreta. Anota estas credenciales en algún sitio o selecciona el botón **Download Credentials**, ya que tendrás que introducirlas cuando conectes tus claves de AWS KMS.
3. Debes configurar KMS en las siguientes regiones de AWS:
    - **Clústeres de Braze US:** `us-east-1`
    - **Clústeres de Braze EU:** `eu-central-1`
    - **Clúster de Braze AU:** `ap-southeast-2`
    - **Clúster de Braze ID:** `ap-southeast-3`
    - **Clúster de Braze JP:** `ap-northeast-1`
4. En AWS Key Management Service, crea dos claves y asegúrate de que el usuario IAM esté añadido en los permisos de uso de claves:
    - **[Cifrar/descifrar](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Selecciona el tipo de clave **Symmetric** y el uso de clave **Encrypt and Decrypt**.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Selecciona el tipo de clave **Symmetric** y el uso de clave **Generate and Verify MAC**. La especificación de clave debe ser **HMAC_256**. Después de crear la clave, anota en algún sitio el ID de la clave HMAC, ya que tendrás que introducirlo en Braze.

![Configuración de clave con las opciones symmetric, generate and verify MAC y HMAC_256 seleccionadas.]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Paso 1: Conecta tus claves de AWS KMS {#step-1-connect-your-aws-kms-keys}

En el panel de Braze, ve a **Configuración de datos** > **Field-Level Encryption**. Para tu configuración de AWS KMS, introduce lo siguiente:

- ID de la clave de acceso
- Clave de acceso secreta
- ID de la clave HMAC (no se puede actualizar después de guardar)

## Paso 2: Selecciona tus campos cifrados {#step-2-select-your-encrypted-fields}

A continuación, selecciona **Email address** para cifrar el campo.

Cuando se activa el cifrado de un campo, no se puede revertir a un campo descifrado. Esto significa que el cifrado es una configuración permanente. Cuando configures el cifrado para la dirección de correo electrónico, confirma que ningún usuario tenga direcciones de correo electrónico en el espacio de trabajo. Esto garantiza que no se almacenen direcciones de correo electrónico en texto plano en Braze al activar la característica para el espacio de trabajo.

![Configuración de cifrado a nivel de campo.]({% image_buster /assets/img/field_level_encryption.png %})

## Paso 3: Importar y actualizar usuarios {#step-3-import-and-update-users}

Cuando el cifrado a nivel de campo del identificador está activado, debes aplicar hash y cifrar la dirección de correo electrónico antes de añadirla a Braze. Asegúrate de convertir la dirección de correo electrónico a minúsculas antes de aplicar el hash. Consulta el [objeto de atributos del usuario](#user-attributes-object) para más detalles.

Al actualizar la dirección de correo electrónico en Braze, debes utilizar el valor de correo electrónico con hash siempre que se incluya `email`. Esto incluye lo siguiente:

- Puntos finales REST:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Añadir o actualizar usuarios mediante CSV

{% alert note %}
Al crear un nuevo usuario con una dirección de correo electrónico, debes añadir `email_encrypted` con el valor del correo electrónico cifrado del usuario. De lo contrario, no se creará el usuario. Del mismo modo, si vas a añadir una dirección de correo electrónico a un usuario existente que no tiene correo electrónico, debes añadir `email_encrypted`. De lo contrario, el usuario no se actualizará.
{% endalert %}

## Consideraciones {#considerations}

Estas características no son compatibles con el cifrado a nivel de campo del identificador:

- Identificar y capturar la dirección de correo electrónico mediante SDK
- Formularios de captura de correo electrónico en mensajes dentro de la aplicación
- Informes sobre el dominio del destinatario, incluidos los gráficos del proveedor de buzón de correo de Email Insights
- Filtrar direcciones de correo electrónico por expresión regular
- Sincronización de audiencia
- Integración con Shopify

### Objeto de atributos del usuario {#user-attributes-object}

Cuando utilices el cifrado a nivel de campo del identificador con el punto de conexión `/users/track`, toma nota de estos detalles de campo para el [objeto de atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens):

- El campo `email` debe ser el valor con hash del correo electrónico.
- El campo `email_encrypted` debe ser el valor cifrado del correo electrónico.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuál es la diferencia entre cifrar y aplicar hash? {#what-is-the-difference-between-encrypting-and-hashing}

El cifrado es una función bidireccional en la que es posible cifrar y descifrar datos. Si el mismo valor de texto plano se cifra varias veces, el algoritmo de cifrado de AWS (AES-256-GCM) producirá valores cifrados diferentes. El hash es una función unidireccional en la que el texto plano se codifica de forma que no se pueda descifrar. El hash produce siempre el mismo valor. Esto nos permite mantener los estados de suscripción de varios usuarios que comparten la misma dirección de correo electrónico.

### ¿Qué dirección de correo electrónico debo utilizar en mi envío de prueba? {#what-email-address-should-i-use-in-my-test-send}

Las direcciones de correo electrónico en texto plano son compatibles con los envíos de prueba. Para ver cómo se ve un correo electrónico para un usuario concreto, haz lo siguiente:

1. Selecciona **Preview message as a user**.
2. En **Test Send**, selecciona **Override recipients attributes with current preview user's attributes**.

{%raw%}
### ¿Qué ocurre si añado esta dirección de correo electrónico Liquid `{{${email_address}}}` en Braze? {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Braze mostrará la dirección de correo electrónico en texto plano al enviar el correo electrónico. En las vistas previas, se mostrará la versión cifrada del correo electrónico. Te recomendamos que utilices el ID externo del usuario si haces referencia a un usuario en una URL personalizada de un clic.

`{{${email_address}}}` no se admite actualmente en el centro de preferencias ni en las páginas para cancelar suscripción.
{%endraw%}

### ¿Qué dirección de correo electrónico debo esperar ver en Currents? {#what-email-address-should-i-expect-to-see-in-currents}

La dirección de correo electrónico con hash se incluye en los eventos de entrega e interacción por correo electrónico.

### ¿Qué dirección de correo electrónico debo esperar ver en el archivado de mensajes? {#what-email-address-should-i-expect-to-see-in-message-archiving}

La dirección de correo electrónico en texto plano se incluye en el archivado de mensajes. Se envían directamente al proveedor de almacenamiento en la nube del cliente y puede haber otros datos personales incluidos en los cuerpos del correo electrónico.

### ¿Puedo utilizar mail-to list-unsubscribe para la gestión de suscripciones con el cifrado a nivel de campo del identificador? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

No. Si utilizas mail-to list-unsubscribe, se enviaría la dirección de correo electrónico descifrada en texto plano a Braze. Con el cifrado a nivel de campo del identificador activado, admitimos el método HTTP basado en URL, incluido el de un clic. También te recomendamos que incluyas un enlace para cancelar suscripción con un solo clic en el cuerpo de tu correo electrónico.

### ¿El cifrado a nivel de campo del identificador admite otros identificadores como el teléfono? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

No. Actualmente, el cifrado a nivel de campo del identificador solo es compatible con las direcciones de correo electrónico.