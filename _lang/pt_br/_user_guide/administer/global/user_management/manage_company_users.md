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

1. Acesse **Configurações** > **Gerenciamento de usuários** > **Usuários da empresa**.
2. Selecione **+ Add New User**.
3. Insira as informações solicitadas, incluindo e-mail, departamento e [função do usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role).
4. Para usuários que não são administradores, selecione as [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions) no nível da empresa e no nível do espaço de trabalho que você deseja que esse usuário tenha.

![Permissões no nível do espaço de trabalho com uma seção para campos de permissões personalizadas.]({% image_buster /assets/img/add_new_user_3.png %})

### Requisitos de endereço de e-mail {#email-address-requirements}

Cada endereço de e-mail usado em uma [instância]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) deve ser único. Isso significa que, se você tentar adicionar um endereço de e-mail que já está associado a um usuário que teve ou ainda tem acesso a um espaço de trabalho da empresa nessa instância, verá uma mensagem de erro.

Se sua equipe usa o Gmail e você está tendo problemas para adicionar um endereço de e-mail, é possível criar um alias adicionando um sinal de mais (+) como "+1" ou "+test" ao endereço de e-mail. Por exemplo, `contractor@braze.com` pode ter o alias `contractor+1@braze.com`. E-mails enviados para `contractor+1@braze.com` ainda serão entregues em `contractor@braze.com`, mas o alias será reconhecido como um endereço de e-mail único.

Para usar uma conta em várias empresas sem aliases, consulte [Usar desenvolvedores multiempresa]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#use-multi-company-developers). Se você usa SSO, revise [Considerações sobre login único (SSO)]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#considerations-for-single-sign-on-sso) antes de se registrar com vários endereços de e-mail.

### Posso alterar o endereço de e-mail da minha conta da Braze? {#can-i-change-my-braze-accounts-email-address}

Por motivos de segurança, os usuários não podem alterar o endereço de e-mail associado à sua conta da Braze. Se um usuário quiser atualizar seu endereço de e-mail, um administrador deve [criar uma nova conta](#adding-company-users) para ele com o endereço de e-mail desejado.

## Atribuindo acesso e responsabilidades ao usuário {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Suspendendo usuários da empresa {#suspending-company-users}

Suspender um usuário coloca a conta dele em um estado inativo, no qual o usuário não pode mais fazer login, mas os dados associados à conta são preservados. Somente administradores podem suspender ou reativar usuários da empresa. Observe que usuários suspensos ainda podem receber notificações da Braze.

Para suspender um usuário, acesse **Configurações** > **Gerenciamento de usuários** > **Usuários da empresa**, encontre o nome de usuário e selecione <i class="fa-solid fa-user-lock" aria-label="Suspender"></i> **Suspend**.

![Opção para suspender um usuário.]({% image_buster /assets/img_archive/suspend_user.png %})

Os administradores também podem suspender um usuário selecionando o nome dele na lista e clicando em **Suspend user** no rodapé.

![Suspender um usuário ao editar os detalhes do usuário.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Excluindo usuários da empresa {#deleting-company-users}

Para excluir um usuário, acesse **Configurações** > **Gerenciamento de usuários** > **Usuários da empresa**, encontre o nome do usuário e selecione <i class="fa fa-trash-can" aria-label="Excluir usuário"></i> **Delete user**.

Somente administradores podem excluir usuários da empresa, e os usuários não podem excluir suas próprias contas. Um administrador não pode excluir sua própria conta do dashboard; outro administrador deve fazer isso por ele.

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

A Braze manterá os seguintes dados da conta:

- Atributos personalizados ou dados de teste associados à conta
- Campaigns ou Canvas criados pelo usuário (mas o nome do usuário não aparecerá neles, como na coluna **Last edited by**)

### Impacto da exclusão de um usuário do dashboard {#impact-of-deleting-a-dashboard-user}

Quando um usuário do dashboard é excluído, não há impacto significativo nos ativos que ele criou dentro do dashboard, como campanhas, segmentos e Canvas. No entanto, o campo **Created By** desses ativos exibirá um valor "null" em vez do endereço de e-mail do usuário excluído.

Se um novo usuário do dashboard for criado posteriormente com o mesmo endereço de e-mail do usuário excluído, a Braze não reassociará os ativos criados pelo usuário excluído ao novo usuário. O novo usuário do dashboard começará do zero e não será creditado como criador de nenhum ativo existente no dashboard.

## Solução de problemas {#troubleshooting}

### "Unable to perform action" ao adicionar um usuário {#unable-to-perform-action-when-adding-a-user}

Se a adição de um usuário do dashboard falhar com o erro "Unable to perform action" (ou similar):

- Remova espaços iniciais ou finais e caracteres ocultos do endereço de e-mail.
- Confirme se o endereço está em um formato de e-mail válido para a sua organização. Alguns caracteres especiais são rejeitados.
- O mesmo e-mail não pode ser usado para dois usuários do dashboard no mesmo [cluster]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Se o endereço já estiver registrado em outro espaço de trabalho nesse cluster, use um endereço diferente ou um alias como `user+1@company.com`.

### "Email is already taken" ao tentar adicionar um usuário {#email-is-already-taken-when-trying-to-add-a-user}

Se você tentar adicionar um novo usuário e receber um erro informando que o e-mail já está em uso, mas não conseguir encontrá-lo na sua lista de usuários, esse usuário provavelmente existe em uma instância diferente do mesmo cluster do dashboard da Braze.

Para criar esse novo usuário, você pode fazer uma das seguintes opções:

1. Excluir o usuário da outra instância antes de criá-lo na nova, ou
2. Criar o usuário com uma string de e-mail diferente (como `testing+01@braze.com`) ou outro alias de e-mail.

Se você não receber a mensagem de ativação na sua caixa de entrada ao usar `testing+01@braze.com`, confirme com sua equipe de TI se é possível receber mensagens desse tipo de endereço de e-mail. Alguns administradores filtram mensagens enviadas para endereços de e-mail com `+`.

## Próximas etapas {#next-steps}

Após adicionar usuários, gerencie o acesso deles:

- [Permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para configurar o que cada usuário pode fazer no dashboard.
- [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) para organizar usuários em grupos com acesso compartilhado a objetos específicos do dashboard.