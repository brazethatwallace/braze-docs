---
nav_title: WSC Sports
article_title: WSC Sports
description: "Este artigo de referência descreve a parceria entre a Braze e a WSC Sports, uma plataforma de vídeo esportivo que permite incluir mídia esportiva rica e robusta nas notificações por push da Braze."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> A plataforma [WSC Sports](https://wsc-sports.com/) gera vídeos esportivos personalizados para cada plataforma digital e cada fã de esportes - automaticamente e em tempo real.

_Esta integração é mantida pela WSC Sports._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a WSC Sports permite incluir mídia esportiva rica e robusta nas notificações por push da Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da WSC | É necessário ter uma conta na WSC para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões de **Messages**, **Segments**, **Campaigns** e **Canvas**. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br_1 .reset-td-br_2 aria-label="Pré-requisitos" }

## Integração {#integration}

O aplicativo WSC Sports lida com o processo de ponta a ponta, desde a seleção do vídeo até a chegada da notificação por push no dispositivo do usuário final.

### Etapa 1: selecionar configurações de envio {#step-1-select-send-settings}

![Painel de configurações de envio da WSC Sports com seleção de Campaign e Segment da Braze.]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Antes de iniciar a integração, certifique-se de ter a Campaign desejada e os segmentos de usuários criados na Braze. Quando concluído, na plataforma WSC Sports, selecione o vídeo desejado e, nas configurações de envio, selecione o Segment de usuário da Braze e o ID da Campaign que deseja usar. Por fim, escolha o horário em que deseja que a mensagem push seja enviada.

#### Chamada de API {#api-call}

Depois de enviada, a WSC Sports entregará a notificação por push aos segmentos de usuários escolhidos, usando os seguintes endpoints da Braze, com base nas opções selecionadas:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

O corpo da mensagem resultante é o seguinte:
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Etapa 2: fazer envio de teste {#step-2-test-send}

Nesse ponto, sua Campaign deve estar pronta para ser testada e enviada. Verifique os registros de mensagens de erro da Braze se encontrar erros.