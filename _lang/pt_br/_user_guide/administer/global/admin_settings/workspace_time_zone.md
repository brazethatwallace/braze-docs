---
nav_title: Fusos horários do espaço de trabalho
article_title: Fusos Horários de Espaço de Trabalho para Envio de Mensagens
alias: /workspace_time_zones/
page_order: 3
description: "Este artigo de referência cobre como configurar diferentes fusos horários para seus espaços de trabalho Braze, proporcionando mais controle sobre o agendamento de campanhas e Canvases para equipes que operam em várias localizações geográficas."
---

# Fusos horários de espaço de trabalho para envio de mensagens

> Os fusos horários de espaço de trabalho permitem que os administradores definam fusos horários específicos para espaços de trabalho individuais. Isso faz com que campanhas agendadas e Canvases (que não usam fuso local ou Intelligent Timing) sejam enviadas de acordo com o fuso horário designado do espaço de trabalho, em vez do fuso horário geral da empresa.

{% multi_lang_include early_access_beta_alert.md feature='Workspace time zones' %}

Por padrão, um novo espaço de trabalho herda o fuso horário definido para sua empresa. Os administradores podem substituir esse padrão para um ou mais espaços de trabalho com fusos horários de espaço de trabalho. Quando um fuso horário de espaço de trabalho é definido, campanhas agendadas e Canvases dentro desse espaço de trabalho referenciam esse novo fuso horário para seus horários de envio.

Por exemplo, se um fuso horário de espaço de trabalho é definido como PST, e uma campanha dentro desse espaço de trabalho está agendada para ser enviada às 15h PST, ela será entregue às 15h PST. Isso é verdade mesmo que o fuso horário geral da sua empresa seja diferente (como EST, onde 15h PST seria 18h EST).

## Gerenciando fusos horários de espaço de trabalho

Se você é um administrador, pode acessar e gerenciar fusos horários de espaço de trabalho indo para **Configurações** > **Configurações de administrador** > **Fusos horários do espaço de trabalho**.

Aqui, você pode visualizar uma lista de todos os seus espaços de trabalho, o fuso horário definido para cada um e a última vez que o fuso horário foi editado. Use a barra de pesquisa para encontrar espaços de trabalho específicos pelo nome.

![Página "Fusos horários do espaço de trabalho" com uma lista de espaços de trabalho, seus respectivos fusos horários e quando os fusos horários foram editados pela última vez.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Definindo um fuso horário

{% alert note %}
Pode levar alguns minutos para que as atualizações de fuso horário entrem em vigor.
{% endalert %}

{% tabs %}
{% tab Individual %}
1. Localize o espaço de trabalho desejado na lista.
2. Selecione o ícone **Editar** ao lado do nome do espaço de trabalho.

![Botão "Editar" ao lado do nome de um espaço de trabalho.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. No menu suspenso, selecione o fuso horário desejado para esse espaço de trabalho.
4. Selecione **Salvar**.

![Menu suspenso com o fuso horário GMT selecionado.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Múltiplas %}

Você pode aplicar um fuso horário específico a vários espaços de trabalho de uma só vez fazendo o seguinte:

1. Marque as caixas ao lado de todos os espaços de trabalho que deseja atualizar.
2. Selecione **Editar fuso horário**.
3. No menu suspenso, selecione um fuso horário para aplicar a todos os espaços de trabalho selecionados.

![Página "Fusos horários do espaço de trabalho" com vários espaços de trabalho selecionados e um botão "Editar fuso horário".]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. Selecione **Salvar**.

{% endtab %}
{% endtabs %}

## Impacto em campanhas e Canvas

{% alert important %}
Informe as equipes e partes interessadas relevantes dentro de cada espaço de trabalho sobre quaisquer alterações de fuso horário para evitar confusão sobre os agendamentos de campanhas.
{% endalert %}

- **Campanhas com horário local e Intelligent Timing:** Campanhas e Canvas que usam o horário local do usuário ou [Intelligent Timing]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/#option-3-intelligent-timing) para entrega continuarão funcionando como antes e não serão afetados pelos fusos horários de espaço de trabalho.
- **Campanhas e Canvas agendados:** Qualquer campanha ou Canvas agendado que não use o horário local do usuário ou Intelligent Timing para entrega agora será enviado com base no fuso horário selecionado do espaço de trabalho.
- **Campanhas agendadas antes de uma alteração de fuso horário:** Se você agendou uma campanha ou Canvas antes de alterar o fuso horário do espaço de trabalho, a Braze mantém o horário de envio original e não o reagenda. Por exemplo, se uma campanha está configurada para ser enviada às 19h PST e o fuso horário do espaço de trabalho é alterado para EST, a campanha ainda será enviada às 19h PST (que agora corresponde a 22h EST). O sistema continuará referenciando o horário original, mas o interpretará através do novo fuso horário do espaço de trabalho.

## Impacto em filtros de público baseados em data

Quando um fuso horário de espaço de trabalho é atualizado, os filtros de público que usam critérios baseados apenas em data (onde nenhum horário específico é fornecido) são reavaliados com base nos limites do novo fuso horário.

Para filtros como "Realizou o evento personalizado X pela última vez após", a Braze usa o fuso horário do espaço de trabalho para determinar o início e o fim do dia no calendário. Alterar essa configuração muda o ponto de corte das 23h59 para aquela data específica.

### Exemplo

Um espaço de trabalho atualiza seu fuso horário de Eastern Time (EST) para Pacific Time (PST).

- **Horário de corte anterior:** 23h59 EST
- **Novo horário de corte:** 23h59 PST (que é 2h59 EST do dia seguinte)

Após essa alteração, um usuário que realiza o evento personalizado às 22h PST em 6 de março de 2026 (que é 1h EST em 7 de março de 2026) agora é incluído no público, pois ele se enquadrou dentro do limite do calendário PST para aquela data.

## Discrepâncias em relatórios

Os fusos horários de espaço de trabalho proporcionam controle preciso sobre o envio de campanhas, mas você deve estar ciente de possíveis discrepâncias em relatórios enquanto esse recurso está em acesso antecipado. Faça referência cruzada dos pontos de dados e esteja atento ao fuso horário ao analisar relatórios de espaços de trabalho com substituições de fuso horário específicas.