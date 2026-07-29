---
nav_title: Email deliverability glossary
article_title: Email deliverability glossary
layout: glossary_page
glossary_top_header: "Email deliverability glossary"
glossary_top_text: "This glossary defines common email deliverability and email infrastructure terms you may encounter when sending email through Braze."
page_order: 1
page_type: glossary
description: "This glossary defines common email deliverability and email infrastructure terms you may encounter when sending email through Braze."
channel:
  - email

glossaries:
  - name: Allowlist
    description: A list of contacts that the user deems are acceptable to receive email from and should not be filtered or sent to the trash or spam folder.
  - name: Block
    description: A block bounce is the result of an email not being accepted for delivery by the mailbox provider. Many mailbox providers block email from IP addresses or domains that have been reported to send spam or viruses or have content that violates email policy or spam filters. SendGrid uses "block" to refer to what is typically called a soft bounce. At SendGrid, a block results when an email is not accepted for delivery due to a technical or temporary reason.
  - name: Blocklist
    description: Lists of IP addresses that have been reported and listed as known sources of spam. There are public and private blocklists. Public blocklists are published and made available to the public—many times as a free service, sometimes for a fee.
  - name: Bounce
    description: Also known as a hard bounce, an address that has bounced is permanently undeliverable and is suppressed from subsequent sends. For more information about bounces in Braze, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#bounces">Bounces</a> in the email analytics glossary.
  - name: Bulk folder
    description: Also referred to as junk or spam folder in some email clients.
  - name: CAN-SPAM Act
    description: "US law regulating commercial email (full name: Controlling the Assault of Non-Solicited Pornography and Marketing Act of 2003)."
  - name: Click rate
    description: The rate at which recipients have clicked a link within the message. For more information, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-clicks">Unique Clicks</a> in the email analytics glossary.
  - name: Content filters
    description: Software filters that block email based on text, words, phrases, or header information within the email itself.
  - name: Deferred
    description: If a message is unable to be delivered on its first attempt, that message is considered as being deferred. Most deferred mail eventually delivers.
  - name: Deliverability
    description: In the deliverability community, deliverability primarily focuses on the ability to reach the inbox. This rate is not something Braze can track directly, so you need to use other available data to make inferences about inbox placement.
  - name: Delivery rate
    description: The rate of successful deliveries, regardless of inbox placement or whether the mail gets opened. For more information, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#deliveries">Deliveries %</a> in the email analytics glossary.
  - name: DKIM
    description: DomainKeys Identified Mail lets an organization take responsibility for a message while it is in transit. The organization is a handler of the message, either as its originator or as an intermediary. Their reputation is the basis for evaluating whether to trust the message for delivery.
  - name: DMARC
    description: Domain-based Message Authentication, Reporting & Conformance is a technical specification created by organizations to reduce email phishing and fraud. It is currently used by all major mailbox providers, including Google, Yahoo, and Microsoft.
  - name: Drop
    description: SendGrid keeps email lists to track bounces, spam reports, and unsubscribes for each of their users. If a user sends a message to an email address that exists on one of these lists within their account, SendGrid automatically drops the message (that is, does not send to the address).
  - name: ESP (email service provider)
    description: Company that provides email sending and transport capability to email marketers. Many of today's marketing, CRM, and customer engagement platforms include an email-sending component and are commonly referred to as ESPs in reference to email-sending capability. Examples include ConstantContact, MailChimp, Emarsys, Salesforce Marketing Cloud, Cheetah Digital, and Sailthru.
  - name: Feedback loop (FBL)
    description: The mechanism by which senders are notified of spam reports so that they can calculate a spam report rate and remove the address from future sends.
  - name: Hard bounce
    description: Message sent to an invalid, closed, or nonexistent email account. Typically, hard-bounced emails can be identified with a 500 series SMTP reply code. For more information, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#hard-bounce">Hard Bounce</a> in the email analytics glossary.
  - name: IP
    description: A unique number assigned to each device connected to the Internet.
  - name: ISP (Internet Service Provider)
    description: Company that provides Internet services to consumers like AT&T, British Telecom, Comcast (Xfinity), Cox, Orange, Sky, Spectrum, Tiscali, TalkTalk, and Virgin. Also colloquially includes mailbox providers like Gmail, Yahoo, and Microsoft.
  - name: List hygiene
    description: The act of maintaining a list so that hard bounces and unsubscribed names are removed from mailings.
  - name: List-Unsubscribe
    description: The List-Unsubscribe header is text you can include in the header portion of your messages, allowing recipients to see an unsubscribe button they can select to automatically stop future messages.
  - name: Mailbox provider (MBP)
    description: The provider of email access to recipients, such as Gmail, Yahoo, and Microsoft.
  - name: MX record
    description: An MX record is a type of resource record in the Domain Name System (DNS) specifying how Internet email should be routed using the Simple Mail Transfer Protocol (SMTP).
  - name: NDR (non-delivery report)
    description: Feedback from an email receiver when they choose not to accept an email for delivery, in the form of an SMTP response. NDRs are often referred to as bounces.
  - name: Opens unique rate
    description: The rate at which the open tracking pixel was loaded, only counting unique recipients (no duplicates). For more information, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-opens">Unique Opens</a> in the email analytics glossary.
  - name: Phishing
    description: A form of identity theft in which a scammer uses an authentic-looking email to trick recipients into giving out sensitive personal information, such as credit card or bank account numbers, Social Security numbers, and other personally identifiable information (PII).
  - name: Re-engagement campaign
    description: An email campaign sent to inactive or non-responders in an attempt to win them back and get them engaged with your emails again in the form of opens, clicks, and conversions. A re-engagement campaign can be sent to inactive as a stand-alone campaign or as a series of campaigns.
  - name: Reverse DNS (rDNS)
    description: The process in which an IP address is matched correctly to a domain name, instead of a domain name being matched to an IP address. If a spam filter or program can't match the IP address to the domain name, it can reject the email.
  - name: Smart Network Data Services (SNDS)
    description: Offered by Windows Live Hotmail, SNDS provides data to senders based on actual mail sent to Hotmail subscribers. Metrics reported on include complaints, SmartScreen filter results, and spam trap hits.
  - name: Soft bounce
    description: Any bounce due to a temporary or transient issue like "mailbox full," "user over quota," "mail blocked for spam-like characteristics," "message rejected because it violates organization policies," or "server temporarily not available." SendGrid calls these "blocks."<br><br>Delivery to any soft bounce believed to be a temporary issue (usually those with an SMTP 4xx code) is attempted again until the message is either delivered or 72 hours elapse. If a message that has soft bounced cannot be delivered after 72 hours, further delivery attempts are stopped and the failed message delivery is counted as a bounce. For more information, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#soft-bounce">Soft Bounce</a> in the email analytics glossary.
  - name: Spam
    description: Unwanted email. In the metrics, users must mark these emails as spam (so this count includes them in deliveries as the email needs to be delivered first). For more information, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">Spam</a> in the email analytics glossary.
  - name: SpamCop
    description: A blocklist and IP address database, formerly privately owned but now part of the email vendor Ironport. Many mailbox providers check the IP addresses of incoming emails against SpamCop's records to determine whether the address has been blocklisted due to spam complaints.
  - name: Spam rate
    description: The rate at which recipients have marked a message as being spam while viewing it. This rate does not include mail that lands in the spam folder. It also does not include complaints from mailbox providers who do not have a feedback loop, such as Gmail and iCloud. For more information, see <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">Spam</a> in the email analytics glossary.
  - name: Spam trap
    description: An email used to collect and detect spam by ISPs and antispam organizations. Also known as spamtrap. For more information, see <a href="/docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps">Deliverability pitfalls and spam traps</a>.
  - name: Suppression list
    description: Braze does not have suppression lists, however, you can create a sunset policy as documented in <a href="/docs/user_guide/channels/email/best_practices/sunset_policies">Sunset policies</a>. For more information about managing email subscriptions, see <a href="/docs/user_guide/channels/email/subscriptions">Subscriptions</a>.
  - name: Throttling
    description: The practice of regulating how many email messages a broadcaster sends to one mailbox provider or mail server at a time. Some mailbox providers bounce email if they receive too many messages.
  - name: Transactional mail
    description: Transactional messages are defined under CAN-SPAM as any email "facilitating, completing or confirming a previously agreed upon transaction." Unlike commercial messages, transactional messages aren't required to have a U.S. Postal Service address or an unsubscribe link.

---
