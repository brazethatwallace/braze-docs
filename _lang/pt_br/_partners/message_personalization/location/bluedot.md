---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Este artigo de referência descreve a parceria entre a Braze e a Bluedot, uma plataforma de localização que fornece recursos precisos e simples de geofencing para seus apps."
page_type: partner
search_tag: Partner

---

# Bluedot

> A [Bluedot](https://bluedot.io/) é uma plataforma de localização que fornece recursos precisos e simples de geofencing para seus apps. Use o SDK da Bluedot para enviar mensagens mais inteligentes, automatizar check-ins de pedidos móveis, otimizar fluxos de trabalho e criar experiências sem atrito.

_Essa integração é mantida pela Bluedot._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Bluedot permite que você use os serviços de geofence da Bluedot para criar eventos de usuário que podem ser usados para criar jornadas, Campaigns e analisar os comportamentos e interesses dos clientes. Os eventos (entrada/saída) gerados pelo usuário em seu dispositivo são enviados imediatamente à Braze com todas as informações relevantes.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Bluedot | É necessário ter uma conta Bluedot para aproveitar essa integração. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

As informações de localização do evento personalizado fornecidas pela Bluedot podem ser usadas em suas Campaigns para alcançar casos de uso comuns, como:
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Restaurante de serviço rápido)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/)

## Integração {#integration}

### Etapa 1: Criar um projeto Bluedot {#step-1-create-a-bluedot-project}
Configure sua conta da Bluedot e faça login no [dashboard do Bluedot Canvas](https://docs.bluedot.io/canvas/). Visite a [documentação da Bluedot](https://docs.bluedot.io/canvas/creating-a-new-project/) para saber como criar um novo projeto.

### Etapa 2: Integrar os SDKs {#step-2-integrate-the-sdks}
Integre o SDK do Bluedot Point e o SDK da Braze ao seu app usando as etapas fornecidas na documentação de [integração Bluedot-Braze](https://docs.bluedot.io/integrations/braze-integration/).

### Etapa 3: Autenticar o SDK da Bluedot {#step-3-authenticate-the-bluedot-sdk}
Use o `projectId` criado na etapa 1 para autenticar o SDK do Bluedot Point.

### Etapa 4: Usar eventos Bluedot na Braze {#step-4-use-bluedot-events-in-braze}

#### Disparando mensagens {#triggering-messages}

Você pode configurar uma Campaign push ou um Canvas que será acionado a partir de eventos de localização gerados pelo SDK da Bluedot. Essa rota de integração é ideal para o envio de mensagens em tempo real no momento em que os usuários entram em um local de interesse, ou para uma comunicação de acompanhamento posterior à sua saída.

Configure uma Campaign baseada em ações na Braze que enviará mensagens com base em um local definido. Para seu gatilho, use um evento personalizado de `bluedot_entry` ou `bluedot_exit`, conforme mostrado na captura de tela a seguir:

![Uma Campaign baseada em ação na etapa de entrega. Aqui, você tem duas opções de agendamento que enviarão a Campaign se um usuário executar um evento personalizado "bluedot_entry" ou "bluedot_exit".]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Direcionamento de usuários {#targeting-users}

Certifique-se de direcionar **Todos os usuários** para seu espaço de trabalho.
![Uma Campaign baseada em ações com a etapa de direcionamento de usuários incentivando você a selecionar "Todos os usuários" como o segmento desejado.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}