---
nav_title: Rastreamento de desinstalação
article_title: Rastreamento de desinstalação para iOS
platform: iOS
page_order: 7
description: "Este artigo aborda como configurar o rastreamento de desinstalação para seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Rastreamento de desinstalação para iOS {#uninstall-tracking-for-ios}

> Este artigo aborda como configurar o rastreamento de desinstalação para seu aplicativo iOS e como testar para que seu app não execute nenhuma ação automática indesejada ao receber um push de rastreamento de desinstalação da Braze.

O rastreamento de desinstalação utiliza notificações por push em segundo plano com um sinalizador da Braze na carga útil. Para saber mais, consulte o [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) em nosso guia do usuário.

## Etapa 1: Ativando push em segundo plano {#step-1-enabling-background-push}

Certifique-se de que você ativou a opção **Remote notifications** na seção **Background Modes** da guia **Capabilities** do seu projeto Xcode. Consulte nossa documentação sobre [notificações por push silenciosas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications) para mais detalhes.

## Etapa 2: Verificando o push em segundo plano da Braze {#step-2-checking-for-braze-background-push}

A Braze usa notificações por push em segundo plano para coletar análises de rastreamento de desinstalação. Certifique-se de que seu aplicativo [não execute nenhuma ação indesejada]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push) ao receber nossas notificações de rastreamento de desinstalação.

## Etapa 3: Testar a partir do dashboard {#step-3-test-from-the-dashboard}

Em seguida, envie uma notificação por push de teste para você mesmo a partir do dashboard. Esse push de teste não atualizará seu perfil de usuário.

1. Na página **Campaigns**, crie uma campanha de notificação por push e selecione **iOS push** como sua plataforma.<br><br>
2. Na página **Configurações**, adicione a chave `appboy_uninstall_tracking` com o valor correspondente `true` e marque **Add Content-Available Flag**.<br><br>
3. Use a página **Prévia** para enviar a si mesmo um push de teste de rastreamento de desinstalação.<br><br>
4. Verifique se o seu app não executa nenhuma ação automática indesejada ao receber o push.

{% alert important %}
Essas etapas de teste são um substituto para o envio de um push de rastreamento de desinstalação da Braze. Se você tiver contagens de emblemas ativadas, um número de emblema será enviado junto com o push de teste, mas os pushes de rastreamento de desinstalação da Braze não definirão um número de emblema no seu aplicativo.
{% endalert %}

## Etapa 4: Ativar o rastreamento de desinstalação {#step-4-enable-uninstall-tracking}

Siga as instruções para [ativar o rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).