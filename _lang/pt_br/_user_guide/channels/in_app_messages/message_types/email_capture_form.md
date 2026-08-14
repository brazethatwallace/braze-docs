---
nav_title: Formulário de captura de e-mail
article_title: Formulário de captura de e-mail
page_order: 5
page_type: reference
description: "Este artigo fornece uma visão geral do tipo de mensagem no app de captura de e-mail."
channel:
  - in-app messages
---

# Formulário de captura de e-mail {#email-capture-form}

> As mensagens de captura de e-mail permitem que você solicite aos usuários do seu site que enviem seus endereços de e-mail. A Braze adiciona o endereço ao perfil de usuário para uso em todas as suas campanhas de envio de mensagens.

Esse tipo de mensagem está disponível no [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Como funciona {#how-it-works}

Quando um usuário final insere seu endereço de e-mail nesse formulário, a Braze adiciona o endereço de e-mail ao perfil de usuário.

- Para [usuários anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) que ainda não possuem uma conta, o endereço de e-mail é armazenado no perfil de usuário anônimo vinculado ao dispositivo do usuário.
- Se já existir um endereço de e-mail no perfil de usuário, o novo endereço inserido substituirá o endereço existente.
- Se o usuário conhecido tiver um endereço de e-mail sinalizado como [hard bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#hard-bounce), a Braze verifica se o novo endereço de e-mail inserido é diferente do que está no perfil da Braze. Se o endereço de e-mail fornecido for diferente, a Braze atualiza o endereço de e-mail e remove o status de hard bounce.
- Se um usuário inserir um endereço de e-mail inválido, verá a mensagem de erro: "Please enter a valid email."
    - Endereços de e-mail inválidos:
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Endereços de e-mail válidos:
        - `example@gmail.com`
        - `example@gnail.com` (com erro de digitação)
    - Para saber mais sobre a validação de e-mail na Braze, consulte [Diretrizes técnicas e notas sobre e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation).

{% details Mais sobre usuários identificados versus anônimos %}

O formulário de captura de e-mail define o endereço de e-mail no perfil de usuário atualmente ativo na Braze. O comportamento varia dependendo de o usuário ser identificado (logado, `changeUser` chamado) ou não.

Se um usuário anônimo inserir seu e-mail no formulário e enviá-lo, a Braze adicionará o endereço de e-mail ao perfil dele. Se `changeUser` for chamado posteriormente na jornada web e um novo `external_id` for atribuído (como quando um novo usuário se registra no serviço), todos os dados do perfil de usuário anônimo serão mesclados, incluindo o endereço de e-mail.

Se `changeUser` for chamado com um `external_id` existente, o perfil de usuário anônimo será órfão e [campos específicos de dados do perfil de usuário]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) que ainda não existem no usuário identificado serão mesclados, mas os campos que já existem serão perdidos, incluindo o endereço de e-mail.

Para saber mais, consulte o [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).

{% enddetails %}

## Etapa 1: Crie uma Campaign de mensagem no app {#step-1-create-an-in-app-message-campaign}

Para acessar essa opção, você precisa criar uma Campaign de mensagem no app. A partir daí, dependendo do seu caso de uso, defina **Send To** como **Web Browsers**, **Mobile Apps** ou **Both Mobile Apps & Web Browsers** e selecione **Email Capture Form** como seu **Message Type**.

{% alert note %}
**Direcionando usuários da web?** <br>Para ativar mensagens no app em HTML pelo Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso é por motivos de segurança, já que mensagens no app em HTML podem executar JavaScript, então exigimos que um mantenedor do site as ative.
{% endalert %}

## Etapa 2: Personalize o formulário {#customizable-features}

Em seguida, personalize o formulário conforme necessário. Você pode personalizar os seguintes recursos do formulário de captura de e-mail:

- Texto do cabeçalho, corpo e botão de envio
- Uma imagem opcional
- Um link opcional de "Termos de Serviço"
- Cores diferentes para o texto do cabeçalho e corpo, botões e plano de fundo
- Pares de chave-valor
- Estilo do texto do cabeçalho e corpo, botões, cor da borda dos botões, plano de fundo e sobreposição
- Botão de envio
    - O botão de envio aparece somente depois que o usuário insere um endereço de e-mail válido. Isso ajuda você a coletar endereços de e-mail completos.

![Criador do formulário de captura de e-mail.]({% image_buster /assets/img/email_capture.png %})

Se você precisar de mais personalização, escolha **Custom Code** como seu **Message Type**. Use este [modelo de modal de captura de e-mail](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) do repositório GitHub [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) como código inicial.

## Etapa 3: Defina seu público de entrada {#step-3-set-your-entry-audience}

Se você estiver usando uma mensagem no app para capturar e-mails de usuários, pode querer limitar o público a usuários que ainda não forneceram essa informação.

- **Para direcionar usuários sem endereço de e-mail:** Use o filtro `Email Available` como `false`. Isso faz com que o formulário apareça apenas para usuários que não têm um e-mail registrado, ajudando a evitar solicitações redundantes para usuários conhecidos.
- **Para direcionar usuários anônimos sem IDs externos:** Use o filtro `External User ID` `is blank`. Isso é útil quando você deseja identificar usuários que ainda não foram autenticados ou registrados.

Você também pode combinar os dois filtros usando a lógica `AND`, se desejar. Isso faz com que o formulário apareça apenas para usuários que não possuem endereço de e-mail nem ID de usuário externo — ideal para capturar novos leads ou incentivar a criação de contas.

## Etapa 4: Direcione usuários que preencheram o formulário (opcional) {#step-4-target-users-who-filled-out-the-form-optional}

Depois de lançar o formulário de captura de e-mail e coletar endereços de e-mail dos seus usuários, você pode direcionar os usuários que preencheram o formulário.

1. Em qualquer filtro de segmento na Braze, selecione o filtro `Clicked/Opened Campaign`.
2. No menu suspenso, selecione `clicked in-app message button 1`.
3. Selecione sua Campaign de formulário de captura de e-mail.