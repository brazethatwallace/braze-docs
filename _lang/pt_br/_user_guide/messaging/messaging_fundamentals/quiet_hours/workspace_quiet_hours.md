---
nav_title: Horário de silêncio do espaço de trabalho
article_title: Horário de silêncio do espaço de trabalho
page_order: 4
page_type: reference
description: "Este artigo de referência aborda o horário de silêncio do espaço de trabalho, como a Braze lida com mensagens durante o período de silêncio e como o horário de silêncio interage com o Intelligent Timing."
---

# Horário de silêncio do espaço de trabalho {#workspace-quiet-hours}

> O horário de silêncio do espaço de trabalho permite definir uma janela padrão de horário de silêncio para um canal de envio de mensagens em todo o seu espaço de trabalho. Cada Campaign e Canvas que envia nesse canal respeita automaticamente a janela, então você não precisa configurar o horário de silêncio em cada Campaign ou Canvas individualmente.

O horário de silêncio do espaço de trabalho é separado do horário de silêncio no nível de Campaign e Canvas, que ainda se aplica quando configurado. Use o horário de silêncio do espaço de trabalho para o caso padrão (por exemplo, um requisito de conformidade em todos os envios de SMS). Mantenha o horário de silêncio no nível de Campaign e Canvas para exceções.

{% alert important %}
O horário de silêncio do espaço de trabalho está atualmente disponível em acesso antecipado. As opções de configuração podem mudar antes da disponibilidade geral. Entre em contato com a equipe da sua conta Braze para solicitar acesso.
{% endalert %}

## Como funciona {#how-it-works}

- **Uma janela por canal:** Cada canal suporta uma única janela de horário de silêncio no espaço de trabalho, definida por um horário de início e um horário de término.
- **Fuso local:** Assim como o horário de silêncio no nível de Campaign e Canvas, o horário de silêncio do espaço de trabalho é aplicado no fuso local de cada destinatário, não no fuso horário da sua empresa.
- **Retida para entrega posterior:** Uma mensagem que seria enviada durante a janela é retida e entregue posteriormente, ou interrompida, dependendo do tipo de Campaign. Consulte [O que acontece com uma mensagem retida](#what-happens-to-a-held-message). O horário de silêncio nunca modifica o conteúdo da mensagem. Ele afeta apenas o momento do envio.
- **Duração máxima da janela:** Uma janela de horário de silêncio não pode exceder 20 horas. Esse limite existe para evitar a pausa acidental de todos os envios em um canal (por exemplo, definindo o horário de início e término com o mesmo valor).

### Canais compatíveis {#supported-channels}

Você pode definir uma janela de horário de silêncio no espaço de trabalho para qualquer um dos seguintes canais:

- Content Cards
- E-mail
- KakaoTalk
- LINE
- Push
   - Isso abrange todas as plataformas de push no seu espaço de trabalho. Não há opção para definir horários de silêncio diferentes para plataformas individuais (por exemplo, iOS vs. Android).
- SMS/MMS/RCS
- Webhook
- WhatsApp

## Pré-requisitos {#prerequisites}

Para criar ou atualizar o horário de silêncio do espaço de trabalho, você precisa da permissão "Edit horário de silêncio".

| Permissão | Acesso |
|---|---|
| Edit horário de silêncio | Criar e atualizar o horário de silêncio do espaço de trabalho. |
| View horário de silêncio | Visualizar a configuração do horário de silêncio do espaço de trabalho sem editá-la. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões de horário de silêncio" }

As permissões existentes de edição de Campaign e Canvas não são afetadas. Usuários com essas permissões ainda podem editar o horário de silêncio no nível de Campaign ou Canvas.

## Configurar o horário de silêncio do espaço de trabalho {#set-up-workspace-quiet-hours}

### Configurar a janela do espaço de trabalho {#configure-the-workspace-window}

1. Acesse **Configurações** > **Horário de silêncio**.
2. Selecione **Adicionar horário de silêncio**.
3. Selecione um canal e insira um horário de início e um horário de término. Um canal pode ter no máximo uma janela de horário de silêncio do espaço de trabalho por vez.
4. (Opcional) Para adicionar outro canal, selecione **Adicionar horário de silêncio** novamente.
5. Salve suas alterações.

![A página de configurações de horário de silêncio do espaço de trabalho com janelas de horário de silêncio para SMS e e-mail, cada uma com um horário de início e de término, e uma opção de adicionar horário de silêncio.]({% image_buster /assets/img/quiet_hours/workspace_quiet_hours_settings.png %}){: style="max-width:90%;"}

As atualizações no horário de silêncio do espaço de trabalho são registradas em um changelog, incluindo quem fez a alteração e quando, já que essa configuração afeta todas as Campaigns e Canvas no canal.

### Aplicar ou substituir em uma Campaign ou Canvas {#apply-or-override-in-a-campaign-or-canvas}

Depois de salvar, a janela de horário de silêncio do espaço de trabalho aparece no editor de Campaigns e Canvas para cada canal que possui uma janela configurada. Você pode manter o padrão do espaço de trabalho ou desativar e aplicar uma janela específica da Campaign ou do Canvas, da mesma forma que você desativa um limite de frequência no nível do espaço de trabalho.

1. Selecione **Aplicar horário de silêncio para esta campanha** (ou o equivalente no Canvas).
2. Selecione **Usar horário de silêncio do espaço de trabalho** para aplicar o padrão do espaço de trabalho, ou selecione **Usar horário de silêncio personalizado** para definir uma janela específica da Campaign ou do Canvas.
3. Para revisar a janela do espaço de trabalho para os canais em uso, selecione **Ver horário de silêncio**.

![A seção de horário de silêncio de uma Campaign com a opção de aplicar horário de silêncio para esta campanha selecionada, usar horário de silêncio do espaço de trabalho selecionado e a janela de e-mail do espaço de trabalho de 20h às 8h expandida.]({% image_buster /assets/img/quiet_hours/campaign_workspace_quiet_hours.png %}){: style="max-width:70%;"}

## Precedência: horário de silêncio do espaço de trabalho versus Campaign ou Canvas {#precedence-workspace-versus-campaign-or-canvas-quiet-hours}

Para qualquer Campaign ou Canvas, apenas uma configuração de horário de silêncio está em vigor por vez (horário de silêncio do espaço de trabalho, uma janela específica de Campaign ou Canvas, ou nenhuma). Uma janela de horário de silêncio no nível de Campaign ou Canvas sempre tem precedência sobre o padrão do espaço de trabalho.

A forma como o horário de silêncio é aplicado também depende de quando a Campaign ou o Canvas foi criado:

- **Campaigns e Canvas existentes** (criados antes de você ativar o horário de silêncio do espaço de trabalho): Se a Campaign ou o Canvas não tiver sua própria janela de horário de silêncio, a janela de horário de silêncio do espaço de trabalho para aquele canal é aplicada automaticamente. Se já houver uma janela no nível de Campaign ou Canvas, essa janela continua sendo aplicada.
- **Novas Campaigns e novos Canvas:** Ao criar uma Campaign ou um Canvas, você pode usar o padrão de horário de silêncio do espaço de trabalho, definir uma janela personalizada no nível de Campaign ou Canvas, ou desativar o horário de silêncio completamente.

| Configuração presente | Qual horário de silêncio é aplicado |
|---|---|
| A Campaign ou o Canvas tem sua própria janela de horário de silêncio | A janela no nível de Campaign ou Canvas é aplicada. O horário de silêncio do espaço de trabalho é ignorado para essa Campaign ou esse Canvas. |
| A Campaign ou o Canvas não tem sua própria janela de horário de silêncio, e existe uma janela de horário de silêncio do espaço de trabalho para o canal utilizado | A janela de horário de silêncio do espaço de trabalho é aplicada automaticamente. Isso inclui Campaigns e Canvas existentes que nunca configuraram horário de silêncio. |
| A Campaign ou o Canvas optou por não usar horário de silêncio | Nenhum horário de silêncio é aplicado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Precedência do horário de silêncio" }

### O que acontece com uma mensagem retida {#what-happens-to-a-held-message}

O que acontece com uma mensagem que cai dentro de uma janela de horário de silêncio depende do tipo de entrega da Campaign ou do Canvas:

- **Campaigns e Canvas baseados em ação:** O fallback pode ser **Interromper mensagem** ou **Enviar no próximo horário disponível**, as mesmas opções do horário de silêncio no nível de Campaign e Canvas.
- **Campaigns agendadas com horário de envio fixo:** O fallback é **Interromper mensagem**. A Braze não adia um envio de horário fixo para o próximo horário disponível, pois isso poderia concentrar um grande volume de mensagens em uma janela de envio comprimida assim que o horário de silêncio terminar.
- **Campaigns usando Intelligent Timing:** Nenhum fallback separado é necessário. A Braze já considera a janela de horário de silêncio do espaço de trabalho no horário de envio ideal calculado para cada usuário, então as mensagens não são agendadas dentro da janela.
- **Campaigns disparadas por API or interface de programação do aplicativo (API) e Campaigns de API or interface de programação do aplicativo (API):** O fallback é **Interromper mensagem** por padrão.

### Campaigns disparadas por API or interface de programação do aplicativo (API) e Campaigns de API or interface de programação do aplicativo (API) {#api-triggered-and-api-campaigns}

O horário de silêncio funciona de forma diferente para Campaigns disparadas por API or interface de programação do aplicativo (API) e Campaigns de API or interface de programação do aplicativo (API).

#### Campaigns disparadas por API or interface de programação do aplicativo (API) {#api-triggered-campaigns}

Campaigns disparadas por API or interface de programação do aplicativo (API) seguem as mesmas opções de horário de silêncio que outras Campaigns no dashboard. Você pode usar o padrão de horário de silêncio do espaço de trabalho, definir uma janela personalizada no nível de Campaign ou desativar o horário de silêncio na configuração da Campaign. Não existe um parâmetro de API or interface de programação do aplicativo (API) `ignore_workspace_quiet_hours` para envios disparados por API or interface de programação do aplicativo (API).

Para envios agendados disparados por API or interface de programação do aplicativo (API) usando `at_optimal_time`, o horário de silêncio do espaço de trabalho já é considerado no horário de envio ideal, de forma semelhante ao [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

#### Campaigns de API or interface de programação do aplicativo (API) {#api-campaigns}

Campaigns de API or interface de programação do aplicativo (API) não podem usar horário de silêncio no nível de Campaign. Apenas a janela de horário de silêncio do espaço de trabalho é aplicada. Para enviar durante essa janela, inclua o parâmetro opcional `ignore_workspace_quiet_hours` na sua requisição de API or interface de programação do aplicativo (API).

### Exclusões {#exclusions}

Os itens a seguir nunca são retidos pelo horário de silêncio do espaço de trabalho, independentemente do canal:

- Mensagens de e-mail de transação
- Respostas automáticas de SMS (por exemplo, respostas com as palavras-chave `STOP` ou `HELP`)
- Envios de teste e envios de grupo de teste

## Outras considerações {#other-considerations}

- **Envios agendados no fuso horário da empresa:** O horário de silêncio do espaço de trabalho é baseado no fuso local de cada destinatário, mas o horário de envio de uma Campaign agendada pode estar definido no fuso horário da sua empresa. Essa diferença significa que um horário de envio que parece adequado no fuso da empresa ainda pode cair dentro do horário de silêncio para alguns destinatários. Revise os detalhes do horário de silêncio do espaço de trabalho exibidos no editor da Campaign antes de enviar.
- **Entrega após o término do horário de silêncio:** Se um grande público foi retido durante a janela, essas mensagens podem se tornar elegíveis para envio todas de uma vez quando a janela se encerrar. Planeje-se para isso quando um canal tiver um público amplo e uma janela longa de horário de silêncio.
- **Independente do limite de frequência e do limite de taxa:** O horário de silêncio do espaço de trabalho se aplica de forma independente do limite de frequência e do limite de taxa. Uma mensagem que passou por esses controles ainda pode ser retida pelo horário de silêncio, e uma mensagem retida pelo horário de silêncio ainda é avaliada em relação aos limites de taxa quando estiver pronta para envio.
- **O Intelligent Timing substitui o horário de silêncio do espaço de trabalho para Campaigns multicanal baseadas em ação. Para limitar os horários de envio, defina um horário de silêncio personalizado.**

## Configurações relacionadas {#related-settings}

- [Horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours): A versão existente desse recurso, configurada por Campaign e por Canvas. O horário de silêncio do espaço de trabalho não o substitui; ele define o padrão que se aplica quando uma Campaign ou um Canvas não configura sua própria janela.
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing): Calcula um horário de envio ideal por usuário. Quando ativado junto com o horário de silêncio do espaço de trabalho, o horário de silêncio é considerado nesse cálculo.
- [Limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Controles de entrega separados que se aplicam de forma independente do horário de silêncio.