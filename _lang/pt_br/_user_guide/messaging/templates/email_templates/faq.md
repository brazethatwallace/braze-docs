---
nav_title: FAQ
article_title: FAQ sobre modelos de e-mail e modelos de link
page_order: 10

page_type: FAQ
description: "Esta página aborda perguntas frequentes sobre modelos de e-mail e modelos de link."
tool:
  - Templates
channel: email

---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página fornece respostas para algumas perguntas frequentes sobre modelos de e-mail e modelos de link.

## Modelos de e-mail {#email-templates}

### Posso adicionar um link "ver este e-mail no navegador" aos meus e-mails? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Não, a Braze não oferece essa funcionalidade. Isso ocorre porque a grande maioria dos e-mails é aberta em dispositivos móveis e clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Alternativa:** Para obter o mesmo resultado, você pode hospedar o conteúdo do seu e-mail em uma landing page externa (como o seu site), que pode ser vinculada a partir da campanha de e-mail que você está criando usando a ferramenta **Link** ao editar o corpo do e-mail.

### Como crio um link de cancelamento de inscrição personalizado para meus modelos de e-mail? {#how-do-i-create-a-custom-unsubscribe-link-for-my-email-templates}

Existe uma opção de redirecionamento para a página de cancelamento de inscrição.

Você pode alterar o link de cancelamento de inscrição no rodapé personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} para um link do seu próprio site com um parâmetro de consulta que inclua o ID do usuário. Um exemplo é:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Em seguida, você pode chamar o [endpoint `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para atualizar o status de inscrição do usuário. Para saber mais, consulte nossa documentação sobre [como alterar inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions/#changing-email-subscriptions).

Para salvar esse novo link, a tag padrão de cancelamento de inscrição da Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} deve estar no rodapé. Isso significa que você precisará incluir o link padrão "ocultando-o", colocando a tag em um comentário ou em uma tag `<div>` oculta.

- **Exemplo de tag em comentário:** colocando a tag em um comentário: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Exemplo de comentário em tag `<div>` oculta:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### O que acontece se eu editar um modelo de e-mail que está sendo usado em uma campanha? {#what-happens-if-i-edit-an-email-template-that-is-currently-being-used-in-a-campaign}

As edições feitas em um modelo existente não serão refletidas em campanhas que foram criadas usando versões anteriores desse modelo. Para campanhas da API que usam um modelo no corpo da REST API, a Braze usará a versão mais recente do modelo no momento do envio.

## Modelos de link {#link-templates}

### Posso fazer upload de vários modelos de link no meu e-mail? {#can-i-upload-multiple-link-templates-to-my-email}

Sim, você pode inserir quantos modelos quiser nas suas mensagens de e-mail. Como prática recomendada, teste seus e-mails para garantir que os links não excedam 2.000 caracteres, já que a maioria dos navegadores encurta ou corta os links.

### Como pré-visualizo meus links com todas as tags aplicadas? {#how-do-i-preview-my-links-with-all-of-the-tags-applied}

Existem várias maneiras de pré-visualizar seus links. Depois de aplicar o [modelo de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template/), você pode enviar um [e-mail de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para si mesmo para visualizar todos os links.

No painel de pré-visualização em uma nova guia, você também pode abrir os links para visualizá-los. Você também pode passar o mouse sobre os links no painel de pré-visualização e vê-los na parte inferior do seu navegador.

### Como o modelo de link funciona com Liquid? {#how-does-link-templating-work-with-liquid}

Os modelos de link são expandidos e adicionados a cada URL antes de qualquer expansão de Liquid acontecer. Se parte da sua URL for gerada usando um trecho de Liquid, recomendamos que a URL base e o ponto de interrogação (?) sejam codificados diretamente para que os modelos de link sejam expandidos corretamente.

Evite adicionar o ponto de interrogação (?) ao seu Liquid, pois isso fará com que os modelos de link adicionem primeiro um ponto de interrogação (?) e, depois, o processo de expansão do Liquid adicione um segundo ponto de interrogação (?).

## Alias de link {#link-aliasing}

### Como a ativação do alias de link afeta meus Content Blocks e modelos de link? {#how-will-enabling-link-aliasing-impact-my-content-blocks-and-link-templates}

Para todos os novos Content Blocks criados, o alias de link é aplicado em todos os espaços de trabalho, já que esse é um recurso no nível da empresa.

Os Content Blocks existentes não serão modificados quando o alias de link for ativado. Embora os modelos de link existentes não sejam modificados, a seção de modelo de link existente em uma mensagem será removida. Confira [Alias de link em Content Blocks]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/#link-aliasing-in-content-blocks) para saber mais.

### Posso usar lógica condicional de Liquid inteiramente dentro de uma tag âncora HTML? {#can-i-use-liquid-conditional-logic-entirely-within-an-html-anchor-tag}

Não, o alias de link da Braze não reconhecerá o HTML corretamente.

Quando uma lógica como essa é usada em conjunto com recursos que precisam analisar o HTML (como um pré-cabeçalho ou modelo de link), a biblioteca usada para escanear o HTML pode modificar a tag âncora de uma forma que impedirá que o `href` correto seja aplicado pelo modelo. A biblioteca então determinará que o HTML é inválido porque é agnóstica ao código Liquid.

Em vez disso, use lógica Liquid que contenha uma tag âncora completa em cada etapa. Isso não interferirá na análise do HTML porque a lógica inclui múltiplas instâncias de HTML válido. Você também pode simplificar sua lógica atribuindo e depois aplicando uma variável na tag âncora apropriada.