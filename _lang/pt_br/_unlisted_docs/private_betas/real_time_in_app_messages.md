---
nav_title: Entrega de mensagens no app em tempo real
article_title: Entrega de mensagens no app em tempo real
permalink: "/real_time_in_app_messages/"
description: "Esta página cobre o acesso antecipado da entrega de mensagens no app em tempo real, que entrega mensagens no app a um dispositivo assim que o usuário se torna elegível, em vez de esperar pelo próximo início de sessão."
page_type: reference
hidden: true
noindex: true
---

# Entrega de mensagens no app em tempo real {#real-time-in-app-message-delivery}

> Com a entrega em tempo real, a Braze envia uma mensagem no app para o dispositivo assim que o usuário se torna elegível para recebê-la. Os usuários não precisam mais iniciar uma nova sessão para receber uma mensagem no app para a qual se tornaram elegíveis no meio de uma sessão.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Real-time in-app message delivery' type='early_access' %}

## Como funciona {#how-it-works}

Sem a entrega em tempo real, o SDK or kit de desenvolvimento de software solicita as mensagens no app elegíveis no início da sessão e as armazena em cache no dispositivo. Um usuário que se torna elegível durante uma sessão não recebe a mensagem até o início da próxima sessão. Para saber mais sobre esse comportamento, consulte [Disparar mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).

Com a entrega em tempo real, a Braze envia a mensagem ao dispositivo por meio de uma conexão ativa que o SDK or kit de desenvolvimento de software mantém durante a sessão. A Braze envia uma mensagem em dois casos:

- Um usuário se torna elegível para uma Campaign de mensagem no app.
- Um usuário avança para uma etapa de mensagem no app em um Canvas.

A entrega em tempo real altera quando a mensagem chega ao dispositivo. O comportamento de exibição permanece o mesmo: a mensagem aguarda seu evento-gatilho antes de aparecer.

### O que isso significa para suas campanhas {#what-this-means-for-your-campaigns}

| Cenário | Sem entrega em tempo real | Com entrega em tempo real |
| --- | --- | --- |
| Um usuário se torna elegível para uma Campaign de mensagem no app no meio da sessão | A mensagem chega no próximo início de sessão | A mensagem chega durante a sessão atual |
| Um usuário alcança uma etapa de mensagem no app em um Canvas no meio da sessão | A mensagem chega no próximo início de sessão | A mensagem chega durante a sessão atual |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comparação de entrega de mensagens no app em tempo real" }

## Requisitos de SDK or kit de desenvolvimento de software {#sdk-requirements}

A entrega em tempo real requer as seguintes versões mínimas de SDK or kit de desenvolvimento de software:

{% sdk_min_versions swift:18.0.0 android:43.1.1 %}

Os dispositivos continuam recebendo mensagens no app no início da sessão, independentemente da versão do SDK or kit de desenvolvimento de software.

## Limitações atuais {#current-limitations}

- **O SDK or kit de desenvolvimento de software para web ainda não é compatível:** a entrega em tempo real está disponível para os SDKs Swift e Android durante o acesso antecipado.
- **Edições em uma campanha ativa são aplicadas no próximo início de sessão:** se você alterar uma mensagem no app que um dispositivo já recebeu, esse dispositivo mantém a versão que possui até o próximo início de sessão do usuário.

## Participar do acesso antecipado {#participate-in-early-access}

1. Entre em contato com o gerente de conta da Braze para que seu espaço de trabalho seja adicionado ao acesso antecipado.
2. Atualize seu app para a versão mínima do SDK or kit de desenvolvimento de software da sua plataforma.
3. Publique o app atualizado para seus usuários.

A entrega em tempo real não requer configuração no dashboard, alterações em Campaigns nem mudanças no código do SDK or kit de desenvolvimento de software. Depois que seu espaço de trabalho for adicionado ao acesso antecipado, a entrega em tempo real será aplicada às suas Campaigns de mensagens no app e Canvas existentes.

## Compartilhe feedback {#share-feedback}

A Braze está desenvolvendo ativamente esse recurso, e seu feedback influencia o que será disponibilizado na versão geral. Envie ao seu gerente de conta suas observações sobre o tempo de entrega, qualquer comportamento diferente do esperado e os cenários que você gostaria que a entrega em tempo real cobrisse a seguir.