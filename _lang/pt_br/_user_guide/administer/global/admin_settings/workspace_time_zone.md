---
nav_title: Fusos horários do espaço de trabalho
article_title: Fusos horários do espaço de trabalho
alias: /workspace_time_zones/
page_order: 3
description: "Este artigo de referência cobre como configurar diferentes fusos horários para seus espaços de trabalho da Braze, proporcionando mais controle sobre o agendamento de Campaigns e Canvas para equipes que operam em várias localizações geográficas."
toc_headers: h2
---

# Fusos horários do espaço de trabalho {#workspace-time-zones}

> Os fusos horários do espaço de trabalho permitem que os administradores definam fusos horários específicos para espaços de trabalho individuais. Isso faz com que Campaigns agendadas e Canvas (que não usam horário local ou Intelligent Timing) sejam enviados de acordo com o fuso horário designado do espaço de trabalho, em vez do fuso horário geral da empresa.

{% alert important %}
Os fusos horários do espaço de trabalho para envio de mensagens estão sendo disponibilizados gradualmente. Talvez você ainda não veja essas configurações no seu dashboard.
{% endalert %}

Por padrão, um novo espaço de trabalho herda o fuso horário definido para sua empresa. Os administradores podem substituir esse padrão para um ou mais espaços de trabalho com fusos horários do espaço de trabalho. Quando um fuso horário do espaço de trabalho é definido, Campaigns agendadas e Canvas dentro desse espaço de trabalho referenciam esse novo fuso horário para seus horários de envio.

Por exemplo, se um fuso horário do espaço de trabalho é definido como PST, e uma Campaign dentro desse espaço de trabalho está agendada para ser enviada às 15h PST, ela será entregue às 15h PST. Isso é verdade mesmo que o fuso horário geral da sua empresa seja diferente (como EST, onde 15h PST seria 18h EST).

## Gerenciar fusos horários do espaço de trabalho {#manage-workspace-time-zones}

Se você é um administrador, pode acessar e gerenciar fusos horários do espaço de trabalho indo para **Settings** > **Admin Settings** > **Workspace Time Zones**.

Aqui, você pode visualizar uma lista de todos os seus espaços de trabalho, o fuso horário definido para cada um e a última vez que o fuso horário foi editado. Use a barra de pesquisa para encontrar espaços de trabalho específicos pelo nome.

![Página "Workspace Time Zones" com uma lista de espaços de trabalho, seus respectivos fusos horários e quando os fusos horários foram editados pela última vez.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Definindo um fuso horário {#setting-a-time-zone}

{% alert note %}
Pode levar alguns minutos para que as atualizações de fuso horário entrem em vigor.
{% endalert %}

{% tabs %}
{% tab Individual %}
1. Localize o espaço de trabalho desejado na lista.
2. Selecione o ícone **Edit** ao lado do nome do espaço de trabalho.

![Botão "Edit" ao lado do nome de um espaço de trabalho.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. No menu suspenso, selecione o fuso horário desejado para esse espaço de trabalho.
4. Selecione **Save**.

![Menu suspenso com o fuso horário GMT selecionado.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Múltiplas %}

Você pode aplicar um fuso horário específico a vários espaços de trabalho de uma só vez fazendo o seguinte:

1. Marque as caixas ao lado de todos os espaços de trabalho que deseja atualizar.
2. Selecione **Edit time zone**.
3. No menu suspenso, selecione um fuso horário para aplicar a todos os espaços de trabalho selecionados.

![Página "Workspace time zones" com vários espaços de trabalho selecionados e um botão "Edit time zone".]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. Selecione **Save**.

{% endtab %}
{% endtabs %}

## Impacto em Campaigns e Canvas {#impact-on-campaigns-and-canvases}

{% alert important %}
Informe as equipes e partes interessadas relevantes dentro de cada espaço de trabalho sobre quaisquer alterações de fuso horário para evitar confusão sobre os agendamentos de Campaigns.
{% endalert %}

- **Campaigns com horário local e Intelligent Timing:** Campaigns e Canvas que usam o horário local do usuário ou [Intelligent Timing]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/#option-3-intelligent-timing) para entrega continuarão funcionando como antes e não serão afetados pelos fusos horários do espaço de trabalho.
- **Campaigns e Canvas agendados:** Qualquer Campaign ou Canvas agendado que não use o horário local do usuário ou Intelligent Timing para entrega agora será enviado com base no fuso horário selecionado do espaço de trabalho.
- **Campaigns agendadas antes de uma alteração de fuso horário:** Se você agendou uma Campaign ou Canvas antes de alterar o fuso horário do espaço de trabalho, a Braze mantém o horário de envio original e não o reagenda. Por exemplo, se uma Campaign está configurada para ser enviada às 19h PST e o fuso horário do espaço de trabalho é alterado para EST, a Campaign ainda será enviada às 19h PST (que agora corresponde a 22h EST). O sistema continuará referenciando o horário original, mas o interpretará através do novo fuso horário do espaço de trabalho.

## Impacto em filtros de público baseados em data {#impact-on-date-based-audience-filters}

Quando um fuso horário do espaço de trabalho é atualizado, os filtros de público que usam critérios baseados apenas em data (onde nenhum horário específico é fornecido) são reavaliados com base nos limites do novo fuso horário.

Para filtros como "Realizou o evento personalizado X pela última vez após", a Braze usa o fuso horário do espaço de trabalho para determinar o início e o fim do dia no calendário. Alterar essa configuração muda o ponto de corte das 23h59 para aquela data específica.

### Exemplo {#example}

Um espaço de trabalho atualiza seu fuso horário de Eastern Time (EST) para Pacific Time (PST).

- **Horário de corte anterior:** 23h59 EST
- **Novo horário de corte:** 23h59 PST (que é 2h59 EST do dia seguinte)

Após essa alteração, um usuário que realiza o evento personalizado às 22h PST em 6 de março de 2026 (que é 1h EST em 7 de março de 2026) agora é incluído no público, pois ele se enquadrou dentro do limite do calendário PST para aquela data.

## Impacto nos dados de desempenho {#impact-on-performance-data}

Atualizar o fuso horário do seu espaço de trabalho afeta como os dados de desempenho são agregados e exibidos no seu dashboard. Como as análises de dados como *usuários ativos diários* (DAU) dependem do fuso horário do espaço de trabalho para definir o início e o fim de um dia de 24 horas, uma alteração nessa configuração desloca essas janelas de relatório.

Quando você altera o fuso horário, pode notar flutuações ou "deslocamentos" nos seus dados históricos. Isso ocorre porque a janela de 0h a 23h59 foi movida em relação ao UTC.

Considere o seguinte exemplo para um espaço de trabalho que move seu fuso horário de UTC para PST (UTC-8):

- **Antes da alteração:** Um "dia" para relatórios é medido de 0h UTC a 23h59 UTC.
- **Após a alteração:** Um "dia" para relatórios agora é medido de 0h PST a 23h59 PST.

Como resultado, um evento que ocorreu à 1h UTC em 1º de janeiro teria sido contabilizado anteriormente nas estatísticas de 1º de janeiro. Após a alteração para PST, esse mesmo evento (que ocorreu às 17h PST em 31 de dezembro) seria atribuído às métricas do dia anterior no relatório atualizado.