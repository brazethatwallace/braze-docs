---
nav_title: NiftyImages
article_title: NiftyImages
description: "Saiba como conectar a NiftyImages à Braze para criar visuais dinâmicos e personalizados, sincronizar propriedades de contato e publicar ativos como Content Blocks reutilizáveis."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> A [NiftyImages](https://niftyimages.com) ajuda os clientes da Braze a criar conteúdo visual personalizado e em tempo real para e-mail, dispositivos móveis e envio de mensagens no app. Ao conectar dados de clientes, produtos e negócios a imagens e conteúdos dinâmicos, as marcas podem oferecer experiências oportunas e relevantes, como temporizadores de contagem regressiva, recomendações personalizadas, mensagens localizadas, atualizações de estoque e ofertas promocionais que impulsionam o engajamento e as conversões.

_Esta integração é mantida pela NiftyImages._

## Sobre a integração {#about-the-integration}

A integração da NiftyImages com a Braze ajuda você a criar visuais dinâmicos e personalizados usando dados de contato da Braze. As equipes podem criar ativos como imagens personalizadas, temporizadores de contagem regressiva, mapas, calendários, visuais de fidelidade e muito mais, e depois publicá-los como [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) reutilizáveis na Braze para uso em Campaigns e Canvas. Isso economiza tempo, reduz erros e simplifica o gerenciamento de conteúdo personalizado.

## Casos de uso {#use-cases}

Você pode usar a NiftyImages para:

- **Personalizar imagens:** crie imagens que incluam o nome de cada cliente, status de fidelidade, saldo de recompensas, localização, preferência de produto, nível de associação, detalhes da conta ou outras propriedades de contato da Braze.
- **Adicionar temporizadores de contagem regressiva:** adicione temporizadores de contagem regressiva em tempo real para promoções, lançamentos de produtos, eventos, ofertas por tempo limitado, compromissos, prazos de integração e datas de expiração personalizadas.
- **Exibir mapas dinâmicos:** mostre a loja mais próxima, local do evento, área de atendimento, revendedor, clube, filial ou ponto de retirada com base nos dados de localização do cliente ou nas propriedades de contato da Braze.
- **Exibir calendários:** exiba datas personalizadas, eventos, compromissos, períodos de renovação, momentos de campanha ou marcos do cliente diretamente nos visuais da campanha.
- **Realizar enquetes ao vivo:** adicione enquetes interativas às campanhas e exiba resultados atualizados em tempo real após os clientes votarem.
- **Criar raspadinhas:** crie experiências gamificadas de raspadinha que revelam uma recompensa, desconto, oferta, imagem ou mensagem personalizada.
- **Visualizar dados de fidelidade:** transforme dados de clientes em barras de progresso, resumos de conta, visuais de fidelidade, gráficos e tabelas personalizados para cada destinatário.
- **Aplicar conteúdo baseado em regras:** exiba visuais diferentes com base em horário, localização, dispositivo, dados do cliente, segmento de público ou lógica de campanha.
- **Reutilizar conteúdo dinâmico:** publique ativos finalizados da NiftyImages em Content Blocks da Braze para que as equipes possam reutilizá-los em e-mails de marketing, modelos, Campaigns e ativos de marca compartilhados.

## Pré-requisitos {#prerequisites}

Antes de começar, confirme que você tem o seguinte:

| Requisitos | Descrição |
| ---------- | --------- |
| Conta NiftyImages | Uma [conta NiftyImages](https://niftyimages.com/Signup) é necessária para criar e gerenciar imagens personalizadas, temporizadores, mapas, calendários, raspadinhas, gráficos e outros visuais dinâmicos. |
| Conta Braze | Uma conta Braze é necessária para usar a NiftyImages em Campaigns, Canvas, modelos de e-mail e canais de envio de mensagens da Braze. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `custom_attributes.get` e `content_blocks.create`.<br><br>Ela pode ser criada no dashboard da Braze em **Configurações** > **APIs e identificadores**. |
| Endpoint REST da Braze | [A URL do seu endpoint REST]({{site.baseurl}}/api/basics#endpoints). Seu endpoint depende da URL da Braze para a sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Conecte sua conta Braze na NiftyImages para sincronizar propriedades de contato e publicar ativos em Content Blocks da Braze.

### Etapa 1: Abrir integrações na NiftyImages {#step-1-open-integrations-in-niftyimages}

1. Na NiftyImages, acesse **Settings** > **Integrations**.
2. Selecione **Braze**.
3. Selecione **Connect Braze**.

### Etapa 2: Criar sua chave da API REST da Braze {#step-2-create-your-braze-rest-api-key}

1. Na Braze, acesse **Configurações** > **APIs e identificadores**.
2. Crie ou selecione uma chave da API REST para a integração com a NiftyImages.
3. Em **Custom Attributes**, selecione `custom_attributes.get`.
4. Em **Content Blocks**, selecione `content_blocks.create`.
5. Salve a chave de API e copie a chave da API REST e o seu [endpoint REST]({{site.baseurl}}/api/basics#endpoints).

### Etapa 3: Conectar sua conta Braze na NiftyImages {#step-3-connect-your-braze-account-in-niftyimages}

1. Volte para a tela de integração com a Braze na NiftyImages.
2. Cole a chave da API REST da Braze.
3. Insira o endpoint REST da Braze.
4. Confirme a conexão.
5. Verifique se sua conta Braze aparece em **Connected Braze accounts** com o status **Active** ou **Connected**.

Você pode conectar várias contas Braze, se necessário, o que é útil para agências, equipes multimarcas ou organizações que gerenciam várias instâncias da Braze.

## Personalizar ativos na NiftyImages {#customize-assets-in-niftyimages}

Depois de conectar a Braze, use a sincronização de variáveis de contato e a publicação em Content Blocks para gerenciar visuais personalizados.

### Usar a sincronização de variáveis de contato {#use-contact-variable-sync}

A sincronização de variáveis de contato permite que você use propriedades de contato existentes da Braze diretamente na NiftyImages sem precisar digitar ou recriar merge tags manualmente.

1. Crie ou edite uma imagem personalizada ou outro ativo da NiftyImages.
2. Abra o seletor de merge tag ou personalização.
3. Selecione **Pick from connected integrations** e escolha as propriedades da Braze que deseja usar.
4. Adicione esses valores a camadas de texto, imagem, temporizador, mapa, gráfico, calendário ou conteúdo dinâmico.
5. Salve a imagem.

Imagens salvas que usam variáveis da Braze incluem automaticamente esses valores de personalização na URL da imagem da NiftyImages.

### Publicar em Content Blocks da Braze {#publish-to-braze-content-blocks}

1. Finalize seu ativo na NiftyImages.
2. Selecione **Send to Braze**.

## Usar a NiftyImages na Braze {#use-niftyimages-in-braze}

Use Content Blocks publicados em modelos de e-mail, Campaigns e Canvas da Braze.

### Adicionar um ativo da NiftyImages a um e-mail da Braze {#add-a-niftyimages-asset-to-a-braze-email}

1. Abra um modelo de e-mail, uma Campaign ou uma mensagem de e-mail em Canvas na Braze.
2. No editor de mensagens, abra o menu de personalização e selecione **Content Blocks** como o tipo de personalização.
3. Selecione o Content Block da NiftyImages que você publicou a partir da NiftyImages.

### Reutilizar ativos da NiftyImages na Braze {#reuse-niftyimages-assets-across-braze}

1. Use o Content Block publicado em e-mails de marketing, modelos de e-mail, Campaigns, ativos de marca compartilhados e fluxos automatizados.
2. Quando um ativo da NiftyImages usa variáveis dinâmicas, a Braze passa os valores de contato com base na mensagem e no canal.
3. Atualize o ativo de origem na NiftyImages quando precisar de alterações criativas.

### Desconectar uma conta Braze {#disconnect-a-braze-account}

1. Volte para **Settings** > **Integrations** na NiftyImages.
2. Abra a página de conexão com a Braze.
3. Selecione o ícone de remover ou desconectar da conta que deseja remover.
4. Confirme a desconexão.

## Considerações {#considerations}

- **Permissões da API REST:** a chave da API REST da Braze deve incluir `custom_attributes.get` para sincronização de propriedades de contato e `content_blocks.create` para publicação de ativos em Content Blocks da Braze.
- **Disponibilidade de propriedades de contato:** somente as propriedades de contato disponíveis para a conta Braze conectada podem ser sincronizadas na NiftyImages.
- **Valores de fallback:** use valores de fallback ao criar visuais personalizados para que cada cliente veja uma imagem bem acabada, mesmo quando uma propriedade de contato estiver ausente.
- **Content Blocks reutilizáveis:** publicar em Content Blocks da Braze ajuda as equipes a evitar copiar e colar HTML manualmente, reduzir erros de merge tags e reutilizar ativos em Campaigns e modelos.
- **Várias contas Braze:** a NiftyImages suporta várias contas Braze conectadas, o que é útil para agências, equipes multimarcas e equipes que gerenciam várias instâncias da Braze.
- **Testes:** teste a mensagem final na Braze com perfis de clientes de amostra antes de lançar uma Campaign ou Canvas.

## Solução de problemas {#troubleshooting}

Consulte a tabela a seguir se você tiver problemas com a integração da NiftyImages.

| Problema | Solução |
| -------- | ------- |
| A conta Braze não conecta | Confirme se a chave da API REST é válida, se o endpoint REST está correto e se a chave inclui as permissões necessárias. |
| As propriedades de contato da Braze não aparecem na NiftyImages | Confirme se a chave de API inclui `custom_attributes.get`. Em seguida, atualize a conexão com a Braze dentro da NiftyImages. |
| O ativo não é publicado em Content Blocks da Braze | Confirme se a chave de API inclui `content_blocks.create` e se a conta Braze conectada permite a criação de Content Blocks. |
| A personalização não é exibida corretamente | Verifique se a propriedade de contato da Braze selecionada contém um valor para o usuário teste. Adicione valores de fallback na NiftyImages quando necessário. |
| A imagem não é renderizada na Braze | Confirme se o ativo da NiftyImages está salvo, ativo e publicado corretamente. Envie uma mensagem de teste na Braze para verificar a imagem no canal pretendido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }