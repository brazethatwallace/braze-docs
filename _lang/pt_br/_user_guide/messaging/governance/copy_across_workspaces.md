---
nav_title: Copiar entre espaços de trabalho
article_title: Copiar entre espaços de trabalho
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artigo de referência fornece uma visão geral de como copiar Campaigns e Canvas para diferentes espaços de trabalho."
tool:
    - Campaigns
    - Canvas
---

# Copiar Campaigns e Canvas entre espaços de trabalho {#copy-campaigns-and-canvases-across-workspaces}

> Copiar Campaigns entre espaços de trabalho permite que você agilize a composição de mensagens começando com uma cópia de uma Campaign em um espaço de trabalho diferente. Esta página explica como copiar Campaigns para diferentes espaços de trabalho e lista o que é e o que não é copiado.

Quando você copia uma Campaign ou Canvas para um espaço de trabalho diferente, a cópia permanecerá como rascunho até que você edite e lance, ajudando a manter e desenvolver suas estratégias de envio de mensagens bem-sucedidas.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
A cópia de Campaigns entre espaços de trabalho está disponível de forma geral. O suporte de canal para Content Cards não está disponível no momento.
{% endalert %}

Você pode copiar Campaigns entre espaços de trabalho para os seguintes canais compatíveis: SMS, mensagens no app, notificações por push, e-mail e webhooks. Você também pode copiar modelos de e-mail, Feature Flags e Content Blocks. Observe que campanhas multicanais com canais não compatíveis não podem ser copiadas para um espaço de trabalho diferente.

Para copiar uma Campaign para um espaço de trabalho diferente:

1. Selecione o ícone de engrenagem <i class="fas fa-cog"></i> ao lado da Campaign selecionada.
2. Selecione **Copiar para espaço de trabalho**.
3. Após a cópia, revise e teste sua Campaign para confirmar que todos os campos funcionam corretamente.

{% endtab %}
{% tab canvas %}

{% alert important %}
A cópia de Canvas entre espaços de trabalho está disponível de forma geral. Os seguintes canais não são compatíveis no momento: LINE, Content Cards e WhatsApp.
{% endalert %}

Você pode copiar Canvas entre espaços de trabalho para os seguintes canais compatíveis: e-mail, mensagens no app, push, webhooks e SMS.

Para copiar um Canvas para um espaço de trabalho diferente:

1. Selecione o menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;ao lado do Canvas selecionado.
2. Selecione **Copiar para espaço de trabalho**.
3. Após a cópia, revise e teste seu Canvas para confirmar que todos os campos funcionam corretamente.

Ao copiar um Canvas com etapas de Audience Sync, as configurações não serão copiadas para o espaço de trabalho de destino, mas as etapas da jornada serão.

{% endtab %}
{% endtabs %}

## O que é copiado entre espaços de trabalho {#whats-copied-across-workspaces}

Observe que a lista a seguir não é abrangente sobre o que é copiado entre espaços de trabalho e o que é omitido. Como prática recomendada, verifique os detalhes da Campaign e do Canvas e teste para confirmar que sua mensagem funciona conforme o esperado.

### Informações {#details}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios |
| Tipo | Tags |
| Ações (aninhadas) | Segments e filtros |
| Comportamentos de conversão (aninhados) | [Aprovações]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| Configurações de horário silencioso | Programação de gatilho |
| Configurações de limite de frequência | Resumos da Campaign |
| Estado de inscrição do destinatário |  |
| Programação recorrente |  |
| É transacional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios |
| Tipo | Tags |
| Ações (aninhadas) | Segments e filtros |
| Comportamentos de conversão (aninhados) | [Aprovações]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| Configurações de horário silencioso | Programação de gatilho |
| Configurações de limite de frequência | Resumos do Canvas |
| Estado de inscrição do destinatário |  |
| Programação recorrente | Critérios de saída |
| É transacional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

Os critérios de filtro das etapas do Canvas (por exemplo, etapas de [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)) não são copiados para o espaço de trabalho de destino. Reconfigure esses filtros após a cópia.

{% endtab %}
{% endtabs %}

### Comportamentos de conversão {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com a Campaign | ID da Campaign |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com o Canvas | ID do Canvas |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

{% endtab %}
{% endtabs %}

### Ações {#actions}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com a Campaign | ID da Campaign |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com o Canvas | ID do Canvas |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% endtabs %}

### Variações de mensagem {#message-variations}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Porcentagem de envio | ID da API |
| Tipo | IDs do grupo de teste |
|  | IDs do modelo de link |
|  | IDs do grupo de usuários internos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Porcentagem de envio | ID da API |
| Tipo | IDs do grupo de teste |
|  | IDs do modelo de link |
|  | IDs do grupo de usuários internos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% endtabs %}


### Variação de mensagem de e-mail {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Endereço do remetente |
| Extras da mensagem | Responder para |
| Título | CCO |
| Assunto | Modelo de link |
|  | Alias de link |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Endereço do remetente |
| Extras da mensagem | Responder para |
| Título | CCO |
| Assunto | Modelo de link |
|  | Alias de link |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

{% endtab %}
{% endtabs %}

### Corpo do e-mail {#email-body}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Texto simples | Alias de link |
| Conteúdo HTML e arrastar e soltar | Traduções |
| Pré-cabeçalho |  |
| CSS inline |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Texto simples | Alias de link |
| Conteúdo HTML e arrastar e soltar | Traduções |
| Pré-cabeçalho |  |
| CSS inline |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

{% endtab %}
{% endtabs %}

### Modelos de e-mail {#email-templates}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | IDs da API |
| Descrição | IDs de imagem |
| Assunto | Territórios |
| Cabeçalhos | Tags |
| | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | IDs da API |
| Descrição | IDs de imagem |
| Assunto | Territórios |
| Cabeçalhos | Tags |
| | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Nome | Alias de link |
| Descrição | Chaves de API |
| Conteúdo | Territórios |
| Conteúdo HTML e arrastar e soltar | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Nome | Alias de link |
| Descrição | Chaves de API |
| Conteúdo | Territórios |
| Conteúdo HTML e arrastar e soltar | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### Variação de mensagem SMS {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo | Serviço de envio de mensagens |
| Encurtamento de link | Itens de mídia VCF |
| Rastreamento de cliques |  |
| Itens de mídia |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo | Serviço de envio de mensagens |
| Encurtamento de link | Itens de mídia VCF |
| Rastreamento de cliques |  |
| Itens de mídia |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% endtabs %}

## Copiando mensagens que contêm Liquid {#copying-messages-that-contain-liquid}

As referências Liquid dentro dos corpos das mensagens são copiadas para o espaço de trabalho de destino, mas podem não funcionar conforme o esperado. Isso significa que, se um Canvas do Espaço de trabalho A for copiado para o Espaço de trabalho B, o Espaço de trabalho B não poderá referenciar os detalhes do Espaço de trabalho A, incluindo referências Liquid. Por exemplo, campos como ações-gatilho, filtros de público e critérios de filtro de [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) não são copiados.

Acompanhe as seguintes referências Liquid com dependências ao copiar Campaigns e Canvas entre espaços de trabalho:

- Tags de itens do catálogo
- Tags de Conteúdo conectado
- Content Blocks
- Atributos personalizados
- Centrais de Preferências
- Recomendações de produto
- Tags de estado de inscrição
- Tags de voucher e promoção

## Copiando mensagens com Feature Flags {#copying-messages-with-feature-flags}

Para copiar uma Campaign de Feature Flag e um Canvas com uma etapa de Feature Flag entre espaços de trabalho, certifique-se de que o espaço de trabalho de destino tenha um [experimento de Feature Flag]({{site.baseurl}}/developer_guide/feature_flags/experiments/) configurado com um ID que corresponda ao Feature Flag referenciado na Campaign original ou à etapa de Feature Flag referenciada no Canvas original.

Se você copiar uma Campaign ou Canvas que tenha uma etapa de Feature Flag com um ID de Feature Flag que não existe no espaço de trabalho de destino, a etapa de Feature Flag será copiada, mas seu conteúdo não será.

## Copiando mensagens com Content Blocks {#copying-messages-with-content-blocks}

Quando você copia uma Campaign entre espaços de trabalho, os Content Blocks não serão copiados. No entanto, um Content Block pode ser referenciado no espaço de trabalho de destino se existir um bloco com o mesmo nome. Como alternativa, você pode criar o Content Block (ou essas referências Liquid) no espaço de trabalho de destino para evitar erros ao lançar uma Campaign.

Para Canvas que referenciam um Content Block, o Content Block deve primeiro ser copiado para o espaço de trabalho de destino.