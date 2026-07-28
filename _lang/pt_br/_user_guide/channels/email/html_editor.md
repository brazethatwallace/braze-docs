---
nav_title: Editor de HTML
article_title: Criar um e-mail com HTML personalizado
page_order: 2
description: "Este artigo de referência aborda como criar um e-mail usando a plataforma Braze. Inclui práticas recomendadas sobre como redigir suas mensagens, pré-visualizar seu conteúdo e programar sua campanha ou Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# Criar um e-mail com HTML personalizado {#create-an-email-with-custom-html}

> As mensagens de e-mail são ótimas para entregar conteúdo aos seus usuários nos termos deles. Também são excelentes ferramentas para reengajar usuários que podem até ter desinstalado seu app. Enviar mensagens de e-mail personalizadas e sob medida vai melhorar a experiência dos seus usuários e ajudá-los a extrair o máximo valor do seu app.

Para ver exemplos de campanhas de e-mail, confira nossos [Casos de uso](https://www.braze.com/customers).

{% alert tip %}
Se esta é a primeira vez que você cria uma campanha de e-mail, recomendamos fortemente conferir estes cursos do Braze Learning:<br><br>
- [Opt-ins e permissões de e-mail](https://learning.braze.com/messaging-channels-email)
- [Projeto: Crie um programa básico de e-mail marketing](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Use Campaigns para envios de mensagens simples e únicos. Use Canvas para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **Email** ou, para Campaigns direcionadas a vários canais, selecione **Multichannel**.
3. Dê à sua Campaign um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * As tags facilitam a busca e a criação de relatórios das suas Campaigns. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para a sua Campaign. Para saber mais sobre esse tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua Campaign forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, escolha **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Se você planeja criar HTML personalizado e precisa que os planos de fundo permaneçam consistentes no app móvel do Gmail com o modo escuro do dispositivo ativado, consulte [App móvel do Gmail e cores de fundo no modo escuro](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Etapa 2: Selecione sua experiência de edição {#step-2-choose-your-template-and-compose-your-email}

A Braze oferece duas experiências de edição ao criar uma campanha de e-mail: nosso [editor de arrastar e soltar]({{site.baseurl}}/dnd) e nosso editor de HTML padrão. Escolha o bloco apropriado para a experiência de edição que você preferir.

![Escolhendo entre o editor de arrastar e soltar, o editor de HTML ou modelos para sua experiência de edição de e-mail.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Depois, você pode selecionar um [modelo de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) existente, [fazer upload de um modelo]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) a partir de um arquivo (somente editor de HTML) ou usar um modelo em branco.

Se você usar o editor de HTML e precisar que as cores de fundo permaneçam consistentes no app móvel do Gmail quando o dispositivo estiver no modo escuro, consulte [App móvel do Gmail e cores de fundo no modo escuro](#gmail-dark-mode).

{% alert tip %}
Recomendamos selecionar uma experiência de edição por campanha de e-mail. Por exemplo, escolha **HTML Classic** ou **Block editor** em uma única campanha de e-mail em vez de alternar entre editores.
{% endalert %}

## Etapa 3: Crie seu e-mail {#step-3-compose-your-email}

Depois de selecionar seu modelo, você verá uma visão geral do seu e-mail, onde pode ir diretamente ao editor em tela cheia para redigir seu e-mail, alterar suas informações de envio e visualizar alertas sobre entregabilidade ou conformidade legal. Você pode alternar entre as guias HTML, clássico, texto simples e [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email) enquanto compõe.

![O botão "Regenerar a partir do HTML".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

A Braze atualiza automaticamente a versão em texto simples a partir da versão HTML até detectar uma edição no texto simples. Depois que a Braze detecta uma edição, ela para de atualizar o texto simples porque assume que você fez alterações intencionais. Para restaurar a sincronização automática, acesse **Texto simples** e selecione **Regenerar a partir do HTML** (visível apenas quando o texto simples não está sincronizando).

{% alert tip %}
Para adicionar movimento em um e-mail com uma prévia precisa, use GIFs em vez de elementos que exigem JavaScript, pois a maioria das caixas de entrada não suporta JavaScript.
{% endalert %}


{% alert important %}
A Braze remove automaticamente os manipuladores de eventos HTML referenciados como atributos. Isso modifica o HTML, então verifique novamente o e-mail depois de finalizar. Saiba mais sobre [manipuladores HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Precisa de ajuda para criar textos incríveis? Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto e a IA gerará textos de marketing semelhantes aos escritos por humanos para uso nas suas mensagens.

![Botão para iniciar o Assistente de Copywriting com IA, localizado na guia Corpo do criador de e-mail.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Precisa de ajuda para criar mensagens da direita para a esquerda em idiomas como árabe e hebraico? Consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) para conhecer as práticas recomendadas.

### App móvel do Gmail e modo escuro {#gmail-dark-mode}

O app móvel do Gmail (Android e iOS) pode inverter as cores de fundo quando o dispositivo está no modo escuro. Isso pode quebrar layouts em que o fundo do e-mail deve corresponder à borda de uma imagem ou a uma cor específica da marca.

Para evitar isso, na célula da tabela que precisa de um fundo estável, use um `linear-gradient` CSS de cor única em vez de `background-color`. O Gmail tem menos probabilidade de inverter esse tratamento do que uma cor de fundo sólida.

Por exemplo, para manter um fundo branco em uma célula, use isto:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Substitua `#ffffff` pela cor desejada.

{% alert note %}
Essa abordagem não se aplica de forma confiável apenas a elementos `<table aria-label="App móvel do Gmail e modo escuro #gmail-dark-mode">`, então defina o gradiente na célula em vez de apenas na tabela.
  <caption>App móvel do Gmail e modo escuro</caption>
{% endalert %}

Para saber mais sobre a sintaxe de gradientes, consulte [Gradientes CSS no W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Etapa 3.1: Adicione suas informações de envio {#step-31-add-your-sending-information}

Depois de finalizar o design e a construção da sua mensagem de e-mail, adicione suas informações de envio em **Configurações de envio**.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Uma prévia no painel à direita será preenchida com as informações de envio que você adicionou. Essas informações também podem ser atualizadas acessando **Configurações** > **Preferências de e-mail** > **Configuração de envio**.

#### Avançado {#advanced}

Em **Configurações de envio** > **Avançado**, ative o **CSS inline** para o suporte mais amplo de clientes. Se as mensagens forem cortadas ou as imagens se esticarem até a altura da linha, tente desativar o CSS inline **temporariamente**. Alguns modelos funcionam melhor sem inlining.

Você também pode adicionar personalização para cabeçalhos de e-mail e extras de e-mail para enviar dados adicionais de volta a outros provedores de serviços de e-mail.

##### Anexos de e-mail {#email-attachments}

Você também pode adicionar anexos de e-mail pelos seguintes métodos:

{% multi_lang_include email/attachment_upload_options.md %}

Consulte as [Diretrizes de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) para conhecer as práticas recomendadas específicas a serem consideradas.

##### Cabeçalhos de e-mail {#email-headers}

Para adicionar cabeçalhos de e-mail, selecione **Adicionar novo cabeçalho**. Os cabeçalhos de e-mail contêm informações sobre o e-mail sendo enviado. Esses [pares de chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) geralmente incluem informações sobre remetente, destinatário, protocolo de autenticação e roteamento. A Braze adiciona automaticamente as informações de cabeçalho exigidas pela RFC para que os e-mails cheguem aos provedores de caixa de entrada.

A Braze oferece a flexibilidade de adicionar cabeçalhos de e-mail adicionais conforme necessário para casos de uso avançados. Existem alguns campos reservados que a plataforma da Braze substituirá durante o envio.

Evite usar as seguintes chaves:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table aria-label="Cabeçalhos de e-mail" id="reserved-fields">
  <caption>Cabeçalhos de e-mail</caption>
<thead>
  <tr>
    <th>Campos reservados</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Reply-To</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>From</td>
    <td>Subject</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>To</td>
  </tr>
  <tr>
    <td>Content-Type</td>
    <td>Received</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signature</td>
    <td>received</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### Adicionando extras de e-mail {#adding-email-extras}

Os extras de e-mail permitem enviar dados adicionais de volta a outros provedores de serviços de e-mail. Isso é aplicável apenas para casos de uso avançados, então você só deve usar extras de e-mail se sua empresa já tiver essa configuração.

Para adicionar extras de e-mail, acesse **Informações de envio** e selecione **Adicionar novo extra**.

{% alert warning %}
O total de pares de chave-valor adicionados não deve exceder 1 KB. Caso contrário, as mensagens sofrerão interrupção.
{% endalert %}

Os valores de extras de e-mail não são publicados no Currents ou no Snowflake. Se você deseja enviar metadados adicionais ou valores dinâmicos para o Currents ou o Snowflake, use [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) em vez disso.

### Etapa 3.2: Pré-visualize e teste sua mensagem {#step-3b-preview-and-test-your-message}

Depois de finalizar a composição do seu e-mail, teste-o antes de enviar. Na parte inferior da tela de visão geral, selecione **Prévia e teste**.

Aqui, você pode pré-visualizar como seu e-mail aparecerá na caixa de entrada de um cliente. Com **Pré-visualizar como usuário** selecionado, você pode pré-visualizar seu e-mail como um usuário aleatório, selecionar um usuário específico ou criar um usuário personalizado. Isso permite testar se suas chamadas de Connected Content e personalização estão funcionando como esperado.

Em seguida, você pode **Copiar link de prévia** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link durará sete dias antes de precisar ser regenerado.

Você também pode alternar entre as visualizações de desktop, dispositivo móvel e texto simples para ter uma ideia de como sua mensagem aparecerá em diferentes contextos.

{% alert tip %}
Quer saber como seu e-mail fica para usuários no modo escuro? Selecione o botão **Prévia do modo escuro** localizado na seção **Prévia e teste** (apenas no editor de arrastar e soltar). Se você usa o editor de HTML, ainda pode lidar com a renderização do modo escuro do app móvel do Gmail com [App móvel do Gmail e modo escuro](#gmail-dark-mode).
{% endalert %}

Quando estiver pronto para uma verificação final, selecione **Envio de teste** e envie uma mensagem de teste para você ou para um grupo de testadores para confirmar que o e-mail é exibido corretamente em diferentes dispositivos e clientes.

![Opção de envio de teste e exemplo de prévia de e-mail ao compor seu e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Se você encontrar algum problema com seu e-mail ou quiser fazer alterações, selecione **Editar e-mail** para retornar ao editor.

{% alert tip %}
Os clientes de e-mail que suportam texto de prévia sempre puxam caracteres suficientes para preencher todo o espaço disponível de texto de prévia. No entanto, isso pode deixar você em situações em que o texto de prévia fica incompleto ou não otimizado.
<br><br>Para evitar isso, você pode criar espaço em branco após o texto de prévia desejado para que os clientes de e-mail não puxem outros textos ou caracteres que distraiam para o conteúdo do envelope. Na seção **Configurações de envio**, você pode marcar a caixa de seleção **Adicionar espaço em branco após o pré-cabeçalho** para adicionar espaço em branco automaticamente. <br><br>Alternativamente, se você precisar de mais controle, pode adicionar manualmente uma sequência de não-juntores de largura zero (‌`&zwnj;`) e espaços não separáveis (`&nbsp;`) após o texto de prévia que deseja exibir. <br><br>Quando adicionado ao final do seu texto de prévia na seção de pré-cabeçalho, o seguinte trecho de código para o editor de HTML adicionará o espaço em branco que você procura:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Para o editor de arrastar e soltar, adicione apenas os não-juntores de largura zero (‌`&zwnj;`) sem a formatação `<div>` diretamente no pré-cabeçalho na seção **Configurações de envio**.
{% endalert %}

{% alert note %}
No app Apple Mail, os links de imagem em e-mails HTML devem usar URLs `https://` para serem clicáveis. Use links seguros para qualquer imagem envolvida em uma tag de âncora quando esperar cliques de destinatários do Apple Mail.
{% endalert %}

### Etapa 3.3: Verifique erros de e-mail {#step-33-check-for-email-errors}

Antes do envio, o editor sinaliza problemas comuns:

- Nome de exibição do remetente e cabeçalho não definidos juntos
- Endereços de remetente ou de resposta inválidos
- Chaves de cabeçalho duplicadas
- Erros de sintaxe Liquid
- Content Blocks que incluem um `<!DOCTYPE html>` completo
- O corpo do e-mail excede 400&nbsp;KB
  - Procure manter [menos de 102&nbsp;KB]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips#email-size) para evitar cortes.
- Corpo ou assunto em branco
- Link de cancelamento de inscrição ausente
- Domínio do remetente não está na lista de permissões (envios fortemente limitados)

## Etapa 4: Crie o restante da sua campanha ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
Em seguida, crie o restante da sua campanha. Consulte as seções a seguir para saber como usar as ferramentas da Braze para criar sua campanha de e-mail.

### Escolha o cronograma de entrega ou o disparo {#choose-delivery-schedule-or-trigger}

Entregue e-mails com base em um horário agendado, uma ação ou um disparo de API. Para saber mais, consulte [Agendamento da sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

{% alert note %}
Para campanhas disparadas por API, quando a ação-gatilho é definida como **Interagir com Campaign**, selecionar a opção **Receber** como interação fará com que sua nova campanha seja disparada assim que a Braze marcar a Campaign selecionada como enviada, mesmo que a mensagem sofra bounce ou não seja entregue.
{% endalert %}

Você também pode definir a duração da campanha, especificar o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) e configurar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Escolha os usuários a serem direcionados {#choose-users-to-target}

Em seguida, [direcione os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo Segments ou filtros. A Braze mostra uma prévia em tempo real da população do Segment, incluindo quantos usuários são alcançáveis por e-mail. A composição exata do Segment é calculada logo antes do envio.

{% multi_lang_include audience/target_audiences.md %}

Você também pode optar por enviar sua campanha apenas para usuários com um [status de inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions) específico, como aqueles que estão inscritos e aceitaram receber e-mails.

Opcionalmente, você também pode limitar a entrega a um número específico de usuários dentro do Segment ou permitir que os usuários recebam a mesma mensagem duas vezes em caso de recorrência da campanha.

{% alert note %}
Ao criar uma nova campanha de e-mail, o grupo de controle é definido como 20% por padrão e pode ser ajustado ou removido conforme necessário para sua campanha.
{% endalert %}

#### Campanhas multicanal com e-mail e push {#multichannel-campaigns-with-email-and-push}

Para campanhas multicanal direcionadas a canais de e-mail e push, você pode querer limitar sua campanha para que apenas os usuários que aceitaram explicitamente recebam a mensagem (excluindo usuários inscritos ou não inscritos). Por exemplo, digamos que você tenha três usuários com diferentes status de aceitação:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Para fazer isso, em **Resumo do público**, selecione enviar esta campanha para "somente usuários que aceitaram". Essa opção garantirá que apenas os usuários que aceitaram receberão seu e-mail, e a Braze enviará push apenas para os usuários que estão com push ativado por padrão.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Públicos-alvo** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

### Escolha os eventos de conversão {#choose-conversion-events}

A Braze permite que você acompanhe a frequência com que os usuários realizam ações específicas, chamadas [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma campanha. Você pode especificar qualquer uma das seguintes ações como evento de conversão:

- Abre o app
- Realiza uma compra (pode ser uma compra genérica ou de um item específico)
- Realiza um evento personalizado específico
- Abre o e-mail

Você pode permitir uma janela de até 30 dias durante a qual a Braze contabiliza uma conversão se o usuário realizar a ação especificada. Embora a Braze rastreie aberturas e cliques automaticamente, você pode definir o evento de conversão como uma abertura ou clique para usar a [seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection).
{% endtab %}

{% tab Canvas %}
Se ainda não tiver feito isso, conclua as seções restantes dos componentes do seu Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar testes multivariantes e seleção inteligente, e muito mais, consulte a etapa [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) da nossa documentação de Canvas.
{% endtab %}
{% endtabs %}

## Etapa 5: Revisar e implantar {#step-5-review-and-deploy}

A seção final resume a campanha que você criou. Confirme todos os detalhes relevantes e selecione **Launch Campaign**.

Para saber como acessar os resultados das suas campanhas de e-mail, confira [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting).