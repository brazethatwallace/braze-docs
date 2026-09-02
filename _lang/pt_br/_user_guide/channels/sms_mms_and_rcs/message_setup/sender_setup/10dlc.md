---
nav_title: "A2P 10DLC"
article_title: "A2P 10DLC"
page_order: 2.9
description: "Este artigo aborda o A2P 10DLC, por que o registro 10DLC é necessário para clientes de long code nos EUA, informações úteis sobre custos e throughput, e como começar o processo de registro."
page_type: reference
channel:
  - SMS

---

# Application-to-Person 10-Digit Long Codes {#application-to-person-10-digit-long-codes}

> A2P 10DLC refere-se a um sistema nos Estados Unidos que permite que empresas enviem mensagens do tipo Application-to-Person (A2P) por meio de um número de telefone padrão de 10 dígitos (10DLC). Esses long codes registrados recebem maior throughput, melhor entregabilidade e conformidade aprimorada em comparação com o long code padrão.

{% alert important %}
Todos os clientes que atualmente possuem e/ou usam long codes dos EUA para enviar mensagens a clientes nos EUA são obrigados a registrar seus long codes para 10DLC; aqueles que não o fizerem terão uma filtragem intensa de todas as mensagens. Esse processo de inscrição leva de 4 a 6 semanas.
{% endalert %}

## Por que é necessário {#why-its-necessary}

O serviço 10DLC foi criado especificamente para facilitar o envio de mensagens A2P usando long codes. Historicamente, os long codes eram destinados a mensagens Person-to-Person (P2P), mas quando usados para fins de marketing, faziam com que as empresas ficassem limitadas por baixo throughput e filtragem elevada.

O 10DLC ajuda a aliviar esses problemas ao oferecer:
- **Maior throughput**: Números 10DLC suportam um volume maior de mensagens do que long codes comuns.
- **Melhor entregabilidade**: Números 10DLC são designados para tráfego A2P, então as mensagens enviadas com esses números têm mais chances de chegar ao destinatário e menos chances de serem filtradas ou rejeitadas pela operadora do que mensagens enviadas por long codes locais comuns.
- **Conformidade aprimorada**: Usar um long code local para envio de mensagens de texto comerciais vai contra as diretrizes da [CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Os números 10DLC foram designados para envio de mensagens em massa e permitem que as marcas cumpram as regulamentações do setor sem depender de short codes.
- **Econômico**: O 10DLC é uma ótima opção para empresas que desejam começar a enviar SMS ou enviar SMS em pequenos volumes. Para marcas que enviam volumes maiores de mensagens, acima de 100.000 mensagens por dia, recomendamos o uso de um short code.

Desde 2019, as operadoras começaram a adotar o 10DLC para mensagens comerciais, com a Verizon e a AT&T atualmente suportando o 10DLC, e esperamos que todas as principais operadoras sigam em breve. Embora possa causar inconvenientes no curto prazo, no longo prazo, os clientes terão melhores taxas de entregabilidade enquanto protegem seus consumidores de mensagens indesejadas.

## O que você precisa saber {#what-you-need-to-know}

### Acesso {#access}

O registro de long codes com A2P 10DLC levará de 4 a 6 semanas.

### Custos {#costs}

O registro com A2P 10DLC pode incluir vários tipos de taxas:

| Tipo de taxa | Descrição |
| -------- | ---------- |
| Taxas de registro | Taxas nominais aplicadas ao registrar sua marca e caso de uso em todas as principais redes dos EUA. |
| Taxas de verificação secundária | As marcas podem contestar sua [pontuação de confiança da marca](#trust-score) e solicitar um processo de verificação secundária para melhorar seu throughput geral; há uma taxa associada a esse processo. |
| Taxas da operadora | Taxas cobradas pelas operadoras para mensagens SMS e MMS de saída enviadas aos usuários após o registro 10DLC. A partir de 1º de outubro de 2021, as taxas da operadora serão mais altas para tráfego não registrado (long codes padrão) do que para tráfego registrado (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custos" }

Visite o artigo da Twilio sobre 10DLC para conferir as [estimativas de taxas](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) atualizadas.

### Throughput {#throughput}

O throughput de mensagens para seu 10DLC depende de vários fatores, incluindo a pontuação de confiança da marca, limites diários de mensagens e seus casos de uso de envio de mensagens.

#### Pontuação de confiança da marca {#trust-score}

O Campaign Registry (TCR) é uma agência terceirizada que usa um algoritmo de reputação para avaliar critérios específicos relacionados à sua empresa e atribuir uma pontuação de confiança que determina o throughput de mensagens para cada marca. Essa pontuação de confiança será atribuída quando um cliente se registrar para o envio de mensagens 10DLC nos EUA. Quanto maior a pontuação de confiança, melhor será a taxa de MPS (MPS) que você terá.

|     | Pontuação de confiança | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Alta | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Média | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Baixa | 1-49 | 4 MPS | 4 MPS | 4 MPS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Brand trust score #trust-score" }

{% alert tip %}
Empresas listadas no Índice Russell 3000 receberão alto throughput e pontuação de confiança da marca após o registro e revisão do 10DLC.
{% endalert %}

#### Limites diários de mensagens {#daily-message-limits}

Os limites diários variam de 2.000 a 200.000 mensagens, dependendo da sua pontuação de confiança da marca, e se aplicam a todos os long codes. Embora pontuações de confiança altas venham com um throughput de 60 MPS, quaisquer limites diários de mensagens definidos pela operadora ainda se aplicam. Isso significa que short codes seriam uma opção melhor se o pico diário de mensagens de uma marca for maior do que o limite diário imposto.

#### Casos de uso de envio de mensagens {#messaging-use-cases}

O throughput também é afetado pelo tipo de caso de uso de envio de mensagens que você escolher. A maioria dos clientes se enquadrará no caso de uso de marketing padrão ou marketing misto. Outros casos de uso menos comuns estarão sujeitos a valores de throughput diferentes.

Dependendo do seu caso de uso, a pontuação de confiança necessária para atingir o throughput máximo irá variar. As tabelas a seguir listam os casos de uso padrão e as faixas comuns de pontuação de confiança por caso de uso. Para casos de uso especiais, como serviços de emergência ou caridade, consulte a [documentação da Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Casos de uso padrão | Descrição |
| ------------------ | ----------- |
| Marketing | Conteúdo promocional, como vendas e ofertas por tempo limitado. |
| Misto | Campanha que abrange múltiplos casos de uso, como atendimento ao cliente. |
| Ensino superior | Campanhas para instituições de ensino superior. |
| Pesquisas e votações | Pesquisas e votações não políticas, como pesquisas de satisfação do cliente. |
| PSA | PSAs para conscientização sobre um determinado tema. |
| Atendimento ao cliente | Suporte, gerenciamento de conta e outras interações com o cliente. |
| Notificações de entrega | Status de mensagens de entrega. |
| Notificações de conta | Notificações sobre o status de uma conta. |
| 2FA | Qualquer autenticação ou verificação de conta, como OTP. |
| Alertas de segurança | Notificação de um sistema comprometido. |
| Alertas de fraude | Mensagens sobre atividade potencialmente fraudulenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso de envio de mensagens" }

{% tabs %}
{% tab Caso de uso declarado %}
Um caso de uso declarado significa que você escolheu um caso de uso específico que não é marketing (por exemplo, 2FA ou notificações de conta).

| Pontuação de confiança | Throughput total para as principais redes dos EUA | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Casos de uso de envio de mensagens" }

{% endtab %}
{% tab Caso de uso de marketing misto %}

Casos de uso de marketing misto podem ser registrados para clientes que desejam enviar mensagens para múltiplos casos de uso a partir do mesmo conjunto de números ou para marketing.

| Pontuação de confiança | Throughput total para as principais redes dos EUA | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Casos de uso de envio de mensagens" }

{% endtab %}
{% endtabs %}

Visite o artigo da Twilio sobre 10DLC para conferir as [estimativas de throughput](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) atualizadas.

## Próximas etapas {#next-steps}

Os clientes que ainda não se registraram para o 10DLC devem trabalhar com seu CSM para registrar seus long codes. **Se os clientes não registrarem seus long codes, a partir de 1º de outubro de 2021, qualquer remetente A2P usando long codes terá uma filtragem intensa de todas as mensagens.** Entre em contato com seu CSM para iniciar o registro do seu 10DLC.