---
nav_title: Campaigns e Canvas sem atividades
article_title: Campaigns e Canvas sem atividades
page_order: 1
page_type: reference
alias: /idle_campaigns/
description: "Este artigo de referência aborda o status de inatividade de Campaigns e Canvas, incluindo critérios de interrupção automática e perguntas frequentes."
toc_headers: h2
---

# Campaigns e Canvas sem atividades {#idle-campaigns-and-canvases}

> Campaigns e Canvas ficam sem atividades quando param de enviar mensagens ou de registrar a entrada de usuários por um período definido.

A Braze interrompe automaticamente Campaigns e Canvas sem atividades nas datas de interrupção associadas. Eles permanecem ativos até que a Braze os interrompa. Envios únicos e envios de mensagens com datas de término ficam sem atividades quando essa data passa e são interrompidos automaticamente após sete dias. Envios de mensagens sem data de término ficam sem atividades após 11 meses sem atividade e são interrompidos automaticamente após um ano.

## Campaigns sem atividades {#idle-campaigns}

A Braze interrompe Campaigns sem atividades que atendam a qualquer um destes critérios:

- Um envio único agendado está com a data de envio ultrapassada em sete dias
- Uma Campaign agendada ou baseada em ação com data de término está com a data de término ultrapassada em sete dias
- Uma Campaign sem data de término não enviou uma mensagem, não inscreveu um usuário em um grupo de controle, nem foi editada em um ano

Para Campaigns sem data de término, um envio, inscrição em grupo de controle ou edição reinicia a contagem de um ano. Quando a Braze interrompe Campaigns, ela notifica os usuários da empresa no dashboard e por e-mail.

A Braze interrompe Campaigns na data mais tardia entre a data de interrupção padrão e um dia após o último prazo de conversão. Envios de uma variante vencedora ou variante personalizada são tratados como envios agendados, e a Braze os interrompe sete dias após o envio dessa variante. Campaigns são interrompidas às 4h UTC todos os dias.

Content Cards não são interrompidos até o prazo de expiração, e também seguem os critérios de interrupção de Campaigns sem atividades e a regra do prazo de conversão. Para mais detalhes, consulte [Como funciona a interrupção de Content Cards?](#how-does-stopping-content-cards-work).

Use esta tabela para manter uma Campaign sem atividades ativa. O status de inatividade e a interrupção automática usam janelas diferentes: uma Campaign sem data de término fica sem atividades após 11 meses sem atividade, e a Braze a interrompe automaticamente após um ano.

| Motivo do status de inatividade | Etapas para tornar a Campaign ativa |
|---|---|
| Envio único agendado está com a data de envio ultrapassada | Agendar um envio futuro |
| Campaign agendada ou baseada em ação tem uma data de término que já passou | Estender a data de término |
| Campaign sem data de término não enviou uma mensagem, não inscreveu um usuário em um grupo de controle, nem foi editada em 11 meses | Enviar uma mensagem ou editar a Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como manter uma Campaign sem atividades ativa" }

Campaigns de Feature Flag e experimentos de Feature Flag não ficam sem atividades e não são interrompidos automaticamente.

### Campaigns de mensagens no app {#in-app-message-campaigns}

Campaigns de mensagens no app baseadas em ação ficam sem atividades após 30 dias sem envio, inscrição em grupo de controle ou edição. Uma Campaign de mensagem no app sem atividades continua entregando com base em sua configuração. Dependendo do seu espaço de trabalho, a Braze pode entregá-la como uma [mensagem no app com modelo]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

Um envio, inscrição em grupo de controle ou edição retorna a Campaign ao status ativo e reinicia a janela de 30 dias. A interrupção automática ainda segue as regras de sete dias e um ano em [Campaigns sem atividades](#idle-campaigns), não a janela de 30 dias de inatividade.

## Canvas sem atividades {#idle-canvases}

A Braze interrompe Canvas sem atividades que atendam a qualquer um destes critérios:

- Um envio único agendado está com a data de envio e a [duração máxima]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#maximum-duration) ultrapassadas em mais de sete dias
- Um Canvas agendado ou baseado em ação com data de término está com a data de término e a duração máxima ultrapassadas em mais de sete dias
- Um Canvas sem data de término não registrou a entrada de usuários nem foi editado em mais de 12 meses mais sua duração máxima

Para Canvas sem data de término, a entrada de um usuário ou edição reinicia a contagem de um ano. Quando a Braze interrompe Canvas, ela notifica os usuários da empresa no dashboard e por e-mail.

A duração máxima de um Canvas é o maior tempo possível que um usuário pode levar para concluir esse Canvas. Essa duração inclui prazos de expiração de Content Cards e mensagens no app.

Use esta tabela para manter um Canvas sem atividades ativo. O status de inatividade e a interrupção automática usam janelas diferentes: um Canvas sem data de término fica sem atividades após 11 meses mais sua duração máxima sem atividade, e a Braze o interrompe automaticamente após 12 meses mais sua duração máxima.

| Motivo do status de inatividade | Etapas para tornar o Canvas ativo |
|---|---|
| Envio único agendado está com a data de envio e a duração máxima ultrapassadas | Agendar um envio futuro |
| Canvas agendado ou baseado em ação tem uma data de término e duração máxima que já passaram | Estender a data de término |
| Canvas sem data de término não registrou a entrada de usuários nem foi editado em 11 meses mais sua duração máxima | Registrar a entrada de um usuário ou editar o Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como manter um Canvas sem atividades ativo" }

Canvas com etapas de Feature Flag não ficam sem atividades e não são interrompidos automaticamente.

Para dados de interação de mensagens em Campaigns e Canvas interrompidos, consulte [Sobre a disponibilidade de dados de interação de mensagens]({{site.baseurl}}/messaging_interaction_data).

## Perguntas frequentes {#frequently-asked-questions}

### A quais Campaigns ou Canvas isso se aplica? {#what-campaigns-or-canvases-does-this-apply-to}

Isso se aplica a Campaigns e Canvas que já atendem aos critérios deste artigo e àqueles que atenderem aos critérios posteriormente.

### Como saber se uma Campaign ou Canvas está sem atividades? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Para encontrar Campaigns e Canvas sem atividades, acesse a página **Campaigns** ou **Canvas** e filtre por **Idle**. A data em que a Braze interromperá a Campaign ou o Canvas é listada como uma coluna na lista.

![O filtro "Idle" na página Campaigns.]({% image_buster /assets/img/idle_filter.png %}){: style="max-width:80%;"}

### O que acontece se uma Campaign ou Canvas sem atividades for atualizado? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Se você atualizar uma Campaign que não enviou mensagens ou um Canvas que não registrou a entrada de usuários, a contagem será reiniciada.

### O que acontece com Campaigns que não enviaram mensagens em um ano (ou Canvas que não registraram a entrada de usuários em um ano), mas têm uma data de término no futuro? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

A Braze interrompe essas Campaigns e Canvas sete dias após a data de término, às 4h UTC.

### Posso impedir que Campaigns sejam interrompidas automaticamente? {#can-i-prevent-campaigns-from-auto-stopping}

Não. A interrupção automática mantém apenas as Campaigns necessárias ativas, o que reduz a desordem no dashboard e melhora o desempenho. Se você precisa de uma lista de todas as Campaigns interrompidas automaticamente, [envie um ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Quem recebe notificações por e-mail sobre Campaigns e Canvas interrompidos? {#who-receives-email-notifications-about-stopped-campaigns-and-canvases}

Por padrão, todos os usuários com permissões de administrador estão inscritos para receber notificações por e-mail sobre Campaigns e Canvas interrompidos automaticamente. O criador da Campaign ou do Canvas é sempre notificado quando ele é interrompido. Para gerenciar os destinatários, acesse **Configurações** > **Configuração de administrador** > **Preferências de notificação** e adicione ou remova destinatários de **Campaign Automatically Stopped** e **Canvas Automatically Stopped**.

### Como funciona a interrupção de Content Cards? {#how-does-stopping-content-cards-work}

Content Cards em Campaigns não são interrompidos até o prazo de expiração e o período de buffer apropriado. A Braze os interrompe na data mais tardia entre o período de buffer (envio único, data de término ou sem data de término) e o prazo de expiração.

Por exemplo, se um Content Card expira em 1º de abril, é um envio único e tem um prazo de conversão de 10 dias, a Braze o interrompe em 12 de abril (10 dias após o prazo de conversão, mais um dia). Se um Content Card expira em 1º de abril, é disparado por API or interface de programação do aplicativo (API) e não enviou mensagens desde 15 de março, ele expira em 15 de março do ano seguinte.

Canvas são interrompidos somente após a interrupção de seus Content Cards, ou seja, quando sua duração máxima tiver passado.

### Tenho um experimento de Feature Flag no meu Canvas. Após a Feature Flag ser configurada, o Canvas permanece ativo? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-does-the-canvas-remain-active}

Sim. Canvas com etapas de Feature Flag não são interrompidos automaticamente e não ficam sem atividades. Campaigns de Feature Flag e experimentos de Feature Flag seguem a mesma exceção.

### Por que Campaigns sem atividades aparecem quando filtro a lista de Campaigns apenas por ativas? {#why-do-idle-campaigns-appear-when-i-filter-the-campaign-list-to-active-only}

Campaigns sem atividades são consideradas ativas até serem interrompidas.

### Uma Campaign está sem atividades se ainda estiver enviando notificações por push? {#is-a-campaign-idle-if-its-still-sending-push-notifications}

Não. Uma Campaign é listada como sem atividades quando não está mais enviando mensagens ativamente.