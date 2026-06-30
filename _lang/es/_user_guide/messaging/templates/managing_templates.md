---
nav_title: Administrar plantillas
article_title: Administrar plantillas
page_order: 1

page_type: reference
description: "Este artículo de referencia describe cómo duplicar y archivar plantillas en la sección Plantillas del panel de Braze."
tool:
  - Templates
  - Media

---

# Administrar plantillas {#manage-templates}

> Archivar o duplicar plantillas puede ayudar a organizarlas y administrarlas mejor. Este artículo de referencia explica cómo archivar y duplicar plantillas en la sección **Plantillas** del panel de Braze.

## Duplicar plantillas {#duplicating-templates}

{% tabs %}
{% tab Plantilla individual %}

![Menú desplegable con la opción de duplicar.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Para duplicar una plantilla individual, selecciona <i class="fas fa-ellipsis-v"></i> **Más opciones** de la plantilla y luego selecciona **Duplicar** en el menú desplegable.
<br><br>

{% alert note %}
Para las plantillas de [bloques de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), se crea una copia en borrador. Para todas las demás plantillas, se crea automáticamente una nueva copia duplicada.
{% endalert %}

{% endtab %}
{% tab Múltiples plantillas %}

{% raw %}

Para duplicar varias plantillas, selecciona la casilla de verificación junto al nombre de la plantilla. Primero, selecciona las plantillas y luego selecciona **Duplicar**.

Las plantillas duplicadas se pueden encontrar ordenando la columna **Fecha últ. modific.**. De forma predeterminada, las nuevas plantillas se nombrarán `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![Tres plantillas ordenadas por la fecha en que se editaron por última vez, con una plantilla copiada en la parte superior de la lista.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

{% endtab %}
{% endtabs %}

## Archivar plantillas {#archiving-templates}

![Menú desplegable de configuración expandido que muestra tres opciones: "Archivar", "Duplicar" y "Copiar al espacio de trabajo", con la opción "Archivar" resaltada.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Para archivar una plantilla individual, selecciona <i class="fas fa-ellipsis-v"></i> **Más opciones** en la pantalla de la cuadrícula de plantillas y selecciona **Archivar**. Cuando se archiva una plantilla, ten en cuenta los siguientes escenarios:

- Las campañas activas continúan usando la plantilla archivada sin ninguna interrupción.
- Los borradores de campañas conservan el contenido de la plantilla archivada y se pueden editar y lanzar.
- Para editar una plantilla archivada, primero debes desarchivarla. De igual forma, para usar una plantilla archivada en una campaña, primero debes desarchivar la plantilla.

Para archivar varias plantillas, selecciona la casilla de verificación junto a cada plantilla que desees archivar. Después de seleccionar varias plantillas, selecciona **Archivar**. Puedes encontrar tus plantillas archivadas seleccionando **Archivadas** en **Mostrar** en la cuadrícula de plantillas.

![Sección de plantillas de correo electrónico de arrastrar y soltar guardadas que muestra dos plantillas seleccionadas y una barra de herramientas con la opción de archivar.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
Archivar no está disponible actualmente para las [plantillas de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-templates).
{% endalert %}