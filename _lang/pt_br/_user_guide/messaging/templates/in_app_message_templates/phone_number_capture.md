---
nav_title: Formulário de inscrição para SMS, RCS e WhatsApp
article_title: Formulário de inscrição para SMS, RCS e WhatsApp
alias: "/phone_number_capture/"
page_order: 2
description: "Esta página explica como criar um formulário de inscrição para SMS, RCS e WhatsApp com o editor de arrastar e soltar de mensagens no app."
---

# Formulário de inscrição para SMS, RCS e WhatsApp {#sms-rcs-and-whatsapp-sign-up-form}

> Os formulários de inscrição para SMS, RCS e WhatsApp são modelos disponíveis no editor de arrastar e soltar para mensagens no app. Use esses modelos para coletar os números de telefone dos usuários e expandir seus grupos de inscrições de SMS, MMS, RCS e WhatsApp.

![Três exemplos de mensagens no app criadas usando o modelo de formulário de inscrição por telefone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criando um formulário de inscrição por número de telefone {#creating-a-phone-number-sign-up-form}

### Etapa 1: Escolha seu modelo {#step-1-choose-your-template}

Ao criar uma mensagem no app de arrastar e soltar, selecione **SMS sign-up** (que também funciona para inscrição em RCS) ou **WhatsApp sign-up** como modelo e, em seguida, selecione **Build message**. Esses modelos são compatíveis com apps para dispositivos móveis e navegadores web.

![Modal para selecionar SMS sign-up ou WhatsApp sign-up como modelo ao criar uma mensagem no app.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Etapa 2: Configure os estilos da sua mensagem {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![Fluxo de trabalho para fazer upload e selecionar uma fonte personalizada.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Etapa 3: Personalize o componente de entrada de número de telefone {#step-3-customize-your-phone-number-input-component}

Para começar a criar seu formulário de inscrição, selecione o componente de entrada de número de telefone no editor.

![Área de pré-visualização ao criar um formulário de inscrição com o componente de entrada de número de telefone selecionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

No menu lateral, especifique para qual grupo de inscrições este modelo coletará números de telefone. Para seguir as melhores práticas de conformidade, você só pode coletar consentimento para um grupo de inscrições por formulário de inscrição de número de telefone. No entanto, se desejar, você pode usar vários formulários para coletar consentimento para outros grupos de inscrições.

![Menu suspenso de grupo de inscrições com um grupo de inscrições selecionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Por padrão, coletamos números globalmente. No entanto, você pode limitar os países dos quais os números são coletados. Isso é útil se você pretende enviar mensagens apenas para usuários com números de telefone em países específicos e pode ajudar na limpeza da lista. Para isso, desative **Collect numbers from all countries** e use o menu suspenso para selecionar países específicos. Seus usuários só poderão selecionar os países que você adicionou explicitamente.

![Menu suspenso de países para selecionar os países dos quais você deseja coletar números.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Números de telefone inválidos {#invalid-phone-numbers}

Se seus usuários inserirem um número de telefone que inclua caracteres especiais não aceitos, eles verão um indicador de erro genérico que não é personalizável e não poderão enviar o formulário. Você pode visualizar o comportamento de erro na guia **Preview & Test** e no seu dispositivo de teste. Consulte este artigo para saber [como a Braze formata números de telefone]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#importing-phone-numbers).

### Etapa 4: Adicione o texto de aviso legal (para formulários de inscrição de SMS e RCS) {#step-4-add-disclaimer-language-for-sms-and-rcs-sign-up-forms}

Para formulários de inscrição de SMS e RCS, é importante comunicar claramente o tipo de SMS ou RCS que será enviado. Certifique-se de que o crescimento da sua lista esteja em conformidade incluindo as seguintes informações no seu formulário:

- Descrição dos tipos de mensagens SMS e RCS que seus clientes podem esperar (lembretes de carrinho, promoções e ofertas, lembretes de compromissos, etc.). Você não precisa listar todos os casos de uso, mas deve fornecer uma descrição dos tipos de mensagens que sua marca enviará.
- Observação de que o consentimento não é condição para nenhuma compra (se aplicável).
- Frequência de mensagens e lembrete de que taxas de mensagens e dados podem ser aplicadas. Se você não souber a frequência exata de mensagens, pode informar que a frequência pode variar.
- Links para seus Termos e Condições e Política de Privacidade de SMS e RCS.
- Lembrete das palavras-chave de ajuda e descadastramento (HELP para ajuda; STOP para cancelar).

Incluímos um aviso legal de exemplo no modelo apenas como referência — ele não constitui aconselhamento jurídico e não deve ser utilizado para fins de conformidade. É importante trabalhar com sua equipe jurídica para desenvolver um texto adequado à sua marca específica.

{% alert note %}
Esta documentação não se destina a fornecer, nem pode ser considerada como, aconselhamento jurídico completo.
{% endalert %}

Para saber mais sobre conformidade de SMS e RCS, consulte [Leis e regulamentações para SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).

### Etapa 5: Estilize sua mensagem {#step-5-style-your-message}

Personalize a aparência da sua mensagem usando os [componentes de mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components) de arrastar e soltar.

## Analisando os resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![Painel de desempenho de mensagens no app mostrando os cliques em cada link da mensagem no app.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})