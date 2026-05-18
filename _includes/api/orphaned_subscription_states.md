## How Braze handles orphaned subscription states

An orphaned subscription state is a subscription state stored for a phone number or email address that isn't associated with any user profile. For SMS, email, WhatsApp, and LINE, Braze handles orphaned subscription states as follows:

- If a user profile is deleted and that user was the only profile associated with a given phone number or email address, the subscription state for that phone number or email address is deleted immediately.
- If you call `/subscription/status/set` with a phone number or email address that is not currently associated with any user profile, Braze stores that subscription state for up to 30 days, after which it is automatically deleted.
- If a new user profile is created with a phone number or email address that has an orphaned subscription state stored for it, that user inherits the stored subscription state but only within the 30-day window. This 30-day grace period is intentional and exists to handle race conditions where the subscription state is immediately before creating the associated user profile.