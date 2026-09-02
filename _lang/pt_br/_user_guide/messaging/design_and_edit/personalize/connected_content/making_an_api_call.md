---
nav_title: Fazer uma chamada de Conteúdo conectado
article_title: Fazer uma chamada de API or interface de programação do aplicativo (API) de Conteúdo conectado
page_order: 0
description: "Este artigo de referência aborda como fazer uma chamada de API or interface de programação do aplicativo (API) de Conteúdo conectado, além de exemplos úteis e casos de uso avançados de Conteúdo conectado."
search_rank: 2
toc_headers: h2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Fazer uma chamada de API de Conteúdo conectado {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Use o Conteúdo conectado para inserir qualquer informação acessível por API or interface de programação do aplicativo (API) diretamente nas mensagens que você envia aos usuários. Você pode obter conteúdo diretamente do seu servidor web ou de APIs acessíveis publicamente.<br><br>Esta página aborda como fazer chamadas de API or interface de programação do aplicativo (API) de Conteúdo conectado, casos de uso avançados de Conteúdo conectado, tratamento de erros e mais.

## Sobre o volume de chamadas de Conteúdo conectado {#understanding-connected-content-call-volume}

{% alert important %}
Um envio não equivale a uma chamada de Conteúdo conectado. A Braze não garante uma proporção de 1:1 entre envios de mensagens e solicitações de Conteúdo conectado. O sistema é projetado para priorizar a renderização e a entrega corretas das mensagens em vez de minimizar o número de chamadas. Seus endpoints devem ser preparados para lidar com mais solicitações do que o número de destinatários ou mensagens enviadas.
{% endalert %}

A Braze pode fazer a mesma chamada de API or interface de programação do aplicativo (API) de Conteúdo conectado mais de uma vez por destinatário. Os motivos mais comuns incluem:

- **E-mail com múltiplas partes:** Um único e-mail pode acionar passes de renderização separados para o corpo HTML, corpo em texto simples e versão Accelerated Mobile Pages (AMP) (AMP) (se presente). Cada passe pode acionar o Conteúdo conectado naquela parte, então um destinatário pode gerar múltiplas chamadas idênticas ou semelhantes.
- **Validação e novas tentativas:** As cargas úteis das mensagens podem ser renderizadas múltiplas vezes por destinatário para validação, lógica de nova tentativa ou outros propósitos internos.
- **Comportamento do canal:** O Conteúdo conectado é executado quando a mensagem é renderizada. Para mensagens no app, a mensagem é renderizada no momento da impressão.

Se você observar mais chamadas de Conteúdo conectado nos seus registros do que envios ou destinatários, esse comportamento é esperado. Para orientações sobre como reduzir a carga e planejar para escala, consulte [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Enviar uma chamada de Connected Content {#send-a-connected-content-call}

Para enviar uma chamada de Connected Content, use a tag {% raw %}`{% connected_content %}`{% endraw %}. Com essa tag, atribua ou declare variáveis usando `:save`. Aspectos dessas variáveis podem ser referenciados depois na mensagem com [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

### Detalhamento da chamada de API or interface de programação do aplicativo (API) {#break-down-the-api-call}

O exemplo a seguir usa a API or interface de programação do aplicativo (API) Sunrise-Sunset e inclui o horário do nascer do sol de hoje em uma mensagem:

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

Veja o que cada parte faz:

| Componente | O que faz |
| --- | --- |
| Tag `connected_content` | Diz à Braze para fazer uma solicitação HTTP durante a renderização da mensagem. |
| `https://api.sunrise-sunset.org/v2` | O endpoint da API or interface de programação do aplicativo (API) que a Braze chama. |
| `lat=40.7128&lng=-74.0060` | Parâmetros de consulta para as coordenadas da cidade de Nova York. |
| `date=today` | Solicita dados do dia atual nessas coordenadas. |
| `:save result` | Armazena a resposta da API or interface de programação do aplicativo (API) em uma variável local chamada `result`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhamento da chamada de API or interface de programação do aplicativo (API)" }

### Como a resposta da API or interface de programação do aplicativo (API) Sunrise-Sunset funciona {#how-the-sunrise-sunset-api-response-works}

Esse endpoint retorna JSON com campos de nível superior como `sunrise`, `sunset` e `tzid`. Os horários são retornados no fuso horário do local por padrão (neste exemplo, horário de Nova York).

Por exemplo, o formato da resposta é semelhante a:

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### Mapear a resposta da API or interface de programação do aplicativo (API) para Liquid {#map-the-api-response-to-liquid}

Como a resposta é salva como `result`, faça referência a cada campo diretamente a partir desse objeto.

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

Use esse padrão sempre que salvar JSON do Connected Content:

1. Salve a resposta da API or interface de programação do aplicativo (API) com `:save`.
2. Encontre o campo desejado na resposta JSON.
3. Faça referência a ele em Liquid como `saved_variable.field_name`.

### Adicionar variáveis {#add-variables}

Você também pode incluir atributos de perfil de usuário como variáveis na string de URL ao fazer solicitações de Connected Content.

Por exemplo, você pode ter um serviço web que retorna conteúdo com base no endereço de e-mail e no ID de um usuário. Se estiver passando atributos que contêm caracteres especiais, como o arroba (@), use o filtro Liquid `url_param_escape` para substituir quaisquer caracteres não permitidos em URLs por suas versões escapadas compatíveis com URL, conforme mostrado no atributo de endereço de e-mail a seguir.

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Os valores de atributos devem estar entre `${}` para funcionar corretamente na nossa versão da sintaxe Liquid.
{% endalert %}

As solicitações de Connected Content aceitam apenas solicitações GET e POST.

## Tratamento de erros {#error-handling}

Se a URL estiver indisponível e retornar uma página 404, a Braze renderiza uma string vazia no lugar. Se a URL retornar uma página HTTP 500 ou 502, a URL falhará na lógica de nova tentativa.

Se o endpoint retornar JSON, você pode detectar isso verificando se o valor `connected` é nulo e, em seguida, [interromper condicionalmente a mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content). A Braze permite apenas URLs que se comunicam pela porta 80 (HTTP) e 443 (HTTPS).

### Detecção de host não íntegro {#unhealthy-host-detection}

O Connected Content emprega um mecanismo de detecção de host não íntegro para identificar quando o host de destino apresenta uma alta taxa de lentidão significativa ou sobrecarga, resultando em timeouts, excesso de solicitações ou outros cenários que impedem a Braze de se comunicar com sucesso com o endpoint de destino. Ele atua como uma proteção para reduzir a carga desnecessária que pode estar causando dificuldades no host de destino. Também serve para estabilizar a infraestrutura da Braze e manter velocidades de envio de mensagens rápidas.

Se o host de destino apresentar uma alta taxa de lentidão significativa ou sobrecarga, a Braze interrompe temporariamente as solicitações ao host de destino por um minuto, simulando respostas que indicam a falha. Após um minuto, a Braze verifica a integridade do host usando um pequeno número de solicitações antes de retomar as solicitações em velocidade total, caso o host seja considerado íntegro. Se o host ainda estiver não íntegro, a Braze aguarda mais um minuto antes de tentar novamente.

Se as solicitações ao host de destino forem interrompidas pelo detector de host não íntegro, a Braze continua a renderizar mensagens e seguir sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Connected Content sejam tentadas novamente quando forem interrompidas pelo detector de host não íntegro, use a opção `:retry`. Para saber mais sobre a opção `:retry`, consulte [Novas tentativas de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Se você acredita que a detecção de host não íntegro possa estar causando problemas, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact).

{% alert note %}
Você pode adicionar URLs específicas a uma lista de permissões para uso com o Connected Content. Para acessar esse recurso, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

{% alert tip %}
Para saber mais sobre códigos de erro comuns, consulte [Solução de problemas de solicitações de webhook e Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection).
{% endalert %}

### Limites de frequência (429) versus detecção de host não íntegro {#rate-limits-429-versus-unhealthy-host-detection}

Os seguintes são mecanismos diferentes:

- **429 Too Many Requests:** Seu endpoint (ou um serviço upstream) está retornando essa resposta. Isso significa que seu servidor ou middleware está recusando tráfego, geralmente porque possui seu próprio limite de frequência. A Braze não aplica um limite de frequência separado ao Connected Content; o volume de solicitações do Connected Content escala diretamente com o [limite de frequência de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting). Como as mensagens podem ser renderizadas várias vezes por destinatário (por exemplo, para HTML de e-mail, texto simples e AMP), o número de solicitações de Connected Content pode exceder esse limite de frequência — não assuma que será menor ou igual ao número de mensagens por minuto que você definiu. Se você estiver recebendo 429s, escale seu endpoint ou middleware para lidar com o volume de solicitações esperado, ou reduza o [limite de frequência de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) da Campaign ou do Canvas para que menos mensagens (e, consequentemente, menos chamadas de Connected Content) sejam enviadas por minuto.
- **Detecção de host não íntegro:** Uma proteção do lado da Braze que é acionada após uma alta taxa e volume de *falhas* em uma janela de um minuto. A contagem de falhas inclui os códigos de status `408`, `429`, `502`, `503`, `504` e `529`. Quando acionada, a Braze interrompe temporariamente as solicitações para esse host e simula uma resposta de falha. Isso é independente do seu próprio limite de frequência. Para limites de detecção e mais detalhes, consulte [Solução de problemas de solicitações de webhook e Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection). Para evitar acionar a detecção de host não íntegro, certifique-se de que seu endpoint consiga lidar com o volume de chamadas descrito em [Entendendo o volume de chamadas de Connected Content](#understanding-connected-content-call-volume) e [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Garantir desempenho eficiente {#allowing-for-efficient-performance}

Como a Braze entrega mensagens em uma taxa muito rápida, certifique-se de que seu servidor pode lidar com milhares de conexões simultâneas para que não fique sobrecarregado ao buscar conteúdo. Ao usar APIs públicas, confirme que seu uso não violará nenhum limite de frequência que o provedor da API or interface de programação do aplicativo (API) possa aplicar. A Braze exige que o tempo de resposta do servidor seja inferior a dois segundos por motivos de desempenho; se o servidor levar mais de dois segundos para responder, o conteúdo não será inserido.

Para saber mais sobre planejamento de capacidade de endpoints e redução do volume de chamadas, consulte [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Informações importantes {#things-to-know}

- A Braze não cobra por chamadas de API or interface de programação do aplicativo (API) e elas não contam para o uso de pontos de dados disponível.
- Há um limite de 1 MB para respostas de Connected Content.
- O Connected Content é executado quando a mensagem é renderizada. Para mensagens no app, a mensagem é renderizada no momento da impressão.
- As chamadas de Connected Content não seguem redirecionamentos. Apenas respostas `2xx` são tratadas como bem-sucedidas. Se o seu endpoint retornar um redirecionamento `3xx` (por exemplo, `301` ou `302`), a Braze não seguirá o redirecionamento até a URL final. Para sintomas e etapas de solução de problemas, consulte [Por que o Connected Content falha quando meu endpoint retorna um redirecionamento?](#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302).

### Como as chamadas de Connected Content são processadas {#how-connected-content-calls-are-processed}

As chamadas de Connected Content dentro de um único modelo de mensagem são executadas sequencialmente (de cima para baixo) durante a renderização do Liquid. Isso significa que chamadas posteriores podem referenciar variáveis definidas por chamadas anteriores. Neste exemplo, a primeira chamada recupera dados do usuário, e a segunda chamada usa esses dados para buscar preferências:

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### Envio global e volume de solicitações {#global-sending-and-request-volume}

Embora as chamadas de Connected Content sejam executadas sequencialmente dentro de uma única mensagem, as mensagens são enviadas em paralelo em suas Campaigns e Canvas. Envios de alto volume podem gerar tráfego significativo de solicitações para seus endpoints durante períodos de pico de envio. Para gerenciar e controlar esse tráfego — incluindo limites de frequência de envio de mensagens do espaço de trabalho, limite de frequência de velocidade de entrega e cache — consulte [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints).

## Práticas recomendadas para endpoints de alto volume {#best-practices-for-high-volume-endpoints}

Se suas mensagens usam Connected Content e você envia em alto volume, planeje para mais solicitações do que o número de destinatários ou envios:

- **Estime a carga de pico:** Use um multiplicador conservador ao dimensionar seu endpoint ou middleware — as solicitações de Connected Content podem exceder o número de destinatários ou mensagens enviadas. Por exemplo, para e-mail, um único destinatário pode gerar múltiplas chamadas (HTML, texto simples e AMP), então destinatários × 2 ou × 3 é frequentemente usado como uma estimativa conservadora.
- **Use cache quando apropriado:** Solicitações GET são armazenadas em cache por padrão. Para solicitações POST, adicione `:cache_max_age` quando a resposta puder ser reutilizada por um período (por exemplo, token ou conteúdo que não muda por solicitação). Consulte [Respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) e o [FAQ de cache POST](#what-is-caching-behavior) na seção a seguir.
- **Defina limites de frequência de mensagens:** [Limites de frequência de envio de mensagens do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) e [limite de frequência de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) em Campaigns ou Canvas limitam indiretamente o volume de solicitações de Connected Content — a Braze não limita a frequência do Connected Content em si. Esses são proxies, não perfeitos, porque as solicitações de Connected Content não têm relação 1:1 com as mensagens. Use-os para manter o volume de mensagens (e, consequentemente, de Connected Content) dentro do que seu endpoint pode suportar.
- **Projete para idempotência e tentativas repetidas:** A Braze pode chamar seu endpoint mais de uma vez por destinatário. Certifique-se de que seu endpoint consiga tolerar solicitações duplicadas sem efeitos colaterais incorretos.

## Tipos de autenticação {#authentication-types}

### Usando autenticação básica {#using-basic-authentication}

Se a URL exigir autenticação básica, a Braze pode armazenar uma credencial de autenticação básica para você usar em sua chamada de API or interface de programação do aplicativo (API). Você pode gerenciar credenciais de autenticação básica existentes e adicionar novas em **Settings** > **Connected Content**.

![As configurações de Connected Content no dashboard da Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para adicionar uma nova credencial, selecione **Add credential** > **Basic authentication**.

![Menu suspenso "Add credential" com a opção de usar autenticação básica ou autenticação por token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Dê um nome à sua credencial e insira o nome de usuário e a senha.

![A janela "Create New Credential" com a opção de inserir um nome, nome de usuário e senha.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Você pode então usar essa credencial de autenticação básica em suas chamadas de API or interface de programação do aplicativo (API) referenciando o nome do token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Se você excluir uma credencial, lembre-se de que todas as chamadas de Connected Content que tentarem usá-la serão abortadas.
{% endalert %}

As credenciais armazenadas são aplicadas às solicitações {% raw %}`{% connected_content %}`{% endraw %} enquanto a Braze renderiza uma mensagem. Elas não são aplicadas à solicitação HTTP principal configurada em uma etapa de [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials). Use cabeçalhos de solicitação ou uma tag {% raw %}`{% connected_content %}`{% endraw %} dentro de um campo de cabeçalho ou corpo do webhook quando precisar recuperar segredos para essa chamada.

### Usando autenticação por token {#using-token-authentication}

Ao usar o Connected Content da Braze, você pode perceber que certas APIs exigem um token em vez de um nome de usuário e senha. A Braze também pode armazenar credenciais que contêm valores de cabeçalho de autenticação por token.

Para adicionar uma credencial que contenha valores de token, selecione **Add credential** > **Token authentication**. Em seguida, adicione os pares de chave-valor para os cabeçalhos da sua chamada de API or interface de programação do aplicativo (API) e o domínio permitido.

![Um exemplo de token "token_credential_abc" com detalhes de autenticação por token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Você pode então usar essa credencial em suas chamadas de API or interface de programação do aplicativo (API) referenciando o nome da credencial:

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

### Usar Open Authentication (OAuth) {#use-open-authentication-oauth}

Algumas configurações de API or interface de programação do aplicativo (API) exigem a recuperação de um token de acesso que pode então ser usado para autenticar o endpoint de API or interface de programação do aplicativo (API) que você deseja acessar.

#### Etapa 1: recuperar o token de acesso {#step-1-retrieve-the-access-token}

O exemplo a seguir ilustra a recuperação e o salvamento de um token de acesso em uma variável local, que pode então ser usada para autenticar a chamada de API or interface de programação do aplicativo (API) subsequente. Um parâmetro `:cache_max_age` pode ser adicionado para corresponder ao tempo de validade do token de acesso e reduzir o número de chamadas de Connected Content enviadas. Para saber mais, consulte [Cache configurável]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

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

{% alert note %}
Quando o endpoint de token espera `application/x-www-form-urlencoded` e você passa credenciais em `:body`, codifique em URL quaisquer caracteres especiais nos valores dos parâmetros. Por exemplo, barras (`/`) se tornam `%2F` e sinais de mais (`+`) se tornam `%2B`. Caracteres especiais não codificados podem fazer com que as solicitações de token OAuth falhem.
{% endalert %}

#### Etapa 2: autorizar a API or interface de programação do aplicativo (API) usando o token de acesso recuperado {#step-2-authorize-the-api-using-the-retrieved-access-token}

Depois que o token é salvo, ele pode ser inserido dinamicamente como template na chamada de Connected Content subsequente para autorizar a solicitação:

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
- Para autenticação por token, você pode atualizar os pares de chave-valor do cabeçalho e o domínio permitido. Observe que os valores de cabeçalho definidos anteriormente não ficarão visíveis.

## Lista de permissões de IP do Connected Content {#connected-content-ip-allowlisting}

Quando uma mensagem usando Connected Content é enviada pela Braze, os servidores da Braze fazem automaticamente solicitações de rede aos servidores de nossos clientes ou de terceiros para recuperar dados. Com a lista de permissões de IP, você pode verificar se as solicitações de Connected Content estão realmente vindo da Braze, adicionando uma camada de segurança.

A Braze enviará solicitações de Connected Content a partir dos seguintes intervalos de IP. Os intervalos listados são adicionados automática e dinamicamente a quaisquer chaves de API or interface de programação do aplicativo (API) que tenham sido incluídas na lista de permissões.

A Braze tem um conjunto reservado de IPs usados para todos os serviços, e nem todos estão ativos em um determinado momento. Isso foi projetado para que a Braze possa enviar a partir de um data center diferente ou realizar manutenção, se necessário, sem impactar os clientes. A Braze pode usar um, um subconjunto ou todos os IPs listados a seguir ao fazer solicitações de Connected Content.

Se as solicitações de Connected Content retornarem consistentemente `403 Forbidden` e a autenticação estiver configurada corretamente, adicione esses IPs à lista de permissões no servidor que recebe a solicitação. Um `403` também pode indicar permissões insuficientes ou credenciais inválidas, então confirme tanto as configurações de rede quanto as de autenticação. Para orientações específicas sobre webhooks, consulte [403 Forbidden e lista de permissões de IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Usando a lista de permissões de IP com Amazon S3 {#using-ip-allowlisting-with-amazon-s3}

Ao usar Connected Content para recuperar arquivos do Amazon S3, configure seu bucket para permitir solicitações HTTP `GET` não autenticadas a partir dos endereços IP da Braze.

1. **Adicione uma política de bucket com condições de IP:** Conceda `s3:GetObject` nos objetos do seu bucket com `Principal: "*"` e uma condição `IpAddress` que use os [intervalos de IP da Braze](#connected-content-ip-allowlisting) para sua instância. Você não precisa definir ACLs de leitura pública em objetos individuais.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["{YOUR_BRAZE_IP_RANGE}"]
        }
      }
    }
  ]
}
```

Substitua `{YOUR_BRAZE_IP_RANGE}` pelos intervalos de IP da Braze para sua instância listados em [Lista de permissões de IP do Connected Content](#connected-content-ip-allowlisting). Você pode adicionar um ou mais intervalos como valores separados no array `aws:SourceIp`.

{: start="2"}
2. **Revise as configurações de S3 Block Public Access:** Políticas de bucket que usam `Principal: "*"` são tratadas como acesso público pela AWS, mesmo com condições de IP. Pode ser necessário permitir o acesso público baseado em política de bucket enquanto mantém o acesso público baseado em ACL bloqueado.

3. **Use a URL do objeto S3 na sua tag de Connected Content:** Referencie o objeto com sua URL padrão do S3 (por exemplo, `https://your-bucket.s3.amazonaws.com/path/to/object.json`).

Para saber mais sobre políticas de bucket e chaves de condição, consulte a [documentação da AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html).

## Cabeçalhos da solicitação de saída {#outgoing-request-headers}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

As solicitações de webhook também enviam um `User-Agent` que começa com `Braze Sender` quando você não definiu esse cabeçalho.

## Solução de problemas {#troubleshooting}

Se a sua chamada de Connected Content não está sendo renderizada corretamente ou não está sendo renderizada, verifique os seguintes detalhes:

- **Inspecione a solicitação e a resposta em tempo real:** Use o [Depurador de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) em **prévia & Test**.
- **Confirme se uma chamada de Connected Content foi feita:** Você pode verificar se uma chamada foi feita na [guia histórico de mensagens]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab). Você também pode fazer um envio de teste de uma única solicitação de Connected Content.
- **Verifique pelo Postman ou por uma solicitação CURL se a solicitação esperada funciona:** Se a solicitação funcionar e retornar uma resposta, compare a solicitação em detalhes (incluindo cabeçalhos). Confirme se os cabeçalhos estão capturados em pares chave-valor com aspas duplas.
- **Valide se a autorização está sendo tratada corretamente:** Confirme se a opção `:basic_auth`/`:auth_credentials` está sendo usada e se a autorização de Connected Content foi adicionada às configurações do espaço de trabalho de Connected Content. Às vezes, a URL de Connected Content exige cabeçalhos além da autenticação que precisam ser inseridos.
- **Verifique se os dados estão no formato esperado:** Para o corpo da resposta, a Braze faz o parse de JSON válido em um objeto Liquid; caso contrário, a resposta é tratada como texto simples (incluindo HTML). A opção `:content_type` define os cabeçalhos `Content-Type` e `Accept` de saída na sua solicitação e não afeta o parse da resposta. Para o `:body` da solicitação, se o seu JSON contiver espaços, siga as orientações na seção [Fornecendo corpo JSON]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#providing-json-body).
- **Confirme se os dados foram analisados corretamente:** Verifique se o Liquid está referenciando corretamente o campo esperado. Para JSON aninhado, use {% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %} para apontar para o campo aninhado desejado. Você pode verificar as propriedades do JSON aninhado imprimindo o resultado esperado com {% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %}.
- **Verifique o código de status da resposta:** O código de status da resposta deve ser um código `2XX`. O Connected Content não tem como consumir a resposta quando o código não é `2XX`.

Gere uma prévia em **prévia & Test** e selecione **View details** para abrir o [Depurador de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger). O depurador lista os cabeçalhos da sua tag de Connected Content. Para os cabeçalhos que a Braze adiciona à solicitação de saída, consulte [Cabeçalhos de solicitação de saída](#outgoing-request-headers).

Você também pode verificar se a Liquid tag inclui os parâmetros que o seu endpoint espera (por exemplo, `:method`, `:headers`, `:content_type`, `:body` e `:basic_auth`, quando necessário). Se você depende da chave de código de status HTTP em um objeto JSON salvo, o endpoint deve retornar um objeto JSON e um status `2XX`.

Para taxas de erro elevadas do seu host, consulte [Detecção de host com problemas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content) e [Volume de chamadas de Connected Content](#understanding-connected-content-call-volume).

### Codificação de "e" comercial em solicitações POST de e-mail {#ampersand-encoding-in-email-post-requests}

Em mensagens de e-mail, o parse de HTML converte automaticamente os "e" comerciais (`&`) dentro de blocos {% raw %}`{% capture %}`{% endraw %} para `&amp;`. Para solicitações POST `application/x-www-form-urlencoded`, isso faz com que a solicitação envie nomes de parâmetros com o prefixo `amp;` (por exemplo, `amp;username`), o que pode quebrar a chamada de API or interface de programação do aplicativo (API).

Para contornar esse problema, use o filtro `replace` para remover o prefixo `amp;` antes de passar o corpo para `:body`:

{% raw %}
```liquid
{% capture body_with_amps %}
grant_type=client_credentials&username=test&password=test
{% endcapture %}
{% connected_content https://api.example.com/token
   :method post
   :body {{body_with_amps | replace: "amp;", ""}}
   :content_type application/x-www-form-urlencoded
   :save token
%}
```
{% endraw %}

## Perguntas frequentes {#frequently-asked-questions}

### Por que o Connected Content falha quando meu endpoint retorna um redirecionamento (301 ou 302)? {#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302}

Um redirecionamento pode fazer com que o Connected Content renderize em branco na prévia ou no envio, ou registre um erro no Message Activity Log com código de status HTTP `301` ou `302`. O Postman e outros clientes geralmente seguem redirecionamentos automaticamente, então uma URL pode funcionar no Postman, mas falhar na Braze.

Configure seu endpoint para retornar uma resposta `2xx` (normalmente `200`) com o corpo da resposta na URL que a Braze chama. Se essa URL retornar um redirecionamento, substitua-a pela URL de destino final.

Para verificações relacionadas quando o conteúdo renderiza em branco, consulte [Connected Content não retorna corpo de resposta]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#connected-content-returns-no-response-body).

### Por que há mais chamadas de Connected Content do que usuários ou envios? {#why-are-there-more-connected-content-calls-than-users-or-sends}

A Braze pode fazer a mesma chamada de API or interface de programação do aplicativo (API) de Connected Content mais de uma vez por destinatário para renderizar a carga útil da mensagem. As cargas úteis de mensagens podem ser renderizadas várias vezes por destinatário para validação, lógica de nova tentativa ou outros fins internos. No entanto, observe que apenas uma das chamadas de Connected Content preenche uma mensagem.

É esperado que uma chamada de API or interface de programação do aplicativo (API) de Connected Content possa ser feita mais de uma vez por destinatário, mesmo que a lógica de nova tentativa não seja usada na chamada. Recomendamos configurar o limite de frequência de qualquer mensagem que contenha Connected Content ou configurar seus servidores para lidar melhor com o volume esperado que considera múltiplas chamadas de Connected Content sendo feitas por envio de mensagem.

Consulte [Entendendo o volume de chamadas de Connected Content](#understanding-connected-content-call-volume) e [Práticas recomendadas para endpoints de alto volume](#best-practices-for-high-volume-endpoints) para detalhes e mitigação.

### Como o limite de frequência funciona com o Connected Content? {#how-does-rate-limiting-work-with-connected-content}

O Connected Content não tem seu próprio limite de frequência. Em vez disso, o limite de frequência é baseado na taxa de envio de mensagens. Recomendamos configurar o limite de frequência de envio de mensagens acima do limite de frequência pretendido para o Connected Content, caso haja mais chamadas de Connected Content do que mensagens enviadas.

### Qual é o comportamento de cache? {#what-is-caching-behavior}

Requisições GET são armazenadas em cache por padrão (consulte [Armazenamento de respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)). **Requisições POST não são armazenadas em cache por padrão**, mas você pode ativar o cache adicionando `:cache_max_age` à chamada de Connected Content. Isso pode reduzir a carga no endpoint quando o mesmo POST (por exemplo, uma solicitação de token ou conteúdo) seria feito repetidamente dentro da janela de cache.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

O cache pode ajudar a reduzir chamadas duplicadas de Connected Content, mas não garante uma única chamada por usuário. A duração do cache é entre cinco minutos e quatro horas. Para detalhes completos, consulte [Armazenamento de respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

### Qual é o comportamento HTTP padrão do Connected Content? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### O que acontece se eu usar a mesma chamada de Connected Content em vários lugares? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

Cada tag de Connected Content é avaliada separadamente, mesmo que várias tags usem a mesma URL e os mesmos parâmetros. Quando a URL e as configurações de cache permitem, requisições idênticas podem ser servidas a partir do cache em vez de disparar uma nova requisição de saída (consulte [Armazenamento de respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) para detalhes).