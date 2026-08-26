---
nav_title: Criar um catálogo
article_title: Criar um catálogo
alias: "/catalogs/"
page_order: 1
description: "Este artigo de referência aborda como criar catálogos que fazem referência a dados de não usuários em suas campanhas da Braze por meio do Liquid."
---

# Criar um catálogo {#create-a-catalog}

> A criação de um catálogo envolve a importação de um arquivo CSV de dados de não usuários para a Braze. Isso permite que você acesse essas informações para enriquecer suas mensagens. Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, esses dados são algum tipo de metadados da sua empresa, como informações sobre produtos para uma empresa de comércio eletrônico ou informações sobre cursos para um provedor de educação.

## Casos de uso {#use-cases}

Casos de uso comuns para catálogos incluem:

- Produtos
- Serviços
- Alimentos
- Próximos eventos
- Música
- Pacotes

Depois que essas informações forem importadas, você pode começar a acessá-las em mensagens de forma semelhante a como acessa atributos personalizados ou propriedades de eventos personalizados por meio de Liquid.

## Tipos de dados suportados {#supported-data-types}

A tabela a seguir lista os tipos de dados de catálogo suportados e como eles podem ser criados ou atualizados.

| Tipo de dado | Descrição | Disponível via upload de CSV | Disponível via API e CDI |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| String | Uma sequência de caracteres. | ✅ Sim | ✅ Sim |
| Número | Um valor numérico, inteiro ou decimal. | ✅ Sim | ✅ Sim |
| Booleano | Um valor `true` ou `false`. | ✅ Sim | ✅ Sim |
| Hora | Uma string formatada no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | ✅ Sim | ✅ Sim |
| Geolocalização | Um array de coordenadas `[longitude, latitude]`. A latitude deve estar entre -90 e 90; a longitude deve estar entre -180 e 180. Por exemplo, `[-73.988103, 40.779109]`. | ✅ Sim | ✅ Sim |
| Objeto JSON | Um objeto aninhado com pares chave-valor. Pode ser exibido na plataforma, mas só pode ser criado ou atualizado por meio da API ou CDI. | ⛔ Não | ✅ Sim |
| Array de strings | Uma lista de strings. Pode ser exibido na plataforma, mas só pode ser criado ou atualizado por meio da API ou CDI. Máximo de 100 elementos. | ⛔ Não | ✅ Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Criando um catálogo {#creating-a-catalog}

Para criar um catálogo, acesse **Configurações de dados** > **Catálogos** e selecione **Criar novo catálogo**. Em seguida, escolha uma das seguintes opções:

{% tabs local %}
{% tab Upload CSV %}
### Etapa 1: Revise seu arquivo CSV {#step-1-review-your-csv-file}

Antes de enviar seu arquivo CSV, verifique se ele atende aos seguintes requisitos:

| Requisito do CSV | Detalhes |
|-------------------|----------|
| Cabeçalhos | A primeira coluna no arquivo CSV deve ser nomeada `id`, e cada linha deve ter um valor de `id` único. |
| Colunas | Um arquivo CSV pode ter no máximo 1.000 campos (colunas), e cada nome de coluna pode ter até 250 caracteres. |
| Tamanho do arquivo | Para planos Free, o tamanho total de todos os arquivos CSV em uma empresa é limitado a 500 MB. Para planos Pro, o tamanho máximo de um único arquivo CSV é 2 GB. |
| Valores de campo | Cada célula (valor de campo) pode conter até 5.000 caracteres. |
| Caracteres válidos | A coluna `id` e todos os valores de cabeçalho podem conter apenas letras, números, hífens e underscores. |
| Tipos de dados | Os tipos de dados compatíveis com uploads de CSV incluem string, número, booleano, hora e geolocalização. Para a lista completa de tipos de dados, incluindo aqueles disponíveis apenas por meio da API e CDI, consulte [Tipos de dados compatíveis](#supported-data-types). |
| Formatação | Formate todo o texto em minúsculas para manter a consistência. |
| Codificação | Salve e envie o arquivo CSV usando codificação UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Precisa de mais espaço para seus arquivos CSV? Entre em contato com seu gerente de conta da Braze para saber mais sobre como fazer upgrade dos seus catálogos.
{% endalert %}

### Etapa 2: Faça o upload do CSV {#step-2-upload-csv}

Arraste e solte seu arquivo na zona de upload, ou selecione **Upload CSV** e escolha seu arquivo.

![Arraste e solte seu arquivo na zona de upload, ou selecione Upload CSV e escolha seu arquivo.]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Selecione um tipo de dados para cada coluna.

{% alert note %}
Esse tipo de dados não pode ser editado após a configuração do seu catálogo. Além disso, um valor `NULL` não é compatível com upload de CSV e será tratado como uma string.
{% endalert %}

![Esse tipo de dados não pode ser editado após a configuração do seu catálogo. Além disso, um valor NULL não é compatível com upload de CSV e será tratado como uma string.]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Insira um nome e uma descrição opcional para o seu catálogo. Tenha os seguintes requisitos em mente ao nomear seu catálogo:

  - Deve ser único
  - Máximo de 250 caracteres
  - Pode conter apenas números, letras, hífens e underscores

{% alert tip %}
Você também pode [usar modelos em um nome de catálogo](#template-catalog-names), permitindo gerar dinamicamente nomes de catálogo com base em variáveis como idioma ou Campaign.
{% endalert %}

![Um catálogo chamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Selecione **Process Catalog** para criar o catálogo.

{% alert important %}
Seu arquivo CSV pode ser rejeitado se você exceder o limite do seu [plano](#tiers).
{% endalert %}

### Tutorial: Criando um catálogo a partir de um arquivo CSV {#tutorial-creating-a-catalog-from-a-csv-file}

Para este tutorial, estamos usando um catálogo que lista dois jogos, seus preços e um link de imagem.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Tutorial: Criando um catálogo a partir de um arquivo CSV">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Criaremos o catálogo fazendo upload de um arquivo CSV. Os tipos de dados para `id`, `title`, `price` e `image_link` são string, string, número e string, respectivamente.

{% alert note %}
Esse tipo de dados não pode ser editado após a configuração do seu catálogo.
{% endalert %}

![Quatro nomes de colunas do catálogo: "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Em seguida, nomearemos este catálogo como "games_catalog" e selecionaremos o botão **Process Catalog**. A Braze verificará se há erros no catálogo antes da criação.

![Um catálogo chamado "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Observe que não será possível editar esse nome após a criação do catálogo. Você pode excluir um catálogo e reenviar uma versão atualizada usando o mesmo nome de catálogo.

Após criar o catálogo, você pode começar a fazer referência ao [catálogo em uma campanha]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs).

{% alert important %}
Arquivos CSV enviados anteriormente ficam disponíveis para download na página **Catálogos** por 30 dias após a data de upload. Após 30 dias, o arquivo é excluído permanentemente e não poderá mais ser acessado.
{% endalert %}
{% endtab %}

{% tab Criar no navegador %}
### Pré-requisitos {#prerequisites}

Antes de poder editar ou criar catálogos no navegador, você precisa das seguintes [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para o seu espaço de trabalho:

- View Catalogs
- Edit Catalogs
- Export Catalogs
- Delete Catalogs

### Etapa 1: Insira os detalhes do catálogo {#step-1-enter-catalog-details}

Insira um nome e uma descrição opcional para o seu catálogo. Tenha os seguintes requisitos em mente ao nomear seu catálogo:

- Deve ser único
- Máximo de 250 caracteres
- Pode conter apenas números, letras, hífens e underscores

{% alert tip %}
Você também pode [usar modelos em um nome de catálogo](#template-catalog-names), permitindo gerar dinamicamente nomes de catálogo com base em variáveis como idioma ou Campaign.
{% endalert %}

![Um catálogo chamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Etapa 2: Crie seu catálogo {#step-2-create-your-catalog}

Selecione seu catálogo na lista e, em seguida, selecione **Update Catalog** > **Add fields**. Insira o **Field name** e use o menu suspenso para selecionar o tipo de dados. Repita conforme necessário.

![Dois campos de exemplo: "rating" e "name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Selecione **Update Catalog** > **Add items** para adicionar um item ao seu catálogo, inserindo as informações com base nos campos que você adicionou anteriormente. Em seguida, selecione **Save Item** ou **Save and Add Another** para continuar adicionando seus itens.

![Adicionar um item ao catálogo.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
A Braze processa valores de hora com base no timestamp do dashboard. Por exemplo, se uma coluna tem o valor "03/13/2024" e seu fuso horário é o Fuso Horário do Pacífico, esse horário será importado para a Braze como "Mar 12, 2024, 5:00 PM".
{% endalert %}
{% endtab %}
{% endtabs %}

## Tipos de dados de catálogo {#catalog-data-types}

Os catálogos suportam vários tipos de dados para ajudar você a organizar e estruturar seus dados de forma eficaz. A tabela a seguir descreve cada tipo de dado suportado e como ele é mapeado para os nomes de tipo em CSV e API:

| Tipo de dados | Formato | Exemplo | Descrição |
|-----------|--------|---------|-------------|
| String | Texto | `"Hello World"` | Qualquer sequência de caracteres usada para dados de texto, como nomes, descrições e IDs. Equivalente ao tipo `string` em importações de CSV e API. |
| Time | ISO 8601 ou timestamp Unix (segundos) | `"2024-03-15T14:30:00Z"` | Valores de data e hora formatados como ISO 8601 ou timestamp Unix em segundos. Equivalente ao tipo `time` na API e ao tipo `datetime` em importações de CSV. |
| Boolean | `true` ou `false` | `true` | Valores lógicos representando estados verdadeiro ou falso. Equivalente ao tipo `boolean` em importações de CSV e API. |
| Number | Inteiro ou decimal | `42` ou `19.99` | Valores numéricos incluindo inteiros e números de ponto flutuante para preços, quantidades, avaliações e mais. Equivalente aos tipos `integer` e `float` em importações de CSV e ao tipo `number` na API. |
| Geolocation | Array `[longitude, latitude]` | `[-73.988103, 40.779109]` | Um par de coordenadas representando uma localização geográfica. A longitude deve estar entre -180 e 180; a latitude deve estar entre -90 e 90. O valor de `type` na API é `geo`. Pode ser adicionado pelo drawer **Add Fields** na interface de catálogos, por upload de CSV ou pela REST API. |
| Object | Objeto JSON | `{"key": "value", "price": 10}` | Estruturas de dados aninhadas complexas. O valor de `type` na API é `object`. Exibido como JSON Object no dashboard. Disponível apenas via API ou ingestão de dados na nuvem (CDI). |
| Array | Array de strings | `["red", "blue", "green"]` | Listas de valores de string. O valor de `type` na API é `array`. Exibido como String array no dashboard. Disponível apenas pela API ou CDI. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Usando modelos em nomes de catálogo {#template-catalog-names}

Ao nomear seu catálogo, você também pode usar modelos em um nome de catálogo. Isso permite gerar dinamicamente nomes de catálogo com base em variáveis como idioma ou Campaign. Por exemplo, você pode usar o seguinte:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Gerenciando catálogos {#managing-catalogs}

### No dashboard {#in-the-dashboard}

Para atualizar seu catálogo depois de fazer upload de um CSV ou criar um catálogo no navegador, selecione **Update Catalog > Upload CSV** e, em seguida, selecione se deseja atualizar, adicionar ou excluir itens no seu catálogo.

### Usando a REST API {#using-the-rest-api}

À medida que você cria mais catálogos, também pode usar o [endpoint Listar catálogos]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) para retornar uma lista dos catálogos em um espaço de trabalho.

A REST API oferece suporte a todos os [tipos de dados de catálogo](#supported-data-types), incluindo objetos JSON e arrays de strings. Objetos JSON e arrays de strings só podem ser criados ou atualizados por meio da REST API.

### Usando a ingestão de dados na nuvem {#using-cloud-data-ingestion}

Você pode manter catálogos por meio da [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data), sincronizando dados de catálogo diretamente do seu data warehouse (como Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric ou S3) de forma programada.

## Gerenciando itens do catálogo {#managing-catalog-items}

Além de gerenciar seus catálogos, você também pode usar endpoints assíncronos e síncronos para gerenciar os itens do catálogo. Isso inclui a capacidade de editar e excluir itens do catálogo, além de listar detalhes dos itens do catálogo.

Por exemplo, se você quiser editar um item individual do catálogo, pode usar o [endpoint `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item).

## Armazenamento de catálogo {#tiers}

A versão gratuita dos catálogos suporta tamanhos de arquivo CSV de até 500 MB para todos os arquivos CSV combinados na sua empresa, enquanto a versão Catalogs Pro suporta tamanhos de arquivo CSV de até 2 GB para um único arquivo CSV.

{% alert important %}
O direito ao pacote mostrado no dashboard da Braze é arredondado para a unidade mais próxima para fins visuais; no entanto, você ainda tem direito ao valor total adquirido. Para solicitar um upgrade do armazenamento de catálogos, fale com seu gerente de conta da Braze.
{% endalert %}

### Versão gratuita {#free-version}

O tamanho do armazenamento da versão gratuita dos catálogos é de até 500&nbsp;MB. Você pode ter itens ilimitados desde que estejam abaixo de 500&nbsp;MB.

#### Catalogs Pro {#catalogs-pro}

Em nível de empresa, o armazenamento máximo do Catalogs Pro é baseado no tamanho dos dados do catálogo. As opções de tamanho de armazenamento são: 5&nbsp;GB, 10&nbsp;GB ou 15&nbsp;GB. Observe que o armazenamento da versão gratuita (500&nbsp;MB) está incluído em cada um desses planos.

## Especificações {#specifications}

A tabela a seguir resume as especificações sobre o que você pode incluir em catálogos.

| Área | Especificações |
|------|-----------|
| Caracteres por valor de item | Até 5.000 caracteres em um único valor. Por exemplo, se você tiver um campo chamado `description`, o número máximo de caracteres dentro do campo é 5.000. |
| Caracteres no nome da coluna do item | Até 250 caracteres |
| Seleções por catálogo | Até 30 seleções por catálogo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
As Liquid tags de catálogo não podem ser usadas recursivamente, ou seja, você não pode referenciar um item de catálogo que então chama um segundo item de catálogo dentro da mesma avaliação Liquid.
{% endalert %}