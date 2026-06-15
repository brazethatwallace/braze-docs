---
nav_title: mParticle por Rokt
article_title: mParticle por Rokt
alias: /partners/mparticle/
description: "Este artigo de referência descreve a parceria entre a Braze e a mParticle, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
search_tag: Partner

---

# mParticle por Rokt {#mparticle-by-rokt}

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> A plataforma de dados do cliente da mParticle ajuda você a fazer mais com os seus dados. Os melhores profissionais de marketing usam a mParticle para orquestrar dados em todo o growth stack, para vencer nos momentos mais importantes da jornada do cliente.

A integração entre a Braze e a mParticle permite que você controle com praticidade o fluxo de informações entre os dois sistemas:
- Sincronize os públicos da mParticle com a Braze para segmentação de Campaign e Canvas na Braze.
- Compartilhe dados entre as duas plataformas. Isso pode ser feito por meio da integração do kit mParticle e da integração de servidor a servidor.
- [Envie a interação do usuário da Braze para a mParticle por meio do Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), tornando-a acionável em todo o growth stack.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta mParticle | É necessário ter uma [conta mParticle](https://app.mparticle.com/login) para usar essa parceria. |
| Instância da Braze | Sua instância da Braze pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints) (por exemplo, `US-01` ou `US-02`). |
| Chave do identificador do app Braze | A chave do identificador do seu app. <br><br>Ela pode ser encontrada em **Gerenciar configurações** > **Chave de API** no dashboard da Braze. |
| Chave da API REST do espaço de trabalho | (Servidor a servidor) Uma chave da API REST da Braze<br><br>Ela pode ser criada em **Console de desenvolvedor** > **Configurações da API** > **Chave de API** no dashboard da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Públicos {#audiences}

Use a parceria entre a Braze e a mParticle para configurar sua integração e importar públicos da mParticle diretamente para a Braze para redirecionamento, criando um ciclo completo de dados de um sistema para outro.

Qualquer integração que você configurar registrará pontos de dados. Se tiver dúvidas sobre as nuances dos pontos de dados da Braze, seu gerente de conta da Braze pode esclarecê-las.

#### Encaminhamento de públicos {#forwarding-audiences}

A mParticle oferece três maneiras de definir atributos de associação a coortes, controladas pela configuração "[Enviar segmentos como](#send_settings)". Consulte as seções a seguir para o processamento de cada opção:

- [Atributo de string único](#string)
- [Atributo de array único](#array)
- [Um atributo por segmento](#per-segment)
- [Atributo de array único e atributo de string único](#both-1)
- [Atributo de array único e um atributo por segmento](#both-2)
- [Atributo de string único e um atributo por segmento](#both-3)
- [Atributo de array único, atributo de string único e um atributo por segmento](#multi)

##### Atributo de string único {#string}

A mParticle criará um único atributo personalizado chamado `SegmentMembership`. O valor desse atributo é uma string de IDs de público da mParticle separados por vírgula que correspondem ao usuário. Esses IDs de público podem ser encontrados no dashboard da mParticle em **Audiences**.

Por exemplo, se um público da mParticle "Ibiza dreamers" tiver um ID de público "11036", você pode segmentar esses usuários com o filtro `SegmentMembership` — `matches regex` — `11036`.

Embora essa seja a opção padrão na mParticle, a maioria dos usuários da empresa opta por usar [atributos de array único](#array) para a experiência de filtragem ao criar segmentos na Braze.

{% alert important %}
Essa solução não é recomendada se você tiver mais do que alguns públicos, pois os atributos personalizados podem ter até 255 caracteres. Portanto, não será possível armazenar dezenas ou centenas de públicos em um perfil de usuário usando esse método. Se você tiver um grande número de coortes por usuário, recomendamos fortemente a configuração "um atributo por segmento".
{% endalert %}

![Associação a segmento da mParticle]({% image_buster /assets/img_archive/mparticle1.png %})

##### Atributo de array único {#array}

A mParticle cria um único atributo de array personalizado na Braze para cada usuário, chamado `SegmentMembershipArray`. O valor desse atributo é um array de IDs de público da mParticle que correspondem ao usuário.

Por exemplo, se um usuário for membro de três públicos da mParticle com os IDs de público "13053", "13052" e "13051", você pode segmentar os usuários que correspondem a um desses públicos com o filtro `SegmentMembershipArray` — `includes value` — `13051`.

{% alert note %}
Os atributos de array da Braze têm um comprimento máximo padrão de 500. Se algum dos seus usuários for membro de mais de 500 públicos, a Braze truncará as informações de associação. Para uma solução alternativa, entre em contato com seu gerente de conta da Braze para aumentar o limite máximo de comprimento do array.
{% endalert %}

##### Um atributo por segmento {#per-segment}

A mParticle criará um atributo personalizado booleano para cada público ao qual um usuário pertence. Por exemplo, se um público da mParticle se chamar "Possible Parisians", você pode segmentar esses usuários com o filtro `In Possible Parisians` - `equals` - `true`.

![Atributo personalizado da mParticle]({% image_buster /assets/img_archive/mparticle2.png %})

##### Atributo de array único e atributo de string único {#both-1}

A mParticle enviará atributos conforme descrito tanto pelo atributo de array único quanto pelo atributo de string único.

##### Atributo de array único e um atributo por segmento {#both-2}

A mParticle enviará atributos conforme descrito tanto pelo atributo de array único quanto por um atributo por segmento.

##### Atributo de string único e um atributo por segmento {#both-3}

A mParticle enviará atributos conforme descrito tanto pelo atributo de string único quanto por um atributo por segmento.

##### Atributo de array único, atributo de string único e um atributo por segmento {#multi}

A mParticle enviará atributos conforme descrito pelo atributo de array único, atributo de string único e um atributo por segmento.

#### Etapa 1: Crie um público na mParticle {#send_settings}

Para criar um público na mParticle:

1. Navegue até **Audiences** > **Single Workspace** > **+ New Audience**.
2. Para conectar a Braze como uma saída para o seu público, você deve fornecer os seguintes campos:

| Nome do campo | Descrição |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chave de API | No dashboard da Braze, acesse **Settings** > **API Keys**. |
| Sistema operacional da chave de API | Selecione a qual sistema operacional sua chave de API da Braze corresponde. Essa seleção limitará os tipos de tokens por push encaminhados em uma atualização de público. |
| Enviar segmentos como | O método de envio de públicos para a Braze. Consulte a seção [Encaminhamento de públicos](#forwarding-audiences) para mais detalhes. |
| Chave da API REST do espaço de trabalho | Chave da API REST da Braze com permissões completas. Ela pode ser criada no dashboard da Braze em **Settings** > **API Keys**. |
| Tipo de identidade externa | O tipo de identidade de usuário da mParticle a ser encaminhado como ID externo para a Braze. Recomendamos manter o valor padrão, Customer ID. |
| Tipo de identidade de e-mail | O tipo de identidade de usuário da mParticle a ser encaminhado como e-mail para a Braze. |
| Instância da Braze | Especifique para qual cluster seus dados da Braze serão encaminhados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Crie um público na mParticle" }

{:start="3"}
3. Por fim, **salve** seu público.

Você deve começar a ver os públicos sincronizando com a Braze em poucos minutos. A associação ao público será atualizada apenas para usuários com `external_ids` (ou seja, não para usuários anônimos). Para saber mais sobre como criar públicos da mParticle na Braze, consulte a documentação da mParticle sobre [Configurações](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Etapa 2: Segmente usuários na Braze {#step-2-segment-users-in-braze}

Na Braze, para criar um segmento desses usuários, navegue até **Segments** em **Engagement** e nomeie seu segmento. A seguir estão dois exemplos de segmentos dependendo da opção que você selecionou para **Send segments as**. Para mais detalhes sobre cada opção, consulte [Encaminhamento de públicos](#forwarding-audiences).

- **Atributo de array único:** Selecione `SegmentMembershipArray` como seu filtro. Em seguida, use a opção "includes value" e insira o ID de público desejado. ![Filtro de segmento da mParticle "SegmentMembershipArray" definido como "includes value" e ID de público.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Um atributo por segmento:** Selecione seu atributo personalizado como filtro. Em seguida, use a opção "equals" e escolha a lógica apropriada. ![Filtro de segmento da mParticle "in possible parisians" definido como "equals" e "true".]({% image_buster /assets/img_archive/mparticle3.png %})

Depois de salvo, você pode referenciar esse segmento durante a criação de Canvas ou Campaign na etapa de direcionamento de usuários.

#### Desativando e excluindo conexões {#deactivating-and-deleting-connections}

Como a mParticle não mantém segmentos diretamente na Braze, ela não excluirá segmentos quando a conexão de público correspondente da mParticle for excluída ou desativada. Quando isso acontecer, a mParticle não atualizará os atributos de usuário do público na Braze para remover o público de cada usuário.

Para remover o público de um usuário da Braze antes da exclusão, ajuste os filtros de público para forçar o tamanho do público a 0 antes de excluir um público. Após o cálculo do público ser concluído e retornar 0 usuários, exclua o público. Então, a associação ao público será atualizada na Braze para `false` para a opção de atributo único ou removerá o ID de público do formato de array.

## Mapeamento de dados {#data-mapping}

Os dados podem ser mapeados para a Braze usando a [integração de kit incorporado](#embedded-kit-integration) se você quiser conectar seus apps móveis e web à Braze por meio da mParticle. Você também pode usar a [integração de API servidor a servidor](#server-api-integration) para encaminhar dados do lado do servidor para a Braze.

Independentemente da abordagem escolhida, você deve configurar a Braze como uma saída:

### Configure as configurações de saída da Braze {#configure-your-braze-output-settings}

Na mParticle, navegue até **Setup > Outputs > Add Outputs** e selecione **Braze** para abrir a configuração do kit Braze. **Salve** quando concluído.

| Nome da configuração | Descrição |
| ------------ | ----------- |
| Chave do identificador do app Braze | A chave do identificador do seu app Braze pode ser encontrada no dashboard da Braze em **Settings** > **API Keys**. Observe que as chaves de API serão diferentes para cada plataforma (iOS, Android e Web). |
| Tipo de identidade externa | O tipo de identidade de usuário da mParticle a ser encaminhado como ID externo para a Braze. Recomendamos manter o valor padrão, Customer ID. |
| Tipo de identidade de e-mail | O tipo de identidade de usuário da mParticle a ser encaminhado como e-mail para a Braze. Recomendamos manter o valor padrão, Email. |
| Instância da Braze | O cluster para o qual seus dados da Braze serão encaminhados; deve ser o mesmo cluster do seu dashboard. |
| Ativar encaminhamento de fluxo de eventos | (Servidor a servidor) Quando ativado, todos os eventos serão encaminhados em tempo real. Caso contrário, todos os eventos serão encaminhados em lote. Ao optar por ativar o encaminhamento de fluxo de eventos, certifique-se de que os dados que você está enviando para a Braze respeitarão os [limites de taxa]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configure as configurações de saída da Braze" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Integração de kit incorporado {#embedded-kit-integration}

O SDK da mParticle e o SDK da Braze estarão presentes no seu aplicativo por meio da integração de kit incorporado. No entanto, diferentemente de uma integração direta com a Braze, a mParticle cuida de chamar a maioria dos métodos do SDK da Braze para você. Os métodos da mParticle que você usa para rastrear dados de usuários serão automaticamente mapeados para os métodos do SDK da Braze.

Esses mapeamentos do SDK da mParticle para [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) e [Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) são de código aberto e podem ser encontrados na [página do GitHub da mParticle](https://github.com/mparticle-integrations).

A integração de SDK de kit incorporado permite que você aproveite nosso conjunto completo de recursos (push, mensagens no app e todo o rastreamento de análise de dados de mensagens relevante).

{% alert note %}
Para integrações de Content Cards e mensagens no app personalizadas, chame os métodos do SDK da Braze diretamente.
{% endalert %}

#### Etapa 1: Integre os SDKs da mParticle {#step-1-integrate-the-mparticle-sdks}

Integre os SDKs apropriados da mParticle no seu app com base nas necessidades da sua plataforma:

* [mParticle para Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle para iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle para Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Etapa 2: Conclua a integração do kit de eventos Braze da mParticle {#step-2-complete-mparticles-braze-event-kit-integration}

Embora o SDK da Braze não precise ser incluído diretamente no seu site ou app para essa integração com a mParticle, o seguinte Kit Appboy da mParticle deve ser instalado para encaminhar dados do seu app para a Braze.

O [guia de integração do kit de eventos Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) da mParticle orientará você sobre instruções personalizadas de alinhamento entre mParticle e Braze com base nas suas necessidades de envio de mensagens (Push, monitoramento de localização, etc.).

#### Etapa 3: Configurações de conexão para sua saída Braze {#step-3-connections-settings-for-your-braze-output}

Na mParticle, navegue até **Connections** > **Connect** > **[Sua plataforma desejada]** > **Connect Output** para adicionar a Braze como uma saída. Em seguida, selecione **Save**.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Nem todas as configurações de conexão se aplicam a todas as plataformas e tipos de integração. Para uma análise das configurações de conexão e das plataformas às quais se aplicam, consulte a [documentação da mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Integração de API servidor a servidor {#server-api-integration}

Este é um complemento para encaminhar seus dados de backend para a Braze se você estiver usando os SDKs do lado do servidor da mParticle (por exemplo, Ruby, Python, etc.). Para configurar essa integração servidor a servidor com a Braze, siga a [documentação da mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
A integração servidor a servidor não oferece suporte a recursos de interface da Braze, como mensagens no app, Content Cards ou notificações por push. Também existem dados capturados automaticamente, como campos no nível do dispositivo, que não estão disponíveis por esse método.

Considere uma integração lado a lado se desejar usar esses recursos.

Para que os dados do lado do servidor sejam encaminhados para a Braze, eles devem incluir um `external_id`; usuários anônimos não serão encaminhados.
{% endalert %}

#### Configurações de conexão para sua saída Braze {#connections-settings-for-your-braze-output}

Na mParticle, navegue até **Connections > Connect > [Sua plataforma desejada] > Connect Output** para adicionar a Braze como uma saída. **Salve** quando concluído.

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

Nem todas as configurações de conexão se aplicam a todas as plataformas e tipos de integração. Para uma análise das configurações de conexão e das plataformas às quais se aplicam, consulte a [documentação da mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Antes de ativar "Enriched User Attributes" ou "Enriched User Identities", recomendamos revisar [Possíveis excedentes de pontos de dados](#potential-data-point-overages) para garantir que você esteja ciente de como essas configurações afetarão o uso de pontos de dados.

### Detalhes do mapeamento de dados {#data-mapping-details}

#### Tipos de dados {#data-types}
Nem todos os tipos de dados são suportados entre ambas as plataformas.
- [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) suportam objetos de string, numéricos, booleanos ou de data. Não suportam arrays ou objetos aninhados.
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) suportam objetos de string, numéricos, booleanos, de data e arrays, mas não suportam objetos ou objetos aninhados.

{% alert note %}
A Braze não suporta timestamps anteriores ao ano 0 ou posteriores ao ano 3000 em atributos personalizados do tipo `Time`. A Braze ingerirá esses valores quando forem enviados pela mParticle, mas o valor será armazenado como uma string.
{% endalert %}

#### Mapeamento de dados

| Tipo de dado mParticle | Tipo de dado Braze | Descrição |
| ------------------- | --------------- | ----------- |
| Atributos de usuário (reservados) | Atributo padrão | Por exemplo, a chave de atributo de usuário reservada `$FirstName` da mParticle é mapeada para o campo de atributo padrão `first_name` da Braze. |
| Atributos de usuário (outros) | Atributo personalizado | Quaisquer atributos de usuário passados para a mParticle que estejam fora de suas chaves de atributo de usuário reservadas são registrados na Braze como um atributo personalizado.<br><br>Atributos de usuário suportam string, numéricos, booleanos, data e arrays, mas não suportam objetos ou objetos aninhados. |
| Evento personalizado | Evento personalizado | Eventos personalizados da mParticle são reconhecidos pela Braze como um evento personalizado. Atributos de evento são encaminhados como propriedades de evento personalizado.<br><br>Atributos de evento passados para a Braze como propriedades de evento suportam objetos de string, numéricos, booleanos ou de data, mas não suportam arrays ou objetos aninhados. |
| Evento de comércio de compra | Evento de compra | Eventos de comércio de compra serão mapeados para eventos de compra da Braze. <br><br>Alterne o valor da configuração para agrupar dados de eventos de comércio para registrar compras no nível do pedido ou do produto. Por exemplo, se `false`, um único evento de entrada com dois produtos, promoções ou impressões únicos resultaria em pelo menos dois eventos de saída da Braze. Se definido como `true`, resultaria em um único evento de saída com um array aninhado de produtos, promoções ou impressões, respectivamente.<br><br>Para saber mais sobre os campos de comércio adicionais que serão registrados, consulte a [documentação da mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Ao definir "bundle commerce event data" como `false`, atributos de produto passados para a Braze como propriedades de evento de compra suportam objetos de string, numéricos, booleanos ou de data, mas não suportam arrays ou objetos aninhados.|
| Todos os outros eventos de comércio | Evento personalizado | Todos os outros eventos de comércio serão mapeados para eventos personalizados. <br><br>Alterne o valor da configuração para agrupar dados de eventos de comércio para registrar compras no nível do pedido ou do produto. Por exemplo, se `false`, um único evento de entrada com dois produtos, promoções ou impressões únicos resultaria em pelo menos dois eventos de saída da Braze. Se definido como `true`, resultaria em um único evento de saída com um array aninhado de produtos, promoções ou impressões, respectivamente.<br><br>Além de certos valores de comércio padrão, atributos de produto serão registrados como propriedades de evento da Braze. Para saber mais sobre os campos de comércio adicionais que serão registrados, consulte a [documentação da mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Ao definir "bundle commerce event data" como `false`, atributos de produto passados para a Braze como propriedades de evento suportam objetos de string, numéricos, booleanos ou de data, mas não suportam arrays ou objetos aninhados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mapeamento de dados" }

#### Mapeamento de identidade de usuário {#user-identity-mapping}
Para cada saída da mParticle, você pode selecionar o tipo de identidade externa a ser enviado para a Braze como o `external_id`. Embora o valor padrão seja customer ID, você pode optar por mapear outro ID, como `MPID`, para enviar para a Braze como o `external_id`. Esteja ciente de que escolher um identificador diferente do customer ID pode influenciar como os dados são enviados na Braze.

Por exemplo, mapear MPID para o `external_id` da Braze terá os seguintes efeitos:
- Devido à natureza de quando o MPID é atribuído, todos os usuários receberão um `external_id` no início da sessão.
- A configuração do Currents pode exigir mapeamento adicional devido a tipos de dados diferentes entre MPID e `external_id`.

### Encaminhamento de solicitações de exclusão (solicitações de titulares de dados) {#forwarding-erasure-requests-data-subject-requests}

Encaminhe solicitações de exclusão para a Braze configurando uma saída de solicitação de titular de dados para a Braze. Para encaminhar solicitações de exclusão para a Braze, siga a [documentação da mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Possíveis excedentes de pontos de dados {#potential-data-point-overages}

### Atributos de usuário enriquecidos {#enriched-user-attributes}

#### Ativando atributos/identidades de usuário enriquecidos (somente servidor a servidor) {#enriched}

Nas configurações de conexão da mParticle, a Braze recomenda desativar **Include Enriched User Attributes**. Se ativado, a mParticle encaminhará todos os atributos de usuário disponíveis (como atributos padrão, atributos personalizados e atributos calculados) do perfil existente para a Braze em cada evento registrado. Isso resulta em alto consumo de pontos de dados porque a mParticle envia para a Braze os mesmos atributos inalterados em cada chamada.

Por exemplo, se um usuário adicionar seu nome, sobrenome e número de telefone durante sua primeira sessão e depois se inscrever em uma newsletter adicionando as mesmas informações e um e-mail, disparando um evento de inscrição na newsletter:
- Se ativado (padrão), cinco pontos de dados serão incorridos. (evento de inscrição, endereço de e-mail, nome, sobrenome e número de telefone)
- Se desativado, dois pontos de dados serão incorridos (evento de inscrição e endereço de e-mail)

{% alert note %}
Desativar essa configuração não verificará dados em alteração. No entanto, impedirá que a integração envie todos os atributos de usuário no perfil do usuário que não foram recebidos no lote de entrada original ou definidos explicitamente como um atributo para o evento. Ainda é importante verificar se apenas deltas estão sendo passados para a Braze.
{% endalert %}

#### Considerações ao desativar atributos de usuário enriquecidos {#considerations-of-turning-off-enriched-user-attributes}

Existem algumas considerações ao desativar **Include Enriched User Attributes**:
1. A integração servidor a servidor usa a API de eventos da mParticle para enviar eventos para a Braze. Cada solicitação é disparada por um evento. Quando um atributo de usuário é alterado, como a atualização de um endereço de e-mail, mas não está associado a um evento específico (por exemplo, um evento personalizado de atualização de perfil), o novo valor só é passado para uma saída como a Braze como um "atributo enriquecido" na carga útil do próximo evento disparado pelo usuário. Quando **Include Enriched User Attributes** está desativado, esse novo valor de atributo não associado a um evento específico não será passado para a Braze.
  - Para resolver isso, recomendamos criar um evento separado de "atributo de usuário atualizado" que envie apenas o(s) atributo(s) de usuário específico(s) que foram atualizados para a Braze. Observe que, com essa abordagem, você ainda estará registrando um ponto de dados adicional para o evento "atributo de usuário atualizado", mas o uso de pontos de dados será muito menor do que enviar todos os atributos de usuário em cada chamada com o recurso ativado.
2. Atributos calculados são passados para a Braze como um atributo de usuário enriquecido, então quando "Enriched User Attributes" está desativado, eles não serão mais passados para a Braze. Para encaminhar atributos calculados para a Braze quando "Enriched User Attributes" estiver desativado, um [feed de atributos calculados](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) pode ajudar sem enviar todos os atributos. O feed disparará uma atualização downstream para a Braze quando um atributo calculado mudar.

## Solução de problemas {#troubleshooting}

### Solução de problemas de notificações por push no iOS com o kit de eventos Braze {#troubleshooting-ios-push-notifications-with-the-braze-event-kit}

Se as notificações por push não estiverem funcionando ao usar o kit de eventos Braze (integração de kit incorporado) no iOS, verifique o seguinte:
1. **Encaminhamento de token por push:** Confirme que a mParticle está encaminhando tokens por push para a Braze. No dashboard da mParticle, verifique se a conexão do kit Braze tem push ativado e se a credencial correta de push da Apple está configurada no dashboard da Braze.
2. **Ordem de inicialização do kit:** O kit Braze deve ser inicializado antes que seu app solicite permissões de push. Se as permissões de push forem solicitadas antes que o kit esteja ativo, o token por push pode não ser encaminhado para a Braze. Verifique se o SDK da mParticle é iniciado no início do ciclo de vida do seu app.
3. **Method swizzling:** O kit Apple da mParticle usa method swizzling para encaminhar automaticamente tokens por push e lidar com eventos de notificação por push. Se você desativou o swizzling ou outro SDK está interferindo, os tokens por push podem não chegar à Braze. Verifique se o swizzling está ativado na sua configuração da mParticle.
4. **Tratamento manual de token:** Se você gerencia tokens por push manualmente (por exemplo, implementando `application:didRegisterForRemoteNotificationsWithDeviceToken:`), certifique-se de que está passando o token para a mParticle atribuindo-o à propriedade de token de notificação por push, por exemplo: `MParticle.sharedInstance().pushNotificationToken = deviceToken`. O kit então o encaminhará para a Braze.
5. **Incompatibilidade de ambiente:** Confirme que o ambiente da credencial APNs (desenvolvimento vs. produção) corresponde ao build do seu app. Para mais detalhes, consulte [Solução de problemas de push no iOS]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift).
6. **Timing de inicialização do kit:** Se você acessa a instância da Braze a partir de `didFinishLaunchingWithOptions`, o kit da mParticle pode não estar pronto quando um push chega. Inicialize o tratamento de push em [`userNotificationCenter(_:didReceive:withCompletionHandler:)`]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) (ou o delegate de resposta de notificação equivalente) para que o kit Braze esteja ativo quando o usuário abrir uma notificação.

### Envio de dados desnecessários ou duplicados para a Braze {#sending-unnecessary-or-duplicate-data-to-braze}
A Braze conta um ponto de dados cada vez que um atributo é passado para a Braze, mesmo que o valor não tenha mudado. Por esse motivo, a Braze recomenda encaminhar apenas os dados necessários para ações dentro da Braze e garantir que apenas deltas de atributos estejam sendo passados.