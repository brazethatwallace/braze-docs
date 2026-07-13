---
nav_title: Mixpanel
article_title: Importação de coortes do Mixpanel
description: "Este artigo de referência descreve a funcionalidade de importação de coorte do Mixpanel, uma plataforma de análise de dados, permitindo a importação de coortes do Mixpanel para a Braze para criar segmentos da Braze que podem ser usados para direcionamento de usuários em futuras Campaigns ou Canvas da Braze."
page_type: partner
search_tag: Partner
---

# Importação de coorte do Mixpanel {#mixpanel-cohort-import}

> Este artigo descreve como fazer a importação de coortes de usuários do [Mixpanel](https://mixpanel.com/) para a Braze. Para saber mais sobre a integração do Mixpanel e suas outras funcionalidades, consulte o [artigo principal do Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

## Integração de importação de dados {#data-import-integration}

Quando você sincroniza uma coorte do Mixpanel para a Braze, a Braze recebe atualizações de associação à coorte para os usuários que o Mixpanel consegue corresponder a perfis existentes na Braze. Após a sincronização, você pode direcionar esses usuários com o filtro de segmento **Mixpanel cohorts**.

A sincronização de coorte não importa eventos do Mixpanel, propriedades de usuário do Mixpanel nem atributos personalizados para a Braze. O comportamento do conector, incluindo a cadência de sincronização, é controlado no Mixpanel. Para detalhes de configuração, consulte a [documentação de sincronização de coortes da Braze do Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze). Para requisitos de correspondência de usuários, consulte [Correspondência de usuários](#user-matching).

Qualquer integração configurada registrará pontos de dados. Se você tiver alguma dúvida sobre as nuances dos pontos de dados da Braze, seu gerente de conta da Braze poderá respondê-la.

{% alert important %}
Em conformidade com as políticas de retenção de dados do Mixpanel, os eventos enviados antes de 1º de janeiro de 2010 serão removidos durante a importação.
{% endalert %}

### Etapa 1: Obter a chave de importação de dados da Braze {#step-1-get-the-braze-data-import-key}

Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Mixpanel**. Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze.

Após a geração, você pode criar outra chave ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard do Mixpanel.<br><br>![Página da parceira de tecnologia Mixpanel na Braze mostrando a chave de importação de dados e o endpoint.]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Etapa 2: Configurar a integração da Braze no Mixpanel {#step-2-set-up-the-braze-integration-in-mixpanel}

1. No Mixpanel, acesse **Data Management > Integrations.**
2. Selecione a guia de integração da Braze e selecione **Connect**.
3. No prompt exibido, forneça a chave de importação de dados e o endpoint REST da Braze.
4. Selecione **Continue**.

![Modal de configuração da integração Braze no Mixpanel com campos de chave e endpoint.]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Etapa 3: Exportar uma coorte do Mixpanel para a Braze {#step-3-export-a-mixpanel-cohort-to-braze}

No Mixpanel, acesse **Data Management > Cohorts**. Selecione a coorte a ser enviada para a Braze e depois selecione **Export to Braze**. Por fim, selecione uma sincronização única ou uma sincronização dinâmica. A seleção da sincronização dinâmica mantém a coorte atualizada em uma programação recorrente controlada pelo Mixpanel. Para saber a cadência de sincronização mais recente, consulte a [documentação de sincronização de coortes da Braze do Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).

![Fluxo de exportação de coorte do Mixpanel mostrando as opções de sincronização para exportar para a Braze.]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Somente os usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

### Etapa 4: Segmentar usuários na Braze {#step-4-segment-users-in-braze}

Na Braze, para criar um segmento desses usuários, acesse **Público** > **Segments**, nomeie seu segmento e selecione **Mixpanel_Cohorts** como o filtro. Em seguida, use a opção "includes" e escolha a coorte que você criou no Mixpanel.

![No criador de segmentos da Braze, o filtro de atributos do usuário "Mixpanel cohorts" é definido como "includes" e "Braze cohort".]({% image_buster /assets/img_archive/mixpanel1.png %})

Depois de salvar, você pode fazer referência a esse segmento durante a criação de Canvas ou Campaign na etapa de direcionamento de usuários.

## Correspondência de usuários {#user-matching}

Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.

## Solução de problemas {#troubleshooting}

Se uma sincronização de coorte do Mixpanel parecer incompleta ou não atualizar para determinados usuários, consulte [Solução de problemas]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel#troubleshooting) no artigo principal do Mixpanel.

Para etapas específicas do conector e cadência de sincronização, consulte a [documentação de sincronização de coortes da Braze do Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).