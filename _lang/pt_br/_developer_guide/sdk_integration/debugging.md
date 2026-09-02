---
page_order: 1.3
nav_title: Depuração
article_title: Depuração do SDK da Braze
description: "Saiba como usar o depurador do SDK da Braze para solucionar problemas em seus canais com SDK, sem ativar o registro detalhado em seu app."
---

# Depuração do SDK da Braze {#debugging-the-braze-sdk}

> Saiba como usar o depurador integrado do SDK da Braze para solucionar problemas em seus canais com SDK, sem precisar ativar o registro detalhado em seu app.

{% alert tip %}
Para uma investigação mais aprofundada, você também pode [ativar o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) para capturar a saída detalhada do SDK e [aprender a ler logs detalhados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) para canais específicos.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar o depurador do SDK da Braze, você precisará das permissões "View IPI" e "View User Profiles (IPI Redacted)". Para baixar os logs da sua sessão de depuração, você também precisará da permissão "Export User Data". Além disso, seu SDK da Braze precisa atender ou apontar para as seguintes versões mínimas:

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

Para coletar logs do depurador quando `Braze.configuration.logger.level` estiver definido como `.disabled`, use o Swift SDK 11.9.0 ou posterior. Para saber mais, consulte os [changelogs do Swift]({{site.baseurl}}/developer_guide/changelogs#swift_fixed-12).

## Depurando o SDK da Braze

{% alert tip %}
Para ativar a depuração do SDK da Braze para web, você pode [usar um parâmetro de URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#logging).
{% endalert %}

### Etapa 1: Feche o app {#step-1-close-your-app}

Antes de iniciar a sessão de depuração, feche o app que está apresentando problemas. Você poderá reabrir o app no início da sessão.

### Etapa 2: Crie uma sessão de depuração {#step-2-create-a-debugging-session}

Na Braze, acesse **Configurações** e, em **Configuração e teste**, selecione **SDK Debugger**.

![A seção "Configuração e teste" com "SDK Debugger" destacado.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Selecione **Criar sessão de depuração**.

![A página do "SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Etapa 3: Selecione um usuário {#step-3-select-a-user}

Pesquise um usuário pelo endereço de e-mail, `external_id`, alias de usuário ou token por push. Quando estiver pronto para iniciar a sessão, selecione **Selecionar usuário**.

![A página de depuração do usuário selecionado.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Etapa 4: Reabra o app {#step-4-relaunch-the-app}

Primeiro, abra o app e confirme que o dispositivo está pareado. Se o pareamento for bem-sucedido, reabra o app — isso garantirá que os logs de inicialização do app sejam totalmente capturados.

### Etapa 5: Reproduza as etapas do problema {#step-5-complete-the-reproduction-steps}

Depois de reabrir o app, siga as etapas para reproduzir o erro.

{% alert tip %}
Ao reproduzir o erro, siga as etapas de reprodução o mais fielmente possível para criar [logs de qualidade](#step-6-export-your-session-logs-optional).
{% endalert %}

### Etapa 6: Encerre a sessão {#step-6-end-your-session}

Quando terminar as etapas de reprodução, selecione **Encerrar sessão** > **Fechar**.

![A sessão de depuração mostrando o botão "Encerrar sessão".]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Pode levar alguns minutos para gerar os logs, dependendo da duração da sessão e da conectividade de rede.
{% endalert %}

### Etapa 7: Compartilhe ou exporte a sessão (opcional) {#step-7-share-or-export-your-session-optional}

Após a sessão, você pode exportar os logs como um arquivo CSV. Além disso, outras pessoas podem usar o **ID da sessão** para pesquisar sua sessão de depuração, dispensando o envio direto dos logs.

![A página de depuração com "Exportar logs" e "Copiar ID da sessão" exibidos após a sessão.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})