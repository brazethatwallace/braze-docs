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

Defina um limite de volume para entradas de usuários ou mensagens enviadas, e a Braze notifica você por e-mail ou webhook se esse limite for ultrapassado. Você também pode criar vários alertas para o mesmo Canvas — por exemplo, um alerta para entradas de usuários e outro para mensagens enviadas.

Não sabe por onde começar? O [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) pode orientar você sobre como configurar um alerta de limite de Canvas.

## Etapa 1: Criar um alerta {#step-1-create-an-alert}

Os alertas são definidos no nível do Canvas, e você pode configurá-los tanto para Canvas ativos quanto para rascunhos. Para abrir a página **Gerenciar alertas** de um Canvas, faça uma das seguintes opções:

- Acesse **Messaging** > **Canvas** e selecione **Gerenciar alertas** no menu de contexto de um Canvas individual.
- Para Canvas ativos, abra **Canvas Analytics** e selecione **Gerenciar alertas**.

Na página **Gerenciar alertas**, selecione **Configurar alerta** para criar um novo alerta.

## Etapa 2: Nomeie seu alerta e selecione um Canvas {#step-2-name-your-alert-and-select-a-canvas}

Dê um nome ao seu alerta e confirme o Canvas ao qual ele se aplica.

![O painel Configurar Alerta mostrando os campos de nome do alerta e nome do Canvas, um grupo de regras vazio e uma barra lateral de resumo para regras de alerta, cronograma e notificações.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Etapa 3: Definir regras de alerta {#step-3-set-alert-rules}

As regras de alerta definem o limite que dispara uma notificação. Você pode criar regras usando duas métricas:

- **Entradas de usuários:** Número de usuários que entraram no Canvas
- **Mensagens enviadas:** Número de mensagens enviadas a partir do Canvas

Para cada regra, escolha uma comparação (menor que, maior que, menor ou igual a, maior ou igual a, ou igual a) e um limite de volume. Por exemplo, uma regra para "Entradas de usuários menor que 3.000" sinaliza um Canvas que normalmente alcança milhares de usuários, mas parou repentinamente — um sinal de um problema no público ou na entrada upstream que vale a pena investigar.

Você pode agrupar várias regras e combinar grupos de regras com lógica AND ou OR para criar condições de alerta mais específicas.

## Etapa 4: Definir o cronograma de alertas {#step-4-set-the-alert-schedule}

Defina a frequência com que suas regras de alerta são verificadas. Você pode configurar a frequência de verificação de 3 a 12 horas (em incrementos de 1 hora) ou a cada 24 horas. Depois de ativado, um alerta continua verificando nesse cronograma enquanto o alerta e o Canvas associado estiverem ativos.

## Etapa 5: Configurar notificações {#step-5-set-up-notifications}

Escolha quem deve ser notificado quando uma regra de alerta for atendida e como será notificado:

- **E-mail:** Adicione um ou mais endereços de e-mail de destinatários
- **Webhook:** Insira a URL do webhook para notificação e, opcionalmente, adicione cabeçalhos de solicitação personalizados exigidos pelo destino do seu webhook

Você pode ativar um ou ambos os métodos de notificação para um único alerta.

![A seção de notificações do painel Configurar Alerta, mostrando os botões de alternância de e-mail e webhook, um campo de destinatários de e-mail, um campo de URL de webhook, uma nota sobre o conteúdo da carga útil e campos opcionais de cabeçalho da solicitação.]({% image_buster /assets/img/canvas_threshold_alerts/notifications.png %})

Alertas por webhook são úteis para encaminhar notificações a plataformas externas, como um canal do Slack. Para saber mais, consulte a documentação do Slack sobre [envio de mensagens usando webhooks de entrada](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Cada notificação por webhook envia uma carga útil JSON com o nome do alerta, a janela de avaliação e as condições que dispararam o alerta.

### Exemplo de carga útil de webhook {#example-webhook-payload}

A seguir, um exemplo da carga útil JSON enviada em uma solicitação POST para o endpoint do seu webhook quando um alerta é disparado:

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
      "group_index": 0
    },
    {
      "subject": "messages_sent",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0
    }
  ]
}
```

## Etapa 6: Salvar seu alerta {#step-6-save-your-alert}

Revise as regras do alerta, o cronograma e as configurações de notificação no painel de resumo e selecione **Save alert**.

## Etapa 7: Ativar o alerta {#step-7-activate-the-alert}

Salvar um alerta não o ativa. Para ativá-lo, acesse a página **Gerenciar alertas** e use o botão **Status** do seu alerta. Um alerta permanece ativo até que você o desative ou até que o Canvas associado não esteja mais ativo. A coluna **Alertas configurados** na página do **Canvas** exibe um ícone de sino para qualquer Canvas com pelo menos um alerta salvo.

## Considerações {#considerations}

- **Canvas em rascunho:** Você pode configurar um alerta de limite para um Canvas que ainda está em rascunho, mas o alerta não começará a verificar suas regras até que o Canvas seja lançado.