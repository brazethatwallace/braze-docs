---
nav_title: Criar uma mensagem de WhatsApp
article_title: Criar uma mensagem de WhatsApp
page_order: 1
description: "Este artigo de referência aborda como criar uma mensagem de WhatsApp e configurar campos, configurações e comportamentos específicos do WhatsApp."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - WhatsApp
search_rank: 1
---

# Criar uma mensagem de WhatsApp {#create-a-whatsapp-message}

> Use Campaigns de WhatsApp para alcançar seus clientes diretamente. Use Liquid e outros conteúdos dinâmicos para personalizar cada mensagem e criar uma experiência de marca consistente.

## Pré-requisitos {#prerequisites}

Antes de começar, verifique se você tem o seguinte:

| Requisito | Descrição |
| --- | --- |
| Campaign ou Canvas | Configure uma [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou um [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) antes de criar sua mensagem do WhatsApp. |
| Configuração do canal do WhatsApp | Conclua o [fluxo de configuração do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup): reconheça as políticas, configure sua conexão e defina a infraestrutura de envio. |
| Modelos aprovados | Para envios iniciados pela empresa, crie e aprove modelos na Meta. Para mais detalhes, consulte a [etapa 3 da configuração do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos de mensagens do WhatsApp" }

## Tipo de mensagem {#message-type}

O WhatsApp oferece suporte a dois tipos de mensagem na Braze:

- **Mensagem de modelo:** Use para conversas iniciadas pela empresa. Os modelos devem ser aprovados na Meta antes do envio.
- **Mensagem de resposta:** Use para responder a mensagens recebidas do usuário durante uma janela de conversa ativa de 24 horas.

## Grupo de inscrições {#subscription-group}

Selecione um grupo de inscrições do WhatsApp para cada variante de mensagem ou etapa de mensagem do Canvas. O grupo de inscrições determina qual configuração de remetente é usada e quais usuários são elegíveis para receber a mensagem.

## Idiomas para mensagens de modelo {#languages-for-template-messages}

Cada modelo aprovado está vinculado a um idioma específico. Configure variantes separadas ou etapas do Canvas quando precisar oferecer suporte a vários idiomas de modelo.

Se você estiver adicionando texto em um idioma da direita para a esquerda, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Composição {#step-2-compose-your-whatsapp-message}

Crie seu conteúdo do WhatsApp no criador de mensagem. Para opções de configuração específicas do WhatsApp, use a referência de campos a seguir.

| Campo ou configuração | O que ele controla | Notas |
| --- | --- | --- |
| **Grupo de inscrições** | O remetente do WhatsApp e o público elegível para a mensagem. | O número de telefone de envio associado aparece no alerta da guia **Teste**. |
| **Tipo de mensagem** | Se a variante envia uma mensagem de modelo ou uma mensagem de resposta. | Envios iniciados pela empresa exigem um modelo. Mensagens de resposta exigem uma janela de conversa ativa. |
| **Modelo** (Mensagens de modelo) | O modelo aprovado da Meta usado para enviar a mensagem. | Campos desativados no criador vêm do modelo aprovado e só podem ser alterados na Meta após nova aprovação. |
| **Idioma** (Mensagens de modelo) | O idioma do modelo selecionado para a variante ou etapa. | Crie uma variante de campanha ou etapa do Canvas por idioma para corresponder aos destinatários corretamente. |
| **Variáveis** (Mensagens de modelo) | Valores inseridos nos espaços reservados de variáveis do modelo. | Use Liquid ou texto simples entre chaves duplas. Inclua valores padrão para Liquid para que os envios não falhem quando dados do perfil estiverem ausentes. |
| **Links dinâmicos** | URLs personalizadas de chamada para ação. | A Meta exige que as variáveis apareçam no final das URLs de CTA. |
| **Imagens dinâmicas** | URL de mídia ou imagem da biblioteca de mídia usada em mensagens de modelo ou de resposta. | Imagens dinâmicas aceitam Liquid e Connected Content em URLs. |
| **Layout de resposta** (Mensagens de resposta) | O formato do conteúdo da resposta. | Os layouts compatíveis são Quick Reply, Text Message, Media Message, Call-to-action Button, List Message, Flow Message, Meta Product Messages e Carousel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos e configurações específicos do WhatsApp" }

{% tabs %}
{% tab Mensagens de modelo %}

### Mensagens de modelo {#template-messages}

Use [mensagens de modelo aprovadas do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates) para iniciar conversas no WhatsApp. As aprovações de modelo são feitas pela Meta e podem levar até 24 horas. Se você editar o texto do modelo, atualize-o na Meta e reenvie para aprovação.

Para criar e enviar um novo modelo sem sair do criador de campanha ou Canvas, selecione **Criar novo modelo**. Para categorias, tipos e o processo completo de criação, consulte [Construtor de modelos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder).

Campos de texto desativados (destacados em cinza) não podem ser editados, pois fazem parte do modelo aprovado do WhatsApp. Para fazer atualizações no texto desativado, você precisa editar o modelo e obter nova aprovação.

#### Campos de conteúdo {#content-fields}

Use a tabela de referência de campos para as definições de variáveis, links dinâmicos e imagens dinâmicas. Esta seção aborda o comportamento e os exemplos específicos de modelos.

![Lista de modelos com prévias de suas mensagens, idiomas atribuídos e status de aprovação.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

{% alert tip %}
Se você usar Liquid, inclua valores padrão para os campos de personalização. Mensagens com valores de personalização ausentes não são enviadas pelo WhatsApp.
{% endalert %}

![Ferramenta Adicionar Personalização com o atributo "first_name" e o valor padrão "you".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Imagens dinâmicas {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Mensagens de resposta %}

### Mensagens de resposta {#response-messages}

Use mensagens de resposta para responder a mensagens recebidas dos usuários durante a janela de conversa ativa de 24 horas. Essas mensagens são criadas na Braze e podem ser editadas a qualquer momento.

As mensagens de resposta aceitam os seguintes layouts:
- Quick Reply
- Text Message
- Media Message
- Call-to-action Button
- List Message
- Flow Message
- Meta Product Messages
- Carousel

![Criador de mensagem de resposta para uma Reply Message que dá as boas-vindas a novos usuários com um código de desconto.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

## Resultados do envio de teste do WhatsApp {#step-4-view-test-send-results}

Após enviar uma mensagem de teste do WhatsApp, você pode visualizar um relatório detalhado de entrega diretamente no criador de mensagem. Isso ajuda a confirmar que sua mensagem chegou ao destinatário pretendido e a solucionar falhas antes do lançamento.

O botão **View test results** aparece quando os dados do envio de teste estão disponíveis para a Campaign ou etapa do Canvas atual. Selecione-o para abrir o painel de resultados.

O painel de resultados mostra cada estágio pelo qual sua mensagem passou até chegar ao destinatário:
- **Braze:** Se a Braze processou e despachou a mensagem com sucesso
- **Meta:** Se a Meta aceitou a mensagem para entrega
- **User device:** Se a mensagem foi entregue ao dispositivo do destinatário

Cada estágio exibe seu status atual. Se um estágio falhar, o painel mostra o erro encontrado e orientações sobre como resolvê-lo. Os resultados persistem se você fechar e reabrir a mesma Campaign ou Canvas.

![Painel de resultados de teste mostrando dois envios de teste bem-sucedidos e um envio de teste com falha.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

### Tentativas e tentativas anteriores {#retries-and-past-attempts}

Se um envio de teste falhar, a Braze tenta automaticamente a entrega por até 24 horas. O painel de resultados reflete isso com duas guias:

- **Latest:** A tentativa de entrega mais recente, atualizada em tempo real conforme as novas tentativas ocorrem
- **Past attempts:** Um histórico de tentativas anteriores, cada uma mostrando os status dos estágios e quaisquer erros encontrados

Quando o resultado final é determinado (entrega bem-sucedida, tentativas esgotadas ou uma falha que novas tentativas não resolverão), as guias são renomeadas respectivamente para **Result** e **Retry history**.

{% alert note %}
Como as tentativas podem continuar por até 24 horas, talvez você não veja um resultado final imediatamente após um envio com falha.
{% endalert %}

### Solução de problemas de falhas {#troubleshoot-failures}

Se um estágio mostrar uma falha, o painel exibe o erro e as próximas etapas sugeridas. Motivos comuns para a falha de um envio de teste incluem:

- O modelo de mensagem está pausado ou ainda não foi aprovado na Meta
- O número de telefone do destinatário está com taxa limitada
- As variáveis Liquid na mensagem não foram preenchidas para o usuário teste selecionado

Para problemas persistentes, verifique o status do seu modelo no Meta Business Manager ou confirme que o destinatário de teste possui os atributos de usuário necessários preenchidos na Braze.

## O que você precisa saber {#supported-whatsapp-features}

### Mensagens de saída {#outbound-messages}

Os seguintes recursos são compatíveis com mensagens de saída do WhatsApp enviadas pela Braze:

| Recurso | Detalhes | Tamanho máximo | Formatos compatíveis |
| ------- | ------- | ------------- | ---------------------- |
| Texto do cabeçalho | Strings e parâmetros variáveis são compatíveis. | — | —
| Texto do corpo | Strings e parâmetros variáveis são compatíveis. | — | — |
| Texto do rodapé | Strings e parâmetros variáveis são compatíveis. | — | — |
| Links de CTA | Vários tipos de chamada para ação (CTA) são compatíveis. Para saber mais, consulte [Tipos de chamada para ação](#ctas). | — | — |
| Imagens | As imagens podem ser incorporadas no texto do corpo. Elas devem ser de 8 bits e usar o modelo de cores RGB ou RGBA. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Documentos | Os documentos podem ser incorporados no texto do corpo. Os arquivos devem ser hospedados por URL. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Vídeos | Os vídeos podem ser incorporados no texto do corpo. Os arquivos devem ser hospedados por URL ou na [biblioteca de mídia da Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). | < 16 MB | `.3gp`, `.mp4` |
| Áudio | O áudio só é compatível por meio de mensagens de resposta. Os arquivos devem ser hospedados por URL. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensagens de saída" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Mensagens de entrada {#inbound-messages}

Os seguintes recursos são compatíveis com mensagens de entrada do WhatsApp recebidas pela Braze:

| Recurso | Detalhes | Formatos compatíveis |
| ------- | ------- | ------------------ |
| Texto do corpo | Somente strings padrão são compatíveis. | — |
| Imagens | As imagens devem ser de 8 bits e usar o modelo de cores RGB ou RGBA. Os arquivos devem ter menos de 5 MB. | `.jpg`, `.png` |
| Áudio | Somente arquivos Ogg codificados com o codec Opus são compatíveis. Outros formatos Ogg não são compatíveis. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documentos | Os documentos são compatíveis por meio de anexo de mensagem. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Vídeo | Somente o codec de vídeo H.264 e o codec de áudio AAC são compatíveis. Os vídeos devem ter uma única faixa de áudio ou nenhuma faixa de áudio. | `.mp4`, `.3gp` |
| Links de CTA | Vários tipos de chamada para ação (CTA) são compatíveis. Para saber mais, consulte [Tipos de chamada para ação](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensagens de entrada" }

### Tipos de chamada para ação {#ctas}

Os seguintes tipos de chamada para ação são compatíveis com mensagens do WhatsApp enviadas pela Braze:

| Tipo de CTA | Detalhes |
| ----------- |---------------- |
| Visitar website | No máximo um botão (incluindo parâmetros variáveis). |
| Ligar para número de telefone | Disponível apenas para modelos de mensagem. <br>No máximo um botão. |
| Botões de resposta rápida personalizados | No máximo três botões. |
| Botão de cancelamento de marketing | Por padrão, os status de inscrição não são atualizados automaticamente. Para um passo a passo completo, consulte [Aceitações e cancelamentos]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection). |
| Modelos de mensagem com código de cupom | Disponível apenas para modelos de mensagem. <br>Eles podem ser abertos e editados como outros modelos de mensagem e são compatíveis com Liquid e códigos de promoção da Braze. |
| Mensagens de resposta com CTA | Crie uma mensagem de resposta que inclua um botão de chamada para ação. |
| [Mensagens de resposta em lista]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | Crie uma mensagem de resposta que inclua uma lista com até 10 opções para os usuários escolherem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de chamada para ação" }

## Próximas etapas {#next-steps}

Depois de compor sua mensagem do WhatsApp, continue criando e validando seu envio:

{% article_tiles %}
- name: Criar um Canvas
  link: /docs/user_guide/messaging/canvas/create_a_canvas
- name: Agendar sua campanha
  link: /docs/user_guide/messaging/campaigns/schedule_your_campaign
- name: Direcionar usuários
  link: /docs/user_guide/messaging/messaging_fundamentals/target_users
- name: Eventos de conversão
  link: /docs/user_guide/messaging/messaging_fundamentals/conversion_events
- name: Enviar mensagens de teste
  link: /docs/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp
- name: Relatórios do WhatsApp
  link: /docs/user_guide/channels/whatsapp/reporting
{% endarticle_tiles %}