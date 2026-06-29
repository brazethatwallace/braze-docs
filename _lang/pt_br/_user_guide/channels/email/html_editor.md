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

Use Campaigns para envio de mensagens simples e únicas. Use Canvas para jornadas de usuário com múltiplas etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **Email** ou, para campanhas direcionadas a múltiplos canais, selecione **Multichannel**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) conforme necessário.
   * Tags facilitam encontrar suas campanhas e criar relatórios a partir delas. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Para saber mais sobre este tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes extras. Depois, escolha **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Escolha um [cronograma de etapa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) e especifique uma postergação conforme necessário.
4. Filtre seu público para esta etapa, se necessário. Você pode refinar ainda mais os destinatários desta etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Escolha quaisquer outros canais de envio de mensagens que você deseja combinar com sua mensagem.
{% endtab %}
{% endtabs %}

{% alert tip %}
Se você planeja criar HTML personalizado e precisa que os fundos permaneçam consistentes no app móvel do Gmail com o modo escuro do dispositivo ativado, consulte [App móvel do Gmail e cores de fundo no modo escuro](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Etapa 2: Selecione sua experiência de edição {#step-2-choose-your-template-and-compose-your-email}

A Braze oferece duas experiências de edição ao criar uma campanha de e-mail: nosso [editor de arrastar e soltar]({{site.baseurl}}/dnd/) e nosso editor de HTML padrão. Escolha o bloco apropriado para a experiência de edição que você preferir.

![Escolhendo entre o editor de arrastar e soltar, o editor de HTML ou modelos para sua experiência de edição de e-mail.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Depois, você pode selecionar um [modelo de e-mail]({{site.baseurl}}/user_guide/channels/email/html_editor/#creating-an-email-template) existente, [fazer upload de um modelo]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template/) a partir de um arquivo (somente editor de HTML) ou usar um modelo em branco.

Se você usar o editor de HTML e precisar que as cores de fundo permaneçam consistentes no app móvel do Gmail quando o dispositivo estiver no modo escuro, consulte [App móvel do Gmail e cores de fundo no modo escuro](#gmail-dark-mode).

{% alert tip %}
Recomendamos selecionar uma experiência de edição por campanha de e-mail. Por exemplo, escolha **HTML Classic** ou **Block editor** em uma única campanha de e-mail em vez de alternar entre editores.
{% endalert %}

## Etapa 3: Redija seu e-mail {#step-3-compose-your-email}

Depois de selecionar seu modelo, você verá uma visão geral do seu e-mail onde pode ir diretamente ao editor em tela cheia para redigir seu e-mail, alterar suas informações de envio e visualizar avisos sobre entregabilidade ou conformidade legal. Você pode alternar entre as guias HTML, clássico, texto simples e [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email/) enquanto redige.

![O botão "Regenerar a partir do HTML".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

A Braze atualiza automaticamente a versão em texto simples a partir da versão HTML até detectar uma edição no texto simples. Depois que a Braze detecta uma edição, ela para de atualizar o texto simples porque assume que você fez alterações intencionais. Para restaurar a sincronização automática, acesse **Plaintext** e selecione **Regenerate from HTML** (visível apenas quando o texto simples não está sincronizando).

{% alert tip %}
Para adicionar movimento em um e-mail com uma pré-visualização precisa, use GIFs em vez de elementos que requerem JavaScript, pois a maioria das caixas de entrada não suporta JavaScript.
{% endalert %}


{% alert important %}
A Braze remove automaticamente os manipuladores de eventos HTML referenciados como atributos. Isso modifica o HTML, então verifique novamente o e-mail depois de terminar. Saiba mais sobre [manipuladores HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Precisa de ajuda para criar textos incríveis? Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy). Insira o nome ou a descrição de um produto e a IA gerará textos de marketing semelhantes aos escritos por humanos para uso no seu envio de mensagens.

![Botão Iniciar Assistente de Copywriting com IA, localizado na guia Corpo do criador de e-mail.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Precisa de ajuda para criar mensagens da direita para a esquerda para idiomas como árabe e hebraico? Consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/) para práticas recomendadas.

### App móvel do Gmail e modo escuro {#gmail-dark-mode}

O app móvel do Gmail (Android e iOS) pode inverter as cores de fundo quando o dispositivo está no modo escuro. Isso pode quebrar layouts onde o fundo do e-mail deve corresponder à borda de uma imagem ou a uma cor específica da marca.

Para evitar isso, na célula da tabela que precisa de um fundo estável, use um `linear-gradient` CSS de cor única em vez de `background-color`. O Gmail tem menos probabilidade de inverter esse tratamento do que uma cor de fundo plana.

Por exemplo, para manter um fundo branco em uma célula, use isto:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Substitua `#ffffff` pela cor desejada.

{% alert note %}
Essa abordagem não se aplica de forma confiável apenas a elementos `<table aria-label="Gmail mobile app and dark mode #gmail-dark-mode">`, então defina o gradiente na célula em vez de apenas na tabela.
  <caption>Gmail mobile app and dark mode</caption>
{% endalert %}

Para mais informações sobre a sintaxe de gradientes, consulte [Gradientes CSS no W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Etapa 3.1: Adicione suas informações de envio {#step-31-add-your-sending-information}

Depois de terminar de projetar e construir sua mensagem de e-mail, adicione suas informações de envio em **Sending Settings**.

1. Em **Sending Info**, selecione um e-mail como **From Display Name + Address**. Você também pode personalizar isso selecionando **Customize From Display Name + Address**.
2. Selecione um e-mail como **Reply-To Address**. Você também pode personalizar isso selecionando **Customize Reply-To Address**.
3. Em seguida, selecione um e-mail como **BCC Address** para tornar seu e-mail visível para esse endereço.
4. Adicione uma linha de assunto ao seu e-mail. Opcionalmente, você também pode adicionar um pré-cabeçalho e um espaço em branco após o pré-cabeçalho.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Uma pré-visualização no painel à direita será preenchida com as informações de envio que você adicionou. Essas informações também podem ser atualizadas acessando **Settings** > **Email Preferences** > **Sending Configuration**.

#### Avançado {#advanced}

Em **Sending Settings** > **Advanced**, ative **inline CSS** para o suporte mais amplo de clientes. Se as mensagens forem cortadas ou as imagens se esticarem até a altura da linha, tente desativar o inline CSS **temporariamente**. Alguns modelos funcionam melhor sem inlining.

Você também pode adicionar personalização para cabeçalhos de e-mail e extras de e-mail para enviar dados adicionais de volta para outros prestadores de serviço de e-mail.

##### Anexos de e-mail {#email-attachments}

Você também pode adicionar anexos de e-mail pelos seguintes métodos:

- **Fazer upload de um arquivo:** Arraste e solte ou navegue para fazer upload de um arquivo diretamente do seu computador para o e-mail. A Braze valida o tipo e o tamanho do arquivo (até 2&nbsp;MB por padrão) antes do upload, e então esses arquivos são enviados para a biblioteca de mídia. Arquivos maiores que o limite de 2&nbsp;MB não podem ser enviados.
- **Usar a biblioteca de mídia:** Navegue e selecione entre os ativos já armazenados na [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). PDFs, documentos Word, arquivos Excel e apresentações PowerPoint são todos suportados.
- **Adicionar a partir de URL:** Insira uma URL apontando para o arquivo e forneça um nome de exibição para o arquivo. Como a Braze não pode verificar URLs arbitrárias quanto ao tamanho durante a composição do e-mail, o tamanho do arquivo é aplicado no momento do envio. Observe que Liquid não é suportado neste campo.

Consulte as [Diretrizes de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines/) para práticas recomendadas específicas a considerar.

##### Cabeçalhos de e-mail {#email-headers}

Para adicionar cabeçalhos de e-mail, selecione **Add New Header**. Os cabeçalhos de e-mail contêm informações sobre o e-mail sendo enviado. Esses [pares de chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) geralmente incluem informações sobre remetente, destinatário, protocolo de autenticação e roteamento. A Braze adiciona automaticamente as informações de cabeçalho exigidas pela RFC para que os e-mails cheguem aos provedores de caixa de entrada.

A Braze permite a flexibilidade de adicionar cabeçalhos de e-mail adicionais conforme necessário para casos de uso avançados. Existem alguns campos reservados que a plataforma Braze substituirá durante o envio.

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

Os extras de e-mail permitem enviar dados adicionais de volta para outros prestadores de serviço de e-mail. Isso é aplicável apenas para casos de uso avançados, então você só deve usar extras de e-mail se sua empresa já tiver isso configurado.

Para adicionar extras de e-mail, acesse **Sending Info** e selecione **Add New Extra**.

{% alert warning %}
O total de pares de chave-valor adicionados não deve exceder 1 KB. Caso contrário, as mensagens serão abortadas.
{% endalert %}

Os valores de extras de e-mail não são publicados no Currents ou Snowflake. Se você deseja enviar metadados adicionais ou valores dinâmicos para o Currents ou Snowflake, use [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras/) em vez disso.

### Etapa 3.2: Pré-visualize e teste sua mensagem {#step-3b-preview-and-test-your-message}

Depois de terminar de redigir seu e-mail, teste-o antes de enviar. Na parte inferior da tela de visão geral, selecione **Preview and Test**.

Aqui, você pode pré-visualizar como seu e-mail aparecerá na caixa de entrada de um cliente. Com **Preview as User** selecionado, você pode pré-visualizar seu e-mail como um usuário aleatório, selecionar um usuário específico ou criar um usuário personalizado. Isso permite testar se suas chamadas de Conteúdo conectado e personalização estão funcionando como esperado.

Depois, você pode usar **Copy preview link** para gerar e copiar um link de pré-visualização compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link durará sete dias antes de precisar ser regenerado.

Você também pode alternar entre as visualizações de desktop, celular e texto simples para ter uma ideia de como sua mensagem aparecerá em diferentes contextos.

{% alert tip %}
Curioso sobre como seu e-mail fica para usuários no modo escuro? Selecione o botão **Dark Mode Preview** localizado na seção **Preview and Test** (somente editor de arrastar e soltar). Se você usar o editor de HTML, ainda pode lidar com a renderização do modo escuro no app móvel do Gmail com [App móvel do Gmail e modo escuro](#gmail-dark-mode).
{% endalert %}

Quando estiver pronto para uma verificação final, selecione **Test Send** e envie uma mensagem de teste para você mesmo ou para um grupo de testadores para confirmar que o e-mail é exibido corretamente em diferentes dispositivos e clientes.

![Opção de envio de teste e exemplo de pré-visualização de e-mail ao redigir seu e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Se você encontrar algum problema com seu e-mail ou quiser fazer alterações, selecione **Edit Email** para retornar ao editor.

{% alert tip %}
Clientes de e-mail que suportam texto de pré-visualização sempre puxam caracteres suficientes para preencher todo o espaço disponível de texto de pré-visualização. No entanto, isso pode deixá-lo em situações onde o texto de pré-visualização está incompleto ou não otimizado.
<br><br>Para evitar isso, você pode criar espaço em branco após o texto de pré-visualização desejado para que os clientes de e-mail não puxem outros textos ou caracteres que distraiam para o conteúdo do envelope. Para isso, adicione uma cadeia de zero-width non-joiners (‌`&zwnj;`) e espaços não quebráveis (`&nbsp;`) após o texto de pré-visualização que você deseja exibir. <br><br>Quando adicionado ao final do seu texto de pré-visualização na seção de pré-cabeçalho, o seguinte trecho de código para o editor de HTML adicionará o espaço em branco que você procura:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Para o editor de arrastar e soltar, adicione apenas os zero-width non-joiners (‌`&zwnj;`) sem a formatação `<div>` diretamente no pré-cabeçalho na seção **Sending Settings**.
{% endalert %}

{% alert note %}
No app Apple Mail, links de imagem em e-mails HTML devem usar URLs `https://` para serem clicáveis. Use links seguros para qualquer imagem envolvida em uma tag de âncora quando você esperar cliques de destinatários do Apple Mail.
{% endalert %}

### Etapa 3.3: Verifique erros de e-mail {#step-33-check-for-email-errors}

Antes do envio, o editor sinaliza problemas comuns:

- Nome de exibição do remetente e cabeçalho não configurados juntos
- Endereços de remetente ou resposta inválidos
- Chaves de cabeçalho duplicadas
- Erros de sintaxe Liquid
- Content Blocks que incluem um `<!DOCTYPE html>` completo
- Corpo do e-mail acima de 400&nbsp;KB
  - Procure manter [menos de 102&nbsp;KB]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size) para evitar cortes.
- Corpo ou assunto em branco
- Link de cancelamento de inscrição ausente
- Domínio do remetente não na lista de permissões (envios fortemente limitados)

## Etapa 4: Construa o restante da sua campanha ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
Em seguida, construa o restante da sua campanha. Consulte as seções a seguir para detalhes sobre como usar as ferramentas da Braze para construir sua campanha de e-mail.

### Escolha o cronograma de entrega ou gatilho {#choose-delivery-schedule-or-trigger}

Entregue e-mails com base em um horário programado, uma ação ou um gatilho de API. Para saber mais, consulte [Programando sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

{% alert note %}
Para Campaigns disparadas por API, quando a ação-gatilho é definida como **Interact With Campaign**, selecionar uma opção **Receive** como interação fará com que sua nova campanha seja disparada assim que a Braze marcar a campanha selecionada como enviada, mesmo que essa mensagem sofra bounce ou falhe na entrega.
{% endalert %}

Você também pode definir a duração da campanha, especificar o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) e definir regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

### Escolha os usuários-alvo {#choose-users-to-target}

Em seguida, [direcione os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) escolhendo segmentos ou filtros. A Braze mostra uma pré-visualização ao vivo da população do segmento, incluindo quantos usuários são alcançáveis por e-mail. A associação exata ao segmento é calculada logo antes do envio.

{% multi_lang_include audience/target_audiences.md %}

Você também pode optar por enviar sua campanha apenas para usuários que tenham um [status de inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions/) específico, como aqueles que estão inscritos e optaram por receber e-mail.

Opcionalmente, você também pode limitar a entrega a um número específico de usuários dentro do segmento, ou permitir que os usuários recebam a mesma mensagem duas vezes em caso de recorrência da campanha.

{% alert note %}
Ao criar uma nova campanha de e-mail, o grupo de controle é definido como 20% por padrão e pode ser ajustado ou removido conforme necessário para sua campanha.
{% endalert %}

#### Campaigns multicanal com e-mail e push {#multichannel-campaigns-with-email-and-push}

Para Campaigns multicanal direcionadas a canais de e-mail e push, você pode querer limitar sua campanha para que apenas os usuários que explicitamente optaram por receber a mensagem (excluindo usuários inscritos ou com inscrição cancelada). Por exemplo, digamos que você tenha três usuários com diferentes status de opt-in:

- **Usuário A** está inscrito em e-mail e tem push ativado. Este usuário não recebe o e-mail, mas receberá o push.
- **Usuário B** optou por receber e-mail, mas não tem push ativado. Este usuário receberá o e-mail, mas não receberá o push.
- **Usuário C** optou por receber e-mail e tem push ativado. Este usuário receberá tanto o e-mail quanto o push.

Para fazer isso, em **Audience Summary**, selecione enviar esta campanha para "opted-in users only". Esta opção garantirá que apenas usuários que optaram por receber receberão seu e-mail, e a Braze enviará seu push apenas para usuários que têm push ativado por padrão.

{% alert important %}
Com esta configuração, não inclua nenhum filtro na etapa **Target Audiences** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite rastrear com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você pode especificar qualquer uma das seguintes ações como evento de conversão:

- Abre o app
- Realiza uma compra (pode ser uma compra genérica ou um item específico)
- Realiza um evento personalizado específico
- Abre o e-mail

Você pode permitir um período de até 30 dias durante o qual a Braze conta uma conversão se o usuário realizar a ação especificada. Embora a Braze rastreie aberturas e cliques automaticamente, você pode definir o evento de conversão como uma abertura ou clique para usar a [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Se ainda não o fez, conclua as seções restantes dos seus componentes de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar testes multivariantes e Seleção inteligente, e mais, consulte a etapa [Construa seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação de Canvas.
{% endtab %}
{% endtabs %}

## Etapa 5: Revise e implante {#step-5-review-and-deploy}

A seção final resume a campanha que você projetou. Confirme todos os detalhes relevantes e selecione **Launch Campaign**.

Para saber como acessar os resultados das suas campanhas de e-mail, confira [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/).