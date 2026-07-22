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
{% multi_lang_include partners/workflow_automation/mozart_data_integration_bullets.md %}

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
| Cuenta de Mozart Data | Se requiere una cuenta de Mozart Data para aprovechar esta integración. [Regístrate para obtener una cuenta de Mozart Data](https://app.mozartdata.com/signup)|
| Cuenta de Snowflake<br>Opción 1: cuenta nueva | Selecciona **Create a New Snowflake Account** durante el proceso de creación de la cuenta de Mozart Data para que Mozart Data aprovisione una nueva cuenta de Snowflake para ti. |
| Cuenta de Snowflake<br>Opción 2: cuenta existente | Si tu organización ya tiene una cuenta de Snowflake, puedes usar la opción Mozart Data Connected.<br><br>Selecciona la opción **Already Have a Snowflake Account** para conectar una cuenta de Snowflake existente. Para seguir esta opción, un usuario con permisos a nivel de cuenta debe [seguir estos pasos](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

La integración es compatible tanto para sincronizar datos [de Braze a Mozart Data](#syncing-data-from-braze-to-mozart-data) como [de Mozart Data a Braze](#syncing-data-from-mozart-data-to-braze).

### Sincronizar datos de Braze a Mozart Data {#syncing-data-from-braze-to-mozart-data}

#### Paso 1: Configurar el conector de Braze {#step-1-set-up-braze-connector}

1. En Mozart Data, ve a **Connectors** y selecciona **Add Connector**.
2. Busca "Braze" y selecciona la tarjeta del conector.
3. Introduce un nombre de esquema de destino donde se almacenarán todos los datos sincronizados de Braze. Recomendamos usar el nombre de esquema predeterminado `braze`.
4. Selecciona **Add Connector**.

#### Paso 2: Completar el formulario del conector de Fivetran {#step-2-fill-out-the-fivetran-connector-form}

La página del conector de Fivetran se abre después de completar el paso 1. Rellena los campos proporcionados y luego selecciona **Continue** > **Save & Test** para completar el conector de Fivetran.

Fivetran comienza a sincronizar datos de tu cuenta de Braze a tu almacén de datos de Snowflake. Puedes acceder a los datos de consulta desde Mozart Data una vez que el conector termine de sincronizar.

### Sincronizar datos de Mozart Data a Braze {#syncing-data-from-mozart-data-to-braze}

#### Paso 1: Configurar un almacén de datos de Snowflake {#step-1-set-up-a-snowflake-data-warehouse}

Sigue las instrucciones de [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) para configurar una tabla, un usuario y un permiso desde la interfaz de Snowflake. Ten en cuenta que este paso requiere acceso de nivel administrador a Snowflake.

#### Paso 2: Configurar tu integración de Snowflake en Braze {#step-2-set-up-your-snowflake-integration-in-braze}

Después de configurar tu almacén de Snowflake, en Mozart Data, ve a la página **Integration** y selecciona **Braze**. La vista de integración de **Braze** muestra las credenciales que debes copiar en Braze.

![Página de integración de Mozart Data con Braze seleccionado y credenciales de conexión de Snowflake para usar en Braze.]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

A continuación, con la sesión iniciada en Braze, ve a **Integraciones > Partners tecnológicos > Snowflake** para comenzar el proceso de integración. Copia las credenciales de Mozart Data y agrégalas a la página de importación de datos de Snowflake. Selecciona **Set up sync details** e introduce la información de tu cuenta de Snowflake y la tabla de origen.

![Formulario de integración del partner Snowflake en Braze con los campos de cuenta, almacén, base de datos y esquema completados con las credenciales de Mozart Data.]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

A continuación, elige un nombre para tu sincronización, proporciona correos electrónicos de contacto y selecciona un tipo de datos y una frecuencia de sincronización en la pantalla de configuración de importación de Snowflake en Braze.

#### Paso 3: Agregar una clave pública al usuario de Braze {#step-3-add-a-public-key-to-the-braze-user}
En este punto, regresa a Snowflake para completar la configuración. Agrega la clave pública que se muestra en el panel de Braze al usuario que creaste para que Braze se conecte a Snowflake.

Para obtener información adicional sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si deseas rotar las claves en algún momento, Mozart Data puede generar un nuevo par de claves y proporcionarte la nueva clave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Paso 4: Probar la conexión {#step-4-test-connection}

Una vez que el usuario se haya actualizado con la clave pública, regresa al panel de Braze y selecciona **Test connection**. Si la conexión es exitosa, verás una vista previa de los datos. Si por alguna razón la conexión no es exitosa, se mostrará un mensaje de error para ayudarte a solucionar el problema.

![Resultado de la prueba de conexión de la integración de Snowflake en Braze mostrando una vista previa exitosa después de aplicar la clave pública.]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Debes probar exitosamente una integración antes de que pueda pasar del estado Borrador al estado Activo. Si necesitas cerrar la página de creación, tu integración se guardará y podrás volver a la página de detalles para hacer cambios y probar.
{% endalert %}

## Uso de esta integración {#using-this-integration}

### Cómo acceder a los datos de Braze como usuario de Mozart Data {#how-to-access-braze-data-as-a-mozart-data-user}
Una vez que hayas creado correctamente una cuenta de Mozart Data, podrás acceder a tus datos de Braze sincronizados con tu almacén de datos de Snowflake desde Mozart Data.

#### Transformaciones {#transforms}
Mozart Data ofrece una capa de transformación SQL que permite a los usuarios crear una vista o tabla. Puedes crear una tabla de dimensiones a nivel de usuario (por ejemplo, `dim_users`) para resumir los datos de uso del producto, el historial de transacciones y las actividades de participación de cada usuario con los mensajes de Braze.

#### Análisis {#analysis}
Usando los modelos de transformación o los datos sin procesar sincronizados desde Braze, puedes analizar la participación de los usuarios con los mensajes de Braze. Además, puedes combinar los datos de Braze con otros datos de la aplicación y analizar cómo la información obtenida de la interacción de los usuarios con los mensajes de Braze se relaciona con otros datos que puedas tener sobre los usuarios. Por ejemplo, su información demográfica, historial de compras, uso del producto y participación con el servicio de atención al cliente.

Esto puede ayudarte a tomar decisiones más informadas sobre las estrategias de participación para mejorar la retención de usuarios. Todo esto se puede hacer dentro de la interfaz de Mozart Data usando la herramienta de consultas, donde puedes exportar los resultados a una hoja de Google Sheets o un CSV para preparar una presentación.

#### Inteligencia empresarial (BI) {#business-intelligence-bi}
¿Listo para visualizar y compartir tu información con otros miembros del equipo? Mozart Data se integra con casi todas las herramientas de BI. Si aún no tienes una herramienta de BI, contacta a Mozart Data para configurar una cuenta gratuita de Metabase.