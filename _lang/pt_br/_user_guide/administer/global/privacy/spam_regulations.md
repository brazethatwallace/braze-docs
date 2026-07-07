---
nav_title: Regulamentações de spam
article_title: Regulamentações de spam
page_order: 0
page_type: reference
description: "Este artigo fornece resumos e recursos sobre vários regulamentos sobre spam que podem afetar você ou seus usuários."
channel:
- email
- push
- SMS

---

# Regulamentações de spam {#spam-regulations}

> Há várias leis que regulam os remetentes de comunicações eletrônicas, incluindo e-mail, notificações por push e SMS. Você deve estar sempre ciente das [regulamentações locais](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country) que podem afetar você ou seus usuários.

A Braze está fornecendo informações relevantes com base em nossa própria pesquisa, mas você também deve consultar o texto completo dessas leis para obter detalhes completos e atualizados.

- [CAN-SPAM](#can-spam)
- [Lei anti-spam canadense](#casl)

## CAN-SPAM {#can-spam}

A Lei CAN-SPAM de 2003 regulamenta os remetentes de e-mail nos EUA que enviam "qualquer mensagem de e-mail cujo objetivo principal seja o anúncio comercial ou a promoção de um produto ou serviço comercial". Você pode ler mais detalhes no site oficial da [Federal Trade Commission](http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business).

Há sete requisitos principais para a CAN-SPAM:

1. Não use informações de cabeçalho falsas ou enganosas (como "From", "To" e "Reply-To")
2. Não use linhas de assunto enganosas
3. Identifique a mensagem como um anúncio
4. Informe aos destinatários onde você está localizado (como endereço físico)
5. Informe aos destinatários como podem optar por não receber seus futuros e-mails
6. Atenda prontamente aos pedidos de cancelamento de inscrição
7. Monitore o que outros estão fazendo em seu nome

E-mails de transação estão isentos dessas regras, com exceção da regra nº 1.

## Lei anti-spam canadense (CASL) {#casl}

Em 1º de julho de 2014, a Lei Anti-Spam Canadense (CASL) entrou em vigor para e-mails enviados a residentes canadenses. Você pode ler o texto completo da lei no site [Justice Laws Website](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) do Governo do Canadá. A lei basicamente diz que os destinatários canadenses de e-mails e notificações por push precisam fornecer consentimento "expresso ou implícito" para a sua comunicação com eles.

### CASL versus CAN-SPAM {#casl-versus-can-spam}

Existem algumas diferenças importantes entre a CASL e a CAN-SPAM, principalmente:

- A CASL se aplica ao local onde a mensagem é recebida, então remetentes fora do Canadá também são afetados
- Os destinatários da mensagem precisam fazer opt-in, em vez de descadastramento

### Responsabilidade {#liability}

Embora a CASL tenha um período de transição de três anos, terminando em 1º de julho de 2017, a Canadian Radio-Television and Telecommunications Commission (CRTC), o Competition Bureau e o Office of the Privacy Commissioner of Canada podem iniciar investigações e litígios durante esse período. Ao final do período de transição, indivíduos também podem processar entidades que acreditem estar enviando spam.

### Mensagens isentas {#exempt-messages}

Os seguintes tipos de mensagens estão isentos dos requisitos da CASL:

- Mensagens abertas fora do Canadá
- Mensagens para familiares ou outras relações pessoais
- Mensagens para indivíduos associados ao seu negócio, incluindo colaboradores ou prestadores de serviço
- Mensagens fornecendo informações de garantia, recall de produto ou informações de segurança sobre um produto ou serviço que o destinatário usou ou comprou
- Mensagens fornecendo notificação de informações factuais sobre inscrição, associação ou conta
- Mensagens entregando um produto ou serviço, incluindo atualizações ou upgrades de produto

{% alert note %}
Esta não é a lista completa de isenções. Consulte o [texto completo da lei](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) para mais detalhes.
{% endalert %}

### Consentimento de mensagem {#message-consent}

A Braze exige consentimento explícito para todas as mensagens de e-mail e SMS/MMS.

#### Consentimento implícito {#implied-consent}

O consentimento implícito pode ser legalmente permitido em algumas jurisdições, mas não é suficiente para o envio de e-mails pela Braze. Nossa Política de Uso Aceitável vai além dos requisitos legais.

#### Consentimento expresso {#express-consent}

O consentimento expresso é uma confirmação escrita ou oral do destinatário da mensagem e só é válido se a mensagem incluir uma descrição clara e simples de:

- Por que o consentimento está sendo solicitado
- A pessoa ou organização que está solicitando o consentimento

## Filtros de spam {#spam-filters}

O fato de seus e-mails terem sido enviados com sucesso não significa que eles necessariamente foram vistos. Não existe uma solução única para evitar todos os filtros de spam, pois cada filtro é único na forma como avalia a "pontuação de spam" de um e-mail. No entanto, aqui estão algumas dicas para evitar que seus e-mails sejam rotulados como "spam".

### Obtenha permissão {#get-permission}

Um processo de double opt-in consiste em enviar um e-mail de acompanhamento com um link de confirmação após um opt-in inicial. Isso fornece validação de que os destinatários desejam receber seu conteúdo. Você pode ir ainda mais longe pedindo aos usuários que adicionem você à lista de contatos deles. Além disso, certifique-se de fazer suas listas de e-mail crescerem organicamente&#8212;listas compradas tendem a estar desatualizadas!


### Construa sua reputação {#build-your-reputation}

Certifique-se de definir expectativas quando as pessoas se inscrevem para receber seus e-mails. Seja explícito sobre o que você enviará e com que frequência. Então, incentive os usuários a interagir com suas campanhas de e-mail fornecendo conteúdo valioso. Ter conteúdo personalizado e relevante diminui a probabilidade de seus destinatários marcarem as mensagens como spam.

### Mantenha sua reputação {#maintain-your-reputation}

Esteja em contato constante com seus usuários para evitar que suas listas de e-mail fiquem desatualizadas. Esperar muito tempo para enviar uma mensagem pode fazer com que o destinatário se esqueça de você e marque você como spam. Mantenha suas listas de e-mail atualizadas implementando uma política de sunset para remover endereços de e-mail que geram bounce. As taxas de bounce são um fator-chave usado pelos provedores de acesso à internet para avaliar a reputação de um remetente.

### Verifique e teste {#check-and-test}

Certifique-se de que sua mensagem não contém nada que possa acionar filtros de spam. Isso inclui tags supérfluas de editores de texto externos como o Microsoft Word, formatação de texto anormal, uso excessivo de pontos de exclamação (!) e pontos de interrogação (?) como pontuação, escrever em LETRAS MAIÚSCULAS e palavras que acionam filtros de spam. Envie e-mails com conteúdo variado usando recursos de testes multivariantes para garantir que seus e-mails não estejam indo para spam.

## Canal de envio de mensagens {#messaging-channel}

### E-mail {#spam-email}

A qualidade da sua lista de e-mails é especialmente importante. Um punhado de e-mails ruins na sua lista pode arruinar a entrega para um milhão de bons usuários. Coletar uma lista de e-mails ruins gera bounces, bloqueios, hits em armadilhas de spam e derruba suas taxas de resposta. Remover e-mails que não têm atividade regularmente e eliminar bounces óbvios são o primeiro passo. Seja implementando opt-in (marcar a caixa), descadastramento (desmarcar a caixa), confirmação de opt-in (um e-mail que agradece pela inscrição e fornece um link de cancelamento de inscrição) ou double opt-in (um e-mail que exige um clique para confirmar), o que você deve considerar é a qualidade da lista.

### iOS {#spam-ios-windows}

No iOS, seus usuários sempre foram solicitados a fazer opt-in para notificações por push. A caixa de diálogo do iOS simplesmente aparece ao entrar no app e pede ao usuário para fazer opt-in para notificações do seu app. O usuário do app vê a mesma mensagem pop-up no momento em que abre o app pela primeira vez, então todos que estão na sua lista de notificações por push do iOS, por definição, fizeram opt-in.

### Android {#spam-android}

No Android, seus usuários podem ser considerados como tendo feito opt-in pelo consentimento implícito declarado na sua política de privacidade ou contrato de licença de usuário final. Você pode querer implementar um processo de opt-in expresso, talvez em uma tela inicial assim que o usuário inicia o app pela primeira vez. Visite o artigo [Práticas recomendadas de push]({{site.baseurl}}/user_guide/channels/push/best_practices) para mais detalhes. Você também pode orientar o usuário sobre quais tipos de notificações por push ele receberá, aumentando assim a taxa de opt-in.