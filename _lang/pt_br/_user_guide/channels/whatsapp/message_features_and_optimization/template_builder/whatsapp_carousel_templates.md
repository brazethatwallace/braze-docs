---
nav_title: Modelos de carrossel
article_title: Modelos de carrossel do WhatsApp
description: "Este artigo de referência aborda os modelos de carrossel do WhatsApp."
tool:
  - WhatsApp
alias: /whatsapp_carousel_templates/
toc_headers: h2
---

# Modelos de carrossel do WhatsApp {#whatsapp-carousel-templates}

> Os modelos de carrossel do WhatsApp permitem criar mensagens interativas com vários cartões pelos quais os usuários podem deslizar. Cada carrossel pode conter até 10 cartões com imagens ou vídeos, além de botões personalizáveis para engajamento. Esse recurso é ideal para apresentar seus produtos e serviços, ou conteúdo em várias etapas em um formato visualmente atraente.

## Pré-requisitos {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Criar um modelo de carrossel {#create-a-carousel-template}

Você pode criar modelos de carrossel na Braze com o construtor de modelos do WhatsApp. Ao criar modelos, a Braze valida seu conteúdo para atender aos critérios da Meta.

Ao criar um modelo na Braze, você pode usar:
- Liquid que você espera usar ao enviar a mensagem. A Braze salva isso para referência futura.
- Variáveis genéricas como {% raw %}`{{1}}`{% endraw %}.

{% alert note %}
As Liquid tags {% raw %}`{% %}`{% endraw %} não são compatíveis com o construtor de modelos porque não atendem aos critérios de conteúdo da Meta.
{% endalert %}

Após o envio do modelo, ele aparece na lista de modelos da WABA e é revisado em até 24 horas. No entanto, a revisão geralmente ocorre em poucos minutos.

### Etapa 1: Acessar o construtor de modelos {#step-1-access-the-template-builder}

1. Na Braze, acesse **Modelos**.
2. Selecione **Modelos de WhatsApp** nas opções disponíveis.

![Modelos de WhatsApp no menu de navegação de Modelos.]({% image_buster /assets/img/whatsapp/templates/whatsapp_templates.png %}){: style="max-width:70%;"}

{: start="3"}
3. Selecione **Criar modelo de carrossel**.

![Botão para criar um modelo de carrossel.]({% image_buster /assets/img/whatsapp/templates/create_carousel_template.png %})

### Etapa 2: Configurar as definições do modelo {#step-2-configure-template-settings}

Preencha os campos obrigatórios.

| Campo | Descrição |
| --- | --- |
| Conta do WhatsApp Business | Selecione a WABA onde este modelo será armazenado. Lembre-se de que todos os grupos de inscrições e números de telefone dentro desta WABA terão acesso ao modelo. |
| Idioma do modelo | Selecione o idioma do seu modelo. A Meta restringe os modelos a um único idioma, então escolha o idioma que seu público verá. |
| Nome do modelo | Insira um nome descritivo que ajude a identificar este modelo posteriormente. Os nomes de modelo não podem conter espaços — use underscores ou remova os espaços completamente (como `carousel_example` ou `carouselexample`). |
| Categoria | Definida automaticamente como **Marketing**. Todas as mensagens de carrossel são categorizadas como mensagens de marketing. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Configurar as definições do modelo" }

![Painel de detalhes do modelo de WhatsApp com uma conta do WhatsApp Business selecionada, inglês como idioma do modelo e o nome do modelo "welcome_message".]({% image_buster /assets/img/whatsapp/templates/whatsapp_template_details.png %}){: style="max-width:70%"}

### Etapa 3: Adicionar conteúdo do corpo {#step-3-add-body-content}

Toda mensagem de carrossel deve começar com o conteúdo do corpo, que é o texto exibido antes dos cartões do carrossel.

Você pode incluir variáveis Liquid para personalização, como {% raw %}`{{first_name}}`{% endraw %}, que cria um espaço de variável vazio que pode ser preenchido com conteúdo dinâmico ou modificado posteriormente ao usar o modelo em Campaigns. As variáveis não podem ser colocadas no início ou no final do conteúdo do corpo.

### Etapa 4: Configurar as definições do carrossel {#step-4-configure-carousel-settings}

Antes de criar cartões individuais, defina a estrutura geral do carrossel com as configurações do carrossel. Essas configurações se aplicam a todos os cartões e não podem ser alteradas após o envio do modelo.

#### Tipo de mídia {#media-type}

Escolha o tipo de mídia: **Imagem** ou **Vídeo**. Isso é usado para todos os cartões.

![Criador com opções para selecionar o tipo de mídia Imagem ou Vídeo.]({% image_buster /assets/img/whatsapp/templates/media_types.png %})

#### Configuração de botões {#button-configuration}

Escolha o tipo de botão: **Resposta rápida**, **Número de telefone** ou **Visitar site**. Essa configuração é usada para todos os cartões. Em seguida, selecione até dois botões por cartão.

### Etapa 5: Criar cartões do carrossel {#step-5-create-carousel-cards}

Agora você pode criar cartões individuais do carrossel. Todos os cartões mantêm o mesmo formato e estrutura. Você pode adicionar até 10 cartões, mas deve adicionar pelo menos dois.

{% alert important %}
Não é possível alterar o número de cartões após enviar o modelo para revisão da Meta.
{% endalert %}

1. Faça upload de uma imagem ou vídeo, dependendo do tipo de mídia selecionado.
2. Adicione o texto ou a descrição do cartão.
3. Configure o texto e as ações dos botões.
4. Adicione variáveis Liquid onde necessário. Você pode adicioná-las onde houver um botão **+** (mais).

{% alert tip %}
Use variáveis Liquid estrategicamente para personalizar conteúdo como porcentagens de desconto, nomes de produtos ou ofertas específicas para o usuário. As variáveis podem ser adicionadas ao texto do cartão, texto do botão e URLs.
{% endalert %}

![Criador com exemplos de cartões de carrossel promovendo alimentos nutritivos.]({% image_buster /assets/img/whatsapp/templates/example_carousel_cards.png %})

### Etapa 6: Pré-visualizar e enviar {#step-6-preview-and-submit}

1. Use a seção **Prévia** para ver como seu carrossel aparecerá para os usuários.
2. Selecione **Enviar para revisão da Meta** para que a Braze envie o modelo para aprovação da Meta.
3. A aprovação geralmente leva poucos minutos, mas pode levar até 24 horas.
4. Verifique o status do modelo na lista de **Modelos** na página de modelos do WhatsApp ou no seletor de Canvas e Campaign.

{% alert note %}
O envio de teste não está disponível até que a Meta aprove o modelo. O status do modelo aparece como **Rascunho** durante a criação e muda para **Aprovado** após a Meta concluir a revisão.
{% endalert %}

## Usar modelos de carrossel {#use-carousel-templates}

Após a aprovação do seu modelo de carrossel pela Meta, você pode usá-lo em Campaigns e Canvas. O processo é semelhante para ambos os tipos de mensagem.

### Etapa 1: Criar uma mensagem do WhatsApp {#step-1-create-a-whatsapp-message}

1. Na Braze, acesse **Campaigns** ou **Canvas** e crie uma mensagem do WhatsApp.
2. Selecione o grupo de inscrições que corresponde à conta do WhatsApp Business (WABA) do seu modelo.

{% alert important %}
Se você tiver várias contas do WhatsApp Business, selecione um grupo de inscrições da mesma WABA onde o modelo foi criado. Os modelos não são compartilhados entre WABAs, mas são compartilhados entre todos os grupos de inscrições e números de telefone dentro da mesma WABA.
{% endalert %}

### Etapa 2: Selecionar seu modelo de carrossel {#step-2-select-your-carousel-template}

1. Pesquise seu modelo pelo nome (como "carousel_example").
2. Verifique se o status do modelo é **Aprovado**.
3. Selecione o modelo para carregá-lo no criador de mensagens.

### Etapa 3: Personalizar conteúdo dinâmico {#step-3-customize-dynamic-content}

Quando seu modelo é carregado, ele contém conteúdo bloqueado e editável.

{% tabs local %}
{% tab Conteúdo bloqueado %}


- O texto estático (qualquer conteúdo enviado sem variáveis) é bloqueado e não pode ser editado.
- O número de cartões do carrossel é fixo.
- O tipo de mídia e a configuração de botões não podem ser alterados.

{% endtab %}
{% tab Conteúdo editável %}


{% raw %}
- Qualquer campo com uma variável pode ser modificado com Liquid diferente.
- Se você enviou o modelo com Liquid (por exemplo, `{{first_name}}`), a Braze preserva e exibe automaticamente esse Liquid.
- Você pode alterar o Liquid para variáveis diferentes (por exemplo, trocar de `{{first_name}}` para `{{last_name}}`).
- Imagens com variáveis podem ser tornadas dinâmicas usando URLs com Liquid.
- Você pode fazer upload de novas imagens da biblioteca de mídia da Braze em vez de usar a mídia enviada.
{% endraw %}

#### Exemplo {#example}

{% raw %}Por exemplo, digamos que seu modelo inclua uma variável de porcentagem de desconto: `{{discount_percentage}}`. Na Campaign, você pode manter isso ou alterar para `{{custom_attributes.vip_discount}}`.{% endraw %} A Meta exige apenas que o espaço da variável seja preenchido — o Liquid específico usado é flexível.

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar sua Campaign ou Canvas {#step-4-launch-your-campaign-or-canvas}

Após a composição, prossiga com o fluxo de lançamento da sua Campaign ou Canvas, incluindo testes. O modelo de carrossel funciona como qualquer outro modelo de mensagem do WhatsApp.

## Práticas recomendadas {#best-practices}

### Diretrizes de conteúdo {#content-guidelines}

- **Posicionamento do conteúdo do corpo:** as variáveis não podem ser colocadas no final do conteúdo do corpo. Adicione pelo menos uma palavra ou sinal de pontuação após cada variável.
- **Estrutura consistente dos cartões:** todos os cartões devem ter o mesmo formato, tipo de mídia e configuração de botões. Planeje seu conteúdo de acordo.
- **Quantidade ideal de cartões:** embora você possa criar até 10 cartões, considere a experiência do usuário. Muitos cartões podem ser cansativos; de 3 a 5 cartões funcionam bem para a maioria dos casos de uso.
- **Valores padrão:** ao usar variáveis Liquid, sempre forneça valores padrão para uma prévia precisa. Isso ajuda a confirmar que a mensagem é exibida corretamente caso determinados dados do perfil do usuário estejam ausentes.

### Contas do WhatsApp Business e grupos de inscrições {#whatsapp-business-accounts-and-subscription-groups}

- **Entenda o compartilhamento de modelos:** os modelos são compartilhados entre todos os grupos de inscrições dentro da mesma conta do WhatsApp Business (WABA), mas não entre WABAs diferentes. Planeje-se caso gerencie várias WABAs.
- **Organize por WABA:** se você tiver várias WABAs, considere organizar seus modelos por conta comercial para evitar confusão ao selecionar modelos em Campaigns.

### Testes e aprovação {#testing-and-approval}

- **Pré-visualize antes do envio:** sempre pré-visualize seus modelos para identificar erros antes de enviar para aprovação da Meta.
- **Planeje o tempo de aprovação:** embora a aprovação geralmente leve apenas alguns minutos, considere possíveis atrasos ao planejar lançamentos de Campaigns.
- **Teste com cuidado:** após a aprovação, teste seu carrossel com dados reais de usuários para confirmar que todas as variáveis são preenchidas corretamente e que a experiência do usuário é fluida.

## Solução de problemas {#troubleshooting}

| Problema | Solução |
| --- | --- |
| O modelo não aparece na Campaign | Verifique se o grupo de inscrições selecionado pertence à mesma WABA do modelo. Além disso, confirme se o status do modelo é **Aprovado** e não está em status de **Rascunho** ou **Pendente**. |
| Não é possível colocar variável no final do corpo | Mova a variável para antes no texto e adicione pelo menos um caractere ou sinal de pontuação após ela. Esse é um requisito da Meta para modelos do WhatsApp. |
| As variáveis não são preenchidas no teste | Verifique se a sintaxe Liquid está correta e se os atributos existem nos perfis dos seus usuários. Confira se há erros de digitação nos nomes das variáveis e verifique se os valores padrão estão definidos quando apropriado. |
| O nome do modelo contém espaços | Os nomes de modelo não podem conter espaços. Use underscores (`template_name`) ou remova os espaços completamente (`templatename`). |
| Não é possível alterar o número de cartões | O número de cartões é fixado quando você cria o modelo e não pode ser alterado após o envio. Se precisar de um número diferente de cartões, será necessário criar um novo modelo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }