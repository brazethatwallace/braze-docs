---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar Campaigns de WhatsApp."
page_type: FAQ
channel:
  - WhatsApp
---

# Perguntas frequentes {#frequently-asked-questions}

> Nesta página, vamos tentar responder às suas perguntas mais importantes sobre o WhatsApp!<br><br>Este FAQ não tem a intenção de fornecer, nem pode ser considerado como aconselhamento jurídico. O uso do canal WhatsApp está sujeito a requisitos específicos da Meta Platforms, Inc. Para garantir que você esteja usando o canal WhatsApp em conformidade com todos os requisitos aplicáveis e quaisquer leis às quais você possa estar especificamente sujeito, você deve buscar orientação do seu departamento jurídico.

## Tópicos do FAQ {#faq-topics}
- [Contas comerciais do WhatsApp](#whatsapp-business-accounts)
- [Número de telefone da conta comercial do WhatsApp](#whatsapp-business-account-phone-numbers)
- [Opt-in e gerenciamento de inscrições](#opt-in-and-subscription-management)
- [Limites de envio de mensagens e classificação de qualidade](#messaging-limits-and-quality-rating)
- [Modelos e criador do WhatsApp](#whatsapp-templates-and-composer)
- [Entregabilidade e cobrança](#deliverability-and-billing)
- [Integrações, dados e relatórios](#integrations-data-and-reporting)

### Contas comerciais do WhatsApp {#whatsapp-business-accounts}

#### Como crio uma conta comercial do WhatsApp? {#how-do-i-create-a-whatsapp-business-account}
Recomendamos criar sua conta comercial do WhatsApp (WABA) por meio do fluxo de cadastro integrado no dashboard da Braze.

#### Já tenho uma conta comercial da Meta. Ainda preciso de uma conta comercial do WhatsApp? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Sim, você ainda precisa criar uma conta comercial do WhatsApp. Recomendamos que você [vincule sua WABA à sua conta comercial principal da Meta]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### Como acesso minha conta comercial do WhatsApp? {#how-do-i-access-my-whatsapp-business-account}
Após concluir o fluxo de cadastro integrado, você pode acessar sua conta em business.facebook.com navegando até a [seção do WhatsApp](https://business.facebook.com/wa/manage/home).

#### Posso conectar múltiplas WABAs à Braze? {#can-i-connect-multiple-wabas-to-braze}
Sim, você pode adicionar até 10 contas WhatsApp Business por espaço de trabalho, e cada conta comercial pode ser vinculada a um Meta Business Manager diferente.

![Diagrama do ecossistema da Braze e WhatsApp, mostrando como espaços de trabalho e contas WhatsApp Business se conectam entre si: você pode conectar um grupo de inscrições a um número de telefone, múltiplas contas WhatsApp Business a um espaço de trabalho e um espaço de trabalho a múltiplos Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### Posso alterar a moeda da minha conta WhatsApp Business? {#can-i-change-my-whatsapp-business-account-currency}
Não. A Meta controla a moeda da sua conta WhatsApp Business, e a Braze não pode alterá-la ou convertê-la. Para usar uma moeda diferente, [crie uma conta WhatsApp Business separada]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) com essa moeda, ou entre em contato com o suporte da Meta para perguntar se eles podem atualizar a moeda da sua conta existente.

#### O que é verificação de empresa? {#what-is-business-verification}
A verificação de empresa é um conceito do WhatsApp usado para garantir que a marca é uma empresa legítima. Ela pode ser concluída no WhatsApp Manager. A verificação de empresa também é necessária para escalar o envio de mensagens. Sem a verificação de empresa, os clientes só podem enviar mensagens para até 250 usuários finais únicos em um período contínuo de 24 horas.

#### O que é uma conta comercial oficial? {#what-is-an-official-business-account}
A OBA (conta comercial oficial) dá a você a marca de verificação verde ao lado do seu nome de exibição e é opcional. Você pode solicitar uma conta comercial oficial após concluir a verificação de empresa. Observe que a verificação de empresa e uma conta comercial oficial são conceitos diferentes do WhatsApp.

### Números de telefone da conta comercial do WhatsApp {#whatsapp-business-account-phone-numbers}

#### Preciso de um número de telefone para minha conta comercial do WhatsApp? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Sim, você precisa de um número ao qual tenha acesso. Será solicitado que você verifique seu número de telefone com autenticação de dois fatores ao passar pelo fluxo de cadastro integrado. O número de telefone não pode ser usado em outras contas do WhatsApp (comerciais ou pessoais).

#### Quais tipos de números de telefone são compatíveis com o WhatsApp? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Consulte os requisitos da Meta para [números de telefone](https://developers.facebook.com/docs/whatsapp/phone-numbers) para mais informações.

#### Posso usar um número de telefone em múltiplas WABAs? {#can-i-use-one-phone-number-across-multiple-wabas}
Não. Um número de telefone não pode ser compartilhado entre múltiplas WABAs.

#### Preciso de um tipo específico de número de telefone para enviar mensagens para países específicos? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
Não. O WhatsApp permite que você envie mensagens para usuários finais a partir de qualquer número de telefone compatível em qualquer país. Consulte os requisitos da Meta para [números de telefone](https://developers.facebook.com/docs/whatsapp/phone-numbers) para mais informações.

#### Como os números de telefone dos usuários precisam ser armazenados na Braze? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Os números de telefone dos usuários precisam ser armazenados no [formato E.164]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting).

#### Posso importar números de telefone de usuários? {#can-i-import-user-phone-numbers}
Sim. Você pode [importar números de telefone de usuários]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

### Opt-in e gerenciamento de inscrições {#opt-in-and-subscription-management}

#### Preciso coletar opt-in para enviar mensagens de marketing para usuários finais no WhatsApp? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Sim, o WhatsApp exige que as empresas [coletem consentimento de opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para enviar mensagens de marketing para usuários finais.

#### Posso enviar mensagens proativamente para usuários finais no WhatsApp para coletar consentimento de opt-in? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Se você optar por enviar mensagens proativamente para usuários finais, sua primeira mensagem iniciada pela empresa deve perguntar ao usuário se ele deseja receber mensagens de marketing da sua empresa e deve estar em conformidade com os requisitos da Meta para [obter opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Tenha em mente que o WhatsApp monitorará a reputação da sua empresa no canal, então a melhor prática recomendada é ser explícito com os usuários finais e enviar apenas mensagens que eles indicaram querer receber.

#### Preciso coletar o número de telefone do usuário final quando coleto o opt-in? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Você precisa ter o número de telefone do usuário final no perfil da Braze para enviar mensagens.
- Se você já tem o número, não precisa coletá-lo durante o opt-in.
- Se você não tem o número do usuário final, seu método de opt-in deve incluir a captura do número de telefone.

#### Como atualizo o status de inscrição dos usuários finais que fizeram opt-in? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
O gerenciamento de inscrições do canal WhatsApp funciona de forma semelhante a como funciona em outros canais da Braze. Consulte [Gerenciando inscrições de usuários]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) para mais informações.

#### Se eu já tenho uma lista de usuários que fizeram opt-in para receber mensagens de marketing no WhatsApp, como atualizo o status de inscrição deles na Braze? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Você pode atualizar o status de inscrição deles via [importação de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional).

#### Quais métodos devo usar para coletar opt-ins? {#what-methods-should-i-use-to-collect-opt-ins}
A Braze recomenda consultar as [diretrizes da Meta para métodos de opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para manter a conformidade. Consulte o seguinte recurso para [ideias e sugestões de canais e opt-in da Braze](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit).

#### O double opt-in é obrigatório para o WhatsApp? {#is-double-opt-in-required-for-whatsapp}
Não, o double opt-in não é obrigatório.

#### Como meus usuários cancelam a inscrição de mensagens do WhatsApp? {#how-do-my-users-opt-out-of-whatsapp-messages}
Seus usuários podem cancelar a inscrição de duas formas:
1. Configure uma mensagem de entrada do WhatsApp com uma palavra específica de descadastramento e use um webhook para atualizar o status de inscrição do usuário.
2. Adicione uma resposta rápida de descadastramento dentro do modelo de WhatsApp, com um webhook correspondente para atualizar.

### Limites de envio de mensagens e classificação de qualidade {#messaging-limits-and-quality-rating}

#### O que são limites de envio de mensagens? {#what-are-messaging-limits}
Os limites de envio de mensagens são um conceito de integridade do WhatsApp. Eles determinam o número máximo de conversas iniciadas pela empresa que cada número de telefone pode iniciar em um período contínuo de 24 horas. Existem quatro níveis de limite de envio de mensagens: 1 mil, 10 mil, 100 mil e ilimitado.

#### Como aumento meu limite de envio de mensagens? {#how-do-i-increase-my-messaging-limit}
O WhatsApp aumentará seu limite de envio de mensagens se você atender às seguintes condições:
1. O [status do número de telefone](https://www.facebook.com/business/help/896873687365001) é **Connected**
2. A [classificação de qualidade do número de telefone](https://www.facebook.com/business/help/896873687365001) é **Medium** ou **High**
3. Nos últimos sete dias, você iniciou X ou mais conversas com usuários únicos, onde X é seu limite de envio de mensagens atual dividido por 2

Então, para ir de 100 mil para ilimitado, você deve enviar pelo menos 50.000 conversas iniciadas pela empresa em um período de 7 dias.

#### Quanto tempo leva para aumentar meus limites de envio de mensagens? {#how-long-does-it-take-to-increase-my-messaging-limits}
Se todas as condições anteriores forem atendidas, você pode aumentar seu limite de envio de mensagens de 1 mil para ilimitado em 4 dias.

#### Onde posso ver meu limite de envio de mensagens atual? {#where-can-i-see-my-current-messaging-limit}
Você pode verificar seus limites de envio de mensagens atuais na guia **WhatsApp Manager > Overview Dashboard > Insights**.

#### O que acontece se eu tentar enviar mensagens quando já atingi meu limite de envio de mensagens? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Se você tentar enviar uma Campaign ou Canvas para mais usuários únicos do que seu limite atual permite, as mensagens não serão enviadas. A Braze continuará tentando reenviar as mensagens se/quando seu limite de envio de mensagens aumentar por até um dia.

#### Meu limite de envio de mensagens pode diminuir? {#can-my-messaging-limit-decrease}
Sim, se a classificação de qualidade do seu número de telefone cair muito, você corre o risco de o WhatsApp diminuir seu limite de envio de mensagens. A Braze recomenda que você se inscreva e seja notificado sobre atualizações relacionadas à qualidade do WhatsApp, incluindo atualizações no status do seu número de telefone e no nível do limite de envio de mensagens. Você pode se inscrever para notificações diretamente no dashboard do WhatsApp Manager.

#### Quais fatores afetam a classificação de qualidade do número de telefone, e o que acontece quando minha classificação de qualidade cai muito? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Os fatores que afetam a classificação de qualidade do número de telefone incluem um usuário final bloquear uma empresa (e os motivos que ele fornece ao bloquear a empresa) e um usuário final denunciar uma empresa.

Quando a classificação de qualidade está baixa, o status do número de telefone muda de **Connected** para **Flagged**. Se a qualidade não melhorar em sete dias, o status retorna para **Connected**. No entanto, o limite de envio de mensagens diminuirá para o próximo nível. Por exemplo, um número de telefone que costumava ter um limite de envio de mensagens de 100.000 agora tem um limite de envio de mensagens de 10.000.

#### Qual é o limite de throughput da Meta? {#what-is-the-meta-throughput-limit}
A Meta tem seu próprio limite de throughput separado do limite de envio de mensagens da WABA. O limite padrão que a API em nuvem suporta é de 80 mensagens por segundo. Se você acha que suas Campaigns excederão esse limite, pode [solicitar](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) que seu limite seja aumentado. A Meta recomenda que você envie essa solicitação com pelo menos três dias de antecedência dos envios da Campaign.

### Modelos e criador do WhatsApp {#whatsapp-templates-and-composer}

#### O que é um modelo de WhatsApp? {#what-is-a-whatsapp-template}
O WhatsApp exige que todas as mensagens iniciadas pela empresa comecem usando um modelo aprovado. O modelo inclui o texto da mensagem, junto com mídia rica opcional, como imagens, chamadas para ação e botões de resposta rápida. Após o WhatsApp aprovar os modelos, eles podem ser usados para compor uma mensagem de WhatsApp na Braze.

#### Onde crio, edito e gerencio meus modelos de WhatsApp? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Você criará, editará, gerenciará e enviará modelos para aprovação diretamente no WhatsApp Manager. Após sua WABA ser conectada à Braze, você verá todos os seus modelos no dashboard com um indicador de status. Se um modelo for rejeitado, você o reenviará diretamente pelo WhatsApp Manager. **Os modelos não podem ser criados ou editados diretamente na Braze.**

#### Quanto tempo leva para o WhatsApp revisar um envio de modelo? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
O processo de aprovação pode levar até 24 horas, mas frequentemente os modelos são processados em questão de horas ou minutos.

#### Quantos modelos posso ter em um determinado momento? {#how-many-templates-can-i-have-at-a-given-time}
Seu limite de modelos de mensagem depende do status de verificação da sua empresa. Você pode verificar seu limite na página **WhatsApp Manager > Message Templates**.

#### Como personalizo o texto e a mídia rica do modelo na Braze? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
O WhatsApp permite que parâmetros variáveis sejam inseridos nos modelos de mensagem. As mensagens não podem começar ou terminar com um parâmetro variável. Os parâmetros variáveis podem ser preenchidos com lógica Liquid na plataforma da Braze. Consulte [compondo uma mensagem de WhatsApp na Braze]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) para saber mais sobre parâmetros variáveis.

#### Meu modelo foi rejeitado. A Braze pode me ajudar a aprová-lo? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
A equipe da Braze não tem visibilidade sobre rejeições de modelos. Você deve trabalhar diretamente com seu WhatsApp Business Manager para editar e reenviar o modelo. Certifique-se de fornecer um modelo de exemplo quando necessário. Verifique se seu modelo segue as políticas de [negócios](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) ou [comércio](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) da Meta.

#### A mídia rica pode ser segmentada ou personalizada na Braze? {#can-the-rich-media-be-targeted-or-personalized-in-braze}
As imagens podem ser carregadas da biblioteca de mídia, mas não podem ser segmentadas dinamicamente. Para URLs, a última parte do link pode ser [preenchida dinamicamente usando Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

#### Que tipo de mídia rica é compatível com os modelos de WhatsApp? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Você pode adicionar imagens, chamadas para ação (URL ou número de telefone) e botões de resposta rápida aos modelos de WhatsApp. Você pode adicionar esses elementos ao criar modelos diretamente no WhatsApp.

#### E se meu modelo foi sinalizado incorretamente por violar a Política de Comércio do WhatsApp? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Se você acredita que a Meta sinalizou seu modelo incorretamente, use o link de revisão no e-mail do WhatsApp para solicitar uma reanálise. A equipe do WhatsApp Business analisa a decisão e a reverte se for apropriado.

#### Por que meu modelo importado do WhatsApp mostra "Message Incomplete" no criador? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
O aviso "Message Incomplete" aparece quando os campos de variáveis obrigatórios do modelo não estão preenchidos com valores válidos no criador.

Quando você cria modelos usando o [Construtor de modelos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), a Braze renumera as variáveis em marcadores sequenciais ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %}, e assim por diante). Modelos criados externamente no WhatsApp Manager da Meta podem ainda incluir padrões que tornam o mapeamento de variáveis propenso a erros, como:

- Numeração não sequencial (por exemplo, {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Variáveis ausentes na sequência (por exemplo, pulando {% raw %}`{{2}}`{% endraw %})
- Variáveis que começam com um número diferente de 1

Para resolver isso, edite seu modelo no WhatsApp Manager da Meta para usar formatação de marcadores sequenciais e reimporte-o na Braze. Na Braze, confirme que cada campo de variável obrigatório está preenchido com um valor Liquid válido.

### Entregabilidade e cobrança {#deliverability-and-billing}

#### Por que uma mensagem não seria entregue? {#why-would-a-message-not-be-delivered}
Existem vários motivos pelos quais uma mensagem pode não ser entregue, incluindo problemas de rede e o dispositivo estar desligado.

#### Se uma mensagem não for entregue, serei cobrado? {#if-a-message-is-not-delivered-will-i-be-billed}
Não. Se uma mensagem não for entregue, você não será cobrado.

#### O que acontece se um usuário final bloquear minha empresa? {#what-happens-if-an-end-user-blocks-my-business}
Se um usuário final bloquear sua empresa, as mensagens subsequentes que você tentar enviar não serão entregues, e você não será cobrado.

#### O que acontece se um usuário final denunciar uma mensagem? {#what-happens-if-an-end-user-reports-a-message}
Se um usuário final denunciar uma mensagem, você ainda poderá enviar mensagens subsequentes para esse usuário. No entanto, a denúncia pode afetar sua classificação de qualidade no canal.

#### Se um usuário final bloquear ou denunciar minha empresa, o status de inscrição dele será atualizado na Braze? {#if-an-end-user-blocks-or-reports-my-business-will-their-subscription-status-be-updated-in-braze}
Não. O status de inscrição na Braze não será atualizado.

#### As mensagens de resposta do WhatsApp são gratuitas? {#are-whatsapp-response-messages-free}

As mensagens de resposta compostas no editor de Campaign ou Canvas da Braze (não modelos aprovados do WhatsApp) são tratadas como mensagens de serviço pela Meta. Mensagens de serviço enviadas por meio da integração nativa de WhatsApp da Braze não consomem Action Credits quando são enviadas como [mensagens de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) dentro de uma janela de atendimento ao cliente aberta.

| Tipo de mensagem | Action Credits | Observações |
|---|---|---|
| Mensagem de resposta (resposta de entrada) | Não consumidos | Composta na Braze; não é um modelo aprovado pela Meta. |
| Mensagem de modelo | Consumidos | Modelos de marketing, utilidade, autenticação e oferta por tempo limitado são cobrados por envio. |
| Modelo de utilidade na janela de serviço | Não consumidos pela Meta | A Meta não cobra por modelos de utilidade enviados dentro de 24 horas de uma mensagem iniciada pelo usuário. O consumo de Action Credits segue seu contrato. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Action Credits de mensagens de resposta" }

Para fluxos de Canvas em que os usuários tocam em respostas rápidas após a janela original de 24 horas, consulte [Respostas rápidas e mensagens de entrada fora da janela de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### O que acontece se um usuário responder ou tocar em uma resposta rápida após o fechamento da janela de 24 horas? {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
Uma nova janela de atendimento ao cliente de 24 horas é aberta. Consulte [Respostas rápidas e mensagens de entrada fora da janela de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Preciso configurar meu Action Path do Canvas para 31 dias para respostas rápidas do WhatsApp? {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
Não. A duração padrão do Action Path é suficiente. Consulte [Respostas rápidas e mensagens de entrada fora da janela de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Posso ver quantos créditos de WhatsApp uma Campaign ou Canvas específico consumiu? {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
Não no dashboard da Braze atualmente. A análise de dados de Campaigns e Canvas mostra envios, entregas e falhas, mas não o consumo de créditos por mensagem. As contagens de envio não correspondem diretamente ao uso de créditos porque a categoria do modelo e o tipo de mensagem afetam a cobrança de formas diferentes. Para detalhes de cobrança, consulte [As mensagens de resposta do WhatsApp são gratuitas?](#are-whatsapp-response-messages-free).

### Integrações, dados e relatórios {#integrations-data-and-reporting}

#### A Braze oferece suporte a casos de uso de atendimento ao cliente, como chatbots e chat assistido por humanos para WhatsApp? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Não oferecemos suporte a chatbots ou chat assistido por humanos dentro da Braze ou por meio de integrações diretas.

Se você já usa o WhatsApp como canal de atendimento ao cliente, recomendamos que mantenha sua configuração atual e crie uma nova WABA via Braze para envio de mensagens de marketing. Essa WABA exigirá um novo número de telefone.

#### Como posso "conectar" meu envio de mensagens de atendimento ao cliente com meu envio de mensagens de marketing via Braze? {#how-can-i-bridge-the-gap-between-my-customer-support-messaging-and-my-marketing-messaging-via-braze}
Você pode usar as propriedades Liquid do WhatsApp para encaminhar o conteúdo de mensagens de entrada do WhatsApp (incluindo corpo da mensagem e URLs de mídia) da Braze para outras plataformas, incluindo qualquer ferramenta de atendimento ao cliente. Para mais detalhes, consulte nossas [Tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Para enviar informações para a Braze, por exemplo, para indicar que um usuário está em uma conversa de suporte ativa, você pode registrar um atributo personalizado (como um booleano "tem chat de suporte existente = verdadeiro/falso") e usar isso como critério de segmentação nas suas Campaigns de marketing. Você também pode usar deep links entre dois threads de chat para direcionar os usuários ao thread de suporte a partir do thread de marketing e vice-versa.

#### A Braze armazena as respostas dos usuários? {#does-braze-store-user-responses}
As mensagens são armazenadas apenas pelo tempo necessário para processá-las. Para acessar as mensagens dos usuários, use Currents.

#### Quais métricas estão disponíveis no dashboard da Braze? {#what-metrics-are-available-in-the-braze-dashboard}
Você pode ver destinatários únicos, envios, entregas, leituras e falhas no dashboard da Braze. Observe que os recibos de leitura dos usuários finais devem estar "Ativados" para que a Braze rastreie as leituras. Você também pode configurar eventos de conversão para monitorar o desempenho da Campaign, de forma semelhante a outros canais.

#### O que é uma conversa do WhatsApp? {#what-is-a-whatsapp-conversation}
O WhatsApp é um canal focado em mensagens bidirecionais e, portanto, se baseia em conversas (em vez do número de mensagens individuais). Uma conversa é um thread de 24 horas entre uma empresa e um usuário final.

- **Conversa iniciada pela empresa**: Uma conversa em que a empresa começa enviando uma mensagem de modelo aprovado para o usuário final. Assim que a empresa envia uma mensagem, o período de 24 horas começa.
- **Conversa iniciada pelo usuário**: Uma conversa em que o usuário final envia uma mensagem para a empresa. Quando a empresa envia uma mensagem em resposta, o período de 24 horas começa.