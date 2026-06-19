---
nav_title: Mozart Data
article_title: Mozart Data
description: "Este artículo de referencia describe la asociación entre Braze y Mozart Data, una plataforma de datos moderna todo en uno, que te permite utilizar Fivetran para importar datos a Snowflake, crear transformaciones, combinar datos y mucho más."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) es una moderna plataforma de datos todo en uno impulsada por Fivetran, Portable y Snowflake.

La integración de Braze y Mozart Data te permite:
- Utilizar Fivetran para importar datos de Braze a Snowflake
- Crear transformaciones combinando datos de Braze con datos de otras aplicaciones y analizar eficazmente los comportamientos de los usuarios
- Importar datos de Snowflake a Braze para crear nuevas oportunidades de interacción con los clientes
- Combinar los datos de Braze con los de otras aplicaciones para obtener una comprensión más holística de los comportamientos de los usuarios
- Integrarlo con una herramienta de inteligencia empresarial para explorar más a fondo los datos almacenados en Snowflake

## Requisitos previos {#prerequisites}

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Mozart Data | Se necesita una cuenta de Mozart Data para beneficiarse de esta asociación. [Regístrate aquí.](https://app.mozartdata.com/signup)|
| Cuenta Snowflake<br>Opción 1: Cuenta nueva | Selecciona **Create a New Snowflake Account** durante el proceso de creación de la cuenta de Mozart Data para que Mozart Data te facilite una nueva cuenta de Snowflake. |
| Cuenta Snowflake<br>Opción 2: Cuenta existente | Si tu organización ya tiene una cuenta Snowflake, puedes utilizar la opción Mozart Data Connected.<br><br>Selecciona la opción **Already Have a Snowflake Account** para conectar una cuenta Snowflake existente. Para seguir esta opción, un usuario con permisos a nivel de cuenta debe [seguir estos pasos](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

La integración es compatible tanto para sincronizar datos de [Braze con Mozart Data](#syncing-data-from-braze-to-mozart-data) como [de Mozart Data con Braze](#syncing-data-from-mozart-data-to-braze).

### Sincronizar datos de Braze con Mozart Data {#syncing-data-from-braze-to-mozart-data}

#### Paso 1: Configurar el conector de Braze {#step-1-set-up-braze-connector}

1. En Mozart Data, ve a **Connectors** y haz clic en **Add Connector**.
2. Busca "Braze" y selecciona la tarjeta del conector.
3. Introduce un nombre de esquema de destino donde se almacenarán todos los datos sincronizados de Braze. Recomendamos utilizar el nombre predeterminado del esquema `braze`.
4. Haz clic en **Add Connector**.

#### Paso 2: Rellena el formulario del conector de Fivetran {#step-2-fill-out-the-fivetran-connector-form}

Se te redirigirá a la página del conector de Fivetran. En esta página, rellena los campos indicados. A continuación, haz clic en **Continue** > **Save & Test** para completar el conector de Fivetran.

Fivetran comenzará a sincronizar los datos de tu cuenta de Braze con tu almacén de datos de Snowflake. Puedes acceder a los datos de la consulta desde Mozart Data una vez que el conector haya finalizado la sincronización.

### Sincronizar datos de Mozart Data con Braze {#syncing-data-from-mozart-data-to-braze}

#### Paso 1: Configurar un almacén de datos de Snowflake {#step-1-set-up-a-snowflake-data-warehouse}

Sigue las instrucciones de [Ingesta de datos de Cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) para configurar una tabla, un usuario y un permiso desde la interfaz de Snowflake. Ten en cuenta que este paso requiere acceso a Snowflake a nivel de administrador.

#### Paso 2: Configurar tu integración de Snowflake en Braze {#step-2-set-up-your-snowflake-integration-in-braze}

Después de configurar tu almacén de Snowflake, en Mozart Data, ve a la página **Integration** y selecciona **Braze**. Aquí encontrarás las credenciales que necesitarás proporcionar a Braze.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

A continuación, mientras estás conectado a Braze, ve a **Integrations > Technology Partners > Snowflake** para iniciar el proceso de integración. Copia las credenciales de Mozart Data y añádelas a la página de importación de datos de Snowflake. Haz clic en **Set up sync details** e introduce tu cuenta de Snowflake y la información de la tabla de origen.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

A continuación, en la pantalla de importación de Snowflake en Braze, elige un nombre para la sincronización, proporciona las direcciones de correo electrónico de contacto y selecciona un tipo de datos y una frecuencia de sincronización.

#### Paso 3: Añadir una clave pública al usuario de Braze {#step-3-add-a-public-key-to-the-braze-user}
En este punto, tendrás que volver a Snowflake para completar la configuración. Añade la clave pública que aparece en el panel de Braze al usuario que creaste para que Braze se conecte a Snowflake.

Para más información sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si quieres rotar las claves en cualquier momento, Mozart Data puede generar un nuevo par de claves y proporcionarte la nueva clave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Paso 4: Probar la conexión {#step-4-test-connection}

Una vez que el usuario esté actualizado con la clave pública, vuelve al panel de Braze y haz clic en **Test connection**. Si la conexión es correcta, verás una vista previa de los datos. Si, por alguna razón, la conexión no tiene éxito, se mostrará un mensaje de error para ayudar a solucionar el problema.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Debes probar con éxito una integración antes de que pueda pasar del estado Borrador al Activo. Si necesitas salir de la página de creación, tu integración se guardará y podrás volver a visitar la página de detalles para realizar cambios y pruebas.
{% endalert %}

## Uso de esta integración {#using-this-integration}

### Cómo acceder a los datos de Braze como usuario de Mozart Data {#how-to-access-braze-data-as-a-mozart-data-user}
Tras crear correctamente una cuenta de Mozart Data, podrás acceder desde Mozart Data a tus datos de Braze sincronizados con tu almacén de datos de Snowflake.

#### Transformaciones {#transforms}
Mozart Data ofrece una capa de transformación SQL que permite a los usuarios crear una vista o una tabla. Puedes crear una tabla de dimensiones a nivel de usuario (por ejemplo, `dim_users`) para resumir los datos de uso del producto, el historial de transacciones y las actividades de interacción con mensajes de Braze de cada usuario.

#### Análisis {#analysis}
Utilizando los modelos de transformación o los datos brutos sincronizados desde Braze, puedes analizar la interacción de los usuarios con los mensajes de Braze. Además, puedes combinar los datos de Braze con otros datos de la aplicación y analizar cómo la información obtenida de la interacción de los usuarios con los mensajes de Braze se relaciona con otros datos que puedas tener sobre los usuarios. Por ejemplo, su información demográfica, historial de compras, uso de productos y participación en el servicio de atención al cliente.

Esto puede ayudarte a tomar decisiones más informadas sobre las estrategias de interacción para mejorar la retención de usuarios. Todo esto puede hacerse dentro de la interfaz de Mozart Data utilizando la herramienta de consulta, donde puedes exportar los resultados a una hoja de Google o a un CSV para preparar una presentación.

#### Inteligencia empresarial (BI) {#business-intelligence-bi}
¿Listo para visualizar y compartir tus conclusiones con otros miembros del equipo? Mozart Data se integra con casi todas las herramientas de BI. Si aún no tienes una herramienta de BI, ponte en contacto con Mozart Data para crear una cuenta gratuita de Metabase.