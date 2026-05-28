---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Este artigo de referência descreve a parceria entre a Braze e a Optimizely, que permite sincronizar seus segmentos de clientes, eventos e eventos do Currents da Braze com a Optimizely Data Platform."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> A [Optimizely](https://www.optimizely.com/) é uma plataforma líder em experiência digital que oferece ferramentas de experimentação e gerenciamento de conteúdo para produtos digitais e campanhas de marketing.

A integração entre a Braze e a Optimizely é uma integração bidirecional que permite a você:

- Sincronizar seus segmentos e eventos de clientes da Braze com a Optimizely Data Platform (ODP) todas as noites para enriquecer os perfis, os relatórios e a segmentação de clientes da Optimizely.
- Enviar eventos do Braze Currents da Braze para a ferramenta de relatórios da Optimizely.
- Sincronizar dados e eventos de clientes do ODP com a Braze para enriquecer seus dados de clientes da Braze e disparar envios de mensagens da Braze com base em eventos de clientes no ODP.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|----------------------------------|-------------|
| Conta da Optimizely Data Platform | É necessário ter uma conta na Optimizely Data Platform (ODP) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as seguintes permissões: `users.track`, `users.export.segments`, `segments.list`, `campaigns.trigger.send` e `canvas.trigger.send`. |
| Currents | Para exportar dados de volta para a Optimizely, você precisa ter o Braze Currents configurado para sua conta. |
| URL e token da Optimizely | Isso pode ser obtido acessando seu dashboard da Optimizely e copiando a URL de ingestão e o token. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Configurar a integração {#step-1-configure-the-integration}

1. No **App Directory** da Optimizely Data Platform (ODP), selecione o app **Braze** e, em seguida, selecione **Install App**.
2. Acesse a guia **Settings**. Na seção **Authorization**, faça o seguinte:
    1. Insira a **REST API Key** da Braze.
    2. Selecione a **Instance URL** da Braze.
    2. Selecione **Verify API Key**.
3. Na Braze, acesse **[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/)**.
4. Selecione **Create New Current** > **Custom Currents Export**.
5. Configure o Current usando o endpoint e o token fornecidos no ODP. Isso é necessário para sincronizar os eventos da Braze com o ODP.

![Autorização da Optimizely.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. No ODP, expanda a seção **Segments** e selecione segmentos específicos na lista **Segments to Sync**, ou selecione **Import All Customers** para sincronizar todos os segmentos.
7. Adicione quaisquer [mapeamentos de campo adicionais](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) que desejar entre a Braze e o ODP.
8. Selecione **Save**.

![Sincronização de Segment entre Optimizely e Braze.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Você deve selecionar segmentos para importar perfis de clientes da Braze. Se você não selecionar nenhum segmento, a integração não importará nenhum perfil de cliente.
{% endalert %}

### Etapa 2: Mapear campos de dados {#step-2-map-data-fields}

A integração possui mapeamentos de campo de dados padrão entre a Braze e o ODP. Por exemplo, o campo **Email** na Braze é mapeado para o campo **Last Seen Email** no ODP.

![Campos de mapeamento de Segment entre Optimizely e Braze.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Mapear campos adicionais (opcional) {#map-additional-fields-optional}

Se houver campos de dados adicionais na Braze que você deseja mapear para o ODP, faça o seguinte no ODP:

1. Na seção **Segments** do app, selecione o campo da Braze na lista suspensa **Braze User Data Fields**.
2. Selecione o campo do ODP na lista suspensa **ODP Customer Fields**.
3. Selecione **Save Field Map**.

![Salvar mapas de campo de Segment entre Optimizely e Braze]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Excluir mapeamentos de campo não necessários (opcional) {#delete-non-required-field-mappings-optional}

Você também pode excluir qualquer mapeamento de campo de dados que não seja necessário. Faça o seguinte no ODP:

1. Na seção **Segments** do app, selecione o mapeamento de campo que deseja excluir na lista suspensa **Field Map**.
2. Selecione **Delete Field Map**.

![Excluir mapas de campo de Segment entre Optimizely e Braze]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### Etapa 3: Sincronizar dados da Optimizely Data Platform (ODP) com a Braze {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

Depois de configurar a integração, você pode definir uma ativação no ODP para sincronizar os dados de seus clientes do ODP com a Braze.

1. Acesse **Activation** > **Engage** e selecione **Create New Campaign**.
2. Selecione **Behavioral** para configurar uma sincronização automatizada e recorrente.
3. Selecione **Create From Scratch** e insira um nome para a ativação que represente os dados que você está sincronizando com a Braze (como **Braze Data Sync**).
4. Na seção **Enrollment**, é possível sincronizar dados de clientes que correspondem a um segmento ou sincronizar dados de clientes que disparam um evento (como quando o ODP registra que um cliente abre um e-mail):
   - **Clientes que correspondem a um segmento:** Selecione o segmento desejado e, em seguida, selecione **Next**.<br><br>![Seleção de Segment na Optimizely]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Clientes que disparam um evento:** Expanda a lista suspensa **Filter** e selecione o evento do ODP a ser usado como gatilho para essa sincronização de dados com a Braze. Em seguida, expanda **Automation Rules** e ajuste conforme desejado. <br><br>![Evento de gatilho da Optimizely]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Expanda **Touchpoints**, selecione para editar **Touchpoint 1** e, em seguida, selecione **Braze**.
6. Expanda a seção **Targeting** e selecione o **Target Identifier**.
7. Selecione uma das seguintes opções para **Add Users To** na seção **Configure**:
    - **Campaign:** Adicionar clientes a uma Campaign específica na Braze. Depois de escolher essa opção, você deve selecionar a Campaign da Braze.
    - **Canvas:** Adicionar clientes a um Canvas específico na Braze. Depois de escolher essa opção, você deve selecionar o Canvas da Braze.
    - **Profile Update Only:** Atualizar apenas o perfil do cliente na Braze.
8. (Opcional) Selecione o **Number of Additional Fields** que você deseja sincronizar com a Braze (até 20).
    Em seguida, selecione o seguinte para a lista suspensa e o campo de entrada de cada campo adicional:
    - Em cada lista suspensa **Field #**, selecione o campo da Braze que deseja preencher.
    - Em cada **Field # Value** correspondente, insira o campo do ODP que deseja enviar para o campo da Braze selecionado. Por exemplo, se você selecionou **Company Name** na lista suspensa **Field #**, insira `{{customer.company_name}}` para o **Field # Value** correspondente.
9. Selecione **Save** e, em seguida, selecione o nome da ativação na trilha de navegação.
10. Selecione **Select start time and schedule** na seção **Touchpoints** se tiver selecionado **Customers that match a segment** para a inscrição.
11. Preencha as seguintes configurações:
    - **Recurring or Continuous:** Selecione **Recurring**.
    - **Start Date:** Insira a data em que você deseja enviar os dados para a Braze.
    - **End:** O padrão é **Never**. Se quiser encerrar a sincronização de dados da Braze em uma data específica, defina isso aqui.
    - **Repeats:** Defina como **Daily**.
    - **Repeat Every:** Defina como **1 day**.
    - **Timing:** Insira a hora em que deseja enviar os dados para a Braze.
    - **Time Zone:** Selecione o fuso horário no qual você deseja enviar esses dados.
12. Selecione **Apply**, **Save** e **Go Live**. Sua sincronização começa na data e hora de início designadas (ou quando ocorre o evento de gatilho).

## Solução de problemas {#troubleshooting}

### Inspecionar eventos {#inspect-events}

Para verificar se os dados estão sendo sincronizados corretamente do ODP para a Braze, você pode inspecionar os eventos no ODP.

1. No ODP, acesse **Account Settings** > **Event Inspector**.
2. Selecione **Start Inspector**.
3. Quando os dados estão disponíveis no inspetor, um número é exibido ao lado de **Refresh**. Selecione para visualizar os dados.
4. Os dados brutos que o ODP e a Braze enviam entre si são exibidos. Selecione **View Details** para ver a versão formatada desses dados brutos.
5. Os campos de dados enviados da Braze de volta ao ODP começam com `_braze`.

### Verificar os registros de atividade {#check-activity-logs}

Cada sincronização de dados também é registrada no [registro de atividades do ODP](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP):

1. Acesse **Account Settings** > **Activity Log**.
2. Filtre as categorias por **braze**.
3. Selecione **View Details** para obter uma exibição formatada dos detalhes do registro, incluindo o número de correspondências.