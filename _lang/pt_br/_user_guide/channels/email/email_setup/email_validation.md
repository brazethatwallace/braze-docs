---
nav_title: Validação de e-mail
article_title: Validação de e-mail
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Este artigo de referência aborda as regras de validação da parte local e do host para endereços de e-mail."
channel: email

---

# Validação de e-mail {#email-validation}

> Este artigo de referência aborda as regras de validação da parte local e do host para endereços de e-mail. A validação é usada para endereços de e-mail do dashboard, endereços de e-mail do usuário final (seus clientes) e endereços de origem e de resposta de uma mensagem de e-mail.

## Como funciona {#how-it-works}

A Braze valida um endereço de e-mail quando ele é atualizado, importado por API, upload de CSV, SDK ou modificado no dashboard. Endereços de e-mail não podem incluir espaços em branco. Se você usar a API, espaços em branco retornam um erro `400`.

A Braze rejeita determinados caracteres e marca o endereço como inválido. Se um e-mail retornar bounce, a Braze marca o endereço como inválido e não altera o status da inscrição. Se o corpo do e-mail contiver caracteres [ASCII](https://en.wikipedia.org/wiki/ASCII) não padrão, a Braze não envia o e-mail.

{% details Caracteres aceitos %}
- Letras (A-Z)
- Números (0-9)
- Símbolos
	- -
	- &#94;
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- `
	- |
	- ~
	- !
	- ?
	- . (somente entre letras ou outros caracteres)
{% enddetails %}

{% details Caracteres não aceitos %}
- Espaços em branco (ASCII e Unicode)
{% enddetails %}

Essa validação é uma verificação de sintaxe, não um serviço de validação. Um dos objetivos desse processo é suportar caracteres internacionais (como UTF-8) na parte local do endereço de e-mail.

A Braze valida a sintaxe tanto da parte local quanto da parte do host de um endereço de e-mail. A parte local é tudo antes do arroba (@); a parte do host é tudo depois. A parte local pode começar e terminar com qualquer caractere permitido, exceto ponto (.). Esse processo não verifica se o domínio possui um servidor MX válido ou se um usuário existe naquele domínio.

{% alert important %}
Se a parte do domínio contiver caracteres ASCII não padrão, será necessário codificá-la em [Punycode](https://www.punycoder.com/) antes de fornecê-la à Braze.
{% endalert %}

Se a Braze receber uma solicitação para adicionar um usuário com um endereço de e-mail inválido, a API retorna um erro. Para upload de CSV, a Braze cria o usuário, mas omite o endereço de e-mail inválido.

## Regras de validação da parte local {#local-part-validation-rules}

### Validação geral de e-mail {#general-email-validation}

Para a maioria dos domínios, a parte local deve seguir estes parâmetros:
- Pode conter qualquer letra, número, incluindo letras e números Unicode, bem como os seguintes caracteres: (+) (&) (#) (_) (-) (^) ou (/)
- Pode conter, mas não pode começar ou terminar com o seguinte caractere: (.)
- Não pode conter aspas duplas (")
- Deve ter entre 1 e 64 caracteres

A seguinte expressão regular pode ser usada para validar se um endereço de e-mail será considerado válido:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Endereços Gmail {#gmail-addresses}

Se a parte do domínio for Gmail, a parte local deve ter pelo menos dois caracteres e seguir a validação por expressão regular listada anteriormente nesta seção.

### Domínios Microsoft {#microsoft-domains}

Se o domínio do host incluir "msn", "hotmail", "outlook" ou "live", a Braze usa a seguinte expressão regular para validar a parte local: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

A parte local do endereço Microsoft deve seguir estes parâmetros:

- Pode começar com um caractere (a-z), um sublinhado (_) ou um número (0-9).
- Pode conter qualquer caractere alfanumérico (a-z ou 0-9) ou um sublinhado (_)
- Pode conter os seguintes caracteres: (.) ou (-)
- Não pode começar com um ponto (.)
- Não pode conter dois ou mais pontos consecutivos (.)
- Não pode terminar com um ponto (.)

O teste de validação verifica se a parte local que precede o "+" corresponde à expressão regular.

## Regras de validação da parte do host {#host-part-validation-rules}

A parte do host não pode ser um endereço IPv4 ou IPv6. O domínio de nível superior (como .com, .org, .net) não pode ser totalmente numérico.

A seguinte expressão regular é usada para validar o domínio:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

O nome de domínio deve atender a estes parâmetros:

- Consiste em dois ou mais rótulos separados por ponto
	- Cada parte de um nome de domínio é chamada de "rótulo". Por exemplo, o nome de domínio "example.com" consiste no rótulo "example" e no rótulo "com".
- Deve conter pelo menos um ponto (.)
- Não pode conter dois ou mais pontos consecutivos
- Cada rótulo separado por ponto deve:
	- Conter apenas caracteres alfanuméricos (a-z ou 0-9) e o hífen (-)
	- Começar com um caractere alfanumérico (a-z ou 0-9)
	- Terminar com um caractere alfanumérico (a-z ou 0-9)
	- Conter de 1 a 63 caracteres

### Validação adicional necessária {#additional-validation-required}

O rótulo final do domínio deve ser um domínio de nível superior (TLD) válido, determinado por tudo que vem após o último ponto (.). Esse TLD deve constar na [lista de TLDs da ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). O validador da Braze verifica apenas a sintaxe. Ele não detecta erros de digitação ou endereços inexistentes.

{% alert important %}
Unicode é aceito apenas para a parte local do endereço de e-mail. Unicode não é aceito para a parte do domínio, mas ela pode ser codificada em Punycode.
{% endalert %}