---
nav_title: Accesibilidad
article_title: Accesibilidad
platform: Web
page_order: 22
page_type: reference
description: "Este artículo describe cómo Braze favorece la accesibilidad."

---

# Accesibilidad {#accessibility}

> Este artículo ofrece un resumen de cómo Braze favorece la accesibilidad dentro de tu integración.

Braze Web SDK es compatible con los estándares establecidos por las [Pautas de Accesibilidad al Contenido en la Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Mantenemos una [puntuación de 100/100 en Lighthouse](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) para las tarjetas de contenido y los mensajes dentro de la aplicación en todas nuestras nuevas versiones, con el fin de mantener nuestro estándar de accesibilidad.

## Requisitos previos {#prerequisites}

La versión mínima del SDK que cumple con WCAG 2.1 es cercana a la v3.4.0. Sin embargo, recomendamos actualizar al menos a la versión 6.0.0 para obtener correcciones importantes en las etiquetas de imagen.

### Correcciones notables en materia de accesibilidad {#notable-accessibility-fixes}

| Versión | Tipo | Cambios clave |
|---------|------|-------------|
| **6.0.0** | **Mayor** | Imágenes como etiquetas `<img>`, campos `imageAltText` o `language`, mejoras generales en la accesibilidad de la interfaz de usuario |
| **3.5.0** | Menor | Mejoras en la accesibilidad del texto desplazable |
| **3.4.0** | Corrección | Corrección del rol `article` en Content Cards |
| **3.2.0** | Menor | Objetivos táctiles mínimos de 45x45 px para botones |
| **3.1.2** | Menor | Texto alternativo predeterminado para imágenes |
| **2.4.1** | **Mayor** | HTML semántico (`h1` o `button`), atributos ARIA, navegación con el teclado, gestión del foco |
| **2.0.5** | Menor | Gestión del foco, navegación con el teclado, etiquetas |
{: .reset-td-br-1, .reset-td-br-2 aria-label="Notable accessibility fixes" }

## Características de accesibilidad compatibles {#supported-accessibility-features}

Admitimos estas características para Content Cards y mensajes dentro de la aplicación:

- Roles y etiquetas ARIA
- Compatibilidad con la navegación mediante teclado
- Gestión del foco
- Anuncios del lector de pantalla
- Compatibilidad con texto alternativo para imágenes

## Directrices de accesibilidad para integraciones de SDK {#accessibility-guidelines-for-sdk-integrations}

Consulta [Crea mensajes accesibles en Braze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/) para obtener directrices generales sobre accesibilidad. Esta guía proporciona consejos y prácticas recomendadas para lograr la máxima accesibilidad al integrar Braze Web SDK en tu aplicación web.

### Content Cards

#### Establecer una altura máxima {#setting-a-maximum-height}

Para evitar que las Content Cards ocupen demasiado espacio vertical y mejorar la accesibilidad, puedes establecer una altura máxima en el contenedor de la fuente, como en este ejemplo:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Consideraciones sobre la ventana gráfica {#viewport-considerations}

Para las Content Cards que se muestran en línea, ten en cuenta las restricciones del área de visualización, como en este ejemplo.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### Mensajes dentro de la aplicación {#in-app-messages}

{% alert warning %}
No incluyas información importante en los mensajes dentro de la aplicación de tipo deslizable, ya que no son accesibles para los lectores de pantalla.
{% endalert %}

### Consideraciones sobre los dispositivos móviles {#mobile-considerations}

#### Diseño adaptable {#responsive-design}

El SDK incluye puntos de interrupción adaptables. Confirma que tus personalizaciones funcionan en todos los tamaños de pantalla, como en este ejemplo:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }

  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Pruebas de accesibilidad {#testing-accessibility}

#### Lista de verificación de pruebas manuales {#manual-test-checklist}

Comprueba manualmente tu accesibilidad completando estas tareas:

- Navega por las Content Cards y los mensajes dentro de la aplicación solo con el teclado (Tab, Intro, Espacio)
- Prueba con un lector de pantalla (NVDA, JAWS, VoiceOver)
- Verifica que todas las imágenes tengan texto alternativo
- Comprueba las relaciones de contraste de color (utiliza herramientas como WebAIM Contrast Checker)
- Prueba en dispositivos móviles con pantalla táctil
- Comprueba que los indicadores de foco sean visibles
- Prueba la captura de foco en mensajes modales
- Verifica que se pueda acceder a todos los elementos interactivos mediante el teclado

### Problemas comunes de accesibilidad {#common-accessibility-issues}

Para evitar problemas comunes de accesibilidad, haz lo siguiente:

1. **Mantén los estilos de foco:** Los indicadores de foco del SDK son esenciales para los usuarios de teclado.
2. **Usa `display: none` solo en elementos no interactivos:** Usa `visibility: hidden` u `opacity: 0` para ocultar elementos interactivos.
3. **No anules los atributos ARIA:** El SDK establece los roles y etiquetas ARIA adecuados.
4. **Usa los atributos `tabindex`:** Estos controlan el orden de navegación del teclado.
5. **Proporciona un desplazamiento si configuras `overflow: hidden`:** Confirma que el contenido desplazable sigue siendo accesible.
6. **No interfieras con los controladores de teclado integrados:** Confirma que la navegación con el teclado existente funciona correctamente.