---
nav_title: Formulários de várias etapas
article_title: Formulários de landing page de várias etapas
page_order: 2
page_type: reference
description: "Saiba como criar um formulário de várias etapas em uma landing page da Braze, gerenciar etapas no editor de arrastar e soltar e personalizar a etapa de confirmação integrada."
---

# Formulários de landing page de várias etapas {#multi-step-landing-page-forms}

> Divida um formulário longo de landing page em várias etapas, cada uma com seus próprios campos, para que os usuários avancem pelo formulário uma etapa de cada vez. Todo formulário de várias etapas inclui uma etapa de confirmação bloqueada, para que os usuários sempre vejam uma confirmação após o envio.

## Pré-requisitos {#prerequisites}

Para acessar o construtor de landing pages, você precisa de [determinadas permissões]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Se você não tiver acesso, peça ajuda ao administrador da Braze.

Você também deve estar familiarizado com os [blocos de formulário de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page).

## Como funcionam os formulários de várias etapas {#how-multi-step-forms-work}

Para criar um formulário de várias etapas, adicione uma linha **Form** na seção **Layout** do painel **Build**. A linha **Form** inclui botões de ação integrados e suporte a várias etapas, então você não precisa montar a estrutura da linha manualmente.

Você pode adicionar apenas uma linha **Form** por landing page. Quando você a arrasta para a página, ela começa com uma única etapa e uma etapa de confirmação bloqueada que é executada após o envio.

{% alert note %}
Como a linha **Form** gerencia sua própria navegação de várias etapas, todas as suas etapas ficam dentro dessa única linha em uma página. Isso é diferente da abordagem padrão de criar um formulário de etapa única e vincular o botão **Submit** a uma landing page de confirmação separada. Para saber mais, consulte [Etapa 4: Criar uma página de confirmação]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional).
{% endalert %}

![Um formulário de landing page de várias etapas no criador de landing pages.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## Adicionar um formulário de várias etapas {#add-a-multi-step-form}

1. No editor de landing pages, acesse o painel **Build** e selecione **Layout**.
2. Arraste a linha **Form** para a sua página.
3. Com a linha **Form** selecionada, use a seção **Steps** no painel de propriedades do lado direito para construir seu formulário:
   - Adicione [blocos de formulário]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) (como **Email Capture**, **Phone Capture**, **Input Field**, **Dropdown**, **Checkbox** ou **Checkbox Group**) à **Step 1**.
   - Selecione **Add step** para criar etapas adicionais e adicione blocos de formulário a cada uma.

Por exemplo, um formulário de três etapas pode solicitar um nome na **Step 1**, um número de telefone na **Step 2** e, em seguida, chegar à etapa **Confirmation** para agradecer ao usuário pelo envio.

## Navegar entre etapas durante a edição {#navigate-between-steps-while-editing}

Mova-se entre as etapas no editor de duas maneiras:

| Método | Como fazer |
|--------|--------|
| Navegador de etapas | No canvas, use o controle **Step X of Y** para ir para a etapa anterior ou seguinte. |
| Painel de etapas | Selecione a linha **Form** e, em seguida, use a seção **Steps** no painel de propriedades do lado direito para ir diretamente a uma etapa, incluindo a etapa **Confirmation**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Navegar entre etapas durante a edição" }

## Gerenciar etapas {#manage-steps}

Use a seção **Steps** no painel de propriedades da linha **Form** para adicionar, remover e reordenar etapas:

| Ação | Como fazer |
|--------|--------|
| Adicionar uma etapa | Selecione **Add step**. Novas etapas são adicionadas após as etapas existentes e antes da etapa **Confirmation**. |
| Remover uma etapa | Selecione o ícone de lixeira ao lado da etapa que deseja remover.<br><br>Observe que a etapa **Confirmation** não possui ícone de lixeira e não pode ser removida ou reordenada. Ela sempre é executada por último, após o usuário concluir as etapas anteriores. |
| Reordenar etapas | Use a alça de arraste ao lado de uma etapa para alterar sua ordem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gerenciar etapas" }

## Personalizar a etapa de confirmação {#customize-the-confirmation-step}

Todo formulário de várias etapas inclui uma etapa **Confirmation** listada em **After submission** na seção **Steps**. Essa etapa é bloqueada para que não possa ser excluída, o que significa que os usuários sempre verão uma experiência de confirmação após enviarem o formulário.

Embora a etapa **Confirmation** não possa ser removida, você pode personalizá-la como qualquer outra etapa: selecione-a na seção **Steps** e, em seguida, adicione e estilize blocos para criar sua mensagem de confirmação.

## Rastrear dados de formulários parcialmente preenchidos {#track-data-from-partially-completed-forms}

Se um usuário sair do formulário antes de chegar à etapa **Confirmation**, a Braze ainda salva os dados de todas as etapas concluídas no perfil de usuário. O evento **Submitted a Landing Page form** não é registrado até que o usuário conclua todas as etapas e chegue à etapa **Confirmation**.

{% alert note %}
O [redirecionamento e a entrega por disparo]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users) dependem do evento **Submitted a Landing Page form**. Um usuário que envia algumas etapas, mas não todas, tem os dados salvos no perfil, mas não é incluído nesse evento — mesmo que seus dados parciais tenham sido capturados.
{% endalert %}

Isso difere das [pesquisas de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys), em que um usuário que não chega à etapa final é rastreado como um envio parcial.

## Limitações e considerações {#limitations-and-considerations}

- Uma landing page suporta uma única linha **Form**, então todas as suas etapas e a etapa de confirmação ficam nessa única linha.
- Você pode adicionar até 10 etapas de coleta de dados. A etapa **Confirmation** não conta para esse limite.
- Cada etapa inclui um botão padrão com comportamento ao clicar configurado para ir para a próxima etapa. Essa ação valida e salva as entradas da etapa atual; na última etapa de coleta de dados, ela também registra o evento **Submitted a Landing Page form** e avança para **Confirmation**. Se uma etapa não estiver conectada, adicione o comportamento ao clicar para que o botão vá para a próxima etapa. Para saber mais, consulte [Button]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) em Blocos do editor.
- Você não precisa criar ou vincular uma segunda landing page para servir como experiência de confirmação, pois a etapa **Confirmation** é integrada à linha **Form**.
- Se você não vir a linha **Form** em **Layout**, entre em contato com o gerente de conta da Braze.