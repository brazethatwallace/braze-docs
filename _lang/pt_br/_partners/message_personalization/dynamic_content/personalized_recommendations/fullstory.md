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

## Sobre essa integração {#about-this-integration}

Você pode alavancar os insights da Fullstory na Braze para criar imagens momento a momento da experiência de um usuário no website ou no app e fornecer envio de mensagens hipercontextuais. A API de resumo de sessão da Fullstory possibilita a captura de metadados detalhados sobre o comportamento de navegação de um usuário para uso no envio de mensagens da Braze, o que é particularmente poderoso quando aproveitado em uma jornada de envio de mensagens de várias etapas, como um Canvas.

O valor em tempo real dos dados de resumo de sessão da Fullstory é melhor aproveitado por meio do Connected Content. Ao usar o Connected Content em uma etapa do Canvas Context, é possível armazenar os dados da Fullstory durante toda a jornada do usuário no Canvas para uso em qualquer etapa subsequente do Canvas. Isso também evita a necessidade de gravar esses dados em um perfil de usuário da Braze por meio de eventos ou atributos personalizados.

No exemplo a seguir, os dados do Canvas Context são aproveitados em uma etapa de AI Agent do Canvas para gerar a mensagem ideal para incentivar um usuário a retomar um carrinho abandonado. No entanto, é possível aproveitar os dados para personalizar a mensagem diretamente, para determinar a jornada do usuário por meio de jornadas do público ou para determinar o texto ou os ativos usados nas etapas subsequentes do envio de mensagens.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa dos seguintes itens:

| Requisito | Descrição |
|-----------------------|-----------------|
| Um token de autorização da API de sessão da Fullstory | Consulte a Etapa 1 neste guia. |
| Um token de autorização de Connected Content da Braze ativado | Veja a nota de Acesso Antecipado nesta seção. |
| Uma etapa do Canvas Context da Braze | Veja a nota de Acesso Antecipado nesta seção. |
| Etapa de Braze AI Agent ativada | Veja a nota de Acesso Antecipado nesta seção. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert important %}
Braze Agents, Canvas Context e tokens de autorização de Connected Content estão todos em Acesso Antecipado. Se você tem interesse em aproveitar essa solução, fale com seu CSM da Braze sobre a ativação dessas ferramentas.
{% endalert %}

## Integrar a Fullstory {#integrate-fullstory}

### Etapa 1: Configurar a Fullstory para ativação da API de resumo de sessão {#step-1}

#### Etapa 1.1: Recuperar o token de autenticação para o endpoint da API de resumo de sessão {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

Para criar uma [chave de API da Fullstory](https://developer.fullstory.com/server/authentication/):

1. Na Fullstory, acesse **Settings** > **API Keys**.
2. Selecione o nível de permissão **Standard**.
3. Copie o valor da chave imediatamente, pois ele aparece apenas uma vez.

#### Etapa 1.2: Criar um ID de perfil de resumo de sessão {#step-12-create-a-session-summary-profile-id}

Seguindo [as orientações da Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), crie um perfil de resumo de sessão usando o endpoint dedicado. É aqui que você define o tipo de dados que deseja que a resposta do resumo de sessão forneça à Braze.

Na resposta a essa solicitação, a Fullstory fornece um ID de perfil de sessão. Esse ID de perfil é um componente-chave do corpo da solicitação de Connected Content usado no caso de uso a seguir.

### Etapa 2: Criar a autenticação do token de Connected Content {#step-2-create-the-connected-content-token-authentication}

1. Na Braze, acesse **Settings** > **Workspace Settings** > **Connected Content** > **Add Credential** > **Token Authentication**.
2. Nomeie a autenticação como `fullstory`.
3. Adicione a chave de cabeçalho "Authorization". Forneça o valor do cabeçalho que a Fullstory forneceu na etapa anterior.
4. Em **Allowed Domain**, insira **api.fullstory.com**.

![Captura de tela da Braze mostrando os campos de edição de credencial]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## Casos de uso {#use-cases}

### Criar jornadas de mensagens dinâmicas {#create-dynamic-message-journeys}

Usando os [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) da Fullstory, você pode disparar Canvas da Braze imediatamente após interações-chave do usuário. O poder dessa integração está no `client_session_id` exclusivo (acessível via {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que o sistema passa automaticamente da Fullstory para a Braze. Esse ID funciona como uma chave, permitindo que a Braze busque o resumo completo da sessão, exatamente o que o usuário experimentou.

Ao aproveitar as etapas do Canvas Context e o Connected Content, você pode usar esse ID para fazer uma solicitação de API à Fullstory, recuperar os dados da sessão e armazená-los como uma variável para uso posterior na jornada.

![Etapa do Canvas Context da Braze mostrando a variável de contexto "summary_result" sendo criada e preenchida com uma chamada de Connected Content à Fullstory para recuperar um resumo da sessão]({% image_buster /assets/img/fullstory/2.png %})

Com o token de autorização criado anteriormente, use a seguinte estrutura de solicitação para extrair os dados do resumo da sessão.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
A resposta é armazenada como a tag Liquid {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Use essa tag Context nas etapas subsequentes do Canvas.
{% endalert %}

Nesse estágio, o Canvas pode acessar a resposta à chamada de Connected Content, que contém toda a carga útil da mensagem para a sessão de um usuário.

{% details Exemplo de carga útil da API de resumo de sessão %}

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

É possível aproveitar qualquer um dos dados disponíveis no objeto acima usando a tag Liquid do contexto posteriormente na jornada do usuário no Canvas. As etapas a seguir mostram como você pode usar esses dados em uma etapa de [Agent]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step).

{% alert note %}
Para evitar comportamentos inesperados, inclua uma etapa de jornada do público após a etapa Context, que pode retirar os usuários do contexto se a tag Context estiver vazia, indicando que a chamada de Connected Content falhou ou não retornou nenhuma informação.

![Etapa de jornada do público na Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### Produzir texto apropriado {#produce-appropriate-copy}

Ao criar uma [etapa de Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) em um Canvas disparado pela Fullstory e incluir a etapa Context descrita nesta seção, você pode referenciar os dados de resumo de sessão da Fullstory no agente.

Neste exemplo, você usa esses dados para permitir que o agente da Braze gere um texto de mensagem apropriado para uso em um cartão de conteúdo, o que pode incentivar o usuário a retornar à cesta abandonada.

![Captura de tela do criador de contexto do Braze Agent com o prompt]({% image_buster /assets/img/fullstory/4.png %})

Use o mesmo nome para a tag Liquid de Context criada nesta etapa que a tag Liquid de contexto usada na etapa de AI Agent criada anteriormente.

O prompt necessário para o seu caso de uso varia. Para conhecer as práticas recomendadas para a criação de prompts de agente eficazes, consulte [Instruções de redação]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions).

No seu Canvas, selecione uma etapa de AI Agent e, em seguida, selecione o agente **Session Context** no menu suspenso. Salve a saída como uma variável, nesse caso "message", que pode ser colocada no texto da mensagem usando a tag Liquid {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Captura de tela da etapa do Canvas de contexto do Braze Agent com o prompt]({% image_buster /assets/img/fullstory/5.png %})

Crie uma etapa de mensagem que aproveite o texto criado pelo AI Agent. Use a tag Liquid nessa etapa.

{% alert important %}
A API de resumo de sessão da Fullstory pode retornar dados de usuários identificáveis e confidenciais. Para garantir a conformidade ao lidar com IPI (informações de identificação pessoal), certifique-se de que as regras de captura de dados da Fullstory excluam IPI antes de usar esse caso de uso.
{% endalert %}