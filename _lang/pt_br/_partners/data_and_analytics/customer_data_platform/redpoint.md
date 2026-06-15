---
nav_title: Redpoint
article_title: Redpoint
description: "A integração da Redpoint com a Braze permite a integração e o enriquecimento dos perfis de usuários da Braze com seus dados primários."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> A [Redpoint](https://www.redpointglobal.com) é uma plataforma de tecnologia que fornece aos profissionais de marketing uma plataforma de orquestração de campanhas totalmente integrada. Aproveite os recursos de segmentação, programação e automação da Redpoint para controlar como e quando os dados do CDP são importados para a Braze.

_Essa integração é mantida pela Redpoint._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Redpoint permite criar Segments na Braze com base nos dados do Redpoint CDP. A Redpoint fornece dois modos de transmissão de dados para a Braze:

1. Modo **Braze Onboarding and Upsert**: faz "upsert" de um perfil de usuário da Redpoint para a Braze. É usado na integração ou atualização de registros de usuários quando os dados são alterados.
2. Modo **Braze Append**: atualiza um perfil de usuário se esse usuário já existir na Braze.

Você configurará um modelo de exportação e um canal de saída para cada modo.

{% alert note %}
"Upsert" é uma combinação das palavras "update" (atualização) e "insert" (inserção). É usado quando se deseja inserir um novo registro em uma tabela do banco de dados, se ele ainda não existir, ou atualizar o registro, se ele já existir. Essencialmente, o upsert verifica se um determinado registro está presente no banco de dados. Se o registro estiver presente, ele será atualizado e, se não estiver presente, um novo registro será inserido.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Artefatos do Redpoint Data Management | A integração da Braze é suportada por um conjunto de artefatos do Redpoint Data Management. Entre em contato com o [suporte da Redpoint](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) para solicitar os artefatos para a sua versão do Redpoint Data Management. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Atributos personalizados do Redpoint CDP {#redpoint-cdp-custom-attributes}

Os seguintes atributos personalizados da Redpoint podem ser adicionados a um perfil de usuário da Braze.

| Campo               | Descrição                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | O objeto de atributo de perfil do Redpoint CDP                                                                                  |
| `rpi_audience_outputs`| Matriz de tags de saída do público em que o usuário é direcionado em uma execução do canal Redpoint Outbound Delivery Braze         |
| `rpi_offers`         | Matriz de tags de oferta em que o usuário é direcionado em uma execução do canal Redpoint Outbound Delivery Braze                   |
| `rpi_contact_ids`    | Matriz de IDs de contato do histórico de ofertas em que o usuário é direcionado em uma execução do canal Redpoint Outbound Delivery Braze     |
| `rpi_channel_exec_ids`| Matriz de IDs de execução de canal em que o usuário é direcionado em uma execução do canal Redpoint Outbound Delivery Braze       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Integração {#integration}

### Etapa 1: Configurar modelos {#step-1-set-up-templates}

#### Etapa 1a: Criar o modelo de integração e upsert da Braze {#step-1a-create-the-braze-onboarding-and-upsert-template}

No Redpoint Interaction (RPI), crie um novo modelo de exportação e dê a ele o nome **Braze Onboarding and Upsert**. Esse modelo define os mapeamentos principais entre o Redpoint CDP e o perfil de usuário da Braze, juntamente com quaisquer atributos personalizados adicionais que você queira adicionar aos seus perfis de usuário na Braze.

Arraste os atributos do Redpoint CDP para a coluna **Attribute**. Defina cada **Header Row Value** como o [atributo de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) correspondente da Braze.

A tabela a seguir lista os atributos do Redpoint CDP e seus atributos correspondentes na Braze:

| Atributo do Redpoint | Header Row Value |
|--------------------|------------------|
| PID                | `external_id`    |
| First Name          | `first_name`     |
| Last Name          | `last_name`      |
| Primary Email      | `email`          |
| Primary Country    | `country`        |
| DOB                | `dob`            |
| Gender             | `gender`         |
| Primary City       | `home_city`      |
| Primary Phone      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Adicione o atributo **Output Name** da tabela **Offer History**. Por fim, adicione quaisquer atributos personalizados adicionais da Redpoint que você queira mesclar na Braze. Por exemplo, o modelo a seguir faz integração e upsert com educação, renda e estado civil como atributos adicionais.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Etapa 1b: Criar o modelo Braze Append {#step-1b-create-the-braze-append-template}

Crie um segundo modelo de exportação para operações somente de acréscimo, denominado **Braze Append**.

Você definirá apenas dois atributos para esse modelo. Para **PID**, defina o **Header Row Value** como `external_id`. Para **Output Name**, defina o **Header Row** como `output_name`.

![Um modelo de exportação de exemplo com os atributos `external_id` e output name.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Etapa 1c: Definir formato de data {#step-1c-set-date-format}

Para ambos os modelos de exportação, navegue até a guia **Options** e defina o **Date Format** como o valor de **Custom Format**. Defina o formato como **yyyy-MM-dd**.

![A guia de opções mostrando o formato de data definido como yyyy-MM-dd.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Etapa 2: Criar canais de saída {#step-2-create-outbound-channels}

No RPI, crie dois novos canais. Defina ambos os canais como **Outbound Delivery**. Nomeie um canal como **Braze Onboarding and Upsert** e o outro como **Braze Append**.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Após a integração inicial dos registros do CDP na Braze, verifique se os fluxos de trabalho subsequentes do Redpoint Interaction que usam o canal Braze Onboarding and Upsert foram projetados para selecionar apenas os registros alterados desde a sincronização inicial de integração.
{% endalert %}

### Etapa 3: Configurar os canais {#step-3-configure-the-channels}

#### Etapa 3a: Definir o modelo e o formato do caminho de exportação {#step-3a-set-template-and-export-path-format}

Navegue até a guia **General** na tela de **Configuration** dos canais. Defina o modelo de exportação para cada canal respectivo.

Em seguida, defina um **Export path format** em ambos os canais que aponte para uma rede compartilhada, protocolo de transferência de arquivos ou local de provedor de conteúdo externo que seja acessível ao Redpoint Interaction e ao Redpoint Data Management.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

O formato do diretório de exportação em ambos os canais será idêntico e deverá terminar com `\\[Channel]\\[Offer]\\[Workflow ID]`.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Etapa 3b: Configurar a pós-execução {#step-3b-configure-post-execution}

Navegue até a guia **Post Execution** na tela de **Configuration** dos canais.

Marque a caixa de seleção **Post-execution** para chamar uma URL de serviço após a execução do canal. Digite a URL do serviço web do Redpoint Data Management. Essa entrada será idêntica tanto no canal de integração quanto no de acréscimo.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Etapa 4: Configurar os componentes da Braze no Redpoint Data Management {#step-4-set-up-braze-components-in-redpoint-data-management}

O arquivo que contém os artefatos do Redpoint Data Management (RPDM) para suportar a integração da Braze contém um README com instruções detalhadas para configurar os componentes necessários. Tenha em mente os seguintes detalhes ao configurar sua integração.

#### Etapa 4a: Atualizar a automação RPI para Braze com seu endpoint REST da Braze e o diretório de saída RPI base {#step-4a-update-the-rpi-to-braze-automation-with-your-braze-rest-endpoint-and-base-rpi-output-directory}

Depois de importar os artefatos relacionados à Braze para o Redpoint Data Management, abra a automação denominada **AUTO_Process_RPI_to_Braze** e atualize as duas variáveis de automação a seguir com os valores do seu ambiente:

* **BRAZE_API_URL**: o endpoint REST da Braze
* **BASE_OUTPUT_DIRECTORY**: o diretório de saída compartilhado entre o Redpoint Interaction e o Redpoint Data Management

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Etapa 4b: Atualizar o projeto de acréscimo do RPI para Braze {#step-4b-update-the-rpi-to-braze-append-project}

O projeto do Redpoint Data Management chamado **PROJ_RPI_to_Braze_Append** contém o esquema de arquivo de exportação de entrega e os mapeamentos para o objeto de atributo personalizado `rpi_cdp_attributes` na Braze.

Atualize o esquema de entrada de arquivos e a ferramenta de injeção de documentos denominada **RPI to Braze Document Injector** com quaisquer atributos personalizados adicionais de CDP definidos no seu modelo de arquivo de exportação. Este exemplo mostra o mapeamento adicional de educação, renda e estado civil:

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Usando a integração {#using-the-integration}

O canal Outbound Delivery Braze agora pode ser usado nos fluxos de trabalho do Redpoint Interaction. Siga as práticas padrão para criar regras de seleção e públicos no RPI e criar programações e gatilhos de fluxo de trabalho associados.

Para ativar a sincronização de uma saída de público do RPI para a Braze, crie uma oferta de entrega e associe-a ao canal **Braze Onboarding and Upsert** ou **Braze Append**. Isso depende se a intenção é criar ou mesclar novos registros na Braze, ou apenas acrescentar dados de campanha se o registro já existir na Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Após a execução bem-sucedida do fluxo de trabalho no RPI, os dados de orquestração e CDP provenientes do RPI agora podem ser usados para criar Segments na Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Você pode visualizar as propriedades associadas à Redpoint no perfil do usuário.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}