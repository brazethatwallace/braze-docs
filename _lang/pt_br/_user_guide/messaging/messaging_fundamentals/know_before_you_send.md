---
nav_title: "Saiba antes de enviar"
article_title: "Saiba antes de enviar"
description: "Depois de consultar nosso guia de pré-lançamento, confira esta lista final de verificações ou 'pegadinhas' para Content Cards, e-mail, mensagens no app, push e SMS."
alias: /know_before_send/
page_order: 7
tool:
    - Campaigns
    - Canvas
---

# Saiba antes de enviar: canais {#know-before-you-send-channels}

> Lance suas Campaigns e Canvas com confiança! Consulte esta lista final de verificações ou "pegadinhas" para os [canais]({{site.baseurl}}/user_guide/channels) de envio de mensagens mais populares da Braze.

{% alert note %}
Embora ofereçamos uma lista extensa de recursos para consultar antes do envio, cada canal tem particularidades individuais que continuam a crescer à medida que evoluímos nossos produtos. As verificações listadas abaixo são sugestões úteis, e recomendamos testar minuciosamente suas Campaigns e envios em grande escala antes de enviá-los.
{% endalert %}

## Geral {#general}

### Itens para verificar {#things-to-check}
- [**Limites de frequência de API**](https://braze.com/resources/articles/whats-rate-limiting): Revise os [limites de frequência]({{site.baseurl}}/api/api_limits) da API da Braze para seus espaços de trabalho e evite erros. Se você deseja aumentar seus limites de frequência (e já está agrupando solicitações em lotes), entre em contato com seu CSM. Lembre-se de que esse processo requer um prazo de antecedência, então planeje-se adequadamente.
- [**Substituições necessárias de limite de frequência**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Existem algumas campanhas, como mensagens transacionais, que você vai querer que sempre cheguem ao usuário, mesmo que ele já tenha atingido seu limite de frequência (por exemplo, uma notificação de entrega). Se você quiser que uma Campaign específica substitua as regras de limite de frequência, configure isso no dashboard da Braze ao agendar a entrega dessa Campaign, desativando o limite de frequência.

### Itens para saber {#things-to-know}
- [**Grupos de controle global**]({{site.baseurl}}/user_guide/audience/global_control_group): Se você estiver usando um grupo de controle global, uma porcentagem de usuários não receberá nenhuma Campaign ou Canvas. (Você pode criar exceções com as [configurações de exclusão]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings)). Para ver uma lista desses usuários, exporte-os via CSV ou [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).
- [**Limites de frequência de Canvas**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Em um Canvas, o limite de frequência se aplica ao Canvas inteiro, não às etapas individuais. Por exemplo, se você definir um limite de frequência de 10.000 mensagens por minuto em um Canvas com múltiplas etapas, ele ainda ficará limitado a 10.000 mensagens, porque o limite terá sido atingido na primeira etapa.
- **Limite de frequência**:
  - As regras de limite de frequência são aplicadas a push, e-mail, SMS e webhooks, mas não a mensagens no app e Content Cards.
  - O limite de frequência global é agendado com base no fuso local do usuário e é calculado por dias corridos, não por períodos de 24 horas. Por exemplo, se você configurar uma regra de limite de frequência para enviar no máximo uma Campaign por dia, um usuário poderá receber uma mensagem às 23h em seu fuso local e ainda será elegível para receber outra mensagem uma hora depois.

{% alert tip %}
Para mais assistência com solução de problemas de Canvas e Campaign, entre em contato com o suporte da Braze dentro de 30 dias após a ocorrência do problema, pois só temos os últimos 30 dias de registros de diagnóstico.
{% endalert %}

## Banners {#banners}

### Coisas para verificar
- **Dimensões do Banner:** Construa seus Banners usando um elemento de dimensão fixa e teste-os no editor.
- **Prioridade:** Se você estiver lançando vários Banners, pode definir manualmente a prioridade de como cada banner é exibido.

### Coisas para saber
- **Personalização com Liquid:** A personalização com Liquid é atualizada a cada solicitação de atualização.
- **Proporção de posicionamento e Banner:** Cada posicionamento de Banner pode ser usado em até 25 mensagens em um espaço de trabalho.
- **Cliques e impressões:** Cliques e impressões para Banners são rastreados automaticamente com o SDK.
- **Limitações:** Atualmente, os seguintes recursos não são compatíveis: integração com Canvas, Campaigns disparadas por API e baseadas em ação, Connected Content, códigos de promoção e `catalog_items` usando a [tag `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- **Testes:** Para exibir o Banner de teste, o dispositivo que você está usando precisa ser capaz de receber notificações por push em primeiro plano.
- **HTML personalizado:** Use o [ponte JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge) para registrar cliques ao usar HTML personalizado para definir ações de clique, como links e botões. As ações de clique só são registradas automaticamente ao usar os componentes pré-construídos no editor de arrastar e soltar.
- **Solicitação de posicionamentos:** Até 10 posicionamentos podem ser retornados ao SDK em uma única solicitação de atualização. Cada posicionamento incluirá o Banner de maior prioridade para o qual o usuário é elegível.

## Content Cards

### O que verificar
- **Tamanho do Content Card**: Os campos de mensagem do Content Card são limitados a 2&nbsp;KB em tamanho pré-compressão, calculado pela soma do comprimento em bytes dos seguintes campos: título, mensagem, URL da imagem, texto do link, URLs do link e pares de chave-valor. Mensagens que excederem esse tamanho não serão enviadas. Observe que isso não inclui o tamanho da imagem, mas sim o comprimento da URL da imagem.
- **Atualização do texto após o envio**: Depois que um cartão é enviado, você não poderá atualizar o texto desse mesmo cartão. Consulte [Atualizando cartões enviados]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) para entender como abordar esse cenário.

### O que saber
- **Limite de Campaigns ativas de Content Card**: Você pode ter até 500 Campaigns ativas de Content Card. Essa contagem inclui Content Cards enviados com qualquer opção de [criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card).
- [**Termos de relatório**]({{site.baseurl}}/user_guide/channels/content_cards/reporting): Revise termos como impressões totais, impressões únicas e destinatários únicos, pois as definições podem causar confusão.
- **Atualização de Content Cards**: Por padrão, a Braze atualiza as solicitações de Content Card conforme elas sincronizam no início da sessão, ao deslizar o feed para baixo (celular) e quando a visualização de cartões é aberta se a última atualização foi há mais de um minuto.
- **Cache de Content Cards**: As opções de cache de Content Cards podem ser encontradas em nossa documentação para [Android/FireOS]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style) e [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards).
- **Limite de frequência**: O limite de frequência não se aplica a Content Cards.
- **Impressões**: As impressões geralmente são registradas quando um cartão é visualizado. Por exemplo, se você tiver uma caixa de entrada cheia de Content Cards, uma impressão não será registrada até que o usuário role até o Content Card específico. Existem algumas diferenças entre as plataformas Web, Android e iOS.
- **Sessões do SDK e criação de cartões**: Content Cards não são criados para usuários sem sessões do SDK, mesmo que esses usuários atendam aos critérios do Segment. No entanto, se um usuário já tiver uma sessão Android, Content Cards com ações de clique específicas para iOS ainda serão criados, e o usuário poderá visualizar esses Content Cards no iOS assim que tiver uma sessão lá. Consulte [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) para saber mais sobre quando os cartões são criados.

## E-mail {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### O que verificar
- **Consentimento do cliente**: Antes de enviar seus e-mails iniciais, é importante obter a permissão dos seus clientes primeiro. Consulte [Consentimento e coleta de endereços]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection) e nossa [Política de Uso Aceitável da Braze](https://www.braze.com/company/legal/aup) para saber mais.
- **Volume previsto**: 2 milhões de e-mails por dia para um único IP é a recomendação geral, desde que esse volume tenha sido [devidamente aquecido]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).
  - Se você planeja enviar consistentemente um volume maior do que esse, para evitar que os provedores limitem o recebimento de e-mails — resultando em uma alta quantidade de soft bounces, menor taxa de entregabilidade e diminuição da reputação do IP — considere usar vários endereços IP agrupados em um pool de IP.
  - Se você deseja enviar em um período mais curto, recomendamos verificar a velocidade com que diferentes provedores aceitam e-mails para determinar o número adequado de IPs para o envio.

### O que saber
- **Fatores de volume de envio**: Alguns fatores que determinam a capacidade de volume de envio de um IP incluem:
  - Caixas de entrada: Grandes provedores de e-mail provavelmente conseguem lidar com milhões por dia a partir de um único IP, enquanto um provedor de caixa de entrada regional menor ou com uma infraestrutura mais limitada pode não conseguir lidar com esse volume.
  - Reputação do remetente: Você pode conseguir enviar um volume maior por dia a partir de um único IP se o remetente tiver sido aquecido até esse volume e se a reputação do remetente for forte o suficiente em cada caixa de entrada ou domínio para o qual está enviando.
- **Práticas recomendadas**: Revise as [práticas recomendadas de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices) da Braze e entre em contato com a equipe de conta da Braze se quiser saber mais sobre serviços de entregabilidade.

## Mensagens no app {#in-app-messages}

### O que você precisa saber
- **Disparo de mensagens no app**: No início da sessão, o SDK solicita que todas as mensagens no app elegíveis sejam enviadas ao dispositivo junto com seus disparadores, para que, se o usuário realizar o evento durante a sessão, ele possa receber a mensagem no app de forma rápida e confiável.
- **Enviadas versus impressões**: Para mensagens no app, o conceito de "enviada" difere dos outros canais disponíveis. Para ver uma mensagem no app, o usuário precisa iniciar uma sessão, estar no público elegível e realizar o disparo. Por isso, rastreamos "impressões", pois é mais claro.
- **Disparo**: Por padrão, as mensagens no app são disparadas por eventos registrados pelo SDK. Se você quiser disparar mensagens no app por eventos enviados pelo servidor, também é possível fazer isso por meio destes guias para [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift) e [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android).
- [Mensagens no app no Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior): Essas mensagens aparecem na primeira vez que o usuário abre o app (disparadas pelo início da sessão) depois que a mensagem agendada no componente do Canvas é enviada a ele.
- **Chamadas de Connected Content**: Usar Connected Content permite enviar conteúdo dinâmico nas mensagens. Quando você envia mensagens por um canal como mensagens no app, isso pode criar mais conexões simultâneas com os dispositivos dos seus usuários (as mensagens são enviadas uma a uma, em vez de em lotes). Para gerenciar isso, recomendamos aplicar [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) às suas mensagens.

## Push {#push}

### Coisas para verificar
- [**Aceite/inscrito e push ativado**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states): Para que os usuários recebam uma mensagem por push da Braze, o status de inscrição deles precisa ser aceite (iOS) ou inscrito (Android), e `Push Enabled = True`. Note que o Android 13 introduz uma mudança importante na forma como os usuários gerenciam apps que enviam notificações por push. O [guia de upgrade do SDK para Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13) da Braze continuará sendo atualizado conforme novas versões beta do Android 13 forem lançadas.

### Coisas para saber
- **Web push**: Se você já configurou o [SDK Web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web) da Braze, considere utilizar o web push para engajar os usuários. O web push funciona da mesma forma que as notificações por push de apps no seu celular. Para saber mais sobre como compor um web push, confira [Criação de uma notificação por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).
- **Direcionamento para um único app**: Revise as [diferenças na segmentação]({{site.baseurl}}/user_guide/get_started/workspaces) para direcionar um único app e seus usuários.

## SMS

### O que verificar
- **Cotas e throughput**: Entenda quais cotas de SMS estão atualmente vinculadas à sua conta (short code, long code e similares) e [quanto throughput isso proporciona]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) para confirmar que você tem throughput suficiente para enviar no tempo desejado.
- **Estimar segmentos a partir do texto do SMS**: Teste o texto do seu SMS na [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator). Tenha em mente que o número de segmentos de SMS deve ser considerado junto com suas capacidades de throughput. (Público × segmentos de SMS = throughput necessário). Consulte as perguntas frequentes sobre SMS para [evitar excedentes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).
- **Leis e regulamentações de SMS**: [Revise as leis, regulamentações e prevenção de abuso de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) para confirmar que você está usando os serviços de SMS em conformidade com todas as leis aplicáveis. Certifique-se de buscar orientação do seu departamento jurídico antes de enviar.

### O que saber
- **Padrão de envio de mensagens SMS**: As mensagens SMS normalmente são configuradas por padrão para serem enviadas a partir do short code no pool de remetentes.
- **ID de remetente alfanumérico**: O envio de mensagens bidirecionais não funcionará mais se você usar um ID de remetente alfanumérico; agora eles são apenas unidirecionais.
- **Throughput atualizado nos EUA**: O throughput mudou nos EUA com o [registro A2P 10DLC nos EUA](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Observe que não nos comprometemos contratualmente com nenhum SLA de velocidade de envio devido a múltiplos fatores, como congestionamento de tráfego e problemas com operadoras, que podem impactar as taxas reais de entrega.
- **Grupo de inscrições**: Para lançar uma Campaign de SMS pela Braze, um grupo de inscrições deve ser selecionado. Além disso, para aderir às [diretrizes e conformidade de telecomunicações internacionais]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), a Braze nunca enviará SMS para usuários que não tenham se [inscrito no grupo de inscrições selecionado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#check-a-users-group).

## WhatsApp

### O que saber

- [**Melhores práticas**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices): Revise nossas melhores práticas sugeridas para WhatsApp.