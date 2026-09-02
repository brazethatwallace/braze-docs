---
nav_title: Styling-Beispiele
article_title: Styling-Beispiele
description: "So werden Seiten in Braze Docs gestaltet, einschließlich Überschriften, Tabs, Codeblöcke und mehr."
page_order: 8
noindex: true
---

# Styling-Beispiele {#styling-examples}

So werden Seiten in Braze Docs gestaltet, einschließlich Überschriften, Tabs, Codeblöcke und mehr.

## Überschriften-Test {#header-test}

{% tabs %}
{% tab Styling %}

# H1-Banner
H1-Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## H2-Banner
H2-Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### H3-Banner
H3-Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### H4-Banner
H4-Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### H5-Banner
H5-Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### H6-Banner
H6-Text

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

## Benutzerdefinierter Überschriften-Anker {#custom-header-anchor}

Um einer Überschrift einen Anker hinzuzufügen, fügen Sie den folgenden Code am Ende der Zeile hinzu, in der sich die Überschrift befindet. Ersetzen Sie `anchor-text` durch den Anker für diese Überschrift. Verwenden Sie Kleinbuchstaben und setzen Sie Bindestriche zwischen die Wörter.

```
# Heading Text {#anchor-text}
```

Sie können auf Überschriften mit benutzerdefinierten Ankern verlinken, indem Sie einen Standardlink mit einem Nummernzeichen `#` gefolgt vom benutzerdefinierten Anker erstellen.

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## Schriftarten-Test {#font-test}

{% tabs %}
{% tab Styling %}

Normaler Text

*Hervorgehobener Text*

**Fett**

_**Fett hervorgehoben**_

~~Durchgestrichen~~

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

## Zitat-Test {#quote-test}

{% tabs %}
{% tab Styling %}
> Zitierter Text

#### Inline-Zitat {#inline-quote}
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

#### Zitat-Block {#quote-chunk}
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

## Tabellen-Test

{% tabs %}
{% tab Styling %}
| Instanz  | Dashboard-URL                                                         | REST-Endpunkt                   |
| -------- | --------------------------------------------------------------------- | ------------------------------- |
| US-01    | `https://dashboard.braze.com` oder<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` oder<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
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

#### Zurücksetzen des Tabellen-Wortumbruchs nach Spalte

Um den Tabellen-Wortumbruch nach Spalte zurückzusetzen, verwenden Sie die folgende Syntax:

```markdown
{: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM aria-label="Resetting Table word-break by column" }
```

Ersetzen Sie `NUM` durch die entsprechende Spaltennummer, bis zu maximal 4 Spalten. Wenn Sie weniger als 4 Spalten haben, entfernen Sie die zusätzlichen `.reset-td-br-NUM`-Platzhalter. Ihre Tabelle sollte in etwa so aussehen:

```markdown
| Event Name                                                       | Feed Type              | Description                                                  | Custom Attributes                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | An email was successfully delivered to a User's mail server. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | User opened an email.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App Message Impression                                        | Platform-specific Feed | User viewed an In-App Message.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }

```
{% tabs local %}
{% tab Vorher %}

| Event Name                                                       | Feed Type              | Description                                                  | angepasste Attribute                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Eine E-Mail wurde erfolgreich an den Mailserver einer Nutzer:in zugestellt. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | Nutzer:in hat eine E-Mail geöffnet.                          | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | Nutzer:in hat eine In-App-Nachricht angesehen.               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |

{% endtab %}
{% tab Nachher %}

| Event Name                                                       | Feed Type              | Description                                                  | angepasste Attribute                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Eine E-Mail wurde erfolgreich an den Mailserver einer Nutzer:in zugestellt. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | Nutzer:in hat eine E-Mail geöffnet.                          | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | Nutzer:in hat eine In-App-Nachricht angesehen.               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }
{% endtab %}
{% endtabs %}

## Link-Test
{% tabs %}
{% tab Styling %}
Link hier: [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## Bild-Test
{% tabs %}
{% tab Styling %}
Bild: ![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

#### Verlinktes Bild – Test

Verlinktes Bild: [![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### Bild-Styling

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### Bilder verankern

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
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

## Galerie-Test
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d <br> Dies ist ein [Link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e <br> Dies ist ein weiterer `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68 <br> Dies ist noch ein weiterer **Kommentar**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **BILDTITEL** <br> Dies ist ein Test, um zu sehen, ob ein Zeilenumbruch erfolgt.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a <br> Dies ist ein normaler Kommentar.
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

## Interaktives Bild – Test
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

## Code-Snippet-Test

{% tabs %}
{% tab Styling %}
#### Code-Test Objective C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### Code-Test Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### Code-Test Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### Code-Test JSON
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### Code-Test JavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### Pygments-Test
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
![Markdown-Beispiel]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## Hinweis-Test

{% tabs %}
{% tab Styling %}

{% alert tip %}Dies ist ein Tipp{% endalert %}

{% alert note %}Dies ist ein Hinweis{% endalert %}

{% alert important %}Dies ist ein wichtiger Hinweis{% endalert %}

{% alert warning %}Dies ist eine Warnung{% endalert %}

{% alert update %}Dies ist ein Update{% endalert %}

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

## Eingebettetes Video – Test
{% tabs %}
{% tab Styling %}
#### Eingebettetes Video/YouTube
Standardmäßig wird YouTube eingebettet.
{% multi_lang_include video.html id="9SrKbY4BV2E" source="youtube" %}

#### Eingebettetes Video/Wistia
Bettet ein Wistia-Video ein.
{% multi_lang_include video.html id="c5lgi4xnvo" source="wistia" %}

#### Eingebettetes Video rechtsbündig
{% multi_lang_include video.html id="9SrKbY4BV2E" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Eingebettetes Video linksbündig
{% multi_lang_include video.html id="9SrKbY4BV2E" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### Loom-Beispiel
* Verwenden Sie `source="loom"`
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

Sie benötigen die YouTube-ID, um ein YouTube-Video einzubetten. Sie erscheint nach `v=` in der URL. Zum Beispiel hat `https://www.youtube.com/watch?v=VR1qn1OBP7k` die ID `VR1qn1OBP7k`.

{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" source="youtube" %}
```
{% endraw %}

Um rechts- oder linksbündig auszurichten und die maximale Breite auf 50 % zu begrenzen, verwenden Sie den Parameter `align` = `left` oder `right`:
{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youtube_id]" align="right" source="youtube" %}
```
{% endraw %}

Loom-Beispiel:
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Featured-Video-Layout mit Statusplatzierung für höhere Auflösung

Um das Featured-Video-Layout zu verwenden, das ein statisches Video auf der linken Seite für eine höhere Auflösung platziert, fügen Sie eine `video_id` und einen `video_type` (z. B. `youtube`) zum YAML-Header der Seite hinzu. Standardmäßig ist `video_source` auf `youtube` gesetzt.

{% raw %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## Listen-Test
{% tabs %}
{% tab Styling %}
#### Aufzählung

- Liste 1
  - Unterliste 1
- Liste 2
  - Unterliste 2a
    - Unter-Unterliste 2
- Liste 3

#### Nummeriert

1. Liste 1
   - Unterliste 1
2. Liste 2
3. Liste 3
   - Unterliste 3a
   - Unterliste 3b
     - Unter-Unterliste 3
4. Liste 4
    1. Unterliste 4a
        1. Unter-Unterliste 4
    2. Unterliste 4b
        1. Unter-Unterliste 4

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

## Einklappbarer Inhalt – Test {#collapsible-content}
{% tabs %}
{% tab Styling %}
{% details Klicken Sie hier zum Aufklappen %}
#### Schau! Ein versteckter Codeblock!

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

## Tab-Test

#### Benutzerdefinierte Tabs

{% tabs local %}
{% tab OBJECTIVE-C %}

Fügen Sie die folgende Codezeile zu Ihrer `AppDelegate.m`-Datei hinzu:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Fügen Sie in Ihrer `AppDelegate.m`-Datei das folgende Snippet innerhalb Ihrer `application:didFinishLaunchingWithOptions`-Methode hinzu:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Wenn Sie das Braze SDK mit CocoaPods oder Carthage integrieren, fügen Sie die folgende Codezeile zu Ihrer `AppDelegate.swift`-Datei hinzu:

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Weitere Informationen zur Verwendung von Objective-C-Code in Swift-Projekten finden Sie in der [Apple Developer Docs][apple_initial_setup_19].

Fügen Sie in `AppDelegate.swift` das folgende Snippet zu Ihrer `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` hinzu:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### Verwendung
{% raw %}
Umschließen Sie **Tabs** mit `{% tabs %}` und `{% endtabs %}`
Umschließen Sie einzelne **Tabs** mit dem Liquid-Code und dem Namen des Tabs `{% tab [Tab-Name] %}` und `{% endtab %}`
{% endraw %}

{% alert important %}
 Beachten Sie, dass die Anzahl der Tabs auf der Seite konsistent sein sollte, da sonst Tab-Inhalte möglicherweise ausgeblendet werden.
 Wenn beispielsweise ein Tab-Set `C++`, `C-Sharp` und `JS` enthält und ein anderes Tab-Set `C-Sharp` und `JS`,
dann wird beim Klick auf `C++` der andere Abschnitt nichts anzeigen. Siehe die folgende Option für lokale Tabs als Workaround.
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

#### Lokale Tabs
Für eigenständige Tabs, die nur den Tab-Inhalt für den jeweiligen Abschnitt ändern, verwenden Sie den lokalen Parameter im übergeordneten Tabs-Block.

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### Unter-Tabs
Für Tabs innerhalb von Tabs können `subtabs` und `subtab` verwendet werden. Die Standardeinstellung ist `local`.
Für globale `subtabs` verwenden Sie die Option `global`: {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
Tab-Inhalt 1
{% subtabs %}
{% subtab Subtab 1a %}
Subtab-1a-Inhalt
{% endsubtab %}
{% subtab Subtab 2a %}
Subtab-2a-Inhalt
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
Tab-Inhalt 2
{% subtabs %}
{% subtab Subtab 1b %}
Subtab-1b-Inhalt
{% endsubtab %}
{% subtab Subtab 2b %}
Subtab-2b-Inhalt
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