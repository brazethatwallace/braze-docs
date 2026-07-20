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

Identifique seu sintoma na tabela para navegar até a seção relevante.

| Sintoma | Acesse |
| --- | --- |
| O HTML do e-mail de teste aparece incorreto | [HTML renderiza incorretamente em e-mails de teste](#html-renders-incorrectly-in-test-emails) |
| O editor se comporta de forma estranha no Chrome | [Conflitos de extensões](#extension-conflicts) |
| O e-mail aparece diferente em cada cliente | [Renderização de e-mail](#email-rendering) |
| A prévia do Inbox Vision não corresponde ao e-mail enviado | [Inlining de CSS](#css-inlining) |
| Espaço em branco ou linhas após imagens em e-mails de teste | [Espaço em branco abaixo das imagens](#white-space-under-images) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de e-mail HTML" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho quando a renderização do e-mail HTML ou o comportamento do editor não corresponder ao esperado. Comece pela etapa 1.

1. Valide sua marcação HTML no editor ou em um validador externo.
2. Envie um [e-mail de teste]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) e anote quais clientes de e-mail ou navegadores apresentam o problema.
3. Pré-visualize com o [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) para comparar a renderização entre clientes.
4. Descarte [conflitos de extensões de navegador](#extension-conflicts) se o próprio editor estiver se comportando de forma estranha.
5. Se o problema persistir, abra um [ticket de suporte]({{site.baseurl}}/braze_support) com capturas de tela do Inbox Vision e dos clientes afetados.

## HTML renderiza incorretamente em e-mails de teste {#html-renders-incorrectly-in-test-emails}

**Sintoma:** Um [e-mail de teste]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) não corresponde ao que você espera do editor.

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

### Inlining de CSS {#css-inlining}

Há momentos em que as prévias no Inbox Vision ainda não correspondem ao que é enviado pela Braze. Isso pode ser causado pela diferença no inlining de CSS realizado pela Braze e por outras ferramentas. Se você suspeitar que esse é o caso, desative o inlining de CSS.

### Espaço em branco abaixo das imagens {#white-space-under-images}

**Sintoma:** Espaço em branco ou linhas aparecem após imagens em e-mails de teste.

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
