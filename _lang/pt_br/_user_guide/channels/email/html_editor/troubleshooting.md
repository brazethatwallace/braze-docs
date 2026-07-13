---
nav_title: Solução de problemas
article_title: Solução de problemas
page_order: 9
description: "Este artigo de ajuda explica como solucionar problemas com e-mails HTML."
channel: email
---

# Solução de problemas {#troubleshooting}

> Este artigo aborda problemas comuns com e-mails HTML e como resolvê-los, incluindo conflitos de extensões, diferenças de renderização e inlining de CSS.

## HTML renderiza incorretamente em e-mails de teste {#html-renders-incorrectly-in-test-emails}

Se o seu [e-mail de teste]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) parecer estranho, recomendamos primeiro verificar a configuração do seu HTML. Em seguida, você pode verificar estes problemas:
* [Conflitos de extensões](#check-conflicts)
* [Renderização de e-mail](#check-rendering)
* [Inlining de CSS](#switch-css-inlining)
* [Espaço em branco abaixo das imagens](#white-space-under-images)

### Conflitos de extensões {#extension-conflicts}

Certas extensões de navegador podem causar problemas com nosso editor de e-mail. Um exemplo é o [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) quando usado com o Google Chrome. Se você estiver usando uma dessas extensões, deve:
- Editar e-mails da Braze em um navegador que não tenha o Grammarly como extensão
- Entrar em contato com o gerente da sua conta na Braze e solicitar a troca dos editores de e-mail para somente HTML ou texto simples.

A visualização em texto simples remove o editor `WYSIWYG` (o que você vê é o que você obtém), então confirme primeiro que todos os membros da equipe estão confortáveis com HTML antes de fazer essa solicitação.

### Renderização de e-mail {#email-rendering}

Os e-mails são renderizados de forma diferente dependendo dos navegadores e clientes de e-mail, então anote em quais navegadores e clientes de e-mail você está enfrentando problemas.

- Pré-visualize seus e-mails usando o [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision) para ver como seus e-mails aparecem em diferentes navegadores e clientes de e-mail.
- Depois de identificar quais navegadores ou clientes de e-mail estão causando problemas, informe sua equipe de desenvolvimento que será necessário modificar o HTML e fazer ajustes para acomodar esses navegadores ou clientes de e-mail.

### Inlining de CSS {#css-inlining}

Há momentos em que as prévias no Inbox Vision ainda não correspondem ao que é enviado pela Braze. Isso pode ser causado pela diferença no inlining de CSS realizado pela Braze e por outras ferramentas. Se você suspeitar que esse é o caso, desative o inlining de CSS.

### Espaço em branco abaixo das imagens {#white-space-under-images}

Se você notar espaço em branco ou linhas aparecendo abaixo das imagens nos seus e-mails de teste, isso geralmente é causado pela forma como os clientes de e-mail renderizam elementos inline. As imagens são inline por padrão e são alinhadas à linha de base, o que permite que os navegadores acomodem descendentes (a parte de letras como "g" ou "y" que se estendem abaixo da linha de base). Isso cria um pequeno espaço que aparece como espaço em branco.

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

Ainda precisa de ajuda? Abra um [ticket de suporte]({{site.baseurl}}/braze_support).