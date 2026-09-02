---
nav_title: Retenção de dados
article_title: "Informações de retenção de dados da Braze"
alias: /data_retention/
description: "Este artigo de referência aborda informações gerais sobre retenção de dados da Braze."
page_type: reference
page_order: 2.5
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informações de retenção de dados da Braze {#braze-data-retention-information}

*Última revisão em 1º de abril de 2024*

> Este artigo aborda informações gerais de retenção de dados da Braze.<br><br>Os dados armazenados na Braze são retidos e podem ser utilizados para segmentação, personalização e direcionamento durante toda a vida útil da conta do cliente. Isso significa que dados como atributos de perfil de usuário, atributos personalizados, eventos personalizados e compras são armazenados indefinidamente para usuários ativos, a menos que sejam removidos pelo cliente, durante a vigência do contrato.<br><br>A Braze tem recursos, processos e APIs para implementar automaticamente boas práticas de higiene de dados para conformidade com o GDPR e outras práticas recomendadas. As seções a seguir descrevem como a retenção de dados é gerenciada.

## Retenção de dados gerenciada pelos clientes por meio do dashboard ou API or interface de programação do aplicativo (API) da Braze {#data-retention-handled-by-customers-through-brazes-dashboard-or-api}

A Braze permite que seus clientes excluam perfis de usuário inteiros e dados de atributos de seus espaços de trabalho.

Isso significa que você pode:
- Excluir perfis de usuário usando o [endpoint de API or interface de programação do aplicativo (API) para exclusão de usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) da Braze
- Excluir (anular) ou alterar atributos em perfis de usuário usando o [endpoint de API or interface de programação do aplicativo (API) para rastreamento de usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze

Eventos comportamentais não podem ser excluídos de um perfil de usuário (eventos personalizados, sessões, Campaigns, compras). Para remover esses eventos, você deve excluir o perfil de usuário inteiro.

Para conformidade com privacidade, pode ser necessário excluir todos os dados pessoais referentes a um usuário mediante solicitação dele. Você pode encontrar instruções na nossa página de [assistência técnica de proteção de dados]({{site.baseurl}}/help/dp-technical-assistance#the-right-to-erasure).

{% alert note %}
Um usuário pode ter vários perfis, e pode ser necessário excluir vários perfis para remover todos os dados referentes a um único usuário. Siga as instruções na página de assistência técnica de proteção de dados sobre como excluir completamente todos os dados referentes a um usuário.
{% endalert %}

## Retenção de dados gerenciada pela Braze para recursos específicos dos serviços da Braze {#data-retention-handled-by-braze-for-specific-features-of-the-braze-services}

### Banco de dados da Braze: arquivamento/exclusão automática de usuários desistentes {#braze-database-automatic-archivingdeletion-of-churned-users}

Toda semana, a Braze executa um processo para remover usuários inativos e usuários inativos dos serviços da Braze. Em geral, são usuários que não podem ser alcançados (por exemplo, não têm endereço de e-mail, número de telefone, token por push, não usam seus apps nem visitam seus websites), não tiveram nenhuma atividade registrada em seu perfil de usuário e não receberam mensagens nem foram engajados usando a Braze. Isso é feito para aderir aos princípios e às práticas recomendadas do GDPR. Você pode saber mais sobre esse processo em nossa página de <a href="/docs/user_archival">definições de arquivamento de usuário</a>.

{% alert note %}
Os clientes têm controle total sobre quando um usuário é inativo ou inativo, e podem evitar o arquivamento de perfis de usuário registrando um ponto de dados em intervalos regulares. O BRAZE CANVAS oferece a capacidade de fazer isso automaticamente, permitindo que você desative efetivamente essa funcionalidade para alguns ou todos os seus usuários inativos.
{% endalert %}

### Dados de interação de Campaigns e Canvas {#campaign-and-canvas-interactions-data}

Os dados de interação de mensagens referem-se a como um usuário interage com uma Campaign ou Canvas que recebeu (por exemplo, quando um usuário abre a Campaign A ou um usuário recebe a variante A). Esses dados são usados para redirecionamento. Você pode saber mais sobre a disponibilidade dos dados de interação de mensagens em [Sobre a disponibilidade dos dados de interação de mensagens]({{site.baseurl}}/messaging_interaction_data).

## Retenção de dados gerenciada pela Braze {#data-retention-handled-by-braze}

As seguintes políticas de retenção dizem respeito à conformidade da Braze com o GDPR e as regulamentações de privacidade, e referem-se ao armazenamento transitório de dados à medida que eles passam por nossos sistemas internos. Essas políticas de retenção não afetam os Serviços da Braze e são informativas para suas equipes jurídica e de privacidade.

### Servidores da Braze: retenção de curto prazo para fins de recuperação {#braze-servers-short-term-retention-for-recovery-purposes}

Os dados enviados pela Braze a determinados subprocessadores ainda podem existir nos sistemas internos da Braze por até 90 dias.

### Retenção de dados do Data Lake da Braze {#braze-data-lake-data-retention}

Os dados disponíveis para os clientes no dashboard da Braze são, em sua maioria, agregados. Registros detalhados são mantidos em um banco de dados separado criado pela Braze (o "Data Lake"). Os dados do Data Lake são usados para relatórios agregados e outras funcionalidades avançadas. A Braze remove informações de identificação pessoal dos dados de eventos armazenados no Data Lake após dois anos (consulte mais informações em nossa página de [Retenção de dados Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_retention)).

Se você usar nossas APIs para excluir perfis de usuário ou excluir ou alterar atributos de perfis de usuário, pode levar até três semanas para que esses dados sejam excluídos do Data Lake da Braze. A exclusão de dados no Data Lake não afeta a segmentação ou a personalização, mas garante que os dados sejam removidos de todos os sistemas da Braze.

### Servidores de backup da Braze {#braze-backup-servers}

Quando os dados são excluídos da sua instância de produção, eles permanecem nos servidores de backup da Braze por seis meses e, em seguida, são excluídos de acordo com nossos processos internos.