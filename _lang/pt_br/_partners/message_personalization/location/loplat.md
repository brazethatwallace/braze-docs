---
nav_title: loplat
article_title: loplat
description: "Este artigo de referência descreve a parceria entre a Braze e a loplat, uma plataforma de marketing offline baseada em localização, que permite executar campanhas de marketing de proximidade adicionando contexto de localização."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [A Loplat](https://www.loplat.com/) é a principal plataforma offline baseada em localização. Use o SDK da loplat para aumentar o número de visitantes da sua loja de forma inteligente e executar campanhas de marketing que incentivem compras na loja. Você pode medir o desempenho da loja por meio da análise de tráfego após o término da campanha.

_Esta integração é mantida pela Loplat._

## Sobre a integração {#about-the-integration}

A integração da Braze com a loplat permite que você use os serviços de localização da loplat (POI da loja e geofence personalizado) para disparar campanhas de marketing de contexto geográfico e criar eventos personalizados usando segmentação offline. Quando os usuários visitam o local direcionado que você definiu no loplat X, as informações da campanha e do local são enviadas imediatamente para a Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta loplat X | É necessário ter uma conta do loplat X para aproveitar essa integração.<br><br>Envie um e-mail para [support@loplat.com](mailto:support@loplat.com) para solicitar uma conta do loplat X. |
| SDK da loplat | O SDK da loplat reconhece as visitas dos usuários à loja, processa eventos de localização e distingue se os usuários estão em um local ou se estão em movimento. Você pode usar o SDK da loplat para analisar o tráfego da sua loja, enviar mensagens push quando os usuários entram na loja etc.<br><br>Observe que o SDK está disponível apenas para Android e iOS. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as seguintes permissões:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

As informações de localização do evento personalizado fornecidas pela loplat podem ser usadas em suas campanhas para alcançar casos de uso como:

- [Alerta de promoção de duty-free](https://www.loplat.com/loplat-x#usecase)
    - Envie cupons de desconto de lojas duty-free para os usuários que estiverem próximos aos portões de embarque no aeroporto.
- Push de localização de estações de carregamento de veículos elétricos (EV)
    - Defina geofences em torno das estações de carregamento de EV e notifique os usuários quando estiverem perto da estação, incentivando-os a carregar.

## Integração {#integration}

### Etapa 1: Integrar os SDKs {#step-1-integrate-the-sdks}

Integre o SDK da loplat e o SDK da Braze ao seu app usando as etapas fornecidas na documentação da [integração loplat-Braze](https://developers.loplat.com/braze/).

### Etapa 2: Sincronizar os dashboards da Braze e do loplat X e criar uma campanha {#step-2-sync-the-braze-and-loplat-x-dashboards-and-create-a-campaign}

Crie uma nova chave de API no dashboard da Braze. Copie a chave de API e cole-a em **Settings > API Settings** no dashboard do loplat X. Consulte o [guia do usuário do loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25) para obter mais detalhes.

#### Entrega disparada por API {#api-triggered-delivery}

1. Crie uma Campaign ou um Canvas na Braze que envie com **API-Triggered Delivery** e copie o ID da campanha.
2. Lance a campanha na Braze depois de concluir todas as etapas.
3. Acesse o loplat X e crie uma campanha seguindo as instruções do [guia do usuário do loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. Cole o ID da campanha da Braze em **Campaign Message Settings** e inicie a campanha.

![Configurações de campanha do loplat X mostrando o ID da campanha da Braze para entrega disparada por API.]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### Entrega baseada em ação {#action-based-delivery}

Com a integração, você pode aplicar condições de localização enviando informações de geofence, região, nome da marca ou nome da loja. Além disso, você pode adicionar segmentos ou atribuir conversão com o evento personalizado que criou.
1. Crie uma campanha no loplat X seguindo as instruções do [guia do usuário do loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. Adicione um evento personalizado em **Campaign Message Settings** e inicie a campanha.
3. Acesse o dashboard da Braze e crie uma Campaign ou um Canvas que envie com **Action-Based Delivery**.
4. Selecione o evento personalizado que você criou no loplat X para definir uma ação-gatilho de localização.

![Configuração de campanha baseada em ação na Braze usando um evento personalizado da loplat como gatilho.]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})