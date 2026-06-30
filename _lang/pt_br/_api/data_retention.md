---
nav_title: Retenção de dados
article_title: Retenção de dados
alias: /data_retention/
description: "Este artigo de referência traz informações gerais sobre retenção de dados da Braze."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informações de retenção de dados da Braze {#braze-data-retention-information}

*Última revisão em 1º de abril de 2024*

> Este artigo aborda informações gerais de retenção de dados da Braze.<br><br>Os dados armazenados na Braze são retidos e podem ser utilizados para segmentação, personalização e direcionamento durante toda a vida útil da conta do Cliente. Isso significa que dados como atributos de perfil de usuário, atributos personalizados, eventos personalizados e compras são armazenados indefinidamente para usuários ativos, a menos que sejam removidos pelo Cliente, durante a vigência do contrato.<br><br>A Braze tem recursos, processos e APIs para implementar automaticamente boas práticas de higiene de dados para conformidade com o GDPR e outras práticas recomendadas. Elas são descritas a seguir.

## Retenção de dados gerenciada pelos clientes por meio do dashboard ou da API da Braze {#data-retention-handled-by-customers-through-brazes-dashboard-or-api}

A Braze capacita seus clientes a excluir perfis de usuário e dados de atributos inteiros de seu espaço de trabalho.

Isso significa que você pode:
- Excluir perfis de usuário usando o [endpoint da API Excluir usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) da Braze
- Excluir (nulo) ou alterar atributos em perfis de usuário usando o [endpoint da API Rastrear usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze

Os eventos comportamentais não podem ser excluídos de um perfil de usuário (eventos personalizados, sessões, Campaigns, compras). Para remover esses eventos, é necessário excluir todo o perfil de usuário.

Para fins de conformidade com a privacidade, talvez seja necessário excluir todos os dados pessoais pertencentes a um usuário mediante solicitação do mesmo. Você pode encontrar instruções em nossa página de [assistência técnica de proteção de dados]({{site.baseurl}}/help/dp-technical-assistance#the-right-to-erasure).

{% alert note %}
Um usuário pode ter vários perfis, e talvez seja necessário excluir vários perfis para excluir todos os dados pertencentes a um único usuário. Siga as instruções na página de assistência técnica de proteção de dados sobre como excluir totalmente todos os dados de um usuário.
{% endalert %}

## Retenção de dados gerenciada pela Braze para recursos específicos dos Serviços Braze {#data-retention-handled-by-braze-for-specific-features-of-the-braze-services}

### Banco de dados da Braze: arquivamento/exclusão automática de usuários perdidos {#braze-database-automatic-archivingdeletion-of-churned-users}

A cada semana, a Braze executa um processo para remover usuários inativos dos Serviços Braze. Em geral, esses são usuários que não estão acessíveis (por exemplo, não têm endereço de e-mail, número de telefone, token por push, não usam seus apps ou visitam seus sites), não tiveram nenhuma atividade registrada em seu perfil de usuário e não receberam mensagens ou não se engajaram com a Braze. Isso é feito para aderir aos princípios e às práticas recomendadas do GDPR. Você pode ler mais sobre esse processo em nossa página de [definições de arquivamento de usuários]({{site.baseurl}}/user_archival).

{% alert note %}
Os clientes têm controle total sobre se um usuário está inativo e podem impedir o arquivamento de perfis de usuários registrando um ponto de dados em intervalos regulares. O Canvas da Braze oferece a capacidade de fazer isso automaticamente, o que permite desativar efetivamente essa funcionalidade para alguns ou todos os seus usuários inativos.
{% endalert %}

### Dados de interação de Campaigns e Canvas {#campaign-and-canvas-interactions-data}

Os dados de interação de mensagens referem-se a como um usuário interage com uma Campaign ou um Canvas que recebeu (por exemplo, quando um usuário abre a Campaign A ou um usuário recebe a variante A). Esses dados são usados para redirecionamento. Você pode ler mais sobre a disponibilidade de dados de interação de mensagens em [Sobre a disponibilidade dos dados de interação de mensagens]({{site.baseurl}}/messaging_interaction_data).

## Retenção de dados gerenciada pela Braze {#data-retention-handled-by-braze}

As políticas de retenção abaixo se referem à conformidade da Braze com o GDPR e com os regulamentos de privacidade e dizem respeito ao armazenamento de dados transitórios à medida que passam por nossos sistemas internos. Essas políticas de retenção não afetam os Serviços Braze e são informativas para suas equipes jurídicas e de privacidade.

### Servidores da Braze: retenção de curto prazo para fins de recuperação {#braze-servers-short-term-retention-for-recovery-purposes}

Os dados enviados pela Braze a determinados subprocessadores ainda poderão existir nos sistemas internos da Braze por até 90 dias.

### Retenção de dados do Braze Data Lake {#braze-data-lake-data-retention}

Os dados disponíveis para os clientes no dashboard da Braze são, em sua maioria, agregados. Os registros detalhados são mantidos em um banco de dados separado criado pela Braze (o "Data Lake"). Os dados do Data Lake são usados para relatórios agregados e outras funcionalidades avançadas. A Braze remove as informações de identificação pessoal dos dados de eventos armazenados no Data Lake após dois anos (consulte mais informações em nossa página [Retenção de dados do Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention)).

Se você usar nossas APIs para excluir perfis de usuários ou excluir ou alterar atributos de perfis de usuários, poderá levar até três semanas para que esses dados sejam excluídos do Data Lake da Braze. A exclusão de dados no Data Lake não afetará a segmentação ou a personalização, mas garantirá que os dados sejam removidos de todos os sistemas da Braze.

### Servidores de backup da Braze {#braze-backup-servers}

Quando os dados são excluídos de sua instância de produção, eles permanecem nos servidores de backup da Braze por seis meses e, em seguida, são excluídos de acordo com nossos processos internos.