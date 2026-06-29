---
nav_title: Modelos de Canvas
article_title: Criar um modelo de Canvas
page_order: 2
alias: "/canvas_templates/"
description: "Crie e gerencie modelos reutilizáveis de Canvas ou comece com modelos pré-criados da Braze para casos de uso comuns."
---

# Criar um modelo de Canvas {#create-a-canvas-template}

> Este artigo de referência aborda como criar e gerenciar modelos para Canvas. O uso de modelos pode aprimorar seu envio de mensagens criando uma estrutura consistente que pode ser facilmente personalizada para atender aos seus objetivos específicos em seus Canvas.

{% alert tip %}
Economize tempo e simplifique a criação do seu Canvas usando os [modelos de Canvas da Braze](#available-braze-templates)! Navegue pela nossa biblioteca de modelos pré-criados para encontrar um que se encaixe no seu caso de uso e personalize-o para atender às suas necessidades específicas.
{% endalert %}

## Método 1: Criar a partir de um Canvas existente {#method-1-create-from-an-existing-canvas}

### Etapa 1: Selecione seu Canvas existente {#step-1-select-your-existing-canvas}

No dashboard da Braze, acesse **Messaging** > **Canvas** e selecione um Canvas existente que você deseja usar como modelo.

### Etapa 2: Crie seu modelo {#step-2-create-your-template}

No editor de Canvas, selecione **Edit Canvas** ou **Editar rascunho**, dependendo se o seu Canvas está ativo ou em rascunho. Expanda o menu suspenso **Salvar como rascunho** no rodapé e selecione **Salvar como modelo**.


### Etapa 3: Salve seu modelo {#step-3-save-your-template}

Em seguida, dê um nome ao seu modelo e adicione as tags relevantes. Depois, selecione **Save**. Seu modelo agora está pronto para ser usado na criação de um Canvas, dando a você uma vantagem com as configurações básicas e etapas já definidas.

## Método 2: Criar pelo editor de modelos de Canvas {#method-2-create-via-canvas-template-editor}

### Etapa 1: Acesse o editor de modelos de Canvas {#step-1-go-to-the-canvas-template-editor}

No dashboard da Braze, acesse **Conteúdo** > **Canvas**.

### Etapa 2: Crie um novo modelo {#step-2-create-a-new-template}

Selecione **Criar modelo** e comece a configurar os detalhes do seu Canvas. Você pode começar dando um nome ao seu modelo de Canvas.

![Um exemplo de modelo de Canvas chamado "Annual sale Canvas template" com a descrição "Use for annual spring promotion".]({% image_buster /assets/img/canvas_template_example.png %})

### Etapa 3: Personalize seu modelo {#step-3-customize-your-template}

Em seguida, personalize seu modelo [configurando seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-2-build-your-canvas). Você pode decidir quando os usuários devem entrar no Canvas, determinar quais usuários podem entrar nesse Canvas, ajustar suas configurações de envio e construir a jornada do usuário para o modelo.

### Etapa 4: Salve seu modelo {#step-4-save-your-template}

Depois de terminar de personalizar seu modelo, selecione o botão **Salvar modelo**. Na página **Modelo de Canvas**, você pode visualizar os detalhes do seu modelo de Canvas selecionando <i class="fas fa-list" aria-label="Detalhes do modelo"></i> **Detalhes do modelo**.

## Usando modelos de Canvas {#using-canvas-templates}

Existem duas maneiras de usar seu modelo ao criar um Canvas:

- **A partir de Messaging**: Acesse **Messaging** > **Canvas**. Selecione o botão **Criar Canvas** e depois **Usar um modelo de Canvas**.
- **A partir de Conteúdo**: Acesse **Conteúdo** > **Canvas** e encontre o modelo desejado em **Modelos de Canvas**. Em seguida, selecione o menu <i class="fas fa-ellipsis-vertical" aria-label="Mais opções"></i> seguido de **Aplicar modelo**. Isso levará você a um novo Canvas com o modelo aplicado no criador de Canvas.

### Modelos da Braze disponíveis {#available-braze-templates}

Para uma lista de modelos de Canvas disponíveis, consulte [Modelos de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/). Para detalhes sobre o uso de modelos de Canvas de eCommerce, consulte [Como usar eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

## Gerenciando modelos de Canvas {#managing-canvas-templates}

Os modelos de Canvas podem ser duplicados e arquivados, de forma semelhante a um Canvas real. Para editar um modelo de Canvas, selecione o modelo e depois **<i class="fas fa-pencil-alt"></i>Editar**.

Em nível de espaço de trabalho, você pode atualizar as permissões de usuário para permitir ou limitar o acesso para criar, editar, visualizar ou arquivar modelos de Canvas.

### Permissões para equipes e espaços de trabalho {#permissions-for-teams-and-workspaces}

Para permitir que apenas determinados usuários acessem e usem modelos de Canvas específicos, [adicione uma equipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) aos modelos e, em seguida, atribua permissões em nível de equipe para "Acessar Campaigns, Canvas, Content Cards, Content Blocks, Feature Flags, Segments, Biblioteca de mídia e Central de Preferências".

Se você atribuir qualquer uma das seguintes permissões em nível de equipe, mas não em nível de espaço de trabalho, você só poderá fazer o seguinte atribuído à sua equipe:

- Criar e editar modelos de Canvas
- Visualizar modelos de Canvas
- Arquivar modelos de Canvas

Se as permissões forem concedidas tanto em nível de espaço de trabalho quanto de equipe, as permissões em nível de espaço de trabalho terão prioridade.

## Perguntas frequentes {#frequently-asked-questions}

### Posso salvar uma etapa incompleta em um modelo de Canvas? {#can-i-save-an-incomplete-step-in-a-canvas-template}

Sim, você pode salvar etapas incompletas como um modelo de Canvas. No entanto, quando o modelo for usado, haverá um erro no botão **Salvar modelo** indicando o que é necessário para lançar o Canvas.

### Posso salvar as configurações do criador de Canvas como modelo, ou só posso salvar etapas? {#can-i-save-my-canvas-builder-settings-as-a-template-or-can-i-only-save-steps}

Sim, você pode salvar as configurações do criador de Canvas dentro de um modelo de Canvas. Por exemplo, se você planeja usar uma combinação de segmentos e filtros com frequência, pode salvar essas configurações de **Público-alvo** como parte do seu modelo de Canvas.