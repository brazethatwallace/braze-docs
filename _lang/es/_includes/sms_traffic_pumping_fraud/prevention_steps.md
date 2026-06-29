### ¿Qué pasos fundamentales inmediatos debería tomar mi empresa para prevenir este fraude? {#what-immediate-foundational-steps-should-my-company-take-to-prevent-this-fraud}

El paso más crítico que tu empresa puede tomar dentro de tu plataforma de interacción con los clientes es minimizar tu superficie de ataque utilizando limitaciones geográficas.

#### Utiliza la lista de permisos geográficos de Braze {#utilize-the-braze-geographic-permissions-allowlist}

Deberías auditar de forma proactiva las regiones donde residen tus clientes objetivo reales y configurar una lista de permitidos para autorizar explícitamente el envío de mensajes solo a esos países. Para conocer los pasos de configuración, consulta [Permisos geográficos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/).

##### Bloquea destinos de alto riesgo {#block-high-risk-destinations}

Si solo haces negocios en Norteamérica o Europa Occidental, no hay razón para dejar las puertas abiertas a países internacionales de alto costo en otras regiones. Como regla general, desactiva de forma proactiva cualquier país donde no comercialices activamente ni tengas operaciones para eliminar la exposición innecesaria.

{% if include.detail %}
Considera cuidadosamente cualquier solicitud para abrir rutas a países marcados como de **alto riesgo de fraude**.

##### Defensa en capas {#layered-defense}

Las restricciones geográficas son un primer paso crítico, pero son solo una capa dentro de una estrategia más amplia de defensa en profundidad. Ningún control individual es suficiente: combinar múltiples medidas hace que el abuso sea significativamente más complejo y difícil de ejecutar a escala. Más allá de la lista de permitidos geográfica, los controles clave incluyen protecciones como:

- Validación del lado del cliente y del servidor para garantizar la integridad de los datos
- Límites de velocidad razonables en puntos de conexión vulnerables para ralentizar los envíos automatizados
- Tokens CSRF para asegurar que las solicitudes se originen desde tus formularios legítimos
- CAPTCHA para disuadir las entradas fraudulentas masivas

{% alert note %}
Recomendamos colaborar con tu equipo interno de seguridad para adaptar estas sugerencias a tu infraestructura específica.
{% endalert %}
{% endif %}