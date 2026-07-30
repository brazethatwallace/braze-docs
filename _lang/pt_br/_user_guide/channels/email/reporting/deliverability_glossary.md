---
nav_title: Glossário de entregabilidade de e-mail
article_title: Glossário de entregabilidade de e-mail
layout: glossary_page
glossary_top_header: "Glossário de entregabilidade de e-mail"
glossary_top_text: "Este glossário define termos comuns de entregabilidade de e-mail e infraestrutura de e-mail que você pode encontrar ao enviar e-mails pela Braze."
page_order: 1
page_type: glossary
description: "Este glossário define termos comuns de entregabilidade de e-mail e infraestrutura de e-mail que você pode encontrar ao enviar e-mails pela Braze."
channel:
  - email

glossaries:
  - name: Allowlist
    description: Uma lista de contatos que o usuário considera aceitáveis para receber e-mails e que não devem ser filtrados ou enviados para a lixeira ou pasta de SPAM.
  - name: Block
    description: Um block bounce é o resultado de um e-mail não ser aceito para entrega pelo provedor de caixa de entrada. Muitos provedores de caixa de entrada bloqueiam e-mails de endereços IP ou domínios que foram reportados por enviar SPAM ou vírus, ou que possuem conteúdo que viola políticas de e-mail ou filtros de SPAM. O SendGrid usa "block" para se referir ao que normalmente é chamado de soft bounce. No SendGrid, um block ocorre quando um e-mail não é aceito para entrega por um motivo técnico ou temporário.
  - name: Blocklist
    description: Listas de endereços IP que foram reportados e listados como fontes conhecidas de SPAM. Existem blocklists públicas e privadas. As blocklists públicas são publicadas e disponibilizadas ao público — muitas vezes como um serviço gratuito, às vezes mediante pagamento.
  - name: Bounce
    description: Também conhecido como hard bounce, um endereço que sofreu bounce é permanentemente não entregável e é suprimido dos envios subsequentes. Para saber mais sobre bounces na Braze, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#bounces">Bounces</a> no glossário de análise de dados de e-mail.
  - name: Bulk folder
    description: Também chamada de pasta de lixo eletrônico ou pasta de SPAM em alguns clientes de e-mail.
  - name: CAN-SPAM Act
    description: "Lei dos EUA que regulamenta e-mails comerciais (nome completo: Controlling the Assault of Non-Solicited Pornography and Marketing Act of 2003)."
  - name: Click rate
    description: A taxa na qual os destinatários clicaram em um link dentro da mensagem. Para saber mais, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-clicks">Unique Clicks</a> no glossário de análise de dados de e-mail.
  - name: Content filters
    description: Filtros de software que bloqueiam e-mails com base em texto, palavras, frases ou informações de cabeçalho dentro do próprio e-mail.
  - name: Deferred
    description: Se uma mensagem não puder ser entregue na primeira tentativa, ela é considerada como adiada (deferred). A maioria dos e-mails adiados acaba sendo entregue.
  - name: Deliverability
    description: Na comunidade de entregabilidade, o foco principal é a capacidade de chegar à caixa de entrada. Essa taxa não é algo que a Braze pode rastrear diretamente, então você precisa usar outros dados disponíveis para fazer inferências sobre o posicionamento na caixa de entrada.
  - name: Delivery rate
    description: A taxa de entregas bem-sucedidas, independentemente do posicionamento na caixa de entrada ou de o e-mail ser aberto. Para saber mais, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#deliveries">Deliveries %</a> no glossário de análise de dados de e-mail.
  - name: DKIM
    description: DomainKeys Identified Mail permite que uma organização assuma a responsabilidade por uma mensagem enquanto ela está em trânsito. A organização é um manipulador da mensagem, seja como originador ou como intermediário. Sua reputação é a base para avaliar se a mensagem é confiável para entrega.
  - name: DMARC
    description: Domain-based Message Authentication, Reporting & Conformance é uma especificação técnica criada por organizações para reduzir phishing e fraude por e-mail. Atualmente é utilizada por todos os principais provedores de caixa de entrada, incluindo Google, Yahoo e Microsoft.
  - name: Drop
    description: O SendGrid mantém listas de e-mails para rastrear bounces, relatórios de SPAM e cancelamentos de inscrição para cada um de seus usuários. Se um usuário enviar uma mensagem para um endereço de e-mail que existe em uma dessas listas dentro de sua conta, o SendGrid automaticamente descarta a mensagem (ou seja, não envia para o endereço).
  - name: ESP (provedor de serviços de e-mail)
    description: Empresa que fornece capacidade de envio e transporte de e-mail para profissionais de marketing por e-mail. Muitas das plataformas atuais de marketing, CRM e engajamento do cliente incluem um componente de envio de e-mail e são comumente chamadas de ESPs em referência à capacidade de envio de e-mail. Exemplos incluem ConstantContact, MailChimp, Emarsys, Salesforce Marketing Cloud, Cheetah Digital e Sailthru.
  - name: Feedback loop (FBL)
    description: O mecanismo pelo qual os remetentes são notificados sobre relatórios de SPAM para que possam calcular uma taxa de relatórios de SPAM e remover o endereço de envios futuros.
  - name: Hard bounce
    description: Mensagem enviada para uma conta de e-mail inválida, encerrada ou inexistente. Normalmente, hard bounces podem ser identificados com um código de resposta SMTP da série 500. Para saber mais, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#hard-bounce">Hard Bounce</a> no glossário de análise de dados de e-mail.
  - name: IP
    description: Um número único atribuído a cada dispositivo conectado à Internet.
  - name: ISP (provedor de serviços de internet)
    description: Empresa que fornece serviços de Internet a consumidores, como AT&T, British Telecom, Comcast (Xfinity), Cox, Orange, Sky, Spectrum, Tiscali, TalkTalk e Virgin. Também inclui coloquialmente provedores de caixa de entrada como Gmail, Yahoo e Microsoft.
  - name: List hygiene
    description: O ato de manter uma lista para que hard bounces e nomes com inscrição cancelada sejam removidos dos envios.
  - name: List-Unsubscribe
    description: O cabeçalho List-Unsubscribe é um texto que você pode incluir na parte de cabeçalho das suas mensagens, permitindo que os destinatários vejam um botão de cancelamento de inscrição que podem selecionar para interromper automaticamente mensagens futuras.
  - name: Mailbox provider (MBP)
    description: O provedor de acesso a e-mail para os destinatários, como Gmail, Yahoo e Microsoft.
  - name: MX record
    description: Um registro MX é um tipo de registro de recurso no Sistema de Nomes de Domínio (DNS) que especifica como o e-mail da Internet deve ser roteado usando o Simple Mail Transfer Protocol (SMTP).
  - name: NDR (non-delivery report)
    description: Feedback de um receptor de e-mail quando ele opta por não aceitar um e-mail para entrega, na forma de uma resposta SMTP. NDRs são frequentemente chamados de bounces.
  - name: Opens unique rate
    description: A taxa na qual o pixel de rastreamento de abertura foi carregado, contando apenas destinatários únicos (sem duplicatas). Para saber mais, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-opens">Unique Opens</a> no glossário de análise de dados de e-mail.
  - name: Phishing
    description: Uma forma de roubo de identidade na qual um golpista usa um e-mail de aparência autêntica para enganar os destinatários e fazê-los fornecer informações pessoais sensíveis, como números de cartão de crédito ou conta bancária, números de seguro social e outras informações de identificação pessoal (IPI).
  - name: Re-engagement campaign
    description: Uma campanha de e-mail enviada para usuários inativos ou que não respondem, na tentativa de reconquistá-los e fazê-los interagir novamente com seus e-mails por meio de aberturas, cliques e conversões. Uma campanha de reengajamento pode ser enviada para inativos como uma campanha independente ou como uma série de campanhas.
  - name: Reverse DNS (rDNS)
    description: O processo no qual um endereço IP é correspondido corretamente a um nome de domínio, em vez de um nome de domínio ser correspondido a um endereço IP. Se um filtro ou programa de SPAM não conseguir corresponder o endereço IP ao nome de domínio, ele pode rejeitar o e-mail.
  - name: Smart Network Data Services (SNDS)
    description: Oferecido pelo Windows Live Hotmail, o SNDS fornece dados aos remetentes com base nos e-mails realmente enviados aos assinantes do Hotmail. As métricas reportadas incluem reclamações, resultados do filtro SmartScreen e ocorrências em spam traps.
  - name: Soft bounce
    description: Qualquer bounce devido a um problema temporário ou transitório, como "caixa de entrada cheia", "usuário acima da cota", "e-mail bloqueado por características semelhantes a SPAM", "mensagem rejeitada porque viola políticas da organização" ou "servidor temporariamente indisponível". O SendGrid chama esses casos de "blocks".<br><br>A entrega para qualquer soft bounce considerado um problema temporário (geralmente aqueles com um código SMTP 4xx) é tentada novamente até que a mensagem seja entregue ou 72 horas se passem. Se uma mensagem que sofreu soft bounce não puder ser entregue após 72 horas, novas tentativas de entrega são interrompidas e a falha na entrega da mensagem é contabilizada como um bounce. Para saber mais, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#soft-bounce">Soft Bounce</a> no glossário de análise de dados de e-mail.
  - name: Spam
    description: E-mail indesejado. Nas métricas, os usuários precisam marcar esses e-mails como SPAM (portanto, essa contagem os inclui nas entregas, pois o e-mail precisa ser entregue primeiro). Para saber mais, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">Spam</a> no glossário de análise de dados de e-mail.
  - name: SpamCop
    description: Uma blocklist e banco de dados de endereços IP, anteriormente de propriedade privada, mas agora parte do fornecedor de e-mail Ironport. Muitos provedores de caixa de entrada verificam os endereços IP dos e-mails recebidos nos registros do SpamCop para determinar se o endereço foi incluído na blocklist devido a reclamações de SPAM.
  - name: Spam rate
    description: A taxa na qual os destinatários marcaram uma mensagem como SPAM ao visualizá-la. Essa taxa não inclui e-mails que caem na pasta de SPAM. Também não inclui reclamações de provedores de caixa de entrada que não possuem um feedback loop, como Gmail e iCloud. Para saber mais, consulte <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">Spam</a> no glossário de análise de dados de e-mail.
  - name: Spam trap
    description: Um e-mail usado para coletar e detectar SPAM por ISPs e organizações antispam. Também conhecido como spamtrap. Para saber mais, consulte <a href="/docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps">Armadilhas de entregabilidade e spam traps</a>.
  - name: Suppression list
    description: A Braze não possui listas de supressão, no entanto, você pode criar uma política de sunset conforme documentado em <a href="/docs/user_guide/channels/email/best_practices/sunset_policies">Políticas de sunset</a>. Para saber mais sobre o gerenciamento de inscrições de e-mail, consulte <a href="/docs/user_guide/channels/email/subscriptions">Inscrições</a>.
  - name: Throttling
    description: A prática de regular quantas mensagens de e-mail um remetente envia para um provedor de caixa de entrada ou servidor de e-mail por vez. Alguns provedores de caixa de entrada rejeitam e-mails se receberem mensagens em excesso.
  - name: Transactional mail
    description: Mensagens transacionais são definidas pelo CAN-SPAM como qualquer e-mail que "facilita, completa ou confirma uma transação previamente acordada". Diferentemente das mensagens comerciais, mensagens transacionais não precisam incluir um endereço postal dos EUA ou um link de cancelamento de inscrição.

---