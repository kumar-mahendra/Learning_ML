# -------------------------------------------------------------------------------------------------------

# Web scrapping the news headlines 

# SOURCE ---- [firstpost.com] -Firstpost is an Indian news and media website.

################################################################################################################

# IMPORT REQUIRED LIBRARIES 
import re
import requests
from bs4 import BeautifulSoup 

def scrap_data(no_of_headlines): 

        headings = ['health','india','entertainment','sports','world','tech']

        for news_type in headings : 
            # print("Hello")
            Count,N_PAGES,headlines_count= 0,500,0
            url =  "https://www.firstpost.com/category/"+news_type
        
            # f  = open(news_type+".txt","w+")   

            with open(news_type+".txt","wb+") as f:
                f.truncate()            # clear file
                print(news_type, "Data collection Started .....")
                # first make url as they are present on website for each tag 
                if (news_type == "tech"):                                       
                    url ="https://www.firstpost.com/"+news_type+"/news-analysis"

                for page_no in range(1,N_PAGES):
                    # print("Entered Again",page_no)
                    URL =url+"/page/"+str(page_no)      
                    html_content = requests.get(URL).text 
                    parser = 'html5lib'
                    parse_tree = BeautifulSoup(html_content,parser)

                    if (news_type=="tech"):
                        content = parse_tree.find_all(name=['p'],attrs={'class':'headline'})
                    else : 
                        content = parse_tree.find_all('h3',attrs={'class':'main-title'})  #Attributes are set after inspecting the webpage   
                   
                    # endline = '\n'.encode('utf8')
                    for t in content : 
                       
                        headline = t.text.strip()
                        f.write(headline.encode('ascii','ignore'))
                        f.write('\n'.encode('ascii','ignore'))
                        # print(headline)
                        headlines_count+=1
                        if (headlines_count==no_of_headlines):
                            print(news_type+"Headlines collection finished.-------------")
                            print(headlines_count, "headlines collected.\n")
                            f.close()
                            break 
                    else : 
                        continue 
                    break
                f.close()
                print(news_type+" Headlines collection finished.-------------")
                print(headlines_count, "headlines collected.\n")

scrap_data(10000)



