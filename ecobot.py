import requests, re, argparse, math, pickle, os

class EcoBot:
    def __init__(self, wlist, verbose=False):
        self.session = requests.Session()
        self.wordlist = wlist
        self.searchcount = 0
        self.treecount = 0
        self.verbose = verbose

    def navigate(self):
        with open(self.wordlist) as file:
            for searchterm in file:
                searchterm = searchterm.rstrip("\n")

                if self.verbose:
                    print("Current search term: " + searchterm)

                r = self.session.get("https://www.ecosia.org/search?q=" + searchterm)
                match = re.search(r"<p class=\"tree-counter-text-mobile\">(\d+)", r.text)

                current_searchcount = int(match.group(1))
                current_treecount = int(math.floor(current_searchcount / 45)) # According to ecosia, around 45 searches are required to plant 1 tree
                if current_searchcount > self.searchcount and self.verbose:
                    print("Number of 'valid' searches: " + str(current_searchcount))
                    self.searchcount = current_searchcount
                if current_treecount > self.treecount:
                    print("Yay! {0} trees planted!".format(current_treecount))
                    self.treecount = current_treecount

    def save_session(self, name="session"):
        if not os.path.isdir("sessions"):
            os.makedirs("sessions")

        with open("sessions/" + name, "wb") as session:
            pickle.dump(self.session.cookies, session)

    def load_session(self, name="session"):
        print("Trying to load previous session...")
        if os.path.isfile("sessions/" + name):
            with open("sessions/" + name, "rb") as session:
                self.session.cookies = pickle.load(session)
            print("Session restored successfully!")
        else:
            print("Session does not exist! Continuing anyway...")

    def destroy_sessions(self, session="session"):
        if session == "*":
            for session in os.listdir("sessions"):
                print("Destroying session " + session + "...")
                os.remove("sessions/" + session)
        else:
            if not os.path.isfile("sessions/" + session):
                print("Failed to destroy session (it does not exist)!")
                return

            print("Removing session " + session + "...")
            os.remove("sessions/" + session)

parser = argparse.ArgumentParser(description="An 'ecological' bot for ecosia search engine [https://www.ecosia.org/]")
parser.add_argument('-l', help="wordlist.txt or any other file", nargs="?", default="wordlist.txt", required=True)
parser.add_argument('-v', help="toggle verbose output", action="store_true")
parser.add_argument('--loop', help="toggle repeat the same wordlist", action="store_true", default=False)
parser.add_argument('--save', help="save session under custom name", nargs="?", default="session")
parser.add_argument('--load', help="load custom session", nargs="?", default="session")
parser.add_argument('--destroy', help="destroy a saved session (* = all)", nargs="?")
parser.add_argument('--nosave', help="toggle do not store session", action="store_true", default=False)

args = parser.parse_args()

scraper = EcoBot(args.l, args.v)
try:
    if args.destroy:
        scraper.destroy_sessions(args.destroy)
    scraper.load_session(args.load)
    print("Browsing the web using ecosia [https://www.ecosia.org/]")
    loop = True
    while loop:
        scraper.navigate()
        if args.loop == False:
            loop = False
except KeyboardInterrupt:
    print("Force quitting...")
finally:
    if args.nosave == False:
        print("Saving current session...")
        scraper.save_session(args.save)
        print("Session saved!")
    print("Application has been terminated.")
