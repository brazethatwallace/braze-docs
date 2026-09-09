## Prueba de centros de preferencias {#testing-preference-centers}

Los enlaces del centro de preferencias se generan para cada usuario en el momento del envío y están vinculados a un envío en vivo de una Campaign o Canvas. Los envíos de prueba y las vistas previas del editor no admiten guardar cambios de suscripción. Este es el comportamiento esperado.

### Lo que verás {#what-youll-see}

- **Envíos de prueba:** Es posible que las etiquetas de Liquid del centro de preferencias no se resuelvan en un enlace válido. Si la página se carga, el botón **Save Preferences** está deshabilitado y los cambios de suscripción no se guardan.
- **Pestaña Vista previa del editor de arrastrar y soltar:** Puedes previsualizar el diseño y el estilo, pero no puedes probar el guardado de preferencias desde el editor.

### Cómo probar de extremo a extremo {#how-to-test-end-to-end}

Para verificar que los enlaces y botones del centro de preferencias funcionan antes de un lanzamiento completo:

1. Crea una Campaign o un paso de correo electrónico en Canvas que incluya tu etiqueta de Liquid del centro de preferencias.
2. Dirige el mensaje solo a tus usuarios de prueba o a un Segment interno pequeño.
3. Lanza el mensaje y abre el correo electrónico desde un buzón de entrada real (no con **Send Test**).
4. Selecciona el enlace del centro de preferencias, actualiza los grupos de suscripción y selecciona **Save Preferences**.
5. Confirma los cambios en el perfil del usuario en el panel de Braze.

{% if include.section == "api" %}
Como alternativa para los centros de preferencias creados mediante API, usa el [endpoint Generar URL del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) para obtener una URL funcional para un usuario específico fuera de un envío de prueba.
{% endif %}

Para otras limitaciones de los envíos de prueba, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages#limitations).

### Vista previa, envío de prueba y envío en vivo {#preview-test-send-and-live-send}

| Método | Vista previa del diseño | Guardar cambios de suscripción |
| --- | --- | --- |
| Pestaña **vista previa** del editor de arrastrar y soltar | Sí | No |
| **Send Test** de Campaign o Canvas | Parcial (el correo electrónico llega) | No |
| Envío en vivo a un usuario de prueba o Segment | Sí | Sí |
| API [Generar URL del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Sí | Sí |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vista previa, envío de prueba y envío en vivo" }