---
nav_title: Chord
article_title: Chord
description: "Conecte a CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente (CDP or plataforma de dados do cliente) Chord à Braze para encaminhar eventos de eCommerce e atualizações de identidade para envio de mensagens, segmentação e jornadas."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> A [Chord](https://www.chord.co/) oferece uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente que captura e padroniza eventos da sua loja de eCommerce. Quando você conecta a Chord à Braze, atividades de compra, eventos comportamentais e atualizações de identidade fluem para a Braze, permitindo disparar Campaigns e manter perfis atualizados sem precisar construir esses pipelines por conta própria.

_Essa integração é mantida pela Chord._

Para saber mais sobre configuração, opções de conexão e listas de campos, consulte a [integração Chord Braze](https://docs.chord.co/braze#chord-x-braze-integration).

## Sobre a integração {#about-the-integration}

O Chord atua como a camada de dados entre sua loja e a Braze. Depois de conectar a Braze como um destino na CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente do Chord, o Chord mapeia eventos de seu plano de rastreamento para a Braze. Use esses dados em Segments, Canvas e personalização de mensagens para refletir o que seus consumidores estão fazendo no seu site.

## Pré-requisitos {#prerequisites}

Antes de conectar o Chord e a Braze, confirme que você tem o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Chord | Uma conta Chord é necessária para usar esta integração. |
| Credenciais de API or interface de programação do aplicativo (API) da Braze | As credenciais necessárias dependem do seu [modo de conexão](#connection-modes). O modo cloud usa uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze. O modo dispositivo usa a chave de API or interface de programação do aplicativo (API) do canal web para o SDK or kit de desenvolvimento de software da Braze, que é separada da sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional. |
| Endpoint REST or transferir estado representacional da Braze | O Chord envia dados do lado do servidor para os endpoints [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) e [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Sua URL base segue a sua instância da Braze, por exemplo, `https://rest.iad-01.braze.com`. Para saber mais, consulte [Endpoints da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Modos de conexão {#connection-modes}

O Chord oferece suporte ao modo cloud (chamadas de servidor para servidor por meio das REST or transferir estado representacional APIs da Braze) e ao modo de dispositivo (o Chord inicializa o Braze Web SDK or kit de desenvolvimento de software e encaminha as chamadas mapeadas). Escolha o modo adequado conforme sua necessidade: recursos completos do Web SDK or kit de desenvolvimento de software (por exemplo, mensagens no app) ou apenas encaminhamento de eventos do lado do servidor.

### Modo cloud {#cloud-mode}

1. Na plataforma de dados do Chord, abra a CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente e acesse **Destinations**.
2. Selecione **Add** ao lado de destinos, escolha **Braze** no catálogo, depois insira um nome para o destino e sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze.
3. Crie o destino para concluir a conexão.

Crie a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. Se você usa a navegação antiga, acesse **Console de desenvolvedor** > **API or interface de programação do aplicativo (API) Settings**. A menos que o Chord documente requisitos diferentes para seu espaço de trabalho, a chave precisa das permissões `users.track` e `users.identify`. Para saber mais, consulte [Chaves de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics).

### Modo de dispositivo {#device-mode}

1. Na plataforma de dados do Chord, abra a CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente e acesse **Destinations**.
2. Selecione **Add** ao lado de destinos, escolha **Braze (device mode)** no catálogo, depois insira um nome para o destino e sua chave de API or interface de programação do aplicativo (API) do canal Web.
3. Crie o destino para concluir a conexão.

Use a chave de API or interface de programação do aplicativo (API) do canal Web em **Configurações** > **Configurações do app** > **Web** > **API or interface de programação do aplicativo (API) Key** no dashboard da Braze. Não use sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional para o modo de dispositivo.

### Configuração do modo de dispositivo {#device-mode-configuration}

Nas configurações de destino do Chord, configure o seguinte:

- **Versão do Braze Web SDK or kit de desenvolvimento de software:** O Chord disponibiliza versões selecionáveis do SDK or kit de desenvolvimento de software na CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente; confirme o intervalo disponível na documentação do Chord.
- **Endpoint do SDK or kit de desenvolvimento de software:** Deve corresponder à sua instância da Braze. Para saber mais, consulte [Endpoints de API or interface de programação do aplicativo (API) e SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).
- **Opções de eventos e SDK or kit de desenvolvimento de software:** Por exemplo, quais comportamentos de rastreamento ou identificação enviar, tratamento de eventos de página, comportamento de mensagens no app, timing de inicialização do SDK or kit de desenvolvimento de software e configurações relacionadas a consentimento.

## Mapeamento de eventos (modo dispositivo) {#event-mapping-device-mode}

Quando você usa o modo dispositivo, o Chord mapeia eventos para a Braze conforme mostrado nesta tabela:

| Chord | Braze |
| ----- | ----- |
| Pedido concluído | `logPurchase` |
| Outros eventos `track` | `logCustomEvent` |
| Identify | Atualizações de usuário (por exemplo, atributos por meio do objeto de usuário do SDK or kit de desenvolvimento de software) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Somente os eventos incluídos no seu plano de rastreamento do Chord e configurados para o destino Braze são encaminhados.

## Usando a integração {#using-the-integration}

### Etapa 1: Confirmar eventos na Braze {#step-1-confirm-events-in-braze}

Depois que os dados começarem a fluir, abra os perfis de usuário ou suas ferramentas de eventos na Braze para confirmar que os eventos e atributos estão chegando conforme o esperado.

### Etapa 2: Criar públicos e jornadas {#step-2-build-audiences-and-journeys}

Use eventos e atributos sincronizados em [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) e Campaigns para direcionar consumidores com base no comportamento na loja.

## Casos de uso {#use-cases}

- **Mensagens pós-compra:** dispare confirmações, vendas cruzadas ou solicitações de avaliação quando a Chord receber pedidos concluídos.
- **Enriquecimento de perfil:** mantenha os atributos da Braze alinhados com os dados mais recentes do perfil de consumidor da Chord para uma segmentação mais precisa.
- **Redirecionamento comportamental:** reengaje consumidores que não compraram ou converteram recentemente usando eventos comportamentais da Chord.

## Considerações {#considerations}

{% alert important %}
Se outra ferramenta já envia os mesmos eventos para a Braze, coordene com os responsáveis por essa integração antes de conectar a Braze por meio da Chord CDP or plataforma de dados do cliente. Executar destinos em paralelo pode criar eventos duplicados downstream.
{% endalert %}

## Solução de problemas {#troubleshooting}

Se os eventos não aparecerem na Braze:

1. No Chord CDP or plataforma de dados do cliente, confirme que os eventos em tempo real estão chegando das suas fontes.
2. Verifique se o destino da Braze usa a chave de API or interface de programação do aplicativo (API) correta, a versão do SDK or kit de desenvolvimento de software (modo de dispositivo) e o endpoint REST or transferir estado representacional ou SDK or kit de desenvolvimento de software da sua instância.
3. Confirme que o destino está vinculado à fonte esperada no Chord.
4. No Chord, revise os logs do destino de API or interface de programação do aplicativo (API) ou de funções para chamadas bem-sucedidas a `/users/track` e `/users/identify` e, em seguida, verifique novamente na Braze.

Para localizações de logs e etapas de interface específicas do Chord, consulte [Integração Chord Braze](https://docs.chord.co/braze#chord-x-braze-integration).