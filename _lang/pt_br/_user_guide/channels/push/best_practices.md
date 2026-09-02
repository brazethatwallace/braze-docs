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

## Crie sua mensagem de push {#compose-your-push-message}

Como melhor prática, a Braze recomenda manter cada linha de texto, tanto no título opcional quanto no corpo da mensagem, com aproximadamente 30 a 40 caracteres em uma notificação por push para dispositivos móveis. O contador de caracteres no criador não considera os caracteres de Liquid. Isso significa que a contagem final de caracteres de uma mensagem depende de como o Liquid é renderizado para cada usuário. Na dúvida, seja breve e direto.

## Reduzir o tamanho do payload da notificação por push {#reduce-push-notification-payload-size}

O tamanho máximo do payload depende da plataforma.

| Plataforma | Tamanho máximo do payload |
| --- | --- |
| Web | 3.807 bytes |
| Android | 3.930 bytes |
| iOS | 3.960 bytes |
| Kindle | 5.985 bytes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reduzir o tamanho do payload da notificação por push" }

Se sua notificação por push exceder o tamanho máximo do payload, a mensagem pode não ser enviada. Como melhor prática, mantenha seu payload em poucos centenas de bytes.

### O que é um payload de push? {#what-is-a-push-payload}

Os provedores de serviço de push calculam se a notificação por push pode ser exibida para o usuário analisando o tamanho em bytes de todo o payload da notificação. O payload é limitado a **4 KB (4.096 bytes)** na maioria dos serviços de push, incluindo:

- Serviço de Notificações por Push da Apple (APNs)
- Firebase Cloud Messaging (FCM) do Android
- Web push
- Push da Huawei

Esses serviços de push rejeitarão qualquer notificação que exceda esse limite.

A Braze reserva uma parte do payload da notificação por push para fins de integração e análise de dados. Sendo assim, nosso tamanho máximo de payload é de **3.807 bytes**. Se sua notificação por push exceder esse tamanho, a mensagem pode não ser enviada. Como melhor prática, mantenha seu payload em poucos centenas de bytes.

Os seguintes elementos da sua notificação por push compõem o payload:

- Texto, como o título e o corpo da mensagem
- Renderização final de qualquer personalização em Liquid
- URLs de imagens (mas não o tamanho da imagem em si)
- URLs de destinos de clique
- Nomes dos botões
- Pares de chave-valor

### Dicas para reduzir o tamanho do payload {#tips-to-reduce-payload-size}

Para reduzir o tamanho do payload:

- Mantenha sua mensagem breve. Uma boa diretriz geral é torná-la acionável e útil em menos de 40 caracteres.
- Omita espaços em branco e quebras de linha do seu texto.
- Considere como o Liquid será renderizado no envio. Como a renderização final de qualquer personalização em Liquid varia de usuário para usuário, a Braze não consegue determinar se o payload da notificação por push excederá o limite de tamanho quando o Liquid estiver incluído. Se o Liquid renderizar uma mensagem mais curta, provavelmente não haverá problema. No entanto, se o Liquid resultar em uma mensagem mais longa, sua notificação por push poderá exceder o limite de tamanho do payload. Sempre teste sua notificação por push em um dispositivo real antes de enviá-la aos usuários.
- Considere encurtar URLs usando um encurtador de URLs.

## Otimizar o direcionamento {#optimize-targeting}

### Colete dados relevantes dos usuários {#collect-relevant-user-data}

As notificações por push devem ser tratadas com cuidado para direcionar os usuários com notificações oportunas e relevantes. A Braze coleta informações úteis sobre dispositivos e uso que podem ser usadas para direcionar Segments relevantes. Essas informações devem ser complementadas com eventos personalizados e atributos específicos do seu app. Com esses dados, você pode direcionar mensagens com precisão para aumentar as taxas de abertura e diminuir os casos de usuários desativando o push.

### Crie uma página de configurações de notificação {#create-a-notification-settings-page}

Você pode criar uma página de configurações no seu app que permita aos usuários informar quais notificações desejam receber. Uma abordagem comum é criar um atributo personalizado booleano na Braze correspondente ao status da configuração do app. Por exemplo, um app de notícias pode ter configurações de inscrição para notícias de última hora, esportes ou política.

Quando o app de notícias quiser criar uma Campaign direcionada apenas a usuários interessados em Política, basta adicionar o filtro de atributo `Subscribes to Politics` ao Segment or segmento. Quando definido como verdadeiro, apenas os usuários que se inscreveram nas notificações irão recebê-las.

Para saber mais sobre como definir atributos personalizados, consulte os seguintes artigos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android) ou [REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Aumente as aceitações e a relevância {#increase-opt-ins-and-relevance}

### Obtenha a permissão do usuário {#obtain-user-permission}

As estatísticas gerais de push ativado referem-se à aprovação do usuário para receber notificações no sistema operacional. Se os usuários desativarem as notificações no iOS, eles serão automaticamente removidos do nosso sistema, já que a Apple não permite o envio do token por push.

O Android 13 e versões superiores exigem a obtenção de permissão antes que as notificações por push possam ser exibidas. Versões mais antigas do Android inscrevem os usuários nas notificações por padrão.

### Prepare os usuários para o push {#prime-users-for-push}

Você tem apenas uma chance de solicitar a permissão de push ao usuário e, após a recusa, é muito difícil convencê-lo a reativar o push nas configurações do dispositivo. Por isso, você deve preparar os usuários para o push usando uma mensagem no app antes de exibir o prompt do sistema. Consulte [Mensagens no app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para saber mais sobre como aumentar as aceitações.

### Adicione controles de inscrição de push {#add-push-subscription-controls}

Para evitar que os usuários desativem as notificações no nível do dispositivo — o que remove completamente o token por push em primeiro plano — permita que os usuários controlem sua inscrição de push diretamente no seu app. Consulte [Atualização dos estados de inscrição de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) para mais detalhes.

### Use agendamento avançado ou adicione postergações {#use-advanced-scheduling-or-add-delays}

Dependendo do tamanho do seu público e de quanto tempo antes a mensagem de push é agendada, podem ocorrer atrasos na entrega de push. O tempo necessário para enviar notificações por push depende da capacidade de processamento alocada. Por exemplo, se a sua mensagem de push usa várias chamadas de Connected Content, isso pode aumentar a complexidade da criação do template da mensagem e resultar em velocidades limitadas pela rapidez com que as APIs de terceiros retornam dados.

Uma carga útil de push menor e uma prioridade de notificação mais alta podem ajudar a reduzir atrasos e escalar suas mensagens. Você pode adicionar `Push Enabled = true` no filtro de público para reduzir o tamanho do público, de modo que apenas usuários com push ativado sejam processados para o envio da Campaign.

Também recomendamos minimizar o número de chamadas de API or interface de programação do aplicativo (API) otimizando os dados de que você precisa. Se possível, tente obter todos os dados necessários em uma única chamada de API or interface de programação do aplicativo (API), em vez de fazer múltiplas chamadas.

### Entenda os estados de inscrição de push {#understand-push-subscription-states}

O estado de inscrição de push não garante que uma notificação por push será entregue — os usuários também precisam estar com push ativado para receber notificações. Isso ocorre porque um perfil de usuário pode ter vários dispositivos com diferentes permissões de push em primeiro plano, mas apenas um único estado de inscrição de push.

Se um usuário não tiver um token por push em primeiro plano válido para um app (ou seja, ele desativou os tokens por push no nível do dispositivo por meio das configurações, optando por não receber notificações), seu estado de inscrição ainda pode ser considerado `subscribed` para push. No entanto, esse usuário não seria `Foreground Push Enabled for App` na Braze, pois o token por push em primeiro plano não é válido.

Além disso, se um perfil de usuário não tiver nenhum token por push válido ou registrado para nenhum outro app, o filtro `Foreground Push Enabled` na segmentação também será falso.

## Implemente uma política de descontinuação para usuários não responsivos {#implement-a-sunset-policy-for-unresponsive-users}

Mesmo quando você envia apenas notificações por push relevantes e oportunas, alguns usuários ainda podem não responder a elas e considerá-las SPAM. Suponha que um usuário tenha um histórico de ignorar repetidamente suas notificações por push. Nesse caso, é uma boa ideia parar de enviar pushes antes que ele fique irritado com as comunicações do seu app ou o desinstale completamente.

Para fazer isso, crie uma [política de descontinuação]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) que eventualmente pare de enviar notificações por push para usuários que não tiveram uma Abertura Direta ou Abertura por Influência por um longo período.

1. Identifique os usuários não responsivos com base em Aberturas Diretas ou Aberturas por Influência.
2. Pare gradualmente de enviar notificações por push para esses usuários.
3. Antes de remover completamente as notificações por push, envie uma notificação final explicando por que eles não receberão mais essas mensagens. Isso dá aos usuários a chance de demonstrar interesse em continuar recebendo pushes ao abrir essa notificação.
4. Após a política de descontinuação entrar em vigor, use uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages) para lembrar esses usuários de que, embora não recebam mais pushes, os canais de mensagens no app continuarão a entregar informações interessantes e úteis.

Embora você possa relutar em parar de enviar pushes para usuários que originalmente aceitaram recebê-los, lembre-se de que outros canais de envio de mensagens podem alcançar esses usuários de forma mais eficaz, especialmente se eles já ignoraram seus pushes anteriormente. Se o usuário abre seus e-mails, Campaigns de e-mail são uma boa maneira de alcançá-lo fora do seu app. Caso contrário, as mensagens no app são a melhor forma de entregar conteúdo sem correr o risco de o usuário desinstalar o app.

## Definir eventos de conversão para aberturas de app {#set-conversion-events-for-app-opens}

Ao atribuir [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) a uma campanha de push, você pode rastrear aberturas de app por um determinado período após o recebimento da campanha. Definir um evento de conversão para aberturas de app fornece um insight diferente das estatísticas de resultados que você normalmente recebe após uma campanha de push.

Embora todos os resultados de campanhas de push detalhem as aberturas diretas e as aberturas totais de uma mensagem (que incluem tanto as diretas quanto as [Aberturas por Influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)), o rastreamento de conversão registra qualquer tipo de abertura, seja direta ou por influência.

Além disso, ao usar o evento de conversão "abre o app", você está rastreando aberturas de app que ocorrem antes do prazo de conversão (por exemplo, três dias). Isso difere de uma abertura por influência, pois o tempo que um usuário tem para registrar uma abertura por influência pode variar de pessoa para pessoa, dependendo do comportamento de engajamento anterior de cada usuário.

## Regulamentações para mensagens push {#push-message-regulations}

Como as mensagens push são um tipo intrusivo de envio de mensagens que chega diretamente ao telefone ou navegador do seu cliente, existem diretrizes para o envio de mensagens push por meio de apps e sites.

### Regulamentações de push para dispositivos móveis em apps {#mobile-push-regulations-for-apps}

| Políticas da Apple App Store |
| --- |
| [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inaceitável: (i) Criar uma interface para exibir apps, extensões ou plug-ins de terceiros de forma semelhante à App Store ou como uma coleção de interesse geral. |
| [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Notificações por push não devem ser obrigatórias para o funcionamento do app e não devem ser usadas para enviar informações pessoais sensíveis ou confidenciais. Notificações por push não devem ser usadas para fins de promoção ou marketing direto, a menos que os clientes tenham dado consentimento explícito para recebê-las por meio de uma linguagem de consentimento exibida na interface do app, e que você forneça um método no app para que o usuário possa optar por não receber essas mensagens. |
| [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Você não pode monetizar recursos integrados fornecidos pelo hardware ou sistema operacional, como notificações por push, câmera ou giroscópio; ou serviços e tecnologias da Apple, como acesso ao Apple Music, armazenamento no iCloud ou APIs do Screen Time. |
{: .reset-td-br-1 aria-label="Regulamentações de push para dispositivos móveis em apps" }

| Política da Google Play Store |
| --- |
| [Uso não autorizado ou imitação de funcionalidades do sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Não permitimos apps ou anúncios que imitem ou interfiram em funcionalidades do sistema, como notificações ou alertas. Notificações em nível de sistema só podem ser usadas para recursos essenciais do app, como um app de companhia aérea que notifica os usuários sobre ofertas especiais ou um jogo que notifica os usuários sobre promoções dentro do jogo. |
{: .reset-td-br-1 aria-label="Regulamentações de push para dispositivos móveis em apps" }

## Artigos relacionados {#related-articles}

Não encontrou o que procurava? Confira estes artigos adicionais sobre melhores práticas:

- [Formatos de mensagens e imagens para push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Mensagens no app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)
- [Entregabilidade para dispositivos Android chineses]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)
- [Saiba antes de enviar: canais]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)