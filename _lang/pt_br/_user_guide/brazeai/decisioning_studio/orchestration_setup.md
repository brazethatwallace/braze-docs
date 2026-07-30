---
nav_title: Configurar orquestração
article_title: Configurar orquestração
page_order: 4
page_type: reference
description: "Este artigo explica como configurar a orquestração para o BrazeAI Decisioning Studio, incluindo a escolha da sua CEP, a coleta das credenciais necessárias e a configuração da sua integração."
toc_headers: h2
---

# Configurar orquestração {#set-up-orchestration}

> Os agentes de decisão precisam se conectar a uma plataforma de engajamento com clientes (CEP) para orquestrar comunicações depois de ingerir dados de clientes e personalizar em nível 1:1. Este artigo aborda o que você precisa preparar e como configurar a integração para cada CEP compatível.

## O que é orquestração? {#what-is-orchestration}

Orquestração é a conexão entre o Decisioning Studio e sua plataforma de engajamento com clientes (CEP). Depois que seu agente de decisão determina a ação ideal para cada cliente, a orquestração executa essas decisões disparando comunicações personalizadas por meio da sua CEP.

Pense da seguinte forma:

- **Decisioning Studio** decide *o que* enviar e *quando* enviar
- **Sua CEP** cuida de *como* enviar

## Escolha sua plataforma de engajamento com clientes {#choose-your-cep}

A primeira etapa é escolher qual plataforma de engajamento com clientes usar com o Decisioning Studio. Sua escolha afeta a complexidade da configuração e os recursos disponíveis.

### Plataformas de engajamento com clientes compatíveis {#supported-ceps}

| Plataforma | Tipo de integração | Complexidade da configuração |
|-----|-----------------|------------------|
| **Braze** | Integração nativa via API (recomendada) | Baixa |
| **Salesforce Marketing Cloud** | Eventos de API + Journey Builder | Média |
| **Outras plataformas** | Personalizada (arquivo de recomendação) | Alta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plataformas de engajamento com clientes compatíveis" }

{% alert tip %}
Se você já usa a Braze como sua plataforma de engajamento com clientes, recomendamos usar a integração nativa da Braze para a experiência de configuração mais simples.
{% endalert %}

## Pré-requisitos {#prerequisites}

Antes de configurar a orquestração, reúna os itens a seguir com base na CEP escolhida.

{% tabs %}
{% tab Braze %}

| Requisito | Descrição |
|------|-------------|
| **Chave da API REST** | Uma nova chave de API com permissões para dados de usuários, mensagens, Campaigns, Canvas, Segments e modelos. |
| **URL do dashboard da Braze** | A URL da sua instância da Braze (por exemplo, `https://dashboard-01.braze.com`). |
| **ID do app** | A chave de API associada ao app que você deseja rastrear (encontrada em **Configurações** > **Configurações do app**). |
| **Nome de exibição e endereço de e-mail** | As informações do remetente a serem usadas nas suas campanhas (encontradas em **Configurações** > **Preferências de e-mail**). |
| **Modelos base** | Os modelos de mensagem que seu agente usa para orquestração. Você cria Campaigns disparadas por API para cada modelo. |
| **ID do usuário teste** | Um ID de usuário para testar a integração antes do lançamento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Requisito | Descrição |
|------|-------------|
| **Credenciais do pacote do app** | Client ID, Client Secret, Authentication Base URI, REST Base URI e SOAP Base URI de um pacote instalado com integração de API server-to-server. |
| **Permissões de API** | Escopos para canais, ativos, automações, jornadas, contatos, extensões de dados e eventos de rastreamento. |
| **Extensões de dados** | Você precisa de extensões de dados para dados de assinantes, dados de engajamento e recomendações. |
| **Modelos de e-mail** | Os modelos que você deseja que o Decisioning Studio use, com IDs de modelo para cada um. |
| **Acesso ao Journey Builder** | Acesso para criar e ativar jornadas com múltiplas etapas usando fontes de entrada de eventos de API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% tab Outras CEPs %}

Se você está usando uma CEP diferente da Braze ou do Salesforce Marketing Cloud, o Decisioning Studio pode se integrar por meio de uma abordagem de arquivo de recomendações:

| Item | Descrição |
|------|-------------|
| **Capacidade de ingestão de dados** | Sua CEP deve ser capaz de ingerir arquivos de recomendação (normalmente CSV ou JSON) contendo decisões personalizadas para cada cliente. |
| **Suporte a conteúdo dinâmico** | Suas campanhas devem suportar o preenchimento de campos dinamicamente com base nos dados de recomendação. |
| **Recursos de engenharia personalizados** | Sua equipe precisa construir a integração para ler os arquivos de recomendação e disparar as comunicações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% endtabs %}

## Planeje suas campanhas {#plan-your-campaigns}

Antes de configurar a orquestração, considere os seguintes detalhes:

### Modelos base {#base-templates}

Um modelo base é qualquer modelo de mensagem que seu agente de decisão pode usar. Considere:

- **Quantos modelos?** Seu agente pode trabalhar com um modelo ou vários. Se forem vários, o agente pode personalizar qual modelo cada cliente recebe.
- **Quais canais?** E-mail, push, SMS ou uma combinação. Cada canal pode exigir modelos e Campaigns separados.
- **Quais elementos dinâmicos?** Identifique quais partes da sua mensagem o agente personaliza (linhas de assunto, CTAs, ofertas, timing, etc.). Esses elementos se tornam propriedades de disparo de API ou placeholders dinâmicos.

### Configurações de reelegibilidade {#re-eligibility-settings}

Suas Campaigns devem permitir que os usuários recebam mensagens várias vezes:

- Para testes, você envia a mesma Campaign para o mesmo usuário repetidamente
- Em produção, o agente pode determinar que a mesma Campaign é a ideal para um usuário em dias consecutivos

{% alert note %}
Ao configurar a reelegibilidade para testes, os agentes do Decisioning Studio são projetados para respeitar os limites de frequência e não enviam a mesma Campaign para um usuário mais de uma vez por dia em produção.
{% endalert %}

### Propriedades de disparo de API {#api-trigger-properties}

Para integrações com a Braze, planeje quais dimensões seu agente otimiza. Essas dimensões se tornam propriedades de disparo de API que passam valores dinâmicos para suas Campaigns:

| Exemplo de dimensão | Propriedade de disparo de API |
|-------------------|---------------------|
| Linha de assunto | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Chamada para ação | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Oferta | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Valor do desconto | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Propriedades de disparo de API" }

## Configuração da integração {#integration-setup}

Selecione sua plataforma de engajamento com clientes nesta lista para começar a configuração da integração.

{% tabs %}
{% tab Braze %}

## Configurar a integração com a Braze {#set-up-braze-integration}

Siga estas etapas para integrar um agente do Decisioning Studio com os recursos de orquestração da Braze (a equipe de serviços da Braze está disponível para ajudar):

### Etapa 1: Criar uma chave de API {#step-1-create-an-api-key}

Acesse **Configurações** > **Chaves de API** e crie uma nova chave com as seguintes permissões:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Etapa 2: Configurar Campaigns disparadas por API {#step-2-set-up-api-triggered-campaigns}

Configure uma Campaign disparada por API para cada modelo base com propriedades de disparo de API para todas as dimensões otimizadas.

Um modelo base é qualquer modelo que o agente do Decisioning pode usar para orquestrar mensagens. Um agente do Decisioning pode ter 1 modelo base ou vários. Nesse caso, escolher o modelo base certo para cada cliente é uma das decisões que o agente personaliza.

### Etapa 3: Configurar a reelegibilidade {#step-3-configure-re-eligibility}

Certifique-se de que todas as Campaigns disparadas por API permitam que os usuários se tornem reelegíveis em até 15 minutos.

![Diagrama do Decisioning Pro mostrando configuração de limite de frequência]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Embora o agente do Decisioning Studio nunca envie a mesma Campaign mais de uma vez por dia, é importante ter a capacidade de enviar as mesmas Campaigns várias vezes ao dia para fins de teste.
{% endalert %}

### Etapa 4: Adicionar placeholders dinâmicos {#step-4-add-dynamic-placeholders}

Eles servem como placeholders dinâmicos para as decisões que o agente do Decisioning Studio está otimizando.

#### Exemplo 1: Campaign de e-mail {#example-1-email-campaign}

Suponha que o agente do Decisioning Studio esteja otimizando uma Campaign de e-mail. A configuração pode ser assim:

![Exemplo de Campaign de e-mail no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Supondo que o agente esteja otimizando a escolha de modelos e a mensagem de Call to Action (CTA), uma Campaign disparada por API deve ser criada para cada modelo, e a seção de CTA de um modelo pode ter esta aparência:

![Exemplo de seção CTA em modelo de e-mail no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Exemplo 2: Campaign de push {#example-2-push-campaign}

Suponha que um agente do Decisioning Studio esteja otimizando a mensagem de uma Campaign de push. A configuração pode ser assim:

![Exemplo de Campaign de push no Decisioning Studio - configuração]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Exemplo de Campaign de push no Decisioning Studio - propriedades]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Resultando na seguinte mensagem:

![Exemplo de Campaign de push no Decisioning Studio - resultado]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Exemplo 3: Campaign de SMS {#example-3-sms-campaign}

Suponha que o agente do Decisioning Studio esteja otimizando campos em uma Campaign de SMS. A configuração pode ser assim:

![Exemplo de Campaign de SMS no Decisioning Studio - configuração]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Exemplo de Campaign de SMS no Decisioning Studio - propriedades]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Resultando na seguinte mensagem:

![Exemplo de Campaign de SMS no Decisioning Studio - resultado]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurar a integração com o SFMC {#set-up-sfmc-integration}

O Decisioning Studio oferece integração nativa com o Salesforce Marketing Cloud. O Decisioning Studio dispara eventos de API em uma jornada com os dados necessários para preencher elementos dinâmicos.

{% alert important %}
Ao configurar casos de uso, **os IDs de API devem ser inseridos em letras maiúsculas**. Isso inclui IDs de jornada, IDs de Campaign e quaisquer outros identificadores. Se os IDs de API forem inseridos em letras minúsculas, mas seus dados do SFMC contiverem UUIDs em maiúsculas, os filtros de eventos não corresponderão e as métricas de relatório não serão preenchidas corretamente.
{% endalert %}

{% endtab %}
{% tab Outras plataformas %}

## Configurar integrações com outras plataformas {#set-up-other-cep-integrations}

O Decisioning Studio pode se integrar com qualquer plataforma de engajamento com clientes. No entanto, isso pode exigir algum trabalho de engenharia personalizado da sua equipe, já que o Decisioning Studio não consegue disparar comunicações diretamente.

Nesse cenário, o agente entrega um "arquivo de recomendação". Esse arquivo contém linhas para cada cliente, com colunas que indicam todas as decisões personalizadas para aquele cliente.

Por exemplo, o seguinte arquivo de recomendação:

![Exemplo de arquivo de recomendação no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Pode ser usado para otimizar uma Campaign de e-mail com a seguinte aparência:

![Exemplo de Campaign de e-mail personalizada no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Boas práticas {#best-practices}

Tenha estas boas práticas em mente ao se preparar para a orquestração:

1. **Comece com um escopo reduzido:** Use um canal e um ou dois modelos no início. Você pode expandir depois, conforme aprende o que funciona.
2. **Teste com cuidado:** Antes de lançar, teste sua integração com um pequeno grupo de usuários para verificar se o conteúdo dinâmico é preenchido corretamente.
3. **Documente sua configuração:** Mantenha um registro dos IDs de Campaigns, IDs de modelos, chaves de API e outros identificadores. Você precisará deles para fazer referência no portal do Decisioning Studio.
4. **Coordene com sua equipe:** A configuração da orquestração pode envolver equipes de marketing, engenharia e dados. Certifique-se de que todos entendam seu papel no processo.
5. **Planeje os dados de feedback:** A orquestração envia mensagens e coleta dados de engajamento e conversão que ajudam seu agente a aprender. Consulte [Preparar seus dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data) para mais detalhes.

## Próximas etapas {#next-steps}

Após configurar a orquestração, prossiga para projetar seu agente:

- [Projetar agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)