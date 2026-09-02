---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Este artigo de referência descreve a parceria entre a Braze e a Amperity, uma plataforma abrangente de dados do cliente, que permite sincronizar os usuários da Amperity, unificar dados, enviar dados para a Braze usando buckets S3 da AWS e muito mais."
page_type: partner
search_tag: Partner

---

# Amperity

> A [Amperity](https://amperity.com/) é uma plataforma abrangente de dados do cliente, que ajuda as marcas a conhecerem seus clientes, a tomarem decisões estratégicas e a adotarem consistentemente o curso de ação correto para atender melhor seus consumidores. A Amperity fornece recursos inteligentes para a unificação do gerenciamento de dados, análise de dados, insights e ativação.

_Essa integração é mantida pela Amperity._

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

A integração da Braze e da Amperity oferece uma visão unificada de seus clientes nas duas plataformas. Essa integração permite que você:
- **Sincronize perfis de clientes**: Mapeie os dados de usuários e os atributos personalizados da Amperity para a Braze.
- **Crie e envie públicos**: Crie segmentos que retornem listas de clientes ativos e seus atributos personalizados associados para a Braze, e envie-os para a Braze.
- **Gerencie atualizações de dados**: Controle a frequência de envio de atualizações de atributos personalizados para a Braze.
- **Unifique dados**: Unifique os dados em várias plataformas suportadas pela Amperity e pela Braze.
- **Sincronize os dados da Braze com o Amazon S3**: Use o Braze Currents para integrar os dados de engajamento das Campaigns da Braze, permitindo que você sincronize os dados com o Amazon S3 no formato Apache Avro.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Amperity | É necessário ter uma [conta Amperity](https://amperity.com/request-a-demo) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br> Ela pode ser criada no dashboard da Braze em **Console de desenvolvedor** > **Chave da API REST** > **Criar nova chave de API**. |
| Instância da Braze | Sua instância da Braze pode ser obtida com seu gerente de integração da Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics#endpoints). |
| Endpoint REST da Braze | A URL do seu endpoint da Braze. Seu endpoint dependerá da sua instância da Braze. |
| Conector Currents (opcional) | O conector S3 Currents. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Mapeamento de dados {#data-mapping}

Atributos padrão e personalizados podem ser enviados da Amperity para a Braze, permitindo que você enriqueça os perfis de clientes na Braze com dados de várias fontes por meio da Amperity. Os atributos específicos que podem ser enviados dependerão dos dados em seu sistema Amperity e dos atributos que você configurou na Braze.

Leia esta seção para saber mais sobre esses atributos.

### Atributos padrão {#standard-attributes}

[Os atributos de perfil]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) descrevem quem são seus clientes. Eles geralmente são associados à identidade do cliente, como:
- Nomes
- Datas de nascimento
- Endereços de e-mail
- Números de telefone

### Atributos personalizados {#custom-attributes}

[Os atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) na Braze são campos determinados por sua marca. Se quiser que a Amperity gerencie atributos personalizados que já existem na Braze, alinhe a saída enviada pela Amperity com os nomes que já estão em seu espaço de trabalho da Braze. Isso pode incluir o seguinte:
- Históricos de compras
- Status de fidelidade
- Níveis de valor
- Dados recentes de engajamento

Verifique os nomes dos atributos personalizados que serão enviados para a Braze pela Amperity. A Amperity adicionará um atributo personalizado sempre que não houver um nome correspondente.

Os atributos personalizados serão atualizados somente para os usuários que tiverem um `external_id` ou `braze_id` correspondente na Braze.

### Públicos da Amperity {#amperity-audiences}

Os públicos sincronizados da Amperity para a Braze serão registrados nos perfis de usuário como atributos personalizados. Eles podem ser usados para direcionar esses usuários na Braze.

![Lista suspensa de filtros com atributos personalizados exibidos na categoria de dados personalizados.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![Lista suspensa de atributos personalizados, como "l12m_frequency" e "l12m_monetary".]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### Tipos de dados {#data-types}

Os tipos de dados compatíveis incluem:
- Booleano
- Date
- Datetime
- Decimal
- Float
- Inteiro
- String
- Varchar

O tipo de dados usado depende da natureza do atributo. Por exemplo, um endereço de e-mail seria uma string, enquanto a idade de um cliente poderia ser um número inteiro.

### Duplicação de atributos {#duplication-of-attributes}

Evite enviar atributos personalizados que dupliquem os campos padrão do perfil do usuário. Por exemplo, as datas de nascimento devem ser enviadas para a Braze como um campo de perfil de usuário chamado "dob" para corresponder ao atributo padrão da Braze. Se forem enviados como "birthday", "Birthdate" ou qualquer outra string, será criado um atributo personalizado e os valores no campo "dob" não serão atualizados.

### Pontos de dados {#data-points}

A Amperity mantém o controle do que muda entre as sincronizações com a Braze e o status dos envios em geral. A Amperity enviará para a Braze apenas a associação à lista e outros atributos escolhidos que foram alterados desde a última sincronização.

## Integração {#integration}

### Etapa 1: Capturar detalhes de configuração para a Braze {#step-1-capture-configuration-details-for-braze}

1. Crie uma chave da API REST da Braze para seu espaço de trabalho da Braze com as permissões `users.track` em **Dados do usuário**. O endpoint `users.track` sincroniza o público da Amperity com a Braze como um atributo personalizado.
2. Determine o [endpoint da API REST]({{site.baseurl}}/api/basics#endpoints) para sua instância da Braze. Por exemplo, se a URL da Braze for `https://dashboard-03.braze.com`, o endpoint da API REST será `https://rest.iad-03.braze.com`, e sua instância será "US-03".
3. Determine uma lista de [campos de perfil de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) e [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) que podem ser enviados para a Braze pela Amperity.

### Etapa 2: Configure a Braze como destino — operador de DataGrid {#step-2-set-up-braze-as-a-destinationdatagrid-operator}

#### Etapa 2a: Criar a tabela de perfis de clientes {#step-2a-build-the-customer-profiles-table}

Crie uma nova tabela chamada "Braze Customer Attributes" no seu banco de dados Customer 360 na Amperity. Essa tabela deve conter todos os atributos da Braze que sua marca deseja gerenciar na Amperity, incluindo os campos de perfil de usuário padrão exigidos pela Braze e quaisquer atributos personalizados. Use SQL para definir a estrutura dessa tabela, conforme mostrado na [documentação da Amperity](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table).

#### Etapa 2b: Nomear, validar e salvar a tabela {#step-2b-name-validate-and-save-the-table}

Nomeie a tabela como "Braze Customer Attributes" e salve-a. Verifique se a tabela está acessível ao **Segment Editor** e ao editor **Edit Attributes** nas campanhas.

#### Etapa 2c: Adicionar a Braze como destino {#step-2c-add-braze-as-a-destination}

Na plataforma da Amperity, navegue até a guia **Destinations**. Procure a opção de adicionar um novo destino. Entre as opções disponíveis, selecione **Braze**.

![A seção de novo destino com o nome "Braze API", a descrição "Send audience attributes to Braze." e o plug-in "Braze".]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### Etapa 2d: Configurar os detalhes do destino {#step-2d-configure-destination-details}

Em **Braze settings**, forneça as credenciais da Braze e as configurações do destino, conforme mostrado na [documentação da Amperity](https://docs.amperity.com/datagrid/destination_braze.html#add-destination). Insira os detalhes de configuração coletados na etapa anterior e defina o identificador da Braze. Os identificadores disponíveis para correspondência são:
- `braze_id`: Um identificador da Braze atribuído automaticamente, que é imutável e associado a um determinado usuário quando ele é criado na Braze.
- `external_id`: Um identificador atribuído pelo cliente, normalmente um UUID.

![A seção Braze Settings com uma instância de "US-03", identificador de usuário de "external_id", nome do segmento em branco, bucket S3 de "amperity-training-abc123" e pasta S3 de "braze-attributes".]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### Etapa 2e: Adicionar um modelo de dados {#step-2e-add-a-data-template}

Na guia **Destinations**, abra o menu do destino Braze e selecione **Add data template**. Digite um nome e uma descrição para o modelo (por exemplo, "Braze" e "Send custom attributes to Braze"), verifique o acesso do usuário corporativo e confira todas as definições de configuração.

Se as configurações necessárias não tiverem sido definidas como parte do destino, configure-as como parte do modelo de dados. Salve o modelo de dados.

![A seção de nome do modelo de dados com o nome "Braze Audience Attributes" e a descrição "Send audience attributes to Braze."]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### Etapa 2f: Salvar a configuração {#step-2f-save-the-configuration}

Depois de preencher os detalhes necessários, salve a configuração. Agora que a Braze está configurada como destino, os usuários do Amp360 e do AmpIQ podem sincronizar os dados com a Braze.

### Etapa 3: Sincronizar dados com a Braze {#step-3-sync-data-to-braze}

Confira se a Braze está ativada para seu locatário da Amperity. Se não estiver, fale com o operador de DataGrid ou com o representante da Amperity para obter assistência.

Em seguida, siga as instruções de sincronização do Amp360 ou do AmpIQ, conforme aplicável à sua empresa.

#### Opção de sincronização 1: Enviar resultados da consulta para a Braze via Amp360 {#syncing-option-1-send-query-results-to-braze-via-amp360}

Os usuários do Amp360 podem usar SQL para escrever consultas de forma livre e, em seguida, configurar uma programação que envia os resultados para a Braze.

##### Etapa 1: Criar uma consulta na Amperity {#step-1-create-a-query-in-amperity}

Navegue até a função de consulta na Amperity e construa uma consulta SQL que produzirá o conjunto desejado de dados de clientes. Os resultados devem incluir os atributos específicos que você deseja enviar para a Braze. Veja este exemplo de consulta da Amperity para retornar uma lista de usuários com seus históricos de compras.

##### Etapa 2: Adicionar uma nova orquestração na Amperity {#step-2-add-a-new-orchestration-in-amperity}

1. Acesse a seção **Orchestration** e clique na opção para adicionar uma nova orquestração.
2. Especifique o que a orquestração deve fazer. Isso geralmente envolve a especificação da consulta SQL que deve ser executada e para onde os resultados devem ser enviados. Nesse caso, selecione a consulta SQL que você criou para gerar a lista de clientes ativos e especifique a Braze como o destino dos resultados.
3. Defina quando e com que frequência a orquestração deve ser executada. Por exemplo, você pode executar a orquestração diariamente em um horário específico.
4. Salve a orquestração depois de configurá-la de acordo com suas preferências. Ela será adicionada à sua lista de orquestrações na Amperity.
5. Teste a orquestração para garantir que ela funcione conforme o esperado. Você pode fazer isso disparando manualmente a orquestração e verificando os resultados na Braze.

##### Etapa 3: Executar a orquestração {#step-3-run-the-orchestration}

Execute a orquestração para executar a consulta e enviar os resultados para a Braze. Isso pode ser feito manualmente ou de acordo com a programação que você definiu nas configurações de orquestração.

#### Opção de sincronização 2: Enviar públicos para a Braze via AmpIQ {#syncing-option-2-send-audiences-to-braze-via-ampiq}

Os usuários do AmpIQ podem criar segmentos na Amperity por meio de uma interface não SQL e sincronizá-los com destinos downstream, como a Braze. Os usuários podem selecionar destinos e, em seguida, configurar uma lista de atributos a serem enviados para cada destino.

##### Etapa 1: Criar um Segment na Amperity {#step-1-create-a-segment-in-amperity}

Crie um Segment na Amperity que retorne uma lista de clientes. Esse Segment deve estar associado aos atributos personalizados que você deseja atualizar na Braze.

{% alert note %}
Consulte a documentação da Amperity para obter exemplos de diferentes tipos de segmentos que você pode querer enviar para a Braze.
{% endalert %}

##### Etapa 2: Criar uma campanha na Amperity {#step-2-build-a-campaign-in-amperity}

1. Acesse a seção **Campaign** e clique na opção para criar uma nova campanha.
2. Dê à sua campanha um nome descritivo e exclusivo que o ajudará a identificá-la posteriormente, especialmente se você tiver várias campanhas.
3. Selecione o segmento de clientes que você deseja direcionar com essa campanha. Esse deve ser o segmento que você criou anteriormente. <br>![O campo suspenso para segmentos a serem excluídos do direcionamento.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. Escolha os dados que você deseja enviar como parte da campanha. Isso pode incluir uma série de atributos do cliente. ![O modal Editar atributos da campanha permite selecionar um destino e atributos do cliente.]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. Selecione **Braze** como o destino para o qual os dados da campanha serão enviados.
6. Escolha quando e com que frequência você deseja que a campanha seja executada. Isso pode ser um evento avulso ou um agendamento recorrente.
7. Salve sua campanha e execute um teste para garantir que ela funcione conforme o esperado.

##### Etapa 3: Executar a campanha {#step-3-run-the-campaign}

Execute a campanha para enviar o Segment para a Braze. Isso pode ser feito manualmente ou com base na programação que você definiu nas configurações da campanha.


### Como usar a Amperity com o Braze Currents {#using-amperity-with-braze-currents}
Para enviar dados do Braze Currents para a Amperity:
1. [Configure um Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents) para enviar dados para um bucket S3 da Amazon.
2. Configure a Amperity para [ler os arquivos do Apache Avro a partir desse bucket S3 da Amazon](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Configure feeds e automatize cargas de dados usando fluxos de trabalho padrão.