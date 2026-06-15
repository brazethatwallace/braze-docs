---
nav_title: Exemples de mise en forme
article_title: Exemples de mise en forme
description: "Voici comment les pages sont mises en forme sur Braze Docs, y compris les en-têtes, les onglets, les blocs de code, et plus encore."
page_order: 8
noindex: true
---

# Exemples de mise en forme {#styling-examples}

Voici comment les pages sont mises en forme sur Braze Docs, y compris les en-têtes, les onglets, les blocs de code, et plus encore.

## Test d'en-têtes {#header-test}

{% tabs %}
{% tab Styling %}

# Bannière H1 {#h1-banner}
Texte H1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## Bannière H2 {#h2-banner}
Texte H2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### Bannière H3 {#h3-banner}
Texte H3

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Bannière H4 {#h4-banner}
Texte H4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### Bannière H5 {#h5-banner}
Texte H5

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### Bannière H6 {#h6-banner}
Texte H6

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

## Ancre d'en-tête personnalisée {#custom-header-anchor}

Pour ajouter une ancre à un en-tête, ajoutez le code suivant à la fin de la ligne où se trouve l'en-tête. Remplacez `anchor-text` par l'ancre de cet en-tête. Utilisez des lettres minuscules et séparez les mots par des tirets.

```
# Heading Text {#anchor-text}
```

Vous pouvez créer des liens vers des en-têtes avec des ancres personnalisées en créant un lien standard avec un signe dièse `#` suivi de l'ancre personnalisée.

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## Test de polices {#font-test}

{% tabs %}
{% tab Styling %}

Texte normal

*Texte en italique*

**Gras**

_**Gras italique**_

~~Barré~~

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

## Test de citations {#quote-test}

{% tabs %}
{% tab Styling %}
> Texte cité

#### Citation en ligne {#inline-quote}
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

#### Bloc de citation {#quote-chunk}
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

## Test de tableaux

{% tabs %}
{% tab Styling %}
| Instance | URL du tableau de bord                                                | Endpoint REST                   |
| -------- | --------------------------------------------------------------------- | ------------------------------- |
| US-01    | `https://dashboard.braze.com` ou<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` ou<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
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

#### Réinitialiser le retour à la ligne du tableau par colonne

Pour réinitialiser le retour à la ligne du tableau par colonne, utilisez la syntaxe suivante :

```markdown
{: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM aria-label="Resetting Table word-break by column" }
```

Remplacez `NUM` par le numéro de colonne correspondant, jusqu'à un maximum de 4 colonnes. Si vous avez moins de 4 colonnes, supprimez les marques substitutives `.reset-td-br-NUM` supplémentaires. Votre tableau devrait ressembler à ceci :

```markdown
| Event Name                                                       | Feed Type              | Description                                                  | Custom Attributes                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | An email was successfully delivered to a User's mail server. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | User opened an email.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App Message Impression                                        | Platform-specific Feed | User viewed an In-App Message.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }

```
{% tabs local %}
{% tab Avant %}

| Nom de l'événement                                               | Type de flux           | Description                                                                          | Attributs personnalisés                                                       |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Un e-mail a été livré avec succès au serveur de messagerie de l'utilisateur.         | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | L'utilisateur a ouvert un e-mail.                                                    | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | L'utilisateur a consulté un message in-app.                                          | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |

{% endtab %}
{% tab Après %}

| Nom de l'événement                                               | Type de flux           | Description                                                                          | Attributs personnalisés                                                       |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Un e-mail a été livré avec succès au serveur de messagerie de l'utilisateur.         | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | L'utilisateur a ouvert un e-mail.                                                    | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | L'utilisateur a consulté un message in-app.                                          | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }
{% endtab %}
{% endtabs %}

## Test de liens
{% tabs %}
{% tab Styling %}
Lien ici : [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## Test d'images
{% tabs %}
{% tab Styling %}
Image : ![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

#### Test d'image avec lien

Image avec lien : [![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### Mise en forme d'image

![Texte]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### Ancrage d'images

![Texte]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
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

## Test de galerie
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d <br> Ceci est un [lien](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e <br> Ceci est un autre `commentaire`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68 <br> Ceci est encore un autre **commentaire**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **TITRE DE L'IMAGE** <br> Ceci est un test pour voir si le retour à la ligne fonctionne.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a <br> Ceci est un commentaire normal.
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

## Test d'image interactive
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

## Test d'extraits de code

{% tabs %}
{% tab Styling %}
#### Test de code Objective C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### Test de code Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### Test de code Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### Test de code JSON
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### Test de code JavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### Test Pygments
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
![Exemple Markdown]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## Test d'alertes

{% tabs %}
{% tab Styling %}

{% alert tip %}Ceci est un conseil{% endalert %}

{% alert note %}Ceci est une note{% endalert %}

{% alert important %}Ceci est une alerte importante{% endalert %}

{% alert warning %}Ceci est un avertissement{% endalert %}

{% alert update %}Ceci est une mise à jour{% endalert %}

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

## Test de vidéo intégrée
{% tabs %}
{% tab Styling %}
#### Vidéo intégrée/YouTube
Par défaut, la vidéo est intégrée depuis YouTube.
{% multi_lang_include video.html id="9SrKbY4BV2E" source="youtube" %}

#### Vidéo intégrée/Wistia
Intègre une vidéo Wistia.
{% multi_lang_include video.html id="c5lgi4xnvo" source="wistia" %}

#### Vidéo intégrée alignée à droite
{% multi_lang_include video.html id="9SrKbY4BV2E" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Vidéo intégrée alignée à gauche
{% multi_lang_include video.html id="9SrKbY4BV2E" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### Exemple Loom
* utilisez `source="loom"`
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

Vous aurez besoin de l'ID YouTube pour intégrer une vidéo YouTube. Il apparaît après `v=` dans l'URL. Par exemple, `https://www.youtube.com/watch?v=VR1qn1OBP7k` a pour ID `VR1qn1OBP7k`.

{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" source="youtube" %}
```
{% endraw %}

Pour aligner à droite ou à gauche et limiter la largeur maximale à 50 %, utilisez le paramètre `align` = `left` ou `right` :
{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youtube_id]" align="right" source="youtube" %}
```
{% endraw %}

Exemple Loom :
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Disposition vidéo mise en avant avec placement statique pour une résolution plus élevée

Pour utiliser la disposition vidéo mise en avant qui place une vidéo statique sur le côté gauche pour un affichage en haute résolution, ajoutez un `video_id` et un `video_type` (tel que `youtube`) dans l'en-tête YAML de la page. Par défaut, `video_source` est défini sur `youtube`.

{% raw %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## Test de listes
{% tabs %}
{% tab Styling %}
#### Puces

- Liste 1
  - Sous-liste 1
- Liste 2
  - Sous-liste 2a
    - Sous-sous-liste 2
- Liste 3

#### Numérotée

1. Liste 1
   - Sous-liste 1
2. Liste 2
3. Liste 3
   - Sous-liste 3a
   - Sous-liste 3b
     - Sous-sous-liste 3
4. Liste 4
    1. Sous-liste 4a
        1. Sous-sous-liste 4
    2. Sous-liste 4b
        1. Sous-sous-liste 4

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

## Test de contenu rétractable {#collapsible-content}
{% tabs %}
{% tab Styling %}
{% details Cliquez pour développer %}
#### Regardez ! Un bloc de code caché !

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

## Test d'onglets

#### Onglets personnalisés

{% tabs local %}
{% tab OBJECTIVE-C %}

Ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Dans votre fichier `AppDelegate.m`, ajoutez l'extrait de code suivant dans votre méthode `application:didFinishLaunchingWithOptions` :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec CocoaPods ou Carthage, ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` :

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Pour plus d'informations sur l'utilisation de code Objective-C dans des projets Swift, consultez la [documentation Apple Developer][apple_initial_setup_19].

Dans `AppDelegate.swift`, ajoutez l'extrait de code suivant dans votre `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### Utilisation
{% raw %}
Encadrez les **onglets** avec `{% tabs %}` et `{% endtabs %}`
Encadrez chaque **onglet** individuel avec le code Liquid et le nom de l'onglet `{% tab [Nom de l'onglet] %}` et `{% endtab %}`
{% endraw %}

{% alert important %}
 Notez que le nombre d'onglets sur la page doit être cohérent, sinon le contenu des onglets pourrait être masqué.
 Par exemple, si un ensemble d'onglets contient `C++`, `C-Sharp` et `JS`, et qu'un autre ensemble contient `C-Sharp` et `JS`,
alors lorsque quelqu'un clique sur `C++`, l'autre section n'affichera rien. Consultez l'option d'onglets locaux ci-dessous pour une solution de contournement.
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

#### Onglets locaux
Pour des onglets autonomes, c'est-à-dire des onglets qui ne modifient le contenu que pour la section spécifique, utilisez le paramètre local dans le bloc d'onglets parent.

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### Sous-onglets
Pour des onglets à l'intérieur d'onglets, `subtabs` et `subtab` peuvent être utilisés. Le paramètre par défaut est `local`.
Pour des `subtabs` globaux, utilisez l'option `global` : {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
contenu de l'onglet 1
{% subtabs %}
{% subtab Subtab 1a %}
Contenu du sous-onglet 1a
{% endsubtab %}
{% subtab Subtab 2a %}
Contenu du sous-onglet 2a
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
contenu de l'onglet 2
{% subtabs %}
{% subtab Subtab 1b %}
Contenu du sous-onglet 1b
{% endsubtab %}
{% subtab Subtab 2b %}
Contenu du sous-onglet 2b
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