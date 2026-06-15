---
nav_title: Exemplos de estilização
article_title: Exemplos de estilização
description: "É assim que as páginas são estilizadas no Braze Docs, incluindo cabeçalhos, guias, blocos de código e mais."
page_order: 8
noindex: true
---

# Exemplos de estilização {#styling-examples}

É assim que as páginas são estilizadas no Braze Docs, incluindo cabeçalhos, guias, blocos de código e mais.

## Teste de cabeçalho {#header-test}

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

## Âncora de cabeçalho personalizada {#custom-header-anchor}

Para adicionar uma âncora a um cabeçalho, adicione o seguinte código ao final da linha em que o cabeçalho está. Substitua `anchor-text` pela âncora desse cabeçalho. Use letras minúsculas e coloque hifens entre as palavras.

```
# Heading Text {#anchor-text}
```

Você pode criar links para cabeçalhos com âncoras personalizadas criando um link padrão com o sinal de número `#` seguido da âncora personalizada.

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## Teste de fonte {#font-test}

{% tabs %}
{% tab Styling %}

Texto normal

*Texto enfatizado*

**Negrito**

_**Negrito enfatizado**_

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

## Teste de citação {#quote-test}

{% tabs %}
{% tab Styling %}
> Texto citado

#### Citação inline {#inline-quote}
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

#### Bloco de citação {#quote-chunk}
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

## Teste de tabela

{% tabs %}
{% tab Styling %}
| Instância | URL do dashboard                                                      | Endpoint REST                   |
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

#### Redefinindo a quebra de palavra da tabela por coluna

Para redefinir a quebra de palavra da tabela por coluna, use a seguinte sintaxe:

```markdown
{: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM aria-label="Resetting Table word-break by column" }
```

Substitua `NUM` pelo número da coluna correspondente, até um máximo de 4 colunas. Se você tiver menos de 4 colunas, remova os espaços reservados `.reset-td-br-NUM` extras. Sua tabela deve ficar semelhante ao seguinte:

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

| Nome do evento                                                   | Tipo de feed           | Descrição                                                                     | Atributos personalizados                                                      |
| ---------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Um e-mail foi entregue com sucesso ao servidor de e-mail do usuário.          | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | O usuário abriu um e-mail.                                                    | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | O usuário visualizou uma mensagem no app.                                     | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |

{% endtab %}
{% tab Depois %}

| Nome do evento                                                   | Tipo de feed           | Descrição                                                                     | Atributos personalizados                                                      |
| ---------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | Um e-mail foi entregue com sucesso ao servidor de e-mail do usuário.          | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | O usuário abriu um e-mail.                                                    | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | O usuário visualizou uma mensagem no app.                                     | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }
{% endtab %}
{% endtabs %}

## Teste de link
{% tabs %}
{% tab Styling %}
Link aqui: [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## Teste de imagem
{% tabs %}
{% tab Styling %}
Imagem: ![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

#### Teste de imagem com link

Imagem com link: [![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### Estilização de imagem

![Texto]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### Ancoragem de imagens

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

## Teste de galeria
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d <br> Este é um [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e <br> Este é outro `comentário`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68 <br> Este é mais um **comentário**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **TÍTULO DA IMAGEM** <br> Este é um teste para ver se haverá quebra de linha.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a <br> Este é um comentário normal.
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

## Teste de imagem interativa
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

## Teste de trecho de código

{% tabs %}
{% tab Styling %}
#### Teste de código Objective C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### Teste de código Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### Teste de código Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### Teste de código JSON
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### Teste de código JavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### Teste Pygments
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
![Exemplo de Markdown]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## Teste de alerta

{% tabs %}
{% tab Styling %}

{% alert tip %}Esta é uma dica{% endalert %}

{% alert note %}Esta é uma nota{% endalert %}

{% alert important %}Este é um alerta importante{% endalert %}

{% alert warning %}Este é um aviso{% endalert %}

{% alert update %}Esta é uma atualização{% endalert %}

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

## Teste de vídeo incorporado
{% tabs %}
{% tab Styling %}
#### Vídeo incorporado/YouTube
O padrão é incorporação do YouTube.
{% multi_lang_include video.html id="9SrKbY4BV2E" source="youtube" %}

#### Vídeo incorporado/Wistia
Incorpora um vídeo do Wistia.
{% multi_lang_include video.html id="c5lgi4xnvo" source="wistia" %}

#### Vídeo incorporado alinhado à direita
{% multi_lang_include video.html id="9SrKbY4BV2E" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Vídeo incorporado alinhado à esquerda
{% multi_lang_include video.html id="9SrKbY4BV2E" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### Exemplo Loom
* use `source="loom"`
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

Você vai precisar do ID do YouTube para incorporar um vídeo do YouTube. Ele aparece após `v=` na URL. Por exemplo, `https://www.youtube.com/watch?v=VR1qn1OBP7k` tem o ID `VR1qn1OBP7k`.

{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" source="youtube" %}
```
{% endraw %}

Para alinhar à direita ou à esquerda e limitar a largura máxima a 50%, use o parâmetro `align` = `left` ou `right`:
{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youtube_id]" align="right" source="youtube" %}
```
{% endraw %}

Exemplo Loom:
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Layout de vídeo em destaque com posicionamento estático para maior resolução

Para usar o layout de vídeo em destaque que posiciona um vídeo estático no lado esquerdo para exibição em maior resolução, adicione um `video_id` e um `video_type` (como `youtube`) ao cabeçalho YAML da página. Por padrão, `video_source` é definido como `youtube`.

{% raw %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## Teste de lista
{% tabs %}
{% tab Styling %}
#### Marcadores

- Lista 1
  - Sublista 1
- Lista 2
  - Sublista 2a
    - Sub-sublista 2
- Lista 3

#### Numerada

1. Lista 1
   - Sublista 1
2. Lista 2
3. Lista 3
   - Sublista 3a
   - Sublista 3b
     - Sub-sublista 3
4. Lista 4
    1. Sublista 4a
        1. Sub-sublista 4
    2. Sublista 4b
        1. Sub-sublista 4

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

## Teste de conteúdo recolhível {#collapsible-content}
{% tabs %}
{% tab Styling %}
{% details Clique para expandir %}
#### Olha! Um bloco de código oculto!

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

## Teste de guias

#### Guias personalizadas

{% tabs local %}
{% tab OBJECTIVE-C %}

Adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Dentro do seu arquivo `AppDelegate.m`, adicione o seguinte trecho no método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Se você está integrando o SDK da Braze com CocoaPods ou Carthage, adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift`:

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Para saber mais sobre o uso de código Objective-C em projetos Swift, consulte a [documentação para desenvolvedores da Apple][apple_initial_setup_19].

Em `AppDelegate.swift`, adicione o seguinte trecho ao seu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### Uso
{% raw %}
Envolva as **guias** em `{% tabs %}` e `{% endtabs %}`
Envolva cada **guia** individual com o código Liquid e o nome da guia `{% tab [Tab name] %}` e `{% endtab %}`
{% endraw %}

{% alert important %}
 Observe que o número de guias na página deve ser consistente, caso contrário o conteúdo da guia pode ficar oculto.
 Por exemplo, se um conjunto de guias tem `C++`, `C-Sharp` e `JS`, e outro conjunto de guias tem `C-Sharp` e `JS`,
então quando alguém clicar em `C++`, a outra seção não mostrará nada. Veja a opção de guias locais a seguir para uma solução alternativa.
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

#### Guias locais
Para guias independentes, como guias que alteram apenas o conteúdo da guia para a seção específica, use o parâmetro local no bloco de guias pai.

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### Subguias
Para guias dentro de guias, `subtabs` e `subtab` podem ser usados. A configuração padrão é `local`.
Para `subtabs` globais, use a opção `global`: {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
conteúdo da guia 1
{% subtabs %}
{% subtab Subtab 1a %}
Conteúdo da subguia 1a
{% endsubtab %}
{% subtab Subtab 2a %}
Conteúdo da subguia 2a
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
conteúdo da guia 2
{% subtabs %}
{% subtab Subtab 1b %}
Conteúdo da subguia 1b
{% endsubtab %}
{% subtab Subtab 2b %}
Conteúdo da subguia 2b
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