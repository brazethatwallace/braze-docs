---
nav_title: Enviar mensagens de teste
article_title: Enviar mensagens de teste
page_order: 11.5
tool:
  - Campaigns
  - Canvas
page_type: reference
description: "Este artigo de referência aborda como enviar mensagens de teste nos diferentes canais da Braze e como incorporar propriedades de eventos personalizados ou atributos de usuários."
---

# Enviar mensagens de teste {#send-test-messages}

> Antes de enviar uma campanha de mensagens para seus usuários, como prática recomendada, sugerimos testar para garantir que tudo esteja correto e funcione conforme o esperado. Você pode criar e enviar mensagens de teste para dispositivos selecionados ou membros da equipe usando as ferramentas do dashboard da Braze.

{% alert important %}
Salve o rascunho da sua campanha após o teste para evitar a exclusão da campanha. Você pode enviar mensagens de teste sem salvar a mensagem como rascunho.
{% endalert %}

## Etapa 1: Identifique seus usuários de teste {#step-1-identify-your-test-users}

Antes de testar sua campanha de mensagens, é importante identificar seus usuários de teste. Esses usuários podem ser IDs de usuário ou endereços de e-mail existentes, ou novos usuários usados exclusivamente para testar campanhas de mensagens.

### Opcional: Crie um grupo de teste de conteúdo {#optional-create-a-content-test-group}

Uma maneira conveniente de organizar seus usuários de teste é criando um [grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), que inclui um grupo de usuários que receberão mensagens de teste de campanhas. Você pode adicionar esse grupo de teste ao campo **Add Content Test Groups** em **Test Recipients** na sua campanha e iniciar seus testes sem criar ou adicionar usuários de teste individuais.

## Etapa 2: Envie mensagens de teste específicas por canal {#step-2-send-channel-specific-test-messages}

Para ver as etapas de envio de mensagens de teste, consulte a seção a seguir para o respectivo canal.

{% tabs local %}
{% tab Banner %}

{% alert important %}
Antes de testar mensagens de Banner na Braze, você precisará criar uma campanha de Banner na Braze. Além disso, verifique se o posicionamento que deseja testar já está [inserido no seu app ou site]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Após criar sua mensagem de Banner, você pode pré-visualizar o Banner ou enviar uma mensagem de teste.

1. Rascunhe sua mensagem de Banner.
2. Selecione **Preview** para pré-visualizar seu Banner ou enviar uma mensagem de teste.
3. Para enviar uma mensagem de teste, adicione um grupo de teste de conteúdo ou um ou mais usuários individuais como **Test Recipients** e selecione **Send Test**.

Você poderá visualizar sua mensagem de teste no dispositivo por até 5 minutos.

![Guia de pré-visualização do criador de Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Lembre-se de que sua pré-visualização pode não ser idêntica à renderização final no dispositivo do usuário devido a diferenças de hardware.
{% endalert %}

### Lista de verificação do teste {#test-checklist}

- Sua campanha de Banner está atribuída a um posicionamento?
- As imagens e mídias aparecem e funcionam conforme o esperado nos tipos de dispositivos e tamanhos de tela direcionados?
- Seus links e botões direcionam o usuário para onde deveriam?
- O Liquid funciona conforme o esperado? Você considerou um valor de atributo padrão caso o Liquid não retorne nenhuma informação?
- Seu texto está claro, conciso e correto?

{% endtab %}
{% tab Content Card %}

{% alert important %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuários individuais, o push deve estar ativado nos seus dispositivos de teste com tokens de push válidos registrados para o usuário de teste antes do envio. Para usuários iOS, é necessário tocar na notificação por push enviada pela Braze para visualizar o Content Card de teste. Esse comportamento se aplica apenas a Content Cards de teste.
{% endalert %}

Content Cards de teste são entregues por meio de uma notificação por push. O cartão é empacotado na carga útil do push, e o SDK o extrai e armazena em cache localmente quando o push é recebido.

Esse processo ignora o sistema normal de entrega de cartões, por isso o push deve estar ativado mesmo que você esteja testando um Content Card.

Content Cards de teste expiram aproximadamente cinco minutos após o envio.

Após criar seu Content Card, você pode enviar um Content Card de teste para o seu app e ver como ele ficará em tempo real.

1. Rascunhe seu Content Card.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou usuário individual para receber esta mensagem de teste.
3. Selecione **Send Test** para enviar seu Content Card para o app.

![Testar Content Card]({% image_buster /assets/img/contentcard_test.png %})

### Pré-visualização {#preview}

Você pode pré-visualizar seu cartão enquanto o compõe na guia **Preview**. Isso deve ajudar a visualizar como sua mensagem final ficará da perspectiva do usuário.

{% alert note %}
Na guia **Preview** do criador, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Recomendamos sempre enviar uma mensagem de teste para um dispositivo para garantir que suas mídias, textos, personalização e atributos personalizados sejam gerados corretamente.
{% endalert %}

### Lista de verificação do teste

- Seu usuário de teste está inscrito para push com um token de push válido?
- As imagens e mídias aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atributo padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) caso o Liquid não retorne nenhuma informação?
- Seu texto está claro, conciso e correto?
- Seus links direcionam o usuário para onde deveriam?
- Seu usuário de teste está inscrito para push com um token de push válido?

### Solução de problemas com imagens quebradas {#troubleshooting-broken-images}

Se a imagem de um Content Card não está sendo renderizada ou aparece quebrada:

- **Verifique se a URL está correta e codificada:** Caracteres especiais na URL (como espaços ou parâmetros de consulta) devem ser codificados corretamente. Caso contrário, a solicitação da imagem falhará.
- **Verifique as políticas de segurança de conteúdo:** Se sua organização possui uma política de segurança de conteúdo (CSP) ou regras internas de segurança de TI, a política pode bloquear o domínio da imagem. Confirme que o domínio da URL da imagem é permitido pela sua CSP.
- **Use HTTPS:** As URLs de imagem devem usar `https://` em vez de `http://` para evitar bloqueio de conteúdo misto em navegadores e apps.
- **Abra a URL diretamente em um navegador:** Se a imagem não carrega em um navegador, o problema está na URL da imagem ou na hospedagem — não na Braze.

### Depuração {#debug}

Após o envio dos seus Content Cards, você pode detalhar ou depurar quaisquer problemas a partir do [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) no Console de desenvolvedor.

Um caso de uso comum é tentar depurar por que um usuário não consegue ver um Content Card específico. Para isso, você pode verificar nos **Registros de usuários de eventos** os Content Cards entregues ao SDK no início da sessão, mas antes de uma impressão, e rastreá-los até uma campanha específica:

1. Acesse **Settings** > **Event User Log**.
2. Localize e expanda a solicitação do SDK para seu usuário de teste.
3. Clique em **Raw Data**.
4. Encontre o `id` da sua sessão. Veja um exemplo de trecho a seguir:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

{: start="5"}
5. Use uma ferramenta de decodificação como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar o `id` do formato Base64 e encontrar o `campaign_id` associado. No nosso exemplo, o resultado é o seguinte:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Onde `4861692e-6fce-4215-bd05-3254fb9e9057` é o `campaign_id`.<br><br>

6. Acesse a página **Campaigns** e pesquise pelo `campaign_id`.

![Pesquisar campaign_id na página Campaigns]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

A partir daí, você pode revisar as configurações e o conteúdo da mensagem para investigar e determinar por que um usuário não consegue ver um Content Card específico.

{% endtab %}
{% tab E-mail %}

1. Rascunhe sua mensagem de e-mail.
2. Selecione **Preview and Test**.
3. Selecione a guia **Test Send** e adicione seu endereço de e-mail ou ID de usuário no campo **Add individual users**.
4. Selecione **Send Test** para enviar o e-mail rascunhado para sua caixa de entrada.

![Testar e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Se sua campanha de e-mail contém uma imagem grande e não está sendo exibida conforme o esperado no Outlook, considere reduzir as dimensões reais do arquivo da imagem com uma ferramenta de edição ou redimensionamento de imagem, em vez de apenas redimensioná-la com CSS ou HTML.

{% endtab %}
{% tab Mensagem no app %}

{% alert warning %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuários individuais, o push deve estar ativado nos seus dispositivos de teste antes do envio. Por exemplo, você deve ter o push ativado no seu dispositivo iOS para tocar na notificação antes que a mensagem de teste seja exibida. {% endalert %}

Se você tem notificações por push configuradas no seu app e no seu dispositivo de teste, pode enviar mensagens de teste no app para ver como ficam em tempo real.

1. Rascunhe sua mensagem no app.
2. Selecione a guia **Test** e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users**.
3. Selecione **Send Test** para enviar sua mensagem push para o dispositivo.

Uma mensagem push de teste aparecerá no topo da tela do seu dispositivo.

![Testar mensagem no app]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Envios de teste podem resultar em mais de uma mensagem no app sendo enviada para cada destinatário.
{% endalert %}

Ao clicar diretamente e abrir a mensagem push, você será direcionado ao seu app, onde poderá visualizar o teste da mensagem no app. Observe que esse recurso de teste de mensagem no app depende de o usuário clicar em uma notificação por push de teste para acionar a mensagem no app. Portanto, o usuário deve ser elegível para receber notificações por push no app relevante para a entrega bem-sucedida da notificação por push de teste.

### Pré-visualização

Você pode pré-visualizar sua mensagem no app enquanto a compõe na guia **Preview**. Isso deve ajudar a visualizar como sua mensagem final ficará da perspectiva do usuário. Você pode pré-visualizar como sua mensagem ficará para um usuário aleatório, um usuário específico ou um usuário personalizado. Também é possível pré-visualizar mensagens para dispositivos móveis ou tablets.

![Guia de composição ao criar uma mensagem no app mostrando a pré-visualização de como a mensagem ficará. Nenhum usuário está selecionado, então o Liquid adicionado na seção do corpo é exibido como está.]({% image_buster /assets/img/in-app-message-preview.png %})

A Braze tem três gerações de mensagens no app disponíveis. Você pode ajustar para quais dispositivos suas mensagens devem ser enviadas, com base na geração que eles suportam.

![Alternando entre gerações ao pré-visualizar uma mensagem no app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
Na **Preview**, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Recomendamos sempre enviar uma mensagem de teste para um dispositivo para garantir que suas mídias, textos, personalização e atributos personalizados sejam gerados corretamente.
{% endalert %}

### Lista de verificação do teste

- As imagens e mídias aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atributo padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) caso o Liquid não retorne nenhuma informação?
- Seu texto está claro, conciso e correto?
- Seus botões direcionam o usuário para onde deveriam?

### Scanner de acessibilidade {#accessibility-scanner}

Para apoiar as melhores práticas de acessibilidade, a Braze verifica automaticamente o conteúdo de mensagens no app criadas usando o editor HTML tradicional em relação aos padrões de acessibilidade. Esse scanner ajuda a identificar conteúdo que pode não atender aos padrões das Diretrizes de Acessibilidade para Conteúdo Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). WCAG é um conjunto de padrões técnicos reconhecidos internacionalmente, desenvolvidos pelo World Wide Web Consortium (W3C) para tornar o conteúdo web mais acessível a pessoas com deficiência.

![Resultados do scanner de acessibilidade]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
O scanner de acessibilidade de mensagens no app funciona apenas em mensagens criadas com HTML personalizado.
{% endalert %}

#### Como funciona {#how-it-works}

O scanner é executado automaticamente em mensagens HTML personalizadas e avalia toda a sua mensagem HTML em relação ao [conjunto completo de regras WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema identificado, ele mostra:

- O elemento HTML específico envolvido
- Uma descrição do problema de acessibilidade
- Um link para contexto adicional ou orientação de correção

#### Entendendo testes automatizados de acessibilidade {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Crie sua mensagem LINE.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou usuário individual para receber esta mensagem de teste.
3. Selecione **Send Test** para enviar sua mensagem.

![Testar mensagem LINE.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Push para celular {#mobile-push}

1. Rascunhe seu push para celular.
2. Selecione a guia **Test** e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users**.
3. Selecione **Send Test** para enviar a mensagem rascunhada para o seu dispositivo.

![Testar push]({% image_buster /assets/img_archive/testpush.png %})

Se você vir um erro informando que nenhum dos usuários selecionados possui tokens de push correspondentes, o usuário de teste não possui um token de push válido para a plataforma selecionada. O usuário deve ter iniciado uma sessão no app e ativado o push para esse dispositivo. Para saber mais, consulte [Ativação de push e estados de inscrição de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

#### Push para a web {#web-push}

1. Crie seu push para a web.
2. Selecione a guia **Test**.
3. Selecione **Send Test to Myself**.
4. Selecione **Send Test** para enviar seu push para a web ao seu navegador.

![Testar push para a web]({% image_buster /assets/img_archive/testwebpush.png %})

Se você já aceitou mensagens push do dashboard da Braze, a mensagem aparecerá no canto da sua tela. Caso contrário, selecione **Allow** quando solicitado, e a mensagem será exibida.

Se você vir um erro informando que nenhum dos usuários selecionados possui tokens de push correspondentes para push para a web, verifique se o usuário de teste possui um token de push válido registrado para a plataforma selecionada. Para receber um token de push, o usuário deve estar configurado para receber notificações por push do app no seu dispositivo. Para mais detalhes, consulte [Ativação de push e estados de inscrição de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

{% endtab %}
{% tab SMS/MMS e RCS %}

Após criar sua mensagem SMS, MMS ou RCS, você pode enviar uma mensagem de teste para o seu telefone e ver como ficará em tempo real.

1. Rascunhe sua mensagem SMS, MMS ou RCS.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou usuário individual para receber esta mensagem de teste.
3. Selecione **Send Test** para enviar sua mensagem de teste.

![Testar mensagem SMS]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Após criar seu webhook, você pode fazer um envio de teste para verificar a resposta do webhook. Selecione a guia **Test** e selecione **Send Test** para enviar um teste para a URL do webhook fornecida. Você também pode selecionar um usuário individual para pré-visualizar a resposta como um usuário específico.

{% endtab %}
{% tab WhatsApp %}

1. Crie sua mensagem WhatsApp.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou usuário individual para receber esta mensagem de teste.
3. Inicie uma janela de conversa enviando uma mensagem WhatsApp para o número de telefone associado ao grupo de inscrições que você está usando para esta mensagem. O número de telefone associado está listado no alerta na guia **Test**.
4. Selecione **Send Test** para enviar sua mensagem.

![Testar mensagem WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Testar campanhas personalizadas {#test-personalized-campaigns}

Se você está testando campanhas que preenchem dados de usuários ou usam propriedades de eventos personalizados, será necessário seguir etapas adicionais ou diferentes.

### Testando campanhas personalizadas com atributos de usuário {#testing-campaigns-personalized-with-user-attributes}

Se você está usando [personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/overview) na sua mensagem, precisará seguir etapas adicionais para pré-visualizar corretamente sua campanha e verificar se os dados do usuário estão preenchendo o conteúdo adequadamente.

Ao enviar uma mensagem de teste, certifique-se de escolher a opção **Select Existing User** ou pré-visualizar como um **Custom User**.

![Testando uma mensagem personalizada]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Selecionando um usuário existente {#selecting-an-existing-user}

Se estiver selecionando um usuário existente, insira o ID de usuário ou e-mail específico no campo de pesquisa. Em seguida, use a pré-visualização do dashboard para ver como sua mensagem apareceria para esse usuário e envie uma mensagem de teste para o seu dispositivo que reflita o que esse usuário veria.

![Selecionar um usuário]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Selecionando um usuário personalizado {#selecting-a-custom-user}

Se estiver pré-visualizando como um usuário personalizado, insira texto para os vários campos disponíveis para personalização, como o nome do usuário e quaisquer atributos personalizados. Novamente, você pode inserir seu próprio endereço de e-mail para enviar um teste para o seu dispositivo.

![Usuário personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personalizando um usuário existente {#customizing-an-existing-user}

Você pode editar campos individuais de um usuário aleatório ou existente para ajudar a testar conteúdo dinâmico na sua mensagem. Selecione **Edit** para converter o usuário selecionado em um usuário personalizado que você pode modificar.

![A guia "Preview as a User" com um botão "Edit".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Testando campanhas personalizadas com propriedades de eventos personalizados {#testing-campaigns-personalized-with-custom-event-properties}

Testar campanhas personalizadas com [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) difere um pouco do teste de outros tipos de campanhas descritos.

{% tabs local %}
{% tab Disparar manualmente %}

#### Método 1: Disparando a campanha manualmente {#method-1-triggering-campaign-manually}

Você pode disparar a campanha manualmente como uma forma robusta de testar campanhas personalizadas usando propriedades de eventos personalizados:

1. Escreva o texto envolvendo a propriedade do evento.

![Compondo mensagem de teste com propriedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Use a [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para entregar a campanha quando o evento ocorrer.

{% alert note %}
Se você está testando uma campanha de push para iOS, deve definir um delay de um minuto para ter tempo de sair do app, pois o iOS não entrega notificações por push para o app atualmente aberto. Outros tipos de campanhas podem ser configurados para entrega imediata.
{% endalert %}

![Entrega da mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Direcione os usuários como faria para testes, usando um filtro de teste ou direcionando seu próprio endereço de e-mail, e finalize a criação da campanha.

![Direcionamento da mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Acesse seu app e conclua o evento personalizado.

A campanha será disparada e mostrará a mensagem personalizada com a propriedade do evento.

![Exemplo de mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Mensagem de teste %}

#### Método 2: Enviando uma mensagem de teste para si mesmo {#method-2-sending-yourself-a-test-message}

Alternativamente, se você está salvando IDs de usuário personalizados, também pode testar a campanha enviando uma mensagem de teste personalizada para si mesmo.

1. Escreva o texto da sua campanha.
2. Selecione a guia **Test** e escolha **Customized User**.
3. Adicione a propriedade do evento personalizado na parte inferior da página e adicione seu ID de usuário ou endereço de e-mail na caixa superior.
4. Selecione **Send Test** para receber uma mensagem personalizada com a propriedade.

![Testando usando usuário personalizado]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Usando Liquid {#method-3-using-liquid}

Você pode testar propriedades de eventos personalizados inserindo valores manualmente com Liquid.

1. No editor de mensagens, insira valores para suas propriedades de eventos personalizados.
2. Selecione a guia **Preview as a User** para verificar se a mensagem correta é exibida.

{% endtab %}
{% endtabs %}

## Limitações {#limitations}

Existem algumas situações em que as mensagens de teste não se comportam da mesma forma que Campaigns ou Canvas enviados para usuários reais. Nesses casos, considere lançar a Campaign ou o Canvas para um conjunto limitado de usuários de teste para validar esse comportamento.

- Visualizar a Central de Preferências da Braze a partir de mensagens de teste fará com que o botão **Save Preferences** fique esmaecido.
- Para testar mensagens no app e Content Cards, o usuário alvo deve ter um token de push para o dispositivo alvo.
- Para testar links de cancelamento de inscrição em e-mails, certifique-se de que o endereço de e-mail do seu usuário de teste esteja no respectivo espaço de trabalho.
- O cabeçalho `List-Unsubscribe` não é incluído em e-mails enviados pela funcionalidade de mensagem de teste.
- E-mails enviados para usuários do grupo de teste não atualizam a lista de Campaigns recebidas no perfil do usuário nem incrementam os envios na análise de dados do dashboard.

## Solução de problemas {#troubleshooting}

### Mensagens no app {#in-app-messages}

Se sua campanha de mensagem no app não está sendo disparada por uma campanha de push, verifique a segmentação da campanha no app para confirmar que o usuário atende ao público-alvo **antes** de receber a mensagem push.

Para envios de teste no Android e iOS, as mensagens no app que usam o comportamento ao clicar **Request push permission** podem não ser exibidas em alguns dispositivos. Como solução alternativa:
- **Android:** Os dispositivos devem estar no Android 13 e na versão 21.0.0 do nosso SDK Android. Outro motivo pode ser que o dispositivo no qual a mensagem no app é exibida já possui um prompt no nível do sistema. Você pode ter selecionado **Do not ask again**, então pode ser necessário reinstalar o app para redefinir as permissões de notificação antes de testar novamente.
- **iOS:** Recomendamos que sua equipe de desenvolvimento revise a implementação de notificações por push do seu app e remova manualmente qualquer código que solicite permissões de push. Para saber mais, consulte [Mensagens no app de introdução ao push]({{site.baseurl}}/user_guide/channels/push/best_practices).

Para que uma campanha de mensagem no app baseada em ação seja entregue, você deve registrar eventos personalizados por meio do SDK da Braze, não por REST APIs, para que os usuários recebam mensagens no app elegíveis diretamente em seus dispositivos. Os usuários recebem a mensagem no app se realizarem o evento durante a sessão.