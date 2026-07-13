---
nav_title: Crear códigos
article_title: Crear códigos promocionales
page_order: 0.1
description: "Aprende a crear códigos promocionales en tus campañas y Canvas."
---

# Crear códigos promocionales {#create-promotion-codes}

> Aprende a crear códigos promocionales en tus campañas y Canvas.

## Crear una lista de códigos promocionales {#create}

### Paso 1: Crear una nueva lista {#step-1-create-a-new-list}

En el dashboard, ve a **Configuración de datos** > **Códigos promocionales** y selecciona **Crear lista de códigos promocionales**.

![Botón para crear un código promocional.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Paso 2: Introducir los detalles {#step-2-enter-the-details}

1. Asigna un nombre a tu lista de códigos promocionales y añade una descripción opcional.
2. A continuación, crea un fragmento de código para el código promocional.

Aquí tienes algunos detalles a tener en cuenta al crear un fragmento de código:

- No puedes editar un fragmento de código después de guardarlo.
- Los fragmentos de código distinguen entre mayúsculas y minúsculas. Por ejemplo, el sistema reconoce "Birthday_promo" y "birthday_promo" como dos fragmentos de código diferentes.
- Usa el nombre del fragmento de código en Liquid para hacer referencia a este conjunto de códigos promocionales.
- Asegúrate de que el fragmento de código no se esté usando ya en otra lista.

![Una lista de códigos promocionales llamada "SpringSale2025" con el fragmento de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Paso 3: Elegir las opciones del código promocional {#step-3-choose-promotion-code-options}

Cada lista de códigos promocionales tiene una fecha y hora de expiración correspondiente que se establece en el momento de la creación. La duración máxima de expiración es de seis meses a partir del día en que creas o editas tu lista.

En ese tiempo, puedes cambiar y actualizar la fecha de expiración repetidamente. Esta fecha de expiración se aplica a todos los códigos añadidos a esta lista. Al expirar, los códigos se eliminan del sistema de Braze y cualquier mensaje que haga referencia al fragmento de código de esa lista no se envía.

![Configuración de expiración de la lista indicando que todos los códigos restantes expirarán el 30 de abril de 2025 a las 12 am.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

También tienes la opción de configurar alertas de umbral opcionales y personalizadas. Si se configuran, estas alertas envían un correo electrónico al destinatario designado cuando la lista se está quedando sin códigos promocionales disponibles o cuando tu lista de códigos promocionales está cerca de expirar. El destinatario recibe una notificación una vez al día.

![Un ejemplo de una alerta de umbral para notificar a "marketing@abc.com" cuando la lista de códigos promocionales expire en 5 días.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Paso 4: Cargar códigos promocionales {#step-4-upload-promotion-codes}

Braze no gestiona la creación ni el canje de códigos, lo que significa que debes generar tus códigos promocionales en un archivo CSV y cargarlos en Braze.

Asegúrate de que tu archivo CSV siga estas directrices:

- Incluye una columna para los códigos promocionales.
- Tiene un código promocional por fila.

Puedes usar nuestra integración incorporada con [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify) o [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone) para crear y exportar códigos promocionales.

{% alert important %}
El tamaño máximo del archivo es de 100&nbsp;MB y el tamaño máximo de la lista es de 20 millones de códigos sin usar. Si descubres que se cargó el archivo incorrecto, carga uno nuevo para reemplazar el archivo anterior.
{% endalert %}

1. Una vez completada la carga, selecciona **Guardar lista** para guardar todos los detalles y códigos que acabas de introducir.

![Archivo CSV llamado "springsale" que se cargó correctamente.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2. Después de seleccionar guardar, aparece una nueva fila en el **Historial de importación**.
3. Para actualizar la tabla y ver si tu importación ha finalizado, selecciona <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sincronizar** en la parte superior de la tabla.

![Códigos promocionales en proceso de carga.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Los archivos más grandes tardan varios minutos en importarse. Mientras esperas, puedes salir de la página y trabajar en otra cosa mientras la importación está en curso. Cuando la importación finalice, el estado cambia a **Completado** en la tabla.
{% endalert %}

## Actualizar una lista de códigos promocionales {#updating-a-promotion-code-list}

Para actualizar una lista, selecciona una de tus listas existentes. Puedes cambiar el nombre, la descripción, la expiración de la lista y las alertas de umbral. También puedes añadir más códigos a la lista cargando nuevos archivos y seleccionando **Actualizar lista**. Todos los códigos de la lista tienen la misma expiración, independientemente de la fecha de importación.

{% alert important %}
Los códigos promocionales no se pueden eliminar.
{% endalert %}

### Modificar una lista de códigos promocionales incorrecta {#modifying-an-incorrect-promotion-code-list}

Si cargaste un archivo CSV con los códigos promocionales incorrectos y seleccionaste **Guardar lista**, puedes resolver esto con cualquiera de estos métodos:

- Deprecar la lista completa: deja de usar la lista de códigos promocionales actual en cualquier campaña, Canvas o plantilla. Luego, carga el archivo CSV con los códigos correctos y úsalos en tu mensajería.
- Usar los códigos incorrectos: crea una campaña que envíe códigos promocionales de la lista incorrecta a un marcador de posición hasta que se agoten todos los códigos incorrectos. Luego, carga los códigos promocionales correctos en la misma lista.