---
nav_title: Respostas em cache
article_title: Respostas de Conteúdo conectado em cache
page_order: 2.5
description: "Este artigo aborda como armazenar em cache as respostas de Conteúdo conectado em diferentes campanhas ou mensagens no mesmo espaço de trabalho para otimizar a velocidade de envio."
---

# Respostas de Conteúdo conectado em cache {#cache-connected-content-responses}

> As respostas de Conteúdo conectado podem ser armazenadas em cache em diferentes campanhas ou mensagens (no mesmo espaço de trabalho) para otimizar a velocidade de envio.

A Braze não registra nem armazena permanentemente os **corpos de resposta** do Conteúdo conectado. Durante a renderização da mensagem, as respostas podem ser mantidas temporariamente (por exemplo, em memória e em cache) para que a Braze possa renderizar o Liquid e enviar a mensagem.

Para evitar o armazenamento em cache, você pode especificar `:no_cache`, o que pode causar aumento no tráfego de rede. Para ajudar na solução de problemas e no monitoramento da integridade do sistema, a Braze registra metadados de solicitações de Conteúdo conectado (como a URL da solicitação totalmente renderizada e o código de status da resposta) para chamadas bem-sucedidas e com falha. Esses registros são mantidos por até 30 dias.

{% details Renderização de Conteúdo conectado e tratamento de dados (avançado) %}
Esta seção oferece uma visão mais detalhada e de ponta a ponta de como a Braze renderiza Liquid e Conteúdo conectado e onde os dados podem existir temporariamente antes de uma mensagem ser enviada. Isso pode ajudar em revisões de privacidade e tratamento de dados.

## O que é e o que não é armazenado {#what-is-and-isnt-stored}

- **Corpo da resposta do Conteúdo conectado:** Não é armazenado permanentemente pela Braze. Pode ser mantido temporariamente em memória e, quando o cache está ativado, armazenado em cache com um tempo de vida (TTL).
- **Metadados da solicitação de Conteúdo conectado:** Metadados da solicitação, como a URL totalmente renderizada, o código de status HTTP e a duração da resposta, são registrados para solução de problemas e monitoramento. Esses registros são mantidos por até 30 dias.
- **Mensagem final renderizada:** Existe em memória durante a renderização. Também pode ser armazenada em outro lugar dependendo da sua configuração e canal (por exemplo, Arquivamento de mensagem ou Content Cards).

## Fluxo de renderização (visão geral) {#rendering-flow-high-level}

O fluxo a seguir descreve como a Braze renderiza e envia mensagens para canais baseados em provedor, como e-mail, SMS e push. Canais entregues via SDK, como Content Cards, usam a mesma renderização subjacente de Liquid e Conteúdo conectado, mas diferem em quando o conteúdo é gerado e como é entregue.

1. Um worker em segundo plano renderiza o modelo Liquid de uma mensagem quando ela está sendo preparada para entrega.
2. As tags de Conteúdo conectado são avaliadas durante a renderização do Liquid.
3. Para cada tag de Conteúdo conectado, a Braze verifica um cache de múltiplas camadas. Se não existir valor em cache (ou se o cache estiver desativado), a Braze chama seu endpoint e recebe a resposta.
4. A resposta é injetada no modelo Liquid e a mensagem é totalmente renderizada.
5. Para canais baseados em provedor, a mensagem renderizada é enviada ao provedor do canal e depois ao usuário. Para canais entregues via SDK, como Content Cards, o conteúdo renderizado é sincronizado com o SDK da Braze e pode ser gerado na primeira impressão ou no momento da exibição, quando é mostrado ao usuário.

## Onde as respostas de Conteúdo conectado podem existir temporariamente {#where-connected-content-responses-can-live-temporarily}

A Braze usa um cache de múltiplas camadas para respostas de Conteúdo conectado com TTLs entre cinco minutos e quatro horas, dependendo do uso de `:cache_max_age` e outras regras de cache:

- **Cache em memória do processo:** Cache transitório dentro do processo do worker. Os dados existem apenas durante a execução do job (até ~11 minutos com base no timeout do worker).
- **Cache local da máquina:** Um cache por worker, como uma instância local do Memcached.
- **Cache do cluster:** Um cache distribuído compartilhado entre workers, como um cluster Memcached.

Essas camadas de cache são voláteis e podem remover dados antes do TTL configurado.

## O que muda quando você usa `:no_cache` {#what-changes-when-you-use-no_cache}

Para endpoints que não estão hospedados dentro da infraestrutura da Braze, usar `:no_cache` impede que o corpo da resposta do Conteúdo conectado seja armazenado no Memcached. Nesses casos, a resposta existe apenas na memória do processo do worker durante a execução do job de renderização (até ~11 minutos). Para endpoints que resolvem para hosts internos da Braze, as respostas ainda podem ser armazenadas em cache conforme descrito em [Invalidação de cache](#cache-busting).

## Onde a saída final renderizada pode existir {#where-the-final-rendered-output-can-live}

- **Arquivamento de mensagem:** Se o Arquivamento de mensagem estiver ativado, a Braze pode gravar a mensagem final renderizada no bucket de armazenamento em nuvem configurado. Se a resposta do Conteúdo conectado estiver incluída na mensagem renderizada, ela será incluída na cópia arquivada.
- **Dispositivos dos usuários:** Após a entrega, o conteúdo da mensagem totalmente renderizada pode persistir nos dispositivos dos usuários por um período indeterminado.
- **Content Cards:** O conteúdo renderizado para Content Cards é armazenado em um banco de dados da Braze até que o cartão expire.
{% enddetails %}

## Configurações padrão de cache {#default-cache-settings}

O tempo de cache é de até cinco minutos (300 segundos). Você pode atualizar isso adicionando o parâmetro `:cache_max_age` à chamada de Conteúdo conectado. Exemplo:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Solicitações GET são armazenadas em cache por padrão. Você pode desativar o cache adicionando o parâmetro `:no_cache` à chamada de Conteúdo conectado.

Solicitações POST não são armazenadas em cache por padrão, mas você pode ativar o cache adicionando o parâmetro `:cache_max_age` à chamada de Conteúdo conectado. O tempo mínimo de cache é 5 minutos e o tempo máximo é 4 horas.

{% alert note %}
As configurações de cache não são garantidas. O cache pode reduzir as chamadas aos seus endpoints, então recomendamos usar múltiplas chamadas por endpoint dentro da duração do cache em vez de depender excessivamente do armazenamento em cache.
{% endalert %}

### Limite de tamanho do cache {#cache-size-limit}

O corpo da resposta do Conteúdo conectado pode ter até 1&nbsp;MB. Se o corpo da resposta for maior que 1&nbsp;MB, ele não será armazenado em cache.

## Tempo de cache {#cache-time}

O Conteúdo conectado armazenará em cache o valor retornado de endpoints GET por no mínimo cinco minutos. Se um tempo de cache não for especificado, o tempo padrão é de cinco minutos.

O tempo de cache do Conteúdo conectado pode ser configurado para ser mais longo com `:cache_max_age`, conforme mostrado no exemplo a seguir. O tempo mínimo de cache é cinco minutos e o tempo máximo é quatro horas. Os dados de Conteúdo conectado são armazenados em cache na memória usando um sistema de cache volátil, como o Memcached.

Como resultado, independentemente do tempo de cache especificado, os dados de Conteúdo conectado podem ser removidos do cache em memória da Braze antes do previsto. Isso significa que as durações de cache são sugestões e podem não representar de fato o período em que os dados estão garantidamente armazenados em cache pela Braze. Você pode ver mais solicitações de Conteúdo conectado do que esperaria com uma determinada duração de cache.

### Cache por segundos especificados {#cache-for-specified-seconds}

Este exemplo armazenará em cache por 900 segundos (ou 15 minutos).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Invalidação de cache {#cache-busting}

Para evitar que o Conteúdo conectado armazene em cache o valor retornado de uma solicitação GET, você pode usar a configuração `:no_cache`. No entanto, respostas de hosts internos da Braze ainda serão armazenadas em cache.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Certifique-se de que o endpoint de Conteúdo conectado fornecido pode lidar com grandes picos de tráfego antes de usar esta opção, caso contrário você provavelmente verá aumento na latência de envio (maiores atrasos ou intervalos de tempo mais amplos entre solicitação e resposta) devido à Braze fazer solicitações de Conteúdo conectado para cada mensagem individual.
{% endalert %}

Com um POST, não é necessário invalidar o cache, pois solicitações POST não são armazenadas em cache por padrão. Para armazenar em cache uma resposta POST, adicione `:cache_max_age`; para evitar o cache de um POST, omita `:cache_max_age`.

## Informações importantes {#things-to-know}

{% raw %}
- O cache pode ajudar a reduzir chamadas duplicadas de Conteúdo conectado. No entanto, não é garantido que sempre resulte em uma única chamada de Conteúdo conectado por usuário.
- O cache de Conteúdo conectado é baseado no espaço de trabalho, na URL da solicitação, no tipo de conteúdo da solicitação e no corpo da solicitação. Se a chamada de Conteúdo conectado for para a mesma URL, ela pode ser armazenada em cache entre Campaigns e Canvas.
- O cache é baseado em uma combinação única de URL, tipo de conteúdo e corpo da solicitação, não em um ID de usuário ou Campaign. Isso significa que a versão em cache de uma chamada de Conteúdo conectado pode ser usada por múltiplos usuários e Campaigns em um espaço de trabalho se a URL, o tipo de conteúdo e o corpo da solicitação forem os mesmos.
- O cache de Conteúdo conectado pode ser ignorado se a marcação da tag incluir qualquer um dos seguintes trechos de alta cardinalidade:
    - `{{${user_id}}}`
    - `{{${braze_id}}}`
    - `{{${email}}}`
    - `{{${email_address}}}`
    - `{{${phone_number}}}`
    - `{{${date_of_birth}}}`
{% endraw %}