---
nav_title: Atualizações de preços do WhatsApp
permalink: "/whatsapp_pricing_updates/"
hidden: true
noindex: true
hide_toc: true
---

# Atualizações de preços do WhatsApp {#whatsapp-pricing-updates}

## Alterações adicionais de preços do WhatsApp em outubro de 2025 {#additional-whatsapp-pricing-changes-in-october-2025}
*Última atualização: 3 de setembro de 2025*

### Alterações de preços em algumas regiões {#pricing-changes-in-some-regions}

A partir de **1º de outubro**, a Meta está atualizando as tarifas em mercados específicos.

- **Para mensagens utilitárias e de autenticação:** As tarifas estão sendo reduzidas na Argentina, Egito, México e América do Norte para garantir que os preços continuem atrativos.
- **Para mensagens de marketing:** As tarifas estão sendo reduzidas no México para garantir que os preços continuem motivando a adoção e promovendo um ecossistema saudável de envio de mensagens.

| País e tipo de mensagem | % de alteração |
| --- | --- |
| Argentina - Autenticação                  | -10,04%  |
| Argentina - Utilitária                    | -10,04%  |
| Egito - Autenticação                      | -30,43%  |
| Egito - Autenticação - Internacional      | -0,58%   |
| Egito - Utilitária                        | -30,43%  |
| México - Marketing                        | -30,08%  |
| América do Norte - Autenticação           | -70,39%  |
| Arábia Saudita - Autenticação             | -6,89%   |
| Arábia Saudita - Utilitária              | -6,89%   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Mudanças adicionais nos preços do WhatsApp em julho de 2025 {#additional-whatsapp-pricing-changes-in-july-2025}
*Última atualização: 12 de junho de 2025*

Além das atualizações de preços de julho anunciadas anteriormente, a Meta está implementando algumas atualizações adicionais que também entrarão em vigor em 1º de julho de 2025.

Aqui está um resumo rápido das mudanças anunciadas anteriormente:
- Os preços do WhatsApp passarão para um modelo "por mensagem" em vez de um modelo "por conversa". **As tarifas "por mensagem" serão as mesmas que as tarifas atuais "por conversa".**
- Modelos utilitários enviados em resposta a mensagens de usuários (portanto, dentro de uma [janela de atendimento ao cliente](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) aberta) serão gratuitos.

*Para mais detalhes sobre essas mudanças, consulte a publicação anterior datada de 12 de março mais adiante neste artigo.*

Mudanças adicionais de 1º de julho (anunciadas pela Meta em 15 de maio):
- A Meta está atualizando as tarifas de utilidade e autenticação em vários mercados como parte dos esforços contínuos para garantir que os preços estejam equiparados aos canais alternativos.
    - Os preços para mensagens de utilidade e autenticação estão diminuindo em todos os mercados, exceto na Indonésia. Na Indonésia, os preços de utilidade estão aumentando e os preços de autenticação estão diminuindo.
- A Meta está refinando sua definição de utilidade, com base no engajamento e no sentimento dos usuários, transferindo assim casos de uso específicos de e para a categoria de utilidade. Consulte a nova [definição de modelo utilitário](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing#updates-to-template-category-guidelines) da Meta.

Para a maioria dos clientes, essas atualizações entrarão em vigor automaticamente em 1º de julho.

## Próximas alterações de preços do WhatsApp em julho de 2025 {#upcoming-whatsapp-pricing-changes-in-july-2025}

*Última atualização em 12 de março de 2025 (publicado originalmente em 13 de dezembro de 2024)*

O WhatsApp está fazendo mais duas atualizações em seus preços a partir de 1º de julho de 2025. A Braze atualizará nossos preços para refletir essas mudanças no mesmo dia. Um resumo das alterações e das práticas recomendadas para se adequar a elas está na seção a seguir.

### Atualização 1: o preço do WhatsApp passará para um modelo "por mensagem" em vez de um modelo "por conversa". {#update-1-whatsapp-pricing-will-shift-to-a-per-message-model-instead-of-a-per-conversation-model}

**As taxas "por mensagem" serão as mesmas que as taxas atuais "por conversa".**

#### Por que estão fazendo essa mudança? {#why-are-they-making-this-change}

A Meta está migrando para um modelo "por mensagem" para ajudar as marcas a simplificar os cálculos de retorno sobre investimento (ROI or retorno sobre o investimento (ROI)). Essa mudança também facilitará que as marcas façam comparações diretas de ROI or retorno sobre o investimento (ROI) com outros canais que cobram por mensagem.

#### Como isso vai afetar meu uso atual do WhatsApp? {#how-will-this-affect-my-current-whatsapp-usage}

- As conversas atuais enviadas com um modelo de mensagem na janela de 24 horas não serão afetadas.
- **As conversas atuais enviadas com dois ou mais modelos de mensagem do _mesmo tipo_ na janela de 24 horas terão um aumento de custo.** Por exemplo, enviar dois modelos de marketing no período de 24 horas terá o dobro do custo, porque a cobrança será feita por modelo de mensagem.

| Cenário de exemplo | Preço antes de abril de 2025 | Preço depois de abril de 2025 |
| --- | --- | --- |
| Marca envia um modelo de mensagem de marketing na janela de 24 horas | Cobrança de uma conversa de marketing | Cobrança de uma mensagem de marketing |
| Marca envia dois modelos de mensagem de marketing na janela de 24 horas | Cobrança de uma conversa de marketing | Cobrança de duas mensagens de marketing |
| Marca envia um modelo de mensagem de utilidade na janela de 24 horas | Cobrança de uma conversa de utilidade | Cobrança de uma mensagem de utilidade |
| Marca envia dois modelos de mensagem de utilidade na janela de 24 horas | Cobrança de uma conversa de utilidade | Cobrança de duas mensagens de utilidade |
| Marca envia um modelo de mensagem de marketing e um modelo de mensagem de utilidade na janela de 24 horas | Cobrança de uma conversa de marketing e uma conversa de utilidade | Cobrança de uma mensagem de marketing e uma mensagem de utilidade |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Essa atualização se aplica a modelos de marketing, utilidade e autenticação. As conversas de serviço são gratuitas desde 1º de novembro de 2024.

*Nota: essa atualização estava originalmente prevista para 1º de abril, depois 1º de maio, e agora **1º de julho**.*

### Atualização 2: modelos de utilidade enviados durante uma janela de atendimento ao cliente de 24 horas serão gratuitos. {#update-2-utility-templates-sent-during-a-24-hour-customer-service-window-will-be-free-of-charge}

#### Como isso funciona? {#how-does-this-work}

Uma [janela de atendimento ao cliente de 24 horas](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) é criada quando um usuário final envia uma mensagem para uma marca. Se a sua marca responder com um modelo de utilidade, não haverá cobrança.

Modelos de utilidade enviados fora de uma janela de atendimento ao cliente de 24 horas (por exemplo, modelos de utilidade enviados proativamente por uma marca para lembretes de conta e atualizações de status de pedido) ainda serão cobrados.

Recomendamos as seguintes práticas para se adequar a essas mudanças e maximizar seu orçamento de marketing no WhatsApp:

- Limite o envio de vários modelos de mensagem do mesmo tipo (sem resposta do usuário) no período de 24 horas. Você não será cobrado mais do que era anteriormente no modelo "por conversa". Essa também é uma prática recomendada para proporcionar experiências de qualidade aos seus clientes e limitar a fadiga de mensagens.
- Use o [envio de mensagens de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) ao responder às mensagens de usuários finais. As mensagens de resposta são gratuitas.

| Cenário de exemplo | Preço antes de abril de 2025 | Preço depois de abril de 2025 |
| --- | --- | --- |
| - Marca envia modelo de marketing <br>- Usuário responde <br>- Marca responde com uma mensagem de resposta | Cobrança de uma conversa de marketing | Cobrança de uma mensagem de marketing |
| - Usuário envia mensagem para a marca <br>- Marca responde com uma mensagem de resposta | Gratuito <br> _Classificado como conversa de serviço_ | Gratuito <br> _Classificado como conversa de serviço_ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Recomendamos as seguintes práticas para se adequar a essas mudanças e maximizar seu orçamento de marketing no WhatsApp:

- Limite o envio de vários modelos de mensagem do mesmo tipo (sem resposta do usuário) no período de 24 horas. Isso evita que você seja cobrado mais do que era anteriormente no modelo "por conversa". Essa também é uma prática recomendada para proporcionar experiências de qualidade aos seus clientes e limitar a fadiga de mensagens.
- Use o [envio de mensagens de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) ao responder às mensagens de usuários finais. As mensagens de resposta são gratuitas.

*Nota: essa atualização estava originalmente prevista para 1º de abril e **agora 1º de julho**.*

## Mudanças nos preços do WhatsApp de agosto de 2024 a novembro de 2024 {#whatsapp-pricing-changes-from-august-2024-november-2024}

*Última atualização em 29 de outubro de 2024*

### Conversas utilitárias {#utility-conversations}

Em 1º de agosto de 2024, a Meta reduziu as tarifas de conversas utilitárias para incentivar as marcas a facilitar mais jornadas do cliente pós-compra na plataforma. Repassamos essas reduções de custo para seus direitos de Message Credits ou WhatsApp Credits em proporções iguais. Essa atualização entrou em vigor no mesmo dia que a da Meta (1º de agosto).

#### O que são conversas utilitárias? {#what-are-utility-conversations}

As conversas utilitárias permitem que você faça acompanhamento de ações ou solicitações específicas dos clientes. Exemplos incluem confirmação de aceitação, atualizações e confirmações de pedidos, atualizações ou alertas de conta (por exemplo, lembretes de pagamento) ou pesquisas de feedback.

#### Como você pode se beneficiar dessa atualização? {#how-can-you-benefit-from-this-update}

Incentivamos que você aproveite essa atualização usando o WhatsApp para envio de mensagens transacionais. Você também pode considerar migrar algumas das suas mensagens transacionais de SMS para o WhatsApp, se isso fizer sentido para sua marca (com base no alcance e engajamento do seu público em cada canal). Por exemplo, essa pode ser uma boa opção para clientes na Ásia, América Latina e Europa, onde o WhatsApp é um canal amplamente utilizado.

### Conversas de marketing {#marketing-conversations}

Em 1º de outubro de 2024, a Meta reduziu os preços das conversas de marketing no Reino Unido em 25% para refletir a demanda atual. Repassamos essas reduções de custo para seus direitos de Message Credits ou WhatsApp Credits em proporções iguais. Essa atualização entrou em vigor no mesmo dia que a da Meta (1º de outubro).

#### O que são conversas de marketing? {#what-are-marketing-conversations}

As conversas de marketing permitem que você alcance uma ampla variedade de objetivos, desde gerar reconhecimento até impulsionar vendas e redirecionar clientes. Exemplos incluem anúncios de novos produtos, promoções/ofertas direcionadas e campanhas de abandono de carrinho.

### Conversas de serviço {#service-conversations}

Em 1º de novembro de 2024, todas as conversas de serviço passaram a ser gratuitas. As conversas de serviço não consumirão mais direitos de Message Credits ou WhatsApp Credits. Essa mudança entrou em vigor no mesmo dia que a da Meta (1º de novembro).

#### O que são conversas de serviço? {#what-are-service-conversations}

As conversas de serviço permitem que você responda a dúvidas dos clientes. Isso inclui conversas iniciadas por um usuário final nas quais a marca responde com uma [mensagem de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) em vez de um modelo de mensagem.

#### Como você pode se beneficiar dessa atualização?

Algumas conversas que anteriormente eram cobradas como "serviço" agora são gratuitas. Elas incluem:

- [Campaigns de resposta não reconhecida]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages), em que um usuário final envia uma mensagem que não é reconhecida e a marca responde com uma mensagem genérica usando [envio de mensagens de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages). Por exemplo, um usuário final envia uma mensagem sem uma palavra-chave e a marca responde com "Não reconhecemos sua mensagem, entre em contato com o suporte ao cliente."
- Conversas que começam quando um usuário final envia à marca uma palavra-chave promovida e a marca responde usando uma [mensagem de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages). Exemplos comuns incluem aceitar o envio de mensagens via WhatsApp ou participar de uma promoção específica.

<br>

Informações detalhadas sobre a redução das conversas utilitárias estão na seção a seguir:

| Região de faturamento                      | Percentual de redução utilitária |
|--------------------------------------------|----------------------------------|
| Argentina                                  | 16,7%                            |
| Brasil                                     | 77,1%                            |
| Chile                                      | 65,9%                            |
| Colômbia                                   | 97,6%                            |
| Egito                                      | 92,4%                            |
| França                                     | 60,9%                            |
| Alemanha                                   | 35,5%                            |
| Índia                                      | 66,7%                            |
| Indonésia                                  | 0,0%                             |
| Israel                                     | 71,8%                            |
| Itália                                     | 28,6%                            |
| Malásia                                    | 30,0%                            |
| México                                     | 62,4%                            |
| Países Baixos                              | 37,5%                            |
| Nigéria                                    | 79,0%                            |
| América do Norte                           | 73,3%                            |
| Outros                                     | 77,2%                            |
| Paquistão                                  | 78,7%                            |
| Peru                                       | 52,3%                            |
| Restante da África                         | 61,9%                            |
| Restante da Ásia-Pacífico                  | 66,7%                            |
| Restante da Europa Central e Oriental      | 43,0%                            |
| Restante da América Latina                 | 77,1%                            |
| Restante do Oriente Médio                  | 20,7%                            |
| Restante da Europa Ocidental               | 28,6%                            |
| Rússia                                     | 16,1%                            |
| Arábia Saudita                             | 54,4%                            |
| África do Sul                              | 62,0%                            |
| Espanha                                    | 47,4%                            |
| Turquia                                    | 43,0%                            |
| Emirados Árabes Unidos                     | 20,7%                            |
| Reino Unido                                | 44,7%                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para entender melhor como você pode aproveitar essas atualizações, entre em contato com seu gerente de sucesso do cliente.