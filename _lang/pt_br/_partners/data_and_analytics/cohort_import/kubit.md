---
nav_title: Kubit
article_title: Importação de coorte do Kubit
description: "Este artigo de referência descreve a funcionalidade de importação de coortes do Kubit, uma plataforma de análise de dados sem código e de autoatendimento que oferece insights instantâneos sobre o produto, permitindo a importação de coortes de usuários do Kubit e seu direcionamento no envio de mensagens da Braze."
page_type: partner
search_tag: Partner
---

# Importação de coorte do Kubit {#kubit-cohort-import}

> Este artigo descreve como importar coortes de usuários do [Kubit](https://kubit.ai/) para a Braze. Para saber mais sobre a integração do Kubit e suas outras funcionalidades, consulte o [artigo principal do Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit).

## Integração de importação de dados {#data-import-integration}

### Etapa 1: Obter a chave de importação de dados da Braze {#step-1-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Kubit**. Aqui você encontra o endpoint REST or transferir estado representacional e gera sua chave de importação de dados da Braze.

Após a geração, você pode criar outra chave ou invalidar uma existente. A chave de importação de dados e o endpoint REST or transferir estado representacional são usados na próxima etapa ao configurar um postback no dashboard do Kubit.

![A página da parceira de tecnologia Kubit na Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Etapa 2: Configurar a Braze no Kubit {#step-2-configure-braze-in-kubit}

Forneça a chave de importação de dados da Braze e o endpoint REST or transferir estado representacional da Braze ao seu contato de suporte do Kubit. Eles configurarão a integração do lado deles e informarão quando a integração estiver ativa.

### Etapa 3: Importar coortes para a Braze {#step-3-import-cohorts-to-braze}

#### Criar uma coorte no Kubit {#create-a-cohort-in-kubit}
[Crie uma coorte](https://www.kubit.ai/doc/fundamentals#cohort) no Kubit e defina os critérios dos seus usuários-alvo.<br><br>![Criador de coortes do Kubit com critérios de usuários-alvo configurados.]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Importar usuários para a Braze {#import-users-to-braze}
Depois de salvar sua coorte, você pode importá-la para a Braze para ser usada em segmentos da Braze. Esses segmentos podem então ser usados para criar campanhas de e-mail ou push e Canvas direcionados.

Para fazer isso, navegue até a coorte existente e, em **Cohort Control**, selecione **Import to Braze**.

![Menu Cohort Control do Kubit com a opção Import to Braze selecionada.]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Em seguida, selecione a cadência de importação desejada. As importações únicas permitem que você importe uma vez agora. As importações agendadas permitem que você importe diariamente, semanalmente ou mensalmente em um horário específico. Note que cada coorte só pode ter um cronograma de importação ativo.

![Configurações de cronograma de importação do Kubit com opções de cadência para importações para a Braze.]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Somente os usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

#### Verificar o status da importação {#verify-import-status}
Após a conclusão de uma importação, uma notificação por e-mail será enviada aos destinatários especificados no cronograma de importação. Você também pode verificar o status de importação de uma coorte em **Schedule** no Kubit. O histórico do cronograma exibirá o horário de execução de cada importação, o resultado e o número total de usuários na coorte que foram importados para a Braze.<br><br>![Histórico de cronograma do Kubit mostrando horários de execução, resultados e contagens de usuários importados.]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Você pode disparar manualmente uma importação clicando no ícone **Import to Braze** para esse cronograma de importação.

### Etapa 4: Criar segmentos da Braze com coortes do Kubit {#step-4-create-braze-segments-with-kubit-cohorts}
Depois de importar coortes para a Braze, você pode usá-las como filtros para criar segmentos da Braze e incluí-las em campanhas ou Canvas da Braze. Visite nossa documentação de segmentos para saber mais sobre [como criar segmentos da Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#step-4-add-filters-to-your-segment).

![No criador de segmentos da Braze, o atributo do usuário "Kubit cohorts" está definido como "includes_value" e mostra uma lista de coortes disponíveis.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Correspondência de usuários {#user-matching}

Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.