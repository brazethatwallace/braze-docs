---
nav_title: Mensagens no app de push primer
article_title: Mensagens no app de push primer
page_order: 1
page_type: reference
description: "Este artigo aborda os pré-requisitos para mensagens no app de push primer e como configurá-las."
channel: push

---

# Mensagens no app de push primer {#push-primer-in-app-messages}

> Você tem apenas uma chance de pedir permissão de push aos usuários, então otimizar o registro de push é crucial para maximizar o alcance das suas notificações por push. Use mensagens no app para explicar que tipo de mensagens seus usuários podem esperar receber caso optem por aceitar, antes de mostrar o prompt nativo de push. Isso é chamado de push primer.

![Mensagem no app de push primer para app de streaming. A notificação diz "Receber notificações por push do Movie Cannon? As notificações podem incluir novos filmes, séries de TV ou outros avisos e podem ser desativadas a qualquer momento."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

Para criar uma mensagem no app de push primer na Braze, você pode usar o comportamento ao clicar do botão "Solicitar permissão de push" ao criar uma mensagem no app para iOS, Android ou Web.

## Pré-requisitos {#prerequisites}

Este recurso requer [comportamento ao clicar do botão](#button-actions), que é compatível com as seguintes versões mínimas ou posteriores:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Além disso, observe os seguintes detalhes específicos de cada plataforma:

{% tabs local %}
{% tab android %}
| Versão do SO | Informações adicionais |
|----------|----------------------|
| **Android 12 e anteriores** | A implementação de push primers não é recomendada porque o push é aceito por padrão. |
| **Android 13+** | Se um usuário negar o prompt de permissão de push duas vezes, o Android bloqueia prompts adicionais — incluindo mensagens de push primer da Braze. Para conceder permissão após isso, os usuários devem ativar manualmente o push para o seu app nas configurações do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }
{% endtab %}

{% tab swift %}
### Informações gerais {#general-information}

- O prompt de push pode ser exibido apenas uma vez por instalação, imposto pelo sistema operacional.
- O prompt não é exibido se a configuração de push do app estiver explicitamente ativada ou desativada. Ele só é exibido para usuários com [autorização provisória](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **Configuração de push do app ativada:** a Braze não exibe a mensagem no app, pois o usuário já aceitou.
  - **Configuração de push do app desativada:** você precisa redirecionar o usuário para as configurações de notificação por push do app dentro das configurações do dispositivo.
- **Reteste após recusa:** Se um usuário recusar o prompt nativo, o iOS não o exibirá novamente para aquela instalação do app. Para retestar o fluxo de push primer, os usuários geralmente precisam desinstalar e reinstalar o app, ou alterar a permissão de notificação para o seu app em **Configurações**.

### Remoção manual de código {#manual-code-removal}

A mensagem no app que você configurou usando este tutorial chama o código nativo de prompt de push automaticamente quando um usuário clica no botão da mensagem no app. Para evitar solicitar permissão de notificação por push duas vezes, ou no momento errado, um desenvolvedor deve modificar qualquer integração de notificação por push existente que tenha implementado para garantir que sua mensagem no app seja o primeiro push primer que seus usuários veem.

Sua equipe de desenvolvimento deve revisar a implementação de notificações por push do seu app ou site e remover manualmente qualquer código que solicite permissão de push. Por exemplo, remova referências ao seguinte código:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Etapa 1: Criar uma mensagem no app {#step-1-create-an-in-app-message}

Primeiro, [crie uma mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) e selecione o tipo e a disposição da mensagem.

Para garantir que você tenha espaço suficiente para a mensagem e os botões, use uma disposição de mensagem em tela cheia ou modal. Se você escolher tela cheia, observe que uma imagem é obrigatória.

## Etapa 2: Construir sua mensagem {#step-2-build-your-message}

Agora é hora de adicionar seu texto! Lembre-se de que um push primer deve preparar o usuário para ativar as notificações por push. No corpo da mensagem, sugerimos destacar os motivos pelos quais seus usuários devem ter as notificações por push ativadas. Seja específico sobre o tipo de notificações que você deseja enviar e o valor que elas podem oferecer.

Por exemplo, um app de notícias pode usar o seguinte push primer:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Enquanto um app de streaming pode usar o seguinte:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Para práticas recomendadas e recursos adicionais, consulte [Criando prompts de opt-in personalizados]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Etapa 3: Especificar o comportamento dos botões {#button-actions}

Para adicionar botões à sua mensagem no app, arraste dois blocos de **Botão** para a mensagem, que funcionam como os botões primário e secundário na sua mensagem no app. Você também pode arrastar uma linha para a mensagem e depois arrastar os botões para dentro da linha, para que os botões fiquem na mesma linha horizontal (em vez de empilhados um sobre o outro). Recomendamos "Permitir notificações" e "Agora não" como botões iniciais, mas há muitos prompts de botão diferentes que você pode atribuir.

Depois de adicionar o texto dos botões, especifique o comportamento ao clicar de cada botão:

- **Botão 1:** Defina como "Fechar mensagem". Este é o botão secundário, ou a opção "Agora não".
- **Botão 2:** Defina como "Solicitar permissão de push". Este é o botão primário, ou a opção "Permitir notificações".

![Criador de mensagens no app com dois botões: "Permitir notificações" e "Agora não".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Etapa 4: Programar a entrega {#step-4-schedule-delivery}

Para configurar o envio do push primer em um momento relevante, você deve programar sua mensagem no app como uma mensagem baseada em ação com **Executar evento personalizado** como ação-gatilho.

Embora o momento ideal varie, a Braze sugere esperar até que o usuário conclua algum tipo de [ação de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), indicando que ele está começando a ver valor no seu app ou site, ou quando há uma necessidade convincente que as notificações por push podem atender (como depois de fazer um pedido e você querer oferecer informações de rastreamento de envio). Dessa forma, o prompt é benéfico para o cliente e não apenas para a sua marca.

![Configurações de entrega baseada em ação para enviar a usuários que realizaram o evento personalizado "Adicionar à lista de favoritos".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Etapa 5: Direcionar usuários {#step-5-target-users}

O objetivo de uma Campaign de push primer é solicitar aos usuários em qualquer dispositivo onde eles ainda não concederam permissões de push. Isso pode incluir usuários novos ou usuários existentes que adquiriram um novo dispositivo ou reinstalaram seu aplicativo.

{% alert important %}
**Supressão automática com push primer sem código**: Se você usar o push primer sem código (a ação de botão "Solicitar permissão de push"), não é necessário adicionar filtros de inscrição de push à sua segmentação. O SDK suprime automaticamente a mensagem no app em dispositivos que já possuem um token de push ativo, independentemente do status de push do usuário em outros dispositivos. Para saber mais sobre o direcionamento de usuários com múltiplos dispositivos, consulte [Direcionamento de usuários com múltiplos dispositivos](#targeting-users-with-multiple-devices).
{% endalert %}

Se você não estiver usando o push primer sem código, adicione um filtro onde `Foreground Push Enabled For App is false`. Este filtro identifica instalações individuais de app que ainda não aceitaram notificações por push em primeiro plano.

{% alert important %}
Usar um filtro em nível de usuário como `Push Subscription Status is not Opted In` exclui usuários que já aceitaram em outro dispositivo, impedindo-os de receber o prompt no novo dispositivo.
{% endalert %}

Além disso, você pode decidir quais segmentos adicionais considera mais apropriados. Por exemplo, você pode direcionar usuários que concluíram uma segunda compra, usuários que acabaram de criar uma conta para se tornarem membros, ou até mesmo usuários que visitam seu app mais de duas vezes por semana. Direcionar usuários para esses segmentos cruciais aumenta a probabilidade de os usuários aceitarem e se tornarem habilitados para push.

### Direcionamento de usuários com múltiplos dispositivos {#targeting-users-with-multiple-devices}

Como a Braze captura dados de usuários no nível do perfil e não no nível do dispositivo, direcionar usuários que possuem múltiplos dispositivos pode ser desafiador. Os filtros de inscrição de push na segmentação incluem ou excluem usuários com base no estado de inscrição de um único dispositivo, e não no estado de inscrição do dispositivo específico direcionado. Além disso, os estados provisórios no iOS adicionam complexidade, pois esses dispositivos tecnicamente possuem tokens de push em primeiro plano, mas os usuários não aceitaram explicitamente.

#### O problema com filtros de inscrição de push {#the-problem-with-push-subscription-filters}

Quando um usuário tem múltiplos dispositivos com diferentes estados de inscrição de push, os filtros de inscrição de push na sua segmentação podem falhar ao direcionar alguns dispositivos. Considere estes cenários:

{% details Cenário 1: Usuário tem dois dispositivos em plataformas diferentes %}

**O usuário tem dois dispositivos:**
- Dispositivo A: Android, aceitou push
- Dispositivo B: iOS, não aceitou push

**Filtros de segmento que não funcionam:**
- `Push enabled = false` - O usuário está habilitado para push no dispositivo Android, então ele não entra no segmento. O segmento não inclui o dispositivo iOS.
- `Push subscription status is not opted in` - O usuário está habilitado para push no dispositivo Android, então ele não entra no segmento. O segmento não inclui o dispositivo iOS.

**Filtros de segmento que funcionam:**
- `Push enabled for iOS = false` - O usuário está habilitado para push no dispositivo Android, mas estamos direcionando apenas dispositivos iOS, então o usuário entra no segmento. O segmento inclui o dispositivo iOS.

{% enddetails %}

{% details Cenário 2: Usuário tem dois dispositivos iOS com estados diferentes %}

**O usuário tem dois dispositivos iOS:**
- Dispositivo A: Aceitou push
- Dispositivo B: Provisoriamente habilitado, mas não aceitou

**Filtros de segmento que não funcionam:**
- `Push enabled = false` - O Dispositivo A aceitou push, então o usuário não entra no segmento. O segmento não inclui o Dispositivo B.
- `Provisionally opted in = true` - O Dispositivo A aceitou completamente, o que significa que não está em estado provisório. O usuário não entra no segmento. O segmento não inclui o Dispositivo B.
- `Push enabled for app > iOS = false` - O Dispositivo A aceitou push no iOS, então o usuário não entra no segmento. O segmento não inclui o Dispositivo B.
- `Push subscription status is not opted in` - O Dispositivo A aceitou push, então o usuário não entra no segmento. O segmento não inclui o Dispositivo B.

**Resultado:** Usar qualquer combinação desses filtros de push resulta na exclusão de pelo menos um dispositivo do segmento.

{% enddetails %}

{% details Cenário 3: Usuário tem três ou mais dispositivos no mesmo SO %}

**O usuário tem três dispositivos:**
- Dispositivo A: Aceitou push
- Dispositivo B: Não aceitou push
- Dispositivo C: Não aceitou push

**Filtros de segmento que não funcionam:**
- `Push enabled = false` - O Dispositivo A aceitou push, então o usuário não entra no segmento. O segmento não inclui os Dispositivos B e C.
- `Push enabled for app > X = false` - O Dispositivo A aceitou push no app especificado, então o usuário não entra no segmento. O segmento não inclui os Dispositivos B e C.
- `Push subscription status is not opted in` - O Dispositivo A aceitou push, então o usuário não entra no segmento. O segmento não inclui os Dispositivos B e C.

**Resultado:** Usar qualquer combinação desses filtros de push deixa pelo menos um dispositivo sem direcionamento.

{% enddetails %}

#### Solução: Use o push primer sem código {#solution-use-the-no-code-push-primer}

A solução recomendada é usar o push primer sem código (a ação de botão "Solicitar permissão de push") sem filtros adicionais de status de push na segmentação.

{% alert important %}
**Supressão automática**: O push primer sem código suprime automaticamente em dispositivos que já possuem um token de push ativo. O SDK verifica se um usuário no dispositivo específico já possui um token de push. Se o SDK detectar que o usuário já aceitou (por exemplo, de uma solicitação anterior ou pelas configurações do dispositivo), o SDK suprime automaticamente a mensagem no app sem a necessidade de filtros de segmentação adicionais. O primer é exibido em todos os outros cenários, inclusive se um usuário estiver provisoriamente aceito para push.
{% endalert %}

O benefício de usar o push primer sem código é que a funcionalidade é suportada pelo SDK da Braze. Como o SDK pode detectar o status do token de push no dispositivo específico que exibe a mensagem, você não precisa depender de filtros de segmentação em nível de perfil que podem excluir usuários com múltiplos dispositivos.

#### Considerações {#considerations}

**Push primer sem código obrigatório**: Você deve usar o push primer sem código para que a supressão automática funcione. Se você configurar lógica personalizada ou deep links em vez de usar a ação de botão "Solicitar permissão de push", o SDK não consegue identificar que você está tentando exibir um push primer. Isso resulta na exibição da mensagem independentemente do estado de inscrição daquele dispositivo.

**Supressão para usuários que recusaram**: Você pode querer suprimir a mensagem no app para usuários que recusaram explicitamente o push (por exemplo, a partir da solicitação nativa ou das configurações do dispositivo) e redirecionar esses usuários com uma Campaign de nutrição separada. Para isso, use a seguinte lógica Liquid em combinação com o primer sem código:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %}
{% abort_message('user turned off push notifications') %}
{% endif %}
- message goes here -
```
{% endraw %}

O filtro Liquid `targeted_device` analisa apenas o dispositivo onde a mensagem está sendo exibida, e não o perfil do usuário. Nesse dispositivo, `foreground_push_enabled` é definido como `true` quando há um token de push em primeiro plano ativo e como `false` quando o sistema operacional informa que as notificações por push foram desativadas (por exemplo, o usuário as desativou explicitamente). Para dispositivos completamente novos que ainda não responderam a um estado de permissão de push, `foreground_push_enabled` não está definido e não possui valor. Como a condição Liquid verifica especificamente {% raw %}`false`{% endraw %}, ela suprime o primer apenas para dispositivos com uma recusa explícita, enquanto dispositivos nesse estado desconhecido ainda se qualificam e podem receber o push primer.

## Etapa 6: Eventos de conversão {#step-6-conversion-events}

A Braze sugere configurações padrão para conversões, mas você pode querer configurar [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) relacionados a push primers.