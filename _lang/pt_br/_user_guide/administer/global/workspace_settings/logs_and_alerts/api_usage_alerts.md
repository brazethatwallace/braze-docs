---
nav_title: Alertas de uso da API
article_title: Alertas de uso da API
description: "Este artigo fornece uma visão geral dos alertas de uso da API, que permitem detectar proativamente tráfego inesperado."
page_order: 0
---

# Alertas de uso da API {#api-usage-alerts}

> Os alertas de uso da API fornecem visibilidade crítica sobre o uso da sua API, permitindo que você detecte proativamente tráfego inesperado. Ao configurar esses alertas para monitorar volumes de solicitações de API, você pode receber notificações em tempo real e resolver problemas antes que eles impactem suas campanhas de marketing.

## Sobre os alertas de uso da API {#about-api-usage-alerts}

Você pode usar alertas de uso da API para monitorar volumes de solicitações para as seguintes categorias:

| Categoria da API | Detalhes |
|--------------|---------|
| Endpoints da REST API | Monitora o uso de todas as chamadas da REST API feitas para o backend da Braze, como enviar mensagens, criar campanhas ou exportar usuários. |
| Solicitações da API do SDK | Monitora as solicitações da API feitas a partir dos SDKs da Braze em apps clientes, como disparar mensagens no app ou sincronizar dados de usuários.<br><br>_*Disponível apenas para clientes que adquiriram Usuários Ativos Mensais – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre os alertas de uso da API" }

## Criando um alerta de uso da API {#creating-an-api-usage-alert}

Para criar um alerta de uso da API:

1. Acesse **Configurações** > **APIs e identificadores** > **Alertas de Uso da API** e crie um novo alerta.
2. Digite um nome para o seu alerta e escolha os endpoints da REST API e as chaves de API para as quais você gostaria de ser alertado.
3. Defina os critérios do alerta escolhendo um ou mais códigos de resposta e especificando os [limites do alerta](#api-usage-alert-thresholds).
4. Quando terminar, ative **Alerta ativado**.
    ![Um exemplo de alerta de uso da API que envia notificações quando o endpoint Track users aumenta em 100 por cento dentro de uma hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

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

Você pode configurar um alerta por e-mail, um alerta por webhook ou ambos. Alertas por webhook podem ser muito úteis para casos de uso como enviar um alerta para plataformas externas, como um canal do Slack. Para ver um exemplo, consulte nossa [documentação]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) sobre integração de alertas com o Slack nas preferências de notificação.

![Um e-mail será enviado para o endereço selecionado quando os critérios do alerta forem atingidos.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Exemplo de carga útil {#payload}

A seguir, um exemplo de carga útil para o corpo de um webhook de alerta de uso da API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Exemplos de alertas {#example-alerts}

Aqui estão algumas formas de configurar seus alertas de uso da API para ser notificado nos seguintes cenários.

{% tabs local %}
{% tab integridade da API %}
Você pode configurar alertas para monitorar a integridade geral da sua API. Por exemplo, você pode configurar esses alertas quando os erros da API aumentam drasticamente, como 20% em relação à hora anterior.

| Endpoint | Chave de API | Código de resposta | Condição do limite | Volume do limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | Todas as chaves de API | `4XX` e `5XX` | Aumentou em 10% | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}

{% tab limite de frequência do endpoint %}
Seja alertado quando seu espaço de trabalho atingir o limite de frequência para o endpoint `/users/track`. Você também pode aplicar essa configuração para outros endpoints da Braze.

| Endpoint | Chave de API | Código de resposta | Condição do limite | Volume do limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas as chaves de API | `429` | Maior ou igual a | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}

{% tab Campaigns disparadas por API %}
Essa configuração de alerta notifica você quando ocorrem erros em Campaigns e Canvas disparados por API, alguns dos quais podem ser de alta prioridade.

| Endpoint | Chave de API | Código de resposta | Condição do limite | Volume do limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Todas as chaves de API | `4XX` e `5XX` | Maior ou igual a | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}

{% tab integrações com parceiros %}
Use a seguinte configuração de alerta para ser notificado quando uma integração com parceiros parar de enviar dados para a Braze.

| Endpoint | Chave de API | Código de resposta | Condição do limite | Volume do limite | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos os endpoints | A chave de API usada para sua integração com parceiros | Todos os códigos de resposta | Menor ou igual a | 0 | 1 dia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemplos de alertas" }
{% endtab %}
{% endtabs %}

## Considerações {#considerations}

- Cada alerta ativo enviará apenas uma notificação por e-mail ou webhook a cada 8 horas. Isso é para evitar notificações excessivas de um único alerta. Se o seu alerta está notificando você prematuramente, considere editar os critérios do alerta para melhor atender ao seu caso de uso.
- Você pode ter até 10 alertas por espaço de trabalho.