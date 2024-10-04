def normalize_email(email):
    try:
        email = email.replace(" ","")
        email_name, domain_part = email.strip().split('@', 1)
        email = f"{email_name.lower()}@{domain_part.lower()}"
    except Exception as e:
        raise ValueError("Not a valid email address")
    return email