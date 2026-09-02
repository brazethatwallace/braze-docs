---
nav_title: Facebook Lead Ads a través de Zapier
article_title: Facebook Lead Ads a través de Zapier
description: "Este artículo de referencia describe la integración entre Braze y Facebook Lead Ads a través de Zapier para automatizar la transferencia de datos de clientes potenciales de Facebook a Braze, lo que permite la interacción en tiempo real y acciones de seguimiento personalizadas."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner
---

# Integración de Facebook Lead Ads a través de Zapier {#facebook-lead-ads-via-zapier-integration}

> Con la integración de Facebook Lead Ads a través de <a href="https://zapier.com/" target="_blank">Zapier</a>, puedes importar tus clientes potenciales de Facebook a Braze y realizar un seguimiento de un evento personalizado cuando se captan clientes potenciales.

Facebook Lead Ads es un formato de anuncio que permite a las empresas recopilar información sobre clientes potenciales directamente en Facebook. Estos anuncios están diseñados para que el proceso de generación de clientes potenciales sea fácil y fluido. Al aprovechar una integración de Zapier y Braze, puedes automatizar la transferencia de datos de clientes potenciales de Facebook a Braze, lo que permite la interacción en tiempo real y acciones de seguimiento personalizadas.

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Cuenta de Zapier | Se requiere una cuenta de Zapier para aprovechar esta integración. Esta integración requiere el uso de <a href="https://zapier.com/app/pricing/" target="_blank">aplicaciones premium de Zapier</a>, así que verifica que tu plan de Zapier tenga acceso a aplicaciones premium. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Acceso a Facebook Leads</a> | Se requiere acceso a Facebook Leads para cada cuenta de anuncios que planees usar con Braze. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Administrador</a> | Usarás Facebook Business Administrador, una herramienta centralizada para gestionar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas y aplicaciones), como parte de esta integración. |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Cuenta de anuncios de Facebook</a> | Necesitarás una cuenta de anuncios de Facebook activa vinculada al administrador de negocios de tu marca. <br><br>Asegúrate de que tengas el permiso "Manage ad accounts" para cada cuenta de anuncios que planees usar con Braze, y de que hayas aceptado los términos y condiciones de tu cuenta de anuncios. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Página de Facebook</a> | Necesitarás una página de Facebook activa vinculada al administrador de negocios de tu marca. <br><br>Asegúrate de que tengas los permisos "Manage Pages" para cada página de Facebook que planees usar con Braze. |
| Endpoint REST de Braze | Asegúrate de conocer tu [URL del endpoint REST]({{site.baseurl}}/api/basics#api-definitions). Tu endpoint de API coincide con la URL del panel para tu instancia de Braze. <br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu endpoint será `dashboard-03`. |
| Clave de API REST de Braze | Asegúrate de tener una clave de API REST de Braze con permisos `users.track`. <br><br> Esto se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crea una Campaign de Lead Ads con un formulario instantáneo {#step-1-create-a-lead-ads-campaign-with-an-instant-form}

Desde Facebook Ads Administrador, crea una <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Campaign de Facebook Leads y un formulario de Facebook Lead Ads</a>.

Puedes utilizar una dirección de correo electrónico o un número de teléfono al realizar una solicitud al [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para actualizar o crear el perfil de usuario. Por este motivo, incluye un **campo de contacto** para **correo electrónico** o **teléfono** en tu formulario de anuncio de leads. Si recopilas nombres o apellidos, recógelos por separado en tu formulario en lugar de utilizar nombres completos.

### Paso 2: Conecta tu cuenta de Facebook a Zapier {#step-2-connect-your-facebook-account-to-zapier}

#### Paso 2a: Selecciona tu método de conexión en Zapier {#step-2a-select-your-connection-method-in-zapier}

En Zapier, ve a **Apps** para buscar las aplicaciones de Facebook disponibles. Selecciona **Facebook Lead Ads** o **Facebook Lead Ads (for Business admins)**.

Para obtener más información sobre estos dos métodos de conexión de tu cuenta de Facebook a Zapier, consulta:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![Búsqueda de aplicaciones en Zapier mostrando las opciones de conexión de Facebook Lead Ads.]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Paso 2b: Añade Zapier al acceso de leads en Facebook Business Administrador {#step-2b-add-zapier-to-leads-access-in-facebook-business-manager}

En tu Facebook Business Administrador, ve a **Integrations** > **Leads Access** en el menú de navegación. Selecciona tu página de Facebook y luego haz clic en **CRMs**. En la pestaña CRM, selecciona **Assign CRMs** y añade **Zapier**.

![Página de acceso de leads de Facebook Business Manager con Zapier asignado como integración de CRM.]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Para conocer los pasos para asignar Zapier como una integración de CRM, consulta la <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">documentación</a> de Facebook.

### Paso 3: Crea tu Zap {#step-3-create-your-zap}

#### Paso 3a: Crea el desencadenador {#step-3a-create-the-trigger}

Una vez que hayas conectado tu cuenta de Facebook, puedes proceder a crear un Zap. Para el **desencadenador**, selecciona **Facebook Lead Ads** o **Facebook Lead Ads (for Business Admins)** según tu elección del paso 2.

![Paso de desencadenador en Zapier con Facebook Lead Ads seleccionado.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

Para el **evento**, selecciona **New Leads** > **Continue**.

![Selección de evento del desencadenador en Zapier mostrando New Leads.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Selecciona tu cuenta de Facebook y luego **Continue**.

![Paso de conexión de cuenta de Facebook en Zapier para el desencadenador.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Selecciona tu página de Facebook y el formulario instantáneo que creaste previamente, y luego **Continue**.

![Configuración del desencadenador en Zapier seleccionando una página de Facebook y un formulario instantáneo.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

A continuación, prueba este desencadenador. Después de validar la salida de tu formulario, selecciona **Continue with selected record**.

#### Paso 3b: Crea una acción {#step-3b-create-an-action}

Añade un nuevo paso y selecciona **Webhooks by Zapier**. A continuación, selecciona **Custom Request** para el campo **Event** y haz clic en **Continue**.

![Paso de acción en Zapier configurado con Webhooks by Zapier y Custom Request.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Por último, configura tu solicitud personalizada insertando campos en tu carga útil. El siguiente fragmento de código muestra un ejemplo de carga útil.

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Aquí tienes un ejemplo de cómo se ve esto en Zapier:

![Ejemplo de mapeado de carga útil del webhook en Zapier para enviar campos de leads de Facebook a Braze.]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

Después de configurar tu webhook, selecciona **Continue and test**. Si la prueba es exitosa, puedes publicar tu Zap.

### Paso 4: Prueba tu Zap de Facebook Lead Ads {#step-4-test-your-facebook-lead-ads-zap}

Para probar esto de extremo a extremo, utiliza la herramienta de pruebas de Lead Ads de Facebook en tu consola para desarrolladores de Facebook. Para obtener más información, consulta <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testing and Troubleshooting</a>.

## Gestión de identidad de usuario {#user-identity-management}

Esta integración te permite atribuir tus clientes potenciales de Facebook por correo electrónico a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number).

* Si el correo electrónico coincide con un perfil de usuario existente, Braze actualizará el perfil con los datos de clientes potenciales de Facebook.
* Si hay varios perfiles de usuario con el mismo correo electrónico, Braze dará prioridad al perfil actualizado más recientemente que tenga un ID externo.
* Si el ID externo no existe, Braze dará prioridad al perfil actualizado más recientemente con el correo electrónico coincidente.
* Si no existe ningún perfil con el correo electrónico proporcionado, Braze creará un nuevo perfil y se creará un nuevo perfil de usuario alias. Para identificar los perfiles de usuario alias recién creados, utiliza el [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

{% alert note %}
También puedes utilizar un número de teléfono o un ID externo como parte de la solicitud a Braze si esos campos están disponibles y son el identificador principal que deseas usar para la integración. Para hacerlo, modifica tu carga útil de solicitud como se indica en el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).
{% endalert %}

## Solución de problemas {#troubleshooting}

{% details Probé el desencadenador y la acción con éxito, entonces ¿por qué no puedo publicar mi Zap de Zapier? %}
Para utilizar esta integración, debes tener un <a href="https://zapier.com/app/pricing/" target="_blank">plan de Zapier</a> que sea compatible con aplicaciones premium.
{% enddetails %}

{% details ¿Por qué los leads de Facebook no se sincronizan con Braze? %}
1. Comprueba que tienes acceso de administrador a tu página de Facebook, cuenta publicitaria y acceso a leads. Luego, vuelve a conectar tu cuenta en Zapier.
2. Verifica que el formulario instantáneo que creaste en Facebook coincida con el formulario seleccionado en tu paso de desencadenador.
3. Comprueba que has asignado Zapier al acceso a leads yendo a **Facebook Business Administrador** > **Integrations** > **Lead Access**.
{% enddetails %}

{% details ¿Por qué veo perfiles de usuario duplicados con el mismo correo electrónico? %}
Existen formas únicas de crear y gestionar perfiles de usuario en Braze según su [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).

Dependiendo de tus procesos internos y de cuándo estás desencadenando la creación de clientes en Braze, podrías encontrar perfiles de usuario duplicados debido a una condición de carrera entre la creación del perfil de usuario por la integración y el momento en que el usuario se crea desde tu sistema. Puedes [fusionar perfiles de usuario]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) en Braze.
{% enddetails %}

{% details No tengo una cuenta de Zapier. ¿Cómo puedo desencadenar webhooks de Facebook Lead Ads en Braze? %}
Si no usas Zapier y no planeas usarlo, puedes crear la integración directamente desde Facebook hacia Braze. Consulta la <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">documentación de Lead Ads</a> para obtener más información.

Para recuperar leads de Facebook, usa <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhooks</a>. Consulta la <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">documentación de webhooks</a> para empezar a usar webhooks en Facebook.

Después de establecer la URL de webhooks en Facebook, trabaja con tu equipo para determinar la mejor ruta para reenviar los datos al [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). De forma similar al enfoque de Zapier, recomendamos hacer una [solicitud por correo electrónico]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number) a través del endpoint `users/track`.
{% enddetails %}

{% alert tip %}
Para más consejos de solución de problemas, consulta la <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">guía de solución de problemas de leads de Facebook</a> de Zapier.
{% endalert %}