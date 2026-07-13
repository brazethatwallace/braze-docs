---
article_title: Limites de taxa do espaço de trabalho
description: "Saiba como definir limites de taxa do espaço de trabalho para controlar como o limite de taxa geral da API da sua empresa é distribuído entre espaços de trabalho individuais, evitando que uma única integração ou equipe faça solicitações demais para um endpoint específico."
permalink: /workspace_rate_limits/
---

# Limites de taxa do espaço de trabalho {#workspace-rate-limits}

> Saiba como definir limites de taxa do espaço de trabalho para controlar como o limite de taxa geral da API da sua empresa é distribuído entre espaços de trabalho individuais, evitando que uma única integração ou equipe faça solicitações demais para um endpoint específico.

## Pré-requisitos {#prerequisites}

Os limites de taxa do espaço de trabalho estão disponíveis apenas para contratos da Braze sem pontos de dados. Além disso, você precisará de [permissões de administrador]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para gerenciar limites de taxa.

## Sobre os limites de taxa do espaço de trabalho {#about-workspace-rate-limits}

Por padrão, os limites de taxa no nível da empresa são compartilhados entre seus espaços de trabalho.

Com os limites de taxa do espaço de trabalho, você pode definir um número máximo de solicitações de API que um espaço de trabalho pode fazer para um endpoint de ingestão específico, como `/users/track` ou dados do SDK. Você também pode aplicar limites de taxa a um grupo de espaços de trabalho, o que significa que o limite é compartilhado entre todos os espaços de trabalho desse grupo.

Por exemplo, se o seu endpoint `/users/track` tem um limite de taxa no nível da empresa de 500.000 solicitações por hora, você poderia definir os seguintes limites de taxa do espaço de trabalho:

- Um limite de taxa de 10.000 solicitações por hora aplicado ao _Espaço de trabalho 1_
- Um limite de taxa compartilhado de 200.000 solicitações por hora aplicado ao _Espaço de trabalho 2_ e ao _Espaço de trabalho 3_
- Nenhum limite de taxa aplicado ao _Espaço de trabalho 4_, o que significa que o limite de taxa padrão no nível da empresa é utilizado

## Gerenciando limites de taxa do espaço de trabalho {#managing-workspace-rate-limits}

### Atribuindo um limite {#assigning-a-limit}

Para atribuir um novo limite de taxa para um ou mais espaços de trabalho, acesse **Configurações** > **Configurações de administrador** > **Limites de taxa do espaço de trabalho** e selecione **Atribuir limites de taxa**.

![A página "Limites de taxa do espaço de trabalho" no dashboard da Braze.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

Em seguida, escolha um endpoint e um ou mais espaços de trabalho e insira o limite de taxa. O limite pode ser qualquer número inteiro maior que 1.000 que não exceda o limite de taxa no nível da empresa.

Quando terminar, selecione **Atualizar limite de taxa**.

![A janela pop-up "Limite de taxa" com opções para escolher um endpoint, espaços de trabalho e limite de taxa.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
Se você escolher mais de um espaço de trabalho, o limite de taxa será compartilhado entre esse grupo de espaços de trabalho.
{% endalert %}

### Editando um limite {#editing-a-limit}

Para editar um limite de taxa de espaço de trabalho existente, acesse **Configurações** > **Configurações de administrador** > **Limites de taxa do espaço de trabalho** e selecione o <i class="fas fa-ellipsis-vertical" aria-label="Abrir menu de opções"></i> menu de reticências verticais e escolha **Editar**. O novo limite de taxa pode levar alguns minutos para entrar em vigor.

### Redefinindo um limite {#resetting-a-limit}

Para redefinir um limite de taxa existente e revertê-lo ao limite de taxa no nível da empresa, acesse **Configurações** > **Configurações de administrador** > **Limites de taxa do espaço de trabalho** e selecione o <i class="fas fa-ellipsis-vertical" aria-label="Abrir menu de opções"></i> menu de reticências verticais e escolha **Redefinir**.

## Monitorando o uso {#monitoring-usage}

### Cabeçalhos de resposta {#response-headers}

Por padrão, todas as respostas de ingestão incluem os seguintes cabeçalhos, que refletem o limite de taxa estável no nível da empresa.

Recomendamos usar esses cabeçalhos na lógica da sua integração para gerenciar limites de taxa de forma eficaz. Por exemplo, você pode reduzir o volume de solicitações à medida que se aproxima desses limites e usar o cabeçalho `Retry-After` para determinar quando tentar novamente.

| Nome do cabeçalho | Descrição |
| ----- | ----- |
| `X-RateLimit-Limit` | O número máximo de solicitações permitidas no período atual do limite de taxa. |
| `X-RateLimit-Remaining` | O número de solicitações restantes no período atual. |
| `X-RateLimit-Reset` | Quando o período atual do limite de taxa é redefinido (segundos epoch UTC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Códigos de erro {#error-codes}

Se um limite de taxa do espaço de trabalho for atingido, sua solicitação retornará um código de resposta `429` e os cabeçalhos incluirão um valor `Retry-After`. Esse valor representa o número de segundos até que o limite de taxa seja redefinido.

O valor `Retry-After` reflete o número de segundos até o início da próxima hora, quando o limite de taxa do espaço de trabalho é redefinido.

### Dashboard de uso da API {#api-usage-dashboard}

Para monitorar o volume de solicitações, códigos de resposta e comportamento de ingestão entre espaços de trabalho, você também pode usar o [dashboard de uso da API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/).

Você pode filtrar o dashboard para exibir `429 Workspace Rate Limited` ou `429 Company Rate Limited`, para identificar rapidamente se uma solicitação foi limitada pelo limite de taxa da empresa ou do espaço de trabalho.