---
nav_title: Documentação de conformidade
article_title: Documentação de conformidade
page_order: 1
permalink: /compliance_documentation/
toc_headers: h2
noindex: true
---

# Documentação de conformidade {#compliance-documentation}

_Data de revisão: 30 de março de 2026_

## O que está incluído na documentação de conformidade? {#what-is-included-in-the-compliance-documentation}

A documentação de conformidade abaixo estabelece os termos específicos aplicáveis ao produto, canal, recurso, funcionalidade ou serviço adquirido:

- Para a funcionalidade dos Serviços da Braze que permite que os clientes interajam, se integrem ou acessem o produto, site, aplicativo ou serviço de um Prestador de Serviços Terceirizado, a documentação de conformidade contém os termos do Prestador de Serviços Terceirizado aplicáveis ao seu uso de tal funcionalidade; e
- Quaisquer práticas e padrões gerais do setor que os clientes da Braze devem cumprir para o uso de tal produto, canal, recurso, funcionalidade ou serviço da Braze.

## Atualizações na documentação de conformidade {#updates-to-the-compliance-documentation}

Você pode se inscrever para receber atualizações da nossa documentação (incluindo a documentação de conformidade) através do [repositório GitHub da Braze](https://github.com/braze-inc/release-notes).

## Documentação de conformidade para canais, integrações e recursos específicos {#compliance-documentation-for-specific-channels-integrations-and-features}

Abaixo está a lista dos nossos produtos, canais, recursos, funcionalidades e serviços que possuem documentação de conformidade aplicável. Se você estiver usando múltiplos produtos, toda a documentação de conformidade relevante se aplica.

### Termos gerais {#general-terms}

Sem limitar quaisquer obrigações do Cliente nos termos do Contrato, e para evitar dúvidas, o Cliente será o único responsável por obter todos os direitos, consentimentos e autorizações necessários e por fornecer avisos de privacidade legalmente adequados em conexão com seu uso, bem como por obter todos os consentimentos e autorizações legalmente exigidos para o uso dos Canais e Recursos listados abaixo.

## Canais e recursos {#channels-and-features}

1. [Canal de mensagens para celular](#mobile-messages-channel)
2. [Canal de webhooks](#webhooks-channel)
3. [Documentação de conformidade do canal do WhatsApp](#hatsapp-channel-compliance-documentation)
4. [Documentação de conformidade do canal LINE](#line-channel-compliance-documentation)
5. [Documentação de conformidade da integração Shopify](#shopify-integration-compliance-documentation)
6. [Documentação de conformidade do Audience Sync](#audience-sync-compliance-documentation)
7. [Documentação de conformidade de arquivamento de mensagens e criptografia em nível de campo](#message-archiving-and-field-level-encryption-compliance-documentation)
8. [Documentação de conformidade do Console do agente](#agent-console-compliance-documentation)
9. [Documentação de conformidade do canal KakaoTalk](#kakaotalk-channel-compliance-documentation)

## 1. Canal de mensagens para celular {#mobile-messages-channel}

Os seguintes termos adicionais se aplicam em relação ao uso do Canal de Mensagens para Celular pelo Cliente:

### Definições {#definitions}

"**Agregadores**", "**Operadoras**" ou "**Intermediários de Mensagens para Celular**" significam intermediários terceirizados que (i) transmitem Mensagens para Celular entre Provedores de Mensagens para Celular e Operadoras; (ii) são provedores de serviços sem fio (por exemplo, T-Mobile, AT\&T, etc.); e/ou (iii) estão envolvidos na transmissão de Mensagens RCS dos Provedores de Mensagens para Celular para os Usuários Finais.

**"Provedores de SMS/MMS" ou "Provedores de Mensagens para Celular"** significam Subprocessadores da Braze utilizados na transmissão de Mensagens SMS, MMS e/ou RCS, conforme identificado em [www.braze.com/subprocessors](http://www.braze.com/subprocessors).

"**Mensagens SMS/MMS**" ou "**Mensagens para Celular**" significam Mensagens SMS, MMS e/ou RCS.

### Padrões e melhores práticas aplicáveis do setor {#applicable-industry-standards-and-best-practices}

Ao enviar Mensagens para Celular, os Clientes devem cumprir as políticas de uso aceitável e de envio de mensagens aplicáveis dos Provedores de Mensagens para Celular, os padrões e diretrizes aplicáveis do setor e, quando aplicável, os códigos do setor e as diretrizes aplicáveis dos Intermediários de Mensagens para Celular para qualquer país onde o Cliente pretenda enviar Mensagens para Celular, conforme estabelecido em mais detalhes na [Política de Uso Aceitável](https://www.braze.com/company/legal/aup/) da Braze.

Terceiros envolvidos no envio de Mensagens para Celular, incluindo Intermediários de Mensagens para Celular, podem impor taxas ou penalidades com base em Mensagens para Celular enviadas em violação de seus termos ou leis aplicáveis. O Cliente é responsável pelo pagamento de taxas e penalidades resultantes da violação pelo Cliente de tais termos de terceiros, independentemente de tais taxas ou penalidades serem impostas ao Cliente ou à Braze.

### Subprocessadores {#sub-processors}

A Braze pode utilizar qualquer Provedor de Mensagens para Celular que esteja incluído em sua lista de Subprocessadores em [www.braze.com/subprocessors](https://www.braze.com/subprocessors/).

Não obstante o acima exposto, no caso de o Cliente enviar Mensagens para Celular usando o modelo "Bring Your Own (BYO) SMS Connector", os Provedores de Mensagens para Celular envolvidos no envio serão considerados Prestadores de Serviços Terceirizados (conforme definido no Contrato) e não Subprocessadores da Braze, e as isenções de responsabilidade abaixo se aplicarão a tais Prestadores de Serviços Terceirizados.

### Termos de exceção para uso de webhooks {#webhook-use-exception-terms}

Aplicável a Clientes que contrataram Créditos de Ação em ou após 9 de dezembro de 2024 (conforme a Data de Vigência do Formulário de Pedido): as restrições descritas na Documentação de Conformidade do Canal de Webhooks não se aplicam ao uso de webhooks para envio de Mensagens para Celular por meio de uma plataforma de Prestador de Serviços Terceirizado.

### Bring Your Own (BYO) SMS Connector

Os Clientes podem enviar Mensagens para Celular a partir da Braze usando provedores terceirizados por meio do modelo "BYO SMS Connector". Não obstante o acima exposto, os Clientes não devem usar o modelo BYO SMS Connector para enviar Mensagens para Celular para os EUA e Canadá.

### Isenções de responsabilidade {#disclaimers}

A Braze se isenta de quaisquer representações, garantias, responsabilidades e obrigações de indenização com relação a qualquer Prestador de Serviços Terceirizado ou Intermediários de Mensagens para Celular envolvidos no envio ou processamento de Mensagens para Celular, incluindo responsabilidade relacionada à capacidade do sistema, taxa de transferência de mensagens ou entrega real ao dispositivo de um Usuário Final.

## 2. Canal de webhooks {#webhooks-channel}

Os seguintes termos adicionais se aplicam em relação ao uso do Canal de Webhooks pelo Cliente:

### Termos de uso do canal de webhooks {#webhooks-channel-use-terms}

Salvo disposição em contrário na Documentação de Conformidade do Canal aplicável, (a) o Cliente não deve usar webhooks quando a Braze oferece capacidades nativas para alcançar o mesmo resultado, e (b) o Cliente não deve usar um webhook para acionar o envio de qualquer mensagem por meio de uma plataforma de Prestador de Serviços Terceirizado na medida em que a Braze forneça um mecanismo nativo para enviar tais mensagens por meio dos Serviços da Braze.

Se a Braze disponibilizar um mecanismo novo ou atualizado de forma geral nos Serviços da Braze durante o Período de Assinatura atual do Cliente, então o Cliente será proibido de usar webhooks para acionar o envio de Mensagens por meio da Plataforma de Terceiros especificada a partir de seis (6) meses após a data de lançamento geral do novo mecanismo ou ao final do ano atual do Período de Assinatura do Cliente, o que ocorrer por último.

### Exceções aos termos de uso do canal de webhooks {#exceptions-to-the-webhook-channel-use-terms}

Consulte [Canal de mensagens para celular](#mobile-messages-channel) e [Canal do WhatsApp](#whatsapp-channel-compliance-documentation)

### Isenção de responsabilidade {#disclaimer}

A Braze se isenta de toda responsabilidade com relação ao uso de webhooks pelo Cliente para acionar o envio de qualquer Mensagem ou quaisquer outras ações fora dos Serviços da Braze.

## 3. Documentação de conformidade do canal do WhatsApp {#whatsapp-channel-compliance-documentation}

Os seguintes termos adicionais se aplicam em relação ao uso do Canal do WhatsApp pelo Cliente:

### Termos aplicáveis do prestador de serviços terceirizado {#applicable-third-party-provider-terms}

O Cliente deve cumprir quaisquer pré-requisitos, termos e políticas aplicáveis ao Canal do WhatsApp, incluindo quaisquer termos exigidos pelo WhatsApp, LLC e suas afiliadas do grupo, conforme descrito na página de [configuração do WhatsApp](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/overview/) da Braze.

### Termos de exceção para uso de webhooks

O Cliente não pode usar webhooks para acionar o envio de mensagens pelo Canal do WhatsApp, a menos que seja para fins de suporte ao cliente, como casos de uso de chat assistido por humanos e/ou casos de uso de chatbot.

### Bring Your Own (BYO) WhatsApp Connector

Os Clientes podem conectar suas contas diretas do WhatsApp com a Braze usando o "BYO WhatsApp Connector".

## 4. Documentação de conformidade do canal LINE {#line-channel-compliance-documentation}

Os seguintes termos adicionais se aplicam em relação ao uso do Canal LINE pelo Cliente:

### Pré-requisitos {#pre-requisites}

Para enviar Mensagens pelo Canal LINE, os clientes devem obter uma Conta Oficial Verificada do LINE, que é aprovada e concedida pelo LINE a seu próprio critério. Os clientes devem garantir que obtenham uma Conta Oficial Verificada do LINE antes de adquirir Créditos de Ação da Braze para uso do Canal LINE.

### Termos aplicáveis do prestador de serviços terceirizado

Ao usar o Canal LINE, o Cliente concorda em cumprir e estar vinculado, conforme aplicável, a todos os termos e políticas exigidos pela LY Corporation e suas afiliadas (coletivamente "LINE"), incluindo, sem limitação, os Termos de Uso da Conta Oficial LINE, os Termos de Uso da API da Conta Oficial, as Diretrizes da Conta Oficial LINE, a Política de Dados do Usuário LINE e quaisquer políticas, termos, diretrizes e documentação incorporados por referência (coletivamente, os "Termos do LINE"). Para fins de esclarecimento, o Cliente é responsável por: (i) garantir que quaisquer dados processados em conexão com o LINE sejam processados de acordo com os Termos do LINE, conforme aplicável; e (ii) quaisquer taxas ou pagamentos devidos ao LINE pelo uso dos serviços LINE em conexão com o Canal LINE.

Não obstante qualquer disposição em contrário nos Termos do LINE, o Cliente permanece primariamente responsável pelo seu uso dos serviços LINE.


## 5. Documentação de conformidade da integração Shopify {#shopify-integration-compliance-documentation}

Os seguintes termos adicionais se aplicam em relação ao uso da integração Shopify pelo Cliente em conexão com os Serviços da Braze ("**Integração Shopify**"):

O Cliente concorda em cumprir e estar vinculado a quaisquer termos e condições, políticas, diretrizes e documentação aplicáveis da Shopify Inc. ou de qualquer uma de suas Afiliadas ("**Shopify**") aplicáveis ao uso da Integração Shopify.

O Cliente reconhece que a Shopify pode, a qualquer momento e a seu exclusivo critério: (i) exigir que a Braze desabilite ou bloqueie o acesso do Cliente à Integração Shopify; ou (ii) deixar de fornecer, suspender ou encerrar o acesso do Cliente à Integração Shopify. A Braze não terá responsabilidade com relação à Shopify deixar de fornecer acesso à Integração Shopify ao Cliente ou por meio dos Serviços da Braze de forma geral.

## 6. Documentação de conformidade do Audience Sync {#audience-sync-compliance-documentation}

Os seguintes termos adicionais se aplicam ao uso do Audience Sync pelo Cliente.

### Termos aplicáveis do prestador de serviços terceirizado

O Cliente concorda em cumprir e estar vinculado a quaisquer termos e condições, políticas, diretrizes e documentação aplicáveis dos Prestadores de Serviços Terceirizados que o Cliente utiliza em conexão com quaisquer integrações do Audience Sync.

O Cliente reconhece que os Prestadores de Serviços Terceirizados podem revisar, examinar e/ou remover quaisquer dados, anúncios ou conteúdo utilizados em conexão com seus serviços.

## 7. Documentação de conformidade de arquivamento de mensagens e criptografia em nível de campo {#message-archiving-and-field-level-encryption-compliance-documentation}

### Isenção de responsabilidade
O Cliente reconhece que o uso do Arquivamento de Mensagens e/ou da Criptografia em Nível de Campo (cada um, o "**Recurso**") pode impactar a velocidade de envio de Mensagens enviadas por meio dos Serviços da Braze. A Braze não será responsável por qualquer impacto desse tipo, e quaisquer compromissos de velocidade de envio não se aplicarão quando o Cliente estiver usando o Recurso. O Recurso pode ser usado para apoiar os esforços de conformidade do Cliente, no entanto, o Cliente reconhece que a Braze não faz representações ou garantias sobre se o uso do Recurso em si satisfaz as obrigações de conformidade do Cliente, e se isenta de toda responsabilidade em relação a isso.

## 8. Documentação de conformidade do Console do agente {#agent-console-compliance-documentation}

### Provedores de LLM como subprocessadores ou prestadores de serviços terceirizados {#llm-providers-as-sub-processors-or-third-party-providers}

Quando o Cliente usa uma integração com um modelo de linguagem de grande escala fornecido pela Braze por meio da opção Braze Auto nos Serviços da Braze ("LLM fornecido pela Braze"), o provedor de tal LLM fornecido pela Braze estará atuando como Subprocessador da Braze, sujeito aos termos do Adendo de Processamento de Dados (DPA) entre o Cliente e a Braze.

Se o Cliente optar por trazer sua própria chave de API para integrar com a funcionalidade de IA da Braze, o provedor da assinatura de LLM própria do Cliente será considerado um Prestador de Serviços Terceirizado, conforme definido no contrato entre o Cliente e a Braze.

## 9. Documentação de conformidade do canal KakaoTalk {#kakaotalk-channel-compliance-documentation}

Os seguintes termos adicionais se aplicam em relação ao uso do Canal KakaoTalk pelo Cliente:

### Pré-requisitos

Para enviar Mensagens pelo Canal KakaoTalk, os clientes devem primeiro obter uma Conta KakaoTalk e contratar serviços KakaoTalk com os Prestadores de Serviços Terceirizados envolvidos no fornecimento da funcionalidade KakaoTalk ao Cliente ("Prestadores de Serviços Terceirizados KakaoTalk"). As Contas KakaoTalk são aprovadas e concedidas por tais Prestadores de Serviços Terceirizados KakaoTalk a seu próprio critério.

### Termos aplicáveis do prestador de serviços terceirizado

Ao usar o Canal KakaoTalk, o Cliente concorda em cumprir e estar vinculado a quaisquer termos e políticas aplicáveis do KakaoTalk e dos Prestadores de Serviços Terceirizados KakaoTalk (coletivamente, os "Termos do KakaoTalk") e ser responsável pelo seu uso dos serviços KakaoTalk. Para fins de esclarecimento, o Cliente é responsável por quaisquer taxas ou pagamentos devidos ao KakaoTalk e/ou aos Prestadores de Serviços Terceirizados KakaoTalk pelo uso de tais serviços dos Prestadores de Serviços Terceirizados KakaoTalk em conexão com o Canal KakaoTalk.

{% multi_lang_include braze_legal/english_language_governance.md %}