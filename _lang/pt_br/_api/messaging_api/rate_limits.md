---
nav_title: Limites de taxa
article_title: Limites de taxa da API de envio de mensagens
page_order: 3
page_type: reference
description: "Saiba como funcionam os limites de taxa e os cabeçalhos de resposta da API de envio de mensagens."
hidden: true
---

# Limites de taxa da API de envio de mensagens {#messaging-api-rate-limits}

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API de envio de mensagens estão sujeitos a alterações.
{% endalert %}

A Braze aplica limites de taxa da API de envio de mensagens por espaço de trabalho. Se um espaço de trabalho exceder um limite, a Braze retorna um código de status `429 Too Many Requests`.

Os limites da API de envio de mensagens são separados dos limites padrão documentados para outros endpoints da REST API da Braze. Não presuma que um limite, janela de tempo, tamanho de carga útil ou cronograma de redefinição documentado para outro endpoint se aplique à API de envio de mensagens.

## Cabeçalhos de limite de taxa {#rate-limit-headers}

Quando informações de limite de taxa estão disponíveis, a resposta inclui os seguintes cabeçalhos:

| Cabeçalho | Descrição |
|---|---|
| `X-RateLimit-Limit` | O número máximo de solicitações permitidas no intervalo atual. |
| `X-RateLimit-Remaining` | O número de solicitações restantes na janela de limite de taxa atual. |
| `X-RateLimit-Reset` | O horário epoch UTC em que a janela de limite de taxa atual é redefinida. |
| `X-RateLimit-Retry-After` | O número de segundos a aguardar antes de tentar novamente uma solicitação com limite de taxa excedido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cabeçalhos de limite de taxa da API de envio de mensagens" }

Use esses cabeçalhos para reduzir ou pausar solicitações antes de atingir um limite. Os cabeçalhos podem não estar presentes em todas as respostas.

## Tratamento de limites de taxa {#handling-rate-limits}

Quando você receber uma resposta `429`:

1. Pare ou reduza as solicitações para o espaço de trabalho afetado.
2. Use `X-RateLimit-Retry-After`, quando presente, para determinar quanto tempo aguardar. Caso contrário, use `X-RateLimit-Reset`, quando disponível, para determinar quando retomar.
3. Tente novamente com backoff exponencial e um número máximo de tentativas.