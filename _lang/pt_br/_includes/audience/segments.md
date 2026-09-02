{% if include.section == "Differing audience size" %}

O tamanho do público-alvo exibido em uma Campaign ou Canvas pode ser diferente do [tamanho do público alcançável para um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation), mesmo que você esteja adicionando diretamente esse segmento à sua Campaign ou Canvas sem filtros adicionais.
Isso pode ocorrer por vários motivos:

- Quando um grupo de controle global se aplica a uma Campaign ou Canvas, os usuários desse grupo de controle global são excluídos da contagem de usuários contatáveis.
- O tamanho do público-alvo de uma Campaign ou Canvas exclui os usuários que não podem ser contatados por meio de vários canais de mensagens; o comportamento difere de canal para canal. Por exemplo, o público alcançável de uma Campaign ou Canvas exclui os usuários que cancelaram a inscrição, foram marcados como SPAM (para e-mails) ou sofreram hard bounce (para e-mails). O segmento em si, no entanto, exclui apenas os cancelamentos de inscrição ao mostrar o número estimado de usuários alcançáveis por e-mail.
- A Braze só envia mensagens SMS para usuários dentro do grupo de inscrições selecionado, portanto, o público-alvo de SMS para uma Campaign ou Canvas também excluirá todos os usuários que não fizerem parte do grupo de inscrições selecionado.

{% endif %}

{% if include.section == "Refresh settings" %}

Se não precisar que sua extensão seja atualizada regularmente, você pode salvá-la sem usar as configurações de atualização, e a Braze gerará sua extensão de segmento com base na associação do usuário naquele momento. Use o comportamento padrão se quiser gerar o público apenas uma vez e depois direcioná-lo com uma Campaign única.

Seu segmento sempre começará a ser processado após o salvamento inicial. Sempre que seu segmento for atualizado, a Braze executará novamente o segmento e atualizará a associação do segmento para refletir os usuários em seu segmento no momento da atualização. Isso pode ajudar suas Campaigns recorrentes a alcançar os usuários mais relevantes.

#### Configuração de uma atualização recorrente {#setting-up-a-recurring-refresh}

Para definir uma programação recorrente designando configurações de atualização, selecione **Ativar atualização**. A opção de designar configurações de atualização está disponível para todos os tipos de extensões de segmento, incluindo segmentos SQL, extensões de segmento CDI e extensões de segmento simples baseadas em formulário.

{% alert important %}
Para otimizar seu gerenciamento de dados, as configurações de atualização são automaticamente desativadas para extensões de segmento não utilizadas. As extensões de segmento são consideradas não utilizadas quando:

- Não são usadas em nenhuma Campaign, Canvas ou segmento ativo ou inativo (rascunho, interrompido, arquivado); ou
- Não foram modificadas há mais de 7 dias

A Braze notificará o contato da empresa e o criador da extensão se essa configuração for desativada. A opção de regenerar extensões diariamente pode ser ativada novamente a qualquer momento.
{% endalert %}

#### Seleção das configurações de atualização {#selecting-your-refresh-settings}

![Configurações de intervalo de atualização com uma frequência de atualização semanal, horário de início às 10h e segunda-feira selecionada como dia.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

No painel **Configurações de intervalo de atualização**, você pode selecionar a frequência de atualização dessa extensão de segmento: por hora, diariamente, semanalmente ou mensalmente. Também será necessário selecionar o horário específico (no fuso horário da sua empresa) em que a atualização ocorrerá, como por exemplo:

- Se você tiver uma Campaign de e-mail que é enviada todas as segundas-feiras às 11h, horário da empresa, e quiser garantir que seu segmento seja atualizado logo antes do envio, escolha uma programação de atualização semanal às 10h das segundas-feiras.
- Se quiser que seu segmento seja atualizado todos os dias, selecione a frequência de atualização diária e, em seguida, escolha a hora do dia para atualizar.

{% alert note %}
A capacidade de definir uma programação de atualização por hora não está disponível para extensões de segmento baseadas em formulário (mas você pode definir programações diárias, semanais ou mensais).
{% endalert %}

#### Consumo de crédito e custos adicionais {#credit-consumption-and-additional-costs}

Como as atualizações executam novamente a consulta do seu segmento, cada atualização para segmentos SQL consumirá créditos de segmento SQL, e cada atualização para extensões de segmento CDI incorrerá em um custo no seu data warehouse de terceiros.

{% alert note %}
Os segmentos podem levar até 60 minutos para serem atualizados devido ao tempo de processamento dos dados. Os segmentos que estão em processo de atualização terão o status "Processing" na lista de extensões de segmento. Isso tem algumas implicações:

- Para concluir o processamento do seu segmento antes de um horário específico, escolha um horário de atualização que seja 60 minutos antes.
- Somente uma atualização pode ocorrer de cada vez para uma extensão de segmento específica. Se houver um conflito em que uma nova atualização seja iniciada quando uma atualização existente já tiver começado a ser processada, a Braze cancelará a nova solicitação de atualização e continuará o processamento em andamento.
{% endalert %}

#### Critérios para desativar automaticamente extensões obsoletas {#criteria-to-automatically-disable-stale-extensions}

As atualizações programadas são automaticamente desativadas quando uma extensão de segmento se torna obsoleta. Uma extensão de segmento é considerada obsoleta se atender aos seguintes critérios:

- Não é usada em nenhuma Campaign ou Canvas ativo
- Não é usada em nenhum segmento que esteja em uma Campaign ou Canvas ativo
- Não é usada em nenhum segmento que tenha o [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) ativado
- Não foi modificada há mais de sete dias
- Não foi adicionada a uma Campaign ou Canvas (incluindo rascunhos) ou segmento há mais de sete dias

Se a atualização programada for desativada para uma extensão de segmento, essa extensão terá uma notificação informando isso.

![Uma notificação informando que "As atualizações programadas foram desativadas para essa extensão porque ela não é usada em nenhuma Campaign, Canvas ou segmento ativo. A extensão de segmento foi desativada em 23 de fevereiro de 2025 às 12:00 AM."]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

Quando estiver pronto para usar uma extensão de segmento obsoleta, revise as configurações de atualização, selecione a programação de atualização que corresponda ao seu caso de uso e salve as modificações.

{% endif %}

{% if include.section == "same channel identifier" %}

Quando uma mensagem é recebida, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal que o perfil que registrou a interação (por exemplo, o mesmo endereço de e-mail para e-mail, ou o mesmo número de telefone para SMS ou WhatsApp). Usuários que compartilham um identificador com alguém que recebeu, abriu ou clicou na mensagem podem corresponder a esse filtro mesmo que não estivessem originalmente na Campaign ou não tenham recebido a mensagem diretamente.

{% endif %}

{% if include.section == "Canvas variant archived segment" %}

### Não é possível excluir uma variante de Canvas por causa de um segmento arquivado {#cant-delete-a-canvas-variant-because-of-an-archived-segment}

Se a Braze bloquear a exclusão de uma variante de Canvas porque um filtro de segmento ainda faz referência a essa variante, abra o segmento que usa a referência — incluindo segmentos arquivados — e remova a variante dos filtros. Depois de salvar o segmento, volte ao Canvas e tente excluir a variante novamente.

Para descobrir quais segmentos fazem referência a um Canvas, abra o Canvas e revise os filtros de público, ou verifique a seção [Uso em envio de mensagens]({{site.baseurl}}/user_guide/audience/segments/managing_segments#messaging-use) de cada segmento para identificar Canvas vinculados.

{% endif %}