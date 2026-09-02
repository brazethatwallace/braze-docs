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
- [Contas do WhatsApp Business](#whatsapp-business-accounts)
- [Número de telefone da conta do WhatsApp Business](#whatsapp-business-account-phone-numbers)
- [Aceitação e gerenciamento de inscrições](#opt-in-and-subscription-management)
- [Limites de envio de mensagens e classificação de qualidade](#messaging-limits-and-quality-rating)
- [Modelos e criador do WhatsApp](#whatsapp-templates-and-composer)
- [Entregabilidade e faturamento](#deliverability-and-billing)
- [Integrações, dados e relatórios](#integrations-data-and-reporting)
- [Mídia e imagens](#media-and-images)

### Contas do WhatsApp Business {#whatsapp-business-accounts}

#### Como crio uma conta do WhatsApp Business? {#how-do-i-create-a-whatsapp-business-account}
Recomendamos criar sua conta do WhatsApp Business (WABA) pelo fluxo de cadastro integrado no dashboard da Braze.

#### Já tenho uma conta Meta Business. Ainda preciso de uma conta do WhatsApp Business? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Sim, você ainda precisa criar uma conta do WhatsApp Business. Recomendamos [vincular sua WABA à sua conta Meta Business principal]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### Como acesso minha conta do WhatsApp Business? {#how-do-i-access-my-whatsapp-business-account}
Após concluir o fluxo de cadastro integrado, você pode acessar sua conta em business.Facebook.com navegando até a [seção do WhatsApp](https://business.facebook.com/wa/manage/home).

#### Posso conectar várias WABAs à Braze? {#can-i-connect-multiple-wabas-to-braze}
Sim, você pode adicionar até 10 contas do WhatsApp Business por espaço de trabalho, e cada conta pode estar vinculada a um Meta Business Manager diferente.

![Diagrama do ecossistema Braze e WhatsApp, mostrando como espaços de trabalho e contas do WhatsApp Business se conectam: você pode conectar um grupo de inscrições a um número de telefone, várias contas do WhatsApp Business a um espaço de trabalho e um espaço de trabalho a vários Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### Posso alterar a moeda da minha conta do WhatsApp Business? {#can-i-change-my-whatsapp-business-account-currency}
Não. A Meta controla a moeda da sua conta do WhatsApp Business, e a Braze não pode alterá-la ou convertê-la. Para usar uma moeda diferente, [crie uma conta do WhatsApp Business separada]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) com essa moeda, ou entre em contato com o suporte da Meta para saber se eles podem atualizar a moeda na sua conta existente.

#### O que é verificação de empresa? {#what-is-business-verification}
A verificação de empresa é um conceito do WhatsApp usado para garantir que a marca é um negócio legítimo. Ela pode ser concluída no WhatsApp Manager. A verificação de empresa também é necessária para escalar o envio de mensagens. Sem a verificação de empresa, os clientes só podem enviar mensagens para até 250 usuários finais únicos em um período contínuo de 24 horas.

#### O que é uma conta comercial oficial? {#what-is-an-official-business-account}
A OBA (conta comercial oficial) exibe a marca de verificação verde ao lado do seu nome de exibição e é opcional. Você pode solicitar uma conta comercial oficial após concluir a verificação de empresa. Note que a verificação de empresa e a conta comercial oficial são conceitos diferentes no WhatsApp.

#### Por que meu nome de exibição do WhatsApp Business pode ser rejeitado? {#why-might-my-whatsapp-business-display-name-be-rejected}
As rejeições de nome de exibição do WhatsApp Business são controladas pela Meta. Se seu nome de exibição for rejeitado, consulte as [diretrizes de nome de exibição do WhatsApp](https://faq.whatsapp.com/793641088597363).

Se seu nome de exibição atende às diretrizes e ainda está sendo rejeitado, a Braze não consegue ver os motivos específicos. No entanto, o motivo mais comum para rejeição é que a presença online da empresa é muito baixa, ou a empresa está divulgando [produtos regulamentados ou restritos](https://business.whatsapp.com/policy#further-guidance).

Para mais orientações sobre rejeições de nome de exibição, consulte [Recursos da Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources).

### Números de telefone da conta do WhatsApp Business {#whatsapp-business-account-phone-numbers}
#### Preciso de um número de telefone para minha conta do WhatsApp Business? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Sim, você precisa de um número ao qual tenha acesso. Será solicitado que você verifique seu número de telefone com autenticação de dois fatores durante o fluxo de cadastro integrado. O número de telefone não pode ser usado em outras contas do WhatsApp (comerciais ou pessoais).

#### Quais tipos de números de telefone são compatíveis com o WhatsApp? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Consulte os requisitos da Meta para [números de telefone](https://developers.facebook.com/docs/whatsapp/phone-numbers) para saber mais.

#### Posso usar um número de telefone em várias WABAs? {#can-i-use-one-phone-number-across-multiple-wabas}
Não. Um número de telefone não pode ser compartilhado entre várias WABAs.

#### Preciso de um tipo específico de número de telefone para enviar mensagens para países específicos? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
Não. O WhatsApp permite que você envie mensagens para usuários finais a partir de qualquer número de telefone compatível, em qualquer país. Consulte os requisitos da Meta para [números de telefone](https://developers.facebook.com/docs/whatsapp/phone-numbers) para saber mais.

#### Como os números de telefone dos usuários precisam ser armazenados na Braze? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Os números de telefone dos usuários precisam ser armazenados no [formato E.164]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting).

#### Posso importar números de telefone dos usuários? {#can-i-import-user-phone-numbers}
Sim. Você pode [importar números de telefone dos usuários]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

### Aceitação e gerenciamento de inscrições {#opt-in-and-subscription-management}

#### Preciso coletar aceitação para enviar mensagens de marketing para usuários finais no WhatsApp? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Sim, o WhatsApp exige que as empresas [coletem consentimento de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para enviar mensagens de marketing a usuários finais.

#### Posso enviar mensagens proativas para usuários finais no WhatsApp para coletar consentimento de aceitação? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Se você optar por enviar mensagens proativas para usuários finais, sua primeira mensagem iniciada pela empresa deve perguntar ao usuário se ele deseja receber mensagens de marketing da sua empresa e deve cumprir os requisitos da Meta para [obter aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Lembre-se de que o WhatsApp monitora a reputação da sua empresa no canal, então a prática recomendada é ser explícito com os usuários finais e enviar apenas mensagens que eles indicaram querer receber.

#### Preciso coletar o número de telefone do usuário final quando coleto a aceitação? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Você precisa ter o número de telefone do usuário final no perfil da Braze para enviar mensagens.
- Se você já tem o número, não precisa coletá-lo durante a aceitação.
- Se você não tem o número do usuário final, seu método de aceitação deve incluir a captura do número de telefone.

#### Como atualizo o status de inscrição dos usuários finais que aceitaram? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
O gerenciamento de inscrições do canal WhatsApp funciona de forma semelhante ao de outros canais da Braze. Consulte [Gerenciando inscrições de usuários]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) para saber mais.

#### Se já tenho uma lista de usuários que aceitaram receber mensagens de marketing no WhatsApp, como atualizo o status de inscrição deles na Braze? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Você pode atualizar o status de inscrição via [importação de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional).

#### Quais métodos devo usar para coletar aceitações? {#what-methods-should-i-use-to-collect-opt-ins}
A Braze recomenda consultar as [diretrizes da Meta para métodos de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para manter a conformidade. Consulte [Aceitação e cancelamento]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) para métodos de configuração de Canvas e Campaign.

#### A aceitação dupla é obrigatória para o WhatsApp? {#is-double-opt-in-required-for-whatsapp}
Não, a aceitação dupla não é obrigatória.

#### Como meus usuários cancelam o recebimento de mensagens do WhatsApp? {#how-do-my-users-opt-out-of-whatsapp-messages}
Seus usuários podem cancelar de duas formas:
1. Configure uma mensagem de entrada do WhatsApp com uma palavra específica de cancelamento e use um webhook para atualizar o status de inscrição do usuário.
2. Adicione uma resposta rápida de cancelamento no modelo do WhatsApp, com um webhook correspondente para atualizar.

#### Posso usar um grupo de inscrições do WhatsApp na Braze se envio mensagens do WhatsApp por terceiros? {#can-i-use-a-braze-whatsapp-subscription-group-if-i-send-whatsapp-messages-through-a-third-party}
Não. Os grupos de inscrições do WhatsApp na Braze se aplicam a mensagens enviadas pelo canal WhatsApp da Braze. Se você envia mensagens do WhatsApp por um provedor terceirizado ou integrações personalizadas fora de Campaigns e Canvas do WhatsApp da Braze, você pode armazenar o consentimento de aceitação em um atributo personalizado (ou seu próprio modelo de inscrição) e usar esse atributo para segmentação e elegibilidade. Para padrões relacionados quando a Braze é dona do número do WhatsApp, consulte [Como conecto suporte e marketing do WhatsApp na Braze?](#how-do-i-connect-whatsapp-support-and-marketing-in-braze).

### Limites de envio de mensagens e classificação de qualidade {#messaging-limits-and-quality-rating}

#### O que são limites de envio de mensagens? {#what-are-messaging-limits}
Os limites de envio de mensagens são um conceito de integridade do WhatsApp. Eles determinam o número máximo de conversas iniciadas pela empresa que cada número de telefone pode iniciar em um período contínuo de 24 horas. Existem quatro níveis de limite de envio: 1 mil, 10 mil, 100 mil e ilimitado.

#### Como aumento meu limite de envio de mensagens? {#how-do-i-increase-my-messaging-limit}
O WhatsApp aumentará seu limite de envio de mensagens se você atender às seguintes condições:
1. O [status do número de telefone](https://www.facebook.com/business/help/896873687365001) é **Conectado**
2. A [classificação de qualidade do número de telefone](https://www.facebook.com/business/help/896873687365001) é **Média** ou **Alta**
3. Nos últimos sete dias, você iniciou X ou mais conversas com usuários únicos, onde X é o seu limite de envio atual dividido por 2

Então, para passar de 100 mil para ilimitado, você deve enviar pelo menos 50.000 conversas iniciadas pela empresa em um período de 7 dias.

#### Quanto tempo leva para aumentar meus limites de envio? {#how-long-does-it-take-to-increase-my-messaging-limits}
Se todas as condições anteriores forem atendidas, você pode aumentar seu limite de envio de 1 mil para ilimitado em 4 dias.

#### Onde posso ver meu limite de envio atual? {#where-can-i-see-my-current-messaging-limit}
Você pode verificar seus limites de envio atuais na guia **WhatsApp Manager > Overview Dashboard > Insights**.

#### O que acontece se eu tentar enviar mensagens quando já atingi meu limite de envio? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Se você tentar enviar uma Campaign ou Canvas para mais usuários únicos do que seu limite atual permite, as mensagens falharão no envio. A Braze continuará tentando reenviar as mensagens se/quando seu limite de envio aumentar, por até um dia.

#### Meu limite de envio pode diminuir? {#can-my-messaging-limit-decrease}
Sim, se a classificação de qualidade do seu número de telefone cair muito, há risco do WhatsApp diminuir seu limite de envio. A Braze recomenda que você se inscreva e seja notificado sobre atualizações relacionadas à qualidade do WhatsApp, incluindo atualizações no status do seu número de telefone e no nível do limite de envio. Você pode se inscrever para notificações diretamente no dashboard do WhatsApp Manager.

#### Quais fatores afetam a classificação de qualidade do número de telefone e o que acontece quando minha classificação cai muito? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Os fatores que afetam a classificação de qualidade do número de telefone incluem um usuário final bloqueando uma empresa (e os motivos fornecidos ao bloquear) e um usuário final denunciando uma empresa.

Quando a classificação de qualidade está baixa, o status do número de telefone muda de **Conectado** para **Sinalizado**. Se a qualidade não melhorar em sete dias, o status retorna para **Conectado**. No entanto, o limite de envio diminuirá para o próximo nível. Por exemplo, um número de telefone que tinha um limite de 100.000 agora tem um limite de 10.000.

#### Qual é o limite de throughput da Meta? {#what-is-the-meta-throughput-limit}
A Meta tem seu próprio limite de throughput, separado do limite de envio da WABA. O limite padrão que a API Cloud suporta é de 80 MPS. Se você acha que suas Campaigns excederão esse limite, pode [solicitar](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) que seu limite seja aumentado. A Meta recomenda que você envie essa solicitação com pelo menos três dias de antecedência dos envios de Campaigns.

### Modelos e criador do WhatsApp {#whatsapp-templates-and-composer}

#### O que é um modelo do WhatsApp? {#what-is-a-whatsapp-template}
O WhatsApp exige que todas as mensagens iniciadas pela empresa comecem usando um modelo aprovado. O modelo inclui o texto da mensagem, junto com mídia rica opcional, como imagens, chamadas para ação e botões de resposta rápida. Após o WhatsApp aprovar os modelos, eles podem ser usados para compor uma mensagem do WhatsApp na Braze.

#### Onde crio, edito e gerencio meus modelos do WhatsApp? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Você pode criar e enviar modelos na Braze usando o [Construtor de Modelos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), ou no WhatsApp Manager da Meta. Modelos criados em qualquer um dos locais aparecem no dashboard da Braze com um indicador de status. Após o envio, campos bloqueados requerem reaprovação da Meta; consulte [limitações de edição no FAQ do Construtor de Modelos]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder#can-i-edit-a-template-after-its-been-approved) para detalhes.

#### Quanto tempo leva para o WhatsApp revisar o envio de um modelo? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
O processo de aprovação pode levar até 24 horas, mas frequentemente os modelos são processados em questão de horas ou minutos.

#### Quantos modelos posso ter ao mesmo tempo? {#how-many-templates-can-i-have-at-a-given-time}
Seu limite de modelos de mensagem depende do seu status de verificação de empresa. Você pode verificar seu limite na página **WhatsApp Manager > Message Templates**.

#### Como personalizo o texto e a mídia rica dos modelos na Braze? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
O WhatsApp permite que parâmetros variáveis sejam inseridos nos modelos de mensagem. As mensagens não podem começar ou terminar com um parâmetro variável. Os parâmetros variáveis podem ser preenchidos com lógica Liquid na plataforma da Braze. Consulte [criando uma mensagem do WhatsApp na Braze]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) para saber mais sobre parâmetros variáveis.

#### Meu modelo foi rejeitado. A Braze pode me ajudar a aprová-lo? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
A equipe da Braze não tem visibilidade sobre rejeições de modelos. Você deve trabalhar diretamente com seu WhatsApp Business Manager para editar e reenviar o modelo. Certifique-se de fornecer um modelo de exemplo quando necessário. Verifique se seu modelo segue as políticas [comerciais](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) ou de [comércio](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) da Meta.

#### Mídia rica pode ser direcionada ou personalizada na Braze? {#can-rich-media-be-targeted-or-personalized-in-braze}
Sim. Você pode carregar imagens estáticas da biblioteca de mídia, ou adicionar imagens por URL e personalizá-las com [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). URLs de imagens suportam lógica Liquid completa em qualquer parte da URL. Isso se aplica a mensagens de modelo e mensagens de resposta (mensagens de mídia e layouts de resposta rápida). Para detalhes, consulte [Imagens dinâmicas]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#dynamic-images).

#### Que tipo de mídia rica é compatível com modelos do WhatsApp? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Você pode adicionar imagens, chamadas para ação (URL ou número de telefone) e botões de resposta rápida aos modelos do WhatsApp. Você pode adicionar esses elementos ao criar modelos diretamente no WhatsApp.

#### E se meu modelo foi sinalizado incorretamente por violar a Política Comercial do WhatsApp? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Se você acredita que a Meta sinalizou seu modelo incorretamente, use o link de revisão no e-mail do WhatsApp para solicitar uma reavaliação. A equipe do WhatsApp Business revisa a decisão e a reverte se apropriado.

#### Por que meu modelo importado do WhatsApp mostra "Message Incomplete" no criador? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
O aviso "Message Incomplete" aparece quando os espaços de variáveis obrigatórios do modelo não estão preenchidos com valores válidos no criador.

Quando você cria modelos usando o [Construtor de Modelos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), a Braze renumera as variáveis em espaços reservados sequenciais ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %} e assim por diante). Modelos criados externamente no WhatsApp Manager da Meta podem ainda incluir padrões que tornam o mapeamento de variáveis propenso a erros, como:

- Numeração não sequencial (por exemplo, {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Variáveis ausentes na sequência (por exemplo, pulando {% raw %}`{{2}}`{% endraw %})
- Variáveis que começam com um número diferente de 1

Para resolver isso, edite seu modelo no WhatsApp Manager da Meta para usar formatação sequencial de espaços reservados e reimporte-o na Braze. Na Braze, confirme que cada campo de variável obrigatório está preenchido com um valor Liquid válido.

#### Por que minha Campaign do WhatsApp não está enviando apesar do modelo aparecer corretamente na prévia? {#why-is-my-whatsapp-campaign-not-sending-despite-template-previewing}
Se seu modelo aparece corretamente na prévia, mas o registro de processamento mostra **Abort** com detalhes "Param text cannot have new-line/tab characters or more than 4 consecutive spaces", verifique os valores dos parâmetros com Liquid na sua mensagem. O WhatsApp exige que os valores de texto dos parâmetros não contenham:

- Caracteres de nova linha
- Caracteres de tabulação
- Mais de 4 espaços consecutivos

Confirme que qualquer lógica Liquid que preenche os parâmetros do modelo remove esses caracteres ou formata o texto adequadamente antes do envio.

### Entregabilidade e faturamento {#deliverability-and-billing}

#### Por que uma mensagem não seria entregue? {#why-would-a-message-not-be-delivered}
Existem vários motivos pelos quais uma mensagem pode falhar na entrega, incluindo problemas de rede e o dispositivo estar desligado.

#### Se uma mensagem não for entregue, serei cobrado? {#if-a-message-is-not-delivered-will-i-be-billed}
Não. Se uma mensagem não for entregue, você não será cobrado.

#### O que acontece se um usuário bloquear minha empresa? {#what-happens-if-a-user-blocks-my-business}
Se um usuário bloquear sua empresa, as mensagens subsequentes que você tentar enviar não serão entregues e você não será cobrado. O status de inscrição do usuário não será atualizado.

#### O que acontece se um usuário denunciar uma mensagem? {#what-happens-if-a-user-reports-a-message}
Se um usuário denunciar uma mensagem, você ainda pode enviar mensagens subsequentes para ele. No entanto, a denúncia pode afetar sua classificação de qualidade no canal. O status de inscrição do usuário não é atualizado.

#### Como posso excluir usuários que denunciaram minha conta do WhatsApp de lançamentos futuros? {#how-can-i-exclude-users-who-report-my-whatsapp-account-from-upcoming-launches}
A Braze não recebe notificações do WhatsApp quando sua conta é sinalizada ou denunciada, então você não pode identificar ou excluir automaticamente esses usuários na Braze. Usuários que denunciam sua conta podem permanecer no seu grupo de inscrições do WhatsApp e continuar elegíveis para mensagens futuras.

No entanto, você pode configurar uma Campaign que dispara quando um usuário responde com uma palavra-chave de cancelamento, o que automaticamente cancela a inscrição usando o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Para saber mais, consulte [Processo de aceitação e cancelamento do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

#### A Braze suporta fallback automático de SMS quando a entrega do WhatsApp falha? {#does-braze-support-automatic-sms-fallback-when-whatsapp-delivery-fails}

Não. A Braze não oferece um caminho nativo de fallback do WhatsApp para SMS. Para tentar novamente em outro canal, segmente os usuários com envios do WhatsApp que falharam (por exemplo, por meio de eventos de falha no Currents) e direcione uma Campaign de SMS ou e-mail.

#### Mensagens de resposta do WhatsApp são gratuitas? {#are-whatsapp-response-messages-free}

Mensagens de resposta compostas no editor de Campaign ou Canvas da Braze (não modelos aprovados do WhatsApp) são tratadas como mensagens de serviço pela Meta. Até 30 de setembro de 2026, mensagens de serviço enviadas pela integração nativa do WhatsApp da Braze não consomem Action Credits quando são enviadas como [mensagens de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) dentro de uma janela de atendimento ao cliente aberta.

A partir de 1º de outubro de 2026, mensagens de serviço consomem Action Credits por mensagem entregue. Essa classificação depende da própria mensagem: uma resposta sem modelo é uma mensagem de serviço, mesmo quando a conversa começou com um modelo. Se você responder com um modelo aprovado de marketing, utilidade ou autenticação, a mensagem é cobrada de acordo com sua categoria de modelo.

| Tipo de mensagem | Action Credits | Observações |
|---|---|---|
| Mensagem de resposta (resposta de entrada) | Não consumidos até 30 de setembro de 2026; consumidos a partir de 1º de outubro de 2026 | Composta na Braze; não é um modelo aprovado pela Meta. A Meta classifica como mensagem de serviço. |
| Mensagem de modelo | Consumidos | Modelos de marketing, utilidade, autenticação e oferta por tempo limitado são cobrados por envio. |
| Modelo de utilidade em janela de serviço | Não cobrados pela Meta até 30 de setembro de 2026; cobrados a partir de 1º de outubro de 2026 | O consumo de Action Credits segue o seu contrato. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Action Credits de mensagens de resposta" }

Para fluxos de Canvas em que os usuários tocam em respostas rápidas após a janela original de 24 horas, consulte [Respostas rápidas e mensagens de entrada fora da janela de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### O que acontece se um usuário responder ou tocar em uma resposta rápida após o fechamento da janela de 24 horas? {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
Uma nova janela de atendimento ao cliente de 24 horas é aberta. Consulte [Respostas rápidas e mensagens de entrada fora da janela de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Preciso configurar meu Action jornada do Canvas para 31 dias para respostas rápidas do WhatsApp? {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
Não. A duração padrão do Action jornada é suficiente. Consulte [Respostas rápidas e mensagens de entrada fora da janela de 24 horas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Posso ver quantos créditos do WhatsApp uma Campaign ou Canvas específico consumiu? {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
Não no dashboard da Braze atualmente. As análises de Campaigns e Canvas mostram envios, entregas e falhas, mas não o consumo de créditos por mensagem. As contagens de envio não correspondem diretamente ao uso de créditos porque a categoria do modelo e o tipo de mensagem afetam o faturamento de forma diferente. Para detalhes de faturamento, consulte [Mensagens de resposta do WhatsApp são gratuitas?](#are-whatsapp-response-messages-free).

### Integrações, dados e relatórios {#integrations-data-and-reporting}

#### Por que o WhatsApp não aparece em Parceiros de Tecnologia? {#why-isnt-whatsapp-listed-under-technology-partners}
O WhatsApp aparece na página **Parceiros de Tecnologia** quando o WhatsApp está ativado para sua empresa. Se você não vê o WhatsApp nessa página, entre em contato com sua equipe de conta da Braze para confirmar que o WhatsApp está provisionado para seu dashboard.

#### A Braze suporta casos de uso de suporte ao cliente, como chatbots e chat assistido por humanos para o WhatsApp? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Não oferecemos suporte a chatbots ou chat assistido por humanos dentro da Braze ou por meio de integrações diretas.

Se você já usa o WhatsApp como canal de suporte ao cliente, recomendamos manter sua configuração atual e criar uma nova WABA via Braze para envio de mensagens de marketing. Essa WABA precisará de um novo número de telefone.

#### Como conecto suporte e marketing do WhatsApp na Braze? {#how-do-i-connect-whatsapp-support-and-marketing-in-braze}

Você pode usar propriedades Liquid do WhatsApp para encaminhar o conteúdo de mensagens de entrada do WhatsApp (incluindo corpo da mensagem e URLs de mídia) da Braze para outras plataformas, incluindo qualquer ferramenta de suporte ao cliente. Para detalhes, consulte nossas [Tags de personalização suportadas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Para enviar informações para a Braze, por exemplo, para indicar que um usuário está em uma conversa de suporte ativa, você pode registrar um atributo personalizado (como um booleano "tem chat de suporte existente = verdadeiro/falso") e usar isso como critério de segmentação em suas Campaigns de marketing. Você também pode criar deep links entre duas conversas para direcionar os usuários da conversa de marketing para a de suporte e vice-versa.

#### A Braze armazena as respostas dos usuários? {#does-braze-store-user-responses}
As mensagens são armazenadas apenas pelo tempo necessário para processá-las. Para acessar mensagens dos usuários, use o Currents.

#### Quais métricas estão disponíveis no dashboard da Braze? {#what-metrics-are-available-in-the-braze-dashboard}
Você pode ver destinatários únicos, envios, entregas, leituras e falhas no dashboard da Braze. Note que os recibos de leitura do usuário devem estar "Ativados" para que a Braze rastreie as leituras. Você também pode configurar eventos de conversão para monitorar o desempenho das Campaigns, de forma semelhante a outros canais.

#### O que é uma conversa do WhatsApp? {#what-is-a-whatsapp-conversation}
O WhatsApp é um canal focado em mensagens bidirecionais e, por isso, se baseia em conversas (em vez do número de mensagens individuais). Uma conversa é uma interação de 24 horas entre uma empresa e um usuário final.

- **Conversa iniciada pela empresa**: uma conversa em que a empresa inicia enviando uma mensagem de modelo aprovado ao usuário final. Assim que a empresa envia a mensagem, a janela de 24 horas começa.
- **Conversa iniciada pelo usuário**: uma conversa em que o usuário final envia uma mensagem para a empresa. Quando a empresa envia uma mensagem em resposta, a janela de 24 horas começa.

### Mídia e imagens {#media-and-images}

#### Por que as imagens não carregam quando enviadas como mensagem do WhatsApp? {#why-wont-images-load-when-sent-as-a-whatsapp-message}
Se os usuários relatam que as imagens nas mensagens do WhatsApp não são baixadas ou o ícone de download não responde, isso provavelmente se deve a um problema conhecido em versões mais antigas do app WhatsApp. Esse problema geralmente pode ser resolvido atualizando o dispositivo para a versão mais recente do WhatsApp.