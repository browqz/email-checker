import requests

def email_site_checker(email):
    sites = [
          "https://www.facebook.com/{}",
        "https://www.instagram.com/{}",
        "https://twitter.com/{}",
        "https://www.linkedin.com/in/{}",
        "https://github.com/{}",
        "https://www.root-me.org/{}",
        "https://www.youtube.com/{}",
        "https://www.tiktok.com/{}",
        "https://www.pinterest.com/{}",
        "https://soundcloud.com/{}",
        "https://steamcommunity.com/id/{}",
        "https://www.pornhub.com/users/{}",
        "https://www.twitch.tv/{}",
        "https://www.reddit.com/user/{}",
        "https://www.snapchat.com/add/{}",
        "https://www.quora.com/profile/{}",
        "https://www.myspace.com/{}",
        "https://www.meetup.com/members/{}",
        "https://www.tripadvisor.com/members/{}",
        "https://www.stackoverflow.com/users/{}",
        "https://www.goodreads.com/user/show/{}",
        "https://www.blogger.com/profile/{}",
        "https://www.wattpad.com/user/{}",
        "https://www.etsy.com/people/{}",
        "https://www.behance.net/{}",
        "https://www.flickr.com/people/{}",
        "https://www.last.fm/user/{}",
        "https://www.dribbble.com/{}",
        "https://www.kickstarter.com/profile/{}",
        "https://www.deviantart.com/{}",
    ]

    for site in sites : 
      url = site.format(email)
      response = requests.get(url)

      if response.status_code == 200:
          print(f"L'adresse e-mail {email} est associée sur {url}")
      else:
            print(f"L'adresse e-mail {email} n'est pas associée sur {url}")

def main():
    email_a_check = input("Quelle e-mail dois-je check ? ")
    email_site_checker(email_a_check)

if __name__ == "__main__":
  main()
  input("Presse Entré pour fermer le terminal...")
