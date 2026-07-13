---
page_order: 22
nav_title: Melhores práticas
article_title: Melhores práticas de push
description: "Esta página contém melhores práticas e casos de uso de push para garantir que suas mensagens push inspirem engajamento em vez de incômodo."
channel: push
---

# Melhores práticas de push {#push-best-practices}

> Esta página contém melhores práticas e casos de uso de push para garantir que suas mensagens push inspirem engajamento em vez de incômodo.

As notificações por push são ferramentas poderosas para interagir com os usuários do seu app, mas devem ser usadas com cuidado para garantir que entreguem mensagens oportunas e relevantes. Antes de enviar sua mensagem push, consulte as melhores práticas a seguir para saber o que você deve conhecer e verificar.

{% alert important %}
Suas mensagens push devem estar em conformidade com as diretrizes da Apple App Store e das políticas da Google Play Store, especificamente no que diz respeito ao uso de mensagens push como anúncios, spam, promoções e outros. Nesta página, consulte [Regulamentações de mensagens push](#push-message-regulations).
{% endalert %}

## Redija sua mensagem push {#compose-your-push-message}

Como melhor prática, a Braze recomenda manter cada linha de texto, tanto para o título opcional quanto para o corpo da mensagem, em aproximadamente 30 a 40 caracteres em uma notificação por push para dispositivos móveis. O contador de caracteres no criador não contabiliza caracteres Liquid. Isso significa que a contagem final de caracteres de uma mensagem depende de como o Liquid é renderizado para cada usuário. Em caso de dúvida, seja breve e direto.

## Reduza o tamanho da carga útil da notificação por push {#reduce-push-notification-payload-size}

O tamanho máximo da carga útil depende da plataforma.

| Plataforma | Tamanho máximo da carga útil |
| --- | --- |
| Web | 3.807 bytes |
| Android | 3.930 bytes |
| iOS | 3.960 bytes |
| Kindle | 5.985 bytes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reduza o tamanho da carga útil da notificação por push" }

Se o seu push exceder o tamanho máximo da carga útil, a mensagem pode não ser enviada. Como melhor prática, mantenha sua carga útil em algumas centenas de bytes.

### O que é uma carga útil de push? {#what-is-a-push-payload}

Os provedores de serviço de push calculam se sua notificação por push pode ser exibida para um usuário verificando o tamanho em bytes de toda a carga útil do push. A carga útil é limitada a **4 KB (4.096 bytes)** para a maioria dos serviços de push, incluindo:

- Serviço de Notificações por Push da Apple (APNs)
- Firebase Cloud Messaging (FCM) do Android
- Push para a web
- Push da Huawei

Esses serviços de push rejeitarão qualquer notificação que exceda esse limite.

A Braze reserva uma parte da carga útil do push para fins de integração e análise de dados. Diante disso, nosso tamanho máximo de carga útil é de **3.807 bytes**. Se o seu push exceder esse tamanho, a mensagem pode não ser enviada. Como melhor prática, mantenha sua carga útil em algumas centenas de bytes.

Os seguintes elementos no seu push compõem a carga útil do push:

- Texto, como o título e o corpo da mensagem
- Renderização final de qualquer personalização com Liquid
- URLs de imagens (mas não o tamanho da imagem em si)
- URLs de destino de clique
- Nomes de botões
- Pares de chave-valor

### Dicas para reduzir o tamanho da carga útil {#tips-to-reduce-payload-size}

Para reduzir o tamanho da carga útil:

- Mantenha sua mensagem breve. Uma boa diretriz geral é torná-la acionável e útil em menos de 40 caracteres.
- Omita espaços em branco e quebras de linha do seu texto.
- Considere como o Liquid será renderizado no envio. Como a renderização final de qualquer personalização com Liquid varia de usuário para usuário, a Braze não consegue determinar se a carga útil de um push excederá o limite de tamanho quando o Liquid está incluído. Se o seu Liquid renderizar uma mensagem mais curta, pode não haver problema. No entanto, se o seu Liquid resultar em uma mensagem mais longa, seu push pode exceder o limite de tamanho da carga útil. Sempre teste sua mensagem push em um dispositivo real antes de enviá-la aos usuários.
- Considere encurtar URLs usando um encurtador de URL.

## Otimize o direcionamento {#optimize-targeting}

### Colete dados relevantes dos usuários {#collect-relevant-user-data}

As notificações por push devem ser tratadas com cuidado para direcionar os usuários com notificações oportunas e relevantes. A Braze coletará informações úteis sobre dispositivos e uso que podem ser usadas para direcionar segmentos relevantes. Essas informações devem ser complementadas com eventos personalizados e atributos específicos do seu app. Usando esses dados, você pode direcionar mensagens cuidadosamente para aumentar as taxas de abertura e diminuir os casos de usuários desativando o push.

### Crie uma página de configurações de notificação {#create-a-notification-settings-page}

Você pode criar uma página de configurações no seu app que permita aos usuários informar quais notificações desejam receber. Uma abordagem comum é criar um atributo personalizado booleano na Braze correspondente ao status da configuração do app. Por exemplo, um app de notícias pode ter configurações de inscrição para notícias de última hora, esportes ou política.

Quando o app de notícias deseja criar uma Campaign direcionada apenas a usuários interessados em política, ele adiciona o filtro de atributo `Subscribes to Politics` ao segmento. Quando definido como verdadeiro, apenas os usuários que se inscreveram para receber notificações as receberão.

Para saber mais sobre como definir atributos personalizados, consulte os seguintes artigos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes#setting-custom-attributes) ou [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data#user-attributes-object-specification).

## Aumente os opt-ins e a relevância {#increase-opt-ins-and-relevance}

### Obtenha a permissão do usuário {#obtain-user-permission}

As estatísticas gerais de push ativado estão relacionadas a se o usuário aprovou as notificações no sistema operacional. Se os usuários desativarem as notificações no iOS, eles serão automaticamente removidos do nosso sistema, pois a Apple não permitirá que o token por push seja enviado.

O Android 13 e versões superiores exigem a obtenção de permissão antes que as notificações por push possam ser exibidas. Versões mais antigas do Android inscrevem os usuários nas notificações por padrão.

### Prepare os usuários para o push {#prime-users-for-push}

Você tem apenas uma chance de pedir permissão de push a um usuário, e depois que ele recusa, é muito difícil convencê-lo a reativar o push nas configurações do dispositivo. Por esse motivo, você deve preparar os usuários para o push usando uma mensagem no app antes de exibir o prompt do sistema. Consulte [Mensagens no app de preparação para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para saber mais sobre como aumentar os opt-ins.

### Adicione controles de inscrição de push {#add-push-subscription-controls}

Para evitar que os usuários desativem as notificações no nível do dispositivo, o que remove completamente o token por push em primeiro plano, permita que os usuários controlem sua inscrição de push diretamente no seu app. Consulte [Atualizando estados de inscrição de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state) para mais informações.

### Use agendamento avançado ou adicione postergações {#use-advanced-scheduling-or-add-delays}

Dependendo do tamanho do seu público e de quanto tempo antes sua mensagem push está agendada, pode haver atrasos na entrega do push. O tempo necessário para enviar pushes depende do poder de processamento alocado. Por exemplo, se sua mensagem push usa várias chamadas de Conteúdo conectado, isso pode aumentar a complexidade da criação do template da mensagem push e resultar em velocidades limitadas pela rapidez com que as APIs de terceiros retornam dados.

Uma carga útil de push menor e uma prioridade de notificação mais alta podem ajudar a reduzir atrasos e escalar suas mensagens. Você pode adicionar `Push Enabled = true` no filtro de público para reduzir o tamanho do público, de modo que apenas usuários com push ativado sejam processados para o envio da Campaign.

Também recomendamos minimizar o número de chamadas de API otimizando os dados necessários. Se possível, tente obter todos os dados necessários em uma única chamada de API em vez de fazer várias chamadas.

### Entenda os estados de inscrição de push {#understand-push-subscription-states}

O estado de inscrição de push não garante que um push será entregue — os usuários também precisam estar com o push ativado para receber notificações. Isso ocorre porque um perfil de usuário pode ter vários dispositivos com diferentes permissões de push em primeiro plano, mas apenas um único estado de inscrição de push.

Se um usuário não tiver um token por push em primeiro plano válido para um app (ou seja, ele desativa os tokens por push no nível do dispositivo nas configurações, optando por não receber notificações), seu estado de inscrição ainda pode ser considerado `subscribed` para push. No entanto, esse usuário não estaria com `Foreground Push Enabled for App` na Braze, pois o token por push em primeiro plano não é válido.

Além disso, se um perfil de usuário não tiver nenhum token por push válido ou registrado para nenhum outro app, o filtro `Foreground Push Enabled` na segmentação também será falso.

## Implemente uma política de desativação para usuários não responsivos {#implement-a-sunset-policy-for-unresponsive-users}

Mesmo quando você envia apenas notificações por push relevantes e oportunas, alguns usuários ainda podem não responder a elas e considerá-las spam. Suponha que um usuário mostre um histórico de ignorar repetidamente suas notificações por push. Nesse caso, é uma boa ideia parar de enviar pushes antes que ele fique irritado com as comunicações do seu app ou desinstale-o completamente.

Para fazer isso, crie uma [política de desativação]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) que eventualmente pare de enviar notificações por push para usuários que não tiveram uma abertura direta ou por influência por um longo período.

1. Identifique usuários não responsivos com base em aberturas diretas ou por influência.
2. Pare gradualmente de enviar notificações por push para esses usuários.
3. Antes de remover as notificações por push completamente, envie uma última notificação explicando por que eles não receberão mais. Isso dá aos usuários a chance de demonstrar seu interesse em continuar recebendo pushes ao abrir essa notificação.
4. Depois que a política de desativação entrar em vigor, use uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages) para lembrar esses usuários de que, embora não recebam mais pushes, os canais de mensagens no app continuarão a entregar informações interessantes e úteis.

Embora você possa relutar em parar de enviar pushes para usuários que originalmente optaram por recebê-los, lembre-se de que outros canais de envio de mensagens podem alcançar esses usuários de forma mais eficaz, especialmente se eles já ignoraram seus pushes anteriormente. Se o usuário abrir seus e-mails, campanhas de e-mail são uma boa maneira de alcançá-lo fora do seu app. Caso contrário, as mensagens no app são a melhor forma de entregar conteúdo sem arriscar que o usuário desinstale seu app.

## Defina eventos de conversão para aberturas do app {#set-conversion-events-for-app-opens}

Ao atribuir [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) a uma Campaign de push, você pode rastrear aberturas do app por um determinado período após o recebimento da Campaign. Definir um evento de conversão para aberturas do app fornece um insight diferente das estatísticas de resultados que você normalmente recebe após uma Campaign de push.

Embora todos os resultados de Campaigns de push detalhem as aberturas diretas e as aberturas de uma mensagem (que incluem tanto aberturas diretas quanto [aberturas por influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)), o rastreamento de conversão acompanhará qualquer tipo de abertura, seja direta ou por influência.

Além disso, ao usar o evento de conversão "abre o app", você está rastreando aberturas do app que ocorrem antes do prazo de conversão (por exemplo, três dias). Isso difere de uma abertura por influência, pois o tempo que um usuário tem para registrar uma abertura por influência pode variar de pessoa para pessoa, dependendo do comportamento de engajamento anterior de cada usuário.

## Regulamentações de mensagens push {#push-message-regulations}

Como as mensagens push são um tipo intrusivo de envio de mensagens que vai diretamente para o telefone ou navegador do seu cliente, existem diretrizes para o envio de mensagens push por meio de apps e sites.

### Regulamentações de push para dispositivos móveis em apps {#mobile-push-regulations-for-apps}

| Políticas da Apple App Store |
| --- |
| [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inaceitável: (i) Criar uma interface para exibir apps, extensões ou plug-ins de terceiros semelhante à App Store ou como uma coleção de interesse geral. |
| [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) As notificações por push não devem ser obrigatórias para o funcionamento do app e não devem ser usadas para enviar informações pessoais sensíveis ou confidenciais. As notificações por push não devem ser usadas para fins de promoção ou marketing direto, a menos que os clientes tenham optado explicitamente por recebê-las por meio de linguagem de consentimento exibida na interface do seu app, e você forneça um método no seu app para que o usuário opte por não receber tais mensagens. |
| [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Você não pode monetizar recursos integrados fornecidos pelo hardware ou sistema operacional, como notificações por push, a câmera ou o giroscópio; ou serviços e tecnologias da Apple, como acesso ao Apple Music, armazenamento iCloud ou APIs de Tempo de Uso. |
{: .reset-td-br-1 aria-label="Regulamentações de push para dispositivos móveis em apps" }

| Política da Google Play Store |
| --- |
| [Uso não autorizado ou imitação de funcionalidade do sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Não permitimos apps ou anúncios que imitem ou interfiram na funcionalidade do sistema, como notificações ou avisos. As notificações no nível do sistema podem ser usadas apenas para recursos essenciais de um app, como um app de companhia aérea que notifica os usuários sobre ofertas especiais ou um jogo que notifica os usuários sobre promoções dentro do jogo. |
{: .reset-td-br-1 aria-label="Regulamentações de push para dispositivos móveis em apps" }

## Artigos relacionados {#related-articles}

Não encontrou o que procurava? Confira estes artigos adicionais de melhores práticas:

- [Formatos de mensagem e imagem de push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Mensagens no app de preparação para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)
- [Entregabilidade para dispositivos Android chineses]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)
- [Saiba antes de enviar: canais]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)