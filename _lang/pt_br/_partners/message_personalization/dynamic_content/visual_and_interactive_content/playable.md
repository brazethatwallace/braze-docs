---
nav_title: "Playable"
article_title: "Playable"
description: "Este artigo de referência descreve a parceria entre a Braze e a Playable, uma plataforma de vídeo que permite adicionar conteúdo de vídeo às suas campanhas de e-mail da Braze."
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> A [Playable](https://playable.video) permite que você adicione conteúdo de vídeo de reprodução automática às suas campanhas de e-mail da Braze.

_Essa integração é mantida pela Playable._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Playable permite que você entregue seu melhor conteúdo (vídeo de alta qualidade) ao seu melhor público (e-mail), aumentando suas métricas de cliques e pós-clique com conteúdo envolvente e de alta qualidade que é reproduzido automaticamente na caixa de entrada.

{% alert important %}
Vídeos incorporados não são suportados nativamente por muitos clientes de e-mail e podem aumentar significativamente o tamanho do e-mail, o que pode fazer com que as mensagens sejam marcadas como SPAM. A Playable resolve isso entregando conteúdo de vídeo otimizado que funciona em diferentes clientes de e-mail. Para mais detalhes sobre vídeo em e-mail, consulte [Posso incorporar vídeos em e-mails?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-embed-videos-in-emails)
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Playable | É necessário informar uma conta Playable para aproveitar essa parceria. Se você ainda não tem uma conta Playable, [inscreva-se para uma conta Playable](https://signup.playable.video).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }
Conteúdo de vídeo | Faça upload de arquivos de vídeo para a Playable ou forneça URLs de vídeo de websites como Facebook, Instagram, YouTube, X (antigo Twitter), TikTok e outros. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Implementação {#implementation}

### Etapa 1: Adicione seu vídeo à Playable {#step-1-add-your-video-to-playable}

Na plataforma Playable, faça upload de arquivos de vídeo ou adicione vídeos fornecendo a URL do seu vídeo no Facebook, Instagram, YouTube, X (antigo Twitter), TikTok e outros.

### Etapa 2: Copie o código de incorporação da Playable {#step-2-copy-the-embed-code-from-playable}

Após o upload, a Playable gerará um código que, quando inserido na sua Campaign da Braze, incorporará o vídeo no seu e-mail para reprodução automática ao ser aberto. Quando o e-mail for aberto, os servidores da Playable entregarão a melhor versão possível do seu vídeo, dependendo do cliente de e-mail, dispositivo, tamanho da tela e condições de rede.

{% alert tip %}
Os vídeos serão reproduzidos automaticamente em mais de 98% das caixas de entrada, incluindo iPhone Mail, Gmail, Apple Mail, Outlook para iOS, Outlook para Android, Outlook para Mac e versões mais recentes do Outlook 365 para Windows. Usuários do Outlook legado para Windows verão uma imagem estática.
{% endalert %}

### Etapa 3: Cole o código de incorporação na Braze {#step-3-paste-the-embed-code-into-braze}

Por fim, cole o código na sua Campaign de e-mail da Braze e continue a projetar, testar e publicar sua Campaign de e-mail.