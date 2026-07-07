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

A integração entre a Braze e a Playable permite que você forneça seu melhor conteúdo (vídeo de alta qualidade) para seu melhor público (e-mail), aumentando suas métricas de cliques e pós-cliques com conteúdo empolgante de alta qualidade que é reproduzido automaticamente na caixa de entrada.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Playable | É necessário ter uma conta da Playable para usar essa parceria. Se ainda não tiver uma conta da Playable, inscreva-se [aqui](https://signup.playable.video).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }
Conteúdo de vídeo | Faça upload de arquivos de vídeo para a Playable ou forneça URLs de vídeo de sites como Facebook, Instagram, YouTube, X (antigo Twitter), TikTok e muito mais. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Implementação {#implementation}

### Etapa 1: adicione seu vídeo à Playable {#step-1-add-your-video-to-playable}

Na plataforma Playable, faça upload de arquivos de vídeo ou adicione vídeos fornecendo uma URL do seu vídeo no Facebook, Instagram, YouTube, X (antigo Twitter), TikTok e muito mais.

### Etapa 2: copie o código de incorporação da Playable {#step-2-copy-the-embed-code-from-playable}

Após o upload, a Playable gerará um código que, quando inserido na sua campanha da Braze, incorporará o vídeo no seu e-mail para reprodução automática ao ser aberto. Quando seu e-mail for aberto, os servidores da Playable fornecerão a melhor versão possível do seu vídeo, dependendo do cliente de e-mail, dispositivo, tamanho da tela e condições da rede.

{% alert tip %}
Os vídeos serão reproduzidos automaticamente em mais de 98% das caixas de entrada, incluindo iPhone Mail, Gmail, Apple Mail, Outlook para iOS, Outlook para Android, Outlook para Mac e versões mais recentes do Outlook 365 para Windows. Os usuários do Outlook para Windows legado verão uma imagem estática.
{% endalert %}

### Etapa 3: cole o código de incorporação na Braze {#step-3-paste-the-embed-code-into-braze}

Por fim, cole o código na sua campanha de e-mail da Braze e, em seguida, continue a projetar, testar e publicar sua campanha de e-mail.