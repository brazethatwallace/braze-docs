---
nav_title: Centro de Entregabilidade
article_title: Centro de Entregabilidade
alias: "/deliverability_center/"
page_order: 4
description: "Este artigo de referência explica como configurar o Centro de Entregabilidade, um recurso que permite que profissionais de marketing visualizem a reputação dos domínios de envio de e-mail e dos IPs, além de entender a entregabilidade dos seus e-mails."
channel:
  - email

---

# Centro de Entregabilidade {#deliverability-center}

> O Centro de Entregabilidade oferece mais insights sobre o desempenho dos seus e-mails, com suporte ao uso do [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para rastrear dados de e-mails enviados e coletar informações sobre o seu domínio de envio.

A entregabilidade de e-mail é o ponto central do sucesso de uma campanha. Usando o Centro de Entregabilidade no dashboard da Braze, você pode visualizar seus domínios por **IP Reputation** ou **Delivery Errors** para identificar e solucionar possíveis problemas de entregabilidade de e-mail.

Para acessar o Centro de Entregabilidade, você precisa das [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) listadas no dropdown a seguir para o seu espaço de trabalho.

{% details Permissões de usuário para o Centro de Entregabilidade %}

- View Campaigns
- Edit Campaigns
- Archive Campaigns
- View Canvases
- Edit Canvases
- Archive Canvases
- View Frequency Capping Rules
- Edit Frequency Capping Rules
- View Message Prioritization
- Edit Message Prioritization
- View Content Blocks
- View Feature Flags
- Edit Feature Flags
- Archive Feature Flags
- View Segments
- Edit Segments
- View IAM Templates
- Edit IAM Templates
- Archive IAM Templates
- View Email Templates
- Edit Email Templates
- Archive Email Templates
- View Webhook Templates
- Edit Webhook Templates
- Archive Webhook Templates
- View Email Link Templates
- Edit Email Link Templates
- View Media Library Assets
- Edit Media Library Assets
- Delete Media Library Assets
- View Locations
- Edit Locations
- Archive Locations
- View Promotion Codes
- Edit Promotion Codes
- Export Promotion Codes
- View Preference Centers
- Edit Preference Centers
- View Reports
- Edit Reports
- View Usage Data

{% enddetails %}

## Configure sua conta do Google Postmaster {#set-up-your-google-postmaster-account}

Antes de conectar ao Centro de Entregabilidade, você precisa configurar uma conta do Google Postmaster Tools. Você pode usar uma conta do Gmail pessoal ou corporativa para configurar o Google Postmaster.

1. Acesse o [dashboard do Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. Na parte inferior da página, selecione <i class="fas fa-plus-circle"></i> **Add domain**.
3. Insira o domínio raiz (principal) para autenticar seu e-mail. Certifique-se de que o registro TXT esteja vinculado a esse domínio raiz (principal), e **não** ao subdomínio que você está usando na Braze. Verificar o domínio raiz (principal) permite que você adicione subdomínios posteriormente no Postmaster Tools sem criar registros TXT adicionais. Por exemplo, ao verificar `braze.com`, você pode adicionar `demo.braze.com` como um subdomínio separado no Postmaster Tools para visualizar métricas no nível do subdomínio.
4. O Google gera um registro TXT que pode ser adicionado diretamente ao DNS do seu domínio. Geralmente, isso é gerenciado por quem administra o seu DNS. Para informações e orientações sobre como atualizar o seu DNS específico, consulte [Verificar seu domínio (etapas específicas por host)](https://support.google.com/a/topic/1409901).
5. Selecione **Next**. <br>![Um exemplo de domínio "demo.braze.com" para autenticar um e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Após o registro TXT ser adicionado ao DNS, retorne ao dashboard do Google Postmaster Tools e selecione **Verify**. Essa etapa confirma que você é o proprietário do domínio, permitindo que você acesse as métricas de entregabilidade do Gmail na sua conta do Postmaster. <br>![Um prompt para verificar a propriedade do domínio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})
7. Após verificar o domínio raiz (principal), adicione seus subdomínios de envio ao Google Postmaster.

{% alert note %}
Se seus subdomínios não aparecem no Centro de Entregabilidade do Google Postmaster, isso pode ser resultado de ter adicionado apenas o domínio raiz (principal) ao Google Postmaster. Após a verificação dos domínios raiz no Google Postmaster, você pode adicionar seus subdomínios, que são verificados automaticamente. Esse processo permite que o Google reporte métricas no nível do subdomínio, que podem então ser importadas para o Centro de Entregabilidade da Braze.
{% endalert %}

## Integrar o Google Postmaster {#integrating-google-postmaster}

{% alert important %}
**Migração do Google Postmaster Tools v2**<br>
O Google está descontinuando a versão antiga do Postmaster Tools (v1) e lançou uma versão de nova geração (v2) com uma interface moderna e novos dashboards, incluindo um dashboard de conformidade para ajudar a monitorar a aderência às diretrizes de remetente do Gmail. Todos os usuários devem migrar para a v2 até 31 de outubro de 2026.<br><br>
Para reautorizar sua conexão com o Google Postmaster Tools, acesse **Integrações de parceiros** > **Parceiros de tecnologia**, abra **Google Postmaster** e selecione **Change Account** para reautenticar com as novas permissões da v2. Ao concluir, você será atualizado para a v2 e terá acesso aos novos dashboards e dados.<br><br>
Para saber mais, consulte o [anúncio do Google sobre o novo Postmaster Tools](https://support.google.com/mail/answer/16594218?hl=en).
{% endalert %}

Antes de configurar o Centro de Entregabilidade, verifique se seus domínios foram [adicionados ao Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Siga estas etapas para integrar com o Google Postmaster e configurar o Centro de Entregabilidade:

1. Acesse **Analytics** > **Email Performance**.
2. Selecione a guia **Deliverability Center**. <br>![Um Centro de Entregabilidade com o Google Postmaster desconectado.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecione **Connect with Google Postmaster**.
4. Selecione sua conta do Google e depois selecione **Allow** para permitir que a Braze visualize as métricas de tráfego de e-mail dos domínios registrados no Postmaster Tools.

Seus domínios verificados serão exibidos no Centro de Entregabilidade.

![Dois domínios verificados no Google Postmaster com reputação média e baixa.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Você também pode acessar o Google Postmaster no dashboard da Braze em **Integrações de parceiros** > **Parceiros de tecnologia** > **Google Postmaster**. Após a integração, a Braze importa dados de reputação e erros dos últimos 30 dias. Os dados podem não estar disponíveis imediatamente e podem levar alguns minutos para serem carregados.

### Autorização inválida ou expirada {#invalid-or-expired-authorization}

Se você receber um alerta informando que as credenciais de autorização do Google Postmaster Tools são inválidas, o envio de e-mails pela Braze **não** é afetado. Apenas a conexão entre a Braze e o Google Postmaster é interrompida, o que impede a sincronização dos dados de reputação e erros do Gmail com o Centro de Entregabilidade até que você reconecte.

Para restaurar a integração, acesse **Integrações de parceiros** > **Parceiros de tecnologia**, abra **Google Postmaster**, selecione **Disconnect** e depois refaça o fluxo de conexão (mesmas etapas de [Integrar o Google Postmaster](#integrating-google-postmaster)).

### Métricas e definições {#metrics-and-definitions}

As métricas e definições a seguir se aplicam ao Google Postmaster Tools.

#### Reputação de IP {#ip-reputation}

Para entender as classificações de reputação de IP, consulte esta tabela:

| Classificação de reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de gerar poucas reclamações de spam (como usuários clicando no botão "spam"). |
| Média/Razoável | Conhecido por gerar engajamento positivo, mas ocasionalmente recebe reclamações de spam. A maioria dos e-mails deste domínio é entregue na caixa de entrada, exceto quando as reclamações de spam aumentam. |
| Baixa | Conhecido por receber taxas elevadas de reclamações de spam regularmente. E-mails deste remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. E-mails deste domínio quase sempre são rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reputação de IP" }

#### Reputação do domínio {#domain-reputation}

Use a tabela a seguir para monitorar e entender as classificações de reputação do seu domínio e evitar que seus e-mails sejam filtrados para a pasta de spam.

| Classificação de reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de reclamações de spam muito baixas. Está em conformidade com as diretrizes de remetente do Gmail. E-mails raramente são filtrados para a pasta de spam. Tem um bom histórico de taxa de spam muito baixa. Está em conformidade com as [diretrizes de remetente do Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Média/Razoável | Conhecido por gerar engajamento positivo, mas ocasionalmente recebe um baixo volume de reclamações de spam. A maioria dos e-mails deste domínio chega à caixa de entrada (exceto quando há um aumento notável nos níveis de spam). |
| Baixa | Conhecido por receber reclamações de spam regularmente. E-mails deste remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. E-mails deste domínio quase sempre são rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reputação do domínio" }

#### Autenticação {#authentication}

Use o dashboard de autenticação para verificar a porcentagem de e-mails que passaram pelo Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) e Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Tipo de gráfico | Definição |
| ----- | ---------- |
| SPF | Mostra a porcentagem de e-mails que passaram pelo SPF em relação a todos os e-mails do domínio que tentaram o SPF. Isso exclui qualquer e-mail falsificado. |
| DKIM | Mostra a porcentagem de e-mails que passaram pelo DKIM em relação a todos os e-mails do domínio que tentaram o DKIM. |
| DMARC | Mostra a porcentagem de e-mails que passaram pelo alinhamento DMARC em relação a todos os e-mails recebidos do domínio que passaram pelo SPF ou DKIM. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autenticação" }

#### Criptografia {#encryption}

Consulte esta tabela para entender qual porcentagem do seu tráfego de entrada e saída é criptografada.

| Termo | Definição |
| ----- | ---------- |
| TLS de entrada | Mostra a porcentagem de e-mails recebidos (para o Gmail) que passaram pelo TLS em relação a todos os e-mails recebidos daquele domínio. |
| TLS de saída | Mostra a porcentagem de e-mails enviados (do Gmail) aceitos via TLS em relação a todos os e-mails enviados para aquele domínio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Criptografia" }

Para mais ideias sobre como melhorar a entregabilidade, leia [Armadilhas de entregabilidade e spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#deliverability-pitfalls-and-spam-traps). Consulte também nossas [Práticas recomendadas de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices) para verificar o que deve ser revisado antes de enviar uma campanha de e-mail.

## Configurar o Microsoft Smart Network Data Services (SNDS) {#set-up-microsoft-smart-network-data-services-snds}

Se a Microsoft é o seu principal provedor de caixa de e-mail, você pode visualizar os dados do Microsoft SNDS no Centro de Entregabilidade. Isso inclui IPs de envio dedicados para espaços de trabalho que usam Amazon SES, SendGrid ou SparkPost. Use esses dados para monitorar a integridade dos IPs e entender como os provedores de caixa de entrada da Microsoft estão classificando seus envios.

O Microsoft SNDS fornece dados no nível de IP sobre reclamações de spam, hits de spam trap e volume de envio, conforme reportado por provedores de caixa de entrada da Microsoft, como Outlook, Hotmail e Live.

{% alert important %}
Se você não vê seus dados no Centro de Entregabilidade, entre em contato com o [Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) com uma lista dos seus endereços IP.
{% endalert %}

### Amazon SES

Para espaços de trabalho que enviam e-mails pelo Amazon SES, o Centro de Entregabilidade exibe as métricas do Microsoft SNDS para seus IPs de envio dedicados. A Braze preenche retroativamente até 90 dias de dados históricos do SNDS quando esse recurso é ativado para o seu espaço de trabalho.

{% alert note %}
O Amazon SES não fornece as métricas **Trap message period start** ou **Trap message period end**. Para IPs de envio do SES, essas colunas ficam ocultas na tabela do Microsoft SNDS. Você ainda pode visualizar outras métricas do SNDS para esses IPs, incluindo hits de spam trap.
{% endalert %}

![Um exemplo de resultados do Microsoft SNDS, incluindo IPs de amostra, destinatários, comandos RCPT, comandos DATA, resultado do filtro, taxa de reclamação, período de início e fim de mensagens de spam trap e hits de spam trap.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas e definições

As métricas a seguir se aplicam ao Microsoft SNDS.

#### Destinatários {#recipients}

Esta métrica se refere ao número de destinatários em mensagens transmitidas pelo IP.

#### Comandos DATA {#data-commands}

Esta métrica rastreia o número de comandos DATA enviados pelo IP. Os comandos DATA fazem parte do protocolo SMTP usado para enviar e-mails.

#### Resultados do filtro {#filter-results}

Consulte esta tabela para entender os resultados do filtro.

| Resultado | Definição |
| ----- | ---------- |
| Verde | Considerado spam pelo filtro de spam da Microsoft em até 10% do período analisado. |
| Amarelo | Considerado spam pelo filtro de spam da Microsoft entre 10% e 90% do período analisado. |
| Vermelho | Considerado spam pelo filtro de spam da Microsoft em mais de 90% do período analisado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Resultados do filtro" }

#### Taxa de reclamação {#complaint-rate}

Esta é a fração de vezes em que uma mensagem recebida do IP é reportada como spam por um usuário do Hotmail ou Windows Live durante o período de atividade. Os usuários têm a opção de reportar praticamente todas as mensagens como lixo eletrônico pela interface web.

Para calcular a taxa de reclamação, divida o número de reclamações pelo número de destinatários da mensagem.

| Resultado | Definição |
| ----- | ---------- |
| Menos de 0,3% | A taxa de reclamação ideal. |
| Mais de 0,3% | Revise seu processo de inscrição e verifique se o link de cancelamento de inscrição está funcionando. Considere também se o e-mail poderia ser mais personalizado para o seu público. |
| Mais de 100% | Observe que o SNDS exibe as reclamações no dia em que foram reportadas, e não retroativamente no dia em que o e-mail reclamado foi entregue. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Taxa de reclamação" }

#### Hits de spam trap {#spam-trap-hits}

Hits de spam trap são o número de mensagens enviadas para "contas armadilha", que são contas mantidas pelo Outlook.com que não solicitam nenhum e-mail. É provável que qualquer mensagem enviada para essas contas armadilha seja considerada spam, por isso é importante monitorar essa métrica e garantir que ela esteja baixa. Hits de spam trap baixos significam que as mensagens não estão sendo enviadas para essas contas e estão sendo entregues para contas reais.

#### Período de início e fim de mensagens de spam trap {#trap-message-period-start-and-end}

Essas colunas mostram quando as primeiras e últimas mensagens enviadas para contas armadilha foram recebidas do IP durante o período de atividade. O Amazon SES não fornece essas métricas, então as colunas ficam ocultas quando você visualiza apenas IPs de envio do SES na tabela do Microsoft SNDS.

{% alert tip %}
Se você está procurando registros relacionados a um dos seus domínios verificados na Braze, observe que o Centro de Entregabilidade lista seus dados do Google Postmaster ou Microsoft SNDS, o que significa que é possível que nenhuma das plataformas tenha dados para compartilhar com a Braze. Como alternativa, tente manter um envio de e-mail consistente, pois isso pode levar a uma reputação mais alta.
{% endalert %}