---
nav_title: Usuários da empresa
article_title: Gerenciar usuários da empresa
page_order: 0
page_type: reference
description: "Esta página aborda o gerenciamento dos usuários da sua empresa, como adicionar e excluir usuários, definir permissões de usuário, criar equipes e gerenciar configurações da empresa."
---

# Gerenciar usuários da empresa {#manage-company-users}

> Saiba como gerenciar usuários na conta da sua empresa, incluindo adicionar, suspender e excluir usuários.

## Adicionando usuários da empresa {#adding-company-users}

Você precisa ter permissões de administrador para adicionar usuários à sua conta da Braze.

Para adicionar um novo usuário:

1. Acesse **Configurações** > **Configurações da empresa** > **Gerenciamento de usuários** > **Usuários da empresa**.
2. Selecione **+ Adicionar novo usuário**.
3. Insira as informações conforme solicitado, incluindo e-mail, departamento e [função do usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role).
4. Para usuários que não são administradores, selecione as [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions) no nível da empresa e no nível do espaço de trabalho que você deseja que esse usuário tenha.

![Permissões no nível do espaço de trabalho com uma seção para campos de permissões personalizadas.]({% image_buster /assets/img/add_new_user_3.png %})

### Requisitos de endereço de e-mail {#email-address-requirements}

Cada endereço de e-mail usado em uma [instância]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) deve ser único. Isso significa que, se você tentar adicionar um endereço de e-mail que já está associado a um usuário que teve ou ainda tem acesso a um espaço de trabalho da empresa nessa instância, uma mensagem de erro será exibida.

Se sua equipe usa Gmail e está tendo problemas para adicionar um endereço de e-mail, você pode criar um alias adicionando um sinal de mais (+) como "+1" ou "+test" ao endereço de e-mail. Por exemplo, `contractor@braze.com` pode ter um alias de `contractor+1@braze.com`. E-mails enviados para `contractor+1@braze.com` ainda são entregues em `contractor@braze.com`, mas o alias é reconhecido como um endereço de e-mail único.

Para usar uma conta em várias empresas sem aliases, consulte [Usar desenvolvedores multiempresa]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#use-multi-company-developers). Se você usa SSO, revise [Considerações sobre Single Sign-On (SSO)]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#considerations-for-single-sign-on-sso) antes de se registrar com vários endereços de e-mail.

### Posso alterar o endereço de e-mail da minha conta da Braze? {#can-i-change-my-braze-accounts-email-address}

Por motivos de segurança, os usuários não podem alterar o endereço de e-mail associado à sua conta da Braze. Se um usuário deseja atualizar seu endereço de e-mail, um administrador deve [criar uma nova conta](#adding-company-users) para ele com o endereço de e-mail de sua preferência.

## Atribuindo acesso e responsabilidades dos usuários {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Suspendendo usuários da empresa {#suspending-company-users}

Suspender um usuário coloca a conta dele em um estado inativo, onde o usuário não pode mais fazer login, mas os dados associados à conta são preservados. Apenas administradores podem suspender ou reativar usuários da empresa. Observe que usuários suspensos ainda podem receber notificações da Braze.

Para suspender um usuário, acesse **Configurações** > **Configurações da empresa** > **Gerenciamento de usuários** > **Usuários da empresa**, encontre o nome de usuário e selecione <i class="fa-solid fa-user-lock" aria-label="Suspender usuário"></i> **Suspender**.

![Opção para suspender um usuário.]({% image_buster /assets/img_archive/suspend_user.png %})

Os administradores também podem suspender um usuário selecionando o nome na lista e escolhendo **Suspender usuário** no rodapé.

![Suspender um usuário ao editar os detalhes do usuário.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Excluindo usuários da empresa {#deleting-company-users}

Para excluir um usuário, acesse **Configurações** > **Configurações da empresa** > **Gerenciamento de usuários** > **Usuários da empresa**, encontre o nome do usuário e selecione <i class="fa fa-trash-can"></i> **Excluir usuário**.

Somente administradores podem excluir usuários da empresa, e os usuários da empresa não podem excluir suas próprias contas. Um administrador não pode excluir sua própria conta do dashboard; outro administrador deve fazer isso por ele.

![Excluir um usuário.]({% image_buster /assets/img_archive/delete_user_new.png %})

Após a exclusão de um usuário, a Braze não mantém nenhum dos seguintes dados da conta:

- Quaisquer atributos que o usuário possuía
- Endereço de e-mail
- Número de telefone
- ID de usuário externo
- Gênero
- País
- Idioma
- Outros dados semelhantes

A Braze mantém os seguintes dados da conta:

- Atributos personalizados ou dados de teste associados à conta
- Campaigns ou Canvas que o usuário criou (mas o nome do usuário não aparecerá neles, como na coluna **Última edição por**)

### Impacto da exclusão de um usuário do dashboard {#impact-of-deleting-a-dashboard-user}

A exclusão de um usuário do dashboard não afeta significativamente os ativos que ele criou no dashboard, como campanhas, Segments e Canvas. No entanto, o campo **Criado por** desses ativos exibe um valor "nulo" em vez do endereço de e-mail do usuário excluído.

Se um novo usuário do dashboard for criado posteriormente com o mesmo endereço de e-mail do usuário excluído, a Braze não reassocia os ativos criados pelo usuário excluído ao novo usuário. O novo usuário do dashboard começa do zero e não é creditado como criador de nenhum ativo existente no dashboard.

## Solução de problemas {#troubleshooting}

### "Não foi possível realizar a ação" ao adicionar um usuário {#unable-to-perform-action-when-adding-a-user}

Se a adição de um usuário do dashboard falhar com o erro "Unable to perform action" (ou similar):

- Remova espaços iniciais, finais e caracteres ocultos do endereço de e-mail.
- Confirme se o endereço está em um formato de e-mail válido para sua organização. Alguns caracteres especiais são rejeitados.
- O mesmo e-mail não pode ser usado para dois usuários do dashboard no mesmo [cluster]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Se o endereço já estiver registrado em outro espaço de trabalho nesse cluster, use um endereço diferente ou um alias como `user+1@company.com`.

### "E-mail já está em uso" ao tentar adicionar um usuário {#email-is-already-taken-when-trying-to-add-a-user}

Se você tentar adicionar um novo usuário e receber um erro informando que o e-mail já está em uso, mas não conseguir encontrá-lo na sua lista de usuários, esse usuário provavelmente existe em uma instância diferente do mesmo cluster do dashboard da Braze.

Para criar esse novo usuário, você pode fazer uma das seguintes opções:

1. Excluir o usuário da outra instância antes de criá-lo na nova, ou
2. Criar o usuário com um endereço de e-mail diferente (como `testing+01@braze.com`) ou outro alias de e-mail.

Se você não receber a mensagem de ativação na sua caixa de entrada ao usar `testing+01@braze.com`, confirme com sua equipe de TI se é possível receber mensagens desse tipo de endereço de e-mail. Alguns administradores filtram mensagens enviadas para endereços de e-mail com `+`.

## Próximas etapas {#next-steps}

Após adicionar usuários, gerencie o acesso deles:

{% article_tiles %}
- name: Permissões
  link: /docs/user_guide/administer/global/user_management/permissions
  description: Configure o que cada usuário pode fazer no dashboard.
- name: Equipes
  link: /docs/user_guide/administer/global/user_management/teams
  description: Organize os usuários em grupos com acesso compartilhado a objetos específicos do dashboard.
{% endarticle_tiles %}