---
nav_title: Criar notificações Rich
article_title: "Criando notificações por push avançadas para Android"
page_order: 3
page_layout: tutorial
description: "Este tutorial aborda como configurar notificações Rich para Android nas suas Campaigns da Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns

---

# Criar notificações por push avançadas para Android {#create-rich-push-notifications-for-android}

> As notificações Rich permitem mais personalização nas suas notificações por push, adicionando conteúdo além de apenas texto. As notificações Android já incluem imagens em notificações por push há algum tempo, conhecidas como "imagem de notificação expandida".

## Pré-requisitos {#prerequisites}

Antes de criar uma notificação Rich por push para Android, observe os seguintes detalhes:

- As imagens de notificação expandida do Android devem ter proporção 2:1, mas não possuem limite de tamanho.
- O Android também permite definir uma imagem separada para a visualização padrão da notificação. Estes são os tamanhos de imagem recomendados:
  - **Pequena:** 512x256
  - **Média:** 1024x512
  - **Grande:** 2048x1024
- Atualmente, as notificações Rich para Android só permitem imagens estáticas, incluindo os formatos JPEG e PNG. GIF e outros formatos de imagem ainda não são compatíveis.
- Adicionar botões de ação à sua notificação por push pode afetar a área da imagem que é exibida. Teste com a prévia do dashboard e em dispositivos reais para confirmar que os resultados estão conforme o esperado.
- O SDK da Braze para Android deve estar ativado para que a imagem seja renderizada.

{% alert note %}
Embora a Braze forneça instruções sobre como configurar notificações Rich por push, a renderização real dessas notificações pode variar dependendo de fatores externos, como proporção de tela do dispositivo, versão do Android, restrições específicas do fabricante (OEM), entre outros. Recomendamos fazer um envio de teste para vários dispositivos Android para garantir que suas notificações Rich por push apareçam como você deseja.
{% endalert %}

## Configurando sua notificação Rich para Android {#setting-up-your-android-rich-notification}

### Etapa 1: Criar uma Campaign de push {#step-1-create-a-push-campaign}

Siga as etapas para [criar uma Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#create-a-push-message) e redigir uma notificação por push para Android. Você usará o mesmo criador para configurar notificações por push que não contêm conteúdo avançado.

### Etapa 2: Adicionar legenda {#step-2-add-captioning}

Adicione o **Summary Text** que você deseja exibir antes da imagem na notificação.

![Uma notificação Rich por push de um app de ração para pets chamado Dog, indicando que é hora de pedir mais comida para o Spot, com texto de resumo.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Etapa 3: Adicionar mídia {#step-3-add-media}

Adicione sua imagem no campo **Android Notification Image** no criador da mensagem. As imagens podem ser enviadas diretamente pelo dashboard ou especificando uma URL de conteúdo hospedada em outro local.

Para detalhes sobre imagens compatíveis, confira [Especificações de imagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications).

![A seção de imagem de notificação Android onde você pode adicionar uma imagem ou inserir uma URL de imagem.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Etapa 4: Continuar criando sua Campaign {#step-4-continue-creating-your-campaign}

Após o conteúdo da sua notificação Rich ser enviado ao dashboard, você pode continuar [agendando sua Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).