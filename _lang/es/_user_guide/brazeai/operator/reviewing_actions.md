---
nav_title: Revisar acciones
article_title: Revisión de las acciones de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Aprende a revisar y aprobar acciones cuando BrazeAI Operator proponga cambios en el panel."
---

# Revisión de las acciones de BrazeAI Operator {#reviewing-brazeai-operator-actions}

> Aprende a revisar y aprobar acciones cuando BrazeAI Operator<sup>TM</sup> proponga cambios en el panel.

![Operator presentando tarjetas de acciones sugeridas para su revisión.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Cómo funcionan las tarjetas de acción {#how-action-cards-work}

Cuando Operator propone cambios en el panel (como rellenar campos de formulario, actualizar configuraciones o generar imágenes), presenta cada cambio como una tarjeta de acción para su revisión.

1. **Operator resume el plan:** Operator explica lo que planea hacer antes de mostrar las tarjetas de acción.
2. **Aparecen las tarjetas de acción individuales:** Cada cambio propuesto se presenta como una tarjeta independiente que muestra lo que Operator quiere cambiar o hacer en el panel. Para los cambios en valores existentes, tanto el valor anterior como el valor propuesto se muestran uno junto al otro para su comparación.
3. **Revisa y aprueba:** Revisa cada tarjeta y apruébala o recházala.
4. **Se ejecuta la acción:** Las acciones aprobadas se ejecutan en Braze. Las acciones rechazadas no se aplican.

Si una acción falla después de la aprobación, Operator te notifica con detalles sobre el error.

### Disponibilidad {#availability}

Operator puede proponer tarjetas de acción en las páginas del panel compatibles, incluidos los creadores de mensajes, las páginas de listas y resúmenes, la configuración y otras superficies donde puede actuar. Para una cobertura representativa, consulta [Lo que puedes hacer con Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Para los canales de mensajes y editores compatibles, consulta [Generar mensajes]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).

La cobertura se amplía regularmente. Si Operator no puede actuar en la página en la que te encuentras, proporciona una lista de pasos a seguir en la interfaz de usuario.

## Modificar un plan {#modify-a-plan}

Para modificar el plan de Operator, primero aprueba o rechaza las acciones pendientes. Luego describe el cambio deseado en un nuevo mensaje de chat.

Las acciones aprobadas no se pueden deshacer a través de Operator. Describe el nuevo cambio a Operator o realiza los cambios manualmente en el panel.

## Acciones de aprobación automática {#auto-approve-actions}

El alternador **Acciones de aprobación automática** se encuentra en el panel de chat de Operator.

- **Activado:** Las acciones sugeridas por Operator se ejecutan inmediatamente sin requerir aprobación manual, incluyendo [navegar a una página diferente]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) para completar tu solicitud. Algunas acciones aún requieren aprobación explícita por seguridad, como generar imágenes o realizar modificaciones en la configuración a nivel de espacio de trabajo.
- **Desactivado (predeterminado):** Todas las acciones propuestas siguen el proceso de revisión manual descrito, incluyendo la navegación entre páginas: Operator propone el movimiento y espera tu aprobación antes de llevarte allí.

![El alternador de aprobación automática y el modal de confirmación en el panel de chat de Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

La aprobación automática se restablece cuando actualizas la página, abres una nueva pestaña o cierras sesión y vuelves a iniciarla. Navegar entre páginas en el panel no la restablece. La aprobación automática se puede desactivar en cualquier momento.

Para obtener información sobre cómo restringir el acceso de Operator y auditar el uso del equipo, consulta [Privacidad de datos y seguridad]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).