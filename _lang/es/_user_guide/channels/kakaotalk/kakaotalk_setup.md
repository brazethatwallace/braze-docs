---
nav_title: Configurar KakaoTalk
article_title: Configurar KakaoTalk
description: "Este artículo de referencia describe cómo configurar tu canal de KakaoTalk, incluyendo cómo configurar usuarios, conciliar ID de usuario y crear usuarios de prueba."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# Configurar KakaoTalk {#set-up-kakaotalk}

> Este artículo cubre cómo configurar el [canal de mensajería KakaoTalk]({{site.baseurl}}/kakaotalk) en Braze, incluyendo cómo configurar usuarios, conciliar ID de usuario y crear usuarios de prueba de KakaoTalk.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta con un partner de KakaoTalk compatible | Se requiere una cuenta con un partner de KakaoTalk compatible, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) o [Infobip](https://marketplace.braze.com/partners/infobip), para usar el canal de mensajería de KakaoTalk. |
| Canal de negocios de KakaoTalk | Tu cuenta de KakaoTalk debe ser un canal de negocios de KakaoTalk para enviar mensajes de KakaoTalk a través de Braze. Cuando creas una cuenta, su estado predeterminado es básico. Para convertir tu cuenta en un canal de negocios, deberás verificar tu empresa y proporcionar la documentación pertinente. |
| Clave de remitente de KakaoTalk | Una clave de remitente de KakaoTalk válida. |
| Número de teléfono de contacto | Un número de teléfono de contacto para el administrador de tu canal de KakaoTalk. |
| IP del clúster de Braze en la lista de permitidos | El registro en la lista de IP permitidas es obligatorio para todos los clientes. Registra las direcciones IP de Braze para tu clúster antes de integrar KakaoTalk en Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

### Registrar las direcciones IP de Braze {#register-braze-ip-addresses}

Registra las direcciones IP de Braze para tu clúster en tu panel de Comm.One.

1. En tu panel de Comm.One, ve a **Account Management (계정 관리)**, selecciona el icono de menú y luego selecciona **View Details (자세히보기)**.
2. Selecciona **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)**.
3. Agrega las direcciones IP de tu clúster de Braze. Para la lista completa de IP por clúster, consulta [Lista de IP permitidas]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting).

![Panel de Comm.One que muestra dónde puedes agregar direcciones IP.]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### Tipos de cuentas de KakaoTalk {#types-of-kakaotalk-accounts}

| Tipo de cuenta | Descripción |
| --- | --- |
| Canal básico | Un canal estándar de KakaoTalk que cualquier organización puede configurar. Permite mensajería de difusión y chat 1:1 a través de KakaoTalk. |
| [Canal de negocios](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Un canal de KakaoTalk mejorado y verificado para empresas que requiere un proceso de solicitud y verificación. Ofrece características mejoradas, como {::nomarkdown}<ul><li>Señal de verificación</li><li>Aparición como canal recomendado</li><li>Soporte para mensajería empresarial</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de cuentas de KakaoTalk" }

#### Solicitar un canal de negocios {#apply-for-a-business-channel}

Antes de iniciar la solicitud, reúne la siguiente documentación empresarial:
- Certificado de registro empresarial coreano
- Identificación del representante de la empresa
- Certificado de empleo
- Licencias específicas del sector

{% alert important %}
La información de tu canal de KakaoTalk (como el nombre del canal, la imagen de perfil y otros datos) debe coincidir exactamente con la información de tus documentos oficiales presentados.
{% endalert %}

Después de reunir tu documentación, sigue estos pasos:

1. Inicia sesión en el [Centro de administración de canales de KakaoTalk](https://center-pf.kakao.com/).
2. Selecciona el canal de KakaoTalk existente que deseas actualizar.
3. En la sección **Management (관리)**, selecciona la opción **Business Channel Application (비즈니스 채널 신청)**.
4. Selecciona el botón **Apply** o **Request (신청)** para iniciar el proceso.
5. Proporciona la información requerida.
6. Espera una notificación con los resultados de la revisión.

## Integrar KakaoTalk {#integrate-kakaotalk}

### Paso 1: Conectar el canal de KakaoTalk a Braze {#step-1-connect-the-kakaotalk-channel-to-braze}

1. Ve a **Partner Integrations** > **Technology Partners** y selecciona tu proveedor de KakaoTalk.
2. Reúne las credenciales necesarias para tu proveedor (consulta la siguiente sección), luego introdúcelas en la página de **Technology Partners** y guarda.
3. Usa las credenciales recién guardadas para el envío.

#### CJ OliveNetworks

Ve a tu [panel de Comm.One](https://ums.cjmplace.com/) y reúne la siguiente información.

| Campo | Ubicación |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Selecciona tu perfil. |
| **Sender Key (발신프로필 키)** | Ve a **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | En tu panel de Comm.One, ve a **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Ve a <b>Account Management (계정 관리)</b>, selecciona el icono de menú y luego selecciona <b>View Details (자세히보기)</b>.</li><li>Ve a <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Ve a la misma ubicación del **Sender number (사업자 등록번호)**, luego ve a **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Panel de Comm.One mostrando un ID de inicio de sesión censurado.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Panel de Comm.One mostrando una Sender Key censurada.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
Solo puedes integrar una Sender Key de KakaoTalk en un espacio de trabajo a la vez. Para usar la misma Sender Key en un espacio de trabajo diferente, primero debes archivar el grupo de suscripción de KakaoTalk en el espacio de trabajo original y luego contactar a [soporte de Braze]({{site.baseurl}}/braze_support) para eliminar la integración. Después de que Braze elimine la integración, puedes configurar la integración en el nuevo espacio de trabajo.
{% endalert %}

![Credenciales para un canal de KakaoTalk en Braze.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Panel de Comm.One mostrando un nombre de canal censurado.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Panel de Comm.One mostrando un ID de credencial y contraseña censurados.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Solo se pueden registrar los canales mapeados a un único ID común.
{% endalert %}

![Campos en la página de Technology Partners para CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Ve a tu panel de Infobip y reúne la siguiente información.

| Campo | Ubicación |
| --- | --- |
| **API Base URL** | Selecciona **Developer Tools** > **API Keys**. |
| **API Key** | Selecciona **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | Selecciona **Channels and Numbers** > **Channels**, luego selecciona la pestaña **Senders**. |
| **Sender profile UUID** | Proporcionado directamente por Infobip. Contacta a Infobip si no tienes esta información. |
| **Channel name** | Proporcionado directamente por Infobip. Contacta a Infobip si no tienes esta información. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

## Configurar perfiles de usuario {#set-user-profiles}

Los perfiles de usuario deben tener números de teléfono en formato E.164 para enviarles mensajes a través de KakaoTalk. Los números de teléfono se muestran en el perfil de usuario. KakaoTalk requiere que los números de teléfono estén en formato E.164 (por ejemplo, `+821025749774`). Esto difiere de otros canales de mensajería que pueden aceptar números de teléfono en múltiples formatos.

### Importar números de teléfono {#import-phone-numbers}

Importa números de teléfono [cargando un CSV o usando la API]({{site.baseurl}}/user_guide/data/unification/user_data/import_users) para crear un usuario. Asegúrate de que los números de teléfono estén en formato E.164 antes de importarlos.