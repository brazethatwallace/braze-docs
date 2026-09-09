---
nav_title: Solução de problemas
article_title: Solução de problemas de push
page_order: 5
page_type: reference
description: "Diagnostique problemas de entrega de push, comportamento ao clicar e credenciais usando um índice de sintomas e um caminho de investigação padrão."
channel: push
---

# Solução de problemas de push {#troubleshoot-push}

> Use esta página para solucionar problemas de entrega de push, comportamento ao clicar e credenciais. Para configuração específica do SDK, consulte [Solução de problemas de notificações por push para o SDK da Braze]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting). Para códigos de erro, consulte [Mensagens de erro comuns de push]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

| Sintoma | Acesse |
| --- | --- |
| O usuário não recebeu uma notificação por push | [Notificações por push ausentes](#missing-push-notifications) |
| As notificações por push chegam com atraso | [Notificações por push atrasadas](#delayed-push-notifications) |
| Os envios de push estão mais lentos do que o esperado | [As notificações por push estão sendo enviadas mais lentamente do que o esperado](#push-notifications-are-sending-slower-than-expected) |
| Erro `MismatchSenderID` (Android) | [Erro: MismatchSenderID](#error-mismatch-sender-id) |
| Tocar em uma notificação por push não abre o app | [Clicar em uma notificação por push não abre o app](#clicking-a-push-notification-does-not-open-the-app) |
| Links de push abrem no app em vez do navegador | [Cliques em push abrem inesperadamente no app](#push-clicks-unexpectedly-open-in-app) |
| Problemas de permissão ou entrega de web push | [As notificações web push não estão funcionando como esperado](#web-push-notifications-are-not-behaving-as-expected) |
| Precisa migrar de `.p12` para `.p8` (iOS) | [Migrar para uma chave de autenticação .p8](#migrate-to-a-p8-authentication-key) |
| Código de erro de push específico nos logs | [Mensagens de erro de push](#push-error-messages) |
| Contagens de desinstalação não correspondem por plataforma | [Métricas de desinstalação](#uninstall-metrics) |
| Migração de usuários ou dados de push para outro espaço de trabalho | [Migração de dados do espaço de trabalho](#workspace-data-migration) |
| Precisa saber se uma sessão foi iniciada a partir de uma abertura de push | [Sessão e atribuição](#session-and-attribution) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de push" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho quando um usuário ou dispositivo de teste não recebeu uma notificação por push. Comece pela etapa 1.

1. Confirme que o usuário está inscrito ou optou por receber push e possui um token por push válido na guia **Engajamento** do perfil.
2. Confirme que o usuário está no público-alvo da Campaign ou do Canvas no momento do envio (os Segments são atualizados em tempo real).
3. Verifique os limites de frequência globais, os limites de taxa e a atribuição ao grupo de controle da Campaign ou do Canvas.
4. Confirme que você está usando o tipo correto de push para o dispositivo (por exemplo, Android, iOS ou Kindle).
5. Para testes internos, confirme que o testador está conectado ao app correto no dispositivo.
6. Se a entrega ainda falhar, consulte [Mensagens de erro comuns de push]({{site.baseurl}}/user_guide/channels/push/push_error_codes) ou entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) informando o ID da Campaign ou do Canvas, o ID do usuário e o registro de data/hora com fuso horário.

## Notificações por push ausentes {#missing-push-notifications}

**Sintoma:** Um usuário não recebeu uma notificação por push esperada.

Se as notificações por push não estão chegando como esperado, verifique os seguintes itens:

- [Status da inscrição para push](#push-subscription-status)
- [Segment](#segment)
- [Limites de notificações por push](#push-notification-caps)
- [Limites de frequência](#rate-limits)
- [Status do grupo de controle](#control-group-status)
- [Token por push válido](#valid-push-token)
- [Tipo de notificação por push](#push-notification-type)
- [App atual](#current-app)

### Status da inscrição para push {#push-subscription-status}

Pushes só podem ser enviados para usuários inscritos ou que optaram por receber. No **Perfil de usuário**, abra a guia [Engajamento]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) e confirme que você está ativamente registrado para push no espaço de trabalho que está testando. Se você estiver registrado em vários apps, eles serão listados em **Push Registered For**:

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

Você também pode exportar perfis de usuário usando os endpoints de exportação da Braze:

- [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Usuários por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Ambos os endpoints retornam um objeto de token por push que inclui informações de ativação de push por dispositivo.

### Segment {#segment}

Confirme que você faz parte do Segment que está sendo direcionado (se for uma campanha ativa e não um teste). No **Perfil de usuário**, você pode ver em quais segmentos o usuário está atualmente incluído. A associação ao Segment é atualizada em tempo real.

![Lista de Segments]({% image_buster /assets/img_archive/trouble2.png %})

Você também pode confirmar que o usuário faz parte do Segment usando a **Pesquisa de usuário** ao criar um Segment. A **Pesquisa de usuário** aceita apenas `external_id` ou `braze_id` — não endereços de e-mail ou números de telefone. Para pesquisar por e-mail, telefone, token por push ou alias de usuário, consulte [**Pesquisar usuários**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

![Seção de pesquisa de usuário com um campo de busca.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### Limites de notificações por push {#push-notification-caps}

Verifique os limites de frequência globais. É possível que você não tenha recebido a notificação por push porque seu espaço de trabalho possui limite de frequência global ativo e você já atingiu o limite de notificações por push para o período especificado.

Na página **Analytics** da Campaign, verifique se há um banner de limite de frequência mostrando aproximadamente quantos usuários não receberam a Campaign nos últimos 30 dias. Para investigar envios individuais, use o [dashboard de Diagnóstico de mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) e filtre por **Frequency capped**. Para revisar ou alterar as regras, consulte [limite de frequência global]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over).

![Detalhes da Campaign]({% image_buster /assets/img_archive/trouble3.png %})

### Limites de frequência {#rate-limits}

Se você tiver um limite de frequência definido para sua Campaign ou Canvas, pode estar deixando de receber mensagens por ter excedido esse limite. Para saber mais, consulte [Limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting).

### Status do grupo de controle {#control-group-status}

Se for uma Campaign de canal único ou um Canvas com grupo de controle, é possível que você esteja no grupo de controle.

  1. Verifique a [distribuição de variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-4-choose-a-segment-and-distribute-your-users-across-variants) para ver se há um grupo de controle.
  2. Se houver, crie um Segment filtrando por [no grupo de controle da Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group) e depois [exporte o Segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details) e verifique se o ID do seu usuário está nessa lista.

### Token por push válido {#valid-push-token}

Um token por push é um identificador que os remetentes usam para direcionar um dispositivo específico com uma notificação por push. Sem um token por push válido, a Braze não consegue enviar um push para esse dispositivo.

A Braze armazena até 20 dispositivos por perfil de usuário. Quando um 21º dispositivo é registrado, o dispositivo mais antigo é removido (primeiro a entrar, primeiro a sair, ou FIFO). Chamar [`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids) no SDK registra novamente o dispositivo atual no perfil.

### Tipo de notificação por push {#push-notification-type}

Use o tipo de push que corresponde ao dispositivo ou plataforma que você está direcionando. Por exemplo, use uma notificação por push Kindle para Fire TV, não uma Campaign de push para Android. Para dispositivos Android, use uma notificação por push para Android em vez de uma Campaign de push para iOS.

Para fluxos de trabalho de solução de problemas específicos por plataforma, consulte:

- [Solução de problemas de notificações por push da Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Solução de problemas do Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

### App atual {#current-app}

Ao testar push com usuários internos, confirme que o destinatário pretendido está logado no app correto. Caso contrário, ele pode não receber o push ou pode receber um que você não esperava com base na segmentação.

{% alert note %}
Se você está enviando mensagens push com imagens no Android, o FCM pode, às vezes, descartar a imagem e exibir apenas o texto na mensagem push. Esse problema geralmente é causado por problemas de conectividade com o servidor.
{% endalert %}

## Erro: MismatchSenderID {#error-mismatch-sender-id}

**Sintoma:** O push para Android falha com um erro `MismatchSenderID`.

MismatchSenderID indica uma falha de autenticação com o Firebase Cloud Messaging (FCM). Confirme se o ID do remetente do Firebase e a chave de API do FCM estão corretos.

Para encontrar a chave de servidor correta do Firebase e substituí-la:

1. Acesse o console do Firebase do seu app.
2. Em **Project Overview**, selecione **Project Settings**.
3. Na guia **Cloud Messaging**, verifique se o ID do remetente listado com as chaves de API corresponde ao que está na Braze (em **Settings** > **App Settings** > **Cloud Messaging API Key**).

{% alert warning %}
Não altere o ID do remetente no seu dashboard da Braze. Fazer isso invalida os registros de push existentes. Se o ID do remetente não corresponder, você deve encontrar o projeto do Firebase com o ID do remetente correspondente.
{% endalert %}

4. Copie a **Server Key** em **Project credentials**.
5. Na Braze, acesse **Settings** > **App Settings**, selecione seu app e cole a chave do servidor no campo **Cloud Messaging API Key** (substituindo a chave desatualizada).
6. Selecione **Save**.
7. Para verificar, envie um push de teste para um dispositivo antes e depois de alterar a chave de API sem abrir o aplicativo. Isso ajuda a confirmar que os usuários continuam recebendo notificações por push sem a necessidade de gerar um novo ID de registro de push (token por push).

## Cenários de solução de problemas {#troubleshooting-scenarios}

### Notificações por push atrasadas {#delayed-push-notifications}

**Sintoma:** As notificações por push chegam mais tarde do que o esperado.

Suas notificações por push podem atrasar por estes motivos:

- Conexão de dados fraca no dispositivo
- Código personalizado no app que pode suprimir notificações por push da Braze
- Preferências do usuário para notificações por push nas configurações do dispositivo
- Prioridade da mensagem do push ao criar na Campaign ou no Canvas
- Atrasos de tráfego ou problemas com os provedores de serviço de push (FCM e APNs)

### Notificações por push estão sendo enviadas mais lentamente do que o esperado {#push-notifications-are-sending-slower-than-expected}

**Sintoma:** Os envios de push de Campaigns ou Canvas demoram mais do que o esperado para serem concluídos.

Confirme se a configuração das suas notificações por push segue estas práticas recomendadas:

- Se você está enviando para grandes públicos sem considerar o status de push ativado, isso pode levar a uma velocidade de envio mais lenta. Em vez disso, considere enviar apenas para usuários com push ativado para reduzir o tamanho do seu público.
- Se possível, tente agendar suas Campaigns com antecedência em vez de imediatamente.
- Se você está direcionando um número maior de usuários com notificações por push em um Canvas, pode esperar que as etapas de mensagem subsequentes no Canvas exijam tempos de processamento diferentes de uma Campaign que envia para os usuários imediatamente. Nesse caso, as Campaigns normalmente concluem o envio antes de um Canvas, já que a primeira "etapa" de um Canvas é verificar se os usuários se qualificam para a jornada de usuário específica.

## Clicar em uma notificação por push não abre o app {#clicking-a-push-notification-does-not-open-the-app}

**Sintoma:** Tocar em uma notificação por push não abre o app nem navega conforme configurado.

Se clicar em uma notificação por push não abre seu app, verifique o seguinte com base na sua plataforma.

### Android

1. **Verifique o comportamento ao clicar:** Confirme que a Campaign está configurada para abrir o app ao ser clicada.
2. **Verifique o tratamento de deep links:** No seu arquivo `braze.xml`, verifique se `com_braze_handle_push_deep_links_automatically` está definido como `true` ou `false`.
   - Se definido como `true`, o SDK da Braze trata os deep links diretamente e o app deve abrir conforme esperado.
   - Se definido como `false`, seu app precisa de um broadcast receiver para escutar e tratar os intents de push recebido e aberto. Verifique se esse receiver está implementado corretamente.
3. **Colete logs detalhados:** [Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduza o problema e forneça os logs junto com seus arquivos `braze.xml` e `AndroidManifest.xml` ao suporte da Braze.

### iOS

1. **Verifique o comportamento ao clicar:** Confirme que a Campaign está configurada para abrir o app ao ser clicada.
2. **Verifique a integração de push:** O deep linking de um push para o app é tratado automaticamente pela [integração padrão de push]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift) da Braze. Confirme que a integração está implementada corretamente, incluindo qualquer tratamento de delegate personalizado.
3. **Colete logs detalhados:** [Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduza o problema e forneça os logs ao suporte da Braze.

## Cliques em push abrem inesperadamente no app {#push-clicks-unexpectedly-open-in-app}

**Sintoma:** Links em notificações por push abrem dentro do app em vez do navegador de internet do dispositivo.

Se você está enfrentando problemas com links em notificações por push que abrem inesperadamente no seu app em vez do navegador de internet, pode haver um problema com a configuração da sua Campaign ou com a implementação do SDK. Consulte as etapas a seguir para obter ajuda.

### Verifique o comportamento ao clicar {#verify-on-click-behavior}

Na sua Campaign ou etapa do Canvas, verifique novamente se **Open web URL inside mobile app** não está selecionado. Se estiver, desmarque a seleção e relance.

A interação padrão para o comportamento ao clicar "Open web URL" difere por versão do SDK. Para as versões do SDK iOS 2.29.0 e Android 2.0.0 e superiores, essa opção é selecionada por padrão e as URLs da web são abertas em uma web view dentro do app. Antes dessas versões, essa opção é desmarcada por padrão e as URLs da web abrem no navegador de internet padrão do dispositivo.

Se esse não for o problema, pode haver um problema com sua implementação de push.

### Verifique novamente a integração de push {#double-check-push-integration}

Se os links nas suas notificações por push estão abrindo no app inesperadamente, isso pode ser devido a problemas com a integração ou configurações de personalização das notificações por push. Siga estas etapas para solucionar:

1. **Revise a implementação do delegate de push:** certifique-se de que o delegate de push da Braze está implementado corretamente. Para instruções detalhadas, consulte o guia de integração de notificações por push para sua [plataforma]({{site.baseurl}}/developer_guide/home).
2. **Inspecione o tratamento personalizado de links:** verifique se o app inclui tratamento personalizado para todos os links `https://`. Configurações personalizadas podem sobrescrever comportamentos padrão. Colabore com sua equipe de desenvolvimento para revisar e ajustar essas configurações, se necessário.
3. **Verifique o registro de push no iOS:** para iOS, revise a etapa 1 do guia de integração de push sobre [registrar notificações por push com APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). Certifique-se de que seu objeto delegate é atribuído de forma síncrona antes que o app termine de iniciar. Essa etapa deve ser concluída no método `application:didFinishLaunchingWithOptions:`.
4. **Teste sua integração:** após fazer os ajustes, teste o comportamento das notificações por push em dispositivos iOS e Android para confirmar que o problema foi resolvido.

### Deep links com o app ainda em execução em segundo plano (iOS) {#deep-links-with-app-still-running-in-the-background-ios}

Se os deep links funcionam quando o app não está em execução ou quando o link é usado diretamente, mas não quando o aplicativo já está em execução em segundo plano, o problema pode estar relacionado à forma como o app trata o link. Verifique se você está usando alguma biblioteca de terceiros que utiliza method swizzling. Recomendamos desativar o swizzling, pois ele pode causar problemas com implementações de deep link.

## Migrar para uma chave de autenticação .p8 {#migrate-to-a-p8-authentication-key}

**Sintoma:** Você precisa migrar as credenciais de push do iOS de um certificado legado para uma chave `.p8`, ou a entrega de push falhou após uma alteração de credencial.

As chaves de autenticação `.p8` da Apple são a abordagem obrigatória para push via APNs na Braze. Diferentemente dos tipos de arquivo de certificado legados, as chaves `.p8` não expiram e suportam todos os seus apps com uma única chave, eliminando a necessidade de renovações anuais de certificados e reduzindo o risco de falhas na entrega de push.

Se você está usando atualmente um certificado `.p12` ou `.pem`, migre para uma chave `.p8` o mais rápido possível. Para instruções sobre como criar e fazer upload de uma chave `.p8`, consulte [Fazer upload do seu certificado de push APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). Para orientações da Apple sobre como gerar uma chave `.p8` a partir da sua conta de desenvolvedor, consulte [Communicate with APNs using authentication tokens](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

### Chaves .p8 versus certificados .p12 {#p8-keys-versus-p12-certificates}

Use a tabela a seguir para comparar tipos de credenciais, expiração e como cada um aparece no dashboard.

| Credencial | Expiração | Indicador de status no dashboard |
| --- | --- | --- |
| Chave de autenticação `.p8` | Não expira | Sem indicador verde de status (isso é esperado) |
| Certificado de push `.p12` | Expira anualmente | Indicador verde quando o certificado é válido |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Chaves .p8 versus certificados .p12" }

Quando você substitui um certificado `.p12` por uma chave `.p8` (ou faz upload de uma nova credencial), a entrega de push pode pausar brevemente enquanto a Braze processa a alteração. Planeje atualizações durante uma janela de manutenção, quando possível.

Em **Configurações** > **Configurações do app** > **Configurações das notificações por push**, confirme que **App Bundle ID**, **Team ID** e **Key ID** (para chaves `.p8`) correspondem aos valores na sua conta de desenvolvedor da Apple. Vários espaços de trabalho da Braze podem usar a mesma credencial de push da Apple quando o **bundle ID** do app iOS é idêntico; o ambiente da credencial (desenvolvimento versus produção) deve corresponder à forma como o app foi compilado.

Apps com [Braze Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) ou posterior podem usar o [gerenciamento dinâmico de gateway APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management), que roteia tokens para o ambiente APNs correto automaticamente.

## As notificações por web push não estão funcionando como esperado {#web-push-notifications-are-not-behaving-as-expected}

**Sintoma:** As notificações por push do navegador não são exibidas ou as permissões do site parecem travadas.

Se você está enfrentando problemas com notificações por push no seu navegador, pode ser necessário redefinir as permissões de notificação do site e limpar o armazenamento do site. Siga as etapas abaixo para obter ajuda.

{% tabs %}
{% tab Chrome %}

### Redefinir o Chrome no desktop {#reset-chrome-on-desktop}

1. Ao lado da URL no navegador Chrome, selecione o ícone de controle deslizante **View Site Information**.
2. Em **Notifications**, selecione **Reset permission**.
3. Abra o Chrome DevTools. A seguir estão os atalhos relevantes por sistema operacional.

<style>
table {
    max-width: 50%;
}
</style>

| SO      | Atalhos de teclado                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redefinir o Chrome no desktop" }

{:start="4"}
4. No DevTools, navegue até a guia **Application**.
5. Na barra lateral, selecione **Storage**.
6. Selecione **Clear site data**.
7. O Chrome solicitará que você recarregue a página para aplicar as configurações atualizadas. Selecione **Reload**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e teste.

### Redefinir o Chrome no Android {#reset-chrome-on-android}

Se você tem uma notificação do seu site visível na gaveta de notificações do Android:

1. Na notificação por push, selecione <i class="fas fa-cog" title="Configurações"></i> **Configurações** e selecione **Configurações do site**.
2. Em **Configurações do site**, toque em **Limpar e redefinir**.

Se você não tem uma notificação do seu site aberta:

1. Abra o Chrome no Android.
2. Toque no menu <i class="fas fa-ellipsis-vertical"></i>.
3. Acesse **Configurações** > **Configurações do site** > **Notificações**.
4. Verifique se as notificações estão definidas como **Perguntar antes de enviar (recomendado)**.
5. Encontre seu site na lista.
6. Selecione a entrada e toque em **Limpar e redefinir**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e teste.

{% endtab %}
{% tab Firefox %}

### Redefinir o Firefox no desktop {#reset-firefox-on-desktop}

1. Ao lado da URL do seu site, selecione <i class="fa-solid fa-circle-info" alt="ícone de informação"></i> ou <i class="fas fa-lock" alt="ícone de cadeado"></i>.
2. Em **Permissões**, ao lado de **Receber notificações**, selecione <i class="fa-solid fa-circle-xmark" title="Limpar esta permissão e perguntar novamente"></i> **Limpar permissão** para limpar as permissões de notificação.
3. No mesmo menu, selecione **Limpar cookies e dados do site**.
4. Na caixa de diálogo para confirmar sua escolha, selecione **OK**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e teste.

### Redefinir o Firefox no Android {#reset-firefox-on-android}

Para redefinir as permissões de push no Android, consulte [Clear your browsing history and other personal data](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) no suporte da Mozilla.

{% endtab %}
{% tab Safari %}

### Redefinir o Safari no macOS {#reset-safari-on-macos}

{% alert note %}
Estas etapas são apenas para macOS, pois a Apple não oferece suporte a web push para Safari no Windows.
{% endalert %}

1. Abra o Safari.
2. Na [barra de menus do Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), acesse **Safari** > **Ajustes** > **Sites** > **Notificações**.
3. Selecione seu site na lista.
4. Selecione **Remover** para excluir as permissões de notificação do site.
5. Em seguida, acesse **Privacidade** > **Gerenciar dados de sites**.
6. Selecione seu site na lista.
7. Selecione **Remover** ou, para remover todos os dados do site, selecione **Remover tudo**.
8. Selecione **OK**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e teste.

{% endtab %}
{% endtabs %}

## Métricas de abertura de push {#push-open-metrics}

A Braze registra uma Abertura Direta quando um usuário toca na notificação e o app inicia uma sessão. Expandir uma notificação por push rich sem abrir o app não registra uma Abertura Direta.

Se um usuário abrir o app após receber um push sem tocar na notificação, a Braze pode registrar uma Abertura por Influência. Para definições e relatórios, consulte [Aberturas por Influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

## Mensagens de erro de push {#push-error-messages}

**Sintoma:** Você vê um código de erro de push específico (por exemplo, `DEVICE_UNREGISTERED`, `Unregistered` ou `NotRegistered`).

Para definições de códigos de erro comuns de push (incluindo `DEVICE_UNREGISTERED`, `NotRegistered` e `Unregistered`), consulte [Mensagens de erro comuns de push]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

Quando um provedor de push sinaliza que um token de registro não é mais válido (por exemplo, `DEVICE_UNREGISTERED` ou `NotRegistered` do FCM), a Braze remove o token por push afetado do perfil do usuário e conta o usuário como desinstalado. As campanhas de Uninstall Tracking usam a mesma lógica de remoção de token em escala.

Outros erros de push são registrados como bounces e não removem o token. Por exemplo, uma falha de autenticação como [`MismatchSenderID`](#error-mismatch-sender-id) significa que a Braze não conseguiu autenticar com o FCM, então corrija a credencial em vez de tratar o erro como um sinal de desinstalação.

Para o rastreamento de desinstalação no Android, a Braze envia pushes de detecção de desinstalação como dry run (somente validação) ou como push silencioso ativo, dependendo da configuração do seu espaço de trabalho. Como um dry run valida a solicitação sem entregar a mensagem, seus resultados podem diferir de um envio ativo. Se as contagens de desinstalação parecerem baixas, confirme se a sua integração Android atende aos pré-requisitos de [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) e revise os erros de bounce no Message Activity Log.

## Métricas de desinstalação {#uninstall-metrics}

### Por que o total de desinstalações não corresponde à soma de Android e iOS? {#why-dont-total-uninstalls-match-android-plus-ios}

O **Total de desinstalações** do espaço de trabalho pode exceder a soma das métricas de desinstalação específicas por plataforma porque a invalidação de tokens de web push também contribui para as contagens de desinstalação. Quando um token de web push se torna inválido (por exemplo, após o usuário limpar os dados do site ou revogar a permissão), a Braze pode registrar uma desinstalação para esse registro web, mesmo quando as métricas de desinstalação mobile permanecem inalteradas.

### Qual status de inscrição os tokens de push iOS importados exibem? {#what-subscription-status-do-imported-ios-push-tokens-show}

Os tokens de push iOS importados geralmente aparecem como **Subscribed** até que o usuário registre uma sessão em um app que usa o SDK da Braze para esse espaço de trabalho. Depois que o SDK registra o token no início da sessão, o perfil normalmente muda para **Opted-In** quando a autorização de push é concedida. Para saber mais sobre estados de inscrição e campos de perfil, consulte [Estados de inscrição de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

## Migração de dados do espaço de trabalho {#workspace-data-migration}

### Posso migrar dados entre espaços de trabalho? {#can-i-migrate-data-between-workspaces}

A Braze não oferece uma migração com um clique entre espaços de trabalho. Aponte seu app ou site para a chave de API do espaço de trabalho de destino e, em seguida, recrie os usuários nele com o endpoint [Users Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou a [importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import). Exporte os perfis de origem primeiro com [Exportar usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) ou [Exportar usuários por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

Para saber o que você pode copiar, o que precisa recriar e os limites de tokens por push, consulte [Migrar dados entre espaços de trabalho]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/migrate_workspace_data). Trabalhe com a equipe da sua conta Braze ao planejar uma grande mudança de espaço de trabalho.

## Sessão e atribuição {#session-and-attribution}

### Posso saber, a partir do início da sessão, se o usuário abriu o app por meio de um push? {#can-i-tell-from-session-start-whether-the-user-opened-the-app-from-a-push}

Não. Os eventos de início de sessão não incluem um indicador de que a sessão começou a partir de uma abertura de push. Use **Aberturas Diretas**, **Aberturas por Influência** ou eventos personalizados (por exemplo, registrando um handler de clique no seu app) para correlacionar sessões com engajamento de push. Consulte [Métricas de abertura de push](#push-open-metrics).