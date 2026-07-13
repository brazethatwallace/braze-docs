---
nav_title: Modelos de links
article_title: Modelos de links
page_order: 4
description: "Este artigo aborda como criar diferentes tipos de modelos de links nos seus e-mails."
tool:
  - Templates
channel:
  - email

---

# Modelos de links {#link-templates}

> Com os modelos de links, você pode criar links dinâmicos e reutilizáveis para suas campanhas de e-mail, adicionando parâmetros ou prefixando URLs. Isso pode criar consistência nos URLs de suas campanhas e mensagens.

{% alert note %}
Os modelos de links são um recurso opcional. Se **Modelos de links de e-mail** não estiver disponível na seção **Modelos**, entre em contato com o gerente da sua conta para ativar o recurso.
{% endalert %}

## Como funciona {#how-it-works}

Os modelos de links são mais frequentemente usados nos seguintes casos de uso:

- Adicionar parâmetros de consulta do Google Analytics a todos os links em uma determinada mensagem de e-mail
- Prefixar um URL a todos os links em uma determinada mensagem de e-mail

Digamos que você esteja executando uma Campaign promocional de e-mail para o lançamento de um novo produto. Você pode usar um modelo de link que direciona os usuários para a página do produto e personalizar o link para incluir o nome do usuário ou um código promocional específico. Isso permite rastrear quantos usuários clicaram no link e fizeram uma compra. Dessa forma, você pode criar consistência nos seus links e acompanhar melhor sua análise de dados.

## Criando um modelo de link {#creating-a-link-template}

Você pode criar um número ilimitado de modelos de links para atender às suas diversas necessidades. Para criar um modelo de link, faça o seguinte:

1. Acesse **Conteúdo** > **Link de e-mail**.
2. Selecione **Criar modelo de link de e-mail**.
3. Dê um nome ao seu modelo de link.
4. (Opcional) Adicione uma descrição, equipe ou tag para incluir detalhes sobre o modelo de link.
5. (Opcional) Selecione o botão de alternância para adicionar automaticamente o modelo de link aos links em campanhas de e-mail e Canvas. Isso se aplica ao adicionar um novo link a qualquer e-mail novo ou existente.

Existem dois tipos de modelos de links que você pode criar:

- [Modelo de link que insere antes de um URL](#prepend-link-template)
- [Modelo de link que insere depois de um URL](#append-link-template)

Ao usar modelos de links e [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), o Liquid deve ser adicionado apenas dentro da tag body para garantir uma renderização consistente.

### Prefixar: criar um modelo de link que insere antes de um URL {#prepend-link-template}

Para adicionar uma string ou URL antes dos links na sua mensagem de e-mail, faça o seguinte:

1. Crie um novo modelo de link.
2. Defina a **Posição do modelo** como **Antes do URL**.
3. Insira uma string que sempre será prefixada ao seu URL.

A **Pré-visualização do modelo** é fornecida para dar um exemplo de como o modelo de link será inserido antes de um URL.

![Campos de posição do modelo, URL prefixado e pré-visualização do modelo para o processo de inserção do modelo de link antes de um URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Sufixar: criar um modelo de link que insere depois de um URL {#append-link-template}

Se você quiser adicionar parâmetros de consulta depois de um URL na sua mensagem de e-mail:

1. Crie um novo modelo de link.
2. Defina a **Posição do modelo** como **Após o URL**.
3. Insira os parâmetros de consulta (`value=example`) no final de cada URL. Você pode ter vários parâmetros adicionados ao final de um URL.

![Campos de posição do modelo, parâmetros de consulta e pré-visualização do modelo para o processo de inserção do modelo de link depois de um URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Usando modelos de links em campanhas de e-mail {#using-link-templates-in-email-campaigns}

Depois de configurar seus modelos de links, você pode aplicá-los no seu e-mail.

Para aplicar um modelo de link no editor de HTML ou no editor de arrastar e soltar, siga estas etapas:

{% alert important %}
Para acessar a guia **Link Management** no editor de HTML atualizado ou no editor de arrastar e soltar, você precisa ter o link aliasing ativado. Para ativar o link aliasing, entre em contato com o gerente da sua conta. Para saber mais, consulte [Link aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing).
{% endalert %}

- **Editor de HTML atualizado:** Na guia **Content**, selecione **Link Management**, selecione **Add a Link Template**, escolha seu modelo de link e selecione **Add**.
- **Editor de arrastar e soltar:** Na guia **Content**, selecione **Link Management**, selecione **Add a Link Template**, escolha seu modelo de link e selecione **Add**.

![Guia Link Management no editor de arrastar e soltar com uma lista de exemplo de modelos de links.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Os modelos de links não são aplicados a texto simples. Isso significa que o Currents pode mostrar cliques que não incluem os parâmetros dos modelos de links, pois esses cliques podem vir da versão em texto simples do e-mail.
{% endalert %}

Ao adicionar modelos de links na guia **Link Management**, role para a direita para visualizar os modelos que você adicionou. Se links existentes em um e-mail já tiverem um modelo de link adicionado, os links recém-adicionados também terão o modelo de link adicionado por padrão.

## Gerenciando modelos de links {#managing-link-templates}

Você também pode [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) modelos de links. Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e mídia]({{site.baseurl}}/user_guide/messaging/templates).

{% alert important %}
O arquivamento de modelos não está disponível atualmente para modelos de links.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

Para respostas às perguntas frequentes sobre modelos de links, confira nossa página de [Perguntas frequentes sobre modelos]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).