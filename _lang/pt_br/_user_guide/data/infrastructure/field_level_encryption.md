---
nav_title: Criptografia em nível de campo do identificador
article_title: Criptografia em nível de campo do identificador
page_order: 2
alias: "/field_level_encryption/"
description: "Este artigo de referência aborda como criptografar endereços de e-mail para minimizar as informações de identificação pessoal (IPI) compartilhadas na Braze."
page_type: reference
---

# Criptografia em nível de campo do identificador {#identifier-field-level-encryption}

> Criptografe endereços de e-mail para minimizar as informações de identificação pessoal (IPI) compartilhadas na Braze.

{% multi_lang_include data_activation/field_level_encryption_pii_description.md %}

{% alert important %}
A criptografia em nível de campo do identificador está disponível como um recurso complementar. Para começar com a criptografia em nível de campo do identificador, entre em contato com seu gerente de conta da Braze.
{% endalert %}

## Como funciona {#how-it-works}

Os endereços de e-mail devem ser hasheados e criptografados antes de serem adicionados à Braze. Quando uma mensagem é enviada, uma chamada será feita ao AWS KMS para obter o endereço de e-mail descriptografado. Em seguida, o endereço de e-mail hasheado será inserido nos metadados para que os eventos de entrega e engajamento possam ser vinculados ao usuário original. É assim que a Braze consegue rastrear a análise de dados de e-mail. A Braze vai redigir quaisquer endereços de e-mail em texto simples que estejam incluídos e não armazenará o endereço de e-mail em texto simples do usuário.

## Pré-requisitos {#prerequisites}

Para usar a criptografia de campo em nível de identificador, você deve ter acesso ao AWS KMS para [criptografar](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) e [gerar hash](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) de endereços de e-mail **antes** de enviá-los à Braze.

Siga estas etapas para configurar seu método de autenticação de chave secreta da AWS.

1. Para recuperar seu ID de chave de acesso e chave de acesso secreta, [crie um usuário IAM e um grupo de administradores](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) na AWS com uma política de permissões para o AWS Key Management Service. O usuário IAM deve ter as permissões [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) e [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Para mais detalhes, consulte [Permissões do AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Selecione **Show User Security Credentials** para revelar seu ID de chave de acesso e chave de acesso secreta. Anote essas credenciais em algum lugar ou selecione o botão **Download Credentials**, pois você precisará inseri-las ao conectar suas chaves do AWS KMS.
3. Você deve configurar o KMS nas seguintes regiões da AWS:
    - **Clusters Braze US:** `us-east-1`
    - **Clusters Braze EU:** `eu-central-1`
    - **Cluster Braze AU:** `ap-southeast-2`
    - **Cluster Braze ID:** `ap-southeast-3`
    - **Cluster Braze JP:** `ap-northeast-1`
4. No AWS Key Management Service, crie duas chaves e certifique-se de que o usuário IAM foi adicionado nas permissões de uso da chave:
    - **[Criptografar/descriptografar](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Selecione o tipo de chave **Symmetric** e o uso de chave **Encrypt and Decrypt**.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Selecione o tipo de chave **Symmetric** e o uso de chave **Generate and Verify MAC**. A especificação da chave deve ser **HMAC_256**. Após criar a chave, anote o ID da chave HMAC em algum lugar, pois você precisará inseri-lo na Braze.

![Configurações de chave com as opções symmetric, generate and verify MAC e HMAC_256 selecionadas.]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Etapa 1: Conectar suas chaves do AWS KMS {#step-1-connect-your-aws-kms-keys}

No dashboard da Braze, acesse **Configurações de Dados** > **Criptografia em Nível de Campo**. Para suas configurações do AWS KMS, insira o seguinte:

- ID da chave de acesso
- Chave de acesso secreta
- Identificador da chave HMAC (ID da chave ou ARN da chave; não pode ser atualizado após salvar)

## Etapa 2: Selecione os campos criptografados {#step-2-select-your-encrypted-fields}

Em seguida, selecione **Email address** para criptografar o campo.

Quando a criptografia é ativada para um campo, ela não pode ser revertida para um campo descriptografado. Isso significa que a criptografia é uma configuração permanente. Ao configurar a criptografia para o endereço de e-mail, confirme que nenhum usuário tem endereços de e-mail no espaço de trabalho. Isso garante que nenhum endereço de e-mail em texto simples seja armazenado na Braze quando o recurso for ativado para o espaço de trabalho.

![Configurações de criptografia em nível de campo.]({% image_buster /assets/img/field_level_encryption.png %})

## Etapa 3: Importar e atualizar usuários {#step-3-import-and-update-users}

Quando a criptografia no nível do campo de identificador está ativada, você deve aplicar hash e criptografar o endereço de e-mail antes de adicioná-lo à Braze. Certifique-se de converter o endereço de e-mail para letras minúsculas antes de aplicar o hash. Consulte [objeto de atributos do usuário](#user-attributes-object) para mais detalhes.

Ao atualizar o endereço de e-mail na Braze, você deve usar o valor de e-mail com hash sempre que `email` estiver incluído. Isso inclui:

- Endpoints REST or transferir estado representacional:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Adicionar ou atualizar usuários via CSV

{% alert note %}
Ao criar um novo usuário com um endereço de e-mail, você deve adicionar `email_encrypted` com o valor de e-mail criptografado do usuário. Caso contrário, o usuário não será criado. Da mesma forma, se você estiver adicionando um endereço de e-mail a um usuário existente que não possui um e-mail, deve adicionar `email_encrypted`. Caso contrário, o usuário não será atualizado.
{% endalert %}

## Considerações {#considerations}

Estes recursos não são compatíveis com a criptografia em nível de campo de identificador:

- Identificação e captura de endereço de e-mail via SDK or kit de desenvolvimento de software
- Formulários de captura de e-mail em mensagens no app
- Relatórios sobre domínio do destinatário, incluindo gráficos de provedores de caixa de entrada do Email Insights
- Filtro de endereço de e-mail por expressão regular
- Audience sync
- Integração com Shopify

### Objeto de atributos do usuário {#user-attributes-object}

Ao usar a criptografia em nível de campo de identificador com o endpoint `/users/track`, observe estes detalhes de campo para o [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- O campo `email` deve ser o valor com hash do e-mail.
- O campo `email_encrypted` deve ser o valor criptografado do e-mail.

## Perguntas frequentes {#frequently-asked-questions}

### Qual é a diferença entre criptografia e hashing? {#what-is-the-difference-between-encrypting-and-hashing}

A criptografia é uma função bidirecional em que é possível criptografar e descriptografar dados. Se o mesmo valor em texto simples for criptografado várias vezes, o algoritmo de criptografia da AWS (AES-256-GCM) gerará valores criptografados diferentes. O hashing é uma função unidirecional em que o texto simples é embaralhado de uma forma que não pode ser descriptografada. O hashing sempre gera o mesmo valor. Isso nos permite manter estados de inscrição entre vários usuários que compartilham o mesmo endereço de e-mail.

### Qual endereço de e-mail devo usar no meu envio de teste? {#what-email-address-should-i-use-in-my-test-send}

Endereços de e-mail em texto simples são aceitos no envio de teste. Para ver como um e-mail fica para um usuário específico, faça o seguinte:

1. Selecione **prévia message as a user**.
2. Em **Test Send**, selecione **Override recipients attributes with current prévia user's attributes**.

### Posso usar um ARN para a chave HMAC? {#can-i-use-an-arn-for-the-hmac-key}

Sim. Em **Data Settings** > **Field-Level Encryption**, o identificador da chave HMAC aceita um ID de chave ou um ARN de chave.

### Como removo ou redefino uma chave HMAC? {#how-do-i-remove-or-reset-an-hmac-key}

Não é possível remover ou redefinir uma chave HMAC no dashboard após salvá-la. Para solicitar a redefinição de uma chave HMAC ou a remoção da configuração de criptografia em nível de campo do identificador, entre em contato com o gerente da sua conta Braze ou abra um [ticket de suporte]({{site.baseurl}}/braze_support).

{%raw%}
### O que acontece se eu adicionar este endereço de e-mail Liquid `{{${email_address}}}` na Braze? {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

A Braze renderizará o endereço de e-mail em texto simples ao enviar o e-mail. Nas prévias, exibiremos a versão criptografada do e-mail. Recomendamos usar o ID externo do usuário se você estiver referenciando um usuário em uma URL de clique único personalizada.

`{{${email_address}}}` não é compatível atualmente com a Central de Preferências e as páginas de cancelamento de inscrição.
{%endraw%}

### Qual endereço de e-mail devo esperar ver no Currents? {#what-email-address-should-i-expect-to-see-in-currents}

O endereço de e-mail com hash é incluído nos eventos de entrega e engajamento de e-mail.

### Qual endereço de e-mail devo esperar ver no arquivamento de mensagens? {#what-email-address-should-i-expect-to-see-in-message-archiving}

O endereço de e-mail em texto simples é incluído no arquivamento de mensagens. Eles são enviados diretamente ao provedor de armazenamento em nuvem do cliente, e pode haver outros dados pessoais incluídos no corpo dos e-mails.

### Posso usar mail-to list-unsubscribe para gerenciamento de inscrições com criptografia em nível de campo do identificador? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

Não. Usar mail-to list-unsubscribe enviaria o endereço de e-mail descriptografado em texto simples para a Braze. Com a criptografia em nível de campo do identificador ativada, oferecemos suporte ao método baseado em URL HTTP:, incluindo clique único. Também recomendamos incluir um link de cancelamento de inscrição com clique único no corpo do seu e-mail.

### A criptografia em nível de campo do identificador é compatível com outros identificadores, como telefone? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

Não. Atualmente, a criptografia em nível de campo do identificador é compatível apenas com endereços de e-mail.