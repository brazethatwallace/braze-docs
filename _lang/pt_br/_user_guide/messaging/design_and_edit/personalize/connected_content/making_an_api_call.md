---
nav_title: Fazer uma chamada de Conteúdo conectado
article_title: Fazer uma chamada de API de Conteúdo conectado
page_order: 0
description: "Este artigo de referência aborda como fazer uma chamada de API de Conteúdo conectado, além de exemplos úteis e casos de uso avançados de Conteúdo conectado."
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Fazer uma chamada de API de Conteúdo conectado {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Use o Conteúdo conectado para inserir qualquer informação acessível por API diretamente nas mensagens que você envia aos usuários. Você pode obter conteúdo diretamente do seu servidor web ou de APIs acessíveis publicamente.<br><br>Esta página aborda como fazer chamadas de API de Conteúdo conectado, casos de uso avançados de Conteúdo conectado, tratamento de erros e mais.

## Entendendo o volume de chamadas de Conteúdo conectado {#understanding-connected-content-call-volume}

{% alert important %}
Um envio não equivale a uma chamada de Conteúdo conectado. A Braze não garante uma proporção de 1:1 entre envios de mensagens e solicitações de Conteúdo conectado. O sistema é projetado para priorizar a renderização e a entrega corretas das mensagens em vez de minimizar o número de chamadas. Seus endpoints devem ser preparados para lidar com mais solicitações do que o número de destinatários ou mensagens enviadas.
{% endalert %}

A Braze pode fazer a mesma chamada de API de Conteúdo conectado mais de uma vez por destinatário. Os motivos mais comuns incluem:

- **E-mail com múltiplas partes:** Um único e-mail pode acionar passes de renderização separados para o corpo HTML, corpo em texto simples e versão Accelerated Mobile Pages (AMP) (se presente). Cada passe pode acionar o Conteúdo conectado naquela parte, então um destinatário pode gerar múltiplas chamadas idênticas ou semelhantes.
- **Validação e novas tentativas:** As cargas úteis das mensagens podem ser renderizadas múltiplas vezes por destinatário para validação, lógica de nova tentativa ou outros propósitos internos.
- **Comportamento do canal:** O Conteúdo conectado é executado quando a mensagem é renderizada. Para mensagens no app, a mensagem é renderizada no momento da impressão.

Se você observar mais chamadas de Conteúdo conectado nos seus registros do que envios ou destinatários, esse comportamento é esperado. Para orientações sobre como reduzir a carga e planejar para escala, consulte [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Enviando uma chamada de Conteúdo conectado {#sending-a-connected-content-call}

{% raw %}

Para enviar uma chamada de Conteúdo conectado, use a tag `{% connected_content %}`. Com essa tag, você pode atribuir ou declarar variáveis usando `:save`. Aspectos dessas variáveis podem ser referenciados posteriormente na mensagem com [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

Por exemplo, o corpo de mensagem a seguir acessará a URL `http://numbersapi.com/random/trivia` e incluirá uma curiosidade divertida na sua mensagem:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Adicionando variáveis {#adding-variables}

Você também pode incluir atributos do perfil do usuário como variáveis na string da URL ao fazer solicitações de Conteúdo conectado.

Por exemplo, você pode ter um serviço web que retorna conteúdo com base no endereço de e-mail e no ID de um usuário. Se você estiver passando atributos que contêm caracteres especiais, como o arroba (@), certifique-se de usar o filtro Liquid `url_param_escape` para substituir quaisquer caracteres não permitidos em URLs por suas versões escapadas compatíveis com URL, conforme mostrado no atributo de endereço de e-mail a seguir.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Os valores dos atributos devem estar cercados por `${}` para funcionar corretamente na nossa versão da sintaxe Liquid.
{% endalert %}

As solicitações de Conteúdo conectado suportam apenas solicitações GET e POST.

## Tratamento de erros {#error-handling}

Se a URL estiver indisponível e retornar uma página 404, a Braze renderizará uma string vazia no lugar. Se a URL retornar uma página HTTP 500 ou 502, a URL falhará na lógica de nova tentativa.

Se o endpoint retornar JSON, você pode detectar isso verificando se o valor `connected` é nulo e, em seguida, [abortar condicionalmente a mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content). A Braze permite apenas URLs que se comunicam pelas portas 80 (HTTP) e 443 (HTTPS).

### Detecção de host com problemas {#unhealthy-host-detection}

O Conteúdo conectado emprega um mecanismo de detecção de host com problemas para identificar quando o host de destino apresenta uma alta taxa de lentidão significativa ou sobrecarga, resultando em timeouts, excesso de solicitações ou outros resultados que impedem a Braze de se comunicar com sucesso com o endpoint de destino. Ele atua como uma proteção para reduzir a carga desnecessária que pode estar causando dificuldades ao host de destino. Também serve para estabilizar a infraestrutura da Braze e manter velocidades rápidas de envio de mensagens.

Se o host de destino apresentar uma alta taxa de lentidão significativa ou sobrecarga, a Braze interromperá temporariamente as solicitações ao host de destino por um minuto, simulando respostas que indicam a falha. Após um minuto, a Braze verificará a integridade do host usando um pequeno número de solicitações antes de retomar as solicitações em velocidade total, caso o host esteja saudável. Se o host ainda estiver com problemas, a Braze aguardará mais um minuto antes de tentar novamente.

Se as solicitações ao host de destino forem interrompidas pelo detector de host com problemas, a Braze continuará renderizando mensagens e seguindo sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Conteúdo conectado sejam refeitas quando interrompidas pelo detector de host com problemas, use a opção `:retry`. Para mais informações sobre a opção `:retry`, consulte [Novas tentativas de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Se você acredita que a detecção de host com problemas está causando problemas, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact).

{% alert note %}
Você pode adicionar URLs específicas a uma lista de permissões para uso com Conteúdo conectado. Para acessar esse recurso, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

{% alert tip %}
Para saber mais sobre códigos de erro comuns, consulte [Solução de problemas de webhooks e solicitações de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection).
{% endalert %}

### Limites de taxa (429) versus detecção de host com problemas {#rate-limits-429-versus-unhealthy-host-detection}

Os seguintes são mecanismos diferentes:

- **429 Too Many Requests:** Seu endpoint (ou um serviço upstream) está retornando essa resposta. Isso significa que seu servidor ou middleware está recusando tráfego, geralmente porque possui seu próprio limite de taxa. A Braze não aplica um limite de taxa separado ao Conteúdo conectado; o volume de solicitações de Conteúdo conectado escala diretamente com seu [limite de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting). Como as mensagens podem ser renderizadas múltiplas vezes por destinatário (por exemplo, para HTML de e-mail, texto simples e AMP), o número de solicitações de Conteúdo conectado pode exceder esse limite de taxa — não assuma que será menor ou igual às mensagens por minuto que você definiu. Se você estiver recebendo 429s, escale seu endpoint ou middleware para lidar com o volume esperado de solicitações, ou reduza o limite de taxa da Campaign ou etapa do Canvas para que menos mensagens (e, consequentemente, menos chamadas de Conteúdo conectado) sejam enviadas por minuto.
- **Detecção de host com problemas:** Uma proteção do lado da Braze que é acionada após uma alta taxa e volume de *falhas* em uma janela de um minuto. A contagem de falhas inclui os códigos de status `408`, `429`, `502`, `503`, `504` e `529`. Quando acionada, a Braze interrompe temporariamente as solicitações a esse host e simula uma resposta de falha. Isso é independente do seu próprio limite de taxa. Para limites de detecção e mais detalhes, consulte [Solução de problemas de webhooks e solicitações de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection). Para evitar acionar a detecção de host com problemas, certifique-se de que seu endpoint pode lidar com o volume de chamadas descrito em [Entendendo o volume de chamadas de Conteúdo conectado](#understanding-connected-content-call-volume) e [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Garantindo desempenho eficiente {#allowing-for-efficient-performance}

Como a Braze entrega mensagens em uma taxa muito rápida, certifique-se de que seu servidor pode lidar com milhares de conexões simultâneas para que não fique sobrecarregado ao buscar conteúdo. Ao usar APIs públicas, confirme que seu uso não violará nenhum limite de taxa que o provedor da API possa aplicar. A Braze exige que o tempo de resposta do servidor seja inferior a dois segundos por motivos de desempenho; se o servidor levar mais de dois segundos para responder, o conteúdo não será inserido.

Para mais informações sobre planejamento de capacidade de endpoints e redução do volume de chamadas, consulte [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Informações importantes {#things-to-know}

* A Braze não cobra por chamadas de API e elas não contam para o uso de pontos de dados.
* Há um limite de 1 MB para respostas de Conteúdo conectado.
* O Conteúdo conectado é executado quando a mensagem é renderizada. Para mensagens no app, a mensagem é renderizada no momento da impressão.
* As chamadas de Conteúdo conectado não seguem redirecionamentos.

## Práticas recomendadas para endpoints de alto volume {#best-practices-for-high-volume-endpoints}

Se suas mensagens usam Conteúdo conectado e você envia em alto volume, planeje para mais solicitações do que o número de destinatários ou envios:

1. **Estime a carga de pico:** Use um multiplicador conservador ao dimensionar seu endpoint ou middleware — as solicitações de Conteúdo conectado podem exceder o número de destinatários ou mensagens enviadas. Por exemplo, para e-mail, um único destinatário pode gerar múltiplas chamadas (HTML, texto simples e AMP), então destinatários × 2 ou × 3 é frequentemente usado como uma estimativa conservadora.
2. **Use cache quando apropriado:** Solicitações GET são armazenadas em cache por padrão. Para solicitações POST, adicione `:cache_max_age` quando a resposta puder ser reutilizada por um período (por exemplo, token ou conteúdo que não muda por solicitação). Consulte [Armazenando respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) e as [Perguntas frequentes sobre cache de POST](#what-is-caching-behavior) na seção a seguir.
3. **Defina o limite de taxa de velocidade de entrega:** O [limite de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) em Campaigns ou etapas do Canvas é a única alavanca para limitar indiretamente o volume de solicitações de Conteúdo conectado — a Braze não aplica limite de taxa ao Conteúdo conectado em si. É apenas um proxy, e não perfeito, porque as solicitações de Conteúdo conectado não são 1:1 com as mensagens. Use-o para manter o volume de mensagens (e, consequentemente, de Conteúdo conectado) dentro do que seu endpoint pode suportar.
4. **Projete para idempotência e novas tentativas:** A Braze pode chamar seu endpoint mais de uma vez por destinatário. Certifique-se de que seu endpoint pode tolerar solicitações duplicadas sem efeitos colaterais incorretos.

## Tipos de autenticação {#authentication-types}

### Usando autenticação básica {#using-basic-authentication}

Se a URL requer autenticação básica, a Braze pode armazenar uma credencial de autenticação básica para você usar na sua chamada de API. Você pode gerenciar credenciais de autenticação básica existentes e adicionar novas em **Configurações** > **Conteúdo conectado**.

![As configurações de Conteúdo conectado no dashboard da Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para adicionar uma nova credencial, selecione **Adicionar credencial** > **Autenticação básica**.

![Menu suspenso "Adicionar credencial" com a opção de usar autenticação básica ou autenticação por token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Dê um nome à sua credencial e insira o nome de usuário e a senha.

![A janela "Criar nova credencial" com a opção de inserir um nome, nome de usuário e senha.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Você pode então usar essa credencial de autenticação básica nas suas chamadas de API referenciando o nome do token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Se você excluir uma credencial, tenha em mente que quaisquer chamadas de Conteúdo conectado que tentem usá-la serão abortadas.
{% endalert %}

As credenciais armazenadas se aplicam a solicitações {% raw %}`{% connected_content %}`{% endraw %} enquanto a Braze renderiza uma mensagem. Elas não são aplicadas à solicitação HTTP principal configurada em uma etapa de [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials). Use cabeçalhos de solicitação ou uma tag {% raw %}`{% connected_content %}`{% endraw %} dentro de um campo de cabeçalho ou corpo do webhook quando precisar recuperar segredos para essa chamada.

### Usando autenticação por token {#using-token-authentication}

Ao usar o Conteúdo conectado da Braze, você pode descobrir que certas APIs exigem um token em vez de um nome de usuário e senha. A Braze também pode armazenar credenciais que contêm valores de cabeçalho de autenticação por token.

Para adicionar uma credencial que contém valores de token, selecione **Adicionar credencial** > **Autenticação por token**. Em seguida, adicione os pares chave-valor para os cabeçalhos da sua chamada de API e o domínio permitido.

![Um exemplo de token "token_credential_abc" com detalhes de autenticação por token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Você pode então usar essa credencial nas suas chamadas de API referenciando o nome da credencial:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Usando Open Authentication (OAuth) {#using-open-authentication-oauth}

Algumas configurações de API exigem a recuperação de um token de acesso que pode então ser usado para autenticar o endpoint da API que você deseja acessar.

#### Etapa 1: Recuperar o token de acesso {#step-1-retrieve-the-access-token}

O exemplo a seguir ilustra a recuperação e o salvamento de um token de acesso em uma variável local, que pode então ser usada para autenticar a chamada de API subsequente. Um parâmetro `:cache_max_age` pode ser adicionado para corresponder ao tempo de validade do token de acesso e reduzir o número de chamadas de Conteúdo conectado de saída. Consulte [Cache configurável]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#configurable-caching) para mais informações.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Etapa 2: Autorizar a API usando o token de acesso recuperado {#step-2-authorize-the-api-using-the-retrieved-access-token}

Após o token ser salvo, ele pode ser inserido dinamicamente na chamada de Conteúdo conectado subsequente para autorizar a solicitação:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### Editando credenciais {#editing-credentials}

Você pode editar o nome da credencial para os tipos de autenticação.

- Para autenticação básica, você pode atualizar o nome de usuário e a senha. Observe que a senha inserida anteriormente não ficará visível.
- Para autenticação por token, você pode atualizar os pares chave-valor do cabeçalho e o domínio permitido. Observe que os valores de cabeçalho definidos anteriormente não ficarão visíveis.


## Lista de permissões de IP do Conteúdo conectado {#connected-content-ip-allowlisting}

Quando uma mensagem usando Conteúdo conectado é enviada pela Braze, os servidores da Braze fazem automaticamente solicitações de rede aos servidores dos nossos clientes ou de terceiros para buscar dados. Com a lista de permissões de IP, você pode verificar que as solicitações de Conteúdo conectado estão realmente vindo da Braze, adicionando uma camada de segurança.

A Braze enviará solicitações de Conteúdo conectado a partir dos seguintes intervalos de IP. Os intervalos listados são adicionados automática e dinamicamente a quaisquer chaves de API que tenham sido habilitadas para a lista de permissões.

A Braze possui um conjunto reservado de IPs usados para todos os serviços, nem todos ativos em um determinado momento. Isso é projetado para que a Braze possa enviar a partir de um data center diferente ou realizar manutenção, se necessário, sem impactar os clientes. A Braze pode usar um, um subconjunto ou todos os IPs listados a seguir ao fazer solicitações de Conteúdo conectado.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Cabeçalho `User-Agent` {#user-agent-header}

A Braze inclui um cabeçalho `User-Agent` em todas as solicitações de Conteúdo conectado e webhooks, semelhante ao seguinte:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Tenha em mente que o valor do hash muda regularmente. Se você estiver filtrando tráfego por `User-Agent`, permita todos os valores que começam com `Braze Sender`.
{% endalert %}

## Solução de problemas {#troubleshooting}

Use o [Webhook.site](https://webhook.site/) para solucionar problemas nas suas chamadas de Conteúdo conectado e diagnosticar problemas com os cabeçalhos da solicitação, corpo da solicitação e outras informações que estão sendo enviadas na chamada.

1. Substitua a URL na sua chamada de Conteúdo conectado pela URL única gerada no site.
2. Pré-visualize e teste sua Campaign ou etapa do Canvas para ver as solicitações chegando a esse site.

Você também pode verificar se a Liquid tag inclui os parâmetros que seu endpoint espera (por exemplo, `:method`, `:headers`, `:content_type`, `:body` e `:basic_auth` quando necessário). Se você depende da chave de código de status HTTP em um objeto JSON salvo, o endpoint deve retornar um objeto JSON e um status `2XX`.

Para altas taxas de erro do seu host, consulte [Detecção de host com problemas]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) e [Volume de chamadas de Conteúdo conectado](#understanding-connected-content-call-volume).

## Perguntas frequentes {#frequently-asked-questions}

### Por que há mais chamadas de Conteúdo conectado do que usuários ou envios? {#why-are-there-more-connected-content-calls-than-users-or-sends}

A Braze pode fazer a mesma chamada de API de Conteúdo conectado mais de uma vez por destinatário para renderizar uma carga útil de mensagem. As cargas úteis das mensagens podem ser renderizadas múltiplas vezes por destinatário para validação, lógica de nova tentativa ou outros propósitos internos. No entanto, observe que apenas uma das chamadas de Conteúdo conectado preenche uma mensagem.

É esperado que uma chamada de API de Conteúdo conectado possa ser feita mais de uma vez por destinatário, mesmo que a lógica de nova tentativa não seja usada na chamada. Recomendamos definir o limite de taxa de quaisquer mensagens que contenham Conteúdo conectado ou configurar seus servidores para serem mais capazes de lidar com o volume esperado que considera múltiplas chamadas de Conteúdo conectado sendo feitas por envio de mensagem.

Consulte [Entendendo o volume de chamadas de Conteúdo conectado](#understanding-connected-content-call-volume) e [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints) para detalhes e mitigação.

### Como o limite de taxa funciona com o Conteúdo conectado? {#how-does-rate-limiting-work-with-connected-content}

O Conteúdo conectado não possui seu próprio limite de taxa. Em vez disso, o limite de taxa é baseado na taxa de envio de mensagens. Recomendamos definir o limite de taxa de envio de mensagens mais alto do que o limite de taxa pretendido para o Conteúdo conectado, caso haja mais chamadas de Conteúdo conectado do que mensagens enviadas.

### Qual é o comportamento de cache? {#what-is-caching-behavior}

Solicitações GET são armazenadas em cache por padrão (consulte [Armazenando respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)). **Solicitações POST não são armazenadas em cache por padrão**, mas você pode habilitar o cache adicionando `:cache_max_age` à chamada de Conteúdo conectado. Isso pode reduzir a carga no endpoint quando o mesmo POST (por exemplo, uma solicitação de token ou conteúdo) seria feito repetidamente dentro da janela de cache.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

O cache pode ajudar a reduzir chamadas duplicadas de Conteúdo conectado, mas não garante uma única chamada por usuário. A duração do cache é entre cinco minutos e quatro horas. Para detalhes completos, consulte [Armazenando respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

### Qual é o comportamento HTTP padrão do Conteúdo conectado? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### O que acontece se eu usar a mesma chamada de Conteúdo conectado em vários lugares? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

Cada tag de Conteúdo conectado é avaliada separadamente, mesmo que múltiplas tags usem a mesma URL e os mesmos parâmetros. Quando a URL e as configurações de cache permitem, solicitações idênticas podem ser servidas a partir do cache em vez de acionar uma nova solicitação de saída (consulte [Armazenando respostas em cache]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses) para detalhes).