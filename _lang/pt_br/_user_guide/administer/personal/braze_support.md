---
nav_title: Suporte da Braze
article_title: Suporte da Braze
page_order: 4
description: "Esta página ajuda você a localizar o Portal de Suporte da Braze para enviar feedback sobre produtos da Braze. Esta página só está acessível para clientes da Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Suporte da Braze {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Saiba como acessar o Portal de Suporte da Braze, enviar e acompanhar casos de suporte e fornecer as informações necessárias para uma solução de problemas eficiente.

## Acessar o Portal de Suporte {#access-the-support-portal}

Para entrar em contato com a equipe de suporte da Braze, acesse **Support** > **Get help with Operator** para abrir o BrazeAI<sup>TM</sup> Operator.

O Operator pode solucionar seu problema usando o contexto da sua conversa e da tela atual. Se o Operator não conseguir resolver seu problema, peça para ele redigir um ticket de suporte com base na sua conversa e envie o ticket no Portal de Suporte da Braze (se você for um contato de suporte designado). Você também pode selecionar <i class="fa-regular fa-circle-question"></i> **Contact Support** dentro do Operator para registrar um ticket diretamente. Se **Get help with Operator** não estiver disponível no seu dashboard, selecione **Support** > **Get help** para abrir o portal de suporte ou o formulário de suporte.

Para saber mais, consulte [registrar tickets de suporte com o BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets). Se você não tem certeza se é um contato de suporte da Braze, entre em contato com o administrador da Braze da sua empresa, o gerente de sucesso da Braze ou o proprietário da conta.

![O menu suspenso "Support" mostrando "Get help with Operator".]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}

## Adicionando contatos de suporte designados {#adding-designated-support-contacts}

Os contatos de suporte designados podem acessar todos os casos de suporte da sua empresa, independentemente de quem os enviou. Você pode definir usuários como contatos de suporte designados diretamente na página **Editar usuário**.

1. Acesse **Configurações** > **Usuários da empresa** e pesquise o usuário pelo nome ou endereço de e-mail.
2. Selecione o nome do usuário ou passe o cursor sobre a linha do nome do usuário para exibir um menu.
3. No menu, selecione **Editar** para ser redirecionado à página **Editar usuário**.
4. Marque a caixa de seleção **Set this user as a Designated Support Contact for Braze Support Portal**.

### Obtendo acesso {#gaining-access}

Depois que um usuário é designado como contato de suporte, o Portal de Suporte da Braze envia a esse usuário um e-mail de boas-vindas com instruções para configurar o acesso.

## Ver casos da sua empresa {#view-cases-from-your-company}

Se você é um contato de suporte designado, use as visualizações de filtro **My Org's** no portal de suporte para ver todos os casos enviados por usuários da sua empresa. Casos de todos os canais de envio (BrazeAI<sup>TM</sup> Operator, formulário web, e-mail ou portal) estão incluídos nessas visualizações.

## Práticas recomendadas para enviar um caso de suporte {#best-practices-for-submitting-a-support-case}

### Forneça o máximo de informações possível {#provide-as-much-information-as-possible}

Quanto mais insights você puder oferecer, melhor. Inclua detalhes específicos como o espaço de trabalho, a URL da Campaign ou do Segment or segmento e quaisquer IDs externos relevantes. Isso pode nos ajudar a solucionar seu problema com mais eficiência.

### Forneça uma amostra de usuários {#provide-a-sample-of-users}

Compartilhe uma amostra de usuários em vez de todo o Segment or segmento afetado. Fornecer um número menor de usuários nos ajuda a restringir o escopo e acelerar nossas investigações.

### Esclareça o comportamento esperado versus o real {#clarify-expected-versus-actual-behavior}

Informe o que você esperava e o que realmente aconteceu. Isso pode nos ajudar a identificar as possíveis causas do problema.

### Anexe imagens relevantes {#attach-relevant-images}

Considere anexar uma captura de tela para ilustrar o problema. Fornecer essas imagens pode ajudar significativamente na nossa compreensão do problema e acelerar o processo de resolução.

### Avalie o impacto {#assess-the-impact}

Selecione o nível de severidade apropriado para nos ajudar a designar os recursos certos para resolver o problema.

{% alert important %}
Marcar um problema como "Crítico" significa que sua instância de produção está fora do ar e todo o trabalho na Braze foi interrompido.
{% endalert %}

## Solução de problemas de carregamento do dashboard {#troubleshooting-dashboard-load-issues}

Se o dashboard da Braze não estiver carregando corretamente, tente o seguinte antes de entrar em contato com o suporte:

1. Abra o dashboard em um navegador diferente ou em uma janela anônima ou privada.
2. [Limpe o cache e os cookies do seu navegador]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies).
3. Desative bloqueadores de anúncios e extensões do navegador e recarregue o dashboard.
4. Se você usa uma VPN, desconecte e tente novamente.

Se o console de desenvolvedor do seu navegador exibir `ERR_BLOCKED_BY_CLIENT`, uma extensão ou bloqueador de anúncios está bloqueando recursos do dashboard. Desative o bloqueador para a URL do seu dashboard da Braze e recarregue a página.

## Solução de problemas de acesso {#troubleshooting-access}

Se você receber um erro ao fazer login no Portal de Suporte da Braze, como `Check your entry`, verifique se seguiu o link no seu e-mail de boas-vindas para definir uma senha para o portal. Se você já fez isso ou conseguia fazer login no portal anteriormente, crie um ticket de suporte.