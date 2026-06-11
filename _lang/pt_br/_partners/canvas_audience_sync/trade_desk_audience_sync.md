---
nav_title: The Trade Desk
article_title: Audience Sync do Canvas para o The Trade Desk
description: "Este artigo de referência aborda como usar o Audience Sync da Braze com o The Trade Desk para entregar anúncios com base em gatilhos comportamentais, segmentação e muito mais."
alias: /trade_desk_audience_sync/
tool:
  - Canvas
page_order: 7
---

# Audience Sync para o The Trade Desk {#audience-sync-to-the-trade-desk}

> Usando o Audience Sync da Braze para o The Trade Desk, você pode sincronizar dinamicamente seus dados primários de usuários da Braze diretamente no The Trade Desk para redirecionamento de anúncios, modelagem de públicos semelhantes e supressão.

**Casos de uso comuns para sincronização de público incluem:**

- Redirecionar seus usuários existentes no The Trade Desk com campanhas personalizadas.
- Enviar dados primários para o The Trade Desk para exclusão de direcionamento.
- Sincronizar usuários com públicos novos ou existentes ou segmentos de dados de CRM.

## Pré-requisitos {#prerequisites}

Certifique-se de que os itens a seguir foram criados, concluídos ou aceitos antes de configurar a etapa de Audience Sync com o The Trade Desk no Canvas.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Token de API | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | Um token de API padrão criado na plataforma do The Trade Desk. Recomendamos definir a validade do token de API para até um ano para evitar interrupções nos seus Canvas com o Audience Sync do The Trade Desk. |
| Termos e Políticas do The Trade Desk | The Trade Desk | Você deve concordar com uma política de participação UID2/CRM antes de ser habilitado para enviar dados ao The Trade Desk. Fale com seu representante no The Trade Desk para confirmar que você tem a assinatura apropriada para ativar a entrega de dados ao The Trade Desk.<br><br> {::nomarkdown}<ul><li>Confirme que o Acesso ao Gerenciamento de Dados de CRM está ativado na sua conta&#8212;seu representante no The Trade Desk pode ajudar com isso. Você deve ter seu ID de anunciante.</li><li>Tenha seu token de API padrão pronto. Você pode seguir as instruções nesta página para gerar um.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar a conta do The Trade Desk {#step-1-connect-the-trade-desk-account}

Para começar, acesse **Integrações de parceiros** > **Parceiros de tecnologia** > **The Trade Desk**. Forneça os seguintes dados da sua conta do Trade Desk:

- **Token de API**
- **Nome do ID do anunciante** (este nome opcional identifica a conta do anunciante para referência na etapa de Audience Sync do Canvas)
- **ID do anunciante**

Em seguida, selecione **Conectar**.

![Um exemplo de um Audience Sync não conectado para o The Trade Desk.]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

#### Conectar múltiplas contas do The Trade Desk (opcional) {#connect-multiple-the-trade-desk-accounts-optional}

Depois de conectar sua primeira conta do The Trade Desk, você pode adicionar contas de anunciante adicionais na página de parceiros do The Trade Desk selecionando **Conectar mais anunciantes** e fornecendo o **Nome do ID do anunciante** e o **ID do anunciante** para cada conta.

### Etapa 2: Adicionar uma etapa de Audience Sync com o The Trade Desk {#step-2-add-an-audience-sync-step-with-the-trade-desk}

Adicione um componente no seu Canvas e selecione **Audience Sync**. Em seguida, selecione **The Trade Desk** como o parceiro de Audience Sync.

![Opção para selecionar seu parceiro para sincronizar com a etapa de Audience Sync.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### Etapa 3: Configurar sua sincronização {#step-3-set-up-your-sync}

Em seguida, configure os detalhes da sua sincronização:

1. Selecione uma conta de anúncios.
2. Escolha um público existente ou crie um novo público.

![Configuração do Audience Sync com um campo de público contendo o nome "valentines2025".]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. Selecione uma ação para **Adicionar usuários ao público** ou **Remover usuários do público**.

![Configuração do Audience Sync para adicionar usuários ao público.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. Escolha um dos seguintes campos para correspondência: **E-mail**, **Telefone** ou **ID de anunciante móvel**.

{% alert note %}
Se você estiver sincronizando com um público no The Trade Desk com uma região definida como UE, o número de telefone não é suportado pelo The Trade Desk. Fale com o The Trade Desk para suporte a número de telefone na região da UE.
{% endalert %}

### Etapa 4: Lançar seu Canvas {#step-4-launch-your-canvas}

Depois de configurar seu Audience Sync para o The Trade Desk, você está pronto para lançar o Canvas! O novo público é criado, e os usuários que passam pela etapa de Audience Sync são incluídos nesse público no The Trade Desk. Se o seu Canvas contiver componentes subsequentes, seus usuários avançam para a próxima etapa na jornada do usuário.

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo leva para os tamanhos de público serem preenchidos no The Trade Desk? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-the-trade-desk}

Isso pode levar até 24 horas.

### Qual é o tamanho mínimo de público para o The Trade Desk preencher na sua conta de anúncios? {#what-is-the-minimum-audience-size-for-the-trade-desk-to-populate-within-your-ad-account}

Não há tamanho mínimo de público para públicos de CRM no The Trade Desk.

### Como sei se os usuários foram correspondidos após enviar usuários ao The Trade Desk? {#how-do-i-know-if-users-have-matched-after-passing-users-to-the-trade-desk}

No The Trade Desk, os IDs recebidos aparecem ao lado do segmento.

- IDs recebidos são o número de IDs que recebemos nos últimos 30 dias.
- IDs ativos são o número de IDs que vimos em lances nos últimos sete dias.

### Quantos públicos o The Trade Desk pode suportar? {#how-many-audiences-can-the-trade-desk-support}

Não há limite para quantos públicos podem ser suportados no The Trade Desk.