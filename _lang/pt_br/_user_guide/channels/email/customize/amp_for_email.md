---
nav_title: "AMP para e-mail"
article_title: "AMP para e-mail"
alias: /amphtml/
page_order: 11
description: "Este artigo de referência oferece uma visão geral do AMP para e-mail e casos de uso comuns."
channel:
  - email

---

# AMP para e-mail {#amp-for-email}

> Com o [AMP para e-mail](https://amp.dev/about/email), você pode adicionar elementos interativos aos seus e-mails e elevar a comunicação com seus clientes, entregando uma experiência completa diretamente na caixa de entrada do usuário. O AMP torna isso possível por meio de diversos componentes que podem ser usados para criar ofertas de e-mail envolventes, como pesquisas, questionários de feedback, campanhas de votação, avaliações, centros de inscrição e muito mais. Ferramentas como essas podem oferecer oportunidades para aumentar o engajamento e a retenção.

## Requisitos {#requirements}

A Braze não é responsável pelo registro dos usuários no Google nem pelo cumprimento dos requisitos de segurança necessários. O AMP para e-mail está disponível apenas para SparkPost e SendGrid.

| Requisito   | Descrição |
| --------------| ----------- |
| AMP para e-mail ativado | O AMP está disponível para todos os usuários. |
| Capacitação da conta do Gmail | Consulte [Ativando a conta do Gmail](#enabling-gmail-account). |
| Autenticação de remetente do Google | O Gmail [autentica o remetente](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) de e-mails AMP com DKIM, SPF e DMARC. Esses protocolos devem estar configurados na sua conta. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| Elementos de e-mail AMP | Um e-mail AMP atraente inclui o uso estratégico de diversos componentes. Consulte a guia Essenciais na seção [Componentes](#components) abaixo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

### Clientes de e-mail compatíveis {#supported-email-clients}

Antes de enviar e-mails AMP para os usuários, você precisa se registrar nos nossos clientes de e-mail. O processo de registro envolve o envio de um e-mail de teste em AMP HTML para aprovação. Os tempos de aprovação variam de cliente para cliente. Siga os links de registro para mais informações.

| Cliente | Link de registro |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported email clients" }

Para uma lista completa de clientes de e-mail compatíveis, consulte a [documentação do AMP](https://amp.dev/support/faq/email-support).

### Ativando a conta do Gmail {#enabling-gmail-account}

Acesse as configurações do Gmail e selecione **Ativar e-mail dinâmico** na guia **Geral**.

![Um exemplo das configurações do Gmail com a caixa de seleção "Ativar e-mail dinâmico" marcada.]({% image_buster /assets/img/dynamic-content.png %})

## Uso da API {#api-usage}

Você também pode usar o AMP para e-mail com a nossa API. Se você usar qualquer um dos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) da Braze para enviar um e-mail, adicione `amp_body` como uma especificação de objeto, conforme mostrado abaixo.

### Especificação do objeto de e-mail {#email-object-specification}

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Criando seu e-mail AMP {#create-your-amp-email}

Primeiro, crie seu e-mail AMP usando [componentes](#components). Em seguida, use a [API da Braze](#api-usage) para enviar sua mensagem, incluindo `amp_body` para o seu AMP HTML.

Além do AMP HTML, exigimos uma versão HTML regular em `body` e sugerimos uma versão `plaintext_body` do seu e-mail AMP. Todos os e-mails AMP são enviados em formato multipart, o que significa que a Braze envia um e-mail que suporta HTML, texto simples e AMP HTML. Isso é útil caso seu e-mail seja enviado por um provedor que ainda não suporta AMP para e-mail, pois o e-mail será automaticamente exibido na versão apropriada com base no usuário e no dispositivo.

{% alert note %}
Ao criar um e-mail AMP, verifique se você está no editor AMP, pois o código AMP não deve ser adicionado ao editor de HTML.
{% endalert %}

Consulte estes recursos adicionais:

- [Tutorial do AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Código de exemplo](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) para ver como o produto final deve ficar.
- [Biblioteca de componentes de e-mail AMP](https://amp.dev/documentation/components/?format=email/)

### Componentes {#components}

Ao criar os elementos AMP, recomendamos que você consulte sua equipe de engenharia e inclua recursos de design e elementos para um acabamento extra.

{% tabs %}
  {% tab Essenciais %}

Cada um desses elementos é obrigatório no corpo do seu e-mail AMP.

| Componente | Descrição | Exemplo |
|---------|--------------|---------|
| Identificação <br><br> `⚡4email` ou `amp4email`| Identifica seu e-mail como um e-mail AMP HTML. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Carregar runtime do AMP <br><br> `<script>` | Permite que o AMP funcione no seu e-mail usando JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS Boilerplate | Oculta o conteúdo até que o AMP seja carregado. <br> Provedores de e-mail que suportam e-mails AMP aplicam verificações de segurança que permitem apenas scripts AMP verificados em seus clientes. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

  {% endtab %}
  {% tab Dinâmico %}

Use esses componentes para criar layouts e comportamentos dinâmicos nos seus e-mails.

| Componente | Descrição | Script obrigatório |
|---------|--------------|---------|
| [Accordion](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Permite que os usuários visualizem o resumo do conteúdo e naveguem para qualquer seção. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulários](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Cria formulários para enviar campos de entrada em um documento AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

{% alert note %}
Qualquer componente que exija autenticação do usuário deve usar [tokens de acesso do Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [tokens de asserção de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Criativo %}

  Dê um toque especial com os componentes do AMP que podem ajudar a personalizar seu e-mail para o seu público.

| Componente | Descrição | Script obrigatório |
|---------|--------------|---------|
| [Imagem animada](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Exibe uma imagem animada (geralmente um GIF) gerenciada via runtime. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrossel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Exibe vários conteúdos semelhantes ao longo de um eixo horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Imagem](https://amp.dev/documentation/components/amp-img?format=email) | Uma substituição gerenciada via runtime para a tag HTML `img`. <br>  Você também pode criar um [lightbox para sua imagem](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

{% alert note %}
Qualquer componente que exija autenticação do usuário deve usar [tokens de acesso do Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [tokens de asserção de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Outros %}

| Componente | Descrição |
|---------|--------------|
| [Data Binding e expressões](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Adiciona interatividade personalizada com estado às suas páginas AMP por meio de data binding e expressões semelhantes a JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Components" }

{% alert note %}
Qualquer componente que exija autenticação do usuário deve usar [tokens de acesso do Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [tokens de asserção de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

Para uma lista completa de componentes AMP, confira a [documentação do AMP](https://amp.dev/documentation/components/?format=email).

### Casos de uso {#use-cases}

{% tabs local %}
{% tab Pesquisas interativas %}

Usando o componente `<amp-form>`, você pode criar pesquisas interativas que podem ser respondidas sem sair da caixa de entrada do e-mail. Isso pode ser feito usando `<amp-form>` para enviar a resposta da pesquisa e, em seguida, fazer com que seu backend forneça esses dados agregados.

Alguns exemplos incluem:
* E-mail de pesquisa de conferência
* Atualização dinâmica de itens no feed
* E-mail de favoritos de artigos

Com esse componente, os usuários podem enviar ou limpar valores de campos. Além disso, dependendo de como você configurar seu e-mail, é possível fornecer avisos adicionais aos usuários, como se o envio da pesquisa foi bem-sucedido, ou exibir as respostas dos usuários mostrando os resultados da pesquisa (como uma campanha de votação).

{% endtab %}
{% tab Conteúdo recolhível %}

Expanda suas seções de conteúdo usando o componente `<amp-accordion>`. Esse componente permite exibir seções de conteúdo recolhíveis e expansíveis, oferecendo uma maneira para os leitores visualizarem o resumo do conteúdo e navegarem para qualquer seção.

Se você costuma enviar artigos educacionais longos ou recomendações personalizadas, isso oferece uma maneira para os leitores visualizarem o resumo do conteúdo e navegarem para qualquer seção ou recomendação de produto específica para obter mais detalhes. Isso pode ser particularmente útil para usuários de dispositivos móveis, onde até mesmo algumas frases em uma seção já exigem rolagem.
{% endtab %}
{% tab E-mails com muitas imagens %}

Se você costuma enviar e-mails com muitas fotos profissionais, como marcas de varejo, pode usar o componente `<amp-image-lightbox>`, que permite que os usuários interajam com uma imagem que os atraia. Quando o usuário clica na imagem, esse componente exibe a imagem no centro da mensagem, criando um efeito de lightbox.

Além disso, o componente `<amp-image-lightbox>` permite que o usuário visualize uma descrição detalhada da imagem. Você pode usar o mesmo componente para mais de uma imagem. Por exemplo, se você tiver várias imagens incluídas no seu e-mail, quando o usuário clicar em qualquer uma delas, a imagem será exibida no lightbox.

{% endtab %}
{% tab E-mails baseados em texto %}

Para e-mails que dependem principalmente de texto, o componente `<amp-fit-text>` permite gerenciar o tamanho e o ajuste do texto dentro de uma área especificada.

Exemplos incluem:

- Dimensionar o texto para caber em uma área
- Dimensionar o texto para caber na área usando um tamanho máximo de fonte, onde você pode definir o tamanho máximo da fonte
- Truncar o texto quando o conteúdo excede a área

{% endtab %}
{% endtabs %}

### Usando amp-mustache {#use-amp-mustache}

Assim como o Liquid, o AMP suporta uma linguagem de script para casos de uso mais avançados. Esse componente é chamado [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). Ao incluir qualquer linguagem de marcação Mustache, você precisará envolvê-la com a tag [`raw`](https://shopify.github.io/liquid/tags/raw/) do Liquid. Note que o Liquid e o Mustache compartilham o mesmo estilo de sintaxe.

Ao envolver seu conteúdo com a tag `raw`, o mecanismo de processamento da Braze ignorará qualquer conteúdo entre as tags `raw` e enviará a variável Mustache que sua equipe precisa.

## Métricas e análise de dados {#metrics-and-analytics}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Metrics and analytics">
  <caption>Métricas e análise de dados</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Informações</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total de aberturas</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} Para e-mails AMP, esse é o total de aberturas das versões HTML e texto simples.</td>
        </tr>
        <tr>
            <td class="no-split">Total de cliques</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} Para e-mails AMP, esse é o total de cliques nas versões HTML e texto simples.</td>
        </tr>
        <tr>
            <td class="no-split">Aberturas AMP</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">Cliques AMP</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Testes e solução de problemas {#test-and-troubleshoot}


Antes de enviar seu e-mail AMP, recomendamos:

- Testar de acordo com estas [diretrizes do Gmail](https://developers.google.com/gmail/ampemail/testing-dynamic-email).
- Usar o [Gmail AMP for Email Playground](https://amp.gmail.dev/playground/) para validar a marcação AMP.
  - Se o seu e-mail AMP usar Liquid tags, substitua-as por valores estáticos de placeholder antes de colar no Gmail AMP for Email Playground. Liquid tags não renderizadas causam erros de validação.

Para que seu e-mail AMP seja entregue a qualquer conta do Gmail, o e-mail deve atender às seguintes condições:

- Os requisitos de segurança do AMP para e-mail devem ser cumpridos.
- A parte MIME do AMP deve conter um documento AMP válido.
- O e-mail deve incluir a parte MIME do AMP antes da parte MIME do HTML.
- A parte MIME do AMP deve ter menos de 100&nbsp;KB.

Observe que o total de cliques e os cliques únicos não contabilizam cliques que ocorrem em uma mensagem AMP (apenas HTML e texto simples). Os cliques específicos do AMP são atribuídos à métrica *amp_click*.

Se nenhuma dessas condições estiver causando o erro, entre em contato com o [Suporte]({{site.baseurl}}/support_contact/).

### Configurar a caixa de entrada do Gmail para renderizar e-mails AMP {#configure-gmail-inbox-to-render-amp-emails}

Você pode configurar sua caixa de entrada do Gmail para renderizar e-mails AMP para fins de teste seguindo os passos abaixo:

1. No Gmail, selecione **Configurações** no canto superior direito da sua caixa de entrada.
2. Selecione **Ver todas as configurações**.
3. Na guia **Geral**, vá até a seção **E-mail dinâmico** e confirme que a caixa de seleção **Ativar e-mail dinâmico** está marcada.
4. Em seguida, selecione **Configurações de desenvolvedor** e marque a caixa de seleção **Sempre permitir e-mails dinâmicos deste remetente:**.
5. Insira o mesmo domínio do endereço de remetente da sua mensagem de teste.
6. Salve suas alterações.

Agora você pode enviar o e-mail de teste para sua conta do Gmail, e os e-mails AMP devem ser renderizados no Gmail.

### Perguntas frequentes {#frequently-asked-questions}

#### Devo segmentar com e-mails AMP? {#should-i-segment-with-amp-emails}

Recomendamos não segmentar para enviar a todos os diferentes tipos de usuários. Isso porque enviamos mensagens AMP em formato multipart, com diferentes versões incluídas no e-mail original. Se um usuário não conseguir ver a versão AMP, o e-mail será exibido automaticamente na versão HTML.