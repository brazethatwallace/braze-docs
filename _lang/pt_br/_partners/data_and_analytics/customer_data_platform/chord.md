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

O Chord atua como a camada de dados entre sua loja e a Braze. Depois de conectar a Braze como um destino no Chord CDP, o Chord mapeia eventos do seu plano de rastreamento para a Braze. Use esses dados em Segments, Canvas e personalização de mensagens para refletir o que seus consumidores estão fazendo no seu site.

## Pré-requisitos {#prerequisites}

Antes de conectar o Chord à Braze, confirme que você tem o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Chord | É necessária uma conta do Chord para usar esta integração. |
| Credenciais de API da Braze | As credenciais necessárias dependem do seu [modo de conexão](#connection-modes). O modo cloud usa uma chave da API REST da Braze. O modo device usa a chave de API do canal web para o SDK da Braze, que é separada da sua chave da API REST. |
| Endpoint REST da Braze | O Chord envia dados do lado do servidor para os endpoints [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) e [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Sua URL base segue a sua instância da Braze, por exemplo, `https://rest.iad-01.braze.com`. Para saber mais, consulte [Endpoints da REST API da Braze]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Modos de conexão {#connection-modes}

O Chord é compatível com o modo cloud (chamadas servidor a servidor por meio das REST APIs da Braze) e o modo de dispositivo (o Chord inicializa o SDK da Braze para web e encaminha as chamadas mapeadas). Escolha o modo mais adequado dependendo de você precisar dos recursos completos do SDK para web (por exemplo, In-App Messages) ou apenas do encaminhamento de eventos no lado do servidor.

### Modo cloud {#cloud-mode}

1. Na plataforma de dados do Chord, abra a plataforma de dados do cliente e acesse **Destinations**.
2. Selecione **Add** ao lado de destinos, escolha **Braze** no catálogo e insira um nome para o destino e sua chave da API REST da Braze.
3. Crie o destino para finalizar a conexão.

Crie a chave da API REST no dashboard da Braze em **Configurações** > **Chaves de API**. Se você usa a navegação anterior, acesse **Console de desenvolvedor** > **Configurações de API**. A menos que o Chord documente requisitos diferentes para o seu espaço de trabalho, a chave precisa das permissões `users.track` e `users.identify`. Para saber mais, consulte [Chaves de API]({{site.baseurl}}/api/api_key).

### Modo de dispositivo {#device-mode}

1. Na plataforma de dados do Chord, abra a plataforma de dados do cliente e acesse **Destinations**.
2. Selecione **Add** ao lado de destinos, escolha **Braze (device mode)** no catálogo e insira um nome para o destino e sua chave de API do canal web.
3. Crie o destino para finalizar a conexão.

Use a chave de API do canal web em **Configurações** > **Configurações do app** > **Web** > **API Key** no dashboard da Braze. Não use sua chave da API REST para o modo de dispositivo.

### Configuração do modo de dispositivo {#device-mode-configuration}

Nas configurações de destino do Chord, configure o seguinte:

- **Versão do SDK da Braze para web:** o Chord disponibiliza versões selecionáveis do SDK na plataforma de dados do cliente. Confirme o intervalo disponível na documentação do Chord.
- **Endpoint do SDK:** deve corresponder à sua instância da Braze. Para saber mais, consulte [Endpoints de API e SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).
- **Opções de eventos e SDK:** por exemplo, quais comportamentos de rastreamento ou identificação enviar, tratamento de eventos de página, comportamento de In-App Messages, tempo de inicialização do SDK e configurações relacionadas a consentimento.

## Mapeamento de eventos (modo de dispositivo) {#event-mapping-device-mode}

Ao usar o modo de dispositivo, o Chord mapeia eventos para a Braze conforme mostrado nesta tabela:

| Chord | Braze |
| ----- | ----- |
| Pedido concluído | `logPurchase` |
| Outros eventos `track` | `logCustomEvent` |
| Identify | Atualizações de usuário (por exemplo, atributos por meio do objeto de usuário do SDK) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Somente os eventos incluídos no seu plano de rastreamento do Chord e configurados para o destino Braze são encaminhados.

## Usando a integração {#using-the-integration}

### Etapa 1: Confirmar eventos na Braze {#step-1-confirm-events-in-braze}

Após o fluxo de dados, abra os perfis de usuário ou suas ferramentas de eventos na Braze para confirmar se os eventos e atributos estão chegando conforme esperado.

### Etapa 2: Criar públicos e jornadas {#step-2-build-audiences-and-journeys}

Use eventos e atributos sincronizados em [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) e Campaigns para direcionar consumidores com base no comportamento na loja.

## Casos de uso {#use-cases}

- **Envio de mensagens pós-compra:** Dispare confirmações, vendas cruzadas ou solicitações de avaliação quando o Chord receber pedidos concluídos.
- **Enriquecimento de perfil:** Mantenha os atributos da Braze alinhados com os dados mais recentes do perfil do consumidor vindos do Chord para uma segmentação mais precisa.
- **Redirecionamento comportamental:** Reengaje consumidores que não compraram ou converteram recentemente usando eventos comportamentais do Chord.

## Considerações {#considerations}

{% alert important %}
Se outra ferramenta já envia os mesmos eventos para a Braze, coordene com os responsáveis por essa integração antes de conectar a Braze por meio da plataforma de dados do cliente Chord. Executar destinos em paralelo pode criar eventos duplicados no fluxo seguinte.
{% endalert %}

## Solução de problemas {#troubleshooting}

Se os eventos não aparecerem na Braze:

1. No Chord CDP, confirme se os eventos em tempo real estão chegando das suas fontes.
2. Verifique se o destino da Braze usa a chave de API correta, a versão do SDK (modo de dispositivo) e o endpoint REST ou de SDK para a sua instância.
3. Confirme se o destino está vinculado à fonte esperada no Chord.
4. No Chord, revise os logs do destino de API ou os logs de função para chamadas bem-sucedidas a `/users/track` e `/users/identify` e, em seguida, verifique novamente na Braze.

Para locais de log específicos do Chord e etapas na interface, consulte [Integração Chord com Braze](https://docs.chord.co/braze#chord-x-braze-integration).