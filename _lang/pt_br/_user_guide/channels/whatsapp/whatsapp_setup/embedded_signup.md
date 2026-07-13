---
nav_title: Cadastro integrado
article_title: Cadastro integrado do WhatsApp
page_order: 1
description: "Este artigo de referência fornece um passo a passo do fluxo de cadastro integrado do WhatsApp na Braze."
page_type: reference
channel:
  - WhatsApp
---

# Cadastro integrado do WhatsApp {#whatsapp-embedded-signup}

> Este artigo de referência fornece um passo a passo do fluxo de cadastro integrado do WhatsApp na Braze.

O fluxo de cadastro integrado do WhatsApp é acessado quando você [integra o WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) ao seu espaço de trabalho da Braze pela primeira vez, e quando você [adiciona uma conta do WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) a uma integração existente do WhatsApp.

{% alert note %}
Você pode adicionar [múltiplas contas do WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) a um espaço de trabalho da Braze. No entanto, cada conta específica do WhatsApp Business pode ser adicionada a apenas um espaço de trabalho da Braze.
{% endalert %}

## Acessando o fluxo {#accessing-the-workflow}

Acesse **Integrações de parceiros** > **Parceiros de tecnologia**, pesquise e selecione **WhatsApp**. A próxima seleção depende do seu caso de uso:

- Se você está integrando o WhatsApp ao seu espaço de trabalho, selecione **Begin Integration**. <br><br>![Página de parceiro do WhatsApp com um botão para iniciar a integração.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- Se você está adicionando uma conta do WhatsApp Business a uma integração existente do WhatsApp, selecione **Add WhatsApp Business Account**. <br><br>![Integração de envio de mensagens do WhatsApp com opções para adicionar uma conta do WhatsApp Business ou um grupo de inscrições e número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

O fluxo a partir daqui é o mesmo para ambos os casos de uso.

## Fluxo de cadastro integrado do WhatsApp {#whatsapp-embedded-signup-workflow}

1. Na janela de login da Meta (Facebook), selecione **Login as** ou **Continue**. <br><br>![Janela de login da Meta.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Leia as permissões que serão compartilhadas com a Braze e selecione **Get Started**. <br><br>![Lista de permissões que serão compartilhadas com a Braze para a integração.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. Nesta tela, configure o seguinte e selecione **Next**:
- No menu suspenso **Business portfolio**, selecione seu portfólio de negócios. Isso se conecta à sua conta do WhatsApp Business. Se você não encontrar o portfólio de negócios esperado, verifique suas permissões.
- No campo **WhatsApp business account**, selecione **Create a new WhatsApp Business Account**, inclusive quando estiver adicionando outra conta do WhatsApp Business ao seu espaço de trabalho ou quando essa conta já existir na Meta. Escolha essa opção em vez de selecionar uma conta existente do WhatsApp Business no menu suspenso. <br><br>![Uma janela com campos para inserir as informações do seu negócio, incluindo o nome do portfólio de negócios.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. Selecione as seguintes opções nos campos suspensos e depois selecione **Next**.
- **Choose a WhatsApp Business account**: Create a WhatsApp business account
- **Create or select a WhatsApp Business profile**: Create a new WhatsApp business profile <br><br>![Campos para especificar se você está escolhendo ou criando uma conta e perfil do WhatsApp Business.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. Forneça as seguintes informações e selecione **Next**.
- Nome da conta do WhatsApp Business
- Nome de exibição do WhatsApp Business
- Categoria <br><br>![Campos para fornecer detalhes da nova conta do WhatsApp Business.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. Insira seu número de telefone e escolha **Text message** ou **Phone call**. Para um número novo, ele deve atender aos requisitos de número de telefone do WhatsApp, incluindo não estar registrado em nenhuma outra conta do WhatsApp. Se você está migrando um número existente (veja a etapa 3) e a Meta indicar que o número já está em uso, continue além do aviso para concluir a migração. <br><br>![Campos para adicionar um número de telefone.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. Insira o código de autenticação de dois fatores e selecione **Next**. <br><br>![Um campo de entrada para o código de autenticação de dois fatores.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. Revise as permissões que sua conta do WhatsApp Business receberá e selecione **Continue**. <br><br>![Lista de permissões solicitadas pela conta do WhatsApp Business.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. Pronto! <br><br>![Janela informando que você está pronto para começar a enviar mensagens.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}