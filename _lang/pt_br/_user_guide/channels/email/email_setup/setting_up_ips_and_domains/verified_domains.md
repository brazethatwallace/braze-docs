---
nav_title: Domínios verificados
article_title: Domínios verificados
page_order: 0
page_type: tutorial
channel: email
description: "Este artigo explica como configurar domínios verificados para que a Braze gerencie o DNS para envio de e-mail e rastreamento de cliques HTTPS."
toc_headers: h2
---

# Domínios verificados {#verified-domains}

> Os domínios verificados permitem que você conceda à Braze o controle de um subdomínio específico para automatizar a configuração de e-mail e o rastreamento HTTPS. Com a delegação de domínio DNS, a Braze gerencia os registros DNS necessários para o envio de e-mail e o rastreamento de cliques. Por exemplo, se o seu subdomínio é "mail.example.com", você pode delegá-lo à Braze para configurar seus domínios de envio e rastreamento.

{% alert important %}
Atualmente, os domínios verificados são compatíveis apenas com o Amazon SES. Se você usa SendGrid ou SparkPost, esse recurso não está disponível.<br><br>Os domínios verificados são compatíveis apenas com e-mail. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

## Benefícios {#benefits}

- Integração mais rápida: a automação dessas etapas reduz o tempo de integração de e-mail.
- Menos coordenação: você não precisa mais trabalhar com o suporte da Braze para tarefas de configuração de domínio, o que aproxima você de uma experiência totalmente self-service.
- Gerenciamento automatizado de SSL: a Braze cuida da criação e renovação de certificados SSL, eliminando um ponto comum de falha e trabalho manual. Proteger seus links com SSL é uma prática recomendada padrão — os destinatários tendem a confiar mais em links seguros, e a camada adicional de autenticação ajuda a proteger seus dados.
- Menos erros de configuração: fluxos de integração guiados e validação automatizada substituem a configuração manual de DNS, que é propensa a erros, reduzindo as chances de configurar registros incorretamente e comprometer a configuração de e-mail.
- Monitoramento proativo: a Braze monitora seus registros DNS e notifica você quando detecta problemas, em vez de esperar que as falhas apareçam.

## Considerações {#considerations}

Antes de começar, tenha em mente os seguintes detalhes:

- Escolha um subdomínio dedicado. Após concluir a delegação de domínio, a Braze gerencia todos os registros DNS desse subdomínio. A Braze recomenda delegar um subdomínio em vez do domínio principal da sua marca, porque delegar um domínio principal significa perder visibilidade e controle sobre ele. Se você quiser usar um domínio principal, use um que não esteja sendo utilizado em nenhum outro lugar.
- A delegação de NS (nameserver) é necessária para que a Braze possa gerenciar os registros DNS do seu subdomínio, como SPF, DKIM e rastreamento HTTPS, sem que você precise configurar cada um manualmente.

{% alert note %}
A delegação CNAME não é compatível. {% multi_lang_include product_feedback_cta.md context="gap" feature="CNAME delegation for verified domains" %}
{% endalert %}

- Planeje um subdomínio de envio com no mínimo três níveis. Como a Braze cria um subdomínio dentro do seu domínio delegado (como "mail.example.com"), seu domínio de envio precisa ter pelo menos três níveis de profundidade. Um exemplo é "e.mail.example.com".
- A Braze gerencia seus registros DNS. Após a conclusão da delegação, a Braze é responsável pelos registros DNS no subdomínio delegado. Não modifique esses registros por conta própria, pois isso pode causar problemas com o envio de e-mail.
- A permissão "Edit Domain Settings" é necessária para configurar domínios verificados.

## Etapa 1: Adicionar o domínio verificado {#step-1-add-the-verified-domain}

1. Acesse **Settings** > **Verified Domains** > **Add verified domain**.
2. Insira o subdomínio e o nome raiz. Por exemplo, se você está delegando o subdomínio "mail.example.com" à Braze, o nome raiz é "example.com" e o subdomínio é "mail".
3. Confirme que o subdomínio escolhido não está em uso em outro lugar e não possui registros DNS conflitantes.
4. Selecione **Add** para receber os registros TXT e NS.

## Etapa 2: Configurar registros DNS {#step-2-configure-dns-records}

Após enviar o domínio verificado, a Braze gera os registros DNS necessários que você deve adicionar ao seu provedor DNS. Essa etapa pode exigir coordenação com sua equipe de TI ou DNS. Você tem 30 dias para que os registros sejam verificados antes de expirarem. Após esse prazo, será necessário refazer a configuração.

{% alert tip %}
Confirme que todos os quatro registros NS estão explicitamente presentes usando o comando `dig` e que o domínio é validado no dashboard antes de considerar a configuração concluída. A verificação de DNS expira após 30 dias.
{% endalert %}

## Etapa 3: Verificar o domínio {#step-3-verify-the-domain}

Após a propagação dos registros DNS, a Braze verifica se os registros estão presentes e configurados corretamente em até 24 horas. Quando a verificação é bem-sucedida:

- O status do domínio é atualizado para **Verified**.
- A Braze envia um e-mail notificando que o domínio está pronto.
- O domínio aparece como ativo na lista de **Verified Domains**.

Após a delegação bem-sucedida de um subdomínio, crie domínios de e-mail, como seus domínios de envio e rastreamento, acessando **Add custom domain**. Em seguida, você será direcionado à página de **Sender Verification** para concluir a configuração. Para etapas detalhadas, consulte [E-mail self-service]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve).