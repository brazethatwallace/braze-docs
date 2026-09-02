---
nav_title: "SMS, MMS e RCS"
article_title: "SMS, MMS e RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "Saiba mais sobre SMS, MMS e RCS na Braze, incluindo configuração, conformidade e práticas recomendadas para alcançar usuários pelo número de telefone."
---

# SMS, MMS e RCS {#sms-mms-and-rcs}

> SMS (Short Messaging Service), MMS (Multimedia Messaging Service) e RCS (Rich Communication Services) oferecem uma forma direta de alcançar seus usuários pelo número de telefone em tempo real. O SMS continua sendo um dos canais mais utilizados no mundo porque é rápido, familiar e eficaz para atualizações urgentes. Este hub aborda a configuração de remetentes, conformidade, coleta de aceitação, criação de mensagens e relatórios de SMS, MMS e RCS na Braze. Consulte [Leis e regulamentações]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) e [Coleta de aceitação de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) antes de enviar sua primeira mensagem.

## Pré-requisitos {#prerequisites}

A disponibilidade de SMS, MMS e RCS depende do seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.

Antes de começar, verifique se você tem o seguinte:

- Códigos curtos, códigos longos ou IDs de remetente alfanuméricos configurados. Para saber mais, consulte [Configuração do remetente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Familiaridade com leis e regulamentações de SMS, incluindo TCPA e requisitos de operadoras. Para saber mais, consulte [Leis e regulamentações]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Consentimento explícito de aceitação coletado dos usuários. Para saber mais, consulte [Coleta de aceitações de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Casos de uso {#use-cases}

| Caso de uso | Explicação |
| --- | --- |
| Lembretes de compromissos | Envie lembretes oportunos antes de compromissos agendados, reduzindo faltas e mantendo os clientes informados. |
| Atualizações de pedidos | Notifique os clientes sobre confirmações de pedidos, status de envio e atualizações de entrega em tempo real. |
| Autenticação de dois fatores | Entregue códigos de verificação únicos para login de conta e confirmação de transação. |
| Ofertas promocionais | Alcance os clientes com promoções por tempo limitado, promoções relâmpago e descontos personalizados diretamente no celular. |
| Suporte ao cliente | Ative conversas bidirecionais para resolver dúvidas de clientes, coletar feedback ou confirmar solicitações de serviço. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Comparação entre SMS, MMS e RCS {#sms-mms-and-rcs-compared}

- **SMS** entrega mensagens somente de texto com até 160 caracteres (ou 70 caracteres com Unicode). É universalmente compatível com todos os dispositivos móveis e operadoras.
- **MMS** estende o SMS com suporte a conteúdo multimídia, incluindo imagens, GIFs e áudio. O MMS requer suporte da operadora e do dispositivo.
- **RCS** é a próxima geração de envio de mensagens empresariais, oferecendo recursos avançados como perfis de remetente com marca, respostas sugeridas, carrosséis e confirmações de leitura. A disponibilidade do RCS depende do suporte da operadora e do dispositivo.

### Por que usar RCS? {#why-use-rcs}

O RCS (Rich Communication Services) expande o SMS com uma experiência mais rica e semelhante a um app no aplicativo de mensagens padrão dos dispositivos compatíveis. As marcas usam o RCS para:

- Entregar imagens e vídeos em alta resolução em vez de apenas texto simples.
- Adicionar respostas e ações sugeridas para que os clientes possam responder com um único toque.
- Exibir um perfil de remetente verificado com identidade visual para que as mensagens sejam fáceis de confiar.
- Oferecer suporte a confirmações de leitura e indicadores de digitação quando as operadoras permitirem.

O RCS é ideal para casos de uso como atualizações transacionais (envio, agendamentos), promoções com criativos ricos, suporte ao cliente com opções de resposta rápida e integração ou tutoriais que se beneficiam de mídia e ações estruturadas. Para configuração e migração a partir do SMS, consulte [Configuração do RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Perguntas frequentes {#frequently-asked-questions}

### Preciso de consentimento de aceitação antes de enviar SMS na Braze? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Sim. Colete o consentimento explícito de aceitação e siga as leis aplicáveis, como TCPA e os requisitos das operadoras. Consulte [Coleta de aceitações de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) e [Leis e regulamentações]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Qual é a diferença entre SMS, MMS e RCS? {#what-is-the-difference-between-sms-mms-and-rcs}

O SMS envia mensagens somente de texto, o MMS adiciona multimídia como imagens, e o RCS adiciona recursos avançados como perfis de remetente com marca e respostas sugeridas em dispositivos compatíveis. Consulte **Comparação entre SMS, MMS e RCS** nesta mesma página.

### Como configuro os números de remetente para SMS? {#how-do-i-configure-sender-numbers-for-sms}

Configure códigos curtos, códigos longos ou IDs de remetente alfanuméricos na Braze antes de lançar Campaigns. Consulte [Configuração do remetente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Próximos passos {#next-steps}

- [Configuração de mensagem]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [Criar uma mensagem]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)