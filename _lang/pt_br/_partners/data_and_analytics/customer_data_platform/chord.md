---
nav_title: Chord
article_title: Chord
description: "Conecte a plataforma de dados do cliente (CDP) Chord à Braze para encaminhar eventos de eCommerce e atualizações de identidade para envio de mensagens, segmentação e jornadas."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> A [Chord](https://www.chord.co/) oferece uma plataforma de dados do cliente que captura e padroniza eventos da sua loja de eCommerce. Quando você conecta a Chord à Braze, atividades de compra, eventos comportamentais e atualizações de identidade fluem para a Braze, permitindo disparar Campaigns e manter perfis atualizados sem precisar construir esses pipelines por conta própria.

_Essa integração é mantida pela Chord._

Para saber mais sobre configuração, opções de conexão e listas de campos, consulte a [integração Chord Braze](https://docs.chord.co/braze#chord-x-braze-integration).

## Sobre a integração {#about-the-integration}

A Chord atua como a camada de dados entre sua loja e a Braze. Depois que você conecta a Braze como destino na CDP da Chord, a Chord mapeia eventos do seu plano de rastreamento para a Braze. Use esses dados em Segments, Canvas e personalização de mensagens para refletir o que seus consumidores estão fazendo no seu site.

## Pré-requisitos {#prerequisites}

Antes de conectar a Chord e a Braze, confirme que você tem o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Chord | Uma conta Chord é necessária para usar essa integração. |
| Credenciais de API da Braze | As credenciais necessárias dependem do seu [modo de conexão](#connection-modes). O modo cloud usa uma chave da API REST da Braze. O modo device usa a chave de API do canal Web para o SDK da Braze, que é diferente da sua chave da API REST. |
| Endpoint REST da Braze | A Chord envia dados server-side para os endpoints [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) e [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). Sua URL base segue a sua instância da Braze, por exemplo, `https://rest.iad-01.braze.com`. Para saber mais, consulte [Endpoints da REST API da Braze]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Modos de conexão {#connection-modes}

A Chord suporta modo cloud (chamadas server-to-server pelas REST APIs da Braze) e modo device (a Chord inicializa o SDK Web da Braze e encaminha chamadas mapeadas). Escolha o modo adequado conforme você precise de recursos completos do SDK Web (por exemplo, mensagens no app) ou apenas encaminhamento de eventos server-side.

### Modo cloud {#cloud-mode}

1. Na plataforma de dados da Chord, abra a CDP e acesse **Destinations**.
2. Selecione **Add** ao lado de destinations, escolha **Braze** no catálogo e insira um nome de destino e sua chave da API REST da Braze.
3. Crie o destino para finalizar a conexão.

Crie a chave da API REST no dashboard da Braze em **Settings** > **API Keys**. Se você usa a navegação antiga, acesse **Developer Console** > **API Settings**. A menos que a Chord documente requisitos diferentes para o seu espaço de trabalho, a chave precisa das permissões `users.track` e `users.identify`. Para saber mais, consulte [Chaves de API]({{site.baseurl}}/api/api_key/).

### Modo device {#device-mode}

1. Na plataforma de dados da Chord, abra a CDP e acesse **Destinations**.
2. Selecione **Add** ao lado de destinations, escolha **Braze (device mode)** no catálogo e insira um nome de destino e sua chave de API do canal Web.
3. Crie o destino para finalizar a conexão.

Use a chave de API do canal Web em **Settings** > **App Settings** > **Web** > **API Key** no dashboard da Braze. Não use sua chave da API REST para o modo device.

### Configuração do modo device {#device-mode-configuration}

Nas configurações de destino da Chord, configure o seguinte:

- **Versão do SDK Web da Braze:** A Chord disponibiliza versões selecionáveis do SDK na CDP; confirme o intervalo disponível na documentação da Chord.
- **Endpoint do SDK:** Deve corresponder à sua instância da Braze. Para saber mais, consulte [Endpoints de API e SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/).
- **Opções de eventos e SDK:** Por exemplo, quais comportamentos de track ou identify enviar, tratamento de eventos de página, comportamento de mensagens no app, timing de inicialização do SDK e configurações relacionadas a consentimento.

## Mapeamento de eventos (modo device) {#event-mapping-device-mode}

Quando você usa o modo device, a Chord mapeia eventos para a Braze conforme mostrado nesta tabela:

| Chord | Braze |
| ----- | ----- |
| Order completed | `logPurchase` |
| Outros eventos `track` | `logCustomEvent` |
| Identify | Atualizações de usuário (por exemplo, atributos pelo objeto de usuário do SDK) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Apenas eventos incluídos no seu plano de rastreamento da Chord e configurados para o destino Braze são encaminhados.

## Usando a integração {#using-the-integration}

### Etapa 1: Confirme os eventos na Braze {#step-1-confirm-events-in-braze}

Depois que os dados começarem a fluir, abra perfis de usuário ou suas ferramentas de eventos na Braze para confirmar que os eventos e atributos estão chegando conforme esperado.

### Etapa 2: Crie públicos e jornadas {#step-2-build-audiences-and-journeys}

Use eventos e atributos sincronizados em [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) e Campaigns para direcionar consumidores com base no comportamento na loja.

## Casos de uso {#use-cases}

- **Mensagens pós-compra:** Dispare confirmações, vendas cruzadas ou solicitações de avaliação quando a Chord recebe pedidos concluídos.
- **Enriquecimento de perfil:** Mantenha os atributos da Braze alinhados com os dados mais recentes do perfil do consumidor vindos da Chord para uma segmentação mais limpa.
- **Redirecionamento comportamental:** Reengaje consumidores que não compraram ou converteram recentemente usando eventos comportamentais da Chord.

## Considerações {#considerations}

{% alert important %}
Se outra ferramenta já envia os mesmos eventos para a Braze, coordene com os responsáveis por essa integração antes de conectar a Braze pela CDP da Chord. Executar destinos em paralelo pode criar eventos duplicados downstream.
{% endalert %}

## Solução de problemas {#troubleshooting}

Se os eventos não aparecem na Braze:

1. Na CDP da Chord, confirme que eventos ao vivo estão chegando das suas fontes.
2. Verifique se o destino Braze usa a chave de API correta, a versão do SDK (modo device) e o endpoint REST ou SDK correto para a sua instância.
3. Confirme que o destino está vinculado à fonte esperada na Chord.
4. Na Chord, revise os logs de destino de API ou de funções para chamadas bem-sucedidas a `/users/track` e `/users/identify`, e depois verifique novamente na Braze.

Para localizações de logs e etapas de UI específicas da Chord, consulte a [integração Chord Braze](https://docs.chord.co/braze#chord-x-braze-integration).