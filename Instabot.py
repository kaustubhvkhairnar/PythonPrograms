from selenium import webdriver
from time import sleep
from time import time
import sys

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print()
        print("Unfollowers list")
        print()
        for i in range(len(not_following_back)):
            print(i+1,not_following_back[i])
            
        print()
        print("Total number of unfollowers :-",i+1)

    def _get_names(self):
        sleep(2)
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        #/html/body/div[4]/div/div[2]
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names
        
def displayhelp():
    border = "-"*84;
    print("-"*40+"HELP"+'-'*40)
    print()
    print(border);
    print("This is a script which allows you to see who is not following back on instagram...");   
    print(border);
    print()
    print("The script shows you the process in realtime")
    print()
    print("SYNTAX:-");
    print("python Application_Name.py Username Password");
    print()
    print(border)
    print("EXAMPLE:-");

    print("python InstaBot.py abc xyz");
    print("InstaBot.py - ApplicationName")
    print("abc         - Username");
    print("xyz         - Password")
    print(border);
            
def main():
    print()
    print("Application Name =",sys.argv[0])
    print()
    print("Designed and developed by Kaustubh Khairnar");
    try:
        start = time();
        my_bot = InstaBot(sys.argv[1], sys.argv[2])
        my_bot.get_unfollowers()
        end = time();
        print()
        print("Thank you for using script");
        print()
        print("Total time required for executing the script",end-start);
        print()
        print("Total time required for executing the script depends on the number of Followers and the speed of the internet connection");
    except Exception as E:
        print()
        print("ERROR",E);
        print()
        displayhelp();
        exit();

if __name__ == "__main__":
    main();