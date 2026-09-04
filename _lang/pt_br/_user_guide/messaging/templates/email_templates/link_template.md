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

Os modelos de link são mais frequentemente usados nos seguintes casos de uso:

- Adicionar parâmetros de consulta do Google Analytics a todos os links em uma determinada mensagem de e-mail
- Adicionar um URL como prefixo a todos os links em uma determinada mensagem de e-mail

Digamos que você esteja executando uma Campaign de e-mail promocional para o lançamento de um novo produto. Você pode usar um modelo de link que direcione os usuários para a página do produto e personalizar o link para incluir o nome do usuário ou um código promocional específico. Isso permite rastrear quantos usuários clicaram no link e realizaram uma compra. Dessa forma, você pode criar consistência em todos os seus links e acompanhar melhor sua análise de dados.

## Criando um modelo de link {#creating-a-link-template}

Você pode criar um número ilimitado de modelos de link para atender às suas diversas necessidades. Para criar um modelo de link, faça o seguinte:

1. Acesse **Conteúdo** > **Link de e-mail**.
2. Selecione **Criar modelo de link de e-mail**.
3. Dê um nome ao seu modelo de link.
4. (Opcional) Adicione uma descrição, equipe ou tag para incluir detalhes sobre o modelo de link.
5. (Opcional) Selecione o botão de alternância para adicionar automaticamente o modelo de link aos links em Campaigns de e-mail e Canvas. Isso se aplica ao adicionar um novo link a qualquer e-mail novo ou existente.

Existem dois tipos de modelos de link que você pode criar:

- [Modelo de link que insere antes de uma URL](#prepend-link-template)
- [Modelo de link que insere depois de uma URL](#append-link-template)

Ao usar modelos de link e [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), o Liquid deve ser adicionado apenas dentro da tag body para garantir uma renderização consistente.

### Prefixo: criar um modelo de link que insere antes de uma URL {#prepend-link-template}

Para adicionar uma string ou URL antes dos links na sua mensagem de e-mail, faça o seguinte:

1. Crie um novo modelo de link.
2. Defina a **Posição do modelo** como **Antes da URL**.
3. Insira uma string que sempre será prefixada à sua URL.

A **Prévia do modelo** é fornecida para mostrar um exemplo de como o modelo de link será inserido antes de uma URL.

![Campos de posição do modelo, URL de prefixo e prévia do modelo para o processo de inserção do modelo de link antes de uma URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Sufixo: criar um modelo de link que insere depois de uma URL {#append-link-template}

Se você quiser adicionar parâmetros de consulta depois de uma URL na sua mensagem de e-mail:

1. Crie um novo modelo de link.
2. Defina a **Posição do modelo** como **Depois da URL**.
3. Insira os parâmetros de consulta (`value=example`) ao final de cada URL. Você pode ter vários parâmetros adicionados ao final de uma URL.

![Campos de posição do modelo, parâmetros de consulta e prévia do modelo para o processo de inserção do modelo de link depois de uma URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

#### Liquid tags para `utm_campaign` {#liquid-tags-for-utm_campaign}

As Liquid tags para `utm_campaign` diferem entre Campaigns e Canvas.

Em Campaigns, use:

{% raw %}
- `{{campaign.${name}}}` para obter o nome da Campaign
- `{{campaign.${message_name}}}` para obter o nome da variante da mensagem
{% endraw %}

Em Canvas, use:

{% raw %}
- `{{canvas.${name}}}` para obter o nome do Canvas
- `{{campaign.${name}}}` para obter o nome da etapa do Canvas (apenas etapas de mensagem)
{% endraw %}

Para uma comparação completa desses atributos em Liquid, REST API e Currents, consulte [Atributos de Campaign e Canvas entre fontes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources). Para orientações sobre codificação de URL, consulte [Nomes de Campaign em URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

## Usando modelos de link em campanhas de e-mail {#using-link-templates-in-email-campaigns}

Depois de configurar seus modelos de link, você pode aplicá-los no seu e-mail.

Para aplicar um modelo de link no editor de HTML ou no editor de arrastar e soltar, siga estas etapas:

{% alert note %}
Se os modelos de link de e-mail ou o [link aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) estiverem ativados para o seu espaço de trabalho, você poderá acessar a guia **Link Management** no editor de HTML atualizado e no editor de arrastar e soltar.
{% endalert %}

- **Editor de HTML atualizado:** Na guia **Content**, selecione **Link Management**, selecione **Add a Link Template**, escolha seu modelo de link e selecione **Add**.
- **Editor de arrastar e soltar:** Na guia **Content**, selecione **Link Management**, selecione **Add a Link Template**, escolha seu modelo de link e selecione **Add**.

![Guia Link Management no editor de arrastar e soltar com uma lista de exemplo de modelos de link.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Os modelos de link não são aplicados ao texto simples. Isso significa que o Currents pode mostrar cliques que não incluem os parâmetros dos modelos de link, pois esses cliques podem vir da versão em texto simples do e-mail.
{% endalert %}

À medida que você adiciona modelos de link na guia **Link Management**, cada modelo aparece como uma coluna adicional na tabela. Se links existentes em um e-mail já tiverem um modelo de link adicionado, novos links adicionados também terão o modelo de link adicionado por padrão.

{% alert tip %}
Ao incluir links na sua mensagem, certifique-se de iniciar as URLs com `http://` ou `https://`.
{% endalert %}

## Gerenciamento de modelos de link {#managing-link-templates}

Você também pode [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) modelos de link. Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e mídias]({{site.baseurl}}/user_guide/messaging/templates).

{% alert important %}
O arquivamento de modelos não está disponível no momento para modelos de link.
{% endalert %}

## Solução de problemas {#troubleshooting}

### Parâmetros UTM ausentes {#missing-utm-parameters}

Os modelos de link não são aplicados a links em comentários HTML padrão (`<!-- ... -->`). Para comentários condicionais do Outlook (por exemplo, `<!--[if mso]>`), os modelos de link são aplicados quando o link aliasing está ativado para o seu espaço de trabalho. Espaços de trabalho sem link aliasing ativado ainda ignoram comentários condicionais.

### Parâmetros UTM presentes no navegador, mas ausentes nos links {#utm-parameters-present-in-browser-but-missing-from-links}

Isso pode acontecer quando o caminho da URL no seu e-mail não corresponde ao caminho completo pretendido (por exemplo, um caminho encurtado ou diferente da URL completa do website).

- **O que verificar:** O `href` no e-mail inclui o caminho completo para a página (não apenas um caminho parcial que depende de redirecionamentos).
- **O que esperar:** Se o caminho no e-mail estiver incompleto ou diferente, os parâmetros UTM do seu modelo de link podem não ser aplicados a esse link quando ele for clicado, mesmo que o website ainda redirecione o visitante para a página correta.

Por exemplo, se o link completo é `https://www.somewebsite.com/women/designer/johnjane`, mas o e-mail usa `https://www.somewebsite.com/designer/johnjane`, é esperado que os parâmetros UTM não sejam adicionados ao link do e-mail.

### Parâmetros UTM ausentes em links renderizados por Liquid {#utm-parameters-missing-from-liquid-rendered-links}

Ao aplicar modelos de link, a Braze analisa cada URL para determinar onde anexar os parâmetros. Se uma Liquid tag renderiza uma URL que não pode ser interpretada como um URI válido, o modelo de link é ignorado silenciosamente. Verifique se a saída do seu Liquid produz uma URL bem formada. Teste visualizando a prévia da mensagem para um usuário específico e verificando se a URL renderizada é válida. Se a URL inclui variáveis Liquid no caminho ou na query string, confirme se a saída não contém caracteres inválidos ou codificação quebrada.

### Valores UTM ausentes em envios de teste {#utm-values-missing-in-test-sends}

Ao fazer envios de teste com modelos de link, {% raw %}`{{${user_id}}}`{% endraw %} não é renderizado. Em vez disso, duplique a Campaign e configure-a para direcionar ao e-mail ou `external_id` dos seus usuários internos e lance a Campaign para verificar se todos os parâmetros UTM do modelo de link estão preenchidos.

## Perguntas frequentes {#frequently-asked-questions}

Para respostas às perguntas frequentes sobre modelos de link, confira nossa página de [Perguntas frequentes sobre modelos]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).