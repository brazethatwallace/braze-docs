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

Orquestração é a conexão entre o Decisioning Studio e a sua plataforma de engajamento com clientes (CEP). Depois que o seu agente de decisão determina a ação ideal para cada cliente, a orquestração executa essas decisões disparando comunicações personalizadas por meio da sua CEP.

Pense da seguinte forma:

- O **Decisioning Studio** decide *o que* enviar e *quando* enviar
- A **sua CEP** cuida de *como* enviar

## Escolha a sua CEP {#choose-your-cep}

O primeiro passo é escolher qual CEP usar com o Decisioning Studio. Sua escolha afeta a complexidade da configuração e os recursos disponíveis.

### CEPs compatíveis {#supported-ceps}

| CEP | Tipo de integração | Complexidade da configuração |
|-----|-----------------|------------------|
| **Braze** | Integração nativa via API (recomendada) | Baixa |
| **Salesforce Marketing Cloud** | Eventos de API + Journey Builder | Média |
| **Outras CEPs** | Personalizada (arquivo de recomendação) | Alta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CEPs compatíveis" }

{% alert tip %}
Se você já usa a Braze como sua CEP, recomendamos usar a integração nativa da Braze para a experiência de configuração mais fluida.
{% endalert %}

## Pré-requisitos {#prerequisites}

Antes de configurar a orquestração, reúna os itens a seguir com base na CEP escolhida.

{% tabs %}
{% tab Braze %}

| Requisito | Descrição |
|------|-------------|
| **Chave da API REST** | Uma nova chave de API com permissões para dados de usuários, mensagens, Campaigns, Canvas, Segments e modelos. |
| **URL do dashboard da Braze** | A URL da sua instância da Braze (por exemplo, `https://dashboard-01.braze.com`). |
| **ID do app** | A chave de API associada ao app que você deseja rastrear (encontrada em **Settings** > **App Settings**). |
| **Nome de exibição e endereço de e-mail** | As informações do remetente a serem usadas nas suas campanhas (encontradas em **Settings** > **Email Preferences**). |
| **Modelos base** | Os modelos de mensagem que o seu agente usará para orquestração. Você criará Campaigns disparadas por API para cada modelo. |
| **ID do usuário teste** | Um ID de usuário para testar a integração antes do lançamento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Requisito | Descrição |
|------|-------------|
| **Credenciais do pacote de app** | Client ID, Client Secret, Authentication Base URI, REST Base URI e SOAP Base URI de um pacote instalado com integração de API servidor-a-servidor. |
| **Permissões de API** | Escopos para canais, ativos, automações, jornadas, contatos, extensões de dados e eventos de rastreamento. |
| **Extensões de dados** | Você precisará de extensões de dados para dados de assinantes, dados de engajamento e recomendações. |
| **Modelos de e-mail** | Os modelos que você deseja que o Decisioning Studio use, com IDs de modelo para cada um. |
| **Acesso ao Journey Builder** | Acesso para criar e ativar jornadas de múltiplas etapas com fontes de entrada de eventos de API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% tab Outras CEPs %}

Se você está usando uma CEP diferente da Braze ou do Salesforce Marketing Cloud, o Decisioning Studio pode se integrar por meio de uma abordagem de arquivo de recomendação:

| Item | Descrição |
|------|-------------|
| **Capacidade de ingestão de dados** | Sua CEP deve ser capaz de ingerir arquivos de recomendação (normalmente CSV ou JSON) contendo decisões personalizadas para cada cliente. |
| **Suporte a conteúdo dinâmico** | Suas campanhas devem suportar o preenchimento de campos dinamicamente com base nos dados de recomendação. |
| **Recursos de engenharia personalizados** | Sua equipe precisará construir a integração para ler os arquivos de recomendação e disparar comunicações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% endtab %}
{% endtabs %}

## Planeje suas campanhas {#plan-your-campaigns}

Antes de configurar a orquestração, considere os seguintes detalhes:

### Modelos base {#base-templates}

Um modelo base é qualquer modelo de mensagem que o seu agente de decisão pode usar. Considere:

- **Quantos modelos?** Seu agente pode trabalhar com um modelo ou vários. Se forem vários, o agente pode personalizar qual modelo cada cliente recebe.
- **Quais canais?** E-mail, push, SMS ou uma combinação. Cada canal pode exigir modelos e campanhas separados.
- **Quais elementos dinâmicos?** Identifique quais partes da sua mensagem o agente vai personalizar (linhas de assunto, CTAs, ofertas, horários, etc.). Esses se tornarão propriedades de disparo de API ou placeholders dinâmicos.

### Configurações de reelegibilidade {#re-eligibility-settings}

Suas campanhas devem permitir que os usuários recebam mensagens várias vezes:

- Para testes, você vai querer enviar a mesma campanha para o mesmo usuário repetidamente
- Em produção, o agente pode determinar que a mesma campanha é ideal para um usuário em dias consecutivos

{% alert note %}
Embora a configuração de reelegibilidade seja necessária para testes, os agentes do Decisioning Studio são projetados para respeitar limites de frequência e não enviarão a mesma campanha para um usuário mais de uma vez por dia em produção.
{% endalert %}

### Propriedades de disparo de API {#api-trigger-properties}

Para integrações com a Braze, planeje quais dimensões o seu agente vai otimizar. Essas se tornam propriedades de disparo de API que passam valores dinâmicos para as suas campanhas:

| Exemplo de dimensão | Propriedade de disparo de API |
|-------------------|---------------------|
| Linha de assunto | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Call to action | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Oferta | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Valor do desconto | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Propriedades de disparo de API" }

## Configuração da integração {#integration-setup}

Selecione a sua CEP abaixo para começar a configuração da integração.

{% tabs %}
{% tab Braze %}

## Configurar a integração com a Braze {#set-up-braze-integration}

Siga estas etapas para integrar um agente do Decisioning Studio com os recursos de orquestração da Braze (a equipe de serviços da Braze estará disponível para ajudar):

### Etapa 1: Criar uma chave de API {#step-1-create-an-api-key}

Acesse **Settings** > **API Keys** e crie uma nova chave com as seguintes permissões:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Etapa 2: Configurar Campaigns disparadas por API {#step-2-set-up-api-triggered-campaigns}

Configure uma Campaign disparada por API para cada modelo base com propriedades de disparo de API para todas as dimensões otimizadas.

Um modelo base é qualquer modelo que o agente de decisão pode usar para orquestrar mensagens. Um agente de decisão pode ter 1 modelo base ou vários; nesse caso, escolher o modelo base certo para cada cliente será uma das decisões que o agente personaliza.

### Etapa 3: Configurar reelegibilidade {#step-3-configure-re-eligibility}

Certifique-se de que todas as Campaigns disparadas por API permitam que os usuários se tornem reelegíveis em até 15 minutos.

![Diagrama de limite de frequência do Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Embora o agente do Decisioning Studio nunca envie a mesma campanha mais de uma vez por dia, você vai querer ter a capacidade de enviar as mesmas campanhas várias vezes ao dia para fins de teste.
{% endalert %}

### Etapa 4: Adicionar placeholders dinâmicos {#step-4-add-dynamic-placeholders}

Esses servem como placeholders dinâmicos para as decisões que o agente do Decisioning Studio está otimizando.

#### Exemplo 1: Campaign de e-mail {#example-1-email-campaign}

Suponha que o agente do Decisioning Studio esteja otimizando uma Campaign de e-mail. A configuração pode ser assim:

![Exemplo de configuração de Campaign de e-mail no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Supondo que o agente esteja otimizando a escolha de modelos e a mensagem de Call to Action (CTA), uma Campaign disparada por API deve ser criada para cada modelo, e a seção de CTA de um modelo pode ficar assim:

![Exemplo de seção de CTA em um modelo de e-mail no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Exemplo 2: Campaign de push {#example-2-push-campaign}

Suponha que um agente do Decisioning Studio esteja otimizando a mensagem de uma Campaign de push. A configuração pode ser assim:

![Exemplo de configuração de Campaign de push no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Exemplo de propriedades de disparo de API para Campaign de push]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Resultando na seguinte mensagem:

![Exemplo de mensagem push resultante no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Exemplo 3: Campaign de SMS {#example-3-sms-campaign}

Suponha que o agente do Decisioning Studio esteja otimizando campos em uma Campaign de SMS. A configuração pode ser assim:

![Exemplo de configuração de Campaign de SMS no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Exemplo de propriedades de disparo de API para Campaign de SMS]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Resultando na seguinte mensagem:

![Exemplo de mensagem SMS resultante no Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurar a integração com o SFMC {#set-up-sfmc-integration}

O Decisioning Studio oferece suporte a integração nativa com o Salesforce Marketing Cloud. O Decisioning Studio dispara eventos de API em uma jornada com os dados necessários para preencher elementos dinâmicos.

Para etapas detalhadas sobre como configurar a integração com o SFMC, siga as [instruções do SFMC]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) na documentação do Decisioning Studio Go.

{% endtab %}
{% tab Outras CEPs %}

## Configurar integrações com outras CEPs {#set-up-other-cep-integrations}

O Decisioning Studio pode se integrar com qualquer plataforma de engajamento com clientes. No entanto, isso pode exigir algum trabalho de engenharia personalizado da sua equipe, já que o Decisioning Studio não pode disparar comunicações diretamente.

Nesse cenário, o agente entregará um "arquivo de recomendação". Esse arquivo contém linhas para cada cliente, com colunas que indicam todas as decisões personalizadas para aquele cliente.

Por exemplo, o seguinte arquivo de recomendação:

![Exemplo de arquivo de recomendação com decisões personalizadas por cliente]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Pode ser usado para otimizar uma Campaign de e-mail com a seguinte aparência:

![Exemplo de Campaign de e-mail otimizada com dados do arquivo de recomendação]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Práticas recomendadas {#best-practices}

Tenha estas práticas recomendadas em mente ao se preparar para a orquestração:

1. **Comece com um escopo reduzido.** Use um canal e um ou dois modelos no início. Você pode expandir depois, conforme aprende o que funciona.
2. **Teste com cuidado.** Antes de lançar, teste sua integração com um pequeno grupo de usuários para verificar se o conteúdo dinâmico é preenchido corretamente.
3. **Documente sua configuração.** Mantenha um registro dos IDs de Campaign, IDs de modelo, chaves de API e outros identificadores. Você precisará consultá-los no portal do Decisioning Studio.
4. **Coordene com a sua equipe.** A configuração da orquestração pode envolver equipes de marketing, engenharia e dados. Certifique-se de que todos entendam seu papel no processo.
5. **Planeje os dados de feedback.** A orquestração inclui o envio de mensagens e a coleta de dados de engajamento e conversão que ajudam o seu agente a aprender. Consulte [Preparar seus dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/) para mais detalhes.

## Próximas etapas {#next-steps}

Após configurar a orquestração, prossiga para projetar o seu agente:

- [Projetar agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents/)