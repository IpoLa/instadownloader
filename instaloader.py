# pip install instaloader

import instaloader

ig = instaloader.Instaloader()
dp = input('Enter Insta Username : ')
ig.doanload_profile(dp, profile_pic_only = True)
