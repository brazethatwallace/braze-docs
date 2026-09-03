---
nav_title: Fullstory
article_title: Fullstory
description: "Este artigo de referência descreve a parceria entre a Braze e a Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

> A plataforma de dados comportamentais da [Fullstory](https://www.fullstory.com/) ajuda líderes de tecnologia a tomar decisões melhores e mais bem informadas. Ao injetar dados comportamentais digitais em seu stack de análise de dados, a tecnologia patenteada da Fullstory libera o poder dos dados comportamentais de qualidade em escala, transformando cada visita digital em insights práticos.

*Essa integração é mantida pela Fullstory*

## Sobre esta integração {#about-this-integration}

Você pode aproveitar os insights do Fullstory na Braze para construir uma visão momento a momento da experiência de um usuário no website ou app, entregando mensagens hipercontextuais. A API de resumo de sessão do Fullstory permite capturar metadados detalhados sobre o comportamento de navegação de um usuário para uso no envio de mensagens da Braze, o que é especialmente poderoso quando utilizado em uma jornada de envio de mensagens de várias etapas, como um Canvas.

O valor em tempo real dos dados de resumo de sessão do Fullstory é melhor aproveitado por meio do Connected Content. Ao usar o Connected Content em uma etapa de contexto do Canvas, você pode armazenar os dados do Fullstory ao longo da jornada do Canvas de um usuário para uso em qualquer etapa subsequente do Canvas. Isso também elimina a necessidade de gravar esses dados em um perfil de usuário da Braze por meio de eventos personalizados ou atributos.

No exemplo a seguir, os dados de contexto do Canvas são utilizados em uma etapa de Canvas com Agent AI para gerar a mensagem ideal e incentivar o usuário a retomar um carrinho abandonado. No entanto, você pode aproveitar os dados para personalizar a mensagem diretamente, determinar a jornada do usuário com jornadas do público ou definir o texto e os ativos usados em etapas de envio de mensagens subsequentes.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

|Requisito     | Descrição |
|-----------------------|-----------------|
| Um token de autorização da API de sessão do Fullstory   | Consulte a Etapa 1 neste guia. |
| Um token de autorização de Connected Content da Braze ativado | Consulte a nota de Acesso Antecipado nesta seção. |
| Uma etapa de contexto do Canvas da Braze | Consulte a nota de Acesso Antecipado nesta seção. |
| Etapa de Braze AI Agent ativada | Consulte a nota de Acesso Antecipado nesta seção. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert important %}
Braze Agents, Canvas Context e tokens de autorização de Connected Content estão todos em Acesso Antecipado. Se você tem interesse em alavancar essa solução, fale com seu CSM da Braze sobre como ativar essas ferramentas.
{% endalert %}

## Integrar o Fullstory {#integrate-fullstory}

### Etapa 1: Configurar o Fullstory para habilitação da API de resumo de sessão {#step-1}

#### Etapa 1.1: Recuperar o token de autenticação para o endpoint da API de resumo de sessão {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

Para criar uma [chave de API do Fullstory](https://developer.fullstory.com/server/authentication/):

1. No Fullstory, acesse **Settings** > **API Keys**.
2. Selecione o nível de permissão **Standard**.
3. Copie o valor da chave imediatamente, pois ele aparece apenas uma vez.

#### Etapa 1.2: Criar um ID de perfil de resumo de sessão {#step-12-create-a-session-summary-profile-id}

Seguindo as [orientações do Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), crie um perfil de resumo de sessão usando o endpoint dedicado. É aqui que você define que tipo de dados deseja que a resposta do resumo de sessão forneça à Braze.

Na resposta a essa solicitação, o Fullstory fornece um ID de perfil de sessão. Esse ID de perfil é um componente essencial do corpo da solicitação de Connected Content usado no caso de uso a seguir.

### Etapa 2: Criar o token de autenticação do Connected Content {#step-2-create-the-connected-content-token-authentication}

1. Na Braze, acesse **Configurações** > **Configurações do espaço de trabalho** > **Connected Content** > **Adicionar credencial** > **Autenticação por token**.
2. Nomeie a autenticação como `fullstory`.
3. Adicione a chave de cabeçalho "Authorization". Forneça o valor do cabeçalho que o Fullstory disponibilizou na etapa anterior.
4. Em **Domínio permitido**, insira **api.fullstory.com**.

![Captura de tela da Braze mostrando os campos de edição de credencial]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## Casos de uso {#use-cases}

### Criar jornadas de mensagens dinâmicas {#create-dynamic-message-journeys}

Usando os [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) da Fullstory, você pode disparar Canvas da Braze imediatamente após interações importantes do usuário. O poder dessa integração está no `client_session_id` exclusivo (acessível via {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que o sistema passa automaticamente da Fullstory para a Braze. Esse ID funciona como uma chave, permitindo que a Braze busque o Resumo de Sessão completo de exatamente o que o usuário vivenciou.

Ao alavancar etapas de Contexto do Canvas e Connected Content, você pode usar esse ID para fazer uma requisição de API à Fullstory, recuperar os dados da sessão e armazená-los como uma variável para uso posterior na jornada.

![Etapa de Contexto do Canvas na Braze mostrando a variável de contexto "summary_result" sendo criada e preenchida com uma chamada de Connected Content para a Fullstory, para recuperar um resumo de sessão]({% image_buster /assets/img/fullstory/2.png %})

Com o token de autorização criado anteriormente, use a seguinte estrutura de requisição para obter os dados do resumo de sessão.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
A resposta é armazenada como a Liquid tag {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Use essa tag de Contexto nas etapas subsequentes do Canvas.
{% endalert %}

Nesta etapa, o Canvas pode acessar a resposta da chamada de Connected Content, que contém toda a carga útil da mensagem referente à sessão do usuário.

{% details Exemplo de carga útil da API de Resumo de Sessão %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

Você pode alavancar qualquer um dos dados disponíveis no objeto anterior usando a Liquid tag de contexto posteriormente na jornada do Canvas do usuário. As etapas a seguir mostram como usar esses dados em uma etapa de [Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

{% alert note %}
Para evitar comportamentos inesperados, inclua uma etapa de jornada do público após a etapa de Contexto, que pode remover os usuários do contexto se a tag de Contexto estiver vazia, indicando que a chamada de Connected Content falhou ou não retornou nenhuma informação.

![A etapa de jornada do público na Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### Produzir copy apropriado {#produce-appropriate-copy}

Ao criar uma [etapa de Agente]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) em um Canvas disparado pela Fullstory, e incluir a etapa de Contexto descrita nesta seção, você pode referenciar os dados de resumo de sessão da Fullstory no agente.

Neste exemplo, você usa esses dados para permitir que o agente da Braze gere o copy de mensagem apropriado para uso em um cartão de conteúdo, que pode incentivar o usuário a retornar ao carrinho abandonado.

![Captura de tela do criador de Contexto do Agente Braze com o prompt]({% image_buster /assets/img/fullstory/4.png %})

Use o mesmo nome para a Liquid tag de Contexto criada nesta etapa que a Liquid tag de contexto usada na etapa do Agente de IA criada anteriormente.

O prompt necessário varia de acordo com o seu caso de uso. Para práticas recomendadas sobre como criar prompts eficazes para agentes, consulte [Instruções de escrita]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions).

No seu Canvas, selecione uma etapa de Agente de IA e, em seguida, selecione o agente **Session Context** no menu suspenso. Salve a saída como uma variável — neste caso, "message" — que você pode inserir no copy da mensagem usando a Liquid tag {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Captura de tela da etapa do Canvas de Contexto do Agente Braze com o prompt]({% image_buster /assets/img/fullstory/5.png %})

Crie uma etapa de Mensagem que aproveite o copy criado pelo Agente de IA. Use a Liquid tag nesta etapa.

{% alert important %}
A API de Resumo de Sessão da Fullstory pode retornar dados sensíveis e identificáveis do usuário. Para garantir conformidade ao lidar com IPI (informações pessoais identificáveis), confirme que suas regras de captura de dados da Fullstory excluam IPI antes de usar este caso de uso.
{% endalert %}