---
nav_title: Recursos da Meta
article_title: Recursos da Meta
page_order: 6
description: "Este artigo fornece documentação, informações e recursos úteis da Meta para melhorar sua compreensão da integração com o WhatsApp."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Recursos da Meta {#meta-resources}

> Esta página fornece documentação útil da Meta, atualizações de produto e perguntas frequentes para melhorar sua compreensão da integração do WhatsApp com a Braze.

## Documentação da Meta {#meta-documentation}

Consulte a documentação da Meta a seguir para orientações sobre nomes de exibição, números de telefone e mais.

- [Orientações sobre nome de exibição](https://www.facebook.com/business/help/757569725593362)
- [Ativando o Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Requisitos de número de telefone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites de envio de mensagens](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Classificação de qualidade](https://www.facebook.com/business/help/896873687365001)

## Atualizações de produto do WhatsApp {#whatsapp-product-updates}

### 2026: Nomes de usuário comerciais {#2026-business-usernames}
*Última atualização em maio de 2026*

A Meta está introduzindo nomes de usuário comerciais para o WhatsApp — um nome de exibição opcional que os negócios podem adotar para seu número de telefone do WhatsApp. Quando um nome de usuário é definido, ele aparece nas janelas de chat do WhatsApp e do WhatsApp Business no lugar do número de telefone. Observe que adotar um nome de usuário não oculta seu número de telefone; ele sempre permanece visível no seu perfil comercial.

Os nomes de usuário são únicos em todos os números de telefone do WhatsApp — dois números, sejam de consumidores ou comerciais, não podem compartilhar o mesmo nome de usuário. Eles não diferenciam maiúsculas de minúsculas para fins de unicidade, mas pontos e underscores são tratados como caracteres distintos. Por exemplo, `myid`, `my.id` e `my_id` são todos considerados nomes de usuário diferentes, enquanto `myID` e `myid` são tratados como o mesmo.

Os nomes de usuário comerciais devem atender aos seguintes requisitos de formato:

- Contém apenas letras em inglês (a–z), dígitos (0–9), pontos (`.`) ou underscores (`_`)
- Tem entre 3 e 35 caracteres
- Contém pelo menos uma letra em inglês
- Não começa nem termina com um ponto e não contém dois pontos consecutivos
- Não começa com `www`
- Não termina com um sufixo de domínio comum (como `.com`, `.org` ou `.net`)

#### Reivindicando um nome de usuário reservado {#claiming-a-reserved-username}

Antes de o recurso de nome de usuário estar amplamente disponível, a Meta pode ter pré-reservado um nome de usuário para o seu negócio — geralmente correspondendo a um nome de usuário existente de Página do Facebook ou Instagram. Você pode reivindicar esse nome de usuário reservado ou escolher um diferente pelo [WhatsApp Manage](https://business.facebook.com/wa/manage/). Os nomes de usuário reivindicados não são ativados até que a Meta disponibilize o recurso.

Se o nome de usuário reservado corresponder a um já associado à sua Página do Facebook ou conta do Instagram, você deve primeiro vincular seu número de telefone comercial a essa Página ou conta. Você pode fazer isso ao reivindicar o nome de usuário no WhatsApp Manager ou Meta Business Suite, ou adicionando seu número de telefone diretamente da Página ou conta relevante. A vinculação requer controle total da Página ou conta, ou acesso parcial básico com a permissão `manage_phone`.

#### Prioridade de exibição nas janelas de chat {#display-priority-in-chat-windows}

Quando seu perfil comercial aparece em uma janela de chat, o WhatsApp usa a seguinte ordem de prioridade (da mais alta para a mais baixa):

1. Nome do contato salvo
2. Nome comercial verificado ou nome de Conta Comercial Oficial (OBA)
3. Nome de usuário
4. Número de telefone

Para saber mais, consulte a documentação da Meta sobre [nomes de usuário comerciais](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/#business-usernames).

### Abril de 2026: Arquivamento automático de modelos inativos {#april-2026-automatic-archival-of-inactive-templates}
*Última atualização em abril de 2026*

- A Meta arquiva automaticamente modelos que estão inativos há 12 meses ou mais.
- O arquivamento automático está ativado para todas as contas do WhatsApp Business e não pode ser desativado.
- A atividade do modelo inclui criar, editar, enviar, recorrer ou desarquivar um modelo.
- Modelos arquivados não podem ser enviados e são programados para exclusão permanente após 28 dias.
- Você pode desarquivar modelos dentro da janela de 28 dias para restaurá-los e cancelar a exclusão programada.
- As notificações são enviadas pelo webhook `message_template_status_update`, por e-mail e por um banner único no WhatsApp Manager.

Para saber mais, consulte a documentação da Meta sobre [arquivamento de modelos](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-archival).

### Junho de 2026: IDs de usuário com escopo de negócio {#june-2026-business-scoped-user-ids}
*Última atualização em março de 2026*

- A Meta está introduzindo IDs de usuário para substituir o compartilhamento de números de telefone por questões de privacidade
- A Braze está trabalhando em uma solução antes da implementação
- Implementação esperada pela Meta em junho de 2026

### Novembro de 2025: [API de mensagens de marketing para WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (anteriormente Marketing Messages Lite API) {#november-2025-marketing-messages-api-for-whatsapphttpsdevelopersfacebookcomdocumentationbusiness-messagingwhatsappmarketing-messagesoverview-formerly-marketing-messages-lite-api}
*Última atualização em março de 2026*

- Substitui os limites estáticos da Cloud API por limites dinâmicos baseados em engajamento
- Não disponível na EMEA, Japão ou Coreia do Sul para entrega otimizada
- Mensagens de utilidade/autenticação continuam pela Cloud API automaticamente

### Outubro de 2025: Processo de aprovação de Conta Comercial Oficial (OBA) alterado {#october-2025-official-business-account-oba-approval-process-changed}
*Última atualização em março de 2026*

- Anteriormente aberto a todos os clientes pelo WhatsApp Manager
- Agora restrito a: governo/grandes anunciantes da Meta, anunciantes diretos ou via um BSP como a Braze (até 5 por semana)
- Novos pré-requisitos: verificação de negócio, verificação em duas etapas, nome de exibição aprovado, notabilidade
- Entre em contato com seu gerente de sucesso do cliente para assistência

### Outubro de 2025: Reduções de preço regionais {#october-2025-regional-pricing-rate-cuts}
*Última atualização em março de 2026*

- Tarifas mais baixas de utilidade/autenticação na Argentina, Egito, México e América do Norte
- Tarifas de marketing mais baixas no México (vigentes a partir de 1º de outubro de 2025)

### Outubro de 2025: Limites de envio de mensagens mudam de por telefone para por portfólio de negócios {#october-2025-messaging-limits-change-from-per-phone-to-per-business-portfolio}
*Última atualização em março de 2026*

- Os limites agora são compartilhados entre todos os números de telefone em um portfólio
- Os portfólios herdam o limite mais alto existente
- Acesso mais rápido a limites mais altos (em até 6 horas)
- Risco: negócios sem um número "ilimitado" podem ver os limites agregados diminuírem

### 1º de julho de 2025: Reformulação de preços {#july-1-2025-pricing-overhaul}
*Última atualização em março de 2026*

- A cobrança por mensagem substituiu a cobrança por conversa
- Mensagens de utilidade enviadas em uma janela de atendimento de 24 horas passaram a ser gratuitas
- Tarifas de utilidade/autenticação atualizadas em vários mercados, com novas faixas de volume
- Novas regras sobre categorização incorreta de modelos de utilidade — negócios podem enfrentar rejeição de modelos e restrições de envio

### Abril de 2025: Pausa de mensagens de marketing para números de telefone dos EUA {#april-2025-pause-of-marketing-messages-to-us-phone-numbers}
*Última atualização em agosto de 2025*

A Meta pausará a entrega de todas as mensagens de modelo de marketing para usuários do WhatsApp que possuem um número de telefone dos Estados Unidos (um número composto pelo código de discagem `+1` e um código de área dos EUA). Não há uma data programada para quando essa pausa será encerrada.

Qualquer tentativa de enviar um modelo para um usuário do WhatsApp com um número de telefone dos EUA resultará no erro `131049`.

### Março de 2025: Restrições por uso indevido de categoria de modelo {#march-2025-template-category-misuse-restrictions}
*Última atualização em março de 2026*

- A Meta introduziu medidas de aplicação para negócios que fazem uso indevido da categorização de utilidade/marketing
- Pode resultar em restrições de 7 a 30 dias na criação de modelos e revisões de categoria

### Março de 2025: Limites de mensagens de modelo de marketing por usuário {#march-2025-per-user-marketing-template-message-limits}
*Última atualização em agosto de 2025*

A Meta limitará o número de mensagens de modelo de marketing que um usuário pode receber de todos os negócios em um determinado período de tempo, começando com mensagens que têm menor probabilidade de serem lidas.

Uma exceção é: se uma pessoa responder a uma mensagem de marketing, isso iniciará uma janela de atendimento ao cliente de 24 horas. Mensagens de marketing enviadas dentro dessa janela não contarão para o limite da pessoa.

O limite específico varia por usuário, dependendo do nível de engajamento. Saiba mais sobre os limites de mensagens de modelo de marketing por usuário do WhatsApp [aqui](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Janeiro de 2025: WhatsApp pausando o envio de mensagens de marketing para usuários dos EUA a partir de 1º de abril {#january-2025-whatsapp-pausing-marketing-message-sending-to-us-users-starting-april-1}
*Última atualização em janeiro de 2025*

O WhatsApp pausará o envio de mensagens de marketing para usuários dos EUA (pessoas com números de telefone dos EUA) a partir de 1º de abril de 2025. [Mensagens de utilidade, serviço e autenticação](https://developers.facebook.com/docs/whatsapp/pricing/) e [mensagens de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#response-messages) ainda serão permitidas nos EUA.

O envio de mensagens de marketing (além de todos os outros tipos de mensagem) para todos os outros países ou regiões ainda é permitido e não será afetado.

A Meta nos informou que está fazendo essa atualização para manter a integridade do ecossistema do WhatsApp nos EUA, onde o WhatsApp está crescendo rapidamente, mas ainda está em um estágio inicial (por exemplo, mensagens de marketing têm menor engajamento do que em outras regiões). Eles continuarão avaliando quando o mercado dos EUA estará pronto para retomar as mensagens de marketing.

A entrega de mensagens de marketing para números de telefone com códigos de área dos EUA será rejeitada pelo WhatsApp e retornará um código de erro 131049.

### Novembro de 2024: Mudanças na política de opt-in do WhatsApp {#november-2024-changes-to-whatsapp-opt-in-policy}
*Última atualização em janeiro de 2025*

A Meta atualizou recentemente sua [política de opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Em vez de exigir consentimento específico do canal, os negócios agora podem enviar mensagens aos usuários na plataforma se:

1. A pessoa forneceu seu número de telefone.
2. A pessoa concedeu permissão de opt-in para mensagens em geral, não apenas para o WhatsApp.

Os negócios ainda precisam cumprir todas as leis locais e seguir os requisitos abaixo ao obter o opt-in:

- Os negócios devem declarar claramente que a pessoa está optando por receber comunicações do negócio
- Os negócios devem declarar claramente o nome do negócio do qual a pessoa está optando por receber mensagens
- Os negócios devem cumprir a legislação aplicável

Embora o WhatsApp tenha flexibilizado sua política, a Braze ainda recomenda coletar opt-in específico para o canal do WhatsApp, a fim de promover a melhor experiência do cliente e taxas de engajamento. Como sempre, consulte sua equipe jurídica para ver o que faz sentido para sua marca.

### Novembro de 2024: Atualizações no limite de modelo de marketing por usuário para pessoas nos EUA, antes da temporada de festas {#november-2024-updates-to-the-per-user-marketing-template-limit-for-people-in-the-us-ahead-of-the-holiday-season}
*Última atualização em dezembro de 2024*

Desde que a Meta implementou o limite de modelo de marketing por usuário, a Meta observou melhorias significativas nas taxas de leitura e no sentimento dos usuários.

A partir de agora, antes da temporada de festas, pessoas nos EUA receberão menos novas conversas de marketing. A Meta espera que essa mudança crie públicos mais engajados, o que, em última análise, leva a melhores resultados para os negócios. Isso pode resultar em taxas de entrega mais baixas para o seu negócio se você enviar mensagens de marketing para números de telefone dos EUA, o que pode ser monitorado com o código de erro `131049` pelo Braze Currents e pelo Registro de atividades de envio de mensagem.

Negócios nos EUA ainda podem entregar mensagens de marketing em outras regiões geográficas, e não há impacto em mensagens de utilidade, autenticação ou serviço, nem em mensagens de modelo de marketing enviadas dentro de uma janela de conversa iniciada pelo usuário (por exemplo, um anúncio de clique para WhatsApp, carrossel de produtos ou modelo de cupom enviado como parte de uma conversa).

### Novembro de 2024: WhatsApp expandindo aplicações de qualidade em nível de conta para incluir taxas de leitura {#november-2024-whatsapp-expanding-quality-based-account-enforcements-to-include-read-rates}
*Última atualização em dezembro de 2024*

O WhatsApp está investindo continuamente em novas formas de ajudar os negócios a criar experiências de qualidade para seus clientes, como reduzir comportamentos semelhantes a spam em sua plataforma.

Em 22 de novembro, o WhatsApp começou a expandir suas aplicações de qualidade existentes em nível de conta nas contas comerciais do WhatsApp (WABAs) com taxas de leitura extremamente baixas. Essa mudança será implementada globalmente.

Quando a taxa de leitura de uma conta cai significativamente (por exemplo, a maioria das mensagens enviadas pela conta não são lidas), bloqueios de envio de mensagens serão aplicados na conta. A severidade do bloqueio aumentará se houver taxas de leitura consistentemente baixas em escala.

Se a taxa de leitura da conta for extremamente baixa, as seguintes ações serão tomadas:

- A conta será bloqueada para envio de mensagens iniciadas pelo negócio. Ela ainda poderá responder a mensagens iniciadas pelo cliente. Esse bloqueio inicial é um "bloqueio suave" e pode ser reconhecido selecionando o botão de reconhecimento em Qualidade da Conta para começar a enviar mensagens novamente.
- Se a taxa de leitura continuar caindo ou permanecer baixa após o bloqueio suave, os negócios podem enfrentar um aumento gradual nas ações de aplicação (por exemplo, alguns dias de restrições de envio de mensagens).
- Os negócios terão que aguardar o limite aplicado para começar a enviar mensagens novamente. Se a taxa de leitura continuar baixa após bloqueios suaves repetidos, a conta será eventualmente desativada.

#### Como se manter atualizado sobre esses avisos e aplicações {#how-to-stay-updated-on-these-warnings-and-enforcements}

Semelhante às aplicações existentes da plataforma, os negócios serão notificados sobre essas ações e podem reconhecê-las usando a página de Qualidade da Conta no WhatsApp Business Manager. Confirme que você tem os detalhes de contato corretos listados no WhatsApp Business Manager para todos os administradores necessários, pois os e-mails de notificação de aplicação serão enviados com base nessas informações.

Notificações sobre violações graves de spam serão:

- Exibidas no Centro de Notificações do WhatsApp Business Manager
- Exibidas em um banner no WhatsApp Manager
- Enviadas por e-mail para todos os administradores configurados no WhatsApp Business Manager

### Maio de 2024: Cloud API entrando em operação na Turquia {#may-2024-cloud-api-going-live-in-trkiye}
*Última atualização em maio de 2024*

A Meta agora fornece acesso à Cloud API para negócios na Turquia para envio de mensagens comerciais. Anteriormente, a Cloud API do WhatsApp estava disponível para negócios na Turquia, mas usuários do WhatsApp com números turcos não conseguiam enviar ou receber mensagens enviadas via Cloud API.

A Meta sempre deixa claro para os usuários quando eles estão conversando com um negócio hospedado pela Meta, e todos os usuários são obrigados a aceitar os Termos de Serviço e a Política de Privacidade relevantes do WhatsApp para prosseguir com o envio de mensagens comerciais. A atualização dos Termos de Serviço e da Política de Privacidade de 2021 na Turquia havia sido pausada, mas agora está sendo implementada. Ela não altera o compromisso da Meta com a privacidade — conversas pessoais continuam protegidas por criptografia de ponta a ponta, o que significa que apenas você e o destinatário pretendido podem vê-las. A atualização permite que usuários turcos acessem recursos comerciais opcionais, se desejarem, e fornece mais transparência sobre como o WhatsApp funciona.

Negócios com Cloud API agora podem iniciar conversas com usuários do WhatsApp com números turcos, que agora retornarão um webhook como uma conversa "enviada", em vez do código de erro 131026 atual.

Para que uma mensagem comercial seja "entregue" ou "lida", é necessário que o usuário aceite os termos do WhatsApp. Um negócio não será cobrado a menos que a mensagem seja entregue.

Usuários que receberem ou tentarem enviar uma mensagem para um negócio com Cloud API verão uma notificação no app sobre a atualização dos termos, que deixa claro que eles não podem enviar mensagens para um negócio com Cloud API até que aceitem a atualização do WhatsApp. Além disso, usuários que registrarem ou re-registrarem o app em seu telefone serão solicitados a aceitar a atualização do WhatsApp.

Quando um usuário aceitar a atualização, ele verá o aviso existente de mensagem do sistema da Cloud API ao conversar com um negócio com Cloud API.

### Maio de 2024: Limites de mensagens de modelo de marketing por usuário {#may-2024-per-user-marketing-template-message-limits}
*Última atualização em maio de 2024*

A Meta está implementando novas abordagens para manter experiências de alta qualidade para os usuários e maximizar o engajamento com mensagens de modelo de marketing na plataforma WhatsApp. A partir de 23 de maio de 2024, eles limitarão o número de mensagens de modelo de marketing que cada usuário individual pode receber de todos os negócios com os quais interage durante um determinado período de tempo, começando com um pequeno número de conversas que têm menor probabilidade de serem lidas. Observe que o limite é determinado com base no número de mensagens de modelo de marketing que essa pessoa já recebeu de qualquer negócio, e não está relacionado especificamente à sua marca. No entanto, isso pode afetar a entregabilidade de suas mensagens de modelo de marketing.

O limite se aplica apenas a mensagens de modelo de marketing que normalmente abririam uma nova conversa de marketing. Se uma conversa de marketing já estiver aberta entre sua marca e um usuário do WhatsApp, as mensagens de modelo de marketing enviadas ao usuário não serão afetadas.

Se uma mensagem de modelo de marketing não for entregue a um determinado usuário devido ao limite, a Cloud API retornará o código de erro 131026. Observe, no entanto, que esses códigos de erro cobrem uma ampla gama de problemas que podem resultar na não entrega de uma mensagem, e por razões de privacidade, a Meta não divulgará se de fato a mensagem não foi entregue devido ao limite. Consulte o [documento de solução de problemas](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) da Cloud API para descrições dos motivos de não entrega e o que você pode fazer para determinar a causa subjacente.

Se você receber um desses códigos de erro e suspeitar que é devido ao limite, evite reenviar imediatamente a mensagem de modelo, pois isso resultará apenas em outra resposta de erro.

Para saber mais sobre essa atualização de entregabilidade, incluindo detalhes sobre como monitorar sua entregabilidade e outras práticas recomendadas para envio de mensagens de marketing no WhatsApp, consulte nosso [post recente no blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Abril de 2024: Ritmo de modelo para modelos de utilidade {#april-2024-template-pacing-for-utility-templates}
*Última atualização em abril de 2024*

No ano passado, o WhatsApp introduziu o ritmo de modelo para mensagens de marketing como uma nova forma de ajudar os negócios a melhorar o engajamento de seus modelos e criar experiências valiosas para os usuários. A partir de 30 de abril, eles estão expandindo o ritmo de modelo para mensagens de utilidade. Se um modelo de utilidade de uma conta for pausado devido ao feedback dos usuários, eles aplicarão ritmo aos novos modelos de utilidade criados nos próximos sete dias.

### Abril de 2024: Taxas de leitura afetarão a classificação de qualidade para modelos de marketing {#april-2024-read-rates-will-affect-quality-rating-for-marketing-templates}
*Última atualização em março de 2024*

O WhatsApp está testando novas abordagens, começando com consumidores na Índia, para criar experiências mais valiosas e maximizar o engajamento com as conversas de marketing dos negócios. Isso pode incluir limitar o número de conversas de marketing que uma pessoa recebe de qualquer negócio em um determinado período, começando com um pequeno número de conversas que têm menor probabilidade de serem lidas. A Braze receberá um código de erro se uma mensagem não for entregue.

O WhatsApp começará a considerar as taxas de leitura como parte da classificação de qualidade para modelos de marketing, juntamente com métricas tradicionais como bloqueios e denúncias. O WhatsApp pode pausar temporariamente Campaigns de mensagens de marketing com baixas taxas de leitura, dando aos negócios tempo para iterar nos modelos com menor engajamento antes de escalar o volume, a partir de 1º de abril de 2024.

### Fevereiro de 2024: Experimentação de conversas de marketing {#february-2024-marketing-conversations-experimentation}
*Última atualização em fevereiro de 2024*

A partir de 6 de fevereiro de 2024, o WhatsApp está testando novas abordagens, começando com consumidores na Índia, para criar experiências mais valiosas e maximizar o engajamento dos clientes com as conversas de marketing da sua marca. Isso pode incluir limitar o número de conversas de marketing que um usuário recebe da sua marca em um determinado período, começando com um pequeno número de conversas que têm menor probabilidade de serem lidas.

### Outubro de 2023: Ritmo de modelo {#october-2023-template-pacing}
*Última atualização em outubro de 2023*

A partir de 12 de outubro de 2023, o WhatsApp está introduzindo um conceito chamado "ritmo de modelo" para mensagens de marketing. Em vez de enviar sua mensagem para todo o público da Campaign simultaneamente, o "ritmo de modelo" inicialmente entrega a mensagem a um subconjunto menor de usuários para coletar feedback em tempo real dos destinatários da Campaign antes de enviar as mensagens restantes.

O "limite de ritmo" (o subconjunto inicial de mensagens enviadas) é variável dependendo do modelo. Após o envio inicial, o WhatsApp reterá as mensagens restantes por no máximo 30 minutos. Durante esse período de retenção, eles avaliam a qualidade do modelo com base no feedback dos clientes. Se o feedback for positivo, indicando um modelo de alta qualidade, eles entregam as mensagens restantes. Se o feedback for negativo, eles descartam as mensagens restantes não entregues, evitando mais feedback negativo de uma parcela maior dos seus clientes e ajudando você a evitar possíveis problemas de aplicação de qualidade (como impactos na classificação de qualidade do número de telefone).

Observe que o WhatsApp usa o mesmo sistema para avaliar a qualidade do modelo no ritmo de modelo que usa para a pausa de modelo. Portanto, mensagens não entregues durante o ritmo de modelo (devido a modelos de baixa qualidade) são as mesmas que teriam sido pausadas em uma escala maior.

Em última análise, essa atualização fornece um ciclo de feedback mais rápido (30 minutos versus horas ou dias com a pausa de modelo), para que você possa ajustar seus modelos e proporcionar uma melhor experiência ao cliente.

**Se você tiver mais perguntas sobre essa atualização, entre em contato com seu representante parceiro da Meta.**

### Junho de 2023: Experimentação de envio de mensagens {#june-2023-messaging-experimentation}
*Última atualização em junho de 2023*

A partir de 14 de junho de 2023, a Meta está introduzindo novas práticas de experimentação na plataforma WhatsApp para avaliar como as mensagens de marketing impactam a experiência e o engajamento do consumidor. Esse experimento pode afetar suas mensagens de marketing enviadas pela API do WhatsApp Business com a Braze.

A Meta pretende continuar com essa experimentação na plataforma WhatsApp. Consulte a [documentação da Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) para mais informações.

**A experimentação do WhatsApp afeta apenas mensagens de marketing.** Esse experimento tem o potencial de impactar a entrega de mensagens de modelo de marketing. Modelos de utilidade e autenticação continuarão sendo entregues sem qualquer impacto da experimentação.

No experimento, a Meta seleciona aleatoriamente aproximadamente 1% dos consumidores do WhatsApp como participantes. Se selecionado, a Meta não entregará mensagens de modelo de marketing a esses consumidores, a menos que uma das seguintes condições seja verdadeira:

- Se um consumidor respondeu a você nas últimas 24 horas;
- Se uma conversa de marketing existente está aberta; ou
- Se um anúncio do WhatsApp foi clicado pelo consumidor nas últimas 72 horas.

## Perguntas frequentes {#faq}

### Como saberei se minha mensagem de marketing foi impactada pelo experimento da Meta? {#how-will-i-know-if-my-marketing-message-was-impacted-by-metas-experiment}

Se uma mensagem não for entregue devido ao experimento, um código de erro específico será exibido no Registro de Atividades e no Currents. A mensagem também será contabilizada como uma falha e incorporada às suas métricas de Falhas do WhatsApp em todos os relatórios dentro do dashboard da Braze. Você não será cobrado por essas mensagens.

Esse código de erro 130472 indicará "User's number is part of an experiment." Consulte a [documentação da Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) para mais informações sobre códigos de erro da Cloud API do WhatsApp.

### Posso optar por não participar do experimento da Meta? {#can-i-opt-out-of-metas-experiment}

Não, a Meta não permite nenhuma exclusão do experimento. Todos os provedores e usuários da API do WhatsApp Business estão sujeitos a esse experimento da Meta.

### Posso tentar reenviar um modelo depois? {#can-i-try-to-resend-a-template-later}

Não há um prazo fixo para esse experimento. Sendo assim, um consumidor pode continuar sujeito ao experimento.

### O que posso fazer se minhas mensagens de marketing não forem entregues devido ao experimento da Meta? {#what-can-i-do-if-my-marketing-messages-are-not-delivered-due-to-metas-experiment}

Recomendamos usar outros canais da Braze, como e-mail, SMS, notificações por push ou mensagens no app, para enviar uma mensagem com conteúdo semelhante aos seus usuários pretendidos.