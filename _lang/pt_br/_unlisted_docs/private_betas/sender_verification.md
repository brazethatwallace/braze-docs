---
nav_title: "Verificação do remetente"
article_title: "Verificação do remetente"
permalink: /sender_verification/
description: "Este artigo aborda como configurar a verificação do remetente e delegar seus próprios subdomínios à Braze."
hidden: true
---

# Verificação do remetente {#sender-verification}

> Esta página aborda como delegar seus próprios subdomínios à Braze. Use a verificação do remetente para configurar e delegar o controle de um subdomínio de envio dedicado à Braze, permitindo maior consistência de marca com seu domínio de remetente e links de rastreamento sob o mesmo subdomínio.

{% alert important %}
Esse recurso está em beta e está disponível apenas para equipes internas da Braze.
{% endalert %}

## Como a verificação do remetente funciona {#how-sender-verification-works}

A delegação de domínio é uma opção de configuração de DNS que permite delegar o controle de um subdomínio de envio específico à Braze. Por exemplo, se você usa "marketing.example.com" como seu subdomínio, a Braze gerencia os registros DNS necessários para recursos de envio de mensagens, como e-mail.

### Benefícios {#benefits}

Usar a verificação do remetente ajuda a simplificar a configuração e a manutenção. A Braze cria e atualiza o que for necessário, o que significa menos oportunidades de configuração incorreta de DNS.

### Considerações {#considerations}

- Escolha um subdomínio dedicado.
- Após concluir a delegação de domínio, a Braze gerencia seus registros DNS para o subdomínio delegado.
- Se você tem várias marcas ou espaços de trabalho da Braze, é possível selecionar um subdomínio delegado por marca.
- Há um limite de 50 domínios de envio e 50 domínios de rastreamento para a verificação do remetente. Se precisar adicionar mais, entre em contato com o suporte da Braze.

## Etapa 1: Concluir os pré-requisitos {#step-1-complete-prerequisites}

No dashboard da Braze, acesse **Configurações** > **Verificação do remetente** em **Configurações da empresa** e trabalhe com seu gerente de integração para concluir os seguintes pré-requisitos:

- Adicionar um pool de IP
- Adicionar endereços IP
- Adicionar um domínio delegado e verificar o registro NS

## Etapa 2: Adicionar seu subdomínio de envio {#step-2-add-your-sending-subdomain}

1. Na seção **Domínios de envio**, selecione **Adicionar domínio de envio**.
2. Preencha os campos **Mail from** e **Domínio de envio** com seu subdomínio de envio para o pool de IP. Um exemplo é "marketing.mail.example.com".
3. Selecione seu domínio delegado no menu suspenso.
4. Em seguida, selecione **Enviar**.

![Formulário mostrando campos para endereço Mail from e domínio de envio, com um menu suspenso de domínio delegado e botão Enviar.]({% image_buster /assets/unlisted_docs/img/sender_verification/sending_subdomain.png %}){: style="max-width:85%;"}

Leva de 5 a 10 minutos para os registros DNS se propagarem. Após a conclusão, você receberá um e-mail de notificação informando que seu domínio está pronto para uso.

{% alert important %}
Os domínios não podem ser alterados após o envio. A Braze cria registros DNS para verificação e autenticação e os adiciona às suas configurações de DNS.
{% endalert %}

## Etapa 3: Adicionar seu subdomínio de rastreamento {#step-3-add-your-tracking-subdomain}

Após criar um subdomínio e tê-lo verificado:

1. Selecione **Adicionar domínio de rastreamento**.
2. Insira o subdomínio de rastreamento. Por exemplo, se seu subdomínio de rastreamento é "click", seu subdomínio seria: "click.marketing.mail.example.com".
3. Selecione o domínio de envio associado no menu suspenso.
4. Em seguida, selecione **Enviar**.

![Um exemplo de domínio de rastreamento a ser adicionado.]({% image_buster /assets/unlisted_docs/img/sender_verification/tracking_domain.png %}){: style="max-width:85%;"}

Pode levar até 24 horas para esses registros DNS se propagarem, mas geralmente leva menos tempo. Após a conclusão, você receberá um e-mail de notificação informando que seu domínio está pronto para uso.

{% alert important %}
O domínio de rastreamento deve ser um subdomínio do domínio de envio para a delegação de DNS funcionar corretamente.
{% endalert %}

## Etapa 4: Selecionar os espaços de trabalho {#step-4-select-the-workspaces}

Em seguida, selecione os espaços de trabalho que devem ter acesso ao domínio e selecione **Confirmar**. Opcionalmente, você pode adicionar automaticamente um domínio de envio a novos espaços de trabalho quando eles forem criados.

![Caixa de diálogo mostrando caixas de seleção de espaços de trabalho com opção de adicionar automaticamente o domínio de envio a novos espaços de trabalho e um botão Confirmar.]({% image_buster /assets/unlisted_docs/img/sender_verification/select_workspaces_domain.png %}){: style="max-width:85%;"}

## Etapa 5: Testar o envio de e-mail {#step-5-test-your-email-sending}

Quando os domínios de envio e rastreamento estiverem com o status **Pronto para uso**, você pode testar o envio de e-mail fazendo o seguinte:

1. No seu espaço de trabalho, acesse **Configurações** > **Configurações de e-mail**.
2. Verifique se o novo domínio de envio está listado na seção **Display Name Address**.
3. Adicione o endereço de e-mail usando o novo domínio (como "marketing@marketing.mail.example.com").
4. Selecione **Salvar**.
5. Em seguida, crie uma Campaign de e-mail de teste e envie um e-mail para você mesmo para confirmar o seguinte:
- Seu e-mail foi entregue com sucesso.
- O endereço de remetente está correto.
- O link de rastreamento de cliques usa o domínio de rastreamento.
- Os cabeçalhos do seu e-mail são exibidos corretamente.