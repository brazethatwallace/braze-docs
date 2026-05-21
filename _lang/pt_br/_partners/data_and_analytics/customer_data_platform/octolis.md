---
nav_title: Octolis
article_title: Octolis
description: "Este artigo de referência descreve a parceria entre a Braze e a Octolis, uma plataforma de ativação de dados que permite integrar seus dados à Braze."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> A [Octolis](http://octolis.com) é uma poderosa plataforma de ativação de dados (ou CDP headless). Sobreposta a um banco de dados de sua propriedade, a Octolis é uma maneira fácil de unificar, preparar, pontuar e sincronizar dados em suas ferramentas de negócios.

_Essa integração é mantida pela Octolis._

## Sobre a integração {#about-the-integration}

A integração da Braze com a Octolis atua como middleware entre suas fontes de dados brutos e a Braze, permitindo recuperar e unificar dados de várias fontes, online e offline:
1. Unifique e combine dados de fontes como loja virtual, CRM, sistema de PDV etc.
2. Normalize e pontue
3. Sincronização em tempo real de campos computados e eventos para a Braze

![Diagrama do fluxo de dados entre fontes, Octolis e Braze]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Octolis | É necessário ter uma conta Octolis para usar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). <br><br> Isso pode ser criado no dashboard da Braze em **Settings** > **API Keys**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Chave do app da Braze | A chave do identificador do seu app. Ela pode ser encontrada em **Braze Dashboard > Manage Settings > API Key**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

Antes de iniciar a integração, consulte as seções a seguir sobre conexões, fontes, públicos e sincronizações.

Para saber mais, consulte a seção [Como começar](https://help.octolis.com/) da Octolis.

### Etapa 1: Conecte a Octolis às suas fontes de dados {#step-1-connect-octolis-to-your-data-sources}

Para enviar dados para a Braze, confirme se você criou pelo menos um [público](https://help.octolis.com/audiences/create-a-no-code-audience). Um público combina várias fontes de dados, aplica-as às etapas de preparação e adiciona campos computados.

Esses públicos precisam ser criados com base em várias fontes de dados. Uma fonte pode ser qualquer uma das seguintes:
- Um objeto do Salesforce (contatos, contas, etc.)
- Um objeto do Zendesk (tickets)
- Um arquivo dentro de um SFTP (arquivo CSV contendo alguns contatos, arquivo JSON contendo eventos...)
- Uma tabela/visualização de um banco de dados.
- Um dos seus sistemas envia registros por meio de webhooks ou chamadas de API.

### Etapa 2: Adicionar a Braze como destino {#step-2-add-braze-as-a-destination}

Em seguida, para definir a Braze como um novo destino, selecione **+ Add more** na parte superior do seu destino atual na tela principal e selecione **Braze** entre as ferramentas de negócios disponíveis.

![Tela de seleção de destino na Octolis com a opção Braze]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

Depois de selecionado, forneça o seguinte:

- Sua chave de API da Braze: isso pode ser criado no dashboard da Braze em **Settings** > **API Keys**.
- Período: a Octolis aplicará a limitação de taxa no período determinado.
- Volume de solicitações: número de solicitações que você pode fazer dentro desse período.
- Atributos personalizados: especifique aqui os novos campos que você enviará para a Braze, seu formato (string, integer, float) e marque a opção **Required for syncs** se quiser que um deles seja obrigatório para uma sincronização.

![Tela de configuração do destino Braze na Octolis]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

Após a configuração, a Braze aparecerá como um novo destino na tela inicial.

### Etapa 3: Criar uma nova sincronização {#step-3-create-a-new-sync}

No menu, clique em **Syncs** e selecione **Add sync** no canto superior direito. Selecione o público desejado a partir dos públicos que você criou anteriormente.
Em seguida, selecione **Braze** como o destino e para qual entidade você enviará os dados.

![Tela de criação de sincronização na Octolis com Braze selecionado]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### Etapa 4: Definir configurações de saída {#step-4-set-output-settings}

Por padrão, a Braze cria todos os atributos que você enviaria, mas é preciso documentar a lista de campos a serem sincronizados.

![Tela de configurações de saída da sincronização na Octolis]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

Aqui está uma definição específica dos campos de configuração.

| Campo | Descrição |
| --- | --- |
| Para onde você deseja sincronizar o público? | A entidade Braze onde você criará ou atualizará registros. |
| Qual campo é usado para identificar um registro? | O campo que a Octolis usará para identificar um registro caso ele já exista na Braze. |
| Com que frequência você deseja enviar cada registro? | Por padrão, a sincronização será incremental para todas as integrações (API, banco de dados, FTP). Isso significa que somente os novos valores desde a última atualização serão atualizados. Caso necessário, você também pode enviar tabelas inteiras em intervalos regulares. Ao iniciar, a Octolis enviará a tabela completa. |
| Quais campos devem ser sincronizados? | Mapeamento de campos da Octolis para a Braze. A lista de todos os campos disponíveis aparece no menu suspenso. Para enviar um campo computado para a Braze, você deve primeiro garantir que criou a coluna correspondente na sua entidade Braze. |
| Quando você deseja sincronizar o público? | Como os dados serão enviados à Braze: manualmente, em tempo real ou em períodos programados.  |
| Sincronizar quando o registro é... | Criar: para opt-ins, é importante que a tabela da Braze continue sendo a principal. Não é ideal que a Octolis dispare uma sincronização quando o campo for atualizado.<br><br>Atualizar: por outro lado, para um campo de nome, por exemplo, é recomendável atualizar o campo na tabela da Braze sempre que um cliente informar uma nova entrada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Desduplicação de várias chaves {#multi-keys-deduplication}

A desduplicação é um grande desafio ao reconciliar dados de várias fontes, especialmente online e offline. Por meio do módulo avançado sem código da Octolis, você pode usar várias chaves para [desduplicação](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work). Esse módulo está disponível para cada tabela mestre, o que significa que você pode adaptar a lógica a cada entidade.