import urllib.request
from os import system
from time import sleep


sleep_time = 3 # this is check if the site is up every three seconds (incase requests times out)

# ^ failsafe timeout 


def site_is_up():
    try:
        system("say 'E-class is up'")
    except:
        # not sure if this works on windows, hopefully it does
        system("echo 'E-class is up'|ptts")
    exit("eclass is up !!")


def check_if_site_is_up():
    status_code = None
    try:
        status_code = urllib.request.urlopen("https://eclass.yorku.ca").getcode()
        if status_code == 200:
            return True
    except:
        # who cares about handling errors amiright
        pass
    return False


def main():
    while True:
        if check_if_site_is_up():
            site_is_up()
            # break
        sleep(sleep_time)



if __name__ == "__main__":
    print("\nThe program has started, it will notify you once the site is up and running..")
    main()


