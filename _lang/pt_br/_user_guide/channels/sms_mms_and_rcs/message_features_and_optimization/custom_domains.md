---
nav_title: Domínios personalizados de autoatendimento
article_title: Domínios personalizados de autoatendimento
page_order: 2
description: "Esta página aborda como usar domínios personalizados com encurtamento de links para personalizar a aparência dos seus URLs encurtados."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Domínios personalizados de autoatendimento {#self-serve-custom-domains}

> Esta página aborda como configurar seus próprios domínios personalizados no dashboard da Braze. Domínios personalizados permitem que você use um link encurtado com a sua marca, que reflete a identidade da sua marca, em vez de um link encurtado genérico ou do domínio da Braze (`brz.ai`) — melhorando a confiança do usuário e o engajamento das campanhas com links de SMS.

Os domínios personalizados de autoatendimento permitem que você configure e gerencie seus próprios domínios personalizados para SMS, RCS e WhatsApp — diretamente do seu dashboard da Braze. Você pode facilmente adicionar, monitorar e gerenciar até 10 domínios personalizados em um só lugar.

## Benefícios dos domínios personalizados de autoatendimento {#benefits-of-self-serve-custom-domains}

- **Configuração simplificada:** Configure seus domínios na página **Configurações da empresa**, reduzindo o tempo de configuração.
- **Maior transparência:** Receba atualizações em tempo real sobre o status de configuração do seu domínio por meio de banners no dashboard.
- **Notificações proativas:** Receba alertas imediatos quando seu domínio personalizado estiver conectado ou se ocorrerem erros de configuração.

## Requisitos de domínio {#domain-requirements}

- Os domínios devem ser adquiridos, de sua propriedade e gerenciados por você. Isso pode ser feito por meio de um registrador de domínios, como GoDaddy, Amazon Route 53 ou Cloudflare.
- O domínio usado para esse recurso deve ser:
  - Único (diferente do domínio do seu website)
  - Não pode ser usado para hospedar nenhum conteúdo web
    - Você também pode usar subdomínios exclusivos. Por exemplo, o domínio `braze.com` poderia ter subdomínios como `sms.braze.com` ou `whatsapp.braze.com`.

## Delegando seu domínio personalizado {#delegating-your-custom-domain}

Exigimos que você delegue seu domínio personalizado à Braze para que possamos facilitar o roteamento adequado e a compatibilidade de infraestrutura com nossos serviços de encurtamento de links e rastreamento de cliques. Quando você delega seu domínio à Braze, gerenciamos automaticamente a renovação do certificado para evitar uma interrupção no serviço.

{% alert important %}
Se seus registros DNS não forem atualizados em até 45 dias, o token de configuração expira. Reinicie a configuração do domínio em **SMS/RCS and Messaging Apps Domains** para gerar novos registros DNS.
{% endalert %}

## Adicionando um domínio personalizado {#adding-a-custom-domain}

1. Na Braze, acesse **Company Settings** > **SMS/RCS and Messaging Apps Domains**.
![Página "SMS/RCS and Messaging Apps Domains" com vários domínios listados.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. Selecione **Add Domain** para iniciar a configuração de um novo domínio personalizado.
3. Insira o domínio personalizado que você adquiriu no campo de entrada do app, que usa nossa lógica de validação existente para formatação adequada, e selecione **Next** e **Submit**.

![Botão "Add Domain" na página "SMS/RCS and Messaging Apps Domains".]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. Peça à sua equipe técnica (como engenharia ou TI) para atualizar a configuração de DNS com os detalhes do registro DNS do Cloudflare exibidos. Sua equipe técnica deve atualizar os registros DNS com esses detalhes em até 45 dias.
  - Se você precisar de mais tempo para atualizar seus registros DNS, poderá reiniciar o processo e gerar um novo conjunto de registros DNS para o seu domínio.

A Braze verifica sua configuração de DNS aproximadamente a cada 30 minutos para checar atualizações.

![Seção "Registro DNS" com 3 etapas a serem concluídas para finalizar a configuração do seu domínio.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
O progresso do seu domínio é salvo automaticamente. Se você precisar sair no meio do processo, poderá retomar mais tarde selecionando a entrada de domínio pendente na página **SMS/RCS and Messaging Apps Domains**.
{% endalert %}

### Gerenciamento e uso contínuos {#ongoing-management-and-usage}

Após a verificação do seu domínio, seus domínios personalizados aparecerão na tabela da página **SMS/RCS and Messaging Apps Domains** com indicadores de status. Você pode usar imediatamente os domínios conectados em vários grupos de inscrições, espaços de trabalho e nos canais SMS, RCS e WhatsApp.

![Lista de domínios personalizados e status.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

O monitoramento em tempo real alerta você no dashboard da Braze se algum dos seus domínios ativos apresentar um problema, para que seus links personalizados permaneçam utilizáveis. Se você encontrar algum problema, consulte os detalhes do erro no app ou entre em contato com o [Suporte]({{site.baseurl}}/braze_support) da Braze para obter assistência.

## Atribuindo domínios personalizados a grupos de inscrições {#assigning-custom-domains-to-subscription-groups}

Depois de configurados, os domínios personalizados podem ser atribuídos a um ou vários grupos de inscrições de SMS, RCS e WhatsApp.

1. Acesse **Público** > **Gerenciamento de grupo de inscrições**.
2. Encontre e selecione seu grupo de inscrições na lista.
3. Em **Detalhes do grupo de inscrições**, selecione seu domínio personalizado no menu suspenso **Domínio de encurtamento de link**.

As Campaigns enviadas com o encurtamento de link ativado usam o domínio atribuído associado ao seu grupo de inscrições de SMS, RCS ou WhatsApp.

![Prévia do criador de mensagem SMS com um domínio de link encurtado diferente do domínio na caixa "Mensagem".]({% image_buster /assets/img/custom_domain2.png %})

## Perguntas frequentes {#frequently-asked-questions}

### Os domínios delegados podem ser compartilhados entre vários grupos de inscrições? {#can-delegated-domains-be-shared-across-multiple-subscription-groups}

Sim. Um único domínio pode ser usado com vários grupos de inscrições. Para isso, selecione o domínio para cada grupo de inscrições ao qual ele deve ser associado.

### Os domínios delegados podem ser compartilhados entre vários espaços de trabalho? {#can-delegated-domains-be-shared-across-multiple-workspaces}

Sim. Os domínios podem ser associados a grupos de inscrições em vários espaços de trabalho, desde que os espaços de trabalho estejam contidos na mesma empresa.

### Quantos domínios personalizados posso adicionar? {#how-many-custom-domains-can-i-add}

Você pode adicionar até 10 domínios personalizados por dashboard. A Braze pode configurar um limite maior para a sua empresa mediante solicitação.

Domínios com status **Pending** ou **Error** contam para esse limite. Exclua-os ou resolva o erro na página **SMS/RCS and Messaging Apps Domains**.

Não é possível excluir um domínio que está atribuído como **Link Shortening Domain** em um grupo de inscrições. Primeiro, reatribua o domínio em cada grupo de inscrições e, em seguida, exclua o domínio.

### O que acontece se eu não atualizar meus registros DNS em 45 dias? {#what-happens-if-i-dont-update-my-dns-records-within-45-days}

Embora os detalhes do seu registro DNS do Cloudflare expirem após 45 dias, você pode reiniciar o processo de configuração com o mesmo domínio, e a Braze gera um novo conjunto de registros DNS para estender sua janela de configuração.

### Sou notificado se houver um erro durante o processo de atualização de DNS? {#am-i-notified-if-there-is-an-error-during-the-dns-update-process}

Sim. Se houver um erro, você receberá um banner no dashboard da Braze detalhando o problema junto com as etapas para resolvê-lo.

### Posso usar um domínio personalizado em vários canais? {#can-i-use-a-custom-domain-across-multiple-channels}

Sim. Depois que um domínio personalizado é verificado, ele pode ser usado em todos os grupos de inscrições de SMS, RCS e WhatsApp em todos os espaços de trabalho dentro de um dashboard.

### E se eu tiver dúvidas ou precisar de suporte adicional? {#what-if-i-have-questions-or-need-further-support}

Para orientações mais detalhadas sobre como configurar e gerenciar domínios personalizados, incluindo etapas de solução de problemas e requisitos técnicos, [entre em contato com o Suporte]({{site.baseurl}}/braze_support).