---
nav_title: Prévia compartilhável
article_title: Compartilhar uma prévia de mensagem com stakeholders
page_order: 5
page_type: reference
description: "Este artigo de referência explica como gerar e compartilhar um link de prévia de uma mensagem ou conteúdo, para que stakeholders sem acesso ao dashboard possam revisá-lo antes do envio."
---

# Compartilhar uma prévia de mensagem com stakeholders {#share-a-message-preview-with-stakeholders}

> A prévia compartilhável permite gerar um link para uma prévia da sua mensagem ou conteúdo e compartilhá-lo com revisores, como stakeholders, equipes jurídicas ou de compliance, que não têm acesso ao seu dashboard da Braze. Os destinatários podem visualizar a prévia no navegador sem fazer login na Braze.

## Canais compatíveis {#supported-channels}

Você pode gerar um link de prévia compartilhável para os seguintes canais e tipos de conteúdo:

- Banners
- Content Blocks
- Content Cards
- E-mail e rodapé de e-mail
- Landing pages
- LINE
- Notificações por push
- Páginas de inscrição
- SMS e RCS
- WhatsApp

{% alert note %}
A prévia compartilhável está sendo disponibilizada gradualmente e pode ainda não estar disponível para todos os canais no seu espaço de trabalho. Entre em contato com o gerente de conta da Braze se você não encontrar a opção para um canal listado nesta seção.
{% endalert %}

## Como a prévia compartilhável funciona {#how-shareable-preview-works}

O comportamento a seguir é consistente em todos os canais compatíveis.

### Gerar um link {#generating-a-link}

Ao compor sua mensagem ou conteúdo, selecione **Copy prévia link** para gerar um link compartilhável. A Braze copia automaticamente o link para a sua área de transferência.

- O link abre um snapshot estático e somente leitura da sua mensagem como ela estava no momento em que você gerou o link. Ele não é atualizado automaticamente conforme você continua editando. Gere um novo link para capturar suas alterações mais recentes.
- Se a sua mensagem inclui personalização, como Liquid ou Connected Content que resolve com base em um usuário teste, um perfil de usuário personalizado ou um usuário aleatório, a prévia reflete essa mesma personalização, correspondendo ao que você vê em **prévia and Test**.
- Selecionar **Regenerate link** cria um novo snapshot com sua própria data de expiração. Isso não invalida o link anterior. Ambos os links continuam funcionando de forma independente até que cada um expire.

### Visualizar o link {#viewing-the-link}

Qualquer pessoa com o link pode visualizar a prévia. Não é necessário login na Braze nem permissões do dashboard.

{% alert important %}
Trate o link como qualquer outro documento compartilhável: envie-o apenas para as pessoas que você deseja que tenham acesso e evite publicá-lo em locais públicos.
{% endalert %}

### Expiração do link {#link-expiration}

- Todo link de prévia compartilhável expira sete dias após ser gerado.
- Quando um link expira, ele não abre mais. Gere um novo link a partir do criador para obter um link atualizado.
- Não é possível revogar ou desativar manualmente um link antes de ele expirar. Regenerar um link não revoga o anterior; cada link simplesmente expira em seu próprio prazo de sete dias.

## Particularidades por canal {#per-channel-nuances}

Embora a experiência principal seja a mesma em todos os canais, alguns têm pequenas diferenças que vale a pena conhecer.

{% alert note %}
A prévia compartilhável não está disponível para mensagens no app.
{% endalert %}

| Canal | O que é diferente |
|---|---|
| E-mail | A prévia inclui os campos Para, De e linha de assunto da mensagem, além do corpo da mensagem. <br><br>Se você está personalizando como um usuário personalizado, valores inseridos como propriedades de disparo de API ou propriedades de evento podem não aparecer na prévia, mesmo que sejam exibidos corretamente em **prévia and Test**. Atributos personalizados, usuários teste e usuários aleatórios não são afetados. |
| Banner (editor de arrastar e soltar) | A prévia reflete o conteúdo da última vez que você abriu a guia **prévia** no criador, não necessariamente suas edições mais recentes. <br><br>Abra **prévia** novamente antes de gerar ou regenerar um link para garantir que esteja atualizado. |
| SMS e RCS | Ambos são regidos pela mesma funcionalidade de prévia compartilhável, mas cada um gera seu próprio link independente. |
| WhatsApp | A prévia compartilhável está disponível separadamente para mensagens de modelo do WhatsApp e mensagens de resposta do WhatsApp. |
| Content Blocks, rodapés de e-mail e páginas de inscrição | Esses geram uma prévia do conteúdo independente, sem vínculo com nenhuma Campaign ou Canvas específico em que são usados. |
| Landing pages | A prévia funciona de forma diferente para landing pages em comparação com outros canais. Consulte [Pré-visualizar a página]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-5-preview-the-page) para mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Particularidades por canal" }

## Perguntas frequentes {#frequently-asked-questions}

{% details O destinatário precisa de uma conta na Braze para visualizar a prévia? %}
Não. Qualquer pessoa com o link pode visualizar a prévia no navegador sem fazer login.
{% enddetails %}

{% details A prévia é atualizada se eu continuar editando minha mensagem? %}
Não. Um link de prévia compartilhável é um snapshot do momento em que foi criado. Selecione **Regenerate link** para capturar suas alterações mais recentes e obter um novo link.
{% enddetails %}

{% details Por quanto tempo o link permanece ativo? %}
Sete dias a partir do momento em que foi gerado. Se você regenerar o link, o novo link terá sua própria expiração de sete dias, separada do anterior.
{% enddetails %}

{% details Posso revogar um link antecipadamente? %}
Não, você não pode revogar um link. Regenerar o link não invalida o anterior. Todos os links funcionam até expirarem após sete dias.
{% enddetails %}