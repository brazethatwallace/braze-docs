---
nav_title: Autenticación del correo electrónico
article_title: Autenticación del correo electrónico
page_order: 2
page_type: reference
description: "Este artículo de referencia trata sobre la autenticación del correo electrónico, un conjunto de técnicas destinadas a dotar a tu correo electrónico de información verificable sobre su origen."
channel: email

---

# Autenticación del correo electrónico {#email-authentication}

> La autenticación del correo electrónico es un conjunto de técnicas que dotan a tus correos electrónicos de información verificable sobre su origen.<br><br>Una autenticación adecuada es crucial para que los proveedores de servicios de Internet (ISP or proveedor de servicios de Internet) te reconozcan como remitente de correos electrónicos deseados y entreguen tu correo de inmediato. Sin autenticación, se presume que tus comunicaciones son fraudulentas.

{% alert note %}
No se requiere ninguna coordinación especial con Braze para **BIMI** (Brand Indicators for Message Identification). Los registros de DNS y certificados necesarios se gestionan de tu lado.
{% endalert %}

## Métodos de autenticación {#methods-of-authentication}

### Sender Policy Framework (SPF) {#spf}

Este método confirma que la dirección IP de envío de correo electrónico de Braze está autorizada para enviar correo en tu nombre. SPF es tu autenticación básica y se logra publicando los registros de texto en la configuración de DNS. El servidor receptor verificará los registros de DNS y determinará si son auténticos. Este método está diseñado para validar al remitente del correo electrónico.

Braze configura tu registro SPF cuando configuramos tus IP y dominios. Más allá de agregar los registros de DNS que te proporcionamos, no necesitas realizar ninguna acción adicional.

### Domain Keys Identified Mail (DKIM) {#dkim}

Este método confirma que tu dominio de envío de correo electrónico de Braze está autorizado para enviar correo en tu nombre. Este método está diseñado para validar la autenticidad del remitente y valida que se preserve la integridad del mensaje. También utiliza firmas digitales criptográficas individuales para que los ISP or proveedor de servicios de Internet puedan asegurarse de que el correo que están entregando es el mismo que tú enviaste.

Braze firma el correo con tu clave privada secreta. Los ISP or proveedor de servicios de Internet verifican la firma contra tu clave pública, que está almacenada en tu registro de DNS personalizado. No hay dos firmas exactamente iguales, y solo tu clave pública puede verificar con éxito la firma de tu clave privada.

Braze configura tu registro DKIM cuando configuramos tus IP y dominios. Más allá de agregar los registros de DNS que te proporcionamos, no necesitas realizar ninguna acción adicional.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC) {#dmarc}

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) es un protocolo de autenticación de correo electrónico para que los remitentes demuestren la legitimidad de su correo, lo que genera confianza en el receptor del buzón y fomenta la aceptación del correo. DMARC permite a los remitentes de correo electrónico especificar cómo manejar los correos que no fueron autenticados mediante Sender Policy Framework (SPF) o Domain Keys Identified Mail (DKIM). Esto se logra verificando que tanto las comprobaciones de SPF como de DKIM se hayan superado.

Los remitentes instruyen a los proveedores de buzones sobre cómo manejar el correo que no supera las comprobaciones de firma o autenticación. Los fallos pueden indicar suplantación de identidad. Puedes indicar a los proveedores que rechacen o pongan en cuarentena el correo que falle y que envíen informes automatizados. Esto ayuda a los proveedores a identificar emisores de correo no deseado, bloquear correo malicioso, minimizar falsos positivos y mejorar la transparencia de los informes de autenticación.

#### Cómo funciona {#how-it-works}

Para implementar DMARC, necesitas publicar un registro DMARC en tu sistema de nombres de dominio (DNS). Este es un registro TXT que expresa públicamente la política de tu dominio de correo electrónico después de verificar el estado de SPF y DKIM. DMARC autentica si SPF o DKIM, o ambos, se superan. Esto se conoce como alineación DMARC.

Un registro DMARC también indica a los servidores de correo electrónico que envíen informes XML de vuelta a la dirección de correo electrónico de informes indicada en el registro DMARC. Estos informes proporcionan información sobre cómo se mueve tu correo electrónico a través del ecosistema y te permiten identificar todo lo que intenta usar tu dominio de correo electrónico para enviar comunicaciones por correo electrónico.

Establece una política DMARC en el dominio raíz para que se aplique a todos los subdominios. Esto evita configuraciones adicionales en subdominios actuales y futuros. Puedes establecer una de las siguientes políticas:

| Política | Impacto |
| --- | --- |
| None | Indica al proveedor de buzones que no realice ninguna acción contra los mensajes que fallen. |
| Quarantine | Indica al proveedor de buzones que envíe los mensajes que fallen a la carpeta de correo no deseado. |
| Reject | Indica al proveedor de buzones que los mensajes que fallen irán a la carpeta de correo no deseado y deben ser bloqueados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo funciona" }

#### Cómo verificar la autenticación DMARC de tu dominio {#how-to-check-your-domains-dmarc-authentication}

Hay dos opciones para verificar la autenticación DMARC de tu dominio:

- **Opción 1:** Puedes ingresar tu dominio principal o subdominio en cualquier verificador DMARC de terceros, como [MXToolbox](https://mxtoolbox.com/dmarc.aspx), para auditar si tienes una política DMARC implementada y en qué está configurada.
    - **MXToolbox**: Si configuraste tu DMARC como el dominio raíz, ingrésalo en MXToolbox. Si configuraste el DMARC en el subdominio, ingresa el subdominio en MXToolbox. Ten en cuenta que MXToolbox no "busca hacia arriba o hacia abajo" al realizar consultas. Esto significa que si configuraste el DMARC en el dominio raíz e ingresas el subdominio, MXToolbox mostrará un fallo ya que no sabe que el DMARC se ha configurado en el dominio raíz.
- **Opción 2:** Abre un correo electrónico de tu dominio o subdominio en tu buzón y busca el mensaje original para verificar si DMARC está superando la autenticación en ese correo electrónico.

Los pasos varían según el cliente de correo electrónico:

{% tabs %}
{% tab Gmail %}

1. Selecciona **Más** <i class="fa-solid fa-ellipsis"></i> en un mensaje de correo electrónico.
2. Selecciona **Mostrar original**.
3. Verifica si tienes un estado "PASS" para **DMARC**.

![Un correo electrónico que tiene "PASS" como valor de DMARC.]({% image_buster /assets/img_archive/dmarc_example.png %})

{% endtab %}
{% tab Outlook %}

1. Abre el correo electrónico.
2. Selecciona la flecha junto a **Responder**.
3. Selecciona **Mostrar origen del mensaje**.
4. Verifica si tienes un estado "PASS" para **DMARC**.

{% endtab %}
{% tab Apple Mail %}

1. Abre el correo electrónico.
2. Selecciona **Ver** en la barra de menú.
3. Selecciona **Mensaje** > **Código fuente**.
4. Verifica si tienes un estado "PASS" para **DMARC**.

{% endtab %}
{% endtabs %}

#### Solucionar fallos de DMARC {#troubleshoot-dmarc-failures}

Si DMARC muestra **FAIL** para los mensajes enviados a través de Braze:

1. Abre los encabezados sin procesar o los resultados de autenticación de un mensaje reciente y observa si **SPF** y **DKIM** se superan o fallan.
2. **Alineación:** DMARC se supera cuando *SPF* *o* *DKIM* se alinean con el dominio **From**. La alineación significa que el dominio **From** coincide con el dominio que superó SPF (a menudo el dominio **Return-Path** / sobre) *o* el dominio en la firma **d=** de DKIM.
3. Si SPF se supera pero DMARC falla, es posible que el dominio Return-Path no esté alineado con tu dominio **From**; confirma que tus [dominios de envío y seguimiento con marca]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains) coincidan con los dominios para los que publicas SPF y DKIM.
4. Si DKIM falla, verifica que los registros de DNS de DKIM proporcionados por Braze estén presentes y sin modificaciones.

Los verificadores de terceros (por ejemplo, [MXToolbox](https://mxtoolbox.com/dmarc.aspx)) ayudan a confirmar los registros publicados; valida siempre también con un mensaje en vivo de Braze.