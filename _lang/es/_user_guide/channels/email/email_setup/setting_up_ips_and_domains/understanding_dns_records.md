---
nav_title: Comprender los registros de DNS
article_title: Comprender los registros de DNS
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo funcionan los registros de DNS en los proveedores de servicios de correo electrónico de Braze, incluidos SPF, DKIM, DMARC y las estructuras de registros específicas de cada ESP."
channel: email
---

# Comprender los registros de DNS {#understanding-dns-records}

> Esta referencia explica cómo funcionan los registros de DNS dentro de Braze en tres proveedores de servicios de correo electrónico (ESP) principales: SparkPost, SendGrid y Amazon Simple Email Service (SES). Una configuración de DNS adecuada es esencial para la autenticación de correo electrónico (SPF, DKIM, DMARC) y la alineación de marca, y afecta directamente a la capacidad de entrega.

Para más información, consulta [Autenticación de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).

## Fundamentos de la autenticación de correo electrónico {#core-email-authentication-fundamentals}

Antes de revisar las estructuras específicas de cada proveedor, es importante entender qué hacen estos registros y cómo Braze los utiliza para lograr una alineación adecuada.

### Sender Policy Framework (SPF) {#spf}

SPF es un registro de DNS en un dominio que especifica qué direcciones IP están autorizadas para enviar correo electrónico en nombre de ese dominio.

Braze no te pide que modifiques ni añadas registros SPF en tu dominio raíz corporativo (como `example.com`). En su lugar, Braze aísla la entrega utilizando un dominio Return-Path dedicado y personalizado (también conocido como dominio de rebote, dominio MAIL FROM o dominio de sobre From), como `bounce.mail.example.com`.

Dado que los proveedores de buzón de entrada receptores validan SPF contra este dominio Return-Path en lugar del dominio visible en el encabezado `From:`, la configuración de SPF reside completamente a nivel de subdominio. Dependiendo del ESP subyacente, Braze gestiona esta validación de una de dos maneras:

- Delegación CNAME (SendGrid y SparkPost): crea un `CNAME` que apunte tu subdominio de vuelta al ESP. El ESP aloja y actualiza las políticas SPF en su infraestructura, pasando la verificación SPF automáticamente.
- Registro TXT explícito (Amazon SES): publica un registro `TXT` codificado directamente en el subdominio de rebote que contenga una cadena de autorización explícita (por ejemplo, `v=spf1 include:amazonses.com ~all`), otorgando a AWS permiso para enviar correo desde esa zona.

### Domain Keys Identified Mail (DKIM) {#dkim}

DKIM añade una firma digital criptográfica al encabezado del correo electrónico. El servidor receptor utiliza la clave pública del remitente (publicada en DNS) para verificar que el correo electrónico se originó del propietario del dominio y no fue alterado en tránsito.

Braze requiere que las claves públicas DKIM se publiquen a través de registros `TXT` o `CNAME` para que los ISP receptores puedan validar las firmas criptográficas generadas por tu ESP.

### Alineación DMARC {#dmarc}

Para que un correo electrónico pase DMARC, el dominio en el encabezado `From:` visible para el usuario debe coincidir (alinearse) con el dominio validado por SPF (el Return-Path) o DKIM. Dado que las configuraciones de Braze logran la alineación a través de SPF y DKIM, tus políticas DMARC se satisfacen de forma segura.

Braze gestiona la autenticación SPF y DKIM básica de forma predeterminada, pero aún necesitas añadir un registro DMARC a tu dominio de envío. DMARC es una herramienta de autenticación esencial requerida por casi todos los principales proveedores de buzón de entrada. Demuestra que tus correos electrónicos son legítimos, fortalece la reputación de tu dominio y mantiene tu capacidad de entrega saludable a lo largo del tiempo.

Dado que esto requiere acceso al registro de dominio de tu empresa, tú o tu administrador de red necesitan añadir este registro a nivel de dominio raíz. Si estás comenzando, una política básica como `p=none` satisface los requisitos mínimos de los buzones de entrada. Para más información sobre DMARC, consulta [DMARC.org](https://dmarc.org/). Para orientación específica de Braze sobre DMARC, consulta [Autenticación de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc).

## Arquitectura de DNS específica del ESP {#esp-specific-dns-architecture}

Las diferentes arquitecturas de ESP gestionan la delegación de DNS de forma distinta. Al aprovisionar tu entorno, utiliza los registros exactos mapeados a tu clúster de ESP específico.

### Arquitectura de SparkPost {#sparkpost-architecture}

SparkPost utiliza una configuración híbrida. Emplea registros `CNAME` explícitos para apuntar la infraestructura de seguimiento y Return-Path de vuelta a SparkPost, mientras usa un registro `TXT` sin procesar para la autenticación DKIM.

- Configuración de SPF y Return-Path: SparkPost solicita un subdominio designado para rebotes (por ejemplo, `mail.example.com`). Un registro `CNAME` apunta este subdominio a los procesadores de rebotes entrantes de SparkPost. Esto enruta el tráfico de rebotes correctamente y valida SPF automáticamente porque el servidor de destino de SparkPost gestiona el protocolo.
- Configuración de DKIM: SparkPost requiere un registro `TXT` que contenga la cadena exacta de clave pública mapeada a un SELECTOR específico.
- Seguimiento de clics y aperturas: Configura un subdominio de seguimiento con un `CNAME` que apunte a los endpoints de seguimiento de SparkPost (o un proxy CDN si se solicita seguimiento SSL).

#### Tabla de DNS de ejemplo de SparkPost {#example-sparkpost-dns-table}

La siguiente tabla muestra registros de DNS de ejemplo para una configuración de SparkPost.

| Tipo de registro | Host/Nombre | Valor/Destino | Propósito |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Alineación de Return-Path / SPF |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | Autenticación criptográfica DKIM |
| CNAME | click.mail.example.com | spgo.io (o endpoint CDN) | Seguimiento de clics y aperturas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabla de DNS de ejemplo de SparkPost" }

### Arquitectura de SendGrid {#sendgrid-architecture}

SendGrid se basa en una infraestructura automatizada conocida como autenticación de dominio. En lugar de proporcionar claves `TXT` sin procesar, SendGrid proporciona una serie de registros `CNAME` que apuntan directamente a los servidores gestionados por SendGrid.

- Configuración de SPF y Return-Path: SendGrid utiliza un `CNAME` específico (a menudo con el prefijo `em`) que mapea tu subdominio de envío a `uXXXXXX.wl.sendgrid.net`. SendGrid aloja y actualiza dinámicamente el registro SPF en ese endpoint.
- Configuración de DKIM: SendGrid genera dos registros `CNAME` separados para DKIM (a menudo usando selectores como `s1` y `s2`). Estos apuntan de vuelta a las claves de SendGrid.
- SendGrid proporciona dos registros `CNAME` de DKIM para poder rotar las claves criptográficas automáticamente sin requerir que actualices tu DNS manualmente.

#### Tabla de DNS de ejemplo de SendGrid {#example-sendgrid-dns-table}

La siguiente tabla muestra registros de DNS de ejemplo para una configuración de SendGrid.

| Tipo de registro | Host/Nombre | Valor/Destino | Propósito |
| --- | --- | --- | --- |
| CNAME | em.mail.example.com | u123456.wl.SendGrid.net | Return-Path / SPF dinámico |
| CNAME | s1._domainkey.mail.example.com | s1.domainkey.u123456.wl.SendGrid.net | Clave DKIM primaria (rotativa) |
| CNAME | s2._domainkey.mail.example.com | s2.domainkey.u123456.wl.SendGrid.net | Clave DKIM secundaria (rotativa) |
| CNAME | email.mail.example.com | SendGrid.net (o endpoint CDN) | Seguimiento de clics y aperturas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabla de DNS de ejemplo de SendGrid" }

### Arquitectura de Amazon SES {#amazon-ses-architecture}

Amazon SES utiliza Easy DKIM con registros `CNAME` junto con enrutamiento explícito de `MX` y `TXT` para el seguimiento personalizado de rebotes.

- Configuración de DKIM: Amazon SES utiliza Easy DKIM, proporcionando tres registros `CNAME`. Estos apuntan a subdominios gestionados por AWS que contienen las claves públicas. SES rota automáticamente estas claves de forma transparente para mantener el cumplimiento de seguridad.
- Configuración de SPF y MAIL FROM personalizado: SendGrid y SparkPost gestionan el enrutamiento del dominio de rebotes a través de un `CNAME`. Amazon SES requiere un registro `MX` explícito y un registro `TXT` colocados directamente en el subdominio MAIL FROM designado. El registro `MX` asegura que los avisos de rebote regresen a los servidores de Amazon, y el registro `TXT` contiene la cadena SPF autorizada codificada.

Para más información, consulta [Configuración de Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).

#### Tabla de DNS de ejemplo de Amazon SES {#example-amazon-ses-dns-table}

La siguiente tabla muestra registros de DNS de ejemplo para una configuración de Amazon SES.

| Tipo de registro | Host/Nombre | Valor/Destino | Propósito |
| --- | --- | --- | --- |
| CNAME | sel1._domainkey.mail.example.com | sel1.dkim.amazonses.com | Clave Easy DKIM 1 (rotativa) |
| CNAME | sel2._domainkey.mail.example.com | sel2.dkim.amazonses.com | Clave Easy DKIM 2 (rotativa) |
| CNAME | sel3._domainkey.mail.example.com | sel3.dkim.amazonses.com | Clave Easy DKIM 3 (rotativa) |
| MX | bounce.mail.example.com | 10 feedback-smtp.us-east-1.amazonses.com | Enruta el procesamiento de rebotes a AWS |
| TXT | bounce.mail.example.com | v=spf1 include:amazonses.com ~all | Autorización SPF explícita |
| CNAME | track.mail.example.com | r.us-east-1.awstrack.me (o CDN) | Seguimiento de clics y aperturas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabla de DNS de ejemplo de Amazon SES" }

## Consideraciones avanzadas de DNS {#advanced-dns-considerations}

### División de cadenas de registros TXT DKIM {#txt-dkim-record-string-splitting}

Al implementar SparkPost o configuraciones manuales de DKIM, es posible que encuentres claves criptográficas largas (claves DKIM de 2048 bits).

La especificación principal de DNS (RFC 1035) limita cualquier cadena de caracteres individual dentro de un registro `TXT` a un máximo de 255 caracteres. Una clave pública de 2048 bits supera habitualmente los 400 caracteres, lo que provoca que los registros de dominio rechacen la cadena única o la trunquen, invalidando la firma.

La división de cadenas resuelve este problema. Divide la cadena de caracteres en fragmentos de menos de 255 caracteres. Encierra cada fragmento entre comillas rectas, separados por un espacio, dentro del mismo registro `TXT`.

{% alert note %}
Cuando usas proveedores de DNS como Cloudflare o AWS Route 53, estas interfaces gestionan automáticamente la división cuando pegas una cadena larga. Los sistemas heredados (como GoDaddy o Network Solutions) requieren que formatees manualmente la división usando la técnica de comillas dobles.
{% endalert %}

### Usa subdominios dedicados {#dedicated-subdomains}

Un error común durante la incorporación es solicitar el uso de un dominio organizacional de nivel superior (como `example.com`) directamente en Braze como dominio de envío. Braze requiere el uso de un subdominio dedicado (por ejemplo, `mail.example.com` o `engage.example.com`).

Usar el dominio principal puede afectar la infraestructura corporativa de las siguientes maneras:

#### Conflictos de registros MX {#mx-record-conflicts}

Un dominio solo puede admitir un conjunto de registros `MX` de enrutamiento principal. Si mapeas tu dominio principal (`example.com`) a la infraestructura del ESP de Braze, los registros `MX` personalizados necesarios para los rebotes sobrescriben tus registros de correo electrónico corporativo. Esto puede interrumpir las plataformas de mensajería interna corporativa como Google Workspace o Microsoft 365.

#### Exceso de includes SPF y el límite de 10 búsquedas {#spf-include-bloat-and-the-10-lookup-limit}

La especificación SPF (RFC 7208) limita a los servidores de correo receptores a un máximo de 10 búsquedas de DNS al validar un registro SPF.

- Si un dominio principal añade los mecanismos del ESP de Braze (`include:sparkpostmail.com` o `include:amazonses.com`), esto cuenta significativamente contra ese límite.
- Si se excede el límite, se desencadena un PermError permanente de SPF, lo que provoca que todos los correos electrónicos corporativos fallen en la autenticación.

#### Aislamiento de reputación de IP y dominio {#ip-and-domain-reputation-isolation}

Si las Campaigns de marketing, los recibos transaccionales y los correos electrónicos internos de empleados comparten un espacio de dominio raíz idéntico, un aumento repentino en las quejas de correo no deseado de marketing puede dañar la reputación del dominio principal. Esto pone en riesgo que las comunicaciones corporativas críticas se dirijan a las carpetas de correo no deseado. Usar un subdominio distinto aísla la reputación de tu alcance de marketing.

## Flujo de trabajo de implementación {#implementation-workflow}

Para garantizar una transición e implementación sin problemas, sigue esta secuencia:

1. Proporciona los registros estructurados a tu administrador de TI o de red para que los agregue a tu plataforma de alojamiento (Cloudflare, Route 53, etc.).
2. Establece un valor bajo de TTL (TTL) (por ejemplo, 300 segundos o cinco minutos) para las pruebas iniciales. Esto permite una recuperación rápida si se comete un error tipográfico durante la entrada.
3. Ejecuta una búsqueda de DNS (por ejemplo, `dig CNAME mail.example.com`) o usa una herramienta de validación para confirmar que los registros se resuelven correctamente antes de pasar a la fase de calentamiento.

## Documentación de proveedores de DNS {#dns-provider-documentation}

Cada proveedor de DNS tiene una interfaz única. Comparte estas especificaciones con tu administrador de red o consulta la documentación de tu proveedor específico para mapear las entradas correctamente en tu archivo de zona.

La siguiente tabla enumera la documentación oficial de los proveedores de DNS más utilizados.

| Proveedor de DNS | Recursos |
| --- | --- |
| Cloudflare | [Gestionar registros de DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [Crear conjuntos de registros de recursos](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [Gestionar registros de DNS](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [Configurar registros de DNS para un nombre de dominio](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [Gestionar registros de DNS mediante el portal de Azure](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Documentación de proveedores de DNS" }

Para obtener recursos adicionales sobre proveedores de dominios, consulta [Configurar IPs y dominios]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-2-add-and-verify-a-sending-domain).