---
nav_title: Open Loyalty
article_title: Open Loyalty
description: "A integração entre a Braze e o Open Loyalty permite que você sincronize dados de fidelidade, como saldo de pontos, alterações de nível e avisos de vencimento, diretamente na Braze em tempo real."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Open Loyalty

> O [Open Loyalty](https://www.openloyalty.io/) é uma plataforma de programa de fidelidade baseada na nuvem que permite criar e gerenciar programas de fidelidade e recompensas para clientes. A integração entre a Braze e o Open Loyalty sincroniza dados de fidelidade, como saldo de pontos, alterações de nível e avisos de vencimento, diretamente na Braze em tempo real. Isso permite disparar mensagens personalizadas (e-mail, push, SMS) quando o status de fidelidade de um usuário muda.

_Essa integração é mantida pela Open Loyalty_

## Sobre a integração {#about-the-integration}

Essa integração usa Transformação de Dados da Braze para capturar webhooks do Open Loyalty e mapeá-los para os perfis de usuários da Braze.

* **Atualizações em tempo real**: Envie eventos de fidelidade (pontos ganhos, upgrades de nível) para a Braze.
* **Personalização**: Use atributos de fidelidade (saldo atual, nome do próximo nível) em seus modelos da Braze.
* **Bidirecional**: Atualize os atributos personalizados do cliente do Open Loyalty com base nos dados de engajamento da Braze.

## Casos de uso {#use-cases}

Essa integração abrange os seguintes fluxos de dados:

1. **Sincronização de eventos com a Braze (entrada)**: Rastreie alterações de pontos, upgrades de níveis ou resgates de recompensas enviando dados do Open Loyalty para a Braze. A Transformação de Dados converte esses dados em um evento de usuário.
2. **Modificação de membros do Open Loyalty (saída)**: Atualize automaticamente os dados de membros no Open Loyalty com base no comportamento do usuário na Braze, como adicionar etiquetas "VIP" ou atualizar atributos personalizados.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa dos seguintes itens:

| Requisito | Descrição |
| :--- | :--- |
| Conta Open Loyalty | É necessário ter uma conta de administrador em um tenant do Open Loyalty para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional do Open Loyalty | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional do Open Loyalty (para integrações que enviam dados da Braze para o Open Loyalty). <br><br> Crie essa chave em **Settings > Admins > API or interface de programação do aplicativo (API) Keys**. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. <br><br> Crie essa chave no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Transformação de Dados da Braze | É necessário acessar a guia "Configurações de dados" na Braze para configurar os ouvintes de webhook. |
| IDs correspondentes | O `external_id` do usuário na Braze deve corresponder ao `loyaltyCardNumber` (ou outro identificador padrão) no Open Loyalty. |
| Tenant ID | Seu Open Loyalty Tenant ID (necessário para atualizações de saída). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A integração primária sincroniza os eventos de webhook do Open Loyalty com a Braze usando a Transformação de Dados.

### Etapa 1: Gerar a URL do webhook na Braze {#step-1-generate-the-webhook-url-in-braze}

Primeiro, crie uma transformação de dados na Braze para gerar uma URL exclusiva para receber dados.

1.  Na Braze, abra **Data Settings > Data Transformation**.
2.  Clique em **Create Transformation**.
3.  Preencha os seguintes campos:
     * **Transformation name**: Forneça um nome descritivo (por exemplo, "Open Loyalty Point Update Events").
     * **Select destination**: Escolha **POST: Track users**.
4.  Clique em **Create Transformation**.
5.  Localize a **Webhook URL** no painel de detalhes e clique em **Copy**.

{% alert important %}
Mantenha essa URL em segurança; você precisará dela para a próxima etapa.
{% endalert %}

### Etapa 2: Criar a inscrição do webhook no Open Loyalty {#step-2-create-the-webhook-subscription-in-open-loyalty}

Diga ao Open Loyalty para enviar eventos específicos para a URL que você acabou de gerar.

1.  Faça login no painel de administração do Open Loyalty.
2.  Navegue até **General > Webhooks**.
3.  Clique em **Add new webhook** e configure a inscrição:
    * **eventName**: Selecione o evento que deseja rastrear (por exemplo, `AvailablePointsAmountChanged`, `CustomerLevelChanged` ou `CampaignEffectWasApplied`).
    * **url**: Cole a URL do webhook da Braze da Etapa 1.
    * Adicione os seguintes cabeçalhos:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Salve a inscrição do webhook.

### Etapa 3: Configurar a Transformação de Dados {#step-3-configure-the-data-transformation}

Escreva a lógica JavaScript na Braze para mapear a carga útil de entrada do Open Loyalty para as propriedades da Braze.

1.  Na Braze, abra a transformação de dados que você criou na Etapa 1.
2.  Dispare o evento no Open Loyalty (por exemplo, altere os pontos de um membro ou atribua um nível) para gerar uma carga útil de amostra no painel **Webhook details**.
3.  No editor **Transformation code**, escreva um script para mapear os dados de entrada. Use o exemplo a seguir como guia:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,

      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",

      // timestamp
      "time": new Date().toISOString(),

      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. Clique em **Validate** para garantir que o código seja executado na sua carga útil de amostra e, em seguida, clique em **Activate**.


## Usando o Open Loyalty com a Braze {#using-open-loyalty-with-braze}

Depois de concluir a integração de entrada, configure **atualizações de saída** para modificar os membros do Open Loyalty com base no comportamento na Braze.

### Etapa 1: Configurar a Campaign de webhook da Braze {#step-1-configure-braze-webhook-campaign}

Esse processo usa webhooks da Braze para enviar uma solicitação `PATCH` para a API or interface de programação do aplicativo (API) de membros do Open Loyalty (por exemplo, para adicionar uma etiqueta "VIP").

1.  Na Braze, crie uma nova **Campaign de webhook** (ou use um webhook dentro de um Canvas).
2.  Clique em **Compose Webhook**.
3.  **Webhook URL**: Construa a URL usando sua instância do Open Loyalty, o Tenant ID e a variável Liquid da Braze para o ID do usuário.
    * Formato:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Preencha os seguintes campos:
    * **Request Method**: `PATCH`
    * **Request Headers**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Request Body**: Selecione `Raw text` e cole a carga útil:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Etapa 2: Configurar o gatilho {#step-2-configure-the-trigger}

1.  Navegue até a guia **Delivery** ou **Entry agendar/cronograma**.
2.  Preencha os seguintes campos:
    * **Delivery Method**: Baseado em ações.
    * **Trigger**: Defina o gatilho relevante (por exemplo, um usuário entra em um Segment or segmento específico na Braze).
    * **Launch**: Ative a Campaign.

## Solução de problemas {#troubleshooting}

### Verificar eventos de entrada {#verify-inbound-events}
Quando a Transformação de Dados está ativa, os dados aparecem na Braze como um evento personalizado. Verifique isso criando uma Campaign com um gatilho **Perform Custom Event** e verificando se o evento definido (por exemplo, `Loyalty Event Triggered`) está disponível.

### Verificar webhooks de saída {#verify-outbound-webhooks}
Verifique o registro de atividades de envio de mensagem na Braze para garantir que o webhook retornou um status `200 OK`.
* **Erro 401**: Verifique seu token da API or interface de programação do aplicativo (API) do Open Loyalty.
* **Erro 404**: O ID do usuário na Braze não existe no Open Loyalty.