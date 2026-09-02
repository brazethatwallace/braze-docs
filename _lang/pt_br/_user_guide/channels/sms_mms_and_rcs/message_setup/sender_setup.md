---
nav_title: Configuração de remetente
article_title: Remetentes de SMS, MMS e RCS
page_order: 2
description: "Este artigo fornece uma visão geral dos códigos e remetentes disponíveis para envio de mensagens SMS, MMS e RCS."
page_type: reference
alias: /sending_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

{% multi_lang_include channels/sms/short_and_long_codes.md %}

## Requisitos específicos de MMS {#mms-specific-requirements}

### Requisitos de remetente MMS {#mms-sender-requirements}

> MMS e SMS estão ambos vinculados ao canal de SMS da Braze. Para acessar MMS na sua conta, é necessário adquirir o SMS para aqueles que ainda não compraram o acesso. Clientes de SMS existentes podem acessar MMS após adquiri-lo.

Atualmente, o MMS é compatível com short codes dos EUA (números de 5 a 6 dígitos), long codes dos EUA e do Canadá (números de 10 dígitos) e números de clientes dos EUA e do Canadá. O MMS é compatível com números toll-free por determinados prestadores de serviço.

É possível enviar MMS para números fora dos EUA e do Canadá, mas as mensagens MMS são convertidas em uma mensagem SMS com um link para o ativo de mídia.

### Short codes MMS {#mms-short-codes}

Alguns usuários podem não implementar ou usar short codes MMS, mas eles estão disponíveis caso sejam necessários posteriormente.

Para usuários que obtiveram seus short codes antes de a Braze oferecer suporte a MMS, todos os clientes existentes com short codes dos EUA são elegíveis para ativar MMS instantaneamente. Entre em contato com seu CSM se essa situação se aplica a você e você deseja ativar o MMS.

{% alert important %}
Ao ativar o MMS para short codes que anteriormente não tinham MMS ativado, os short codes podem precisar ser reaprovados em um processo de aprovação que pode levar semanas. É importante considerar esse prazo ao decidir ativar o MMS.
{% endalert %}

#### Práticas recomendadas para short codes MMS {#mms-short-code-best-practices}

- Na Braze, recomendamos fortemente manter as mensagens transacionais e promocionais separadas, cada uma com short codes diferentes. Como o MMS está vinculado ao canal de SMS, e o canal de SMS é altamente regulamentado, os clientes podem ser obrigados a pagar uma penalidade monetária por uso indevido do canal e ter seu short code suspenso (o que é irreversível). Manter as mensagens transacionais e promocionais vinculadas a short codes diferentes protege suas mensagens transacionais.
- Se os clientes já possuem um short code dedicado a mensagens promocionais e ele está habilitado para MMS, não é necessário um short code separado para MMS.

### Long codes MMS {#mms-long-codes}

Os clientes podem enviar MMS com long codes. Para isso, você deve garantir que seus long codes estejam habilitados para MMS. Isso pode ser feito inicialmente durante a configuração ou posteriormente de dentro da sua conta.

Mensagens MMS não podem ser enviadas com um ID de remetente alfanumérico.

### Limites de mensagens MMS e throughput {#mms-message-limits-and-throughput}

O throughput de MMS é de um Segment por segundo por meio de um long code.

As operadoras impõem seus próprios limites de tamanho de arquivo, que determinam o sucesso dos envios de MMS. Esses limites podem variar por região e operadora, então a Braze recomenda não exceder 600&nbsp;KB para seu ativo multimídia e também incluir um corpo de mensagem. No criador de SMS ou MMS da Braze, uploads acima de 1&nbsp;MB são bloqueados. A mensagem de erro recomenda fazer upload de um arquivo de 600&nbsp;KB ou menos. Também recomendamos testar para confirmar que sua mídia pode ser entregue nas operadoras dos seus usuários.

#### Limites de tamanho de arquivo por operadora {#carrier-file-size-limits}

| Tamanho&nbsp;do arquivo | Tratamento pela operadora |
| --- | --- |
| 300&nbsp;KB | Todas as operadoras devem lidar de forma confiável com mensagens MMS desse tamanho. |
| 600&nbsp;KB | Este é considerado o tamanho máximo padrão de arquivo para MMS na maioria das operadoras. |
| 1&nbsp;MB | A maioria das operadoras dos EUA e do Canadá pode lidar com mensagens MMS desse tamanho, embora isso possa variar por operadora. Algumas operadoras podem permitir tamanhos de arquivo maiores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de tamanho de arquivo por operadora" }

#### Tipos de arquivo aceitos {#accepted-file-types}

A Braze aceita arquivos JPEG, GIF, PNG e VCF e permite anexar um único ativo multimídia à sua mensagem MMS.