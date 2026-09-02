---
nav_title: Outgrow
article_title: Outgrow
alias: /partners/outgrow/
description: "Este artigo fornece um guia abrangente sobre a configuração de uma integração nativa entre o Outgrow e a Braze para sincronização aprimorada de dados de usuários e campanhas personalizadas."
page_type: partner
search_tag: Partner
---

# Outgrow

> A [Outgrow](https://outgrow.co/) é uma plataforma de conteúdo interativo que permite criar questionários, calculadoras, pesquisas e outros tipos de conteúdo envolvente para coletar dados e insights de usuários. A integração da Braze com o Outgrow permite transferir automaticamente os dados de usuários do Outgrow para a Braze, possibilitando campanhas altamente personalizadas e direcionadas.

Quando você usa a integração da Braze com o Outgrow para conteúdo interativo, os benefícios incluem:

- **Personalização aprimorada**: Colete dados de questionários, pesquisas e calculadoras do Outgrow que podem ser mapeados para atributos personalizados na Braze. Esses dados permitem uma segmentação precisa e campanhas personalizadas.
- **Sincronização de dados em tempo real**: Receba os dados do Outgrow na Braze em tempo real, permitindo que você aja imediatamente com base nos insights dos usuários. Isso possibilita acompanhamentos oportunos ou mensagens personalizadas com base nas interações mais recentes dos usuários.
- **Gerenciamento de dados simplificado**: Automatize a transferência de dados entre o Outgrow e a Braze, eliminando exportações e importações manuais de dados, reduzindo discrepâncias e economizando tempo.
- **Melhoria da experiência do usuário**: Aproveite os insights dos usuários para criar experiências mais relevantes, levando a maior satisfação, retenção e valor do tempo de vida.
- **Direcionamento e segmentação flexíveis**: Refine a segmentação na Braze usando os dados do Outgrow, permitindo direcionar usuários com base em interações específicas (como pontuações de questionários ou respostas a pesquisas) para criar campanhas que repercutam entre seus usuários.

## Pré-requisitos {#prerequisites}

Antes de configurar a integração do Outgrow com a Braze, confirme que você tem o seguinte:

| Requisito | Descrição |
|-------------|-------------|
| **Conta Outgrow** | Uma conta Outgrow registrada para configurar e gerenciar o conteúdo interativo e as configurações de transferência de dados |
| **Conta Braze** | Uma conta Braze com acesso às credenciais da REST or transferir estado representacional API or interface de programação do aplicativo (API) |
| **Chave de API or interface de programação do aplicativo (API)** | Uma chave de API or interface de programação do aplicativo (API) da Braze com a permissão `users.track` para ativar a transferência de dados de usuários |
| **Atributos personalizados na Braze** | Atributos personalizados configurados na Braze para capturar respostas do Outgrow (como pontuações de questionários, segmentos e outros) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Siga estas etapas para configurar a integração da Braze com o Outgrow:

### Etapa 1: Gerar a chave de API or interface de programação do aplicativo (API) da Braze {#step-1-generate-braze-api-key}

1. Na sua conta Braze, acesse **Console de desenvolvedor** > **Configurações de API or interface de programação do aplicativo (API)**.
2. Selecione **Create New API or interface de programação do aplicativo (API) Key**.
3. Dê um nome à sua chave de API or interface de programação do aplicativo (API), ative a permissão `users.track` e salve a chave de API or interface de programação do aplicativo (API).

### Etapa 2: Configurar a integração da Braze no Outgrow {#step-2-configure-the-braze-integration-in-outgrow}

1. Faça login na sua conta do Outgrow.
2. No dashboard, acesse **Integrations**.
3. Na lista de integrações disponíveis, selecione **Braze**.
4. Insira sua **Braze API or interface de programação do aplicativo (API) Key** e a **REST or transferir estado representacional API or interface de programação do aplicativo (API) Endpoint URL**:
   - **API or interface de programação do aplicativo (API) Key**: Insira a chave de API or interface de programação do aplicativo (API) que foi gerada na Braze
   - **REST or transferir estado representacional Endpoint URL**: Insira o endpoint da sua instância da Braze (por exemplo, `https://rest.iad-01.braze.com`)
5. Selecione **Save** para ativar a integração.

### Etapa 3: Mapear dados do Outgrow para atributos da Braze {#step-3-map-outgrow-data-to-braze-attributes}

No Outgrow, você pode mapear respostas de conteúdo interativo (como resultados de questionários, segmentos personalizados ou pontuações de engajamento) para atributos personalizados da Braze.

1. Nas **Integration Settings** do Outgrow para a Braze, defina quais respostas do Outgrow devem ser mapeadas para atributos da Braze.
2. Certifique-se de que cada resposta selecionada esteja alinhada com um atributo personalizado na Braze. Por exemplo:
   - A pontuação do questionário é mapeada para `outgrow_quiz_score`.
   - O Segment or segmento or segmento personalizado é mapeado para `outgrow_custom_segment`.
3. Salve suas configurações de mapeamento.

### Etapa 4: Testar a integração {#step-4-test-the-integration}

Depois de configurar a integração, execute um teste para confirmar se os dados estão sendo transferidos corretamente do Outgrow para a Braze.

1. Publique uma experiência do Outgrow (como um questionário ou uma calculadora) e conclua-a como um usuário teste.
2. Na sua conta Braze, acesse a seção **Perfil de usuário** e verifique se há atributos atualizados (como `outgrow_quiz_score` ou `outgrow_custom_segment`).
3. Verifique se os dados estão preenchidos corretamente nos atributos personalizados apropriados.

## Uso de dados do Outgrow na Braze para segmentação e direcionamento {#using-outgrow-data-in-braze-for-segmentation-and-targeting}

### Criação de segmentos na Braze com dados do Outgrow {#creating-segments-in-braze-with-outgrow-data}

Com a integração, você pode criar segmentos na Braze com base em atributos personalizados preenchidos a partir das respostas do Outgrow.

1. Na Braze, acesse **Engajamento** > **Segments** e selecione **Create New Segment or segmento**.
2. Dê um nome ao seu Segment or segmento or segmento e defina filtros com base nos dados do Outgrow. Por exemplo:
   - Filtre por `outgrow_quiz_score` para direcionar os usuários que pontuaram acima de um determinado limite.
   - Filtre por `outgrow_custom_segment` para direcionar os usuários que pertencem a um determinado Segment or segmento or segmento definido pelo Outgrow.
3. Salve seu Segment or segmento or segmento para uso em Campaigns e Canvas.

### Lançamento de Campaigns com segmentos definidos pelo Outgrow {#launching-campaigns-with-outgrow-defined-segments}

Você pode usar os segmentos personalizados criados a partir dos dados do Outgrow para personalizar suas Campaigns na Braze e direcionar os usuários com base em suas respostas ao conteúdo interativo. Para fazer isso e criar uma experiência de usuário mais personalizada, siga estas etapas:

1. Na Braze, acesse **Engajamento** > **Campaigns**.
2. Selecione **Create Campaign** e escolha o tipo de Campaign (e-mail, push, mensagem no app ou outros).
3. Na etapa de direcionamento do público, selecione o Segment or segmento or segmento criado a partir dos atributos do Outgrow (como usuários com pontuações de questionário ou segmentos específicos).
4. Personalize o conteúdo e as configurações da sua Campaign e, em seguida, lance-a.

## Solução de problemas comuns {#troubleshooting-common-issues}

| Problema | Solução |
|-------|----------|
| **Os dados não estão sendo transferidos para a Braze** | Verifique se a chave de API or interface de programação do aplicativo (API) e a URL do endpoint estão corretas nas configurações de integração do Outgrow. Certifique-se de que a chave de API or interface de programação do aplicativo (API) tenha a permissão `users.track` ativada. |
| **Mapeamento incorreto de dados** | Certifique-se de que cada resposta do Outgrow mapeada corresponda a um atributo personalizado válido na Braze e que os nomes dos atributos correspondam exatamente. |
| **O Segment or segmento or segmento não está sendo filtrado corretamente** | Certifique-se de que os atributos personalizados na Braze estejam configurados corretamente e recebendo dados. Verifique novamente a lógica do filtro do Segment or segmento or segmento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas comuns" }

## Considerações adicionais {#additional-considerations}

- **Privacidade de dados**: Cumpra as normas de privacidade de dados (como GDPR e CCPA) ao transferir dados de usuários entre plataformas.
- **Limites de frequência**: Os dados do Outgrow são enviados para a Braze em tempo real, mas os limites de frequência da API or interface de programação do aplicativo (API) da Braze podem se aplicar a grandes volumes de dados. Planeje adequadamente para experiências de alto tráfego.
- **Configuração de atributos personalizados**: Verifique se os atributos personalizados da Braze usados nessa integração estão configurados corretamente para capturar os dados enviados pelo Outgrow.

Para obter assistência adicional, consulte a [documentação do Outgrow](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) ou entre em contato com o Suporte do Outgrow.