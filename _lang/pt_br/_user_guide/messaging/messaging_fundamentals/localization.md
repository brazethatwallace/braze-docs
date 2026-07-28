---
nav_title: Localização
article_title: Localização
page_order: 8
description: "Este artigo de referência aborda os conceitos básicos de localização, lista os benefícios de diferentes abordagens de orquestração em Campaigns e Canvas, e apresenta diferentes formas de lidar com a personalização no envio de mensagens."
tool:
    - Campaigns
    - Canvas
---

# Localização {#localization}

> Para empresas com clientes em vários países, lidar com a localização no início da sua jornada com a Braze pode economizar tempo e recursos.

## Como funciona {#how-it-works}

As informações de localidade são armazenadas no perfil do usuário com base nos dados que você coleta usando um [SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration) (automaticamente) ou a [REST API]({{ site.baseurl }}/api/endpoints/user_data/post_user_track). A localidade contém o idioma e um identificador de região. Essas informações estão disponíveis na ferramenta de segmentação da Braze em **País** e **Idioma**.

{% alert tip %}
Para detalhes técnicos sobre como a localidade é coletada pelos nossos SDKs, consulte a documentação oficial do [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html), [Android](http://developer.android.com/reference/java/util/Locale.html) e [Web](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language).
{% endalert %}

## Gerenciamento de traduções {#translation-management}

Considere as seguintes abordagens para gerenciar suas traduções.

{% tabs local %}
{% tab campaign %}
### Um modelo para todos {#one-template-for-all}

Nesta abordagem, a localização é aplicada a um único modelo na Braze usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Após o envio, o dashboard fornece análises agregadas da Campaign. O engajamento no nível do usuário pode ser medido usando funis de segmentos personalizados, por exemplo, combinando os filtros **País** e **Campaign recebida**.

| Vantagens | Considerações |
| --- | --- |
| - Abordagem centralizada<br>- Tempo reduzido de criação de e-mail, sem necessidade de criar o mesmo e-mail várias vezes | - Criação manual de relatórios<br>- O relatório da Campaign mostra métricas agregadas em vez de métricas por país<br>- É necessário testar o Liquid minuciosamente para garantir que ele seja preenchido conforme esperado<br>- Dependendo de como você obtém o valor do país ou de quantos países você configurou, pode ser difícil testar cada país<br>- Mais difícil programar envios para horários específicos em diferentes fusos horários<br>- Mais difícil de usar se você quiser enviar conteúdo diferente por país. |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Um modelo para todos" }

### Um modelo por país {#one-template-per-country}

Nesta abordagem, os modelos são separados em diferentes localidades de envio. Após o envio, o dashboard exibe análises de envio com base em cada país separadamente, e quaisquer eventos de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) no nível do usuário também estarão vinculados a uma Campaign específica.

- Os modelos se beneficiam da implementação de [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) para fins de manutenção e rastreamento.
- As Campaigns podem herdar as configurações do mesmo [modelo da Braze]({{site.baseurl}}/user_guide/messaging/templates) e [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) (como [modelos de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates) que contêm Liquid).
- Campaigns e modelos pré-existentes podem ser [duplicados]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating) para permitir um tempo de retorno mais rápido.

| Vantagens | Considerações |
| --- | --- |
| - Escalável para múltiplas localidades<br>- Relatórios de receita por país dentro da Braze (como por Campaign)<br>- Flexibilidade se houver conteúdo drasticamente diferente por país | - Requer estruturação estratégica<br>- Mais esforço de construção necessário (como Campaigns separadas para cada país) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Um modelo por país" }
{% endtab %}

{% tab canvas %}
### Uma jornada para todos {#one-journey-for-all}

Nesta abordagem, a localização é tratada dentro dos [fundamentos do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_basics#building-the-customer-journey) e do Liquid para definir o envio de mensagens para cada usuário.

Após o envio de um Canvas, o dashboard fornece [análises agregadas do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics), enquanto o engajamento no nível do usuário pode ser medido por meio de [funis de segmentos]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size) personalizados, como a combinação dos filtros [**País**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#country) e [**Etapa do Canvas recebida**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step).

| Vantagens | Considerações |
| --- | --- |
| - Abordagem centralizada<br>- Tempo reduzido de criação de e-mail — sem necessidade de criar o mesmo e-mail várias vezes. | - Criação manual de relatórios<br>- O relatório do Canvas mostra métricas agregadas em vez de métricas por país<br>- É necessário testar o Liquid minuciosamente para garantir que ele seja preenchido conforme esperado<br>- Dependendo de como você obtém o valor do país ou de quantos países você configurou, pode ser difícil testar cada país<br>- Mais difícil programar envios para horários específicos em diferentes fusos horários<br>- Mais difícil de usar se você quiser enviar conteúdo diferente por país. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Uma jornada para todos" }

### Uma jornada por país {#one-journey-per-country}

Nesta abordagem, o construtor de jornadas do [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) oferece a flexibilidade de criar jornadas de usuário por meio de múltiplos [componentes do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components). Esses componentes podem ser [duplicados]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating) no nível do componente e da jornada geral.

A localização pode ser alcançada com os seguintes métodos:

- Canvas separados por país, garantindo que as jornadas complexas de usuário sejam definidas no topo do funil usando filtros de público
- Jornadas de usuário personalizadas por país, com a implementação de [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) para segmentar usuários de forma intuitiva em grande escala para cada jornada, criando threads de mensagens separados para cada país em um único Canvas

Após o envio, o dashboard fornece análises dinâmicas por país e, dentro dos eventos de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) no nível do usuário, com base na localização atual do cliente.

| Vantagens | Considerações |
| --- | --- |
| - Relatórios de receita por país dentro da Braze (como por Canvas, variante ou etapa)<br>- Flexibilidade se houver conteúdo drasticamente diferente por país<br>- Possibilidade de adicionar outros canais como parte da jornada no futuro | - Requer estruturação estratégica<br>- Mais esforço de construção necessário (como etapas de mensagem separadas para cada país)<br>- O Canvas pode ficar grande e difícil de ler se você tiver jornadas personalizadas e complexas para cada país em um único Canvas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Uma jornada por país" }
{% endtab %}
{% endtabs %}

## Envio de mensagens traduzidas {#sending-translated-messages}

Para enviar mensagens personalizadas com base no idioma, localidade ou atributos personalizados de um usuário, use um dos métodos a seguir.

### Tags Liquid de tradução (recomendado) {#translation-liquid-tag}

A Braze oferece suporte a uma tag Liquid {% raw %}`{% translation salutation %}Hello!{% endtranslation %}`{% endraw %} para direcionar usuários em diferentes idiomas com uma única mensagem.

Para um passo a passo completo, consulte o [guia sobre o uso de tags de tradução]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

### Abordagens alternativas {#alternative-approaches}

{% tabs local %}
{% tab Custom Liquid %}
Você pode colar manualmente seu conteúdo no corpo da mensagem e usar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) para exibir [condicionalmente]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) o idioma correto para o destinatário. Para fazer isso:

1. Redija sua mensagem e selecione **Idioma** para gerar a lógica condicional Liquid para cada um dos idiomas selecionados.
2. Você pode usar o seguinte modelo Liquid para ajudar a construir sua mensagem. Para cada campo com modelo, você deve inserir as variações após o segmento de modelo entre colchetes. A variação deve corresponder ao código de idioma referenciado nos colchetes antes dela.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. Teste sua mensagem antes de enviá-la inserindo o ID ou e-mail de um usuário para verificar como a mensagem apareceria para uma pessoa dependendo do idioma dela.

{% alert tip %}
Sempre recomendamos incluir uma instrução {% raw %}`{% else %}`{% endraw %} no seu envio de mensagens. Embora a maioria dos usuários veja a mensagem no seu idioma específico, o texto será visível para aqueles que:
- Não têm um idioma selecionado
- Têm um idioma que a Braze não suporta
- Têm um dispositivo em que o idioma não é detectável
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Os [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) da Braze são blocos de conteúdo reutilizáveis. Quando um bloco é alterado, todas as referências a esse bloco são atualizadas. Por exemplo, atualizações em um cabeçalho ou rodapé de e-mail serão refletidas em todos os e-mails, ou para abrigar traduções. Esses blocos também podem ser [criados]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) e [atualizados]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) usando a REST API, e os usuários podem fazer upload de traduções programaticamente.

Ao criar uma Campaign no dashboard, os Content Blocks podem ser referenciados usando a tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. Esses blocos podem conter todas as traduções dentro de lógica condicional para cada idioma, como mostrado na opção 1, ou um bloco separado para cada idioma pode ser usado.

Os Content Blocks também podem ser utilizados como um processo de gerenciamento de tradução, onde o conteúdo que precisa de tradução é armazenado em um Content Block, buscado, traduzido e então atualizado:
1. Crie manualmente um Content Block no dashboard com a tag "Needs Translation".
2. Seu serviço realiza uma busca noturna de todos os Content Blocks usando o [endpoint `/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks).
3. Seu serviço busca detalhes de cada Content Block por meio do [endpoint `/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) para ver quais blocos estão marcados para tradução.
4. Seu serviço de tradução traduz o corpo de todos os Content Blocks marcados como "Needs Translation".
5. Seu serviço acessa o [endpoint `/content_block/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) para atualizar o conteúdo traduzido e atualizar a tag para "Translation Complete".
{% endtab %}

{% tab Catalogs %}
Os [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) permitem que você acesse dados de objetos JSON importados via API e arquivos CSV para enriquecer suas mensagens, de forma semelhante a atributos personalizados ou propriedades de eventos personalizados por meio de Liquid. Por exemplo:

{% subtabs local %}
{% subtab API %}

Crie um catálogo por meio da seguinte chamada de API:
```bash
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

Adicione itens por meio da seguinte chamada de API:

```bash
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
Crie um CSV no seguinte formato:

| id | context | language | body |
| --- | --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abordagens alternativas" }
{% endsubtab %}
{% endsubtabs %}

Esses itens de catálogo podem ser referenciados usando [personalização]({{site.baseurl}}/user_guide/data/activation/catalogs/create), conforme mostrado no exemplo a seguir, ou [seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) que permitem criar grupos de dados.

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}}
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Braze partners %}
Muitos parceiros da Braze oferecem soluções de localização, incluindo [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex#about-the-integration) e [Crowdin](https://crowdin.com/). Normalmente, os usuários utilizam a plataforma em conjunto com uma equipe interna e uma agência de tradução. Essas traduções são então carregadas e ficam acessíveis via REST API. Esses serviços também costumam utilizar [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), permitindo que os usuários busquem as traduções via API.

Por exemplo, as seguintes chamadas de Conteúdo conectado chamam o Transifex e o Crowdin para buscar uma tradução, utilizando {% raw %}`{{${language}}}`{% endraw %} para identificar a tradução correta para um determinado usuário. Essa tradução é então salva no bloco JSON "strings" e referenciada.

{% subtabs local %}
{% subtab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Spreadsheets %}
Armazene as traduções em uma planilha e use um dos métodos a seguir para enviar sua mensagem no idioma relevante.

{% subtabs local %}
{% subtab Connected Content %}
Você pode trabalhar com uma agência de tradução para armazenar traduções em uma planilha do Google e consultar esse conteúdo usando o [Conteúdo conectado da Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Quando você envia uma mensagem, a tradução relevante para cada usuário será inserida no corpo da sua Campaign com base no idioma selecionado.

{% alert note %}
A API do Google Sheets tem um limite de 500 solicitações por 100 segundos por projeto. As chamadas de Conteúdo conectado podem ser armazenadas em cache, mas essa solução não é escalável para Campaigns de alto tráfego.
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
Esta opção fornece um método alternativo de transformar planilhas do Google em objetos JSON consultados via Conteúdo conectado. Ao transformar uma planilha em uma API JSON via SheetDB, você pode escolher entre [múltiplos planos de assinatura](https://sheetdb.io/pricing) dependendo da cadência das chamadas de API.

A estrutura da planilha segue as etapas da opção 4, mas o SheetDB também fornece [filtros adicionais](https://docs.sheetdb.io/#sheetdb-api) para consultar os objetos.

Alguns usuários podem preferir implementar o SheetDB com menos dependências de Liquid e blocos de Conteúdo conectado, implementando o [método de busca](https://docs.sheetdb.io/#get-search-in-document) do SheetDB em chamadas de solicitação GET para filtrar os objetos JSON com base na tag Liquid {% raw %}`{{${language}}}`{% endraw %} para retornar automaticamente os resultados de um único idioma, em vez de construir grandes blocos condicionais.

#### Etapa 1: Formate a planilha do Google {#step-1-format-the-google-sheet}

Primeiro, construa a planilha do Google de forma que os idiomas sejam objetos diferentes:

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Etapa 1: Formate a planilha do Google" }

#### Etapa 2: Use a tag Liquid de idioma em uma chamada de Conteúdo conectado {#step-2-use-the-language-liquid-tag-in-a-connected-content-call}

Em seguida, implemente a tag Liquid {% raw %}`{{${language}}}`{% endraw %} dentro de uma chamada de Conteúdo conectado. Observe que o SheetDB gerará automaticamente o `sheet_id` ao criar a planilha.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Etapa 3: Crie o modelo das suas mensagens {#step-3-template-your-messages}

Por fim, use Liquid para criar o modelo das suas mensagens:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Considerações {#considerations}

- O campo {% raw %}`{{${language}}}`{% endraw %} precisa estar definido para todos os usuários; caso contrário, um bloco condicional Liquid deve ser incluído como tratamento de fallback para usuários sem um idioma definido.
- A modelagem de dados no Google Sheets deve seguir uma estrutura vertical orientada por idioma, em vez de ter objetos de mensagem.
- O SheetDB oferece uma conta gratuita limitada e múltiplas opções pagas que devem ser consideradas com base na sua estratégia de Campaign.
- As chamadas de Conteúdo conectado podem ser armazenadas em cache. Recomendamos medir a cadência projetada das chamadas de API e investigar uma abordagem alternativa de chamar o endpoint principal do SheetDB em vez de usar o método de busca.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}