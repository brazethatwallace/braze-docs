---
nav_title: Começar
article_title: Comece com o Braze Pilot
page_order: 2
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."
---

# Comece com o Braze Pilot {#get-started-with-braze-pilot}

> Este artigo explica como começar a usar o Braze Pilot. Vamos orientar você pelo download do app, pela inicialização da conexão com seu dashboard da Braze e pela conclusão da configuração.

## Etapa 1: Baixe o Braze Pilot {#step-1-download-braze-pilot}

Para começar a usar o Braze Pilot, primeiro você precisa baixar o app na Apple App Store ou na Google Play Store. Você pode pesquisar o app na loja de apps ou escanear os códigos QR na seção a seguir para acessar a página do app no seu dispositivo.

## Etapa 2: Aceite os termos e condições {#step-2-accept-the-terms-and-conditions}

Em seguida, aceite os termos e condições e insira seu e-mail de trabalho no formulário. Seu e-mail será usado apenas para análise de dados de uso do app e não será utilizado para fins de marketing.

![Página de boas-vindas do Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Opção para inserir seu endereço de e-mail de trabalho.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Etapa 3: Inicialize a conexão com o SDK da Braze {#step-3-initialize-the-connection-with-the-braze-sdk}

O Braze Pilot permite que você inicialize o SDK da Braze em qualquer dashboard da Braze. Depois que o SDK for inicializado, o Pilot começará a enviar dados de engajamento para a Braze e permitirá que você acione qualquer envio de mensagens lançado a partir desse dashboard.

Existem dois métodos para configurar a conexão do SDK no Pilot: códigos QR de demonstração e o assistente de configuração.

{% tabs local %}
{% tab Códigos QR de demonstração %}

### Método 1: Códigos QR de demonstração {#method-1-demo-qr-codes}

Escaneie um código QR que inclui todos os detalhes necessários para inicializar o SDK, criar seu perfil de usuário e fazer deep link para uma simulação de app específica no Braze Pilot. Os códigos QR de demonstração são exibidos no painel complementar de campanhas de demonstração específicas no seu teste gratuito.

| Pilot para Android | Pilot para iOS |
| --- | --- |
| ![Código QR para Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![Código QR para iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Método 1: Códigos QR de demonstração" }

{% endtab %}
{% tab Assistente de configuração %}

### Método 2: Assistente de configuração {#method-2-setup-wizard}

Siga um guia passo a passo para inicializar a conexão com o espaço de trabalho do seu dashboard a partir da página **Configurações do app** no seu dashboard da Braze.

![Etapa 1 do assistente de configuração do Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Essa conexão é específica do espaço de trabalho. Isso significa que, se você inicializar a conexão a partir do espaço de trabalho de demonstração e depois mudar para o espaço de trabalho ativo no dashboard do seu teste gratuito, será necessário reinicializar o SDK a partir desse espaço de trabalho para receber as campanhas lançadas nele.

![O menu suspenso de espaços de trabalho no dashboard da Braze com "Demo - Braze" selecionado como o espaço de trabalho ativo.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Etapa 4: Permita as notificações push {#step-4-allow-push-permissions}

Por fim, é recomendado que você permita que o app envie notificações push se quiser testar os recursos de push pelo app. Você pode conceder essas permissões das seguintes formas: atualizando as configurações do app nas configurações do seu dispositivo ou lançando uma mensagem introdutória de push da Braze para o app.

{% tabs local %}
{% tab Atualize as configurações do app %}

Abra as configurações do seu dispositivo e localize o Braze Pilot. Em seguida, atualize as configurações para permitir que as notificações apareçam na sua tela de bloqueio.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Lance uma mensagem introdutória de push %}

Você pode usar uma mensagem no app da Braze para solicitar permissões de push para o app, assim como faria para seus próprios consumidores. Para saber como criar esse tipo de mensagem na Braze, consulte [Mensagens introdutórias de push no app]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Etapa 5: Experimente o envio de mensagens da Braze no Pilot {#step-5-experience-braze-messaging-in-pilot}

Agora você está pronto para começar a receber campanhas e Canvas do seu dashboard da Braze como usuário do Braze Pilot! Acesse qualquer uma das campanhas lançadas no seu espaço de trabalho de demonstração para uma rápida demonstração dos casos de uso da Braze. Depois, vá para o seu espaço de trabalho ativo para começar a enviar suas próprias mensagens.

Para mais informações sobre como configurar campanhas e Canvas na Braze, consulte [Primeiros passos: Campaigns e Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).