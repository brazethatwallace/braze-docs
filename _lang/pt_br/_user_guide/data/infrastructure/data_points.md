---
nav_title: Pontos de dados
article_title: Pontos de dados
page_order: 3
page_type: reference
description: "Este artigo de referência descreve o que são pontos de dados na Braze e como você pode estar ciente de seu uso."
search_rank: 6
---

# Pontos de dados {#data-points}

> Na Braze, dados significam ação: cada dado que chega à Braze atualiza a associação do Segment or segmento or segmento, pode disparar e cancelar o envio de mensagens, está imediatamente disponível para a personalização de mensagens e muito mais. Os pontos de dados ajudam você a definir as informações mais impactantes para sua empresa. Ao considerar cuidadosamente quais informações devem ser rastreadas, você garante o direcionamento dos dados de maior impacto para a experiência dos usuários.

Os pontos de dados são baseados em informações registradas em perfis de usuários. Você pode encontrar uma descrição mais detalhada dessa definição em seu contrato com a Braze. Nossa equipe de sucesso do cliente pode ajudar a recomendar as melhores práticas de dados para atender às suas necessidades.

## Definição {#definition}

"Pontos de dados" referem-se a uma unidade faturável de uso dos Serviços da Braze, medida por um início de sessão, fim de sessão, evento personalizado ou compra registrada, bem como qualquer atributo definido em um perfil de usuário final. Para fins de esclarecimento, cada um dos dados mencionados anteriormente nesta seção (como início de sessão, fim de sessão, evento personalizado ou compra registrada, bem como qualquer atributo) definido no perfil de um usuário final em um determinado momento conta como um único ponto de dados.

Dados e eventos coletados por padrão pelos Serviços da Braze, incluindo, por exemplo, tokens por push, informações do dispositivo e todos os eventos de rastreamento de engajamento de Campaign, como aberturas de e-mail e cliques em notificações por push, *não* são contabilizados como pontos de dados.

Consulte a seção [Contagem de consumo](#consumption-count) deste artigo para entender quais dados contam para a sua alocação de pontos de dados.

## Visualizando o uso de pontos de dados {#viewing-data-point-usage}

Para visualizar o uso de pontos de dados, acesse **Configurações** > **Faturamento** e selecione a guia **Uso total de pontos de dados**.

### Cronograma de atualização de pontos de dados {#data-point-refresh-schedule}

O uso de pontos de dados é armazenado em cache (não em tempo real) a cada 24 horas, por volta das 2h ET. Até que o cache seja atualizado, diferentes usuários do dashboard podem ver os mesmos totais, mesmo que abram a guia em horários diferentes no mesmo dia. Para o mesmo comportamento de cache em outras visualizações de faturamento, consulte [Dashboard de pontos de dados totais]({{site.baseurl}}/user_guide/administer/global/billing#total-data-points-dashboard).

Para saber mais sobre os componentes do dashboard de pontos de dados, consulte [Faturamento]({{site.baseurl}}/user_guide/administer/global/billing).

{% alert tip %}
**Não desperdice pontos de dados. Atualize apenas dados que mudam!**<br><br>
Para minimizar o uso de pontos de dados, recomendamos configurar um programa que evite o envio dos mesmos dados inalterados, passando apenas dados novos e relevantes para a Braze. A Braze trabalhará com você para estabelecer essa prática recomendada durante a integração.
{% endalert %}

## Contagem de consumo {#consumption-count}

Em resumo, os pontos de dados são acumulados quando os dados do perfil de um usuário são atualizados ou quando ele realiza ações específicas. Essencialmente, pontos de dados são contagens de cada `session starts`, `session ends`, `events` e `purchases` dos seus usuários.

Você pode encontrar um detalhamento de como a Braze acumula pontos de dados nas seções a seguir. Se tiver dúvidas sobre as nuances dos pontos de dados da Braze, seu gerente de conta da Braze pode respondê-las.

Para ingestão por API or interface de programação do aplicativo (API), cada atualização faturável por meio de [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) segue as mesmas regras de outras atualizações de perfil: por exemplo, cada **evento personalizado** registrado conta como um ponto de dados, e **atributos personalizados** geralmente contam por atributo atualizado naquela requisição (consulte as tabelas de faturamento na seção a seguir e [Circunstâncias especiais](#special-circumstances)).

As seguintes ações não registram pontos de dados:
- Excluir usuários da Braze
- Usar Connected Content no envio de mensagens
- Alterações no estado de inscrição globalmente e em grupos de inscrições
- Renomear os IDs externos dos seus usuários por meio de [chamadas de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)
- Bloquear eventos, atributos ou propriedades de eventos

### Circunstâncias especiais {#special-circumstances}

#### Arrays {#arrays}

Um array é uma coleção ordenada de itens armazenados em um atributo personalizado. Atualizar um array custa um ponto de dados por chamada de API or interface de programação do aplicativo (API), mesmo que o array não seja realmente alterado. Por exemplo, enviar uma operação `remove` para um valor que não existe no array ainda consome um ponto de dados. Da mesma forma, definir um atributo personalizado como `null` para removê-lo do perfil consome um ponto de dados. Se você adicionar valores a um array de forma incremental, cada valor contará como um ponto de dados.

{% alert tip %}
Para arrays simples, se você definir o array inteiro de uma vez, ele contará como um único ponto de dados. Sendo assim, arrays são uma ótima ferramenta para manter os perfis de usuário atualizados com informações relevantes e reduzir custos. <br><br> Arrays de objetos consomem um ponto de dados para cada chave atualizada. Reduza o consumo desnecessário de pontos de dados enviando apenas atualizações para a Braze.
{% endalert %}

#### Atributos personalizados aninhados {#nested-custom-attributes}

Atributos personalizados aninhados referem-se a um objeto que define um conjunto de atributos como propriedade de outro atributo. Cada chave no objeto contará como um ponto de dados.

{% alert note %}
Atualizar um objeto de atributo personalizado para `null` também consome um ponto de dados.
{% endalert %}

#### CSV

Atributos personalizados enviados por importação de CSV contam para seus pontos de dados. No entanto, importações de CSV para fins de segmentação (importações feitas com `external_id`, `braze_id` ou `user_alias_name` como único campo) não registram pontos de dados.

Além disso, como alterações no estado de inscrição não registram pontos de dados, atualizar os campos `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` no seu arquivo CSV não gerará cobranças.

## Pontos de dados

{% alert note %}
As tabelas a seguir são ilustrativas. Para convenções exatas de nomenclatura, capitalização e valores aceitos para determinados campos, consulte a documentação relevante para o seu método de ingestão.
{% endalert %}

{% tabs %}
{% tab Não faturáveis %}

### Pontos de dados não faturáveis (padrão) {#non-billable-data-points-default}

<div class="small_table"></div>

| Tipo de dados | Ponto de dados |
| --------- | ---------- |
| Dados de perfil | País |
| Dados de perfil | Idioma |
| Dados de perfil | ID do usuário |
| Dados de perfil | Alias de usuário |
| Dispositivos recentes | Número de dispositivos |
| Dispositivos recentes | Relógio mais recente |
| Dispositivos recentes | Versão do app |
| Dispositivos recentes | Dispositivo |
| Dispositivos recentes | SO do dispositivo |
| Configurações de contato | Inscrito para e-mail |
| Configurações de contato | Inscrito para push |
| Configurações de contato | Apps registrados para push |
| Configurações de contato | Grupo de inscrições |
| Campaigns recebidas | Endereço de e-mail |
| Atribuição de instalação | Fonte de instalação |
| Atribuição de instalação | Campaign |
| Atribuição de instalação | Grupo de anúncios |
| Atribuição de instalação | Anúncio |
| Diversos | Número de bucket aleatório |
| Mensagens de Canvas recebidas | Mensagens de Canvas recebidas |
| Engajamento com mensagem | Todos os eventos de engajamento (como aberturas, cliques, impressões e dispensas) |
| Twitter | Seguidores |
| Twitter | Seguindo |
| Twitter | Número de tweets |
| Facebook | Curtidas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pontos de dados não faturáveis (padrão)" }

{% endtab %}
{% tab Faturáveis %}

### Pontos de dados faturáveis {#billable-data-points}

{% alert important %}
Adicionar, remover ou atualizar os seguintes tipos de dados resultará em um ponto de dados faturável.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Tipo de dados | Ponto de dados | Observações |
| --------- | ---------- | ----- |
| Dados de perfil | Nome | |
| Dados de perfil | Sobrenome | |
| Dados de perfil | Endereço de e-mail | |
| Dados de perfil | Gênero | |
| Dados de perfil | Faixa etária | |
| Dados de perfil | País | Quando coletado manualmente. Não é contabilizado no consumo quando coletado automaticamente. |
| Dados de perfil | Cidade | |
| Dados de perfil | Idioma | Quando coletado manualmente. Não é contabilizado no consumo quando coletado automaticamente. |
| Dados de perfil | Localidade mais recente do dispositivo | |
| Dados de perfil | Fuso horário | |
| Dados de perfil | Data de nascimento (DOB) | |
| Dados de perfil | Biografia | |
| Dados de perfil | Número de telefone | |
| Dados de uso do app | Início da sessão | |
| Dados de uso do app | Fim da sessão | |
| Atributos personalizados | Todos os atributos personalizados | |
| Eventos personalizados | Todos os eventos personalizados | |
| Propriedades de eventos personalizados | Todas as propriedades de eventos personalizados | Propriedades de eventos personalizados habilitadas para segmentação com os filtros `X Custom Event Property in Y Days` ou `X Purchase Property in Y Days` são contabilizadas como pontos de dados separados, além do ponto de dados contabilizado pelo próprio evento personalizado. |
| Compras | Todas as compras | |
| Propriedades de compra | Todas as propriedades de compra | |
| Atribuição de coorte do Amplitude | Todas as atribuições | |
| Atribuição de coorte do Mixpanel | Todas as atribuições | |
| Atribuição de coorte do Hightouch | Todas as atribuições | |
| Atribuição de coorte do Appsflyer | Todas as atribuições | |
| Localização mais recente | Todas as localizações mais recentes | Entrar ou sair de geofences não registra pontos de dados porque os dados de geofence não são armazenados no perfil do usuário. As geofences são monitoradas pelos serviços de localização da Apple e do Google; a Braze só é notificada quando um usuário aciona uma geofence. |
| Twitter | Nome de usuário | |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pontos de dados faturáveis" }

{% endtab %}
{% endtabs %}