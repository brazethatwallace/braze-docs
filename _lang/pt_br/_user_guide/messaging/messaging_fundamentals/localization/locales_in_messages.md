---
nav_title: Mensagens multilíngues
article_title: Mensagens multilíngues
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artigo fornece etapas sobre como usar locais nas suas mensagens."
---

# Mensagens multilíngues {#multi-language-messages}

> Depois de adicionar locais ao seu espaço de trabalho, você pode direcionar usuários em diferentes idiomas, tudo dentro de um único push, e-mail, banner, mensagem no app ou Content Block.

## Pré-requisitos {#prerequisites}

Assista ao vídeo a seguir para uma visão geral opcional sobre como configurar e usar mensagens multilíngues.

{% multi_lang_include video.html id="whfstwrel5" source="wistia" %}

{% tabs %}
{% tab Locais multilíngues %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Tipos de mensagem %}

| Recurso | Permissões de usuário necessárias |
| --- | --- |
| Tipos&nbsp;de&nbsp;mensagem | Você precisa destas permissões para adicionar locais e traduções a Campaigns e Canvas:<br><br> <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos"}

{% endtab %}
{% tab Modelos %}

| Recurso | Permissões de usuário necessárias |
| --- | --- |
| Modelos | Você precisa destas permissões para o tipo de modelo ao qual deseja adicionar locais e traduções:<br><br> <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% endtabs %}

## Usar locais {#use-locales}

### Etapa 1: Configurar locais {#step-1-set-up-locales}

Antes de adicionar traduções a uma mensagem, você deve primeiro [criar os locais que deseja suportar]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings). Os locais definem as variantes de idioma (e opcionalmente região) disponíveis para envio de mensagens.

### Etapa 2: Marcar conteúdo para tradução {#step-2-mark-content-for-translation}

Envolva o texto que deseja traduzir com as tags de tradução Liquid {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} e atribua um ID de tag. Os IDs das tags de tradução devem ser únicos dentro de uma mensagem. Considere usar nomes de ID semânticos que descrevam claramente o texto, como {% raw %}`{% translation header %}`{% endraw %}.

Aqui está um exemplo de mensagem marcada para tradução: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Selecione o texto que deseja traduzir e use o atalho de teclado **Cmd + Alt + L** (macOS) ou **Ctrl + Alt + L** (Windows) para envolvê-lo em tags de tradução.<br><br> Esse atalho funciona em todos os canais que suportam mensagens multilíngues, exceto nos editores de arrastar e soltar para e-mail e Content Blocks. Para esses, use o botão **Add personalization** para adicionar tags de tradução.
{% endalert %}

#### Localizar URLs {#localize-urls}

Ao traduzir conteúdo, URLs exigem tratamento especial para evitar links quebrados.

##### URLs padrão (estáticas) {#standard-static-urls}

URLs estáticas são inseridas manualmente no editor (por exemplo, `https://example.com`). Também recomendamos o seguinte:

| Recomendação | Motivo |
| --- | --- |
| Mantenha o protocolo (`https://`) fora das tags de tradução. Envolva apenas o domínio e o caminho (por exemplo, `example.com/en`). | Tradutores podem alterar ou remover acidentalmente caracteres especiais, causando links quebrados. |
| Não inclua parâmetros de consulta dentro das tags de tradução (por exemplo, `?utm_source=promo`). | Tradutores podem alterar ou remover acidentalmente caracteres especiais, resultando em links quebrados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs padrão (estáticas)" }

Uma URL padrão que segue ambas as recomendações é:

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### URLs geradas por Liquid {#liquid-generated-urls}

Se sua URL é gerada com Liquid (por exemplo, {% raw %}`{% landing_page_url %}`{% endraw %}), recomendamos o seguinte:

| Recomendação | Motivo |
| --- | --- |
| Envolva a URL gerada por Liquid em tags de tradução somente se ela precisar ser localizada. | A sintaxe Liquid deve ser cuidadosamente preservada para renderizar corretamente. |
| Não inclua parâmetros de consulta (por exemplo, `?utm_source=promo`) dentro das tags de tradução. | Tradutores podem alterar ou remover acidentalmente caracteres especiais, resultando em links quebrados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs geradas por Liquid" }

Uma URL gerada por Liquid que segue ambas as recomendações é:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
Se você está usando [rastreamento de links de e-mail](#email-link-tracking) (alias de link ou modelos de link), é necessária configuração adicional quando URLs estão envolvidas em tags de tradução.
{% endalert %}

#### Atributos e estrutura HTML {#html-attributes-and-structure}

Envolva apenas texto legível por humanos em tags de tradução. Evite envolver atributos HTML (como `class`, `style` ou `id`) ou outro código estrutural. Atributos HTML controlam layout, estilo e funcionalidade. Envolvê-los em tags de tradução pode quebrar a formatação ou os estilos nas versões localizadas da sua mensagem.

Este texto está corretamente envolvido:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Texto envolvido incorretamente %}

Este texto está envolvido **incorretamente**:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### Etapa 3: Adicionar locais à sua mensagem {#step-3-add-locales-to-your-message}

Depois de adicionar tags de tradução à sua mensagem, selecione **Manage languages** no editor (**Languages** nos editores de arrastar e soltar para e-mail e Content Blocks) e selecione pelo menos um local para o qual deseja adicionar traduções.

![O menu suspenso Add locale com opções para selecionar o local padrão ou atributos personalizados.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks com traduções {#content-blocks-containing-translation}

Se sua mensagem contém Content Blocks que já possuem traduções salvas, você não precisa fazer upload dessas traduções novamente. As traduções salvas são aplicadas automaticamente quando o Content Block é adicionado à sua mensagem.

No modal **Manage languages**, Content Blocks com traduções salvas aparecem na lista, junto com os locais que suportam. Isso permite que você veja quais partes da sua mensagem já estão localizadas antes de adicionar novas traduções.

![A seção Manage languages com uma lista de Content Blocks que possuem traduções salvas.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Certifique-se de que cada Content Block inclua traduções para todos os locais adicionados à sua mensagem. Se um Content Block não tiver traduções para um dos locais que você adicionou, ele será exibido no idioma original para os usuários daquele local.
{% endalert %}

### Etapa 4: Adicionar traduções {#step-4-add-translations}

Depois de selecionar os locais, adicione traduções à sua mensagem usando um dos seguintes métodos:

![A guia Adicionar traduções com opções para fazer upload de traduções por CSV ou conectando-se a parceiros de tradução.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Fazer upload de modelo CSV %}

Selecione **Download template** para baixar um CSV contendo uma matriz dos seus IDs de tradução selecionados e locais. Insira as traduções para cada local. Faça upload do arquivo completo e as traduções serão aplicadas à sua mensagem.

{% alert important %}
Para evitar problemas de exibição com caracteres não ingleses, evite usar o Excel para o seu CSV de tradução.
{% endalert %}

![CSV com tags de tradução para título, texto da oferta, valor da oferta e CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Usar a API de tradução %}

Use uma API de tradução de parceiro para gerenciar e atualizar traduções nas suas Campaigns e Canvas. Isso é útil se você usa um sistema externo para localização ou deseja se conectar diretamente com um parceiro de tradução.

Para usar os endpoints de tradução com Canvas, inclua os seguintes parâmetros:
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Ao usar a API de tradução com etapas do Canvas que foram criadas após o lançamento do Canvas, o `message_variation_id` que você passa para a API estará vazio ou em branco.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Pré-visualizar traduções {#step-5-preview-translations}

Para pré-visualizar sua mensagem, selecione a opção **Multi-Language User** no menu suspenso **Preview as User**. Isso permite que você alterne entre diferentes definições de local para pré-visualizar todas as traduções da sua mensagem.

![Pré-visualizações de locais]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Gerenciar traduções {#manage-translations}

### Duplicar etapas do Canvas ou Campaigns e traduções {#duplicate-canvas-steps-or-campaigns-and-translations}

Quando você duplica uma etapa do Canvas, uma Campaign ou uma variante, as traduções são incluídas. Isso também vale ao copiar entre espaços de trabalho, desde que os locais estejam definidos no espaço de trabalho de destino. Certifique-se de revisar e atualizar as traduções ao fazer modificações no seu Canvas ou Campaign.

### Salvar traduções em Content Blocks {#save-translations-in-content-blocks}

Content Blocks suportam multilíngue da mesma forma que as mensagens. Ao criar ou editar Content Blocks, você pode marcar conteúdo para tradução, adicionar locais e fazer upload de traduções usando um CSV ou a [API de tradução]({{site.baseurl}}/api/endpoints/translations).

As traduções salvas permanecem associadas ao Content Block. Quando o bloco é adicionado a uma mensagem, suas traduções são incluídas automaticamente.

### Mensagens da direita para a esquerda {#right-to-left-messages}

Ao preencher o arquivo de tradução para idiomas escritos da direita para a esquerda (como árabe), envolva a tradução com `span` para que seja formatada corretamente:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Rastreamento de links de e-mail {#email-link-tracking}

Em Campaigns de e-mail, a Braze rastreia links adicionando informações de rastreamento (parâmetros de consulta) a cada URL. Esse comportamento suporta tanto [alias de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) quanto [modelos de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).

Quando uma URL está envolvida em tags de tradução, a Braze pode não conseguir determinar onde adicionar essas informações de rastreamento. Para garantir que isso funcione corretamente, você deve incluir um caractere especial no final da URL para indicar onde o rastreamento deve ser adicionado.

URLs usam dois caracteres especiais para controlar como isso funciona:
  - `?` adiciona rastreamento a uma URL que ainda não o possui.
  - `&` adiciona rastreamento adicional se um `?` já estiver presente na URL. Uma URL pode conter apenas um `?`.

| URL | Contém&nbsp;`?` | Descrição | Exemplo |
| --- | --- | --- | --- |
| URL padrão | Não | Adicione `?` após a tag de tradução de fechamento se a URL ainda não contiver um. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL padrão | Sim | Use `&` no final da URL (após a tag de tradução de fechamento) se ela já contiver `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Gerada por Liquid | Não | Use `?` após as tags de tradução de fechamento se a URL gerada ainda não contiver um. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Gerada por Liquid | Sim | Use `&` após a tag de tradução de fechamento se a URL gerada já contiver um `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Rastreamento de links de e-mail" }

### Configurações de idioma e acessibilidade {#language-settings-and-accessibility}

Comece com [Idioma de acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) em [Acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) para contexto WCAG, comportamento de canal e editor (incluindo landing pages) e configurações de **Accessibility** no nível da mensagem.

Ao usar **mensagens multilíngues**, alinhe o idioma de acessibilidade com cada local para que os envios localizados declarem o idioma apropriado.

#### Configurar o idioma de acessibilidade {#configuring-the-accessibility-language}

Você pode definir o idioma de acessibilidade em dois níveis:

##### Nível da mensagem {#message-level}

No nível da mensagem, defina o idioma de acessibilidade na seção **Accessibility** das configurações da sua mensagem. Para selecionar um idioma, usar Liquid e limitações por canal, consulte [Idioma de acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language).

##### Nível do local {#locale-level}

Para mensagens multilíngues, defina o idioma de acessibilidade para cada local nas **Configurações de localização**. Você pode usar {% raw %}`{{accessibility_language}}`{% endraw %} na seção **Accessibility** para que o idioma do documento ou cartão seja mapeado para os valores desses locais.

Se esse token aparece por padrão em novas mensagens depende do canal e do editor. Por exemplo, mensagens no app e banners se comportam de forma diferente de landing pages e e-mails de arrastar e soltar. Consulte [Idioma de acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) para mais detalhes.

## Perguntas frequentes {#frequently-asked-questions}

### Quais são os limites para tags de tradução? {#what-are-the-limits-for-translation-tags}

Ao usar tags de tradução, os seguintes limites se aplicam:

- Cada mensagem pode ter até 200 tags de tradução.
- Cada texto padrão (o conteúdo entre as tags de tradução) pode ter até 2.000 caracteres.
- As traduções por local podem ter até 409.600 bytes (aproximadamente 409,6&nbsp;KB).

#### Posso fazer uma alteração na cópia traduzida em um dos meus locais? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

Sim. Primeiro, faça a edição no CSV e depois faça upload do arquivo novamente para alterar a cópia traduzida.

### A Braze fornece traduções? {#does-braze-provide-translations}

Não. Você deve [fornecer suas próprias traduções](#step-4-add-translations) fazendo upload de um CSV ou usando a API de tradução.

### Posso aninhar tags de tradução? {#can-i-nest-translation-tags}

Não.

#### Posso envolver mensagens HTML inteiras em uma tag de tradução? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

Não. Como boa prática, você deve envolver apenas texto legível por humanos ou conteúdo que precisa ser localizado. Isso ajuda a evitar formatação quebrada, links ou outros elementos não textuais.

Além disso, considere envolver partes menores e semanticamente relacionadas do texto para criar traduções precisas e evitar limitações de desempenho ou tamanho.

#### Posso fazer uma alteração na cópia traduzida em um dos meus locais?

Sim. Se estiver usando um CSV, primeiro faça a edição no arquivo e depois faça upload novamente para alterar a cópia traduzida. Se estiver usando a [API de tradução]({{site.baseurl}}/api/endpoints/translations), use os endpoints de atualização para fazer alterações.

#### Quais validações ou verificações adicionais a Braze realiza? {#what-validations-or-extra-checks-does-braze-do}

| Cenário | Validação na Braze |
| --- | --- |
| Uma mensagem contém dois ou mais IDs de tradução correspondentes que mapeiam para textos diferentes. | Este arquivo de tradução não será baixado. |
| Um arquivo de tradução está sem um ou mais IDs de tag de tradução. | Este arquivo de tradução não será enviado. |
| Um arquivo de tradução contém locais que estão ausentes na mensagem. | Este arquivo de tradução não será enviado. |
| Tags de tradução devem ser adicionadas a uma mensagem antes de baixar o modelo de tradução. | Este arquivo de tradução não será baixado. |
| Tags de tradução encontradas no arquivo enviado estão ausentes na sua mensagem. | Traduções extras não serão salvas na mensagem. |
| {% raw %}Uma mensagem contém uma ou mais tags Liquid quebradas. Para abrir tags, use `{% translation your_id_here %}`, feche tags de tradução com `{% endtranslation %}`.{% endraw %} | Este arquivo de tradução não será baixado. |
| Um arquivo de tradução contém texto padrão que não corresponde ao que está na mensagem. | As traduções são adicionadas, mas o texto original da mensagem não é atualizado. |
| Um ou mais locais em uma mensagem foram excluídos nas configurações e não existem mais. | Traduções que já foram adicionadas continuam a existir dentro da mensagem. Se excluídas da mensagem, as traduções são perdidas. |
| Tags de tradução contêm URLs completas ou URLs geradas por Liquid. | Tags de tradução contendo URLs são identificadas caso ocorram problemas com links quebrados ou rastreamento de links. |
| Tags de tradução incluem parâmetros de consulta. | Tags de tradução contendo parâmetros de consulta são identificadas caso ocorram problemas com links quebrados ou rastreamento de links. |
| Tags de tradução contêm atributos ou estruturas HTML. | Tags de tradução contendo atributos ou estruturas HTML são identificadas caso ocorram problemas com estilos e formatação. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quais validações ou verificações adicionais a Braze realiza?" }