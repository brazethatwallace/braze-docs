---
nav_title: Criar um modelo de e-mail
article_title: Criar um modelo de e-mail
page_order: 0
description: "Este artigo de referência aborda como criar, personalizar e gerenciar modelos de e-mail."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Criar um modelo de e-mail {#create-an-email-template}

> O dashboard da Braze tem um editor de modelos de e-mail que permite criar e-mails personalizados e visualmente atraentes, salvando-os para uso posterior em Campaigns. Você também pode fazer upload do seu próprio [modelo de e-mail HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template).

## Etapa 1: Acesse o editor de modelos de e-mail {#step-1-navigate-to-the-email-template-editor}

No dashboard da Braze, acesse **Content** > **Email**.

## Etapa 2: Selecione sua experiência de edição {#step-2-select-your-editing-experience}

Selecione entre o **editor de arrastar e soltar** ou o **editor de código HTML** para sua experiência de edição.

Você também pode escolher entre modelos predefinidos da Braze, criar um novo modelo ou editar um modelo existente (simples ou [responsivo para dispositivos móveis]({{site.baseurl}}/releases/2018/may#mobile-responsive-email-templates)).

![Um modelo de e-mail para a promoção de primavera de uma empresa com opções para selecionar o editor de arrastar e soltar ou o editor de HTML, ou para selecionar entre modelos da Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Quaisquer modelos HTML personalizados existentes devem ser recriados usando o editor de arrastar e soltar.
{% endalert %}

## Etapa 3: Personalize seu modelo {#step-3-customize-your-template}

Após selecionar sua experiência de editor, essa é a oportunidade de ser criativo na personalização do seu modelo de e-mail. Você pode usar HTML para criar e reproduzir a identidade da sua marca no editor de HTML, ou incluir uma variedade de [detalhes criativos]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) no editor de arrastar e soltar.

### Incluir um link de cancelamento de inscrição {#include-an-unsubscribe-link}

Ao criar seu modelo de e-mail, se você não incluir um link de cancelamento de inscrição, a Braze solicitará que você adicione um no seu e-mail, pois ele é exigido por lei em todos os e-mails de marketing. Você pode adicionar esse link de cancelamento de inscrição como um rodapé na parte inferior dos seus e-mails usando a Liquid tag {% raw %}``${email_footer}``{% endraw %}, ou [personalizando o rodapé]({{site.baseurl}}/user_guide/channels/email/subscriptions#custom-footer) no seu modelo.

## Etapa 4: Verificar erros de e-mail {#step-4-check-for-email-errors}

Os erros de e-mail são apresentados na guia **Composição** do fluxo de trabalho da mensagem. Os erros impedem que você avance. "Avisos" indicam lembretes para ajudar a seguir as práticas recomendadas. Dependendo do seu negócio, você pode optar por ignorá-los.

![Lista de erros e avisos de um exemplo de e-mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Aqui está uma lista de erros que são verificados em nosso editor:

- Sintaxe Liquid incorreta
- [Corpos de e-mail maiores que 400 kb; é altamente recomendado que os corpos tenham menos de 102 kb]({{site.baseurl}}/user_guide/channels/email/best_practices)
- Modelos sem link de cancelamento de inscrição
- E-mails com **Corpo** ou **Assunto** em branco
- E-mails sem link de cancelamento de inscrição

## Etapa 5: Visualize e teste sua mensagem {#step-5-preview-and-test-your-message}

Após terminar de compor seu modelo, você pode testá-lo antes de enviá-lo.

Na parte inferior da tela de visão geral, selecione **Preview and Test**. Aqui, você pode visualizar como seu e-mail aparecerá na caixa de entrada de um cliente. Com **Preview as User** selecionado, você pode visualizar seu e-mail como um usuário aleatório, selecionar um usuário específico ou criar um usuário personalizado. Isso permite testar se suas chamadas de Connected Content e personalização estão funcionando como esperado.

Em seguida, você pode selecionar **Copy preview link** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail aparece para um usuário aleatório. Para saber mais, consulte [Prévia compartilhável]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

Você também pode alternar entre as visualizações de desktop, dispositivo móvel e texto simples para ter uma ideia de como sua mensagem aparece em diferentes contextos.

{% alert tip %}
Curioso para saber como seu e-mail aparece para usuários no modo escuro? Selecione o botão **Dark Mode Preview** localizado na seção **Preview and Test** (somente no editor de arrastar e soltar).
{% endalert %}

Quando estiver pronto para uma verificação final, selecione **Test Send** e envie uma mensagem de teste para você mesmo ou para um grupo de testadores de conteúdo para garantir que seu e-mail seja exibido corretamente em diversos dispositivos e clientes de e-mail.

![Exemplo de prévia de e-mail a ser enviada para teste.]({% image_buster /assets/img_archive/newEmailTest.png %})

Se você encontrar algum problema com seu modelo ou quiser fazer alterações, selecione **Edit Email** para retornar ao editor. Observe que as edições feitas no editor **Classic** podem não ser refletidas no editor de HTML ou na prévia do e-mail.

## Etapa 6: Salve seu modelo {#step-6-save-your-template}

Salve seu modelo selecionando **Save Template**. Agora você pode usar esse modelo em qualquer Campaign ou componente do Canvas que quiser. Para acessar seu modelo, selecione a experiência de edição com a qual você o criou e, em seguida, selecione-o na lista de modelos disponíveis.

{% alert note %}
Se você fizer qualquer edição em um modelo existente, essas alterações não serão refletidas em Campaigns criadas usando versões anteriores desse modelo.
{% endalert %}

### Gerencie seus modelos {#manage-your-templates}

Você pode visualizar modelos de e-mail em **Templates** > **Email Templates**, filtrando por status, tipo, tags, o usuário que o criou, ou pesquisando pelo nome do modelo. Você precisa das permissões de usuário relevantes, como **View Email Templates**, para visualizar esses modelos. Para saber mais, consulte [Permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

À medida que você cria mais modelos de e-mail, pode [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicating-templates) e [arquivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archiving-templates) modelos de e-mail. Saiba mais sobre como criar e gerenciar sua biblioteca de modelos e conteúdo criativo em [Modelos e mídia]({{site.baseurl}}/user_guide/messaging/templates).

### Use seus modelos em Campaigns de API {#use-your-templates-in-api-campaigns}

Para usar seu e-mail em uma Campaign de API, você precisa de um `email_template_id`, que pode ser encontrado na parte inferior de qualquer modelo de e-mail criado na Braze.

![Identificador de API localizado na parte inferior de um modelo de e-mail.]({% image_buster /assets/img/email_templates/template5.png %})

### Comente em modelos de e-mail {#comment-on-email-templates}

Você pode colaborar e comentar em modelos de e-mail no editor de arrastar e soltar.

1. Selecione o bloco de conteúdo ou a linha no corpo do e-mail em que você deseja comentar.
2. Selecione o ícone de comentário <i class="fas fa-comment" aria-label="Comentário"></i>.
3. Insira seu comentário na barra lateral e selecione **Submit**.
4. Após inserir seus comentários, selecione **Done**.
5. Selecione **Save Template** para salvar seus comentários.

Após o modelo ser salvo, os usuários poderão ver ícones sobre comentários não resolvidos. Selecione **Resolve** para resolver esses comentários.

![Um comentário em modelo de e-mail que diz "Looks good to me".]({% image_buster /assets/img/email_templates/template_comment.png %})

Para respostas a perguntas frequentes sobre modelos de e-mail, consulte nosso [FAQ de modelos]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).