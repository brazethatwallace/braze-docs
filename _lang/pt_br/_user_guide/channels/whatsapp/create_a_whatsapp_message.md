---
nav_title: Criar uma mensagem de WhatsApp
article_title: Criar uma mensagem de WhatsApp
page_order: 1
description: "Este artigo de referência aborda as etapas envolvidas na criação de uma mensagem de WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Criar uma mensagem de WhatsApp {#create-a-whatsapp-message}

> Campaigns de WhatsApp são ótimas para alcançar diretamente seus clientes e conversar com eles de forma programática. Você pode usar Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e promover um ambiente que incentive e aprimore uma experiência discreta com a sua marca.

## Pré-requisitos {#prerequisites}

Antes de criar mensagens de WhatsApp, você precisa revisar e concluir o seguinte na [Visão geral do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup):
  - Reconhecer as políticas, limites e regras de conteúdo
  - Configurar sua conexão com o WhatsApp
  - Criar modelos iniciais no Meta para usar em suas mensagens

## Criando uma mensagem {#creating-a-message}

### Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

{% alert note %}
O WhatsApp cria diferentes [modelos de mensagem](#template-messages) para cada idioma. Crie uma Campaign para cada idioma com segmentação para enviar o modelo correto aos usuários, ou use o Canvas.
{% endalert %}

Não tem certeza se sua mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de envio de mensagens únicas e direcionadas, enquanto Canvas são melhores para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

**Etapas:**

1. Acesse a página **Campaigns** e clique em <i class="fas fa-plus"></i> **Create Campaign**.
2. Selecione **WhatsApp** ou, para campanhas direcionadas a múltiplos canais, selecione **Multichannel Campaign**.
3. Dê à sua Campaign um nome claro e significativo.
4. Adicione [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a busca e a criação de relatórios das suas campanhas. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua Campaign. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada variante adicionada. Para saber mais sobre este tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua Campaign forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes extras. Em seguida, escolha **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Escolha um [agendamento de etapa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) e especifique uma postergação conforme necessário.
4. Filtre seu público para esta etapa conforme necessário. Você pode refinar ainda mais os destinatários desta etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Escolha quaisquer outros canais de envio de mensagens que deseja combinar com sua mensagem.

{% alert tip %}
Se um Canvas baseado em ação for disparado por uma mensagem de WhatsApp recebida, você pode referenciar as propriedades do WhatsApp em qualquer etapa do Canvas até a próxima jornada de ação.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 2: Crie sua mensagem de WhatsApp {#step-2-compose-your-whatsapp-message}

Selecione se deseja criar uma [mensagem de modelo](#template-messages) de WhatsApp ou uma mensagem de resposta, dependendo do seu caso de uso. Qualquer conversa iniciada pela empresa deve começar com um modelo aprovado, enquanto mensagens de resposta podem ser usadas em respostas a mensagens recebidas de usuários dentro de uma janela de 24 horas.

![A seção Variantes de mensagem permite selecionar um grupo de inscrições e um dos dois tipos de mensagem: Mensagem de modelo do WhatsApp e Mensagem de resposta.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Mensagens de modelo %}

Você pode usar [modelos de mensagem aprovados do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates
) para iniciar conversas com seus usuários no WhatsApp. Essas mensagens são enviadas antecipadamente ao WhatsApp para aprovação de conteúdo, o que pode levar até 24 horas. Qualquer edição que você fizer no texto precisa ser editada e reenviada ao WhatsApp.

Campos de texto desabilitados (destacados em cinza) não podem ser editados, pois fazem parte do modelo aprovado do WhatsApp. Para fazer atualizações no texto desabilitado, você deve editar seu modelo e obter uma nova aprovação.

#### Idiomas {#languages}

Cada modelo tem um idioma atribuído, então você precisa criar uma Campaign ou etapa do Canvas para cada idioma para configurar corretamente a correspondência de usuários. Por exemplo, se você está criando um Canvas que usa modelos atribuídos com indonésio e inglês, precisa criar uma etapa do Canvas para o modelo em indonésio e uma etapa do Canvas para o modelo em inglês.

![Lista de modelos incluindo pré-visualizações de suas mensagens, seus idiomas atribuídos e seus status de aprovação.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Se você estiver adicionando texto em um idioma escrito da direita para a esquerda, observe que a aparência final das mensagens da direita para a esquerda depende em grande parte de como os prestadores de serviço as renderizam. Para práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Variáveis {#variables}

Se você adicionou variáveis ao criar o modelo do WhatsApp no Meta Business Manager, essas variáveis aparecerão como espaços em branco no criador de mensagens. Substitua esses espaços em branco por Liquid ou texto simples. Para usar texto simples, use o formato "texto aqui" entre chaves duplas. Se você optou por incluir imagens ao criar seu modelo, pode fazer upload ou adicionar imagens da biblioteca de mídia ou referenciando uma URL de imagem. Quando possível, recomendamos fazer upload das imagens diretamente na sua biblioteca de mídia para garantir consistência e confiabilidade.

Observe que campos de texto desabilitados (destacados em cinza) não podem ser editados, pois fazem parte do modelo aprovado do WhatsApp. Se você deseja fazer atualizações no texto desabilitado, deve editar seu modelo e obter uma nova aprovação.

{% alert tip %}
{% raw %}
Se você planeja usar Liquid, inclua um valor padrão para a personalização escolhida, para que, caso o perfil do usuário destinatário esteja incompleto, ele não receba uma mensagem. Qualquer mensagem com variáveis Liquid ausentes não será enviada pelo WhatsApp.
{% endraw %}
{% endalert %}

![A ferramenta Adicionar personalização com o atributo "first_name" e o valor padrão "you".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Links dinâmicos {#dynamic-links}

URLs de chamada para ação podem conter variáveis, mas o Meta exige que elas estejam no final da URL, como `{% raw %}https://example.com/{{variable}}{% endraw %}`, onde a variável pode ser substituída na Braze com Liquid. Links também podem ser incluídos como texto do corpo como parte do modelo. Ambos os tipos de links podem ser encurtados e rastreados usando o [rastreamento de cliques]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking).

### Imagens dinâmicas {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Mensagens de resposta %}

Você pode usar mensagens de resposta para responder a mensagens recebidas de seus usuários. Essas mensagens são criadas no app na Braze durante sua experiência de composição e podem ser editadas a qualquer momento. Você pode usar Liquid para combinar o idioma da mensagem de resposta com os usuários apropriados.

Existem cinco layouts de mensagem de resposta que você pode usar:
- Resposta rápida
- Mensagem de texto
- Mensagem de mídia
- Botão de chamada para ação
- Mensagem de lista

![O criador de mensagens de resposta para uma mensagem de resposta que dá boas-vindas a novos usuários com um código de desconto.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Etapa 3: Pré-visualize e teste sua mensagem {#step-3-preview-and-test-your-message}

A Braze sempre recomenda pré-visualizar e testar sua mensagem antes de enviá-la. Alterne para a guia **Test** para enviar uma mensagem de teste do WhatsApp para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuários individuais, ou pré-visualize a mensagem como um usuário diretamente na Braze.

![Uma pré-visualização de mensagem para um usuário personalizado chamado Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
Uma janela de conversa é necessária para enviar mensagens de resposta, incluindo mensagens de teste. Para iniciar uma janela de conversa, envie uma mensagem de WhatsApp para o número de telefone associado ao grupo de inscrições que você está usando para esta mensagem. O número de telefone associado está listado no alerta na guia **Test**.
{% endalert %}

![Um alerta que diz para abrir uma janela de mensagem enviando uma mensagem de WhatsApp e, em seguida, enviar uma mensagem para o usuário teste.]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp).

### Etapa 4: Visualize os resultados do envio de teste {#step-4-view-test-send-results}

Após enviar uma mensagem de teste do WhatsApp, você pode visualizar um relatório detalhado de entrega diretamente no criador de mensagens. Isso ajuda a confirmar que sua mensagem chegou ao destinatário pretendido e a solucionar falhas antes do lançamento.

O botão **View test results** aparece quando há dados de envio de teste disponíveis para a Campaign ou etapa do Canvas atual. Selecione-o para abrir o painel de resultados.

O painel de resultados mostra cada estágio pelo qual sua mensagem passou até chegar ao destinatário:
- **Braze:** Se a Braze processou e despachou a mensagem com sucesso
- **Meta:** Se o Meta aceitou a mensagem para entrega
- **Dispositivo do usuário:** Se a mensagem foi entregue ao dispositivo do destinatário

Cada estágio exibe seu status atual. Se um estágio falhou, o painel mostra o erro encontrado e orientações sobre como resolvê-lo. Os resultados persistem se você fechar e reabrir a mesma Campaign ou Canvas.

![Painel de resultados de teste mostrando dois envios de teste bem-sucedidos e um envio de teste com falha.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

#### Novas tentativas e tentativas anteriores {#retries-and-past-attempts}

Se um envio de teste falhar, a Braze tenta automaticamente a entrega novamente por até 24 horas. O painel de resultados reflete isso com duas guias:

- **Mais recente:** A tentativa de entrega mais recente, atualizada em tempo real conforme as novas tentativas ocorrem
- **Tentativas anteriores:** Um histórico das tentativas anteriores, cada uma mostrando os status dos estágios e quaisquer erros encontrados

Quando o resultado final é determinado (entrega bem-sucedida, tentativas esgotadas ou uma falha que novas tentativas não resolverão), as guias são renomeadas respectivamente para **Resultado** e **Histórico de tentativas**.

{% alert note %}
Como as novas tentativas podem continuar por até 24 horas, você pode não ver um resultado final imediatamente após um envio com falha.
{% endalert %}

#### Solução de problemas de falhas {#troubleshoot-failures}

Se um estágio mostrar uma falha, o painel exibe o erro e as próximas etapas sugeridas. Motivos comuns pelos quais um envio de teste pode falhar incluem:

- O modelo de mensagem está pausado ou ainda não foi aprovado no Meta
- O número de telefone do destinatário está com limite de taxa
- As variáveis Liquid na mensagem não foram preenchidas para o usuário teste selecionado

Para problemas persistentes, verifique o status do seu modelo no Meta Business Manager ou confirme que o destinatário do teste possui os atributos de usuário necessários preenchidos na Braze.

### Etapa 5: Crie o restante da sua Campaign ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Em seguida, crie o restante da sua Campaign. Consulte as seções a seguir para mais detalhes sobre como usar nossas ferramentas da melhor forma para criar mensagens de WhatsApp.

#### Escolha um agendamento de entrega ou gatilho {#choose-a-delivery-schedule-or-trigger}

Mensagens de WhatsApp podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para saber mais, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para entrega baseada em ação, você também pode definir a duração da Campaign e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

Nesta etapa, você também pode especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para receber a Campaign, ou habilitar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

#### Escolha os usuários a serem direcionados {#choose-users-to-target}

Em seguida, você deve [direcionar usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo segmentos ou filtros para refinar seu público. Você já deve ter escolhido o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você. Nesta etapa, você seleciona o público maior dos seus segmentos e refina ainda mais esse segmento com nossos filtros. Você recebe automaticamente um resumo de como é a população aproximada desse segmento. Lembre-se de que a composição exata do segmento é sempre calculada antes do envio da mensagem.

{% multi_lang_include audience/target_audiences.md %}

#### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite que você rastreie com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma Campaign. Você pode permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo e pense em como você realmente deseja medir o sucesso desta Campaign.

{% endtab %}

{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar testes multivariantes e seleção inteligente, e mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) da nossa documentação de Canvas.

Como as janelas de conversa só podem durar 24 horas por mensagem recebida, a Braze verificará se não há postergações superiores a 24 horas entre uma mensagem recebida e uma mensagem de resposta.

{% endtab %}
{% endtabs %}

### Etapa 5: Revise e implante {#step-5-review-and-deploy}

Depois de terminar de construir a última parte da sua Campaign ou Canvas, revise os detalhes, teste e envie!

Em seguida, confira os [Relatórios do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting) para saber como acessar os resultados das suas Campaigns de WhatsApp.

## Recursos suportados do WhatsApp {#supported-whatsapp-features}

### Mensagens de saída {#outbound-messages}

Os seguintes recursos são suportados para mensagens de saída do WhatsApp que você envia pela Braze:

| Recurso | Detalhes | Tamanho máximo | Formatos suportados |
| ------- | ------- | ------------- | ---------------------- |
| Texto do cabeçalho | Strings e parâmetros variáveis são suportados. | — | —
| Texto do corpo | Strings e parâmetros variáveis são suportados. | — | — |
| Texto do rodapé | Strings e parâmetros variáveis são suportados. | — | — |
| Links CTA | Vários tipos de chamada para ação (CTA) são suportados. Para mais detalhes, consulte [Tipos de chamada para ação](#ctas). | — | — |
| Imagens | As imagens podem ser incorporadas no texto do corpo. Elas devem ser de 8 bits e usar o modelo de cores RGB ou RGBA. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Documentos | Os documentos podem ser incorporados no texto do corpo. Os arquivos devem ser hospedados via URL. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Vídeos | Os vídeos podem ser incorporados no texto do corpo. Os arquivos devem ser hospedados via URL ou na [biblioteca de mídia da Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). | < 16 MB | `.3gp`, `.mp4` |
| Áudio | O áudio é suportado apenas por meio de mensagens de resposta. Os arquivos devem ser hospedados via URL. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensagens de saída" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Mensagens de entrada {#inbound-messages}

Os seguintes recursos são suportados para mensagens de entrada do WhatsApp que você recebe pela Braze:

| Recurso | Detalhes | Formatos suportados |
| ------- | ------- | ------------------ |
| Texto do corpo | Apenas strings padrão são suportadas. | — |
| Imagens | As imagens devem ser de 8 bits e usar o modelo de cores RGB ou RGBA. Os arquivos devem ter menos de 5 MB. | `.jpg`, `.png` |
| Áudio | Apenas arquivos Ogg codificados com o codec Opus são suportados. Outros formatos Ogg não são suportados. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documentos | Os documentos são suportados por meio de anexo de mensagem. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Vídeo | Apenas o codec de vídeo H.264 e o codec de áudio AAC são suportados. Os vídeos devem ter uma única faixa de áudio ou nenhuma faixa de áudio. | `.mp4`, `.3gp` |
| Links CTA | Vários tipos de chamada para ação (CTA) são suportados. Para mais detalhes, consulte [Tipos de chamada para ação](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensagens de entrada" }

### Tipos de chamada para ação {#ctas}

Os seguintes tipos de chamada para ação são suportados para mensagens de WhatsApp que você envia pela Braze:

| Tipo de CTA | Detalhes |
| ----------- | ---------------- |
| Visitar site | Máximo de um botão (incluindo parâmetros variáveis). |
| Ligar para número de telefone | Disponível apenas para modelos de mensagem. <br>Máximo de um botão. |
| Botões de resposta rápida personalizados | Máximo de três botões. |
| Botão de descadastramento de marketing | Por padrão, os status de inscrição não são atualizados automaticamente. Para um passo a passo completo, consulte [Opt-ins e descadastramentos]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection). |
| Modelos de mensagem com código de cupom | Disponível apenas para modelos de mensagem. <br>Eles podem ser abertos e editados como outros modelos de mensagem e são compatíveis com Liquid e códigos de promoção da Braze. |
| Mensagens de resposta com CTA | Crie uma mensagem de resposta que inclua um botão de chamada para ação. |
| [Mensagens de resposta com lista]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | Crie uma mensagem de resposta que inclua uma lista de até 10 opções para os usuários escolherem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de chamada para ação" }