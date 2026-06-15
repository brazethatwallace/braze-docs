---
nav_title: Extole
article_title: Extole
description: "Este artigo descreve a parceria entre a Braze e a Extole, uma empresa de marketing de indicação, que permite transferir eventos e atributos de clientes dos programas de indicação de amigos e de crescimento para a Braze."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> A [Extole](https://www.extole.com/), uma empresa de SaaS, é líder do setor em marketing de indicação de amigos, ajudando a criar e otimizar programas eficazes de marketing de indicação para aumentar a aquisição de clientes.

_Essa integração é mantida pela Extole._

## Sobre a integração {#about-the-integration}

Com a integração entre a Braze e a Extole, você pode transferir eventos e atributos de clientes dos programas de indicação de amigos e de crescimento da Extole para a Braze, o que permite criar campanhas de marketing mais personalizadas que aumentam a aquisição, o engajamento e a fidelidade dos clientes. Também é possível extrair dinamicamente atributos de conteúdo da Extole, como códigos de compartilhamento e links personalizados, para as comunicações da Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Extole | É necessário ter uma conta da Extole para usar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com a permissão `users.track`. Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| URL da API da Braze | Seu URL da API da Braze é específico para sua [instância da Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Os casos de uso a seguir mostram algumas maneiras de usar a integração da Extole com a Braze. Trabalhe com seus gerentes de implementação e de sucesso do cliente da Extole para desenvolver uma opção que atenda às necessidades específicas da sua empresa.

- Use eventos personalizados dos seus programas de indicação e engajamento para disparar uma Campaign ou Canvas na Braze
- Crie Segments, dashboards e relatórios personalizados usando os dados dos seus programas com tecnologia Extole
- Cancele automaticamente a inscrição ou inscreva usuários na sua lista de marketing na Braze

## Integração {#integration}

Conclua as etapas a seguir para colocar sua integração em funcionamento rapidamente. Seus gerentes de implementação e de sucesso do cliente da Extole darão suporte durante todo o processo e responderão a quaisquer perguntas que você possa ter.

### Conecte-se à sua conta da Braze {#connect-to-your-braze-account}

1. Selecione a integração da Braze na página [Partners](https://my.extole.com/partners) da sua conta My Extole.
2. Na integração da Braze, selecione **Install** para iniciar a conexão entre a Extole e a Braze.
3. Preencha os campos obrigatórios, começando com sua chave da API REST da Braze.
4. Digite seu URL da API da Braze. Esse URL depende da instância em que sua conta da Braze está provisionada.
5. Adicione todos os eventos da Extole que você gostaria de enviar para a Braze. Os eventos padrão, as propriedades do evento e os atributos de usuário são descritos na [tabela de eventos da Extole](https://dev.extole.com/docs/braze#extole-program-events).
6. Adicione quaisquer estados de recompensas que você gostaria de enviar para a Braze, além do estado `FULFILLED`. Consulte a [tabela de recompensas da Extole](https://dev.extole.com/docs/braze#extole-rewards) para obter descrições dos estados de recompensas disponíveis.
7. Selecione o mapeamento da sua chave de ID externa da Braze. É assim que a Extole atualiza os perfis de usuário na Braze. Você pode mapear a chave de ID externa da Braze para `email_address` ou `partner_user_id` da Extole para o usuário. Recomendamos usar `external_id` em vez de `email_address`, pois é mais seguro.
8. Salve suas configurações para concluir a conexão. Agora, os eventos da Extole podem fluir para sua conta da Braze.

### Eventos do programa Extole {#extole-program-events}

Abaixo estão os eventos padrão, as propriedades do evento e os atributos de usuário que a Extole enviará para a Braze. Entre em contato com os gerentes de implementação ou de sucesso do cliente da Extole para identificar e adicionar eventos adicionais da Extole à sua integração.

| Evento | Descrição | Propriedades do evento | Atributos do usuário |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Um participante cria seu link de compartilhamento inserindo seu e-mail no Extole Share Experience. | Nome do evento  <br>Hora do evento  <br>Parceiro (Extole)  <br>Funil (defensor ou amigo)  <br>Programa | <br>ID externo <br>E-mail  <br>Link de compartilhamento |
| `extole_shared` | Um participante compartilha seu link de indicação com um amigo. | Nome do evento  <br>Hora do evento  <br>Parceiro (Extole)  <br>ID externo  <br>Funil (defensor ou amigo)  <br>Programa  <br>Canal de compartilhamento | E-mail <br>Nome <br>Sobrenome |
| `outcome` - O resultado é dinâmico com base na configuração do seu programa (como `extole_shipped`, `extole_converted`)| Um participante converteu ou concluiu o evento de resultado desejado configurado para o programa. | Dinâmico por programa | E-mail <br>Nome <br>Sobrenome |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eventos do programa Extole" }

### Estados de inscrição da Extole {#extole-subscription-states}

| Estado da inscrição | Descrição | Propriedades do evento | Atributos do usuário |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Um participante optou por receber mensagens de marketing. | N/D | E-mail  <br>Tipo de lista  <br>ID externo  <br>Inscrição de e-mail (aceitação) |
| `unsubscribed` | Um participante cancelou o recebimento das comunicações por e-mail da Extole. | E-mail  <br>ID externo  <br>Estado da inscrição (inscrição cancelada)  <br>ID do grupo de inscrições  | Tipo de lista |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Estados de inscrição da Extole" }

### Recompensas da Extole {#extole-rewards}

Por padrão, a Extole enviará eventos de recompensas no estado `FULFILLED` para a Braze para que você possa disparar notificações de recompensas por meio de uma Campaign ou Canvas na Braze. Consulte a tabela a seguir para ver mais estados de recompensas.

| Estado da recompensa | Descrição | Propriedades do evento | Atributos do usuário |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | O estado padrão. Foi atribuído um valor (como cupom ou cartão-presente) à recompensa por um fornecedor de recompensas da Extole. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `EARNED` | Uma recompensa foi criada e associada a uma pessoa. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `SENT` | A recompensa foi processada e enviada por e-mail ou em um dispositivo para o destinatário. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `REDEEMED` | A recompensa foi usada pelo destinatário, conforme evidenciado em um evento de conversão ou resgate enviado à Extole. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `FAILED` | Um problema impediu que a recompensa fosse emitida ou enviada, exigindo atenção. | E-mail <br>Valor nominal  <br>Código de cupom  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `CANCELED` | A recompensa foi desativada e retornará ao inventário. | E-mail <br>Valor nominal  <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
| `REVOKED` | A recompensa cumprida foi invalidada. Por exemplo, a Extole solicitou um cartão-presente de um fornecedor e depois determinou que o cartão foi enviado por engano. Se o fornecedor oferecer suporte à revogação da recompensa, a Extole solicitará a devolução dos fundos, e a recompensa não será mais válida. | E-mail <br>Valor nominal   <br>Tipo de valor nominal  | E-mail <br>Nome  <br>Sobrenome |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Recompensas da Extole" }


## Personalização {#customization}

### Localizar e criar usuários na Braze {#find-and-create-users-in-braze}

Para determinados casos de uso, como uma nova inscrição de e-mail ou SMS em que a Extole não tem um ID externo (ID de usuário), a Extole pode verificar o identificador do usuário usando o endpoint [Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) da Braze. A Extole adicionará e atualizará quaisquer atributos de perfil se o usuário existir na Braze. Se a solicitação não retornar um perfil de usuário, a Extole usará o endpoint `/users/track` para criar um alias de usuário com o endereço de e-mail do usuário como o nome do alias.

## Usando esta integração {#using-this-integration}

Depois de conectar suas contas, os eventos começarão a fluir automaticamente da Extole para a Braze sem nenhuma ação da sua parte. Uma visualização em tempo real dos eventos enviados para a Braze pode ser encontrada na central de webhooks de saída da Extole para solução de problemas.