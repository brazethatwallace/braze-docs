---
nav_title: "Ciclo de vida do token por push"
article_title: "Ciclo de vida do token por push"
page_order: 1
page_type: reference
description: "Este artigo de referência discute o que significa estar registrado para push e como enviamos notificações por push e lidamos com tokens por push e registro de push na Braze."
channel:
 - Push
---

# Ciclo de vida do token por push {#push-token-lifecycle}

> Este artigo aborda o processo pelo qual um usuário recebe um token por push e como a Braze envia notificações por push para seus usuários.

## Sobre tokens por push {#push-tokens}

Quando um app solicita permissões de push a um dispositivo, o provedor de notificação por push do dispositivo gera um token por push para esse app. Cada app recebe seu próprio token por push exclusivo e anônimo, que é como ele identifica o dispositivo e a instância atual do app ao enviar uma notificação por push.

Lembre-se de que tokens por push não são identificadores estáticos que duram para sempre&#8212;eles podem ser atualizados e podem [expirar](#push-token-expire).

{% alert tip %}
Para detalhes específicos de cada plataforma, consulte [Registro de token por push](#push-token-registration).
{% endalert %}

### Push em primeiro plano vs. em segundo plano {#foreground-vs-background}

Os tokens por push são usados para enviar notificações por push tanto em primeiro plano quanto em segundo plano.

| Tipo       | Requer opt-in? | Descrição                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Push em primeiro plano | Sim       | Uma notificação é exibida visivelmente para o usuário enquanto o app está em primeiro plano.           |
| Push em segundo plano | Não        | Uma notificação é entregue silenciosamente em segundo plano sem ser exibida. Frequentemente usada para funcionalidades como rastreamento de desinstalação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push em primeiro plano vs. em segundo plano" }

Quando um usuário faz opt-in para notificações por push do seu app, ele será considerado "registrado para push", o que significa que agora pode ser segmentado usando o filtro de segmentação `Foreground Push Enabled for App` na Braze.

{% alert note %}
Isso é diferente do filtro de segmentação `Foreground Push Enabled`, que é usado para identificar usuários que fizeram opt-in em pelo menos um dos seus apps — não em um app específico. Para saber mais, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#foreground-push-enabled).
{% endalert %}

### Múltiplos usuários em um dispositivo {#multiple-users-on-a-device}

Os tokens por push são exclusivos tanto para o dispositivo quanto para o app, o que significa que não podem ser usados para segmentar usuários específicos se múltiplos usuários estiverem usando o mesmo dispositivo.

Por exemplo, digamos que você tenha dois usuários: Charlie e Kim. Se Charlie ativou as notificações por push do seu app no celular dele e Kim usa o celular de Charlie para sair do perfil de Charlie e entrar no dela, o token por push será reatribuído ao perfil de Kim. O token por push permanecerá atribuído ao perfil de Kim naquele dispositivo até que ela saia e Charlie faça login novamente.

Um app ou site pode ter apenas uma inscrição de push por dispositivo. Então, quando um usuário sai de um dispositivo ou site e um novo usuário faz login, o token por push é reatribuído ao novo usuário. Isso é refletido no perfil do usuário na seção **Contact Settings** da guia **Engagement**:

![Changelog do token por push na guia **Engagement** do perfil de um usuário, que lista quando o token por push foi movido para outro usuário e qual era o token.]({% image_buster /assets/img/push_token_changelog.png %})

Como não há uma forma de os provedores de push (APNs/FCM) distinguirem entre múltiplos usuários em um dispositivo, passamos o token por push para o último usuário que fez login para determinar qual usuário segmentar no dispositivo para push.

{% alert tip %}
Se você vir uma mensagem de erro em **Contact Settings** > **Push Changelog**, consulte [Mensagens de erro comuns de push]({{site.baseurl}}/user_guide/channels/push/push_error_codes/) para explicações e próximos passos.
{% endalert %}

## Registro de token por push {#push-token-registration}

Cada plataforma de dispositivo lida com o registro de token por push de forma diferente. Consulte os detalhes específicos de cada plataforma a seguir:

{% tabs local %}
{% tab web %}
Você deve solicitar opt-in explícito dos usuários por meio da caixa de diálogo de permissão nativa do navegador. O token será recebido após os usuários fazerem opt-in. Diferentemente do iOS e Android, que permitem que seu app exiba o prompt de permissão a qualquer momento, alguns navegadores modernos só exibirão o prompt se acionado por um "gesto do usuário" (clique do mouse ou tecla pressionada). Se o seu site tentar solicitar permissão de notificação por push no carregamento da página, provavelmente será ignorado ou silenciado pelo navegador.
{% endtab %}

{% tab android %}
Quando seu app é instalado, um token por push é gerado automaticamente para o app&#8212;no entanto, ele só pode ser usado para [notificações por push em segundo plano](#foreground-vs-background) até que o usuário faça opt-in explicitamente. Além disso, o registro é tratado de forma diferente entre as versões do Android:

| Versão       | Detalhes                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | A permissão de push deve ser solicitada e concedida pelo usuário. Seu app pode solicitar a permissão manualmente, ou os usuários serão solicitados automaticamente após a criação de um [canal de notificação](https://developer.android.com/reference/android/app/NotificationChannel). |
| **Android 12 e anteriores** | Todos os usuários são considerados `Subscribed` após a primeira sessão. A Braze solicita automaticamente um token por push nesse momento, tornando o usuário habilitado para push com um token válido e um estado de inscrição padrão de `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Registro de token por push" }
{% endtab %}

{% tab ios %}
O iOS não gera automaticamente tokens por push para um app quando ele é instalado. Além disso, o registro é tratado de forma diferente entre as versões do iOS:

| Versão                         | Autorização provisória? | Detalhes                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Sim                         | Quando um usuário faz opt-in para notificações por push, você recebe autorização padrão, permitindo enviar [notificações por push em primeiro plano](#foreground-vs-background). No entanto, você também pode solicitar [autorização provisória]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/#provisional-push), que permite enviar [notificações por push em segundo plano](#foreground-vs-background) silenciosas diretamente para a central de notificações. |
| **iOS 11 ou anterior** | Não                          | Todos os usuários devem fazer opt-in explicitamente para receber notificações por push. Um token por push é gerado somente após a permissão ser concedida.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Registro de token por push" }
{% endtab %}
{% endtabs %}

### Verificando o estado de inscrição de push do usuário {#checking-users-push-subscription-state}

![Perfil de usuário de Jane Doe mostrando o estado de inscrição de push e detalhes de registro de push na guia Engagement.]({% image_buster /assets/img/push_implementation_guide/checking-users-push-subscription-state.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Existem duas formas de verificar o estado de inscrição de push de um usuário na Braze:

- **Perfil de usuário**: Você pode acessar perfis de usuários individuais pelo dashboard da Braze na página [Pesquisa de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/). Após encontrar o perfil de um usuário (por endereço de e-mail, número de telefone ou ID de usuário externo), você pode selecionar a guia **Engagement** para visualizar e ajustar manualmente o estado de inscrição do usuário.
- **Exportação via REST API**: Você pode exportar perfis de usuários individuais em formato JSON usando os endpoints de exportação [Usuários por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). A Braze retornará um objeto de tokens por push que contém informações de habilitação de push por dispositivo.

### Verificando o status de registro de push {#checking-push-registration-status}

Na guia **Engagement** do perfil de um usuário, você verá **Push Registered For** seguido do nome de um app. Se não houver informações do app para aquele dispositivo, você verá dois traços (**&#45;&#45;**). Haverá uma entrada para cada dispositivo que pertence ao usuário.

Se o nome do app na entrada do dispositivo for prefixado por `Foreground:`, o app está autorizado a receber tanto notificações por push em primeiro plano (visíveis para o usuário) quanto notificações por push em segundo plano (não visíveis para o usuário) naquele dispositivo.

![Changelog de push com um exemplo de token por push.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Por outro lado, se o nome do app na entrada do dispositivo for prefixado por `Background:`, o app está autorizado apenas a receber [push em segundo plano]({{site.baseurl}}/user_guide/channels/push/types/#background-push-notifications) e não pode exibir notificações visíveis ao usuário naquele dispositivo. Isso geralmente indica que o usuário desativou as notificações para o app naquele dispositivo.

Se um token por push for movido para um usuário diferente no mesmo dispositivo, o primeiro usuário não estará mais registrado para push.

## Gerenciamento de tokens por push {#push-token-management}

Confira o quadro a seguir para ações que levam a alterações ou remoção de tokens por push dos perfis de usuários.

| Ação | Descrição |
| ------ | ----------- |
| Método `changeUser()` chamado | O método `changeUser()` da Braze alterna o ID de usuário ao qual os SDKs estão atribuindo dados de comportamento do usuário. Esse método geralmente é chamado quando um usuário faz login em um aplicativo. Quando `changeUser()` é chamado com um ID de usuário diferente ou novo em um dispositivo específico, o token por push daquele dispositivo será movido para o perfil da Braze correspondente ao ID de usuário. |
| Ocorre um erro de push | Alguns erros comuns de push que levam à remoção do token incluem `MismatchSenderId`, `InvalidRegistration` e outros tipos de bounces de push. <br><br>Confira nossa lista completa de [erros de push]({{site.baseurl}}/user_guide/channels/push/push_error_codes/) comuns. |
| Usuário desinstala | Quando um usuário desinstala o aplicativo de um dispositivo, a Braze removerá o token por push do usuário do perfil. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gerenciamento de tokens por push" }

### Como isso funciona em uma escala mais ampla? {#what-does-this-look-like-on-a-broader-scale}

Quando um usuário abre um novo aplicativo e concede acesso a push a partir de um prompt de push, uma chamada é feita do SDK da Braze para os provedores de push. Quando essa chamada é feita, o provedor de push executa uma verificação para ver se tudo está configurado corretamente. Se estiver, um token por push é passado para o seu dispositivo. Quando esse token chega, o SDK comunica isso à Braze. Após a Braze receber o token do provedor de push, atualizamos ou criamos um novo perfil de usuário. Esses usuários agora são considerados registrados.

Se quisermos lançar uma Campaign, criamos uma Campaign na Braze que gera uma carga útil de push para enviar ao provedor de push. A partir daí, o provedor entrega a carga útil de push ao dispositivo do usuário e o SDK passa o estado do envio de mensagens para a Braze.

![Um fluxograma que mapeia o processo de push mencionado acima entre a Braze, o cliente e o serviço de Notificações por Push da Apple ou Firebase Cloud Messaging.]({% image_buster /assets/img/push_process.png %})

| Etapas de registro | Etapas de envio de mensagens |
| ------------------ | --------------- |
| 1. Cliente (dispositivo) se registra no provedor de push<br>2. Provedor gera e entrega o token por push<br>3. Envio dos tokens para a Braze |1. A Braze envia a carga útil de push para o provedor<br>2. O provedor entrega a carga útil de push ao dispositivo<br>3. O SDK passa as estatísticas de envio de mensagens para a Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como isso funciona em uma escala mais ampla?" }

## Perguntas frequentes {#frequently-asked-questions}

### O que acontece quando um usuário que fez opt-in exclui e depois baixa novamente meu app? {#what-happens-when-an-opted-in-user-deletes-and-then-redownloads-my-app}

Suponha que um usuário faça opt-in para push, receba algumas notificações por push e depois exclua o app. Isso removerá o consentimento de push no nível do dispositivo. A partir daqui, o primeiro push com bounce após a desinstalação resultará automaticamente no opt-out desse usuário de futuras notificações por push. Depois disso, se o usuário reinstalar o app mas não abri-lo, a Braze não conseguirá enviar um push para o usuário porque os tokens por push não foram concedidos novamente para o seu app.

Além disso, se um usuário reativar o push em primeiro plano, seria necessário o início de uma sessão para atualizar essa informação no perfil do usuário e começar a receber notificações por push.

### Quando os tokens por push expiram? {#push-token-expire}

Infelizmente, APNs e FCM não definem isso de forma clara. Os tokens por push podem expirar quando um app é atualizado, quando os usuários transferem seus dados para um novo dispositivo ou quando reinstalam um sistema operacional. Na maioria dos casos, não temos realmente visibilidade sobre por que os provedores de push expiram determinados tokens por push.

Para lidar com essa ambiguidade, nossas integrações de push do SDK sempre registram e enviam os tokens no início da sessão para garantir que tenhamos o token mais atualizado.