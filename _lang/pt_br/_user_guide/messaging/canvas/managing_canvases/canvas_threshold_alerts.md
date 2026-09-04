---
nav_title: Alertas de Canvas
article_title: Alertas de limite de Canvas
page_order: 4
page_type: reference
description: "Este artigo de referência aborda como configurar alertas de limite para um Canvas, para que você seja notificado proativamente quando as entradas de usuários ou mensagens enviadas ficarem fora do intervalo esperado."
tool: Canvas
channel:
- email
- webhooks
---

# Alertas de limite de Canvas {#canvas-threshold-alerts}

> Os alertas de limite de Canvas avisam quando algo em um Canvas não está saindo como planejado, para que você possa identificar uma jornada parada ou uma queda inesperada antes que isso afete seus clientes.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Canvas threshold alerts' %}

Defina um limite de volume ou porcentagem para entradas de usuários ou mensagens enviadas, e a Braze notifica você por e-mail ou webhook se esse limite for ultrapassado. Você também pode criar vários alertas para o mesmo Canvas — por exemplo, um alerta para entradas de usuários e outro para mensagens enviadas.

Não sabe por onde começar? O [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) pode orientar você sobre como configurar um alerta de limite de Canvas.

## Etapa 1: Criar um alerta {#step-1-create-an-alert}

Os alertas são configurados no nível do Canvas, e você pode configurá-los tanto para Canvas ativos quanto para rascunhos. Para abrir a página **Gerenciar alertas** de um Canvas, você pode:

- Acessar **Messaging** > **Canvas** e selecionar **Gerenciar alertas** no menu de contexto de um Canvas individual
- Para Canvas ativos, abrir **Canvas Analytics** e selecionar **Gerenciar alertas**.

Na página **Gerenciar alertas**, selecione **Configurar alerta** para criar um novo alerta.

## Etapa 2: Nomeie seu alerta e selecione um Canvas {#step-2-name-your-alert-and-select-a-canvas}

Dê um nome ao seu alerta e confirme o Canvas ao qual ele se aplica.

![O painel Configurar alerta mostrando os campos de nome do alerta e nome do Canvas, um grupo de regras vazio e uma barra lateral de resumo para regras de alerta, cronograma e notificações.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Etapa 3: Definir regras de alerta {#step-3-set-alert-rules}

As regras de alerta definem o limite que dispara uma notificação. Você pode criar regras usando duas métricas:

- **Entradas de usuários:** Número de usuários que entraram no Canvas
- **Mensagens enviadas:** Número de mensagens enviadas a partir do Canvas

Para cada regra, escolha uma comparação (menor que, maior que, menor ou igual a, maior ou igual a, ou igual a), uma unidade e um limite.

- **Volume:** Compara a contagem absoluta na janela de verificação atual. Por exemplo, "Entradas de usuários menor que 3.000" sinaliza um Canvas que normalmente alcança milhares de usuários, mas parou repentinamente — um sinal de problema no público ou na entrada upstream que vale a pena investigar.
- **Porcentagem:** Compara a contagem atual com uma linha de base para esse Canvas. A linha de base é a média da mesma janela de tempo nos 7 dias anteriores. Por exemplo, se o alerta verifica a cada 3 horas, uma verificação das 14h às 17h compara com a média das sete janelas anteriores de 14h às 17h. Uma regra de "Mensagens enviadas menor que 50%" sinaliza uma queda para menos da metade do volume habitual.

Os limites são números inteiros. Para regras de porcentagem com **menor que** ou **menor ou igual a**, insira um valor de 1 a 100. Para **maior que**, **maior ou igual a** ou **igual a**, a porcentagem pode ser 0 ou superior, incluindo valores acima de 100, para que você possa alertar sobre um pico em relação à linha de base.

Você pode agrupar várias regras — incluindo a combinação de regras de volume e porcentagem — e combinar grupos de regras com lógica AND ou OR para criar condições de alerta mais específicas.

## Etapa 4: Definir o cronograma de alertas {#step-4-set-the-alert-schedule}

Defina com que frequência as regras de alerta são verificadas. Você pode definir a frequência de verificação de 3 a 12 horas (em incrementos de 1 hora) ou a cada 24 horas. Uma vez ativado, o alerta continua verificando nesse cronograma enquanto o alerta e o Canvas associado estiverem ativos.

## Etapa 5: Configurar notificações {#step-5-set-up-notifications}

Escolha quem deve ser notificado quando uma regra de alerta é acionada e como a notificação será enviada:

- **E-mail:** adicione um ou mais endereços de e-mail de destinatários
- **Webhook:** insira a URL do webhook para notificação e, opcionalmente, adicione cabeçalhos de solicitação personalizados exigidos pelo destino do webhook

Você pode ativar um ou ambos os métodos de notificação para um único alerta.

Alertas por webhook são úteis para encaminhar notificações a plataformas externas, como um canal do Slack. Para saber mais, consulte a documentação do Slack sobre [envio de mensagens usando webhooks de entrada](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Cada notificação por webhook envia uma carga útil JSON com o nome do alerta, a janela de avaliação e as condições que dispararam o alerta. Cada condição inclui um `threshold_unit` de `volume` ou `percentage`. Condições de porcentagem também incluem `percentage_metric_value` (a contagem observada como porcentagem em número inteiro da linha de base). `metric_value` é sempre a contagem absoluta.

### Exemplo de carga útil de webhook {#example-webhook-payload}

A seguir, um exemplo da carga útil JSON enviada em uma solicitação POST para o endpoint do seu webhook quando um alerta é disparado. A primeira condição é uma regra de volume. A segunda é uma regra de porcentagem: 51.235 mensagens enviadas, o que representa 57% da linha de base da mesma janela de 7 dias, em relação a um limite acima de 55%.

```json
{
  "alert": {
    "name": "Canvas Alert - August 6, 2026",
    "target_type": "CANVAS"
  },
  "evaluation_window_start": "2026-08-06T10:28:01Z",
  "evaluation_window_end": "2026-08-06T13:28:01Z",
  "conditions": [
    {
      "subject": "user_entries",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0,
      "threshold_unit": "volume"
    },
    {
      "subject": "messages_sent",
      "operator": "gt",
      "threshold_value": 55,
      "metric_value": 51235.0,
      "group_index": 0,
      "threshold_unit": "percentage",
      "percentage_metric_value": 57
    }
  ]
}
```

## Etapa 6: Salvar seu alerta {#step-6-save-your-alert}

Revise as regras do alerta, o cronograma e as configurações de notificação no painel de resumo e selecione **Save alert**.

## Etapa 7: Ativar o alerta {#step-7-activate-the-alert}

Salvar um alerta não o ativa. Para ativá-lo, acesse a página **Manage Alerts** e use o botão de alternância **Status** do seu alerta. Um alerta permanece ativo até que você o desative ou até que o Canvas associado a ele não esteja mais ativo. A coluna **Alerts Configured** na página **Canvas** exibe um ícone de sino para qualquer Canvas com pelo menos um alerta salvo.

## Considerações {#considerations}

- **Canvas em rascunho:** Você pode configurar um alerta de limite para um Canvas que ainda está em rascunho, mas o alerta não começará a verificar suas regras até que o Canvas seja lançado.
- **Linha de base de porcentagem:** As regras de porcentagem precisam de sete dias completos anteriores com a mesma janela após o lançamento do Canvas. Até que essas janelas existam, ou quando a média da linha de base for zero (nenhuma atividade nessas janelas anteriores), as regras de porcentagem não disparam uma notificação.

## Perguntas frequentes {#frequently-asked-questions}

### Os alertas de limite do Canvas contam para o uso de webhooks? {#do-canvas-threshold-alerts-count-toward-webhook-usage}

Não. Os alertas de limite do Canvas não contam para os limites de frequência de webhooks nem para as métricas de uso.