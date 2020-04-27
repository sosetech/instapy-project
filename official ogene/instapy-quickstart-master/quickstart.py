






# imports
from instapy import InstaPy
from instapy import smart_run
import random

# login credentials
insta_username = ''
insta_password = ''

tags= ['data','analysis','ai','ml','machinelearning','informationtechnology','java','python','roboti','programming','coding','tableau']
users = ['urdatascientist','azurewill','pure.python','xyranks','data_science_learn','data__analysis','what_the_code',]
# get a session!
session = InstaPy(username=insta_username, password=insta_password)


with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=2500,max_following=2200)
    
    #use the value of `False` to permanently turn it off
    session.set_simulation(enabled=False)
    
    session.set_user_interact(amount=2, randomize=True, percentage=40)
    session.set_do_follow(enabled=True, percentage=50)
    session.set_do_like(enabled=True, percentage=80)
    
    
    
    # activity
    session.like_by_tags(tags,
                         amount=random.randint(30, 45), interact=True)
    
    session.follow_by_tags(tags,
                         amount=random.randint(10, 12), interact=True) 
    
    
    session.like_by_feed(amount=random.randint(30, 35), randomize=True, interact=True)
    
    session.follow_commenters(users, amount=5, daysold=365, max_pic = 100, sleep_delay=600, interact=True)
    
    session.unfollow_users(amount=random.randint(10, 15), instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=120*60*60, sleep_delay=600)
