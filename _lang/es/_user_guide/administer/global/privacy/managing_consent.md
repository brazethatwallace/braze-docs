---
nav_title: Gestionar el consentimiento
article_title: Administrar el consentimiento
page_order: 1
page_type: reference
description: "Este artículo de referencia proporciona consejos sobre cómo gestionar el consentimiento utilizando Braze."
---

# Gestionar el consentimiento

> Este artículo de referencia ofrece consejos sobre cómo gestionar el consentimiento de tus usuarios utilizando Braze.

Braze no puede proporcionar asesoramiento específico sobre la interpretación de leyes y reglamentos ni ofrecer orientación sobre la gestión del consentimiento, ya que esto dependerá de la interpretación de la ley que haga tu equipo jurídico. No obstante, ofrecemos una serie de herramientas de apoyo a la gestión de suscripciones y consentimientos.

Tu planteamiento debe depender del rigor que exija tu equipo jurídico en función de su interpretación de la ley. Aquí tienes algunas opciones a considerar, ordenadas de la más estricta a la menos estricta:

- **Equipos:** Utiliza [equipos Braze]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) para una verdadera gobernanza. Se trata de añadir un atributo personalizado a todos los perfiles de usuario para indicar su estado de consentimiento, la fecha de consentimiento o ambos. A continuación, debes migrar todas las Campaigns y Canvas al equipo designado y ajustar los permisos de usuario en el dashboard en consecuencia.
- **Atributo del perfil de usuario:** Añade un atributo de consentimiento a todos los perfiles de usuario. Este atributo indicará si un usuario ha dado su consentimiento o no. En el futuro, podrás incluir un segmento de usuarios que hayan dado su consentimiento (por ejemplo, `consent = true`) en todas tus Campaigns y Canvas.
- **Grupos de suscripción específicos del canal:** Manipula los grupos de suscripción para canales específicos (notificaciones push, correo electrónico, etc.) para gestionar el consentimiento. Inicialmente, marca a los usuarios como dados de baja de estos canales y solo márcalos como suscritos después de que hayan dado su consentimiento.

{% alert important %}
Consulta con tu equipo jurídico para determinar el enfoque adecuado para el cumplimiento de los requisitos de gestión del consentimiento de tu organización.
{% endalert %}