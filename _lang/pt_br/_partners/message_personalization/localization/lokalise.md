---
nav_title: Lokalise
article_title: Lokalise
description: "Este artigo de referência descreve a parceria entre a Braze e o Lokalise, um serviço de gerenciamento de tradução para equipes ágeis."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> O [Lokalise](https://lokalise.com) é um serviço de gerenciamento de tradução para equipes ágeis.

_Esta integração é mantida pelo Lokalise._

## Sobre a integração {#about-the-integration}

O Lokalise oferece duas opções de integração com a Braze:

- **Integração multilíngue (recomendada)**: Usa a [API or interface de programação do aplicativo (API) de composição multilíngue]({{site.baseurl}}/api/endpoints/translations) da Braze para fornecer uma sincronização bidirecional direta entre o Lokalise e a Braze. Essa integração funciona com variantes de mensagens localizadas para Campaigns, Canvas e modelos de e-mail, e oferece suporte a fluxos de trabalho pré-lançamento e pós-lançamento para push, e-mail e In-App Messages.
- **Integração de Connected Content (legada)**: Usa o Connected Content da Braze para inserir conteúdo traduzido com base nas configurações de idioma do usuário.

Este artigo aborda a configuração de ambas as integrações.

## Integração multilíngue (recomendada) {#multi-language-integration-recommended}

A integração multilíngue usa a API or interface de programação do aplicativo (API) de composição multilíngue da Braze para fornecer uma maneira simplificada e automatizada de gerenciar conteúdo multilíngue da Braze dentro do Lokalise.

### Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Lokalise | É necessário ter uma conta do Lokalise para usar essa parceria. |
| Projeto de tradução do Lokalise | Crie um projeto do Lokalise com o tipo **Marketing and support** e escolha **Braze** como a **Content integration**. |
| Configurações multilíngues da Braze | O [suporte multilíngue]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings) deve estar ativado no seu espaço de trabalho da Braze. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões para ler e atualizar Campaigns, Canvas e modelos de e-mail. Você pode criar uma no dashboard da Braze em **Settings** > **API or interface de programação do aplicativo (API) Keys**. |
| Região do servidor da Braze | Sua [região do servidor da Braze]({{site.baseurl}}/api/basics#endpoints) (por exemplo, US-01, EU-01). Você pode encontrá-la no dashboard da Braze. |
| Tags de tradução no conteúdo da Braze | As mensagens devem usar [tags de tradução]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para identificar o conteúdo traduzível. Envolva cada bloco traduzível em tags {% raw %}`{% translation ID %}...{% endtranslation %}`{% endraw %} com um ID exclusivo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Configuração e uso {#setup-and-usage}

Para instruções detalhadas sobre como conectar a integração multilíngue da Braze no Lokalise, importar conteúdo, traduzir e exportar traduções de volta para a Braze, consulte a [documentação de integração com a Braze do Lokalise](https://docs.lokalise.com/en/articles/13654162-braze).

A integração oferece suporte a:
- Sincronização bidirecional direta entre o Lokalise e a Braze (sem manipulação manual de arquivos)
- Variantes de mensagens localizadas para Campaigns, Canvas e modelos de e-mail
- Fluxos de trabalho de tradução pré-lançamento e pós-lançamento

{% alert note %}
Somente o conteúdo configurado para uso multilíngue na Braze e envolvido em tags de tradução está disponível para importação no Lokalise. Os códigos de idioma devem corresponder exatamente na Braze e no Lokalise para que as traduções sejam sincronizadas corretamente.
{% endalert %}

## Integração de Connected Content (legada) {#connected-content-integration-legacy}

A integração legada usa o Connected Content da Braze para inserir conteúdo traduzido com base nas configurações de idioma do usuário.

### Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Lokalise | É necessário ter uma conta do Lokalise para usar essa parceria. |
| Projeto de tradução do Lokalise | Crie um projeto do Lokalise com o tipo de projeto **Software Localization**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Criar um novo projeto do Lokalise {#create-a-new-lokalise-project}

Para criar um novo projeto de tradução, faça login no Lokalise e selecione **New Project**. Em seguida, nomeie seu projeto, escolha um **Base Language** (o idioma a partir do qual você traduzirá), adicione um ou mais **Target Languages** e escolha o tipo de projeto **Software Localization**. Quando estiver pronto, clique em **Proceed**.

### Integração {#integration}

No Lokalise, você criará uma chave de tradução para cada uma das variáveis de Connected Content definidas na Braze. Quando as traduções estiverem prontas, você poderá gerar um arquivo JSON por idioma e publicá-lo nas URLs que servirão seu Connected Content.

#### Etapa 1: Configuração de idiomas do usuário {#step-1-configure-user-languages}

Se ainda não tiver feito isso, abra o dashboard da Braze e vá para **Users > User Import**. Aqui, você pode importar seus usuários. Ao preparar um arquivo CSV para importação, certifique-se de incluir uma coluna de idioma com os idiomas dos usuários. Esse campo de idioma será usado posteriormente na exibição de traduções.

{% alert important %}
Os códigos de idioma usados devem corresponder tanto na Braze quanto no Lokalise.
{% endalert %}

#### Etapa 2: Prepare suas traduções no Lokalise {#step-2-prepare-your-translations-on-lokalise}

Em seguida, para preparar suas traduções no Lokalise, você precisará criar manualmente as chaves de tradução com o mesmo nome que está usando nas variáveis de Connected Content da Braze.

Por exemplo, vamos criar uma chave de tradução simples, `description`:
1. Abra seu projeto do Lokalise, clique em **Add Key** e digite "description" no campo **Key**.
2. Digite "Demo description" no campo **Base Language Value**.
3. Adicione "Web" no menu suspenso **Platforms**.
4. Quando estiver pronto, clique em **Save**.

![Modal de adição de chave do Lokalise criando a chave de tradução description.]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Sua chave de tradução deve aparecer no editor de projetos:

![Editor de projetos do Lokalise mostrando a chave de tradução recém-adicionada.]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

##### Problemas conhecidos {#known-issues}

- Suas chaves devem ser atribuídas à plataforma **Web**.
- Evite usar chaves que contenham pontos (`.`) ou a string `_on`. Por exemplo, use `this_is_the_key` em vez de `this.is.the.key`, e use `join_us_instagram` em vez de `join_us_on_instagram`.

#### Etapa 3: Configuração do app da Braze no Lokalise {#step-3-configure-the-braze-app-on-lokalise}

Abra seu projeto do Lokalise e clique em **Apps**. Procure e instale o app da Braze. Você verá a seguinte tela:

![Configuração da Braze no Lokalise listando o ID do projeto e a URL dos arquivos de tradução.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

Na **Translation File URL**, o Lokalise publica um arquivo JSON contendo todas as traduções para suas chaves no projeto. Você obterá uma URL de arquivo de tradução para cada idioma-alvo do projeto. É por isso que as URLs de arquivo de tradução resultantes têm duas partes:

1. A primeira parte do caminho da URL é comum a todos os idiomas.
2. O nome do arquivo JSON no final da URL é baseado no código do idioma.

A URL do arquivo de tradução é a URL de que você precisará ao configurar uma Campaign da Braze. Você pode atualizar o conteúdo do arquivo JSON clicando em **Refresh**. Note que a URL permanecerá a mesma, e você não precisará alterar sua chamada de Connected Content na Braze.

##### URL de teste {#test-url}

Para testar essa URL, copie-a e substitua {% raw %}`{{${language}}}`{% endraw %} por um código de idioma (por exemplo, `en`) e abra essa URL no seu navegador. Você verá um arquivo JSON com suas chaves e traduções:

![Visualização no navegador do arquivo JSON de tradução exportado pelo Lokalise.]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

#### Etapa 4: Uso de traduções na Campaign da Braze {#step-4-use-translations-in-braze-campaign}

##### Inserir chamada de Connected Content {#insert-connected-content-call}

Quando estiver com tudo pronto, retorne à Braze e abra uma Campaign existente ou crie uma nova. Criaremos uma nova Campaign de e-mail com conteúdo de amostra para este exemplo. Clique em **Edit Email Body**.

Para inserir suas traduções, você precisa adicionar a solicitação de Connected Content no HTML, na parte superior do documento ou logo antes do primeiro local em que a tradução é necessária. Isso pode ser feito inserindo o seguinte markup:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Substitua a URL `https://exports.live.lokalise.cloud/...` pela URL do arquivo de tradução obtida na etapa anterior.

{% raw %}

- `{{${language}}}` significa "inserir o idioma do usuário nessa posição". Caso prefira, é possível codificar seu código de idioma. Exemplo: `en.json`.
  - Para garantir que o arquivo JSON traduzido apropriado seja recuperado para cada usuário, é necessário colocar o atributo de perfil `{{${language}}}` ou outro atributo personalizado semelhante que contenha o idioma do usuário no final da URL dos arquivos de tradução (por exemplo, `/{{${language}}}.json`). Os valores contidos nesses atributos devem corresponder ao prefixo de cada um dos arquivos JSON traduzidos. Isso garantirá que o arquivo de tradução correto será retornado para cada usuário.
- `:save translations` salvará o conteúdo JSON na variável translations.

##### Exibir traduções {#display-translations}

Agora use a variável translations para exibir as traduções desejadas por suas chaves.

Por exemplo, para exibir a chave `description`, use `{{ translations.description }}`.

{% endraw %}
![Exemplo do editor de e-mail da Braze mostrando traduções de Connected Content do Lokalise.]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

Por fim, salve o modelo de e-mail e faça uma prévia. Você deverá ver sua tradução sendo exibida.

## Perguntas frequentes {#frequently-asked-questions}

### O que acontecerá se eu excluir sem querer uma chave do Lokalise? {#what-happens-if-i-accidentally-delete-a-key-from-lokalise}

A string correspondente na Braze não terá mais uma tradução.

### Se eu tiver um locale `en`, mas substituí-lo por `en-US` no Lokalise, a Braze irá lê-lo como `en-US`? {#if-i-have-an-en-locale-but-override-it-with-en-us-on-lokalise-will-braze-read-it-as-en-us}

Não, os códigos ISO de locale devem corresponder na Braze e no Lokalise.

### Podemos usar o sinalizador `:rerender` ao conectar o conteúdo do Lokalise? {#can-we-use-the-rerender-flag-when-connecting-lokalise-content}

Sim, claro. Você pode consultar a documentação da Braze para saber como adicionar esse sinalizador.

### Após atualizar o arquivo de tradução no Lokalise, por que não consigo ver nenhuma alteração no conteúdo traduzido na Braze? {#after-refreshing-the-translation-file-on-lokalise-why-cant-i-see-any-changes-in-the-translated-content-on-braze}

A Braze armazena em cache o conteúdo traduzido, que pode levar alguns minutos para ser atualizado. Se estiver testando suas Campaigns e precisar ver os resultados das traduções imediatamente, poderá usar o parâmetro `:cache_max_age`, conforme explicado neste artigo de referência.