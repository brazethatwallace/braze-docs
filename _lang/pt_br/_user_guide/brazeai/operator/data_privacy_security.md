---
nav_title: Privacidade e segurança de dados
article_title: Privacidade e segurança de dados do BrazeAI Operator
page_order: 5
page_type: reference
description: "Este artigo de referência aborda como o BrazeAI Operator lida com dados, incluindo conformidade com HIPAA, retenção de dados, minimização de IPI e governança."
---

# Privacidade e segurança de dados do BrazeAI Operator {#data-privacy-and-security-for-brazeai-operator}

> O BrazeAI Operator<sup>TM</sup> se integra com a OpenAI para fornecer assistência com tecnologia de IA. Este artigo aborda como o Operator lida com dados, quais informações são compartilhadas com a OpenAI e como minimizar a exposição de IPI e controlar o acesso.

## Como o Operator acessa dados {#how-operator-accesses-data}

O acesso do Operator a dados de cliente é estritamente orientado por eventos e limitado ao escopo da invocação, não sendo persistente. Cada mensagem de usuário ou evento de navegação enquanto o Operator está aberto aciona uma requisição HTTP discreta para a OpenAI. Não há conexão permanente nem feed de dados persistente.

A OpenAI não tem acesso direto aos armazenamentos de dados da Braze nem à tabela completa de usuários. O LLM recebe apenas a carga útil específica associada à requisição ativa.

### Quais dados são incluídos em cada requisição {#what-data-is-included-in-each-request}

Cada carga útil de requisição enviada à OpenAI pode incluir o seguinte:

- **Metadados do sistema:** prompts de sistema criados pela Braze e esquemas de ferramentas (definições de ferramentas que o LLM pode invocar).
- **Mensagem do usuário do dashboard:** a entrada digitada pelo usuário do dashboard.
- **Saídas de ferramentas:** resultados de pesquisa contendo nomes, IDs e dados relacionados.
- **Conteúdo extraído da página:** conteúdo da página ativa do dashboard, truncado para aproximadamente 4.000 caracteres.
- **Strings de contexto da página:** strings contextuais da página ativa do dashboard.

## Subprocessadores de dados {#data-sub-processors}

### Provedores de modelo como subprocessadores ou provedores terceiros {#model-providers-as-sub-processors-or-third-party-providers}

Quando você usa uma integração com um provedor de LLM fornecido pela Braze por meio dos Serviços Braze ("LLM fornecido pela Braze"), os provedores desse LLM fornecido pela Braze atuam como subprocessadores da Braze, sujeitos aos termos do Adendo de Processamento de Dados (DPA) entre você e a Braze. O BrazeAI Operator<sup>TM</sup> se integra com a OpenAI.

### Como os dados são usados com a OpenAI {#how-data-is-used-with-openai}

Para gerar saídas de IA por meio de recursos do BrazeAI que utilizam a OpenAI ("Saída"), a Braze enviará determinadas informações ("Entrada") à OpenAI. A Entrada consiste nos seus prompts, no conteúdo exibido no dashboard e nos dados do espaço de trabalho relevantes para suas consultas. De acordo com os [compromissos da plataforma de API da OpenAI](https://openai.com/enterprise-privacy/), os dados enviados à API da OpenAI por meio da Braze não são usados para treinar ou melhorar os modelos da OpenAI. Entre você e a Braze, a Saída é sua propriedade intelectual. A Braze não reivindicará direitos autorais sobre essa Saída. A Braze não oferece garantia de qualquer tipo em relação a qualquer conteúdo gerado por IA, incluindo a Saída.

## Conformidade com HIPAA e retenção de dados {#hipaa-compliance-and-data-retention}

### Conformidade com HIPAA {#hipaa-compliance}

Se você usa o cluster US-02 da Braze, o Operator é coberto pelo Acordo de Associado Comercial (BAA) da Braze, e Informações de Saúde Pessoais (PHI) podem ser enviadas ao recurso em conformidade com os requisitos da HIPAA. Não envie PHI sujeitas à HIPAA ao usar o Operator em outros clusters da Braze.

### Redação de IPI {#pii-redaction}

Não há uma camada automatizada de redação de IPI no pipeline de requisições do Operator. Os dados são enviados completamente brutos e não são anonimizados antes da transmissão à OpenAI. O acesso é limitado à página ativa do dashboard ou à entrada do usuário do dashboard, mas nenhuma filtragem de conteúdo é aplicada antes da transmissão.

### Retenção de dados da OpenAI {#openai-data-retention}

O tempo de retenção dos dados enviados por meio do Operator pela OpenAI depende do seu cluster:

| Cluster | Retenção |
| --- | --- |
| US-02 (clientes HIPAA) | Retenção Zero de Dados (ZDR). Os dados não são armazenados pela OpenAI após o processamento. |
| Todos os outros clusters | 30 dias para monitoramento de abuso. Este é um período de retenção padrão do setor imposto pela OpenAI. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Retenção de dados da OpenAI por cluster" }

### Treinamento de modelo {#model-training}

Os dados enviados à API da OpenAI por meio da Braze não são usados para treinar ou melhorar os modelos da OpenAI. Isso é regido por acordos contratuais entre a Braze e a OpenAI e pelos compromissos da plataforma de API da OpenAI. A OpenAI atua como subprocessadora da Braze, e todos os Dados Pessoais estão sujeitos ao DPA entre a Braze e seus clientes.

### Roteamento de dados da UE {#eu-data-routing}

O roteamento de dados da UE não está implementado atualmente para o Operator, e não há planos atuais para implementá-lo.

## Minimizar a exposição de IPI {#minimize-pii-exposure}

Existem várias etapas que você pode seguir para limitar a exposição de IPI ao usar o Operator:

- **Desative a configuração Visualizar IPI** para qualquer usuário que use o Operator. Se um usuário não pode visualizar IPI, o Operator também não pode acessá-las.
- **Não abra o Operator em uma página de perfil de usuário.** O conteúdo da página é extraído e incluído em cada requisição enviada à OpenAI.
- **Ao testar, use um perfil de usuário personalizado** em vez de selecionar um existente. Este é o comportamento padrão do Operator.
- **Não digite nem cole IPI** diretamente no prompt do Operator. O Operator não bloqueia IPI incluídas nos prompts do usuário. Se um usuário digitar IPI manualmente em uma requisição, esse conteúdo será enviado ao modelo de linguagem subjacente.
- **Desative a aprovação automática de ações** para manter o controle sobre o que o Operator pode acessar e executar.
- **Não peça ao Operator para exibir valores de prévia de atributos** ao criar um segmento ou escrever Liquid.

## Governança e controle de acesso {#governance-and-access-control}

### Restringir o acesso ao Operator {#restrict-access-to-operator}

O acesso ao Operator é gerenciado no nível do espaço de trabalho por meio de [Permissões granulares de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Os administradores podem conceder ou revogar a permissão "Use BrazeAI Operator" para usuários individuais, garantindo que apenas pessoal autorizado possa interagir com a ferramenta. Sem essas permissões específicas, a interface do Operator é completamente suprimida e os endpoints de backend permanecem protegidos.

### Modelo com humano no circuito {#human-in-the-loop-model}

Por padrão, o Operator requer aprovação explícita antes de confirmar qualquer alteração. As modificações propostas são apresentadas como [cartões de ação]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) para revisão. Se um usuário rejeitar uma proposta, nenhuma alteração ocorre. Se um usuário aceitar uma proposta, o dashboard é atualizado, mas as alterações permanecem pendentes e devem ser salvas ou lançadas manualmente para se tornarem persistentes.

Os usuários podem ativar **Aprovação automática de ações** no painel de chat do Operator, o que faz com que as ações sugeridas sejam executadas imediatamente sem revisão manual. Mesmo com a aprovação automática ativada, algumas ações sempre exigem aprovação explícita por segurança, incluindo a geração de imagens e a modificação de configurações no nível do espaço de trabalho.

### Herança de permissões do usuário {#user-permission-inheritance}

O Operator herda completamente o perfil de permissões do usuário conectado. Ele é impedido de visualizar dados ou executar ações, como modificações de Campaign, que o usuário não está autorizado a realizar de forma independente.

### Permissão Visualizar IPI {#view-pii-permission}

O Operator não requer a permissão "Visualizar IPI" para funcionar, e isso é intencional. O Operator não tem acesso direto ao seu armazenamento de dados e não consulta seu banco de dados de forma independente. Em vez disso, ele faz requisições aos mesmos endpoints de backend que o restante do dashboard, usando as credenciais de sessão do usuário autenticado. Isso significa que o Operator é totalmente limitado pelas [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) existentes do usuário e não pode acessar nada que o usuário já não consiga ver.

IPI só podem chegar ao Operator de duas formas:

- O usuário digita IPI diretamente em um prompt.
- O usuário já está visualizando IPI no dashboard quando usa o Operator.

Se um usuário não tem a permissão "Visualizar IPI", o Operator não pode exibir IPI para ele. Lembre-se de que o Operator não filtra conteúdo digitado diretamente nos prompts — IPI inseridas manualmente são enviadas ao modelo de linguagem subjacente. Para reduzir esse risco, consulte [Minimizar a exposição de IPI](#minimize-pii-exposure).

### Auditar o uso da equipe {#audit-team-usage}

Baixe o [Relatório de eventos de segurança]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) da Braze para monitorar o uso da equipe. O evento "Requested BrazeAI Operator Response" fornece uma trilha de auditoria abrangente, permitindo que você revise as entradas exatas fornecidas ao Operator.