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

## Etapa 1: Identifique seus usuários teste {#step-1-identify-your-test-users}

Antes de testar sua campanha de mensagens, é importante identificar seus usuários teste. Esses usuários podem ser IDs de usuário ou endereços de e-mail já existentes, ou novos usuários que são usados exclusivamente para testar campanhas de mensagens.

### Opcional: Crie um grupo de teste de conteúdo {#optional-create-a-content-test-group}

Uma maneira prática de organizar seus usuários teste é criando um [grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), que inclui um grupo de usuários que receberão mensagens de teste das campanhas. Você pode adicionar esse grupo de teste ao campo **Add Content Test Groups** em **Test Recipients** na sua campanha e iniciar seus testes sem precisar criar ou adicionar usuários teste individuais.

## Etapa 2: Envie mensagens de teste específicas por canal {#step-2-send-channel-specific-test-messages}

Para ver as etapas de envio de mensagens de teste, consulte a seção a seguir para o canal correspondente.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Antes de testar mensagens de Banner na Braze, você precisa criar uma campanha de Banner na Braze. Além disso, verifique se o posicionamento que deseja testar já está [inserido no seu app ou website]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Depois de criar sua mensagem de Banner, você pode visualizar o Banner ou enviar uma mensagem de teste.

1. Elabore sua mensagem de Banner.
2. Selecione **prévia** para visualizar seu Banner ou enviar uma mensagem de teste.
3. Para enviar uma mensagem de teste, adicione um grupo de teste de conteúdo ou um ou mais usuários individuais como **Test Recipients** e selecione **Send Test**.

Você poderá visualizar sua mensagem de teste no dispositivo por até 5 minutos.

![Guia de prévia do criador de Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Lembre-se de que sua prévia pode não ser idêntica à renderização final no dispositivo do usuário devido a diferenças de hardware.
{% endalert %}

### Checklist de teste {#test-checklist}

- Sua campanha de Banner está atribuída a um posicionamento?
- As imagens e mídias aparecem e funcionam conforme o esperado nos tipos de dispositivos e tamanhos de tela direcionados?
- Seus links e botões direcionam o usuário para onde deveriam?
- O Liquid funciona conforme o esperado? Você definiu um valor de atributo padrão para o caso de o Liquid não retornar nenhuma informação?
- Seu texto está claro, conciso e correto?

{% endtab %}
{% tab Content Card %}

{% alert important %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuários individuais, o push deve estar ativado nos seus dispositivos de teste com tokens por push válidos registrados para o usuário teste antes do envio. Para usuários iOS, é necessário tocar na notificação por push enviada pela Braze para visualizar o Content Card de teste. Esse comportamento se aplica apenas a Content Cards de teste.
{% endalert %}

Content Cards de teste são entregues por meio de uma notificação por push. O cartão é empacotado na carga útil do push, e o SDK or kit de desenvolvimento de software o extrai e armazena em cache localmente quando o push é recebido.

Esse processo ignora o sistema normal de entrega de cartões, por isso o push deve estar ativado mesmo que você esteja testando um Content Card.

Content Cards de teste expiram aproximadamente cinco minutos após o envio.

Depois de criar seu Content Card, você pode enviar um Content Card de teste para o seu app e ver como ele ficará em tempo real.

1. Elabore seu Content Card.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou um usuário individual para receber essa mensagem de teste.
3. Selecione **Send Test** para enviar seu Content Card ao seu app.

![Teste de Content Card]({% image_buster /assets/img/contentcard_test.png %})

### Prévia {#preview}

Você pode visualizar seu cartão enquanto o compõe na guia **prévia**. Isso deve ajudar a entender como sua mensagem final ficará na perspectiva do usuário.

{% alert note %}
Na guia **prévia** do seu criador, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Recomendamos sempre enviar uma mensagem de teste para um dispositivo para garantir que suas mídias, textos, personalização e atributos personalizados sejam gerados corretamente.
{% endalert %}

### Checklist de teste

- O usuário teste está habilitado para push com um token por push válido?
- As imagens e mídias aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você definiu um [valor de atributo padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) para o caso de o Liquid não retornar nenhuma informação?
- Seu texto está claro, conciso e correto?
- Seus links direcionam o usuário para onde deveriam?
- O usuário teste está habilitado para push com um token por push válido?

### Solução de problemas para imagens com falha na renderização {#troubleshooting-broken-images}

Se uma imagem de Content Card não está sendo renderizada ou aparece com falha:

- **Verifique se o URL está correto e codificado:** Caracteres especiais no URL (como espaços ou parâmetros de consulta) devem ser codificados corretamente. Caso contrário, a solicitação de imagem falhará.
- **Verifique as políticas de segurança de conteúdo:** Se sua organização possui uma política de segurança de conteúdo (CSP) ou regras internas de segurança de TI, a política pode bloquear o domínio da imagem. Confirme que o domínio do URL da imagem é permitido pela sua CSP.
- **Use HTTPS:** Os URLs das imagens devem usar `https://` em vez de `http://` para evitar bloqueio de conteúdo misto em navegadores e apps.
- **Abra o URL diretamente em um navegador:** Se a imagem não carregar em um navegador, o problema está no URL da imagem ou na hospedagem, não na Braze.

### Depuração {#debug}

Depois que seus Content Cards forem enviados, você pode detalhar ou depurar quaisquer problemas a partir do [registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) no console de desenvolvedor.

Um caso de uso comum é tentar depurar por que um usuário não consegue ver um Content Card específico. Para isso, você pode consultar os **Event User Logs** para os Content Cards entregues ao SDK or kit de desenvolvimento de software no início da sessão, mas antes de uma impressão, e rastrear esses dados até uma campanha específica:

1. Acesse **Settings** > **Event User Log**.
2. Localize e expanda a solicitação do SDK or kit de desenvolvimento de software para o seu usuário teste.
3. Clique em **Raw Data**.
4. Encontre o `id` da sua sessão. A seguir, um trecho de exemplo:

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
5. Use uma ferramenta de decodificação como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar o `id` do formato Base64 e encontrar o `campaign_id` associado. Em nosso exemplo, isso resulta no seguinte:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Onde `4861692e-6fce-4215-bd05-3254fb9e9057` é o `campaign_id`.<br><br>

6. Acesse a página **Campaigns** e pesquise pelo `campaign_id`.

![Pesquisar por campaign_id na página Campaigns]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

A partir daí, você pode revisar as configurações e o conteúdo da mensagem para investigar e determinar por que um usuário não consegue ver um Content Card específico.

{% endtab %}
{% tab Email %}

1. Elabore sua mensagem de e-mail.
2. Selecione **prévia and Test**.
3. Selecione a guia **Test Send** e adicione seu endereço de e-mail ou ID de usuário no campo **Add individual users**.
4. Selecione **Send Test** para enviar seu e-mail elaborado para sua caixa de entrada.

![Teste de e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Se o seu e-mail inclui um link de [Central de Preferências]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center), os envios de teste não geram um link funcional nem permitem salvar preferências. Para testar a Central de Preferências, envie a mensagem para um usuário teste ou um pequeno Segment or segmento or segmento interno. Para mais detalhes, consulte [Testando centrais de preferências]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).

Se sua campanha de e-mail contém uma imagem grande e não está sendo exibida como esperado no Outlook, considere reduzir as dimensões reais do arquivo da imagem com uma ferramenta de edição ou redimensionamento de imagem, em vez de apenas redimensioná-la com CSS ou HTML.

{% endtab %}
{% tab In-app message %}

{% alert warning %}
Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuários individuais, o push deve estar ativado nos seus dispositivos de teste antes do envio. Por exemplo, você deve ter o push ativado no seu dispositivo iOS para tocar na notificação antes que a mensagem de teste seja exibida. {% endalert %}

Se você tem notificações por push configuradas no seu app e no seu dispositivo de teste, é possível enviar mensagens no app de teste ao seu app para ver como ficam em tempo real.

1. Elabore sua mensagem no app.
2. Selecione a guia **Test** e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users**.
3. Selecione **Send Test** para enviar sua mensagem push ao seu dispositivo.

Uma mensagem push de teste aparecerá na parte superior da tela do seu dispositivo.

![Teste de mensagem no app]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Envios de teste podem resultar em mais de uma mensagem no app sendo enviada para cada destinatário.
{% endalert %}

Clicar diretamente e abrir a mensagem push levará você ao seu app, onde poderá visualizar o teste da mensagem no app. Observe que esse recurso de teste de mensagem no app depende de o usuário clicar em uma notificação por push de teste para disparar a mensagem no app. Sendo assim, o usuário deve ser elegível para receber notificações por push no app correspondente para a entrega bem-sucedida da notificação por push de teste.

### Prévia

Você pode visualizar sua mensagem no app enquanto a compõe na guia **prévia**. Isso deve ajudar a entender como sua mensagem final ficará na perspectiva do usuário. Você pode visualizar como sua mensagem ficará para um usuário aleatório, um usuário específico ou um usuário personalizado. Também é possível visualizar mensagens para dispositivos móveis ou tablets.

![Guia de composição ao criar uma mensagem no app mostrando a prévia de como a mensagem ficará. Nenhum usuário está selecionado, então o Liquid adicionado na seção do corpo é exibido como está.]({% image_buster /assets/img/in-app-message-preview.png %})

A Braze tem três gerações de mensagens no app disponíveis. Você pode ajustar para quais dispositivos suas mensagens devem ser enviadas, com base na geração que eles suportam.

![Alternando entre gerações ao visualizar uma mensagem no app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
Em **prévia**, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Recomendamos sempre enviar uma mensagem de teste para um dispositivo para garantir que suas mídias, textos, personalização e atributos personalizados sejam gerados corretamente.
{% endalert %}

### Checklist de teste

- As imagens e mídias aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você definiu um [valor de atributo padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) para o caso de o Liquid não retornar nenhuma informação?
- Seu texto está claro, conciso e correto?
- Seus botões direcionam o usuário para onde deveriam?

### Scanner de acessibilidade {#accessibility-scanner}

Para apoiar as melhores práticas de acessibilidade, a Braze verifica automaticamente o conteúdo de mensagens no app criadas usando o editor HTML tradicional em relação aos padrões de acessibilidade. Esse scanner ajuda a identificar conteúdo que pode não atender aos padrões das Diretrizes de Acessibilidade para Conteúdo Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). O WCAG é um conjunto de padrões técnicos reconhecidos internacionalmente, desenvolvidos pelo World Wide Web Consortium (W3C) para tornar o conteúdo web mais acessível a pessoas com deficiência.

![Resultados do scanner de acessibilidade]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
O scanner de acessibilidade de mensagens no app funciona apenas em mensagens criadas com HTML personalizado.
{% endalert %}

#### Como funciona {#how-it-works}

O scanner é executado automaticamente em mensagens HTML personalizadas e avalia toda a sua mensagem HTML em relação ao conjunto completo de regras [WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema identificado, ele exibe:

- O elemento HTML específico envolvido
- Uma descrição do problema de acessibilidade
- Um link para contexto adicional ou orientações de correção

#### Entendendo testes automatizados de acessibilidade {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Crie sua mensagem LINE.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou um usuário individual para receber essa mensagem de teste.
3. Selecione **Send Test** para enviar sua mensagem.

![Mensagem LINE de teste.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Push móvel {#mobile-push}

1. Elabore seu push móvel.
2. Selecione a guia **Test** e adicione seu endereço de e-mail ou ID de usuário no campo **Add Individual Users**.
3. Selecione **Send Test** para enviar sua mensagem elaborada ao seu dispositivo.

![Teste de push]({% image_buster /assets/img_archive/testpush.png %})

Se você vir um erro informando que nenhum dos usuários selecionados possui tokens por push correspondentes, o usuário teste não tem um token por push válido para a plataforma selecionada. O usuário deve ter iniciado uma sessão no app e ativado o push para aquele dispositivo. Para saber mais, consulte [Ativação de push e inscrição de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

#### Web push {#web-push}

1. Crie seu web push.
2. Selecione a guia **Test**.
3. Selecione **Send Test to Myself**.
4. Selecione **Send Test** para enviar seu web push ao seu navegador de internet or navegador web.

![Teste de web push]({% image_buster /assets/img_archive/testwebpush.png %})

Se você já aceitou mensagens push do dashboard da Braze, a mensagem será exibida no canto da sua tela. Caso contrário, selecione **Allow** quando solicitado, e a mensagem será exibida.

Se você vir um erro informando que nenhum dos usuários selecionados possui tokens por push correspondentes para Web Push, verifique se o usuário teste possui um token por push válido registrado para a plataforma selecionada. Para receber um token por push, o usuário deve estar configurado para receber notificações por push para o app em seu dispositivo. Para mais detalhes, consulte [Ativação de push e inscrição de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

{% endtab %}
{% tab SMS/MMS and RCS %}

Depois de criar sua mensagem SMS, MMS ou RCS, você pode enviar uma mensagem de teste para o seu telefone para ver como ela ficará em tempo real. O destinatário deve pertencer ao grupo de inscrições de SMS que você selecionar ao enviar o teste, ter um número de telefone válido e ter pelo menos um país selecionado em **Geographic Permissions**. Para mais detalhes, consulte [Perguntas frequentes sobre SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

1. Elabore sua mensagem SMS, MMS ou RCS.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou um usuário individual para receber essa mensagem de teste.
3. Selecione **Send Test** para enviar sua mensagem de teste.

![Teste de Content Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Depois de criar seu webhook, você pode fazer um envio de teste para verificar a resposta do webhook. Selecione a guia **Test** e selecione **Send Test** para enviar um teste ao URL do webhook informado. Você também pode selecionar um usuário individual para visualizar a resposta como um usuário específico.

{% endtab %}
{% tab WhatsApp %}

1. Crie sua mensagem WhatsApp.
2. Selecione a guia **Test** e selecione pelo menos um grupo de teste de conteúdo ou um usuário individual para receber essa mensagem de teste.
3. Inicie uma janela de conversa enviando uma mensagem WhatsApp para o número de telefone associado ao grupo de inscrições que você está usando para essa mensagem. O número de telefone associado é listado no alerta na guia **Test**.
4. Selecione **Send Test** para enviar sua mensagem.

![Mensagem WhatsApp de teste.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Testar campaigns personalizadas {#test-personalized-campaigns}

Se você estiver testando campaigns que preenchem dados de usuários ou usam propriedades de eventos personalizados, será necessário seguir etapas adicionais ou diferentes.

### Testando campaigns personalizadas com atributos de usuário {#testing-campaigns-personalized-with-user-attributes}

Se você estiver usando [personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) na sua mensagem, será necessário seguir etapas adicionais para visualizar corretamente sua campaign e verificar se os dados do usuário estão preenchendo o conteúdo adequadamente.

Ao enviar uma mensagem de teste, certifique-se de escolher a opção **Select Existing User** ou visualizar como **Custom User**.

![Testando uma mensagem personalizada]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Selecionando um usuário existente {#selecting-an-existing-user}

Se estiver selecionando um usuário existente, insira o ID de usuário específico ou o e-mail no campo de busca. Em seguida, use a prévia do dashboard para ver como sua mensagem apareceria para esse usuário e envie uma mensagem de teste para o seu dispositivo que reflita o que esse usuário veria.

![Selecionar um usuário]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Selecionando um usuário personalizado {#selecting-a-custom-user}

Se estiver visualizando como um usuário personalizado, insira texto nos diversos campos disponíveis para personalização, como o nome do usuário e quaisquer atributos personalizados. Novamente, você pode inserir seu próprio endereço de e-mail para enviar um teste para o seu dispositivo.

![Usuário personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personalizando um usuário existente {#customizing-an-existing-user}

Você pode editar campos individuais de um usuário aleatório ou existente para ajudar a testar o conteúdo dinâmico dentro da sua mensagem. Selecione **Edit** para converter o usuário selecionado em um usuário personalizado que você pode modificar.

![A guia "prévia as a User" com um botão "Edit".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Testando campaigns personalizadas com propriedades de eventos personalizados {#testing-campaigns-personalized-with-custom-event-properties}

Testar campaigns personalizadas com [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) difere um pouco de testar outros tipos de campaigns descritos.

{% tabs local %}
{% tab Disparar manualmente %}

#### Método 1: Disparando a campaign manualmente {#method-1-triggering-campaign-manually}

Você pode disparar a campaign você mesmo como uma forma robusta de testar campaigns personalizadas usando propriedades de eventos personalizados:

1. Escreva o conteúdo envolvendo a propriedade do evento.

![Compondo uma mensagem de teste com propriedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Use a [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para entregar a campaign quando o evento ocorrer.

{% alert note %}
Se você estiver testando uma campaign de push para iOS, será necessário definir a postergação para um minuto para permitir que você tenha tempo de sair do app, pois o iOS não entrega notificações por push para o app que estiver aberto no momento. Outros tipos de campaigns podem ser configurados para entrega imediata.
{% endalert %}

![Entrega da mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Direcione os usuários como faria para testes, usando um filtro de teste ou direcionando para o seu próprio endereço de e-mail, e finalize a criação da campaign.

![Direcionamento da mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Acesse seu app e conclua o evento personalizado.

A campaign será disparada e exibirá a mensagem personalizada com a propriedade do evento.

![Exemplo de mensagem de teste]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Mensagem de teste %}

#### Método 2: Enviando uma mensagem de teste para você mesmo {#method-2-sending-yourself-a-test-message}

Como alternativa, se você estiver salvando IDs de usuário personalizados, também poderá testar a campaign enviando uma mensagem de teste personalizada para você mesmo.

1. Escreva o conteúdo da sua campaign.
2. Selecione a guia **Test** e escolha **Customized User**.
3. Adicione a propriedade do evento personalizado na parte inferior da página e adicione seu ID de usuário ou endereço de e-mail na caixa superior.
4. Selecione **Send Test** para receber uma mensagem personalizada com a propriedade.

![Testando usando um usuário personalizado]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Usando Liquid {#method-3-using-liquid}

Você pode testar propriedades de eventos personalizados inserindo valores manualmente com Liquid.

1. No editor de mensagens, insira valores para suas propriedades de eventos personalizados.
2. Selecione a guia **prévia as a User** para verificar se a mensagem correta é exibida.

{% endtab %}
{% endtabs %}

## Limitações {#limitations}

Existem algumas situações em que as mensagens de teste não se comportam da mesma forma que Campaigns ou Canvas enviados para usuários reais. Nesses casos, considere lançar a Campaign ou o Canvas para um conjunto limitado de usuários teste para validar esse comportamento.

- Visualizar a [Central de Preferências]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) da Braze a partir de mensagens de teste faz com que o botão **Save Preferences** fique desativado. As Liquid tags da Central de Preferências também podem não resolver para links válidos. Esse é o comportamento esperado. Para testar de ponta a ponta, consulte [Testando centrais de preferências]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).
- Para testar mensagens no app e Content Cards, o usuário-alvo deve ter um token por push para o dispositivo de destino.
- Para testar links de cancelamento de inscrição em e-mails, verifique se o endereço de e-mail do seu usuário teste está no respectivo espaço de trabalho.
- O cabeçalho `List-Unsubscribe` não é incluído em e-mails enviados pela funcionalidade de mensagem de teste.
- E-mails enviados para usuários do grupo de teste não atualizam a lista de Campaigns recebidas no perfil de usuário nem incrementam os envios na análise de dados do dashboard.

## Solução de problemas {#troubleshooting}

### Mensagens no app {#in-app-messages}

Se a campanha de mensagem no app não for disparada por uma campanha de push, verifique a segmentação da campanha de mensagem no app para confirmar que o usuário atende ao público-alvo **antes** de receber a mensagem de push.

Para envios de teste no Android e iOS, as mensagens no app que usam o comportamento ao clicar **Solicitar permissão de push** podem não ser exibidas em alguns dispositivos. Como alternativa:
- **Android:** Os dispositivos precisam estar no Android 13 e na versão 21.0.0 ou superior do nosso SDK or kit de desenvolvimento de software para Android. Outro motivo pode ser que o dispositivo no qual a mensagem no app é exibida já tenha uma solicitação no nível do sistema. Pode ser que você tenha selecionado **Não perguntar novamente**, então talvez seja necessário reinstalar o app para redefinir as permissões de notificação antes de testar novamente.
- **iOS:** Recomendamos que sua equipe de desenvolvimento revise a implementação das notificações por push do seu app e remova manualmente qualquer código que solicite permissões de push. Para saber mais, consulte [Mensagens no app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices).

Para que uma campanha de mensagem no app baseada em ação seja entregue, você precisa registrar eventos personalizados por meio do SDK or kit de desenvolvimento de software da Braze, e não por REST or transferir estado representacional APIs, para que os usuários possam receber mensagens no app elegíveis diretamente no dispositivo. Os usuários recebem a mensagem no app se realizarem o evento durante a sessão.