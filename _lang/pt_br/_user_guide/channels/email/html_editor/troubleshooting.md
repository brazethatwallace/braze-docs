---
nav_title: Solução de problemas
article_title: Solução de problemas de e-mails HTML
page_order: 9
description: "Diagnostique problemas de renderização e do editor de e-mails HTML usando um índice de sintomas e etapas padrão de solução de problemas."
channel: email
---

# Solução de problemas de e-mails HTML {#troubleshoot-html-emails}

> Use esta página para resolver problemas comuns do editor de e-mail HTML e de envios de teste. Para Inbox Vision e entregabilidade, consulte [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) e [Configuração de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

Identifique seu sintoma na tabela para acessar a seção relevante.

| Sintoma | Acesse |
| --- | --- |
| O HTML do e-mail de teste parece errado | [HTML renderiza incorretamente em e-mails de teste](#html-renders-incorrectly-in-test-emails) |
| O editor se comporta de forma estranha no Chrome | [Conflitos de extensão](#extension-conflicts) |
| O e-mail aparece diferente em diferentes clientes | [Renderização de e-mail](#email-rendering) |
| O e-mail exibe código Liquid ou links quebrados | [HTML desbalanceado em modelos Liquid](#unbalanced-html-in-liquid-templates) |
| A prévia do Inbox Vision não corresponde ao e-mail enviado | [CSS inline](#css-inlining) |
| Espaços em branco ou linhas após imagens em e-mails de teste | [Espaço em branco abaixo de imagens](#white-space-under-images) |
| A análise de dados de cliques não inclui parâmetros de consulta | [Limitações da análise de dados de cliques em links](#link-click-analytics-limitations) |
| Sobrescritos causam espaçamento de linha inconsistente | [Problemas de altura de linha com sobrescrito](#superscript-line-height-issues) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de e-mail HTML" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho quando a renderização de e-mail HTML ou o comportamento do editor não corresponder ao esperado. Comece pela etapa 1.

1. Valide sua marcação HTML no editor ou em um validador externo.
2. Envie um [e-mail de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) e observe quais clientes de e-mail ou navegadores apresentam o problema.
3. Visualize com o [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) para comparar a renderização em diferentes clientes.
4. Descarte [conflitos com extensões de navegador](#extension-conflicts) caso o próprio editor apresente comportamento inesperado.
5. Se o problema persistir, abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) com capturas de tela do Inbox Vision e dos clientes afetados.

## HTML renderiza incorretamente em e-mails de teste {#html-renders-incorrectly-in-test-emails}

### Sintoma {#symptom}

Um [e-mail de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) não corresponde ao que você espera do editor.

Verifique primeiro a configuração do seu HTML e, em seguida, revise [conflitos de extensões](#extension-conflicts), [renderização de e-mail](#email-rendering), [inlining de CSS](#css-inlining) e [espaço em branco abaixo das imagens](#white-space-under-images).

### Conflitos de extensões {#extension-conflicts}

Certas extensões de navegador podem causar problemas com o editor de e-mail. Um exemplo é o [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) quando usado com o Google Chrome. Se você estiver usando uma dessas extensões, deve:

- Editar e-mails da Braze em um navegador que não tenha o Grammarly como extensão
- Entrar em contato com o gerente da sua conta na Braze e solicitar a troca dos editores de e-mail para somente HTML ou texto simples.

A visualização em texto simples remove o editor `WYSIWYG` (o que você vê é o que você obtém), então confirme primeiro que todos os membros da equipe estão confortáveis com HTML antes de fazer essa solicitação.

### Renderização de e-mail {#email-rendering}

Os e-mails são renderizados de forma diferente dependendo dos navegadores e clientes de e-mail, então anote em quais navegadores e clientes de e-mail você está enfrentando problemas.

- Pré-visualize seus e-mails usando o [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) para ver como seus e-mails aparecem em diferentes navegadores e clientes de e-mail.
- Depois de identificar quais navegadores ou clientes de e-mail estão causando problemas, informe sua equipe de desenvolvimento que será necessário modificar o HTML e fazer ajustes para acomodar esses navegadores ou clientes de e-mail.
- Se o problema for específico de [como o texto alternativo é exibido]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text), tenha em mente que esse comportamento é controlado pelo cliente de e-mail do destinatário, não pela Braze.

### HTML desbalanceado em modelos Liquid {#unbalanced-html-in-liquid-templates}

#### Sintoma

Alguns usuários recebem uma versão modificada do e-mail em que o código Liquid aparece na mensagem, links estão quebrados ou o espaçamento parece incorreto.

A Braze usa um parser HTML interno para preparar os e-mails antes do envio. Esse parser oferece suporte a recursos como geração de pré-cabeçalho, posicionamento de pixel de rastreamento, modelagem de links e aliasing de links. Quando as tags HTML não estão balanceadas dentro dos blocos de lógica Liquid ou Content Blocks correspondentes, o parser pode modificar o HTML subjacente de maneiras inesperadas. Isso pode resultar em:

- Quebras de linha do Liquid sendo renderizadas em alguns clientes de e-mail
- Espaçamento estranho causado por tags `<p>` adicionadas ao corpo do e-mail
- Conteúdo da tag `<head>` movido para o pré-cabeçalho
- Renderização inconsistente entre sistemas operacionais móveis
- Código específico de AMP removido dos corpos de e-mail AMP, causando falhas de validação
- Links quebrados quando muitos parâmetros de consulta ou media queries diferentes são usados

#### Balanceie o HTML dentro dos blocos Liquid {#balance-html-within-liquid-blocks}

Certifique-se de que todas as tags HTML abram e fechem dentro do bloco de lógica Liquid ou bloco de conteúdo correspondente. Isso evita que o parser interno interprete o HTML como inválido e o modifique.

#### Exemplo desbalanceado {#unbalanced-example}

{% raw %}
```liquid
<img src={% if ${language} == 'en' %}"https://example.com/images/banner-en.png" style="width: 100%"{% elsif ${language} == 'de' %}"https://example.com/images/banner-de.png"{% else %}"https://example.com/images/banner-default.png" {% endif %} />
```
{% endraw %}

Neste exemplo, a tag de abertura `<img` começa fora de qualquer bloco Liquid, e diferentes partes dos atributos da tag estão divididas entre instruções condicionais Liquid. Essa estrutura confunde o parser, que não consegue determinar onde a tag começa ou termina.

#### Exemplo balanceado {#balanced-example}

{% raw %}
```liquid
{% if ${language} == 'en' %}
  <img src="https://example.com/images/banner-en.png" style="width: 100%;" />
{% elsif ${language} == 'de' %}
  <img src="https://example.com/images/banner-de.png" style="width: 100%;" />
{% else %}
  <img src="https://example.com/images/banner-default.png" style="width: 100%;" />
{% endif %}
```
{% endraw %}

Na versão balanceada, cada Branch Liquid contém uma tag `<img>` completa e independente. Essa abordagem garante que o parser processe cada Branch corretamente.

#### Correções adicionais {#additional-fixes}

Se você estiver enfrentando problemas de renderização com media queries ou muitos parâmetros de consulta, tente desativar o inlining de CSS nas configurações de e-mail. Isso pode resolver conflitos entre o parser HTML e regras CSS complexas.

### Inlining de CSS {#css-inlining}

Há momentos em que as prévias no Inbox Vision ainda não correspondem ao que é enviado pela Braze. Isso pode ser causado pela diferença no inlining de CSS realizado pela Braze e por outras ferramentas. Se você suspeitar que esse é o caso, desative o inlining de CSS.

### Espaço em branco abaixo das imagens {#white-space-under-images}

#### Sintoma

Espaço em branco ou linhas aparecem após imagens em e-mails de teste.

Se você notar espaço em branco ou linhas aparecendo após imagens nos seus e-mails de teste, isso geralmente é causado pela forma como os clientes de e-mail renderizam elementos inline. As imagens são inline por padrão e são alinhadas à linha de base, o que permite que os navegadores acomodem descendentes (a parte de letras como "g" ou "y" que se estendem abaixo da linha de base). Isso cria um pequeno espaço que aparece como espaço em branco.

Para corrigir isso, adicione `display: block;` ao CSS da sua imagem:

```html
<style>
  img {
    display: block;
  }
</style>
```

Alternativamente, aplique o estilo diretamente a imagens específicas:

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```

## Limitações da análise de dados de cliques em links {#link-click-analytics-limitations}

### Sintoma

A análise de dados de cliques para e-mails com muitos parâmetros de consulta únicos não corresponde às suas expectativas. Você pode ver contagens de cliques agregadas para URLs sem parâmetros após os primeiros 100 links únicos.

### Como funciona o rastreamento de cliques em links {#how-link-click-tracking-works}

A Braze rastreia cliques tanto em URLs parametrizadas (com parâmetros de consulta) quanto em URLs base sem parâmetros. Para os primeiros 100 links parametrizados únicos clicados em uma Campaign de e-mail ou Canvas, a Braze coleta e reporta dados para ambos:

- A URL parametrizada completa (por exemplo, `https://example.com?user_id=12345`)
- A URL base sem parâmetros (por exemplo, `https://example.com`)

Após os primeiros 100 links parametrizados únicos serem clicados, a Braze incrementa apenas as contagens de cliques para a URL base sem parâmetros. Isso significa que:

- A análise de dados de cliques é agregada no domínio base e no caminho, em vez de combinações individuais de parâmetros de consulta
- Você ainda pode rastrear engajamento significativo com base nos caminhos dos links
- O rastreamento de cliques no nível do usuário individual continua funcionando normalmente

Esse comportamento evita que a análise de dados fique sobrecarregada com milhares de combinações únicas de parâmetros de consulta, enquanto ainda captura padrões gerais de engajamento com links.

### O que isso significa para suas campanhas {#what-this-means-for-your-campaigns}

Se você depende de parâmetros de consulta únicos para rastrear o comportamento específico de usuários em plataformas externas (por exemplo, `https://example.com?user_id=USER_ID`), esteja ciente de que a análise de dados de cliques da Braze preservará esses parâmetros apenas para os primeiros 100 links únicos clicados. Após esse limite, os cliques ainda são registrados na sua análise de dados, mas são atribuídos à URL sem parâmetros.

Os dados de cliques no nível do usuário permanecem disponíveis por meio do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou do [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), independentemente de quantos links parametrizados únicos forem clicados.

### Problemas de altura de linha com sobrescrito {#superscript-line-height-issues}

#### Sintoma

Textos com sobrescritos aparecem com espaçamento de linha inconsistente, onde as linhas parecem mais próximas ou mais afastadas do que o pretendido. Esse é um problema de renderização comum entre clientes de e-mail e não é específico da Braze.

O uso de sobrescrito em e-mails pode causar um comportamento inesperado na altura da linha porque diferentes clientes de e-mail lidam com texto sobrescrito de maneiras variadas.

#### Resolução {#resolution}

Use o editor de HTML para controlar a estilização dos sobrescritos e dos elementos ao redor.

Para definir explicitamente a altura da linha, adicione CSS inline para definir o `line-height` do texto:

```html
<p style="line-height: 1.5;">Example text with superscript<sup style="line-height: inherit;">1</sup></p>
```

Para ajustar o alinhamento vertical, use a propriedade `vertical-align` para alinhar o sobrescrito sem afetar a altura da linha:

```html
<sup style="vertical-align: top; font-size: smaller;">1</sup>
```

Se os sobrescritos continuarem causando problemas, use um `<span>` como alternativa ao `<sup>` para ter mais controle:

```html
<span style="font-size: smaller; vertical-align: top;">1</span>
```
