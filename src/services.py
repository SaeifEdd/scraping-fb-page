from facebook_scraper import get_posts
import time 
import os
from dotenv import load_dotenv
#import schemas
import crud 
from sqlalchemy.orm import Session


load_dotenv()

#def get_creds(cred_path):
#    with open(cred_path) as file:
#        EMAIL = file.readline().split('"')[1]
#        PASSWORD = file.readline().split('"')[1]
#    return (EMAIL, PASSWORD)


def get_fb_page_data(db: Session, page_name):
    email = os.getenv('email')
    pw = os.getenv('pw')
    creds = (email, pw)
    for post in get_posts(str(page_name),credentials= creds,
                      extra_info = True, pages = 3, allow_extra_requests = False):
        crud.create_post(db, post)
        time.sleep(5)
    
    return 
