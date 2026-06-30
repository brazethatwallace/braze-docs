---
nav_title: "Adquirir um número"
article_title: "Adquirir um número de telefone do WhatsApp"
page_order: 1
description: "Este artigo de referência aborda como adquirir um número de telefone pela Twilio e pela Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Adquirir um número de telefone do WhatsApp {#acquire-a-whatsapp-phone-number}

> Para usar o canal de envio de mensagens do WhatsApp, você precisará de um número de telefone que atenda aos requisitos do WhatsApp para sua [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Você deve adquirir seu número de telefone por conta própria, pois a Braze não fará o provisionamento do número para você. Você pode comprar um telefone físico com chip SIM pelo seu provedor de telefonia empresarial ou usar um dos nossos parceiros: Twilio ou Infobip. **Você deve ter sua própria conta na Twilio ou na Infobip, pois isso não pode ser feito pela Braze.**

## Requisitos da API do WhatsApp {#whatsapp-api-requirements}

Seu número de telefone deve atender a estes requisitos da API do WhatsApp:

- Pertencer à sua empresa
- Ter um código de país e de área (como números de telefone fixo e celular)
- Ser capaz de receber chamadas de voz ou SMS
- Estar acessível durante a configuração da conta (para receber códigos de verificação)
- Não ser um código curto (short code)
- Não ter sido usado anteriormente com a WhatsApp Business Platform
- Não estar conectado a uma conta pessoal do WhatsApp

## Adquirindo um número de telefone da Twilio {#acquiring-a-twilio-phone-number}

### Etapa 1: Comprar um número de telefone pelo console ou API da Twilio {#step-1-buy-a-phone-number-from-the-twilio-console-or-api}

1. No console da Twilio, acesse **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Se você não vir essa opção, selecione **Explore Products**, role até **Super Networks** e selecione **Phone Number** > **Buy a number**. <br><br>![Console da Twilio com a guia "Develop" aberta e a opção "Buy a number".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Insira o código de área ou localidade desejada (se tiver). Encontre um número e selecione **Buy**. <br><br> ![Botão para comprar o número de telefone listado.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Após comprar seu número de telefone, acesse **Active Numbers** e selecione o número de telefone que você acabou de comprar. <br><br>!["Active Numbers" mostrando o número de telefone comprado.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Etapa 2: Configurar seu número de telefone {#step-2-configure-your-phone-number}

Configure seu número de telefone da Twilio para receber códigos de verificação por e-mail. **Não vincule seu número de telefone ao WhatsApp no console da Twilio.**

{% alert warning %}
Não vincule seu número de telefone ao WhatsApp no console da Twilio. Se fizer isso, o número será registrado na conta WhatsApp Business da Twilio, o que impedirá que você o conecte à Braze pelo fluxo de inscrição integrado.
{% endalert %}

1. No console da Twilio, acesse a [página Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) e selecione o número de telefone que você comprou.
2. Acesse a seção **Voice Configuration** e, no menu suspenso **Configure with**, selecione **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. Na linha **A call comes in**, selecione **Webhook** e defina a URL como `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, substituindo `YOUR_EMAIL_ADDRESS` pelo seu endereço de e-mail.

### Etapa 3: Concluir o fluxo de inscrição integrado {#step-3-complete-the-embedded-sign-up-workflow}

1. Após a configuração da Twilio, acesse o dashboard da Braze > **Parceiros de tecnologia** > **WhatsApp** e selecione **Begin integration** ou **Add WhatsApp Business Account**, o que estiver disponível, para acionar o [fluxo de inscrição integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).<br><br>Na etapa **Add a phone number for WhatsApp**, selecione **Phone call** para escolher como você deseja verificar seu número de telefone. <br><br>![Seção com as opções para verificar seu número de telefone por mensagem de texto ou chamada telefônica.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Aguarde alguns minutos para que o código de verificação seja enviado para sua caixa de entrada de e-mail, insira o código de verificação e conclua a configuração.

## Adquirindo um número de telefone da Infobip {#acquiring-an-infobip-phone-number}

1. No console da Infobip, acesse **Channels and Numbers** e selecione **Numbers**.<br><br>![Seção "Channels and Numbers" da Infobip com "Numbers" listado abaixo.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Selecione **Buy Number** > o país para onde você deseja enviar mensagens > **SMS**.<br><br>![Botão para comprar um número.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Dependendo do país selecionado, pode ser necessário concluir um processo de registro adicional (como selecionar uma opção 10 DLC ou toll-free para números de telefone dos EUA). Certifique-se de selecionar a opção disponível.<br><br>![Página solicitando que você selecione o tipo de número: 10 DLC ou toll-free.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Selecione a oferta disponível, prossiga pelas demais etapas e aguarde o processamento da sua solicitação. Você pode verificar o status acessando **Numbers** > **My Request**. <br><br>![Uma oferta com informações incluindo taxas e cobertura.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Dependendo do país selecionado, aguarde a equipe da Infobip entrar em contato com você para obter detalhes de registro (como para 10DLC nos EUA).<br><br>

6. Quando seu número de telefone estiver pronto na Infobip, acesse o dashboard da Braze > **Parceiros de tecnologia** > **WhatsApp** e selecione **Begin integration** ou **Add WhatsApp Business Account**, o que estiver disponível, para acionar o [fluxo de inscrição integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).<br><br> Na etapa **Add a phone number for WhatsApp**, selecione **Text message** para escolher como você deseja verificar seu número de telefone.<br><br>![Seção com as opções para verificar seu número de telefone por mensagem de texto ou chamada telefônica.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Verifique os [registros de análise](https://www.infobip.com/docs/analyze/analyze-logs) da Infobip no portal do cliente para obter o código de verificação, que pode levar alguns minutos para aparecer. Em seguida, insira o código de verificação e conclua a configuração.