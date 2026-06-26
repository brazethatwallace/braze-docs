---
nav_title: "Campaigns e Canvas sem atividades"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Campaigns e Canvas sem atividades {#idle-campaigns-and-canvases}

> Este artigo de referência explica o status de sem atividades para Campaigns e Canvas e responde a perguntas frequentes.

{% alert note %}
Em 2024, os Canvas serão marcados como **Sem atividades** e interrompidos, de forma semelhante às Campaigns. Quando os Canvas estiverem sem atividades ou interrompidos, eles seguirão a lógica descrita neste documento.
{% endalert %}

Campaigns e Canvas recebem o status de sem atividades quando não enviam mensagens ou não registram entrada de usuários há algum tempo. Essas Campaigns e Canvas serão automaticamente interrompidos nas datas de interrupção associadas. Você pode filtrar por Campaigns e Canvas sem atividades para ajudar a organizar e gerenciar sua lista de Campaigns e Canvas.

Campaigns e Canvas com datas de término e envios únicos ficam sem atividades por 7 dias antes da interrupção automática. Campaigns e Canvas que não enviaram uma mensagem em 11 meses ficam sem atividades por 1 mês antes da interrupção automática.

## Campaigns sem atividades {#idle-campaigns}

De forma contínua, as Campaigns sem atividades que atenderem aos seguintes critérios serão interrompidas:

- Um envio único agendado ultrapassou a data de envio em sete dias
- Uma Campaign agendada ou baseada em ação com data de término ultrapassou a data de término em sete dias
- Uma Campaign sem data de término que não enviou mensagens em um ano

Para Campaigns sem datas de término, se uma mensagem for enviada ou a Campaign for atualizada, a contagem regressiva de um ano para a interrupção da Campaign será reiniciada. Quando as Campaigns forem interrompidas, a Braze notificará os clientes no dashboard e por e-mail.

As Campaigns serão interrompidas na data mais tardia entre a data de interrupção padrão e um dia após o último prazo de conversão. Envios resultantes de uma Variante Vencedora ou Variante Personalizada são tratados como envios agendados e serão interrompidos sete dias após o envio da Variante Vencedora ou Personalizada. Todas as Campaigns serão interrompidas às 4h UTC todos os dias para todos os usuários da Braze.

Os Content Cards não serão interrompidos até o prazo de expiração e também seguirão os critérios mencionados anteriormente, bem como a regra do prazo de conversão.

Consulte esta tabela para saber como manter uma Campaign sem atividades ativa:

| Motivo do status de sem atividades | Etapas para tornar a Campaign ativa |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campaigns que são envios únicos agendados e ultrapassaram a data de envio | Agendar um envio futuro |
| Campaigns que são agendadas ou baseadas em ação, têm datas de término e ultrapassaram a data de término | Estender a data de término |
| Campaigns sem data de término que não enviaram mensagens em um ano | Enviar uma mensagem ou fazer qualquer edição na Campaign |
| Campaigns com datas de término e envios únicos | Agendar um envio futuro |
| Campaigns que não enviaram uma mensagem em 11 meses | Enviar uma mensagem ou fazer qualquer edição na Campaign |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Campaigns de mensagem no app {#in-app-message-campaigns}

Se uma Campaign de mensagem no app não tiver impressões e não tiver sido editada por mais de 30 dias, ela se torna uma Campaign sem atividades. Uma Campaign de mensagem no app sem atividades continua a entregar com base em sua configuração, mas a mensagem no app se torna uma mensagem no app baseada em modelo.

Se seus usuários dispararem um evento de impressão ou o profissional de marketing editar a Campaign, ela volta ao status ativo e o contador de 30 dias é reiniciado.

## Canvas sem atividades {#idle-canvases}

De forma contínua, os Canvas sem atividades que atenderem aos seguintes critérios serão interrompidos:

- Um envio único agendado ultrapassou a data de envio e a duração máxima em mais de 7 dias
- Um Canvas agendado ou baseado em ação com data de término ultrapassou a data de término e a duração máxima em mais de 7 dias
- Um Canvas sem data de término não registrou entrada de usuários nem foi editado em mais de 12 meses e sua duração máxima

Para Canvas sem datas de término, se um usuário entrar ou o Canvas for atualizado, a contagem regressiva de um ano para a interrupção do Canvas será reiniciada. Quando os Canvas forem interrompidos, a Braze notificará os clientes no dashboard e por e-mail.

A [duração máxima]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) de um Canvas é o maior tempo possível que um usuário pode levar para concluir um determinado Canvas. Essa duração inclui expirações de Content Cards e mensagens no app.

Consulte esta tabela para saber como manter um Canvas sem atividades ativo:

| Motivo do status de sem atividades | Etapas para tornar o Canvas ativo |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Canvas que são envios únicos agendados e a duração máxima ultrapassou a data de envio | Agendar um envio futuro |
| Canvas que são agendados ou baseados em ação, têm datas de término e a duração máxima ultrapassou a data de término | Estender a data de término |
| Canvas sem datas de término que não enviaram mensagens em um ano | Enviar uma mensagem ou fazer qualquer edição no Canvas |
| Canvas com datas de término e envios únicos | Agendar um envio futuro |
| Canvas que não enviaram uma mensagem em 11 meses | Enviar uma mensagem ou fazer qualquer edição no Canvas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se não houver uma opção para restaurar os dados de interação, isso pode ser porque:

- A restauração ou outra operação relacionada a dados de interação está em andamento.
- Não existiam dados de interação para este Canvas.
- Se o Canvas foi criado antes de 2021, os dados podem ter sido excluídos permanentemente com base na política anterior.

## Perguntas frequentes {#frequently-asked-questions}

### A quais Campaigns ou Canvas isso se aplica? {#what-campaigns-or-canvases-does-this-apply-to}

Isso se aplica a Campaigns e Canvas que já atendem aos critérios listados anteriormente, e a Campaigns e Canvas que atenderão aos critérios futuramente.

### Como sei se uma Campaign ou Canvas está sem atividades? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Campaigns e Canvas sem atividades serão exibidos nas páginas de lista de Campaigns e Canvas na categoria **Sem atividades**. A data em que a Campaign ou o Canvas será interrompido é listada como uma coluna na lista.

![O filtro "Sem atividades" na página "Campaigns".][1]{: style="max-width:60%;"}

### O que acontece se uma Campaign ou Canvas sem atividades for atualizado? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Se uma Campaign que não enviou uma mensagem ou um Canvas que não registrou entrada de usuários for atualizado, a contagem regressiva será reiniciada.

### O que acontece com Campaigns que não enviaram uma mensagem em um ano (ou Canvas que não registraram entrada de usuários em um ano), mas têm uma data de término no futuro? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Essas Campaigns e Canvas serão interrompidos sete dias após a data de término, às 4h UTC.

#### Posso impedir que as Campaigns sejam interrompidas automaticamente? {#can-i-stop-campaigns-from-automatically-stopping}

Não. Isso ajuda a manter apenas as Campaigns necessárias ativas para deixar os dashboards menos poluídos e melhorar o desempenho. Se você quiser uma lista de todas as Campaigns interrompidas automaticamente, [envie um tíquete de suporte]({{site.baseurl}}/help/support/) para recebê-la.

### Quem receberá notificações por e-mail sobre Campaigns e Canvas interrompidos? {#who-will-receive-email-notifications-about-stopped-campaigns-and-canvases}

Por padrão, todos os usuários com permissões de administrador estão inscritos para receber notificações por e-mail sobre a interrupção automática de Campaigns e Canvas. O criador da Campaign ou do Canvas sempre será notificado quando for interrompido. Os usuários podem gerenciar as preferências de notificação por e-mail acessando **Configurações da empresa** > **Preferências de notificação** e adicionando ou removendo destinatários da notificação **Campaign Automatically Stopped** e da notificação **Canvas Automatically Stopped**.

### Como funciona a interrupção de Content Cards? {#how-does-stopping-content-cards-work}

Os Content Cards em Campaigns não serão interrompidos até o prazo de expiração e o período de buffer apropriado. Eles serão interrompidos na data mais tardia entre o período de buffer (correspondente a se a Campaign é um envio único, tem uma data de término ou não tem uma data de término) e o prazo de expiração.

Por exemplo, se um Content Card expira em 1º de abril, é um envio único e tem um prazo de conversão de 10 dias, ele será interrompido em 12 de abril (10 dias após o prazo de conversão, mais um dia). Se um Content Card expira em 1º de abril, é disparado por API e não enviou mensagens desde 15 de março, ele expirará em 15 de março do ano seguinte.

Os Canvas só são interrompidos após os Content Cards serem interrompidos, ou seja, após a duração máxima ter passado.

### Tenho um experimento de Feature Flag no meu Canvas. Após minha Feature Flag ser definida, o Canvas permanecerá ativo? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-will-the-canvas-remain-active}

Canvas com etapas de Feature Flag não são interrompidos automaticamente e não ficam sem atividades.

### Por que estou vendo Campaigns sem atividades exibidas na minha lista de Campaigns quando apliquei um filtro para mostrar apenas Campaigns ativas? {#why-am-i-seeing-idle-campaigns-displayed-in-my-campaigns-list-when-i-applied-a-filter-to-show-active-campaigns-only}

Campaigns sem atividades são consideradas ativas até serem interrompidas.

### Uma Campaign seria listada como sem atividades quando ainda está enviando notificações por push? {#would-a-campaign-be-listed-as-idle-when-its-still-sending-push-notifications}

Não. Uma Campaign será listada como sem atividades quando não estiver mais enviando mensagens ativamente.

[1]: {% image_buster /assets/unlisted_docs/img/idle_filter.png %}