---
nav_title: Importe sua lista de e-mails
article_title: Importe sua lista de e-mails para a Braze
page_order: 4
page_type: reference
description: "Este artigo de referência aborda as práticas recomendadas para a importação de sua lista de e-mails para a Braze."
channel: email

---

# Importe sua lista de e-mails para a Braze {#importing-email-lists}

> Uma etapa importante para se tornar um remetente de e-mail bem-sucedido é garantir que você tenha uma lista de e-mails de alta qualidade. O gerenciamento adequado da lista de e-mails pode melhorar a entregabilidade e fornecer resultados de campanha mais precisos e limpos.

## Considerações antes de importar {#considerations-before-importing}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Valide suas listas de e-mail {#validate-your-email-lists}

Antes de importar sua lista de e-mails para a Braze, valide se sua lista inclui apenas endereços de e-mail genuínos. Uma alta taxa de bounce pode prejudicar a reputação do seu remetente de e-mail.

Os serviços de limpeza de listas de e-mail podem fazer isso por você, determinando se o endereço de e-mail segue a sintaxe correta e tem as propriedades físicas de um endereço de e-mail, verificando o domínio do e-mail e conectando-se ao servidor de e-mail para autenticar se o endereço de e-mail existe.

### Verifique se um endereço de e-mail já está associado a um usuário {#check-if-an-email-address-is-already-associated-with-a-user}

Antes de criar um usuário por meio da API ou SDK, chame o endpoint [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) e especifique o `email_address` do usuário. Se retornar um perfil de usuário, esse usuário da Braze já está associado a esse endereço de e-mail.

Recomendamos fortemente que você procure endereços de e-mail únicos quando novos usuários forem criados e evite passar ou importar usuários com o mesmo endereço de e-mail. Caso contrário, você pode ter consequências indesejadas que impactam o envio de mensagens, o direcionamento, os relatórios e outros recursos.

Por exemplo, digamos que você tenha perfis duplicados, mas certos atributos personalizados ou eventos existam em apenas um perfil. Quando você tenta disparar Campaigns ou Canvas com múltiplos critérios, a Braze não consegue identificar o usuário como elegível porque existem dois perfis de usuário. Ou, se uma Campaign direciona um endereço de e-mail compartilhado por dois usuários, a página **Pesquisar usuários** mostrará ambos os perfis de usuário como tendo recebido a Campaign.

### Identifique seus usuários engajados {#identify-your-engaged-users}

Para identificar seus usuários mais engajados, primeiro remova os usuários inativos há muito tempo. É uma prática recomendada não enviar e-mails para usuários que não interagiram com um e-mail há mais de seis meses, pois isso pode prejudicar a reputação do remetente de e-mail. Ao importar sua lista de e-mails, certifique-se de incluir apenas usuários que abriram um e-mail seu nos últimos seis meses.

A longo prazo, você também deve considerar implementar uma [política de sunset]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies).

### Evite listas de supressão {#avoid-suppression-lists}

Se você está migrando de um provedor de e-mail existente, certifique-se de não importar usuários de uma lista de supressão. As listas de supressão contêm endereços de e-mail que cancelaram a inscrição, marcaram seus e-mails como spam ou tiveram hard bounce.

## Métodos de importação {#methods-for-importing}

Depois de preparar sua lista de e-mails, existem várias maneiras de importar usuários na Braze, como por meio da REST API da Braze ou arquivos CSV. Leia mais no nosso artigo dedicado de [Importação de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).