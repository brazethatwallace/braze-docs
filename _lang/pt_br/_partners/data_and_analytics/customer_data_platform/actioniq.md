---
nav_title: ActionIQ
article_title: ActionIQ
description: "Este artigo de referência aborda a integração entre a Braze e a ActionIQ. A ActionIQ é uma plataforma de dados do cliente corporativa para profissionais de marketing, analistas e tecnólogos. Esta integração permite que as marcas sincronizem e mapeiem seus dados ActionIQ diretamente na Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> A [ActionIQ](https://www.actioniq.com/) é uma plataforma de dados do cliente para marcas corporativas que oferece aos profissionais de marketing maneiras fáceis e seguras de ativar dados em qualquer lugar da experiência do cliente. A arquitetura composável exclusiva da ActionIQ significa que os dados podem permanecer em segurança onde estão, e as equipes de marketing usam apenas as ferramentas de que precisam.

_Essa integração é mantida pela ActionIQ._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a ActionIQ permite que as marcas sincronizem e mapeiem seus dados da ActionIQ diretamente na Braze, possibilitando o fornecimento de experiências extraordinárias aos clientes com base em toda a amplitude de seus dados de clientes. As integrações disponíveis permitem que os usuários:

- Atualizem perfis de usuário na Braze com informações de associação de público e quaisquer atributos diretamente da ActionIQ
- Encaminhem os eventos rastreados pela ActionIQ para a Braze em tempo real para disparar campanhas personalizadas e direcionadas
- Entreguem campanhas disparadas por API na Braze diretamente dos pontos de contato em uma jornada da ActionIQ

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta ActionIQ | Uma conta ActionIQ é necessária para aproveitar esta integração. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões necessárias para a respectiva integração. Consulte a respectiva seção de requisitos para obter mais detalhes. <br><br>Essa chave pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrações {#integrations}

### Associação de público {#audience-membership}

Esta integração é usada para sincronizar a associação de público da ActionIQ com a Braze, criando atributos personalizados que indicam se um perfil da Braze faz parte de um segmento. Cada público da ActionIQ corresponde a um atributo personalizado booleano único.

A convenção de nomenclatura padrão para o atributo personalizado criado é: `AIQ_<Audience ID>_<Split ID>`.

Para criar um segmento desses usuários, faça o seguinte:
1. Na Braze, navegue até **Segments**.
2. Crie um novo segmento.
3. Selecione **Custom Attributes** como seu filtro.
4. A partir daqui, escolha o atributo personalizado da ActionIQ.
5. Depois que o segmento for criado, você pode selecioná-lo como um filtro de público ao criar uma campanha ou Canvas.

Além disso, essa integração atualizará qualquer atributo personalizado ou padrão em um perfil de usuário da Braze com os valores de atributo da ActionIQ.

#### Requisitos {#requirements}

É necessária uma chave da API REST da Braze com as permissões `users.track` e `user.export.ids`. Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**.

Na ActionIQ, configure uma conexão com a Braze fornecendo sua chave da API REST e o endpoint REST da Braze.

Para corresponder aos consumidores na plataforma Braze, os seguintes identificadores devem ser incluídos na sua configuração de ativação:
- `braze_id`
- `external_id`

### Eventos {#events}

Você pode configurar a plataforma ActionIQ para receber informações de eventos por meio de seu serviço de ingestão de streaming. Essa opção de integração encaminha esses eventos para a Braze para que os profissionais de marketing os utilizem para orquestração ou para disparar campanhas de marketing. A integração de eventos é capaz de enviar atributos adicionais da ActionIQ como parte das propriedades na carga útil do evento.

#### Requisitos

É necessária uma chave da API REST da Braze com as permissões `users.track` e `user.export.ids`. Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**.

A integração de eventos envia as seguintes informações para a Braze:
- Nome do evento
- Identificador do consumidor (`braze_id` ou `external_id`)
- Data e hora
- Propriedades do evento, que são preenchidas por quaisquer atributos adicionais na configuração de exportação

### Campanhas disparadas {#triggered-campaigns}

Essa integração disparará uma campanha na Braze para todos os usuários em um segmento da ActionIQ. Depois de configurar o texto, os testes multivariantes e as regras de reelegibilidade da sua campanha, você poderá dispará-la a partir de qualquer ponto de contato da jornada da ActionIQ adicionando o ID da campanha da Braze à sua configuração de exportação.

Opcionalmente, você pode incluir quaisquer outros atributos da ActionIQ em sua exportação para preencher o texto da sua campanha. Eles são enviados com o objeto `trigger_properties`.

#### Requisitos

É necessária uma chave da API REST da Braze com as permissões `campaigns.trigger.send` e `campaigns.list`. Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**.

Os seguintes valores devem ser enviados em sua exportação da ActionIQ para a Braze:
- Identificador do consumidor (`braze_id` ou `external_id`)
- ID da campanha