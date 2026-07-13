---
nav_title: Ejemplos de estilo
article_title: Ejemplos de estilo
description: "Así es como se aplican los estilos a las páginas en Braze Docs, incluyendo encabezados, pestañas, bloques de código y más."
page_order: 8
noindex: true
---

# Ejemplos de estilo {#styling-examples}

Así es como se aplican los estilos a las páginas en Braze Docs, incluyendo encabezados, pestañas, bloques de código y más.

## Prueba de encabezados {#header-test}

{% tabs %}
{% tab Styling %}

# Banner H1 {#h1-banner}
Texto H1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## Banner H2 {#h2-banner}
Texto H2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### Banner H3 {#h3-banner}
Texto H3

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Banner H4 {#h4-banner}
Texto H4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### Banner H5 {#h5-banner}
Texto H5

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### Banner H6 {#h6-banner}
Texto H6

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

{% endtab %}
{% tab Markdown %}

```
# H1 Banner

## H2 Banner

### H3 Banner

#### H4 Banner

##### H5 Banner

###### H6 Banner
```
{% endtab %}
{% endtabs %}

## Ancla de encabezado personalizada {#custom-header-anchor}

Para agregar un ancla a un encabezado, añade el siguiente código al final de la línea en la que se encuentra el encabezado. Reemplaza `anchor-text` con el ancla para este encabezado. Usa letras minúsculas y coloca guiones entre las palabras.

```
# Heading Text {#anchor-text}
```

Puedes enlazar a encabezados con anclas personalizadas creando un enlace estándar con un signo de número `#` seguido del ancla personalizada.

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## Prueba de fuentes {#font-test}

{% tabs %}
{% tab Styling %}

Texto normal

*Texto enfatizado*

**Negrita**

_**Negrita enfatizada**_

~~Tachado~~

{% endtab %}
{% tab Markdown %}
```
Normal Text

*Emphasize Text*

**Bold**

_**Bold Emphasize**_

~~Strikethrough~~
```
{% endtab %}
{% endtabs %}

## Prueba de citas {#quote-test}

{% tabs %}
{% tab Styling %}
> Texto citado

#### Cita en línea {#inline-quote}
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

#### Bloque de cita {#quote-chunk}
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
```
{% endtab %}
{% tab Markdown %}
```
> Quoted Text

Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

``` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. ```
```
{% endtab %}
{% endtabs %}

## Prueba de tablas

{% tabs %}
{% tab Styling %}
| Instancia | URL del dashboard                                                     | Punto de conexión REST          |
| -------- | --------------------------------------------------------------------- | ------------------------------- |
| US-01    | `https://dashboard.braze.com` o<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` o<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
| AU-01    | `https://dashboard.au-01.braze.com/`                                  | `https://rest.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table Test" }
{% endtab %}
{% tab Markdown %}
```
| Instance | Dashboard URL                                                         | REST Endpoint                   |
|----------|-----------------------------------------------------------------------|---------------------------------|
| US-01    | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
| EU-02    | `https://dashboard-02.braze.eu`                                       | `https://rest.fra-02.braze.eu`  |
| AU-01    | `https://dashboard.au-01.braze.com/`                                  | `https://rest.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table Test" }
```
{% endtab %}
{% endtabs %}

#### Restablecer el salto de palabra de la tabla por columna

Para restablecer el salto de palabra de la tabla por columna, usa la siguiente sintaxis:

```markdown
{: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM aria-label="Resetting Table word-break by column" }
```

Reemplaza `NUM` con el número de columna correspondiente, hasta un máximo de 4 columnas. Si tienes menos de 4 columnas, elimina los marcadores de posición `.reset-td-br-NUM` adicionales. Tu tabla debería verse similar a lo siguiente:

```markdown
| Event Name                                                       | Feed Type              | Description                                                  | Custom Attributes                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | An email was successfully delivered to a User's mail server. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | User opened an email.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App Message Impression                                        | Platform-specific Feed | User viewed an In-App Message.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }

```
{% tabs local %}
{% tab Antes %}

| Nombre del evento                                                | Tipo de fuente         | Descripción                                                                          | Atributos personalizados                                                      |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Un correo electrónico se entregó correctamente al servidor de correo del usuario.    | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | El usuario abrió un correo electrónico.                                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | El usuario vio un mensaje dentro de la aplicación.                                   | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |

{% endtab %}
{% tab Después %}

| Nombre del evento                                                | Tipo de fuente         | Descripción                                                                          | Atributos personalizados                                                      |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Un correo electrónico se entregó correctamente al servidor de correo del usuario.    | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | El usuario abrió un correo electrónico.                                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | El usuario vio un mensaje dentro de la aplicación.                                   | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }
{% endtab %}
{% endtabs %}

## Prueba de enlaces
{% tabs %}
{% tab Styling %}
Enlace aquí: [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## Prueba de imágenes
{% tabs %}
{% tab Styling %}
Imagen: ![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

#### Prueba de imagen con enlace

Imagen con enlace: [![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### Estilo de imagen

![Texto]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### Anclaje de imágenes

![Texto]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
<br><br><br><br><br>
{% endtab %}
{% tab Markdown %}

```
![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

[![Braze]({% image_buster /assets/img/braze-logo-mark.png %})](https://www.braze.com)

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%;" }
```
{% endtab %}
{% endtabs %}

## Prueba de galería
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d <br> Este es un [enlace](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e <br> Este es otro `comentario`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68 <br> Este es otro **comentario** más.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **TÍTULO DE IMAGEN** <br> Esta es una prueba para ver si hace un salto de línea.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a <br> Este es un comentario normal.
{% endgallery %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> This is a [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> This is another `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> This is yet another **comment**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **IMAGE TITLE** <br> This is a test to see if it will line break.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> This is a regular comment.
{% endgallery %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Prueba de imagen interactiva
{% tabs %}
{% tab Styling %}
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
{% endtab %}
{% tab Markdown %}
```
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
```
{% endtab %}
{% endtabs %}
<!--- Leaving formatting here just in case it's important...
<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>
-->

## Prueba de fragmentos de código

{% tabs %}
{% tab Styling %}
#### Prueba de código Objective C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### Prueba de código Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### Prueba de código Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### Prueba de código json
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### Prueba de código JavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### Prueba de Pygments
```python
#!/usr/bin/python3

from engine import RunForrestRun

"""Test code for syntax highlighting!"""

class Foo:
	def __init__(self, var):
		self.var = var
		self.run()

	def run(self):
		RunForrestRun()  # run along!

```
{% endtab %}
{% tab Markdown %}
![Ejemplo de Markdown]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## Prueba de alertas

{% tabs %}
{% tab Styling %}

{% alert tip %}Este es un consejo{% endalert %}

{% alert note %}Esta es una nota{% endalert %}

{% alert important %}Esta es una alerta importante{% endalert %}

{% alert warning %}Esta es una advertencia{% endalert %}

{% alert update %}Esta es una actualización{% endalert %}

{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% alert tip %}
This is a tip
{% endalert %}

{% alert note %}
This is a note
{% endalert %}

{% alert important %}
This is a important alert
{% endalert %}

{% alert warning %}
This is a warning
{% endalert %}

{% alert update %}
This is a update
{% endalert %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Prueba de video incrustado
{% tabs %}
{% tab Styling %}
#### Video incrustado/YouTube
Por defecto se incrusta de YouTube.
{% multi_lang_include video.html id="9SrKbY4BV2E" source="youtube" %}

#### Video incrustado/Wistia
Incrusta un video de Wistia.
{% multi_lang_include video.html id="c5lgi4xnvo" source="wistia" %}

#### Video incrustado alineado a la derecha
{% multi_lang_include video.html id="9SrKbY4BV2E" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Video incrustado alineado a la izquierda
{% multi_lang_include video.html id="9SrKbY4BV2E" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### Ejemplo de Loom
* usa `source="loom"`
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

Necesitarás el ID de YouTube para incrustar un video de YouTube. Aparece después de `v=` en la URL. Por ejemplo, `https://www.youtube.com/watch?v=VR1qn1OBP7k` tiene un ID de `VR1qn1OBP7k`.

{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" source="youtube" %}
```
{% endraw %}

Para alinear a la derecha o a la izquierda, y limitar el ancho máximo al 50%, usa el parámetro `align` = `left` o `right`:
{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youtube_id]" align="right" source="youtube" %}
```
{% endraw %}

Ejemplo de Loom:
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Diseño de video destacado con ubicación de estado para mayor resolución

Para usar el diseño de video destacado que coloca un video estático en el lado izquierdo para una visualización de mayor resolución, agrega un `video_id` y un `video_type` (como `youtube`) al encabezado YAML de la página. Por defecto, `video_source` está configurado como `youtube`.

{% raw %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## Prueba de listas
{% tabs %}
{% tab Styling %}
#### Viñetas

- Lista 1
  - Sublista 1
- Lista 2
  - Sublista 2a
    - Sub sublista 2
- Lista 3

#### Numeradas

1. Lista 1
   - Sublista 1
2. Lista 2
3. Lista 3
   - Sublista 3a
   - Sublista 3b
     - Sub sublista 3
4. Lista 4
    1. Sublista 4a
        1. Sub sublista 4
    2. Sublista 4b
        1. Sub sublista 4

{% endtab %}
{% tab Markdown %}
```
#### Bullet

- List 1
  - Sub List 1
- List 2
  - Sub List 2a
    - Sub Sub List 2
- List 3

#### Numbered

1. List 1
   - Sub List 1
2. List 2
3. List 3
   - Sub List 3a
   - Sub List 3b
     - Sub Sub List 3
4. List 4
    1. Sub list 4a
        1. Sub Sub List 4
    2. Sub list 4b
        1. sub sub list 4
```
{% endtab %}
{% endtabs %}

## Prueba de contenido desplegable {#collapsible-content}
{% tabs %}
{% tab Styling %}
{% details Haz clic para expandir %}
#### ¡Mira! ¡Un bloque de código oculto!

```python
print("hello world!")
```
{% enddetails %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```liquid
{% details Click me to Expand %}
...
{% enddetails %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Prueba de pestañas

#### Pestañas personalizadas

{% tabs local %}
{% tab OBJECTIVE-C %}

Agrega la siguiente línea de código a tu archivo `AppDelegate.m`:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Dentro de tu archivo `AppDelegate.m`, agrega el siguiente fragmento de código dentro de tu método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si estás integrando el SDK de Braze con CocoaPods o Carthage, agrega la siguiente línea de código a tu archivo `AppDelegate.swift`:

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Para más información sobre el uso de código Objective-C en proyectos Swift, consulta la [documentación de Apple Developer][apple_initial_setup_19].

En `AppDelegate.swift`, agrega el siguiente fragmento de código a tu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### Uso
{% raw %}
Encierra las **pestañas** en `{% tabs %}` y `{% endtabs %}`
Encierra cada **pestaña** individual con el código Liquid y el nombre de la pestaña `{% tab [Tab name] %}` y `{% endtab %}`
{% endraw %}

{% alert important %}
 Ten en cuenta que el número de pestañas en la página debe ser consistente, de lo contrario el contenido de las pestañas podría ocultarse.
 Por ejemplo, si un conjunto de pestañas tiene `C++`, `C-Sharp` y `JS`, y otro conjunto de pestañas tiene `C-Sharp` y `JS`,
entonces cuando alguien haga clic en `C++`, la otra sección no mostrará nada. Consulta la siguiente opción de pestañas locales como solución alternativa.
{% endalert %}

{% raw %}
```liquid
{% tabs %}
{% tab objective-c %}
Content of objective-c
{% endtab %}
{% tab swift %}
Content of swift
{% endtab %}
{% endtabs %}
```
{% endraw %}

#### Pestañas locales
Para pestañas autocontenidas, como pestañas que solo cambian el contenido de la pestaña para la sección específica, usa el parámetro local en el bloque de pestañas padre.

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### Subpestañas
Para pestañas dentro de pestañas, se pueden usar `subtabs` y `subtab`. La configuración predeterminada es `local`.
Para `subtabs` globales, usa la opción `global`: {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
contenido de pestaña 1
{% subtabs %}
{% subtab Subtab 1a %}
Contenido de subpestaña 1a
{% endsubtab %}
{% subtab Subtab 2a %}
Contenido de subpestaña 2a
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
contenido de pestaña 2
{% subtabs %}
{% subtab Subtab 1b %}
Contenido de subpestaña 1b
{% endsubtab %}
{% subtab Subtab 2b %}
Contenido de subpestaña 2b
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Markdown
{% raw %}
```
{% tabs local %}
{% tab Tab 1 %}
tab content 1
{% subtabs %}
{% subtab Subtab 1a %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2a %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
tab content 2
{% subtabs %}
{% subtab Subtab 1b %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2b %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
```
{% endraw %}

[1]: {% image_buster /assets/img_archive/code_snippet.png %}