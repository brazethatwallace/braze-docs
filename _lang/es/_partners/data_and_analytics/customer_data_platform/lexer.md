---
nav_title: Lexer
article_title: Lexer
description: "Este artículo de referencia describe la asociación entre Braze y Lexer, una CDP or plataforma de datos de los clientes or plataforma de datos de los clientes que pone los datos de los clientes en manos de los especialistas en marketing para inspirar experiencias que impulsen las ventas."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/), una CDP or plataforma de datos de los clientes or plataforma de datos de los clientes creada para el comercio minorista, ayuda a las marcas a impulsar ventas incrementales mediante la mejora de la experiencia del cliente, combinando un sólido enriquecimiento de datos con las herramientas más intuitivas y el asesoramiento de expertos.

_Esta integración está mantenida por Lexer._

## Sobre la integración {#about-the-integration}

La integración de Braze y Lexer te permite sincronizar datos entre las dos plataformas. Usa tus datos de Lexer para crear segmentos valiosos en Braze o importa los existentes a Lexer para obtener información.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de partner | Se necesita una cuenta de Lexer para aprovechar esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con todos los permisos de `user` (excepto `user.delete`) y permisos de `segment.list`. El conjunto de permisos puede cambiar a medida que Lexer añada compatibilidad con más objetos de Braze, por lo que es posible que quieras conceder más permisos ahora o planificar la actualización de estos permisos en el futuro.<br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze | La [URL de tu endpoint REST or transferencia de estado representacional]({{site.baseurl}}/api/basics#endpoints). Tu endpoint dependerá de la URL de Braze de tu instancia. |
| Contenedor y credenciales de Amazon AWS S3 | Antes de comenzar la integración, debes tener credenciales de acceso para un contenedor de AWS S3 conectado a tu hub de Lexer (puede ser un contenedor creado por ti o uno que Lexer cree y gestione por ti). Visita [Lexer](https://learn.lexer.io/docs/amazon-s3) para obtener orientación sobre este requisito. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

En Lexer, ve a **Manage > Integration**, selecciona el mosaico **Braze** y haz clic en **Integrate Braze**. Proporciona la siguiente información:
- **Braze REST or transferencia de estado representacional endpoint**
- **Braze REST or transferencia de estado representacional API key**
- **AWS Credentials**
  - **AWS S3 bucket name**
  - **AWS S3 [bucket region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 bucket path**: Esta ruta debe coincidir con la que especificaste al [conectar tu contenedor de S3 a Braze]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3). Debe estar en blanco si no especificaste nada a Braze.
  - **AWS S3 secret access key**: Visita Amazon para obtener información sobre cómo [crear una clave de acceso](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/).
- **Braze export segment ID**: El ID del segmento que creaste en Braze que contiene todos los usuarios que deseas exportar a Lexer. Si hay usuarios que no deseas exportar a Lexer, puedes excluirlos del segmento que creaste en Braze. Para encontrar tu identificador de segmento, haz clic en el segmento deseado en Braze y localiza el **Segment API Identifier**.

![Pantalla de integración de Lexer que muestra los campos de integración de Braze para la URL de la API, la clave de API, los detalles del contenedor de AWS S3 y el ID de segmento de exportación de Braze.]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### Elección de una opción de AWS S3 (gestionada por Lexer o autogestionada) {#choosing-an-aws-s3-option-lexer-managed-or-self-managed}
Usar un contenedor gestionado por Lexer es la forma preferida de conectar Braze a tu hub de Lexer y reduce la cantidad de configuración necesaria. Lexer te proporcionará los detalles puntuales que necesitas para configurar Braze.

Si ya conectaste un contenedor de S3 a Braze y lo estás utilizando para otros fines, tendrás que proporcionar a Lexer acceso a este contenedor autogestionado siguiendo los pasos anteriores.

Esta integración funciona proporcionando a Lexer tu token de API y secretos existentes, lo que permite a Lexer realizar estas exportaciones en tu nombre. También importa tus datos de Braze a Lexer utilizando estas credenciales y tu configuración de S3 para sincronizar tus datos en ambas plataformas de forma automática.

## Envío de segmentos a Braze {#sending-segments-to-braze}

### Paso 1: Crear activación {#step-1-create-activation}

Lexer Activate actualizará automáticamente tus perfiles de Braze, añadiendo o eliminando atributos a medida que los clientes entren y salgan de tu segmento.

1. En Lexer, en **Lexer Activations**, haz clic en **ACTIVATE NEW AUDIENCE**.
2. Selecciona la activación de Braze adecuada para esta campaña.
3. Añade tu segmento.
4. Actualiza el nombre de tu audiencia; este se convertirá en el valor de tu atributo en Braze.
5. Este es el atributo personalizado que se actualizará en Braze. Ponte en contacto con [el soporte de Lexer](mailto:support@lexer.io) para actualizarlo.
6. Marca la acción apropiada de la lista; en la mayoría de los casos, querrás mantener tu lista.
7. Revisa los términos y condiciones y haz clic en **SEND AUDIENCE**.

![Flujo de trabajo de Lexer Activate que muestra la selección del canal de activación, la creación de audiencia y los detalles de activación antes de enviar una audiencia a Braze.]({% image_buster /assets/img/lexer/lexer.png %})

### Paso 2: Verificar la activación {#step-2-verify-activation}

Una vez que se haya confirmado el envío de tu activación en Activate, verás que los registros comienzan a actualizarse en Braze. Tus perfiles no se actualizarán completamente en Braze hasta después de recibir un correo electrónico de confirmación de Lexer.

### Paso 3: Crea tu segmento en Braze {#step-3-create-your-braze-segment}

En Braze, verás que el nombre de tu audiencia en Lexer es ahora un valor en tu atributo personalizado `lexer_audience`. Braze tiene un límite de 100 valores por atributo.

Para crear tu segmento, ve a **Segments > + Create Segment** y selecciona **Custom Attribute** como filtro. A continuación, selecciona `lexer_audience` como tu atributo y el nombre de la audiencia de Lexer que desees. Cuando hayas terminado, **guarda** tu audiencia.

Ahora puedes añadir este segmento recién creado a futuras Campaigns y Canvas de Braze para dirigirte a estos usuarios finales.