---
page_order: 10.9
nav_title: Solução de problemas
article_title: Solução de problemas de notificações por push para o SDK or kit de desenvolvimento de software da Braze
description: "Diagnostique problemas de entrega e exibição de notificações por push usando um índice de sintomas, caminho de investigação padrão e verificações específicas de plataforma do SDK or kit de desenvolvimento de software."
channel:
  - push notifications
---

# Solução de problemas de notificações por push {#troubleshoot-push-notifications}

> Use esta página para diagnosticar problemas de entrega e exibição de notificações por push em um dispositivo. Para verificações de entrega no dashboard (status de inscrição, Segments, limites), consulte [Solução de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Antes de depurar, adicione-se como [usuário teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) e revise [Envio de mensagens de teste]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

Encontre o comportamento que você está observando na tabela e siga as etapas da seção correspondente. Se não tiver certeza de qual seção se aplica, use o [caminho de investigação padrão](#standard-investigation-path).

| Sintoma | Acesse |
| --- | --- |
| Push não recebido em uma plataforma | Selecione a guia do seu SDK or kit de desenvolvimento de software em [Solução de problemas específicos por plataforma](#platform-specific-troubleshooting) |
| Quebras de linha ao redor de Liquid tags ficam incorretas ao salvar | [Quebras de linha em notificações por push](#push-linebreaks) |
| Verificações de entrega no dashboard (inscrição, Segment or segmento, limites) | [Solução de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| Deep link de push não abre corretamente | [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Códigos de erro comuns de push | [Mensagens de erro comuns de push]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de push do SDK or kit de desenvolvimento de software" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho para cada incidente de notificação por push. Comece pela etapa 1.

1. Confirme que o dispositivo possui um token por push válido e que a permissão de push está concedida nas configurações do dispositivo.
2. No dashboard, confirme que o usuário teste corresponde ao [Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) da Campaign ou do Canvas e não está no [grupo de controle]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status).
3. Envie um [push de teste]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) para o dispositivo de teste.
4. [Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduza o problema e revise as orientações específicas da plataforma na [guia do SDK or kit de desenvolvimento de software](#platform-specific-troubleshooting).
5. Se o problema persistir, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) informando os logs detalhados, a plataforma, a versão do SDK or kit de desenvolvimento de software e o ID da Campaign ou do Canvas.

## Cliques em push não registrados {#push-clicks-not-logged}

- Certifique-se de ter seguido as [etapas de integração de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling).
- A Braze não processa notificações por push recebidas silenciosamente em primeiro plano (comportamento padrão de push em primeiro plano antes do framework `UserNotifications`). Isso significa que os links não serão abertos e os cliques em push não serão registrados. Se seu aplicativo ainda não integrou o framework `UserNotifications`, a Braze não processará notificações por push quando o estado do aplicativo for `UIApplicationStateActive`. Certifique-se de que seu app não atrasa chamadas aos [métodos de processamento de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling); caso contrário, o SDK or kit de desenvolvimento de software Swift pode tratar as notificações por push como eventos silenciosos de push em primeiro plano e não processá-las.

## Quebras de linha em notificações por push {#push-linebreaks}

Ao redigir notificações por push com Liquid tags, as quebras de linha adjacentes às Liquid tags são automaticamente removidas antes do envio da mensagem. No [criador de notificações por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message), essas quebras de linha são adicionadas novamente para que sua mensagem permaneça legível durante a edição. Se você notar quebras de linha ao redor das Liquid tags ao salvar sua mensagem, esse é o comportamento esperado.