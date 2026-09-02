---
nav_title: Alertas de uso da API or interface de programação do aplicativo (API)
article_title: Alertas de uso da API or interface de programação do aplicativo (API)
description: "Este artigo fornece uma visão geral dos alertas de uso da API or interface de programação do aplicativo (API), que permitem detectar proativamente tráfego inesperado."
page_order: 0
---

# Alertas de uso da API or interface de programação do aplicativo (API) {#api-usage-alerts}

> Os alertas de uso da API or interface de programação do aplicativo (API) fornecem visibilidade crítica sobre o uso da sua API or interface de programação do aplicativo (API), permitindo que você detecte proativamente tráfego inesperado. Ao configurar esses alertas para monitorar volumes de solicitações de API or interface de programação do aplicativo (API), você pode receber notificações em tempo real e resolver problemas antes que eles impactem suas campanhas de marketing.

## Sobre alertas de uso de API or interface de programação do aplicativo (API) {#about-api-usage-alerts}

Você pode usar alertas de uso de API or interface de programação do aplicativo (API) para monitorar volumes de solicitações nas seguintes categorias:

| Categoria de API or interface de programação do aplicativo (API) | Detalhes |
|--------------|---------|
| Endpoints da REST or transferir estado representacional API or interface de programação do aplicativo (API) | Rastreia o uso de todas as chamadas da REST or transferir estado representacional API or interface de programação do aplicativo (API) feitas ao backend da Braze, como envio de mensagens, criação de Campaigns ou exportação de usuários. |
| Solicitações de API or interface de programação do aplicativo (API) do SDK or kit de desenvolvimento de software | Rastreia solicitações de API or interface de programação do aplicativo (API) feitas a partir dos SDKs da Braze em apps de clientes, como disparar In-App Messages ou sincronizar dados de usuários.<br><br>_*Disponível apenas para clientes que adquiriram Monthly Active Users – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre alertas de uso de API or interface de programação do aplicativo (API)" }

## Criando um alerta de uso de API or interface de programação do aplicativo (API) {#creating-an-api-usage-alert}

Para criar um alerta de uso de API or interface de programação do aplicativo (API):

1. Acesse **Configurações** > **APIs e Identificadores** > **Alertas de uso de API or interface de programação do aplicativo (API)** e crie um novo alerta.
2. Insira um nome para o alerta e escolha os endpoints da REST or transferir estado representacional API or interface de programação do aplicativo (API) e as chaves de API or interface de programação do aplicativo (API) para os quais você deseja ser alertado.
3. Defina os critérios do alerta escolhendo um ou mais códigos de resposta e especificando os [limites do alerta](#api-usage-alert-thresholds).
4. Quando terminar, ative **Alerta ativado**.
    ![Exemplo de um alerta de uso de API que envia notificações quando o endpoint Track users aumenta em 100 por cento em uma hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Limites do alerta {#api-usage-alert-thresholds}

Ao definir os critérios do alerta, você pode ajustar os seguintes limites:

<table aria-label="Limites do alerta">
  <caption>Limites do alerta</caption>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condição do limite</td>
      <td>
        Define as condições que levam ao volume limite sobre o qual você gostaria de ser alertado. As seguintes opções são suportadas:<br><br>
        <ul>
          <li><strong>Aumentou em</strong> ou <strong>Diminuiu em</strong>: Compara as solicitações com o período anterior.</li>
          <li><strong>Aumentou em porcentagem</strong> ou <strong>Diminuiu em porcentagem</strong>: Compara a variação percentual das solicitações com o período anterior.</li>
          <li><strong>Maior ou igual a</strong> ou <strong>Menor ou igual a</strong>: Conta as solicitações em um período.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volume do limite</td>
      <td>Usado em conjunto com a condição do limite.</td>
    </tr>
    <tr>
      <td>Dentro de</td>
      <td>O período de avaliação do alerta.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites do alerta" }

## Configurando notificações de alerta {#setting-up-alert-notifications}

Você pode configurar um alerta por e-mail, um alerta por webhook ou ambos. Alertas por webhook podem ser muito úteis para casos de uso como enviar um alerta para plataformas externas, como um canal do Slack. Para ver um exemplo, consulte nossa [documentação]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) sobre a integração de alertas com o Slack para nossas preferências de notificação.

![Um e-mail será enviado para o endereço selecionado quando os critérios do alerta forem atingidos.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Exemplo de carga útil {#payload}

A seguir, um exemplo de carga útil para o corpo de um webhook de alerta de uso de API or interface de programação do aplicativo (API).

```json
{
  "text": "Your My First API Usage Alert alert has triggered. Please note that this alert is reset every 8 hours, and only one notification will be sent per reset period. You can view your alert and usage here: <link>.",
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "app_group_name": "My Workspace",
    "alert_criteria": {
      "response_codes": "201, 202 and 203",
      "threshold_condition": "increase by",
      "threshold_volume": "50%",
      "within": "1 hour"
    },
    "timeframe_start": "2025-03-20 15:35:00",
    "timeframe_end": "2025-03-20 16:35:00",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20 14:35:00",
    "previous_timeframe_end": "2025-03-20 15:35:00",
    "previous_volume": 1000
  }
}
```

{% alert note %}
Os campos `previous_timeframe_start`, `previous_timeframe_end` e `previous_volume` são opcionais e só aparecem quando o alerta usa uma condição de limite comparativa (`increase by`, `decrease by`). Esses campos são omitidos para alertas `greater than or equal` ou `less than or equal`.
{% endalert %}

#### Detalhes dos campos da carga útil {#payload-field-details}

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `text` | string | Mensagem de alerta legível. |
| `data.alert_name` | string | Nome do alerta. |
| `data.alert_type` | string | Tipo de alerta (sempre `"API Usage Alert"`). |
| `data.app_group_name` | string | Nome do espaço de trabalho. |
| `data.alert_criteria.response_codes` | string | Códigos de resposta selecionados para o alerta. Retorna `"all response codes"` se nenhum for selecionado, um código único como `"201"`, ou múltiplos códigos como `"201, 202 and 203"`. |
| `data.alert_criteria.threshold_condition` | string | Tipo de condição: `"increase by"`, `"decrease by"`, `"greater than or equal"` ou `"less than or equal"`. |
| `data.alert_criteria.threshold_volume` | string ou número | Valor do limite. Quando a condição usa uma porcentagem, é uma string terminando em `%` (por exemplo, `"50%"`). Quando a condição usa um valor numérico, é um número (por exemplo, `50`). |
| `data.alert_criteria.within` | string | Janela de tempo para avaliação do alerta (por exemplo, `"1 day"`). |
| `data.timeframe_start` | string | Início do período do alerta em formato UTC `YYYY-MM-DD HH:MM:SS`. |
| `data.timeframe_end` | string | Fim do período do alerta em formato UTC `YYYY-MM-DD HH:MM:SS`. |
| `data.volume` | número | Volume de requisições durante o período do alerta. |
| `data.previous_timeframe_start` | string | (Opcional) Início do período anterior. Presente apenas para condições de limite comparativas. |
| `data.previous_timeframe_end` | string | (Opcional) Fim do período anterior. Presente apenas para condições de limite comparativas. |
| `data.previous_volume` | número | (Opcional) Volume de requisições durante o período anterior. Presente apenas para condições de limite comparativas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Detalhes dos campos da carga útil" }

### Exemplos de alertas {#example-alerts}

Aqui estão algumas formas de configurar seus alertas de uso de API or interface de programação do aplicativo (API) para ser notificado nos cenários a seguir.

{% tabs local %}
{% tab Integridade da API or interface de programação do aplicativo (API) %}
Você pode configurar alertas para monitorar a integridade geral da sua API or interface de programação do aplicativo (API). Por exemplo, é possível configurar esses alertas quando os erros de API or interface de programação do aplicativo (API) aumentam drasticamente, como 20% em relação à hora anterior.

| Endpoint | Chave de API or interface de programação do aplicativo (API) | Código de resposta | Condição de limite | Volume de limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | Todas as chaves de API or interface de programação do aplicativo (API) | `4XX` e `5XX` | Aumento de 10% | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}

{% tab Limite de frequência do endpoint %}
Seja alertado quando seu espaço de trabalho atingir o limite de frequência para o endpoint `/users/track`. Você também pode aplicar essa configuração para outros endpoints da Braze.

| Endpoint | Chave de API or interface de programação do aplicativo (API) | Código de resposta | Condição de limite | Volume de limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas as chaves de API or interface de programação do aplicativo (API) | `429` | Maior ou igual a | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}

{% tab Campaigns disparadas por API or interface de programação do aplicativo (API) %}
Essa configuração de alerta notifica você quando ocorrem erros em Campaigns e Canvas disparados por API or interface de programação do aplicativo (API), alguns dos quais podem ser de alta prioridade.

| Endpoint | Chave de API or interface de programação do aplicativo (API) | Código de resposta | Condição de limite | Volume de limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Todas as chaves de API or interface de programação do aplicativo (API) | `4XX` e `5XX` | Maior ou igual a | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}

{% tab Integrações com parceiros %}
Use a configuração de alerta a seguir para ser alertado quando uma integração com parceiros parar de enviar dados para a Braze.

| Endpoint | Chave de API or interface de programação do aplicativo (API) | Código de resposta | Condição de limite | Volume de limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | A chave de API or interface de programação do aplicativo (API) usada para sua integração com parceiros | Todos os códigos de resposta | Menor ou igual a | 0 | 1 dia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}
{% endtabs %}

## Considerações {#considerations}

- Cada alerta ativo enviará apenas um e-mail ou notificação por webhook a cada 8 horas. Isso evita o envio de muitas notificações de um único alerta. Se o alerta estiver notificando você prematuramente, considere editar os critérios do alerta para que se adequem melhor ao seu caso de uso.
- Você pode ter até 10 alertas por espaço de trabalho.