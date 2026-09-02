---
nav_title: Autoatendimento de e-mail
article_title: Autoatendimento de e-mail
page_order: 0
page_type: tutorial
channel: email
description: "Este artigo de instruções aborda como configurar domínios de envio e rastreamento com o autoatendimento de e-mail na Braze."
toc_headers: h2
---

# Autoatendimento de e-mail {#email-self-serve}

> Esta página aborda como configurar domínios de envio e rastreamento na Braze para que seu domínio de remetente e links de rastreamento compartilhem o mesmo subdomínio.

## Pré-requisitos {#prerequisites}

Para usar a configuração de e-mail por autoatendimento, você deve atender aos seguintes pré-requisitos:

- Ser um novo cliente em integração
- Ter a permissão de nível de empresa "Edit Domain Settings"
- Ter um pool de IP, endereços IP e um domínio verificado

## Considerações {#considerations}

- Planeje um subdomínio de envio com no mínimo três níveis. Como a Braze cria um subdomínio sob seu domínio delegado (como "marketing.example.com"), seu domínio de envio precisa ter pelo menos três níveis de profundidade (como "e.marketing.example.com").
- O domínio de envio deve ser subordinado a um domínio que você possui. Por exemplo, se você possui "example.com", um subdomínio poderia ser "mail.example.com", o que permite usar o endereço de envio "@mail.example.com".
- Limites de domínio se aplicam. O número total de domínios de rastreamento é limitado a 2 multiplicado pelo número de domínios verificados em seu contrato. Se precisar de mais, entre em contato com seu gerente de conta.

## Configuração {#setup}

### Etapa 1: Adicionar um domínio de envio {#step-1-add-a-sending-domain}

Seu subdomínio de envio é o endereço a partir do qual seus e-mails são enviados. Ele determina o endereço de remetente que seus destinatários veem.

1. Na seção **Domains**, selecione **Add domain**.
2. Adicione seu domínio de envio nos campos **Mail from** e **Sending domain** para o pool de IP.
    - O endereço **Mail from** (envelope sender ou return jornada) é o que lida com bounces nos bastidores. Seus destinatários não veem isso em um e-mail. Por exemplo, você pode usar "bounce" como subdomínio, de modo que o e-mail personalizado de mail from seja "bounce.mail.example.com". Usar esse subdomínio é uma prática recomendada para alinhamento DMARC SPF.
    - O **Sending domain** é o domínio no endereço de remetente que os destinatários veem em sua caixa de entrada. Por exemplo, se o endereço de remetente for "hello@e.mail.example.com", então "e.mail.example.com" é o domínio de envio.
{: start="3"}
3. Selecione seu domínio verificado no menu suspenso.

Os domínios de envio não podem ser alterados após serem enviados. A Braze cria registros DNS para verificação e autenticação e os adiciona às suas configurações de DNS. Se precisar excluir um domínio de envio, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obter assistência.

### Etapa 2: Adicionar um domínio de rastreamento {#step-2-add-a-tracking-domain}

Um domínio de rastreamento é usado para encapsular links em seus e-mails para fins de rastreamento de cliques e branding. Os destinatários veem isso quando passam o cursor sobre ou clicam em links em seus e-mails. Ele deve ser um subdomínio do seu domínio de envio ou domínio verificado para delegação DNS adequada.

1. Selecione se você está usando um **Verified domain** ou **Sending domain** para ser usado como subdomínio do seu domínio de rastreamento:
    - Se quiser que a URL de rastreamento corresponda ao domínio de envio para consistência de marca, selecione **Sending domain**.
    - Se quiser uma URL de rastreamento mais curta, selecione o **Verified domain**.

{: start="2"}
2. Insira seu subdomínio de rastreamento. Isso é adicionado antes do subdomínio selecionado anteriormente.

O exemplo a seguir mostra como o domínio de rastreamento é exibido no e-mail com base na sua seleção:

|  | Seleção | Domínio de rastreamento |
| --- | --- | ---|
| Domínio verificado | mail.example.com | links.mail.example.com |
| Domínio de envio | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Domínio de rastreamento por seleção" }

{: start="3"}
3. Selecione o subdomínio verificado ou de envio associado a ser usado no menu suspenso.
4. Selecione **Submit**. Você pode ver os domínios de envio e rastreamento com o status **Pending**.

Pode levar de 5 a 10 minutos para os registros DNS propagarem para domínios de envio. Quando seu domínio estiver pronto para uso, você receberá um e-mail de notificação. Os registros DNS para domínios de rastreamento podem levar até 24 horas para propagar, embora geralmente leve menos. Você pode ver o subdomínio de envio ficar pronto antes do domínio de rastreamento.

### Etapa 3: Selecionar espaços de trabalho {#step-3-select-workspaces}

Selecione os espaços de trabalho que devem ter acesso ao domínio e, em seguida, selecione **Confirm**. Você também pode optar por adicionar automaticamente o domínio de envio a novos espaços de trabalho quando eles forem criados.

### Etapa 4: Configurar links universais (opcional) {#step-4-set-up-universal-links-optional}

Links universais permitem que os links em suas mensagens abram diretamente no seu app móvel em vez de um navegador móvel. A Braze pode hospedar os arquivos de associação em seus domínios de rastreamento em seu nome.

{% alert note %}
Links universais são aplicados por domínio de rastreamento. O mesmo conteúdo de arquivo pode ser compartilhado entre domínios, mas cada domínio hospeda sua própria cópia.
{% endalert %}

1. Acesse **Settings** > **Company Settings** > **Verified Domains** > **Universal Links**.
2. Selecione **Set up universal links**.
3. Insira um nome para o conjunto de links universais.
4. Ative a configuração iOS e adicione seu arquivo AASA. JSON é o único tipo de arquivo aceito. A Braze lê o arquivo e mostra o número de IDs de app e componentes encontrados, além de uma prévia do arquivo gerado.
5. Ative a configuração Android e adicione seu arquivo Digital Asset Links da mesma forma. A Braze mostra os nomes dos pacotes, a impressão digital do certificado SHA-256 e o número de declarações, além de uma prévia.
6. Verifique cada prévia para confirmar que o conteúdo está correto e, em seguida, selecione **Next: Select tracking domains**. Apenas domínios de rastreamento verificados aparecem. Um conjunto pode ser aplicado a vários domínios de rastreamento.
7. Seu conjunto aparece na página Universal Links junto com seus domínios de rastreamento, canais, status iOS, status Android e data de criação. A Braze verifica se o arquivo AASA está hospedado corretamente para cada domínio e reporta o resultado na coluna de status.

### Etapa 5: Testar o envio de e-mail {#step-5-test-your-email-sending}

Depois que os domínios de envio e rastreamento mostrarem o status **Ready for use**, teste sua configuração:

1. No seu espaço de trabalho, acesse **Settings** > **Email Settings**.
2. Verifique se o novo domínio de envio está listado na seção **Display Name Address**.
3. Adicione um endereço de remetente usando o novo domínio (por exemplo, "hello@e.mail.example.com").
4. Selecione **Save**.
5. Crie uma Campaign de e-mail de teste e envie para você mesmo. Em seguida, confirme que:
    - Seu e-mail foi entregue com sucesso.
    - O endereço de remetente está correto.
    - Os links de rastreamento de cliques usam o domínio de rastreamento.
    - Os links universais estão abrindo o app ou website conforme esperado com base no dispositivo do destinatário.
    - Os cabeçalhos do e-mail são exibidos corretamente.

## Próximas etapas {#next-steps}

Após a verificação do remetente ser concluída, a Braze recomenda o aquecimento de IP para que suas mensagens cheguem às caixas de entrada de destino com uma taxa consistentemente alta. Após concluir essa configuração, consulte a equipe de integração da Braze para confirmar se seus domínios e o [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) estão funcionando.

## Solução de problemas {#troubleshooting}

### A propagação DNS está demorando mais do que o esperado {#dns-propagation-is-taking-longer-than-expected}

Os registros de domínio de envio geralmente propagam em 5 a 10 minutos. Os registros de domínio de rastreamento podem levar até 24 horas, dependendo das configurações de TTL do seu provedor DNS. Se a propagação demorar mais, confirme que os registros NS foram adicionados corretamente primeiro e, em seguida, entre em contato com o suporte da Braze.

### Não consigo remover um domínio verificado {#im-not-able-to-remove-a-verified-domain}

Domínios verificados não podem ser removidos diretamente no dashboard, pois isso pode potencialmente interromper seu envio se não for revisado adequadamente. Entre em contato com o suporte da Braze para ajudá-lo a remover o domínio da sua conta.

### Meus links universais não estão abrindo o app {#my-universal-links-arent-opening-the-app}

Verifique os status iOS e Android na página Universal Links primeiro. Se um domínio não estiver hospedando um arquivo válido, abra o conjunto, corrija a configuração e salve novamente. Se os status parecerem corretos, certifique-se de que você está testando a partir de um link em um e-mail em um dispositivo real, em vez de colar a URL na barra de endereços do navegador.

## Perguntas frequentes {#frequently-asked-questions}

### A Braze pode gerenciar meu certificado SSL sem delegação NS? {#can-braze-manage-my-ssl-certificate-without-ns-delegation}

Verified Domains requer registros NS (Name Server) para delegação de propriedade DNS para a Braze. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### Posso delegar um domínio raiz em vez disso? {#can-i-delegate-a-root-domain-instead}

Verified Domains é projetado e recomendado principalmente para uso com subdomínios. Não recomendamos delegar o domínio pai principal da sua marca por motivos de segurança, pois você perde visibilidade e controle sobre ele. Se quiser delegar um domínio pai, use um domínio pai que não seja usado em nenhum outro lugar além da Braze.

### Por que meu domínio verificado não pode ser também o domínio de envio? {#why-cant-my-verified-domain-also-be-the-sending-domain}

A Braze só pode criar um subdomínio de envio sob seu domínio verificado, que normalmente é um subdomínio do domínio pai (`mail.example.com`). Portanto, a profundidade mínima do domínio de envio nesse caso é de três níveis (`e.mail.example.com`), em vez dos dois níveis típicos.

### O que acontece se eu modificar algum dos meus registros NS após a configuração? {#what-happens-if-i-modify-any-of-my-ns-records-after-setup}

Os domínios verificados dependem totalmente da integridade dos registros NS. Se você fizer alterações em qualquer um dos seus registros NS, isso pode interromper o envio e o rastreamento de e-mails.

### Posso adicionar apenas uma das quatro linhas de registro NS, já que meu comando dig mostra todos os quatro registros? {#can-i-add-only-one-of-four-ns-record-lines-since-my-dig-command-shows-all-four-records}

Confirme que todos os quatro registros NS estão explicitamente presentes usando o comando `dig` e que o domínio é validado no dashboard antes de considerar a configuração concluída.