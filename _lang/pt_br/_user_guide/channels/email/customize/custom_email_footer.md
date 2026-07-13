---
nav_title: Rodapé de e-mail personalizado
article_title: Rodapé de e-mail personalizado
page_order: 6.5
description: "Este artigo descreve como configurar um rodapé de e-mail personalizado em todo o espaço de trabalho."
channel:
  - email

---

# Rodapé de e-mail personalizado {#custom-email-footer}

> Você pode definir um rodapé de e-mail personalizado em todo o espaço de trabalho, que pode ser modelado em cada e-mail usando o atributo Liquid {% raw %}`{{${email_footer}}}`{% endraw %}.

Ao usar rodapés de e-mail personalizados, você não precisa mais criar um novo rodapé para cada modelo de e-mail ou Campaign de e-mail que utilizar. Todas as Campaigns de e-mail novas e existentes refletem as alterações feitas no seu rodapé personalizado. Lembre-se de que a conformidade com a [Lei CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) exige que você inclua um endereço físico da sua empresa e um link de cancelamento de inscrição nos seus e-mails.

{% alert warning %}
É sua responsabilidade garantir que o rodapé personalizado atenda aos requisitos mencionados acima.
{% endalert %}

## Criando seu rodapé personalizado {#create-your-custom-footer}

Para criar ou editar seu rodapé personalizado, faça o seguinte:

1. Acesse **Configurações** > **Preferências de e-mail** > **Páginas e rodapés da inscrição**.
2. Acesse a seção **Rodapé personalizado** e ative os rodapés personalizados.
3. Selecione **Editar** e edite seu rodapé na seção **Redigir**.
4. Selecione **Pré-visualização** para ver como o rodapé do e-mail aparecerá na caixa de entrada do cliente. Opcionalmente, você pode selecionar **Copiar link de pré-visualização** para gerar e copiar um link de pré-visualização compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link será válido por sete dias antes de precisar ser regenerado.
5. Envie uma mensagem de teste.

![Exemplo de um rodapé personalizado.]({% image_buster /assets/img_archive/custom_footer.png %})

O rodapé padrão usa o atributo {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} e nosso endereço postal físico. Se você estiver usando esse padrão, selecione **&#60;other&#62;** para o **Protocolo**.

{% alert important %}
Para cumprir as regulamentações CAN-SPAM, seu rodapé personalizado deve incluir um link de cancelamento de inscrição. Você pode usar o atributo Liquid {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} ou sua própria URL personalizada de cancelamento de inscrição. Não será possível salvar um rodapé personalizado sem um link de cancelamento de inscrição.
{% endalert %}

![Valores de protocolo e URL necessários para o rodapé personalizado.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Rodapés sem links de cancelamento de inscrição {#footers-without-unsubscribe-links}

Tenha muito cuidado ao usar um modelo com o rodapé personalizado {% raw %}`{{${email_footer}}}` mas sem a tag de link de cancelamento de inscrição `{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Um aviso será exibido, mas a decisão de enviar um e-mail com ou sem link de cancelamento de inscrição será sua.

Veja um aviso no criador de e-mail:

![Exemplo de e-mail redigido sem rodapé.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Veja um aviso no criador de Campaign:

![Composição de Campaign sem rodapé.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Adicionando um link personalizado de cancelamento de inscrição {#adding-a-custom-unsubscribe-link}

Para adicionar um link personalizado de cancelamento de inscrição, você pode alterar o link de cancelamento de inscrição no rodapé personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} para um link do seu próprio site com um parâmetro de consulta que inclua o ID do usuário. Um exemplo é:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Em seguida, chame o [endpoint `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) para atualizar o status de inscrição do usuário. Para mais detalhes, consulte nossa documentação sobre [alteração de inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

Depois, salve esse novo link. A tag padrão de cancelamento de inscrição da Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} deve estar no rodapé. Isso significa que você precisa incluir o link padrão "ocultando-o", colocando a tag em um comentário ou em uma tag `<div>` oculta.

## Práticas recomendadas {#best-practices}

Sugerimos as seguintes práticas recomendadas ao criar e usar rodapés personalizados.

### Personalizando com atributos {#personalizing-with-attributes}

Ao criar um rodapé personalizado, a Braze sugere usar [atributos para personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags). O conjunto completo de atributos padrão e personalizados está disponível, mas aqui estão alguns que podem ser úteis:

| Atributo | Tag |
| --------- | --- |
| Endereço de e-mail do usuário | {% raw %}`{{${email_address}}}`{% endraw %} |
| URL personalizada de cancelamento de inscrição do usuário | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Essa tag substitui a tag anterior {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Recomendamos que você use a tag mais recente {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. |
| URL personalizada de opt-in do usuário | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| URL personalizada de inscrição do usuário | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| URL personalizada da Central de Preferências da Braze do usuário | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalizando com atributos" }

### Incluindo um link de cancelamento de inscrição e um link de opt-in {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
Como prática recomendada, a Braze sugere incluir tanto um link de cancelamento de inscrição (como ``{{${set_user_to_unsubscribed_url}}}``) quanto um link de opt-in (como ``{{${set_user_to_opted_in_url}}}``) no seu rodapé personalizado. Dessa forma, os usuários poderão cancelar a inscrição ou fazer opt-in, e você poderá coletar passivamente dados de opt-in de uma parte dos seus usuários.
{% endraw %}

### Configurando rodapés personalizados para e-mails em texto simples {#setting-custom-footers-for-plaintext-emails}

Você também pode configurar um rodapé personalizado para e-mails em texto simples na guia **Páginas e rodapés da inscrição** na página **Preferências de e-mail**, que segue as mesmas regras do rodapé personalizado para e-mails em HTML.

Se você não incluir um rodapé em texto simples, a Braze criará um automaticamente a partir do rodapé HTML. Quando seus rodapés personalizados estiverem do seu agrado, selecione **Salvar**.

![E-mail com a opção Definir rodapé personalizado em texto simples selecionada.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## Considerações {#considerations}

Se você estiver usando o [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio), observe que {% raw %}`{{${email_footer}}}`{% endraw %} não é uma tag Liquid padrão. Ela é pré-processada antes da execução do Liquid, então usar {% raw %}`{{${email_footer}}}`{% endraw %} como valor de variável de contexto e chamar a flag `:rerender` falha silenciosamente. Em vez disso, use um [bloco de conteúdo]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers) para o rodapé de e-mail.