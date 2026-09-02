---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 3
description: "Este artigo de referência aborda as etapas envolvidas na criação e desenvolvimento de uma mensagem WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows é um aprimoramento do canal WhatsApp existente, que permite criar experiências de envio de mensagens interativas e dinâmicas. Esta página fornece instruções passo a passo para usar o WhatsApp Flows.

## Configurando o WhatsApp Flows {#setting-up-whatsapp-flows}

1. Faça login na sua conta Meta.
2. Crie Flows a partir de um dos dois locais principais:
    - **Account tools:** Acesse a guia **Flows** para visualizar o Flow ID e criar um novo Flow.
    - **Manage templates:** Este é o método recomendado para criar Flows. Aqui, você pode gerar modelos e selecionar uma opção de Flow durante o processo de criação do modelo.

![WhatsApp Manager com uma página para criar um modelo de Flows.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{% alert tip %}
Você também pode criar um modelo de Flow de Marketing ou Utilitário na Braze com o [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder). Crie e gerencie o Flow em si no WhatsApp Manager da Meta e, em seguida, selecione esse Flow ao criar o modelo na Braze.
{% endalert %}

{: start="3"}
3. Selecione um Flow existente ou crie um novo. Ao criar um Flow, escolha entre duas opções:
  - **Custom Form:** Para requisitos específicos
  - **Pre-designed Elements:** Para uma configuração mais rápida

## Configurando mensagens e respostas de WhatsApp Flow {#configuring-whatsapp-flow-messages-and-responses}

{% tabs local %}
{% tab Mensagem de modelo %}

1. Em um Canvas da Braze, crie uma etapa de mensagem do WhatsApp que use o modelo de mensagem contendo o respectivo Flow.
2. Continue criando seu modelo. Se necessário, adicione mídia, conteúdo variável ou ambos à sua mensagem. A seleção do seu Flow é feita quando o modelo é criado, então informações adicionais para a experiência do Flow não são necessárias.

![Criador de mensagens do WhatsApp usando um modelo de WhatsApp Flow.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Mensagem de resposta %}

1. Em um Canvas da Braze, crie uma etapa de mensagem do WhatsApp que use uma mensagem de resposta e uma mensagem de Flow.

![Uma etapa de mensagem para um tipo de mensagem de resposta do WhatsApp e layout de mensagem de Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Selecione o respectivo Flow e continue criando sua mensagem.

![Um criador de mensagem de resposta de Flow com um menu suspenso expandido para selecionar um Flow.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Prévia do Flow {#preview-flow}

Antes de lançar um Canvas com um Flow, você pode selecionar **Preview Flow** para visualizar o Flow diretamente na Braze e confirmar que ele se comporta como esperado. Você também pode interagir com o Flow na prévia para experimentar como um usuário navegaria pelo Flow e, em seguida, fazer ajustes em tempo real. Se um Flow contiver várias páginas, você pode interagir com cada página.

![Janela de prévia exibindo um formulário para o usuário concluir o cadastro.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Salvando a resposta completa do Flow {#full-flow}

Ao incorporar uma mensagem de WhatsApp Flow em um Canvas ou uma Campaign da Braze, você pode querer capturar e utilizar informações específicas que os usuários enviam pelo Flow. A Braze precisa receber informações adicionais sobre a estrutura da resposta do usuário, especificamente o formato esperado da resposta JSON, para gerar o esquema de atributo personalizado aninhado (NCA) necessário.

### Etapa 1: Gerar o atributo personalizado do Flow {#step-1-generate-the-flow-custom-attribute}

{% tabs local %}
{% tab Método recomendado %}

A maneira mais simples de fornecer à Braze as informações sobre a estrutura da resposta é salvar a resposta do Flow como um atributo personalizado e realizar um envio de teste.

#### Usando um Flow que ainda não foi usado na Braze {#using-a-flow-that-hasnt-been-used-in-braze}

Se você estiver usando um Flow que não foi usado anteriormente na Braze, ao visualizar a seção **Flow Custom Attribute** em **Compose Messages**, pode ser que nenhuma informação apareça. Isso significa que o esquema ainda não foi gerado.

![Seção Meta Flow com uma opção para visualizar o atributo personalizado do Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Para resolver isso, faça o seguinte:

1. Conclua a configuração da sua etapa de mensagem WhatsApp.
2. Confirme que você marcou **Save Flow responses as a custom attribute**.
3. Envie uma mensagem de teste para si mesmo e conclua o Flow como um usuário.

Agora, a Braze tem o formato da resposta JSON do Flow e pode gerar o atributo personalizado.

{% endtab %}
{% tab Métodos alternativos %}

Use o editor JSON avançado para salvar atributos da resposta do Flow em atributos personalizados, ou use um Canvas de várias etapas para salvar a resposta em um atributo personalizado aninhado.

{% subtabs %}
{% subtab Editor JSON avançado %}

No editor JSON avançado, insira {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, onde "flow_1" é o atributo personalizado no qual você deseja que o Flow seja salvo.

![Etapa de Atualização de usuário com um editor JSON avançado.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab Editor de interface %}

1. Confirme que você já criou um atributo personalizado com o tipo de dados objeto ("flow_1" neste exemplo) dentro das configurações de dados do seu espaço de trabalho.
2. No editor de interface, use o Liquid {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} para preencher o atributo personalizado e salvar toda a resposta do Flow do usuário nele. Você precisa preencher o valor da chave como {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} antes de selecionar o atributo personalizado que você criou.

![Etapa de Atualização de usuário que usa o editor de interface.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Depois que a Braze receber uma resposta do Flow, salvaremos o atributo personalizado aninhado com a nomenclatura prescrita no perfil do usuário. Esse atributo personalizado pode ser utilizado ao criar Canvas.

![Uma janela exibindo o conteúdo de um atributo personalizado "flow_1".]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 2: Visualizar a resposta salva do Flow {#step-2-view-the-saved-flow-response}

Quando o Flow é concluído, a Braze cria automaticamente um atributo personalizado do Flow com um nome baseado no Flow ID. Você pode então acessar o perfil do usuário para visualizar a resposta salva do Flow como um objeto aninhado na seção **Custom Attributes**.

Após a geração do esquema, a seção **Custom Attribute** do Flow exibirá a estrutura esperada, incluindo os tipos de dados previstos para cada resposta (por exemplo, "String" ou "String Array").

![Janela de detalhes dos atributos personalizados do Flow com menu suspenso de esquema.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Considerações {#considerations}

- **Atributos existentes:** Se um atributo personalizado para um Flow específico já foi gerado, o Flow será carregado com as informações do atributo disponíveis. Nesses casos, você não precisa enviar uma mensagem de teste para gerar o esquema, pois a Braze já reconhece as mensagens de resposta esperadas.
- **Alterações no Flow:** Se você fizer qualquer alteração no Flow após a geração do esquema, será necessário enviar uma mensagem de teste adicional para que a Braze possa entender que o formato da resposta do Flow mudou e ajustar a estrutura do atributo de acordo. Essa ação é limitada a uma vez a cada 24 horas.
- **Consistência:** O atributo personalizado do Flow gerado é consistente e será o mesmo atributo para esse Flow específico, independentemente do Canvas em que é usado.
- **Opção manual:** Você não é obrigado a marcar a caixa de seleção **Save Flow responses as a custom attribute**. Você pode gerar manualmente o atributo personalizado [salvando campos específicos das respostas do Flow em um atributo personalizado específico](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), o que evita a duplicação de etapas do usuário.

## Salvando campos específicos das respostas de Flow em um atributo personalizado específico {#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute}

### Etapa 1: Criar uma jornada de ação {#step-1-create-an-action-path}

Crie uma etapa do Canvas de [jornada de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) ou uma campanha baseada em ação. Selecione um gatilho **Send a WhatsApp inbound message** e a condição **Responded to Flow**, depois selecione o Flow relevante ou **Any Flow**.

![Um gatilho para usuários que enviaram uma mensagem de entrada do WhatsApp e responderam a qualquer Flow.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Etapa 2: Extrair campos das respostas de Flow {#step-2-extract-fields-from-flow-responses}

Você pode usar atributos personalizados aninhados ou a Liquid tag `json_parse` para extrair campos específicos das respostas de Flow.

{% tabs %}
{% tab Atributos personalizados aninhados %}

Para salvar partes específicas da resposta de Flow do usuário, conclua todas as etapas em [Salvando a resposta completa do Flow](#full-flow), **incluindo o lançamento do Canvas**. O Canvas precisa ser lançado para criar o atributo personalizado aninhado que você vai referenciar. Após lançar o Canvas e concluir um Flow, siga estas etapas:

1. Crie uma etapa subsequente de Atualização de Usuário que use o editor de UI.
2. Selecione **Add Personalization**, depois selecione **Nested Custom Attribute** e o atributo de nível superior correspondente onde o Flow está armazenado.

![Etapa de Atualização de Usuário com uma personalização de atributos personalizados aninhados.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3. Selecione o atributo-chave que você deseja salvar e insira o Liquid no campo **Key Value**.

![Janela de "flow_1" com atributos disponíveis para seleção.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. Escolha o atributo onde você deseja armazená-lo.
5. Envie uma mensagem de teste para testar o Flow.

{% endtab %}
{% tab Função de parse %}

Use a Liquid tag `json_parse` para extrair respostas específicas do flow. Por exemplo, você pode extrair o token do Flow e as opções selecionadas para personalizar uma mensagem de acompanhamento.

No editor de UI, selecione o seguinte:

- **Attribute Name:** SEU_ATRIBUTO_PERSONALIZADO (neste exemplo: "First_name")
- **Action:** Update
- **Key Value:** {% raw %} `{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}`{% endraw %}

![Criador de mensagem do WhatsApp com um componente "Add Personalization" para inserir uma personalização de propriedades do WhatsApp com o atributo personalizado `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Quando estiver tudo pronto, envie uma mensagem de teste para testar o Flow. Depois, lance o Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Uma nova mensagem do WhatsApp "limpa" a capacidade do Canvas de usar (e reutilizar) a resposta Liquid do Flow, então certifique-se de que as mensagens de acompanhamento estejam após todas as etapas de Atualização de Usuário, webhooks ou outras etapas que usam a resposta Liquid do Flow.
{% endalert %}

## Adicionando uma tag de personalização de Flow {#adding-a-flow-personalization-tag}

Para usar a resposta do Flow por meio de Liquid com [tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), siga as etapas a seguir:

1. Ao criar sua mensagem do WhatsApp, selecione <i class="fas fa-plus-circle"></i> **Adicionar personalização** para abrir a janela **Adicionar personalização**.
2. Selecione **WhatsApp Properties** para o tipo de personalização e **inbound_flow_response** para o atributo personalizado. Isso pode ser usado para salvar informações nos perfis de usuário, incluí-las em mensagens ou encaminhá-las para outros serviços, como webhooks.

![Criador de mensagem do WhatsApp com o componente "Adicionar personalização" para inserir uma personalização de propriedades do WhatsApp com o atributo personalizado inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Para dúvidas ou assistência adicional, entre em contato com o [Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).