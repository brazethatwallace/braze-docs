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

{% tabs %}
{% tab Locais multilíngues %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Tipos de mensagem %}

| Recurso | Permissões de usuário necessárias |
| --- | --- |
| Tipos de&nbsp;mensagem | Você precisa dessas permissões para adicionar locais e traduções a Campaigns e Canvas:<br><br> {::nomarkdown} <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos"}

{% endtab %}
{% tab Modelos %}

| Recurso | Permissões de usuário necessárias |
| --- | --- |
| Modelos | Você precisa dessas permissões para o tipo de modelo ao qual deseja adicionar locais e traduções:<br><br> {::nomarkdown} <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% endtabs %}

## Usar locais {#use-locales}

### Etapa 1: Configurar locais {#step-1-set-up-locales}

Antes de adicionar traduções a uma mensagem, você deve primeiro [criar os locais que deseja suportar]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings). Os locais definem as variantes de idioma (e opcionalmente região) disponíveis para o envio de mensagens.

### Etapa 2: Marcar conteúdo para tradução {#step-2-mark-content-for-translation}

Envolva o texto que deseja traduzir com as tags de tradução Liquid {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} e atribua um ID de tag. Os IDs das tags de tradução devem ser únicos dentro de uma mensagem. Considere usar nomes de ID semânticos que descrevam claramente o texto, como {% raw %}`{% translation header %}`{% endraw %}.

Aqui está um exemplo de mensagem marcada para tradução: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Destaque o texto que deseja traduzir e use o atalho de teclado **Cmd + Alt + L** (macOS) ou **Ctrl + Alt + L** (Windows) para envolver com tags de tradução.<br><br> Esse atalho funciona em todos os canais que suportam envio de mensagens multilíngue, exceto nos editores de arrastar e soltar para e-mail e Content Blocks. Para esses, use o botão **Adicionar personalização** para adicionar tags de tradução.
{% endalert %}

#### Localizar URLs {#localize-urls}

Ao traduzir conteúdo, as URLs exigem tratamento especial para evitar links quebrados.

##### URLs padrão (estáticas) {#standard-static-urls}

URLs estáticas são inseridas manualmente no editor (por exemplo, `https://example.com`). Também recomendamos o seguinte:

| Recomendação | Justificativa |
| --- | --- |
| Mantenha o protocolo (`https://`) fora das tags de tradução. Envolva apenas o domínio e o caminho (por exemplo, `example.com/en`). | Os tradutores podem alterar ou remover acidentalmente caracteres especiais, causando links quebrados. |
| Não inclua parâmetros de consulta dentro das tags de tradução (por exemplo, `?utm_source=promo`). | Os tradutores podem alterar ou remover acidentalmente caracteres especiais, resultando em links quebrados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs padrão (estáticas)" }

Uma URL padrão que segue ambas as recomendações é:

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### URLs geradas por Liquid {#liquid-generated-urls}

Se a sua URL é gerada com Liquid (por exemplo, {% raw %}`{% landing_page_url %}`{% endraw %}), recomendamos o seguinte:

| Recomendação | Justificativa |
| --- | --- |
| Envolva a URL gerada por Liquid em tags de tradução somente se ela precisar ser localizada. | A sintaxe Liquid deve ser cuidadosamente preservada para renderizar corretamente. |
| Não inclua parâmetros de consulta (por exemplo, `?utm_source=promo`) dentro das tags de tradução. | Os tradutores podem alterar ou remover acidentalmente caracteres especiais, resultando em links quebrados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs geradas por Liquid" }

Uma URL gerada por Liquid que segue ambas as recomendações é:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
Se você está usando [rastreamento de links de e-mail](#email-link-tracking) (alias de link ou modelos de link), é necessária configuração adicional quando as URLs estão envolvidas em tags de tradução.
{% endalert %}

#### Atributos e estrutura HTML {#html-attributes-and-structure}

Envolva apenas texto legível por humanos em tags de tradução. Evite envolver atributos HTML (como `class`, `style` ou `id`) ou outro código estrutural. Os atributos HTML controlam layout, estilo e funcionalidade. Envolvê-los em tags de tradução pode quebrar a formatação ou os estilos nas versões localizadas da sua mensagem.

Este texto está corretamente envolvido:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Texto envolvido incorretamente %}

Este texto está **incorretamente** envolvido:

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

Após adicionar tags de tradução à sua mensagem, selecione **Gerenciar idiomas** no editor (**Idiomas** nos editores de arrastar e soltar para e-mail e Content Blocks) e selecione pelo menos um local para o qual deseja adicionar traduções.

![O menu suspenso Adicionar local com opções para selecionar o local padrão ou atributos personalizados.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks com traduções {#content-blocks-containing-translation}

Se a sua mensagem contém Content Blocks que já possuem traduções salvas, você não precisa reenviar essas traduções. As traduções salvas são aplicadas automaticamente quando o Content Block é adicionado à sua mensagem.

No modal **Gerenciar idiomas**, os Content Blocks com traduções salvas aparecem na lista, junto com os locais que suportam. Isso permite que você veja quais partes da sua mensagem já estão localizadas antes de adicionar novas traduções.

![A seção Gerenciar idiomas com uma lista de Content Blocks que possuem traduções salvas.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Certifique-se de que cada Content Block inclua traduções para todos os locais adicionados à sua mensagem. Se um Content Block não tiver traduções para um dos locais que você adicionou, ele será exibido no idioma original para os usuários nesse local.
{% endalert %}

### Etapa 4: Adicionar traduções {#step-4-add-translations}

Após selecionar os locais, adicione traduções à sua mensagem usando um dos seguintes métodos:

![A guia Adicionar traduções com opções para enviar traduções por CSV ou conectar-se a parceiros de tradução.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Enviar modelo CSV %}

Selecione **Baixar modelo** para baixar um CSV contendo uma matriz dos seus IDs de tradução e locais selecionados. Insira as traduções para cada local. Envie o arquivo preenchido e as traduções serão aplicadas à sua mensagem.

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

Para pré-visualizar sua mensagem, selecione a opção **Usuário multilíngue** no menu suspenso **Pré-visualizar como usuário**. Isso permite que você alterne entre diferentes definições de local para pré-visualizar todas as traduções da sua mensagem.

![Prévias de locais]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Gerenciar traduções {#manage-translations}

### Duplicar etapas do Canvas ou Campaigns e traduções {#duplicate-canvas-steps-or-campaigns-and-translations}

Quando você duplica uma etapa do Canvas, uma Campaign ou uma variante, as traduções são incluídas. Isso também vale ao copiar entre espaços de trabalho, desde que os locais estejam definidos no espaço de trabalho de destino. Revise e atualize as traduções quando fizer modificações no seu Canvas ou Campaign.

### Salvar traduções em Content Blocks {#save-translations-in-content-blocks}

Os Content Blocks oferecem suporte a vários idiomas da mesma forma que as mensagens. Ao criar ou editar Content Blocks, você pode marcar conteúdo para tradução, adicionar locais e fazer upload de traduções usando um CSV ou a [API de tradução]({{site.baseurl}}/api/endpoints/translations).

As traduções salvas permanecem associadas ao Content Block. Quando o bloco é adicionado a uma mensagem, suas traduções são incluídas automaticamente.

### Mensagens da direita para a esquerda {#right-to-left-messages}

Ao preencher o arquivo de tradução para idiomas escritos da direita para a esquerda (como árabe), envolva a tradução com `span` para que seja formatada corretamente:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Rastreamento de links em e-mail {#email-link-tracking}

Em Campaigns de e-mail, a Braze rastreia links adicionando informações de rastreamento (parâmetros de consulta) a cada URL. Esse comportamento oferece suporte tanto ao [alias de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) quanto ao [modelo de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).

Quando uma URL está envolvida em tags de tradução, a Braze pode não conseguir determinar onde adicionar essas informações de rastreamento. Para garantir que isso funcione corretamente, você deve incluir um caractere especial no final da URL para indicar onde o rastreamento deve ser adicionado.

As URLs usam dois caracteres especiais para controlar como isso funciona:
  - `?` adiciona rastreamento a uma URL que ainda não o possui.
  - `&` adiciona rastreamento adicional se um `?` já estiver presente na URL. Uma URL pode conter apenas um `?`.

| URL | Contém&nbsp;`?` | Descrição | Exemplo |
| --- | --- | --- | --- |
| URL padrão | Não | Adicione `?` após a tag de tradução de fechamento se a URL ainda não contiver um. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL padrão | Sim | Use `&` no final da URL (após a tag de tradução de fechamento) se ela já contiver `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Gerada por Liquid | Não | Use `?` após as tags de tradução de fechamento se a URL gerada ainda não contiver um. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Gerada por Liquid | Sim | Use `&` após a tag de tradução de fechamento se a URL gerada já contiver um `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Rastreamento de links em e-mail" }

### Configurações de idioma e acessibilidade {#language-settings-and-accessibility}

Comece com [Idioma de acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) em [Acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) para contexto de WCAG, comportamento de canal e editor (incluindo landing pages) e configurações de **Acessibilidade** no nível da mensagem.

Ao usar **mensagens em vários idiomas**, alinhe o idioma de acessibilidade com cada local para que os envios localizados declarem o idioma apropriado.

#### Configurar o idioma de acessibilidade {#configuring-the-accessibility-language}

Você pode definir o idioma de acessibilidade em dois níveis:

##### Nível da mensagem {#message-level}

No nível da mensagem, defina o idioma de acessibilidade na seção **Acessibilidade** das configurações da sua mensagem. Para selecionar um idioma, usar Liquid e conhecer as limitações por canal, consulte [Idioma de acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language).

##### Nível do local {#locale-level}

Para mensagens em vários idiomas, defina o idioma de acessibilidade para cada local em **Configurações de localização**. Você pode usar {% raw %}`{{accessibility_language}}`{% endraw %} na seção **Acessibilidade** para que o idioma do documento ou cartão seja mapeado para esses valores de local.

Se esse token aparece por padrão em novas mensagens depende do canal e do editor. Por exemplo, In-App Messages e Banners se comportam de forma diferente de landing pages e e-mails de arrastar e soltar. Consulte [Idioma de acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) para mais detalhes.

## Perguntas frequentes {#frequently-asked-questions}

### Quais são os limites para tags de tradução? {#what-are-the-limits-for-translation-tags}

Ao usar tags de tradução, os seguintes limites se aplicam:

- Cada mensagem pode ter até 200 tags de tradução.
- Cada texto padrão (o conteúdo entre as tags de tradução) pode ter até 2.000 caracteres.
- As traduções por localidade podem ter até 409.600 bytes (aproximadamente 409,6&nbsp;KB).

#### Posso fazer uma alteração no texto traduzido em uma das minhas localidades? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

Sim. Primeiro, faça a edição no CSV e depois faça o upload do arquivo novamente para alterar o texto traduzido.

### A Braze fornece traduções? {#does-braze-provide-translations}

Não. Você deve [fornecer suas próprias traduções](#step-4-add-translations) fazendo upload de um CSV ou usando a API de tradução.

### Posso aninhar tags de tradução? {#can-i-nest-translation-tags}

Não.

#### Posso envolver mensagens HTML inteiras em uma tag de tradução? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

Não. Como prática recomendada, você deve envolver apenas texto legível ou conteúdo que precisa ser localizado. Isso ajuda a evitar problemas com formatação, links ou outros elementos que não são texto.

Além disso, considere envolver partes menores e semanticamente relacionadas do texto para criar traduções precisas e evitar limitações de performance ou tamanho.

#### Posso fazer uma alteração no texto traduzido em uma das minhas localidades?

Sim. Se estiver usando um CSV, primeiro faça a edição no arquivo e depois faça o upload novamente para alterar o texto traduzido. Se estiver usando a [API de tradução]({{site.baseurl}}/api/endpoints/translations), use os endpoints de atualização para fazer alterações.

#### Quais validações ou verificações extras a Braze faz? {#what-validations-or-extra-checks-does-braze-do}

| Cenário | Validação na Braze |
| --- | --- |
| Uma mensagem contém dois ou mais IDs de tradução correspondentes que mapeiam para textos diferentes. | Este arquivo de tradução não será baixado. |
| Um arquivo de tradução está sem um ou mais IDs de tag de tradução. | Este arquivo de tradução não será enviado. |
| Um arquivo de tradução contém localidades que não existem na mensagem. | Este arquivo de tradução não será enviado. |
| As tags de tradução devem ser adicionadas a uma mensagem antes de baixar o modelo de tradução. | Este arquivo de tradução não será baixado. |
| Tags de tradução encontradas no arquivo enviado estão ausentes na sua mensagem. | As traduções extras não serão salvas na mensagem. |
| {% raw %}Uma mensagem contém uma ou mais tags Liquid com erro. Para abrir tags, use `{% translation your_id_here %}`, e feche tags de tradução com `{% endtranslation %}`.{% endraw %} | Este arquivo de tradução não será baixado. |
| Um arquivo de tradução contém texto padrão que não corresponde ao que está na mensagem. | As traduções são adicionadas, mas o texto original da mensagem não é atualizado. |
| Uma ou mais localidades em uma mensagem foram excluídas nas configurações e não existem mais. | As traduções que já foram adicionadas continuam existindo na mensagem. Se forem excluídas da mensagem, as traduções serão perdidas. |
| As tags de tradução contêm URLs completas ou URLs geradas por Liquid. | Tags de tradução contendo URLs são identificadas para o caso de ocorrerem problemas com links quebrados ou rastreamento de links. |
| As tags de tradução incluem parâmetros de consulta. | Tags de tradução contendo parâmetros de consulta são identificadas para o caso de ocorrerem problemas com links quebrados ou rastreamento de links. |
| As tags de tradução contêm atributos ou estruturas HTML. | Tags de tradução contendo atributos ou estruturas HTML são identificadas para o caso de ocorrerem problemas com estilos e formatação. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quais validações ou verificações extras a Braze faz?" }